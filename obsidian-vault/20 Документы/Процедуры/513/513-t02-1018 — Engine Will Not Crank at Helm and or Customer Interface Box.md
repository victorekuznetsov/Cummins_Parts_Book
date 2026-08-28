---
type: "Процедура"
doc: "513-t02-1018"
title_en: "Engine Will Not Crank at Helm and/or Customer Interface Box"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-t02-1018.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-t02-1018.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/513"
---

# Engine Will Not Crank at Helm and/or Customer Interface Box

> [!abstract] Процедура · `513-t02-1018`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[5411480 — C Command Connect and Connect Premier Marine Panel Systems PS102, PS103 and PS108 Mas|5411480]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2019-09-27
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-t02-1018.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-t02-1018.pdf)

Printable Version

### Symptoms

- The engine will **not** crank when start button is pressed.

### How To Use This Tree

This symptom tree can be used to troubleshoot engine starting symptoms. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.

### Shoptalk

To initiate engine crank, the following panel parameters **must** be met:

- The system enable switch is turned to the ON position

- The engine is stopped

- Main throttle and backup throttle in neutral position

- Throttle is in neutral position

- Battery disconnect is switched ON.

Possible causes are:

- Start is shorted or open

- Start switch malfunction

- Neutral safety circuit open

- Starter lockout on engine is engaged.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the breaker and switches. |  |
|  | **STEP 1A.** Check the breaker on the customer interface box (CIB). | Breaker open or popped? |
|  | **STEP 1B.** Check the starter voltage. | Equal to battery voltage? |
| STEP 2. | Check the engine wiring harness. |  |
|  | **STEP 2A.** Inspect the engine wiring harness. | Dirty or damaged pins? |
|  | **STEP 2B.** Check the engine wiring harness for a pin-to-pin short in the start signal. | Greater than 100k ohms resistance? |
|  | **STEP 2C.** Check the engine wiring harness for an open in the start. | Less than 10 ohms resistance? |
| STEP 3. | Check the engine interface harness. |  |
|  | **STEP 3A.** Inspect the engine interface harness. | Dirty or damaged pins? |
|  | **STEP 3B.** Check the engine interface wiring harness for a pin-to-pin short in the start. | Greater than 100k ohms resistance? |
|  | **STEP 3C.** Check the engine interface wiring harness for an open in the start. | Less than 10 ohms resistance? |
| STEP 4. | Check the original equipment manufacturer (OEM) interface harness. |  |
|  | **STEP 4A.** Inspect the OEM interface wiring harness. | Dirty or damaged pins? |
|  | **STEP 4B.** Check the OEM interface wiring harness for an open circuit in the neutral safety circuit. | Less than 10 ohms? |
| STEP 5. | Check the drive application harness. |  |
|  | **STEP 5A.** Inspect the drive application wiring harness. | Dirty or damaged pins? |
|  | **STEP 5B.** Check the drive application wiring harness for an open circuit in the neutral safety circuit. | Less than 10 ohms? |
| STEP 6. | Check the CIB. |  |
|  | **STEP 6A.** Check the starter lockout relay in the CIB. | LED for starter lockout illuminated? |
|  | **STEP 6B.** Check the start/stop switch (CIB). | Less than 10 ohms resistance when switch is in ON position? |
|  | **STEP 6C.** Check the starter voltage from the CIB. | Approximate battery voltage? |
| STEP 7. | Check main extension wiring harness. |  |
|  | **STEP 7A.** Inspect the main extension harness. | Dirty or damaged pins? |
|  | **STEP 7B.** Check the main extension wiring harness for a pin-to-pin short in the start. | Greater than 100k ohms resistance? |
|  | **STEP 7C.** Check the main extension wiring harness for an open in the start. | Less than 10 ohms resistance? |
| STEP 8. | Check the helm. |  |
|  | **STEP 8A.** Check the start switch (helm). | Less than 10 ohms resistance when switch is in ON position? |
|  | **STEP 8B.** Inspect the helm harness. | Dirty or damaged pins? |
|  | **STEP 8C.** Check the helm wiring harness for a pin-to-pin short in the start. | Greater than 100k ohms resistance? |
|  | **STEP 8D.** Check the helm wiring harness for an open in the start. | Less than 10 ohms resistance? |

### STEP 1. Check the breaker and switches.

#### STEP 1A. Check the breaker on the CIB.

