---
type: "Процедура"
doc: "493-014-016"
title_en: "Aftertreatment Diesel Particulate Filter (DPF) Regeneration Test"
modified: "2020-08-07"
manuals:
  - "5411181"
figures: 9
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/493/493-014-016.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/493-014-016.pdf"
tags:
  - "документ/процедура"
  - "группа/493"
---

# Aftertreatment Diesel Particulate Filter (DPF) Regeneration Test

> [!abstract] Процедура · `493-014-016`
> **Входит в руководства:** [[5411181 — X15 CM2350 X114B - Efficiency Series Service Manual|5411181]]
> **Секции:** Section 14 - Engine Testing - Group 14
> **Даты:** изменён 2020-08-07
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/493/493-014-016.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/493-014-016.pdf)

### Select Service Tools

#### Recommended Cummins® Service Tool

- Cummins® electronic service tool or equivalent

#### Additional Service Items

- Wheel chocks
- Fire extinguisher

### General Information

This procedure contains information about how to inspect the aftertreatment diesel particulate filter (DPF) and perform a stationary regeneration.

There are two main steps when checking the DPF:

1. The Initial Check section of this procedure is used to determine the condition of the aftertreatment DPF without removal of the filter. The Initial Check step should be used to determine if the aftertreatment DPF has malfunctioned due to progressive damage.
2. The Test section of the procedure explains how to perform a stationary regeneration using an electronic service tool or an original equipment manufacturer (OEM)-provided stationary regeneration method. The Test step should **only** be performed when troubleshooting procedures and/or engine indicator lamps indicate this is necessary.

If the aftertreatment DPF requires replacement, before replacing:

- Troubleshoot and clear all fault codes.
- Verify the correct fuel type is being used.
- Troubleshoot **any** oil consumption complaint.
- Troubleshoot **any** coolant consumption complaint.
- Inspect the diesel oxidation catalyst (DOC). Refer to the Clean and Inspect for Reuse section of the DOC procedure. Refer to Procedure 011-049 in Section 11.

The recommended Cummins® electronic service tool or equivalent Aftertreatment DPF Stationary Regeneration Test can be used to:

- Regenerate an aftertreatment DPF.
- Recover the aftertreatment DOC and aftertreatment DPF after coolant contamination.
- Reset the stored soot load in the engine control module (ECM).
- Check the aftertreatment DOC efficiency.
- Check for the presence of the aftertreatment DOC.
- Check for the correct installation of the aftertreatment temperature sensors.

The electronic service tool Aftertreatment DPF Stationary Regeneration Test can be used to regain functionality of the aftertreatment DOC and aftertreatment DPF, after either or both have been exposed to coolant.

The temperatures that are achieved during regeneration are high enough to evaporate the coolant out of both components and return them to normal operating specifications.

> [!note] Note · Примечание
> If these components are suspected of having coolant contamination, do **not** perform the snap acceleration test before performing the regeneration.

### Initial Check

Use the electronic service tool to check for fault codes. If **any** fault codes are present, follow the corresponding troubleshooting tree before performing **any** part of this procedure.

The fault code troubleshooting tree, in some cases, will refer back to this procedure to complete the diagnostics.

![[19r00163.png]]

#### Exhaust System Outlet Inspection

- Inspection of the exhaust system outlet can reveal the condition of the aftertreatment DPF. The exhaust system outlet should appear clean with little to no exhaust residue/soot buildup.
- Some accumulation of exhaust residue/soot is normal and does **not** indicate a malfunctioning aftertreatment DPF.
- A heavy buildup of exhaust residue/soot can indicate a malfunctioning aftertreatment DPF.

To determine if the exhaust residue/soot accumulation on the exhaust system outlet is the result of a malfunctioning aftertreatment DPF, perform one of the following:

- Snap Acceleration Test. Refer to Procedure 014-017 in Section 14.
- Clean the last 152 to 254 mm \[6 to 10 in\] of the exhaust system outlet. Operate the vehicle for one shift or trip and inspect the exhaust system outlet for exhaust residue/soot accumulation.
- Inspect the aftertreatment DPF. Refer to Procedure 011-041 in Section 11.

![[14d00033.png]]

### Test

Initial Setup

> [!danger] WARNING · Опасно
> During regeneration, exhaust gas temperature can reach 800 °C \[1500°F\], and exhaust system surface temperature can exceed 700 °C \[1300°F\], which is hot enough to ignite or melt common materials, and to burn people. The exhaust and exhaust components can remain hot after the vehicle has stopped moving. To avoid the risk of fire, property damage, burns, or other serious personal injury, allow the exhaust system to cool before beginning this procedure or repair and make sure that no combustible materials are located where they are likely to come in contact with hot exhaust or exhaust components.

