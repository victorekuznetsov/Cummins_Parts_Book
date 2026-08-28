---
aliases:
  - "Турбокомпрессор"
type: "Процедура"
doc: "10-010-033-tr"
title_en: "Turbocharger"
title_ru: "Турбокомпрессор"
modified: "2022-10-03"
engines:
  - "80141463"
  - "80248213"
families:
  - "QSX15"
manuals:
  - "3666239"
figures: 85
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/10/10-010-033-tr.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/10-010-033-tr.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSX15"
  - "группа/10"
---

# Turbocharger
**Турбокомпрессор**

> [!abstract] Процедура · `10-010-033-tr`
> **Двигатели:** [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSX15
> **Входит в руководства:** [[3666239 — Signature™, ISX, and QSX15 Service Manual|3666239]]
> **Секции:** Section 10 - Air Intake System · Section 10 - Air Intake System - Group 10 · Section 10 Air Intake System - Group 10
> **Даты:** изменён 2022-10-03
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/10/10-010-033-tr.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/10-010-033-tr.pdf)

### Initial Check

> [!note] Note · Примечание
> Brush away any loose dirt from around the area of air handling connections to avoid contamination of the interior of the engine.

Shut the engine OFF.

Allow the turbocharger to cool.

Remove the intake piping and compressor discharge piping. Cover the openings in the pipes with caps from the Air Handling and Vehicle Air Plumbing Clean Care Kits, Part Numbers 4919403 and 4919425, respectively.

Lubricating oil leaks from the compressor (cold side) or turbine (hot side) seals are symptoms of air restrictions, leaks, or a restricted turbocharger oil drain line.

See Turbocharger Lubricating Oil Leak Troubleshooting, Service Bulletin 5504213, if a turbocharger is leaking oil.

After reviewing Service Bulletin 5504213, see the following troubleshooting trees, if necessary.

- Turbocharger – Compressor Seal Oil Leak
- Turbocharger – Turbine Seal Oil Leak.

![[10c00591.png]]

Inspect the turbocharger compressor impeller blades for damage.

Replace the turbocharger if damage is found.

If the turbocharger compressor impeller is damaged, do the following:

- Inspect the intake piping and filter element for damage.
- Repair any damaged parts before operating the engine.
- See High Blowby and Lubricating Oil Consumption Caused by Dirt and Dust Ingestion, Service Bulletin [[5613318 — Checking For Dirt and Dust Ingestion While Troubleshooting High Blowby|5613318]].

![[ci8ilca.png]]

Inspect the turbine wheel for damage.

Replace the turbocharger if damage is found.

If turbine wheel is damaged, see Prevention of Turbocharger Damage After Engine Mechanical Issue, Service Bulletin [[4326040 — Prevention of Turbocharger Damage After Engine Mechanical Issue|4326040]].

![[tb1ipcd.png]]

### Leak Test

Automotive with CM870

> [!note] Note · Примечание
> This test **only** needs to be performed if troubleshooting for coolant loss or if a leak is suspected

Connect a Turbocharger Coolant Leak Test Kit, Part Number 3164682, to the coolant inlet and outlet.

Use shop air supply to pressurize the turbocharger to 276 kPa \[40 psi\].

Close the air pressure regulator.

![[10c00071.png]]

Watch for the pressure to decrease. Pressure **must not** decrease more than 34 kPa \[5 psi\] in 1 minute.

![[10c00072.png]]

If the pressure decreases more than 34 kPa \[5 psi\] in 1 minute, use a spray bottle of soapy water to wet all of the hose connections. Bubbles will appear if the connections are leaking.

If the pressure does decrease excessively, and the hose connections are **not** leaking, replace the turbocharger.

![[10c00077.png]]

Automotive With CM871

> [!danger] WARNING · Опасно
> Do not remove the pressure cap from a hot engine. Wait until the coolant temperature is below 50°C \[120°F\] before removing the pressure cap. Heated coolant spray or steam can cause personal injury.

> [!danger] WARNING · Опасно
> Coolant is toxic. Keep away from children and pets. If not reused, dispose of in accordance with local environmental regulations.

This test **only** needs to be performed if troubleshooting for coolant loss or if an internal leak is suspected.

> [!note] Note · Примечание
> The engine **must** be within 3°C or 5°F of ambient temperature to perform the test.

If a turbocharger internal coolant leak is suspected, use the Turbocharger Coolant Leak Test Kit, Part Number 5299740, along with Air Pressure Regulator Kit, Part Number 3164231, to check for a leak.

- Drain the cooling system. [[10-008-018-tr — Cooling System|Refer to Procedure 008-018 in Section 8.]]

![[ra8homa.png]]

- To test for a turbocharger bearing housing internal coolant leak, disconnect the coolant inlet line to the bearing housing and install the adapter fitting for the pressure regulator supplied with the Turbocharger Coolant Leak Test Kit, Part Number 5299740.
- To test for a turbocharger actuator internal coolant leak, disconnect the coolant inlet line to the turbocharger actuator and install the adapter fitting for the pressure regulator supplied with the Turbocharger Coolant Leak Test Kit, Part Number 5299740.

![[10r00106.png]]

