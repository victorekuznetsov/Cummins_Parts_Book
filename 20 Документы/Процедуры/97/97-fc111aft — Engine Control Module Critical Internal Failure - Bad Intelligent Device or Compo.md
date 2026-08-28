---
aliases:
  - "Критический внутренний отказ ЭБУ — неисправное устройство"
type: "Процедура"
doc: "97-fc111aft"
title_en: "Engine Control Module Critical Internal Failure - Bad Intelligent Device or Component"
title_ru: "Критический внутренний отказ ЭБУ — неисправное устройство"
modified: "2004-10-15"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
  - "80141463"
  - "80248213"
families:
  - "QSM11"
  - "QSX15"
manuals:
  - "3666415"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-fc111aft.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-fc111aft.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "двигатель/QSX15"
  - "группа/97"
---

# Engine Control Module Critical Internal Failure - Bad Intelligent Device or Component
**Критический внутренний отказ ЭБУ — неисправное устройство**

> [!abstract] Процедура · `97-fc111aft`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSM11, QSX15
> **Входит в руководства:** [[3666415 — ICON Idle Control System Master Repair Manual|3666415]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2004-10-15
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-fc111aft.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-fc111aft.pdf)

### Fault Code: 111 (Aftermarket and OEM)

### Engine Control Module Critical Internal Failure - Bad Intelligent Device or Component

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 111 PID(P): SPN: FMI: Lamp: None SRT: | Engine Control Module Critical Internal Failure - Bad Intelligent Device or Component. Error internal to the ICON™ idle control module related to memory hardware failures or internal microprocessor communication failures. | The ICON™ system will be disabled. Engine will possibly **not** start normally. Keyswitch can possibly **not** operate normally. |

![[19802946.png]]

### Circuit Description

The ICON™ idle control module is a computer that controls the operation of the ICON™ system.

### Component Location

The ICON™ idle control module is typically mounted on the vehicle bulkhead on the intake side of the engine. However, the ICON™ module can be located in a different location depending on the vehicle application.

### Shoptalk

This fault code can be caused **only** by an internal ICON™ idle control module problem. Repairs are **not** possible for the ICON™ idle control module.

The ICON™ system can display **only** the present active fault code. If more than one fault code is active at the same time, the ICON™ system flashes out the highest priority fault. After the fault has been corrected then the next active fault will be flashed out.

The ICON™ electronic service tool can display more than one active and or inactive fault codes at the same time.

## Warnings and Cautions

> [!warning] CAUTION · Осторожно
>

**To avoid damaging a new ICON™ idle control module, all other active fault codes must be investigated prior to replacing the ICON™ idle control module.**

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Read the fault codes. |  |
|  | **STEP 1A.** Use the fault flashout feature or the ICON™ electronic service tool to read the fault codes. | Fault Code 111 inactive |
| STEP 2. | Clear the fault code. |  |
|  | **STEP 2A.** Disable the fault code. | Fault Code 111 cleared |

### STEP 1. Read the fault codes.

#### STEP 1A. Use the fault flashout feature or the ICON™ electronic service tool to read the fault codes.

| **Conditions:** Connect all components. Turn keyswitch ON. Connect the ICON™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
|  | Fault Code 111 inactive. Refer to Inactive or Intermittent Fault Codes, Procedure [[99-019-362 — Inactive or Intermittent Fault Code\|019-362]]. | 2A |
| Replace the ICON™ idle control module. Refer to Procedure [[97-019-358 — ICON™ Idle Control Module\|019-358]]. | Repair complete |  |

### STEP 2. Clear the fault code.

#### STEP 2A. Disable the fault code.

| **Conditions:** Connect all components. Turn keyswitch ON. Connect the ICON™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Use the ICON™ electronic service tool to clear the fault code. Cycle the keyswitch to verify the fault code is inactive. | Fault Code 111 cleared | Repair complete |
| Troubleshoot any remaining active fault codes. | Appropriate troubleshooting charts |  |
