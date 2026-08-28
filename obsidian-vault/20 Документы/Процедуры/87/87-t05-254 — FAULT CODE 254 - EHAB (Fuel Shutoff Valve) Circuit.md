---
aliases:
  - "Код 254 — цепь EHAB (клапан отсечки топлива)"
type: "Процедура"
doc: "87-t05-254"
title_en: "FAULT CODE 254 - EHAB (Fuel Shutoff Valve) Circuit"
title_ru: "Код 254 — цепь EHAB (клапан отсечки топлива)"
modified: "2018-08-09"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666214"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-t05-254.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-t05-254.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
---

# FAULT CODE 254 - EHAB (Fuel Shutoff Valve) Circuit
**Код 254 — цепь EHAB (клапан отсечки топлива)**

> [!abstract] Процедура · `87-t05-254`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2018-08-09
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-t05-254.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-t05-254.pdf)

Printable Version

## Warnings and Cautions

> [!warning] CAUTION · Осторожно
> To reduce the possibility of damaging a new engine control module (ECM), all other active fault codes must be investigated prior to replacing the ECM.

> [!warning] CAUTION · Осторожно
> To reduce the possibility of pin and harness damage, use the following test leads when taking a measurement: Part Number 3822758 - male Deutsch™/AMP™/Metri-Pack™ test lead, Part Number 3822917 - female Deutsch™/AMP™/Metri-Pack™ test lead, Part Number 3823993 - male Deutsch™/AMP™/Metri-Pack™ test lead, Part Number 3163531 - EHAB breakout cable.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the EHAB (fuel shutoff valve). |  |
|  | **STEP 1A.** Check for extra wires spliced into the EHAB circuit. | No extra wires |
|  | **STEP 1B.** Inspect the engine harness and EHAB (fuel shutoff valve) connectors. | No damaged pins |
|  | **STEP 1C.** Read the fault codes. | Fault Code 254 active |
|  | **STEP 1D.** Check the EHAB (fuel shutoff valve) supply voltage. | More than 16.5 VDC |
|  | **STEP 1E.** Check the EHAB (fuel shutoff valve) supply voltage. | More than 16.5 VDC |
|  | **STEP 1E-1.** Check for an open circuit. | Less than 10 ohms |
|  | **STEP 1E-2.** Check for a short circuit to ground. | More than 100k ohms |
|  | **STEP 1E-3.** Check for a short circuit from pin to pin. | More than 100k ohms |
|  | **STEP 1E-4.** Check the ECM output voltage of pin 43. | More than 16.5 VDC |
|  | **STEP 1F.** Check the EHAB (fuel shutoff valve) resistance. | 38.5 to 43.5 ohms for 24-VDC solenoids |
| STEP 2. | Check the ECM. |  |
|  | **STEP 2A.** Inspect the engine harness and ECM connectors. | No damaged pins |
|  | **STEP 2B.** Read the fault codes. | Fault Code 254 active |
|  | **STEP 2C.** Check the supply voltage to the ECM. | More than 17.0 VDC |
|  | **STEP 2C-1.** Check the in-line fuse. | Less than 10 ohms |
|  | **STEP 2C-2.** Check for an open circuit. | Less than 10 ohms |
|  | **STEP 2C-3.** Check for a short circuit to ground. | More than 100k ohms |
|  | **STEP 2C-4.** Check for a short circuit from pin to pin. | More than 100k ohms |
|  | **STEP 2D.** Check the keyswitch voltage at the ECM. | More than 17.0 VDC |
| STEP 3. | Clear the fault codes. |  |
|  | **STEP 3A.** Disable the fault code. | Fault Code 254 inactive |
|  | **STEP 3B.** Clear the inactive fault codes. | All fault codes cleared |

### STEP 1. Check the EHAB (fuel shutoff valve).

#### STEP 1A. Check for extra wires spliced into the EHAB circuit.

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for extra wires spliced into the EHAB circuit. | No extra wires | 1B |
| Remove the extra wires | 3A |  |

#### STEP 1B. Inspect the engine harness and EHAB (fuel shutoff valve) connectors.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the EHAB (fuel shutoff valve). |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the engine harness and EHAB (fuel shutoff valve) connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | No damaged pins | 1C |
| Replace the damaged pins Flush the dirt, debris, or moisture from the connector pins. Repair or replace the engine harness, or replace the EHAB, whichever has the damaged pins. Flush the dirt, debris, or moisture from the connector pins using electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair the engine harness. Use the following procedures. Refer to Procedure 019-201 in Section 19. Refer to Procedure 019-202 in Section 19. Refer to Procedure 019-205 in Section 19. Replace the engine harness. Refer to Procedure 019-043 in Section 19. Replace the EHAB (fuel shutoff valve). Refer to Procedure 005-043 in Section 19. | 3A |  |

