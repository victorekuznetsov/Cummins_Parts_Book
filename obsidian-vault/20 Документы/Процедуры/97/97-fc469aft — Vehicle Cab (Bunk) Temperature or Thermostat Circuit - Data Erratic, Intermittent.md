---
type: "Процедура"
doc: "97-fc469aft"
title_en: "Vehicle Cab (Bunk) Temperature or Thermostat Circuit - Data Erratic, Intermittent or Incorrect"
modified: "2007-01-26"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-fc469aft.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-fc469aft.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "двигатель/QSX15"
  - "группа/97"
---

# Vehicle Cab (Bunk) Temperature or Thermostat Circuit - Data Erratic, Intermittent or Incorrect

> [!abstract] Процедура · `97-fc469aft`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSM11, QSX15
> **Входит в руководства:** [[3666415 — ICON Idle Control System Master Repair Manual|3666415]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2007-01-26
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-fc469aft.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-fc469aft.pdf)

### Fault Code: 469 (Aftermarket and OEM)

### Vehicle Cab (Bunk) Temperature or Thermostat Circuit - Data Erratic, Intermittent or Incorrect

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 469 PID(P): SPN: FMI: Lamp: SRT: | Vehicle Cab (Bunk) Temperature or Thermostat Circuit - Data Erratic, Intermittent or Incorrect. The ICON™ cab thermostat has logged a fault (E3 on the cab thermostat). | E3 will cycle the engine between 20 minutes run and 15 minutes off, or **not** autostart the engine for cab comfort mode (this is a selectable response of the E3 fault in the thermostat trim settings). The ICON™ system will **not** be disabled. Engine mode will remain active. |

![[19802976.png]]

### Circuit Description

The cab thermostat is used to control the cab temperature, either for heating or cooling. At initial turn-on, the thermostat will display the revision level of the software loaded into the thermostat, that is 01, 02, 03, 04, 05 or 06. The cab thermostat is required for cab comfort mode operation. The thermostat communicates with the ICON™ idle control module to command when to autostart the engine to maintain cab temperature. Also, the thermostat is connected to the keyswitch to detect when the ignition is turned on. The above circuit diagram can vary, such as connector or pins, depending on the vehicle make or model. OEM installations can possibly provide the harnessing between the idle control module and other ICON™ devices.

### Component Location

The cab thermostat is typically mounted in the bunk area, above the bed on the wall. The ICON™ module can be located in a different location depending on the vehicle application.

### Shoptalk

The revision level of the software loaded into the cab thermostat is used to identify the set points at which an E3 fault can occur. E3 is an indication that one of the following has occurred:

- Engine has run for more than 45 minutes (revision level 01 and 02) or 60 minutes (revision level 03, 04, 05 or 06) and cool or heat set point is **not** achieved, and the external ambient temperature is within 0° to 100°F (revision level 01 or 02), 0° to 110°F (revision level 03), or 20 to 90°F (revision level 04, 05 or 06). These temperature settings are adjustable as trims 1 and 2, see thermostat trim settings in Procedure [[97-209-017 — ICON™ Idle Control System|209-017]] in Section F)

NOTE: ICON™ thermostat revision level 06 features an expanded range to improve overall ICON™ efficiency. For example, if the set point heat and the set pint cool are both set to 21°C \[70°F\], and the range is 4, then, when the thermostat is in heat mode, the vehicle will start when the cap temperature drops to 19°C \[66°F\] and continue to run until the cab temperature reaches 22°C \[72°F\]. When the thermostat is in cool mode, the vehicle will start when the cab temperature reaches 23°C \[74°F\] and will continue to run until the temperature has dropped to 20°C \[68°F\]. This feature is adjustable.

- A cab thermostat request to start the engine has been made within 10 minutes of an auto-shutdown and the ambient temperature is within 0° to 100° F; that is the thermostat requests an engine restart within 10 minutes of previous shutdown (revision level 01 or 02) or four times within an hour and the ambient temperature is within 0° to 110°F (revision level 03). Revision levels 04, 05, and 06 no longer an E3 fault when the engine is restarted within 10 minutes of a previous shutdown or four times within an hour.

