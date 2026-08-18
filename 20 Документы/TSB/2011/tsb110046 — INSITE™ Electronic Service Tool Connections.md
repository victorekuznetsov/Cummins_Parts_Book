---
aliases:
  - "Подключения INSITE™"
type: "TSB"
doc: "tsb110046"
title_en: "INSITE™ Electronic Service Tool Connections"
title_ru: "Подключения INSITE™"
released: "2011-03-09"
modified: "2011-03-09"
group: "19 - Electronic Engine Controls"
engines:
  - "33239746"
  - "33239899"
  - "41349633"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
  - "QSK19"
figures: 2
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2011/tsb110046.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/tsb/tsb110046.pdf"
tags:
  - "документ/tsb"
  - "двигатель/K38/K50"
  - "двигатель/QSK19"
  - "год/2011"
  - "тема/electronic-engine-controls"
---

# INSITE™ Electronic Service Tool Connections
**Подключения INSITE™**

> [!abstract] TSB · `tsb110046`
> **Раздел Cummins:** 19 - Electronic Engine Controls
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]], [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60, QSK19
> **Даты:** выпущен 2011-03-09 · изменён 2011-03-09
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2011/tsb110046.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/tsb/tsb110046.pdf)

## INSITE™ Electronic Service Tool Connections

### Warranty Statement

The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.

### Contents

This document provides information on a number of issues associated with using INSITE™ electronic service tool to obtain Advanced ECM Data, Fault Snapshot Data, Trend Data, and carry out ECM calibration when a single OEM J1939 data link port is available in applications with twin engines equipped with multiple.ECMs

Typically, two issues are experienced:

1. When the data stream for twin engines equipped with multiple ECMs is broadcast to a common data link, a number of limitations are experienced, because the industry standard baud rate for INSITE™ electronic service tool is insufficient to allow adequate data logging and fault finding functionality.
2. Twin engine equipped applications have calibrations which uniquely identify all six ECMs on both engines. Each engine and module is identified by a unique source address that is assigned by the ECM when it detects different combinations of grounding on the Multi-Unit Synchronisation (MUS) and Identification (ID) pins and compares these to the calibration installed in the ECM. If a mismatch between the grounding combination and the calibration installed is identified, an incorrect source address can be assigned. Also, if the ECMs are installed in engines/applications which do **not** have the MUS pins grounded, INSITE™ electronic service tool may **not** be able to establish communication and Fault Fode 5092 can be activated.

Data logging and fault finding functionality:

When using INSITE™ electronic service tool to obtain Advanced ECM Data, Fault Snapshot Data, and Trend Data from a specific engine using the OEM data link port, manually isolate the engine(s) which are **not** to be communicated with from the data link. Any data link connectors which have been disconnected from the main bus should be terminated using a suitable resistor to give a total data link resistance of 60 ohms.

![[19000002.png]]

3-pin J1939 engine data link (1)

> [!note] Note · Примечание
> Failure to make sure of the correct data link termination resistance can result in damage to the ECM.

With the keyswitch in the ON position, use INSITE™ electronic service tool to connect to the engine using the OEM data link port. A work order can now be created. Advanced ECM Data and Engine Monitoring functions can also be used, if required.

Once INSITE™ electronic service tool is connected and monitoring, the required engine data link can be connected so that any OEM hydraulic derates are unaffected.

If simultaneous data logging of multiple engines is required, connect to any additional engines by connecting to the on-engine 9-pin data link connector using cable, Part Number 3165160, a suitable inline adapter, and extension serial cable, Part Number 3162851. The use of a long extension serial cable allows it to be run into the cab.

Once one engine has been successfully communicated with, the process described above can be repeated as required for all engines.

Once all engines have been successfully communicated with, the termination resistor(s) **must** be removed and all engines reconnected to the data link bus.

Recalibration:

Two methods can be used, depending on whether the correct pin groundings are in place on the engine.

Method 1

This method assumes the module ID and MUS pins have been grounded correctly and the modules simply require calibrating.

1. Isolate any engines **not** requiring calibration by disconnecting them from the main data link bus, as described in the procedure above.

2. Remove the ECM power supply connectors from all ECMs **not** needing calibration, see below.

![[19000003.png]]

4-pin ECM power supply connector (1)

3. Use INSITE™ electronic service tool to connect to the module requiring calibration using the OEM data link port.

4. Use INSITE™ electronic service tool to calibrate the module.

5. Repeat the procedure above, as required, until all modules have been calibrated.

6. Connect all engines and modules to the main data link bus.

Method 2

This method assumes the module ID and/or MUS pins have been grounded incorrectly and/or a ROM boot is required.

The most reliable method for calibration is to ROM boot each ECM individually. This approach makes sure the correct calibration is installed and each ECM assumes the correct source address.

See Table 1 for further information on pin grounding.

1. Use a suitable ROM boot cable, Part Number 3164185, to ground the correct ID pins to create the correct source address and allow INSITE™ electronic service tool to communicate with the ECM (X=grounded), as shown in Table 1.

| Table 1: Pin Allocation for Correct Source Address Assignment |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|
|  | Calibration | Source Address | Module ID Input 1 | Module ID Input 2 | Module ID Input 3 | MUS Pin 3 | MUS Pin 1 | MUS Pin 2 |  |
| Dec | Hex | Pin 08 | Pin 07 | Pin 12 | Pin 02 | Pin 03 | Pin 17 |  |  |
| Left Engine | Parent | 0 | 00 |  | X | X | X | X | X |
| Child 1 | 1 | 01 | X |  | X | X | X | X |  |
| Child 2 | 144 | 90 | X | X |  | X | X | X |  |
| Right Engine | Parent | 145 | 91 |  | X | X | X | X |  |
| Child 1 | 146 | 92 | X |  | X | X | X |  |  |
| Child 2 | 147 | 93 | X | X |  | X | X |  |  |

2. Use INSITE™ electronic service tool to connect to the module requiring calibration.

> [!note] Note · Примечание
> All grounding connections **must** be connected prior to powering up the ECM.

> [!note] Note · Примечание
> The ECM **must** be keyed OFF for 30 seconds and then keyed ON, **every** time the ID pin grounds are changed. This allows the ECM to reset.

> [!note] Note · Примечание
> OEM harnesses should already have the pins grounded.

3. Use INSITE™ electronic service tool to calibrate the module.

4. Repeat the procedure above, as required, until all modules have been calibrated.

5. Connect all modules to the engine.

### Document History
