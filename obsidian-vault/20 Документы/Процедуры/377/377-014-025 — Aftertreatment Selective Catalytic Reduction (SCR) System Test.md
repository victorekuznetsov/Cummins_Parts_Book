---
type: "Процедура"
doc: "377-014-025"
title_en: "Aftertreatment Selective Catalytic Reduction (SCR) System Test"
modified: "2025-09-24"
manuals:
  - "5411181"
figures: 4
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/377/377-014-025.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/377-014-025.pdf"
tags:
  - "документ/процедура"
  - "группа/377"
---

# Aftertreatment Selective Catalytic Reduction (SCR) System Test

> [!abstract] Процедура · `377-014-025`
> **Входит в руководства:** [[5411181 — X15 CM2350 X114B - Efficiency Series Service Manual|5411181]]
> **Секции:** Section 14 - Engine Testing - Group 14
> **Даты:** изменён 2025-09-24
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/377/377-014-025.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/377-014-025.pdf)

### Select Service Tools

#### Recommended Cummins® Service Tools

- Cummins® electronic service tool or equivalent

#### Additional Service Items

- No additional service items required.

### General Information

The Aftertreatment SCR System Test is a diagnostic used to identify malfunctioning aftertreatment SCR system components. The test is located in the recommended Cummins® electronic service tool or equivalent under the diagnostic tests tab.

The SCR system test should **only** be used when directed by a service procedure, fault code troubleshooting tree, or symptom troubleshooting tree.

The test consists of the following subtests.

- Aftertreatment Warm-Up and Diesel Exhaust Fluid (DEF) Dosing System Test
- Aftertreatment SCR Deposit Burn Test
- Aftertreatment Nitrogen Oxides (NOx) Sensor Rationality Test
- Aftertreatment SCR Catalyst Test.

The SCR system test will display the status of each of the subtests in the subtest status window.

![[11t00094.png]]

Aftertreatment SCR System Test Screen

1. Test Instruction Window
2. Monitor Parameter Window
3. Subtest Status Window
4. Main Status Window.

### System Requirements

Check the engine control module (ECM) calibration revision history for calibration updates for this test. If the ECM does not contain that revision or higher, update the calibration. [[105-019-032 — Engine Control Module Calibration Code|Refer to Procedure 019-032 in Section 19.]]

![[19803969.png]]

### Preparatory Steps

> [!danger] WARNING · Опасно
> The test will produce significant engine noise due to the varying engine speeds that will occur during the test process. Do not perform this test in an enclosed environment. Move the equipment to a secluded location. To reduce the possibility of personal injury, hearing protection must be used while conducting this test.

Connect the electronic service tool and check for active fault codes. Troubleshoot any active fault codes prior to performing this test. Do **not** perform the SCR system test with active fault codes, unless guided to do so by the fault code troubleshooting.

Before performing the SCR system test, follow the steps listed below:

1. Perform initial inspection of the aftertreatment system.

- Check for exhaust leaks.

2. Select an appropriate location to park the vehicle.

- The SCR system test is an extremely noisy test
- Move the vehicle to a secluded location, such as a back parking lot
- It is **not** recommended to perform the SCR system test in the shop. If the test **must** be run indoors due to low ambient temperature, be sure the proper exhaust ventilation measures are taken and all personnel in the area are wearing hearing protection
- Perform the test on a reasonably level surface.

3. Park the vehicle securely.

- Set the parking brake. See equipment manufacturer instructions
- Turn engine brakes OFF
- Place the transmission in Park, if equipped; otherwise in Neutral
- Set wheel chocks at the front and rear of at least one tire.

4. Set up a safe area.

- If bystanders might enter the area, set up barriers to keep them at least 1.5 m \[5 ft\] from the front and rear of the vehicle during the SCR system test.
- Make certain that the cab and sleeper are clear of occupants.
- Keep a fire extinguisher nearby.

5. Prepare for engine speed changes during the SCR system test.

- Do **not** operate any power takeoff (PTO) powered devices. Disconnect or disable these devices before starting the SCR system test
- Stay clear of the engine compartment.

6. Start a datalog with the electronic service tool.

