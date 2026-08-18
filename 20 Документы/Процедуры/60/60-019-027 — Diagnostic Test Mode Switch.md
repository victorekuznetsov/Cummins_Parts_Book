---
aliases:
  - "Переключатель режима диагностики"
type: "Процедура"
doc: "60-019-027"
title_en: "Diagnostic Test Mode Switch"
title_ru: "Переключатель режима диагностики"
modified: "2007-12-14"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021674"
figures: 6
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-019-027.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-019-027.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
---

# Diagnostic Test Mode Switch
**Переключатель режима диагностики**

> [!abstract] Процедура · `60-019-027`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section 19 — Electronic Engine Controls — Group 19
> **Даты:** изменён 2007-12-14
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-019-027.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-019-027.pdf)

### General Information

> [!note] Note · Примечание
> Some OEMs use a shorting plug rather than a switch.

The diagnostic ON/OFF switch circuit signals the system that the operator is requesting to read any active fault code recorded in the ECM.

![[gp8swvs.png]]

When the ECM receives the signal from the diagnostic ON/OFF switch, the yellow and red warning lights will come on and start flashing if any active fault code is recorded in the ECM. If both warning lights remain on and do **not** flash, there are no active fault codes present.

![[19400239.png]]

### Resistance Check

If INSITE™ electronic service tool is available, monitor the switch for proper operation. If **not**, follow the troubleshooting procedures in this manual.

Locate the desired ON/OFF toggle switch. Remove and tag the two connectors from the terminals on the switch.

Touch the multimeter probes to the terminals on the switch.

![[19900590.png]]

Move the switch to the OFF position and measure the resistance. The multimeter **must** show an open circuit (100k ohms or more).

If the circuit is **not** open, the switch has failed.

Refer to the OEM troubleshooting and repair manual for the replacement procedure.

![[19900591.png]]

Move the switch to the ON position and measure the resistance. The multimeter **must** show a closed circuit (10 ohms or less). If the circuit is **not** closed, the switch has failed.

Refer to the OEM troubleshooting and repair manual for the replacement procedure.

If the resistance value is correct, the switch **must** still be checked for a short circuit to ground.

![[wr8swkd.png]]

### Check for Short Circuit to Ground

Touch one of the multimeter probes to one of the switch terminals. Touch the other probe to chassis ground. Move the switch to the ON position and measure the resistance. The multimeter **must** show an open circuit (100k ohms or more). If the circuit is **not** open, the switch has failed. Refer to the OEM troubleshooting and repair manual for the replacement procedure. If the switch passes all of the previous checks, the circuit **must** be checked for an open circuit, a short circuit to ground, a short circuit from pin to pin, and a short circuit to an external voltage source. Refer to Procedure 019-028 (Diagnostic Test Mode Switch Circuit) in Section 19.

![[19c01165.png]]
