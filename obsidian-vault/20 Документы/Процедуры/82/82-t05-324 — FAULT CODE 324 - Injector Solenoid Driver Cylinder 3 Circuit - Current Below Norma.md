---
aliases:
  - "Код 324 — цепь электромагнита форсунки цилиндра 3 — ток ниже нормы или обрыв"
type: "Процедура"
doc: "82-t05-324"
title_en: "FAULT CODE 324 - Injector Solenoid Driver Cylinder 3 Circuit - Current Below Normal, or Open Circuit"
title_ru: "Код 324 — цепь электромагнита форсунки цилиндра 3 — ток ниже нормы или обрыв"
modified: "2012-06-12"
engines:
  - "41343322"
  - "41370103"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-t05-324.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-t05-324.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# FAULT CODE 324 - Injector Solenoid Driver Cylinder 3 Circuit - Current Below Normal, or Open Circuit
**Код 324 — цепь электромагнита форсунки цилиндра 3 — ток ниже нормы или обрыв**

> [!abstract] Процедура · `82-t05-324`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-06-12
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-t05-324.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-t05-324.pdf)

Printable Version

## Warnings and Cautions

> [!danger] WARNING · Опасно
> The injector solenoids receive high voltage when the engine is operating. To reduce the possibility of personal injury or death from electrical shock, do not wear jewelry or damp clothing, and do not touch the injector solenoids or the solenoid wires when the engine is operating.

> [!warning] CAUTION · Осторожно
> To reduce the possibility of damaging a new ECM, all other active fault codes must be investigated prior to replacing the ECM.

> [!warning] CAUTION · Осторожно
> To reduce the possibility of pin and harness damage, use the following test leads when taking a measurement: Part Number 3822758 - male Deutsch™/AMP™/Metri-Pack™ test lead and Part Number 3822917 - female Deutsch™/AMP™/Metri-Pack™ test lead.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the fault codes. |  |
|  | **STEP 1A.** Check for active fault codes. | Fault Code 111 active? |
| STEP 2. | Check the fuel injector and circuit. |  |
|  | **STEP 2A.** Inspect the ECM and engine harness connector pins. | Dirty, loose, or damaged pins? |
|  | **STEP 2B.** Check for a circuit fault in the injector solenoid and circuit. | Is the resistance of the injector and circuit 0.5 to 2.5 ohms? |
|  | **STEP 2C.** Check for a circuit fault in the injector solenoid and circuit. | Was the resistance measured in Step 2B less than 0.5 ohms? |
| STEP 3. | Check for a short circuit in the injector solenoid and circuit. |  |
|  | **STEP 3A.** Inspect the fuel injector and connector pins. | Dirty, loose, or damaged pins? |
|  | **STEP 3B.** Check for a short circuit in the injector solenoid. | Is the resistance of the injector solenoid less than 0.5 ohms? |
|  | **STEP 3C.** Check for a short circuit in the engine harness. | Is the resistance greater than 100k ohms? |
|  | **STEP 3D.** Check for a short circuit to ground in the engine harness. | Is the resistance greater then 100k ohms? |
| STEP 4. | Check for high resistance or an open circuit in the injector solenoid and circuit. |  |
|  | **STEP 4A.** Inspect the fuel injector and connector pins. | Dirty, loose, or damaged pins? |
|  | **STEP 4B.** Check for high resistance or an open circuit in the injector solenoid. | Is the resistance of the injector solenoid greater than 1.5 ohms? |
|  | **STEP 4C.** Check for high resistance or an open circuit in the engine harness. | Is the resistance of the circuit greater than 1 ohm? |
| STEP 5. | Clear the fault codes. |  |
|  | **STEP 5A.** Disable the fault code. | Fault Code 324 inactive? |
|  | **STEP 5B.** Clear the inactive fault codes. | All fault codes cleared? |

### STEP 1. Check the fault codes.

#### STEP 1A. Check for active fault codes.

| **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for active fault codes. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 111 active? **YES** | Troubleshoot Fault Code 111 |
| Fault Code 111 active? **NO** | 2A |  |

### STEP 2. Check the fuel injector and circuit.

