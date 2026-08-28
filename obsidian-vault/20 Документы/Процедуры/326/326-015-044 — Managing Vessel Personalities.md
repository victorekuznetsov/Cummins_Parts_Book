---
type: "Процедура"
doc: "326-015-044"
title_en: "Managing Vessel Personalities"
modified: "2019-11-04"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "4358378"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/326/326-015-044.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/326-015-044.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/326"
---

# Managing Vessel Personalities

> [!abstract] Процедура · `326-015-044`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[4358378 — Cummins® Electronic Throttle and Shift (ETS) and Cummins® Inboard Joystick Marine Con|4358378]]
> **Секции:** Section 15 - Instruments and Controls - Group 15
> **Даты:** изменён 2019-11-04
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/326/326-015-044.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/326-015-044.pdf)

### General Information

The Cummins® inboard joystick must be tuned to the vessel it is installed in for maximum performance. Vessel joysticks come with a preloaded default personality file when ordered from the factory. New joysticks have to be updated with a tuned vessel personality file that is specific to boat original equipment manufacturer (OEM) and model. It is necessary to load the most current vessel personality for the vessel. If changing a vessel personality file for other reasons, consider the many factors that can contribute to vessel maneuverability such as the following:

- Boat weight (Number of passengers/cargo, aftermarket add-ons)
- Ballast
- Hull design
- Thruster size
- Location of thruster
- Presence of an optional stern thruster
- Propeller size/design
- Battery voltage/performance
- Alternator performance (if thruster batteries are configured to utilize one)
- Steering wheel/rudder position
- Horsepower output of each engine
- Idle setting of each engine.
- Buildup, corrosion, or erosion of propeller.

Changes or alterations from the factory design of the boat can result in altering the performance of the joystick control. It is important to examine these factors to diagnose the root cause of the performance issue before contacting a Cummins® Authorized Repair Location. If a different personality is needed, please contact the a Cummins® Authorized Repair Location.

The QuickServe® Marine Panel Firmware webpage contains a vessel personality file tracking sheet and joystick vessel personality files.

The Marine Panel Firmware webpage for Cummins® Inboard Joystick (https://quickserve.cummins.com/qs3/qsol/service/marine/mpf\_joystick.html) contains a table with information about each vessel personality file, which helps select the correct file and revision level for the vessel's joystick(s).

> [!note] Note · Примечание
> [https://quickserve.cummins.com/qs3/qsol/service/marine/mpf\_joystick.html](https://quickserve.cummins.com/qs3/qsol/service/marine/mpf_joystick.html)

The Joystick Vessel Personality File Name format consists of 1 letter, 4 digits, and a 2 digit revision level. Example: J1234.01.jst.

Cummins® inboard joystick vessel personality files are loaded into the joystick using the joystick configuration electronic service tool. Use the following procedure for more detail about the vessel configuration electronic service tool. [[326-015-042 — Vessel Configuration Tool|Refer to Procedure 015-042 in Section 15.]]

After a joystick personality download, use the following procedure for information on joystick handle identification number, associated handle identification number, and joystick type setup. [[326-015-054 — Vessel Configuration|Refer to Procedure 015-054 in Section 15.]]

If the same personality file is downloaded into multiple joysticks stations on the vessel, the associated handle identification number will need to be set up differently at each station location. [[326-015-054 — Vessel Configuration|Refer to Procedure 015-054 in Section 15.]]

All control functionality of the Cummins® electronic throttle and shift and Cummins® inboard joystick **must** be tested before leaving the dock after a service event. Refer to Procedure 015-046 in Section 15.

Following a joystick personality file download, if there is a new alarm code or performance complaint, follow the alarm code or the appropriate troubleshooting symptom tree in order to understand if the personality is working correctly and is the appropriate personality for the application.

If it is suspected that the personality file is **not** working correctly, make sure that the appropriate file was loaded for the engine, equipment, and application.

Use the following procedure for more detail. [[326-015-042 — Vessel Configuration Tool|Refer to Procedure 015-042 in Section 15.]]

> [!note] Note · Примечание
> The “Vessel Personality File Tracking Sheet” on the Marine Panel Firmware Updates - Cummins® Inboard Joystick webpage provides information relating to changes made to a personality. This information can be used to establish if there is a commonality between changes made to the personality and the symptoms being observed.
