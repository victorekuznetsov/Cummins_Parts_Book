---
aliases:
  - "Устранение проблем с калибровкой"
type: "TSB"
doc: "tsb110297"
title_en: "Calibration Issue Resolution"
title_ru: "Устранение проблем с калибровкой"
released: "2011-10-28"
modified: "2011-11-07"
group: "19 - Electronic Engine Controls"
engines:
  - "33239746"
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
figures: 6
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2011/tsb110297.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/tsb/tsb110297.pdf"
tags:
  - "документ/tsb"
  - "двигатель/K38/K50"
  - "год/2011"
  - "тема/electronic-engine-controls"
---

# Calibration Issue Resolution
**Устранение проблем с калибровкой**

> [!abstract] TSB · `tsb110297`
> **Раздел Cummins:** 19 - Electronic Engine Controls
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Даты:** выпущен 2011-10-28 · изменён 2011-11-07
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2011/tsb110297.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/tsb/tsb110297.pdf)

## Calibration Issue Resolution

### Warranty Statement

The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.

### Contents

The issue is, during troubleshooting of the electronic control module (ECM), a calibration issue is potentially identified when a new calibration or ECM is installed. Standard troubleshooting trees are exhausted before the root cause is determined.

For verification, the following statements will be true:

1. The existing or replacement module has just been loaded with a calibration which was **not** previously installed.
2. A new issue is experienced, which was **not** present when using the previous module or calibration.
3. It has already been verified that the installed calibration is appropriate for the engine, equipment, and application.

Use the following for resolution.

1. Establish if the suspected feature creating the problem is operating correctly. Reference the relevant “Electronic Controlled Fuel System” procedure 101-007 in Section F of the appropriate Electronic Control System Troubleshooting and Repair Manual on QuickServe™ Online (QSOL) or in INSITE™ electronic service tool, “Fault Information System” (Figures 1 and 2) for further information.

![[19e01007.png]]

Figure 1

- INSITE™ - (Features and Parameters), select Fault Trees Index

.

![[19e01008.png]]

Figure 2

- Select the Electronic Controlled Fuel System (101-007) for the affected engine.

Similarly, review INSITE™ electronic service tool help files, “Adjustable Engine Features” section to determine if the suspected error is due to an incorrectly set adjustable engine feature. Reference to Figures 3 and 4.

![[19e01009.png]]

Figure 3

- INSITE™ - (Features and Parameters), select contents.

![[19e01010.png]]

Figure 4

- Select Adjustable Engine Features.

2. Use QSOL to inspect the calibration revision history. Reference Figures 5 and 6 for the following:

1. Log onto QSOL
2. Select "My Application"
3. Select "ECM Calibration Revisions"
4. Enter the calibration code and select "Search"
5. Review the calibration revision information.

![[19e01011.png]]

Figure 5

- Perform steps 1 through 3.

![[19e01012.png]]

Figure 6

- Perform steps 4 and 5.

The Calibration Revision History provides information relating to changes made to a calibration each time a new revision is released. This information can be used to establish if there is commonality between changes made to the calibration and the symptoms being observed, thus helping determine if a calibration issue exists.

> [!note] Note · Примечание
> The Calibration Revision History can also be downloaded in Excel format by clicking “Spreadsheet” in the record filter box.

3. Perform the necessary research to verify if a known issue is being experienced and whether specific troubleshooting, repair, and reporting steps are required.

4. If no issue can be identified using the above steps, the following information should be collected to allow the issue to enter the technical escalation chain:

1. Engine specifics (engine serial number (ESN), application, rating, engine hours, maintenance history, etc.)
2. ECM codes (the codes before and after, including the revision numbers, will be required)
3. ECM images (before and after calibration download)
4. Data logs (existing pre-defined parameter groups can be found in INSITE™ electronic service tool, otherwise use the relevant wiring diagram to identify if multiple circuits share a common supply and/or ground or monitor parameters which logically would be linked e.g. User Fuelling State, Engine Speed, Commanded Fuel Rail Pressure, Measured Fuel Rail Pressure, etc.)

> [!note] Note · Примечание
> The greater the number of parameters, the slower the rate at which they can be logged. Therefore, **only** log the minimum number of parameters if sample rate is important.

### Document History
