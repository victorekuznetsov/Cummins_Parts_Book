---
aliases:
  - "Самопроизвольный останов двигателя"
type: "Процедура"
doc: "513-t02-1008"
title_en: "Un-requested Engine Stop"
title_ru: "Самопроизвольный останов двигателя"
modified: "2019-10-17"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "5411480"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-t02-1008.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-t02-1008.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/513"
---

# Un-requested Engine Stop
**Самопроизвольный останов двигателя**

> [!abstract] Процедура · `513-t02-1008`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[5411480 — C Command Connect and Connect Premier Marine Panel Systems PS102, PS103 and PS108 Mas|5411480]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2019-10-17
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-t02-1008.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-t02-1008.pdf)

Printable Version

### Symptoms

- The engine shuts OFF without the operator switching OFF the system enable switch at the helm or customer interface box (C.I.B).

### How To Use This Tree

This symptom tree can be used to troubleshoot engine shutoff symptoms. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.

### Shoptalk

PS102 Systems came equipped with Start Switch and Stop Switches.

PS103 Systems came with a single START/STOP button that is a momentary switch or button.

PS103 Starting systems are engine control module controlled rather than C.I.B. controlled.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check C.I.B. |  |
|  | **STEP 1A.** Check the circuit breaker on the C.I.B. | Circuit breaker open or popped? |
|  | **STEP 1B.** Check keyswitch signal at the C.I.B. | Equal to battery voltage? |
|  | **STEP 1C.** Check the START/STOP switch/button (helm). | Greater than 100k ohms resistance when switch is in OFF position? |
| STEP 2. | Check main extension wiring harness. |  |
|  | **STEP 2A.** Inspect the main extension harness. | Dirty or damaged pins? |
|  | **STEP 2B.** Check the main extension wiring harness for a pin-to-pin short in the keyswitch. | Greater than 100k ohms resistance? |
| STEP 3. | Check the helm. |  |
|  | **STEP 3A.** Inspect the helm harness. | Dirty or damaged pins? |
|  | **STEP 3B.** Check the helm wiring harness for a pin-to-pin short in the keyswitch. | Greater than 100k ohms resistance? |
|  | **STEP 3C.** Check the stop switch (helm). | Greater than 100K ohms resistance when switch is in OFF position? |
| STEP 4. | Check the original equipment manufacturer (OEM) interface harness. |  |
|  | **STEP 4A.** Inspect the OEM interface harness. | Dirty or damaged pins? |
|  | **STEP 4B.** Check the OEM interface wiring harness for an open circuit in the fire suppression circuit. | Less than 10 ohms? |
| STEP 5. | Check the engine interface harness. |  |
|  | **STEP 5A.** Inspect the engine interface harness. | Dirty or damaged pins? |
|  | **STEP 5B.** Check the engine interface wiring harness for a pin-to-pin short in the keyswitch. | Greater than 100k ohms resistance? |
| STEP 6. | Check the engine wiring harness. |  |
|  | **STEP 6A.** Inspect the engine wiring harness. | Dirty or damaged pins? |
|  | **STEP 6B.** Check the engine wiring harness for a pin-to-pin short in the start signal. | Greater than 100k ohms resistance? |

### STEP 1. Check C.I.B.

#### STEP 1A. Check the circuit breaker on the C.I.B.

| **Conditions:** Turn system enable switch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the circuit breaker on the C.I.B. Check circuit breaker on C.I.B. | Circuit breaker open or popped? **YESRepair:** Reset circuit breaker on the C.I.B. Refer to Procedure 015-023 in Section 15. | 1B |
| Circuit breaker open or popped? **NO** | Repair complete |  |

#### STEP 1B. Check keyswitch signal at the C.I.B.

| **Conditions:** Open up the customer interface box. Disconnect the engine interface wiring harness from the C.I.B. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check keyswitch signal at the C.I.B. Place one lead on the keyswitch SIGNAL pin 9 of the C.I.B. connector (mating to the engine interface harness). Place the other lead on RETURN pin 4 of the C.I.B. connector (mating to the engine interface harness). Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general multimeter usage techniques. [[99-019-359 — Multimeter Usage\|Refer to Procedure 019-359 in Section 19.]] | Equal to battery voltage? **YES** | 4A |
| Equal to battery voltage? **NO** | 1C |  |

