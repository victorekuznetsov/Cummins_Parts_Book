---
aliases:
  - "Интерпретация результатов анализа масла"
type: "Процедура"
doc: "00-378-013"
title_en: "Engine Oil Analysis Interpretation"
title_ru: "Интерпретация результатов анализа масла"
modified: "2025-12-11"
engines:
  - "33239746"
  - "33239899"
  - "37292556"
  - "37295879"
  - "41343322"
  - "41349633"
  - "93058669"
families:
  - "C8.3 · 6C8.3"
  - "K38/K50 · QSK38, QSK50, QSK60"
  - "NT/NTA855 · ISM/QSM11"
  - "QSK19"
  - "QST30"
manuals:
  - "5411406"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/00/00-378-013.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/00-378-013.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "двигатель/K38/K50"
  - "двигатель/NT/NTA855"
  - "двигатель/QSK19"
  - "двигатель/QST30"
  - "группа/00"
---

# Engine Oil Analysis Interpretation
**Интерпретация результатов анализа масла**

> [!abstract] Процедура · `00-378-013`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]], [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]], [[41343322 — NH NT 855 CPL 3362|41343322]], [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[93058669 — 6C8.3 CPL 3105|93058669]]
> **Семейство:** C8.3 · 6C8.3, K38/K50 · QSK38, QSK50, QSK60, NT/NTA855 · ISM/QSM11, QSK19, QST30
> **Входит в руководства:** [[5411406 — Fluids for Cummins® Products Service Manual|5411406]]
> **Секции:** Section 4 - Engine Oil
> **Даты:** изменён 2025-12-11
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/00/00-378-013.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/00-378-013.pdf)

### General Information

Understanding the oil system is crucial to identifying when an oil sample is indicating a problem. Large oil system capacity, use of Centinel™ oil replenishment systems, and use of Eliminator™ or centrifuge-type filtration systems will result in overall lower contamination levels, compared to an engine that has a standard sump capacity, **no** replenishment system, and standard oil filters.

System capacity can be determined by knowing the volume of the oil required to touch the high-level mark on the dipstick and the volume of any remote oil tanks on the machine in which oil is continuously circulated. Oil sump capacities are listed in the Owners/Operation and Maintenance Manual for all Cummins® engines. If the machine is equipped with an oil reserve system with a reservoir remote from the engine oil sump, the reservoir volume **must** be added to the engine sump volume to determine the total system capacity. This is **only** true for remote tanks in which the oil is continuously circulated. The Centinel™ make-up tank volume does **not** add to system capacity, since the engine oil is **not** continuously circulated through this tank.

The addition of new oil will also decrease the amount of contamination in a particular volume of oil. In all cases, oil consumption **must** be documented by the amount of oil added between each service interval. Trending oil consumption is important, as any rising trend or step change in oil consumption can indicate possible power cylinder wear, system leaks, or other system malfunction.

### Flag Limits

The purpose of flag limits is to identify adverse trends in oil analysis that require further investigation. The guidelines provided in this procedure are **not** to be used to extend oil drain intervals. If a flag limit is reached, contact your local Cummins® service provider.

One way to compensate for the differences in oil systems between units is to look at the normal wear rates for each engine individually. This method establishes a baseline specific to that particular engine. Provided the oil usage remains fairly constant and other systems are functioning consistently, the trends in wear metals should remain consistent.

For example, setting up statistical flag limits based on a large group will normalize the data. If an engine historically had very low rates of wear, but suddenly jumps to a higher wear rate that is consistent with the average wear rate for the group of engines being analyzed, no flag would be triggered. In comparison, looking at historical readings on a particular unit can cause action to be taken at a lower contaminant level.

Cummins Inc. recommends working with an oil analysis lab to establish warning and critical flag limits using ASTM method D7720-11. If samples are taken periodically throughout the oil drain interval, the oil parameter value can be converted into a rate of increase over new oil. For example, parts per million (ppm) per mile (or hour).

As a guideline, engines should be grouped in the following ways for statistical limit comparison.

