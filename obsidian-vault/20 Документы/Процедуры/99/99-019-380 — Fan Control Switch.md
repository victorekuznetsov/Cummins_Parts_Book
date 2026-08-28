---
aliases:
  - "Выключатель управления вентилятором"
type: "Процедура"
doc: "99-019-380"
title_en: "Fan Control Switch"
title_ru: "Выключатель управления вентилятором"
modified: "2015-06-29"
engines:
  - "41343322"
  - "41370103"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 5
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-380.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/99-019-380.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/99"
---

# Fan Control Switch
**Выключатель управления вентилятором**

> [!abstract] Процедура · `99-019-380`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section 19 - Electronic Engine Controls
> **Даты:** изменён 2015-06-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-380.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/99-019-380.pdf)

### General Information

The fan control switch circuit signals the system that the operator is requesting the engine fan to be engaged. The fan on and off circuit consists of the fan control switch signal, the switch return, and the OEM cab-mounted toggle switch. This circuit is considered “fail safe”, meaning when the circuit is open, the engine fan will be engaged by the ECM.

> [!note] Note · Примечание
> This procedure is **only** valid if the fan control switch is wired through the ECM and the feature manual fan switch is enabled in the ECM. If the fan control switch is wired in series with the fan control relay, the ECM could log fan circuit errors during normal operation. Please verify the circuit is wired properly before performing this procedure.

![[eb800vh.png]]

### Resistance Check

If an electronic service tool is available, monitor the fan control switch for proper operation. If **not** operating properly, follow the troubleshooting procedures in this section.

![[19c01217.png]]

Locate the fan control switch. Label the wires with the location of the switch or the wire number. Remove the electrical connectors from the switch. Adjust the multimeter to measure resistance. Touch one multimeter probe to one of the terminals on the switch. Touch the other multimeter probe to the other terminal of the switch.

Move the switch to the ON position and measure the resistance. The multimeter **must** show an open circuit (100k ohms or more). If the circuit is **not** open, the switch has failed. Refer to the OEM troubleshooting and repair manual for replacement procedures.

![[19c01163.png]]

Place the switch in the OFF position and measure the resistance. The multimeter **must** show a closed circuit (10 ohms or less). If the circuit is **not** closed, the switch has failed. Refer to the OEM troubleshooting and repair manual for replacement procedures. If the resistance value is correct, the switch **must** still be checked for a short circuit to ground.

![[19c01164.png]]

### Check for Short Circuit to Ground

Touch one of the multimeter probes to one of the switch terminals. Touch the other probe to chassis ground. Move the switch to the OFF position and measure the resistance. The multimeter **must** show an open circuit (100k ohms or more). If the circuit is **not** open, the switch has failed. Refer to the OEM troubleshooting and repair manual for replacement procedures. If the switch passes all of the previous checks, the circuit **must** be checked for an open circuit, a short circuit to ground, a short circuit from pin to pin, and a short circuit to an external voltage source.

![[19c01165.png]]