#### STEP 1C. Check the START/STOP switch/button (helm).

| **Conditions:** Disconnect the start/stop switch/button at the helm. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance. Measure the resistance of the START switch / button. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Greater than 100k ohms resistance when switch is in OFF position? **YES** | 2A |
| Greater than 100k ohms resistance when switch is in OFF position? **NORepair:** Replace the START switch. For PS102 systems: [[513-015-101 — Start Switch\|Refer to Procedure 015-101 in Section 15.]] For PS103 systems: [[513-015-109 — Start Stop Switch\|Refer to Procedure 015-109 in Section 15.]] | Repair complete. |  |

### STEP 2. Check main extension wiring harness.

#### STEP 2A. Inspect the main extension harness.

| **Conditions:** Turn system enable switch OFF. Disconnect the main extension harness from the C.I.B. Disconnect the main extension harness from the helm harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the main extension harness. Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the harness connector. Clean the connector and pins. Repair the damaged harness, connector, or pins, if possible. For the main extension harness: Refer to Procedure 015-077 in Section 15. For the C.I.B.: Refer to Procedure 015-023 in Section 15. | Repair complete. |
| Dirty or damaged pins? **NO** | 2B |  |

#### STEP 2B. Check the main extension wiring harness for a pin-to-pin short in the keyswitch.

| **Conditions:** Turn system enable switch OFF. Disconnect all mating harnesses to the main extension harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the main extension wiring harness for a pin-to-pin short in the keyswitch. Measure the resistance between the keyswitch SIGNAL pin in the main extension harness connector and all other pins in the main extension harness connector. Measure the resistance between the stop SIGNAL pin in the main extension harness connector and all other pins in the main extension harness connector. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Greater than 100k ohms resistance? **YES** | 3A |
| Greater than 100k ohms resistance? **NORepair:** A short circuit has been detected in the stop signal. Repair or replace the main extension wiring harness. Refer to Procedure 015-077 in Section 15. | Repair complete |  |

### STEP 3. Check the helm.

#### STEP 3A. Inspect the helm harness.

| **Conditions:** Turn system enable switch OFF. Disconnect the helm harness from the main extension harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the helm harness. Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the harness connector. Clean the connector and pins. Repair the damaged harness, connector, or pins, if possible. For the helm harness: Refer to Procedure 015-078 in Section 15. For the main extension harness: Refer to Procedure 015-077 in Section 15. | Repair complete. |
| Dirty or damaged pins? **NO** | 3B |  |

#### STEP 3B. Check the helm wiring harness for a pin-to-pin short in the keyswitch.

| **Conditions:** Turn system enable switch OFF. Disconnect all mating harnesses to the helm harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the helm wiring harness for a pin-to-pin short in the keyswitch. Measure the resistance between the keyswitch SIGNAL pin in the helm harness connector and all other pins in the helm harness connector. Measure the resistance between the stop SIGNAL pin in the helm harness connector and all other pins in the helm harness connector. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Greater than 100k ohms resistance? **YES** | 3C |
| Greater than 100k ohms resistance? **NORepair:** A short circuit has been detected in the stop signal. Repair or replace the helm wiring harness. Refer to Procedure 015-078 in Section 15. | Repair complete |  |

#### STEP 3C. Check the stop switch (helm).

| **Conditions:** Disconnect the stop switch. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the stop switch (helm). Measure the resistance between pin 2 and pin 3 at the stop switch. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Greater than 100k ohms resistance when switch is in OFF position? **YESRepair:** Replace the C.I.B. Refer to Procedure 015-023 in Section 15. | Repair complete |
| Greater than 100k ohms resistance when switch is in OFF position? **NORepair:** Replace the start switch. [[513-015-101 — Start Switch\|Refer to Procedure 015-101 in Section 15.]] | Repair complete |  |

### STEP 4. Check the OEM interface harness.

