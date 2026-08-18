---
aliases:
  - "Сопротивление на входе топлива"
type: "Процедура"
doc: "20-006-020-tr"
title_en: "Fuel Inlet Restriction"
title_ru: "Сопротивление на входе топлива"
modified: "2014-01-08"
engines:
  - "41349633"
families:
  - "QSK19"
manuals:
  - "4021592"
figures: 37
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/20/20-006-020-tr.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/20-006-020-tr.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/20"
---

# Fuel Inlet Restriction
**Сопротивление на входе топлива**

> [!abstract] Процедура · `20-006-020-tr`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021592 — QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual|4021592]]
> **Секции:** Section 6 - Injectors and Fuel Lines - Group 06
> **Даты:** изменён 2014-01-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/20/20-006-020-tr.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/20-006-020-tr.pdf)

### Initial Check

with Electronically Actuated Injector

> [!danger] WARNING · Опасно
> Depending on the circumstance, fuel is flammable. Keep all cigarettes, flames, pilot lights, arcing equipment, and switches out of the work area and areas sharing ventilation to reduce the possibility of severe personal injury or death when working on the fuel system.

> [!warning] CAUTION · Осторожно
> Do not spill or drain fuel into the bilge area when disconnecting or removing fuel lines, replacing filters, and priming the fuel system. Do not drop or throw filter elements into the bilge area. The fuel and fuel filters must be disposed of in accordance with local environmental regulations.

#### Stage 1 Filters

- Remove the air bleed hose (1) from the air bleed check valve (2).
- Remove the air bleed check valve (2) from the drain manifold block (3).

![[06400351.png]]

Install the fuel system tester, (1), Part Number 4918612, in place of the air bleed check valve.

Install the air bleed hose.

> [!tip] Момент затяжки · Torque Value
> Fuel System Tester 55 n•m [41 ft-lb]

> [!tip] Момент затяжки · Torque Value
> Air Bleed Hose 45 n•m [33 ft-lb]

![[06400352.png]]

With the fuel supply valve closed, remove the M14 STOR plug from the fuel inlet manifold and install a Compuchek™ fitting, Part Number 3824844, or equivalent.

![[06400414.png]]

Connect the vacuum gauge and adapter, Part Number 3164491, or equivalent, and digital multimeter, Part Number 3164488 or 3164489, or equivalent, to the Compuchek™ fitting.

![[06400415.png]]

Open the fuel supply valve, and start and operate the engine at high idle.

Record the fuel inlet restriction.

The fuel inlet restriction maximum is: 254 mm-Hg \[10 in-Hg\].

If the restriction is above specifications, measure the Stage 1 fuel filter restriction.

![[14400049.png]]

Install the fuel system tester, (1), Part Number 4918612, in place of the air bleed check valve.

Install the air bleed hose.

> [!tip] Момент затяжки · Torque Value
> Fuel System Tester 55 n•m [41 ft-lb]

> [!tip] Момент затяжки · Torque Value
> Air Bleed Hose 45 n•m [33 ft-lb]

![[06400352.png]]

Remove the vacuum gauge and adapter from the fuel inlet manifold block.

![[06400415.png]]

Remove the Compuchek™ fitting and install the threaded o-ring plug into the port in the fuel inlet manifold block.

> [!tip] Момент затяжки · Torque Value
> Threaded O-ring Plug 29 n•m [21 ft-lb]

![[06400414.png]]

### Test

with Mechanically Actuated Injector

> [!danger] WARNING · Опасно
> Depending on the circumstance, fuel is flammable. Keep all cigarettes, flames, pilot lights, arcing equipment, and switches out of the work area and areas sharing ventilation to reduce the possibility of severe personal injury or death when working on the fuel system.

> [!warning] CAUTION · Осторожно
> Do not spill or drain fuel into the bilge area when disconnecting or removing fuel lines, replacing filters, and priming the fuel system. Do not drop or throw filter elements into the bilge area. The fuel and fuel filters must be disposed of in accordance with local environmental regulations.

The fuel pump **must** be in the "Full Fuel" position to accurately measure fuel line restriction.

![[06600218.png]]

Install a line containing a 7 mm \[0.25 in\] needle valve between the fuel pump shutoff valve and the fuel tank.

![[06600219.png]]

Remove the air/fuel control air supply line from the air intake manifold. Install a plug or a cap in the air manifold hole.

![[06600220.png]]

Install the pressure pump, Part Number 3375515, or equivalent.

If the pressure pump is **not** available, install a regulated air pressure hose, with a shutoff valve, to the line.

Apply 170 kPa \[25 psi\] air pressure to the air/fuel control air supply line.

![[06600220.png]]

Remove the fuel supply hose to the gear pump or the plug from the rear of the fuel pump mounted to the fuel filter.

Install the adapter as close to the fuel pump as possible. Install a vacuum gauge, Part Number ST-434, or equivalent, to the adapter. The minimum gauge capacity **must** be 760 mm-Hg \[30 in-Hg\].

