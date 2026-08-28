---
type: "Процедура"
doc: "513-t02-1004"
title_en: "Unrequested Engine Start"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-t02-1004.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-t02-1004.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/513"
---

# Unrequested Engine Start

> [!abstract] Процедура · `513-t02-1004`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[5411480 — C Command Connect and Connect Premier Marine Panel Systems PS102, PS103 and PS108 Mas|5411480]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2019-09-27
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-t02-1004.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-t02-1004.pdf)

Printable Version

### Symptoms

- Engine cranks without the operator pushing the start button at the helm or customer interface box (CIB).

### How To Use This Tree

This symptom tree can be used to troubleshoot unrequested engine start symptoms. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform depending on the symptom.

### Shoptalk

PS102 Systems came equipped with Start Switch and Stop Switches

PS103 Systems came with a single start/stop button that is a momentary switch or button

PS103 Starting systems are engine control module controlled rather than CIB controlled.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check CIB. |  |
|  | **STEP 1A.** Check the starter voltage from the CIB. | Approximate battery voltage? |
|  | **STEP 1B.** Check the Start/Stop switch (CIB). | Greater than 100k ohms resistance when switch is in OFF position? |
| STEP 2. | Check the start switch/button (helm). |  |
|  | **STEP 2A.** Check the start switch/button (helm). | Greater than 100k ohms resistance when switch is in OFF position? |
| STEP 3. | Check the helm harness. |  |
|  | **STEP 3A.** Inspect the helm harness. | Dirty or damaged pins? |
|  | **STEP 3B.** Check the helm wiring harness for a pin-to-pin short in the keyswitch. | Greater than 100k ohms resistance? |
| STEP 4. | Check main extension wiring harness. |  |
|  | **STEP 4A.** Inspect the main extension harness. | Dirty or damaged pins? |
|  | **STEP 4B.** Check the main extension wiring harness for a pin-to-pin short in the keyswitch. | Greater than 100k ohms resistance? |
| STEP 5. | Check the engine interface harness. |  |
|  | **STEP 5A.** Inspect the engine interface harness. | Dirty or damaged pins? |
|  | **STEP 5B.** Check the engine interface wiring harness for a pin-to-pin short in the keyswitch. | Greater than 100k ohms resistance? |
| STEP 6. | Check the engine wiring harness. |  |
|  | **STEP 6A.** Inspect the engine wiring harness. | Dirty or damaged pins? |
|  | **STEP 6B.** Check the engine wiring harness for a pin-to-pin short in the start signal. | Greater than 100k ohms resistance? |
|  | **STEP 6C.** Check the starter voltage. | Equal to battery voltage? |

### STEP 1. Check CIB.

#### STEP 1A. Check the starter voltage from the CIB.

| **Conditions:** Turn the system enable switch ON Disconnect the engine interface wiring harness from the CIB. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Place one lead on the start SIGNAL pin 10 of the CIB connector (mating to the engine interface wiring harness). Place the other lead on the ground pin 4 of the CIB connector (mating to the engine interface wiring harness). | Approximate battery voltage? **YES** | 1B |
| Approximate battery voltage? **NO** | 5B |  |

#### STEP 1B. Check the Start/Stop switch (CIB).

| **Conditions:** Open the CIB. Refer to Procedure 015-023 in Section 15. Disconnect the start/stop switch. Refer to Procedure 015-109 in Section 15. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance between pin 2 and pin 3 at the start/stop switch connector. | Greater than 100k ohms resistance when switch is in OFF position? **YES** | 2A |
| Greater than 100k ohms resistance when switch is in OFF position? **NORepair:** Replace the start/stop switch. [[513-015-109 — Start Stop Switch\|Refer to Procedure 015-109 in Section 15.]] | Repair complete. |  |

### STEP 2. Check the start switch/button (helm).

#### STEP 2A. Check the start switch/button (helm).

| **Conditions:** Disconnect the start switch/button at the helm. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance of the start switch/button. Refer to wiring diagram for connector pin identification. | Greater than 100k ohms resistance when switch is in OFF position? **YES** | 3A |
| Greater than 100k ohms resistance when switch is in OFF position? **NORepair:** Replace the start/stop switch. For PS102 systems: [[513-015-101 — Start Switch\|Refer to Procedure 015-101 in Section 15.]] For PS103 systems: [[513-015-109 — Start Stop Switch\|Refer to Procedure 015-109 in Section 15.]] | Repair complete. |  |

### STEP 3. Check the helm harness.

#### STEP 3A. Inspect the helm harness.

| **Conditions:** Turn system enable switch OFF. Disconnect the helm harness from the main extension harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the harness connector. Clean the connector and pins. Repair the damaged harness, connector, or pins, if possible. For the helm harness: Refer to Procedure 015-078 in Section 15. For the main extension harness: Refer to Procedure 015-077 in Section 15. | Repair complete. |
| Dirty or damaged pins? **NO** | 3B |  |