| **Conditions:** Turn system enable switch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the breaker on the CIB. Check the circuit breaker on CIB. | Breaker open or popped? **YESRepair:** Reset breaker on the CIB. Refer to Procedure 015-023 in Section 15. | Repair complete. |
| Breaker open or popped? **NO** | 1B |  |

#### STEP 1B. Check the starter voltage.

| **Conditions:** Turn system enable switch ON. Press and hold the start/stop switch in the start position (CIB). |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the starter voltage. Place one test lead on the magnetic start terminal and the other lead to ground at the starter. | Equal to battery voltage? **YESRepair:** Starter issue has been detected. For starter magnetic switch: Reference Procedure 013-017 in Section 13 of the appropriate engine service manual. For starter solenoid: Reference Procedure 013-019 in Section 13 of the appropriate engine service manual. | Repair complete. |
| Equal to battery voltage? **NO** | 2A |  |

### STEP 2. Check the engine wiring harness.

#### STEP 2A. Inspect the engine wiring harness.

| **Conditions:** Turn system enable switch OFF. Disconnect the engine interface wiring harness from the OEM interface panel. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the engine wiring harness. Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Wire insulation damage Connector shell broken Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the harness connector. Clean the connector and pins. Repair the damaged harness, connector, or pins, if possible. For the engine wiring harness: Reference Procedure 019-043 in Section 19 of the appropriate engine service manual. | Repair complete. |
| Dirty or damaged pins? **NO** | 2B |  |

#### STEP 2B. Check the engine wiring harness for a pin-to-pin short in the start signal.

| **Conditions:** Turn system enable switch OFF. Disconnect engine interface wiring harness from the OEM interface panel. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the engine wiring harness for a pin-to-pin short in the start signal. Measure the resistance between the start SIGNAL pin 24 in the OEM interface panel connector and all other pins in the engine wiring harness connector. | Greater than 100k ohms resistance? **YESRepair:** Reroute the harness. | 2C |
| Greater than 100k ohms resistance? **NORepair:** A pin-to-pin short circuit has been detected in the start signal. Repair or replace the engine wiring harness. Reference Procedure 019-043 in Section 19 of the appropriate engine service manual. | Repair complete. |  |

#### STEP 2C. Check the engine wiring harness for an open in the start.

| **Conditions:** Turn system enable switch OFF. Disconnect engine wiring harness from the engine control module (ECM). Disconnect engine wiring harness from the OEM interface panel. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the engine wiring harness for an open in the start. Measure the resistance between the start SIGNAL pin 24 at the OEM interface panel connector and start signal at the starter magnetic switch. | Less than 10 ohms resistance? **YES** | 3A |
| Less than 10 ohms resistance? **NORepair:** An open circuit has been detected in the start. Repair or replace the engine wiring harness. Reference Procedure 019-043 in Section 19 of the appropriate engine service manual. | Repair complete. |  |

### STEP 3. Check the engine interface harness.

#### STEP 3A. Inspect the engine interface harness.

| **Conditions:** Turn system enable switch OFF. Disconnect the engine interface harness from the OEM interface panel. Disconnect the engine interface harness from the CIB. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the engine interface harness. Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the harness connector. Clean the connector and pins. Repair the damaged harness, connector, or pins, if possible. For the engine interface harness: Refer to Procedure 015-093 in Section 15. | Repair complete. |
| Dirty or damaged pins? **NO** | 3B |  |

#### STEP 3B. Check the engine interface wiring harness for a pin-to-pin short in the start.

| **Conditions:** Turn system enable switch OFF. Disconnect the engine interface harness from the OEM interface panel. Disconnect the engine interface harness from the CIB. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the engine interface wiring harness for a pin-to-pin short in the start. Measure the resistance between the start SIGNAL pin 24 in the engine interface harness connector and all other pins in the engine interface harness connector. | Greater than 100k ohms resistance? **YES** | 3C |
| Greater than 100k ohms resistance? **NORepair:** A short circuit has been detected in the start. Repair or replace the engine interface harness. Refer to Procedure 015-093 in Section 15. | Repair complete. |  |

#### STEP 3C. Check the engine interface wiring harness for an open in the start.

