---
aliases:
  - "Турбокомпрессор"
type: "Процедура"
doc: "35-010-033-tr"
title_en: "Turbocharger"
title_ru: "Турбокомпрессор"
modified: "2023-06-07"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "3666322"
figures: 59
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/35/35-010-033-tr.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/35-010-033-tr.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/35"
---

# Turbocharger
**Турбокомпрессор**

> [!abstract] Процедура · `35-010-033-tr`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[3666322 — ISM, ISMe, and QSM11 Service Manual|3666322]]
> **Секции:** Section 10 - Air Intake System - Group 10 · Section 10 - Exhaust System - Group 10 · Section 10 Air Intake System - Group 10
> **Даты:** изменён 2023-06-07
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/35/35-010-033-tr.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/35-010-033-tr.pdf)

### Initial Check

If turbocharger blade damage is suspected:

- Remove the air intake pipe from the turbocharger.
- Inspect the turbocharger compressor impeller blades for damage.
- Replace the turbocharger if damage is found.

![[10200092.png]]

If the turbocharger compressor impeller is damaged, do the following:

- Inspect the intake piping and filter element for damage.
- Repair any damaged parts before operating the engine.
- See High Blowby and Lubricating Oil Consumption Caused by Dirt and Dust Ingestion, Service Bulletin [[5613318 — Checking For Dirt and Dust Ingestion While Troubleshooting High Blowby|5613318]].

![[ci8ilca.png]]

Remove the exhaust pipe from the turbocharger.

Inspect the turbine wheel for damage.

Replace the turbocharger if damage is found.

If turbine wheel is damaged, see Prevention of Turbocharger Damage After Engine Mechanical Issue, Service Bulletin [[4326040 — Prevention of Turbocharger Damage After Engine Mechanical Issue|4326040]].

![[tb2ipsb.png]]

Lubricating oil leaks from the compressor (cold side) or turbine (hot side) seals are symptoms of air restrictions, leaks, or a restricted turbocharger oil drain line.

If a turbocharger is leaking oil, see Service Bulletin, Turbocharger Lubricating Oil Leak Troubleshooting, Bulletin 5504213.

After reviewing the service bulletin above, reference the follow troubleshooting trees, if necessary:

- Turbocharger Compressor Seal Oil Leak (T185) troubleshooting symptom tree in Section TS
- Turbocharger Turbine Seal Oil Leak (T186) troubleshooting symptom tree in Section TS.

![[10c00591.png]]

### Leak Test

Automotive with CM875, CM870 and CM570

On automotive engines with CM570, CM870, and CM875, if a bearing housing coolant leak is suspected, use the Turbocharger Coolant Leak Test Kit, Part Number 3164682.

Drain the coolant. [[35-008-018-tr — Cooling System|Refer to Procedure 008-018 in Section 8.]]

![[ra8homa.png]]

Connect a Turbocharger Coolant Leak Test Kit to the coolant inlet and outlet.

![[10c00071.png]]

Use the shop air supply to pressurize the turbocharger to 276 kPa \[40 psi\].

Shut off the air regulator.

Watch for the pressure to decrease. Pressure **must not** decrease more than 34 kPa \[5 psi\] in 1 minute.

![[10c00072.png]]

Use a spray bottle of soapy water to wet all hose connections. Bubbles will appear if the connections are leaking.

If the pressure does decrease and the hose connections are **not** leaking, replace the turbocharger.

![[10c00077.png]]

Automotive with CM876

> [!danger] WARNING · Опасно
> Do not remove the pressure cap from a hot engine. Wait until the coolant temperature is below 50°C \[120°F\] before removing the pressure cap. Heated coolant spray or steam can cause personal injury.

> [!danger] WARNING · Опасно
> Coolant is toxic. Keep away from children and pets. If not reused, dispose of in accordance with local environmental regulations.

If a turbocharger internal coolant leak is suspected, use the Turbocharger Coolant Leak Test Kit, Part Numbers 2892101, and 3164682, along with Air Pressure Regulator kit, Part Number 3164231, to check for a leak.

Drain the coolant. [[35-008-018-tr — Cooling System|Refer to Procedure 008-018 in Section 8.]]

![[ra8homa.png]]

To test for either a turbocharger bearing housing internal coolant leak or a leaking electric actuator, disconnect the coolant inlet line from the cylinder block and install the adapter fitting for the pressure regulator supplied in Turbocharger Coolant Leak Test Kit, Part Number 2892101.

![[10z00001.png]]

Install the cap included in the Turbocharger Coolant Leak Test Kit, Part Number 3164682, on the coolant outlet fitting of the turbocharger bearing housing. Hand tighten the cap.

![[10z00002.png]]

- Use shop air supply to pressurize the turbocharger and the electronic actuator to 276 kPa \[40 psi\].
- Close the air pressure regulator.
- Watch for the pressure to decrease. The pressure **must not** decrease more than 34 kPa \[5 psi\] in 1 minute.

