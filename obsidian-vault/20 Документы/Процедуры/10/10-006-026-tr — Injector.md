---
aliases:
  - "Форсунка"
type: "Процедура"
doc: "10-006-026-tr"
title_en: "Injector"
title_ru: "Форсунка"
modified: "2014-11-07"
engines:
  - "80141463"
  - "80248213"
families:
  - "QSX15"
manuals:
  - "3666239"
figures: 51
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/10/10-006-026-tr.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/10-006-026-tr.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSX15"
  - "группа/10"
---

# Injector
**Форсунка**

> [!abstract] Процедура · `10-006-026-tr`
> **Двигатели:** [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSX15
> **Входит в руководства:** [[3666239 — Signature™, ISX, and QSX15 Service Manual|3666239]]
> **Секции:** Section 06 - Injectors and Fuel Lines · Section 6 - Injector and Fuel Lines - Group 06 · Section 6 - Injectors and Fuel Lines · Section 6 - Injectors and Fuel Lines - Group 06
> **Даты:** изменён 2014-11-07
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/10/10-006-026-tr.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/10-006-026-tr.pdf)

### Leak Test

This test checks for combustion gas leaks back through the injector rail check valve or other conditions that will allow gas leakage through the injector into the fuel rail.

When the engine is barred over, backpressure is created against the injector by the piston coming up on the compression stroke.

During the test, if the rail check valve is leaking, air is pushed through the rail check valve and into the fuel rail. Pressure is sensed at the test fixture, which is in place of the metering actuator. If a manometer is connected to the test fixture, pressure will be measured as air escapes through the leaking rail check valve. If a container of water is used instead of a manometer, bubbles will be seen as air escapes through the leaking rail check valve.

The overhead set marks on the damper are used to identify which cylinder is on the compression stroke, and therefore which injector has malfunctioned, if a change in manometer pressure or bubbles are seen.

Shut the engine OFF.

![[00c00077.png]]

The fuel-metering actuators are the actuators located on each end of the unit.

For engines equipped with the CM871, remove the fuel-metering actuator for the front three cylinders. Use the Signature™ ISX and QSX15 Electronic Control System Troubleshooting and Repair Manual, Bulletin 3666259. Refer to Procedure 019-110 in Section 19.

For engines equipped with the CM870, remove the fuel-metering actuator for the front three cylinders. Use the Signature™ ISX CM870 Electronic Control System Troubleshooting and Repair Manual, Bulletin 4021334. Refer to Procedure 019-110 in Section 19.

Install the Injector Leak Test Kit, Part Number 3164001, in place of the fuel-metering actuator.

> [!tip] Момент затяжки · Torque Value
> 15.3 n•m [135 in-lb]

Connect the flexible tubing to the hose fitting on the mounting plate.

Place the flexible tubing into a container of water.

![[00c00078.png]]

> [!warning] CAUTION · Осторожно
> Do not crank the engine for more than 20 seconds and allow 2 minutes between crank cycles for the starter to cool. Failure to do so can result in starting motor component damage.

Remove the 4-pin power connector from the engine control module (ECM) and then crank the engine. Disconnecting the 4-pin power connector will prevent the engine from starting.

> [!note] Note · Примечание
> For engines without 4-pin power connectors on the ECM, disconnect the fuel shutoff solenoid supply wire from the fuel shutoff solenoid and then crank the engine. Disconnecting the fuel shutoff solenoid supply wire will prevent the engine from starting.

If no bubbles are observed in the container, there is **not** a leak in the front bank. Continue on to the checks for the rear three cylinders outlined in the procedure below.

If bubbles are observed in the container, proceed with barring over the engine to determine which injector is leaking.

Bar the engine over while watching for bubbles in the container. If no bubbles are observed in the container while barring the engine, it does **not** indicate that there is no leak. Continue to bar the engine over to build sufficient backpressure to determine which injector is leaking.

The engine will need to be barred over three complete revolutions to evaluate each bank.

There can be a few bubbles observed immediately before reaching a timing mark. The leak indicator is if bubbles occur for an extended period between the timing marks.

![[08c00214.png]]

Note between which two timing marks the bubbles occur. Determine the leaking injector by following the diagram.

If bubbles occur between:

- A and B (number 3 injector is leaking)
- B and C (number 1 injector is leaking)
- C and A (number 2 injector is leaking).

![[06c00110.png]]

