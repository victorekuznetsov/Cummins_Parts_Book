---
aliases:
  - "Масляный фильтр (навинчиваемый)"
type: "Процедура"
doc: "56-007-013-tr"
title_en: "Lubricating Oil Filter (Spin-On)"
title_ru: "Масляный фильтр (навинчиваемый)"
modified: "2013-06-04"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
families:
  - "QSK60"
manuals:
  - "4021530"
figures: 20
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/56/56-007-013-tr.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/56-007-013-tr.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK60"
  - "группа/56"
---

# Lubricating Oil Filter (Spin-On)
**Масляный фильтр (навинчиваемый)**

> [!abstract] Процедура · `56-007-013-tr`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]]
> **Семейство:** QSK60
> **Входит в руководства:** [[4021530 — QSK45 and QSK60 Service Manual|4021530]]
> **Секции:** Section 7 - Lubricating Oil System - Group 07
> **Даты:** изменён 2013-06-04
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/56/56-007-013-tr.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/56-007-013-tr.pdf)

### Remove

> [!danger] WARNING · Опасно
> To reduce the possibility of personal injury, avoid direct contact of hot oil with your skin.

> [!danger] WARNING · Опасно
> Some state and federal agencies have determined that used engine oil can be carcinogenic and cause reproductive toxicity. Avoid inhalation of vapors, ingestion, and prolonged contact with used engine oil. If not reused, dispose of in accordance with local environmental regulations.

The QSK45 engine has three combination oil filters and the QSK60 has four combination oil filters.

Use an oil filter wrench, Part Number 3375049 or equivalent, to remove the oil filters.

Discard the filters if **not** required for failure analysis.

![[07600230.png]]

Some QSK60 Power Generation engines have an oil by-pass line from the PRELUB™ to the fuel pump acccessory drive with a small oil filter installed.

Use an oil wrench, Part Number 3400158 or equivalent, to remove the oil filter, if applicable.

Discard the filter if **not** required for failure analysis.

![[07500014.png]]

### Inspect

> [!danger] WARNING · Опасно
> Carefully cut the combination oil filter open. The filter element spring is under compression and can cause personal injury.

Use tube cutter, Part Number 3376579, to open the full-flow oil filter.

Inspect the filter element for evidence of moisture and metal particles.

If metallic debris is found, the lube pump idler shaft and gear **must** be carefully inspected for damage. [[56-007-031-tr — Lubricating Oil Pump|Refer to Procedure 007-031 in Section 7.]]

| Metal | Probable Source |
|---|---|
| Copper | Bearings and bushings |
| Chromium | Piston rings |
| Iron | Cylinder liners, gears, and camshafts |
| Lead | Bearing overlay material |
| Aluminum | Piston skirts, camshaft bushings, crankshaft thrust bearings, and aluminum aftercoolers |

![[lf8etka.png]]

### Install

Clean the oil filter head sealing surface with a lint free cloth.

![[07600259.png]]

The QSK45 engine has three combination oil filters and the QSK60 engine has four combination oil filters.

Use engine oil to lubricate the oil filters' rubber seals.

Fill the oil filters with clean engine oil.

![[lf8etwb.png]]

> [!warning] CAUTION · Осторожно
> Mechanical overtightening can distort the threads or damage the filter element seal. If the threads appear damaged, replace the oil filter head adapter.

> [!warning] CAUTION · Осторожно
> Locate the oil filter wrench, Part Number 3400158, near the top of the oil filter canister. This will reduce the possibility of damaging the oil filter.

Install the oil filter. Turn it until the seal contacts the filter head sealing surface.

Turn the oil filter an additional 3/4 to 1 turn.

![[07600230.png]]

Install and tighten the drain plug.

> [!tip] Момент затяжки · Torque Value
> 47 n•m [35 ft-lb]

![[07600258.png]]

Some QSK60 Power Generation engines have an oil by-pass line from the PRELUBTM to the fuel pump accessory drive with a small oil filter installed.

Use engine oil to lubricate the oil filter's rubber seal.

