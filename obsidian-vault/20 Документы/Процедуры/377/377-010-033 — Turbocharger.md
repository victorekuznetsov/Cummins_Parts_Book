---
aliases:
  - "Турбокомпрессор"
type: "Процедура"
doc: "377-010-033"
title_en: "Turbocharger"
title_ru: "Турбокомпрессор"
modified: "2023-02-10"
manuals:
  - "5411181"
figures: 49
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/377/377-010-033.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/377-010-033.pdf"
tags:
  - "документ/процедура"
  - "группа/377"
---

# Turbocharger
**Турбокомпрессор**

> [!abstract] Процедура · `377-010-033`
> **Входит в руководства:** [[5411181 — X15 CM2350 X114B - Efficiency Series Service Manual|5411181]]
> **Секции:** Section 10 - Air Intake System · Section 10 - Air Intake System - Group 10
> **Даты:** изменён 2023-02-10
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/377/377-010-033.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/377-010-033.pdf)

### Select Service Tools

#### Recommended Cummins® Service Tools

- Leak Test Kit, Part Number 2892320, or equivalent
- Air Pressure Regulator Kit, Part Number 3164231, or equivalent
- Turbocharger Coolant Leak Test Kit, Part Number 5299505, or equivalent
- Fluorescent tracer, Part Number 3376891, or equivalent
- Air Handling Clean Care Kit, Part Number 4919588, or equivalent
- Anti-seize compound, Part Number 3824397, or equivalent
- Clean care parts, Part Numbers 4919216, or equivalent
- Abrasive disc, Part Number 3824541, or equivalent

#### Additional Service Items

- Shop air
- Soapy water
- Scotch-Brite™ 7448 abrasive pad or fine crocus cloth
- INSITE™ electronic service tool

### Initial Check

Brush away any loose dirt from around the area of air handling connections to avoid contamination of the interior of the engine.

Shut the engine OFF.

Allow the turbocharger to cool.

If turbocharger blade damage is suspected, do the following:

- Remove the intake pipe from the turbocharger. See equipment manufacturer service information.
- Inspect the turbocharger compressor impeller blades for damage.
- Replace the turbocharger if damage is found.

![[10200092.png]]

If the turbocharger compressor impeller is damaged, do the following:

- Inspect the intake piping and filter element for damage.
- Repair any damaged parts before operating the engine.
- See High Blowby and Lubricating Oil Consumption Caused by Dirt and Dust Ingestion, Service Bulletin [[5613318 — Checking For Dirt and Dust Ingestion While Troubleshooting High Blowby|5613318]].
- Inspect lubricating oil filter for debris. Refer to Procedure 007-083 in Section 7.

![[ci8ilca.png]]

Inspect the turbocharger turbine wheel.

- Remove the aftertreatment adapter pipe from the turbocharger. [[377-011-043 — Aftertreatment Adapter Pipe|Refer to Procedure 011-043 in Section 11.]]
- Inspect the turbine wheel for damage.
- Replace the turbocharger if damage is found.
- If turbine wheel is damaged, see Prevention of Turbocharger Damage After Engine Mechanical Issue, Service Bulletin [[4326040 — Prevention of Turbocharger Damage After Engine Mechanical Issue|4326040]].
- If turbine wheel is damaged, inspect lubricating oil filter for debris. Refer to Procedure 007-083 in Section 7.

![[10l00079.png]]

Lubricating oil leaks from the compressor (cold side) or turbine (hot side) seals are symptoms of air restrictions, leaks, or a restricted turbocharger oil drain line.

If a turbocharger is leaking oil, see Service Bulletin, Turbocharger Lubricating Oil Leak Troubleshooting, Bulletin [[5504213 — Turbocharger Lubricating Oil Leak Troubleshooting|5504213]].

After review of the above service bulletin reference, the following troubleshooting trees in Section TS, if necessary.

- Turbocharger - Compressor Seal Oil Leak troubleshooting symptom tree
- Turbocharger - Turbine Seal Oil Leak troubleshooting symptom tree.

![[10c00591.png]]

### Leak Test

> [!danger] WARNING · Опасно
> Do not remove the pressure cap from a hot engine. Wait until the coolant temperature is below 50°C \[120°F\] before removing the pressure cap. Heated coolant spray or steam can cause personal injury.

