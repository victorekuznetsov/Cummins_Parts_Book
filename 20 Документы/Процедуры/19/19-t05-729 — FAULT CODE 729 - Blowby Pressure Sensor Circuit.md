---
type: "Процедура"
doc: "19-t05-729"
title_en: "FAULT CODE 729 - Blowby Pressure Sensor Circuit"
modified: "2013-04-15"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
  - "85017333"
families:
  - "QSK23"
  - "QSK60"
manuals:
  - "3666113"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-t05-729.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-t05-729.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
---

# FAULT CODE 729 - Blowby Pressure Sensor Circuit

> [!abstract] Процедура · `19-t05-729`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2013-04-15
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-t05-729.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-t05-729.pdf)

Printable Version

## Warnings and Cautions

> [!warning] CAUTION · Осторожно
> To reduce the possibility of damaging a new engine control module (ECM), all other active fault codes must be investigated prior to replacing the ECM.

> [!warning] CAUTION · Осторожно
> To reduce the possibility of pin and harness damage, use the following test leads when taking a measurement: Part Number 3822758 - male Deutsch™/AMP™/Metri-Pack™ test lead, Part Number 3822917 - female Deutsch™/AMP™/Metri-Pack™ test lead, Part Number 3823994 - female Deutsch™ test lead, Part Number 3824774 - breakout cable.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check for multiple fault codes. |  |
|  | **STEP 1A.** Read the fault codes. | Fault Codes 123, 141, 222, 232, 265, and 471 are not active? |
| STEP 2. | Check the blowby pressure sensor. |  |
|  | **STEP 2A.** Inspect the blowby pressure sensor and engine harness connector pins. | Dirty or damaged pins? |
|  | **STEP 2B.** Read the fault codes. | Fault Code 729 active? |
|  | **STEP 2C.** Check ECM blowby pressure supply voltage. | 4.75 to 5.25-VDC? |
|  | **STEP 2C-1.** Check ECM blowby pressure supply voltage. | 4.75 to 5.25-VDC engine stopped? |
|  | **STEP 2D.** Check ECM blowby pressure signal voltage. | 0.42 to 0.58-VDC engine stopped? |
|  | **STEP 2D-1.** Check for a short circuit from pin to pin. | More than 100k ohms? |
|  | **STEP 2D-2.** Check for continuity in the engine harness. | Less than 10 ohms? |
|  | **STEP 2D-3.** Check the resistance from SIGNAL pin to RETURN pin in the ECM port. | More than 35k ohms? |
| STEP 3. | Check the engine harness. |  |
|  | **STEP 3A.** Inspect the engine harness and ECM connector pins. | Dirty or damaged pins? |
|  | **STEP 3B.** Read the fault codes. | Fault Code 729 active? |
|  | **STEP 3C.** Check for an open circuit. | Less than 10 ohms? |
|  | **STEP 3D.** Check for a short circuit from pin to pin. | More than 100k ohms? |
|  | **STEP 3E.** Check for a short circuit to engine block ground. | More than 100k ohms? |
| STEP 4. | Clear the fault codes. |  |
|  | **STEP 4A.** Disable the fault code. | Fault Code 729 inactive? |
|  | **STEP 4B.** Clear the inactive fault codes. | All fault codes cleared? |

### STEP 1. Check for multiple fault codes.

#### STEP 1A. Read the fault codes.

| **Conditions:** Connect INSITE™ electronic service tool. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Read the fault codes. Use INSITE™ electronic service tool to read the fault codes. | Fault Codes 123, 141, 222, 232, 265, and 471 are not active? | 2A |
| Possible open circuit in the sensor common supply wire. | Multiple fault code trees |  |

### STEP 2. Check the blowby pressure sensor.

#### STEP 2A. Inspect the blowby pressure sensor and engine harness connector pins.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the blowby pressure sensor. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the blowby pressure sensor and engine harness connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? | 2B |
| A damaged connection has been detected in the ECM engine connector or engine harness connector. Repair damaged pins. Repair or replace the engine harness, or replace the blowby pressure sensor, whichever has the damaged pins. Flush the dirt, debris, or moisture from the connector pins, use electronic contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair the engine harness. Refer to Procedure 019-201 in Section 19. Refer to Procedure 019-202 in Section 19. Refer to Procedure 019-204 in Section 19. Replace the engine harness. Refer to Procedure 019-043 in Section 19. Replace the blowby pressure sensor. Refer to Procedure 019-011 in Section 19. | 4A |  |

