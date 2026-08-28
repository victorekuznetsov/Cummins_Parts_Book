---
type: "Процедура"
doc: "513-t02-7266"
title_en: "Rudder Angle - Open Circuit (Short to High) or Loss of Signal"
modified: "2019-09-27"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "5411480"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-t02-7266.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-t02-7266.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/513"
---

# Rudder Angle - Open Circuit (Short to High) or Loss of Signal

> [!abstract] Процедура · `513-t02-7266`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[5411480 — C Command Connect and Connect Premier Marine Panel Systems PS102, PS103 and PS108 Mas|5411480]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2019-09-27
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-t02-7266.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-t02-7266.pdf)

Printable Version

### Symptoms

- Alarm Code 7266 or 7665 displayed on ED-4 screen.

- Rudder angle is a constant value.

### How To Use This Tree

This symptom tree can be used to troubleshoot rudder angle sensor Alarm Code. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.

### Shoptalk

Alarm code 7266 and 7265 are supported on ED-4 operating with any Software Version 5 or lower

Alarm code 7665 and 7664 are supported on ED-4 operating with any Software Version 6 or greater

Possible causes include:

- Rudder angle sensor malfunction

- Rudder angle signal shorted high.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the Alarm Codes. |  |
|  | **STEP 1A.** Check for an active fault code. | Alarm Code 7266 or 7665 active? |
| STEP 2. | Check the ED-4 display. |  |
|  | **STEP 2A.** Verify sensor data in the ED-4 display. | Measured value matches the recorded value? |
| STEP 3. | Check the ED-4 display sensor and circuit. |  |
|  | **STEP 3A.** Inspect the ED-4 display sensor and connector pins. | Dirty or damaged pins? |
|  | **STEP 3B.** Check the circuit response. | Alarm Code 7267 or 7664 active and Alarm Code 7266 or 7665 inactive? |
|  | **STEP 3C.** Check the Alarm Codes and verify sensor condition. | Alarm Code 7266 or 7665 active? |
| STEP 4. | Check the original equipment manufacturer (OEM) sensor wiring harness. |  |
|  | **STEP 4A.** Inspect the OEM sensor wiring harness connector pins. | Dirty or damaged pins? |
|  | **STEP 4B.** Check for an open return circuit in the OEM sensor wiring harness. | Less than 10 ohms? |
|  | **STEP 4C.** Check for an open signal circuit in the OEM sensor wiring harness. | Less than 10 ohms? |
|  | **STEP 4D.** Check for an inactive fault code. | Alarm Code 7266 or 7665 no longer active? |

### STEP 1. Check the Alarm Codes.

#### STEP 1A. Check for an active fault code.

| **Conditions:** Turn system enable switch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the ED-4 display to read the Alarm Codes. | Alarm Code 7266 or 7665 active? **YES** | 2A |
| Alarm Code 7266 or 7665 active? **NO** | 2A |  |

### STEP 2. Check the ED-4 display.

#### STEP 2A. Verify sensor data in the ED-4 display.

| **Conditions:** Turn system enable switch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Record the ED-4 display sensor raw value in the I/O viewer. Disconnect the ED-4 display from the Customer Interface Box (C.I.B.). Refer to Procedure 015-023 in section 15. Disconnect the primary and secondary connectors from the ED-4 display. Place one lead on ED-4 display sensor SIGNAL pin 4 on the ED-4 secondary connector. Place the other lead on the RETURN pin 1 on the ED-4 primary connector. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Measured value matches the recorded value? **YES** | 3A |
| Measured value matches the recorded value? **NORepair:** Check ED-4 display analog Input channels in the data log and view - I/O viewer section. [[513-015-035 — Display(s) and Instrumentation\|Refer to Procedure 015-035 in section 15.]] Replace ED-4 if analog channel is **not** working properly. Refer to Procedure 015-023 in section 15. | Repair complete. |  |

### STEP 3. Check the ED-4 display sensor and circuit.

#### STEP 3A. Inspect the ED-4 display sensor and connector pins.

| **Conditions:** Turn system enable switch OFF. Disconnect the ED-4 display sensor from the OEM sensor wiring harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the sensor connector or harness connector. Clean the connector and pins. Repair the damaged harness, connector, or pins, or replace the ED-4 display sensor. Replace the OEM sensor wiring harness. Refer to Procedure 015-103 in Section 15. | Repair complete. |
| Dirty or damaged pins? **NO** | 3B |  |