- Disconnect the turbocharger coolant return line at the turbocharger outlet port and install the plug supplied with Turbocharger Coolant Leak Test Kit, Part Number 5299740, to block off the turbocharger coolant outlet port.
- Disconnect the turbocharger actuator coolant return line at the turbocharger actuator and install the plug supplied with Turbocharger Coolant Leak Test Kit, Part Number 5299740, to block off the turbocharger actuator coolant outlet port.

![[10r00107.png]]

> [!danger] WARNING · Опасно
> Wear appropriate eye and face protection when using compressed air. Flying debris and dirt can cause personal injury.

- Use compressed air supply to pressurize the turbocharger bearing housing to 276 kPa \[40 psi\].
- Close the air pressure regulator.
- Watch for the pressure to decrease. The pressure **must not** decrease more than 34 kPa \[5 psi\] in 1 minute.

![[10r00108.png]]

- If the pressure decreases, use a spray bottle of soapy water to wet the coolant leak test connections and threaded joints. Bubbles will appear if the connections or threaded joints are leaking
- If the pressure decreases and the hose connections or threaded joints are **not** leaking, replace the turbocharger **only** and reuse the actuator.
- If the pressure does **not** decrease, no leaks have been detected in the turbocharger bearing housing. Proceed to the next steps for testing the actuator for coolant leak.

![[10r00109.png]]

> [!danger] WARNING · Опасно
> Wear appropriate eye and face protection when using compressed air. Flying debris and dirt can cause personal injury.

- Use compressed air supply to pressurize the turbocharger actuator to 276 kPa \[40 psi\].
- Close the air pressure regulator.
- Watch for the pressure to decrease. The pressure **must not** decrease more than 34 kPa \[5 psi\] in 1 minute.

![[10r00110.png]]

- If the pressure decreases, use a spray bottle of soapy water to wet the coolant leak test connections and threaded joints. Bubbles will appear if the connections or threaded joints are leaking.
- If the pressure decreases and the hose connections or threaded joints are **not** leaking, replace the actuator **only** and reuse the turbocharger.
- If the pressure does **not** decrease, no leaks have been detected in the turbocharger actuator. No further Turbocharger Coolant Leak Test steps are necessary.

![[10r00111.png]]

### Preparatory Steps

#### ISX Automotive with CM570, QSX15 with CM570, and Power Generation with CM570

- Remove the wastegate actuator hose. Refer to Procedure 010-050 in Section 10.

Automotive with CM870

> [!danger] WARNING · Опасно
> Coolant is toxic. Keep away from children and pets. If not reused, dispose of in accordance with local environmental regulations.

> [!danger] WARNING · Опасно
> Do not remove the pressure cap from a hot engine. Wait until the coolant temperature is below 50°C \[120°F\] before removing the pressure cap. Heated coolant spray or steam can cause personal injury.

- Drain the coolant. [[10-008-018-tr — Cooling System|Refer to Procedure 008-018 in Section 8.]]
- Disconnect the turbocharger speed sensor. For Signature™ and ISX engines, see the following procedure in the Signature and ISX CM870 Electronic Control System Troubleshooting and Repair Manual, Bulletin 4021334. Refer to Procedure 019-390 in Section 19.
- Disconnect the turbocharger compressor air inlet temperature sensor. For ISX engines, see the following procedure in the Signature and ISX CM870 Electronic Control System Troubleshooting and Repair Manual, Bulletin 4021334. Refer to Procedure 019-395 in Section 19.
- Disconnect the variable geometry actuator air supply line. Refer to Procedure 010-113 in Section 10.
- Remove the turbocharger coolant hoses. [[10-010-041-tr — Turbocharger Coolant Hoses|Refer to Procedure 010-041 in Section 10.]]

Automotive With CM871

> [!danger] WARNING · Опасно
> Coolant is toxic. Keep away from children and pets. If not reused, dispose of in accordance with local environmental regulations.

> [!danger] WARNING · Опасно
> Do not remove the pressure cap from a hot engine. Wait until the coolant temperature is below 50°C \[120°F\] before removing the pressure cap. Heated coolant spray or steam can cause personal injury.

> [!note] Note · Примечание
> Brush away any loose dirt from around the area of the air handling connections to avoid contamination of the interior of the engine.

- Drain the coolant. [[10-008-018-tr — Cooling System|Refer to Procedure 008-018 in Section 8.]]
- Disconnect the turbocharger speed sensor. For ISX and ISM engines, see the following procedure in the ISX CM871 and ISM CM876 Electronic Control System, Troubleshooting and Repair Manual, Bulletin 4021560. Refer to Procedure 019-390 in Section 19.
- Disconnect the turbocharger compressor air inlet temperature sensor. For ISX and ISM engines, see the following procedure in the ISX CM871 and ISM CM876 Electronic Control System, Troubleshooting and Repair Manual, Bulletin 4021560. Refer to Procedure 019-395 in Section 19.
- Remove the turbocharger coolant hoses. [[10-010-041-tr — Turbocharger Coolant Hoses|Refer to Procedure 010-041 in Section 10.]]
- Remove the charge air piping. Use protective caps from the Air Handling Clean Care Kit, Part Number 4919403, to cover open points.
- Remove the turbocharger air inlet piping. Use protective caps from the Air Handling and Vehicle Air Plumbing Clean Care Kits, Part Numbers 4919403 and 4919425 respectively, to cover open points.
- Disconnect the aftertreatment adapter pipe. Use a protective cap from the Air Handling Clean Care Kit, Part Numbers 4919403 and 4919425 respectively, to cover the turbocharger exhaust outlet. [[101-011-043-tr — Aftertreatment Adapter Pipe|Refer to Procedure 011-043 in Section 11.]]

