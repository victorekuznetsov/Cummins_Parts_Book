---
type: "TSB"
doc: "tsb140019"
title_en: "Fuel Pump - Plunger and Tappet Roller Inspection and Repair"
modified: "2026-03-25"
figures: 2
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2014/tsb140019.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb140019.pdf"
tags:
  - "документ/tsb"
---

# Fuel Pump - Plunger and Tappet Roller Inspection and Repair

> [!abstract] TSB · `tsb140019`
> **Даты:** изменён 2026-03-25
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2014/tsb140019.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb140019.pdf)

## Fuel Pump - Plunger and Tappet Roller Inspection and Repair

### Warranty Statement

The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.

### Contents

**Product Affected**

- ISL9 CM2350 L101
- ISX12 CM2350 X102
- ISX12/ISX11.9 CM2250
- ISX15 CM2250
- ISX15 CM2250 SN
- ISX15 CM2350 X101
- PowerGen QSX15 CM2250
- PowerGen QSX15 CM2250 ECF
- QSX11.9 CM2250 ECF
- QSX15 CM2250 ECF
- QSX15 CM2350 X105
- QSX15 CM2350 X106
- X15 CM2350 X114B
- X15 CM2350 X116B
- X15 CM2450 X124B
- X15 CM2450 X134B
- X15 CM2450 X142B

This document, in conjunction with the information provided within the manuals listed in Table 1 provides inspection and repair guidelines following the malfunction of a fuel pump pumping plunger and/or roller tappet assembly.

The level of progressive damage to the fuel pump and other engine components will vary with every incident; however, the repair direction will depend on **only** a few key criteria.

Previous versions of this document provided specific repair directions according to the vintage of the fuel pump and type of pumping plungers. Repair directions have now been made common and apply to all fuel pumps regardless of vintage, pumping plunger type, or tappet roller assembly type.

![[04v00001.png]]

Figure 1, Damaged Fuel Pump Tappet Roller Assembly.

![[04v00002.png]]

Figure 2, Example of Severe Wear on Camshaft Lobe.

**Preliminary Inspection and Repair Direction for all Fuel Pump Malfunctions**

If severe camshaft or tappet roller wear is found, see scenarios below.

Scenario 1: The fuel pump tappet rollers are damaged or pumping plunger damage is found:

- Remove, cut open, and inspect the lubricating oil filter for debris. See Procedure 007-083 in Table 2.
- Connect INSITE™ electronic service tool to the service tool data link and review any logged fault codes.
- Reference Table 1 below for repair direction.

Scenario 2: The fuel pump tappet rollers and pumping plungers are **not** damaged:

- Connect INSITE™ electronic service tool to the service tool data link and review any logged fault codes. Follow appropriate fault code or symptom based troubleshooting in EDS or QuickServe® Online (QSOL).

| Table 1, Repair Direction Decision Matrix |  |  |
|---|---|---|
| Symptoms | Are Any Symptoms Present? | Repair Direction to Follow |
| Non-wear debris or particles are evident in the lubricating oil filter element. Fault Codes 415 or 143 are logged in the engine control module (ECM) within the last 8 hours of engine operation. Engine is seized, or engine rotating assembly produces abnormal noise. | Yes | Repair Direction A |
| No | Repair Direction B |  |

> [!warning] CAUTION · Осторожно
> Immediately upon removal of the lubricating oil cooler assembly, a plug must be inserted into the housing and cylinder block oil passage drillings. Failure to insert the oil passage plug can result in a bearing failure, crankshaft failure, or both.

> [!warning] CAUTION · Осторожно
> Do not allow dirt or foreign material to enter oil passages in the cylinder block when cleaning the gasket sealing surfaces. Connecting rod bearing failures can be caused if debris is introduced into the cylinder block or lubricating oil cooler housing oil passages. Therefore, use of power tools combined with abrasive pads to clean gasket surfaces is not recommended.

**Repair Direction A:**

