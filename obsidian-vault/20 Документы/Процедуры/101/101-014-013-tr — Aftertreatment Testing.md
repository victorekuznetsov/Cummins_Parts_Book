---
type: "Процедура"
doc: "101-014-013-tr"
title_en: "Aftertreatment Testing"
modified: "2015-08-28"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
  - "80141463"
  - "80248213"
families:
  - "QSM11"
  - "QSX15"
manuals:
  - "3666239"
  - "3666322"
figures: 18
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/101/101-014-013-tr.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/101-014-013-tr.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "двигатель/QSX15"
  - "группа/101"
---

# Aftertreatment Testing

> [!abstract] Процедура · `101-014-013-tr`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSM11, QSX15
> **Входит в руководства:** [[3666239 — Signature™, ISX, and QSX15 Service Manual|3666239]], [[3666322 — ISM, ISMe, and QSM11 Service Manual|3666322]]
> **Секции:** Section 14 - Engine Testing - Group 14
> **Даты:** изменён 2015-08-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/101/101-014-013-tr.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/101-014-013-tr.pdf)

### General Information

> [!danger] WARNING · Опасно
> During regeneration, exhaust gas temperature could reach 800°C \[1500°F\] and exhaust system surface temperature can exceed 700°C \[1300°F\], which is hot enough to ignite or melt common materials, and cause severe burn injuries. The exhaust and exhaust components can remain hot after the vehicle stopped moving. To avoid the risk of fire, property damage, burns or other serious personal injury, allow the exhaust system to cool before beginning this procedure or repair and make sure that no combustible materials are located where they are likely to come in contact with hot exhaust or exhaust components.

The Snap Acceleration Test is used to check the aftertreatment diesel particulate filter (DPF) for cracks or other progressive damage, without removing the filter system. It is used to test the functionality of the aftertreatment DPF.

The INSITE™ electronic service tool Aftertreatment Diesel Particulate Filter Stationary Regeneration Test is used to:

- Regenerate an aftertreatment DPF
- Recover the aftertreatment diesel oxidation catalyst (DOC) and aftertreatment DPF after coolant contamination
- Check the aftertreatment DOC efficiency
- Check for the correct installation of the aftertreatment temperature sensors
- Reset the stored soot load in the engine control module (ECM)
- Check the aftertreatment fuel injector, shutoff valve, and drive train functionality.

Check for active fault codes prior to performing either of these procedures. If any active fault codes are present, follow the appropriate fault code troubleshooting tree.

![[11c00245.png]]

The INSITE™ electronic service tool Aftertreatment Diesel Particulate Filter Stationary Regeneration Test can be used to regain functionality of the aftertreatment DOC and aftertreatment DPF after either, or both, have been exposed to coolant.

> [!note] Note · Примечание
> If the DOC and DPF are suspected of having coolant contamination, they do **not** need to be removed and inspected. Consult the Preparatory Steps section of this procedure for further details.

The temperatures that are achieved during the regeneration are high enough to evaporate the coolant out of both components and return both components to normal operating specifications.

> [!note] Note · Примечание
> If these components are suspected of having coolant contamination, do **not** perform the Snap Acceleration Test before performing the regeneration.

![[11c00245.png]]

This section outlines the exhaust system outlet inspection.

Inspection of the exhaust system outlet can reveal the condition of the aftertreatment DPF. The exhaust system outlet should appear clean, with little to no exhaust residue/soot buildup.

The aftertreatment DPF is **not** 100 percent efficient. Some accumulation of exhaust residue/soot is normal, and does **not** indicate a malfunctioning aftertreatment DPF.

A heavy buildup of exhaust residue/soot can indicate a malfunction of the aftertreatment DPF.

To determine if the exhaust residue/soot accumulation on the exhaust system outlet is the result of a malfunctioning aftertreatment DPF, perform one of the following:

1. Snap Acceleration Test as outlined in this procedure.
2. Clean the last 152 to 254 mm \[6 to 10 in\] of the exhaust system outlet. Operate the vehicle for one shift or trip and inspect the exhaust system outlet for exhaust residue/soot accumulation.
3. Inspect the aftertreatment DPF. [[101-011-041-tr — Aftertreatment Diesel Particulate Filter|Refer to Procedure 011-041 in Section 11.]]

![[14d00033.png]]

### Setup

Start and idle the engine.

Prior to the Aftertreatment Diesel Particulate Filter Regeneration Test, inspect the exhaust piping for leaks, cracks, and loose connections.

- For ISM engines, use the following procedure. [[35-010-024-tr — Air Leaks, Air Intake and Exhaust Systems|Refer to Procedure 010-024 in Section 10.]]
- For ISX engines, use the following procedure. Refer to Procedure 010-024 in Section 10.

Tighten the exhaust clamps, if necessary.

Consult the OEM specifications for the correct torque value.

