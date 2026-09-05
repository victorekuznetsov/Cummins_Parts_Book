---
type: "Процедура"
doc: "377-014-028"
title_en: "Engine Compression and Air Handling System Test"
modified: "2025-09-05"
manuals:
  - "5411181"
figures: 3
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/377/377-014-028.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/377-014-028.pdf"
tags:
  - "документ/процедура"
  - "группа/377"
---

# Engine Compression and Air Handling System Test

> [!abstract] Процедура · `377-014-028`
> **Входит в руководства:** [[5411181 — X15 CM2350 X114B - Efficiency Series Service Manual|5411181]]
> **Секции:** Section 14 - Engine Testing - Group 14
> **Даты:** изменён 2025-09-05
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/377/377-014-028.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/377-014-028.pdf)

### Select Service Tools

#### Recommended Cummins® Service Tools

- Cummins® electronic service tool or equivalent, version 9.1.0.74 or later

#### Additional Service Items

- Personal computer (PC) with Windows™ 7, or later, software

### General Information

The Engine Compression and Air Handling System Test is used to identify relative engine compression issues for two or less cylinders and/or malfunctioning air handling system components. The test is located in the electronic service tool under the engine control module (ECM) Diagnostic Tests tab. The average length of the Engine Compression and Air Handling System Test is 15 seconds.

The Engine Compression and Air Handling System Test consists of the following subtests:

- Exhaust manifold pressure at key ON
- Intake manifold pressure at key ON
- Relative Engine Compression Test.

The Engine Compression and Air Handling System Test will display the status of each of the subtests in the subtest status window. Reference Figure 1 below.

![[19903816.png]]

Figure 1

1. Test Instruction Window
2. Monitor Parameter Window
3. Subtest Status Window
4. Main Status Window.

### System Requirements

The Engine Compression and Air Handling System Test requires:

- Personal computer (PC) with Windows™ 7, or later, software
- Cummins® electronic service tool, version 9.1.0.74, or later
- An ECM calibration release date April 2025 or later.
- Check the engine control module (ECM) calibration revision history for calibration updates for this test. If the ECM does **not** contain that revision or higher, update the calibration. [[105-019-032 — Engine Control Module Calibration Code|Refer to Procedure 019-032 in Section 19.]]

![[19803969.png]]

### Preparatory Steps

Connect the electronic service tool and check for active fault codes. Troubleshoot any active fault codes prior to performing this test.

Do **not** perform the Engine Compression and Air Handling System Test with active fault codes, unless guided to do so by a service procedure and/or published troubleshooting.

Prior to performing the Engine Compression and Air Handling System Test, complete the following steps.

1. Park the vehicle securely.
2. Perform a visual inspection of the air handling and exhaust system. [[377-010-024-tr — Air Leaks, Air Intake and Exhaust Systems|Refer to Procedure 010-024 in Section 10.]]

### Test

To perform the Engine Compression and Air Handling System Test, complete the following steps.

- Begin the Engine Compression and Air Handling System Test.
- Use the electronic service tool to initiate the Engine Compression and Air Handling System Test.
- Follow the on-screen instructions.
- Monitor the area.
- Verify the vehicle and surrounding area are monitored during the Engine Compression and Air Handling System Test. If any unsafe condition occurs, stop cranking immediately.
- At the conclusion of the Engine Compression and Air Handling System Test, the electronic service tool will display either pass or fail status for all the subtests.
- Turn the keyswitch to the OFF position.

> [!note] Note · Примечание
> INLINE™ 7 data link adapter tool **must** use 2 pin Delphi™ or 3 pin Deutsch™ adapter (with battery clips).

Once the start button has been pressed in the electronic service tool, engine fueling will be disabled and the engine will be in cranking mode **only**. A 90 second keyswitch cycle will be required to enable engine fueling.

Do **not** start to crank the engine until the screen instructions direct to do so.

Do **not** stop cranking the engine until the screen instructions direct to do so.

Turning the key to the OFF position will cause the test to stop.

A single long cranking event will be required to complete the diagnostic tests.

Test progress can be monitored using the subtest status window.

Test results will be displayed as each subtest completes.

The test will stop if a subtest makes a decision other than PASS and repair action is required.

If the Engine Compression and Air Handling System Test does **not** pass, reset the search to “Engine Compression and Air Handling System Test Did **Not** Pass”. **Only** select the solution title that matches the error message in the recommend Cummins® electronic service tool or equivalent.

> [!note] Note · Примечание
> If the connection between the electronic service tool and the ECM is lost for any reason, a pop-up message will appear. When this occurs, the Engine Compression and Air Handling System Test will automatically abort. The Engine Compression and Air Handling System Test can be restarted after cycling the keyswitch OFF for 90 seconds and then back ON.

![[00g00144.png]]

Figure 2

Figure 2 shows the Status window that will display the abort message.

The Engine Compression and Air Handling System Test will **not** start or will **not** complete if:

- Another diagnostic test is running
- A fault becomes active
- Battery voltage is low during cranking event
- Ambient temperature too low
- Coolant temperature too low
- Cranking speed higher or lower than normal
- Cranking event takes longer than expected
- Operator does **not** crank when test commands to begin cranking
- Brake pedal is depressedParking brake **not** set
- Parking brake incorrectly configured
- Transmission is put into gearPower takeoff (PTO) engaged
- Engine brake switch is ON
- Starter Lockout feature is active
- Original equipment manufacturer (OEM) starter overcrank protection is active.

> [!note] Note · Примечание
> If a starter with overcrank protection is installed on the engine, it may be necessary to use a remote starter switch to complete the test.

If the Engine Compression and Air Handling System Test will **not** start, reset the search to “Engine Compression and Air Handling System Test Will **Not** Start”. **Only** select the solution title that matches the error message in the recommend Cummins® electronic service tool or equivalent.

If the Engine Compression and Air Handling System Test will **not** complete, reset the search to “Engine Compression and Air Handling System Test Will **Not** Complete”. **Only** select the solution title that matches the error message in the recommend Cummins® electronic service tool or equivalent.

### Finishing Steps

Do **not** turn the keyswitch OFF until the test has completed and the results are displayed.

- Turn the keyswitch to the OFF position and allow the ECM to completely power down.
- Check for any active fault codes. If active fault codes are present, follow published troubleshooting.
- Clear all inactive fault codes.
