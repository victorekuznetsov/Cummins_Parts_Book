---
type: "Процедура"
doc: "97-fc469int"
title_en: "Vehicle Cab (Bunk) Temperature or Thermostat Circuit - Data Erratic, Intermittent or Incorrect"
modified: "2004-10-04"
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
  - "3666415"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-fc469int.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-fc469int.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "двигатель/QSX15"
  - "группа/97"
---

# Vehicle Cab (Bunk) Temperature or Thermostat Circuit - Data Erratic, Intermittent or Incorrect

> [!abstract] Процедура · `97-fc469int`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSM11, QSX15
> **Входит в руководства:** [[3666415 — ICON Idle Control System Master Repair Manual|3666415]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2004-10-04
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-fc469int.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-fc469int.pdf)

### Fault Code: 469 (Integrated)

### Vehicle Cab (Bunk) Temperature or Thermostat Circuit - Data Erratic, Intermittent or Incorrect

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 469 PID(P): S215 SPN: FMI: 2/2 Lamp: None SRT: | Vehicle Cab (Bunk) Temperature or Thermostat Circuit - Data Erratic, Intermittent or Incorrect. The ICON™ cab thermostat has logged a fault (E3 on the cab thermostat), or the cab thermostat signal to the electronic control module (ECM) is lost. | E3 will cycle the engine between 20 minutes run and 15 minutes off or until the desired set-point is reached. (This is a selectable response of the E3 fault in the thermostat trim settings.) The ICON™ system will **not** be disabled. Engine mode will remain active. |

![[19803218.png]]

### Circuit Description

The cab thermostat is used to control the cab temperature, either for heating or cooling. It is required for cab comfort mode operation. The thermostat communicates with the ECM to command when to autostart the engine to maintain cab temperature. Also, the thermostat is connected to the keyswitch to detect when the ignition is turned on.

### Component Location

The cab thermostat is mounted in the bunk area, on the wall above the bed.

### Shoptalk

E3 is an indication that one of the following has occurred

