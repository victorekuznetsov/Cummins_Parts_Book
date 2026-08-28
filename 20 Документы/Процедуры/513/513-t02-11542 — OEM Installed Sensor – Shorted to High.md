---
type: "Процедура"
doc: "513-t02-11542"
title_en: "OEM Installed Sensor – Shorted to High"
modified: "2020-06-25"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "5411480"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-t02-11542.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-t02-11542.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/513"
---

# OEM Installed Sensor – Shorted to High

> [!abstract] Процедура · `513-t02-11542`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[5411480 — C Command Connect and Connect Premier Marine Panel Systems PS102, PS103 and PS108 Mas|5411480]]
> **Секции:** Section TA - Troubleshooting Alarm Codes
> **Даты:** изменён 2020-06-25
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-t02-11542.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-t02-11542.pdf)

Printable Version

### Symptoms

- OEM installed sensor Alarm displayed on ED-4 screen.

- OEM installed sensor is a constant value.

### How To Use This Tree

This symptom tree can be used to troubleshoot OEM installed sensor Alarm. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.

### Shoptalk

Possible causes are:

- OEM installed sensor Alarm malfunction.

- OEM installed sensor Alarm shorted high.

ED-4 display is capable of monitoring resistive senders with maximum resistance of approximately 1100 ohms and voltage senders with maximum voltage of 10 Volts.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the OEM installed sensor alarm. |  |
|  | **STEP 1A.** Check for an active OEM installed sensor alarm. | OEM installed sensor – shorted to high Alarm active? |
| STEP 2. | Check the ED-4 display. |  |
|  | **STEP 2A.** Verify sensor data in the ED-4 display. | Measured value match the recorded value? |
| STEP 3. | Check the OEM installed sensor and circuit. |  |
|  | **STEP 3A.** Inspect the OEM Installed sensor and connector pins. | Dirty or damaged pins? |
|  | **STEP 3B.** Check the circuit response. | OEM installed sensor – shorted to high Alarm active and OEM installed sensor - shorted to low Alarm inactive? |
|  | **STEP 3C.** Check the OEM installed sensor Alarm and verify sensor condition. | OEM installed sensor – shorted to high Alarm active? |
| STEP 4. | Check the original equipment manufacturer (OEM) sensor wiring harness. |  |
|  | **STEP 4A.** Inspect the OEM installed sensor wiring harness connector pins. | Dirty or damaged pins? |
|  | **STEP 4B.** Check for an open return circuit in the OEM installed sensor wiring harness. | Less than 10 ohms? |
|  | **STEP 4C.** Check for an open circuit in the OEM installed sensor wiring harness. | Greater than 100k ohms? |
|  | **STEP 4D.** Check for an inactive fault code. | OEM installed sensor – Shorted to High Alarm no longer active? |

### STEP 1. Check the alarm codes.

#### STEP 1A. Check for an active fault code.

| **Conditions:** Turn system enable switch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the ED-4 display to read the alarm codes. | OEM installed sensor – shorted to high Alarm active? **YES** | 2A |
| OEM installed sensor – shorted to high Alarm active? **NO** | Use the following procedure for inactive and intermittent alarm codes. |  |

### STEP 2. Check the ED-4 display.

#### STEP 2A. Verify sensor data in the ED-4 display.

| **Conditions:** Turn system enable switch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Record the OEM installed sensor Measurement Mode in the I/O viewer. Record the OEM installed sensor resistance or voltage raw value in the I/O viewer. Disconnect the ED-4 display from the customer interface box (C.I.B.). Refer to Procedure 015-023. Disconnect the primary and secondary connectors from the ED-4 display. Place one lead on OEM installed sensor SIGNAL pin on the ED-4 secondary connector. Place the other lead on the RETURN pin 1 on the ED-4 primary connector. | Measured value match the recorded value? **YES** | 3A |
| Measured value match the recorded value? **NORepair:** Replace ED-4 if analog channel is **not** working properly. Refer to Procedure 015-023 in Section 15. | Repair complete. |  |

### STEP 3. Check the OEM installed sensor and circuit.

#### STEP 3A. Inspect the OEM installed sensor and connector pins.