### Remove

> [!danger] WARNING · Опасно
> This component or assembly weighs greater than 23 kg \[50 lb\]. To prevent serious personal injury, be sure to have assistance or use appropriate lifting equipment to lift this component or assembly.

#### Automotive, Industrial, and Power Generation with CM570

- Remove the oil supply, oil drain tube, and brace, if equipped, from the turbocharger.

![[17c00120.png]]

Remove the intake and exhaust pipes from the turbocharger.

Remove the charge air cooler piping from the discharge elbow.

![[17c00121.png]]

Remove the clamp, o-ring, and discharge elbow from the turbocharger.

Discard the o-ring.

![[17c00124.png]]

> [!note] Note · Примечание
> In some applications, the turbocharger will **not** clear the lubricating oil cooler assembly during removal and installation. It will, perhaps, be necessary to remove the exhaust manifold and turbocharger together, and then separate the two components. Use the following procedure if the two components **must** be removed together for the removal and installation of the exhaust manifold. Refer to Procedure 011-007 in Section 11.

If the turbocharger mounting nuts do **not** loosen freely, split the nuts to avoid breaking a mounting stud.

Remove the four turbocharger mounting nuts.

Remove the turbocharger and discard the gasket.

![[17c00122.png]]

Automotive with CM870

> [!danger] WARNING · Опасно
> This component or assembly weighs greater than 23 kg \[50 lb\]. To prevent serious personal injury, be sure to have assistance or use appropriate lifting equipment to lift this component or assembly.

> [!warning] CAUTION · Осторожно
> When installing a lifting eye, be sure the shoulder of the lifting eye is bottomed against the bearing housing. Failure to do so can result in failure of the lifting eye and personal injury.

> [!warning] CAUTION · Осторожно
> If the lifting eye is installed in the turbocharger bearing housing, it is to be used exclusively for turbocharger removal and installation. It is not to be used in removal of the exhaust manifold, or engine. Doing so will cause damage to the turbocharger.

Remove the oil supply and the oil drain tube from the turbocharger.

![[10c00136.png]]

Remove the intake and the exhaust pipes from the turbocharger.

Remove the charge air cooler piping from the discharge elbow.

![[10c00201.png]]

Remove the clamp, o-ring, and discharge elbow from the turbocharger.

Discard the o-ring.

![[17c00124.png]]

The capscrew in the top of the turbocharger bearing housing can be removed and replaced with a lifting eye to aid in removal of the turbocharger.

If the turbocharger mounting nuts do **not** loosen freely, split the nuts to avoid breaking a mounting stud.

Remove the four turbocharger mounting nuts.

Remove the turbocharger and discard the gasket.

![[10c00059.png]]

Automotive With CM871

> [!danger] WARNING · Опасно
> This component or assembly weighs greater than 23 kg \[50 lb\]. To prevent serious personal injury, be sure to have assistance or use appropriate lifting equipment to lift this component or assembly.

Remove the turbocharger oil supply line from the male union on the turbocharger bearing housing.

Remove the turbocharger oil supply line from the lubricating oil filter head.

![[10c00374.png]]

Remove the turbocharger oil drain line from the turbocharger and discard the gasket.

Pull the turbocharger oil drain line from the cylinder block by hand.

If the grommet seal is attached to the drain tube, remove and inspect the grommet. Replace the grommet if damaged.

Install the grommet into the cylinder block if no damage is found.

![[07600300.png]]

Thread a lifting strap around the turbocharger bearing housing. Take care **not** to bend the coolant lines when lifting the turbocharger.

Care **must** be taken **not** to damage the turbocharger compressor inlet air temperature sensor, the turbocharger speed sensor, and the turbocharger actuator coolant lines when removing the turbocharger.

Remove the four turbocharger mounting nuts.

> [!note] Note · Примечание
> If the turbocharger mounting nuts do **not** loosen freely, split the nuts to avoid breaking a mounting stud.

Remove the turbocharger and discard the gaskets.

![[10c00247.png]]

Cover the turbocharger exhaust inlet port with heavy tape or a protective cap from the Air Handling and the Vehicle Air Plumbing Clean Care Kit, Part Numbers 4919403 and 4919425, respectively. Cover the opening on the exhaust manifold with heavy tape.

If the turbocharger is being replaced with a new turbocharger, remove the variable geometry turbocharger (VGT) actuator. [[10-010-134 — Variable Geometry Turbocharger Actuator, Electric|Refer to Procedure 010-134 in Section 10.]]

![[10c00308.png]]

### Disassemble

#### Turbine Housing Replacement for ISX Automotive with CM570, QSX15 with CM570, and Power Generation with CM570

- Place the turbocharger outlet on a clean flat surface. Create an alignment mark on the turbine housing, bearing housing and the V-band clamp. This mark will make certain the components are oriented correctly during the assembly process.

> [!note] Note · Примечание
> This procedure applies **only** to Automotive with CM570, QSX15 with CM570, and Power Generation with CM570. Do **not** disassemble VGT.

![[10c00223.png]]

Loosen the turbine side V-band locknut. Remove and discard the V-band clamp.

![[10c00224.png]]