#### STEP 4A. Inspect the OEM interface wiring harness.

| **Conditions:** Turn system enable switch OFF. Disconnect OEM interface wiring harness from the C.I.B. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the OEM interface wiring harness. Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Greater than 100k ohms resistance when switch is in OFF position? **YESRepair:** A damaged connection has been detected in the harness connector. Clean the connector and pins. Repair the damaged harness, connector, or pins, if possible. For the OEM interface wiring harness: Refer to Procedure 015-104 in Section 15. | Repair complete. |
| Greater than 100k ohms resistance when switch is in OFF position? **NO** | 4B |  |

#### STEP 4B. Check the OEM interface wiring harness for an open circuit in the fire suppression circuit.

| **Conditions:** Turn system enable switch OFF. Disconnect OEM Interface wiring harness from the C.I.B. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the OEM interface wiring harness for an open circuit in the fire suppression circuit. Measure the resistance across the fire suppression circuit pins 6 and 7 on the OEM interface wiring harness connector (mating to the C.I.B.). Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Less than 10 ohms? **YES** | 5A |
| Less than 10 ohms? **NORepair:** An open in the fire suppression circuit has been detected. Repair the OEM interface wiring harness and interconnects. Refer to Procedure 015-104 in Section 15. | Repair complete |  |

### STEP 5. Check engine interface harness.

#### STEP 5A. Inspect the engine interface harness.

| **Conditions:** Turn system enable switch OFF. Disconnect the engine interface harness from the OEM interface panel. Disconnect the engine interface harness from the C.I.B. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the engine interface harness. Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the harness connector. Clean the connector and pins. Repair the damaged harness, connector, or pins, if possible. For the engine interface harness: Refer to Procedure 015-093 in Section 15. | Repair complete. |
| Dirty or damaged pins? **NO** | 5B |  |

#### STEP 5B. Check the engine interface wiring harness for a pin-to-pin short in the keyswitch.

| **Conditions:** Turn system enable switch OFF. Disconnect the engine interface harness from the OEM interface panel. Disconnect the engine interface harness from the C.I.B. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the engine interface wiring harness for a pin-to-pin short in the keyswitch. Measure the resistance between the keyswitch signal in the engine interface harness connector and all other pins in the engine interface harness connector. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Greater than 100k ohms resistance? **YESRepair:** Connect all components and verify that the vessel is operational. | 6A |
| Greater than 100k ohms resistance? **NORepair:** A short circuit has been detected in the start signal. Repair or replace the engine interface harness. Refer to Procedure 015-093 in Section 15. | Repair complete |  |

### STEP 6. Check engine wiring harness.

#### STEP 6A. Inspect the engine wiring harness.

| **Conditions:** Turn system enable switch OFF. Disconnect the engine harness from the engine control module (ECM). Disconnect the engine interface wiring harness from the OEM interface panel. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the engine wiring harness. Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the harness connector. Clean the connector and pins. Repair the damaged harness, connector, or pins, if possible. For the engine wiring harness: Reference Procedure 019-043 in Section 19 of the appropriate engine service manual. | Repair complete. |
| Dirty or damaged pins? **NO** | 6B |  |

#### STEP 6B. Check the engine wiring harness for a pin-to-pin short in the start signal.

| **Conditions:** Turn system enable switch OFF. Disconnect engine wiring harness from the ECM. Disconnect engine wiring harness from the OEM interface panel. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the engine wiring harness for a pin-to-pin short in the start signal. Measure the resistance between the keyswitch SIGNAL pin in the engine wiring harness connector and all other pins in the engine wiring harness connector (mating to the OEM interface panel). Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Greater than 100k ohms resistance? **YESRepair:** Reference the Engine Starts But Will Not Keep Running Troubleshooting Symptom tree in Section TT of the appropriate engine service manual. | Repair complete |
| Greater than 100k ohms resistance? **NORepair:** A short circuit has been detected in the keyswitch signal. Repair or replace the engine wiring harness. Reference Procedure 019-043 in Section 19 of the appropriate engine service manual. | Repair complete |  |