![[10c00519.png]]

- If the pressure decreases, use a spray bottle of soapy water to wet all of the hose connections. Bubbles will appear if the connections are leaking.
- If the pressure decreases and the hose connections are **not** leaking, proceed with the next step below.
- If the pressure does **not** decrease, no leaks have been detected in either the turbocharger bearing housing or the electronic actuator. No further turbocharger coolant leak test steps are necessary.

![[10c00520.png]]

- Isolate the turbocharger bearing housing by installing the M12 banjo block-off fitting from the Turbocharger Coolant Leak Test Kit, Part Number 2892101, at the turbocharger electronic actuator coolant inlet port to block off the coolant inlet of the electric turbocharger actuator.

> [!note] Note · Примечание
> Make sure the banjo sealing washers are properly installed when installing the block-off fittings.

> [!note] Note · Примечание
> For access, the turbocharger compressor outlet connection may need to be removed.

![[10c00552.png]]

- Install the M12 banjo block-off fitting from the Turbocharger Coolant Leak Test Kit, Part Number 2892101, at the electric turbocharger actuator coolant outlet port to block off the coolant outlet of the electric turbocharger actuator.

> [!note] Note · Примечание
> Make sure the banjo sealing washers are properly installed when installing the block-off fittings.

![[10z00003.png]]

- Use shop air supply to pressurize the turbocharger bearing housing to 276 kPa \[40 psi\].
- Close the air pressure regulator.
- Watch for the pressure to decrease. The pressure **must not** decrease more than 34 kPa \[5 psi\] in 1 minute.

![[10c00519.png]]

- If the pressure decreases, use a spray bottle of soapy water to wet all of the hose connections. Bubbles will appear if the connections are leaking.
- If the pressure decreases and the hose connections are **not** leaking, replace the turbocharger bearing housing.
- If the pressure does not decrease and the hose connections are not leaking, replace the electronic turbocharger actuator.

![[10c00520.png]]

### Check for Correct Component

Compare the assembly number (1) on the turbocharger dataplate with the turbocharger specified in the engine control parts list (CPL) number (2) listed on the engine dataplate.

![[ap200na.png]]

If the correct turbocharger was **not** installed, remove it and install the correct turbocharger.

![[ap200sa.png]]

### Preparatory Steps

Automotive with CM876

> [!danger] WARNING · Опасно
> Do not remove the pressure cap from a hot engine. Wait until the coolant temperature is below 50°C \[120°F\] before removing the pressure cap. Heated coolant spray or steam can cause personal injury.

> [!danger] WARNING · Опасно
> Coolant is toxic. Keep away from children and pets. If not reused, dispose of in accordance with local environmental regulations.

> [!warning] CAUTION · Осторожно
> When the lifting eye is installed, it is to be used for lifting the turbocharger only. Lifting additional weight may cause damage to the turbocharger.

> [!warning] CAUTION · Осторожно
> When using a lifting eye, make sure the lifting eye is fully engaged in the turbocharger bearing housing and the shoulder of the lifting eye is in contact with the bearing housing.

> [!note] Note · Примечание
> Brush away any loose dirt from around the area of the air handling connections to avoid contamination of the interior of the engine.

- Disconnect the batteries. See equipment manufacturer service information.
- Drain the cooling system. [[35-008-018-tr — Cooling System|Refer to Procedure 008-018 in Section 8.]]
- Remove the exhaust connection and inlet air pipe. [[35-010-024-tr — Air Leaks, Air Intake and Exhaust Systems|Refer to Procedure 010-024 in Section 10.]] Cover open points with caps from the Cummins® Vehicle Air Plumbing Clean Care Kit, Part Number 4919425.
- Remove the discharge elbow on the charge air cooler connection. [[35-010-027-tr — Charge-Air Cooler|Refer to Procedure 010-027 in Section 10.]] Cover open points with caps from the Cummins® Vehicle Air Plumbing Clean Care Kit, Part Number 4919425.
- Disconnect the turbocharger speed sensor and compressor air inlet temperature sensors. Use the following procedure in the ISX CM871 and ISM CM876 Electronic Control System Troubleshooting and Repair Manual, Bulletin 4021560. Refer to Procedure 019-390 in Section 19.
- Disconnect the coolant supply and return lines. [[35-010-041-tr — Turbocharger Coolant Hoses|Refer to Procedure 010-041 in Section 10.]]
- Disconnect the aftertreatment injector adapter tube. [[101-011-043-tr — Aftertreatment Adapter Pipe|Refer to Procedure 011-043 in Section 11.]]
- Remove the oil supply line from the turbocharger. [[35-010-046-tr — Turbocharger Oil Supply Line|Refer to Procedure 010-046 in Section 10.]]
- Remove the oil drain line from the turbocharger. [[35-010-045-tr — Turbocharger Oil Drain Line|Refer to Procedure 010-045 in Section 10.]]