> [!warning] CAUTION · Осторожно
> Turbine blades can be easily damaged and care is required for the turbine housing removal process.

Use a soft hammer to tap the turbine housing down against a soft bench surface.

As the bearing housing and compressor housing assembly loosen, gently lift the assembly out of the turbine housing.

Wastegate mounting is **not** affected by this disassembly process.

**Always** clean the turbine housing before assembly, paying particular attention to the surface close to the turbine housing and the bearing housing location.

![[10c00225.png]]

### Clean and Inspect for Reuse

#### Turbine Housing Cleaning for ISX Automotive with CM570, QSX15 with CM570, and Power Generation with CM570

- The turbocharger turbine housing surface adjacent to the turbine compressor wheels **must** be clean, smooth, and free from deposits.
- Inspect the components to detect signs of burning and other conditions in order to obtain as much information as possible before washing.

> [!note] Note · Примечание
> This procedure applies **only** to Automotive with CM570, QSX15 with CM570, and Power Generation with CM570. Do **not** disassemble VGTs.

![[10c00232.png]]

> [!warning] CAUTION · Осторожно
> Wear appropriate eye and face protection when using non-corrosive metal cleaner.

Soak the turbocharger turbine housing in a non-corrosive, low flash point metal cleaner to loosen deposits.

![[10c00233.png]]

> [!warning] CAUTION · Осторожно
> Wear appropriate eye and face protection when using compressed air. Flying debris and dirt can cause personal injury.

Scale-like deposits, if any, **must** be removed by using a non-metallic bristle brush. After removing the deposits, wash and dry the components.

Dry the components with compressed air.

![[10c00234.png]]

> [!warning] CAUTION · Осторожно
> Wear appropriate eye and face protection when using compressed air. Flying debris and dirt can cause personal injury.

> [!note] Note · Примечание
> Do **not** bead blast aluminum and cast iron components together.

> [!note] Note · Примечание
> To prevent bead spray impinging directly on the clamp plate and turbine flange threads, mask and plug off all items.

> [!note] Note · Примечание
> Prevent the bead spray impinging directly on the wastegate valve spindle, as beads can penetrate the spindle bore and lead to spindle seizure.

It is permissible to bead blast the turbocharger turbine housing if chemical and brush cleaning are **not** effective.

![[10c00236.png]]

After removing the deposits, wash and dry the components.

![[10c00234.png]]

#### ISX Automotive with CM570, QSX15 with CM570 and Power Generation with CM570

- Clean the retaining nut mating surfaces of the turbocharger and the exhaust manifold.
- Clean the mating surfaces with Scotch-Brite™ 7448 abrasive pad.
- The surface under the mounting nuts **must** be free of dirt, rust, or any other debris, before applying anti-seize compound, Part Number 3823097.

![[10200013.png]]

Inspect the wastegate actuator. Refer to Procedure 010-050 in Section 10.

Inspect the turbocharger casings.

Replace the housing if through cracks are found in the outer walls.

![[tb1hssc.png]]

Cracking in the turbine housing inlet flange and the inlet duct generally requires replacement of the turbine housing. Acceptance and rejection guidelines are shown in these illustrations. If an exhaust gasket is available, **always** make certain that cracks do **not** exist within the sealing area.

Check the turbine housing inlet flange flatness. It **must** be within 0.1 mm \[0.004 in\] to be acceptable for reuse.

![[10c00226.png]]

Flange Fasteners - Clearance Holes

Check the fastener hole diameter. It **must not** be more than 1.5 mm \[0.006 in\] larger than the maximum thread diameter of the fastener.

![[10c00227.png]]

> [!warning] CAUTION · Осторожно
> If external cracks are found on the turbine housing, the turbine housing must be replaced.

> [!warning] CAUTION · Осторожно
> Turbine blades can be easily damaged and care is required for the turbine housing installation process.

Cracking of the internal wall at the entry to the turbine wheel (tongue) is acceptable as a service condition, and the turbine housing can be re-used.

![[10c00228.png]]

Inspect the turbocharger compressor V-band outlet and the discharge elbow V-band connection for dents or fretting.

Replace the turbocharger or discharge elbow, if damaged, to prevent compressed air leaks.

![[tb1crmb.png]]

Check the axial movement of the turbocharger wheels and shaft.

Use dial depth gauge, Part Number ST-537, or equivalent.

Push the rotor assembly away from the gauge.

Set the gauge to zero (0).

![[10c00084.png]]

Push the rotor assembly toward the gauge and record the reading.

| Turbocharger Axial Clearance |  |  |
|---|---|---|
| mm |  | in |
| 0.025 | MIN | 0.001 |
| 0.127 | MAX | 0.005 |

If the turbocharger axial clearance is **not** within specifications, the turbocharger **must** be replaced.

![[10c00085.png]]

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

Make sure all system level causes of oil leaks have been addressed using the Compressor Side Oil Leak troubleshooting symptom tree.

Clean turbocharger outlets with a non-reactive oil cleaning spray or solution and a lint-free towel.

![[10a00265.png]]

If the engine experiences a turbocharger malfunction or any other occasion where oil or debris is put into the charge air system, the charge air system **must** be inspected and cleaned. Refer to Procedure 010-027 in Section 10.

![[oi100wi.png]]

Automotive with CM870

Inspect for cracks in the turbocharger and compressor casings.