- Log all parameters in the data monitor/logger screen.

### Test

> [!note] Note · Примечание
> If the connection between the electronic service tool and the ECM is lost for any reason, a pop-up message will appear. When this occurs, the test will automatically abort. The test can be restarted after cycling the keyswitch OFF for 90 seconds and then back ON.

After each run of the SCR system test, a key cycle is required, allowing the ECM to completely power down before the test can be rerun.

1. Begin the SCR system test.

- Use the electronic service tool to perform the SCR system test
- Engine speed will increase to a specified value and then the ECM will perform the analysis process
- At the conclusion of the test, the engine will return to idle and the SCR system test will display either pass or fail status for all systems tested.

2. Monitor the area.

- Make sure that the vehicle and surrounding area are monitored during the SCR system test. If any unsafe condition occurs, shut the engine OFF immediately.

To stop the SCR system test click the STOP button on the test screen. The SCR system test can also be stopped by engaging the clutch, brake, or throttle pedal; or by turning the engine OFF.

When the test is started, engine speed will vary from 950 revolutions per minute (RPM) up to 1700 RPM during the different stages of the test.

Test progress can be monitored using the subtest status window.

Test results will be displayed as each subtest completes. The test will stop if a subtest makes a decision other than PASS and repair action is required.

> [!note] Note · Примечание
> If a subtest message states, “Test **Not** Available” or “ **Not** Supported”, the subtest is **not** supported for this engine or application. No action is needed.

If the Aftertreatment Selective Catalytic Reduction System Test does **not** pass, reset the search to “Aftertreatment Selective Catalytic Reduction System Test Did **Not** Pass”. **Only** select the solution title that matches the error message in the recommend Cummins® electronic service tool or equivalent.

Re-run the Aftertreatment SCR System Test once the issue is corrected, to validate the repair.

![[11t00096.png]]

Aftertreatment SCR System Test Screen

1. Subtest status - all passed
2. Main status window shows test complete
3. Pop-up message appears when test is complete.

Once the SCR system test is complete, the engine will automatically return to normal idle speed. The SCR system test will display the test results for review until the next key cycle.

After the test has completed, stop the electronic service tool datalog.

![[11t00095.png]]

Aftertreatment SCR System Test Screen

1. The “Stopped, Check Status Window” message will be displayed by the subtest that was running when the abort occurred. All other subtests will retain their current messages until a key cycle.
2. Abort Message in Main Status Window. The most recent message will appear at the bottom.

The SCR system test will **not** complete if:

- Coolant temperature too low after the warmup period
- Accelerator pedal is depressed
- Clutch pedal is depressed
- Brake pedal is depressed
- Parking brake **not** set
- Parking brake incorrectly configured
- Transmission is put into gear
- PTO engaged
- Vehicle speed detected
- Engine brake switch is ON
- Engine protection state active
- A regeneration inhibiting fault becomes active
- High aftertreatment temperature faults become active.

If the Aftertreatment Selective Catalytic Reduction System Test will **not** complete, reset the search to “Aftertreatment Selective Catalytic Reduction System Test Will **Not** Complete”. **Only** select the solution title that matches the error message in the recommend Cummins® electronic service tool or equivalent.

The SCR system test will **not** start if:

- Any of the causes listed for the SCR system test will **not** complete above
- Another diagnostic test is running
- Aftertreatment diesel particulate filter (DPF) regeneration is active
- DEF tank level is low
- Ambient temperature is too low
- Barometric pressure is too low
- DEF system is frozen.

If the Aftertreatment Selective Catalytic Reduction System Test will **not** start, reset the search to “Aftertreatment Selective Catalytic Reduction System Test Will **Not** Start”. **Only** select the solution title that matches the error message in the recommend Cummins® electronic service tool or equivalent.

### Finishing Steps

- Do **not** turn the keyswitch OFF until the test has completed and the results are displayed.
- Check to make sure the CHECK ENGINE lamp and/or malfunction indicator lamp (MIL) lamp are **not** illuminated.
- Check for any active fault codes. If active fault codes are present, follow published troubleshooting.
- Clear all inactive fault codes.
