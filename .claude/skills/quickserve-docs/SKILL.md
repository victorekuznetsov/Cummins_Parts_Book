---
name: quickserve-docs
description: Download Cummins QuickServe Online (QSOL) technical documentation — Technical Service Bulletins, Service Bulletins, service manuals (full procedure trees), STI service-tool sheets, install instructions and outlines — for a set of engine serial numbers (ESN), saving each document as PDF + HTML for an offline catalog. Use when the user asks to pull, mirror, or download service bulletins / manuals / QuickServe docs for Cummins engines, or to refresh/extend the Cummins_Parts_Book documentation set.
user-invocable: true
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
---

# QuickServe Online (QSOL) technical-documentation downloader

Mirror the service documentation for one or more Cummins engines from
`quickserve.cummins.com` into `bulletins/<category>/<id>.{pdf,html}`, then
(optionally) push to `github.com/victorekuznetsov/Cummins_Parts_Book`.

This skill acts only on a request typed by the user. It logs into the user's
own QuickServe account with credentials the user supplies — never hard-code or
commit them.

## Prerequisites

- Python with Playwright + real Chrome: `python -m playwright install chrome`
  (QSOL needs a real browser; content loads via JS/POST, so plain `requests`
  gets only a stub shell).
- QuickServe credentials from the user: **username, password, and Company Id**
  (all three are required at login). Pass them as env vars `QS_USER` / `QS_PWD`;
  the Company Id and any prompt are typed by the user in the login window.
- Working dir: the Cummins project (`C:\Projects\cummins`). Scripts live in
  `quickserve/`, output in `bulletins/`.

## How QSOL works (verified 2026-08)

- **Login:** portal `https://quickserve.cummins.com/qs3/portal/index.html`
  redirects to Cummins IAM `mylogin.cummins.com/clw/s/login` (Salesforce
  Lightning). Form fields: `input[name=username]`, `input[name=password]`,
  `input[name=company_id]`. No MFA. Session cookie = `IACSESSION`.
- **Activate an engine:** `GET /qs3/portal/includes/ajax/set_esn.json?esn=<ESN>`
  — sets session context and returns the engine's filter attrs
  `ef, fs, da, ma` (plus `cpl`, `pc`).
- **List bulletins:** `GET /qs3/portal/service/filter_tsb.json?group_num=&ef=&fs=&da=&ma=`
  → `{data:[{doc_num, doc_title, doc_year, doc_type, group_name, ...}]}`.
  `doc_type 37` = TSB, `doc_type 4` = Service Bulletin.
- **Service page** `/qs3/portal/service/index.html` (after set_esn) links the
  rest: manuals, STI, install instructions, outlines.
- **Document URL templates** (`<lang>` = `en`):
  - TSB (type 37): `/qs3/pubsys2/xml/en/tsb/<doc_year>/<doc_num>.html`
  - Service Bulletin (type 4): `/qs3/pubsys2/xml/en/bulletin/<doc_num>.html`
  - Manual revision history: `/qs3/pubsys2/xml/en/manual/<id>/<id>-history.html`
    (this page links every **procedure** of that manual)
  - Manual procedures (the actual manual text):
    `/qs3/pubsys2/xml/en/procedures/<grp>/<code>.html`
  - STI: `/qs3/pubsys2/xml/en/sti/<id>.html`
  - Install instructions: `/qs3/pubsys2/xml/en/install_inst/<id>.html`
  - Outlines: `/qs3/pubsys2/xml/en/outlines/<id>.html`
- Every doc page returns a ~1.3 KB shell on GET, then fills content via a POST
  to the same URL. **Render it in a browser** (headless Chrome with the saved
  session) and read/print — do not scrape the raw GET.

## Workflow

1. **Login & save session** (headed, one-time, user types Company Id):
   `QS_USER=… QS_PWD=… python quickserve/qs_login2.py`
   Auto-fills user/password; user enters Company Id + clicks Login. On success
   it writes `quickserve/storage_state.json` (the reusable session).

2. **Confirm the engine list.** Ask the user which ESNs (or read the catalog's
   engines). This session used 5: `33239899 37292556 41353297 41370103 93087701`.

3. **Enumerate bulletins per ESN:** `python quickserve/qs_scope.py <ESN…>`
   — for each ESN: set_esn → filter_tsb → writes `quickserve/tsb_<ESN>.json`
   and prints counts. TSBs/bulletins overlap across engines; dedupe by doc_num.