> [!danger] WARNING · Опасно
> Coolant is toxic. Keep away from children and pets. If not reused, dispose of in accordance with local environmental regulations.

This test **only** needs to be performed if troubleshooting for coolant loss, or if an internal leak is suspected.

> [!note] Note · Примечание
> The engine **must** be within 3°C or 5°F of ambient temperature to perform the test.

If a turbocharger internal coolant leak is suspected, use the Turbocharger Coolant Leak Test Kit, Part Number 5299505, or equivalent, along with Air Pressure Regulator Kit, Part Number 3164231, or equivalent, to check for a leak.

- Drain the cooling system. Refer to Procedure 008-018 in Section 8.

![[ra8homa.png]]

To test for either a turbocharger bearing housing internal coolant leak or a leaking variable geometry turbocharger (VGT) actuator, disconnect the coolant inlet line to the bearing housing and install the M16 banjo block-off fitting from the Turbocharger Coolant Leak Test Kit, Part Number 5299505, or equivalent.

Lubricate the o-ring with clean engine oil before installation.

> [!tip] Момент затяжки · Torque Value
> 27 n•m [239 in-lb]

![[10l00089.png]]

Disconnect the turbocharger coolant return line at the VGT and install the adapter fitting for the pressure regulator supplied with Turbocharger Coolant Leak Test Kit, Part Number 5299505.

Disconnect the turbocharger actuator coolant return line at the turbocharger actuator and install the plug supplied with Turbocharger Coolant Leak Test Kit, Part Number 5299740, to block off the turbocharger actuator coolant outlet port.

Lubricate the o-ring with clean engine oil before installation.

> [!tip] Момент затяжки · Torque Value
> 27 n•m [239 in-lb]

![[10l00081.png]]

> [!danger] WARNING · Опасно
> Wear appropriate eye and face protection when using compressed air. Flying debris and dirt can cause personal injury.

- Use compressed air supply to pressurize the VGT to 276 kPa \[40 psi\].
- Close the air pressure regulator.
- Watch for the pressure to decrease. The pressure **must not** decrease more than 34 kPa \[5 psi\] in 1 minute.

![[10l00082.png]]

- If the pressure decreases, use a spray bottle of soapy water to wet the coolant leak test connections and threaded joints. Bubbles will appear if the connections or threaded joints are leaking
- If the pressure decreases and the hose connections or threaded joints are **not** leaking, continue to the next step.
- If the pressure does **not** decrease, no leaks have been detected in the VGT. Proceed to the next steps for testing the actuator for coolant leaks.

![[10l00083.png]]

Remove the electric VGT actuator. [[377-010-134 — Variable Geometry Turbocharger Actuator, Electric|Refer to Procedure 010-134 in Section 10.]]

Inspect the pressure testing plate o-ring. Replace the o-ring if damage is found.

![[10l00084.png]]

Install the pressure testing plate onto the turbo bearing housing with the o-ring facing the turbocharger bearing housing.

Tighten the capscrews.

> [!tip] Момент затяжки · Torque Value
> 11 n•m [97 in-lb]

![[10s00052.png]]

Use compressed air supply to pressurize the turbocharger bearing housing to 276 kPa \[40 psi\].

Close the air pressure regulator.

Watch for the pressure to decrease. The pressure **must not** decrease more than 34 kPa \[5 psi\] in 1 minute.

![[10l00182.png]]

If the pressure decreases, use a spray bottle of soapy water to wet all hose connections. Bubbles will appear if the connections are leaking.

If the pressure decreases and the hose connections are **not** leaking, replace the turbocharger.

If no external leak source is detected, the coolant leak is internal to the electric VGT actuator. Replace the electric VGT actuator. [[377-010-134 — Variable Geometry Turbocharger Actuator, Electric|Refer to Procedure 010-134 in Section 10.]]

![[10s00054.png]]

### Check for Correct Component

Compare the assembly number (1) on the turbocharger dataplate with the turbocharger specified in the engine control parts list (CPL) number (2) listed on the engine dataplate.

![[10c00357.png]]

If the correct turbocharger was **not** installed, remove and install the correct turbocharger.

![[10c00358.png]]

### Preparatory Steps

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

> [!danger] WARNING · Опасно
> Coolant is toxic. Keep away from children and pets. If not reused, dispose of in accordance with local environmental regulations.

