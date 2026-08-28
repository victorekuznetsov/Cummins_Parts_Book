---
aliases:
  - "Турбокомпрессор"
type: "Процедура"
doc: "1016-010-033"
title_en: "Turbocharger"
title_ru: "Турбокомпрессор"
modified: "2024-09-04"
engines:
  - "77804810"
families:
  - "15N"
manuals:
  - "5659763"
figures: 28
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/1016/1016-010-033.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/1016-010-033.pdf"
tags:
  - "документ/процедура"
  - "двигатель/15N"
---

# Turbocharger
**Турбокомпрессор**

> [!abstract] Процедура · `1016-010-033`
> **Двигатели:** [[77804810 — 15N CM2380 M104B CPL 5977|77804810]]
> **Семейство:** 15N
> **Входит в руководства:** [[5659763 — 15N CM2380 M104B Service Manual|5659763]]
> **Секции:** Section 10 - Air Intake System - Group 10
> **Даты:** изменён 2024-09-04
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/1016/1016-010-033.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/1016-010-033.pdf)

### Exploded View

![[10r00279.png]]

Turbocharger Exploded View

1. High-temperature stud - quantity 4
2. Turbocharger gasket - quantity 1
3. Turbocharger - quantity 1
4. Turbocharger actuator air line - quantity 1
5. Flange nut - quantity 4

### Select Service Tools

#### Recommended Cummins® Service Tools

- Dial depth gauge, Part Number ST-537
- Fluorescent tracer, Part Number 3376891
- High-intensity black light, Part Number 3163338
- Penetrating oil, Part Number 2892116, or equivalent
- Air Handling Clean Care Kit, Part Number 4919588
- High-temperature anti-seize compound, Part Number 3824879

#### Additional Service Items

- Holset® turbocharger clearance tools.

### Initial Check

Remove the inlet pipe and air inlet connection from the turbocharger. Refer to Procedure 010-022 in Section 10.

Inspect the turbocharger compressor impeller blades for damage.

Replace the turbocharger if damage is found. See Remove and Install sections of this procedure.

If the compressor impeller is damaged, inspect the inlet piping and filter element for damage and debris.

Replace any damaged parts before operating the engine.

![[10r00280.png]]

Inspect the turbine wheel for damage.

Replace the turbocharger if damage is found. See Remove and Install sections of this procedure.

![[10r00281.png]]

#### Turbocharger Actuator Air Line Check

- Inspect the turbocharger actuator air line. Refer to Procedure 010-118 in Section 10.

#### Wastegate Check

- Inspect the lever pin.

Replace the turbocharger if the lever pin is bent or worn excessively. See Remove and Install sections of this procedure.

![[10900200.png]]

- Inspect the valve and valve seat for cracks or erosion.

> [!note] Note · Примечание
> On some turbochargers, removal of the turbine exhaust outlet cover may be necessary to inspect the valve and valve seat. If the turbine exhaust outlet cover is removed, replace the gasket before reinstalling the cover.

Replace the turbocharger if the valve or valve seat are excessively cracked or eroded. See Remove and Install sections of this procedure.

![[10900201.png]]

- Actuate the lever by hand to verify that the shaft rotates freely and is **not** seized.
- Check for excessive movement between the shaft and bushing.

Replace the turbocharger if the shaft is seized or if there is excessive movement between the shaft and bushing. See Remove and Install sections of this procedure.

Turbocharger shaft is seized usually due to coolant leakage from Exhaust Gas Recirculation (EGR). If the wastegate valve color is found to be different with turbine housing internal surface, it **must** be checked for coolant leakage.

![[10900038.png]]

#### Axial Clearance Check

- Use dial depth gauge, Part Number ST-537.
- Push the rotor assembly away from the gauge.
- Set the gauge to zero.

![[10900127.png]]

- Push the rotor assembly toward the gauge and record the reading.

Replace the turbocharger if the clearance does **not** meet specifications. See Remove and Install sections of this procedure.

| Axial Specifications |  |  |
|---|---|---|
| mm |  | in |
| 0.025 | MIN | 0.001 |
| 0.127 | MAX | 0.005 |

![[10900128.png]]

Radial Clearance Check

Use Holset® turbocharger clearance tools to measure the turbocharger radial clearance.

![[10600221.png]]

Or visually check if the impeller rubs with the compressor housing. If **not**, it means the radial clearance meets specifications.

Replace the turbocharger if the radial bearing clearance does **not** meet specifications. See Remove and Install sections of this procedure.

| Radial Specifications |  |  |
|---|---|---|
| mm |  | in |
| 0.330 | MIN | 0.013 |
| 0.508 | MAX | 0.020 |

![[10c00137.png]]

Inspect the turbocharger compressor intake and discharge for oil.

If oil is present in the compressor intake, as well as in the discharge, check upstream of the turbocharger for the source of the oil.

