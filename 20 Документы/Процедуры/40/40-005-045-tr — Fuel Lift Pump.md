---
aliases:
  - "Топливоподкачивающий насос"
type: "Процедура"
doc: "40-005-045-tr"
title_en: "Fuel Lift Pump"
title_ru: "Топливоподкачивающий насос"
modified: "2012-05-03"
engines:
  - "93047320"
families:
  - "6B5.9"
manuals:
  - "3666087"
parts:
  - "3914284"
figures: 14
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/40/40-005-045-tr.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/40-005-045-tr.pdf"
tags:
  - "документ/процедура"
  - "двигатель/6B5.9"
  - "группа/40"
---

# Fuel Lift Pump
**Топливоподкачивающий насос**

> [!abstract] Процедура · `40-005-045-tr`
> **Двигатели:** [[93047320 — 6B5.9 CPL 3111|93047320]]
> **Семейство:** 6B5.9
> **Входит в руководства:** [[3666087 — B3.9, B4.5, B4.5 RGT, and B5.9 Service Manual|3666087]]
> **Секции:** Section 5 - Fuel System · Section 5 - Fuel System - Group 05
> **Даты:** изменён 2012-05-03
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/40/40-005-045-tr.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/40-005-045-tr.pdf)

### Initial Check

Measure the fuel lift pump inlet restriction with a vacuum gauge between the fuel lift pump inlet and the supply line (4) from the fuel tank.

| Fuel Lift Pump Inlet Restriction - Clean Fuel Filter |  |  |
|---|---|---|
| kpa |  | in-hg |
| 63.5 | MAX | 2.5 |

| Fuel Lift Pump Inlet Restriction - Dirty Fuel Filter |  |  |
|---|---|---|
| kpa |  | in-hg |
| 100 | MAX | 4.0 |

![[06900176.png]]

If the inlet restriction is above the maximum, check for restrictions or suction leaks in the fuel circuit to the fuel lift pump:

1. Supply line
2. Prefilter
3. Supply line
4. Supply tank
5. Tank vent.

![[fs900kz.png]]

Look for a plugged supply tank vent first.

![[fs900sc.png]]

Fuel prefilters, in-line and water separator type, can become clogged and cause a loss of fuel flow.

Check the prefilter for clogs or restrictions.

In cold weather, check the prefilter for gelled fuel.

Clean or replace the prefilter, if necessary.

![[fs9etha.png]]

Check for kinks or bends in the fuel supply line that can cause a restriction in the fuel flow.

Remove and blow out the fuel supply lines.

![[fs900ed.png]]

### Test

Output Pressure Test (Diaphragm Style and Piston Style - Low Output)

Operate the engine and measure the output pressure of the fuel lift pump using an in-line pressure gauge at the inlet to the injection pump.

The minimum pressure at high idle is 21 kPa \[3 psi\].

If the minimum pressure is not achieved, check for:

- Dirty fuel filter
- Damaged lift pump.

![[fs900kl.png]]

> [!note] Note · Примечание
> **On some engines, the diaphragm style pump may have been replaced by a low output piston style pump. The specifications below apply to both diaphragm and piston low output pumps. The low output piston pump is visually different from higher output piston pump. The outlet points downward on the low output piston pump.**

![[01400691.png]]

Output Pressure Test (Piston Style - High Output))

Operate the engine, and measure the output pressure of the fuel lift pump with an in-line pressure gauge at the inlet to the injection pump.

Minimum pressure at high idle is 124 kPa \[18 psi\].

If the minimum pressure is not achieved, check for:

- Dirty fuel filter
- Damaged lift pump.

![[fs900kn.png]]

### Preparatory Steps

> [!danger] WARNING · Опасно
> When using solvents, acids, or alkaline materials for cleaning, follow the manufacturer's recommendations for use. Wear goggles and protective clothing to reduce the possibility of personal injury.

> [!danger] WARNING · Опасно
> Wear appropriate eye and face protection when using compressed air. Flying debris and dirt can cause personal injury.

- Clean the debris from the fuel line filters and the fule lift pump.
- Disconnect the low-pressure fuel lines. [[40-006-024-tr — Fuel Supply Lines|Refer to Procedure 006-024]].

![[ck800wa.png]]

### Remove

> [!warning] CAUTION · Осторожно
> To prevent the engine from starting, disconnect the fuel shutdown wiring. Residual fuel in the injection pump can cause the engine to start.

> [!warning] CAUTION · Осторожно
> Do not crank the starter for more than 30 seconds at a time. Doing so can result in starter damage. Also, high voltage during cranking can damage the shutdown solenoid.

![[fv900vb.png]]

Disconnect the fuel shutdown solenoid wire.

Measure the engine cranking speed with a handheld tachometer, Part Number 3377462.

The minimum cranking speed is 120 rpm.

![[fv900vc.png]]

Remove the two fuel lift pump mounting capscrews.

Remove the fuel lift pump.

![[fs900mb.png]]

### Install

> [!warning] CAUTION · Осторожно
> Alternately tighten the mounting capscrews. As the capscrews are tightened, the fuel lift pump plunger is pushed into the pump. Failure to tighten the capscrews in an even manner can result in the plunger being bent or broken, causing sticking and failure.

Diaphragm Style and Piston Style

Install the pump.

> [!tip] Момент затяжки · Torque Value
> 24 n•m [212 in-lb]

The 5 mm \[0.20-in\] spacer (1), Part Number [[3914284]], must be installed along with a new gasket, Part Number 3931348, on each side of the spacer.

> [!note] Note · Примечание
> For some applications, a bracket used for supporting other options will replace the 5 mm \[0.20-in\] spacer.

![[05900503.png]]

### Finishing Steps

- Install the low pressure fuel lines. [[40-006-024-tr — Fuel Supply Lines|Refer to Procedure 006-024 in Section 6]].
- Vent the low-pressure fuel lines. [[40-006-024-tr — Fuel Supply Lines|Refer to Procedure 006-024 in Section 6]].
- Operate the engine and check for leaks.

![[ck800wa.png]]

## Детали, упомянутые в документе

| Артикул | Наименование | Русское название |
|---|---|---|
| [[3914284]] | MOUNTING SPACER | Монтажная распорная втулка |