> [!danger] WARNING · Опасно
> Do not remove the pressure cap from a hot engine. Wait until the coolant temperature is below 50°C \[120°F\] before removing the pressure cap. Heated coolant spray or steam can cause personal injury.

> [!note] Note · Примечание
> Brush away any loose dirt from around the area of the air handling connections to avoid contamination of the interior of the engine.

- Disconnect the batteries. See equipment manufacturer service information.
- Drain the cooling system. Refer to Procedure 008-018 in Section 8.
- Remove the inlet air piping and the discharge elbow on the charge air cooler connection. See equipment manufacturer service information.
- Remove the turbocharger adapter and air compressor inlet tube. [[377-012-109 — Air Compressor Inlet Tube|Refer to Procedure 012-109 in Section 12.]]
- Disconnect the turbocharger speed sensor. Refer to Procedure 019-390 in Section 19.
- Disconnect the turbocharger compressor air inlet temperature sensor. Refer to Procedure 019-395 in Section 19.
- Remove the turbocharger coolant hoses. Refer to Procedure 010-041 in Section 10.
- Remove the oil supply line from the turbocharger. Refer to Procedure 010-046 in Section 10.
- Remove the oil drain line from the turbocharger. Refer to Procedure 010-045 in Section 10.
- Some applications require removal of the aftertreatment adapter tube pipe. [[377-011-043 — Aftertreatment Adapter Pipe|Refer to Procedure 011-043 in Section 11.]]
- Use protective caps from the Air Handling Clean Care Kit, Part Number 4919588, or equivalent, to cover open points.

### Remove

Care **must** be taken **not** to damage the turbocharger compressor inlet air temperature sensor and the turbocharger speed sensor when removing the turbocharger from the engine.

> [!note] Note · Примечание
> Spiral locknuts are utilized to reduce the risk of the turbocharger mounting nuts falling off. These nuts have more of a tendency to **not** loosen freely. If the nut does **not** loosen freely, split the nut to avoid breaking a mounting stud.

Remove the nuts from the turbocharger studs and remove the turbocharger.

Remove the turbocharger and discard the gaskets.

![[10c00359.png]]

Cover the turbocharger exhaust inlet port with heavy tape or a protective cap from the Air Handling Clean Care Kit, Part Number 4919588, or equivalent. Cover the opening on the exhaust manifold with heavy tape.

![[10c00363.png]]

### Disassemble

> [!note] Note · Примечание
> The turbine housing **must not** be removed from the turbocharger for any repair, except when evidence of coolant intrusion is found.

Place the turbocharger on a sturdy table.

Cover the oil supply and drain ports in the bearing housing. Use Clean Care Parts, Part Numbers 4919216 and 4919221, or equivalent.

Remove the turbocharger actuator. [[377-010-134 — Variable Geometry Turbocharger Actuator, Electric|Refer to Procedure 010-134 in Section 10.]]

![[10l00085.png]]

Unbolt the V-band clamp.

After the clamp locknut is loosened, the V-band clamp can be spread and locked open by pressing the threaded end of the clamp against the opposite end. This can aid in the removal of the turbine housing.

> [!note] Note · Примечание
> The V-band clamp **must** be saved for orientation purposes **only**. Do **not** reuse the V-band clamp or locknut.

![[10a00137.png]]

> [!warning] CAUTION · Осторожно
> The turbine blades or the nozzle ring can be easily damaged. Care is required for the turbine housing removal process.

Slightly lift or angle the turbocharger while using a lead hammer to tap the turbine housing down against the bench surface.

Tap so that the turbine housing can be removed squarely. This will reduce the possibility of damage to the nozzle ring assembly. A considerable amount of force is required to remove the turbine housing.

As the bearing housing and compressor housing assembly loosen, gently lift the assembly from the turbine housing and carefully place the assembly on a sturdy table, compressor housing side down.

![[10a00139.png]]

Inspect the VGT nozzle ring for vane damage.

If there are dents, dings, or pieces broken out of any of the nozzle vanes, the turbocharger **must** be replaced.

![[10a00144.png]]

Use a wire brush and air tool or drill to clean both the horizontal and vertical mating surfaces on the turbine housing.

Remove the outer seal ring and outer seal ring carrier from the turbine housing and discard them.

