---
aliases:
  - "Выключатель круиз-контроля или отбора мощности (Set/Resume)"
type: "Процедура"
doc: "82-019-023"
title_en: "Cruise Control or PTO Set/Resume Select Switch"
title_ru: "Выключатель круиз-контроля или отбора мощности (Set/Resume)"
modified: "2003-10-09"
engines:
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 15
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-023.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-019-023.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# Cruise Control or PTO Set/Resume Select Switch
**Выключатель круиз-контроля или отбора мощности (Set/Resume)**

> [!abstract] Процедура · `82-019-023`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section 19 - Electronic Engine Controls
> **Даты:** изменён 2003-10-09
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-023.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-019-023.pdf)

### General Information

The cruise control select switch has two positions: SET/COAST and RESUME/ACCELERATE.

The switch can be used for:

- CRUISE CONTROL: SET/ACCEL and RESUME/COAST
- PTO: INCREMENT/DECREMENT
- IDLE: INCREMENT/DECREMENT
- ROAD SPEED GOVERNOR: INCREMENT/DECREMENT
- DIAGNOSTIC FAULT CODE: INCREMENT/DECREMENT

For additional information, see Section F.

![[gp8swgh.png]]

The operator can set the vehicle cruising speed when the switch is in the SET/COAST position. The SET/COAST position can also be used to reduce the vehicle cruising speed. Hold the switch in the SET/COAST position and the vehicle will coast down to a lower speed. When the select switch is released, the cruising speed will be reset.

> [!note] Note · Примечание
> Some OEMs have switches labeled SET/ACCEL and RESUME/COAST.

![[gp8swgh.png]]

The operator can resume cruise control, after clutching or braking, by moving the switch to RESUME/ACCELERATE. The vehicle speed will return to the last set mph.

The RESUME/ACCELERATE position can also be used to increase the vehicle cruising speed. Hold the select switch in the RESUME/ACCELERATE position and the vehicle will increase in speed. When the switch is released, the cruising speed will be reset.

![[gp8swgk.png]]

The cruise control select switch circuit is the common ground, pin 14 (SET/COAST signal), pin 24 (RESUME/ACCELERATE signal), and the two-position select switch located in the vehicle.

![[19c00179.png]]

### Resistance Check

If INSITE™ is available, monitor the cruise control select switch for proper operation. If **not**, follow the troubleshooting procedures in this section.

Label the wires with the location on the switch or the wire number. Remove the three electrical connectors from the switch.

![[19c00180.png]]

Adjust the multimeter to measure resistance.

Touch one multimeter probe to the center terminal of the switch.

Touch the other multimeter probe to the top terminal of the switch.

![[ee8swkh.png]]

Hold the switch in the SET/COAST position. The multimeter **must** show an open circuit (100k ohms or more) when the switch is held in the SET/COAST position and after it is released. If the circuit is **not** open, the switch has failed. Refer to the OEM troubleshooting and repair manual for replacement procedures.

![[19900504.png]]

Hold the switch in the RESUME/ACCELERATE position. The multimeter **must** show a closed circuit (10 ohms or less) when the switch is held in the RESUME/ACCELERATE position.

![[ee8swkj.png]]

When the switch is released, the multimeter **must** show an open circuit (100k ohms or more). If the multimeter does **not** show the correct values in either test, the switch has failed. Refer to the OEM troubleshooting and repair manual for replacement procedures.

If the resistance value is correct, the switch **must** still be checked for a short circuit to ground.

![[ee8swkk.png]]

Touch one multimeter probe to the center terminal of the switch. Touch the other multimeter probe to the bottom terminal of the switch.

![[wr8swkb.png]]

Hold the switch in the SET/COAST position. The multimeter **must** show a closed circuit (10 ohms or less) while the switch is held on to the SET/COAST position.

![[wr8swkb.png]]

When the switch is released, the multimeter **must** show an open circuit (100k ohms or more). If the multimeter does **not** show the correct values in either test, the switch has failed. Refer to the OEM troubleshooting and repair manual for replacement procedures.

![[ee8swko.png]]

Move the switch to the RESUME/ACCELERATE position. The multimeter **must** show an open circuit (100k ohms or more) when the switch is held on and when it is released. If the circuit is **not** open, the switch has failed. Refer to the OEM troubleshooting and repair manual for replacement procedures.

![[ee8swkp.png]]

### Check for Short Circuit to Ground

Adjust the multimeter to measure resistance.

Touch one multimeter probe to the top terminal of the switch. Touch the other multimeter probe to the chassis ground. Move the switch to the SET/COAST position then to the RESUME/ACCELERATE position. Measure the resistance. The multimeter **must** show an open circuit (100k ohms or more) when the switch is in all positions. If the circuit is **not** open, the switch has failed. Refer to the OEM troubleshooting and repair manual for replacement procedures.

> [!missing]- Иллюстрация `ee8swkl.png` не извлечена — смотрите PDF-оригинал документа

Touch one multimeter probe to the bottom terminal of the switch. Touch the other multimeter probe to chassis ground. Move the switch to the RESUME/ACCELERATE position, then to the SET/COAST position. Measure the resistance. The multimeter **must** show an open circuit (100k ohms or more) when the switch is in all positions. If the circuit is **not** open, the switch has failed. Refer to the OEM troubleshooting and repair manual for replacement procedures.

> [!missing]- Иллюстрация `ee8swkq.png` не извлечена — смотрите PDF-оригинал документа
