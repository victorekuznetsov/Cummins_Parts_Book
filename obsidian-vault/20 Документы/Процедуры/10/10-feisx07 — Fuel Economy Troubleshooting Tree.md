---
type: "Процедура"
doc: "10-feisx07"
title_en: "Fuel Economy Troubleshooting Tree"
modified: "2015-07-08"
engines:
  - "80141463"
  - "80248213"
families:
  - "QSX15"
manuals:
  - "3666239"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/10/10-feisx07.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/10-feisx07.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSX15"
  - "группа/10"
---

# Fuel Economy Troubleshooting Tree

> [!abstract] Процедура · `10-feisx07`
> **Двигатели:** [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSX15
> **Входит в руководства:** [[3666239 — Signature™, ISX, and QSX15 Service Manual|3666239]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2015-07-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/10/10-feisx07.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/10-feisx07.pdf)

Printable Version

### Symptoms

Fuel Consumption Excessive

### How To Use This Tree

This symptom tree is to be used to troubleshoot fuel economy complaints. This tree is used along with the Fuel Consumption Customer Complaint Form and the Driveability Low Power/Excessive Fuel Consumption Checklist to help isolate engine, chassis, or driver issues associated with excessive fuel consumption.

### Shoptalk

The Fuel Consumption General Information section of this manual and Troubleshooting Excessive Fuel Consumption, Bulletin [[3666094 — Excessive Fuel Consumption Troubleshooting|3666094]], should be referenced prior to any troubleshooting being performed on a customer's engine.

The cause of excessive fuel consumption is difficult to diagnose and correct because of the potential number of factors involved. Actual fuel consumption problems can be caused by any of the following factors:

- Engine factors

- Vehicle factors and specifications

- Environmental factors

- Driver technique and operating practices

- Fuel system factors

- Low power or driveability problems.

Before troubleshooting, it is important to determine the exact complaint. Is the complaint based on whether the problem is real or perceived, or does **not** meet driver expectations? The Fuel Consumption Customer Complaint Form is a valuable list of questions that can be used to assist the service technician in determining the cause of the problem. Complete the form before troubleshooting the complaint. The following are some of the factors that **must** be considered when troubleshooting fuel consumption complaints.

- Excessive idling time: Idling the engine can use from 0.5 to 1.5 gallons per hour depending on the engine idle speed.

- Vehicle Aerodynamics: The largest single power requirement for a truck is the power needed to overcome air resistance. As a general rule, each 10 percent reduction in air resistance results in a 5 percent increase in mile per gallon.

- Rolling Resistance: Rolling resistance is the second largest consumer of power on a truck. The type of tire and tread design have a sizeable effect on fuel economy and performance. Changing from a bias ply to a low profile radial tire can reduce rolling resistance by about 36 percent.

- Environmental and Seasonal Weather Changes: There can be as much as 1 to 1.5 mile per gallon difference in fuel consumption, depending on the season and the weather conditions.

- Truck Route and Terrain: East and west routes experience almost continual crosswinds and head winds. Less fuel can be used on north and south routes where parts of the trip are **not** only warmer, but have less wind resistance.

- Driver Technique and Operating Practices: A 1 mile per hour increase in road speed equals a 0.1 mile per gallon increase in fuel consumption. This means that increasing road speed from 50 to 60 mph will result in a loss of fuel mileage of 1 mpg.

- Result of a Low Power or Driveability Problem: An operator will change driving style to compensate for a low power or driveability problem. Some things the driver is likely to do are (a) shift to a high engine rate per minute (rpm) or (b) run on the droop curve in a lower gear instead of upshifting to drive at part-throttle conditions. These changes in driving style will increase the amount of fuel used.

Additional vehicle factors, vehicle specifications and axle alignment, can also affect fuel consumption. For additional information on troubleshooting fuel consumption complaints, refer to Troubleshooting Excessive Fuel Consumption, Bulletin 3387245.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Verify the complaint. |  |
|  | **STEP 1A.** Fill out the Fuel Consumption Customer Complaint Form. | N/A |
| STEP 2. | Electronic checks using INSITE™ electronic service tool. |  |
|  | **STEP 2A.** Check for fault codes. | N/A |
|  | **STEP 2B.** Confirm Features and Parameters. | N/A |
|  | **STEP 2C.** Check the engine control module (ECM) calibrations. | N/A |
|  | **STEP 2D.** Monitor vehicle speed. | N/A |
|  | **STEP 2D-1.** Inspect the engine and chassis grounds. | N/A |
| STEP 3. | Check engine performance. |  |
|  | **STEP 3A.** Engine performance troubleshooting. | N/A |

### STEP 1. Verify the complaint.

#### STEP 1A. Fill the Fuel Consumption Customer Complaint Form.

| **Conditions:** N/A |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Fill out the Fuel Consumption Customer Complaint Form in the Troubleshooting and Repair Manual, ISC, QSC8.3, ISL and QSL9 Engines, Bulletin 4021418. N/A | Problem caused by vehicle factors, environmental factors, or driver technique? **YES** | Repair complete |
| Problem caused by vehicle factors, environmental factors, or driver technique? **NO** | 2A |  |

### STEP 2. Electronic checks using INSITE™ electronic service tool.

#### STEP 2A. Check for fault codes.

| **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Use INSITE™ electronic service tool to read the fault codes. N/A | Any active or high counts of inactive fault codes? **YES** | Troubleshoot fault codes |
| Any active or high counts of inactive fault codes? **NO** | 2B |  |

#### STEP 2B. Confirm Features and Parameters.

| **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Confirm the Programmable Features and Parameters are set correctly. N/A | Features and Parameters set correctly? **YES** | 2C |
| Features and Parameters set correctly? **NORepair:** Reset the Features and Parameters to their appropriate values. | Repair complete |  |

#### STEP 2C. Check the ECM calibration.

| **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Compare the ECM code with the engine rating and control parts list (CPL). Verify the calibration is correct. N/A | Calibration correct? **YES** | 2D |
| Calibration correct? **NORepair:** Recalibrate the ECM with the correct ECM code. | Repair complete |  |

#### STEP 2D. Monitor vehicle speed.

| **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Monitor vehicle speed with INSITE™ electronic service tool while the vehicle is not moving. N/A | Vehicle speed read 0 when the vehicle is not moving? **YES** | 3A |
| Vehicle speed read 0 when the vehicle is not moving? **NO** | 2D-1 |  |

#### STEP 2D-1. Inspect the engine and chassis grounds.

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for loose or corroded engine, chassis, or battery ground connection. Check the engine ground connection Check the chassis ground connections Check the battery terminal connections. | All grounds present, properly grounded, free of corrosion, and tight? **YESRepair:** Check the vehicle speed sensor (VSS) and the VSS circuit. [[99-019-091 — Vehicle Speed Sensor, Magnetic Pick Up\|Refer to Procedure 019-091 in Section 19]]. | Repair complete |
| All grounds present, properly grounded, free of corrosion, and tight? **NORepair:** Replace, clean, or tighten the grounds. | Repair complete |  |

### STEP 3. Check engine performance.

#### STEP 3A. Engine performance troubleshooting.

| **Conditions:** N/A |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Perform the Fuel System Checks, Air Handling Checks, and Base Engine Checks in the Engine Performance Troubleshooting Tree. N/A | Poor fuel economy complaint still exists? **YESRepair:** Perform the Fuel System Checks, Air Handling Checks, and Base Engine Checks in the Engine Performance Troubleshooting Tree. | Repair complete |
| Poor fuel economy complaint still exists? **NO** | Repair complete |  |
