---
aliases:
  - "Переключатель режима диагностики"
type: "Процедура"
doc: "82-019-027"
title_en: "Diagnostic Test Mode Switch"
title_ru: "Переключатель режима диагностики"
modified: "2003-10-09"
engines:
  - "41343322"
  - "41370103"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 6
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-027.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-019-027.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# Diagnostic Test Mode Switch
**Переключатель режима диагностики**

> [!abstract] Процедура · `82-019-027`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section 19 - Electronic Engine Controls
> **Даты:** изменён 2003-10-09
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-027.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-019-027.pdf)

### General Information

> [!warning] CAUTION · Осторожно
> The diagnostic switch must remain in the OFF position (shorting plug removed) while the engine is being operated in order for all fault codes to be logged.

The diagnostic on/off switch circuit signals the system that the operator is requesting to read any active fault code recorded in the ECM.

> [!note] Note · Примечание
> Some OEMs use a shorting plug rather than a switch.

![[gp8swvs.png]]

When the ECM receives the signal from the diagnostic on/off switch, the yellow and red warning lights will come on and start flashing if any active fault code is recorded in the ECM. If both warning lights remain on and do **not** flash, there are no active fault codes present.

> [!note] Note · Примечание
> The equipment **must** be stationary. If road speed is detected, the flashing sequence will **not** occur.

The cruise control selector switch is used to step through the fault codes being flashed out. Each fault code will continue to flash until the cruise control selector switch is used.

![[19400239.png]]

### Resistance Check

If INSITE™ is available, monitor the switch for proper operation. If **not**, follow the troubleshooting procedures in this section.

Locate the desired on/off toggle switch. Remove and tag the two connectors from the switch terminals. Touch the multimeter probes to the terminals on the switch.

![[19900590.png]]

Move the switch to the OFF position and measure the resistance. The multimeter **must** show an open circuit (100k ohms or more). If the circuit is **not** open, the switch has failed.

Refer to the OEM troubleshooting and repair manual for the replacement instructions.

![[19900591.png]]

Move the switch to the ON position and measure the resistance. The multimeter **must** show a closed circuit (10 ohms or less). If the circuit is **not** closed, the switch has failed. Refer to the OEM troubleshooting and repair manual for the replacement procedures.

If the resistance value is correct, the switch **must** still be checked for a short circuit to ground.

![[wr8swkd.png]]

### Check for Short Circuit to Ground

Touch one of the multimeter probes to one of the switch terminals. Touch the other probe to chassis ground. Move the switch to the ON position and measure the resistance. The multimeter **must** show an open circuit (100k ohms or more). If the circuit is **not** open, the switch has failed. Refer to the OEM troubleshooting and repair manual for replacement procedures. If the switch passes all of the previous checks, the circuit **must** be checked for an open circuit, a short circuit to ground, a short circuit from pin to pin, and a short circuit to an external voltage source.

![[19900592.png]]
