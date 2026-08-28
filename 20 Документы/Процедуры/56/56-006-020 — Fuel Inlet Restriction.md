---
aliases:
  - "Сопротивление на входе топлива"
type: "Процедура"
doc: "56-006-020"
title_en: "Fuel Inlet Restriction"
title_ru: "Сопротивление на входе топлива"
modified: "2006-08-17"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
families:
  - "QSK60"
manuals:
  - "4021530"
figures: 19
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/56/56-006-020.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/56-006-020.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK60"
  - "группа/56"
---

# Fuel Inlet Restriction
**Сопротивление на входе топлива**

> [!abstract] Процедура · `56-006-020`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]]
> **Семейство:** QSK60
> **Входит в руководства:** [[4021530 — QSK45 and QSK60 Service Manual|4021530]]
> **Секции:** Section 6 - Injectors and Fuel Lines - Group 06
> **Даты:** изменён 2006-08-17
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/56/56-006-020.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/56-006-020.pdf)

### Measure

with Mechanically Actuated Injector

Use a Compuchek® fitting, vacuum gauge, and adapter. Connect the gauge to the Compuchek® fitting on the fuel pump inlet fitting.

![[06400054.png]]

Start and operate the engine at high idle, no load.

Fuel inlet restriction:

- With clean fuel filters: 102 mm-Hg \[4 in-Hg\]
- With dirty fuel filters: 203 mm-Hg \[8 in-Hg\].

![[06400053.png]]

If the restriction is above specifications:

- Change the fuel filter. Refer to Procedure [[56-006-015-tr — Fuel Filter (Spin-On Type)|006-015]].
- Inspect the fuel lines. Refer to Procedure [[56-006-024-tr — Fuel Supply Lines|006-024]].

![[fp8hoca.png]]

with Electronically Actuated Injector

Stage 1 Filters

Remove the air bleed hose (1) from the air bleed check valve (2).

Remove the air bleed check valve (2) from the drain manifold block (3).

![[05600265.png]]

Install the fuel system tester, Part Number, 4918612, in place of the air bleed check valve.

| Fuel System Tester | 55 n.m | \[41 ft-lb\] |
|---|---|---|

Install the air bleed hose.

| Air Bleed Hose | 45 n.m | \[33 ft-lb\] |
|---|---|---|

![[05600266.png]]

Remove the threaded o-ring plug (1) in the inlet and the threaded o-ring plug (2) in the outlet of Stage 1 filter head and replace them with Compuchek® fittings.

![[05600267.png]]

Connect a vacuum gauge and adapter to the Compuchek® fitting in the inlet port (1).

Start and operate the engine at low idle, no load.

Record the Stage 1 inlet restriction.

The fuel inlet restriction maximum is: 102 mm-Hg \[4 in-Hg\].

If the restriction is above specifications, inspect the fuel lines. Refer to the OEM Troubleshooting and Repair manual to determine the source of the high restriction.

![[05600268.png]]

Remove the vacuum gauge and adapter from the inlet port and install it on the Compuchek® fitting in the outlet port (2).

Start and operate the engine at low idle, no load.

![[05600269.png]]

Record the Stage 1 outlet restriction.

Subtract the measurement obtained at the Stage 1 inlet from the measurement obtained at the Stage 1 outlet. This is the Stage 1 restriction.

Example:

Stage 1 inlet restriction is 25 mm-Hg \[1 in-Hg\]

Stage 1 outlet restriction is 113 mm-Hg \[4.5 in-Hg\]

Stage 1 restriction is 113 mm-Hg \[4.5 in-Hg\] - 25 mm-Hg \[1 in-Hg\] = 88 mm-Hg \[3.5 in-Hg\]

| mm-hg |  | in-hg |
|---|---|---|
| 76 | MIN | 3 |
| 152 | MAX | 6 |

If the restriction is above specifications, replace the Stage 1 fuel filters. Refer to Procedure [[56-006-015-tr — Fuel Filter (Spin-On Type)|006-015]].

![[14400049.png]]

Remove the vacuum gauge, adapter and Compuchek® fittings from the Stage 1 fuel filter head.

![[05600269.png]]

Install the threaded o-ring plugs inlet port (1), and outlet port (2) in the filter head.

| Threaded O-ring Plugs | 27 n.m | \[20 ft-lb\] |
|---|---|---|

![[05600267.png]]

Remove the air bleed hose and fuel system tester from the drain manifold block.

![[05600266.png]]

Install the original air bleed check valve (2) into the drain manifold block (3).

| Air Bleed Check Valve | 55 n.m | \[41 ft-lb\] |
|---|---|---|

Install the air bleed hose to the air bleed check valve.

| Air Bleed Hose | 45 n.m | \[33 ft-lb\] |
|---|---|---|

![[05600265.png]]

Stage 2 Filters:

Remove the threaded o-ring inlet plug (1) and outlet plug (2) in the inlet of the Stage 2 filter head and replace them with Compuchek® fittings.

![[05600271.png]]

Connect a pressure gauge and adapter to the Compuchek® fitting in the inlet port (1).

Start and operate the engine at high idle.

Record the Stage 2 inlet pressure.

![[05600272.png]]

Remove the pressure gauge and adapter from the inlet port and install the pressure gauge and adapter on the outlet port (2).

Start and operate the engine at high idle.

![[05600273.png]]

Record the Stage 2 outlet pressure.

Subtract the measurement obtained at the Stage 2 outlet from the measurement obtained at the Stage 2 inlet. This is the Stage 2 filter restriction.

Example:

Stage 2 inlet pressure is 731.5 kPa \[104.5 psi\]

Stage 2 outlet pressure is 714.0 kPa \[102.0 psi\]

Stage 2 restriction is 728.0 kPa \[104.5 psi\] - 714.0 kPa \[102.0 psi\] = 17.5 kPa \[2.5 psi\]

| kpa |  | psi |
|---|---|---|
| 28 | MAX | 4 |

| kpa |  | psi |
|---|---|---|
| 138 | MAX | 20 |

If the restriction is above specifications, replace the Stage 2 fuel filters. Refer to Procedure [[56-006-015-tr — Fuel Filter (Spin-On Type)|006-015]].

![[14400049.png]]

Remove the pressure gauge and adapter from the Stage 2 filter head.

![[05600273.png]]

Remove the Compuchek® fittings from the Stage 2 filter head.

Install the threaded o-ring plugs into the inlet (1) and outlet (2) ports in the filter head.

Tighten the plugs.

| Threaded O-ring Plugs | 27 n.m | \[20 ft-lb\] |
|---|---|---|

![[05600271.png]]