Replace the turbocharger if through cracks in the outer walls are found.

Inspect for cracks on the turbine inlet and exhaust mounting flanges. Replace the turbocharger if any cracks are found.

![[10c00060.png]]

Clean the retaining nut mating surfaces of the turbocharger and the exhaust manifold.

Clean the mating surfaces with Scotch-Brite™ 7448 abrasive pad.

The surface under the mounting nuts **must** be free of dirt, rust, or any other debris before applying anti-seize compound, Part Number 3823097.

![[10200013.png]]

Inspect the turbocharger compressor V-band outlet and the discharge elbow V-band connection for dents or fretting.

Replace the turbocharger or discharge elbow, if damaged, to prevent compressed air leaks.

Inspect the compressor wheel for signs of rubbing against the compressor cover. Replace the turbocharger if rubbing evidence is seen.

Use light finger pressure to push the compressor wheel. If the compressor wheel contacts the cover, replace the turbocharger.

If the engine experiences a turbocharger malfunction or any other occasion where oil or debris is put into the charge air system, the charge air system **must** be inspected and cleaned. Refer to Procedure 010-027 in Section 10.

![[tb1crmb.png]]

Check the axial movement of the turbocharger wheels and shaft.

Use dial depth gauge, Part Number ST-537, or equivalent.

Push the rotor assembly away from the gauge.

Set the gauge to zero (0).

![[10c00084.png]]

Push the rotor assembly toward the gauge and record the reading.

| Turbocharger Axial Clearance |  |  |
|---|---|---|
| mm |  | in |
| 0.025 | MIN | 0.001 |
| 0.127 | MAX | 0.005 |

If the turbocharger axial clearance is **not** within specifications, the turbocharger **must** be replaced.

![[10c00085.png]]

Inspect the compressor wheel for signs of rubbing against the compressor cover.

Replace the turbocharger if rubbing evidence is seen.

Check the radial movement of the turbocharger wheels and shaft.

Use light finger pressure to push the compressor wheel toward the side of the compressor housing.

Repeat the procedure for the turbine wheel and housing.

Replace the turbocharger if either wheel contacts the housing.

![[10c00137.png]]

Automotive With CM871

Inspect the variable geometry actuator and mechanism for proper operation. [[10-010-134 — Variable Geometry Turbocharger Actuator, Electric|Refer to Procedure 010-134 in Section 10.]]

![[10c00177.png]]

Inspect for cracks in the turbocharger and compressor casings.

Replace the turbocharger if through cracks in the outer walls are found.

Inspect for cracks on the turbine inlet and exhaust mounting flanges. Replace the turbocharger if any cracks are found.

![[10c00387.png]]

> [!note] Note · Примечание
> All openings on the turbocharger, including the turbine inlet connection, **must** be plugged with caps from the Air Handling and Vehicle Air Plumbing Clean Care Kits, Part Numbers 4919403, and 4919425 respectively, during flange cleaning.

Clean the turbocharger and exhaust manifold where the retaining nut contacts the turbocharger and exhaust manifold.

Clean the mating surfaces with Scotch-Brite™ 7448 abrasive pad.

After abrasive cleaning, wipe debris from both surfaces with a clean shop towel.

The surface under the mounting nuts **must** be free of dirt, rust, or any other debris, before applying anti-seize compound, Part Number 3823097.

![[10200013.png]]

Check for evidence of coolant in the oil supply and oil drain fittings. Reference Coolant in the Lubricating Oil troubleshooting symptom tree if coolant is found.

![[10c00388.png]]

Inspect the turbocharger compressor V-band outlet and the discharge elbow V-band connection for dents or fretting.

Replace the turbocharger or discharge elbow, if damaged, to prevent compressed air leaks.

Inspect the compressor wheel for signs of rubbing against the compressor cover. Replace the turbocharger if rubbing evidence is seen.

Use light finger pressure to push the compressor wheel. If the compressor wheel contacts the cover, replace the turbocharger.

If the engine experiences a turbocharger malfunction or any other occasion where oil or debris is put into the charge air system, the charge air system **must** be inspected and cleaned. Refer to Procedure 010-027 in Section 10.

![[tb1crmb.png]]

Check the axial movement of the turbocharger wheels and shaft.

Use dial depth gauge, Part Number ST-537, or equivalent.

Push the rotor assembly away from the gauge.

Set the gauge to zero (0).

![[10c00084.png]]

Push the rotor assembly toward the gauge and record the reading

| Turbocharger Axial Clearance |  |  |
|---|---|---|
| mm |  | in |
| 0.025 | MIN | 0.001 |
| 0.127 | MAX | 0.005 |

If the turbocharger axial clearance is **not** within specifications, the turbocharger **must** be replaced.

![[10c00085.png]]

Inspect the compressor wheel for signs of rubbing against the compressor cover.

Replace the turbocharger if rubbing evidence is seen.

Check the radial movement of the turbocharger wheels and shaft.

Use light finger pressure to push the compressor wheel toward the side of the compressor housing.

Repeat the procedure for the turbine wheel and housing.

Replace the turbocharger if either wheel contacts the housing.

![[10c00137.png]]

### Assemble

#### ISX Automotive with CM570, QSX15 with CM570 and Power Generation with CM570

