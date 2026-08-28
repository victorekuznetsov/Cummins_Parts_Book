---
type: "Процедура"
doc: "97-019-300"
title_en: "Cab Thermostat"
modified: "2003-06-12"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
  - "80141463"
  - "80248213"
families:
  - "QSM11"
  - "QSX15"
manuals:
  - "3666415"
figures: 8
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-019-300.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-019-300.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "двигатель/QSX15"
  - "группа/97"
---

# Cab Thermostat

> [!abstract] Процедура · `97-019-300`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSM11, QSX15
> **Входит в руководства:** [[3666415 — ICON Idle Control System Master Repair Manual|3666415]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-06-12
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-019-300.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-019-300.pdf)

### Remove

Turn the keyswitch to the OFF position.

Remove the screws securing the cab thermostat to the bunk housing wall.

Disconnect the cab thermostat jumper harness and the temperature sensor harness from the cab thermostat.

![[19802874.png]]

Remove the cab thermostat.

![[19802875.png]]

### Install

Make sure the keyswitch is turned to the OFF position.

Position the cab thermostat in a suitable location in the bunk area.

Typically, the thermostat is installed approximately 2 feet over the bunk sleeping area, or midway between the bunk and the ceiling, out of the direct flow of air from the air conditioning or heating.

![[19802875.png]]

Install the screws securing the cab thermostat to the bunk housing wall.

Connect the cab thermostat to the temperature sensor harness.

Connect the cab thermostat to the cab thermostat harness.

![[19802874.png]]

### Adjust

In troubleshooting the ICON™ system, the technician can “force” an engine start via the thermostat's Cab Comfort mode. This artificially created engine start can be accomplished using heat guns or cold spray.

Be aware that, if this technique is being employed for troubleshooting purposes and the “forced” engine restart occurs within 10 minutes of the previous ICON™-ordered restart, the thermostat will generate an E3 fault code.

![[15800001.png]]

When the ICON™ system is set to Cab Comfort mode, the cab thermostat is instrumental in communicating with and enabling the ICON™ system to autostart the vehicle's engine. Thermostat adjustments that are improperly set can prevent the ICON™ system from autostarting the engine. Rule out the possibility of an improperly set cab thermostat before troubleshooting further.

Verify that the thermostat's cool or heat mode is active by checking for the word “COOL” or “HEAT” displayed in the thermostat's lower left corner.

![[15800027.png]]

If the cool or heat mode indicator (“COOL” or “HEAT” displayed in lower left of thermostat display) is flashing, this means that the thermostat has detected the bunk temperature is above the cool set point and range value (or below the heat set point and range value) and is commanding the ICON™ idle control module to start the engine.

It is also possible to get the flashing indication of the thermostat autostart engine command to ICON™ while the engine is already running.

If the engine does **not** start when it is being commanded to do so by the thermostat, troubleshoot the cab harness, cab thermostat jumper harness, or ICON™ engine harness. Check for fault codes.

![[15800023.png]]

The ICON™ system's Cab Comfort mode can seem to be working intermittently. A possible cause for this is that the driver is **not** manually choosing either heat or cool mode each time he desires to utilize ICON™'s Cab Comfort mode. If the cool or heat mode is **not** chosen manually each time Cab Comfort mode is enabled (by turning on the thermostat and choosing heat mode), the thermostat will default to the autocool and autoheat settings as dictated in the thermostat's trim settings. These trim settings can be readjusted according to the driver's personal preferences.

Refer to Cab Thermostat Operation and the Thermostat Trim Settings in Section F for more details on adjusting the thermostat's cool and heat modes, and for the trim table settings, which can be reset.

![[15800020.png]]