> [!note] Note · Примечание
> If the stationary regeneration is being performed to recover either the DOC or DPF, or both, after coolant contamination, the DOC does **not** need to be removed or inspected unless there are active faults that require inspection as part of the fault code troubleshooting steps.

> [!note] Note · Примечание
> Unless there are complaints of black smoke during operation and the exhaust stack is black, the DPF does **not** need to be removed or inspected during this process.

Before performing stationary regeneration, follow the steps listed below:

1. Select an appropriate location to park the vehicle.
2. Park the truck securely.
3. Set up a safe exhaust area.
4. Check exhaust system surfaces.
5. Prepare for engine speed changes during regeneration.
6. Begin the stationary regeneration. This can be performed in two ways:
7. Monitor the area.

To stop a stationary regeneration, engage the clutch, brake, or throttle pedal; or turn off the engine.

Once regeneration is complete, exhaust gas and exhaust surface temperatures will remain elevated for 3 to 5 minutes.

Aftertreatment Diesel Particulate Filter Regeneration

The test can be found under the ECM Diagnostics Test menu in the electronic service tool. Follow the on-screen instructions to perform the test.

To stop the stationary regeneration test at **any** time during the test:

1. Select the stop button on the electronic service tool monitor screen.
2. Depress the clutch, if equipped.
3. Depress the brake.
4. Depress the accelerator pedal.
5. Turn the engine off.

![[19r00163.png]]

> [!note] Note · Примечание
> If the electronic service tool is **not** available, some vehicles can be equipped with an OEM-provided stationary regeneration method. The most common type is a stationary regeneration switch in the cab. The stationary regeneration switch can be a stand-alone switch, or can be combined with the diagnostic switch, at the discretion of the vehicle manufacturer.

OEM stationary regeneration initiations vary. See equipment manufacturer service information.

In order for the stationary regeneration switch to function, the stationary regeneration switch parameter **must** be enabled in the ECM.

Unlike the Aftertreatment Stationary Regeneration Test with the electronic service tool, this switch will **only** start a stationary regeneration if the soot load of the filter is high enough. This is indicated by an illuminated or flashing aftertreatment lamp.

![[14d00035.png]]

If the red STOP ENGINE indicator lamp is illuminated and an active Fault Code 1922 is present, indicating the aftertreatment DPF soot load is at the most severe level, the Aftertreatment DPF Regeneration Test should **not** be performed.

The aftertreatment DPF **must** be inspected. Refer to Procedure 011-041 in Section 11.

After the aftertreatment DPF is replaced, the troubleshooting tree associated with the red STOP ENGINE lamp **must** be followed to reset the soot load value stored in the ECM.

![[11c00254.png]]

During the Aftertreatment DPF Regeneration Test, the following will be monitored:

- Aftertreatment DPF Soot Load: Informs the user of the current soot load of the filter:
- Aftertreatment DPF Outlet Temperature
- Aftertreatment DPF Inlet Temperature
- Aftertreatment Diesel Oxidation Catalyst Inlet Temperature.

![[19r00164.png]]

Tighten the exhaust clamps, if necessary. See equipment manufacturer service information for the correct torque value.

**Any** leaks in the exhaust system will cause the Aftertreatment DPF Test to be less efficient in reducing the soot load of the filter. This will result in the test running longer and possibly **not** completing.

![[10d00395.png]]

> [!note] Note · Примечание
> If the Aftertreatment DPF Regeneration Test will **not** initiate, see the Stationary Regeneration - Will Not Activate troubleshooting symptom tree in Section TS.

Once the Aftertreatment DPF Regeneration Test is started, follow the electronic service tool on-screen instructions. When the test is started, the engine idle speed will be raised automatically to the required level.

The engine will, through engine controls, operate in a manner to build exhaust heat. The turbocharger will emit a slight whining noise during this test. This is normal.

Once the Aftertreatment DPF Regeneration Test is complete, the engine will automatically return to normal idle speed.

![[10900098.png]]

Once the test is complete, check for active fault codes and/or engine indicator lamps for high aftertreatment diesel particulate soot load after performing the Aftertreatment DPF Regeneration Test. If **any** active fault codes are present, follow the appropriate fault code troubleshooting tree.

![[11c00110.png]]
