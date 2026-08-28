---
aliases:
  - "Двигатель не реагирует на команду останова"
type: "Процедура"
doc: "115-t02-1029"
title_en: "Engine Does Not Respond to Engine Stop"
title_ru: "Двигатель не реагирует на команду останова"
modified: "2006-06-12"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4021587"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/115/115-t02-1029.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/115-t02-1029.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/115"
---

# Engine Does Not Respond to Engine Stop
**Двигатель не реагирует на команду останова**

> [!abstract] Процедура · `115-t02-1029`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021587 — C Command Panel System Marine Master Repair Manual|4021587]]
> **Секции:** Section TT — Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2006-06-12
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/115/115-t02-1029.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/115-t02-1029.pdf)

Printable Version

### Symptoms

- The engine will **not** stop when the engine stop button is engaged at the customer interface box.

### How To Use This Tree

This symptom tree can be used to troubleshoot engine stop symptoms. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.

### Shoptalk

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check Customer Interface Box |  |
|  | **STEP 1A.** Check Engine Stop Switch | Less than 10 ohms resistance? |

### STEP 1. Check Customer Interface Box

#### STEP 1A. Check Engine Stop Switch

| **Conditions:** Open customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check engine stop switch. Disconnect the four ignition (engine stop) wires from the button. Place a test lead on each side of one contact of the button. Push the engine stop button. Repeat for the other contact of the button. | Less than 10 ohms resistance? **YESRepair:** Replace the engine stop button. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |
| Less than 10 ohms resistance? **NORepair:** Refer to Section TF in the Troubleshooting and Repair Manual, Electronic Control System, QSK19 CM850, Modular Common Rail System, Series Engines, Bulletin 4021493. | Repair complete. |  |
