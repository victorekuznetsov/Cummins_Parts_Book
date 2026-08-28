---
type: "Процедура"
doc: "101-014-013"
title_en: "Aftertreatment Testing"
modified: "2010-08-04"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "3666322"
figures: 14
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/101/101-014-013.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/101-014-013.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/101"
---

# Aftertreatment Testing

> [!abstract] Процедура · `101-014-013`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[3666322 — ISM, ISMe, and QSM11 Service Manual|3666322]]
> **Секции:** Section 14 - Engine Testing - Group 14
> **Даты:** изменён 2010-08-04
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/101/101-014-013.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/101-014-013.pdf)

### General Information

The Snap-Acceleration Test is used to check the aftertreatment diesel particulate filter for cracks or other progressive damage, without removing the filter system. It is used to test the functionality of the aftertreatment diesel particulate filter.

The INSITE™ electronic service tool Aftertreatment Diesel Particulate Filter Stationary Regeneration Test is used to:

- Regenerate an aftertreatment diesel particulate filter
- Recover the aftertreatment diesel oxidation catalyst and aftertreatment diesel particulate filter after coolant contamination
- Check the aftertreatment diesel oxidation catalyst efficiency
- Check for the correct installation of the aftertreatment temperature sensors
- Reset the stored soot load in the engine ECM
- Check the aftertreatment fuel injector, shutoff valve, and drive train functionality.

Check for active fault codes prior to performing either of these procedures. If any active fault codes are present, follow the appropriate fault code troubleshooting tree.

![[11c00245.png]]

The INSITE™ electronic service tool Aftertreatment Diesel Particulate Filter Stationary Regeneration Test can be used to regain functionality of the Aftertreatment Diesel Oxidation Catalyst (DOC) and Aftertreatment Diesel Particulate Filter (DPF) after either, or both, have been exposed to coolant.

> [!note] Note · Примечание
> If the DOC and DPF are suspected of having coolant contamination, they do **not** need to be removed and inspected. Consult the Preparatory Steps section of this procedure for further details.

The temperatures that are achieved during the Regeneration are high enough to evaporate the coolant out of both components and return both components to normal operating specifications.

> [!note] Note · Примечание
> If these components are suspected of having coolant contamination, do **not** perform the snap acceleration test before performing the regeneration.

![[11c00245.png]]

This section outlines the Exhaust System Outlet Inspection.

Inspection of the exhaust system outlet can reveal the condition of the aftertreatment diesel particulate filter. The exhaust system outlet should appear clean with little to no exhaust residue/soot buildup.

The aftertreatment diesel particulate filter is **not** 100 percent efficient. Some accumulation of exhaust residue/soot is normal, and does **not** indicate a malfunctioning aftertreatment diesel particulate filter.

A heavy buildup of exhaust residue/soot can indicate a malfunction of the aftertreatment diesel particulate filter.

To determine if the exhaust residue/soot accumulation on the exhaust system outlet is the result of a malfunctioning aftertreatment diesel particulate filter, perform one of the following:

1. Snap Acceleration Test as outlined in this procedure.
2. Clean the last 152 to 254 mm \[6 to 10 in\] of the exhaust system outlet. Operate the vehicle for one shift or trip and inspect the exhaust system outlet for exhaust residue/soot accumulation.
3. Inspect the aftertreatment diesel particulate filter.

![[14d00033.png]]

#### Snap Acceleration Test

- The vehicle transmission **must** be in neutral.
- The vehicle parking brake **must** be applied.

Start and idle the engine.

Rapidly depress the accelerator pedal from 0 percent to 100 percent. This can be performed multiple times, if necessary.

![[14c00079.png]]

During this test, visually check for black smoke exiting the exhaust stack, as the engine is accelerated from low idle to high idle

> [!note] Note · Примечание
> In some applications, a snap acceleration test may **not** provide the conditions necessary to reveal a malfunctioning aftertreatment diesel particulate filter. If there is a heavy buildup of exhaust residue/soot on the exhaust system outlet and a snap acceleration does **not** reveal a condition outlined in the following steps, it can be necessary to perform:

- A stall test. [[101-014-008 — Engine Testing (In Chassis)|Refer to Procedure 014-008 in Section 14.]]
- A brief acceleration run under partial to full load.

