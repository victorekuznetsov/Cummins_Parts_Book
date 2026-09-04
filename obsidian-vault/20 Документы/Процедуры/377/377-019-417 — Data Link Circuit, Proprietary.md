---
type: "Процедура"
doc: "377-019-417"
title_en: "Data Link Circuit, Proprietary"
modified: "2025-06-09"
manuals:
  - "5411181"
figures: 7
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/377/377-019-417.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/377-019-417.pdf"
tags:
  - "документ/процедура"
  - "группа/377"
---

# Data Link Circuit, Proprietary

> [!abstract] Процедура · `377-019-417`
> **Входит в руководства:** [[5411181 — X15 CM2350 X114B - Efficiency Series Service Manual|5411181]]
> **Секции:** Section 19 - Electronic Controls - Group 19
> **Даты:** изменён 2025-06-09
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/377/377-019-417.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/377-019-417.pdf)

### Select Service Tools

#### Recommended Cummins® Service Tools

- Multimeter, Part Number 3164488

#### Additional Service Items

- No additional service items required.

### General Information

The proprietary data link circuit is located in the wiring harness and originates from the engine connector of the engine control module (ECM). This is different from the public data link which originates in the original equipment manufacturer (OEM) connector of the ECM.

The purpose of this data link is to allow the ECM to communicate to other data link devices such as the variable geometry turbocharger (VGT) actuator, nitrogen oxides (NOx) sensors, aftertreatment temperature sensor modules, etc.

INSITE™ electronic service tool can communicate with the ECM on the proprietary data link via the 3 pin service data link connector.

![[17c00003.png]]

The proprietary data link incorporates two terminating resistors. One of the terminating resistors is built into the VGT actuator. The other terminating resistor (1) is provided by the OEM and should be located at the end of the backbone (2).

The purpose of the terminating resistors is to minimize reflection of data on the data link.

Reflection of data on the data link can cause messages to become partially or completely lost resulting in intermittent fault codes.

Although the data link can function with a missing or malfunctioning terminating resistor, the terminating resistors **must** be in place to maintain proper communication.

There are several different malfunctions that can influence communication on the proprietary data link. Below is a table of malfunctions and the corresponding effects on communication.

| Malfunction | Effects |
|---|---|
| Open in the Society of Automotive Engineers (SAE) J1939 (+) or SAE J1939 (-) circuit. | Data communication is **not** possible with devices located after the open circuit. Communication with the remaining devices is possible, but can be intermittent. |
| SAE J1939 (+) shorted to battery voltage. | Data communication is **not** possible. |
| SAE J1939 (+) shorted to ground. | Data communication is **not** possible. |
| SAE J1939 (-) shorted to battery voltage. | Data communication is **not** possible. |
| SAE J1939 (-) shorted to ground. | Data communication is possible, but can be intermittent. |
| SAE J1939 (+) shorted to SAE J1939 (-). | Data communication is **not** possible. |
| Loss of terminating resistor or incorrect terminating resistance. | Data communication is possible, but can be intermittent. |

![[19802397.png]]

### Resistance Check

Measurement

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To avoid personal injury, always ventilate the compartment before servicing the batteries. To avoid arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

Disconnect the batteries. See equipment manufacturer service information.

Measure the resistance between the SAE J1939 data link (+) pin and the SAE J1939 data link (-) pin at the 3-pin service data link connector.

| Resistance | Possible Cause |
|---|---|
| 54 to 66 ohms | Terminating resistance is correct. |
| 108 to 132 ohms | One of the terminating resistors is missing. One of the terminating resistors is open or there can be an open between the terminating resistors in the proprietary data link circuit. |
| 36 to 44 ohms | Three terminating resistors have been installed in the harness. One **must** be removed. There **must** be one terminating resistor at each end of the backbone. |
| 0 to 5 ohms | There is a short between the SAE J1939 (+) and SAE J1939 (-) in the proprietary data link circuit. |
| Greater than 1000 ohms | There can be an open between the 3 pin service data link connector and the backbone or both terminating resistors are missing or open. |
| Any other readings | Incorrect terminating resistor resistance. Poor or corroded connections, short circuit to ground, or an open in the proprietary data link. |

To pinpoint the cause of the incorrect terminating resistance, isolate it by systematically disconnecting connections on the data link until the resistance reads within the acceptable limits.

![[19c01212.png]]

Engine Harness Check

To isolate the engine side of the proprietary SAE J1939 data link, disconnect the 14 pin OEM crossover connector and measure the resistance between the SAE J1939 data link (+) pin and the SAE J1939 data link (-) pin at the 3 pin service data link connector.

If the resistance is **not** between 108 to 132 ohms, a malfunction has been detected in the engine side of the proprietary SAE J1939 data link.

![[17c00003.png]]

Disconnect the aftertreatment intake NOx sensor and measure the resistance between the SAE J1939 data link (+) pin and the SAE J1939 data link (-) pin at the 3 pin service data link connector to determine if the aftertreatment intake NOx sensor is the cause of the malfunction.

If the resistance is between 108 to 132 ohms with the aftertreatment intake NOx sensor disconnected, a malfunctioning aftertreatment intake NOx sensor has been connected.

Replace the aftertreatment intake NOx sensor. [[377-019-463 — Aftertreatment Intake NOx Sensor|Refer to Procedure 019-463 in Section 19.]]

If the resistance is **not** between 108 to 132 ohms after disconnecting the aftertreatment intake NOx sensor, then disconnect the VGT actuator from the engine harness and measure the resistance between the SAE J1939 data link (+) pin and the SAE J1939 data link (-) pin of the VGT actuator.

