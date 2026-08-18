---
aliases:
  - "Компрессия двигателя"
type: "Процедура"
doc: "00-014-012"
title_en: "Engine Compression"
title_ru: "Компрессия двигателя"
modified: "2021-11-17"
engines:
  - "33239746"
  - "33239899"
  - "41349633"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
  - "QSK19"
manuals:
  - "4021528"
  - "4021592"
figures: 3
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/00/00-014-012.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/00-014-012.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "двигатель/QSK19"
  - "группа/00"
---

# Engine Compression
**Компрессия двигателя**

> [!abstract] Процедура · `00-014-012`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]], [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60, QSK19
> **Входит в руководства:** [[4021528 — K38, K50, QSK38, and QSK50 Service Manual|4021528]], [[4021592 — QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual|4021592]]
> **Секции:** Section 14 - Engine Testing - Group 14
> **Даты:** изменён 2021-11-17
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/00/00-014-012.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/00-014-012.pdf)

### Preparatory Steps

- Remove the rocker lever cover.

- Remove the rocker lever assembly.

- Remove the injector.

![[ck800wa.png]]

- Establish top dead center (TDC) on the compression stroke.

Continue to rotate the crankshaft until the piston passes TDC and is 12.7 mm \[0.50 inch\] after top dead center (ATDC).

Rotate the crankshaft in the opposite direction to raise the piston 6.35 mm \[0.250 inch\] below TDC.

![[22400200.png]]

> [!danger] WARNING · Опасно
> Fuel is flammable. Keep all cigarettes, flames, pilot lights, arcing equipment, and switches out of the work area and areas sharing ventilation to reduce the possibility of severe personal injury or death when working on the fuel system.

> [!danger] WARNING · Опасно
> Wear appropriate eye and face protection when using compressed air. Flying debris and dirt can cause personal injury.

> [!danger] WARNING · Опасно
> When using a steam cleaner, wear safety glasses or a face shield, as well as protective clothing. Hot steam can cause serious personal injury.

> [!warning] CAUTION · Осторожно
> Clean all fittings before disassembly. Dirt or contaminants can damage the fuel system.

Before servicing any fuel system components, (such as fuel lines, fuel pump, injectors, etc.) which would expose the fuel system or internal engine components to potential contaminants prior to disassembly, clean the fittings, mounting hardware, and the area around the component to be removed. Dirt, paint or other contaminants can be introduced into the fuel system and engine if the surrounding areas are **not** cleaned, resulting in damage to the fuel system and engine.

Use shop air to remove debris on adjacent chassis frame rails and between the fuel pump heads.

To prevent damage from debris and contamination, cover, cap, or plug any openings as soon as possible when servicing the fuel system.

- Relieve the high-pressure fuel from the fuel rail. Refer to Procedure 006-081 in Section 6.
- Remove all fuel injectors. Refer to Procedure 006-026 in Section 6.

> [!note] Note · Примечание
> Some diesel engines will require the removal of overhead components to allow removal of the fuel injector and installation of compression check adapter. Make sure the overhead is properly reset before attempting compression check.

Remove one clean care cap from an injector supply port on the rail (the most accessible). Place a 3/4 inch or 20 mm hose over the open port. Route the hose to a container.

Alternately, a fuel injector supply line can be installed and routed away from the engine into a container.

### General Information

All internal combustion engines require a certain amount of compression to allow ignition of the fuel/air mixture. To ensure compression, cylinders **must not** have high leakage. High leakage has a negative impact on cylinder and engine performance.

Checking cylinder leakage is a quick way to help determine the mechanical health of a cylinder. This check is most effective when performed as part of a series of symptom-directed diagnostic procedures including, but **not** limited to:

- Crankcase blowby check
- Combustion gas in coolant check
- Cylinder compression check
- Chassis and engine load checks.

High leakage can be caused by, but **not** limited to:

| Parts | Root Causes |
|---|---|
| Piston Rings | Worn, broken, incorrect, or missing rings |
| Piston | Cracked piston or hole in piston |
| Cylinder Bore | Worn or polished bore, crack or hole in bore, out of round, incorrect liner protrusion |
| Cylinder Head Gasket | Leaking head gasket |
| Cylinder Head | Cracked head, warped head, bent valves, broken valves, worn or damaged valve seats |
| Camshaft | Worn camshaft lobes, incorrect part |
| Valve Train | Damaged rockers, damaged tappets, damaged or bent pushrods, damaged valve |

Evaluating cylinder leakage check results can be done in two ways:

- Cylinder-to-cylinder or engine-to-engine comparison
- Comparsion against a published specification

See engine specifications in the Engine Testing Specifications of Section V for engine-specific leakage values, if available.

Leakage check should be performed on an engine at room temperature 20°C \[68°F\] for best results.

> [!note] Note · Примечание
> Make sure the overhead is properly set before attempting leakage check. Improper overhead settings could be the root cause of drivability complaints and could invalidate leakage check results. If settings are **not** within specification, adjust overhead and road test. If drivability complaints persist after road test, proceed with leakage test.

This check will be performed with the engine static.

> [!note] Note · Примечание
> The tools and procedure are **not** designed to check running cylinder leakage. Attempting to check cylinder leakage on a running engine may result in personal injury or equipment damage.

### Setup