![[ck800wa.png]]

Automotive with CM875, CM870 and CM570

> [!danger] WARNING · Опасно
> Do not remove the pressure cap from a hot engine. Wait until the coolant temperature is below 50°C \[120°F\] before removing the pressure cap. Heated coolant spray or steam can cause personal injury.

> [!danger] WARNING · Опасно
> Coolant is toxic. Keep away from children and pets. If not reused, dispose of in accordance with local environmental regulations.

> [!warning] CAUTION · Осторожно
> When the lifting eye is installed, it is to be used for lifting the turbocharger only. Lifting additional weight may cause damage to the turbocharger.

> [!warning] CAUTION · Осторожно
> When using a lifting eye, make sure the lifting eye is fully engaged in the turbocharger bearing housing and the shoulder of the lifting eye is in contact with the bearing housing.

- Disconnect the batteries. See equipment manufacturer service information.
- Drain the cooling system. [[35-008-018-tr — Cooling System|Refer to Procedure 008-018 in Section 8.]]
- Remove the exhaust connection and inlet air pipe. [[35-010-024-tr — Air Leaks, Air Intake and Exhaust Systems|Refer to Procedure 010-024 in Section 10.]]
- Remove the discharge elbow on the charge air cooler connection. [[35-010-027-tr — Charge-Air Cooler|Refer to Procedure 010-027 in Section 10.]]
- Disconnect the turbocharger speed sensor and compressor air inlet temperature sensors. Refer to Procedure 019-390 in Section 19 in the Electronic Control System Troubleshooting and Repair Manual, Bulletin Number 4021560.
- Disconnect the actuator air supply line. [[35-010-118-tr — Turbocharger Actuator Air Line|Refer to Procedure 010-118 in Section 10.]]
- Disconnect the coolant supply and return lines. [[35-010-041-tr — Turbocharger Coolant Hoses|Refer to Procedure 010-041 in Section 10.]]
- Remove the oil supply line from the turbocharger. [[35-010-046-tr — Turbocharger Oil Supply Line|Refer to Procedure 010-046 in Section 10.]]
- Remove the oil drain line from the turbocharger. [[35-010-045-tr — Turbocharger Oil Drain Line|Refer to Procedure 010-045 in Section 10.]]

![[ck800wa.png]]

CM570 Engine Control Module

> [!danger] WARNING · Опасно
> Do no remove the pressure cap from a hot engine. Wait until the coolant temperature is below 50°C \[120°F\] before removing the pressure cap. Heated coolant spray or steam can cause personal injury.

> [!danger] WARNING · Опасно
> Coolant is toxic. Keep away from children and pets. If not reused, dispose of in accordance with local environmental regulations.

If a wastegate turbocharger is used, remove the wastegate actuator signal line by cutting the crimped hose clamp.

- Disconnect the batteries. See equipment manufacturer service information.
- Remove the exhaust connection and the inlet air pipes. [[35-010-024-tr — Air Leaks, Air Intake and Exhaust Systems|Refer to Procedure 010-024 in Section 10.]]
- Remove the oil supply line. [[35-010-046-tr — Turbocharger Oil Supply Line|Refer to Procedure 010-046 in Section 10.]]
- Remove the oil drain line. [[35-010-045-tr — Turbocharger Oil Drain Line|Refer to Procedure 010-045 in Section 10.]]

> [!note] Note · Примечание
> Some applications use water-cooled turbochargers.

- If a water-cooled turbocharger is used, drain the cooling system. [[35-008-018-tr — Cooling System|Refer to Procedure 008-018 in Section 8.]]
- Remove the turbocharger coolant hoses from the turbocharger. [[35-010-041-tr — Turbocharger Coolant Hoses|Refer to Procedure 010-041 in Section 10.]]
- Remove the discharge elbow from the turbocharger compressor discharge outlet. [[35-010-027-tr — Charge-Air Cooler|Refer to Procedure 010-027 in Section 10.]]

![[ck800wa.png]]

### Remove

Automotive with CM876

> [!danger] WARNING · Опасно
> This component or assembly weighs greater than 23 kg \[50 lb\]. To prevent the possibility of serious personal injury or equipment damage, be sure to have assistance or use appropriate lifting equipment to lift this component or assembly.

> [!warning] CAUTION · Осторожно
> When installing the lifting eye, make sure the shoulder of the lifting eye is bottomed against the bearing housing. Failure to do so can result in failure of the lifting eye and personal injury.

> [!warning] CAUTION · Осторожно
> If the lifting eye is installed in the turbocharger bearing housing, it is to be used exclusively for turbocharger removal and installation. It is not to be used in removal of the exhaust manifold, or engine. Doing so will cause damage the turbocharger.