#### STEP 1C. Read the fault codes.

| **Conditions:** Connect all components. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Read the fault codes. Start the engine and let it idle for 1 minute. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 254 active | 1D |
| Repair complete. | 3B |  |

#### STEP 1D. Check the EHAB (fuel shutoff valve) supply voltage.

| **Conditions:** Disconnect the engine harness from the EHAB (fuel shutoff valve). Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the EHAB (fuel shutoff valve) supply voltage. Install breakout cable, Part Number 3163531, between the EHAB (fuel shutoff valve) and the engine harness. Measure the voltage from the red test lead of the breakout cable to the black test lead. | More than 16.5 VDC | 1F |
| Less than 16.5 VDC. | 1E |  |

#### STEP 1E. Check the EHAB (fuel shutoff valve) supply voltage.

| **Conditions:** Disconnect the engine harness from the EHAB (fuel shutoff valve). Disconnect breakout cable, Part Number 3163531, from the EHAB (fuel shutoff valve) and engine harness. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the EHAB (fuel shutoff valve) supply voltage. Measure the voltage from pin 2 of the engine harness EHAB (fuel shutoff valve) connector to engine block ground. | More than 16.5 VDC Replace the EHAB (fuel shutoff valve). Refer to Procedure 005-043 in Section 5. | 4A |
|  | 1E-1 |  |

#### STEP 1E-1. Check for an open circuit.

| **Conditions:** Turn keyswitch OFF. Disconnect engine harness from the ECM. Disconnect the engine harness from the EHAB (fuel shutoff valve). |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for an open circuit. Measure the resistance from pin 2 of the engine harness EHAB (fuel shutoff valve) connector to pin 43 of the engine harness connector. | Less than 10 ohms | 1E-2 |
| Repair or replace the engine harness Repair the engine harness. Use the following procedures. Refer to Procedure 019-201 in Section 19. Refer to Procedure 019-202 in Section 19. Refer to Procedure 019-205 in Section 19. Replace the engine harness. Refer to Procedure 019-043 in Section 19. | 3A |  |

#### STEP 1E-2. Check for a short circuit to ground.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM. Disconnect the engine harness from the EHAB (fuel shutoff valve). |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for a short circuit to ground. Measure the resistance from pin 43 of the engine harness connector to engine block ground. | More than 100k ohms | 1E-3 |
| Repair or replace the engine harness Repair the engine harness. Refer to Procedure 019-204 in Section 19. Replace the engine harness. Refer to Procedure 019-043 in Section 19. | 3A |  |

#### STEP 1E-3. Check for a short circuit from pin to pin.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM. Disconnect the original equipment manufacturer (OEM) harness from the ECM. Disconnect the engine harness from the EHAB (fuel shutoff valve). |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for a short circuit from pin to pin. Measure the resistance from pin 43 of the engine harness connector to all other pins in the connector, and to all pins in the OEM harness connector. | More than 100k ohms | 1E-4 |
| Repair or replace the engine harness Repair the engine harness. Refer to Procedure 019-204 in Section 19. Replace the engine harness. Refer to Procedure 019-043 in Section 19. | 3A |  |

#### STEP 1E-4. Verify ECM output voltage.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the ECM output voltage of pin 43. Measure the voltage form ECM pin 43 to engine block ground. | More than 16.5 VDC. | 1F |
| Replace the ECM. [[87-019-031 — Engine Control Module\|Refer to Procedure 019-031 in Section 19.]] | 3A |  |

#### STEP 1F. Check the EHAB (fuel shutoff valve) resistance.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the EHAB (fuel shutoff valve). |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the EHAB (fuel shutoff valve) resistance. Measure the resistance from pin 2 to pin 1 on the sensor side of the connector. | 38.5 to 43.5 ohms for 24-VDC solenoids | 3A |
| Replace the EHAB (fuel shutoff valve). Refer to Procedure 005-043 in Section 5.. | 2A |  |

### STEP 2. Check the ECM.

#### STEP 2A. Inspect the engine harness and ECM connectors.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the engine harness and ECM connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | No damaged pins | 2B |
| Replace the damaged pins Flush the dirt, debris, or moisture from the connector pins. Repair or replace the engine harness, or replace the ECM, whichever has the damaged pins. Flush the dirt, debris, or moisture from the connector pins using electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair the engine harness. Refer to Procedure 019-204 in Section 19. Replace the engine harness. Refer to Procedure 019-043 in Section 19. Replace the ECM. Refer to Procedure 019-031 in Section 19. | 3A |  |

