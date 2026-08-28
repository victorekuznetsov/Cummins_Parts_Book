---
aliases:
  - "Цепь выключателя регулировки холостого хода"
type: "Процедура"
doc: "99-019-053"
title_en: "Idle Adjust Switch Circuit"
title_ru: "Цепь выключателя регулировки холостого хода"
modified: "2015-06-25"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
  - "37292556"
  - "37295879"
  - "41343322"
  - "41370103"
  - "85017333"
  - "93058669"
  - "93087701"
families:
  - "C8.3 · 6C8.3"
  - "NT/NTA855 · ISM/QSM11"
  - "QSK23"
  - "QSK60"
  - "QST30"
manuals:
  - "3666113"
  - "3666214"
  - "3666266"
  - "4021442"
figures: 6
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-053.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/99-019-053.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "двигатель/NT/NTA855"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "двигатель/QST30"
  - "группа/99"
---

# Idle Adjust Switch Circuit
**Цепь выключателя регулировки холостого хода**

> [!abstract] Процедура · `99-019-053`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]], [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]], [[85017333 — QSK23 CM500 CPL 2858|85017333]], [[93058669 — 6C8.3 CPL 3105|93058669]], [[93087701 — 6C8.3 CPL 3105|93087701]]
> **Семейство:** C8.3 · 6C8.3, NT/NTA855 · ISM/QSM11, QSK23, QSK60, QST30
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]], [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]], [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]], [[4021442 — C8.3 Marine Electronic Control System Troubleshooting and Repair Manual|4021442]]
> **Секции:** Section 19 - Electronic Engine Controls · Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2015-06-25
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-053.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/99-019-053.pdf)

### Resistance Check

> [!warning] CAUTION · Осторожно
> Proper leads and/or a Cummins® approved circuit testing tool must be used when working with electrical connectors to prevent pin expansion and damage to the connector.

> [!note] Note · Примечание
> The idle/diagnostic increment/decrement switch is the cruise control/PTO/set/resume select switch.

If electronic service tool is available, monitor the idle adjust switch circuit for proper operation. If **not,** follow the troubleshooting procedures in this section.

Disconnect the original equipment manufacturer (OEM) harness engine interface connector. To determine the location of the connector, see the corresponding engine wiring diagram.

Insert the pin of the test lead into the cruise control/PTO set/coast switch signal in the OEM harness connector. Measure the resistance from the cruise control/PTO set/coast switch signal to the engine block.

![[19c01166.png]]

Hold the idle adjust switch in the positive (+) increment position.

If the OEM connected the return wire to chassis ground the multimeter **must** show a closed circuit (10 ohms or less) while holding the switch on and return to an open circuit (100K ohms or more) when the switch is released. The circuit **must** remain an open circuit when the switch is in the decrement negative (-) position.

If the OEM connected the return wire to the ECM OEM connector the multimeter **must** show an open circuit (100k ohms or more) while holding the switch on and return to a closed circuit (10 ohms or less) when the switch is released. The circuit **must** remain a closed circuit when the switch is in the decrement negative (-) position.

If the resistance values are **not** correct, make sure the return wire and the cruise control/PTO set/coast switch signal wire are properly installed on the idle adjust switch. If both wires are correctly installed, inspect the return wire and the cruise control/PTO set/coast switch signal wire for open circuits, provided the idle adjust switch has been previously checked for short circuits to ground.

![[19c01245.png]]

Remove the lead from the cruise control/PTO set/coast switch signal and insert it into the cruise control/PTO resume/accelerator switch signal.

Hold the idle adjust switch in the negative (-) decrement position. The multimeter **must** show a closed circuit (10 ohms or less) when the switch is held in the decrement position and an open circuit (100K ohms or more) when the switch is released. The circuit **must** remain an open circuit when the switch is in the positive (+) increment position.

If the resistance values are **not** correct, make sure the cruise control/PTO resume/accelerator switch signal wire is properly installed on the idle adjust switch. If the cruise control/PTO resume/accelerator switch signal wire is properly installed on the idle adjust switch, inspect the cruise control/PTO resume/accelerator switch signal wire for an open circuit, provided the idle adjust switch has been previously checked for short circuits to ground.

![[19c01246.png]]

### Check for Short Circuit to Ground

Disconnect the idle/diagnostic decrement wire (attached to the cruise control/PTO resume/ accelerator switch signal) from the switch.

Measure the resistance from the cruise control/PTO resume/accelerator switch signal of the OEM harness connector to the engine block.

![[19c01247.png]]

The multimeter **must** show an open circuit (100K ohms or more). If the circuit is **not** open, there is a short circuit to ground in the cruise control/PTO resume/accelerator switch signal circuit, provided the idle adjust switch has been previously checked.

Repair or replace the wire connected to the cruise control/PTO resume/accelerator switch signal in the OEM harness according to the vehicle manufacturer's instructions.

To check the idle/diagnostic increment wire (attached the to cruise control/PTO set/coast switch signal) for short circuits to ground, follow the same procedure as described above for the idle/diagnostic decrement wire.

![[19c01248.png]]

### Check for Short Circuit from Pin to Pin

Measure the resistance from the cruise control/PTO resume/accelerator switch signal of the OEM harness connector to all other pins in the connector. The multimeter **must** show an open circuit (100k ohms or more).

If the circuit is **not** open, there is a short circuit between the wire connected to the cruise control/PTO resume/accelerator switch signal and any pin that measured less than 100k ohms.

Repair or replace the wires in the OEM harness according to the vehicle manufacturer's instructions.

Remove the lead from the cruise control/PTO resume/accelerator switch signal of the OEM harness connector and insert it into the cruise control/PTO set/coast switch signal of the connector. Measure the resistance from the cruise control/PTO set/coast switch signal to all other pins in the connector. The multimeter **must** show an open circuit (100k ohms or more).

If the circuit is **not** open, there is a short circuit between the wire connected to the cruise control/PTO set/coast switch signal and any pin that measured less than 100k ohms, provided the idle adjust switch has been previously checked.

Repair or replace the wires in the OEM harness according to the vehicle manufacturer's instructions.

Connect all components after completing the repair.

![[19c01249.png]]
