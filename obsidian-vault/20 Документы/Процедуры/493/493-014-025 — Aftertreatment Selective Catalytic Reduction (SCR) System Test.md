---
type: "Процедура"
doc: "493-014-025"
title_en: "Aftertreatment Selective Catalytic Reduction (SCR) System Test"
modified: "2020-08-07"
manuals:
  - "5411181"
figures: 4
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/493/493-014-025.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/493-014-025.pdf"
tags:
  - "документ/процедура"
  - "группа/493"
---

# Aftertreatment Selective Catalytic Reduction (SCR) System Test

> [!abstract] Процедура · `493-014-025`
> **Входит в руководства:** [[5411181 — X15 CM2350 X114B - Efficiency Series Service Manual|5411181]]
> **Секции:** Section 14 - Engine Testing - Group 14
> **Даты:** изменён 2020-08-07
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/493/493-014-025.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/493-014-025.pdf)

### Select Service Tools

#### Recommended Cummins® Service Tools

- Cummins® electronic service tool or equivalent

#### Additional Service Items

- No additional service items required.

### General Information

The Aftertreatment Selective Catalytic Reduction System Test is a diagnostic used to identify malfunctioning aftertreatment SCR system components. The test is located in the recommended Cummins® electronic service tool or equivalent under the diagnostic tests tab.

The test consists of the following subtests.

- Aftertreatment Warm-Up and Diesel Exhaust Fluid (DEF) Dosing System Test
- Aftertreatment SCR Deposit Burn Test
- Aftertreatment Nitrogen Oxides (NOx) Sensor Rationality Test
- Aftertreatment SCR Catalyst Test.

The SCR system test will display the status of each of the subtests in the subtest status window.

The SCR system test will take approximately 60 to 80 minutes to complete.

![[11t00094.png]]

Aftertreatment SCR System Test Screen

1. Test Instruction Window
2. Monitor Parameter Window
3. Subtest Status Window
4. Main Status Window.

### System Requirements

Check the engine control module (ECM) calibration revision history for calibration updates for this test. If the ECM does not contain that revision or higher, update the calibration. [[105-019-032 — Engine Control Module Calibration Code|Refer to Procedure 019-032 in Section 19.]]

The SCR system test should **only** be used when directed by a service procedure, fault code troubleshooting tree, symptom troubleshooting tree, or expert diagnostic system (EDS).

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

> [!note] Note · Примечание
> After each run of the SCR system test, a key cycle is required, allowing the ECM to completely power down (90 seconds) before the test can be rerun.

1. Begin the SCR system test.

- Use the electronic service tool to perform the SCR system test
- Engine speed will increase to a specified value and then the ECM will perform the analysis process
- At the conclusion of the test, the engine will return to idle and the SCR system test will display either pass or fail status for all systems tested.

2. Monitor the area.

- Make sure that the vehicle and surrounding area are monitored during the SCR system test. If any unsafe condition occurs, shut the engine OFF immediately.

To stop the SCR system test click the STOP button on the test screen. The SCR system test can also be stopped by engaging the clutch, brake, or throttle pedal; or by turning the engine OFF.

When the test is started, engine speed will vary from 950 revolutions per minute (rpm) up to 1700 rpm during the different stages of the test.

Test progress can be monitored using the subtest status window.

Test results will be displayed as each subtest completes. The test will stop if a subtest makes a decision other than PASS and repair action is required.

Once the SCR system test is complete, the engine will automatically return to normal idle speed. The SCR system test will display the test results for review until the next key cycle.

After the test has completed stop the electronic service tool datalog.

For information on repair action based on subtest results, see the analyzing the Data section of this procedure. Record the subtest results for later reference.

The SCR system test will **not** start if:

- Another diagnostic test is running
- Aftertreatment diesel particulate filter (DPF) regeneration is active
- DEF tank level is low
- Ambient temperature is too low
- Barometric pressure is too low
- DEF system is frozen.

The SCR system test will **not** start or will be aborted if:

- Coolant temperature too low after the warmup period
- Accelerator pedal is depressed
- Clutch pedal is depressed
- Brake pedal is depressed
- Parking brake **not** set
- Transmission is put into gear
- PTO engaged
- Vehicle speed detected
- Engine brake switch is ON
- Engine protection state active
- A regeneration inhibiting fault becomes active
- High aftertreatment temperature faults become active.

If the SCR system test aborts or will **not** activate, a message will be displayed. Correct the issue identified before proceeding. For more information on abort messages and associated repair action, see the Troubleshooting section of this procedure.

### Troubleshooting

General Information

This section is used to assist troubleshooting abort messages from the Main Status Window.

**Eletronic Service Tool**

![[11t00095.png]]

1. The “Stopped, Check Status Window” message will be displayed by the subtest that was running when the abort occurred. All other subtests will retain their current messages until a key cycle.
2. Abort Message in Main Status Window. The most recent message will appear at the bottom.

Some messages were modified between electronic service tool version 8.1.1 and electronic service tool version 8.1.2 and later. Use the appropriate table below for the version of electronic service tool being used.

INSITE™ 8.1.1 Status Messages

| Main Status Message | Action |
|---|---|
| The test has stopped. | None |
| The test is running. | None |
| The number of allowed attempts for this key cycle has been reached. Key OFF, allow the ECM to completely power down, key ON, and restart the test. | Cycle the keyswitch and restart the test. |
| The ECM has detected a condition in which it will not allow the Aftertreatment SCR System test to run. | The ECM is prohibiting the test from running. Follow the appropriate technical escalation process. |
| The test has completed. Please cycle the keyswitch and restart the engine to restart the test. | If all the subtests have passed, the test is complete. If a subtest has failed, see the subtest message in the “Analyzing the Data” section in this procedure. |
| The test has stopped or could not start because the parking brake is not engaged. Exit the test, correct the issue and restart the test. | Verify that the parking brake is set. See equipment manufacturer service information. Review features and parameters using the electronic service tool. The parking brake switch is defaulted to Enable. If the parking brake status is not transmitted to the ECM this parameter should be set to Disabled for the SCR System Test to run properly. Check the parking brake switch and circuit. |
| The test has stopped or could not start because the accelerator pedal or throttle position is greater than zero. Be sure the accelerator pedal or throttle is released and restart the test. | Verify the engine brake is OFF. Check for foot pedal restriction. Check the accelerator pedal or lever position sensor and circuit. Refer to Procedure 019-085 in Section 19. |
| The test has stopped or could not start because the transmission is in gear or a command on the data link is preventing the test. Place the transmission in Park or Neutral and restart the test. | Verify that the transmission is in Park, if applicable, otherwise in Neutral. See equipment manufacturer service information. |
| The test has stopped or could not start because the Power Take Off (PTO) or Remote PTO is engaged. Disengage the PTO or Remote PTO and restart the test. | Verify the PTO is disengaged. Check the Cruise Control/PTO selector switch and circuit. Refer to Procedure 019-021 in Section 19. Refer to Procedure 019-022 in Section 19. |
| The test has stopped or could not start because the original equipment manufacturer (OEM) sensor ambient conditions are out of range. Check the OEM ambient sensor values and be sure they are in normal operating range, cycle the keyswitch, and restart the test. | The status of one or both of the nitrogen oxides (NOx) sensors is continuously invalid. Check for active NOx sensor fault codes. Be sure the NOx sensors are reaching initializing temperature, above 200°C \[392°F\]. Use the electronic service tool to monitor exhaust gas temperature. Restart the test. If the error message persists, follow the appropriate technical escalation process. |
| The test has stopped or could not start because the vehicle is moving or a vehicle speed sensor fault code is active. Stop the vehicle, verify no vehicle speed sensor fault codes are active, cycle the keyswitch, and restart the test. | Be sure the vehicle is not moving and is properly secured. Troubleshoot any active vehicle speed sensor faults. Check that the vehicle speed sensor is not loose. Check the vehicle speed sensor for poor grounding or electrical interference. |
| The test has stopped or could not start because a command on the data link is preventing the test. Check all the devices on the data link, troubleshoot any active fault codes, cycle the keyswitch, and restart the test. | The anti-lock braking system (ABS) module is sending a data link message to disable the engine brake. This message is causing the ECM to abort the test. Be sure the engine brake is turned OFF. Troubleshoot any fault codes from the ABS module. |
| The test has stopped or could not start because of an EGR or turbocharger issue. Troubleshoot any active fault codes, cycle the keyswitch, and restart the test. | Troubleshoot any active turbocharger or exhaust gas recirculation (EGR) fault codes. |
| The test has stopped or could not start because the current engine operating state is hindering the test. Determine the engine state, correct any issues, cycle the keyswitch, and restart the test. | Another component or feature is taking control of engine speed. Check that OEM or customer-selected inhibit features are not active. Check that programmable parameters or selected features are correct. Refer to Procedure 019-078 in Section 19. Also refer to the service bulletin Multiplexing Troubleshooting, Bulletin 4021378. Check that the vehicle speed sensor is not loose Check the vehicle speed sensor for poor grounding or electrical interference. |
| The test has stopped or could not start because an Engine Protection derate is active. Troubleshoot any active fault codes, cycle the keyswitch, and restart the test. | Troubleshoot active fault codes. |
| The test has stopped or could not start because the clutch or service brake is depressed. Release the clutch or service brake pedal and restart the test. | Check the clutch switch adjustment, switch, and circuit. Refer to Procedure 019-009 in Section 19. Refer to Procedure 019-010 in Section 19. Check the vehicle brake switch and the circuit. Refer to Procedure 019-088 in Section 19. Refer to Procedure 019-089 in Section 19. |
| The test has stopped or could not start because the engine coolant temperature is too low. Continue to run the engine to raise the coolant temperature, cycle the keyswitch, and restart the test. | The coolant temperature warm-up period has timed out. Cycle the keyswitch and restart the test. |
| The test has stopped because the exhaust volumetric flow rate is out of range. | The ECM detected the exhaust flow rate estimate is out of range. Troubleshoot active engine fault codes. Perform the following checks in the Engine Performance Troubleshooting Tree in Section TT. Step 6 - EGR system checks. Step 5 - Air handling checks. |
| The test has stopped because the barometric air pressure or OEM ambient air temperature is low. | Move the vehicle to a warmer location or lower altitude. |
| The aftertreatment DPF regeneration has timed out. Cycle the keyswitch and select Start to restart the test. | Cycle the keyswitch and restart the test. |
| The ECM has detected a fault condition. Check for active faults, troubleshoot fault codes, key OFF, allow the ECM to completely power down, key ON, and restart the test. | An active fault code is preventing the test from running. Troubleshoot active fault codes. |
| The test has stopped because the test engine speed is out of the expected range. | This message indicates engine speed was higher or lower than the commanded value. If engine speed is low: Troubleshoot the engine for low power or the inability to reach rated speed. See Section TT. If engine speed is high: Troubleshoot the engine for surges at low or high idle or surges under load. See Section TT. |
| The test has stopped because the DPF outlet temperature is out of the expected range. | This message indicates the DPF outlet temperature is above the maximum or below the minimum temperature during the test. If DPF outlet temperature is too high a fault code will be set. Troubleshoot the active fault code. If DPF outlet temperature is too low: Refer to the “Stationary Regeneration - Will Not Complete” symptom tree found in Section TS of this manual. Do not refer to the “Stationary Regeneration - Will Not Activate” TS tree. All the conditions/malfunctions in the “Stationary Regeneration - Will Not Activate” TS tree have specific messages in this test. |
| The test has stopped or could not start because the DEF tank level is low. Fill the tank to the proper level and restart the test. | Fill the DEF tank. |
| The test could not start because the DEF in the tank may be frozen or is too cold to dose. Raise the tank temperature prior to restarting the test. | Troubleshoot any active faults or malfunctioning DEF system heating components. Allow the DEF system to thaw. |
| The test has stopped because the NOx levels could not be modulated. | Another component or feature is taking control of engine speed and preventing the test from modulating NOx to the desired level. Check that OEM or customer-selected inhibit features are not active. Check that programmable parameters or selected features are correct. Refer to Procedure 019-078 in Section 19. Also refer to the service bulletin Multiplexing Troubleshooting, Bulletin 4021378. Check that the vehicle speed sensor is not loose. Check the vehicle speed sensor for poor grounding or electrical interference. |

