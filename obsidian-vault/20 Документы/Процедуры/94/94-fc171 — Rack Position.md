---
aliases:
  - "Положение рейки"
type: "Процедура"
doc: "94-fc171"
title_en: "Rack Position"
title_ru: "Положение рейки"
modified: "2003-03-19"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666184"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/94/94-fc171.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/94-fc171.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/94"
---

# Rack Position
**Положение рейки**

> [!abstract] Процедура · `94-fc171`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual|3666184]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2003-03-19
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/94/94-fc171.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/94-fc171.pdf)

### Fault Code: 171

### Rack Position

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 171 PID(P): SPN: FMI: Lamp: SRT: | Fuel pump rack position fault. One or both of the left bank or right bank fuel pump racks is **not** at the commanded position. | Performance could be sluggish or slow to respond. Common Warning output is energized. |

![[19a00011.png]]

### Circuit Description

The rack position sensor circuit's measured, reference and common signals are used by the electronic control module (ECM) to verify that the rack has been properly positioned by the rack actuator. The actuator power supply and PWM return circuits are used by the ECM to drive the actuator to the desired position.

### Component Location

The rack position sensor is located in the governor housing of the fuel pump. The QST30 G-Drive engine has one on each engine bank.

### Shoptalk

- Fault Code 171 will be recorded if the measured rack position for either bank is **not** at commanded rack position. First determine which bank is causing the error, then determine what part of that circuit is at fault.

- Fault Code 171 may be recorded if the fuel pump rack is sticking at one particular point within its travel path. You may need to load the engine to make the fault go active.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Determine which bank is at fault. |  |
|  | **STEP 1A.** Perform fuel pump rack test. | The measured voltage matches the service tool voltage reading (±0.2 VDC) |
|  | **STEP 1A-1.** Monitor the rack position voltages while the engine is in operation. | Voltage reading at pins B and C are identical (±0.2 VDC) |
| STEP 2. | Check engine harness. |  |
|  | **STEP 2A.** Inspect engine harness adaptor cable and ECM connector pins. | No damaged pins |
|  | **STEP 2A-1.** Inspect engine harness and fuel pump connector pins. | No damaged pins |
|  | **STEP 2A-2.** Inspect engine harness connector and any engine harness extension cable used. | No damaged pins |
|  | **STEP 2B.** Check rack position sensor and rack actuator circuits for short circuit from pin to pin. | More than 100k ohms |
|  | **STEP 2B-1.** Check for a short circuit from pin to pin in the engine harness adaptor cable and any engine harness extension cable used. | More than 100k ohms |
|  | **STEP 2C.** Check rack position sensor and rack actuator circuits for an open circuit. | Less than 10 ohms |
|  | **STEP 2C-1.** Check for an open circuit in the engine harness adaptor cable and any engine harness extension cable used. | Less than 10 ohms |
|  | **STEP 2D.** Check rack position sensor and rack actuator circuits for short circuit to ground. | More than 100k ohms |
|  | **STEP 2D-1.** Check for short circuit to ground in the engine harness. | More than 100k ohms |
| STEP 3. | Check rack actuator. |  |
|  | **STEP 3A.** Check the resistance of rack actuator coil. | 0.55 to 0.90 ohms |
|  | **STEP 3B.** Verify rack movement. | Full range of rack movement |
| STEP 4. | Check rack position sensor. |  |
|  | **STEP 4A.** Check resistance of rack position sensor coil. | 17 to 23 ohms |
|  | **STEP 4B.** Check resistance of rack position sensor reference coil. | 17 to 23 ohms |
| STEP 5. | Check ECM. |  |
|  | **STEP 5A.** Check rack position sensor signal pins for proper voltage levels. | 2.4 to 2.6 VDC |
| STEP 6. | Clear the fault code. |  |
|  | **STEP 6A.** Disable the fault code. | Fault Code 171 inactive |
|  | **STEP 6B.** Clear inactive fault codes. | All faults cleared |

### STEP 1. Determine which bank is at fault.

#### STEP 1A. Perform fuel pump rack test.

