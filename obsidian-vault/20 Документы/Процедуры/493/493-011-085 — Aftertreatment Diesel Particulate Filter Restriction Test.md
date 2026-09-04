---
type: "Процедура"
doc: "493-011-085"
title_en: "Aftertreatment Diesel Particulate Filter Restriction Test"
modified: "2022-03-10"
manuals:
  - "5411181"
figures: 6
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/493/493-011-085.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/493-011-085.pdf"
tags:
  - "документ/процедура"
  - "группа/493"
---

# Aftertreatment Diesel Particulate Filter Restriction Test

> [!abstract] Процедура · `493-011-085`
> **Входит в руководства:** [[5411181 — X15 CM2350 X114B - Efficiency Series Service Manual|5411181]]
> **Секции:** Section 11 - Exhaust System - Group 11
> **Даты:** изменён 2022-03-10
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/493/493-011-085.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/493-011-085.pdf)

### Select Service Tools

#### Recommended Cummins® Service Tool

- Cummins® electronic service tool or equivalent

#### Additional Service Items

- No additional service items required.

### General Information

The Aftertreatment Diesel Particulate Filter Restriction Test can be used to evaluate the aftertreatment diesel particulate filter (DPF) (1) restriction, without requiring the use of specialized equipment. The test can be used during troubleshooting for aftertreatment system related fault codes, to determine if an aftertreatment DPF needs to be serviced.

Soot accumulation in the aftertreatment DPF is a normal function of engine operation. However, the accumulation of excessive soot can cause frequent aftertreatment regenerations and is normally caused by fuel system or air handling system issues.

Ash accumulation is the result of non-combustible products collecting in the aftertreatment DPF. Excessive ash accumulation in the aftertreatment DPF can be caused by lubricating oil consumption, coolant consumption, contaminated fuel, and other issues.

Foreign material in the aftertreatment DPF is **not** normal and can be caused by issues such as degraded exhaust system components, exhaust leaks, or damage to engine or other components.

> [!note] Note · Примечание
> Check for active fault codes prior to performing the Aftertreatment Diesel Particulate Filter Restriction Test. If active fault codes are present, reference the appropriate troubleshooting before completing this test, unless you are directed to perform this test in a troubleshooting tree.

> [!note] Note · Примечание
> The Aftertreatment Diesel Particulate Filter Restriction Test **must** be performed immediately after the successful completion of an aftertreatment DPF regeneration, except where noted in this procedure. The aftertreatment DPF regeneration is performed using the recommended Cummins® electronic service tool or equivalent.

Performing the aftertreatment DPF regeneration makes sure that any exhaust residue or soot is removed from the aftertreatment DPF, resulting in a restriction measurement that is attributable to ash content, except where foreign material has entered the aftertreatment DPF. Performing the aftertreatment DPF regeneration also makes sure that the aftertreatment DPF temperature is raised to a level that provides maximum exhaust gas flow rate during the restriction test, and that any moisture present has also been removed.

![[11l00059.png]]

**Single Module Aftertreatment System**

![[11l00059.png]]

**Multi-Module Aftertreatment System**

![[11v00122.png]]

### Preparatory Steps

Exhaust Outlet Inspection

Inspect the exhaust system outlet.

Inspection of the exhaust system outlet can aid in determining the condition of the aftertreatment DPF. The exhaust system outlet should appear clean with little to no exhaust residue or soot buildup.

> [!note] Note · Примечание
> Some accumulation of exhaust residue or soot is normal, and does **not** indicate an issue with the aftertreatment DPF.

A heavy buildup of exhaust residue or soot accumulation on the exhaust system outlet is the result of an issue with the aftertreatment DPF. Perform the Snap Acceleration Test - Aftertreatment Connected. Refer to Procedure 014-017 in Section 14.

![[14d00033.png]]

Snap Acceleration - Aftertreatment Connected

