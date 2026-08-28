---
aliases:
  - "QST30 работает только на одном ряду, активен код 166"
type: "TSB"
doc: "tsb101121"
title_en: "QST30 Only Runs on One Bank and Fault Code 166 is Active."
title_ru: "QST30 работает только на одном ряду, активен код 166"
released: "2011-01-06"
modified: "2011-01-06"
group: "19 - Electronic Engine Controls"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
figures: 4
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2010/tsb101121.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb101121.pdf"
tags:
  - "документ/tsb"
  - "двигатель/QST30"
  - "год/2011"
  - "тема/electronic-engine-controls"
---

# QST30 Only Runs on One Bank and Fault Code 166 is Active.
**QST30 работает только на одном ряду, активен код 166**

> [!abstract] TSB · `tsb101121`
> **Раздел Cummins:** 19 - Electronic Engine Controls
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Даты:** выпущен 2011-01-06 · изменён 2011-01-06
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2010/tsb101121.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb101121.pdf)

## QST30 Only Runs on One Bank and Fault Code 166 is Active.

### Warranty Statement

The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.

### Contents

Issue:

When starting a QST30 engine it will activate fault 166 and **only** run on one bank if a voltage spike from the CM552 ECM is detected. When this occurs, the engine commonly runs on the right bank **only**.

Verification / Confirmation:

Confirm that Fault Code 166 is active and that the engine is **only** running on one bank.

Resolution:

A resistor has been added to the left bank engine wiring harness to prevent Fault Code 166 from becoming active and the engine from running on one bank if a voltage spike from the CM552 ECM occurs.

Check to see if there is a resistor installed between the rack position common wire and ground on the bank that is **not** firing. See the attached figures for resistor locations. If a resistor is **not** found, install a resistor in the wiring harness or replace the wiring harness. Refer to the wiring diagram for the pin location identification. If a resistor is found, check the resistance.

- For power generation applications, use the following procedure in the QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooting and Repair Manual, Bulletin [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti\|4021674]]. [[60-019-043 — Engine Wiring Harness|Refer to Procedure 019-043 in Section 19.]]
- For industrial applications, use the following procedure in the QST30 Industrial Electronic Control System Troubleshooting and Repair Manual, Bulletin [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual\|3666214]] for resistance check instructions. [[87-019-043 — Engine Wiring Harness|Refer to Procedure 019-043 in Section 19.]]

The tables below summarize changes to the engine wiring harness:

| **QST30 CM552 Industrial One-Piece Harness Engines** | **Part Number** | **ESN First or Plant Implementation Date** |
|---|---|---|
| One 2.2k Ohm Resistor (right bank **only**) | 4975508 | 3-August-2009 |
| Two 2.2k Ohm Resistors | 4975755 | 37247268 |

| **QST30 CM850 Power Generation Interface Engines** | **Part Number** | **ESN First or Plant Implementation Date** |
|---|---|---|
| One 2.2k Ohm Resistor (right bank **only**) | 4975505 | 25-May-2009 |
| Two 2.2k Ohm Resistors with 12 Volt Fuel Pump Relay | 2881121 | 13-December-2009 |
| Two 2.2k Ohm Resistors with 24 Volt Fuel Pump Relay | 4975747 | 37245679 |
| Two 1.3k Ohm Resistors with 24 Volt Fuel Pump Relay | 4975760 | 37246974 |

![[19f00008.png]]

![[19f00009.png]]

![[19f00006.png]]

![[19f00007.png]]

Figure 1: Resistor Location for QST30 Industrial Left Bank

Figure 2: Resistor Location for QST30 Industrial Right Bank

Figure 3: Resistor Location for QST30 Power Generation Interface Left Bank

Figure 4: Resistor Location for QST30 Power Generation Interface Right Bank

### Document History
