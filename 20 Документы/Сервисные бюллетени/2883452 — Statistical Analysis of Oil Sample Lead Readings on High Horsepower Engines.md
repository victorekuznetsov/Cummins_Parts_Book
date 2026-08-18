---
aliases:
  - "Статистический анализ содержания свинца в пробах масла двигателей большой мощности"
type: "Сервисный бюллетень"
doc: "2883452"
title_en: "Statistical Analysis of Oil Sample Lead Readings on High Horsepower Engines"
title_ru: "Статистический анализ содержания свинца в пробах масла двигателей большой мощности"
released: "2010-04-23"
modified: "2021-08-11"
group: "07 - Lubricating Oil Systems"
engines:
  - "33239746"
  - "33239899"
  - "41349633"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
  - "QSK19"
figures: 2
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/bulletin/2883452.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/bulletin/2883452.pdf"
tags:
  - "документ/бюллетень"
  - "двигатель/K38/K50"
  - "двигатель/QSK19"
  - "тема/lubricating-oil-systems"
---

# Statistical Analysis of Oil Sample Lead Readings on High Horsepower Engines
**Статистический анализ содержания свинца в пробах масла двигателей большой мощности**

> [!abstract] Сервисный бюллетень · `2883452`
> **Раздел Cummins:** 07 - Lubricating Oil Systems
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]], [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60, QSK19
> **Даты:** выпущен 2010-04-23 · изменён 2021-08-11
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/bulletin/2883452.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/bulletin/2883452.pdf)

## Statistical Analysis of Oil Sample Lead Readings on High Horsepower Engines

## Introduction

This Service Bulletin is an extension to Service Bulletin 4022060, Oil Analysis Techniques for High Horsepower Diesel Engines. It provides additional guidelines for the analysis of oil sample results acquired using the techniques detailed in Service Bulletin 4022060 for QSK45, QSK60, and QSK78 engines.

Investigation and operating procedures recommended in this procedure should be conducted in line with the oil analysis techniques to collect an oil sample, set oil analysis flag limits, and identify and take appropriate corrective action; based on oil analysis results outlined in Service Bulletin 4022060.

The additional guidelines in this document allow for the identification of elevated bearing wear within an engine, throughout its operating life. This information can be used to help plan an appropriate life to rebuild.

Oil analysis data collected over a period of time can provide significant information about the level of main and connecting rod bearing wear. Oil analysis testing is recommended throughout the engine life.

## Oil Sample Result Analysis Guidelines

These guidelines help to identify operations which have higher bearing wear than expected. This helps the operator in planning and reviewing for optimum maintenance and operation.

The wear metal discussed in this analysis is lead. An increased, or overall elevated level of lead may indicate a potential issue with main or connecting rod bearings and can result in reduced engine life. By plotting all the values for lead oil analysis results for an engine and calculating the statistical third quartile, the expected degree of bearing wear can be reviewed, and engine life expectations reviewed accordingly.

Quartiles are values that divide a sample of data into four equal parts. They are commonly used to describe data sets. The data is sorted in ascending order.

| Quartile | Description |
|---|---|
| First (Q1) | 25 percent of the data is less than or equal to this value. |
| Second (Q2) | The median. 50 percent of the data is less than or equal to this value. |
| Third (Q3) | 75 percent of the data is less than or equal to this value. |

For example, for the following data: 7, 16, 36, 39, 45, 46, 48, 52, 57

- Q1 = 36
- Q2 (median) = 45
- Q3 = 48

Examples of how to calculate the third quartile using Minitab® and Microsoft Excel® are shown in Examples 1 and 2, below.

All lead data throughout the full life of the bearings **must** be used for the third quartile calculation.

Table 1 lists the recommended third quartile lead flag limits and appropriate actions for QSK45 and QSK60 engines.

Table 2 lists the recommended third quartile lead flag limits and appropriate actions for QSK78 engines.

Table 3 lists additional investigation items for high lead levels.

| Table 1, QSK45 and QSK60 Third Quartile Lead Limits |  |  |  |
|---|---|---|---|
| Third quartile for ppm lead in oil analysis | Indication | Action | Comment |
| Below 5 ppm lead | Minimal bearing wear | None. | Engine life is **not** limited by bearing life. |
| Over 5 ppm lead | Bearing wear - monitor | Investigate causes of bearing wear. | Engine life is significantly impacted by bearing. |
| Over 10 ppm lead | High bearing wear | Investigate causes of bearing wear. | Engine life is significantly impacted by bearing. |
| Over 20 ppm lead | Significant bearing wear | Investigate causes of bearing wear. | Very high bearing wear. |

| **Table 2 QSK78 Third Quartile Lead Limits** |  |  |  |
|---|---|---|---|
| **Third quartile for ppm lead in oil analysis** | **Indication** | **Action** | **Comment** |
| Below 2 ppm lead | Minimal bearing wear | None. | Engine life is **not** limited by bearing life. |
| Over 2 ppm lead | Bearing wear - monitor | Investigate causes of bearing wear. | Engine life is significantly impacted by bearing. |
| Over 4 ppm lead | High bearing wear | Investigate causes of bearing wear. | Engine life is significantly impacted by bearing. |
| Over 6 ppm lead | Significant bearing wear | Investigate causes of bearing wear. | Very high bearing wear. |

## Items for investigation for engines which are found to have high bearing wear