4. **Enumerate the full service library:** `python quickserve/enum_service.py`
   — for each ESN loads the service page, collects all pubsys2 links (manual /
   sti / install_inst / outlines) + the filter_tsb bulletins →
   `quickserve/doc_manifest.json` (url, category, engines).

5. **Expand manuals into procedures** (the real manual content):
   `python quickserve/enum_procedures.py` then `python quickserve/add_procedures.py`
   — read each downloaded `*-history.html`, extract
   `/procedures/<grp>/<code>.html` links, normalize `procedures//`→`procedures/`,
   dedupe, append to the manifest with `cat=procedures` (engines inherited from
   the referencing manual).

6. **Download** (render → PDF + HTML, resumable):
   `python quickserve/download_docs.py`
   — one headless Chrome with the session, per doc: goto (networkidle) → save
   `page.content()` to `bulletins/<cat>/<id>.html` and `page.pdf()` to
   `bulletins/<cat>/<id>.pdf`; skip if both exist; log `File not found` (real
   server-side gaps) and re-run to retry transient timeouts. Writes
   `bulletins/index.json` (id → cat → url → engines → local paths).
   Scale reference: 5 engines ≈ 3150 docs (≈2600 manual procedures) ≈ 2.1 GB,
   a few hours. Run in the background and watch file counts, not the buffered log.

7. **Verify:** all PDFs > 1 KB, retry until `err=0`; only genuine 404s remain
   (≈3 % of procedures are absent on the server — expected).

8. **Push (only if the user asks):** into `Cummins_Parts_Book`.
   - Recreate/keep `.gitignore` with: `session/`, `*.log`, `*.output`,
     `__pycache__/`, `data/*/drawings/`, `data/*/parts/`, and the QuickServe
     secrets `quickserve/storage_state.json`, `quickserve/traffic*.jsonl`,
     `quickserve/status.txt`, `quickserve/after_login.*`,
     `quickserve/doc_manifest.json`, `quickserve/procedures.json`,
     `quickserve/chrome_profile/`.
   - `git fetch` first — the repo is edited from other sessions; fast-forward
     or rebase onto `origin/main` before pushing.
   - Stage explicitly (`git add bulletins/… quickserve/*.py .gitignore`), never
     `git add -A` (would pull in `session/` and engine data).
   - The set is ~2 GB → commit and **push in chunks** (bulletins first, then
     `procedures/` in 2–3 commits) to stay under GitHub's per-push limit.
     `git add` per-file in a loop is slow — stage a whole directory at once.

## Security (mandatory)

- Never commit `storage_state.json`, `traffic*.jsonl`, or any file containing
  the session cookie `IACSESSION`, the user's email, or the password.
- Keep credentials in env vars `QS_USER` / `QS_PWD`; the login scripts read them
  from the environment — do not hard-code.
- Before every push: `grep -rl 'IACSESSION\|<user-email>\|<password>'` over the
  staged files must return nothing. The rendered doc HTML is clean (verified),
  but the `manualviewer` shell leaks session/PII — never save that page.

## Scripts (in `quickserve/`)

`qs_login2.py` (login + save session), `qs_scope.py` (per-ESN bulletin counts),
`enum_service.py` (full library manifest), `enum_procedures.py` +
`add_procedures.py` (manual procedures), `download_docs.py` (render→PDF+HTML),
`qs_api.py` (raw API calls with the saved session). See memory
`cummins-parts-catalog` for the parts-catalog side of the project.

## Where this can run (verified 2026-08-19)

Run it on the user's own machine. In the Claude Code cloud sandbox the whole
workflow is blocked at step 1: the bundled Chromium has no outbound network at
all (`ERR_CONNECTION_RESET` on any external host, with or without the agent
proxy), so neither the QSOL login nor the render-to-PDF pass can start.
Plain HTTP clients (`curl`, `requests`, `urllib`) do reach the network through
the proxy — that is enough for static assets such as
`parts.cummins.com/graphics/parts/<nnn>/<esn>/<file>.png`, but not for QSOL
document pages, which return only the 1.3 KB shell without a browser.

The parts catalog API has the same constraint from the other side:
`parts.cummins.com/gateway/api/IACDataServices/engine/<ESN>` answers 403 to a
plain client. `GET /gateway/auth/csrf` does set an `XSRF-TOKEN` cookie, but the
call still fails with that token alone — a real browser session is required.