Refer to the Catalyst and Aftertreatment Particulate Filter Reuse Guidelines, Bulletin [[4021600 — Aftertreatment Diesel Oxidation Catalyst (DOC) and Aftertreatment Diesel Particulate|4021600]], for pass or fail guidelines.

![[11c00246.png]]

If gray smoke or faint black smoke is present, refer to the Catalyst and Aftertreatment Particulate Filter Reuse Guidelines, Bulletin [[4021600 — Aftertreatment Diesel Oxidation Catalyst (DOC) and Aftertreatment Diesel Particulate|4021600]], for pass or fail guidelines.

White smoke during the snap-acceleration test does **not** indicate a failure. No repair is necessary.

![[11c00247.png]]

### Preparatory Steps

> [!danger] WARNING · Опасно
> During regeneration, exhaust gas temperature could reach 800°C \[1500°F\] and exhaust system surface temperature can exceed 700°C \[1300°F\], which is hot enough to ignite or melt common materials, and cause severe burn injuries. The exhaust and exhaust components can remain hot after the vehicle stopped moving. To avoid the risk of fire, property damage, burns or other serious personal injury, allow the exhaust system to cool before beginning this procedure or repair and make sure that no combustible materials are located where they are likely to come in contact with hot exhaust or exhaust components.

To perform a stationary regeneration, connect INSITE™ electronic service tool and check for active fault codes. If any fault codes are present other than Fault Codes 2639 or 1921, go to Section TF for any fault code troubleshooting before proceeding. Do **not** perform a stationary regeneration with active fault codes other than Fault Codes 2639 or 1921, unless guided to do so by the fault code troubleshooting.

> [!note] Note · Примечание
> If the stationary regeneration is being performed to recover either the DOC, the DPF, or both after coolant contamination, the DOC does **not** need to be removed or inspected unless there are active fault codes that require inspection as part of the fault code troubleshooting steps.

> [!note] Note · Примечание
> **Unless** there are complaints of black smoke during operation and the exhaust stack is black, the DPF does **not** need to be removed or inspected during this process.

Before performing a stationary regeneration, follow the steps listed below:

1. Select an appropriate location to park the vehicle.
2. Park the truck securely.
3. Set up a safe exhaust area.
4. Check exhaust system surfaces.
5. Prepare for engine speed changes during regeneration.
6. Begin the stationary regeneration. This can be performed in two ways:
7. Monitor the area.

To stop a stationary regeneration, engage the clutch, brake, or throttle pedal; or turn off the engine.

Once regeneration is complete, exhaust gas and exhaust surface temperatures will remain elevated for 3 to 5 minutes.

![[ck800wa.png]]

### Setup

Start and idle the engine.

Prior to the Aftertreatment Diesel Particulate Filter Regeneration Test, inspect the exhaust piping for leaks, cracks, and loose connections.

- For ISM engines, use the following procedure. [[35-010-024-tr — Air Leaks, Air Intake and Exhaust Systems|Refer to Procedure 010-024 in Section 10.]]
- For ISX engines, use the following procedure. Refer to Procedure 010-024 in Section 10.
- For ISX11.9 engines, use the following procedure. Refer to Procedure 010-024 in Section 10.
- For ISX15 engines, use the following procedure. Refer to Procedure 010-024 in Section 10.

Tighten the exhaust clamps if necessary.

Consult the OEM specifications for the correct torque value.

Any leaks in the exhaust system will cause the Aftertreatment Diesel Particulate Filter Regeneration Test to be less efficient in reducing the soot load of the filter.

![[10d00395.png]]

### Test

The Aftertreatment Diesel Particulate Filter Regeneration Test can be found under the ECM Diagnostic Test menu in the INSITE™ electronic service tool.

![[19c00691.png]]

If INSITE™ electronic service tool is **not** available, some vehicles can be equipped with a stationary regeneration switch in the cab. The switch can be a stand-alone switch or can be combined with the diagnostic switch. Check with the OEM for the location and availability of the switch.

> [!note] Note · Примечание
> In order for the stationary regeneration switch to function, the stationary regeneration switch **must** be enabled in the ECM.

Unlike the Aftertreatment Diesel Particulate Filter Regeneration Test with the INSITE™ electronic service tool, this switch will **only** start a stationary regeneration if the soot load of the filter is high enough. This is indicated by the aftertreatment lamp being illuminated or flashing.