For engines equipped with the CM871, remove the mounting plate connected to the port for the front three cylinders. Install the fuel-metering actuator removed previously. Use the Signature™ ISX and QSX15 Electronic Control System Troubleshooting and Repair Manual, Bulletin 3666259. Refer to Procedure 019-110 in Section 19.

For engines equipped with the CM870, remove the mounting plate connected to the port for the front three cylinders. Install the fuel-metering actuator removed previously. Use the Signature™ ISX CM870 Electronic Control System Troubleshooting and Repair Manual, Bulletin 4021334. Refer to Procedure 019-110 in Section 19.

Remove the fuel-metering actuator for the rear three cylinders.

Install the Injector Leak Test Kit, Part Number 3164001, in place of the rear fuel-metering actuator.

> [!tip] Момент затяжки · Torque Value
> 15.3 n•m [135 in-lb]

Place the flexible tubing into a container of water.

Repeat the above procedure for the rear three cylinders.

![[05c00122.png]]

Bar the engine over and note between which two timing marks the bubbles occur.

If the bubbles occur between:

- A and B (number 4 injector is leaking)
- B and C (number 6 injector is leaking)
- C and A (number 5 injector is leaking).

![[06c00109.png]]

Replace the leaking injector(s). Go to the Remove section in this procedure.

![[02c00024.png]]

### Preparatory Steps

> [!danger] WARNING · Опасно
> Do not remove the pressure cap from a hot engine. Wait until the coolant temperature is below 50°C \[120°F\] before removing the pressure cap. Heated coolant spray or steam can cause personal injury.

> [!danger] WARNING · Опасно
> Coolant is toxic. Keep away from children and pets. If not reused, dispose of in accordance with local environmental regulations.

- Drain the coolant to below the cylinder head level. [[10-008-018-tr — Cooling System|Refer to Procedure 008-018 in Section 8.]]
- Remove the rocker lever cover. Refer to Procedure 003-011 in Section 3.
- Disconnect the engine brake solenoid wiring harness. [[10-020-015 — Engine Brake Wiring Harness|Refer to Procedure 020-015 in Section 20.]]

![[ck800wa.png]]

### Remove

> [!warning] CAUTION · Осторожно
> Do not bottom out adjusting screws. Engine damage can occur if adjusting screws are bottomed out.

Remove **only** the injector rocker lever shaft for the injector(s) being removed.

Loosen the injector rocker lever adjusting screws.

Remove the six capscrews and injector rocker lever shaft.

Do **not** let the rocker levers come off the shaft during removal.

![[03c00006.png]]

Rotate the engine to the valve set mark for the injector being removed. [[10-003-004-tr — Overhead Set|Refer to Procedure 003-004 in Section 3.]]

![[17c00091.png]]

Loosen and turn the valve lash adjusting screws **counterclockwise** to allow the intake and exhaust valve crossheads to be removed.

Remove the intake crosshead.

Mark the crossheads to make certain they are installed in the same position.

![[03c00087.png]]

Position the exhaust valve crosshead toward the exhaust side of the engine to allow the injector to be removed.

![[06c00003.png]]

Loosen the injector clamp capscrew.

Use a small magnet to remove the injector clamp capscrew.

Remove the injector clamp.

![[06c00002.png]]

> [!warning] CAUTION · Осторожно
> Do not use a heel bar to pry the injector loose from the cylinder head. Damage to the injector can occur.

Use injector puller, Part Number 3823579, to remove the injectors.

If the injector spring does come loose from the spring retainer, it can be reassembled by using a screwdriver to compress the spring back under the retainer.

![[06c00096.png]]

### Inspect for Reuse

Inspect the injector for missing or damaged o-rings. Replace o-rings as necessary.

![[06c00099.png]]

Inspect the injector cup for missing plug balls. Replace the injector, if necessary.

![[06c00100.png]]

### Disassemble

Oil Seals, Roll pin retained load ring

Thoroughly clean the oil and dirt from the outside of the injector.

Place the injector into the injector holding fixture.

Place the injector holding fixture into a vise. Tighten the vise to hold the fixture in place.

Align the load ring capscrew bracket with the cutout in the fixture plate.

![[22c00182.png]]

Use a T45 Torx™ drive (long version) to loosen the injector coupling retainer capscrew.

![[22c00183.png]]

Make certain the injector remains upright. This will prevent the lower plunger and spring from falling out.

Remove the retainer capscrew and bracket.

Remove the upper plunger/coupling assembly and coupling spring.

Some injector parts are **not** interchangeable.

Place each of the individual injector assembly parts together on a lint-free cloth.

![[22c00184.png]]

Remove the spring clip from the load ring.

