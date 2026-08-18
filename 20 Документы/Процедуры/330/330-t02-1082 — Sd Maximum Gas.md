---
aliases:
  - "Останов: максимальная подача газа"
type: "Процедура"
doc: "330-t02-1082"
title_en: "Sd Maximum Gas"
title_ru: "Останов: максимальная подача газа"
modified: "2024-08-13"
engines:
  - "33239746"
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
manuals:
  - "4358403"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/330/330-t02-1082.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/330-t02-1082.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/330"
---

# Sd Maximum Gas
**Останов: максимальная подача газа**

> [!abstract] Процедура · `330-t02-1082`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Входит в руководства:** [[4358403 — Dual Fuel Technology DF101 Master Repair Manual|4358403]]
> **Секции:** Section TA - Troubleshooting Alarm Codes
> **Даты:** изменён 2024-08-13
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/330/330-t02-1082.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/330-t02-1082.pdf)

Printable Version

### Symptoms

If the unit is running in dual fuel mode, the system will shut down the flow of gas and all dual fuel operations will cease until the fault is corrected.

### How To Use This Tree

This tree can be used to troubleshoot a malfunction. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.

**Circuit Description**

The system monitors diesel fuel flow and compares to a mapped table within the controller. If the gas system is on and there is a difference between the mapped table and actual diesel fuel flow, a ratio of gas to diesel is calculated based on the difference in reported fuel rate and the convert diesel table. This ratio is monitored to make sure the system does **not** supply more gas/diesel substitution to the engine than Cummins Inc. has defined.

**Conditions for Running the Diagnostics**

Controller is powered ON, system is in ‘Auto' Mode, or system is in ‘Manual' Mode with a start command. Engine is running with loads and conditions suitable to begin gas flow and the ‘GAS OK' lamp is ON.

**Conditions for Activating the Fault Message:**

The ratio of gas to diesel has exceeded the variable set-point “MaxGasProt” for greater than a fixed value of 3 seconds. Set-point is factory default at 75 percent and password level 2 protected.

**Conditions for Clearing the Fault Codes Automatically:**

Clearing the fault codes has to be manually reset.

**Conditions for Clearing the Fault Codes Manually:**

Press “Fault Reset” button on front of controller.

### Shoptalk

Possible causes include:

- Throttle body malfunction

- Throttle body feedback malfunction

- Low fuel rate

**Service Tip:** From the controller display the gas/diesel ratio can be seen from the main screen.

**Service Tip:** Using the software package “Drive Monitor” and using the “Control Window” the same observations can be made.

| Fault Message Sd Maximum Gas |  |  |
|---|---|---|
| Gas/Diesel Ratio Has Exceed Set-point Limit and Measures to Reduce the G/D Ratio are **Not** Reducing the Substitution Level |  |  |
| Codes or Messages | Reason | Effect |
| Sd Maximum Gas | Displaced diesel flow and calculated G/D ratio has exceeded limit set- point (80 percent) for 3.0 seconds. | Dual fuel control system will **not** allow gas operations. Dual fuel controller will stop gas flow. |

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Validate the fault message. |  |
|  | **STEP 1A.** Check for active fault message. | Sd Maximum Gas alarm code is active? |
|  | **STEP 1B.** Check for active fault message. | Alarm Codes other than Sd Maximum Gas active? |
|  | **STEP 1C.** Check the engine ECM for engine fault codes. | Engine ECM indicates fault codes? |
| STEP 2. | Monitor Dual Fuel operation. |  |
|  | **STEP 2A.** Observe and record operating characteristics. | Did the valve feedback follow the command? |
| STEP 3. | Check throttle body circuit. |  |
|  | **STEP 3A.** Check throttle body supply. | Voltage between 20-30 VDC? |
|  | **STEP 3B.** Check throttle body supply. | Voltage between 20-30 VDC? |
|  | **STEP 3C.** Check throttle body supply circuit breaker 2. | Circuit breaker tripped? |
|  | **STEP 3D.** Check throttle body supply. | Voltage between 20-30 VDC? |
| STEP 4. | Check throttle body feedback circuit. |  |
|  | **STEP 4A.** Check throttle body feedback circuit. | Voltage measures 5 VDC? |
|  | **STEP 4B.** Check throttle body supply. | Voltage measures 5 VDC? |
|  | **STEP 4C.** Check reference voltage at DF module. | Voltage measures 5 VDC? |
| STEP 5. | Check throttle position signal circuit. |  |
|  | **STEP 5A.** Check throttle position signal for open circuit. | Resistance greater than 10 ohms? |
|  | **STEP 5B.** Check throttle body feedback circuit for pin to pin short. | Resistance less than 100k ohms? |

### STEP 1. Validate the fault message.

#### STEP 1A. Check for active fault message.

| **Conditions:** Power ON dual fuel control module. Connect InteliMonitor to the dual fuel control panel. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check local display panel or InteliMonitor for fault messages in alarm list and history. | Sd Maximum Gas alarm code is active? **YES** | 1B |
| Sd Maximum Gas alarm code is active? **NO** | Return the pump to service and monitor. |  |

#### STEP 1B. Check for active fault message.

| **Conditions:** Power ON dual fuel control module. Connect InteliMonitor to the dual fuel control panel. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check local display panel or InteliMonitor for fault messages in alarm list and history. | Alarm Codes other than Sd Maximum Gas active? **YES** | Troubleshoot all other error codes prior to troubleshooting Sd Maximum Gas. |
| Alarm Codes other than Sd Maximum Gas active? **NO** | 1C |  |

#### STEP 1C. Check the engine ECM for engine fault codes.

