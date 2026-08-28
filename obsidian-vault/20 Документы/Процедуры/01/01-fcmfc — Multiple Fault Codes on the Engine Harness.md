---
aliases:
  - "Множественные коды неисправностей на жгуте двигателя"
type: "Процедура"
doc: "01-fcmfc"
title_en: "Multiple Fault Codes on the Engine Harness"
title_ru: "Множественные коды неисправностей на жгуте двигателя"
modified: "2004-02-03"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fcmfc.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fcmfc.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Multiple Fault Codes on the Engine Harness
**Множественные коды неисправностей на жгуте двигателя**

> [!abstract] Процедура · `01-fcmfc`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2004-02-03
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fcmfc.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fcmfc.pdf)

### Fault Code: Multiple

### Multiple Fault Codes on the Engine Harness

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: Multiple PID(P): SPN: FMI: Lamp: SRT: | Multiple fault codes generated due to a common supply or a return wire failure in the engine harness. | Multiple fault codes. |

![[19802494.png]]

### Circuit Description

The electronic control module (ECM) supplies all of the engine pressure sensors on the engine harness with +5 VDC. The ECM has common returns for most of the engine pressure and temperature sensors. A failure on either of these wires will cause multiple fault codes.

### Component Location

Refer to Procedure 100-002 for the component location.

### Shoptalk

Look for open circuits in the common supply and return wires and shorts from battery or ground to the supply and return wires or defective ECM power supply. A failed pressure sensor can cause multiple fault codes. A failed pressure sensor can cause multiple active fault codes to go inactive once the engine has been started.

## Warnings and Cautions

> [!warning] CAUTION · Осторожно
>

**To reduce the possibility of damaging a new ECM, all other active fault codes must be investigated prior to replacing the ECM.**

To reduce the possibility of pin and harness damage, use the following test leads when taking a measurement: Part Number 3822758 - male Deutsch/AMP/Metri-Pack test lead Part Number 3822917 - female Deutsch/AMP/Metri-Pack test lead.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check for multiple fault codes. |  |
|  | **STEP 1A.** Read the fault codes. | Record all active fault codes |
| STEP 2. | Check the engine harness. |  |
|  | **STEP 2A.** Inspect the engine harness and the extension harness connector pins. | No damaged pins |
|  | **STEP 2B.** Check for a short circuit to engine block ground. | More than 100k ohms |
|  | **STEP 2C.** Check for an open circuit. | Less than 10 ohms |
|  | **STEP 2D.** Check for a short circuit from pin to pin. | More than 100k ohms |
| STEP 3. | Check the extension harness. |  |
|  | **STEP 3A.** Inspect the extension harness and the ECM connector pins. | No damaged pins |
|  | **STEP 3B.** Check for short circuit to engine block ground. | More than 100k ohms |
|  | **STEP 3C.** Check for an open circuit. | Less than 10 ohms |
|  | **STEP 3D.** Check for a short circuit from pin to pin. | More than 100k ohms |
| STEP 4. | Clear the fault codes. |  |
|  | **STEP 4A.** Disable the fault codes. | Recorded fault codes inactive |
|  | **STEP 4B.** Clear the inactive fault codes. | All fault codes cleared |

### STEP 1. Check for multiple fault codes.

#### STEP 1A. Read the fault codes.

| **Conditions:** Run/Stop switch in the Stop position. Connect the electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Using the electronic service tool, read the multiple fault codes. | Record all active fault codes | 2A |
| **Only** a single fault code. Go to the specific fault code procedure. | Specific fault code number |  |

### STEP 2. Check the engine harness.

#### STEP 2A. Inspect the engine harness and the extension harness connector pins.

| **Conditions:** Run/Stop switch in the Stop position. Disconnect the engine harness from the extension harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins. | No damaged pins | 2B |
| Repair the damaged pins. Flush the dirt, debris, or moisture from the connector pins using electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair the engine harness. Refer to Procedure 019-208. Replace the engine harness. Refer to Procedure 019-043. Repair the extension harness. Refer to Procedure 019-208. Replace the extension harness. Refer to Procedure 019-175. | 4A |  |

#### STEP 2B. Check for a short circuit to engine block ground.

