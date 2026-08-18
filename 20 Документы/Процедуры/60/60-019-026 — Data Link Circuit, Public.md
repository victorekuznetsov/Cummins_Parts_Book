---
aliases:
  - "Цепь общедоступной шины данных"
type: "Процедура"
doc: "60-019-026"
title_en: "Data Link Circuit, Public"
title_ru: "Цепь общедоступной шины данных"
modified: "2008-07-09"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021674"
figures: 5
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-019-026.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-019-026.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
---

# Data Link Circuit, Public
**Цепь общедоступной шины данных**

> [!abstract] Процедура · `60-019-026`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section 19 — Electronic Engine Controls — Group 19
> **Даты:** изменён 2008-07-09
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-019-026.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-019-026.pdf)

### General Information

The SAE J1939 public data link circuit is used for INSITE™ electronic service tool to communicate with the ECM.

![[19800902.png]]

The SAE J1939 datalink uses a 9-pin Deutsch™ connector. The wiring positions follow:

Position A - Battery Return (ECM3)

Position B - Battery 1 Voltage Supply

Position C - SAE J1939 Data Link Supply

Position D - SAE J1939 Data Link Return

Position E - SAE J1939 Data Link Shield

Position F - Not used.

Position G - Not used.

Position H - Not used.

Position J - Not used.

![[19a00898.png]]

### Resistance Check

Remove the ECM1 50-pin connector.

Use test lead, Part Number 3822758, on the ECM connector; and use test lead, Part Number 3824812, on the 9-pin Deutsch™ connector.

Turn the Run/Stop switch to the Stop position.

Measure the resistance from the battery voltage 1 return wire of the SAE J1939 data link connector to the corresponding pin on the ECM connector.

Repeat the step for the remaining pins in the SAE J1939 data link connector.

If a resistance measurement is greater than 10 ohms on any pin set, replace the wiring harness. [[60-019-043 — Engine Wiring Harness|Refer to Procedure 019-043 (Engine Wiring Harness) in Section 19.]]

![[19a00884.png]]

### Check for Short Circuit to Ground

Remove the ECM 1 50-pin connector.

Use test lead, Part Number 3824811, for the SAE J1939 data link connector.

Measure the resistance from the battery 1 voltage supply wire of the SAE J1939 data link connector to the engine block.

Repeat the step for all of the remaining pins, except the battery 1 voltage return pin in the SAE J1939 data link connector.

If a resistance measurement is **not** greater than 100k ohms, replace the wiring harness. [[60-019-043 — Engine Wiring Harness|Refer to Procedure 019-043 (Engine Wiring Harness) in Section 19.]]

![[19802484.png]]

### Check for Short Circuit from Pin to Pin

Remove the ECM1 50-pin connector.

Use test lead, Part Number 3824811, for the SAE J1939 data link connector. Measure the resistance from the battery 1 voltage return pin to all other pins in the SAE J1939 data link connector.

Repeat the step for all of the remaining pins in the SAE J1939 data link connector.

If a resistance measurement is **not** greater than 100k ohms, replace the wiring harness. [[60-019-043 — Engine Wiring Harness|Refer to Procedure 019-043 (Engine Wiring Harness) in Section 19.]]

![[19802485.png]]