> [!warning] CAUTION · Осторожно
> The turbocharger actuator must not be used as a lifting mechanism. Doing so will cause damage to the turbocharger actuator.

Thread a lifting strap around the turbocharger bearing housing. Take care **not** to bend the coolant lines when lifting the turbocharger.

Care **must** be taken **not** to damage the turbocharger compressor inlet air temperature sensor, the turbocharger speed sensor, and the turbocharger actuator coolant lines when removing the turbocharger from the engine.

Remove the nuts from the turbocharger studs and remove the turbocharger.

> [!note] Note · Примечание
> If the turbocharger mounting nuts do **not** loosen freely, split the nuts to avoid breaking a mounting stud.

Remove the turbocharger and discard the gaskets.

Cover the turbocharger exhaust inlet port with a cap from the Air Handling and Vehicle Air Plumbing Clean Care Kits, Part Numbers 4919403 and 4919425, respectively. Cover the opening on the exhaust manifold with heavy tape.

If the turbocharger is being replaced with a new turbocharger, remove the variable geometry turbocharger actuator.

[[35-010-134 — Variable Geometry Turbocharger Actuator, Electric|Refer to Procedure 010-134 in Section 10.]]

![[10c00059.png]]

Automotive with CM875, CM870 and CM570

> [!danger] WARNING · Опасно
> This component or assembly weighs greater than 23 kg \[50 lb\]. To prevent serious personal injury, be sure to have assistance or use appropriate lifting equipment to lift this component or assembly.

> [!warning] CAUTION · Осторожно
> When installing the lifting eye, make sure the shoulder of the lifting eye is bottomed against the bearing housing. Failure to do so can result in failure of the lifting eye and personal injury.

> [!warning] CAUTION · Осторожно
> If the lifting eye is installed in the turbocharger bearing housing, it is to be used exclusively for turbocharger removal and installation. It is not to be used in removal of the exhaust manifold, or engine. Doing so will cause damage the turbocharger.

> [!warning] CAUTION · Осторожно
> The turbocharger actuator must not be used as a lifting mechanism. Doing so will cause damage to the turbocharger actuator.

> [!note] Note · Примечание
> ISM CM870 and CM570 - The capscrew in the top of the turbocharger bearing housing can be removed and replaced with a lifting eye to aid in removal of the turbocharger.

Care **must** be taken **not** to damage the turbocharger compressor inlet air temperature sensor, the turbocharger speed sensor, and the turbocharger actuator coolant lines when removing the turbocharger from the engine.

Remove the four turbocharger mounting nuts from the turbocharger studs and remove the turbocharger.

> [!note] Note · Примечание
> If the turbocharger mounting nuts do **not** loosen freely, split the nuts to avoid breaking a mounting stud.

Remove the turbocharger and discard the gaskets.

![[10c00059.png]]

CM570 Engine Control Module

Remove the four turbocharger mounting nuts.

Remove the turbocharger and gasket.

![[10200074.png]]

### Disassemble

#### Turbine Housing Replacement for ISM Automotive with CM570, QSM11 with CM570 and Power Generation with CM570

- Place the turbocharger outlet on a clean, flat surface. Create an alignment mark on the turbine housing, bearing housing, and the V-band clamp. This mark will make certain the components are oriented correctly during the assembly process.

> [!note] Note · Примечание
> This procedure applies **only** to ISM Automotive with CM570, QSM11 with CM570, and Power Generation with CM570. Do **not** disassemble variable geometry turbochargers (VGT).

![[10c00223.png]]

Loosen the turbine side V-band locknut. Remove and discard the V-band clamp.

![[10c00224.png]]

> [!warning] CAUTION · Осторожно
> Turbine blades can be easily damaged and care is required for the turbine housing removal process.

Use a soft hammer to tap the turbine housing down against a soft bench surface.

As the bearing housing and compressor housing assembly loosen, gently lift the assembly out of the turbine housing.

The wastegate mounting is **not** affected by this disassembly process.

**Always** clean the turbine housing before assembly, paying particular attention to the surface close to the turbine housing and the bearing housing location.

![[10c00225.png]]

### Clean and Inspect for Reuse

> [!note] Note · Примечание
> This procedure **only** applies to Automotive with CM570, QSM11 with CM570, and Power Generation with CM570. Do **not** use these cleaning procedures on VGTs.

> [!note] Note · Примечание
> The turbocharger turbine housing surface adjacent to the turbine compressor wheels **must** be clean, smooth, and free from deposits.

#### Automotive with CM570, QSM11 with CM570, and Power Generation with CM570

- Turbocharger Turbine Housing Cleaning
- Inspect the components to detect signs of burning and other conditions in order to obtain as much information as possible before washing.

![[10c00232.png]]