- To install the turbine housing, position the V-band clamp over the bearing housing and align the ink marks applied during the disassembly process.
- Apply anti-seize compound to the bearing housing locating bore of the turbine housing.
- Carefully slide the bearing and compressor housing assembly into the turbine housing. Use the ink alignment mark to locate the turbine housing assembly in the correct orientation with the turbine housing.

![[10c00225.png]]

Place the new V-band clamp in the correct orientation and tighten the locknut.

Torque value for Cummins®-branded turbochargers.

> [!tip] Момент затяжки · Torque Value
> 18 n•m [159 in-lb]

Torque value for Holset®-branded turbochargers.

> [!tip] Момент затяжки · Torque Value
> 11.3 n•m [100 in-lb]

Loosen the locknut 180 degrees, and tighten the locknut again.

Torque value for Cummins®-branded turbochargers.

> [!tip] Момент затяжки · Torque Value
> 18 n•m [159 in-lb]

Torque value for Holset®-branded turbochargers.

> [!tip] Момент затяжки · Torque Value
> 11.3 n•m [100 in-lb]

Make certain the rotor assembly rotates freely and neither the compressor wheel nor the turbine wheel is rubbing against the housing.

![[10c00224.png]]

### Install

#### ISX Automotive with CM570, QSX15 with CM570, and Power Generation with CM570

- Apply a film of high-temperature anti-seize compound, Part Number 3823097, or equivalent, to the turbocharger mounting studs.

![[tb1hshc.png]]

> [!danger] WARNING · Опасно
> This component or assembly weighs greater than 23 kg \[50 lb\]. To prevent serious personal injury, be sure to have assistance or use appropriate lifting equipment to lift this component or assembly.

> [!note] Note · Примечание
> If the exhaust manifold and turbocharger were removed together in order for the turbocharger to clear the lubricating oil cooler assembly, see the following procedure for installation of the exhaust manifold. Refer to Procedure 011-007 in Section 11.

Install a new mounting gasket, the turbocharger, and the four mounting nuts.

Tighten the mounting nuts.

Torque value for the standard nut:

> [!tip] Момент затяжки · Torque Value
> 61 n•m [45 ft-lb]

Torque value for the Spiralock™ nut (identified by "SPL" on the nut flange):

> [!tip] Момент затяжки · Torque Value
> 81 n•m [60 ft-lb]

![[17c00122.png]]

If installing a new turbocharger, it can be necessary to rotate the turbocharger compressor housing to properly align with the charge air cooler piping.

Rotate the turbocharger compressor housing by loosening the V-band between the turbocharger bearing housing and the turbocharger compressor housing.

Rotate the turbocharger compressor housing to properly align with the charge air cooler piping.

Tighten the V-band clamp.

> [!tip] Момент затяжки · Torque Value
> 8 n•m [71 in-lb]

![[tb1csob.png]]

Install the discharge elbow and clamp onto the charge air cooler pipe connection.

Do **not** tighten the clamp until the elbow is installed on the turbocharger.

![[tb1tbhc.png]]

If a new turbocharger is being installed, the variable geometry turbocharger actuator from the original turbocharger **must** be reused.

[[10-010-134 — Variable Geometry Turbocharger Actuator, Electric|Refer to Procedure 010-134 in Section 10.]]

Install a new o-ring, clamp, and discharge elbow to the turbocharger.

Tighten the clamp.

> [!tip] Момент затяжки · Torque Value
> 9 n•m [80 in-lb]

![[10c00083.png]]

Install a new gasket, oil drain tube, and capscrews.

Tighten the capscrews.

> [!tip] Момент затяжки · Torque Value
> 25 n•m [221 in-lb]

![[17c00125.png]]

Install the turbocharger anti-rotation brace, if equipped. The end rests on the oil cooler housing.

This brace requires longer, 1.25 mm \[0.049 in\], capscrews.

Tighten the capscrews.

> [!tip] Момент затяжки · Torque Value
> 25 n•m [221 in-lb]

![[10c00160.png]]

Pour approximately 50 to 60 cc \[1.7 to 2 oz\] of clean engine oil into the turbocharger oil supply opening.

![[17c00126.png]]

> [!warning] CAUTION · Осторожно
> Proper routing of the turbocharger oil supply tube is critical to prevent failure. Avoid any tube-to-metal contact. (The inlet supply fitting must be oriented slightly off vertical to allow proper alignment.)

If installing a new turbocharger, make sure the turbocharger is aligned, loosen the compressor and turbine V-bands, and adjust as needed. Tighten the V-bands.

> [!tip] Момент затяжки · Torque Value
> 9 n•m [80 in-lb]

> [!tip] Момент затяжки · Torque Value
> 12 n•m [106 in-lb]

If installing a new turbocharger, install the male union elbow.

> [!tip] Момент затяжки · Torque Value
> 30 n•m [22 ft-lb]

Install the turbocharger oil supply tube on the elbow.

> [!tip] Момент затяжки · Torque Value
> 30 n•m [22 ft-lb]

![[17c00127.png]]

Install the intake and exhaust pipes to the turbocharger. Tighten the clamp.

> [!tip] Момент затяжки · Torque Value
> 9 n•m [80 in-lb]

![[17c00128.png]]

Automotive with CM870

#### Variable Geometry

- Apply a film of high-temperature anti-seize compound, Part Number 3823097, to the turbocharger mounting studs.

![[tb1hshc.png]]