The areas below should be investigated, in conjunction with the troubleshooting trees, for lead found in the table titled “Lead parts per million (PPM) level exceeds critical lead flag limit based on oil lab results or Cummins Inc. limits” in the following service bulletin. Refer to the Oil Analysis Techniques for High Horsepower Diesel Engines, Service Bulletin [[4022060 — Oil Analysis Techniques for High Horsepower Diesel Engines|4022060]].

| Table 3 |  |  |
|---|---|---|
| Investigation Item | Action | Criteria |
| Prelube operation | Check the prelube system is operating correctly. | Make sure the engine oil pressure reaches 31 kpa \[4.5 psi\] prior to cranking. |
|  | Check that the correct pressure switch is fitted. | Compare to the QSOL parts catalog. |
| Starter operation | Check that the starting system is functioning correctly. | Make sure the engine cranking speed is above 150 rpm, even in cold ambient conditions. |
| Centinel™ operation, if installed | Check that Centinel™ is correctly enabled on the calibration. | Review the features and parameters in INSITE™ electronic service tool. |
|  | Check that Centinel™ is operating correctly. | Review, add oil records, and verify that oil added is 0.3% of the fuel burned. |
| Eliminator™ operation | Check that the hydraulic motor is operating correctly. | View the rotation of the hydraulic motor, per the Maintenance Procedures in the Operation and Maintenance Manual, for the engine being serviced. |
|  | Check that the centrifuge is operating correctly. | Inspect the centrifuge, per the Maintenance Procedures in the Operation and Maintenance Manual, for the engine being serviced. |
| Oil change procedure | Check that all used oil is correctly drained out at oil change. | Reference the Maintenance Procedures in the Operation and Maintenance Manual for the engine being serviced. |
|  | Check that all used oil is correctly drained out of the reserve tank, if installed. | Completely drained and refilled at oil change with new, clean oil. |
|  | Check that the oil change interval adheres to published Cummins Inc. guidelines. | Reference the Maintenance Schedule in the Operation and Maintenance Manual for the engine being serviced. |
|  | Check that oil filters are changed at the specified interval. The use of Centinel™ does **not** preclude the need to change filters. | Reference the Maintenance Schedule in the Operation and Maintenance Manual for the engine being serviced. |
|  | Confirm the reserve oil system volume is filled to the manufacturer's limits, and vented correctly. | Reference the reserve oil system manufacturer's recommendations. |
|  | Confirm the specification of oil meets Cummins Inc. recommendations. | Reference the Cummins® Engine Oil and Oil Analysis Recommendations, Service Bulletin [[3810340 — Cummins® Engine Oil and Oil Analysis Recommendations\|3810340]]. |
|  | Confirm the oil level is checked daily and **always** remains between high and low limits, even after operating all day. | Check 15 minutes after the engine is keyed OFF to allow engine oil to drain back to the sump. |
| Main bearing material condition | Review the main bearing for excessive wear. | Reference Section 2 of the Parts Reuse Guidelines, Service Bulletin [[3810303 — Parts Reuse Guidelines\|3810303]], for inspection reference. |
| Cylinder block, crankshaft geometry (rebuilds **only**) | Confirm the crankshaft bore in the cylinder block and crankshaft journal meet reuse guidelines. | Reference the Cylinder Block Section in the Service Manual for the engine being serviced. |
| Coolant temperature | Confirm that the operating coolant temperature does **not** exceed limits. | Review INSITE™ electronic service tool engine protection logs. |
|  | Correct any cooling system deficiencies, as needed. | Make sure of proper regular cleaning and maintenance. |
|  | Check for coolant leaks into the oil through oil sampling. | Identify the water and coolant additive concentrations in oil samples. Reference the Cummins® Engine Oil and Oil Analysis Recommendations, Service Bulletin [[3810340 — Cummins® Engine Oil and Oil Analysis Recommendations\|3810340]]. |
| Fuel system | Check for fuel leaks into the oil through oil sampling. | Reference the fuel dilution specifications in the Cummins® Engine Oil and Oil Analysis Recommendations, Service Bulletin [[3810340 — Cummins® Engine Oil and Oil Analysis Recommendations\|3810340]]. |
| Transient operation and load factor | Check that there are no unusual overspeed elements in the operation. | Review the INSITE™ electronic service tool engine protection logs. |
|  | Check the load factor. | If the load factor is 80 percent (or more) than expected, the rebuild schedule should be reviewed. |
|  | Check for damaged bearings from earlier, off-design conditions. | Pull the main capscrews and perform a thorough inspection. |
| Vibration | Confirm there is no trunnion or engine mount damage, nor bright markings on “end stops”. | Damage in these locations indicates excessive engine motion. Reference the Vibration Excessive Troubleshooting Symptom Tree in Section TT of the engine being serviced. |

## Example 1: Calculating the third quartile using Minitab®

![[07601303.png]]

Figure 1, Summary of Lead Throughout Life.

Above is an example where the lead levels in parts per million has been plotted for all the readings throughout operating life to rebuild for an engine. The value of lead at the third quartile for this example is 10 ppm.

## Example 2: Calculating the third quartile using Microsoft® Excel

![[07r00249.png]]

Figure 2, Example of the Third Quartile Calculated in Microsoft® Excel.

The third quartile can be calculated in Microsoft Excel® using the QUARTILE (pre-Excel 2007) or QUARTILE.INC (Excel 2007 and up) function. Type the following in a cell:

- =QUARTILE(\[Cell range\],3)
- =QUARTILE.INC(\[Cell range\],3)

Where \[Cell Range\] refers to the cells containing wear metal sample data.

The value of lead at the third quartile for this example is 7 ppm.

### Document History