> [!danger] WARNING · Опасно
> When using solvents, acids, or alkaline materials for cleaning, follow the manufacturer's recommendations for use. Wear goggles and protective clothing to reduce the possibility of personal injury.

> [!danger] WARNING · Опасно
> Some solvents are flammable and toxic. Read the manufacturers instructions before using.

Soak the turbocharger turbine housing in a non-corrosive, low flash point metal cleaner to loosen deposits.

![[10c00233.png]]

> [!danger] WARNING · Опасно
> Wear appropriate eye and face protection when using compressed air. Flying debris and dirt can cause personal injury

Scale-like deposits, if any, **must** be removed by using a non-metallic bristle brush. After removing the deposits, wash and dry the components.

Dry the components with compressed air.

![[10c00234.png]]

> [!danger] WARNING · Опасно
> Wear appropriate eye and face protection when using compressed air. Flying debris and dirt can cause personal injury

> [!note] Note · Примечание
> Do **not** bead blast aluminum and cast iron components together.

> [!note] Note · Примечание
> To prevent bead spray impinging directly on the clamp plate and turbine flange threads, mask off and plug all items.

> [!note] Note · Примечание
> Prevent the bead spray from impinging directly on the wastegate valve spindle, as beads can penetrate the spindle bore, leading to spindle seizure.

It is permissible to bead blast the turbocharger turbine housing if the chemical and brush cleanings are **not** effective.

![[10c00236.png]]

After removing the deposits, wash and dry the components.

![[10c00234.png]]

Clean the mounting nut mating surfaces of the turbocharger and the exhaust manifold with Scotch Brite™ 7448 abrasive pad.

The surface under the mounting nuts **must** be free of dirt, rust, or any other debris before applying anti-seize compound, Part Number 3824379.

Use a clean cloth to wipe around the turbocharger sealing surfaces.

> [!note] Note · Примечание
> Take care **not** to drop any dirt or debris into the turbocharger.

![[10200013.png]]

Inspect the wastegate actuator. [[35-010-050-tr — Turbocharger Wastegate Actuator|Refer to Procedure 010-050 in Section 10.]]

Inspect the turbocharger, exhaust manifold gasket surfaces, and mounting studs for cracks or other damage.

![[10200014.png]]

Inspect the turbine and compressor housings.

If cracks exist on the outer walls, the housing **must** be replaced.

A charge air cooler malfunction can cause progressive damage to the turbine housing. If the turbine housing is damaged, check the charge air cooler. [[35-010-027-tr — Charge-Air Cooler|Refer to Procedure 010-027 in Section 10.]]

![[tb2hssc.png]]

Cracks in the mounting flange longer than 15 mm \[0.6 in\] are **not** acceptable.

![[tb2hsna.png]]

Cracks of any length that reach mounting holes are **not** acceptable.

![[tb2hssb.png]]

Two cracks **must** be separated by at least 6.4 mm \[0.25 in\].

![[tb2hsnb.png]]

Cracks of any length that extend through the divider are acceptable, but **only** if they are separated by at least 12.5 mm \[0.50 in\].

![[tb8hsnd.png]]

If the engine experiences a turbocharger malfunction or any other occasion where oil or debris is put into the charge air system, the charge air system **must** be inspected and cleaned. [[35-010-027-tr — Charge-Air Cooler|Refer to Procedure 010-027 in Section 10.]] [[35-010-023-tr — Air Intake Manifold|Refer to Procedure 010-023 in Section 10.]]

![[oi100wi.png]]

Check the axial movement of the turbocharger wheels and shaft.

Use dial depth gauge, Part Number ST-537, or equivalent.

Push the rotor assembly away from the gauge.

Set the gauge to zero.

![[10c00084.png]]

Push the rotor assembly toward the gauge and record the reading.

| Turbocharger Axial Clearance |  |  |
|---|---|---|
| mm |  | in |
| 0.025 | MIN | 0.001 |
| 0.127 | MAX | 0.005 |

If the turbocharger axial clearance is **not** within specifications, the turbocharger **must** be replaced.

![[10c00085.png]]

Check the radial movement of the turbocharger wheels and shaft.

Use light finger pressure to push the compressor wheel toward the side of the compressor housing.

Repeat the procedure for the turbine wheel and housing.

Replace the turbocharger if either wheel contacts the housing.

![[10c00137.png]]

On water cooled bearing housing turbochargers, inspect the bearing housing and actuator for external oil or coolant leaks.

Check for evidence of coolant in the oil supply and oil drain fittings.

If evidence of coolant is found, see the Leak Test section of this procedure for the Turbocharger Coolant Leak Test.

![[10c00078.png]]

> [!danger] WARNING · Опасно
> When using solvents, acids, or alkaline materials for cleaning, follow the manufacturer's recommendations for use. Wear goggles and protective clothing to reduce the possibility of personal injury.

> [!warning] CAUTION · Осторожно
> Do not use caustic cleaners to clean the charge air cooler. Damage to the charge air cooler will result.