INSITE™ 8.1.2 and Later Status Messages

| Main Status Message | Action |
|---|---|
| The test has stopped. | None |
| The test is running. | None |
| Test did not start because a key cycle is needed. Key cycle and restart test. | Cycle the keyswitch and restart the test. |
| The ECM has detected a condition in which it will not allow the Aftertreatment SCR System test to run. | The ECM is prohibiting the test from running. Follow the appropriate technical escalation process. |
| The test has completed. Please cycle the keyswitch and restart the engine to restart the test. | If all the subtests have passed, the test is complete. If a subtest has failed, refer to the subtest message in the “Analyzing the Data” section in this procedure. |
| The test has stopped or could not start because the parking brake is not engaged. Exit the test, correct the issue and restart the test. | Verify that the parking brake is set. See equipment manufacturer service information. Review features and parameters using the electronic service tool. The parking brake switch is defaulted to Enable. If the parking brake status is not transmitted to the ECM, this parameter should be set to Disabled for the SCR system test to run properly. Check the parking brake switch and circuit. |
| The test has stopped or could not start because the accelerator pedal or throttle position is greater than zero. Correct the issue, key OFF, allow the ECM to completely power down, key ON, and restart the test. | Verify the engine brake is OFF. Check for foot pedal restriction. Check the accelerator pedal or lever position sensor and circuit. Refer to Procedure 019-085 in Section 19. |
| The test has stopped or could not start because the Transmission is in gear or a command on the data link is preventing the test. Correct the issue, key OFF, allow the ECM to completely power down, key ON, and restart the test. | Verify that the transmission is in Park, if applicable, otherwise in Neutral. See equipment manufacturer service information. |
| The test has stopped or could not start because the (PTO) or Remote PTO is engaged. Correct the issue, key OFF, allow the ECM to completely power down, key ON, and restart the test. | Verify the PTO is disengaged. Check the Cruise Control/PTO selector switch and circuit. Refer to Procedure 019-021 in Section 19. Refer to Procedure 019-022 in Section 19. |
| The status of one or both of the NOx sensors is continuously invalid. Correct the issue, key OFF, allow the ECM to completely power down, key ON, and restart the test. | The status of one or both of the NOx sensors is continuously invalid. Check for active NOx sensor fault codes. Be sure the NOx sensors are reaching initializing temperature, above 200°C \[392°F\]. Use the electronic service tool to monitor exhaust gas temperature. Restart the test. If the error message persists, follow the appropriate technical escalation process. |
| The test has stopped or could not start because the vehicle is moving or a vehicle speed sensor fault code is active. Correct the issue, key off, allow the ECM to completely power down, key ON, and restart the test. | Be sure the vehicle is not moving and is properly secured. Troubleshoot any active vehicle speed sensor faults. Check that the vehicle speed sensor is not loose. Check the vehicle speed sensor for poor grounding or electrical interference. |
| The test has stopped or could not start because an engine brake disable request was received on the data link. Correct the issue, key OFF, allow the ECM to completely power down, key ON, and restart the test. | The ABS module is sending a data link message to disable the engine brake. This message is causing the ECM to abort the test. Be sure the engine brake is turned OFF. Troubleshoot any fault codes from the ABS module. |
| The test has stopped or could not start because of an EGR or turbocharger issue. Correct the issue, key OFF, allow the ECM to completely power down, key ON, and restart the test. | Troubleshoot any active turbocharger or EGR fault codes. |
| The test has stopped or could not start because another feature is controlling the engine speed. Correct the issue, key OFF, allow the ECM to completely power down, key ON, and restart the test. | Another component or feature is taking control of engine speed. Check that OEM or customer-selected inhibit features are not active. Check that programmable parameters or selected features are correct. Refer to Procedure 019-078 in Section 19. Also refer to the service bulletin Multiplexing Troubleshooting, Bulletin 4021378. Check that the vehicle speed sensor is not loose. Check the vehicle speed sensor for poor grounding or electrical interference. |
| The test has stopped or could not start because an Engine Protection derate is active. Correct the issue, key OFF, allow the ECM to completely power down, key ON, and restart the test. | Troubleshoot active fault codes. |
| The test has stopped or could not start because the clutch or service brake is depressed. Correct the issue, key OFF, allow the ECM to completely power down, key ON, and restart the test. | Check the clutch switch adjustment, switch, and circuit. Refer to Procedure 019-009 in Section 19. Refer to Procedure 019-010 in Section 19. Check the vehicle brake switch and the circuit. Refer to Procedure 019-088 in Section 19. Refer to Procedure 019-089 in Section 19. |
| The test has stopped or could not start because the engine coolant temperature is too low. Key OFF, allow the ECM to completely power down, key ON, and restart the test. | The coolant temperature warm-up period has timed out. Cycle the keyswitch and restart the test. |
| The test has stopped because the exhaust flow rate is out of range. Correct the issue, key OFF, allow the ECM to completely power down, key ON, and restart the test. | The ECM detected the exhaust flow rate estimate is out of range. Troubleshoot active engine fault codes. Perform the following checks in the Engine Performance Troubleshooting Tree. See Section TT. Step 6 - EGR system checks. Step 5 - Air handling checks. |
| The test has stopped because the barometric air pressure or ambient air temperature is low. Correct the issue, key OFF, allow the ECM to completely power down, key ON, and restart the test. | Move the vehicle to a warmer location or lower altitude. |
| The aftertreatment DPF regeneration has timed out. Key OFF, allow the ECM to completely power down, key ON, and restart the test. | Cycle the key, Restart the test. |
| The ECM has detected a fault condition. Correct the issue, key OFF, allow the ECM to completely power down, key ON, and restart the test. | An active fault code is preventing the test from running. Troubleshoot active fault codes. |
| The test has stopped because engine speed is out of the desired range. Correct the issue, key OFF, allow the ECM to completely power down, key ON, and restart the test. | This message indicates engine speed was higher or lower than the commanded value. If engine speed is low: Troubleshoot the engine for low power or the inability to reach rated speed. See Section TT. If engine speed is high: Troubleshoot the engine for surges at low or high idle or surges under load. See Section TT. |
| The test has stopped because the DPF outlet temperature is out of the desired range. Correct the issue, key OFF, allow the ECM to completely power down, key ON, and restart the test. | This message indicates the DPF outlet temperature is above the maximum or below the minimum temperature during the test. If DPF outlet temperature is too high, a fault code will be set. Troubleshoot the active fault code. If DPF outlet temperature is too low: See the “Stationary Regeneration - Will Not Complete” symptom tree found in section TS of this manual. Do not reference the “Stationary Regeneration - Will Not Activate” TS tree. All the conditions/malfunctions in the “Stationary Regeneration - Will Not Activate” TS tree have specific messages in this test. |
| DEF tank level is too low. Fill tank with DEF, cycle key and restart test | Fill the DEF tank. |
| The test could not start because the DEF in the tank may be frozen or is too cold to dose. Correct the issue, key OFF, allow the ECM to completely power down, key ON, and restart the test. | Troubleshoot any active faults or malfunctioning DEF system heating components. Allow the DEF system to thaw. |
| The test has stopped because the engine out NOx levels could not be modulated to the desired range. Correct the issue, key OFF, allow the ECM to completely power down, key ON, and restart the test. | Another component or feature is taking control of engine speed and preventing the test from modulating NOx to the desired level. Check that OEM or customer-selected inhibit features are not active. Check that programmable parameters or selected features are correct. Refer to Procedure 019-078 in Section 19. Also refer to the service bulletin Multiplexing Troubleshooting, Bulletin 4021378. Check that the vehicle speed sensor is not loose. Check the vehicle speed sensor for poor grounding or electrical interference. |