1. Drain lubricating engine oil. See Procedure 007-037 in Table 2.
2. Remove lubricating oil pan, and clean thoroughly. See procedure 007-025 in Table 2.
3. Remove and inspect lubricating oil pump for reuse. See Procedure 007-031 in Table 2.
4. Remove number 1 and number 4 main bearing caps and main bearings. See procedure 001-006 in Table 2.
5. Inspect number 1 and number 4 main journals of crankshaft for reuse. See Service Bulletin Crankshaft Reuse Guidelines for Cummins® Engines, Bulletin 5411180.
6. Inspect fuel pump for internal damage. See Procedure 005-016 in Table 2 below.
7. Thoroughly clean lubricating oil cooler housing. See Procedure 007-003 in Table 2.
8. Replace following lubricating oil system components:
9. Install lubricating oil pan and other components removed to access main bearings. See procedure 007-025 in Table 2
10. Install a new lubricating oil filter. See Procedure 007-013 in Table 2.
11. Prime and fill the engine with new lubricating oil. See Procedure 007-037 in Table 2.
12. Perform an aftertreatment diesel particulate filter (DPF) regeneration. See Procedure 014-013 in Table 2.
13. Perform a second lubricating oil and lubricating oil filter change. Priming lubricating oil system a second time is **not** required. See Procedure 007-013 and 007-037 in Table 2.

**Repair Direction B:**

1. Inspect the fuel pump for internal damage. If damage is found, replace fuel pump assembly. See Procedure 005-016 in Table 2.
2. Drain the engine lubricating oil and remove the lubricating oil filter. See Procedure 007-013 and 007-037 in Table 2.
3. Replace the lubricating oil filter bypass valve. See Procedure 007-014 in Table 2.
4. Fit a new lubricating oil filter and refill the engine lubricating oil system. Priming the lubricating oil system is **not** required. See Procedure 007-013 and 007-037 in Table 2.