| **Conditions:** Stop/Run switch in the "STOP" position. Controller in the diagnostic mode. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Using INSITE™, Part No. 3825145, perform fuel pump rack test. Gradually ramp the fuel pump rack from it's lower limit of travel (0 mm) to it's maximum limit of travel (20 mm) while reading the voltage from pin B to pin A at the diagnostic connector for the left bank fuel pump. Gradually ramp the fuel pump rack from it's lower limit of travel (0 mm) to it's maximum limit of travel (20 mm) while reading the voltage from pin C to pin A at the diagnostic connector for the right bank fuel pump. | The measured voltage matches the rack position voltages as indicated by the service tool (±0.2 VDC) | 1A-1 |
| Proceed with the following steps (Step 2A) for the engine bank in error. | 2A |  |

#### STEP 1A-1. Monitor the rack position voltages while the engine is in operation.

| **Conditions:** Stop/Run switch in the "RUN" position. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Read the voltages at the diagnostic connector pins B (left bank fuel pump) to pin A (ground) and pin C (right bank fuel pump) to pin A (ground) at various levels of engine load. | Voltage readings between pins A and B are identical (±0.2 VDC) at a given load condition and both voltage reading fluctuate with varying load (fueling) conditions. | 6A |
|  | 2A |  |

### STEP 2. Check engine harness.

#### STEP 2A. Inspect engine harness adaptor cable and ECM connector pins.

| **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness adaptor cable from the ECM. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| bent or broken pins pushed back or expanded pins corroded pins moisture in or on the connector. | No damaged pins | 2A-1 |
| **Repair the damaged pins** Repair or replace the engine harness adaptor cable or the ECM, whichever has the damaged pins. Repair the engine harness adaptor cable. Refer to Procedure 019-240 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Replace the engine harness adaptor cable. Refer to Procedure 019-043 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Replace the ECM. Refer to OEM procedures. Dry the connector by using electrical contact cleaner, Part No. 3824510. | 6A |  |

#### STEP 2A-1. Inspect engine harness and fuel pump connector pins.

| **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness connector from the fuel pump. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| bent or broken pins pushed back or expanded pins corroded pins moisture in or on the connector. | No damaged pins | 2A-2 |
| **Repair the damaged pins** Repair or replace the engine harness or the fuel pump whichever has the damaged pins. Repair the engine harness. Refer to Procedure 019-209 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Replace the engine harness. Refer to Procedure 019-043 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Replace the fuel pump. Refer to Base Engine Troubleshooting and Repair Manual. Dry the connector by using electrical contact cleaner, Part No. 3824510. | 6A |  |

#### STEP 2A-2. Inspect engine harness connector and any engine harness extension cable used.

| **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness connector from the engine harness extension cable(s). |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| bent or broken pins pushed back or expanded pins corroded pins moisture in or on the connector. | No damaged pins | 2B |
| **Repair the damaged pins** Repair or replace the engine harness or the engine harness extension cable(s), whichever has the damaged pins. Repair the engine harness or the engine harness extension cable(s). Refer to Procedure 019-209 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Replace the engine harness or the engine harness extension cable(s). Refer to Procedure 019-043 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Dry the connector by using electrical contact cleaner, Part No. 3824510. | 6A |  |

#### STEP 2B. Check rack position sensor and rack actuator circuits for short circuit from pin to pin.

| **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness adaptor cable from the ECM. Disconnect the engine harness connector from the fuel pump. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from pin 5 (pin 10 for the right fuel pump) of the engine harness adaptor cable connector to all other pins in the connector. Measure the resistance from pin 3 (pin 4 for the right fuel pump) of the engine harness adaptor cable connector to all other pins in the connector. Measure the resistance from pin 6 (pin 9 for the right fuel pump) of the engine harness adaptor cable connector to all other pins in the connector. Measure the resistance from pin 7 (pin 8 for the right fuel pump) of the engine harness adaptor cable connector to all other pins in the connector. Measure the resistance from pin 1 (pin 2 for the right fuel pump) of the engine harness adaptor cable connector to all other pins in the connector. | More than 100k ohms | 2C |
|  | 2B-1 |  |

#### STEP 2B-1. Check for a short circuit from pin to pin in the engine harness adaptor cable and any engine harness extension cable used.