E3 can indicate potential tampering of the thermostat; for example, the operator has chosen cool mode but turned the heater on or opened the windows. The air conditioning system will attempt to cool the truck below the cool set point for correct specified time. At this time, an E3 fault (Fault Code 469) will be logged. A similar situation can occur for heat mode. This fault can also occur, even after achieving the correct temperature, if the battery charging circuit is **not** able to produce the correct voltage for shutdown with all of the fans, lights, refrigerators, and so forth turned on. If this occurs, perform a charging battery system checkout as described in Procedure [[97-210-001 — Installation Procedure|210-001]], Installation Guidelines. The response to an E3 fault is adjustable via the thermostat (trim 8). Select between the following E3 response choices:

- Cycling the engine on for 20 minutes and off for 15 minutes

- Designating that ICON™ system **not** perform an autostart.

Note: An E3 fault displayed on the thermostat is **not** an actual fault with the thermostat. It means that either the heating and air conditioning settings need to be increased, or the operator has set the thermostat temperature beyond what the heating and air conditioning system can accommodate.

Note: The thermostat faults E1 and E2 do **not** flash out on the ICON™ lamp but merely display on the thermostat screen. Refer to the Cab Thermostat Displays a Fault Code troubleshooting symptom tree in Section TS.

The ICON™ system can display **only** the present active fault code. If more than one fault code is active at the same time, the ICON™ system flashes out the highest priority fault. After the fault has been corrected then the next active fault will be flashed out.

Note: The ICON™ electronic service tool can display more than one active and or inactive fault codes at the same time.

## Warnings and Cautions

> [!warning] CAUTION · Осторожно
>

**To reduce the possibility of pin and harness damage, use the following test lead when taking a measurement: Part Number 3822917 - female Deutsch/AMP/Metri-Pack test lead.**

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the fault code status. |  |
|  | **STEP 1A.** Use the fault flashout feature or the ICON™ electronic service tool to read the fault codes. | Fault Code 469 active |
| STEP 2. | Check the cab thermostat set points. |  |
|  | **STEP 2A.** Check the cab thermostat settings. | Set points are within range |
| STEP 3. | Check the ambient air temperature sensor. |  |
|  | **STEP 3A.** Check the ambient air temperature sensor and harness connector pins. | No damaged pins |
|  | **STEP 3B.** Check the resistance of the ambient air temperature sensor. | Specifications for resistance at respective ambient air temperature: 0° C \[32° F \] = 29 to 36k ohms, 25° C \[77° F\] = 9 to 11k ohms, 50° C \[122° F\] = 3 to 4k ohms, 75° C to \[167° F\] = 1300 to 1600 ohms, 100° C \[212° F\] = 600 to 750 ohms |
|  | **STEP 3B-1.** Check for a short to sensor case. | More than 100k ohms |
|  | **STEP 3C.** Check for an open circuit. | Less than 10 ohms |
|  | **STEP 3D.** Check for a short circuit to ground. | More than 100k ohms |
| STEP 4. | Clear the fault code. |  |
|  | **STEP 4A.** Disable the fault code. | Fault Code 469 cleared |

### STEP 1. Check the fault code status.

#### STEP 1A. Use the fault flashout feature or the ICON™ electronic service tool to read the fault codes.

| **Conditions:** Connect all components. Turn keyswitch ON. Connect ICON™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Use the fault flashout feature or the ICON™ electronic service tool to read the fault codes. | Fault Code 469 active. | 2A |
|  | 4A |  |

### STEP 2. Check the cab thermostat set points.

#### STEP 2A. Check the cab thermostat settings.

| **Conditions:** Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Read the fault codes on the cab thermostat display. Note: If this fault occurs after 45 minutes have elapsed (revision level 01 or 02) or 60 minutes have elapsed (revision level 03, 04, 05, or 06), and the cool or heat set points have been set properly, and the vehicle's windows and doors are closed, it is an indication that the heater or air conditioner is performing poorly and requires repair. It can also indicate poor insulation in the cab, which will **not** allow the cab to maintain temperature. Poor insulation can cause the cab to lose temperature too quickly, which will cause an engine restart in less than 10 minutes (revision level 01 or 02) or four times in an hour (revision level 03, 04, 05, or 06). It can be necessary to decrease the Extreme Hot (trim 1) or the Extreme Cold (trim 2). This will allow the ICON™ system to transition into a continuous run mode when the cab is **not** capable of maintaining temperature. It can also be necessary to increase the range to decrease the number of times the engine will be started. | Set points are within range. | 3A |
| Check the thermostat set points and adjust if necessary. Refer to Procedure [[97-019-300 — Cab Thermostat\|019-300]] and Procedure [[97-209-017 — ICON™ Idle Control System\|209-017]]. | 4A |  |