| **Conditions:** Turn system enable switch OFF. Disconnect the engine interface harness from the OEM interface panel. Disconnect the engine interface harness from the CIB. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the engine interface wiring harness for an open in the start. Measure the resistance between the start SIGNAL pin 24 in the engine interface harness connector (mating to the OEM interface panel) and start SIGNAL pin 10 in the engine interface connector (mating to the CIB). | Less than 10 ohms resistance? **YES** | 4A |
| Less than 10 ohms resistance? **NORepair:** A open circuit has been detected in the start. Repair or replace the engine interface harness. Refer to Procedure 015-093 in Section 15. | Repair complete. |  |

### STEP 4. Check the OEM interface harness.

#### STEP 4A. Inspect the OEM interface wiring harness.

| **Conditions:** Turn system enable switch OFF. Disconnect OEM interface wiring harness from the CIB. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the OEM interface wiring harness. Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the harness connector. Clean the connector and pins. Repair the damaged harness, connector, or pins, if possible. For the OEM interface wiring harness: Refer to Procedure 015-104 in Section 15. | Repair complete. |
| Dirty or damaged pins? **NO** | 4B |  |

#### STEP 4B. Check the OEM interface wiring harness for an open circuit in the neutral safety circuit.

| **Conditions:** Turn system enable switch OFF. Disconnect OEM interface wiring harness from the CIB. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the OEM interface wiring harness for an open circuit in the neutral safety circuit. Measure the resistance across the neutral safety circuit pins 11 and 12 on the OEM interface wiring harness connector. | Less than 10 ohms? **YES** | 5A |
| Less than 10 ohms? **NORepair:** An open in the neutral safety circuit has been detected. Repair the OEM interface wiring harness and interconnects. Refer to Procedure 015-104 in Section 15. | Repair complete. |  |

### STEP 5. Check the drive application harness.

#### STEP. Inspect the drive application wiring harness.

| **Conditions:** Turn system enable switch OFF. Disconnect drive application wiring harness from the CIB. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the drive application wiring harness. Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the harness connector. Clean the connector and pins. Repair the damaged harness, connector, or pins, if possible. Repair the OEM interface wiring harness. Refer to Procedure 015-104 in Section 15. | Repair complete. |
| Dirty or damaged pins? **NO** | 5B |  |

#### STEP 5B. Check the drive application wiring harness for an open circuit in the neutral safety circuit.

| **Conditions:** Turn system enable switch OFF. Disconnect drive application wiring harness from engine wiring harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the drive application wiring harness for an open circuit in the neutral safety circuit. Measure the resistance across the neutral safety circuit pins 10 and 11 on the drive application wiring harness connector (mating to the engine wiring harness). | Less than 10 ohms? **YES** | 6A |
| Less than 10 ohms? **NORepair:** An open in the neutral safety circuit has been detected. Repair the OEM interface wiring harness and interconnects. Refer to Procedure 015-099 in Section 15. | Repair complete. |  |

### STEP 6. Check the C.I.B.

#### STEP 6A. Check the starter lockout relay in the CIB.

| **Conditions:** Open up the CIB. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the starter lockout relay in the CIB. Locate the starter lockout relay LED. Refer to Procedure 015-023 in Section 15. | LED for starter lockout illuminated? **YESRepair:** The ECM has locked out the engine from starting. Investigate engine with INSITE™ electronic service tool for related fault codes. | Repair complete |
| LED for starter lockout illuminated? **NO** | 6B |  |

#### STEP 6B. Check the start/stop switch (CIB).

| **Conditions:** Open the CIB. Disconnect the start/stop switch. Refer to Procedure 015-109 in Section 15. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the start/stop switch (CIB). Measure the resistance between pin 2 and pin 3 at the start/stop switch connector. | Less than 10 ohms resistance when switch is in ON position? **YES** | 6C |
| Less than 10 ohms resistance when switch is in ON position? **NORepair:** Replace the start/stop switch. [[513-015-109 — Start Stop Switch\|Refer to Procedure 015-109 in Section 15.]] | Repair complete. |  |

#### STEP 6C. Check the starter voltage from the CIB.

| **Conditions:** Turn the system enable switch ON. Disconnect the engine interface wiring harness from the CIB. Press and hold the start/stop button in the starting position. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the starter voltage from the CIB. Place one lead on the start SIGNAL pin 10 of the CIB connector (mating to the engine interface wiring harness). Place the other lead on the ground pin 4 of the CIB connector (mating to the engine interface wiring harness). | Approximate battery voltage? **YESRepair:** The ECM has locked out the engine from starting. Investigate engine with INSITE™ electronic service tool for related fault codes. | Repair complete. |
| Approximate battery voltage? **NO** | 7A |  |

