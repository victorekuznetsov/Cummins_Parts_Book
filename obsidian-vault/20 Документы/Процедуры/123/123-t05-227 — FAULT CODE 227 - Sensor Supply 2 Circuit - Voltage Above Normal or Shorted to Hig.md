---
aliases:
  - "Код 227 — цепь питания датчиков 2 — напряжение выше нормы"
type: "Процедура"
doc: "123-t05-227"
title_en: "FAULT CODE 227 - Sensor Supply 2 Circuit - Voltage Above Normal or Shorted to High Source"
title_ru: "Код 227 — цепь питания датчиков 2 — напряжение выше нормы"
modified: "2026-02-06"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4022094"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/123/123-t05-227.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/123-t05-227.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/123"
---

# FAULT CODE 227 - Sensor Supply 2 Circuit - Voltage Above Normal or Shorted to High Source
**Код 227 — цепь питания датчиков 2 — напряжение выше нормы**

> [!abstract] Процедура · `123-t05-227`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4022094 — QSK19 CM2150 and CM2670 Electronic Control System Troubleshooting and Repair Manual|4022094]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2026-02-06
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/123/123-t05-227.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/123-t05-227.pdf)

Printable Version

## Warnings and Cautions

> [!warning] CAUTION · Осторожно
> To reduce the possibility of damaging a new ECM, all other active fault codes must be investigated prior to replacing the ECM.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the fault codes. |  |
|  | **STEP 1A.** Check for an active fault code. | Fault Code 227 active? |
| STEP 2. | Check the ECM, OEM harness, and engine harness. |  |
|  | **STEP 2A..** Inspect the ECM, OEM harness, and engine harness connector pins. | Dirty or damaged pins? |
|  | **STEP 2B.** Check for a pin-to-pin short circuit in the OEM harness or engine harness. | Greater than 100k ohms? |
|  | **STEP 2C.** Check for a short circuit in the unswitched battery supply power harness. | Greater than 100k ohms? |
| STEP 3. | Clear the fault codes. |  |
|  | **STEP 3A.** Disable the fault code. | Fault Code 227 inactive? |
|  | **STEP 3B.** Clear the inactive fault codes. | All fault codes cleared? |

### STEP 1. Check the fault codes.

#### STEP 1A. Check for an active fault code.

| **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for an active fault code. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 227 active? **YES** | 2A |
| Fault Code 227 active? **NO** | Use the following procedure for an inactive or intermittent fault code. [[99-019-362 — Inactive or Intermittent Fault Code\|Refer to Procedure 019-362 in Section 19.]] |  |

### STEP 2. Check the ECM, OEM harness, and engine harness.

#### STEP 2A. Inspect the ECM, OEM harness, and engine harness connector pins.

| **Conditions:** Turn keyswitch OFF. Disconnect the accelerator pedal or lever position sensor connector from the OEM harness connector, if equipped. Disconnect the speed bias connector from the OEM harness connector, if equipped. Disconnect the gain adjust potentiometer connector from the OEM harness connector, if equipped. Disconnect the engine harness connector from the ECM 60-pin OEM port connector. Disconnect the engine harness connector from the 31-pin OEM connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the engine harness and sensor connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** Clean the connector and pins. Repair the damaged harness, connector, or pins if possible. Refer to the circuit diagram or wiring diagram for all engine harness interconnections. Refer to Procedure 019-071 in Section 19. Refer to Procedure 019-204 in Section 19. Refer to Procedure 019-043 in Section 19. Refer to the OEM service manual for accelerator pedal or lever position sensor repair instructions. Replace the ECM. [[123-019-031 — Engine Control Module\|Refer to Procedure 019-031 in Section 19.]] | 3A |
| Dirty or damaged pins? **NO** | 2B |  |

#### STEP 2B. Check for a pin-to-pin short circuit in the OEM harness or engine harness.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness connector from the ECM 60-pin OEM port connector. Disconnect the accelerator pedal or lever position sensor connector from the OEM harness connector, if equipped. Disconnect the speed bias connector from the OEM harness connector, if equipped. Disconnect the gain adjust potentiometer connector from the OEM harness connector, if equipped. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for a pin-to-pin short. Measure the resistance between the 5 volt SUPPLY (sensor supply 2) pin in the engine harness ECM connector and all other pins in the connector. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Greater than 100k ohms? **YES** | 2C |
| Greater than 100k ohms? **NORepair:** A short circuit has been detected in the 5 volt SUPPLY (sensor supply 2) wire. Troubleshoot all harnesses connected in series to determine which contains the pin-to-pin short. Refer to the circuit diagram or wiring diagram for all harness interconnections. Replace the damaged section of harness. Refer to Procedure 019-071 in Section 19. Refer to Procedure 019-199 in Section 19. Refer to Procedure 019-043 in Section 19. | 3A |  |

#### STEP 2C. Check for a short circuit in the unswitched battery supply power harness.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness connector from the ECM 60-pin OEM port connector. Disconnect the accelerator pedal or lever position sensor connector from the OEM harness connector, if equipped. Disconnect the speed bias connector from the OEM harness connector, if equipped. Disconnect the gain adjust potentiometer connector from the OEM harness connector, if equipped. Disconnect the engine power harness connector from the ECM connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for a short circuit to battery. Measure the resistance between the 5 volt SUPPLY (sensor supply 2) pin in the engine harness ECM connector and the ECM battery SUPPLY (+) pin or the power harness ECM connector. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Greater than 100k ohms? **YESRepair:** Replace the ECM. [[123-019-031 — Engine Control Module\|Refer to Procedure 019-031 in Section 19.]] | 3A |
| Greater than 100k ohms? **NORepair:** A short circuit to the battery has been detected in the OEM harness or engine harness. Repair the OEM harness. Refer to Procedure 019-071 in Section 19. Repair the engine harness. Refer to Procedure 019-043 in Section 19. | 3A |  |

### STEP 3. Clear the fault codes.

#### STEP 3A. Disable the fault code.

| **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Disable the fault code. Use INSITE™ electronic service tool to verify the fault code is inactive. | Fault Code 227 inactive? **YES** | 3B |
| Fault Code 227 inactive? **NORepair:** Return to the troubleshooting steps or contact a Cummins® Authorized Repair Location if all steps have been completed and checked again. | 1A |  |

#### STEP 3B. Clear the inactive fault codes.

| **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Clear the inactive fault codes. Use INSITE™ electronic service tool to clear the inactive fault codes. | All fault codes cleared? **YES** | Repair complete. |
| All fault codes cleared? **NORepair:** Troubleshoot any remaining active fault codes. | Go to the appropriate troubleshooting steps. |  |