If the resistance of the VGT actuator is **not** between 108 to 132 ohms, a malfunctioning VGT actuator has been detected. Replace the VGT actuator. [[377-010-134 — Variable Geometry Turbocharger Actuator, Electric|Refer to Procedure 010-134 in Section 10.]]

If the resistance of the VGT actuator is between 108 to 132 ohms, a malfunction has been detected in the engine harness. Repair or replace the engine harness. Refer to Procedure 019-043 in Section 19.

OEM Harness Check

To isolate the aftertreatment side of the proprietary SAE J1939 data link, measure the resistance between the SAE J1939 data link (+) pin and the SAE J1939 data link (-) pin on the OEM side of the 14 pin crossover connector.

If the resistance is **not** between 108 to 132 ohms, a malfunction has been detected in the aftertreatment side of the proprietary SAE J1939 data link.

![[17c00003.png]]

To isolate the aftertreatment side of the proprietary SAE J1939 data link, disconnect the following devices from the data link one at a time while measuring the resistance between the SAE J1939 data link (+) pin and the SAE J1939 data link (-) pin on the OEM side of the 14 pin crossover connector.

- Aftertreatment outlet NOx sensor
- Aftertreatment diesel particulate filter (DPF) temperature sensor module
- Aftertreatment selective catalytic reduction (SCR) temperature sensor Module
- Aftertreatment intermediate ammonia (NH3) sensor, if equipped
- Aftertreatment particulate sensor, if equipped
- Data link aftertreatment diesel exhaust fluid (DEF) tank sensors (level, temperature, quality), if equipped.

If the resistance reads between 108 to 132 ohms after disconnecting a data link device, a malfunction has been detected in that data link device. Replace the malfunctioning device.

If the resistance is **not** between 108 to 132 ohms after disconnecting all of the data link devices, the malfunction is located in the wiring.

Troubleshoot the DPF aftertreatment interface harness and the SCR aftertreatment interface harness for opens and short circuits. Replace the aftertreatment interface harnesses, as necessary. Refer to Procedure 019-477 in Section 19.

If the aftertreatment interface harnesses do **not** have any opens or short circuits, the malfunction remains in the OEM wiring or OEM installed terminating resistor. Repair or replace the OEM wiring harness. See equipment manufacturer service information.

### Short Circuit Check

Voltage Checking

Connect the batteries. See equipment manufacturer service information.

[[377-014-034 — J1939 Data Link Diagnostic Tool|Refer to Procedure 014-034 in Section 14.]]

Turn the keyswitch ON.

Measure the voltage between the SAE J1939 data link (+) pin at the 3 pin service data link connector and battery ground.

Measure the voltage between the SAE J1939 data link (-) pin at the 3 pin service data link connector and battery ground.

| Minimum | Normal | Maximum |
|---|---|---|
| 1.0 VDC | 2.5 VDC | 4.5 VDC |

If the voltage reading is less than 1.0 VDC, then the SAE J1939 data link is shorted to ground.

If the voltage reading is greater than 4.5 VDC, then the SAE J1939 data link is shorted to a voltage source.

To pinpoint the short, isolate it by systematically disconnecting connections on the data link until voltage reads within the acceptable limits.

![[19c01270.png]]

Isolate

If the short circuit was detected on the SAE J1939 data link (+) circuit, perform the checks while measuring the voltage between the SAE J1939 data link (+) pin and battery ground.

If the short circuit was detected on the SAE J1939 data link (-) circuit, perform the checks while measuring the voltage between the SAE J1939 data link (-) pin and battery ground.

Disconnect the following devices one at a time while measuring the voltage at the 3 pin service data link connector.

- VGT actuator
- Aftertreatment intake NOx sensor
- Aftertreatment outlet NOx sensor
- Aftertreatment DPF temperature sensor module
- Aftertreatment SCR temperature sensor module
- Aftertreatment intermediate NH3 sensor, if equipped
- Aftertreatment particulate sensor, if equipped
- Data link aftertreatment DEF tank sensors (level, temperature, quality), if equipped.

If the voltage reads between 1.0 to 4.5 volts after disconnecting a data link device, a malfunction has been detected in that data link device. Replace the malfunctioning device.

![[17c00003.png]]

If the voltage is **not** between 1.0 to 4.5 volts after disconnecting all of the data link devices, the malfunction is located in the wiring.

Disconnect the 14 pin OEM crossover connector while measuring the voltage at the 3 pin service connector.

If the voltage is **not** between 1.0 to 4.5 volts after disconnecting the 14 pin OEM crossover connector, a short circuit has been detected in the engine harness. Repair or replace the engine harness. Refer to Procedure 019-043 in Section 19.

If the voltage is between 1.0 to 4.5 volts after disconnecting the 14 pin OEM crossover connector, a short circuit has been detected in the aftertreatment side of the proprietary SAE J1939 data link circuit.

Troubleshoot the DPF aftertreatment interface harness and the SCR aftertreatment interface harness for short circuits. Replace the aftertreatment interface harnesses, as necessary. Refer to Procedure 019-477 in Section 19.

If the aftertreatment interface harnesses do **not** have any short circuits, the short circuit has been detected in the OEM wiring. Repair or replace the OEM wiring harness. See equipment manufacturer service information.

| Data Link Devices Source Addresses |  |
|---|---|
| Device | Source Address |
| Engine Control Module | 0 |
| Variable Geometry Turbocharger Actuator, Electric | 2 |
| Aftertreatment Intake NOx Sensor | 81 |
| Aftertreatment Outlet NOx Sensor | 82 |
| Aftertreatment Particulate Matter Sensor | 129 or 190 |
| Aftertreatment Exhaust Gas Temperature Sensor | 208, 209, 210, or 211 |
| Aftertreatment Diesel Exhaust Fluid Quality Sensor | 163 |