#### STEP 3B. Check the helm wiring harness for a pin-to-pin short in the keyswitch.

| **Conditions:** Turn system enable switch OFF. Disconnect all mating harnesses to the helm harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance between the start SIGNAL pin 10 in the helm harness connector and all other pins in the helm harness connector. | Greater than 100k ohms resistance? **YES** | 4A |
| Greater than 100k ohms resistance? **NORepair:** A short circuit has been detected in the start signal. Repair or replace the helm wiring harness. Refer to Procedure 015-078 in Section 15. | Repair complete. |  |

### STEP 4. Check main extension wiring harness.

#### STEP 4A. Inspect the main extension harness.

| **Conditions:** Turn system enable switch OFF. Disconnect the main extension harness from the CIB. Disconnect the main extension harness from the helm harness |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the harness connector. Clean the connector and pins. Repair the damaged harness, connector, or pins, if possible. For the main extension harness: Refer to Procedure 015-077 in Section 15. For the CIB: Refer to Procedure 015-023 in Section 15. | Repair complete. |
| Dirty or damaged pins? **NO** | 4B |  |

#### STEP 4B. Check the main extension wiring harness for a pin-to-pin short in the keyswitch.

| **Conditions:** Turn system enable switch OFF. Disconnect all mating harnesses to the main extension harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance between the start SIGNAL pin in the main extension harness connector and all other pins in the main extension harness connector. | Greater than 100k ohms resistance? **YESRepair:** A malfunctioning CIB has been detected. Replace the CIB Refer to Procedure 015-023 in Section 15. | Repair complete. |
| Greater than 100k ohms resistance? **NORepair:** A short circuit has been detected in the start signal. Repair or replace the main extension wiring harness. Refer to Procedure 015-077 in Section 15. | Repair complete. |  |

### STEP 5. Check engine interface harness.

#### STEP 5A. Inspect the engine interface harness.

| **Conditions:** Turn system enable switch OFF. Disconnect the engine interface harness from the original equipment manufacturer (OEM) interface panel. Disconnect the engine interface harness from the CIB. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the harness connector. Clean the connector and pins. Repair the damaged harness, connector, or pins, if possible. For the engine interface harness: Refer to Procedure 015-093 in Section 15. | Repair complete. |
| Dirty or damaged pins? **NO** | 5B |  |

#### STEP 5B. Check the engine interface wiring harness for a pin-to-pin short in the keyswitch.

| **Conditions:** Turn system enable switch OFF. Disconnect the engine interface harness from the OEM interface panel. Disconnect the engine interface harness from the CIB. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance between the start SIGNAL pin 24 in the engine interface harness connector and all other pins in the engine interface harness connector. | Greater than 100k ohms resistance? **YESRepair:** Connect all components and verify that the vessel is operational. | 6A |
| Greater than 100k ohms resistance? **NORepair:** A short circuit has been detected in the start signal. Repair or replace the engine interface harness. Refer to Procedure 015-093 in Section 15. | Repair complete. |  |

### STEP 6. Check engine wiring harness.

#### STEP 6A. Inspect the engine wiring harness.

| **Conditions:** Turn system enable switch OFF. Disconnect the engine interface wiring harness from the OEM interface panel. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the harness connector. Clean the connector and pins. Repair the damaged harness, connector, or pins, if possible. For the engine wiring harness: Reference Procedure 019-043 in Section 19 of the appropriate engine service manual. | Repair complete. |
| Dirty or damaged pins? **NO** | 6B |  |

#### STEP 6B. Check the engine wiring harness for a pin-to-pin short in the start signal.

| **Conditions:** Turn system enable switch OFF. Disconnect engine interface wiring harness from the OEM interface panel. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance between the start SIGNAL pin 24 at the OEM interface connector and all other pins in the OEM interface connector. | Greater than 100k ohms resistance? **YES** | 6C |
| Greater than 100k ohms resistance? **NORepair:** A short circuit has been detected in the start signal. Repair or replace the main extension wiring harness. Reference Procedure 019-043 in Section 19 of the appropriate engine service manual. | Repair complete. |  |

#### STEP 6C. Check the starter voltage.

| **Conditions:** Connect all components. Turn system enable switch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Place one test lead on the magnetic start terminal and the other lead to ground at the starter. | Equal to battery voltage? **YESRepair:** Starter issue has been detected. For Starter Magnetic Switch: Reference Procedure 013-017 in Section 13 of the appropriate engine service manual. For Starter Solenoid: Reference Procedure 013-019 in Section 13 of the appropriate engine service manual. | Repair complete. |
| Equal to battery voltage? **NORepair:** Go to the Engine Will Not Shut Off Symptom Tree in the appropriate service manual. | Repair complete. |  |