Fill the oil filter with clean engine oil.

![[lf8etwb.png]]

> [!warning] CAUTION · Осторожно
> Mechanical overtightening can distort the threads or damage the filter element seal. If the threads appear damaged, replace the oil filter head adapter.

> [!warning] CAUTION · Осторожно
> Locate the oil filter wrench, Part Number 3400158, near the top of the oil filter canister. This will reduce the possibility of damaging the oil filter.

Install the oil filter, turning it until the seal contacts the filter head's sealing surface.

Turn the oil filter an additional 3/4 to 1 full turn.

![[07500014.png]]

### Pressure Differential Test

Spin-on Type

This test will indicate oil pressure before and after the oil flows through the filters.

Use a differential pressure gauge or one pressure gauge with two oil hoses and two valves to eliminate gauge error. Use a gauge with a minimum pressure capacity of 1400 kPa \[200 psi\].

Make sure the engine is switched off.

![[07600291.png]]

Remove the M14 hex plug (7) from the outlet end of the oil filter head (10) and install end 7 of the valve assembly in the port of the filter head from where the hex plug (7) has been removed.

This reading will indicate the oil pressure after the oil flows through the filters.

Remove the hex plug (18) from the oil pump inlet end of the filter head (10) and install end 6 of the valve assembly oil hose into where the second hex plug (18) has been removed.

This reading will indicate the oil pressure before the oil flows through the filters.

![[07600525.png]]

Operate the engine at rated rpm until the engine oil reaches its normal operating temperature. Continue to operate the engine at rated rpm for the duration of the pressure test.

![[oi400la.png]]

Close valve (7) and open valve (6) to read the oil pressure before the filters.

Close valve (6) and open valve (7) to read the oil pressure after the filters.

If the difference in pressure is more than the maximum allowable value, an oil filter with excessive restriction is being used. Replace the filters and check the pressure differential again.

| **Measurements** |  |  |  |
|---|---|---|---|
|  | kpa | psi |  |
| Maximum Oil Filter Pressure Differential | New/clean oil filters | 83 | 12 |
|  | Used oil filters | 240 | 35 |

![[07600291.png]]

Turn the engine OFF.

Remove the end of the valve assembly (5) from the oil pump end of filter head (2) and install the hex plug (4).

Tighten the hex plug.

> [!tip] Момент затяжки · Torque Value
> 27 n•m [239 in-lb]

![[07600290.png]]

Remove the hose (3) from the outlet end of filter head (2) and install the hex plug (1).

Tighten the hex plug.

> [!tip] Момент затяжки · Torque Value
> 27 n•m [239 in-lb]

![[07600289.png]]

Eliminator™

This test will indicate oil pressure before and after the oil flows through the eliminator.

Use a differential pressure gauge or one pressure gauge with two oil hoses and two valves to eliminate gauge error. Use a gauge with a minimum pressure capacity of 1400 kPa \[200 psi\].

Make sure the engine is switched off.

![[07600291.png]]

Remove the two plugs from the filter housing.

Install end of the valve assembly in the port of the filter nearest to the centrifuge from where the plug has been removed.

Install the end of the valve assembly in the port of the filter furthest away from the centrifuge from where the other plug has been removed.

![[07600238.png]]

Operate the engine at rated rpm until the engine oil reaches its normal operating temperature. Continue operating the engine at rated rpm for the duration of the pressure test.

![[oi400la.png]]

Close valve (7), open valve (6), and record the pressure value before the eliminator.

Close valve (6), open valve (7), and record the pressure value after the eliminator.

If the difference in pressure is more than the maximum allowable value, inspect and clean the eliminator screens before checking the oil pressure differential again.

| Measurements |  |  |
|---|---|---|
|  | kpa | psi |
| Maximum Oil Pressure Differential | 60 | 9 |

![[07600291.png]]

Turn the engine OFF.

Remove the valve assembly from the Eliminator and install the two plugs.

Tighten the plugs.

> [!tip] Момент затяжки · Torque Value
> 10 n•m [89 in-lb]

![[07600238.png]]