Use the wire brush and an air tool or drill to clean the outer seal ring seating area in the turbine housing.

![[10o00072.png]]

Extend the nozzle ring from the bearing housing by rotating the sector gear.

> [!note] Note · Примечание
> If the sector gear will **not** move, lightly tap inward around the outside of the nozzle ring using a rubber hammer.

Use a wire brush and an air tool or drill to clean both the horizontal and vertical mating surfaces on the bearing housing.

Use a wire brush and air tool or drill to remove any buildup found on the nozzle ring. The outer vertical sides of the nozzle ring **must** be clean and free of buildup.

> [!note] Note · Примечание
> Avoid contacting the turbine wheel with the wire brush.

![[10o00073.png]]

With the nozzle extended, clean the loosened debris from all components.

![[10o00074.png]]

Verify sector gear travels.

If sector gear travel is limited, or can **not** be moved by hand, replace the turbocharger.

![[10a00158.png]]

Check for burrs on the leading edge of the nozzle vanes.

The surface of the vane face **must** be smooth. A burr can be felt with the fingertip.

Use an abrasive disc, Part Number 3824541, or equivalent, and an air tool or drill to clean the burrs from the edge of each vane.

Do **not** use excessive force or time to clean the vanes. Burrs are easy to remove.

Make sure the burrs are removed from each vane by feeling with the fingertip.

Carefully clean off any debris around the bearing housing surface and seal groove.

![[10a00146.png]]

### Clean and Inspect for Reuse

Inspect the VGT actuator and mechanism for proper operation. [[377-010-134 — Variable Geometry Turbocharger Actuator, Electric|Refer to Procedure 010-134 in Section 10.]]

![[10l00086.png]]

Inspect for cracks in the turbocharger and compressor casings.

Replace the turbocharger if through cracks in the outer walls are found.

Inspect for cracks on the turbine inlet and exhaust mounting flanges. Replace the turbocharger if any cracks are found.

![[10c00387.png]]

> [!note] Note · Примечание
> All openings on the turbocharger, including the turbine inlet connection, **must** be plugged with caps from the Air Handling Clean Care Kit, Part Number 4919588, during flange cleaning.

Clean the turbocharger and exhaust manifold where the retaining nut contacts the turbocharger and exhaust manifold.

Clean the mating surfaces with Scotch-Brite™ 7448 abrasive pad.

After abrasive cleaning, wipe debris from both surfaces with a clean shop towel.

The surface under the mounting nuts **must** be free of dirt, rust, or any other debris, before applying anti-seize compound, Part Number 3824397, or equivalent.

![[10200013.png]]

Replace the turbocharger if any leaks are found.

Check for evidence of coolant in the oil supply and oil drain fittings. If coolant is found reference Coolant in the Lubricating Oil troubleshooting symptom tree in Section TS.

![[10c00388.png]]

Inspect the turbocharger compressor V-band outlet and the discharge elbow V-band connection for dents or fretting.

Replace the turbocharger or discharge elbow, if damaged, to prevent compressed air leaks.

![[tb1crmb.png]]

Check the axial movement of the turbocharger wheels and shaft.

| Turbocharger Axial Clearance |  |  |
|---|---|---|
| mm |  | in |
| 0.051 | MIN | 0.002 |
| 0.152 | MAX | 0.006 |

If the turbocharger axial clearance is **not** within specifications, the turbocharger **must** be replaced.

![[10c00061.png]]

Inspect the compressor wheel for signs of rubbing against the compressor cover. Replace the turbocharger if rubbing evidence is seen.

Check the radial movement of the turbocharger wheels and shaft.

Use light finger pressure to push the compressor wheel toward the side of the compressor housing.

Repeat the procedure for the turbine wheel and housing.

Replace the turbocharger if either wheel contacts the housing.

![[10c00137.png]]

> [!danger] WARNING · Опасно
> When using solvents, acids, or alkaline materials for cleaning, follow the manufacturer's recommendations for use. Wear goggles and protective clothing to reduce the possibility of personal injury.

> [!warning] CAUTION · Осторожно
> Do not use caustic cleaners to clean the charge air cooler. Damage to the charge air cooler will result.

If the engine experiences turbocharger damage or any other occasion where oil or debris is put into the charge air system, the charge air and intake air systems **must** be inspected and cleaned.

