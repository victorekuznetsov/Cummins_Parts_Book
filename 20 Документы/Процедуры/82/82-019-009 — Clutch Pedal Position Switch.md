---
aliases:
  - "Выключатель положения педали сцепления"
type: "Процедура"
doc: "82-019-009"
title_en: "Clutch Pedal Position Switch"
title_ru: "Выключатель положения педали сцепления"
modified: "2003-10-09"
engines:
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 7
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-009.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-019-009.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# Clutch Pedal Position Switch
**Выключатель положения педали сцепления**

> [!abstract] Процедура · `82-019-009`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section 19 - Electronic Engine Controls
> **Даты:** изменён 2003-10-09
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-009.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-019-009.pdf)

### General Information

The clutch switch circuit is used to disable the PTO and cruise control features.

The circuit is a normally closed control switch, wire 2 (clutch switch input), and a common ground. When the clutch switch is installed and adjusted, the contact points are held closed. When the clutch pedal is depressed, the clutch switch is in its normally closed position. This will disable the PTO or cruise control operation.

![[19c00202.png]]

### Resistance Check

If INSITE™ is available, monitor the clutch switch for proper operation. If **not**, follow the troubleshooting procedures in this section.

Find the clutch switch. The location will depend on the OEM installation procedures.

Separate the wire connector.

Adjust the multimeter to measure resistance.

Touch the probes of the multimeter to the two terminals in the connector.

![[cl8swka.png]]

Engage the clutch (clutch pedal released). The multimeter **must** show a closed circuit (10 ohms or less).

If the switch is **not** closed when the clutch is fully engaged, adjust the clutch switch trip lever.

![[cl8swkb.png]]

Depress the clutch pedal. The clutch switch **must** open. The multimeter **must** show an open circuit (100k ohms or more).

If the switch is **not** open when the clutch is fully engaged, adjust the clutch switch trip lever.

![[cl8swke.png]]

### Check for Short Circuit to Ground

Remove one multimeter probe from the connector and touch the probe to the chassis ground. The multimeter **must** show an open circuit (100k ohms or more) when the clutch pedal is depressed. If the circuit is closed, replace the clutch switch. Refer to the OEM troubleshooting and repair manual.

If the clutch switch passed all previous checks, connect the switch to the wiring harness. The clutch switch circuit **must** be checked.

![[cl8swkf.png]]

### Check for Short Circuit to External Voltage Source

Turn the vehicle keyswitch to the ON position.

Adjust the multimeter to measure VDC.

Insert one of the multimeter probes into the clutch switch connector.

Touch the other multimeter probe to the engine block ground and measure the voltage. The voltage **must** be 1.5 VDC or less with the clutch pedal released and depressed.

![[19c00879.png]]

If the voltage value is more than 1.5 VDC, there is a short circuit to an external voltage source.

> [!note] Note · Примечание
> An external voltage source is any wire in the OEM harness wiring that carries the voltage.

Remove the external voltage source.

If the clutch switch passed all previous checks, connect the switch to the wiring harness. The clutch switch circuit **must** be checked.

![[19c00724.png]]