If the engine experiences a turbocharger malfunction or any other occasion where oil or debris is put into the charge air system, the charge air system **must** be inspected and cleaned.

Make sure all system level causes of oil leaks have been addressed before proceeding. Reference the following troubleshooting symptom tree:

- Turbocharger Leaks Engine Oil or Fuel (T122) troubleshooting symptom tree in Section TS.

Clean the turbocharger outlets with a non-reactive oil cleaning spray or solution, Part Number 3824421, or equivalent, and a lint-free towel.

![[10a00265.png]]

### Assemble

#### ISM Automotive with CM570, QSM11 with CM570 and Power Generation with CM570

- Install the turbine housing. Position the V-band clamp over the bearing housing and align the ink marks applied during the disassembly process.
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

Loosen the locknut 180 degrees, and tighten the locknut.

Torque value for Cummins®-branded turbochargers.

> [!tip] Момент затяжки · Torque Value
> 18 n•m [159 in-lb]

Torque value for Holset®-branded turbochargers.

> [!tip] Момент затяжки · Torque Value
> 11.3 n•m [100 in-lb]

Make certain the rotor assembly rotates freely and the compressor wheel and turbine wheel are **not** rubbing against the housing.

![[10c00224.png]]

### Install

Automotive with CM876

> [!danger] WARNING · Опасно
> This component or assembly weighs greater than 23 kg \[50 lb\]. To prevent serious personal injury, be sure to have assistance or use appropriate lifting equipment to lift this component or assembly.

> [!warning] CAUTION · Осторожно
> When installing lifting eye, make sure the shoulder of the lifting eye is bottomed against the bearing housing. Failure to do so can result in failure of lifting eye and personal injury.

> [!warning] CAUTION · Осторожно
> If the lifting eye is installed in the turbocharger bearing housing, it is to be used exclusively for turbocharger removal and installation. It is not to be used in removal of the exhaust manifold, or engine. Doing so will cause damage to the turbocharger.

> [!warning] CAUTION · Осторожно
> Do not rotate the turbocharger turbine housing. Loosening the turbine V-band and rotating the turbine housing may cause damage to an internal variable geometry mechanism.

> [!warning] CAUTION · Осторожно
> The turbocharger actuator must not be used as a lifting mechanism. Doing so will cause damage to the turbocharger actuator.

Thread a lifting strap around the turbocharger bearing housing. Take care to **not** bend the coolant lines when lifting the turbocharger.

Care **must** be taken **not** to damage the turbocharger compressor inlet air temperature sensor, the turbocharger speed sensor, and the turbocharger actuator coolant lines when installing the turbocharger.

Install a new gasket, the turbocharger, and the four mounting nuts. Tighten the mounting nuts.

> [!tip] Момент затяжки · Torque Value
> 88 n•m [65 ft-lb]

![[10200069.png]]

If installing a new turbocharger, it can be necessary to rotate the turbocharger compressor housing to properly align with the charge air cooler piping.

Rotate the turbocharger compressor housing by loosening the V-band between the turbocharger bearing housing and the turbocharger compressor housing.

Rotate the turbocharger compressor housing to properly align with the charge air cooler piping.

Tighten the V-band clamp.

> [!tip] Момент затяжки · Torque Value
> 8 n•m [71 in-lb]

![[tb1csob.png]]

If a new turbocharger is being installed, the variable geometry turbocharger actuator from the original turbocharger **must** be reused.

[[35-010-134 — Variable Geometry Turbocharger Actuator, Electric|Refer to Procedure 010-134 in Section 10.]]

If installing a new turbocharger, install the coolant inlet and outlet fittings. [[35-010-041-tr — Turbocharger Coolant Hoses|Refer to Procedure 010-041 in Section 10.]]

If installing a new turbocharger, install the oil supply fitting. [[35-010-046-tr — Turbocharger Oil Supply Line|Refer to Procedure 010-046 in Section 10.]]

> [!note] Note · Примечание
> Use a ratchet and deep well socket on these fittings.

![[10200201.png]]

Automotive with CM875, CM870 and CM570

> [!danger] WARNING · Опасно
> This component or assembly weighs greater than 23 kg \[50 lb\]. To prevent serious personal injury, be sure to have assistance or use appropriate lifting equipment to lift this component or assembly.

> [!warning] CAUTION · Осторожно
> When installing lifting eye, make sure the shoulder of the lifting eye is bottomed against the bearing housing. Failure to do so can result in failure of lifting eye and personal injury.

> [!warning] CAUTION · Осторожно
> If the lifting eye is installed in the turbocharger bearing housing, it is to be used exclusively for turbocharger removal and installation. It is not to be used in removal of the exhaust manifold, or engine. Doing so will cause damage to the turbocharger.

