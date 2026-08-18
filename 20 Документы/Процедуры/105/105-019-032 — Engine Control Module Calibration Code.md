---
aliases:
  - "Калибровочный код ЭБУ"
type: "Процедура"
doc: "105-019-032"
title_en: "Engine Control Module Calibration Code"
title_ru: "Калибровочный код ЭБУ"
modified: "2025-08-08"
engines:
  - "33239746"
  - "33239899"
  - "37292556"
  - "37295879"
  - "41343322"
  - "41349633"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
  - "NT/NTA855 · ISM/QSM11"
  - "QSK19"
  - "QST30"
manuals:
  - "3666214"
  - "3666231"
  - "3666266"
  - "4021674"
  - "4022094"
  - "4022102"
figures: 5
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/105/105-019-032.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/105-019-032.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "двигатель/NT/NTA855"
  - "двигатель/QSK19"
  - "двигатель/QST30"
  - "группа/105"
---

# Engine Control Module Calibration Code
**Калибровочный код ЭБУ**

> [!abstract] Процедура · `105-019-032`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]], [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]], [[41343322 — NH NT 855 CPL 3362|41343322]], [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60, NT/NTA855 · ISM/QSM11, QSK19, QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]], [[3666231 — Centinel™ Master Repair Manual|3666231]], [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]], [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]], [[4022094 — QSK19 CM2150 and CM2670 Electronic Control System Troubleshooting and Repair Manual|4022094]], [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M|4022102]]
> **Секции:** Section 19 - Electronic Controls - Group 19 · Section 19 - Electronic Engine Controls · Section 19 - Electronic Engine Controls - Group 19 · Section 19 - Electronic Engine Controls — Group 19
> **Даты:** изменён 2025-08-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/105/105-019-032.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/105-019-032.pdf)

### Select Service Tools

#### Recommended Cummins® Service Tools

- Cummins® electronic service tool or equivalent

#### Additional Service Items

- No additional service items required.

### General Information

> [!note] Note · Примечание
> Due to the number of various engine control module (ECM) configurations, this procedure has been written to be common. **Not** all illustrations within this procedure will represent the application that is being worked on.

ECM calibrations can be performed by the recommended Cummins® electronic service tool or equivalent.

Cummins ® electronic service tool uses a Service Calibration Management (SCM) process which uses a database along with additional logic to evaluate if a requested ECM code is approved for installation into the ECM. See Service Bulletin, Engine Control Module (ECM) Calibration Download with Cummins ® Electronic Service Tools, Bulletin 6643906.

After an ECM is replaced or calibrated, the actual engine hours / distance **must** be entered correctly into the ECM.

Record the values of ECM Distance Offset, ECM Time Offset, Engine Distance Offset, and Engine Time Offset prior to replacement or calibration of the ECM. These parameters can be found in the Trip Information section of Features and Parameters.

![[19t00005.png]]

### Initial Check

If the tool will **not** communicate with the keyswitch in the ON position, cycle the keyswitch and try again.

The ECM calibration process occurs with the keyswitch turned ON. **Always** follow the instructions on the service tool screens.

![[19800470.png]]

### Preparatory Steps

Connect the electronic service tool to the service tool data link, which is located on the engine or in the cab.

After an ECM is replaced or calibrated, the actual engine hours / distance **must** be entered correctly into the ECM.

Input the values of ECM Distance Offset, ECM Time Offset, Engine Distance Offset, and Engine Time Offset prior to replacement or calibration of the ECM. These parameters can be found in the Trip Information section of Features and Parameters.

Verify vehicle odometer is equal to the value recorded before ECM removal. Contact OEM service location if values are incorrect.

![[19t00005.png]]

### Inspect

Establish if the suspected feature creating the problem is operating correctly. Reference the relevant “Electronic Controlled Fuel System” (Procedure 101-007) in Section 1 of the appropriate Operation and Maintenance Manual.

To access the “Adjustable Engine Features” section, either select Help -\> Contents from the menu bar, or press F1 with an individual feature within the Features and Parameters section in the electronic service tool.

Review the "Adjustable Engine Features” section to determine if the suspected error is due to an incorrectly set adjustable engine feature.

![[19t00005.png]]

Use QuickServe™ Online to inspect the calibraton revision history.

1. Log into QuickServe™ Online
2. Select "My Applications"
3. Select "ECM Calibraton Revisions"
4. Enter the calibration code and select "Search"
5. Review the calibration revision information.

The calibration revision history provides information relating to changes made to a calibration each time a new revision is released. This information can be used to establish if there is a commonality between changes made to the calibration and the symptoms being observed. The calibration revision history can also be downloaded in Excel format by selecting “Spreadsheet” in the record filter box.

The greater the number of parameters, the slower the rate at which they can be logged. Therefore, **only** log the minimum number of parameters if sample rate is important.

If no issue can be identified using the steps listed above, the following information should be collected to allow the issue to enter the technical escalation chain:

1. Engine specifics engine serial number (ESN), application, rating, engine hours, maintenance history, etc.)
2. ECM codes (the codes before and after, including revision numbers)
3. ECM images (before and after calibration downloads)
4. Data logs (utilize existing, pre-defined parameter groups, or use the relevant wiring diagram to identify if multiple circuits utilize a common supply or ground, or monitor parameters which logically would be linked - i.e. User Fuelling State, Engine Speed, Commanded Fuel Rail Pressure, Measured Fuel Rail Pressure, etc.).

![[19t00005.png]]