| **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness from the engine harness extension cable(s). Disconnect the engine harness adaptor cable from the ECM. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from pin 5 (pin 10 for the right fuel pump) of the engine harness adaptor cable connector and any engine harness extension cable connector to all other pins in the connector. Measure the resistance from pin 3 (pin 4 for the right fuel pump) of the engine harness adaptor cable connector and any engine harness extension cable connector to all other pins in the connector. Measure the resistance from pin 6 (pin 9 for the right fuel pump) of the engine harness adaptor cable connector and any engine harness extension cable connector to all other pins in the connector. Measure the resistance from pin 7 (pin 8 for the right fuel pump) of the engine harness adaptor cable connector and any engine harness extension cable connector to all other pins in the connector. Measure the resistance from pin 1 (pin 2 for the right fuel pump) of the engine harness adaptor cable connector and any engine harness extension cable connector to all other pins in the connector. | More than 100k ohms Repair or replace the engine harness Repair the engine harness. Refer to Procedure 019-209 or 019-240 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Replace the engine harness. Refer to Procedure 019-043 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 6A |
| **Repair or replace the engine harness adaptor cable or engine harness extension cable(s), whichever is found faulty** Repair the engine harness adaptor cable or engine harness extension cable(s). Refer to Procedure 019-209 or 019-240 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Replace the engine harness adaptor cable or engine harness extension cable(s). Refer to Procedure 019-043 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 6A |  |

#### STEP 2C. Check rack position sensor and rack actuator circuits for an open circuit.

| **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness connector from the fuel pump. Disconnect the engine harness adaptor cable from the ECM. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from pin 5 (pin 10 for the right bank fuel pump) on the engine harness adaptor cable connector to pin E on the harness side of the fuel pump connector. Measure the resistance from pin 3 (pin 4 for the right bank fuel pump) on the engine harness adaptor cable connector to pin G on the harness side of the fuel pump connector. Measure the resistance from pin 6 (pin 9 for the right bank fuel pump) on the engine harness adaptor cable connector to pin F on the harness side of the fuel pump connector. Measure the resistance from pin 7 (pin 8 for the right bank fuel pump) on the engine harness adaptor cable connector to pin A on the harness side of the fuel pump connector. Measure the resistance from pin 1 (pin 2 for the right bank fuel pump) on the engine harness adaptor cable connector to pin B on the harness side of the fuel pump connector. | Less than 10 ohms | 2D |
|  | 2C-1 |  |

#### STEP 2C-1. Check for an open circuit in the engine harness adaptor cable and any engine harness extension cable used.

| **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness connector from the engine harness extension cable(s). Disconnect the engine harness adaptor cable from the ECM. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the continuity for pin 5 (pin 10 for the right bank fuel pump) on the engine harness adaptor cable and any engine harness extension cables used. Measure the continuity for pin 3 (pin 4 for the right bank fuel pump) on the engine harness adaptor cable and any engine harness extension cables used. Measure the continuity for pin 6 (pin 9 for the right bank fuel pump) on the engine harness adaptor cable and any engine harness extension cables used. Measure the continuity for pin 7 (pin 8 for the right bank fuel pump) on the engine harness adaptor cable and any engine harness extension cables used. Measure the continuity for pin 1 (pin 2 for the right bank fuel pump) on the engine harness adaptor cable and any engine harness extension cables used. | Less than 10 ohms Repair or replace the engine harness Repair the engine harness. Refer to Procedure 019-209 or 019-240 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Replace the engine harness. Refer to Procedure 019-043 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 6A |
| **Repair or replace the engine harness adaptor cable or engine harness extension cable(s), whichever is found faulty** Repair the engine harness adaptor cable or engine harness extension cable(s). Refer to Procedure 019-209 or 019-240 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Replace the engine harness adaptor cable or engine harness extension cable(s). Refer to Procedure 019-043 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 6A |  |

#### STEP 2D. Check rack position sensor and rack actuator circuits for short circuit to ground.

| **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness adaptor cable from the ECM. Disconnect the engine harness connector from the fuel pump. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from pin 5 (pin 10 for the right bank fuel pump) on the engine harness adaptor cable to engine block ground. Measure the resistance from pin 3 (pin 4 for the right bank fuel pump) on the engine harness adaptor cable to engine block ground. Measure the resistance from pin 6 (pin 9 for the right bank fuel pump) on the engine harness adaptor cable to engine block ground. Measure the resistance from pin 7 (pin 8 for the right bank fuel pump) on the engine harness adaptor cable to engine block ground. Measure the resistance from pin 1 (pin 2 for the right bank fuel pump) on the engine harness adaptor cable to engine block ground. | Greater than 100k ohms | 3A |
|  | 2D-1 |  |