| **Conditions:** Turn system enable switch OFF. Disconnect the OEM installed sensor from the wiring harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the sensor connector or harness connector. Clean the connector and pins. Repair the damaged harness, connector, or pins, or replace the OEM installed sensor. Replace the OEM installed sensor wiring harness. Refer to Procedure 015-103 in Section 15. | Repair complete. |
| Dirty or damaged pins? **NO** | 3B |  |

#### STEP 3B. Check the OEM installed sensor voltage.

| **Conditions:** Turn system enable switch ON. Disconnect the OEM installed sensor from the wiring harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the voltage. Place one lead on the OEM installed sensor SUPPLY pin at the wiring harness. Place the other lead on the OEM installed sensor RETURN pin at the wiring harness. Wire insulation damage. Damaged connector locking tab. | Between 4.75 and 5.25 volts? **YES** | 3C |
| Between 4.75 and 5.25 volts? **NO** | 4A |  |

#### STEP 3C. Check the OEM installed sensor alarm and verify sensor condition.

| **Conditions:** Turn system enable switch OFF. Connect the OEM installed sensor from the OEM installed sensor wiring harness. Turn system enable switch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Wait 30 seconds. Check the ED-4 display to read the alarm codes. | OEM installed sensor – shorted to high alarm active? **YESRepair:** A damaged sensor has been detected. Reference the OEM for sensor replacement. | Repair complete. |
| OEM installed sensor - shorted to high alarm active? **NORepair:** None. The removal and installation of the connector corrected the fault. | Repair complete. |  |

### STEP 4. Check the original equipment manfacturer (OEM) sensor wiring harness.

#### STEP 4A. Inspect the OEM installed sensor wiring harness from the C.I.B.

| **Conditions:** Turn system enable switch OFF. Disconnect the OEM installed sensor wiring harness from the C.I.B. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the OEM installed sensor wiring harness connector. Clean the connector and pins. Replace the damaged section of the OEM installed sensor wiring harness or the C.I.B. Repair the damaged harness, connector, or pins, if possible. Refer to Procedure 015-103. | Repair complete. |
| Dirty or damaged pins? **NO** | 4B |  |

#### STEP 4B. Check for an open return circuit in the OEM installed sensor wiring harness.

| **Conditions:** Turn system enable switch OFF. Disconnect the OEM installed sensor wiring harness connector from the C.I.B. Disconnect the OEM installed sensor from the OEM installed sensor wiring harmess. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance. Place one test lead on the OEM installed sensor RETURN pin at the OEM installed sensor wiring harness C.I.B connector. Place the other test lead on the OEM installed sensor RETURN pin at the OEM installed sensor wiring harness sensor connector. Reference the circuit diagram or wiring diagram for connector pin identification. | Less than 10 ohms? **YES** | 4C |
| Less than 10 ohms? **NORepair:** An open return circuit has been detected in the OEM installed sensor wiring harness. Troubleshoot each section of the harness and terminal block. Replace the OEM installed sensor wiring harness, if necessary. Refer to Procedure 015-103. | Repair complete. |  |

#### STEP 4C. Check for an open circuit in the OEM installed sensor wiring harness.

| **Conditions:** Turn system enable switch OFF. Disconnect the OEM installed sensor wiring harness from the C.I.B. Disconnect the OEM installed sensor from the OEM installed sensor wiring harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance. Place one test lead on the OEM installed sensor SIGNAL pin at the OEM installed sensor wiring harness C.I.B connector. Place the other test lead on the OEM installed sensor SIGNAL pin at the OEM installed sensor wiring harness sensor connector. Reference the circuit diagram or wiring diagram for connector pin identification. | Less than 10 ohms? **YESRepair:** | 4D |
| Less than 10 ohms? **NORepair:** An open circuit on the signal line has been detected in the OEM installed sensor wiring harness. Troubleshoot each section of the harness and terminal block. Replace the OEM installed sensor wiring harness, if necessary. Refer to Procedure 015-103. | Repair complete. |  |

#### STEP 4D. Check for an inactive OEM installed sensor alarm.

| **Conditions:** Connect all components. Turn system enable switch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Wait 30 seconds. Check the ED-4 display to read the alarm codes. | OEM installed sensor - short to high alarm no longer active? **YESRepair:** None. The removal and installation of the connector corrected the fault. | Repair complete. |
| OEM installed sensor - short to high alarm no longer active? **NORepair:** A damaged sensor has been detected. Reference the OEM for sensor replacement. | Repair complete. |  |