| **Conditions:** Run/Stop switch in the Stop position. Identify the common wire(s) for all fault codes active. Disconnect the engine harness from the extension harness. Disconnect all sensors that are part of the common wire from the engine harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from the common wire(s) pin on the engine harness inline connector to the engine block ground. | More than 100k ohms | 2C |
| Repair or replace the engine harness. Repair the engine harness. Refer to Procedure 019-208. Replace the engine harness. Refer to Procedure 019-043. | 4A |  |

#### STEP 2C. Check for an open circuit.

| **Conditions:** Run/Stop switch in the Stop position. Identify the common wire(s) for all fault codes active. Disconnect the engine harness from the extension harness. Disconnect all sensors that are part of the common wire from the engine harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from the common wire(s) pin on the engine harness inline connector to the common wire(s) pin on the engine harness sensor connector. | Less than 10 ohms | 2D |
| Repair or replace the engine harness. Repair the engine harness. Refer to Procedure 019-208. Replace the engine harness. Refer to Procedure 019-043. | 4A |  |

#### STEP 2D. Check for a short circuit from pin to pin.

| **Conditions:** Run/Stop switch in the Stop position. Identify the common wire(s) for all fault codes active. Disconnect the engine harness from the extension harness. Disconnect all sensors that are part of the common wire from the engine harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from the common wire(s) pin on the engine harness inline connector to all other pins in the engine harness inline connector. | More than 100k ohms | 3A |
| Repair or replace the engine harness. Repair the engine harness. Refer to Procedure 019-208. Replace the engine harness. Refer to Procedure 019-043. | 4A |  |

### STEP 3. Check the extension harness.

#### STEP 3A. Inspect the extension harness and the ECM connector pins.

| **Conditions:** Run/Stop switch in the Stop position. Disconnect the extension harness connector from the ECM. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins. | No damaged pins | 3B |
| Repair the damaged pins. Flush the dirt, debris, or moisture from the connector pins using electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair the extension harness. Refer to Procedure 019-213. Replace the extension harness. Refer to Procedure 019-175. Replace the ECM. Refer to Procedure 019-031. | 4A |  |

#### STEP 3B. Check for a short circuit to engine block ground.

| **Conditions:** Run/Stop switch in the Stop position. Identify the common wire(s) for all fault codes active. Disconnect the extension harness from the engine harness. Disconnect the extension harness from the ECM. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from the common wire(s) pin on the extension harness connector to the engine block ground. | More than 100k ohms | 3C |
| Repair or replace the extension harness. Repair the extension harness. Refer to Procedure 019-213. Replace the extension harness. Refer to Procedure 019-175. | 4A |  |

#### STEP 3C. Check for an open circuit.

| **Conditions:** Run/Stop switch in the Stop position. Identify the common wire(s) for all fault codes active. Disconnect the extension harness from the engine harness. Disconnect the extension harness from the ECM. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from the common wire(s) pin on the extension harness connector to the common wire(s) pin on the extension harness inline connector. | Less than 10 ohms | 3D |
| Repair or replace the extension harness. Repair the extension harness. Refer to Procedure 019-213. Replace the extension harness. Refer to Procedure 019-175. | 4A |  |

#### STEP 3D. Check for a short circuit from pin to pin.

| **Conditions:** Run/Stop switch in the Stop position. Identify the common wire(s) for all fault codes active. Disconnect the extension harness from the engine harness. Disconnect the extension harness from the ECM. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from the common wire(s) pin on the extension harness connector to all other pins in the extension harness connector. | More than 100k ohms | 4A |
| Repair or replace the extension harness. Repair the extension harness. Refer to Procedure 019-213. Replace the extension harness. Refer to Procedure 019-175. | 4A |  |

### STEP 4. Clear the fault codes.

#### STEP 4A. Disable the fault codes.

| **Conditions:** Connect all components. Connect the electronic service tool. Idle/Rated switch in the Idle position. Run/Stop switch in the Run position and idle for 1 minute. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Using the electronic service tool, verify recorded fault codes are inactive. | Recorded fault codes inactive | 4B |
| Return to troubleshooting steps or contact the nearest authorized repair location if all steps have been completed and checked again. | 1A |  |

#### STEP 4B. Clear the inactive fault codes.

| **Conditions:** Run/Stop switch in the Stop position. Connect all components. Connect the electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Using the electronic service tool, clear the inactive fault codes. | All fault codes cleared | Repair complete |
| Troubleshoot any remaining active fault codes. | Appropriate troubleshooting chart |  |