#### STEP 2D-1. Check for short circuit to ground in the engine harness.

| **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness connector from the engine harness extension cable(s). Disconnect the engine harness connector from the fuel pump. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from pin 5 (pin 10 for the right bank fuel pump) on the engine harness connector to engine block ground. Measure the resistance from pin 3 (pin 4 for the right bank fuel pump) on the engine harness connector to engine block ground. Measure the resistance from pin 6 (pin 9 for the right bank fuel pump) on the engine harness connector to engine block ground. Measure the resistance from pin 7 (pin 8 for the right bank fuel pump) on the engine harness connector to engine block ground. Measure the resistance from pin 1 (pin 2 for the right bank fuel pump) on the engine harness connector to engine block ground. | Greater than 100k ohms | 3A |
| **Repair or replace the engine harness** Repair the engine harness. Refer to Procedure 019-209 or 019-240 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Replace the engine harness. Refer to Procedure 019-043 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 6A |  |

### STEP 3. Check rack actuator.

#### STEP 3A. Check the resistance of the rack actuator coil.

| **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness connector from the fuel pump. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from pin B to pin G of the fuel pump connector. | Less than 10 ohms | 3B |
| **Replace the fuel pump** Refer to Base Engine Troubleshooting and Repair Manual. | 6A |  |

#### STEP 3B. Verify rack movement

| **Conditions:** Stop/Run switch in the "STOP” position. Controller in the diagnostic mode. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Using INSITE™, Part No. 3825145, perform a rack movement test. Insert upper and lower limits of fuel pump rack positions. Remove the cap on the front of the fuel pump and verify rack movement. **Note:** If the cap on the fuel pump is **not** accessible for visual verification of rack movement, proceed with steps 4 and 5 prior to removing the fuel pump. | Full range of rack movement | 4A |
| **Replace the fuel pump** Refer to Base Engine Troubleshooting and Repair Manual. | 6A |  |

### STEP 4. Check rack position sensor.

#### STEP 4A. Check resistance of rack position sensor coil.

| **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness connector from the fuel pump. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from pin E to pin F of the fuel pump connector. | 17 to 23 ohms | 4B |
| **Replace the fuel pump** Refer to Base Engine Troubleshooting and Repair Manual. | 6A |  |

#### STEP 4B. Check resistance of rack position sensor reference coil.

| **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness connector from the fuel pump. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from pin A to pin F of the fuel pump connector. | 17 to 23 ohms | 5A |
| **Replace the fuel pump** Refer to Base Engine Troubleshooting and Repair Manual. | 6A |  |

### STEP 5. Check ECM

#### STEP 5A. Check rack position sensor signal pins for proper voltage.

| **Conditions:** Stop/Run switch in the "STOP" position. Controller in the diagnostic mode. Disconnect engine harness from fuel pump. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the signal voltage from pin A on the harness side of the fuel pump connector to ground. Measure the signal voltage from pin E on the harness side of the fuel pump connector to ground. Measure the signal voltage from pin F on the harness side of the fuel pump connector to ground. | 2.4 to 2.6 VDC | 6A |
| **Replace the ECM** Refer to OEM procedures. | 6A |  |

### STEP 6. Clear the fault code.

#### STEP 6A. Disable the fault code.

| **Conditions:** Connect all components. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| connect all components start the engine and let it idle for one minute verify Fault Code 171 is inactive. | Fault Code 171 inactive | 6B |
| Return to troubleshooting steps or contact your local Cummins Authorized Repair Location if all steps have been completed and checked again. | 1A |  |

#### STEP 6B. Clear the inactive fault codes.

| **Conditions:** Connect all components. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Erase the inactive fault codes using INSITE™, Part No. 3825145. **NOTE:** The datalink connector is located on the right bank of the flywheel housing. | All faults cleared | Repair complete |
| **Troubleshoot any remaining active fault codes.** | Appropriate troubleshooting chart |  |
