---
type: "Процедура"
doc: "98-fc132as"
title_en: "Accelerator Position Sensor (Frequency Accelerator)"
modified: "2003-10-27"
engines:
  - "37269910"
  - "37280605"
families:
  - "K19"
manuals:
  - "3666070"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-fc132as.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-fc132as.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K19"
  - "группа/98"
---

# Accelerator Position Sensor (Frequency Accelerator)

> [!abstract] Процедура · `98-fc132as`
> **Двигатели:** [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]]
> **Семейство:** K19
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2003-10-27
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-fc132as.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-fc132as.pdf)

### Fault Code: 132-fa

### Accelerator Position Sensor (Frequency Accelerator)

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 132-fa PID(P): P91 SPN: FMI: 4 Lamp: Flashing SRT: 00-622 | Low frequency detected at accelerator position signal pin 18 of the main engine harness electronic control module (ECM) connector. | Loss of accelerator control. Engine will **only** run at 1250 rpm. |

![[19802317.png]]

### Circuit Description

The accelerator signal generator provides the driver's accelerator command to the ECM through the OEM harness and main engine harness. The ECM uses this signal to determine the fueling command for the electronic fuel control valve.

### Component Location

The accelerator signal generator location varies with each OEM. Refer to the OEM manual.

## Warnings and Cautions

> [!warning] CAUTION · Осторожно
>

**To reduce the possibility of damaging the new ECM, all other active fault codes must be investigated prior to replacing the ECM.**

> [!warning] CAUTION · Осторожно
>

**To reduce the possibility of pin and harness damage, use the following test leads when taking a measurement: Part Number 3822917 - female Deutsch/AMP/Metri-Pack test lead Part Number 3823993 - male Deutsch test lead Part Number 3823994 - female Deutsch test lead.**

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check for other fault codes. |  |
|  | **STEP 1A.** Read the fault codes. | Fault Code 443 not logged |
| STEP 2. | Check the OEM harness and accelerator signal generator. (The following steps have been constructed for generic OEM troubleshooting of the OEM circuit. See the OEM manual for more details.) |  |
|  | **STEP 2A.** Inspect the OEM and main engine harness connector pins. | No damaged pins |
|  | **STEP 2B.** Check for an open circuit. | 800 to 1200 ohms |
|  | **STEP 2C.** Check for a short circuit to ground. | More than 100k ohms |
|  | **STEP 2D.** Check for a short circuit from pin to pin. | More than 100k ohms |
| STEP 3. | Check the main engine harness. |  |
|  | **STEP 3A.** Inspect the main engine harness and ECM connector pins. | No damaged pins |
|  | **STEP 3B.** Check for an open circuit. | Less than 10 ohms |
|  | **STEP 3C.** Check for a short circuit to ground. | More than 100k ohms |
|  | **STEP 3D.** Check for a short circuit from pin to pin. | More than 100k ohms |
| STEP 4. | Clear the fault codes. |  |
|  | **STEP 4A.** Disable the fault code. | Fault Code 132 inactive |
|  | **STEP 4B.** Clear the inactive fault codes. | All fault codes cleared |

### STEP 1. Check for other fault codes.

#### STEP 1A. Read the fault codes.

| **Conditions:** Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Read the fault codes using Compulink™, Part Number 3823549; Echek™, Part Number 3824437; or INSITE ™, Part Number 3824638. | Fault Code 443 not logged | 2A |
| Troubleshoot Fault Code 443. Refer to Fault Code 443 troubleshooting tree. | Appropriate troubleshooting chart |  |

### STEP 2. Check the OEM harness and accelerator signal generator. (The following steps have been constructed for generic OEM troubleshooting of the OEM circuit. See the OEM manual for more details.)

#### STEP 2A. Inspect the OEM and main engine harness connector pins.

| **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness from the main engine harness at the C6 connector. Flush and clean the connector pins using electronic contact cleaner, Part Number 3824510. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins. | No damaged pins | 2B |
| Repair the damaged pins. Flush the dirt, debris, or moisture from the connector pins. Repair or replace the main engine harness or the OEM harness, whichever has the damaged pins. Flush the dirt, debris, or moisture from the connector pins using electronic contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair the main engine harness. Refer to Procedure 019-043. Replace the main engine harness. Refer to Procedure 019-043. Repair the OEM harness. Refer to the OEM troubleshooting and repair manual. Replace the OEM harness. Refer to the OEM troubleshooting and repair manual. | 4A |  |

#### STEP 2B. Check for an open circuit.

| **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness from the main engine harness at the C6 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from pin E of the OEM harness C6 connector to pin D of the OEM harness C6 connector. | 800 to 1200 ohms | 2C |
| Repair or replace the OEM harness or the accelerator signal generator, whichever has the open circuit. Repair the OEM harness. Refer to the OEM troubleshooting and repair manual. Replace the OEM harness. Refer to the OEM troubleshooting and repair manual. Repair the accelerator signal generator. Refer to the OEM troubleshooting and repair manual. Replace the accelerator signal generator. Refer to the OEM troubleshooting and repair manual. | 4A |  |