| Table 2, Associated Procedures |  |  |  |
|---|---|---|---|
| Procedure Title | Procedure Number | Service Model Name | Bulletin Number |
| Fuel Pump | Refer to Procedure 005-016 | ISX15 CM2250 | 4022250 |
| Fuel Pump | Refer to Procedure 005-016 | ISX15 CM2250 SN | 4310736 |
| Fuel Pump | Refer to Procedure 005-016 | ISX12/ISX11.9 CM2250 | 2883445 |
| Fuel Pump | Refer to Procedure 005-016 | ISX15 CM2350 X101 | 4310641 |
| Fuel Pump | Refer to Procedure 005-016 | QSX15 CM2250 ECF | 2883557 |
| Fuel Pump | Refer to Procedure 005-016 | QSX11.9 CM2250 ECF | 2883561 |
| Fuel Pump | Refer to Procedure 005-016 | QSX15 CM2350 X105 | 4332667 |
| Fuel Pump | Refer to Procedure 005-016 | QSX15 CM2350 X106 | 4332712 |
| Fuel Pump Head | Refer to Procedure 005-227 | ISX15 CM2250 | 4022250 |
| Fuel Pump | Refer to Procedure 005-227 | ISX15 CM2250 SN | 4310736 |
| Fuel Pump Head | Refer to Procedure 005-227 | ISX12/ISX11.9 CM2250 | 2883445 |
| Fuel Pump Head | Refer to Procedure 005-227 | ISX15 CM2350 X101 | 4310641 |
| Fuel Pump Head | Refer to Procedure 005-227 | QSX15 CM2250 ECF | 2883557 |
| Fuel Pump Head | Refer to Procedure 005-227 | QSX11.9 CM2250 ECF | 2883561 |
| Fuel Pump Head | Refer to Procedure 005-227 | QSX15 CM2350 X105 | 4332667 |
| Fuel Pump Head | Refer to Procedure 005-227 | QSX15 CM2350 X106 | 4332712 |
| Lubricating Oil Cooler | Refer to Procedure 007-003 | ISX15 CM2250 | 4022250 |
| Lubricating Oil Cooler | Refer to Procedure 007-003 | ISX15 CM2250 SN | 4310736 |
| Lubricating Oil Cooler | Refer to Procedure 007-003 | ISX12/ISX11.9 CM2250 | 2883445 |
| Lubricating Oil Cooler | Refer to Procedure 007-003 | ISX15 CM2350 X101 | 4310641 |
| Lubricating Oil Cooler | Refer to Procedure 007-003 | QSX15 CM2250 ECF | 2883557 |
| Lubricating Oil Cooler | Refer to Procedure 007-003 | QSX11.9 CM2250 ECF | 2883561 |
| Lubricating Oil Cooler | Refer to Procedure 007-003 | QSX15 CM2350 X105 | 4332667 |
| Lubricating Oil Cooler | Refer to Procedure 007-003 | QSX15 CM2350 X106 | 4332712 |
| Lubricating Oil Cooler Element | Refer to Procedure 007-007 | ISX15 CM2250 | 4022250 |
| Lubricating Oil Cooler Element | Refer to Procedure 007-007 | ISX15 CM2250 SN | 4310736 |
| Lubricating Oil Cooler Element | Refer to Procedure 007-007 | ISX12/ISX11.9 CM2250 | 2883445 |
| Lubricating Oil Cooler Element | Refer to Procedure 007-007 | ISX15 CM2350 X101 | 4310641 |
| Lubricating Oil Cooler Element | Refer to Procedure 007-007 | QSX15 CM2250 ECF | 2883557 |
| Lubricating Oil Cooler Element | Refer to Procedure 007-007 | QSX11.9 CM2250 ECF | 2883561 |
| Lubricating Oil Cooler Element | Refer to Procedure 007-007 | QSX15 CM2350 X105 | 4332667 |
| Lubricating Oil Cooler Element | Refer to Procedure 007-007 | QSX15 CM2350 X106 | 4332712 |
| Lubricating Oil Filter (Spin-On) | Refer to Procedure 007-013 | ISX15 CM2250 | 4022250 |
| Lubricating Oil Filter (Spin-On) | Refer to Procedure 007-013 | ISX15 CM2250 SN | 4310736 |
| Lubricating Oil Filter (Spin-On) | Refer to Procedure 007-013 | ISX12/ISX11.9 CM2250 | 2883445 |
| Lubricating Oil Filter (Spin-On) | Refer to Procedure 007-013 | ISX15 CM2350 X101 | 4310641 |
| Lubricating Oil Filter (Spin-On) | Refer to Procedure 007-013 | QSX15 CM2250 ECF | 2883557 |
| Lubricating Oil Filter (Spin-On) | Refer to Procedure 007-013 | QSX11.9 CM2250 ECF | 2883561 |
| Lubricating Oil Filter (Spin-On) | Refer to Procedure 007-013 | QSX15 CM2350 X105 | 4332667 |
| Lubricating Oil Filter (Spin-On) | Refer to Procedure 007-013 | QSX15 CM2350 X106 | 4332712 |
| Lubricating Oil System | Refer to Procedure 007-037 | ISX15 CM2250 | 4022250 |
| Lubricating Oil System | Refer to Procedure 007-037 | ISX15 CM2250 SN | 4310736 |
| Lubricating Oil System | Refer to Procedure 007-037 | ISX12/ISX11.9 CM2250 | 2883445 |
| Lubricating Oil System | Refer to Procedure 007-037 | ISX15 CM2350 X101 | 4310641 |
| Lubricating Oil System | Refer to Procedure 007-037 | QSX15 CM2250 ECF | 2883557 |
| Lubricating Oil System | Refer to Procedure 007-037 | QSX11.9 CM2250 ECF | 2883561 |
| Lubricating Oil System | Refer to Procedure 007-037 | QSX15 CM2350 X105 | 4332667 |
| Lubricating Oil System | Refer to Procedure 007-037 | QSX15 CM2350 X106 | 4332712 |
| Lubricating Oil Filter Bypass Valve | Refer to Procedure 007-014 | ISX15 CM2250 | 4022250 |
| Lubricating Oil Filter Bypass Valve | Refer to Procedure 007-014 | ISX15 CM2250 SN | 4310736 |
| Lubricating Oil Filter Bypass Valve | Refer to Procedure 007-014 | ISX12/ISX11.9 CM2250 | 2883445 |
| Lubricating Oil Filter Bypass Valve | Refer to Procedure 007-014 | ISX15 CM2350 X101 | 4310641 |
| Lubricating Oil Filter Bypass Valve | Refer to Procedure 007-014 | QSX15 CM2250 ECF | 2883557 |
| Lubricating Oil Filter Bypass Valve | Refer to Procedure 007-014 | QSX11.9 CM2250 ECF | 2883561 |
| Lubricating Oil Filter Bypass Valve | Refer to Procedure 007-014 | QSX15 CM2350 X105 | 4332667 |
| Lubricating Oil Filter Bypass Valve | Refer to Procedure 007-014 | QSX15 CM2350 X106 | 4332712 |
| Lubricating Oil and Filter Analysis | Refer to Procedure 007-083 | ISX15 CM2250 | 4022250 |
| Lubricating Oil and Filter Analysis | Refer to Procedure 007-083 | ISX15 CM2250 SN | 4310736 |
| Lubricating Oil and Filter Analysis | Refer to Procedure 007-083 | ISX12/ISX11.9 CM2250 | 2883445 |
| Lubricating Oil and Filter Analysis | Refer to Procedure 007-083 | ISX15 CM2350 X101 | 4310641 |
| Lubricating Oil and Filter Analysis | Refer to Procedure 007-083 | QSX15 CM2250 ECF | 2883557 |
| Lubricating Oil and Filter Analysis | Refer to Procedure 007-083 | QSX11.9 CM2250 ECF | 2883561 |
| Lubricating Oil and Filter Analysis | Refer to Procedure 007-083 | QSX15 CM2350 X105 | 4332667 |
| Lubricating Oil and Filter Analysis | Refer to Procedure 007-083 | QSX15 CM2350 X106 | 4332712 |
| Lubricating Oil Thermostat | Refer to Procedure 007-039 | ISX15 CM2250 | 4022250 |
| Lubricating Oil Thermostat | Refer to Procedure 007-039 | ISX15 CM2250 SN | 4310736 |
| Lubricating Oil Thermostat | Refer to Procedure 007-039 | ISX12/ISX11.9 CM2250 | 2883445 |
| Lubricating Oil Thermostat | Refer to Procedure 007-039 | ISX15 CM2350 X101 | 4310641 |
| Lubricating Oil Thermostat | Refer to Procedure 007-039 | QSX15 CM2250 ECF | 2883557 |
| Lubricating Oil Thermostat | Refer to Procedure 007-039 | QSX11.9 CM2250 ECF | 2883561 |
| Lubricating Oil Thermostat | Refer to Procedure 007-039 | QSX15 CM2350 X105 | 4332667 |
| Lubricating Oil Thermostat | Refer to Procedure 007-039 | QSX15 CM2350 X106 | 4332712 |
| Aftertreatment Testing | Refer to Procedure 014-013 | ISX15 CM2250 | 4022250 |
| Aftertreatment Testing | Refer to Procedure 014-013 | ISX12/ISX11.9 CM2250 | 2883445 |
| Aftertreatment Testing | Refer to Procedure 014-013 | QSX15 CM2250 ECF | 2883557 |
| Aftertreatment Testing | Refer to Procedure 014-013 | QSX11.9 CM2250 ECF | 2883561 |
| Main Bearings | Refer to Procedure 001-006 | ISX15 CM2250 | 4022250 |
| Main Bearings | Refer to Procedure 001-006 | ISX15 CM2250 SN | 4310736 |
| Main Bearings | Refer to Procedure 001-006 | ISX12/ISX11.9 CM2250 | 2883445 |
| Main Bearings | Refer to Procedure 001-006 | ISX15 CM2350 X101 | 4310641 |
| Main Bearings | Refer to Procedure 001-006 | QSX15 CM2250 ECF | 2883557 |
| Main Bearings | Refer to Procedure 001-006 | QSX11.9 CM2250 ECF | 2883561 |
| Main Bearings | Refer to Procedure 001-006 | QSX15 CM2350 X105 | 4332667 |
| Main Bearings | Refer to Procedure 001-006 | QSX15 CM2350 X106 | 4332712 |

### Document History