### Analyzing the Data

General Information

![[11t00096.png]]

Aftertreatment SCR System Test Screen

1. Subtest status - all passed
2. Main status window shows test complete
3. Pop-up message appears when test is complete.

Aftertreatment Warm Up and DEF Dosing System Test

| Subtest Status Message | Action |
|---|---|
| Test Not Available | None, this subtest is **not** available for this engine or application. |
| Stopped, Check Status Window | The test has aborted. Follow instruction from main test status window. |
| Not Started | None, this portion of the test is **not** currently running. |
| Warmup in Progress | None |
| DEF Doser Test Running | None |
| Passed | None, the test will automatically continue to the next subtest. |
| Failed | Check the DEF for proper concentration and for contamination. Perform the DEF Dosing Unit Override Test. Refer to Procedure 011-063 in Section 11. If the DEF system passes the Dosing Unit Override Test perform the following: Inspect the DEF dosing unit intake fitting for debris. Refer to Procedure 011-058 in Section 11. If debris is found in the intake fitting, replace the fitting and perform the DEF dosing unit airless flush. Refer to Procedure 011-058 in Section 11. Also drain and flush the DEF tank and intake line. See equipment manufacturer service information. If debris is not found in the intake fitting replace the DEF dosing unit. Refer to Procedure 011-058 in Section 11. Re-run the Aftertreatment SCR System Test once the issue is corrected, to validate the repair. |