#### STEP 2C. Check for a short circuit to ground.

| **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness from the main engine harness at the C6 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from pin E of the OEM harness C6 connector to engine block ground. Measure the resistance from pin D of the OEM harness C6 connector to engine block ground. | More than 100k ohms | 2D |
| Repair or replace the OEM harness or the accelerator signal generator, whichever has the short circuit to ground. Repair the OEM harness. Refer to the OEM troubleshooting and repair manual. Replace the OEM harness. Refer to the OEM troubleshooting and repair manual. Repair the accelerator signal generator. Refer to the OEM troubleshooting and repair manual. Replace the accelerator signal generator. Refer to the OEM troubleshooting and repair manual. | 4A |  |

#### STEP 2D. Check for a short circuit from pin to pin.

| **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness from the main engine harness at the C5 and C6 connectors. Disconnect the accelerator pedal or accelerator lever from the OEM harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from pin D of the OEM harness C6 connector to all other pins in the OEM harness C5 and C6 connectors, except pin E of the OEM harness C6 connector. Measure the resistance from pin E of the OEM harness C6 connector to all other pins in the OEM harness C5 and C6 connectors, except pin D of the OEM harness C6 connector. | More than 100k ohms | 3A |
| Repair or replace the OEM harness or the accelerator signal generator, whichever has the short circuit. Repair the OEM harness. Refer to the OEM troubleshooting and repair manual. Replace the OEM harness. Refer to the OEM troubleshooting and repair manual. Repair the accelerator signal generator. Refer to the OEM troubleshooting and repair manual. Replace the accelerator signal generator. Refer to the OEM troubleshooting and repair manual. | 4A |  |

### STEP 3. Check the main engine harness.

#### STEP 3A. Inspect the main engine harness and ECM connector pins.

| **Conditions:** Turn keyswitch OFF. Disconnect the ECM from the main engine harness. Flush and clean the connector pins using electronic contact cleaner, Part Number 3824510. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins. | No damaged pins | 3B |
| Repair the damaged pins. Flush the dirt, debris, or moisture from the connector pins. Repair or replace the main engine harness, or replace the ECM, whichever has the damaged pins. Flush the dirt, debris, or moisture from the connector pins using electronic contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair the main engine harness. Refer to Procedure 019-043. Replace the main engine harness. Refer to Procedure 019-043. Replace the ECM. Refer to Procedure 019-031. | 4A |  |

#### STEP 3B. Check for an open circuit.

| **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness from the main engine harness at the C6 connector. Disconnect the ECM from the main engine harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from pin 13 of the main engine harness ECM connector to pin E of the main engine harness C6 connector. Measure the resistance from pin 18 of the main engine harness ECM connector to pin D of the main engine harness C6 connector. | Less than 10 ohms | 3C |
| Repair or replace the main engine harness. Repair the main engine harness. Refer to Procedure 019-043. Replace the main engine harness. Refer to Procedure 019-043. | 4A |  |

#### STEP 3C. Check for a short circuit to ground.

| **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness from the main engine harness at the C5 and C6 connectors. Disconnect the ECM from the main engine harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from pin 13 of the main engine harness ECM connector to engine block ground. Measure the resistance from pin 18 of the main engine harness ECM connector to engine block ground. | More than 100k ohms | 3D |
| Repair or replace the main engine harness. Repair the main engine harness. Refer to Procedure 019-043. Replace the main engine harness. Refer to Procedure 019-043. | 4A |  |

#### STEP 3D. Check for a short circuit from pin to pin.

| **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness from the main engine harness at the C5 and C6 connectors. Disconnect the ECM from the main engine harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from pin 13 of the main engine harness ECM connector to all other pins in the main engine harness ECM connector. Measure the resistance from pin 18 of the main engine harness ECM connector to all other pins in the main engine harness ECM connector. | More than 100k ohms | 4A |
| Repair or replace the main engine harness. Repair the main engine harness. Refer to Procedure 019-043. Replace the main engine harness. Refer to Procedure 019-043. | 4A |  |

### STEP 4. Clear the fault codes.

#### STEP 4A. Disable the fault code.

| **Conditions:** Connect all components. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Start the engine and idle for one minute. Verify Fault Code 132 is inactive. | Fault Code 132 inactive | 4B |
| Return to troubleshooting steps or contact a local Cummins Authorized Repair Location if all steps have been completed and rechecked. | 1A |  |

#### STEP 4B. Clear the inactive fault codes.

| **Conditions:** Connect all components. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Erase the inactive fault codes using Compulink™, Part Number 3823549; Echek™, Part Number 3824437; or INSITE™, Part Number 3824638. | All fault codes cleared | Repair complete |
| Troubleshoot any remaining active fault codes. | Appropriate troubleshooting charts |  |