- Service Model Name
- Application
- Similar Duty Cycles
- With Centinel™ and without Centinel™
- With Eliminator™ or centrifuge-type filtration and with standard filter configurations
- Common oil system capacities.

If all engines are grouped together regardless of oil systems, the engines with Centinel™, Eliminator™/centrifuge-type filtration, and higher oil system capacities will experience a higher degree of engine wear before the flag limit is reached.

| Table 1: Lubricating Oil Analysis Limits |  |
|---|---|
| Oil Analysis Parameter | Limit |
| **Diesel and Natural Gas** |  |
| Viscosity change at 100°C \[212°F\] (American Society of Testing and Materials (ASTM) D445) | For xW-40 - MIN: 12.5, MAX: 16.3 For xW-30 - MIN: 9.3, MAX: 12.5 |
| Fuel Dilution | 5 percent MAX |
| **Gasoline** |  |
| Viscosity change at 100°C \[212°F\] (American Society of Testing and Materials (ASTM) D445) | For xW-30 - MIN: 7.5, MAX: 12.5 |
| Fuel Dilution | 12 percent MAX |

| Table 2: Oil Contamination Guidelines for Soot |  |  |
|---|---|---|
| Cummins® Engineering Standard (CES) | Midrange B and C Soot Limit | All Other Engines Soot Limit |
| CES 20076, 20077, 20078, 20081, 20086, 20087, and 20088 | 3.0 percent MAX | 5.0 percent MAX |
| CES 20075 | 1.5 percent MAX | 1.5 percent MAX |

| Table 3: Oil Contamination Limits for Total Base Number (TBN) |  |  |
|---|---|---|
|  | Engines ≤ 19L Displacement | Engines ≥ 19L Displacement |
| Total base number (ASTM) D4739 | 2.5 MIN | 2.5 MIN or equal to TAN |

> [!note] Note · Примечание
> Table 4 should **only** be used as a reference if flag limits cannot be established through statistical analysis.

| Table 4: Lubricating Oil Analysis Guidelines |  |
|---|---|
| Oil Analysis Parameter | Limit |
| Water content (ASTM D6304) | 3000 parts per million (ppm) or 0.3 percent MAX |
| Silicon (SI) | 15 ppm increase over new oil |
| Sodium (Na) | 20 ppm increase over new oil |
| Boron (B) | 25 ppm increase over new oil |
| Potassium (K) | 20 ppm increase over new oil |
| Copper (CU) | 30 ppm increase over new oil |
| Iron (FE) | 80 ppm increase over new oil |
| Aluminum (AL) | 20 ppm increase over new oil |

[[00-378-014 — 17 Liter and Up Diesel Engine Oil Analysis|Refer to Procedure 378-014]] in Section 4 for specific recommendations on 17 Liter and Up Diesel Engine Oil Analysis.

### Interpreting Results

The tables below are intended to serve as a guide for investigating oil analysis results. Table 5 provides information related to instances of high wear metals or oil contaminants from analysis results and potential sources of those contaminants. Table 6 provides information related to combinations of wear metals and/or contaminants and associated engine problems that can cause those results.