Make sure all system level causes of oil leaks have been addressed before proceeding. Reference the following troubleshooting symptom trees in Section TS:

- Turbocharger - Compressor Side Oil Leak troubleshooting tree
- Turbocharger - Turbine Side Oil Leak troubleshooting symptom tree.

Inspect the charge air cooler. [[377-010-027 — Charge Air Cooler|Refer to Procedure 010-027 in Section 10.]]

Inspect the air shutoff valve, if equipped. Refer to Procedure 010-143 in Section 10.

Inspect the intake throttle actuator, if equipped. Refer to Procedure 010-140 in Section 10.

Inspect the air compressor. Refer to Procedure 012-003 in Section 12.

Inspect the air intake manifold. [[377-010-023 — Air Intake Manifold|Refer to Procedure 010-023 in Section 10.]]

Clean turbocharger outlets with a non-reactive oil cleaning spray or solution, Part Number 3824421, or equivalent, and a lint-free towel.

![[10a00265.png]]

### Assemble

Place the new V-band clamp directly on top of the old V-band clamp. Align them exactly.

Use the alignment marks that were made on the old V-band clamp to mark the new V-band clamp.

![[10a00151.png]]

Install the outer seal ring and outer seal ring carrier in the turbine housing.

The gap for the seal ring can be placed in any position.

![[10o00075.png]]

Place the new C-seal (bearing housing to turbine housing seal) into the groove on the turbine housing.

Anti-seize compound can be placed in a few places around the circumference of the C-seal to hold the C-seal in place during the assembly process.

![[10o00076.png]]

Do **not** reuse the turbine housing V-band clamp.

To install the turbine housing, position the V-band clamp over the turbine housing and align the ink marks applied during the disassembly process.

The V-band clamp can be spread and locked open by pressing the threaded end of the clamp against the opposite end. This will aid in allowing the bearing housing to drop into place.

![[10o00077.png]]

Align the marks on the bearing housing and the turbine housing.

Carefully lower the bearing housing into the turbine housing.

Carefully rotate the bearing housing, as needed, to engage **all** of the nozzle vanes into the shroud plate.

Remain as parallel to the table as possible while lowering the turbine housing, until the nozzle vanes are fully engaged.

![[10o00078.png]]

If necessary, rotate the assembly so the compressor inlet faces downward. Lightly tap the turbine housing into place until fully seated on the bearing housing.

![[10a00157.png]]

Move the sector gear back and forth by hand to check for smooth movement.

If movement is **not** smooth, gently rotate the turbine housing, as necessary, while using a lead hammer to allow the sector gear to move freely.

Place the new V-band clamp in the correct orientation and tighten the locknut.

> [!tip] Момент затяжки · Torque Value
> 6.8 n•m [60 in-lb]

Using a small hammer, lightly tap the V-band clamp into place, starting on the side opposite the T-bolt and locknut.

Work your way around the clamp in each direction from this center point, moving toward the T-bolt and locknut.

Tighten the V-band clamp.

> [!tip] Момент затяжки · Torque Value
> 11.3 n•m [100 in-lb]

![[10a00158.png]]

Verify proper sector gear travel. [[377-010-134 — Variable Geometry Turbocharger Actuator, Electric|Refer to Procedure 010-134 in section 10.]]

![[10l00070.png]]

### Install

Remove the protective caps and heavy tape from the Air Handling Clean Care Kit, Part Number 4919588, used to cover open points in the air handling system.

![[10c00363.png]]

> [!warning] CAUTION · Осторожно
> Remove the plastic shipping plugs in the turbocharger bearing housing for the oil supply and oil drain. Failure to remove the oil supply shipping plug will damage the turbocharger. Failure to remove the oil drain shipping plug will damage the oil compressor seal. Engine oil can be sucked through the air intake system and cause engine acceleration and overspeeding that can result in a fire, an explosion, and extensive property damage.

If installing a new turbocharger, remove the plastic shipping plugs from the oil drain and oil supply holes located in the turbocharger bearing housing.

![[10c00365.png]]

Install the oil supply fitting. Refer to Procedure 010-046 in Section 10.

Pour 50 to 60 cc \[2 to 3 oz\] of clean engine oil into the turbocharger oil supply opening through the oil supply fitting.

