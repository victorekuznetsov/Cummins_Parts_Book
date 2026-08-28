---
aliases:
  - "Калибровочный код ЭБУ"
type: "Процедура"
doc: "87-019-032"
title_en: "ECM Calibration Code"
title_ru: "Калибровочный код ЭБУ"
modified: "2011-02-16"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666214"
figures: 4
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-019-032.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-019-032.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
---

# ECM Calibration Code
**Калибровочный код ЭБУ**

> [!abstract] Процедура · `87-019-032`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section 19 - Electronic Engine Controls
> **Даты:** изменён 2011-02-16
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-019-032.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-019-032.pdf)

### General Information

> [!note] Note · Примечание
> **Not** all illustrations within this procedure will represent the application that is being worked on.

Electronic control module (ECM) calibrations can be performed by INSITE™ electronic service tool.

After an ECM is replaced or calibrated, the actual engine hours/distance **must** be entered correctly into the ECM.

Record the values of the ECM Time Offset, Engine Time Offset, Base Lambda Offset, Desired Lambda, and Fuel Control Valve Initial Position prior to replacement or calibration of the ECM. These parameters can be found in the Data Monitor/Logger and Trip Information section in INSITE™ electronic service tool.

![[19c01217.png]]

The ECM calibration process occurs with the keyswitch turned ON. Always follow the instructions on the service tool screens.

> [!note] Note · Примечание
> If the tool will **not** communicate with the keyswitch in the ON position, cycle the keyswitch and try again.

![[19800470.png]]

Connect INSITE™ electronic service tool to the service tool datalink, which is located on the engine or in the cab.

> [!note] Note · Примечание
> Single module calibration is **not** supported with INSITE™ electronic service tool for CM552 on QST30 Industrial engines. When calibrating a CM552, the modules **must** be connected together. Use the bench calibration parent cable, Service Tool Part Number 3163151, along with the appropriate calibration adapter harness, Part Number 3165085.

> [!note] Note · Примечание
> For the QST30, both 50 pin connectors, and 01 key connectors on adapter harness, Part Number 3165085, are used to calibrate both CM552 modules at the same time.

![[22d00436.png]]

Reference the help section within INSITE™ electronic service tool for detailed ECM calibration procedures.

After an ECM is replaced or calibrated, the actual engine hours/distance **must** be entered correctly into the ECM.

![[19c01217.png]]