### STEP 7. Check main extension wiring harness.

#### STEP 7A. Inspect the main extension harness.

| **Conditions:** Turn system enable switch OFF. Disconnect the main extension harness from the CIB. Disconnect the main extension harness from the helm harness |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the main extension harness. Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** Repair the damaged harness, connector, or pins, if possible. For the main extension harness: Refer to Procedure 015-077 in Section 15. For the CIB: Refer to Procedure 015-023 in Section 15. | Repair complete. |
| Dirty or damaged pins? **NO** | 7B |  |

#### STEP 7B. Check the main extension wiring harness for a pin-to-pin short in the start.

| **Conditions:** Turn system enable switch OFF. Disconnect the main extension harness from the CIB. Disconnect the main extension harness from the helm harness |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the main extension wiring harness for a pin-to-pin short in the start. Measure the resistance between the start SIGNAL pin in the main extension harness connector and all other pins in the main extension harness connector. | Greater than 100k ohms resistance? **YES** | 7C |
| Greater than 100k ohms resistance? **NORepair:** A short circuit has been detected in the start. Repair or replace the main extension wiring harness. Refer to Procedure 015-077 in Section 15. | Repair complete. |  |

#### STEP 7C. Check the main extension wiring harness for an open in the start.

| **Conditions:** Turn system enable switch OFF. Disconnect the main extension harness from the CIB. Disconnect the main extension harness from the helm harness |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the main extension wiring harness for an open in the start. Measure the resistance between the start SIGNAL pin 10 in the main extension harness connector (mating to the helm harness) and start SIGNAL pin 10 in the main extension connector (mating to the CIB). | Less than 10 ohms resistance? **YES** | 8A |
| Less than 10 ohms resistance? **NORepair:** An open circuit has been detected in the start. Repair or replace the main extension wiring harness. Refer to Procedure 015-077 in Section 15. | Repair complete. |  |

### STEP 8. Check the helm.

#### STEP 8A. Check the start switch (helm).

| **Conditions:** Disconnect the start switch. Refer to Procedure 015-101 in Section 15. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the start switch (helm). Measure the resistance between pin 2 and pin 3 at the system enable switch. | Less than 10 ohms resistance when switch is in ON position? **YES** | 8B |
| Less than 10 ohms resistance when switch is in ON position? **NORepair:** Replace the start switch. [[513-015-101 — Start Switch\|Refer to Procedure 015-101 in Section 15.]] | Repair complete. |  |

#### STEP 8B. Inspect the helm harness.

| **Conditions:** Turn system enable switch OFF. Disconnect the helm harness from the main extension harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the helm harness. Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the harness connector. Clean the connector and pins. Repair the damaged harness, connector, or pins, if possible. For the helm harness: Refer to Procedure 015-078 in Section 15. | Repair complete. |
| Dirty or damaged pins? **NO** | 8C |  |

#### STEP 8C. Check the helm wiring harness for a pin-to-pin short in the start.

| **Conditions:** Turn system enable switch OFF. Disconnect all mating harnesses to the helm harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the helm wiring harness for a pin-to-pin short in the start. Measure the resistance between the start SIGNAL pin 10 in the helm harness connector (mating to the main extension) and all other pins in the helm harness connector. | Greater than 100k ohms resistance? **YES** | 8D |
| Greater than 100k ohms resistance? **NORepair:** A short circuit has been detected in the start. Repair or replace the helm wiring harness. Refer to Procedure 015-078 in Section 15. | Repair complete. |  |

#### STEP 8D. Check the helm wiring harness for an open in the start.

| **Conditions:** Turn system enable switch OFF. Disconnect all mating harnesses to the helm harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the helm wiring harness for an open in the start. Measure the resistance between the start SIGNAL pin 3 in the helm harness connector (mating to the system enable switch) and start SIGNAL pin 10 in the helm harness connector (mating to the main extension harness). | Less than 10 ohms resistance? **YESRepair:** A malfunction has been detected in the CIB. Replace the CIB. Refer to Procedure 015-023 in Section 15. | Repair complete. |
| Less than 10 ohms resistance? **NORepair:** A open circuit has been detected in the start. Repair or replace the helm wiring harness. Refer to Procedure 015-078 in Section 15. | Repair complete. |  |
