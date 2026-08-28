---
aliases:
  - "Код 773 — нет показаний датчика подъёма иглы правого ряда или они вне диапазона"
type: "Процедура"
doc: "87-t05-773"
title_en: "FAULT CODE 773 - Right Bank Needle Lift Sensor Reading Is Not Being Detected or Is Out of Range."
title_ru: "Код 773 — нет показаний датчика подъёма иглы правого ряда или они вне диапазона"
modified: "2017-02-22"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666214"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-t05-773.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-t05-773.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
---

# FAULT CODE 773 - Right Bank Needle Lift Sensor Reading Is Not Being Detected or Is Out of Range.
**Код 773 — нет показаний датчика подъёма иглы правого ряда или они вне диапазона**

> [!abstract] Процедура · `87-t05-773`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2017-02-22
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-t05-773.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-t05-773.pdf)

Printable Version

## Warnings and Cautions

> [!warning] CAUTION · Осторожно
> To reduce the possibility of damaging a new engine control module (ECM), all other active fault codes must be investigated prior to replacing the ECM.

> [!warning] CAUTION · Осторожно
> To reduce the possibility of pin and harness damage, use the following test lead when taking a measurement: Part Number 3822758 - male Deutsch™/AMP™/Metri-Pack™ test lead.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check for multiple fault codes. |  |
|  | **STEP 1A.** Read the fault codes. | Fault Codes 115 and 121 active? |
| STEP 2. | Check the needle lift sensor. |  |
|  | **STEP 2A.** Inspect the engine harness and the needle lift sensor connector pins. | Dirty or damaged pins? |
| STEP 3. | Check the engine harness. |  |
|  | **STEP 3A.** Inspect the engine harness and ECM connectors. | Dirty or damaged pins? |
|  | **STEP 3B.** Check for an open circuit. | Resistance greater than 100K ohms? |
|  | **STEP 3C.** Check for a short circuit. | Resistance less than 10 ohms? |
| STEP 4. | Check the calibration revision. |  |
|  | **STEP 4A.** Verify the present calibration revision. | Is the present calibration the most recent revision? |
| STEP 5. | Check the fuel pump. |  |
|  | **STEP 5A.** Inspect the fuel line between the fuel pump and the needle lift valve. | Fuel line restriction? |
|  | **STEP 5B.** Check the fuel pump timing. | Does the timing specified match the fuel pump code on the dataplate? |
| STEP 6. | Clear the fault code. |  |
|  | **STEP 6A.** Disable the fault codes. | Fault Code 773 inactive? |
|  | **STEP 6B.** Clear the inactive fault codes. | All fault codes cleared? |

### STEP 1. Check for multiple fault codes.

#### STEP 1A. Read the fault codes.

| **Conditions:** Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Read the fault codes. Use INSITE™ electronic service tool to read the fault codes. | Fault Codes 115 and 121 active? **YESRepair:** Troubleshoot Fault Code 115 and Fault Code 121 | Multiple fault code tree |
| Fault Codes 115 and 121 active? **NO** | 2A |  |

### STEP 2. Check the needle lift injector

#### STEP 2A. Inspect the engine harness and the needle lift sensor connector pins.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the needle lift sensor. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Read the fault codes and inspect the connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** Repair the damaged pins. Flush the dirt, debris, or moisture from the connector pins. Use electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair the engine harness. Use the following procedures. Refer to Procedure 019-201 in Section 19.. Refer to Procedure 019-202 in Section 19. Replace the engine harness. Refer to Procedure 019-043 in Section 19. Replace the number 1 injector on the left bank. Use the following procedure in the QST30 Service Manual, Bulletin [[4021539 — QST30 Service Manual\|4021539]]. Refer to Procedure 006-026 in Section 6. | 6A |
| Dirty or damaged pins? **NO** | 3A |  |

### STEP 3. Check the engine harness.

#### STEP 3A. Inspect the engine harness and ECM connectors.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the engine harness and ECM connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** Repair the damaged pins. Repair or replace the engine harness, or replace the ECM, whichever has the damaged pins. Flush the dirt, debris, or moisture from the connector pins. Use electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair the engine harness. Refer to Procedure 019-204 in Section 19. Replace the engine harness. Refer to Procedure 019-043 in Section 19. Replace the ECM. Refer to Procedure 019-031 in Section 19. | 6A |
| Dirty or damaged pins? **NO** | 3B |  |