#### STEP 2B. Read the fault codes.

| **Conditions:** Connect all components. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Read the fault codes. Start the engine and let it idle for 1 minute. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 254 active | 2C |
| Repair complete. | 3B |  |

#### STEP 2C. Check the supply voltage to the ECM.

| **Conditions:** Disconnect the engine harness from the ECM. Disconnect the engine harness from the EHAB (fuel shutoff valve). Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the supply voltage to the ECM. Measure the voltage from pin 38 of the engine harness connector ECM port to engine block ground. | More than 17.0 VDC | 2D |
|  | 2C-1 |  |

#### STEP 2C-1. Check the in-line fuse.

| **Conditions:** Turn keyswitch OFF. Disconnect the in-line fuse from the engine harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the in-line fuse. Measure the resistance across the fuse. | Less than 10 ohms | 2C-2 |
| Replace the fuse. [[99-019-198 — Fuse, Harness In-Line\|Refer to Procedure 019-198 in Section 19]]. | 3A |  |

#### STEP 2C-2. Check for an open circuit.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM. Disconnect the OEM harness from the OEM interface harness at the 21-pin connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for an open circuit. Measure the resistance from pin 38 of the engine harness connector to pin G of the 21-pin OEM harness connector. Measure the resistance from pin 39 of the engine harness connector to pin G of the 21-pin OEM harness connector. Measure the resistance from pin 40 of the engine harness connector to pin G of the 21-pin OEM harness connector. Measure the resistance from pin 50 of the engine harness connector to pin G of the 21-pin OEM harness connector. | Less than 10 ohms | 2C-3 |
| Repair or replace the engine harness Repair the engine harness. Use the following procedures. Refer to Procedure 019-208 in Section 19. Refer to Procedure 019-204 in Section 19. Replace the engine harness. Refer to Procedure 019-043 in Section 19. | 3A |  |

#### STEP 2C-3. Check for a short circuit to ground.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM. Disconnect the OEM harness from the OEM interface harness at the 21-pin connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for a short circuit to ground. Measure the resistance from pin 38 of the engine harness connector to engine block ground. | More than 100k ohms | 2C-4 |
| Repair or replace the engine harness Repair the engine harness. Refer to Procedure 019-204 in Section 19. Replace the engine harness. Refer to Procedure 019-043 in Section 19. | 3A |  |

#### STEP 2C-4. Check for a short circuit from pin to pin.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM. Disconnect the OEM harness from the ECM. Disconnect the OEM harness from the OEM interface harness at the 21-pin connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for a short circuit from pin to pin. Measure the resistance from pin 38 of the engine harness connector to all other pins in the connector, except pins 39, 40, and 50. Measure the resistance from pin 38 of the engine harness connector to all pins in the OEM harness connector. | More than 100k ohms Correct OEM power supply. | 3A |
| Repair or replace the engine harness Repair the engine harness. Refer to Procedure 019-204 in Section 19. Replace the engine harness. Refer to Procedure 019-043 in Section 19. | 3A |  |

#### STEP 2D. Check the keyswitch voltage at the ECM.

| **Conditions:** Disconnect the engine harness from the ECM. Disconnect the engine harness from the EHAB (fuel shutoff valve). Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the keyswitch voltage at the ECM. Measure the voltage from pin 5 of the engine harness connector to engine block ground. | More than 17.0 VDC Replace the ECM. [[87-019-031 — Engine Control Module\|Refer to Procedure 019-031 in Section 19]]. | 3A |
| Check the OEM keyswitch circuit Refer to the OEM service manual. | 3A |  |

### STEP 3. Clear the fault codes.

#### STEP 3A. Disable the fault code.

| **Conditions:** Connect all components. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Disable the fault code. Start the engine and let it idle for 1 minute. Use INSITE™ electronic service tool to verify that the fault code is inactive. | Fault Code 254 inactive | 3B |
| Return to troubleshooting steps or contact a Cummins® Authorized Repair Location if all steps have been completed and checked again. | 1A |  |

#### STEP 3B. Clear the inactive fault codes.

| **Conditions:** Connect all components. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Clear the inactive fault codes. Use INSITE™ electronic service tool to clear the inactive fault codes. | All fault codes cleared | Repair complete |
| Troubleshoot any remaining active fault codes. | Appropriate troubleshooting charts |  |