#### STEP 2A. Inspect the ECM and engine harness connector pins.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the engine harness and ECM connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris on or in the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty, loose, or damaged pins? **YESRepair:** Refer to the circuit diagram or wiring diagram for all harness interconnections. A damaged connection has been detected in the ECM connector or engine harness. Repair the damaged pins. Repair or replace the engine harness or replace the ECM, whichever has the damaged pins. Flush the dirt, debris, or moisture from the connector pins, use electronic contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair the engine harness. Refer to Procedure 019-204 in Section 19. Repair the damaged harness, connector, or pins, if possible. Refer to Procedure 019-043 in Section 19. Replace the ECM. Refer to Procedure 019-031 in Section 19. | 5A |
| Dirty, loose, or damaged pins? **NO** | 2B |  |

#### STEP 2B. Check for a circuit fault in the injector solenoid and circuit.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for a circuit fault in the injector solenoid and circuit. Measure the resistance between pins 6 and 16 at the ECM connector. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Is the resistance of the injector and circuit 0.5 to 2.5 ohms? **YESRepair:** Replace the ECM. Refer to Procedure 019-031 in Section 19. | 5A |
| Is the resistance of the injector and circuit 0.5 to 2.5 ohms? **NO** | 2C |  |

#### STEP 2C. Check for a circuit fault in the injector solenoid and circuit.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Use the resistance measurement from Step 2B. - | Was the resistance measured in Step 2B less than 0.5 ohms? **YES** | 3A |
| Was the resistance measured in Step 2B greater than 2.5 ohms? **NO** | 4A |  |

### STEP 3. Check for a short circuit in the injector solenoid and circuit.

#### STEP 3A. Inspect the fuel injector and connector pins.

| **Conditions:** Turn keyswitch OFF. Remove the rocker lever cover. Use the following procedure in the ISM, ISMe, and QSM11 Service Manual, Bulletin [[3666322 — ISM, ISMe, and QSM11 Service Manual\|3666322]]. Refer to Procedure 003-011 in Section 3. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the engine harness and fuel injector connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris on or in the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty, loose, or damaged pins? **YESRepair:** A damaged connection has been detected in the engine harness or fuel injector connector. Clean the connector and pins. Repair the damaged harness, connector, or pins, if possible. Refer to Procedure 019-043 in Section 19. | 5A |
| Dirty, loose, or damaged pins? **NO** | 3B |  |

#### STEP 3B. Check for a short circuit in the injector solenoid.

| **Conditions:** Turn keyswitch OFF. Remove the rocker lever cover. Use the following procedure in the ISM, ISMe, and QSM11 Service Manual, Bulletin [[3666322 — ISM, ISMe, and QSM11 Service Manual\|3666322]]. Refer to Procedure 003-011 in Section 3. Disconnect the internal actuator harness from the injector solenoid. Remove the injector solenoid wires from the solenoid. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for a short circuit in the injector solenoid. Measure the resistance from post to post on the injector solenoid. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Is the resistance of the injector solenoid less than 0.5 ohms? **YESRepair:** Replace the injector. Use the following procedure in the ISM, ISMe, and QSM11 Service Manual, Bulletin [[3666322 — ISM, ISMe, and QSM11 Service Manual\|3666322]]. [[35-006-026-tr — Injector\|Refer to Procedure 006-026 in Section 6.]] | 4A |
| Is the resistance of the injector solenoid less than 0.5 ohms? **NO** | 3C |  |

#### STEP 3C. Check for a short circuit in the engine harness.

| **Conditions:** Turn keyswitch OFF. Disconnect the injector from the engine harness. Disconnect the engine harness from the ECM connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for a short circuit in the engine harness. Measure the resistance between the injector SIGNAL (+) pin and all other pins in the engine harness ECM connector. Measure the resistance between the injector RETURN (-) pin and all other pins in the engine harness ECM connector. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Is the resistance greater than 100k ohms? **YES** | 3D |
| Is the resistance greater than 100k ohms? **NORepair:** A short circuit has been detected in the engine harness. Troubleshoot the interconnect at the rocker lever housing pass-through connector. Determine if the short circuit is in the internal harness inside the rocker lever housing or in the engine harness. Repair or replace the engine harness. Refer to Procedure 019-043 in Section 19. | 4A |  |

