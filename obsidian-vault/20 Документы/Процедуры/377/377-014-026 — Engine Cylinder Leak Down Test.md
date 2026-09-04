---
type: "Процедура"
doc: "377-014-026"
title_en: "Engine Cylinder Leak Down Test"
modified: "2020-03-04"
manuals:
  - "5411181"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/377/377-014-026.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/377-014-026.pdf"
tags:
  - "документ/процедура"
  - "группа/377"
---

# Engine Cylinder Leak Down Test

> [!abstract] Процедура · `377-014-026`
> **Входит в руководства:** [[5411181 — X15 CM2350 X114B - Efficiency Series Service Manual|5411181]]
> **Секции:** Section 14 - Engine Testing - Group 14
> **Даты:** изменён 2020-03-04
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/377/377-014-026.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/377-014-026.pdf)

### Select Service Tools

#### Recommended Cummins® Service Tools

- Fuel System Clean Care Kit, Part Number 4919073
- Cylinder Diagnostic Kit, Part Number 5394335
- Compression and Leak Down Test Adapter Kit, Part Number 5394350

#### Additional Service Items

- Shop air supply (100 psi or higher preferred)
- 3/4" breaker bar

### General Information

All internal combustion engines require a certain amount of compression to allow ignition of the fuel/air mixture. To ensure compression, cylinders **must not** have high leakage. High leakage has a negative impact on cylinder and engine performance.

Checking cylinder leakage is a quick way to help determine the mechanical health of a cylinder. This check is most effective when performed as part of a series of symptom-directed diagnostic procedures including, but **not** limited to:

- Crankcase blow-by check
- Combustion gas in coolant check
- Cylinder compression check
- Chassis and engine load checks.

High leakage can be caused by, but **not** limited to:

| **Parts** | **Root Causes** |
|---|---|
| Piston Rings | Worn, broken, incorrect, or missing rings |
| Piston | Cracked piston or hole in piston |
| Cylinder Bore | Worn or polished bore, crack or hole in bore, out of round, incorrect liner protrusion |
| Cylinder Head Gasket | Leaking head gasket |
| Cylinder Head | Cracked head, warped head, bent valves, broken valves, worn or damaged valve seats |
| Camshaft | Worn camshaft lobes, incorrect part |
| Valve Train | Damaged rockers, damaged tappets, damaged or bent pushrods, damaged valve springs, dropped valve |

Evaluating cylinder leakage check results can be done in two ways:

- Cylinder-to-cylinder or engine-to-engine comparison
- Comparison against a published specification

See engine specifications in the Engine Testing specifications of Section V for engine-specific leakage values, if available.

Leakage check should be performed on an engine at room temperature 20°C \[68°F\] for best results.

> [!note] Note · Примечание
> Make sure the overhead is properly set before attempting leakage check. Improper overhead settings could be the root cause of drivability complaints and could invalidate leakage check results. If settings are not within specification, adjust overhead and road test. If drivability complaints persist after road test, proceed with leakage test.

This check will be performed with the engine static.

> [!note] Note · Примечание
> The tools and procedure are not designed to check running cylinder leakage. Attempting to check cylinder leakage on a running engine may result in personal injury or equipment damage.

### Preparatory Steps

> [!danger] WARNING · Опасно
> Wear appropriate eye and face protection when using compressed air. Flying debris and dirt can cause personal injury.

> [!danger] WARNING · Опасно
> When using a steam cleaner, wear safety glasses or a face shield, as well as protective clothing. Hot steam can cause serious personal injury.

> [!warning] CAUTION · Осторожно
> Clean all fittings before disassembly. Dirt or contaminants can damage the fuel system.

Before servicing any fuel system components, (such as fuel lines, fuel pump, injectors, etc.) which would expose the fuel system or internal engine components to potential contaminants prior to disassembly, clean the fittings, mounting hardware, and the area around the component to be removed. Dirt, paint or other contaminants can be introduced into the fuel system and engine if the surrounding areas are **not** cleaned, resulting in damage to the fuel system and engine.

Using shop air, remove debris on adjacent chassis frame rails and between the fuel pump heads. To prevent damage from debris and contamination, cover, cap, or plug any openings as soon as possible when servicing the fuel system. Caps and plugs can be found in Fuel System Clean Care Kit, Part Number 4919073.

- Relieve the high-pressure fuel from the fuel rail. [[377-006-081 — Fuel System Pressure Relief Procedure|Refer to Procedure 006-081 in Section 6.]]
- Remove the fuel injector from the cylinder begin tested. [[377-006-026 — Injector|Refer to Procedure 006-026 in Section 6.]]