Engines equipped with a Closed Crankcase Ventilation (CCV) system, in which the crankcase is vented into the air inlet piping, can exhibit some oil misting of the compressor blades. This is normal and does **not** signify turbocharger damage. If oil is pooling in the turbocharger cavities or the charge air cooler cavities, see the Crankcase Gases (Blowby) Excessive troubleshooting symptom tree in Section TS in 15N CM2380 M104B Fault Code Troubleshooting Manual, Bulletin [[5659765 — 15N CM2380 M104B Fault Code Troubleshooting Manual Change History\|5659765]].

Even if oil leakage is found from the turbocharger, as long as the turbocharger radial and axial clearances meet specification, do **not** replace the turbocharger, till the root cause causing the fault is found. Repair and clean the turbocharger and related pipe.

If oil is found on turbocharger compressor inlet pipe, and the turbocharger clearance meets specification, the oil is usually from CCV. Check if there is oil in the pipe that connects CCV and turbocharger as well. If yes, replace or repair CCV, and clean related pipe and turbocharger.

If the engine experiences a turbocharger malfunction or any other occasion where oil is put into the charge air system, the charge air system **must** be inspected and cleaned. [[99-010-027 — Charge-Air Cooler|Refer to Procedure 010-027 in Section 10.]]

![[14x00010.png]]

If heavy deposits and/or streaks of oil are present **only** in the discharge side, install the air inlet and charge air cooler piping to check the air restriction indicator. See equipment manufacturer service information.

Check for air intake restriction. Refer to Procedure 010-031 in Section 10.

If no intake restriction is found, replace the turbocharger.

![[10900128.png]]

### Leak Test

Add one unit of fluorescent tracer, Part Number 3376891, to each 38 liters \[ 10 U.S. gal \] of engine lubricating oil.

Operate the engine at low idle for 10 minutes.

![[10r00282.png]]

Shut the engine off.

Allow the turbocharger to cool.

Remove the exhaust pipe and exhaust pressure regulator from the turbine housing.

![[10r00283.png]]

Use a high-intensity black light, Part Number 3163338, to inspect the turbine outlet for leaks.

A yellow glow indicates an oil leak.

A dark blue glow indicates fuel in the oil.

![[10r00284.png]]

If oil is found on the turbine housing, remove the oil drain line and check for restrictions. Refer to Procedure 010-045 in Section 10.

Clear any restrictions found.

Install the drain line and new o-ring seals into the engine block. Refer to Procedure 010-045 in Section 10.

![[10r00285.png]]

If the oil drain line is **not** restricted, remove the turbocharger.

![[10900505.png]]

Use a high-intensity black light, Part Number 3163338, to inspect the turbine inlet for leaks.

A yellow glow indicates an oil leak from the engine.

If a yellow glow is seen, the turbocharger can be reinstalled and returned to service. A light coating of oil in the turbine housing and on the turbine does **not** need to be cleaned as it will be burned off during engine operation. Any puddles of oil in the turbine housing **must** be removed with a clean rag prior to installation.

If a yellow glow is **not** seen in the turbine inlet, replace the turbocharger.

![[10r00286.png]]

Install the exhaust pipe to the turbocharger turbine outlet.

Install the intake pipe to the turbocharger compressor inlet.

![[10900507.png]]

### Preparatory Steps

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

> [!danger] WARNING · Опасно
> To reduce the possibility of personal injury, avoid direct contact of hot oil with your skin.

> [!danger] WARNING · Опасно
> Some state and federal agencies have determined that used engine oil can be carcinogenic and cause reproductive toxicity. Avoid inhalation of vapors, ingestion, and prolonged contact with used engine oil. If not reused, dispose of in accordance with local environmental regulations.

- Disconnect the batteries. See equipment manufacturer service information.
- Remove the exhaust piping. See equipment manufacturer service information.
- Disconnect the charge air cooler piping. Refer to Procedure 010-019 in Section 10.
- Remove the turbocharger compressor outlet connection. Refer to Procedure 010-132 in Section 10.
- Remove the turbocharger compressor air inlet connection. Refer to Procedure 010-022 in Section 10.
- Remove the turbocharger heat shield and exhaust manifold heat shield. Refer to Procedure 011-032 in Section 11.
- Remove the oil supply line from the turbocharger. Refer to Procedure 010-046 in Section 10.
- Remove the oil drain line from the turbocharger. Refer to Procedure 010-045 in Section 10.
- Remove the turbocharger coolant hoses. Refer to Procedure 010-041 in Section 10.

### Remove

> [!danger] WARNING · Опасно
> This component or assembly weighs greater than 23 kg \[ 50 lb \]. To prevent serious personal injury, be sure to have assistance or use appropriate lifting equipment to lift this component or assembly.

> [!warning] CAUTION · Осторожно
> Before discarding the turbocharger mounting gasket, identify the type of gasket removed. Some turbocharger mounting gaskets have a divider down the middle of the gasket and some do not. Only replace the gasket with a like gasket. Use of the incorrect gasket will result in turbocharger damage.

Spray penetrating oil, Part Number 2892116, or equivalent, on the four turbocharger mounting nuts and let soak for 5 minutes before trying to remove the nuts.

Remove the four turbocharger mounting nuts.

Remove the turbocharger and gasket.

Discard the gasket.

Remove and discard all the mounting studs on turbocharger or exhaust manifold.