Any leaks in the exhaust system will cause the Aftertreatment Diesel Particulate Filter Regeneration Test to be less efficient in reducing the soot load of the filter.

![[10d00395.png]]

### Test

Aftertreatment Diesel Particulate Filter Regeneration

The Aftertreatment Diesel Particulate Filter Regeneration Test can be found under the ECM Diagnostic Test menu in INSITE™ electronic service tool.

To perform a stationary regeneration, connect INSITE™ electronic service tool and check for active fault codes. If any fault codes are present other than Fault Codes 2639 or 1921, go to Section TF for any fault code troubleshooting before proceeding. Do **not** perform a stationary regeneration with active fault codes other than Fault Codes 2639 or 1921, unless guided to do so by the fault code troubleshooting tree.

> [!note] Note · Примечание
> Unless there are complaints of black smoke during operation and the exhaust stack is black, the DPF does **not** need to be removed or inspected during this process.

![[19803969.png]]

If INSITE™ electronic service tool is **not** available, some vehicles can be equipped with a stationary regeneration switch in the cab. The switch can be a stand-alone switch or can be combined with the diagnostic switch. Check with the OEM for the location and availability of the switch.

> [!note] Note · Примечание
> In order for the stationary regeneration switch to function, the stationary regeneration switch **must** be enabled in the ECM.

Unlike the Aftertreatment Diesel Particulate Filter Regeneration Test with INSITE™ electronic service tool, this switch will **only** start a stationary regeneration if the soot load of the filter is high enough. This is indicated by the aftertreatment lamp being illuminated or flashing.

> [!note] Note · Примечание
> A stationary regeneration can **not** be initiated through the use of the cab switch if regeneration inhibit is enabled. INSITE™ electronic service tool **must** then be used to initiate the stationary regeneration.

![[14d00035.png]]

> [!note] Note · Примечание
> If the Aftertreatment Diesel Particulate Filter Regeneration Test will **not** initiate, use the Stationary Regeneration - Will Not Start troubleshooting symptom tree in Section TS.

When the test is started, the engine idle speed will be raised automatically to the required level. Expected engine speed can reach between 1000 and 1500 rpm.

The engine will then, through the engine controls, operate in a manner to build exhaust heat. The turbocharger can emit a slight “whining” noise during the test. This is normal.

The Aftertreatment Diesel Particulate Filter Regeneration can take up to 2-½ hours to complete, depending on the soot loading of the filter, as well as conditions of the environment, such as, but **not** limited to, the temperature and humidity.

Once the Aftertreatment Diesel Particulate Filter Regeneration Test is complete, the engine will automatically return to normal idle speed.

![[10900098.png]]

During the Aftertreatment Diesel Particulate Filter Regeneration Test, the following items will be monitored:

- Aftertreatment Injector Status - Informs the user when fuel is being injected, in small quantity, into the exhaust system upstream of the DOC
- Aftertreatment DPF outlet temperature
- Aftertreatment DPF inlet temperature
- Aftertreatment DOC inlet temperature
- Aftertreatment DPF Soot Load - Informs the user of the current soot load of the filter:

![[19803969.png]]

> [!danger] WARNING · Опасно
> During regeneration, exhaust gas temperature could reach 800°C \[1500°F\] and exhaust system surface temperature can exceed 700°C \[1300°F\], which is hot enough to ignite or melt common materials, and cause severe burn injuries. The exhaust and exhaust components can remain hot after the vehicle stopped moving. To avoid the risk of fire, property damage, burns or other serious personal injury, allow the exhaust system to cool before beginning this procedure or repair and make sure that no combustible materials are located where they are likely to come in contact with hot exhaust or exhaust components.

The stationary regeneration can take up to 2-½ hours to complete, depending on the soot loading of the filter. At any time the stationary regeneration can be aborted by clicking on the “Stop” button in INSITE™ electronic service tool.

The stationary regeneration will be aborted if:

- A fault becomes active
- The accelerator is depressed
- The clutch pedal is depressed
- The brake pedal is depressed
- The transmission is put into gear.

> [!note] Note · Примечание
> If a stationary regeneration can **not** be initiated or is aborted, and the engine has a low power complaint, use the following procedure.

- [[101-011-009-tr — Exhaust Restriction|Refer to Procedure 011-009 in Section 11.]]

Begin the stationary regeneration. This can be performed by a stationary regeneration switch in the cab or by INSITE electronic service tool.

- Stationary regeneration switch in the cab:
- INSITE™ electronic service tool:
- In either case, the engine will create enough heat to regenerate the aftertreatment DPF. Engine speed will increase and the turbocharger can whistle loudly during the regeneration process. Once the aftertreatment DPF is regenerated, the engine will automatically return to normal idle speed
- Monitor the vehicle and surrounding area during regeneration. If any unsafe condition occurs, shut off the engine immediately.