> [!danger] WARNING · Опасно
> This component or assembly weighs greater than 23 kg \[50 lb\]. To prevent serious personal injury, be sure to have assistance or use appropriate lifting equipment to lift this component or assembly.

> [!warning] CAUTION · Осторожно
> When installing a lifting eye, be sure the shoulder of the lifting eye is bottomed against bearing housing. Failure to do so can result in failure of the lifting eye and personal injury.

> [!warning] CAUTION · Осторожно
> If a lifting eye is installed in turbocharger bearing housing, it is to be used exclusively for turbocharger removal and installation. It is not to be used in the removal of the exhaust manifold or engine. Doing so will cause damage to the turbocharger.

> [!warning] CAUTION · Осторожно
> Do not rotate the turbocharger turbine housing. Loosening the turbine V-band and rotating the turbine housing can cause damage to the internal variable geometry mechanism.

The capscrew in the top of the turbocharger bearing housing can be removed and replaced with a lifting eye to aid in the installation of the turbocharger.

Install a new gasket, the turbocharger, and the four mounting nuts. Tighten the mounting nuts.

> [!tip] Момент затяжки · Torque Value
> 102 n•m [75 ft-lb]

![[17c00122.png]]

If installing a new turbocharger, it can be necessary to rotate the turbocharger compressor housing to properly align with the charge air cooler piping.

Rotate the turbocharger compressor housing by loosening the V-band between the turbocharger bearing housing and the turbocharger compressor housing.

Rotate the turbocharger compressor housing to properly align with the charge air cooler piping.

Tighten the V-band clamp.

> [!tip] Момент затяжки · Torque Value
> 8 n•m [71 in-lb]

![[tb1csob.png]]

Install the discharge elbow and clamp onto the charge air cooler pipe connection.

Do **not** tighten the clamp until the elbow is installed on the turbocharger.

![[tb1tbhc.png]]

Install a new o-ring, clamp, and discharge elbow to the turbocharger.

Tighten the clamp.

> [!tip] Момент затяжки · Torque Value
> 9 n•m [80 in-lb]

![[10c00083.png]]

Install a new gasket, oil drain tube, and capscrews.

Tighten the capscrews.

> [!tip] Момент затяжки · Torque Value
> 30 n•m [22 ft-lb]

![[10c00136.png]]

Install the intake and exhaust pipes to the turbocharger, and tighten the clamps.

> [!tip] Момент затяжки · Torque Value
> 9 n•m [80 in-lb]

![[17c00128.png]]

Automotive With CM871

Apply a film of high-temperature anti-seize compound, Part Number 3823097, or equivalent, to the turbocharger mounting studs and to the flange area on the retaining nuts. Properly applying anti-seize compound will reduce the possibility of the nuts loosening over time.

![[tb1hshc.png]]

If installing a new turbocharger, install the coolant and oil fittings into the bearing housing.

> [!note] Note · Примечание
> Use a ratchet and deep well socket to install these fittings.

> [!tip] Момент затяжки · Torque Value
> 30 n•m [22 ft-lb]

> [!warning] CAUTION · Осторожно
> Proper routing of the turbocharger oil supply tube is critical to prevent failure. Avoid any tube-to-metal contact.

Install the turbocharger oil supply hose onto the oil supply fitting. The oil supply hose **must** point directly downward in order for it to properly connect to the oil supply fitting on the lubricating oil filter head.

> [!tip] Момент затяжки · Torque Value
> 30 n•m [22 ft-lb]

Install the turbocharger actuator coolant supply and return fittings into the electronic actuator. [[10-010-041-tr — Turbocharger Coolant Hoses|Refer to Procedure 010-041 in Section 10.]]

![[10c00222.png]]

> [!danger] WARNING · Опасно
> This component or assembly weighs greater than 23 kg \[50 lb\]. To prevent serious personal injury, be sure to have assistance or use appropriate lifting equipment to lift this component or assembly.

> [!warning] CAUTION · Осторожно
> Do not rotate the turbocharger turbine housing. Loosening the turbine V-band and rotating the turbine housing can cause damage to the internal variable geometry mechanism.

> [!note] Note · Примечание
> Thread a lifting strap around the turbocharger bearing housing. Take care **not** to bend the coolant lines when lifting the turbocharger.

> [!note] Note · Примечание
> All four mounting studs have to be the same material for proper clamping force.

Care **must** be taken **not** to damage the turbocharger compressor inlet air temperature sensor, the turbocharger speed sensor, and the turbocharger actuator coolant lines when installing the turbocharger.

Install a new gasket, the turbocharger, and the four mounting nuts. Tighten the mounting nuts.

> [!tip] Момент затяжки · Torque Value
> Stainless Steel 102 n•m [75 ft-lb]

![[10c00247.png]]

If installing a new turbocharger, it can be necessary to rotate the turbocharger compressor housing to properly align with the charge air cooler piping.

Rotate the turbocharger compressor housing by loosening the V-band between the turbocharger bearing housing and the turbocharger compressor housing.

Rotate the turbocharger compressor housing to properly align with the charge air cooler piping.

Tighten the V-band clamp.

> [!tip] Момент затяжки · Torque Value
> 8 n•m [71 in-lb]

![[tb1csob.png]]

Use the torque plus angle method:

> [!tip] Момент затяжки · Torque Value
> INCONEL® with Inscribed “I“ 61 n•m [45 ft-lb]

