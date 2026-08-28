---
aliases:
  - "Стартер не отключается"
type: "Процедура"
doc: "513-t02-1007"
title_en: "Starter Does Not Disengage"
title_ru: "Стартер не отключается"
modified: "2019-10-28"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "5411480"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-t02-1007.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-t02-1007.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/513"
---

# Starter Does Not Disengage
**Стартер не отключается**

> [!abstract] Процедура · `513-t02-1007`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[5411480 — C Command Connect and Connect Premier Marine Panel Systems PS102, PS103 and PS108 Mas|5411480]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2019-10-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-t02-1007.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-t02-1007.pdf)

Printable Version

### Symptoms

- The starter continues to spin after the operator releases the start button.

### How To Use This Tree

This symptom tree can be used to troubleshoot engine start symptoms. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform depending on the symptom.

### Shoptalk

To initiate engine crank from the helm, the following helm parameters **must** be met:

- The system enable switch is turned to the ON position.

- The engine is stopped.

- Throttle is in neutral position.

Possible Causes:

- A failed closed starter relay.

- Proper orientation of the push button starter relay is important.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the starter. |  |
|  | **STEP 1A.** Check for start voltage at the starter magnetic switch. | Zero volts? |
| STEP 2. | Check the push button starter relay. |  |
|  | **STEP 2A.** Check the relay. | Relay within specification? |
| STEP 3. | Check the engine control module (ECM). |  |
|  | **STEP 3A.** Check for start voltage at the ECM. | Zero Volts? |

### STEP 1. Check the starter.

#### STEP 1A. Check for start voltage at the start magnetic switch.

| **Conditions:** Turn system enable switch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the voltage: Place one test lead on start SIGNAL pin (S) at the starter magnetic switch. Place the other test lead on block ground. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general multimeter usage techniques. [[99-019-359 — Multimeter Usage\|Refer to Procedure 019-359 in Section 19.]] | Zero volts? **YESRepair:** Check the starter and starter switch. For the starter: Reference Procedure 013-020 in Section 13 of the appropriate engine service manual. For the starter magnetic switch: Reference Procedure 013-017 in Section 13 of the appropriate engine service manual. | Repair complete. |
| Zero volts? **NO** | 2A |  |

### STEP 2. Check the push button starter relay.

#### STEP 2A. Check the relay.

| **Conditions:** Turn keyswitch OFF. Disconnect the push button starter relay from the wiring harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the push button starter relay. Refer to Procedure 019-642 in Section 19. Refer to the circuit diagram or wiring diagram for connector pin identification. | Relay within specification? **YES** | Repair complete. |
| Relay within specification? **NORepair:** Replace the push button start relay. | 3A |  |

### STEP 3. Check the ECM.

#### STEP 3A. Check for start voltage at the ECM.

| **Conditions:** Disconnect the engine interface harness from the original equipment manufacturer (OEM) interface panel. Turn system enable switch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for start voltage at the ECM. Place one test lead on start SIGNAL pin 24 at the engine interface panel connector (mating to the OEM interface panel). Place the other test lead on block ground. | Zero Volts? **YESRepair:** Voltage detected in the starter circuit without the start button pressed. Refer to the Un-Requested Engine Start troubleshooting symptom tree in Section TT. | Repair complete. |
| Zero Volts? **NORepair:** A short in the engine harness has been detected. Repair or replace the engine harness. Reference Procedure 019-043 in Section 19 of the appropriate engine service manual. | Repair complete. |  |