#### STEP 2B. Read the fault codes.

| **Conditions:** Connect INSITE™ electronic service tool. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Read the fault codes. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 729 active? | 2C |
| Repair complete. | 4B |  |

#### STEP 2C. Check ECM blowby pressure supply voltage.

| **Conditions:** Disconnect the blowby pressure sensor from the engine harness. Install the blowby pressure sensor breakout cable, Part Number 3824774, between the sensor and the engine harness connector. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check ECM blowby pressure supply voltage. Measure the supply voltage by installing the breakout cable's supply (pin A) and return connectors (pin B) into the multimeter. | 4.75 to 5.25-VDC? | 2D |
|  | 2C-1 |  |

#### STEP 2C-1. Check ECM blowby pressure supply voltage.

| **Conditions:** Disconnect the breakout cable from the sensor. (Leave breakout cable connected to the engine harness.) Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the ECM blowby pressure supply voltage. Measure the supply voltage by installing the breakout cable's supply (pin A) and return (pin B) connectors into the multimeter. | 4.75 to 5.25-VDC? Replace the blowby pressure sensor. Refer to Procedure 019-011 in Section 19. | 4A |
|  | 3A |  |

#### STEP 2D. Check ECM blowby pressure signal voltage.

| **Conditions:** Disconnect the blowby pressure sensor from the engine harness. Install the blowby pressure sensor breakout cable, Part Number 3824774, between the sensor and the engine harness connector. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the ECM blowby pressure signal voltage. Measure the signal voltage by installing the breakout cable's signal (pin C) and return connectors (pin B) into the multimeter. | 0.42 to 0.58-VDC? | 3A |
| Does **not** meet specification. | 4A |  |

#### STEP 2D-1. Check for a short circuit from pin to pin.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM. Disconnect blowby pressure sensor from the engine harness. Disconnect rail pressure sensor from the engine harness. Disconnect the fuel pump pressure sensor from the engine harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for a short circuit from pin to pin. Measure the resistance from pin 6 of the engine harness ECM connector to all other pins in the connector. Measure the resistance from pin 25 of the engine harness ECM connector to all other pins in the connector. Measure the resistance from pin 17 of the engine harness ECM connector to all other pins in the connector. | More than 100k ohms? | 2D-2 |
| Repair or replace the engine harness. Repair the engine harness. Refer to Procedure 019-204 in Section 19. Replace the engine harness. Refer to Procedure 019-043 in Section 19. | 5A |  |

#### STEP 2D-2. Check for continuity in the engine harness.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM. Disconnect the blowby pressure sensor from the engine harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for continuity in the engine harness. Measure the resistance from pin 6 of the engine harness ECM connector to pin A of the blowby pressure sensor harness connector. Measure the resistance from pin 25 of the engine harness ECM connector to pin C of the blowby pressure sensor harness connector. Measure the resistance from pin 17 of the engine harness ECM connector to pin B of the blowby pressure sensor harness connector. | Less than 10 ohms? | 2D-3 |
| Repair or replace the engine harness. Repair the engine harness. Refer to Procedure 019-201 in Section 19. Refer to Procedure 019-202 in Section 19. Refer to Procedure 019-204 in Section 19. Replace the engine harness. Refer to Procedure 019-043 in Section 19. | 5A |  |

#### STEP 2D-3. Check the resistance from signal pin to return pin in the ECM port.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the resistance from signal pin to return pin in the ECM port. Measure the resistance from pin 25 (signal) to pin 17 (return) in the ECM engine harness connector port. | More than 35k ohms? Replace the blowby pressure sensor. Refer to Procedure 019-011 in Section 19. | 5A |
| Less than 35k ohms? Replace the ECM. Refer to Procedure 019-031 in Section 19. | 5A |  |

### STEP 3. Check the engine harness.