> [!note] Note · Примечание
> The vacuum gauge, Part Number ST434, contains the gauge, hose, and adapter.

![[06600222.png]]

With the valve installed, operate the engine at high idle. Slowly open the needle valve until the engine rpm drops 100 rpm. This is the "Full Fuel" position.

![[oi8vava.png]]

Hold the gauge at the same level as the gear pump.

> [!note] Note · Примечание
> The gauge will **not** measure the correct vacuum if it is **not** held at the same level as the gear pump.

Operate the engine at the "Full Fuel" position.

Observe the reading on the gauge.

The maximum fuel inlet restriction is as follows:

| Filter Restriction (Clean) |  |  |
|---|---|---|
| mm-hg |  | in-hg |
| 100 | MAX | 4 |

| Filter Restriction (Dirty) |  |  |
|---|---|---|
| mm-hg |  | in-hg |
| 200 | MAX | 8 |

Correct the restriction or replace the fuel filter. Refer to Procedure 006-015 in Section 6.

![[fp8gacd.png]]

### Measure

with Electronically Actuated Injector

> [!danger] WARNING · Опасно
> Depending on the circumstance, fuel is flammable. Keep all cigarettes, flames, pilot lights, arcing equipment, and switches out of the work area and areas sharing ventilation to reduce the possibility of severe personal injury or death when working on the fuel system.

> [!warning] CAUTION · Осторожно
> Do not spill or drain fuel into the bilge area when disconnecting or removing fuel lines, replacing filters, and priming the fuel system. Do not drop or throw filter elements into the bilge area. The fuel and fuel filters must be disposed of in accordance with local environmental regulations.

#### Stage 1 Filters

- Remove the air bleed hose (1) from the air bleed check valve (2).
- Remove the air bleed check valve (2) from the drain manifold block (3).

![[06400351.png]]

Install the fuel system tester (1), Part Number 4918612, in place of the air bleed check valve.

Install the air bleed hose.

> [!tip] Момент затяжки · Torque Value
> Fuel System Tester 55 n•m [41 ft-lb]

> [!tip] Момент затяжки · Torque Value
> Air Bleed Hose 45 n•m [33 ft-lb]

![[06400352.png]]

Industrial Applications

Remove the threaded hex head o-ring plug (1) in the inlet and the threaded hex head o-ring plug (2) in the outlet of Stage 1 filter head manifolds and replace them with Compuchek™ fittings.

![[06400408.png]]

Connect a vacuum gauge and adapter to the Compuchek™ fitting in the inlet port.

Start and operate the engine at high idle.

Record the Stage 1 inlet restriction.

The fuel inlet restriction maximum is 14 kPa \[4 in-Hg\].

If the restriction is above specifications, inspect the fuel lines. Refer to the original equipment manufacturer (OEM) service manual to determine the source of the high restriction.

![[06400410.png]]

Remove the vacuum gauge and adapter from the inlet port and install it on the Compuchek™ fitting in the outlet port.

Start and operate the engine at high idle.

![[06400409.png]]

Record the Stage 1 outlet restriction.

Subtract the measurement obtained at the Stage 1 inlet from the measurement obtained at the Stage 1 outlet. This is the Stage 1 restriction.

Example:

- Stage 1 inlet restriction is 3.4 kPa \[1 in-Hg\]
- Stage 1 outlet restriction is 15.2 kPa \[4.5 in-Hg\]

Stage 1 restriction is 15.2 kPa \[4.5 in-Hg\] minus 3.4 kPa \[1 in-Hg\] equals 11.8 kPa \[3.5 in-Hg\].

| Stage 1 Filter Restriction |  |  |
|---|---|---|
| kpa |  | in-hg |
| 27.1 | MAX | 8 |

If the restriction is above specifications, replace the Stage 1 fuel filters. [[20-006-015-tr — Fuel Filter (Spin-On Type)|Refer to Procedure 006-015 in Section 6.]]

If the restriction is below the maximum specifications, inspect the fuel lines. Refer to the OEM service manual to determine the source of the high restriction.

![[14400049.png]]

Remove the vacuum gauge and adapter from the Stage 1 fuel filter head.

![[06400409.png]]

Remove the Compuchek™ fittings and install the threaded hex head o-ring plugs into the inlet port (1) and outlet (2) in the filter head.

> [!tip] Момент затяжки · Torque Value
> Threaded Hex Head O-ring Plugs 27 n•m [239 in-lb]

![[06400408.png]]

Marine Applications

Remove the threaded hex head o-ring plug (1) in the inlet and the threaded hex head o-ring plug (2) in the outlet of Stage 1 filter head manifolds and replace them with Compuchek™ fittings.

![[06600475.png]]

Connect a vacuum gauge and adapter to the Compuchek™ fitting in the inlet port.

Start and operate the engine at high idle.