- Install compression and leak down check adapter into cylinder being evaluated. For most diesel engines, these adapters simulate fuel injectors and are retained in the same manner. See engine-specific fuel injector procedure for hold-down instructions. In most cases, production hardware is reused for the adapter, but some adapters come with their own retaining hardware.
- Use a vacuum method to evacuate all liquid from inside all cylinders.
- Connect battery charger to make sure of consistent cranking speeds.
- Connect to engine with data link adapter and the recommended Cummins® electronic service tool, or equivalent, to monitor cranking rpm. See the electronic service tool instruction manual.

Minimum Cranking Speed: 100 rpm

- Connect compression gauge, Part Number 3164627, found in kit, Part Number 5394335, to the compression and leakdown check adapter. No gauge calibration is required. Release any residual gauge pressure by pushing the button on the side of the gauge.

### Pressure Test

During cranking, all cylinders will generate jets of pressurized air (and possibly oil) exiting from the top of the cylinder head.

Use the engine starter to crank the engine long enough to generate three to five compression strokes on the cylinder being evaluated.

Do **not** crank the engine for 30 seconds continuously. Crank the engine in 15 second intervals with a 15 second pause between intervals. This reduces the possibility of overheating the starting motor.

> [!note] Note · Примечание
> Units equipped with starter lockout features may require additional cranking aids.

The compression gauge will automatically record the highest pressure achieved.

Record the pressure.

Release pressure from the gauge by pressing the button on the side of the gauge. Repeat this test for all remaining cylinders as necessary. Make sure the start has sufficient time to cool between cranking periods.

Diagnosis:

If one cylinder compression pressure is lower compared to other cylinders, to other similar engines, or to published specifications, there can be a problem with **only** that specific cylinder. See the appropriate troubleshooting symptom tree for additional information. If all cylinder compression pressures are uniform compared to each other but low compared to a similar engine or published specification, the engine may require a full or partial overhaul. Inspect all parts according to all engine specific procedures and established reuse guidelines.

### Pressure Differential Test

Rotate crankshaft with barring tool until the cylinder being evaluated is beginning the compression stroke. Both intake and exhaust valves for the cylinder being evaluated will be fully closed under spring pressure at this point and the rockers of both of these valves will have some free play due to overhead lash settings.

Continue rotating the engine until the piston approaches but does **not** pass top dead center (TDC) for the cylinder being evaluated. Some diesel leak down adapters include a TDC indicator gage. Stop rotating the crankshaft immediately when the gauge stops moving upward with crankshaft rotation. On diesel adapters, if the gauge is **not** included with the adapter being used, a slender rod can be used as a substitute. On gas engines, there are no provisions for using a gauge. Approximate TDC will determined using the complimentary cylinder valve overlap method.

For best results, the piston should **not** be traveling downward when rotation is stopped. If the piston crosses past TDC and starts traveling downward, the piston rings will unseat in the piston ring lands slightly, causing a potential source of measurement error. If the piston starts traveling downward, reverse the barring rotation and rotate the crankshaft until the piston crosses back past TDC in reverse plus 1/3 of a crankshaft rotation. Bar the engine in the normal rotation and try again.

Mechanical Diagnostic Kit, Part Number 5394335, includes two leakage testers. See the chart below to make sure the correct one is used.

> [!note] Note · Примечание
> Use of incorrect leakage tester will generate measurement error.

| **Leakage Test Part Number** | **Usage** |
|---|---|
| 5394340 | Engines with a bore size smaller than 127 mm \[5 in\] |
| 5394360 | Engines with a bore size equal to or larger than 127 mm \[5 in\] |

Connect leakage tester to compression and leak down check adapter.

> [!note] Note · Примечание
> Applying air pressure to the test cylinder may cause the engine to attempt to rotate. Engine **must** be prevented from rotating during testing.

Connect shop air to leakage tester. 100 psi is preferred, but the measurement process will work with lower pressure.

Open the leakage tester pressure regulator and adjust until the gauge closest to the pressure regulator (reference gauge) reads 100 psi (or maximum available pressure).

Allow system pressure to stabilize. Record pressure on the gauge farthest from the pressure regulator (cylinder gauge). Record the pressures.

Use the following formula to determine cylinder leakage as a percent: ((Reference Gauge value – Cylinder Gauge value) / Reference Gauge value) x 100 = Cylinder Leakage percent.

Repeat the test for all remaining cylinders as necessary.

Diagnosis:

If one cylinder leakage is higher compared to other cylinders, to other similar engines, or to published specifications, use stethoscope, Part Number 5394438 from kit, Part Number 5395335, to try to determine where the cylinder is leaking when pressurized.

| **If air can be heard escaping from** | **Likely cause of leakage** |
|---|---|
| Intake Manifold | Intake valve or valve seat, cracked head |
| Exhaust Manifold or Turbocharger | Exhaust valve or valve seat, cracked head |
| Coolant System | Cylinder head gasket, cracked head |
| Engine Crankcase | Piston, piston rings, cylinder bore |

Remove cylinder head and inspect suspect components further to determine root cause. Refer to engine-specific procedures.

If all cylinder leakages are uniform compared to each other but high compared to a similar engine or published specification, the engine may be in need of a full or partial overhaul. Inspect all suspect parts per engine specific procedures and established reuse guidelines.

### Finishing Steps

- Install the injector.

- Install the rocker lever assembly.

- Install the rocker lever cover.

![[ck800wa.png]]