Rotate 60 degrees.

If the compressor housing **must** be rotated, loosen the compressor V-band clamp enough to allow the compressor housing to rotate.

Rotate the compressor housing to the proper orientation.

Tighten the compressor housing V-band clamp.

> [!tip] Момент затяжки · Torque Value
> 8.5 n•m [75 in-lb]

![[10a00246.png]]

Install a new o-ring seal, clamp, and discharge elbow to the turbocharger.

Tighten the clamps.

> [!tip] Момент затяжки · Torque Value
> 9 n•m [80 in-lb]

![[10c00083.png]]

Insert the bottom of the drain tube into the grommet seal that is pressed into the cylinder block.

Install a new gasket, oil drain tube, and capscrews.

Tighten the capscrews.

> [!tip] Момент затяжки · Torque Value
> 25 n•m [221 in-lb]

![[10c00372.png]]

Connect the oil supply hose to the oil supply fitting located on the lubricating oil filter head.

Tighten the oil supply hose.

> [!tip] Момент затяжки · Torque Value
> 30 n•m [22 ft-lb]

Install the turbocharger oil supply line onto the turbocharger bearing housing male union.

> [!tip] Момент затяжки · Torque Value
> 30 n•m [22 ft-lb]

![[10c00374.png]]

### Finishing Steps

#### ISX Automotive with CM570, QSX15 with CM570, and Power Generation with CM570

- Install the wastegate actuator hose. Refer to Procedure 010-050 in Section 10.
- Start and operate the engine until the coolant temperature reaches 82°C \[180°F\]. Check for air, coolant, and oil leaks.

Automotive with CM870

> [!warning] CAUTION · Осторожно
> Turbocharger speed sensor harness and turbocharger compressor inlet air temperature sensor harnesses must be tied securely and away from heat sources, such as the exhaust manifold and exhaust pressure sensor tube. Failure to do so can cause damage to the sensor harness.

> [!warning] CAUTION · Осторожно
> The turbocharger compressor inlet air temperature sensor must be positioned so the sensor body is pointing up and away from the exhaust manifold. Failure to do so can cause sensor damage.

> [!warning] CAUTION · Осторожно
> Do not twist coolant lines while tightening. Failure to do so will damage coolant lines.

- Install the turbocharger coolant hoses. [[10-010-041-tr — Turbocharger Coolant Hoses|Refer to Procedure 010-041 in Section 10.]]
- Connect the variable geometry actuator air supply line. Refer to Procedure 010-113 in Section 10.
- Connect the electrical connectors on the turbocharger speed sensor and the turbocharger compressor air inlet temperature sensor. For ISX engines, see the following procedure in the Signature and ISX CM870 Electronic Control System Troubleshooting and Repair Manual, Bulletin 4021334. Refer to Procedure 019-395 in Section 19. Also, see the following procedure in the Signature and ISX CM870 Electronic Control System Troubleshooting and Repair Manual, Bulletin 4021334. Refer to Procedure 019-390 in Section 19.
- Fill the cooling system with coolant. [[10-008-018-tr — Cooling System|Refer to Procedure 008-018 in Section 8.]]
- Start and operate the engine until the coolant temperature reaches 82°C \[180°F. Check for air, coolant, and oil leaks.

Automotive With CM871

- Install the charge air piping. Refer to Procedure 010-027 in Section 10.
- Install the aftertreatment adapter pipe. [[101-011-043-tr — Aftertreatment Adapter Pipe|Refer to Procedure 011-043 in Section 11.]]
- Install the turbocharger coolant hoses. [[10-010-041-tr — Turbocharger Coolant Hoses|Refer to Procedure 010-041 in Section 10.]]
- Connect the turbocharger compressor air inlet temperature sensor. For the ISX and ISM engines, see the following procedure in the ISX CM871 and ISM CM876 Electronic Control System, Troubleshooting and Repair Manual, Bulletin 4021560. Refer to Procedure 019-395 in Section 19.
- Connect the electrical connector on the turbocharger speed sensor, turbocharger electric actuator, and the turbocharger compressor air inlet temperature sensor. For the ISX and ISM engines, see the following procedure in Section 19 in the ISX CM871 and ISM CM876 Electronic Control System, Troubleshooting and Repair Manual, Bulletin 4021560. Refer to Procedure 019-390 in Section 19.
- Connect the aftertreatment adapter pipe. [[101-011-043-tr — Aftertreatment Adapter Pipe|Refer to Procedure 011-043 in Section 11.]]
- Fill the cooling system. [[10-008-018-tr — Cooling System|Refer to Procedure 008-018 in Section 8.]]
- Operate the engine. Check for leaks.

> [!note] Note · Примечание
> If a malfunction resulted in oil, excessive fuel, or excessive black smoke entering the exhaust system, the aftertreatment system **must** be inspected. [[4021600 — Aftertreatment Diesel Oxidation Catalyst (DOC) and Aftertreatment Diesel Particulate|Refer to the Aftertreatment Diesel Oxidation Catalyst and Aftertreatment Diesel Particulate Filter Reuse Guidelines, Bulletin 4021600.]]

> [!note] Note · Примечание
> If a malfunction resulted in coolant entering the exhaust system, the aftertreatment system can be recovered. [[101-014-013-tr — Aftertreatment Testing|Refer to Procedure 014-013 in Section 14.]]