> [!note] Note · Примечание
> Some diesel engines will require the removal of overhead components to allow removal of the fuel injector.

### Setup

- Install compression and leak down check adapter into cylinder being evaluated. These adapters simulate fuel injectors and are retained in the same manner. In **most** cases, production hardware is reused for the adapter, but some adapters come with their own retaining hardware.
- Use a vacuum method to evacuate all liquid from inside the cylinder.

### Test

Rotate crankshaft with barring tool until the cylinder being evaluated is beginning the compression stroke. Both intake and exhaust valves for the cylinder being evaluated will be fully closed under spring pressure at this point and the rockers of both of these valves will have some free play due to overhead lash settings.

Continue rotating the engine until the piston approaches but does **not** pass top dead center (TDC) for the cylinder being evaluated. Some diesel leak down adapters include a TDC indicator gage. Stop rotating the crankshaft immediately when the gauge stops moving upward with crankshaft rotation. On diesel adapters, if the gauge is **not** included with the adapter being used, a slender rod can be used as a substitute. On gas engines, there are no provisions for using a gauge. Approximate TDC will determined using the complimentary cylinder valve overlap method.

For best results, the piston should not be traveling downward when rotation is stopped. If the piston crosses past TDC and starts traveling downward, the piston rings will unseat in the piston ring lands slightly, causing a potential source of measurement error. If the piston starts traveling downward, reverse the barring rotation and rotate the crankshaft until the piston crosses back past TDC in reverse plus 1/3 of a crankshaft rotation. Bar the engine in the normal rotation and try again.

Mechanical Diagnostic Kit, Part Number 5394335, includes two leakage testers. See the chart below to make sure the correct one is used.

> [!note] Note · Примечание
> Use of incorrect leakage tester will generate measurement error.

| **Leakage Test Part Number** | **Usage** |
|---|---|
| 5394340 | Engines with a bore size smaller than 127 mm \[5 in\] |
| 5394360 | Engines with a bore size equal to or larger than 127 mm \[5 in\] |

Connect leakage tester to compression and leak down check adapter.

> [!note] Note · Примечание
> Applying air pressure to the test cylinder may cause the engine to attempt to rotate. Engine must be prevented from rotating during testing.

Connect shop air to leakage tester. 100 psi is preferred, but the measurement process will work with lower pressure.

Open the leakage tester pressure regulator and adjust until the gauge closest to the pressure regulator (reference gauge) reads 100 psi (or maximum available pressure).

Allow system pressure to stabilize. Record pressure on the gauge farthest from the pressure regulator (cylinder gauge). Record the pressures.

Use the following formula to determine cylinder leakage as a percent: ((Reference Gauge value – Cylinder Gauge value) / Reference Gauge value) x 100 = Cylinder Leakage percent.

Repeat the test for all remaining cylinders as necessary.

Diagnosis:

If one cylinder leakage is higher compared to other cylinders, to other similar engines, or to published specifications, use stethoscope, Part Number 5394338 from kit, Part Number 5394335, to try to determine where the cylinder is leaking when pressurized.

| **If air can be heard escaping from** | **Likely cause of leakage** |
|---|---|
| Intake Manifold | Intake valve or valve seat, cracked head |
| Exhaust Manifold or Turbocharger | Exhaust valve or valve seat, cracked head |
| Coolant System | Cylinder head gasket, cracked head |
| Engine Crankcase | Piston, piston rings, cylinder bore |

Remove cylinder head and inspect suspect components further to determine root cause. Refer to engine-specific procedures.

If all cylinder leakages are uniform compared to each other but high compared to a similar engine or published specification, the engine may be in need of a full or partial overhaul. Inspect all suspect parts per engine specific procedures and established reuse guidelines.

### Finishing Steps

> [!danger] WARNING · Опасно
> Wear appropriate eye and face protection when using compressed air. Flying debris and dirt can cause personal injury.

> [!danger] WARNING · Опасно
> When using a steam cleaner, wear safety glasses or a face shield, as well as protective clothing. Hot steam can cause serious personal injury.

> [!note] Note · Примечание
> Bleeding air from the fuel system is an important step. Air in fuel will make an engine hard to start or **not** start.

- Install compression and leak down check adapter.
- Install the fuel injectors. [[377-006-026 — Injector|Refer to Procedure 006-026 in Section 6.]]
- Bleed air from the fuel system. See the Prime step in the following procedure. Refer to Procedure 005-234 in Section 5.
- Operate the engine to check for leaks.