> [!warning] CAUTION · Осторожно
> Do not rotate the turbocharger turbine housing. Loosening the turbine V-band and rotating the turbine housing may cause damage to an internal variable geometry mechanism.

> [!warning] CAUTION · Осторожно
> The turbocharger actuator must not be used as a lifting mechanism. Doing so will cause damage to the turbocharger actuator.

> [!note] Note · Примечание
> ISM CM870 and CM570 - The capscrew in the top of the turbocharger bearing housing can be removed and replaced with a lifting eye to aid in removal of the turbocharger.

Care **must** be taken **not** to damage the turbocharger compressor inlet air temperature sensor, the turbocharger speed sensor and the turbocharger actuator coolant lines when installing the turbocharger.

Install a new gasket, the turbocharger, and the four mounting nuts. Tighten the mounting nuts.

> [!tip] Момент затяжки · Torque Value
> 88 n•m [65 ft-lb]

![[10200069.png]]

If installing a new turbocharger, it can be necessary to rotate the turbocharger compressor housing to properly align with the charge air cooler piping.

Rotate the turbocharger compressor housing by loosening the V-band between the turbocharger bearing housing and the turbocharger compressor housing.

Rotate the turbocharger compressor housing to properly align with the charge air cooler piping.

Tighten the V-band clamp.

> [!tip] Момент затяжки · Torque Value
> 8 n•m [71 in-lb]

![[tb1csob.png]]

If installing a new turbocharger, install the coolant inlet and outlet fittings. [[35-010-041-tr — Turbocharger Coolant Hoses|Refer to Procedure 010-041 in Section 10.]]

If installing a new turbocharger, install the oil supply fitting. [[35-010-046-tr — Turbocharger Oil Supply Line|Refer to Procedure 010-046 in Section 10.]]

> [!note] Note · Примечание
> Use a ratchet and deep well socket on these fittings.

![[10200201.png]]

CM570 Engine Control Module

Install the wastegate actuator. [[35-010-050-tr — Turbocharger Wastegate Actuator|Refer to Procedure 010-050 in Section 10.]]

Do **not** reuse the gasket, studs or mounting nuts. Install new studs and gasket, the turbocharger, and four new mounting nuts.

Apply a film of anti-seize compound, Part Number 3824879, or equivalent, to the turbocharger mounting studs.

![[10200069.png]]

> [!note] Note · Примечание
> Use Snap-on™ Part Number FRDHM, or equivalent crow's foot or torque wrench extension to properly tighten the mounting nut. The extension **must** be straight in line with the torque wrench to achieve proper torque.

Tighten the mounting nuts.

> [!tip] Момент затяжки · Torque Value
> 61 n•m [45 ft-lb]

![[10200029.png]]

### Finishing Steps

Automotive with CM876

> [!danger] WARNING · Опасно
> Coolant is toxic. Keep away from children and pets. If not reused, dispose of in accordance with local environmental regulations.

> [!danger] WARNING · Опасно
> Do not remove the pressure cap from a hot engine. Wait until the coolant temperature is below 50°C \[120°F\] before removing the pressure cap. Heated coolant spray or steam can cause personal injury.

- Install a new o-ring, the clamp, and the charge air cooler elbow to the turbocharger. [[35-010-027-tr — Charge-Air Cooler|Refer to Procedure 010-027 in Section 10.]]
- If the engine experiences a turbocharger malfunction or any other occasion where oil or debris is put into the charge air system, the charge air system **must** be inspected and cleaned. [[35-010-023-tr — Air Intake Manifold|Refer to Procedure 010-023 in Section 10.]] [[35-010-027-tr — Charge-Air Cooler|Refer to Procedure 010-027 in Section 10.]]
- Connect the coolant supply and return lines. [[35-010-041-tr — Turbocharger Coolant Hoses|Refer to Procedure 010-041 in Section 10.]]
- Install the oil supply line. [[35-010-046-tr — Turbocharger Oil Supply Line|Refer to Procedure 010-046 in Section 10.]]
- Install the oil drain lines. [[35-010-045-tr — Turbocharger Oil Drain Line|Refer to Procedure 010-045 in Section 10.]]
- Connect the actuator electrical connector.
- Connect the turbocharger speed sensor and compressor inlet temperature sensors. For the ISM engine, see the following procedure in the ISX CM871 and ISM CM876 Electronic Control System Troubleshooting and Repair Manual, Bulletin 4021560. Refer to Procedure 019-390 in Section 19.
- Connect the inlet air pipe to turbocharger compressor inlet and install the exhaust connection. [[35-010-024-tr — Air Leaks, Air Intake and Exhaust Systems|Refer to Procedure 010-024 in Section 10.]]
- Fill the engine with coolant. [[35-008-018-tr — Cooling System|Refer to Procedure 008-018 in Section 8.]]
- Connect the batteries. See equipment manufacturer service information.
- Start the engine. Verify operation of the turbocharger.
- Check for coolant, oil, and air leaks.