The load ring drilling is designed to remove and install the roll pin in **only** one direction. Remove in the direction shown.

Use a 5/32 inch punch to lightly tap the roll pin loose and remove it from the load ring.

Discard the roll pin.

![[22c00203.png]]

Remove the load ring from the injector body.

![[22c00186.png]]

Install the coupling/plunger assembly into the injector body bore to prevent debris from entering the bore.

![[22c00187.png]]

The base of the oil seal is visible through the four machined holes in the side of the injector body.

![[22c00188.png]]

> [!warning] CAUTION · Осторожно
> Its very important that a 3/32 inch punch be used so the barrel is not damaged during oil seal removal.

Use a 3/32 inch punch. Place the punch at an upward angle, as shown in the illustration, against the base of the oil seal.

Use a hammer to gently tap the punch against the base of the oil seal. To prevent damage to the seal bore in the barrel, alternate between the four holes in the barrel so that the seal comes out evenly and does **not** score the barrel.

![[22c00189.png]]

> [!danger] WARNING · Опасно
> Wear appropriate eye and face protection when using compressed air. Flying debris and dirt can cause personal injury.

Slide the oil seal up the plunger.

Use a can of safety solvent to blow debris away from the oil seal area before removing the plunger.

![[22c00190.png]]

Make certain the injector remains upright.

Remove the oil seal and plunger assembly from the injector.

Remove the old oil seal from the plunger.

Remove the injector holding fixture and the injector from the vise.

Place the fixture and injector onto the arbor press table.

![[22c00191.png]]

Oil Seals, Clip retained load ring

Thoroughly clean the oil and dirt from the outside of the injector.

Place a clean, lint-free shop towel folded in quarters over the edge of a work bench.

While holding the injector firmly in one hand, place the upper plunger against the outer edge of the work bench with the load ring just above the working surface of the bench.

Lean in on the injector to partially compress the upper spring and plunger. Use care **not** to come in contact with the nozzle of the injector.

![[06c00136.png]]

Use a pick to remove the injector load ring retaining clip.

![[06c00137.png]]

Slowly remove pressure from the injector, releasing the upper spring.

Stand the injector upright and remove the load ring, the upper plunger/coupling assembly, and the spring.

> [!note] Note · Примечание
> Some of the injector parts are **not** interchangeable.

Place each of the individual injector assembly parts together on a lint-free cloth.

![[06c00138.png]]

Place the injector in the holding fixture, mounted in a bench vise.

![[06c00156.png]]

Locate the outer edge of the upper seal.

Use a punch, held at a slight angle, as shown in the illustration, to carefully fold the edge of the seal in and down.

Fold the edge of the seal in, 180 degrees from the first fold.

Use care **not** to damage the injector body.

![[06c00139.png]]

When the seal begins to rotate in the bore of the injector body, carefully insert a small pry bar into the center of the seal.

Carefully pry the seal out of the injector body bore.

Use care **not** to damage the injector body.

![[06c00141.png]]

### Assemble

Oil Seals, Roll pin retained load ring

> [!warning] CAUTION · Осторожно
> Do not install the oil seal upside down. Failure to install the seal correctly will cause damage to the oil seal.

The oil seal will fit on the tool tightly if installed correctly. The spring side of the oil seal, as shown, faces up when installed in the injector.

Install a new oil seal onto the installation tool.

![[22c00192.png]]

With the new oil seal positioned on the tool, position the tool over the seal bore.

Use the arbor press to gently place pressure onto the installation tool until the outer diameter face of the tool contacts the injector body.

When properly installed, the seal height will **not** be flush with the injector body. The height will be approximately 0.5 mm \[0.020 in\] above the injector.

![[22c00193.png]]

Place the injector holding fixture with injector into the vise. Tighten the vise to hold the fixture in place.

Install the load ring on the injector. Align the load ring capscrew hole end with the cutout on the injector fixture.

![[22c00186.png]]

Install a new roll pin into the load ring. By design, the roll pin holes are a different size on each side, so the roll pin **must** be installed in the correct direction, as illustrated.

Use a 5/32 inch punch to gently tap the roll pin into both holes in the load ring. Continue driving the roll pin into the load ring until the pin is centered evenly in both holes and is an equal distance from both sides.

![[22c00204.png]]

Inspect the oil seal and plunger bore for debris. If debris is present, clean with a lint-free cloth.

Clean the injector coupling spring with a lint-free cloth. Assemble the spring onto the load ring.

Clean the plunger and coupling assembly with a lint-free cloth.

