---
type: "Процедура"
doc: "377-014-014"
title_en: "Fuel Injector Performance Test"
modified: "2025-09-03"
manuals:
  - "5411181"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/377/377-014-014.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/377-014-014.pdf"
tags:
  - "документ/процедура"
  - "группа/377"
---

# Fuel Injector Performance Test

> [!abstract] Процедура · `377-014-014`
> **Входит в руководства:** [[5411181 — X15 CM2350 X114B - Efficiency Series Service Manual|5411181]]
> **Секции:** Section 14 - Engine Testing - Group 14
> **Даты:** изменён 2025-09-03
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/377/377-014-014.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/377-014-014.pdf)

### Select Service Tools

#### Recommended Cummins® Service Tools

- Cummins® electronic service tool, or equivalent.

#### Additional Service Items

- No additional service items required.

### General Information

The recommended Cummins® electronic service tool or equivalent Fuel Injector Performance Test is a diagnostic test used to identify malfunctioning fuel injectors. When initiated, the test will increase engine RPM to a specified value and then perform a number of engine decelerations. During these engine decelerations, fuel pressure stability is verified, fuel pressure drop is monitored, the fuel injectors are fired, and fuel injector operation is evaluated. At the conclusion of the test, the engine will return to idle and injectors will be identified as either a pass or fail.

Check for active fault codes prior to performing this procedure. If any active fault codes are present, follow the appropriate fault code troubleshooting tree.

### System Requirements

- Recommended Cummins® electronic service tool, or equivalent.
- Check the engine control module (ECM) calibration revision history for calibration updates for this test. If the ECM does not contain that revision or higher, update the calibration. [[105-019-032 — Engine Control Module Calibration Code|Refer to Procedure 019-032 in Section 19.]]

![[19803969.png]]

### Preparatory Steps

> [!danger] WARNING · Опасно
> The test will produce significant engine noise due to the varying engine speeds that will occur during the test process. Do not perform this test in an enclosed environment. Move the equipment to a secluded location. To reduce the possibility of personal injury, hearing protection must be used while conducting this test.

To perform the Fuel Injector Performance Test, connect the electronic service tool and check for active fault codes. Any fault codes related to the fuel system, such as Fault Codes 3727, 559, or 553, injector circuit Fault Codes 322, 323, 324, 325, 331, or 332, or high aftertreatment temperature Fault Codes 3311, or 3312, go to section TF for fault code troubleshooting before proceeding. Do **not** perform the Fuel Injector Performance Test with active fault codes, unless guided to do so by the fault code troubleshooting.

> [!note] Note · Примечание
> The Fuel Injector Performance Test is designed to run on standard Number 2 diesel fuel. Low viscosity fuels such as Number 1 diesel fuel, kerosene, or aviation fuel, will result in erroneous test results. Verify the fuel type being used before running the Fuel Injector Performance Test.

Before performing the Fuel Injector Performance Test, follow the steps listed below:

1. Select an appropriate location to park the vehicle.
2. Park the truck securely.
3. Set up a safe area.
4. Prepare for engine speed changes during the Fuel Injector Performance Test.
5. Prepare the engine for the Fuel Injector Performance Test.

### Test

The Fuel Injector Performance Test can be found under the ECM Diagnostic Test menu in the electronic service tool.

Follow the on-screen prompts to perform the test.

When the test is started, the engine speed will be raised automatically to the required level. Engine speed will reach between 1800 and 2000 RPM.

The engine will then, through the engine controls, operate in a manner to test the fuel injectors. The engine will enter a motoring event. Engine speed will drop to approximately 1000 RPM, then fuel pressure stability is verified, fuel pressure drop is monitored, fuel injectors are fired, and fuel injector operation is evaluated. Engine speed will then return to between 1800 and 2000 RPM and the sequence will repeat. This is normal.

This process may repeat as many as 24 times before the test is complete.

Make sure that the vehicle and surrounding area are monitored during Fuel Injector Performance Test. If any unsafe condition occurs, shut the engine off immediately.

To stop the Fuel Injector Performance Test, click on the STOP button on the recommended Cummins electronic service tool screen. The Fuel Injector Performance Test can also be stopped by engaging the clutch, brake, or throttle pedal; or by turning the engine OFF.

