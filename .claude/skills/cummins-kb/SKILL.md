---
name: cummins-kb
description: Build a searchable Cummins knowledge base from downloaded QuickServe (QSOL) documentation — TSBs, service bulletins, service manuals and their procedures, STI sheets, install instructions, outlines — organised in QuickServe's own format (engine → CPL/model → category → document) and indexed for fast retrieval (exact doc number, model/CPL/system facets, SPN/FMI fault codes, and client-side full-text). Use when the user wants to turn the raw QSOL corpus (bulletins/ + rawdata/quickserve/) into a browsable/searchable KB, add engines to an existing KB, or improve how quickly the right document is found.
user-invocable: true
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Glob
  - Grep
---

# Cummins knowledge base (QuickServe format, fast document search)

Turn the raw QuickServe documentation corpus into a static, server-less
knowledge base that mirrors QuickServe's own navigation and answers
"which document do I need?" in one or two clicks / one query.

Pairs with the `quickserve-docs` skill: that one **downloads** the docs, this
one **organises and indexes** them. Run `quickserve-docs` first (or when adding
engines), then this skill to (re)build the KB.

## Source corpus (input)

- `rawdata/quickserve/<cat>/<id>.{pdf,html}` and (older set) `bulletins/<cat>/…`
  where `<cat>` ∈ `tsb bulletin manual sti install_inst outlines procedures`.
- `rawdata/quickserve/index.json` (and `bulletins/index.json`): one record per
  doc — `{id, cat, url, engines[], html, pdf}`. `engines[]` are ESNs.
- Engine → CPL/model map: `rawdata/<esn>/report.json` (`cpl`, `serviceModel`)
  and `engines.js` (`window.ENGINES`), plus `fleet/fleet_report.json`
  (`checked[].{esn,cpl,model}`). CPL is the join key — QSOL docs are per model/CPL.
- Fleet context: `fleet/*.tsv` (serial → machine/owner) for machine-level lookup.

## KB data model (output — server-less, lazy-loaded)

The catalog page loads `kb.js` plus these generated data files (all are plain
`window.KB_*` assignments so it works from `file://` and on Vercel):

- `data/kb_docs.js` → `window.KB_DOCS = { <id>: {cat, num, title, model, cpl:[],
  engines:[], system, date, sup:[old nums], pdf, html} }` — the metadata catalog.
- `data/kb_manuals.js` → manuals and their procedure lists (`KB_MANUALS`).
- `data/kb_topics.js` → service topics / groupings (`KB_TOPICS`).
- `data/kb_parts.js` → part ↔ document cross-refs (`KB_PARTS`).
- `data/kb_fleet.js` → machines & engines (`KB_FLEET = {m:[…], g:[…]}`).
- `data/kb_fault_codes.js` → **SPN/FMI (and INSITE) fault code → doc ids** — the
  diagnostic entry point ("engine throws SPN 111 → these TSBs/procedures").
- `data/kb_names.js` → id → human title (RU/EN) for link labels (`KB_NAMES`).
- `data/kb_photos.js` → available illustration filenames (`KB_PHOTOS`).
- `data/kb_search.js` → compact search rows `KB_SEARCH = [[id,cat,title,model,
  keywords]]` for instant type-ahead.
- `data/kb_fts.js` → full-text inverted index `{token: [doc ids]}` for body search.
- `data/kb/body_<N>.js` → document **bodies** split into chunks
  (`window.KB_BODY[id]=…`), loaded on demand so the index stays small.

Keep chunks ≈ a few hundred KB each; never inline all bodies into one file.

## Build pipeline

1. **Load the index** (`rawdata/quickserve/index.json` ∪ `bulletins/index.json`);
   dedupe by `(cat,id)`, union `engines`.
2. **Resolve model/CPL** for each doc from its `engines[]` via the ESN→CPL map.
3. **Parse each HTML** (`<cat>/<id>.html`) → `title`/heading, doc number, revision
   date, applicable model, system/component, and the plain-text **body**
   (strip nav/script). For TSBs also extract **SPN/FMI** and symptom keywords;
   for procedures extract the procedure code and parent manual.
4. **Emit metadata** → `KB_DOCS`, `KB_NAMES`, `KB_MANUALS`, `KB_TOPICS`,
   `KB_FLEET`, `KB_PARTS`, `KB_FAULT_CODES`.
5. **Build search structures:**
   - type-ahead rows → `KB_SEARCH` (id, cat, title, model, top keywords);
   - inverted full-text index over `title + body` → `KB_FTS`
     (lowercase, fold RU/EN, drop stopwords, keep doc-number tokens intact);
   - fault-code map → `KB_FAULT_CODES`.
6. **Chunk bodies** → `data/kb/body_<N>.js`; record chunk-of for each id.
7. **Wire up** `index.html` to load `kb.js` + the `data/kb_*.js` files (bodies are
   fetched lazily by `kb.js`).

Make the build **idempotent and incremental**: adding engines re-parses only new
`id`s and appends to the indexes/chunks.

## Search design — QuickServe format + fast lookup

Mirror QSOL's own path so users think the way the source is organised:

1. **Engine/serial → CPL/model** (pick ESN or machine; docs filter to that CPL).
2. **Category** tab: Service Bulletins (TSB) · Bulletins · Manuals/Procedures ·
   STI · Install · Outlines.
3. Within that, **find the document by:**
   - **exact doc number** (primary key; also resolve **superseded/old numbers**
     to the current one);
   - **facets**: model, CPL, engine system, year, category, fault code;
   - **keyword / full-text** over title + body (`KB_FTS`), ranked title-first;
   - **fault code (SPN/FMI)** → jump straight to the relevant TSBs/procedures.

Rules that keep it fast: doc number is the canonical key; every list is
pre-sorted; full-text is a prebuilt inverted index (no scanning); bodies load
only when a document is opened.

## Verify

- Every `index.json` doc has a `KB_DOCS` entry; every `KB_DOCS` id has a body
  chunk or a "no body" flag (genuine QSOL 404s are expected — mark, don't drop).
- `KB_SEARCH`/`KB_FTS` cover all ids; fault-code map non-empty for TSB-heavy CPLs.
- Open `index.html` from `file://`: no console errors, search returns hits,
  a doc opens and lazy-loads its body, CPL/model facets filter correctly.

## Adding engines later

1. `quickserve-docs` → download the new engines' docs into `rawdata/quickserve/`
   (deduped against `bulletins/`), merge `index.json`.
2. Re-run this build (incremental) → new ids appear in KB + search.
3. Commit `rawdata/quickserve/**` + regenerated `data/kb_*.js` + `data/kb/body_*`
   and push (large → push in chunks, see `quickserve-docs`).

See `quickserve-docs` for the download side and the QSOL URL/endpoint templates.
Fleet coverage is audited by CPL: one document set per CPL covers every serial of
that CPL (verify with `fleet/fleet_report.json` + `index.json` engines).