| Table 5: Sources of Wear Metals or Contaminants |  |
|---|---|
| Aluminum (AL) | Pistons (some applications), crankshaft and camshaft thrust bearings, camshaft bushings, dirt, heat exchanger cooler brazing flux, connecting rod and main bearings, camshaft and gear train bushings |
| Copper (Cu) | Connecting rod and main bearings, turbocharger bearings, connecting rod bushings, camshaft bushings, idler gear and accessory drive bushings and thrust washers, cam follower pins, rocker lever bushings, lube pump bushings and thrust washers, copper brazed oil coolers |
| Fuel | Unburned fuel in lubricating oil, injectors, or fuel pump can be source of contamination. Engine operation, such as frequent starts, excessive idling, and cold weather operation can also lead to fuel dilution. |
| Iron (Fe) | Cylinder liner, pistons (some applications), gears, crankshaft, camshaft, camshaft follower rollers and shafts |
| Lead (Pb) | Some applications: Rod and main bearings, turbocharger bearings, camshaft bushings, idler gear and accessory drive bushings and thrust washers, lube pump bushings and thrust washers |
| Potassium (K) | Element contained in some coolant additive packages, which indicates coolant contamination of oil, heat exchanger cooler brazing flux |
| Silicon (Si) | Sand, dirt, silicon sealants and gasket materials, oil additives, cooling system inhibitor |
| Sodium (Na) | Element contained in some coolant additive packages which indicates coolant contamination of oil, salt from detergent or road, oil additive |
| Viscosity | The property of a fluid measured at a certain temperature that resists the force to cause the fluid to flow. Viscosity can increase after thermal degradation and can decrease with mechanical shear. |
| Total Acid Number (TAN) | A measure of oil's acidity. New oil has a certain level, or starting TAN, due to the type and amount of additives. |
| Total Base Number (TBN) | A measure of the oil's ability to neutralize acid. New oil has a certain level in the oil formula that is depleted over time due to contact with acid generated by blowby gases. |
| Soot | Combustion by-products in oil. Excessive soot can suggest issues with the fuel system or combustion. |
| Oxidation | A generic measure of the breakdown of a lubricant due to age and exposure to high temperature. High oxidation numbers indicate oil is beyond its useful life. |
| Nitration | A generic indicator of excessive "blowby" and also indicates the presence of nitric acid formed by nitric oxide, which is a combustion by-product when the engine operates too lean. Nitric acid can attack metal surfaces in the engine and result in corrosive wear. Nitric acid can accelerate oil oxidation. |

| Table 6: Engine Problems That Result in Oil Analysis Flags |  |
|---|---|
| Fuel Dilution | The best indicators of fuel dilution are an increased percentage of fuel in the oil and a decrease in viscosity. In cases of high fuel dilution, the oil can smell like fuel and the engine oil level may increase. |
| Coolant Contamination | The best method to detect coolant contamination of oil is to look for traces of elements, such as sodium and potassium, which are contained in the coolant additive package. These elements can be detected at very low levels, so they can serve as an early warning. Sodium is occasionally found in lubricant additive packages; therefore, it is important to compare the level of sodium with that measured in the baseline (unused) oil sample and to be aware of the coolant additive package formulation. A water content test is **not** a reliable indicator of a coolant leak because oil temperatures are generally higher than the boiling point of water, which allows the water to boil out during normal engine operation, leaving behind **only** the elements that make up the coolant additive package. Glycol tests can also be inaccurate. Small amounts of glycol may **not** be measurable, and high oil temperatures can break down glycol to a state where it will **not** be detected. In addition to identifying the source of coolant contamination, it is important to determine if progressive damage has occurred. Coolant contamination of the lubricating oil can damage bearings and bushings. |
| Dust Out | Dirt is composed primarily of silica and alumina, so elevated levels of silicon and aluminum in a 2-to-1 to 10-to-1 silicon-to-aluminum ratio indicate dirt intrusion. In addition to identifying the source of dirt entry, it is important to determine if progressive damage has occurred. A dust out can cause piston ring/cylinder liner wear, which can lead to lubricating oil contamination or a breakdown of the lubricating oil properties and bearing/bushing failures. |
| Piston Ring/Cylinder Liner Wear | Increased levels of iron indicate cylinder liner wear. Additionally, wear of the rings and/or liner can allow blowby gases to pass by the rings and contaminate the oil. Elevated levels of soot, oxidation, and nitration, along with an increase in viscosity, can be observed. Contamination of the oil will also increase total acid number and decrease total base number. In addition to identifying the source of coolant contamination, it is important to determine if progressive damage has occurred. Contaminated lubricating oil can damage bearings and bushings. |
| Bearing/Bushing Malfunction | Leaded bearings are made up primarily of lead and copper. An increased level of both these metals at the same time can indicate a malfunction of a bearing and/or bushing. An increase of lead with no increase in copper typically corresponds to a degradation of oil condition that results in attack of the top layer of the bearing. Some other indications of degraded oil can include increases in oxidation, nitration, TAN, and/or a decrease in TBN. Lead free bearings will show increases in elements such as copper, bismuth, aluminum, and tin. |
