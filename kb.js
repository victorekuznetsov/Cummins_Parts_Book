/* База знаний Cummins внутри каталога запасных частей.
   Документы QuickServe, руководства, темы, машины и детали — со сквозными
   перекрёстными ссылками. Данные лежат в data/kb_*.js, тела документов
   подгружаются кусками по мере надобности, поэтому работает и без сервера. */
(function () {
"use strict";

var DOCS   = window.KB_DOCS || {};
var MAN    = window.KB_MANUALS || {};
var PARTS  = window.KB_PARTS || {};
var TOPICS = window.KB_TOPICS || [];
var FLEET  = window.KB_FLEET || { m: [], g: [] };
var SEARCH = window.KB_SEARCH || [];
var NAMES  = window.KB_NAMES || {};
var PHOTOS = {};
(window.KB_PHOTOS || []).forEach(function (n) { PHOTOS[n] = 1; });
window.KB_BODY = window.KB_BODY || {};
window.KB_BODY_RU = window.KB_BODY_RU || {};
window.KB_FLEET = window.KB_FLEET || { m: [], g: [] };

var LANG = "ru";
try { LANG = localStorage.getItem("cummins_lang") || "ru"; } catch (e) {}
function setLang(v) {
  LANG = v === "en" ? "en" : "ru";
  try { localStorage.setItem("cummins_lang", LANG); } catch (e) {}
  var box = document.getElementById("lang-switch");
  if (box) {
    Array.prototype.forEach.call(box.querySelectorAll("button"), function (b) {
      b.classList.toggle("on", b.getAttribute("data-lang") === LANG);
    });
  }
  document.body.classList.toggle("lang-en", LANG === "en");
}

var CAT_RU = {
  procedures: "Процедура", tsb: "TSB", bulletin: "Сервисный бюллетень",
  sti: "Инструкция по инструменту", install_inst: "Инструкция по установке",
  outlines: "Габаритный чертёж", manual: "Руководство"
};
var CAT_MANY = {
  procedures: "Процедуры ремонта и обслуживания", tsb: "Технические бюллетени TSB",
  bulletin: "Сервисные бюллетени", sti: "Инструкции по сервисному инструменту",
  install_inst: "Инструкции по установке", outlines: "Габаритные чертежи",
  manual: "Руководства"
};
var PDF_BASE = "bulletins/";
var ENGINE_TITLE = {};
(window.ENGINES || []).forEach(function (e) {
  ENGINE_TITLE[e.esn] = (e.model || "") + (e.cpl ? " CPL " + e.cpl : "");
});

var root = document.getElementById("kb-root");
var lastQuery = "";

/* ------------------------------------------------------------- утилиты */
function esc(s) {
  return String(s == null ? "" : s).replace(/[&<>"]/g, function (c) {
    return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c];
  });
}
function docLink(id, label) {
  var d = DOCS[id];
  if (!d && DOCS[id + "-history"]) {
    var mm = MAN[id] || {};
    return '<a class="lnk doc" href="#/manual/' + esc(id) + '">' +
           esc(label || mm.ru || mm.t || id) + "</a>";
  }
  if (!d) return esc(label || id);
  var href = d.c === "manual" ? "#/manual/" + id.replace("-history", "") : "#/doc/" + id;
  return '<a class="lnk doc" href="' + href + '">' + esc(label || d.t || id) + "</a>";
}
function partLink(no) {
  if (PARTS[no]) return '<a class="lnk part" href="#/part/' + esc(no) + '">' + esc(no) + "</a>";
  return esc(no);
}
function engineLink(esn) {
  return '<a class="lnk eng" href="#/engine/' + esn + '">' + esn +
         (ENGINE_TITLE[esn] ? " · " + esc(ENGINE_TITLE[esn]) : "") + "</a>";
}
function docTitle(d, id) {
  var main = LANG === "en" ? (d.t || id) : (d.ru || d.t || id);
  var sub = LANG === "en" ? (d.ru || "") : (d.ru ? d.t : "");
  return esc(main) + (sub ? ' <span class="sub">— ' + esc(sub) + "</span>" : "");
}
function sortIds(ids) {
  return (ids || []).slice().sort(function (a, b) {
    var A = DOCS[a] || {}, B = DOCS[b] || {};
    return (A.c || "").localeCompare(B.c || "") || String(a).localeCompare(String(b));
  });
}
function badge(cat) {
  return '<span class="tag t-' + cat + '">' + esc(CAT_RU[cat] || cat) + "</span>";
}
function photoUrl(file) {
  var base = String(file).replace(/\.[a-z]+$/i, "");
  return PHOTOS[base] ? "assets/photos/" + base + ".jpg" : photoCdn(file);
}
function photoCdn(file) {
  var num = String(file).split("_")[0];
  return "https://parts.cummins.com/graphics/parts/" + num.slice(0, 3) + "/" + num + "/" +
         String(file).replace(/\.jpg$/i, ".png");
}

/* --------------------------------------------------- подгрузка кусков */
var pending = {};
function loadScript(src, cb) {
  if (pending[src]) { pending[src].push(cb); return; }
  pending[src] = [cb];
  var s = document.createElement("script");
  s.src = src;
  s.onload = s.onerror = function () {
    var list = pending[src]; pending[src] = null;
    list.forEach(function (f) { f(); });
  };
  document.head.appendChild(s);
}
function withBody(id, cb) {
  var d = DOCS[id];
  if (!d || d.ch < 0) { cb("", "en"); return; }
  var ru = LANG === "ru" && d.ru_body;
  var store = ru ? window.KB_BODY_RU : window.KB_BODY;
  var file = ru ? "data/kb/body_ru_" + d.ch + ".js" : "data/kb/body_" + d.ch + ".js";
  if (store[d.ch]) { cb(store[d.ch][id] || "", ru ? "ru" : "en"); return; }
  loadScript(file, function () {
    var s2 = ru ? window.KB_BODY_RU : window.KB_BODY;
    cb((s2[d.ch] || {})[id] || "", ru ? "ru" : "en");
  });
}

/* -------------------------------------------------------------- режим */
function active() { return document.body.classList.contains("kb-mode"); }
function setMode(on) {
  document.body.classList.toggle("kb-mode", !!on);
  var nav = document.getElementById("kb-nav");
  if (nav) {
    Array.prototype.forEach.call(nav.querySelectorAll("a"), function (a) {
      a.classList.toggle("on", on && a.getAttribute("href") === location.hash);
    });
    var cat = document.getElementById("nav-catalog");
    if (cat) cat.classList.toggle("on", !on);
  }
  if (on) window.scrollTo(0, 0);
}
function render(html) {
  root.innerHTML = html;
  setMode(true);
  root.scrollTop = 0;
}

/* ---------------------------------------------------------- заголовок */
function crumbs(items) {
  return '<nav class="crumbs">' + items.map(function (it) {
    return it.href ? '<a href="' + it.href + '">' + esc(it.t) + "</a>"
                   : "<span>" + esc(it.t) + "</span>";
  }).join('<i>›</i>') + "</nav>";
}

/* ============================================================ главная */
function viewHome() {
  var byCat = {};
  Object.keys(DOCS).forEach(function (id) {
    var c = DOCS[id].c; byCat[c] = (byCat[c] || 0) + 1;
  });
  var tsbRecent = Object.keys(DOCS).filter(function (id) { return DOCS[id].c === "tsb" && DOCS[id].d; })
    .sort(function (a, b) { return DOCS[b].d.localeCompare(DOCS[a].d); }).slice(0, 12);

  var h = [];
  h.push('<div class="kb-hero">');
  h.push("<h1>База знаний Cummins</h1>");
  h.push('<p class="lead">Документация QuickServe и каталоги запчастей двигателей — ' +
         "в одном месте и со сквозными ссылками: из процедуры в деталь, " +
         "из детали в узел и обратно в документы, где она упоминается.</p>");
  h.push('<div class="kb-counters">');
  [["Документов", Object.keys(DOCS).length, "#/docs/all"],
   ["Руководств", Object.keys(MAN).length, "#/docs/manual"],
   ["Деталей Cummins", Object.keys(PARTS).length, "#/parts"],
   ["Двигателей", (window.ENGINES || []).length, "#/engines"]
  ].forEach(function (c) {
    h.push('<a class="counter" href="' + c[2] + '"><b>' + c[1] + "</b><span>" + c[0] + "</span></a>");
  });
  h.push("</div></div>");

  h.push('<div class="kb-cols">');
  h.push('<section class="kb-card"><h2>Документы</h2><ul class="kb-list">');
  ["manual", "procedures", "tsb", "bulletin", "sti", "install_inst", "outlines"].forEach(function (c) {
    if (!byCat[c]) return;
    h.push('<li><a href="#/docs/' + c + '">' + esc(CAT_MANY[c] || c) +
           '</a> <span class="cnt">' + byCat[c] + "</span></li>");
  });
  h.push("</ul></section>");

  h.push('<section class="kb-card"><h2>Темы</h2><ul class="kb-list">');
  TOPICS.forEach(function (t, i) {
    h.push('<li><a href="#/topic/' + i + '">' + esc(t.t) + '</a> <span class="cnt">' +
           t.ids.length + '</span><div class="sub">' + esc(t.d) + "</div></li>");
  });
  h.push("</ul></section>");

  h.push('<section class="kb-card"><h2>Двигатели</h2><ul class="kb-list">');
  (window.ENGINES || []).forEach(function (e) {
    var docs = Object.keys(DOCS).filter(function (id) {
      return (DOCS[id].e || []).indexOf(e.esn) !== -1;
    }).length;
    h.push('<li><a href="#/engine/' + e.esn + '">' + e.esn + " · " + esc(e.model) +
           '</a> <span class="cnt">' + docs + "</span></li>");
  });
  h.push("</ul></section>");
  h.push("</div>");

  h.push('<section class="kb-card wide"><h2>Свежие бюллетени TSB</h2><table class="kb-table">');
  tsbRecent.forEach(function (id) {
    var d = DOCS[id];
    h.push("<tr><td class='c-id'>" + docLink(id, id) + "</td><td>" + docTitle(d, id) +
           "</td><td class='c-date'>" + esc(d.d) + "</td></tr>");
  });
  h.push("</table></section>");
  render(h.join(""));
}

/* ====================================================== список документов */
function viewDocs(cat, q) {
  var ids = Object.keys(DOCS).filter(function (id) {
    return cat === "all" ? true : DOCS[id].c === cat;
  });
  if (cat === "manual") {
    ids = Object.keys(MAN).map(function (m) { return m + "-history"; })
      .filter(function (id) { return DOCS[id]; });
  }
  ids.sort(function (a, b) {
    var A = DOCS[a], B = DOCS[b];
    if (cat === "tsb" || cat === "all") return (B.d || "").localeCompare(A.d || "") ||
      String(a).localeCompare(String(b));
    return String(a).localeCompare(String(b));
  });

  var h = [];
  h.push(crumbs([{ t: "База знаний", href: "#/kb" },
                 { t: cat === "all" ? "Все документы" : (CAT_MANY[cat] || cat) }]));
  h.push('<div class="kb-head"><h1>' + esc(cat === "all" ? "Все документы" : (CAT_MANY[cat] || cat)) +
         ' <span class="cnt">' + ids.length + "</span></h1>");
  h.push('<input class="kb-filter" id="kb-filter" placeholder="Фильтр по номеру или названию…" ' +
         'value="' + esc(q || "") + '"></div>');
  h.push('<div id="kb-doc-list">' + docRows(ids, q) + "</div>");
  render(h.join(""));

  var f = document.getElementById("kb-filter");
  if (f) {
    f.oninput = function () {
      document.getElementById("kb-doc-list").innerHTML = docRows(ids, this.value);
    };
    if (q) f.focus();
  }
}
function docRows(ids, q) {
  q = (q || "").trim().toLowerCase();
  var rows = [], n = 0;
  for (var i = 0; i < ids.length && n < 800; i++) {
    var id = ids[i], d = DOCS[id];
    if (q && (id + " " + d.t + " " + d.ru).toLowerCase().indexOf(q) === -1) continue;
    n++;
    rows.push("<tr><td class='c-id'>" + docLink(id, id) + "</td>" +
      "<td>" + docTitle(d, id) +
      (d.g ? '<div class="sub">' + esc(d.g) + "</div>" : "") + "</td>" +
      "<td class='c-eng'>" + (d.e || []).map(function (e) {
        return '<a class="chip" href="#/engine/' + e + '">' + e + "</a>";
      }).join(" ") + "</td>" +
      "<td class='c-date'>" + esc(d.d || d.mo || "") + "</td>" +
      (d.ok ? "" : '<td class="c-ext" title="В выгрузке нет — только на QuickServe">↗</td>') +
      "</tr>");
  }
  if (!rows.length) return '<p class="empty">Ничего не найдено.</p>';
  return '<table class="kb-table">' + rows.join("") + "</table>" +
    (n >= 800 ? '<p class="sub">Показаны первые 800 — уточните фильтр.</p>' : "");
}

/* ============================================================= документ */
function viewDoc(id) {
  var d = DOCS[id];
  if (!d) { notFound("Документ " + id); return; }
  if (d.c === "manual") { viewManual(id.replace("-history", "")); return; }

  var h = [];
  h.push(crumbs([{ t: "База знаний", href: "#/kb" },
                 { t: CAT_MANY[d.c] || d.c, href: "#/docs/" + d.c },
                 { t: id }]));
  h.push('<article class="kb-doc">');
  h.push('<header class="doc-head">');
  var mainTitle = LANG === "en" ? d.t : (d.ru || d.t);
  var subTitle = LANG === "en" ? (d.ru || "") : (d.ru ? d.t : "");
  h.push("<h1>" + esc(mainTitle) + "</h1>");
  if (subTitle) h.push('<div class="doc-en">' + esc(subTitle) + "</div>");
  h.push('<div class="doc-meta">' + badge(d.c) + '<span class="num">' + esc(id) + "</span>" +
    (d.d ? '<span class="mi">выпущен ' + esc(d.d) + "</span>" : "") +
    (d.mo ? '<span class="mi">изменён ' + esc(d.mo) + "</span>" : "") +
    (d.g ? '<span class="mi">' + esc(d.g) + "</span>" : "") + "</div>");
  h.push('<div class="doc-links">' +
    '<a class="btn-mini" href="' + esc(d.u) + '" target="_blank" rel="noopener">Оригинал в QuickServe ↗</a>' +
    (d.pdf ? ' <a class="btn-mini" href="' + PDF_BASE + esc(d.pdf.replace(/\\/g, "/")) +
             '" target="_blank" rel="noopener">PDF ↗</a>' : "") +
    ' <a class="btn-mini" href="#" onclick="window.print();return false;">Печать</a>' +
    "</div>");
  h.push("</header>");

  if (!d.ok) {
    h.push('<div class="callout missing"><div class="callout-head">' +
      '<span class="callout-ico">—</span>Документа нет в выгрузке</div><div class="callout-body">' +
      "<p>В песочнице этот документ отсутствует — доступна карточка и ссылка на оригинал " +
      "в QuickServe.</p></div></div>");
  }
  h.push('<div class="doc-body" id="doc-body"><p class="sub">Загрузка…</p></div>');
  h.push("</article>");
  h.push('<aside class="doc-side" id="doc-side">' + docSide(id, d) + "</aside>");
  render('<div class="doc-layout">' + h.join("") + "</div>");

  withBody(id, function (body, lang) {
    var box = document.getElementById("doc-body");
    if (!box) return;
    var head = "";
    if (lang === "ru") {
      head = '<div class="mt-note">Черновой перевод: выполнен автоматически, ' +
        'терминология выверена по словарю Cummins. Спорные места сверяйте с ' +
        'оригиналом — <a href="#" data-lang-set="en">показать английский текст</a>' +
        ' или <a href="' + esc(d.u) + '" target="_blank" rel="noopener">открыть в QuickServe ↗</a>.</div>';
    } else if (d.ru_body) {
      head = '<div class="mt-note">Оригинал Cummins. ' +
        '<a href="#" data-lang-set="ru">показать перевод на русский</a>.</div>';
    }
    box.innerHTML = head + (body || '<p class="sub">Текст документа не выгружен.</p>');
  });
}

function docSide(id, d) {
  var h = [];
  if (d.e && d.e.length) {
    h.push('<section><h3>Двигатели</h3><ul class="side-list">');
    d.e.forEach(function (e) { h.push("<li>" + engineLink(e) + "</li>"); });
    h.push("</ul></section>");
  }
  if (d.f && d.f.length) {
    h.push('<section><h3>Семейство</h3><p class="side-p">' + esc(d.f.join(", ")) + "</p></section>");
  }
  if (d.mn && d.mn.length) {
    h.push('<section><h3>Входит в руководства</h3><ul class="side-list">');
    d.mn.forEach(function (m) {
      var mm = MAN[m] || {};
      h.push('<li><a class="lnk doc" href="#/manual/' + m + '">' +
             esc(mm.ru || mm.t || m) + "</a></li>");
    });
    h.push("</ul></section>");
  }
  if (d.sec && d.sec.length) {
    h.push('<section><h3>Секции руководств</h3><ul class="side-list plain">');
    d.sec.forEach(function (s) { h.push("<li>" + esc(s) + "</li>"); });
    h.push("</ul></section>");
  }
  if (d.p && d.p.length) {
    h.push('<section><h3>Детали в тексте <span class="cnt">' + d.p.length + "</span></h3>");
    h.push('<ul class="side-list">');
    d.p.slice(0, 60).forEach(function (p) {
      var pp = PARTS[p] || {};
      h.push("<li>" + partLink(p) + (pp.ru || pp.n ? ' <span class="sub">' +
             esc(pp.ru || pp.n) + "</span>" : "") + "</li>");
    });
    h.push("</ul></section>");
  }
  if (d.bl && d.bl.length) {
    h.push('<section><h3>Ссылаются сюда <span class="cnt">' + d.bl.length + "</span></h3>");
    h.push('<ul class="side-list">');
    d.bl.slice(0, 60).forEach(function (b) {
      var bd = DOCS[b];
      h.push("<li>" + docLink(b, (bd && (bd.ru || bd.t)) || b) + "</li>");
    });
    h.push("</ul></section>");
  }
  var group = String(id).split("-")[0];
  var siblings = Object.keys(DOCS).filter(function (x) {
    return x !== id && DOCS[x].c === d.c && String(x).split("-")[0] === group;
  }).slice(0, 25);
  if (siblings.length) {
    h.push('<section><h3>Рядом в группе ' + esc(group) + "</h3><ul class=\"side-list\">");
    siblings.forEach(function (s) { h.push("<li>" + docLink(s, (DOCS[s].ru || DOCS[s].t)) + "</li>"); });
    h.push("</ul></section>");
  }
  return h.join("");
}

/* =========================================================== руководство */
function viewManual(mid) {
  var m = MAN[mid];
  if (!m) { notFound("Руководство " + mid); return; }
  var h = [];
  h.push(crumbs([{ t: "База знаний", href: "#/kb" },
                 { t: "Руководства", href: "#/docs/manual" }, { t: mid }]));
  h.push('<article class="kb-doc">');
  h.push('<header class="doc-head"><h1>' + esc(m.ru || m.t) + "</h1>");
  if (m.ru) h.push('<div class="doc-en">' + esc(m.t) + "</div>");
  h.push('<div class="doc-meta">' + badge("manual") + '<span class="num">' + esc(mid) + "</span>" +
    '<span class="mi">процедур: ' + m.n + "</span></div>");
  h.push('<div class="doc-links"><a class="btn-mini" href="' + esc(m.u) +
    '" target="_blank" rel="noopener">История изменений в QuickServe ↗</a></div></header>');

  h.push('<div class="doc-body">');
  m.s.forEach(function (pair) {
    var section = pair[0], items = pair[1];
    h.push("<h3>" + esc(section) + ' <span class="cnt">' + items.length + "</span></h3>");
    h.push('<div class="tw"><table class="doc-table"><thead><tr><th>Номер</th>' +
           "<th>Процедура</th><th>Изменена</th></tr></thead><tbody>");
    items.forEach(function (it) {
      var id = it[0], known = DOCS[id];
      h.push("<tr><td>" + (known ? docLink(id, id) : esc(id)) + "</td><td>" +
        (known && known.ru ? esc(known.ru) + ' <span class="sub">' + esc(it[1]) + "</span>"
                           : esc(it[1])) +
        (known ? "" : ' <span class="sub">— вне выгрузки</span>') +
        "</td><td>" + esc(it[2] || "") + "</td></tr>");
    });
    h.push("</tbody></table></div>");
  });
  h.push("</div></article>");

  var side = [];
  if (m.e && m.e.length) {
    side.push('<section><h3>Двигатели</h3><ul class="side-list">');
    m.e.forEach(function (e) { side.push("<li>" + engineLink(e) + "</li>"); });
    side.push("</ul></section>");
  }
  side.push('<section><h3>Другие руководства</h3><ul class="side-list">');
  Object.keys(MAN).sort(function (a, b) {
    return (MAN[a].ru || MAN[a].t).localeCompare(MAN[b].ru || MAN[b].t);
  }).forEach(function (x) {
    if (x === mid) return;
    side.push('<li><a class="lnk doc" href="#/manual/' + x + '">' +
      esc(MAN[x].ru || MAN[x].t) + "</a></li>");
  });
  side.push("</ul></section>");
  render('<div class="doc-layout">' + h.join("") +
         '<aside class="doc-side">' + side.join("") + "</aside></div>");
}

/* ================================================================ тема */
function viewTopic(i) {
  var t = TOPICS[i];
  if (!t) { notFound("Тема"); return; }
  var groups = {};
  t.ids.forEach(function (id) {
    var c = (DOCS[id] || {}).c || "прочее";
    (groups[c] = groups[c] || []).push(id);
  });
  var h = [];
  h.push(crumbs([{ t: "База знаний", href: "#/kb" }, { t: t.t }]));
  h.push('<div class="kb-head"><h1>' + esc(t.t) + ' <span class="cnt">' + t.ids.length +
         "</span></h1><p class=\"lead\">" + esc(t.d) + "</p></div>");
  ["manual", "tsb", "procedures", "bulletin", "sti", "install_inst", "outlines"].forEach(function (c) {
    if (!groups[c]) return;
    h.push('<section class="kb-card wide"><h2>' + esc(CAT_MANY[c] || c) +
           ' <span class="cnt">' + groups[c].length + "</span></h2>");
    h.push(docRows(groups[c].sort(), ""));
    h.push("</section>");
  });
  render(h.join(""));
}

/* ============================================================== деталь */
function viewPart(no) {
  var p = PARTS[no];
  if (!p) { notFound("Деталь " + no); return; }
  var cat = window.CATALOGS || {};
  /* каталоги двигателей грузятся по требованию: если загружены не все,
     дозагружаем и перерисовываем вид с полными данными */
  if (window.CATALOG_API && window.CATALOG_API.allLoaded && !window.CATALOG_API.allLoaded()) {
    window.CATALOG_API.loadAll(function () { route(); });
  }
  var uses = [];       // где применяется: двигатель -> узел -> позиция
  var kits = [];
  Object.keys(cat).forEach(function (esn) {
    var c = cat[esn];
    (c.options || []).forEach(function (o) {
      (o.parts || []).forEach(function (pp) {
        if (pp.no === no) uses.push({ esn: esn, o: o, p: pp });
      });
    });
    (c.kits || []).forEach(function (k) {
      (k.parts || []).forEach(function (pp) {
        if (pp.no === no) kits.push({ esn: esn, k: k });
      });
    });
  });
  var card = null;
  Object.keys(cat).some(function (esn) {
    if (cat[esn].cards && cat[esn].cards[no]) { card = cat[esn].cards[no]; return true; }
    return false;
  });

  var h = [];
  h.push(crumbs([{ t: "База знаний", href: "#/kb" }, { t: "Детали", href: "#/parts" }, { t: no }]));
  h.push('<article class="kb-doc part-page">');
  h.push('<header class="doc-head"><h1>' + esc(no) + " — " + esc(p.ru || p.n) + "</h1>");
  if (p.ru && p.n) h.push('<div class="doc-en">' + esc(p.n) + "</div>");
  h.push('<div class="doc-links">' +
    '<a class="btn-mini" href="#" data-open-catalog="' + esc(no) + '">Открыть в каталоге</a>' +
    ' <a class="btn-mini" href="https://parts.cummins.com/parts-catalog/?partNumber=' + esc(no) +
    '" target="_blank" rel="noopener">parts.cummins.com ↗</a></div></header>');

  h.push('<div class="doc-body">');
  if (p.ph && p.ph.length) {
    h.push('<div class="part-photos">');
    p.ph.forEach(function (f) {
      h.push('<img loading="lazy" src="' + photoUrl(f) + '" alt="" ' +
             'onerror="this.style.display=\'none\'">');
    });
    h.push("</div>");
  }
  if (card) {
    h.push('<div class="tw"><table class="doc-table"><tbody>');
    if (card.wt) h.push("<tr><th>Масса, кг (по каталогу)</th><td>" + esc(card.wt) + "</td></tr>");
    if (card.dim) h.push("<tr><th>Габариты Д×Ш×В, мм</th><td>" + esc(card.dim) + "</td></tr>");
    var attrs = card.attrs || {};
    Object.keys(attrs).forEach(function (k) {
      h.push("<tr><th>" + esc(k) + "</th><td>" + esc(attrs[k]) + "</td></tr>");
    });
    h.push("</tbody></table></div>");
  }
  if (p.pr) {
    h.push("<h3>Цена · Горная Евразия</h3><div class=\"tw\"><table class=\"doc-table\">" +
           "<thead><tr><th>Прайс</th><th>Цена</th></tr></thead><tbody>");
    [["cur", "текущая"], ["new", "несогласованная"]].forEach(function (r) {
      if (p.pr[r[0]] == null) return;
      h.push("<tr><td>" + r[1] + "</td><td>" + esc(String(p.pr[r[0]])) + "</td></tr>");
    });
    h.push("</tbody></table></div>");
  }
  if (uses.length) {
    h.push("<h3>Где применяется</h3><div class=\"tw\"><table class=\"doc-table\"><thead><tr>" +
      "<th>Двигатель</th><th>Узел</th><th>Поз.</th><th>Кол-во</th><th>Типоразмер</th>" +
      "</tr></thead><tbody>");
    uses.forEach(function (u) {
      h.push("<tr><td>" + engineLink(u.esn) + "</td><td>" +
        '<a class="lnk" href="#" data-open-option="' + esc(u.esn) + "|" + esc(u.o.no) + "|" +
        esc(no) + '">' + esc(u.o.no) + " · " + esc(NAMES.opt && NAMES.opt[u.o.no] || u.o.name) +
        "</a></td><td>" + esc(u.p.pos || "") + "</td><td>" + esc(u.p.qty || "") +
        "</td><td>" + esc(u.p.dim || "") + "</td></tr>");
    });
    h.push("</tbody></table></div>");
  }
  if (kits.length) {
    h.push("<h3>Входит в комплекты</h3><ul>");
    kits.forEach(function (k) {
      h.push("<li>" + esc(k.k.no) + " — " + esc(NAMES.kit && NAMES.kit[k.k.no] || k.k.name) +
             " <span class=\"sub\">(" + esc(k.esn) + ")</span></li>");
    });
    h.push("</ul>");
  }
  if (p.sup) {
    h.push("<h3>Цепочка замен номера</h3><div class=\"tw\"><table class=\"doc-table\"><thead><tr>" +
      "<th>Номер</th><th>Статус</th><th>Продаётся</th></tr></thead><tbody>");
    p.sup.forEach(function (s) {
      h.push("<tr><td>" + (s[0] === no ? esc(s[0]) : partLink(s[0])) + "</td><td>" +
             esc(s[1]) + "</td><td>" + (s[2] ? "да" : "нет") + "</td></tr>");
    });
    h.push("</tbody></table></div>");
  }
  h.push("</div></article>");

  var side = [];
  if (p.e && p.e.length) {
    side.push('<section><h3>Двигатели</h3><ul class="side-list">');
    p.e.forEach(function (e) { side.push("<li>" + engineLink(e) + "</li>"); });
    side.push("</ul></section>");
  }
  if (p.d && p.d.length) {
    side.push('<section><h3>Упоминается в документах <span class="cnt">' + p.d.length +
              "</span></h3><ul class=\"side-list\">");
    sortIds(p.d).slice(0, 80).forEach(function (k) {
      var id = k.split("|")[1] || k;
      var dd = DOCS[id];
      side.push("<li>" + (dd ? badge(dd.c) + " " + docLink(id, dd.ru || dd.t) : esc(id)) + "</li>");
    });
    side.push("</ul></section>");
  }
  render('<div class="doc-layout">' + h.join("") +
         '<aside class="doc-side">' + side.join("") + "</aside></div>");
}

/* ============================================================ двигатель */
function viewEngine(esn) {
  var cat = (window.CATALOGS || {})[esn];
  if (!cat && window.CATALOG_API && window.CATALOG_API.loadAll) {
    window.CATALOG_API.loadAll(function () { route(); });
  }
  var ids = Object.keys(DOCS).filter(function (id) {
    return (DOCS[id].e || []).indexOf(esn) !== -1;
  });
  var byCat = {};
  ids.forEach(function (id) { (byCat[DOCS[id].c] = byCat[DOCS[id].c] || []).push(id); });

  var h = [crumbs([{ t: "База знаний", href: "#/kb" }, { t: "Двигатель " + esn }])];
  h.push('<div class="kb-head"><h1>' + esc(esn) + (cat ? " — " + esc(cat.model) : "") + "</h1>");
  if (cat) {
    h.push('<p class="lead">CPL ' + esc(cat.cpl) + " · конфигурация " + esc(cat.config || "—") +
      " · сборка " + esc(cat.buildDate || "—") + " · узлов " + (cat.options || []).length +
      " · комплектов " + (cat.kits || []).length + "</p>");
  }
  h.push('<div class="doc-links"><a class="btn-mini" href="#" data-open-engine="' + esc(esn) +
    '">Открыть каталог этого двигателя</a></div></div>');

  if (byCat.manual) {
    h.push('<section class="kb-card wide"><h2>Руководства</h2><ul class="kb-list">');
    byCat.manual.forEach(function (id) {
      var mid = id.replace("-history", ""), mm = MAN[mid] || {};
      h.push('<li><a href="#/manual/' + mid + '">' + esc(mm.ru || mm.t || mid) +
        '</a> <span class="cnt">' + (mm.n || 0) + "</span></li>");
    });
    h.push("</ul></section>");
  }
  var hasDocs = ["procedures", "tsb", "bulletin", "sti", "install_inst", "outlines"]
    .some(function (c) { return byCat[c]; });
  if (hasDocs) {
    h.push('<section class="kb-card wide"><h2>Документация двигателя</h2><ul class="kb-list cols">');
    ["procedures", "tsb", "bulletin", "sti", "install_inst", "outlines"].forEach(function (c) {
      if (!byCat[c]) return;
      h.push('<li><a href="#/docs/' + c + '">' + esc(CAT_MANY[c]) + '</a> <span class="cnt">' +
             byCat[c].length + "</span></li>");
    });
    h.push("</ul></section>");
  } else {
    h.push('<section class="kb-card wide"><h2>Документация двигателя</h2>' +
      '<p class="lead">Для этого двигателя документы в песочницу не выгружались: ' +
      'в QuickServe документация привязана к другим серийным номерам того же семейства. ' +
      'Каталог запчастей доступен полностью, а документы смотрите на ' +
      '<a class="lnk" href="https://quickserve.cummins.com/qs3/pubsys2/xml/en/index.html" ' +
      'target="_blank" rel="noopener">QuickServe ↗</a> по номеру ' + esc(esn) +
      ".</p></section>");
  }

  if (cat) {
    h.push('<section class="kb-card wide"><h2>Системы и узлы</h2>');
    (cat.systems || []).forEach(function (s) {
      h.push("<h3>" + esc(s.name || s.code) + "</h3><ul class=\"kb-list cols\">");
      (s.options || []).forEach(function (on) {
        var o = null;
        (cat.options || []).some(function (x) { if (x.no === on) { o = x; return true; } return false; });
        var nm = (NAMES.opt && NAMES.opt[on]) || (o && o.name) || "";
        h.push('<li><a class="lnk" href="#" data-open-option="' + esc(esn) + "|" + esc(on) +
               '|">' + esc(on) + " — " + esc(nm) + "</a></li>");
      });
      h.push("</ul>");
    });
    h.push("</section>");
  }
  render(h.join(""));
}

/* =============================================================== поиск */
function viewSearch(q) {
  q = (q || "").trim();
  var h = [crumbs([{ t: "База знаний", href: "#/kb" }, { t: "Поиск" }])];
  h.push('<div class="kb-head"><h1>Поиск</h1>' +
    '<input class="kb-filter" id="kb-q" placeholder="Номер детали, название, номер документа…" value="' +
    esc(q) + '"></div><div id="kb-res"></div>');
  render(h.join(""));
  var inp = document.getElementById("kb-q");
  inp.focus();
  inp.oninput = function () {
    var v = this.value;
    clearTimeout(inp._t);
    inp._t = setTimeout(function () {
      location.replace("#/search/" + encodeURIComponent(v));
      document.getElementById("kb-res").innerHTML = searchHtml(v);
    }, 180);
  };
  document.getElementById("kb-res").innerHTML = searchHtml(q);
}

function searchHtml(q) {
  q = (q || "").trim();
  if (q.length < 2) return '<p class="sub">Введите минимум два символа.</p>';
  var lo = q.toLowerCase();
  var num = q.toUpperCase().replace(/[\s-]/g, "");
  var h = [];

  /* машины парка: по VIN, серийному номеру двигателя, модели и CPL */
  var fl = FLEET.m.filter(function (m) {
    return (m.vin || "").toUpperCase().indexOf(num) >= 0 ||
           (m.esn || "").toUpperCase().indexOf(num) >= 0 ||
           (m.machine || "").toLowerCase().indexOf(lo) >= 0 ||
           (m.cpl && m.cpl === q.trim());
  }).slice(0, 20);
  if (fl.length) {
    h.push('<section class="kb-card"><h2>Парк машин <span class="cnt">' +
      fl.length + "</span></h2>" +
      '<div class="tw"><table class="kb-table"><thead><tr><th>Машина</th><th>VIN</th>' +
      "<th>ESN</th><th>CPL</th><th>Двигатель</th><th>Каталог</th></tr></thead><tbody>");
    fl.forEach(function (m) { h.push(fleetRow(m)); });
    h.push("</tbody></table></div></section>");
  }

  var pHits = [];
  Object.keys(PARTS).forEach(function (no) {
    if (pHits.length > 200) return;
    var p = PARTS[no];
    if (no.toUpperCase().indexOf(num) !== -1 ||
        (p.ru && p.ru.toLowerCase().indexOf(lo) !== -1) ||
        (p.n && p.n.toLowerCase().indexOf(lo) !== -1)) pHits.push(no);
  });
  var dHits = SEARCH.filter(function (r) {
    return r[0].toLowerCase().indexOf(lo) !== -1 ||
           (r[1] && r[1].toLowerCase().indexOf(lo) !== -1) ||
           (r[2] && r[2].toLowerCase().indexOf(lo) !== -1);
  }).slice(0, 300);

  h.push('<div class="res-tabs"><span>Найдено: детали Cummins ' + pHits.length +
    " · детали машин " + mHits.length + " · документы " + dHits.length + "</span></div>");

  if (pHits.length) {
    h.push('<section class="kb-card wide"><h2>Детали Cummins</h2><table class="kb-table">');
    pHits.slice(0, 60).forEach(function (no) {
      var p = PARTS[no];
      h.push("<tr><td class='c-id'>" + partLink(no) + "</td><td>" + esc(p.ru || "") +
        (p.n ? ' <span class="sub">' + esc(p.n) + "</span>" : "") + "</td><td class='c-eng'>" +
        (p.e || []).map(function (e) { return '<span class="chip">' + e + "</span>"; }).join(" ") +
        "</td></tr>");
    });
    h.push("</table>" + (pHits.length > 60 ? '<p class="sub">…ещё ' + (pHits.length - 60) +
      "</p>" : "") + "</section>");
  }
  if (dHits.length) {
    h.push('<section class="kb-card wide"><h2>Документы</h2><table class="kb-table">');
    dHits.slice(0, 120).forEach(function (r) {
      var d = DOCS[r[0]] || {};
      h.push("<tr><td class='c-id'>" + docLink(r[0], r[0]) + "</td><td>" + badge(r[3]) + " " +
        esc(r[2] || "") + (r[1] ? ' <span class="sub">' + esc(r[1]) + "</span>" : "") +
        "</td><td class='c-date'>" + esc(d.d || "") + "</td></tr>");
    });
    h.push("</table></section>");
  }
  if (!pHits.length && !dHits.length) {
    h.push('<p class="empty">Ничего не найдено.</p>');
  }
  return h.join("");
}

/* ------------------------------------------------- списки деталей целиком */
function viewParts(kind, q) {
  var src = PARTS;
  var ids = Object.keys(src).sort();
  var h = [crumbs([{ t: "База знаний", href: "#/kb" }, { t: "Детали Cummins" }])];
  h.push('<div class="kb-head"><h1>' + "Детали Cummins" +
    ' <span class="cnt">' + ids.length + '</span></h1>' +
    '<input class="kb-filter" id="kb-filter" placeholder="Артикул или наименование…" value="' +
    esc(q || "") + '"></div><div id="kb-plist"></div>');
  render(h.join(""));

  function rows(f) {
    f = (f || "").trim().toLowerCase();
    var out = [], n = 0;
    for (var i = 0; i < ids.length && n < 600; i++) {
      var no = ids[i], p = src[no];
      var hay = (no + " " + (p.ru || "") + " " + (p.n || p.en || "")).toLowerCase();
      if (f && hay.indexOf(f) === -1) continue;
      n++;
      out.push("<tr><td class='c-id'>" + partLink(no) + "</td><td>" + esc(p.ru || "") +
        '<span class="sub"> ' + esc(p.n || p.en || "") + "</span></td><td class='c-eng'>" +
        (p.e || []).map(function (e) { return '<span class="chip">' + e + "</span>"; }).join(" ") +
        "</td></tr>");
    }
    if (!out.length) return '<p class="empty">Ничего не найдено.</p>';
    return '<table class="kb-table">' + out.join("") + "</table>" +
      (n >= 600 ? '<p class="sub">Показаны первые 600 — уточните фильтр.</p>' : "");
  }
  document.getElementById("kb-plist").innerHTML = rows(q);
  var f = document.getElementById("kb-filter");
  f.oninput = function () { document.getElementById("kb-plist").innerHTML = rows(this.value); };
}

function viewEngines() {
  var h = [crumbs([{ t: "База знаний", href: "#/kb" }, { t: "Двигатели" }])];
  h.push('<div class="kb-head"><h1>Двигатели</h1></div><table class="kb-table">');
  (window.ENGINES || []).forEach(function (e) {
    var n = Object.keys(DOCS).filter(function (id) {
      return (DOCS[id].e || []).indexOf(e.esn) !== -1; }).length;
    h.push('<tr><td class="c-id"><a class="lnk eng" href="#/engine/' + e.esn + '">' + e.esn +
      "</a></td><td>" + esc(e.model) + ' <span class="sub">CPL ' + esc(e.cpl) +
      "</span></td><td class='c-date'>документов: " + n + "</td></tr>");
  });
  h.push("</table>");
  render(h.join(""));
}

function notFound(what) {
  render('<div class="kb-head"><h1>Не найдено</h1><p class="lead">' + esc(what) +
    ' отсутствует в базе. Попробуйте <a href="#/search/">поиск</a>.</p></div>');
}

/* ============================================================ маршруты */
function route() {
  var hash = location.hash || "";
  if (!hash || hash === "#" || hash.indexOf("#/catalog") === 0) { setMode(false); return; }
  var parts = hash.replace(/^#\//, "").split("/").map(decodeURIComponent);
  var head = parts[0];

  if (head === "kb") return viewHome();
  if (head === "docs") return viewDocs(parts[1] || "all", parts[2]);
  if (head === "doc") return viewDoc(parts.slice(1).join("/"));
  if (head === "manual") return viewManual(parts[1]);
  if (head === "topic") return viewTopic(parseInt(parts[1], 10) || 0);
  if (head === "part") return viewPart(parts[1]);
  if (head === "parts") return viewParts("parts", parts[1]);
  if (head === "engine") return viewEngine(parts[1]);
  if (head === "engines") return viewEngines();
  if (head === "fleet") return viewFleet();
  if (head === "cpl") return viewCpl(parts[1]);
  if (head === "search") return viewSearch(parts.slice(1).join("/"));
  setMode(false);
}

/* ------------------------------------------------------------ парк машин */
function fleetGroup(cpl) {
  var g = null;
  FLEET.g.forEach(function (x) { if (x.cpl === cpl) g = x; });
  return g;
}
function fleetRow(m) {
  var cat = m.cat_esn
    ? '<a class="lnk doc" href="#/engine/' + esc(m.cat_esn) + '">' + esc(m.cat_esn) + "</a>"
    : '<span class="dim">—</span>';
  var cpl = m.cpl
    ? '<a class="lnk doc" href="#/cpl/' + esc(m.cpl) + '">' + esc(m.cpl) + "</a>"
    : '<span class="dim">нет в каталоге</span>';
  return "<tr><td>" + esc(m.machine) + '</td><td class="num">' + esc(m.vin) +
    '</td><td class="num">' + esc(m.esn) + "</td><td>" + cpl + "</td><td>" +
    esc(m.model || "") + "</td><td>" + esc(m.build || "") + "</td><td>" + cat + "</td></tr>";
}
function viewFleet() {
  var h = [crumbs([{ t: "База знаний", href: "#/kb" }, { t: "Парк машин" }])];
  var ok = FLEET.m.filter(function (m) { return m.ok; });
  h.push('<div class="kb-head"><h1>Парк машин</h1><p class="sub">' +
    FLEET.m.length + " машин · " + FLEET.g.length + " групп по CPL · " +
    (FLEET.m.length - ok.length) + " двигателей каталог Cummins не знает</p></div>");

  h.push('<div class="kb-hero"><p class="lead">Каталог запчастей определяется ' +
    "<b>CPL</b>, а не серийным номером: на каждый CPL нужен один каталог, " +
    "остальные машины группы им покрываются.</p></div>");

  h.push('<div class="kb-cols">');
  FLEET.g.forEach(function (g) {
    h.push('<section class="kb-card"><h2><a href="#/cpl/' + esc(g.cpl) + '">CPL ' +
      esc(g.cpl) + "</a></h2>" +
      '<p class="sub">' + esc(g.model) + " · " + esc(g.kinds.join(", ")) + "</p>" +
      '<ul class="kb-list">' +
      '<li>Машин в парке <span class="cnt">' + g.n + "</span></li>" +
      '<li>Каталог по ESN <span class="cnt">' + esc(g.cat_esn || "—") + "</span></li>" +
      '<li>Документов QuickServe <span class="cnt">' + g.docs + "</span></li>" +
      (g.configs.length > 1
        ? '<li class="dim">Конфигураций: ' + g.configs.length + "</li>" : "") +
      "</ul></section>");
  });
  h.push("</div>");

  h.push('<h2 class="kb-h2">Все машины</h2>');
  h.push('<div class="tw"><table class="kb-table"><thead><tr>' +
    "<th>Машина</th><th>VIN</th><th>ESN</th><th>CPL</th><th>Двигатель</th>" +
    "<th>Сборка</th><th>Каталог</th></tr></thead><tbody>");
  FLEET.m.slice().sort(function (a, b) {
    return (a.machine + a.esn).localeCompare(b.machine + b.esn);
  }).forEach(function (m) { h.push(fleetRow(m)); });
  h.push("</tbody></table></div>");
  render(h.join(""));
}

function viewCpl(cpl) {
  var g = fleetGroup(String(cpl));
  if (!g) { notFound("Группа CPL " + cpl); return; }
  var mine = FLEET.m.filter(function (m) { return m.cpl === g.cpl; });
  var h = [crumbs([{ t: "База знаний", href: "#/kb" },
                   { t: "Парк машин", href: "#/fleet" }, { t: "CPL " + g.cpl }])];
  h.push('<div class="doc-layout"><article class="kb-doc">');
  h.push('<div class="doc-head"><h1>CPL ' + esc(g.cpl) + " · " + esc(g.model) + "</h1>" +
    '<div class="doc-en">' + esc(g.kinds.join(", ")) + "</div>" +
    '<div class="doc-meta"><span class="mi">машин в парке: ' + g.n +
    "</span><span class=\"mi\">конфигураций: " + g.configs.length + "</span></div></div>");
  h.push('<div class="doc-body">');
  h.push("<p>Каталог запчастей этой группы — по двигателю " +
    (g.cat_esn ? '<a class="lnk doc" href="#/engine/' + esc(g.cat_esn) + '">' +
      esc(g.cat_esn) + "</a>" : "—") + ". " +
    (g.docs
      ? "Документация QuickServe: <a class=\"lnk doc\" href=\"#/docs/all\">" +
        g.docs + " документов</a> семейства " + esc(g.family || g.model) + "."
      : "<b>Документация QuickServe по этой группе не выгружена.</b>") + "</p>");
  if (g.configs.length > 1) {
    h.push('<div class="cal warning"><div class="cal-t">Несколько конфигураций</div>' +
      "<p>В группе " + g.configs.length + " конфигурации (" +
      esc(g.configs.join(", ")) + ") — состав по редким позициям может отличаться.</p></div>");
  }
  h.push('<div class="tw"><table class="doc-table"><thead><tr>' +
    "<th>Машина</th><th>VIN</th><th>ESN</th><th>Конфигурация</th>" +
    "<th>Сборка</th><th>Позиций</th></tr></thead><tbody>");
  mine.sort(function (a, b) { return (a.build || "").localeCompare(b.build || ""); })
    .forEach(function (m) {
      var mark = m.esn === g.cat_esn ? ' <span class="tag t-manual">каталог</span>' : "";
      h.push("<tr><td>" + esc(m.machine) + '</td><td class="num">' + esc(m.vin) +
        '</td><td class="num">' + esc(m.esn) + mark + "</td><td>" + esc(m.config) +
        "</td><td>" + esc(m.build) + '</td><td class="num">' + (m.parts || "") +
        "</td></tr>");
    });
  h.push("</tbody></table></div></div></article>");

  h.push('<aside class="doc-side"><section><h3>Каталог</h3><ul class="side-list">');
  if (g.cat_esn) {
    h.push('<li><a class="lnk doc" href="#/engine/' + esc(g.cat_esn) + '">Двигатель ' +
      esc(g.cat_esn) + "</a></li>");
  }
  h.push("</ul></section><section><h3>Машины группы</h3><ul class=\"side-list\">");
  mine.forEach(function (m) {
    h.push("<li>" + esc(m.machine) + ' <span class="dim">' + esc(m.esn) + "</span></li>");
  });
  h.push("</ul></section></aside></div>");
  render(h.join(""));
}

/* ------------------------------------------------- клики внутри базы */
document.addEventListener("click", function (e) {
  var a = e.target.closest ? e.target.closest("a") : null;
  if (!a) return;
  var api = window.CATALOG_API;

  if (a.hasAttribute("data-open-catalog") && api) {
    e.preventDefault();
    var pn = a.getAttribute("data-open-catalog");
    setMode(false); location.hash = "#/catalog";
    api.openPart(pn);
    return;
  }
  if (a.hasAttribute("data-open-option") && api) {
    e.preventDefault();
    var v = a.getAttribute("data-open-option").split("|");
    setMode(false); location.hash = "#/catalog";
    api.openOption(v[0], v[1], v[2] || null);
    return;
  }
  if (a.hasAttribute("data-open-engine") && api) {
    e.preventDefault();
    setMode(false); location.hash = "#/catalog";
    api.selectEngine(a.getAttribute("data-open-engine"));
    return;
  }
  if (a.hasAttribute("data-lang-set")) {
    e.preventDefault();
    setLang(a.getAttribute("data-lang-set"));
    route();
    return;
  }
  if (a.id === "nav-catalog") {
    e.preventDefault();
    setMode(false);
    if (location.hash) location.hash = "#/catalog";
  }
});

/* просмотр иллюстрации во весь экран */
document.addEventListener("click", function (e) {
  var img = e.target;
  if (!img || img.tagName !== "IMG") return;
  if (!img.closest(".doc-body, .part-photos")) return;
  var ov = document.createElement("div");
  ov.className = "kb-lightbox";
  ov.innerHTML = '<img src="' + img.getAttribute("src") + '" alt="">';
  ov.onclick = function () { ov.remove(); };
  document.body.appendChild(ov);
});
document.addEventListener("keydown", function (e) {
  if (e.key === "Escape") {
    var ov = document.querySelector(".kb-lightbox");
    if (ov) ov.remove();
  }
});

window.addEventListener("hashchange", route);

/* ------------------------------------------------------- внешний API */
window.KB = {
  active: active,
  lang: function () { return LANG; },
  setLang: function (v) { setLang(v); route(); },
  search: function (q) {
    lastQuery = q;
    if (q && q.trim().length >= 2) location.hash = "#/search/" + encodeURIComponent(q);
  },
  /* дописывает найденные документы в результаты поиска каталога */
  appendDocs: function (q, box) {
    if (!q || q.trim().length < 2 || !box) return;
    var lo = q.trim().toLowerCase();
    var hits = SEARCH.filter(function (r) {
      return r[0].toLowerCase().indexOf(lo) !== -1 ||
             (r[1] && r[1].toLowerCase().indexOf(lo) !== -1) ||
             (r[2] && r[2].toLowerCase().indexOf(lo) !== -1);
    });
    if (!hits.length) return;
    var wrap = document.createElement("div");
    wrap.className = "kb-inline";
    var head = "<h3>Документы базы знаний <span class=\"cnt\">" + hits.length + "</span>" +
      ' <a class="btn-mini" href="#/search/' + encodeURIComponent(q) + '">открыть поиск →</a></h3>';
    var rows = hits.slice(0, 12).map(function (r) {
      var d = DOCS[r[0]] || {};
      return "<tr><td class='c-id'>" + docLink(r[0], r[0]) + "</td><td>" + badge(r[3]) + " " +
        esc(r[2] || r[1]) + "</td><td class='c-date'>" + esc(d.d || "") + "</td></tr>";
    }).join("");
    wrap.innerHTML = head + '<table class="kb-table">' + rows + "</table>";
    box.appendChild(wrap);
  },
  /* ссылки на базу знаний в карточке детали каталога */
  decoratePartCard: function (pn) {
    var host = document.getElementById("pc-name");
    if (!host) return;
    var old = document.getElementById("pc-kb");
    if (old) old.remove();
    var p = PARTS[pn];
    var box = document.createElement("div");
    box.id = "pc-kb";
    box.className = "pc-kb";
    var bits = [];
    if (p && p.ru) bits.push("<b>" + esc(p.ru) + "</b>");
    bits.push('<a class="btn-mini" href="#/part/' + esc(pn) + '">Открыть в базе знаний →</a>');
    if (p && p.d && p.d.length) {
      bits.push('<span class="sub">упоминается в документах: ' + p.d.length + "</span>");
    }
    box.innerHTML = bits.join(" ");
    host.parentNode.insertBefore(box, host.nextSibling);
  },
  photoUrl: photoUrl,
  ruPart: function (pn) { return (PARTS[pn] && PARTS[pn].ru) || ""; },
  ruOption: function (no) { return (NAMES.opt && NAMES.opt[no]) || ""; },
  route: route
};

setLang(LANG);
var langBox = document.getElementById("lang-switch");
if (langBox) {
  langBox.addEventListener("click", function (e) {
    var b = e.target.closest("button[data-lang]");
    if (!b) return;
    setLang(b.getAttribute("data-lang"));
    route();
  });
}
route();
})();