#### STEP 3D. Check for a short circuit to ground in the engine harness.

| **Conditions:** Turn keyswitch OFF. Disconnect the injector from the engine harness. Disconnect the engine harness from the ECM connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for a short circuit to ground in the engine harness. Measure the resistance between the injector SIGNAL (+) pin to engine block ground. Measure the resistance between the injector RETURN (-) pin to engine block ground. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Is the resistance greater then 100k ohms? **YES** | 5A |
| Is the resistance greater then 100k ohms? **NORepair:** A short circuit has been detected in the engine harness. Troubleshoot the interconnect at the rocker lever housing pass-through connector. Determine if the short circuit is in the internal harness inside the rocker lever housing or in the engine harness. Repair or replace the engine harness. Refer to Procedure 019-043 in Section 19. | 5A |  |

### STEP 4. Check for high resistance or an open circuit in the injector solenoid and circuit.

#### STEP 4A. Inspect the fuel injector and connector pins.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the engine harness and ECM connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris on or in the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty, loose, or damaged pins? **YESRepair:** A damaged connection has been detected in the ECM connector or engine harness connector. Clean the connector and pins. Repair the damaged harness, connector, or pins, if possible. Refer to Procedure 019-043 in Section 19. | 5A |
| Dirty, loose, or damaged pins? **NO** | 4B |  |

#### STEP 4B. Check for high resistance or an open circuit in the injector solenoid.

| **Conditions:** Turn keyswitch OFF. Remove the rocker lever cover. Refer to Procedure 003-011 in Section 3 of the ISM, ISMe, and QSM11 Service Manual, Bulletin [[3666322 — ISM, ISMe, and QSM11 Service Manual\|3666322]]. Disconnect the internal actuator harness from the injector solenoid. Remove the injector solenoid wires from the solenoid. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for an open circuit in the injector solenoid. Measure the resistance from post to post on the injector solenoid. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Is the resistance of the injector solenoid greater than 1.5 ohms? **YESRepair:** Replace the injector. Use the following procedure in the ISM, ISMe, and QSM11 Service Manual, Bulletin [[3666322 — ISM, ISMe, and QSM11 Service Manual\|3666322]]. [[35-006-026-tr — Injector\|Refer to Procedure 006-026 in Section 6.]] | 5A |
| Is the resistance of the injector solenoid greater than 1.5 ohms? **NO** | 4C |  |

#### STEP 4C. Check for high resistance or an open circuit in the engine harness.

| **Conditions:** Turn keyswitch OFF. Disconnect the injector from the engine harness. Disconnect the engine harness from the ECM connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for an open circuit in the engine harness. Measure the resistance between the injector SIGNAL (+) pin at the injector and pin 6 at the engine harness ECM connector. Measure the resistance between the injector RETURN (-) pin at the injector and pin 16 at the engine harness ECM connector. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Is the resistance of the circuit greater than 1 ohm? **YESRepair:** An open circuit or high resistance has been detected in the engine harness. Troubleshoot the interconnect at the rocker lever housing pass-through connector. Determine if the short circuit is in the internal harness inside the rocker lever housing or in the engine harness. Repair or replace the engine harness. Refer to Procedure 019-043 in Section 19. | 5A |
| Is the resistance of the circuit greater than 1 ohm? **NO** | 5A |  |

### STEP 5. Clear the fault codes.

#### STEP 5A. Disable the fault code.

| **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Disable the fault code. Use INSITE™ electronic service tool to verify Fault Code 324 is inactive. | Fault Code 324 inactive? **YES** | 5A |
| Fault Code 324 inactive? **NORepair:** Return to the troubleshooting steps or contact a Cummins® Authorized Repair Location if all steps have been completed and checked again. | 1A |  |

#### STEP 5B. Clear the inactive fault codes.

| **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Clear the inactive fault codes. Use INSITE™ electronic service tool to clear the inactive fault codes. | All fault codes cleared? **YES** | Repair complete |
| All fault codes cleared? **NORepair:** Troubleshoot any remaining active fault codes. | Appropriate troubleshooting chart |  |