If gray smoke or faint black smoke is present, refer to the Aftertreatment Diesel Oxidation Catalyst and Aftertreatment Diesel Particulate Filter Reuse Guidelines, Bulletin 4021600, and inspect the aftertreatment DPF for damage. White smoke during the Snap Acceleration Test - Aftertreatment Connected may **not** indicate a malfunction. No additional troubleshooting or repair is necessary at this time.

![[11c00247.png]]

If black or gray smoke is **not** found at the exhaust system outlet, proceed to the Sensor Signal Voltage Test in this section.

![[11o00085.png]]

Sensor Signal Voltage Test

Use the Initial Check section of the following procedure to complete the Sensor Signal Voltage Test. Refer to Procedure 019-443 in Section 19.

Stationary (Parked) Regeneration

Verify that the following conditions have been met:

1. The vehicle is parked in an appropriate location, on a surface that will **not** burn or melt under high temperatures (such as clean concrete or gravel, **not** grass or asphalt) and away from anything that can burn, melt, or explode.
2. The vehicle is parked securely.
3. Set up a safe exhaust area.
4. Check the exhaust system surfaces.
5. Prepare for engine speed changes during regeneration.
6. Make sure that the vehicle and surrounding areas are monitored during regeneration. If any unsafe condition occurs, be prepared to shut the engine OFF immediately.

Start the engine and bring it to operating temperature (above 70°C \[158°F\]).

Allow the engine to idle.

Connect the electronic service tool.

Open Trip Information in the electronic service tool and record the number of complete regenerations and the number of incomplete regenerations. Exit Trip Information.

> [!danger] WARNING · Опасно
> The exhaust and exhaust components can become heated during troubleshooting. To avoid the risk of fire, property damage, burns, or other serious personal injury, allow the exhaust system to cool before beginning any procedure or repair and make sure that no combustible materials are located where they are likely to come in contact with hot exhaust or exhaust components.

Perform the aftertreatment DPF regeneration using the electronic service tool.

> [!note] Note · Примечание
> The Aftertreatment Diesel Particulate Filter Regeneration Test can be found under the ECM Diagnostic Test menu in the electronic service tool.

> [!note] Note · Примечание
> Engine speed will increase and the turbocharger can whistle loudly during the Aftertreatment Diesel Particulate Filter Regeneration Test.

To stop the Aftertreatment Diesel Particulate Filter Regeneration Test, engage the clutch, service brake, accelerator pedal; or shut the engine OFF.

Once regeneration is complete, exhaust gas and exhaust surface temperatures will remain elevated for 3 to 5 minutes.

Open Trip Information in the electronic service tool and compare the number of complete regenerations and the number of incomplete regenerations to the numbers recorded earlier. Verify the number of complete regenerations has increased by one before moving on in this procedure. If the number of complete regenerations has **not** increased by one, perform published troubleshooting for Stationary Regeneration - Will **Not** Complete.

Exit Trip Information.

### Setup

Select the Aftertreatment Diesel Particulate Filter Restriction Test under the ECM Diagnostic Test menu in the electronic service tool.

### Test

Follow the on-screen prompts to perform the test.

Select the appropriate Diesel Particulate Filter Condition and select Start.

The Aftertreatment Diesel Particulate Filter Restriction Test will **not** run if more than 1 hour of engine control module (ECM) run time has elapsed since the last aftertreatment DPF regeneration. Check the Aftertreatment History in Advanced ECM data using the electronic service tool. If the last aftertreatment DPF regeneration occurred more than 1 hour from the current ECM run time, or if the aftertreatment DPF regeneration was unsuccessful, exit this test and perform an aftertreatment DPF regeneration. Refer to Procedure 014-016 in Section 14. Once a successful aftertreatment DPF regeneration has completed, return to this procedure.

Running this test multiple times will result in soot accumulation that will affect the test results. If the Aftertreatment Diesel Particulate Filter Restriction Test **must** be run more than three times, perform a stationary regeneration before obtaining the fourth result.

When the test is started, the engine speed will be raised automatically to the required level. Engine speed will reach between 1800 and 2000 rpm.