> [!note] Note · Примечание
> A stationary regeneration can **not** be initiated through the use of the cab switch if regeneration inhibit is enabled. INSITE™ electronic service tool **must** then be used to initiate the stationary regeneration.

![[14d00035.png]]

> [!note] Note · Примечание
> If the Aftertreatment Diesel Particulate Filter Regeneration Test will **not** initiate, use the Stationary Regeneration - Will Not Start troubleshooting symptom tree.

When the test is started, the engine idle speed will be raised automatically to the required level. Expected engine speed can reach between 1000 and 1500 rpm.

The engine will then, through the engine controls, operate in a manner to build exhaust heat. The turbocharger can emit a slight “whining” noise during the test. This is normal.

The Aftertreatment Diesel Particulate Filter Regeneration can take up to two and one half hours to complete, depending on the soot loading of the filter as well as conditions of the environment, such as but **not** limited to the temperature and humidity.

Once the Aftertreatment Diesel Particulate Filter Regeneration Test is complete, the engine will automatically return to normal idle speed.

![[10900098.png]]

During the Aftertreatment Diesel Particulate Filter Regeneration Test, the following items will be monitored:

- Aftertreatment Injector Status - Informs the user when fuel is being injected, in small quantity, into the exhaust system upstream of the diesel oxidation catalyst
- Aftertreatment Diesel Particulate Filter outlet temperature
- Aftertreatment Diesel Particulate Filter inlet temperature
- Aftertreatment Diesel Oxidation Catalyst inlet temperature
- Aftertreatment Diesel Particulate Filter Soot Load - Informs the user of the current soot load of the filter:

![[11d00240.png]]

> [!warning] CAUTION · Осторожно
> During the stationary regeneration, the exhaust gas temperature can reach 800°C \[1500°F\] and the surface temperature can exceed 700°C \[1300°F\].

The stationary regeneration can take up to 2-1/2 hours to complete, depending on the soot loading of the filter. At any time the stationary regeneration can be aborted by clicking on the “Stop” button in the INSITE™ electronic service tool.

The stationary regeneration will be aborted if:

- A fault becomes active
- The accelerator is depressed
- The clutch pedal is depressed
- The brake pedal is depressed
- The transmission is put into gear.

> [!note] Note · Примечание
> If a stationary regeneration can **not** be initiated or is aborted, and the engine has a low power complaint, use the following procedures.

- For ISM engines, use the following procedure. [[101-011-009-tr — Exhaust Restriction|Refer to Procedure 011-009 in Section 11.]]
- For ISX engines, use the following procedure. [[101-011-009-tr — Exhaust Restriction|Refer to Procedure 011-009 in Section 11.]]
- For ISX11.9 engines, use the following procedure. Refer to Procedure 011-009 in Section 11.
- For ISX15 engines, use the following procedure. Refer to Procedure 011-009 in Section 11.

#### Pass or Fail Criteria

- Pass: Aftertreatment Testing Procedure 014-013 in Section 14 has passed, if there is no visible black smoke and the stationary regeneration completes with no aftertreatment fault codes being generated.
- Fail: Aftertreatment Testing Procedure 014-013 in Section 14 has failed, if there is visible black smoke and/or aftertreatment fault codes are generated. Repair the cause of the black smoke and/or correct the fault codes.

![[19c00691.png]]

### Finishing Steps

Allow the engine and exhaust system to cool down. Temperatures can maintain an elevated state for several minutes.

Check to make sure the diesel particulate filter lamp is **not** illuminated.

> [!note] Note · Примечание
> If the diesel particulate filter lamp is illuminated and Fault Code 2639 or 1921 are still active, a second regeneration will be needed. If the fault is still active after a second regeneration, the filter needs to be cleaned of ash or soot.

- For ISM engines, use the following procedure. [[101-011-041-tr — Aftertreatment Diesel Particulate Filter|Refer to Procedure 011-041 in Section 11.]]
- For ISX engines, use the following procedure. [[101-011-041-tr — Aftertreatment Diesel Particulate Filter|Refer to Procedure 011-041 in Section 11.]]
- For ISX11.9 engines, use the following procedure. Refer to Procedure 011-041 in Section 11.
- For ISX15 engines, use the following procedure. Refer to Procedure 011-041 in Section 11.

Check for any active fault codes. If active fault codes are present, use Section TF for fault code troubleshooting.

Use INSITE™ electronic service tool to clear all inactive fault codes.

![[11d00240.png]]
