---
type: "Процедура"
doc: "326-015-075"
title_en: "Component Software Management"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/326/326-015-075.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/326-015-075.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/326"
---

# Component Software Management

> [!abstract] Процедура · `326-015-075`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[4358378 — Cummins® Electronic Throttle and Shift (ETS) and Cummins® Inboard Joystick Marine Con|4358378]]
> **Секции:** Section 15 - Instruments and Controls - Group 15
> **Даты:** изменён 2019-11-04
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/326/326-015-075.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/326-015-075.pdf)

### General Information

> [!warning] CAUTION · Осторожно
> Before updating software in any control system component, verify that the Vessel Control System is completely operational. It is also important to test and document the configuration settings and vessel personality of the component, if needed.

Cummins® Marine Controls come with a preloaded software from the factory.

For updates to software, please contact a Cummins® Authorized Repair Location.

Prior to software file download, document and understand the vessel performance and alarm/fault codes. Follow the alarm/fault code or the appropriate troubleshooting symptom tree in order to understand issues.

Cummins® Marine Controls Software files are loaded using the Component Software Download Tool Kit. Use the following procedure for more detail about the tool and download process. [[326-015-074 — Component Software Download Tool|Refer to Procedure 015-074 in Section 15.]]

The Marine Panel Firmware Updates - Cummins® Inboard Joystick webpage (https://quickserve.cummins.com/qs3/qsol/service/marine/mpf\_joystick.html) contains a software tracking sheet and software files.

> [!note] Note · Примечание
> [https://quickserve.cummins.com/qs3/qsol/service/marine/mpf\_joystick.html](https://quickserve.cummins.com/qs3/qsol/service/marine/mpf_joystick.html)

The Marine Panel Firmware Updates - Cummins® Inboard Joystick webpage contains files and a tracking sheet with information about each file, which helps select the correct file and revision level for the component. Reference the component name folder for the necessary file.

> [!note] Note · Примечание
> The Cummins® Marine Application Engineering group sends an email to joystick@cummins.com to update the Marine Panel Firmware Updates - Cummins® Inboard Joystick webpage with file name, version, and description of the component it is intended for.

The Software File Name format: “AAA-xxx.pj2”

Where:

AAA = product name

- JST = Inboard Joystick
- CH2 = Lever Control Station, two button
- CH4 = Lever Control Station, four button
- TIM = Thruster Interface Module
- CP3 = Throttle Control Processor Module, EEC3
- CP4 = Throttle Control Processor Module, EEC4

xxx = Software version (examples)

- 2.12 = 212
- 3.6 = 306
- 3.30 = 330
- 3.60 = 360

“.pj2” = software file extension

After an Inboard Joystick, Lever Control Station, or Throttle Control Processor Module software download, use the following procedure for information on component setup and configuration. [[326-015-054 — Vessel Configuration|Refer to Procedure 015-054 in Section 15.]]

After an Inboard Joystick software download, it will be necessary to confirm the vessel personality is working correctly and is the appropriate personality for the application. Use the following procedure for information on managing vessel personalities. [[326-015-044 — Managing Vessel Personalities|Refer to Procedure 015-044 in Section 15.]]

All control functionality of the Cummins® Marine Controls **must** be tested before leaving the dock after a service event. Refer to Procedure 015-046 in Section 15.

After a software file download, if there is a new alarm code or performance complaint, follow the alarm code or the appropriate troubleshooting symptom tree in order to understand if the software is working properly.

If it is suspected that the software or vessel personality file is **not** working correctly, make sure that the appropriate file was loaded for the engine, equipment, and application.

> [!note] Note · Примечание
> The personality file table in the Marine Panel Firmware Updates - Cummins® Inboard Joystick webpage provides information relating to changes made to a software file. This information can be used to establish if there is a commonality between changes made to the software and the symptoms being observed.
