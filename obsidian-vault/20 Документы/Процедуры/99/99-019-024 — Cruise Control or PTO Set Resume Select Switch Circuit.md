---
aliases:
  - "Цепь выключателя круиз-контроля или отбора мощности (Set/Resume)"
type: "Процедура"
doc: "99-019-024"
title_en: "Cruise Control or PTO Set/Resume Select Switch Circuit"
title_ru: "Цепь выключателя круиз-контроля или отбора мощности (Set/Resume)"
modified: "2015-06-25"
engines:
  - "41343322"
  - "41370103"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 10
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-024.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/99-019-024.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/99"
---

# Cruise Control or PTO Set/Resume Select Switch Circuit
**Цепь выключателя круиз-контроля или отбора мощности (Set/Resume)**

> [!abstract] Процедура · `99-019-024`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section 19 - Electronic Engine Controls
> **Даты:** изменён 2015-06-25
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-024.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/99-019-024.pdf)

### General Information

In addition to cruise control functions, the cruise control select switch also provides for increasing/decreasing idle speed, PTO speed, fault code flashout, and road speed governor limit.

![[19200292.png]]

### Resistance Check

> [!warning] CAUTION · Осторожно
> Proper leads and/or a Cummins® approved circuit testing tool must be used when working with electrical connectors to prevent pin expansion and damage to the connector.

If electronic service tool is available, monitor the cruise control/PTO set/resume select switch circuit for proper operation. If **not**, follow the troubleshooting procedures in this section.

![[19803969.png]]

Disconnect the original equipment manufacturer (OEM) harness engine interface connector. To determine the location of the connector, see the corresponding engine wiring diagram.

Insert a test lead into the cruise control/PTO set/coast switch signal of the OEM harness connector and connect the alligator clip to the multimeter probe.

Touch the other probe to engine block ground.

![[19c01182.png]]

Hold the cruise control select switch in the SET/COAST position. The multimeter **must** show a closed circuit (10 ohms or less) while holding the switch in the SET/COAST position and return to an open circuit (100k ohms or more) when the switch is released. The circuit **must** remain an open circuit (100k ohms or more) when the switch is in the RESUME/ACCEL position.

If the resistance values are **not** correct, make sure the cruise control/PTO set/coast input and the cruise control/PTO resume/accel input wires are properly installed on the cruise control select switch. If both control wires are correctly installed, inspect the cruise control/PTO set/coast input and the cruise control/PTO resume/accel wires for an open circuit, provided the cruise control select switch has been previously checked.

![[19c01183.png]]

Remove the lead from the cruise control/PTO set/coast switch signal and insert it into the cruise control/PTO resume/accel switch signal.

![[19c01184.png]]

Hold the cruise control select switch in the RESUME/ACCEL position. The multimeter **must** show a closed circuit (10 ohms or less) when the switch is in the RESUME/ACCEL position and an open circuit (100k ohms or more) when the switch is released.

The circuit **must** remain an open circuit (100k ohms or more) when the switch is held in the SET/COAST position.

![[19c01185.png]]

If the resistance values are **not** correct, make sure the cruise control/PTO resume/accel wire is properly installed on the cruise control select switch. If the cruise control/PTO resume/accel wire is properly installed on the cruise control select switch, inspect the cruise control/PTO resume/accel signal for an open circuit, provided the cruise control select switch has been previously checked.

If the resistance values are correct in the previous checks, the cruise control/PTO set/coast signal and cruise control/PTO resume/accel signal **must** still be checked for a short circuit to ground, a short circuit from pin to pin, and a short circuit to an external voltage source.

![[19c01185.png]]

### Check for Short Circuit from Pin to Pin

Isolate the cruise control/PTO set/resume select switch circuit as described in the previous section. Insert a test lead into the cruise control/PTO set/coast switch signal pin of the OEM harness connector. Insert the other lead into the first pin in the connector. Connect the alligator clips to the multimeter probes. Measure the resistance.

The multimeter **must** show an open circuit (100k ohms or more).

Remove the lead from the first pin in the connector and check all other pins. The multimeter **must** show an open circuit (100k ohms or more).

If the circuit is **not** open, there is a short circuit from the wire connected to the cruise control/PTO set/coast switch signal pin and any pin that measured less than 100k ohms.

Repair or replace the wires in the OEM harness. [[99-019-071 — OEM Wiring Harness|Refer to Procedure 019-071]].

Remove the lead from the cruise control/PTO set/coast signal pin and insert it into the cruise control/PTO resume/accel switch signal pin. Insert the other lead into the first pin in the connector.

Measure the resistance. The multimeter **must** show an open circuit (100k ohms or more).

![[19c01186.png]]

Remove the lead from the first pin in the connector and measure the resistance to all other pins. The multimeter **must** show an open circuit (100k ohms or more). If the circuit is **not** open, there is a short circuit between the wire connected to the cruise control/PTO resume/accel switch signal pin and any pin that measured less than 100k ohms.

Repair or replace the wires in the OEM harness. [[99-019-071 — OEM Wiring Harness|Refer to Procedure 019-071]].

![[19c01187.png]]

### Check for Short Circuit to External Voltage Source

Isolate the cruise control/PTO resume/accel switch circuit as described in the previous section. Turn the vehicle keyswitch to the ON position. Adjust the multimeter to measure VDC. Insert a test lead into the cruise control/PTO resume/accel switch signal of the OEM harness connector. Connect the test lead alligator clip to the positive (+) multimeter probe. Touch the negative (-) multimeter probe to the engine block ground and measure the voltage. The multimeter **must** show less than 1.5 VDC.

If the voltage value is **not** correct, there is an external voltage source short circuit to the cruise control/PTO set/coast switch signal in the OEM harness. Remove the voltage source. Repair or replace the wire in the OEM harness. [[99-019-071 — OEM Wiring Harness|Refer to Procedure 019-071]].

Remove the lead from the cruise control/PTO set/coast switch input pin and insert it into the cruise control/PTO resume/accel switch input pin. Touch the negative multimeter probe to the engine block ground and measure the voltage. The multimeter **must** show less than 1.5 VDC.

If the voltage value is **not** correct, there is an external voltage source short circuit to the cruise control/PTO resume/accel switch input pin in the OEM harness. Remove the voltage source. Repair or replace the wire in the OEM harness. [[99-019-071 — OEM Wiring Harness|Refer to Procedure 019-071]].

Connect all components after completing the repair.

![[19c01189.png]]