#### STEP 3A. Inspect the engine harness and ECM connector pins.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the engine harness and ECM connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? | 3B |
| A damaged connection has been detected in the ECM engine connector or engine harness connector. Repair damaged pins. Repair or replace the engine harness, or replace the ECM, whichever has the damaged pins. Flush the dirt, debris, or moisture from the connector pins, use electronic contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair the engine harness. Refer to Procedure 019-204 in Section 19. Replace the engine harness. Refer to Procedure 019-043 in Section 19. Replace the ECM. Refer to Procedure 019-031 in Section 19. | 4A |  |

#### STEP 3B. Read the fault codes.

| **Conditions:** Connect all components. Connect INSITE™ electronic service tool. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Read the fault codes. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 729 active? | 3C |
| Repair complete. | 4B |  |

#### STEP 3C. Check for an open circuit.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness connector from the ECM. Disconnect the engine harness from the blowby pressure sensor. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for an open circuit. Measure the resistance from pin 25 of the engine harness ECM connector to pin C of the blowby pressure harness sensor connector. Measure the resistance from pin 6 of the engine harness ECM connector to pin A (+5-VDC supply) of the blowby pressure sensor harness connector. | Less than 10 ohms? | 3D |
| Repair or replace the engine harness. Repair the engine harness. Refer to Procedure 019-201 in Section 19. Refer to Procedure 019-202 in Section 19. Refer to Procedure 019-204 in Section 19. Replace the engine harness. Refer to Procedure 019-043 in Section 19. | 4A |  |

#### STEP 3D. Check for a short circuit from pin to pin.

| **Conditions:** Turn keyswitch OFF Disconnect the engine harness from the ECM. Disconnect the engine harness from the blowby pressure sensor. Disconnect the engine harness from the intake manifold air temperature sensor. Disconnect the engine harness from the ambient air pressure sensor. Disconnect the engine harness from the intake manifold pressure sensor. Disconnect the engine harness from the fuel temperature sensor. Disconnect the engine harness from the oil pressure sensor. Disconnect the engine harness from the coolant pressure sensor. Disconnect the engine harness from the coolant temperature sensor. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for a short circuit from pin to pin. Measure the resistance from pin 25 of the engine harness ECM connector to all other pins in the connector. Measure the resistance from pin 17 of the engine harness ECM connector to all other pins in the connector. Measure the resistance from pin 6 of the engine harness ECM connector to all other pins in the connector. | More than 100k ohms? | 3E |
| Repair or replace the engine harness. Repair the engine harness. Refer to Procedure 019-204 in Section 19. Replace the engine harness. Refer to Procedure 019-043 in Section 19. | 4A |  |

#### STEP 3E. Check for a short circuit to engine block ground.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness connector from the ECM. Disconnect the engine harness from the blowby pressure sensor. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for a short circuit to engine block ground. Measure the resistance from pin 25 of the engine harness ECM connector to engine block ground. Measure the resistance from pin 17 of the engine harness ECM connector to engine block ground. Measure the resistance from pin 6 of the engine harness ECM connector to engine block ground. | More than 100k ohms? Replace the ECM. Refer to Procedure 019-031 in Section 19. | 4A |
| Repair or replace the engine harness. Repair the engine harness. Refer to Procedure 019-204 in Section 19. Replace the engine harness. Refer to Procedure 019-043 in Section 19. | 4A |  |

### STEP 4. Clear the fault codes.

#### STEP 4A. Disable the fault code.

| **Conditions:** Connect all components. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Disable the fault code. Start the engine and let it idle for 1 minute. Use INSITE™ electronic service tool to verify that Fault Code 729 is inactive. | Fault Code 729 inactive? | 4B |
| Return to the troubleshooting steps or contact a Cummins® Authorized Repair Location if all steps have been completed and checked again. | 1A |  |

#### STEP 4B. Clear the inactive fault codes.

| **Conditions:** Connect all components. Connect INSITE™ electronic service tool. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Clear the inactive fault codes. Use INSITE™ electronic service tool to clear the inactive fault codes. | All fault codes cleared | Repair complete |
| Troubleshoot any remaining active fault codes. | Appropriate troubleshooting charts |  |