Cover the opening on the exhaust manifold with heavy tape from Air Handling Clean Care Kit, Part Number 4919588.

![[10r00287.png]]

### Clean and Inspect for Reuse

> [!warning] CAUTION · Осторожно
> While cleaning the exhaust mounting flange, ensure no debris falls into the turbine. Damage to the engine and turbocharger can occur.

Clean the turbocharger and exhaust manifold gasket surfaces.

Inspect the turbocharger, exhaust manifold gasket surfaces, and mounting studs for cracks and other damage.

![[10r00288.png]]

Unacceptable cracking of the turbine housing inlet flange may require turbine housing replacement. Acceptance and rejection guidelines are shown in the illustration.

Acceptable exhaust manifold and turbine housing cracks:

- **Must** be 10 mm \[ 0.39 in \] or less in length.
- **Must** be separated from each other by no less than 10 mm \[ 0.39 in \].
- **Must not** extend to the edge of the flange.

Acceptable exhaust manifold and turbine housing flange scaling:

- **Must** be less than 0.1 mm \[ 0.004 in \] in depth.

Replace the exhaust manifold if any cracks are found in the mounting flange surfaces. Refer to Procedure 011-007 in Section 11.

![[10d00789.png]]

> [!danger] WARNING · Опасно
> When using solvents, acids, or alkaline materials for cleaning, follow the manufacturer's recommendations for use. Wear goggles and protective clothing to reduce the possibility of personal injury.

> [!danger] WARNING · Опасно
> When using a steam cleaner, wear safety glasses or a face shield, as well as protective clothing. Hot steam can cause serious personal injury.

> [!danger] WARNING · Опасно
> Wear appropriate eye and face protection when using compressed air. Flying debris and dirt can cause personal injury.

Remove all carbon deposits and gasket material from surfaces.

Use solvent or steam to clean the exterior of the turbocharger.

Dry with compressed air.

![[10r00289.png]]

Inspect the turbine and compressor housings.

If cracks that go all the way through the outer walls are found, the turbocharger **must** be replaced.

A charge air cooler malfunction can cause progressive damage to the turbine housing. If the turbine housing is damaged, check the charge air cooler. [[99-010-027 — Charge-Air Cooler|Refer to Procedure 010-027 in Section 10.]]

![[10r00290.png]]

If the engine experiences a turbocharger malfunction or any other occasion in which oil or debris is put into the charge air system, the charge air system **must** be inspected and cleaned. [[99-010-027 — Charge-Air Cooler|Refer to Procedure 010-027 in Section 10.]]

![[oi100wi.png]]

### Install

> [!danger] WARNING · Опасно
> This component or assembly weighs greater than 23 kg \[ 50 lb \]. To prevent serious personal injury, be sure to have assistance or use appropriate lifting equipment to lift this component or assembly.

> [!warning] CAUTION · Осторожно
> The new gasket must match the one that is removed. Use of the incorrect gasket will result in turbocharger damage. Never reuse a turbocharger mounting gasket.

Install new mounting studs.

Apply a film of high-temperature anti-seize compound, Part Number 3824879, to the turbocharger mounting studs.

[[1016-011-073 — Exhaust Manifold Turbocharger Mounting Stud Replacement|Refer to Procedure 011-073 in Section 11.]]

Install a new mounting gasket, turbocharger, and the four mounting nuts.

Tighten the mounting nuts in a criss-cross pattern.

> [!tip] Момент затяжки · Torque Value
> 80 n•m [59 ft-lb]

After all four nuts are tightened, re-tighten the first two nuts.

![[10r00287.png]]

### Prime

Install and tighten the turbocharger oil drain line. Refer to Procedure 010-045 in Section 10.

![[10900513.png]]

Lubricate the bearings by pouring 60 cc \[ 2 fl-oz \] to 90 cc \[ 3 fl-oz \] of clean 15W-40 engine oil in the turbocharger oil supply line fitting.

Rotate the turbine wheel to allow oil to enter the bearing housing.

![[10900514.png]]

### Finishing Steps

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

- Install the turbocharger coolant hoses. Refer to Procedure 010-041 in Section 10.
- Install the oil drain line to the turbocharger. Refer to Procedure 010-045 in Section 10.
- Install and tighten the turbocharger oil supply line. Refer to Procedure 010-046 in Section 10.
- Install the turbocharger heat shield and exhaust manifold heat shield. Refer to Procedure 011-032 in Section 11.
- Install the turbocharger compressor air inlet connection. Refer to Procedure 010-022 in Section 10.
- Install the turbocharger compressor outlet connection, V-band clamp, and a new o-ring seal on the turbocharger compressor discharge outlet, if applicable. Refer to Procedure 010-132 in Section 10.
- Install the charge air cooler piping. Refer to Procedure 010-019 in Section 10.
- Install the exhaust piping. See equipment manufacturer service information.
- Connect the batteries. See equipment manufacturer service information.
- Operate the engine and check for leaks.

If a malfunction results in oil, excessive fuel, or excessive black smoke entering the exhaust system, the aftertreatment system **must** be inspected.
