---
type: "Процедура"
doc: "35-008-028-tr"
title_en: "Fan Clutch, Viscous"
modified: "2009-01-23"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "3666322"
figures: 16
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/35/35-008-028-tr.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/35-008-028-tr.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/35"
---

# Fan Clutch, Viscous

> [!abstract] Процедура · `35-008-028-tr`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[3666322 — ISM, ISMe, and QSM11 Service Manual|3666322]]
> **Секции:** Section 8 - Cooling System - Group 08
> **Даты:** изменён 2009-01-23
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/35/35-008-028-tr.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/35-008-028-tr.pdf)

### General Information

The fan clutches can be controlled by the electronic control module (ECM). The ECM is programmed to turn the fan on when 0-VDC (normally open switch) is applied to the fan clutch relay, and turn the fan off when 12-VDC (normally closed switch) is applied to the fan clutch relay.

The following fan clutch checks are for fan clutches wired to the electronically controlled fuel system. Refer to the vehicle manufacturer's specifications to determine the installation of the fan clutch.

![[fn2cnkc.png]]

### Initial Check

Viscous fan drives are used as a power-saving device activated by a built-in sensor behind the radiator used to monitor air temperature.

When the air temperature reaches a specific level, depending on the temperature setting of the sensor used, the temperature-sensing control moves an actuator that allows viscous fluid to engage the fan drive and increase the fan speed.

![[fn8cnga.png]]

Use a fan rpm-measuring device to check the operation of the viscous fan hub. A strobe or digital optical tachometer, Part Number 3377462, can be used.

![[fn8toga.png]]

Mark a spot on the fan hub pulley and one fan blade so the measuring device can determine the pulley and the fan speed. Reflective tape, Part Number 3377464, in digital optical tachometer, Part Number 3377462, can be used to mark the fan blade and the pulley.

![[fa8puta.png]]

While the engine is still warm and the vehicle is shut off, cover the radiator grill.

Leave a hole approximately 0.3 m \[1-ft\] in diameter in the cardboard to allow some air to flow to the viscous fan hub.

![[ra8cvhb.png]]

Start the engine. Idle the engine for three to five minutes. Lock the throttle in a HIGH IDLE position.

Use the PTO option to operate the engine at maximum PTO engine rpm.

![[oi800ve.png]]

> [!danger] WARNING · Опасно
> The cooling fan will engage when the engine is started. To reduce the possibility of personal injury, do not put your hands in the path of a rotating fan.

> [!warning] CAUTION · Осторожно
> Do not exceed 100°C \[212°F\] coolant temperature. Higher coolant temperatures can damage the engine.

![[fn800qc.png]]

When the coolant temperature reaches 91°C \[195°F\], measured fan speed **must** reach a minimum of 85 percent of the pulley speed.

Measure the fan speed divided by the fan hub (pulley) speed. The dividend **must** be greater than or equal to 0.85.

Measured Fan Speed ÷ Fan Hub (Pulley Speed) \>= 0.85

![[fn800kd.png]]

While the engine is still at high idle, remove the radiator grill cover. The fan speed **must** begin to decrease after 1 minute and eventually drop to a maximum of 50 percent of the input pulley speed.

If the viscous fan hub fails this test, have it checked by an authorized fan hub dealer for repair or replacement.

![[ra8cvmb.png]]

If the fan does **not** operate within the temperature range indicated on the coolant temperature sensor (1), the fan clutch and the controls **must** be checked. Refer to the OEM service manual.

![[08200052.png]]

If a fan speed measuring device is **not** available and the complaint concerns overheating, remove the viscous fan hub bimetal strip and the control pin. This will cause the fan hub to operate all the time.

![[fa8pima.png]]

If the overheating complaint does **not** occur with the control pin removed, install the control pin, and take the fan hub to an authorized fan hub dealer for repair or replacement.

![[fa8piha.png]]

### Preparatory Steps

- Remove the fan drive belt. [[35-008-002-tr — Drive Belt, Cooling Fan|Refer to Procedure 008-002 in Section 8.]]
- Remove the fan and fan clutch assembly. Refer to the OEM service manual.

![[ck800wa.png]]

### Remove

Remove the nuts, washers, and fan.

![[fa8cnha.png]]

### Install

Install the fan on the fan clutch assembly.

Tighten the mounting nuts. Refer to the OEM service manual for torque specifications.

![[fa8cnha.png]]

### Finishing Steps

- Install the fan clutch and fan assembly on the engine. Refer to the OEM service manual.
- Install, adjust, and tighten the fan drive belt. [[35-008-002-tr — Drive Belt, Cooling Fan|Refer to Procedure 008-002 in Section 8.]]
- Operate the engine and check for proper operation.

![[ck800wa.png]]
