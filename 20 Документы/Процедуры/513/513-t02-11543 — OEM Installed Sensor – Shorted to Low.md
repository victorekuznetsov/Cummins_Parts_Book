---
type: "Процедура"
doc: "513-t02-11543"
title_en: "OEM Installed Sensor – Shorted to Low"
modified: "2020-06-22"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "5411480"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-t02-11543.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-t02-11543.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/513"
---

# OEM Installed Sensor – Shorted to Low

> [!abstract] Процедура · `513-t02-11543`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[5411480 — C Command Connect and Connect Premier Marine Panel Systems PS102, PS103 and PS108 Mas|5411480]]
> **Секции:** Section TA - Troubleshooting Alarm Codes
> **Даты:** изменён 2020-06-22
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-t02-11543.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-t02-11543.pdf)

Printable Version

### Symptoms

- OEM installed sensor Alarm displayed on ED-4 screen.

- OEM installed sensor is a constant value.

### How To Use This Tree

This symptom tree can be used to troubleshoot OEM installed sensor alarm code. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.

### Shoptalk

Possible causes are:

- OEM installed sensor malfunction.

- OEM installed sensor signal shorted low.

ED-4 display is capable of monitoring resistive senders with maximum resistance of approximately 1100 ohms and voltage senders with maximum voltage of 10 Volts.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the alarm codes. |  |
|  | **STEP 1A.** Check for sensor supply alarm codes. | OEM installed sensor Alarm active? |
| STEP 2. | Check the ED-4 display. |  |
|  | **STEP 2A.** Verify sensor data in the ED-4 display. | Measured value match the recorded value? |
| STEP. |  |  |
|  | **STEP 3.** Check the OEM installed sensor and harness connector. |  |
|  | **STEP 3A.** Inspect the OEM installed sensor and connector pins. | Dirty or damaged pins? |
|  | **STEP 3B.** Check the circuit response. | Approximately 5 VDC. OEM installed sensor – shorted to low Alarm Code active? |
|  | **STEP 3C.** Check the alarm codes and verify sensor condition. | OEM installed sensor – shorted to low Alarm Code active? |
| STEP 4. | Check the original equipment manufacturer (OEM) sensor wiring harness. |  |
|  | **STEP 4A.** Inspect the OEM installed sensor wiring harness connector pins. | Dirty or damaged pins? |
|  | **STEP 4B.** Check for a pin-to-pin short circuit in the OEM installed sensor wiring harness. | Less than 10 ohms? |
|  | **STEP 4C.** Check for a pin-to-ground short circuit. | Less than 10 ohms? |
|  | **STEP.** |  |
|  | **STEP 4D.** Check for an inactive alarm code. | OEM installed sensor - shorted to low alarm no longer active? |

### STEP. Check the alarm codes.

#### STEP 1A. Check for sensor supply alarm codes.

| **Conditions:** Turn enable switch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the ED-4 display to read the alarm codes. | OEM installed sensor - shorted to low alarm active? **YES** | 2A |
| OEM installed sensor - shorted to low alarm active? **NO** | 2A |  |

### STEP 2. Check the ED-4 display.

#### STEP 2A. Verify sensor data in the ED-4 display.

| **Conditions:** Turn system enable switch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Record the OEM installed sensor Measurement Mode in the I/O viewer. Record the OEM installed sensor resistance or voltage raw value in the I/O viewer. Disconnect the ED-4 display from the customer interface box (C.I.B.). in Section 15. Disconnect the primary and secondary connectors from the ED-4 display. Place one lead on OEM sensor SIGNAL pin on the ED-4 secondary connector. Place the other lead on the RETURN pin 1 on the ED-4 primary connector. | Measured value match the recorded value? **YES** | 3A |
| Measured value match the recorded value? **NORepair:** Check ED-4 display analog input channels in the data log and view - I/O viewer section. [[513-015-035 — Display(s) and Instrumentation\|Refer to Procedure 015-035]] in Section 15. Replace ED-4 if analog channel is **not** working. Refer to Procedure 015-023 in Section 15. | Repair complete |  |

### STEP 3. Check the OEM Installed Sensor and harness connector.

#### STEP 3A. Inspect the OEM Installed Sensor and connector pins.

