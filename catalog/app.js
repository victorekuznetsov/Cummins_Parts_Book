/* Каталог запасных частей Cummins — вся логика на клиенте,
   данные лежат в data.js (window.CATALOG), поэтому сервер не нужен. */
(function () {
"use strict";

var C = window.CATALOG;
if (!C) { document.body.innerHTML = "<p style='padding:40px'>Не найден файл data.js</p>"; return; }

var LS_CART = "cummins_cart_" + C.esn;
var LS_SER  = "cummins_serial_" + C.esn;

var byNo = {};                     // номер узла -> узел
C.options.forEach(function (o) { byNo[o.no] = o; });

var CARDS = C.cards || {};         // номер детали -> карточка (атрибуты, замены, применяемость)

/* Индекс замен номеров: любой номер из цепочки (в т.ч. снятый с производства)
   ведёт на деталь, которая есть в каталоге. Так «старый» номер тоже находится. */
var SUP_INDEX = {};
Object.keys(CARDS).forEach(function (pn) {
  var chain = CARDS[pn].sup || [];
  chain.forEach(function (s) {
    if (!s.no || s.no === pn) return;
    (SUP_INDEX[normNo(s.no)] = SUP_INDEX[normNo(s.no)] || []).push({ pn: pn, s: s });
  });
});

function normNo(s) { return String(s || "").toUpperCase().replace(/[\s-]/g, ""); }

/* Цепочка замен отсортирована от старого номера к новому: последний элемент —
   действующий номер. Возвращаем его, если это не сам номер детали. */
function currentNo(pn) {
  var chain = (CARDS[pn] || {}).sup || [];
  if (chain.length < 2) return "";
  var last = chain[chain.length - 1];
  return last && last.no !== pn ? last.no : "";
}

var state = { option: null, sheet: 0, cart: loadCart(), zoom: false };

/* ---------- вспомогательное ---------- */
function $(id) { return document.getElementById(id); }
function el(tag, cls, text) {
  var e = document.createElement(tag);
  if (cls) e.className = cls;
  if (text != null) e.textContent = text;
  return e;
}
function money(v) {
  if (v == null || isNaN(v)) return "";
  return v.toLocaleString("ru-RU", { minimumFractionDigits: 2, maximumFractionDigits: 2 });
}
function loadCart() {
  try { return JSON.parse(localStorage.getItem(LS_CART)) || {}; } catch (e) { return {}; }
}
function saveCart() {
  try { localStorage.setItem(LS_CART, JSON.stringify(state.cart)); } catch (e) {}
  renderCartCount();
}

/* ---------- паспорт двигателя ---------- */
function renderPassport() {
  $("engine-line").textContent = (C.model || "") + " · ESN " + C.esn;
  var rows = [
    ["Серийный номер (ESN)", C.esn],
    ["Модель", C.model],
    ["CPL", C.cpl],
    ["Дата сборки", C.buildDate],
    ["Конфигурация", C.config],
    ["Группа", C.group],
    ["Код завода", C.plant]
  ];
  var p = $("passport");
  p.innerHTML = "";
  rows.forEach(function (r) {
    if (!r[1]) return;
    var d = el("div");
    d.appendChild(el("span", null, r[0] + ": "));
    d.appendChild(el("b", null, String(r[1])));
    p.appendChild(d);
  });
  $("serial").value = localStorage.getItem(LS_SER) || C.esn;
}

/* ---------- дерево систем ---------- */
function renderTree() {
  var tree = $("tree");
  tree.innerHTML = "";
  C.systems.forEach(function (s) {
    var box  = el("div", "tree-sys");
    var head = el("div", "tree-sys-head");
    head.appendChild(el("span", null, s.name));
    head.appendChild(el("span", "cnt", s.options.length));
    head.onclick = function () { box.classList.toggle("open"); };
    box.appendChild(head);

    var list = el("div", "tree-opts");
    s.options.forEach(function (no) {
      var o = byNo[no];
      if (!o) return;
      var a = el("div", "tree-opt");
      a.appendChild(el("span", null, o.name));
      a.appendChild(el("span", "no", no + " · позиций: " + o.parts.length));
      a.dataset.no = no;
      a.onclick = function () { openOption(no); };
      list.appendChild(a);
    });
    box.appendChild(list);
    tree.appendChild(box);
  });
}

function highlightTree(no) {
  Array.prototype.forEach.call(document.querySelectorAll(".tree-opt"), function (a) {
    a.classList.toggle("active", a.dataset.no === no);
  });
  var active = document.querySelector('.tree-opt[data-no="' + no + '"]');
  if (active) {
    var sys = active.closest(".tree-sys");
    if (sys && !sys.classList.contains("open")) sys.classList.add("open");
    active.scrollIntoView({ block: "nearest" });
  }
}

/* ---------- показ узла ---------- */
function show(view) {
  ["view-welcome", "view-search", "view-option"].forEach(function (v) {
    $(v).classList.toggle("hidden", v !== view);
  });
}

function openOption(no, focusPart) {
  var o = byNo[no];
  if (!o) return;
  state.option = o; state.sheet = 0; state.zoom = false;
  show("view-option");
  highlightTree(no);

  $("opt-name").textContent = o.name;
  var meta = "Вариант исполнения " + o.no + " · позиций: " + o.parts.length;
  if (o.systems && o.systems.length) meta += " · система: " + o.systems.join(", ");
  $("opt-meta").textContent = meta;

  var rem = $("opt-remarks");
  if (o.remarks) { rem.textContent = o.remarks.replace(/\|/g, "\n"); rem.classList.remove("hidden"); }
  else rem.classList.add("hidden");

  renderSheets(o);
  renderParts(o, focusPart);
  window.scrollTo(0, 0);
}

function renderSheets(o) {
  var img = $("drawing"), car = $("carousel"), hint = $("drawing-hint");
  var wrap = img.parentNode;
  var old = wrap.querySelector(".no-drawing");
  if (old) wrap.removeChild(old);

  if (!o.sheets.length) {
    img.classList.add("hidden");
    car.classList.add("hidden");
    wrap.appendChild(el("div", "no-drawing",
      "Для этого узла Cummins не публикует чертёж — список позиций приведён справа."));
    hint.textContent = "";
    return;
  }
  img.classList.remove("hidden");
  img.classList.remove("zoomed");
  img.src = "drawings/" + o.sheets[state.sheet];
  img.alt = "Чертёж узла " + o.no;
  car.classList.toggle("hidden", o.sheets.length < 2);
  $("sheet-label").textContent = "Лист " + (state.sheet + 1) + " из " + o.sheets.length;
  hint.textContent = "Номер на чертеже = № позиции в таблице. Щелчок по чертежу — увеличить.";
}

$("sheet-prev").onclick = function () {
  var o = state.option; if (!o || !o.sheets.length) return;
  state.sheet = (state.sheet - 1 + o.sheets.length) % o.sheets.length;
  renderSheets(o);
};
$("sheet-next").onclick = function () {
  var o = state.option; if (!o || !o.sheets.length) return;
  state.sheet = (state.sheet + 1) % o.sheets.length;
  renderSheets(o);
};
$("drawing").onclick = function () {
  state.zoom = !state.zoom;
  this.classList.toggle("zoomed", state.zoom);
};

function renderParts(o, focusPart) {
  var tb = $("parts-body");
  tb.innerHTML = "";
  o.parts.forEach(function (p, i) {
    var tr = el("tr", p.lvl ? "lvl" + Math.min(p.lvl, 2) : "");
    tr.dataset.no = p.no;

    // «ASSEMBLY» у Cummins — строка узла в сборе, а не номер позиции на чертеже
    var isAsm = /^assembly$/i.test(p.pos || "");
    var tdPos = el("td", "c-pos" + (isAsm ? " c-asm" : ""), isAsm ? "сборка" : (p.pos || ""));
    if (isAsm) tdPos.title = "Узел в сборе (ASSEMBLY)";
    tr.appendChild(tdPos);

    var tdNo = el("td", "c-no");
    if (p.img) {
      var im = document.createElement("img");
      im.className = "pn-photo"; im.src = "parts/" + p.img; im.alt = "";
      im.onerror = function () { this.style.display = "none"; };
      tdNo.appendChild(im);
    }
    var pnSpan = el("span", "pn", p.no || "—");
    if (p.no && CARDS[p.no]) {
      pnSpan.className = "pn pn-link";
      pnSpan.title = "Открыть карточку детали";
      pnSpan.onclick = function () { openPartCard(p.no); };
    }
    tdNo.appendChild(pnSpan);
    var newNo = p.no ? currentNo(p.no) : "";
    if (newNo) {
      var chip = el("span", "chip-sup", "→ " + newNo);
      chip.title = "Номер заменён; действующий номер " + newNo;
      tdNo.appendChild(chip);
    }
    tr.appendChild(tdNo);

    var tdName = el("td", "c-name");
    tdName.appendChild(document.createTextNode(p.name || ""));
    if (p.dim) tdName.appendChild(el("span", "dim", p.dim));
    if (p.rem) tdName.appendChild(el("span", "dim", p.rem));
    if (p.alt) tdName.appendChild(el("span", "dim", "взаимозаменяемый: " + p.alt));
    tr.appendChild(tdName);

    tr.appendChild(el("td", "c-price", p.price != null ? money(p.price) : "—"));
    tr.appendChild(el("td", "c-qty", p.qty || ""));

    var tdNeed = el("td", "c-need");
    var inp = el("input", "need-input");
    inp.type = "number"; inp.min = "0"; inp.step = "1";
    inp.value = parseInt(p.qty, 10) > 0 ? parseInt(p.qty, 10) : 1;
    tdNeed.appendChild(inp);
    tr.appendChild(tdNeed);

    var tdAdd = el("td", "c-add");
    var btn = el("button", "btn-add", "＋ в заказ");
    btn.onclick = function () {
      var n = parseInt(inp.value, 10);
      if (!p.no || !(n > 0)) return;
      addToCart(p, o, n);
      btn.textContent = "✓ добавлено";
      btn.classList.add("done");
      setTimeout(function () {
        btn.textContent = "＋ в заказ"; btn.classList.remove("done");
      }, 1200);
    };
    if (!p.no) btn.disabled = true;
    tdAdd.appendChild(btn);
    tr.appendChild(tdAdd);

    tb.appendChild(tr);
    if (focusPart && p.no === focusPart && i < 400) {
      setTimeout(function () {
        tr.scrollIntoView({ block: "center", behavior: "smooth" });
        tr.style.background = "#fff5cc";
        setTimeout(function () { tr.style.background = ""; }, 2500);
      }, 150);
    }
  });
}

/* ---------- карточка детали ---------- */
function findPart(pn) {
  for (var i = 0; i < C.options.length; i++) {
    var ps = C.options[i].parts;
    for (var j = 0; j < ps.length; j++) if (ps[j].no === pn) return ps[j];
  }
  return null;
}

function openPartCard(pn) {
  var card = CARDS[pn] || {};
  var part = findPart(pn) || {};
  $("pc-title").textContent = "Деталь " + pn;
  $("pc-name").textContent = part.name || card.en || "";

  // фото: все ракурсы
  var views = card.views || (part.img ? [part.img] : []);
  var main = $("pc-img"), thumbs = $("pc-thumbs");
  thumbs.innerHTML = "";
  document.querySelector(".pc-gallery").style.display = views.length ? "" : "none";
  if (views.length) {
    main.style.display = "";
    main.src = "parts/" + views[0];
    views.forEach(function (v, i) {
      var t = document.createElement("img");
      t.src = "parts/" + v; t.alt = "";
      if (!i) t.className = "sel";
      t.onclick = function () {
        main.src = "parts/" + v;
        Array.prototype.forEach.call(thumbs.children, function (c) { c.className = ""; });
        t.className = "sel";
      };
      t.onerror = function () { this.style.display = "none"; };
      thumbs.appendChild(t);
    });
  } else {
    main.style.display = "none";
  }

  // замены номеров: цепочка старый -> новый
  var chain = card.sup || [];
  var supBox = $("pc-sup"), supBody = $("pc-sup-body");
  supBody.innerHTML = "";
  if (chain.length > 1) {
    var row = el("div", "sup-chain");
    chain.forEach(function (s, i) {
      var isLast = (i === chain.length - 1);
      if (i) row.appendChild(el("span", "sup-arrow", "→"));
      var b = el("span", "sup-no " + (isLast ? "cur" : "old"), s.no);
      b.title = (s.st || "") + (s.sell ? " · продаётся" : " · не продаётся");
      if (CARDS[s.no] && s.no !== pn) b.onclick = function () { openPartCard(s.no); };
      row.appendChild(b);
    });
    supBody.appendChild(row);
    var cur = currentNo(pn), lastSt = chain[chain.length - 1];
    var note;
    if (cur) {
      note = "Номер " + pn + " заменён, действующий номер — " + cur + ".";
      if (lastSt && !lastSt.sell) {
        note += " По данным Cummins он отмечен как «" + lastSt.st +
                "» — наличие уточняйте у поставщика.";
      }
    } else {
      note = "Номер " + pn + " действующий; левее приведены заменённые им номера.";
    }
    supBody.appendChild(el("div", "sup-note", note));
    supBox.classList.remove("hidden");
  } else supBox.classList.add("hidden");

  // характеристики
  var attrs = card.attrs || {}, keys = Object.keys(attrs);
  var at = $("pc-attrs"), atb = $("pc-attrs-body");
  atb.innerHTML = "";
  if (part.qty) addAttr(atb, "Количество на схеме", part.qty);
  if (part.dim) addAttr(atb, "Типоразмер", part.dim);
  if (card.wt) addAttr(atb, "Масса, кг", card.wt);
  if (card.dim) addAttr(atb, "Габариты Д×Ш×В, мм", card.dim);
  // размеры и массу уже показали в метрических единицах — исходные дюймы/фунты не дублируем
  var SKIP = { "Length": 1, "Width": 1, "Height": 1, "Weight": 1 };
  var RU = { "Sellable": "Продаётся отдельно",
             "Hazardous Material": "Опасный груз" };
  keys.forEach(function (k) {
    if (SKIP[k]) return;
    var v = attrs[k];
    if (k === "Sellable") v = (v === "Y" ? "да" : "нет");
    addAttr(atb, RU[k] || k, v);
  });
  if (card.recon) addAttr(atb, "Аналог Recon", card.recon);
  at.classList.toggle("hidden", !atb.children.length);

  // где применяется
  var used = card.used || [];
  var ub = $("pc-used-body");
  ub.innerHTML = "";
  used.forEach(function (u) {
    ub.appendChild(el("span", null, u.o + (u.n ? " · " + u.n : "")));
  });
  $("pc-used").classList.toggle("hidden", !used.length);

  $("part-card").classList.remove("hidden");
  $("part-overlay").classList.remove("hidden");
}

function addAttr(tbl, name, value) {
  var tr = el("tr");
  tr.appendChild(el("td", null, name));
  tr.appendChild(el("td", null, String(value).trim()));
  tbl.appendChild(tr);
}

function closePartCard() {
  $("part-card").classList.add("hidden");
  $("part-overlay").classList.add("hidden");
}
$("pc-close").onclick = closePartCard;
$("part-overlay").onclick = closePartCard;

/* ---------- поиск ---------- */
function escapeRe(s) { return s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&"); }

function doSearch(q) {
  q = (q || "").trim();
  if (q.length < 2) { show("welcome" === q ? "view-welcome" : "view-welcome"); return; }
  var norm = q.toUpperCase().replace(/\s+/g, "");
  var re = new RegExp(escapeRe(q), "i");
  var hits = [], seen = {};

  C.options.forEach(function (o) {
    o.parts.forEach(function (p) {
      var num = normNo(p.no);
      var hitNo = num && num.indexOf(norm) !== -1;
      var hitNm = p.name && re.test(p.name);
      if (!hitNo && !hitNm) return;
      var key = p.no + "|" + o.no;
      if (seen[key]) return;
      seen[key] = 1;
      hits.push({ p: p, o: o, exact: num === norm });
    });
  });

  // поиск по заменённым (старым) номерам: номера нет в каталоге, но он
  // числится в цепочке замен — показываем деталь, которая его заменяет
  Object.keys(SUP_INDEX).forEach(function (old) {
    if (old.indexOf(norm) === -1) return;
    SUP_INDEX[old].forEach(function (rec) {
      C.options.forEach(function (o) {
        o.parts.forEach(function (p) {
          if (p.no !== rec.pn) return;
          var key = p.no + "|" + o.no;
          if (seen[key]) return;
          seen[key] = 1;
          hits.push({ p: p, o: o, exact: false, via: rec.s.no });
        });
      });
    });
  });
  hits.sort(function (a, b) {
    if (a.exact !== b.exact) return a.exact ? -1 : 1;
    return (a.p.no || "").localeCompare(b.p.no || "");
  });

  show("view-search");
  $("search-title").textContent = "Найдено: " + hits.length +
    (hits.length ? "" : " — попробуйте другой номер или слово");
  var box = $("search-results");
  box.innerHTML = "";
  hits.slice(0, 400).forEach(function (h) {
    var d = el("div", "search-hit");
    var no = el("span", "hit-no", h.p.no || "—");
    if (h.via) no.appendChild(el("span", "chip-sup", "вместо " + h.via));
    d.appendChild(no);
    var nm = el("span", "hit-name");
    nm.innerHTML = highlight(h.p.name || "", q);
    d.appendChild(nm);
    d.appendChild(el("span", "hit-where",
      h.o.name + " · " + h.o.no + " · поз. " + (h.p.pos || "—")));
    d.onclick = function () { openOption(h.o.no, h.p.no); };
    box.appendChild(d);
  });
  if (hits.length > 400) {
    box.appendChild(el("p", "sub", "Показаны первые 400 совпадений — уточните запрос."));
  }
}

function highlight(text, q) {
  var safeText = text.replace(/[&<>]/g, function (c) {
    return { "&": "&amp;", "<": "&lt;", ">": "&gt;" }[c];
  });
  try {
    return safeText.replace(new RegExp("(" + escapeRe(q) + ")", "ig"), "<mark>$1</mark>");
  } catch (e) { return safeText; }
}

var searchTimer = null;
$("search").addEventListener("input", function () {
  var v = this.value;
  clearTimeout(searchTimer);
  searchTimer = setTimeout(function () {
    if (v.trim().length < 2) { if (state.option) openOption(state.option.no); else show("view-welcome"); }
    else doSearch(v);
  }, 200);
});
$("search-clear").onclick = function () {
  $("search").value = "";
  if (state.option) openOption(state.option.no); else show("view-welcome");
};

/* ---------- корзина ---------- */
function addToCart(p, o, n) {
  var k = p.no;
  if (!state.cart[k]) {
    state.cart[k] = { no: p.no, name: p.name, price: (p.price != null ? p.price : null),
                      group: p.group || "", alt: p.alt || "",
                      option: o.no, optionName: o.name, pos: p.pos || "", qty: 0 };
  }
  state.cart[k].qty += n;
  saveCart();
  renderCart();
}

function renderCartCount() {
  var keys = Object.keys(state.cart);
  $("cart-count").textContent = keys.length;
}

function renderCart() {
  var tb = $("cart-body"), keys = Object.keys(state.cart).sort();
  tb.innerHTML = "";
  var total = 0, anyPrice = false;
  keys.forEach(function (k) {
    var it = state.cart[k];
    var tr = el("tr");
    tr.appendChild(el("td", "pn", it.no));
    var nm = el("td");
    nm.appendChild(document.createTextNode(it.name || ""));
    nm.appendChild(el("span", "dim", it.optionName + " · " + it.option + " · поз. " + it.pos));
    tr.appendChild(nm);

    var tdQ = el("td");
    var inp = el("input", "need-input");
    inp.type = "number"; inp.min = "1"; inp.step = "1"; inp.value = it.qty;
    inp.onchange = function () {
      var v = parseInt(this.value, 10);
      if (v > 0) { it.qty = v; saveCart(); renderCart(); }
      else { this.value = it.qty; }
    };
    tdQ.appendChild(inp);
    tr.appendChild(tdQ);

    var sum = (it.price != null) ? it.price * it.qty : null;
    if (sum != null) { total += sum; anyPrice = true; }
    tr.appendChild(el("td", null, sum != null ? money(sum) : "—"));

    var tdDel = el("td");
    var del = el("button", "btn-plain", "✕");
    del.title = "Убрать из заказа";
    del.onclick = function () { delete state.cart[k]; saveCart(); renderCart(); };
    tdDel.appendChild(del);
    tr.appendChild(tdDel);

    tb.appendChild(tr);
  });
  $("cart-empty").classList.toggle("hidden", keys.length > 0);
  $("cart-total").textContent = anyPrice ? money(total) : String(keys.length);
  $("cart-total-cur").textContent = anyPrice ? "" : "позиций (цены не загружены)";
  renderCartCount();
}

function openCart() {
  renderCart();
  $("cart").classList.remove("hidden");
  $("cart-overlay").classList.remove("hidden");
}
function closeCart() {
  $("cart").classList.add("hidden");
  $("cart-overlay").classList.add("hidden");
}
$("cart-toggle").onclick = openCart;
$("cart-close").onclick = closeCart;
$("cart-overlay").onclick = closeCart;
$("serial").addEventListener("input", function () {
  try { localStorage.setItem(LS_SER, this.value); } catch (e) {}
});
$("cart-clear").onclick = function () {
  if (!confirm("Очистить весь заказ?")) return;
  state.cart = {}; saveCart(); renderCart();
};
$("cart-print").onclick = function () { window.print(); };

$("cart-csv").onclick = function () {
  var keys = Object.keys(state.cart).sort();
  if (!keys.length) { alert("Заказ пуст"); return; }
  var serial = $("serial").value || C.esn;
  var head = ["Серийный номер", "Номер детали", "Наименование", "Группа",
              "Взаимозаменяемый артикул", "Узел", "Номер узла", "Позиция",
              "Количество", "Цена", "Сумма"];
  var lines = [head.join(";")];
  var total = 0;
  keys.forEach(function (k) {
    var it = state.cart[k];
    var sum = (it.price != null) ? it.price * it.qty : null;
    if (sum != null) total += sum;
    lines.push([serial, it.no, it.name, it.group, it.alt, it.optionName, it.option,
                it.pos, it.qty,
                it.price != null ? String(it.price).replace(".", ",") : "",
                sum != null ? String(sum.toFixed(2)).replace(".", ",") : ""]
      .map(function (v) {
        v = String(v == null ? "" : v);
        return /[";\n]/.test(v) ? '"' + v.replace(/"/g, '""') + '"' : v;
      }).join(";"));
  });
  lines.push(["", "", "ИТОГО", "", "", "", "", "", "", "",
              total ? String(total.toFixed(2)).replace(".", ",") : ""].join(";"));

  var blob = new Blob(["﻿" + lines.join("\r\n")], { type: "text/csv;charset=utf-8;" });
  var a = document.createElement("a");
  a.href = URL.createObjectURL(blob);
  a.download = "zakaz_" + serial + ".csv";
  document.body.appendChild(a); a.click(); document.body.removeChild(a);
  setTimeout(function () { URL.revokeObjectURL(a.href); }, 1000);
};

document.addEventListener("keydown", function (e) {
  if (e.key === "Escape") { closeCart(); closePartCard(); }
});

/* ---------- старт ---------- */
renderPassport();
renderTree();
renderCartCount();
show("view-welcome");
})();