- Engine has run for more than 60 minutes, and cool or heat set point is **not** achieved, and external ambient temperature is within -18° to 43°C \[0 to 110°F\] (thermostat-adjustable trim 01 and 02, see thermostat trim settings in Section F

- A cab thermostat request to start the engine has been requested four times in 1 hour, and the ambient temperature is within -18° to 43°C \[0 to 110°F\].

E3 can indicate potential tampering of the thermostat. For example, the operator has chosen cool mode but turned the heater on or opened the windows. The air-conditioning system will attempt to cool the truck below the cool set point for 60 minutes. At this time, an E3 fault (Fault Code 469) will be logged. A similar situation can occur for heat mode. Once an E3 is displayed on the thermostat, the engine will cycle on for 20 minutes and off for 15 minutes. If the desired temperature set-point is reached in the tamper mode operation (20 minutes on and 15 minutes off), it will return to normal cab mode operation. To clear E3, disable the ICON™ system, key off for approximately 30 seconds, and then reactivate the ICON™ system.

**Note:** The thermostat fault E1 (cab temperature sensor), E2 (external ambient air temperature sensor), and E3 (tamper mode) do **not** flash out on the ICON™ lamp, but merely display on the thermostat display screen. INSITE™ will log an active Fault Code 469 until cleared. Refer to the Cab Thermostat Displays a Fault Code troubleshooting symptom tree in Section TS. Investigate the related fault codes that also can possibly be active.

## Warnings and Cautions

> [!warning] CAUTION · Осторожно
>

**To reduce the possibility of damaging a new ECM, all other active fault codes must be investigated prior to replacing the ECM.**

To reduce the possibility of pin and harness damage, use the following test leads when taking a measurement: Part Number 3822917 - female Deutsch/AMP/Metri-Pack test lead Part Number 3822758 - male Deutsch/AMP/Metri-Pack test lead.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Interview the driver to ascertain the cab temperature system's operation when the fault code occurred and to determine the cab thermostat mode, cab thermostat temperature and range settings, and outside ambient air temperature. |  |
|  | **STEP 1A.** Check the cab thermostat settings and the cab temperature control settings. | Cab thermostat set correctly; cab temperature controls operated appropriately |
| STEP 2. | Read all fault codes. |  |
|  | **STEP 2A.** Read fault codes with INSITE™ electronic service tool. | Fault codes inactive |
|  | **STEP 2B.** Check the cab thermostat display for a fault code. | Fault codes active |
| STEP 3. | Check the ambient air temperature sensor (when cab thermostat fault E2 is displayed). |  |
|  | **STEP 3A.** Check the ambient air temperature sensor and harness connector pins. | No damaged pins |
|  | **STEP 3B.** Check the resistance of the ambient air temperature sensor. | Specifications for resistance at respective ambient air temperature: 0°C \[32°F\] = 29 to 36k ohms, 25°C \[77°F\] = 9 to 11k ohms, 50°C \[122°F\] = 3 to 4k ohms, 75°C \[167°F\] = 1300 to 1600 ohms, 100°C \[212°F\] = 600 to 750 ohms |
|  | **STEP 3C.** Check for an open circuit. | Less than 10 ohms |
|  | **STEP 3D.** Check for a short circuit to ground. | More than 100k ohms |
| STEP 4. | Check the cab thermostat (when cab thermostat fault E1 is displayed). |  |
|  | **STEP 4A.** Check for an open circuit. | Less than 10 ohms |
|  | **STEP 4B.** Check for a short circuit to ground in the cab thermostat output signal. | More than 100k ohms |
|  | **STEP 4C.** Check for cab thermostat communication with the ECM. | Communication of cab thermostat to ECM confirmed |
| STEP 5. | Clear the fault codes. |  |
|  | **STEP 5A.** Disable the fault code. | Fault Code 469 inactive |

### STEP 1. Interview the driver to ascertain the cab temperature system's operation when the fault code occurred and to determine the cab thermostat mode, cab thermostat temperature and range settings, and outside ambient air temperature.

#### STEP 1A. Check the cab thermostat settings and the cab temperature control settings.

| **Conditions:** Turn keyswitch ON. Turn cab thermostat ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check to see that the cab thermostat mode is set appropriately (heat or cool) for the present ambient air temperature conditions and that both the heat and cool mode set points (the range) are programmed into the thermostat properly. (Refer to Procedure 209-017.) Check the cab temperature controls (heat and air conditioning) to make certain that the controls are set appropriately on the cab thermostat mode. | Cab thermostat set correctly; cab temperature controls operated appropriately. | 5A |
| Set the cab thermostat to the appropriate mode and temperature settings; set the cab temperature controls appropriately to coordinate with the cab thermostat settings. Refer to Procedure [[97-209-017 — ICON™ Idle Control System\|209-017]] and or Procedure [[97-019-300 — Cab Thermostat\|019-300]]. | 2A |  |

### STEP 2. Read all fault codes.

#### STEP 2A. Read fault codes with INSITE™ electronic service tool.

| **Conditions:** Turn keyswitch ON. Turn cab thermostat ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Read the fault codes using INSITE™ electronic service tool. | Fault codes inactive | 5A |
| Fault codes active | 2B |  |

#### STEP 2B. Check the cab thermostat display for a fault code.

| **Conditions:** Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| **Note:** If this fault occurs after 60 minutes have elapsed and the cool or heat mode set points are set properly and the vehicle's windows and doors are closed, it indicates that the heater or air conditioning is performing poorly and requires repair, or the insulation in the cab will **not** allow the cab to maintain temperature. Poor insulation can cause the cab to lose temperature too quickly, which causes an engine restart four times in 1 hour. It can be necessary to decrease the Extreme Hot Temperature Trim (trim 1) or the Extreme Cold Temperature Trim (trim 2). Adjusting the trims allows the ICON™ system to transition into a continuous run mode when the cab is **not** capable of maintaining temperature. | No active fault codes | 3A |
| Check the thermostat set points and adjust if necessary. Refer to Procedure [[97-019-300 — Cab Thermostat\|019-300]] and or [[97-209-017 — ICON™ Idle Control System\|209-017]]. | 5A |  |

### STEP 3. Check the ambient air temperature sensor (when cab thermostat fault E2 is displayed).

#### STEP 3A. Check the ambient air temperature sensor and harness connector pins.

| **Conditions:** Turn keyswitch OFF. Disconnect the ambient air temperature sensor from the temperature sensor harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Corroded pins Bent or broken pins Pushed back or expanded pins Wire insulation damage Moisture in or on the connector Missing or damaged connector seals Connector shell broken Dirt or debris in or on the connector pins. For general inspection techniques, refer to Component Connector and Pin Inspection, Procedure [[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | No damaged pins | 3B |
| Repair the damaged pins Flush the dirt, debris, and moisture from the connector pins using electrical contact cleaner, Part Number 3824510. Repair the connector pins. Refer to Procedure 019-202 or 019-206. | 5A |  |

#### STEP 3B. Check the resistance of the ambient air temperature sensor.

| **Conditions:** Turn the keyswitch OFF. Disconnect the ambient air temperature sensor from the temperature sensor harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from pin 1 to pin 2 of the ambient air temperature sensor. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Specifications for resistance at respective ambient air temperature: 0°C \[32°F\] = 29 to 36k ohms 25°C \[77°F\] = 9 to 11k ohms 50°C \[122°F\] = 3 to 4k ohms 75°C \[167°F\] = 1300 to 1600 ohm 100°C \[212°F\] = 600 to 750 ohms | 3C |
| Replace the ambient air temperature sensor. Refer to Procedure [[97-019-134 — Ambient Air Temperature Sensor\|019-134]]. | 5A |  |

#### STEP 3C. Check for an open circuit.

| **Conditions:** Turn keyswitch OFF. Disconnect the ambient air temperature sensor from the temperature sensor harness. Disconnect the temperature sensor harness from the cab thermostat. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from pin 1 of the temperature sensor harness connector, sensor end, to pin 1 of the harness, cab thermostat end. Measure the resistance from pin 2 of the temperature sensor harness connector, sensor end, to pin 3 of the harness, cab thermostat end. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Less than 10 ohms | 3D |
| Repair or replace the OEM temperature sensor harness. Repair the OEM temperature sensor harness. Refer to Procedure 019-202 or 019-206. Replace the OEM temperature sensor harness. Refer to the OEM troubleshooting and repair manual. | 5A |  |

#### STEP 3D. Check for a short circuit to ground.

| **Conditions:** Turn keyswitch OFF. Disconnect the ambient air temperature sensor from the temperature sensor harness. Disconnect the temperature sensor harness from the cab thermostat. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from pin 1 of the temperature sensor harness connector, sensor end, to engine block ground. Measure the resistance from pin 2 of the temperature sensor harness connector, sensor end, to engine block ground. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | More than 100k ohms | 4A |
| Repair or replace the OEM temperature sensor harness. Repair the OEM temperature sensor harness. Refer to Procedure 019-202 019-206. Replace the OEM temperature sensor harness. Refer to OEM troubleshooting and repair manual. | 5A |  |

### STEP 4. Check the cab thermostat (when cab thermostat fault E1 is displayed).

#### STEP 4A. Check for an open circuit.

| **Conditions:** Turn keyswitch OFF. Disconnect the cab thermostat from the OEM harness. Disconnect the OEM harness from the ECM. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from pin 3 of the OEM harness, cab thermostat end, to pin 32 of the OEM harness, ECM end. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Less than 10 ohms | 4B |
| Repair or replace the OEM wiring harness. Refer to the OEM service manual. | 5A |  |

#### STEP 4B. Check for a short circuit to ground in the cab thermostat output signal.

| **Conditions:** Turn keyswitch OFF. Disconnect the cab thermostat from the OEM harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from pin 3 of the cab thermostat harness to engine block ground. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | More than 100k ohms | 4C |
| Repair or replace the cab thermostat. Repair the cab thermostat harness connector. Refer to Procedure 019-202 or 019-206. Replace the cab thermostat. Refer to Procedure 019-300. | 5A |  |

#### STEP 4C. Check for cab thermostat communication with the ECM.

| **Conditions:** Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| **NOTE:** When the bunk thermostat is requesting an engine restart or the engine is running due to a cab comfort mode-generated restart, the word HEAT or COOL will flash on the thermostat display, depending on thermostat mode. This flashing indicates that the thermostat has detected a cab temperature that requires an engine restart and is sending a command to restart the engine to the ECM. | Communication of cab thermostat to ECM confirmed | 5A |
| Replace the cab thermostat. Refer to Procedure [[97-019-300 — Cab Thermostat\|019-300]]. | 5A |  |

### STEP 5. Clear the fault codes.

#### STEP 5A. Disable the fault code.

| **Conditions:** Connect all components. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Use INSITE™ to verify that Fault Code 469 is inactive. Erase the inactive fault codes using INSITE™ electronic service tool. | Fault Code 469 inactive | Repair complete |
| Return to the troubleshooting steps, or contact the local Cummins Authorized Repair Location if all the steps have been completed and rechecked. Troubleshoot any remaining active fault codes. | Appropriate troubleshooting charts |  |