![[ck800wa.png]]

Automotive with CM875, CM870 and CM570

> [!danger] WARNING · Опасно
> Coolant is toxic. Keep away from children and pets. If not reused, dispose of in accordance with local environmental regulations.

> [!danger] WARNING · Опасно
> Do not remove the pressure cap from a hot engine. Wait until the coolant temperature is below 50°C \[120°F\] before removing the pressure cap. Heated coolant spray or steam can cause personal injury.

- Install a new o-ring, the clamp and the charge air cooler elbow to the turbocharger. [[35-010-027-tr — Charge-Air Cooler|Refer to Procedure 010-027 in Section 10.]].
- If the engine experiences a turbocharger malfunction or any other occasion where oil or debris is put into the charge air system, the charge air system **must** be inspected and cleaned. [[35-010-023-tr — Air Intake Manifold|Refer to Procedure 010-023 in Section 10.]] [[35-010-027-tr — Charge-Air Cooler|Refer to Procedure 010-027 in Section 10.]]
- Connect the coolant supply and return lines. [[35-010-041-tr — Turbocharger Coolant Hoses|Refer to Procedure 010-041 in Section 10.]]
- Install the oil supply line. [[35-010-046-tr — Turbocharger Oil Supply Line|Refer to Procedure 010-046 in Section 10.]]
- Install the oil drain lines. [[35-010-045-tr — Turbocharger Oil Drain Line|Refer to Procedure 010-045 in Section 10.]]
- Connect the air line to the actuator. [[35-010-118-tr — Turbocharger Actuator Air Line|Refer to Procedure 010-118 in Section 10.]]
- Connect the turbocharger speed sensor and compressor inlet temperature sensors. For ISM engines, see the following procedure in the ISX CM871 and ISM CM876 Electronic Control System Troubleshooting and Repair Manual, Bulletin 4021560. Refer to Procedure 019-390 in Section 19.
- Connect the inlet air pipe to turbocharger compressor inlet and install the exhaust connection. [[35-010-024-tr — Air Leaks, Air Intake and Exhaust Systems|Refer to Procedure 010-024 in Section 10.]]
- Fill the engine with coolant. [[35-008-018-tr — Cooling System|Refer to Procedure 008-018 in Section 8.]]
- Connect the batteries. See equipment manufacturer service information.
- Start the engine and verify operation of the turbocharger.
- Check for coolant, oil, and air leaks.

![[ck800wa.png]]

CM570 Engine Control Module

> [!danger] WARNING · Опасно
> Coolant is toxic. Keep away from children and pets. If not reused, dispose of in accordance with local environmental regulations.

> [!danger] WARNING · Опасно
> Do not remove the pressure cap from a hot engine. Wait until the coolant temperature is below 50°C \[120°F\] before removing the pressure cap. Heated coolant spray or steam can cause personal injury.

- Connect the wastegate. [[35-010-050-tr — Turbocharger Wastegate Actuator|Refer to Procedure 010-050 in Section 10.]]
- Install the oil supply line. [[35-010-046-tr — Turbocharger Oil Supply Line|Refer to Procedure 010-046 in Section 10.]]
- Install the oil drain line. [[35-010-045-tr — Turbocharger Oil Drain Line|Refer to Procedure 010-045 in Section 10.]]
- Connect the inlet air pipes to the turbocharger compressor inlet and install the exhaust connection. [[35-010-024-tr — Air Leaks, Air Intake and Exhaust Systems|Refer to Procedure 010-024 in Section 10.]]
- Install the new o-ring clamp and charge air cooler elbow to the turbocharger. [[35-010-027-tr — Charge-Air Cooler|Refer to Procedure 010-027 in Section 10.]]
- Connect the coolant supply and return lines. [[35-010-041-tr — Turbocharger Coolant Hoses|Refer to Procedure 010-041 in Section 10.]]
- Fill the engine with coolant. [[35-008-018-tr — Cooling System|Refer to Procedure 008-018 in Section 8.]]
- Connect the batteries. See equipment manufacturer service information.
- Operate the engine and check for leaks. **Note:** If a malfunction resulted in oil, excessive fuel, or excessive black smoke entering the exhaust system, the aftertreatment system **must** be inspected. [[4021600 — Aftertreatment Diesel Oxidation Catalyst (DOC) and Aftertreatment Diesel Particulate|Refer to the Aftertreatment Diesel Oxidation Catalyst and Aftertreatment Diesel Particulate Filter Reuse Guidelines, Bulletin 4021600.]] **Note:** If a malfunction resulted in coolant entering the exhaust system, the aftertreatment system can be recovered. [[101-014-013-tr — Aftertreatment Testing|Refer to Procedure 014-013 in Section 14.]]

![[ck800wa.png]]