### STEP 3. Check the ambient air temperature sensor.

#### STEP 3A. Check the ambient air temperature sensor and harness connector pins.

| **Conditions:** Turn keyswitch OFF. Disconnect the ambient air temperature sensor from the temperature sensor harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check ambient air temperature sensor and harness connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris on or in the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. For general inspection techniques, refer to Component Connector and Pin Inspection, Procedure [[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | No damaged pins. | 3B |
| Repair the damaged pins. Flush the dirt, debris, and moisture from the connector pins using electrical contact cleaner, Part Number 3824510. Repair the connector pins. Refer to Procedure 019-202 or 019-206. | 4A |  |

#### STEP 3B. Check the resistance of the ambient air temperature sensor.

| **Conditions:** Turn the keyswitch OFF. Disconnect the ambient air temperature sensor from the temperature sensor harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the resistance of the ambient air temperature sensor. Measure the resistance from pin 1 to pin 2 of the ambient air temperature sensor. Refer to the wiring diagram or the circuit diagram for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Specifications for resistance at respective ambient air temperature: 0° C \[32° F\] = 29 to 36k ohms 25° C \[77° F\] = 9 to 11k ohms 50° C \[122° F\] = 3 to 4k ohms 75° C \[167° F\] = 1300 to 1600 ohms 100° C \[212° F\] = 600 to 750 ohms | 3B-1 |
| Replace the ambient air temperature sensor. Refer to Procedure [[97-019-134 — Ambient Air Temperature Sensor\|019-134]]. | 4A |  |

#### STEP 3B-1. Check for a short to sensor case.

| **Conditions:** Turn keyswitch OFF. Disconnect the ambient air temperature sensor from the temperature sensor harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for a short circuit. Measure the resistance from pin 1 of the ambient air temperature sensor to the sensor case. Measure the resistance from pin 2 of the ambient air temperature sensor to the sensor case. Refer to the wiring diagram or the circuit diagram for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | More than 100k ohms. | 3C |
| Replace the ambient air temperature sensor. Refer to Procedure [[97-019-134 — Ambient Air Temperature Sensor\|019-134]]. | 4A |  |

#### STEP 3C. Check for an open circuit.

| **Conditions:** Turn keyswitch OFF. Disconnect the ambient air temperature sensor from the temperature sensor harness. Disconnect the temperature sensor harness from the cab thermostat. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for an open circuit in the temperature sensor harness. Measure the resistance from pin 1 of the temperature sensor harness connector, sensor end, to pin 1 of the harness, cab thermostat end. Measure the resistance from pin 2 of the temperature sensor harness connector, sensor end, to pin 3 of the harness, cab thermostat end. Refer to the wiring diagram or the circuit diagram for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Less than 10 ohms. | 3D |
| Repair or replace the temperature sensor harness. Repair the temperature sensor harness. Refer to Procedure 019-202 or 019-206. Replace the temperature sensor harness. Refer to Procedure 019-296. | 4A |  |

#### STEP 3D. Check for a short circuit to ground.

| **Conditions:** Turn keyswitch OFF. Disconnect the ambient air temperature sensor from the temperature sensor harness. Disconnect the temperature sensor harness from the cab thermostat. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for a short circuit to ground. Measure the resistance from pin 1 of the temperature sensor harness connector, sensor end, to engine block ground. Measure the resistance from pin 2 of the temperature sensor harness connector, sensor end, to engine block ground. Refer to the wiring diagram or the circuit diagram for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | More than 100k ohms. | 4A |
| Repair or replace the temperature sensor harness. Repair the temperature sensor harness. Refer to Procedure 019-202 or 019-206. Replace the temperature sensor harness. Refer to Procedure 019-296. | 4A |  |

### STEP 4. Clear the fault code.

#### STEP 4A. Disable the fault code.

| **Conditions:** Connect all components. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Clear the inactive fault code. | Fault Code 469 cleared. | Repair complete |
| If Fault Code 469 is still active, replace the ICON™ idle control module. Refer to Procedure [[97-019-358 — ICON™ Idle Control Module\|019-358]]. | Repair complete |  |