| **Conditions:** Turn keyswitch ON. Connect the recommended Cummins® electronic service tool or equivalent. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Use the recommended Cummins® electronic service tool or equivalent to read the fault code. | Engine ECM indicates fault codes? **YES** | Troubleshoot engine fault codes prior to Troubleshooting Alarm Codes. |
| Engine ECM indicates fault codes? **NO** | 2A |  |

### STEP 2. Monitor Dual Fuel operation.

#### STEP 2A. Observe and record operating characteristics.

| **Conditions:** Power ON dual fuel controller. Verify Dual fuel controller mode is OFF or MANUAL. Operate engine above 400 kw. Connect InteliMonitor to the dual fuel control panel. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Observe and record the following information from values, gas regulation in InteliMonitor. EngPwr MapDiesel GasVlvCommand TB Feedback Place controller in ‘Auto', observe the dual fuel start up sequence and allow stabilization of Load and G/D ratio. This test **must** be performed twice before moving onto the next step. In some cases at lower loads and speeds where the fuel rate is pushed down near the Min Dsl Rate (78 l/hr) the fuelrate can become unstable and even drop sharply which will cause the G/D to then increase sharply. | Did the valve feedback follow the command? **YESRepair:** An error in the fueling table has been identified. Contact a local Cummins® Distributor to recommission the unit. | Repair complete |
| Did the valve feedback follow the command? **NO** | 3A |  |

### STEP 3. Check throttle body circuit.

#### STEP 3A. Check throttle body supply.

| **Conditions:** Power ON dual fuel control module. Disconnect 23 pin connector from Woodward throttle body. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for battery voltage between supply pins of 23 pin Woodward throttle body connector and return pin in same connector. Reference circuit diagrams for proper pin identification. | Voltage between 20-30 VDC? **YES** | 4A |
| Voltage between 20-30 VDC? **NO** | 3B |  |

#### STEP 3B. Check throttle body supply.

| **Conditions:** Power ON dual fuel control module. Disconnect C8 panel connector from dual fuel panel. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for battery voltage between throttle body supply pin of C8 connector and return pin of C8 connector. Reference circuit diagrams for proper pin identification. | Voltage between 20-30 VDC? **YESRepair:** Repair or replace the dual fuel wiring harness. | Repair complete |
| Voltage between 20-30 VDC? **NO** | 3C |  |

#### STEP 3C. Check throttle body supply circuit breaker 2.

| **Conditions:** Power ON dual fuel control module. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Verify throttle body circuit breaker 2 is **not** tripped. | Circuit breaker tripped? **YESRepair:** Reset or replace the circuit breaker. | Repair complete |
| Circuit breaker tripped? **NO** | 3D |  |

#### STEP 3D. Check throttle body supply.

| **Conditions:** Disconnect C2 panel connector from dual fuel panel. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for battery voltage between throttle body supply pins of C2 connector and return pins of C2 connector. Reference circuit diagrams for proper pin identification. | Voltage between 20-30 VDC? **YESRepair:** Repair or replace the dual fuel panel internal wiring harness. | Repair complete |
| Voltage between 20-30 VDC? **NORepair:** Repair or replace the dual fuel panel external power supply wiring harness. | Repair complete |  |

### STEP 4. Check throttle body feedback circuit.

#### STEP 4A. Check throttle body feedback circuit.

| **Conditions:** Power ON dual fuel control module. Disconnect 23 pin connector from Woodward throttle body. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for 5V supply on analog signal and analog return in same connector. Reference circuit diagrams for proper pin identification. | Voltage measures 5 VDC? **YES** | 5A |
| Voltage measures 5 VDC? **NO** | 4B |  |

#### STEP 4B. Check throttle body supply.

| **Conditions:** Power ON dual fuel control module. Disconnect C8 panel connector from dual fuel panel. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for 5V supply on analog signal and analog return in same connector. Reference circuit diagrams for proper pin identification. | Voltage measures 5 VDC? **YESRepair:** Repair or replace the dual fuel wiring harness. | Repair complete |
| Voltage measures 5 VDC? **NO** | 4C |  |

#### STEP 4C. Check reference voltage at DF module

| **Conditions:** Power ON dual fuel control module. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure 5V reference voltage at BF1 connectors of DF Module. | Voltage measures 5 VDC? **YESRepair:** Repair or replace the dual fuel panel internal wiring harness. | Repair complete |
| Voltage measures 5 VDC? **NORepair:** Replace dual fuel module. | Repair complete |  |

### STEP 5. Check throttle position signal circuit.

#### STEP 5A. Check throttle position signal for open circuit.

| **Conditions:** Power OFF dual fuel control module. Disconnect 23 pin connector from Woodward throttle body. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure resistance between throttle position sensor signal pin of 23 pin Woodward throttle body connector and throttle position sensor pin of IBF Module. Reference circuit diagrams for proper pin identification. | Resistance greater than 10 ohms? **YESRepair:** Repair or replace dual fuel wiring harness. | Repair complete |
| Resistance greater than 10 ohms? **NO** | 5B |  |

#### STEP 5B. Check throttle body feedback circuit for pin to pin short.

| **Conditions:** Disconnect 23 pin connector from Woodward throttle body. Disconnect feedback circuit pins from IBF module. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure resistance between throttle position sensor signal pin of 23 pin Woodward throttle body connector and all other pins in that connector. Reference circuit diagrams for proper pin identification. | Resistance less than 100k ohms? **YESRepair:** Repair or replace dual fuel wiring harness. | Repair complete |
| Resistance less than 100k ohms? **NORepair:** Replace Woodward throttle body. Refer to Procedure 005-052 in Section 5. | Repair complete |  |