The engine will then, through the engine controls, operate in a manner to test the aftertreatment DPF restriction.

Once the Aftertreatment Diesel Particulate Filter Restriction Test is complete, the engine will automatically return to normal idle speed.

> [!note] Note · Примечание
> If the Aftertreatment Diesel Particulate Filter Restriction Test will **not** initiate, a message will be displayed. The identified issue will need to be corrected before continuing.

> [!note] Note · Примечание
> If the Aftertreatment Diesel Particulate Filter Restriction Test aborts, a message will be displayed. The identified issue will need to be corrected before continuing or restarting Aftertreatment Diesel Particulate Filter Restriction Test.

The Aftertreatment Diesel Particulate Filter Restriction Test will take 5 minutes to complete. At any time, the Aftertreatment Diesel Particulate Filter Restriction Test can be aborted by clicking on the STOP button in the electronic service tool.

The Aftertreatment Diesel Particulate Filter Restriction Test will also be aborted if:

- A fault code becomes active
- Accelerator pedal is depressed
- Clutch pedal is depressed
- Brake pedal is depressed
- Transmission is put into gear
- Coolant temperature drops below a specified threshold.

If the electronic service tool Aftertreatment Diesel Particulate Filter Restriction Test will **not** activate, a message will be displayed. Correct the issue identified before proceeding. See published troubleshooting for Aftertreatment Diesel Particulate Filter Restriction Test - Will **Not** Activate.

Possible causes include:

- Low coolant temperature
- Clutch switch malfunction
- Brake switch malfunction
- Parking brake **not** set
- Accelerator pedal malfunction
- Transmission in gear
- Vehicle speed greater than 0 mph
- PTO engaged
- Engine protection state active
- Aftertreatment regeneration active
- High aftertreatment temperature faults code(s) become active
- Another diagnostic test is running.

> [!note] Note · Примечание
> If the Aftertreatment Diesel Particulate Filter Restriction Test will **not** initiate due to the parking brake **not** being set, review features and parameters in the electronic service tool. The parking brake switch is defaulted to Enable. If the parking brake status is **not** transmitted to the ECM, this parameter should be set to Disabled for the Aftertreatment Diesel Particulate Filter Restriction Test to run properly.

If the Aftertreatment Diesel Particulate Filter Restriction Test is aborted for any reason, the electronic service tool will display a message describing why the test was aborted. Correct the issue identified before proceeding. See published troubleshooting for Aftertreatment Diesel Particulate Filter Restriction Test - Will **Not** Complete.

Any of the causes listed above for the Aftertreatment Diesel Particulate Filter Restriction Test can **not** initiate above.

- A fault code becomes active.
- Accelerator pedal is depressed.
- Clutch pedal is depressed.
- Brake pedal is depressed.
- Transmission is put into gear.
- High aftertreatment temperature fault code(s) become active.
- Engine speed too low.
- Engine speed too high.

### Finishing Steps

Check for any active fault codes. If any active fault codes are present, reference the appropriate fault code troubleshooting symptom tree in Section TS.

Clear all inactive fault codes.

Perform an Aftertreatment Maintenance Reset All and Aftertreatment Filter Installation procedure **only** if the aftertreatment DPF was serviced.

> [!note] Note · Примечание
> The Aftertreatment Maintenance Reset All and Aftertreatment Filter Installation procedure can be found in the electronic service tool in the Advanced ECM Data section, under Aftertreatment Maintenance.

> [!note] Note · Примечание
> If the aftertreatment diesel particulate filter required servicing for excessive ash and had **not** reached the normal ash cleaning interval, further troubleshooting is required. Reference the Ash Cleaning - Excessive troubleshooting symptom tree, if necessary

Open the electronic service tool, but do **not** connect to the ECM.

Go to Tools \> Options \> Units of Measure.

In the drop down menu in the Units of Measure menu, reset the value to its original setting. Select the Apply button and then select the OK button.

Close the electronic service tool Options menu.
