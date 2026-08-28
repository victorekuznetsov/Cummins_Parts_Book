---
aliases:
  - "Выключатель ступени моторного тормоза"
type: "Процедура"
doc: "82-019-036"
title_en: "Engine Brake Level Switch"
title_ru: "Выключатель ступени моторного тормоза"
modified: "2002-06-03"
engines:
  - "41343322"
  - "41370103"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 7
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-036.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-019-036.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# Engine Brake Level Switch
**Выключатель ступени моторного тормоза**

> [!abstract] Процедура · `82-019-036`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section 19 - Electronic Engine Controls
> **Даты:** изменён 2002-06-03
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-036.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-019-036.pdf)

### General Information

The engine brake SELECTOR switch determines which engine brake should be activated. The engine brake ON/OFF switch needs to be turned ON to activate the engine brake system.

![[19200290.png]]

### Resistance Check

If INSITE™ is available, monitor the engine brake selector switch for proper operation. If **not**, follow the troubleshooting procedures for this section.

Label the wires with the location on the switch or the wire number. Disconnect the three electrical connectors from the switch.

![[19200297.png]]

Adjust the multimeter to measure resistance.

Touch one multimeter probe to the center terminal of the switch. Touch the other multimeter probe to the top terminal of the switch and then to the bottom terminal of the switch in each of the following steps.

![[19200298.png]]

Move the brake selector switch to the No. 1 position. The multimeter **must** show a closed circuit on one terminal, at either the top terminal or the bottom terminal (10 ohms or less) when the switch is in the No. 1 position. If the circuit is **not** closed or if both the top and the bottom terminals show continuity, the switch has failed.

Refer to the OEM troubleshooting and repair manual for replacement procedures.

![[19200298.png]]

Touch the probe to the top terminal again. Move the brake selector switch to the No. 2 position. The multimeter **must** show an open circuit (100k ohms or more) when the switch is in the No. 2 position.

Move the probe to the bottom terminal. The multimeter **must** show an open circuit (100k ohms or more). If the multimeter does **not** show the correct values in both tests, the switch has failed. Refer to the OEM troubleshooting and repair manual for replacement procedures.

![[19200299.png]]

### Check for Short Circuit to Ground

Adjust the multimeter to measure resistance.

Touch one multimeter probe to the top terminal of the switch. Touch the other multimeter probe to the chassis ground. Move the switch to the No. 1 position, then to the No. 2 position. Measure the resistance. The multimeter **must** show an open circuit (100k ohms or more) when the switch is in all positions. If the circuit is **not** open, the switch has failed.

Refer to the OEM troubleshooting and repair manual for replacement procedures.

![[19200300.png]]

Touch one multimeter probe to the bottom terminal of the switch. Touch the other multimeter probe to chassis ground. Move the switch to the No. 2 position, then to the No. 1 position. Measure the resistance. The multimeter **must** show an open circuit (100k ohms or more) when the switch is in all positions. If the circuit is **not** open, the switch has failed.

Refer to the OEM troubleshooting and repair manual for replacement procedures.

![[19200301.png]]
