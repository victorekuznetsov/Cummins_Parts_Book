---
type: "Процедура"
doc: "10-014-027"
title_en: "Aftertreatment Diesel Particulate Filter Regeneration Analyzer"
modified: "2023-09-07"
engines:
  - "80141463"
  - "80248213"
families:
  - "QSX15"
manuals:
  - "3666239"
figures: 3
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/10/10-014-027.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/10-014-027.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSX15"
  - "группа/10"
---

# Aftertreatment Diesel Particulate Filter Regeneration Analyzer

> [!abstract] Процедура · `10-014-027`
> **Двигатели:** [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSX15
> **Входит в руководства:** [[3666239 — Signature™, ISX, and QSX15 Service Manual|3666239]]
> **Секции:** Section 12 - Compressed Air System - Group 12 · Section 14 - Engine Testing - Group 14
> **Даты:** изменён 2023-09-07
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/10/10-014-027.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/10-014-027.pdf)

### Select Service Tools

#### Recommended Cummins® Service Tools

- Cummins® electronic service tool or equivalent.

#### Additional Service Items

- No additional service items required.

### General Information

The Aftertreatment Diesel Particulate Filter (DPF) Regeneration Analyzer Test is a diagnostic used to identify malfunctioning engine performance components. The test is located in INSITE™ electronic service tool under the Diagnostic Tests tab.

The test status will be shown in the status window.

1. Test description window
2. Instructions window
3. Status window
4. Status bar - shows progress of the test (will disappear when the test is complete).

![[19204201.png]]

### System Requirements

The Aftertreatment Diesel Particulate Filter Regeneration Analyzer Test requires:

- INSITE™ electronic service tool version 8.5.2 or later.
- Minimum of 250 MB of available computer hard drive space before starting the test.

The Aftertreatment Diesel Particulate Filter Regeneration Analyzer Test is **only** to be used when directed by published troubleshooting.

![[19803969.png]]

### Preparatory Steps

> [!danger] WARNING · Опасно
> During testing, exhaust gas temperature could reach 800°C \[1500°F\] and exhaust system surface temperature can exceed 700°C \[1300°F\], which is hot enough to ignite or melt common materials, and to burn people. The exhaust and exhaust components can remain hot after the vehicle stops moving. To avoid the risk of fire, property damage, burns or other serious personal injury, allow the exhaust system to cool before beginning this procedure or repair and make sure that no combustible materials are located where they are likely to come in contact with hot exhaust or exhaust components.

Before the Aftertreatment Diesel Particulate Filter Regeneration Analyzer Test, follow the steps listed below:

1. Select an appropriate location to park the vehicle.
2. Park the truck securely.
3. Set up a safe exhaust area.
4. Check exhaust system surfaces.
5. Prepare for engine speed changes during regeneration.
6. To begin the test:

Once the Aftertreatment Diesel Particulate Filter Regeneration Analyzer Test is complete, exhaust gas and exhaust surface temperatures will remain elevated for 3 to 5 minutes. Keep the engine running at idle until the exhaust temperatures are reduced.

### Test

> [!note] Note · Примечание
> If the connection between INSITE™ electronic service tool and the engine control module (ECM) is lost for any reason, a pop-up message will appear. The test can be restarted after cycling the keyswitch OFF for 90 seconds and then back ON.

1. Begin the Aftertreatment Diesel Particulate Filter Regeneration Analyzer Test.
2. Monitor the area.

A logfile will be automatically created and saved to the computer. You may be asked to provide the logfile by Cummins® CARE if technical assistance is required.

The Aftertreatment Diesel Particulate Filter Regeneration Analyzer Test will **not** start or will be aborted if:

- Accelerator pedal is depressed
- Clutch pedal is depressed
- Brake pedal is depressed
- Parking brake **not** set
- Transmission is put into gear
- PTO engaged
- Vehicle speed detected
- Engine protection state active
- Regeneration inhibiting fault code becomes active
- High aftertreatment temperature faults become active.

If the Aftertreatment Diesel Particulate Filter Regeneration Analyzer Test aborts or will **not** activate, a message will be displayed. Correct the issue identified before proceeding. For more information on abort messages and associated repair action, see the Troubleshooting section of this procedure.

### Troubleshooting

This section is used to assist troubleshooting abort messages from the Status Window.

Abort messages will be displayed in the Status Window. The most recent message will appear at the bottom.

![[19204202.png]]

| Status Window Message | Action |
|---|---|
| The test was stopped as there was **not** enough valid data. | Inspect for exhaust manifold leaks. Refer to Procedure 010-024 in Section 10. Clean and inspect the exhaust gas recirculation (EGR) valve. Refer to Procedure 011-022 in Section 11. Check for aftertreatment diesel oxidation catalyst (DOC) face plugging. Clean and inspect for reuse. Refer to Procedure 011-049 in Section 11. Clean and inspect the aftertreatment fuel injector. Refer to Procedure 011-042 in Section 11. Perform the Aftertreatment Fuel Injector Flow Test. Refer to Procedure 011-054 in Section 11. Inspect the cooling fan for damage. Refer to Procedure 008-040 in Section 8. Check the coolant thermostat. Refer to Procedure 008-013 in Section 8. |
| There is **not** enough available storage space. A minimum of 250 MB is required. | Minimum of 250 MB memory space is required to run this test. |
| INSITE™ electronic service tool can **not** currently read the ECM parameters from the connected ECM. Contact technical support. | Follow local escalation process. |
| Data files are **not** available. Proceed with published troubleshooting. | Proceed with published troubleshooting. |
| The user does **not** have sufficient access permissions to create the output file. Contact the local IT administrator. | Contact the local IT administrator. |
| The test has completed and failed. | Read and record status message. |
| The test has stopped or could **not** start because the data link connection was lost. | Check the cables between the computer data link adapter for proper connection and condition. Refer to Procedure 019-165 in Section 19 of the Signature™, ISX, and QSX15 Electronic Control System Troubleshooting and Repair Manual, Bulletin 3666259. |

### Finishing Steps

- Do not turn the keyswitch off until the test has completed and results are displayed.
- Check for any active fault codes. If active fault codes are present, follow published troubleshooting.
