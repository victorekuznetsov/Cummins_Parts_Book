---
aliases:
  - "Топливоподкачивающий насос"
type: "Процедура"
doc: "41-005-045"
title_en: "Fuel Lift Pump"
title_ru: "Топливоподкачивающий насос"
modified: "2003-05-13"
engines:
  - "93058669"
  - "93087701"
families:
  - "C8.3 · 6C8.3"
manuals:
  - "2883407"
  - "3666003"
parts:
  - "3914284"
figures: 16
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/41/41-005-045.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/41-005-045.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "группа/41"
---

# Fuel Lift Pump
**Топливоподкачивающий насос**

> [!abstract] Процедура · `41-005-045`
> **Двигатели:** [[93058669 — 6C8.3 CPL 3105|93058669]], [[93087701 — 6C8.3 CPL 3105|93087701]]
> **Семейство:** C8.3 · 6C8.3
> **Входит в руководства:** [[2883407 — C8.3 (India) Operation and Maintenance Manual|2883407]], [[3666003 — C Troubleshooting and Repair Manual|3666003]]
> **Секции:** Section 5 - Fuel System - Group 05 · Section A - Adjustment, Repair, and Replacement
> **Даты:** изменён 2003-05-13
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/41/41-005-045.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/41-005-045.pdf)

### Initial Check

Measure the pressure drop across the fuel filter at low idle. If the filter restriction is above the maximum, it **must** be replaced.

|  | kpa |  | psi |  |
|---|---|---|---|---|
| Piston Lift Pump |  | 34 | MAX | 5 |

![[ff9etka.png]]

Check for a restriction between the fuel lift pump and the fuel injection pump.

1. Supply line to fuel filter
2. Fuel filter
3. Supply line to fuel injection pump
4. Fuel inlet line from tank.

![[fs900kw.png]]

Measure the fuel lift pump inlet restriction with a vacuum gauge between the fuel lift pump inlet and the supply line (4) from the fuel tank.

| kpa |  | in-hg |
|---|---|---|
| 27 | MAX | 8 |

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

Fuel prefilters, inline and water separator type, can become clogged and cause a loss of fuel flow.

Check the prefilter for clogs or restrictions.

In cold weather, check the prefilter for gelled fuel.

Clean or replace the prefilter, if necessary.

![[fs9etha.png]]

Check for kinks or bends in the fuel supply line that can cause a restriction in the fuel flow.

Remove and blow out the fuel supply lines.

![[fs900ed.png]]

### Preparatory Steps

> [!danger] WARNING · Опасно
> Wear appropriate eye and face protection when using compressed air. Flying debris and dirt can cause personal injury.

- Clean debris from the fuel line fittings and the fuel lift pump.
- Disconnect the low-pressure fuel lines. Refer to Procedure [[41-006-024 — Fuel Supply Lines|006-024]].

![[ft9tbmb.png]]

### Remove

Remove the two fuel lift pump mounting capscrews.

Remove the fuel lift pump.

![[fs900mb.png]]

### Test

The output of the fuel lift pump can be checked in two ways:

Test 1: Measure the output pressure using an in-line pressure gauge installed between the filter head and the fuel injection pump.

Test 2: Measure the flow volume.

![[fs900kk.png]]

Test 1: Output Pressure Test (Piston Style)

Operate the engine and measure the output pressure of the fuel lift pump using an in-line pressure gauge at the inlet to the injection pump.

Minimum pressure at high idle is 138 kPa \[20 psi\].

![[fs900kn.png]]

Test 2: Flow Volume Test (Piston Style)

> [!warning] CAUTION · Осторожно
> To prevent the engine from starting, disconnect the fuel shutdown wiring. Residual fuel in the injection pump can cause the engine to start.

> [!warning] CAUTION · Осторожно
> Do not crank the starter for more than 30 seconds at a time. Doing so can result in starter damage. Also, high voltage during cranking can damage the shutdown solenoid.

![[fv900vb.png]]

Disconnect the fuel shutdown solenoid wire.

Measure the engine cranking speed with a handheld tachometer, Part Number 3377462.

The minimum cranking speed is 120 rpm.

![[fv900vc.png]]

> [!warning] CAUTION · Осторожно
> Leave the shutdown solenoid disconnected for the following check:

Disconnect the output pressure line from the fuel lift pump and run it into a container.

Crank the engine for 30 seconds and measure the fuel lift pump flow volume.

The minimum flow volume is 150 mL \[5 oz\].

![[fs900pa.png]]

### Install

> [!warning] CAUTION · Осторожно
> Alternately tighten the mounting capscrews. As the capscrews are tightened, the fuel lift pump plunger is pushed into the pump. Failure to tighten the capscrews in an even manner can result in the plunger being bent or broken, causing sticking and failure.

Piston Style

Install the pump.

> [!tip] Момент затяжки · Torque Value
> 24 n•m [18 ft-lb]

The 5-mm \[0.20-in\] spacer (1), Part Number [[3914284]], **must** be installed along with a gasket, Part Number 3931348, on each side of the spacer.

> [!note] Note · Примечание
> For some applications, a bracket used for supporting other options will replace the 5-mm spacer.

![[05900503.png]]

### Finishing Steps

- Install the fuel line to the fuel lift pump and fuel filter head. Refer to Procedure [[41-006-024 — Fuel Supply Lines|006-024]].
- Vent the low-pressure fuel lines. Refer to Procedure [[41-006-024 — Fuel Supply Lines|006-024]].

![[ft9tbmd.png]]

## Детали, упомянутые в документе

| Артикул | Наименование | Русское название |
|---|---|---|
| [[3914284]] | MOUNTING SPACER | Монтажная распорная втулка |