#### STEP 3B. Check the circuit response.

| **Conditions:** Turn system enable switch OFF. Disconnect the ED-4 display sensor from the OEM sensor wiring harness. Turn system enable switch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Place a jumper wire between the ED-4 display sensor SIGNAL pin and ED-4 display sensor RETURN pin at the OEM sensor wiring harness connector. Wait 30 seconds. Check the ED-4 display to read the Alarm Codes. Reference the appropriate circuit or wiring diagram for connector pin identification. | Alarm Code 7267 or 7264 active and Alarm Code 7266 or 7665 inactive? **YES** | 3C |
| Alarm Code 7267 or 7264 active and Alarm Code 7266 or 7665 inactive? **NO** | 4A |  |

#### STEP 3C. Check the Alarm Codes and verify sensor condition.

| **Conditions:** Turn system enable switch OFF. Connect the ED-4 display sensor from the OEM sensor wiring harness. Turn system enable switch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Wait 30 seconds. Check the ED-4 display to read the Alarm Codes. | Alarm Code 7266 or 7665 active? **YESRepair:** A damaged sensor has been detected. See equipment manufacturer service information. | Repair complete. |
| Alarm Code 7266 or 7665 active? **NORepair:** None. The removal and installation of the connector corrected the fault. | Repair complete. |  |

### STEP 4. Check the original equipment manufacturer (OEM) sensor wiring harness.

#### STEP 4A. Inspect the OEM sensor wiring harness connector pins.

| **Conditions:** Turn system enable switch OFF. Disconnect the OEM sensor wiring harness from the C.I.B. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the OEM sensor wiring harness connector. Clean the connector and pins. Replace the damaged section of the OEM sensor wiring harness or the C.I.B. Repair the damaged harness, connector, or pins, if possible. Refer to Procedure 015-103 in Section 15. | Repair complete. |
| Dirty or damaged pins? **NO** | 4B |  |

#### STEP 4B. Check for an open return circuit in the OEM sensor wiring harness.

| **Conditions:** Turn system enable switch OFF. Disconnect the OEM sensor wiring harness connector from the C.I.B. Disconnect the ED-4 display sensor from the OEM sensor wiring harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Place one test lead on the ED-4 display sensor RETURN pin at the OEM sensor wiring harness C.I.B. connector. Place the other test lead on the ED-4 display sensor RETURN pin at the OEM sensor wiring harness sensor connector. Reference the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Less than 10 ohms? **YES** | 4C |
| Less than 10 ohms? **NORepair:** An open return circuit has been detected in the OEM sensor wiring harness. Troubleshoot each section of the harness and terminal block. Replace the OEM sensor wiring harness, if necessary. Refer to Procedure 015-103 in Section 15. | Repair complete. |  |

#### STEP 4C. Check for an open signal circuit in the OEM sensor wiring harness.

| **Conditions:** Turn system enable switch OFF. Disconnect the OEM sensor wiring harness connector from the C.I.B. Disconnect the ED-4 display sensor from the OEM sensor wiring harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Place one test lead on the ED-4 display sensor SIGNAL pin at the OEM sensor wiring harness C.I.B. connector. Place the other test lead on the ED-4 display sensor SIGNAL pin at the OEM sensor wiring harness sensor connector. Reference the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Less than 10 ohms? **YES** | 4D |
| Less than 10 ohms? **NORepair:** An open signal circuit has been detected in the OEM sensor wiring harness. Troubleshoot each section of the harness and terminal block. Replace the OEM sensor wiring harness, if necessary. Refer to Procedure 015-103 in Section 15. | Repair complete |  |

#### STEP 4D. Check for an inactive fault code.

| **Conditions:** Connect all components. Turn system enable switch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the ED-4 display to read the Alarm Codes. | Fault Code AC 7266 or 7665 no longer active? **YESRepair:** None. The removal and installation of the connector corrected the fault. | Repair complete. |
| Fault Code AC 7266 or 7665 no longer active? **NORepair:** A damaged sensor has been detected. See equipment manufacturer service information for sensor replacement. | Repair complete. |  |