Once the Fuel Injector Performance Test is complete, the engine will automatically return to normal idle speed and suspect fuel injectors will be identified as either pass or fail.

If the Fuel Injector Performance Test will **not** start, reset the search to “Fuel Injector Performance Test Will **Not** Start”. **Only** select the solution title that matches the error message in the recommend Cummins® electronic service tool or equivalent.

Possible causes include:

- Low coolant temperature (below 72°C \[162°F\])
- Fuel system faults are active
- Clutch switch malfunction
- Brake switch malfunction
- Parking brake **not** set
- Parking brake incorrectly configured
- Accelerator pedal malfunction
- Transmission in gear
- Vehicle speed greater than 0 mph
- PTO engaged
- Engine protection
- Aftertreatment regeneration active
- High aftertreatment temperature faults
- Another diagnostic test is running.

> [!note] Note · Примечание
> If the Fuel Injector Performance Test will **not** start due to the parking brake **not** set, review features and parameters in INSITE™ electronic service tool. The Parking Brake Switch is defaulted to Enable. If the parking brake status is **not** transmitted to the ECM, this parameter should be set to Disabled for the Fuel Injector Performance Test to run properly.

If the Fuel Injector Performance Test will **not** complete, reset the search to “Fuel Injector Performance Test Will **Not** Complete”. **Only** select the solution title that matches the error message in the recommend Cummins® electronic service tool or equivalent.

The Fuel Injector Performance Test will **not** complete if:

- Any of the causes listed for the Fuel Injector Performance Test can **not** start above
- A fault becomes active
- Accelerator is depressed
- Clutch pedal is depressed
- Brake pedal is depressed
- Transmission is put into gear
- High fuel system leakage
- Fuel pressure instability
- Self pumping
- Engine speed too low
- Engine speed too high

Pass or Fail Criteria:

> [!note] Note · Примечание
> The Fuel Injector Performance Test is designed to run on standard Number 2 diesel fuel. Low viscosity fuels such as Number 1 diesel fuel, kerosene, or aviation fuel, will result in erroneous test results.

The electronic service tool will display the pass/fail test results on screen.

If one or two individual fuel injectors fail one or more test points of the Fuel Injector Performance Test, replace those fuel injectors. [[377-006-026 — Injector|Refer to Procedure 006-026 in Section 6.]]

If all fuel injectors in a bank (1, 2, and 3 for the front bank or 4, 5, and 6 for the rear bank) show failed on test point 2 and 3 or 3 and 4, use the Cylinder Cutout Test in the electronic service tool to cut out the front bank of fuel injectors. Perform a brief snap throttle and note how the engine accelerates. Enable the front bank of fuel injectors and cut out the rear bank of fuel injectors. Perform a brief snap throttle and note how the engine accelerates.

If the engine accelerates slowly on the same bank indicated by the Fuel Injector Performance Test results, follow your technical escalation process.

If there is no noticeable difference in engine acceleration from bank to bank, replace the fuel injectors in that bank. [[377-006-026 — Injector|Refer to Procedure 006-026 in Section 6.]]

If all the fuel injectors show failed on test point 2 and 3 or 3 and 4, the fuel injector drivers in the ECM are suspect.

Follow your technical escalation process.

### Finishing Steps

- Do **not** turn the key OFF until the test has completed and the results are displayed.
- A copy of the Fuel Injector Performance Test results **must** be printed and returned with the malfunctioning ECM. Do **not** print the screen. Instead, print a copy of the file that is generated by the recommended Cummins® electronic service tool. The file can be found by opening the start menu, then click on computer, then C:, then Intellect, then Fuel Injector Performance Test. The file can be identified by the date and time the test was performed. Open the file and verify the engine serial number (ESN) matches the ESN of the corresponding engine.
- Check to make sure the CHECK ENGINE lamp and/or malfunction indicator lamp (MIL) lamp are **not** illuminated.
- Check for any active fault codes. If active fault codes are present, use Section TF for fault code troubleshooting.
- Use the recommended Cummins® electronic service tool to clear all inactive fault codes.