#### STEP 3B. Check for an open circuit.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM. Disconnect the engine harness from the needle lift sensor. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for an open circuit. Measure the resistance from the SIGNAL pin of the engine harness connector to the SIGNAL pin of the needle lift sensor connector, engine harness side. Measure the resistance from the RETURN pin of the engine harness connector to the RETURN pin of the needle lift sensor, engine harness side. | Resistance greater than 100k ohms? **YESRepair:** Repair or replace the engine harness. Repair the engine harness. Refer to Procedure 019-201 in Section 19. Refer to Procedure 019-202 in Section 19. Refer to Procedure 019-204 in Section 19. Replace the engine harness. Refer to Procedure 019-043 in Section 19. | 6A |
| Resistance greater than 100k ohms? **NO** | 3C |  |

#### STEP 3C. Check for a short circuit.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM. Disconnect the OEM harness from the ECM. Disconnect the engine harness from the intake manifold pressure sensor. Disconnect the engine harness from the needle lift sensor. Disconnect the engine harness from the intake manifold temperature sensor. Disconnect the engine harness from the ambient air pressure sensor. Disconnect the engine harness from the coolant pressure sensor. Disconnect the engine harness from the oil pressure sensor. Disconnect the engine harness from the CENSE™ connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for a short circuit from pin-to-pin. Measure the resistance from the SIGNAL pin of the engine harness connector to all other pins in the connector, and to all pins in the OEM harness connector. Measure the resistance from the RETURN pin of the engine harness connector to all other pins in the connector, and to all pins in the OEM harness connector. | Resistance less than 10 ohms? **YESRepair:** Repair or replace the engine harness. Repair the engine harness. Refer to Procedure 019-204 in Section 19. Replace the engine harness. Refer to Procedure 019-043 in Section 19. | 6A |
| Resistance less than 10 ohms? **NO** | 4A |  |

### STEP 4. Check the calibration software phase.

#### STEP 4A. Verify the present calibration software phase.

| **Conditions:** Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Confirm the present calibration software phase. Use INSITE™ electronic service tool to verify the present calibration software. | Present calibration software phase 5.1.0.5 (0501005) or greater? **YES** | 5A |
| Present calibration software phase 5.1.0.5 (0501005) or greater? **NO** | 6A |  |

### STEP 4. Check calibration software phase.

#### STEP 4A. Check if an ECM calibration update is available.

| **Conditions:** Connect all components. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Compare the ECM code and revision number in the ECM to the calibration revisions listed in the ECM Calibration Revision History for applicable changes related to this fault code. Use INSITE™ electronic service tool to find the present ECM code and revision number in the ECM. The ECM code and revision number are found in the Calibration Information section of System ID and Dataplate in Features and Parameters. | Is the present calibration the most recent revision? **YES** | 5A |
| Is the present calibration the most recent revision? **NORepair:** If necessary, calibrate the ECM. [[87-019-032 — ECM Calibration Code\|Refer to Procedure 019-032 in Section 19.]] | 6A |  |

### STEP 5. Check the fuel pump.

#### STEP 5A. Inspect the fuel line

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the fuel line between the fuel pump and number 1 left bank injector for the following: Obstructions Debris Crimped tube. | Fuel line restriction? **YESRepair:** Replace the fuel line. | 6A |
| Fuel line restriction? **NO** | 5B |  |

#### STEP 5B. Check fuel injection pump timing.

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the fuel pump timing. Use the following procedure in QST30 Service Manual, Bulletin [[4021539 — QST30 Service Manual\|4021539]]. Refer to Procedure 005-012 in Section 5. | Timing specified match the fuel pump code on the dataplate? **YES** | 6A |
| Timing specified match the fuel pump code on the dataplate? **NORepair:** Set the fuel pump timing as specified in the following procedure in QST30 Service Manual, Bulletin [[4021539 — QST30 Service Manual\|4021539]]. [[57-005-012-tr — Fuel Injection Pumps, In-Line\|Refer to Procedure 005-012 in Section 5.]] | 6A |  |

### STEP 6. Clear the fault codes.

#### STEP 6A. Disable the fault code.

| **Conditions:** Connect all components. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Disable the fault code. Start the engine and let it idle for 1 minute. With the 5.1.0.5 software phase, operate the engine above 1000 rpm for 1 minute. Verify Fault Code 773 is inactive. | Fault code 773 inactive? **YES** | 6B |
| Fault code 773 inactive? **NORepair:** Return to the troubleshooting steps or contact a Cummins® Authorized Repair Location if all steps have been completed and checked again. | 1A |  |

#### STEP 6B. Clear the inactive fault codes.

| **Conditions:** Connect all components. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Clear the fault codes. Use INSITE™ electronic service tool to clear the inactive fault codes. | All fault codes cleared? **YES** | Repair complete. |
| All fault codes cleared? **NORepair:** Troubleshoot any remaining active fault codes. | Go to the appropriate troubleshooting charts. |  |