Record the Stage 1 inlet restriction.

The fuel inlet restriction maximum is 14 kPa \[4 in-Hg\].

If the restriction is above specifications, inspect the fuel lines. Refer to the OEM service manual to determine the source of the high restriction.

![[06400457.png]]

Remove the vacuum gauge and adapter from the inlet port and install it on the Compuchek™ fitting in the outlet port.

Start and operate the engine at high idle.

![[06600476.png]]

Record the Stage 1 outlet restriction.

Subtract the measurement obtained at the Stage 1 inlet from the measurement obtained at the Stage 1 outlet. This is the Stage 1 restriction.

Example:

- Stage 1 inlet restriction is 3.4 kPa \[1 in-Hg\]
- Stage 1 outlet restriction is 15.2 kPa \[4.5 in-Hg\]

Stage 1 restriction is 15.2 kPa \[4.5 in-Hg\] minus 3.4 kPa \[1 in-Hg\] equals 11.8 kPa \[3.5 in-Hg\].

| Stage 1 Filter Restriction |  |  |
|---|---|---|
| kpa |  | in-hg |
| 27.1 | MAX | 8 |

If the restriction is above specifications, replace the Stage 1 fuel filters. [[20-006-015-tr — Fuel Filter (Spin-On Type)|Refer to Procedure 006-015 in Section 6.]]

If the restriction is below the maximum specifications, inspect the fuel lines. Refer to the OEM service manual to determine the source of the high restriction.

![[14400049.png]]

Remove the vacuum gauge and adapter from the Stage 1 fuel filter head.

![[06600476.png]]

Remove the Compuchek™ fittings and install the threaded hex head o-ring plugs into the inlet port (1) and outlet (2) in the filter head.

> [!tip] Момент затяжки · Torque Value
> Threaded Hex Head O-ring Plugs 27 n•m [239 in-lb]

![[06600475.png]]

Remove the air bleed hose and fuel system tester (1) from the fuel drain manifold block.

![[06400352.png]]

Install the original air bleed check valve (2) into the fuel drain manifold block (3).

> [!tip] Момент затяжки · Torque Value
> Air Bleed Check Valve 55 n•m [41 ft-lb]

Install the air bleed hose to the air bleed check valve.

> [!tip] Момент затяжки · Torque Value
> Air Bleed Hose 45 n•m [33 ft-lb]

![[06400351.png]]

#### Stage 2

- Remove the Stage 2 filter head inlet pressure sensor (1). Refer to Procedure 019-119 in Section 19 in the QSK19 (CM850 Modular Common Rail System) Electronic Control System Troubleshooting and Repair Manual, Bulletin 4021493.
- Remove the Stage 2 filter head temperature sensor (2). Refer to Procedure 019-398 in the QSK19 (CM850 Modular Common Rail System) Electronic Control System Troubleshooting and Repair Manual, Bulletin 4021493.
- Install Compchek™ fittings into the Stage 2 filter head pressure and temperature sensor ports.

![[06400411.png]]

Connect a pressure gauge and adapter to the Compuchek™ fitting in the pressure sensor side of the filter head.

Start and operate the engine at high idle.

Record the Stage 2 inlet pressure.

![[06400412.png]]

Remove the pressure gauge and adapter from the pressure sensor side fitting and install the pressure gauge and adapter on the fitting on the temperature sensor side of the filter head.

Start and operate the engine at high idle.

![[06400413.png]]

Record the Stage 2 outlet pressure.

Subtract the measurement obtained at the Stage 2 outlet from the measurement obtained at the Stage 2 inlet. This is the Stage 2 filter restriction.

Example:

- Stage 2 inlet pressure is 731.5 kPa \[104.5 psi\]
- Stage 2 outlet pressure is 714.0 kPa \[102.0 psi\]

Stage 2 restriction is 728.0 kPa \[104.5 psi\] minus 714.0 kPa \[102.0 psi\] equals 17.5 kPa \[2.5 psi\].

| Stage 2 Filter Restriction Limits |  |  |
|---|---|---|
| kpa |  | psi |
| 300 | MAX | 43.5 |

If the restriction is above specifications, replace the Stage 2 fuel filters. [[20-006-015-tr — Fuel Filter (Spin-On Type)|Refer to Procedure 006-015 in Section 6.]]

![[14400049.png]]

Remove the pressure gauge and adapter from the second stage filter head.

![[06400413.png]]

Remove the Compuchek™ fittings from the second stage filter head.

Install the pressure sensor (1) into the filter head. Refer to Procedure 019-119 in Section 19 in the QSK19 (CM850 Modular Common Rail System) Electronic Control System Troubleshooting and Repair Manual, Bulletin 4021493.

Install the temperature sensor (2) into the filter head. Refer to Procedure 019-398 in the QSK19 (CM850 Modular Common Rail System) Electronic Control System Troubleshooting and Repair Manual, Bulletin 4021493.

![[06400411.png]]