#### Pass or Fail Criteria

- Pass: Aftertreatment Testing Procedure 014-013 in Section 14 has passed if there is no visible black smoke and the stationary regeneration completes with no aftertreatment fault codes being generated.
- Fail: Aftertreatment Testing Procedure 014-013 in Section 14 has failed if there is visible black smoke and/or aftertreatment fault codes are generated. Repair the cause of the black smoke and/or correct the fault codes.

![[19803969.png]]

Snap Acceleration - Aftertreatment Connected

The vehicle transmission **must** be in neutral and the vehicle parking brake **must** be applied.

Start and idle the engine. Rapidly depress the accelerator pedal from 0 to 100 percent. This can be performed multiple times, if necessary.

![[14c00079.png]]

During this test, check for black smoke exiting the exhaust stack, as the engine is accelerated from low idle to high idle.

> [!note] Note · Примечание
> In some applications, a Snap Acceleration Test may **not** provide the conditions necessary to reveal a malfunctioning aftertreatment DPF. If there is a heavy buildup of exhaust residue/soot on the exhaust system outlet and a snap acceleration does **not** reveal a condition outlined in the following steps, it may be necessary to perform a brief acceleration run under partial to full load and/or a stall test. [[101-014-008 — Engine Testing (In Chassis)|Refer to Procedure 014-008 in Section 14.]]

Refer to Aftertreatment Diesel Oxidation Catalyst and Aftertreatment Diesel Particulate Filter Reuse Guidelines, Bulletin [[4021600 — Aftertreatment Diesel Oxidation Catalyst (DOC) and Aftertreatment Diesel Particulate|4021600]], for pass or fail guidelines.

![[14d00034.png]]

If gray smoke or faint black smoke is present, refer to Aftertreatment Diesel Oxidation Catalyst and Aftertreatment Diesel Particulate Filter Reuse Guidelines, Bulletin [[4021600 — Aftertreatment Diesel Oxidation Catalyst (DOC) and Aftertreatment Diesel Particulate|4021600]], for pass or fail guidelines.

White smoke during the Snap Acceleration Test does **not** indicate a malfunction. No repair is necessary.

![[11c00247.png]]

Snap Acceleration - Aftertreatment Disconnected

> [!danger] WARNING · Опасно
> The exhaust gas and exhaust components can remain hot after a vehicle has stopped moving. To avoid the risk of fire, property damage, burns, or other serious injury, allow the exhaust system to cool before beginning this procedure or repair and make sure that no combustible materials are located where they are likely to come in contact with hot exhaust gas or exhaust components.

One of the functions of the aftertreatment system is to remove particulates from the exhaust gas. This function prevents the use of black smoke as a diagnostic symptom.

The Snap Acceleration Test (aftertreatment disconnected) is used to check for abnormally high amounts of black smoke in the exhaust gas.

Disconnect the exhaust pipe from the turbocharger turbine outlet.

![[11c00110.png]]

The vehicle transmission **must** be in neutral.

The vehicle parking brake **must** be applied.

It may be necessary to temporarily adjust the maximum engine speed with no VSS parameter in INSITE™ electronic service tool to the high idle speed of the engine.

Start the engine and let it idle.

Quickly depress the accelerator pedal from 0 percent to 100 percent and hold 5 seconds then release. This can be performed multiple times, if necessary.

![[14c00079.png]]

During this test, check for black smoke exiting the turbocharger turbine outlet as the engine is accelerated from low idle to high idle and at high idle.

![[14000010.png]]

A small puff of black smoke upon acceleration that clears at a steady high idle speed is normal.

White smoke during the Snap Acceleration Test does **not** indicate a malfunction. No repair is necessary.

Heavy black smoke indicates other upstream engine issues that need to be diagnosed. Reference the Black Smoke - Excessive troubleshooting symptom tree in Section TS.

![[14000011.png]]

Reconnect the exhaust system.

Inspect the exhaust piping for leaks, cracks, and loose connections.

Tighten the exhaust clamps, if necessary.

Consult the original equipment manufacturer (OEM) specifications for the correct torque specification value.

![[10d00395.png]]

### Finishing Steps

Allow the engine and exhaust system to cool down. Temperatures can maintain an elevated state for several minutes.

Check to make sure the DPF lamp is **not** illuminated.

> [!note] Note · Примечание
> If the DPF lamp is illuminated and Fault Code 2639 or 1921 is still active, a second regeneration will be needed. If the fault is still active after a second regeneration, the filter needs to be cleaned of ash or soot. [[101-011-041-tr — Aftertreatment Diesel Particulate Filter|Refer to Procedure 011-041 in Section 11.]]

Check for any active fault codes. If active fault codes are present, use Section TF for fault code troubleshooting.

Use INSITE™ electronic service tool to clear all inactive fault codes.

![[19803969.png]]