| **Conditions:** Turn system enable switch OFF. Disconnect the OEM installed sensor from the OEM installed sensor wiring harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the sensor or harness connector. Clean the connector pins. Repair the damaged harness, connectors, or pins, if possible. Refer to Procedure 015-103 in Section 15. | Repair complete. |
| Dirty or damaged pins? **NO** | 3B |  |

#### STEP 3B. Check the OEM installed sensor voltage.

| **Conditions:** Turn system enable switch OFF. Disconnect the OEM installed sensor connector from the OEM installed sensor wiring harness. Turn the system enable switch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the voltage between the OEM installed sensor SUPPLY pin and the OEM installed sensor RETURN pin at the OEM installed sensor connector of the OEM installed sensor wiring harness. Reference the circuit diagram or wiring diagram for connector pin identification. | Between 4.75 and 5.25 volts? **YES** | 3C |
| Between 4.75 and 5.25 volts? **NO** | 4A |  |

#### STEP 3C. Check the alarm codes and verify sensor condition.

| **Conditions:** Turn system enable switch OFF. Disconnect the OEM installed level sensor from the OEM installed sensor wiring harness. Turn system enable switch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Wait 30 seconds. Check the ED-4 display to read the alarm codes. | OEM installed sensor - short to low alarm active? **YESRepair:** A damaged sensor has been detected. Replace the OEM installed sensor. See equipment manufacturer service information. | Repair complete. |
| OEM installed sensor – short to low Alarm active? **NORepair:** None. The removal and installation of the connector corrected the fault. | Repair complete. |  |

### STEP 4. Check the original equipment manufacturer (OEM) sensor wiring harness.

#### STEP 4A. Inspect the OEM installed sensor wiring harness connector pins.

| **Conditions:** Turn system enable switch OFF. Disconnect the OEM installed sensor wiring harness from the C.I.B. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector. Missing or damaged connector seals. Dirt or debris in or the connector pins. Connector shell broken Wire insulation damage Damaged connector locking tab. | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the OEM installed sensor wiring harness connector. Clean the connector and pins. Repair the damaged harness, connector, or pins, if possible. Refer to Procedure 015-103 in Section 15. | Repair complete. |
| Dirty or damaged pins? **NO** | 4B |  |

#### STEP 4B. Check for a pin-to-pin short circuit in the OEM installed sensor wiring harness.

| **Conditions:** Turn system enable switch OFF. Disconnect the OEM installed sensor wiring harness from the C.I.B. Disconnect the OEM installed sensor from the OEM installed sensor wiring harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance between the OEM installed sensor SIGNAL pin in the OEM installed sensor wiring harness C.I.B. connector and all other pins in the OEM installed sensor wiring harness C.I.B. connector. Reference the appropriate circuit or wiring diagram for connector pin identification. | Greater than 100k ohms? **YES** | 4C |
| Greater than 100k ohms? **NORepair:** Replace the OEM installed sensor wiring harness, if necessary. Refer to Procedure 015-103 in Section 15. | Repair complete. |  |

#### STEP 4C. Check for a pin-to-ground short circuit.

| **Conditions:** Turn system enable switch OFF. Disconnect the OEM installed sensor wiring harness from the C.I.B. Disconnect the OEM installed sensor from the OEM installed sensor wiring harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance between the OEM installed sensor SIGNAL pin in the OEM installed sensor wiring harness C.I.B. connector and ground. Reference the appropriate circuit or wiring diagram for connector pin identification. | Less than 10k ohms? **YES** | 4D |
| Less than 10k ohms? **NORepair:** A pin-to-ground short circuit on the SIGNAL wire has been detected in the OEM installed sensor wiring harness. Troubleshoot each of the harness/terminal block. Replace the OEM installed sensor wiring harness, if necessary. Refer to Procedure 015-103 in Section 15. | Repair complete. |  |

#### STEP 4D. Check for an inactive alarm code.

| **Conditions:** Connect all components. Turn system enable switch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the ED-4 display to read the alarm codes. | OEM installed sensor - short to low alarm no longer active? **YESRepair:** None. The removal and installation of the connector corrected the fault. | Repair complete. |
| OEM installed sensor – short to low Alarm no longer active? **NORepair:** A damaged sensor has been detected. Replace the OEM installed sensor. See equipment manufacturer service information. | Repair complete. |  |