![[10t00006.png]]

Apply a film of high-temperature anti-seize compound, Part Number 3824397, or equivalent, to the turbocharger mounting studs and to the flange area on the retaining nuts. Properly applying anti-seize compound will reduce the possibility of the nuts loosening over time.

![[tb1hshc.png]]

> [!warning] CAUTION · Осторожно
> Do not rotate the turbocharger turbine housing. Loosening the turbine V-band and rotating the turbine housing can cause damage to internal variable geometry mechanism.

Care **must** be taken **not** to damage the turbocharger compressor inlet air temperature sensor and the turbocharger speed sensor when installing the turbocharger.

Install a new gasket, the turbocharger, and the mounting nuts. Tighten the mounting nuts. After all mounting nuts are tightened, tighten the first mounting nut again.

> [!tip] Момент затяжки · Torque Value
> 81 n•m [60 ft-lb]

![[10c00359.png]]

If installing a new turbocharger, rotate the turbocharger compressor housing to properly align with the charge air cooler piping.

Rotate the turbocharger compressor housing by loosening the V-band between the turbocharger bearing housing and the turbocharger compressor housing.

Rotate the turbocharger compressor housing to properly align with the charge air cooler piping.

Tighten the V-band clamp.

> [!tip] Момент затяжки · Torque Value
> 8.5 n•m [75 in-lb]

![[tb1csob.png]]

> [!warning] CAUTION · Осторожно
> The turbocharger speed sensor harness must be tied up and away from any heat sources and hard or sharp surfaces. Failure to do so will cause damage to the harness.

> [!warning] CAUTION · Осторожно
> Do not install cable ties directly over the sensor connector. Doing so can damage the connector. Tie the speed sensor wiring harness on either side of the connectors.

Use cable ties to secure the turbocharger compressor intake air temperature sensor harness and the turbocharger speed sensor harness away from any heat sources and hard or sharp surfaces.

![[10l00088.png]]

### Finishing Steps

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

> [!note] Note · Примечание
> If a stationary aftertreatment regeneration is needed to complete repair, bring the engine to operating temperature before starting regeneration.

- Remove the protective caps and heavy tape from the Air Handling Clean Care Kit, Part Number 4919588, or equivalent, used to cover open points in the air handling system.
- Install the turbocharger coolant hoses. Refer to Procedure 010-041 in Section 10.
- Install the turbocharger oil supply line. Refer to Procedure 010-046 in Section 10.
- Install the turbocharger oil drain line. Refer to Procedure 010-045 in Section 10.
- Connect the turbocharger actuator electrical connector.
- Connect the turbocharger speed sensor. Refer to Procedure 019-390 in Section 19.
- Connect the compressor inlet temperature sensors. Refer to Procedure 019-395 in Section 19.
- Install the aftertreatment adapter pipe, if removed. [[377-011-043 — Aftertreatment Adapter Pipe|Refer to Procedure 011-043 in Section 11.]]
- Install the turbocharger adapter and air compressor inlet tube. [[377-012-109 — Air Compressor Inlet Tube|Refer to Procedure 012-109 in Section 12.]]
- Install the discharge elbow on the charge air cooler connection piping. See equipment manufacturer service information.
- Fill the cooling system with coolant. Refer to Procedure 008-018 in Section 8.
- Connect the batteries. See equipment manufacturer service information.
- Start the engine. Verify operation of the turbocharger.
- Operate the engine until the coolant temperature reaches 82°C \[180°F\].
- Check for air, coolant, and oil leaks.

> [!note] Note · Примечание
> If a malfunction resulted in oil, excessive fuel, or excessive black smoke entering the exhaust system, the aftertreatment system **must** be inspected. Refer to Service Bulletin, Aftertreatment Diesel Oxidation Catalyst and Aftertreatment Diesel Particulate Filter Reuse Guidelines, Bulletin [[4021600 — Aftertreatment Diesel Oxidation Catalyst (DOC) and Aftertreatment Diesel Particulate|4021600]].

> [!note] Note · Примечание
> If a malfunction resulted in coolant entering the exhaust system, the aftertreatment system can be recovered. [[493-014-016 — Aftertreatment Diesel Particulate Filter (DPF) Regeneration Test|Refer to Procedure 014-016 in Section 14.]]
