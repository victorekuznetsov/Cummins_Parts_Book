---
aliases:
  - "Цепь переключателя режима диагностики"
type: "Процедура"
doc: "99-019-028"
title_en: "Diagnostic Test Mode Switch Circuit"
title_ru: "Цепь переключателя режима диагностики"
modified: "2015-06-25"
engines:
  - "37292556"
  - "37295879"
  - "41343322"
  - "93058669"
families:
  - "C8.3 · 6C8.3"
  - "NT/NTA855 · ISM/QSM11"
  - "QST30"
manuals:
  - "3666214"
  - "3666266"
  - "4021419"
  - "4021442"
  - "4021674"
figures: 7
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-028.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/99-019-028.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "двигатель/NT/NTA855"
  - "двигатель/QST30"
  - "группа/99"
---

# Diagnostic Test Mode Switch Circuit
**Цепь переключателя режима диагностики**

> [!abstract] Процедура · `99-019-028`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]], [[41343322 — NH NT 855 CPL 3362|41343322]], [[93058669 — 6C8.3 CPL 3105|93058669]]
> **Семейство:** C8.3 · 6C8.3, NT/NTA855 · ISM/QSM11, QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]], [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]], [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]], [[4021442 — C8.3 Marine Electronic Control System Troubleshooting and Repair Manual|4021442]], [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section 19 - Electronic Engine Controls · Section 19 - Electronic Engine Controls - Group 19 · Section 19 — Electronic Engine Controls — Group 19
> **Даты:** изменён 2015-06-25
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-028.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/99-019-028.pdf)

### Resistance Check

> [!warning] CAUTION · Осторожно
> Proper leads and/or a Cummins® approved circuit testing tool must be used when working with electrical connectors to prevent pin expansion and damage to the connector.

If electronic service tool is available, monitor the switch circuit for proper operation. If **not**, follow the troubleshooting procedures in this section.

![[19803969.png]]

Disconnect the original equipment manufacturer (OEM) harness engine interface connector. To determine the location of the connector, see the corresponding engine wiring diagram. Insert the test lead into the diagnostic test mode switch signal pin in the OEM harness connector and connect it to the multimeter probe.

Touch the other probe to the engine block or chassis ground.

Move the ON/OFF switch to the ON position.

If the OEM wired the switch return to chassis ground, the multimeter **must** show a closed circuit (10 ohms or less). If the circuit is **not** closed, inspect the diagnostic test mode switch signal wire for an open circuit.

If the OEM wired the switch return to the OEM wire harness, the multimeter **must** show an open circuit (100k ohms or more). If the circuit is **not** open, inspect the diagnostic test mode switch signal wire for a closed circuit.

Refer to the OEM troubleshooting and repair manual.

If the resistance is within specification, the diagnostic test mode switch signal wire **must** be checked for a short circuit to ground, a short circuit from terminal to terminal, and a short circuit to an external voltage source.

![[19c01167.png]]

### Check for Short Circuit to Ground

To isolate the diagnostic test mode switch signal circuit when checking for an electrical short, turn all cab panel switches to the OFF or neutral position.

Set the service brake using the trailer brake hand valve.

Disconnect the clutch pedal position switch.

Disconnect the idle validation switch.

> [!note] Note · Примечание
> Some equipment may vary, depending on OEM application.

![[ee8swsb.png]]

Disconnect the OEM harness connector from the electronic control unit. Set the diagnostic test mode switch to the OFF position.

Insert one of the test leads into the diagnostic test mode switch signal pin of the OEM harness connector and connect it to a multimeter probe.

Touch the other probe to engine block or chassis ground.

The multimeter **must** show an open circuit (100k ohms or more).

![[19c01211.png]]

### Check for Short Circuit from Pin to Pin

Check for a short circuit from pin-to-pin. Isolate the switch circuit by setting the cab panel switches as described in the previous section. Set the diagnostic test mode switch to the OFF position. Insert a test lead into the switch return pin of the OEM harness connector and connect it to the multimeter probe. With the other lead inserted into the diagnostic test mode switch signal pin of the connector, measure the resistance. The multimeter **must** show an open circuit (100k ohms or more).

![[19c01168.png]]

Remove the lead from the switch return and test all pins in the connector. Measure the resistance. The multimeter **must** show an open circuit (100k ohms or more).

If the circuit is **not** open, there is a short circuit between the switch circuit and any pin that shows a closed circuit, provided the switch has previously been checked. Repair or replace the wires in the OEM harness. [[99-019-071 — OEM Wiring Harness|Refer to Procedure 019-071]].

![[19c01215.png]]

### Check for Short Circuit to External Voltage Source

Turn the vehicle keyswitch to the ON position. Set the diagnostic test mode switch to ON. Adjust the multimeter to measure VDC. Insert a test lead into the diagnostic test mode switch signal pin of the OEM harness connector. Touch the other lead to the engine block or chassis ground. Measure the voltage. The voltage **must** be 1.5 VDC or less.

If the voltage is **not** correct, there is an external voltage source connected to the circuit or there is a short circuit between the switch circuit and a wire carrying power in the OEM harness. Remove the voltage source or repair the wiring in the OEM harness. [[99-019-071 — OEM Wiring Harness|Refer to Procedure 019-071]].

Connect all components after completing the repair.

![[19c01216.png]]