Aftertreatment SCR Deposit Burn Test

| Subtest Status Message | Action |
|---|---|
| Test Not Available | None, this subtest is **not** available for this engine or application. |
| Stopped, Check Status Window | The test has aborted. Follow instruction from main test status window. |
| Not Started | None, this portion of the test is **not** currently running. |
| Running | None |
| Deposit Burn Complete | None |
| Deposit Burn Failed | None, the test will continue to run. No repair or inspection will be required unless the Aftertreatment NOx Sensor Rationality Subtest fails. |

Aftertreatment NOx Sensor Rationality Test

| Subtest Status Message | Action |
|---|---|
| Test Not Available | None, this subtest is **not** available for this engine or application. |
| Stopped, Check Status Window | The test has aborted. Follow instruction from main test status window. |
| Not Started | None, this portion of the test is **not** currently running. |
| Running | None |
| Outlet NOx Sensor Passed | Both NOx sensors have passed. Test will automatically continue to the next subtest. |
| Intake NOx Sensor Failed | Replace the aftertreatment intake NOx sensor. Re-run the Aftertreatment SCR System Test, once the issue is corrected, to validate the repair. |
| Inspect Outlet NOx Sensor | Check the decomposition tube for DEF deposits. Run the DEF System Leak Test. Monitor the DEF dosing valve nozzle for leaks. Refer to Procedure 011-080 in Section 11. If no DEF deposits are present and the DEF dosing valve is not leaking, replace the outlet NOx sensor. Re-run the Aftertreatment SCR System Test once the issue is corrected, to validate the repair. |
| Inspect Both NOx Sensors | Check the decomposition tube for DEF deposits. Run the DEF system leak test. Monitor the DEF dosing valve nozzle for leaks. Refer to Procedure 011-080 in Section 11. If no DEF deposits are present and the DEF dosing valve is not leaking, replace both NOx sensors. Re-run the Aftertreatment SCR System Test once the issue is corrected, to validate the repair. |

Aftertreatment SCR Catalyst Test

| Subtest Status Message | Action |
|---|---|
| Not Supported | None, this subtest is **not** supported for this engine or application. |
| Stopped, Check Status Window | The test has aborted. Follow instruction from main test status window. |
| Not Started | None, this portion of the test is **not** currently running. |
| Running | None |
| Passed | None |
| Failed | Replace the aftertreatment SCR catalyst. Re-run the Aftertreatment SCR System Test once the issue is corrected, to validate the repair. |

### Finishing Steps

- Do **not** turn the keyswitch OFF until the test has completed and the results are displayed.
- Check to make sure the CHECK ENGINE lamp and/or malfunction indicator lamp (MIL) lamp are **not** illuminated.
- Check for any active fault codes. If active fault codes are present, use EDS or Section TF for fault code troubleshooting.
- Clear all inactive fault codes.