![[22c00197.png]]

Lubricate the plunger with clean calibration fluid.

![[22c00198.png]]

Slightly angle and rotate the upper plunger while installing the plunger into the oil seal.

Hold the plunger vertically and rotate while installing the plunger into the injector bore.

![[22c00199.png]]

Use a flashlight to view through the coupling spring. Inspect the oil seal to verify the garter spring (1) is still in the correct location around the seal.

![[22c00200.png]]

Install the spring retainer bracket.

Tighten the retainer capscrew.

> [!tip] Момент затяжки · Torque Value
> 30 n•m [22 ft-lb]

Install new injector o-rings.

![[22c00201.png]]

Oil Seals, Clip retained load ring

> [!warning] CAUTION · Осторожно
> Do not install the oil seal upside down. Failure to install the seal correctly will cause damage to the oil seal.

The oil seal will fit on the tool tightly, if installed correctly. The spring side of the oil seal, as shown, faces up when installed in the injector.

Install a new oil seal onto the installation tool.

![[22c00192.png]]

With the new oil seal positioned on the tool, position the tool over the seal bore.

Use the arbor press to gently place pressure onto the installation tool until the outer diameter face of the tool contacts the injector body.

When properly installed, the seal height will **not** be flush with the injector body. The height will be approximately 0.5 mm \[0.020 in\] above the injector.

![[06c00157.png]]

Lubricate the plunger with clean calibration fluid.

Carefully install the spring and load ring on the upper plunger.

![[22c00198.png]]

Holding the injector upright in one hand, slightly angle and rotate the upper plunger while installing the plunger into the oil seal.

Hold the plunger vertically and rotate while installing the plunger into the injector bore.

![[06c00143.png]]

Use a flashlight to view through the coupling spring. Inspect the oil seal to verify the garter spring is still in the correct location around the seal.

![[06c00144.png]]

Place a clean, lint-free shop towel folded in quarters over the edge of a work bench.

While holding the injector firmly in one hand, place the upper plunger against the outer edge of the work bench with the load ring just above the working surface of the bench.

Lean in on the injector to partially compress the upper spring and plunger. Use care **not** to come in contact with the nozzle of the injector.

![[06c00145.png]]

Install the clip onto the injector load ring.

Slowly, remove pressure from the injector, releasing the upper spring against the load ring.

Install new injector o-rings.

![[06c00146.png]]

### Install

Use clean 15W-40 lubricating oil to lubricate the o-rings.

![[06c00097.png]]

> [!warning] CAUTION · Осторожно
> Make sure the injector hold down clamp is properly aligned before tightening the capscrew. It is possible for the clamp to contact a nearby ledge, and result in low clamp load.

Install the injector into the cylinder head. Install the injector clamp and capscrew.

Tighten the capscrew.

> [!tip] Момент затяжки · Torque Value
> 80 n•m [59 ft-lb]

Install the crossheads.

![[06c00098.png]]

### Finishing Steps

- Install and set the injector rocker lever and valve rocker lever assemblies. [[10-003-009-tr — Rocker Lever Assembly|Refer to Procedure 003-009 in Section 3.]]
- Connect the engine brake solenoid wiring harness, if equipped. [[10-020-015 — Engine Brake Wiring Harness|Refer to Procedure 020-015 in Section 15.]]
- Adjust the overhead set as needed. [[10-003-004-tr — Overhead Set|Refer to Procedure 003-004 in Section 3.]]
- Install the rocker lever cover. Refer to Procedure 003-011 in Section 3.
- Fill the cooling system. [[10-008-018-tr — Cooling System|Refer to Procedure 008-018 in Section 8.]]
- Operate the engine to normal operating temperature and check for leaks.

> [!note] Note · Примечание
> If damage resulted in oil, excessive fuel, or excessive black smoke entering the exhaust system, the aftertreatment system **must** be inspected. Reference the Aftertreatment Diesel Oxidation Catalyst and Aftertreatment Diesel Particulate Filter Reuse Guidelines, Bulletin 4021600.

> [!note] Note · Примечание
> If the injector o-rings are being replaced due to an internal coolant leak, the crankcase breather element **must** be changed. [[101-003-019-tr — Crankcase Breather Element|Refer to Procedure 003-019 in Section 3.]]

> [!note] Note · Примечание
> If damage resulted in coolant entering the exhaust system, the aftertreatment system can be recovered. [[101-014-013-tr — Aftertreatment Testing|Refer to Procedure 014-013 in Section 14.]]

![[ck800wa.png]]
