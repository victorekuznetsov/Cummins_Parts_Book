---
aliases:
  - "Код 1542 — цепь вспомогательного датчика давления 1 — напряжение выше нормы"
type: "Процедура"
doc: "123-t05-1542"
title_en: "FAULT CODE 1542 - Auxiliary Pressure Sensor Input 1 Circuit - Voltage Above Normal or Shorted to High Source"
title_ru: "Код 1542 — цепь вспомогательного датчика давления 1 — напряжение выше нормы"
modified: "2013-11-05"
engines:
  - "41349633"
families:
  - "QSK19"
manuals:
  - "4022094"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/123/123-t05-1542.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/123-t05-1542.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/123"
---

# FAULT CODE 1542 - Auxiliary Pressure Sensor Input 1 Circuit - Voltage Above Normal or Shorted to High Source
**Код 1542 — цепь вспомогательного датчика давления 1 — напряжение выше нормы**

> [!abstract] Процедура · `123-t05-1542`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4022094 — QSK19 CM2150 and CM2670 Electronic Control System Troubleshooting and Repair Manual|4022094]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2013-11-05
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/123/123-t05-1542.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/123-t05-1542.pdf)

Printable Version

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the fault codes. |  |
|  | **STEP 1A.** Check for sensor supply or multiple fault codes. | Fault Code 386 active? |
| STEP 2. | Check the original equipment manufacturer (OEM) pressure sensor and circuit. |  |
|  | **STEP 2A.** Inspect the OEM pressure sensor and connector pins. | Dirty or damaged pins? |
|  | **STEP 2B.** Check the circuit response. | Fault Code 1543 active and Fault Code 1542 inactive? |
|  | **STEP 2C.** Check the sensor supply voltage and return circuit. | Voltage between 4.75-VDC and 5.25-VDC? |
|  | **STEP 2D.** Check the fault codes and verify sensor condition. | Fault Code 1542 is active? |
| STEP 3. | Check the engine control module (ECM) and OEM harness. |  |
|  | **STEP 3A.** Inspect the ECM and OEM harness connector pins. | Dirty or damaged pins? |
|  | **STEP 3B.** Check for an open circuit in the OEM harness. | Less than 10 ohms? |
|  | **STEP 3C.** Check for a pin-to-pin short circuit in the OEM harness. | Greater than 100K ohms? |
|  | **STEP 3D.** Check for a pin-to-pin short circuit in the OEM harness. | Greater than 100K ohms? |
|  | **STEP 3E.** Check for an inactive fault code. | Fault Code 1542 inactive? |
| STEP 4. | Clear the fault codes. |  |
|  | **STEP 4A.** Disable the fault code. | Fault Code 1542 inactive? |
|  | **STEP 4B.** Clear the inactive fault codes. | All fault codes cleared? |

### STEP 1. Check the fault codes.

#### STEP 1A. Check for sensor supply or multiple fault codes.

| **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for sensor supply fault codes. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 386 active? **YES** | See the troubleshooting tree for Fault Code 386. |
| Fault Code 386 active? **NO** | 2A |  |

### STEP 2. Check the OEM pressure sensor and circuit.

#### STEP 2A. Inspect the OEM pressure sensor and connector pins.

| **Conditions:** Turn keyswitch ON. Disconnect the OEM pressure sensor from the OEM harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the OEM harness and OEM pressure sensor connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the sensor or harness connector. Clean the connector and pins. Repair the damaged harness, connector, or pins, if possible. Repair the OEM harness. Refer to Procedure 019-071 in Section 19. | 4A |
| Dirty or damaged pins? **NO** | 2B |  |

#### STEP 2B. Check the circuit response.

| **Conditions:** Turn keyswitch OFF. Disconnect the OEM pressure sensor from the OEM harness. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for the appropriate circuit response after 30 seconds. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 1543 active and Fault Code 1542 inactive? **YES** | 2C |
| Fault Code 1543 active and Fault Code 1542 inactive? **NO** | 3A |  |

#### STEP 2C. Check the sensor supply voltage and return circuit.

| **Conditions:** Turn keyswitch OFF. Disconnect the OEM pressure sensor from the OEM harness. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the supply voltage and return circuit. Measure the voltage between the OEM pressure +5 volt SUPPLY pin and the OEM pressure RETURN pin at the sensor connector of the OEM harness. Refer to the circuit diagram or the wiring diagram for connector pin identification. | Voltage between 4.75-VDC and 5.25-VDC? **YES** | 2D |
| Voltage between 4.75-VDC and 5.25-VDC? **NO** | 3A |  |

#### STEP 2D. Check the fault codes and verify sensor condition.

| **Conditions:** Turn keyswitch OFF. Connect the OEM pressure sensor to the OEM harness. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for the appropriate circuit response after 30 seconds. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 1542 active? **YESRepair:** A damaged sensor has been detected. Replace the OEM pressure sensor. Refer to OEM service manual. | 4A |
| Fault Code 1542 active? **NORepair:** None. The removal and installation of the connector corrected the fault. | 4A |  |

### STEP 3. Check the ECM and OEM harness.

#### STEP 3A. Inspect ECM and OEM harness connector pins.

| **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness from the ECM connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the OEM harness and ECM connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the ECM connector or OEM harness connector. Clean the connector and pins. Repair the damaged harness, connector, or pins, if possible. Repair the OEM harness. Refer to Procedure 019-071 in Section 19. | 4A |
| Dirty or damaged pins? **NO** | 3B |  |

#### STEP 3B. Check for an open circuit in the OEM harness.

| **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness from the ECM connector. Disconnect the OEM pressure sensor from the OEM harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for an open circuit. Measure the resistance between the OEM harness ECM connector OEM pressure RETURN pin and the OEM harness OEM pressure sensor connector RETURN pin. Refer to the circuit diagram or the wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Less than 10 ohms? **YES** | 3C |
| Less than 10 ohms? **NORepair:** An open RETURN circuit has been detected in the OEM harness. Troubleshoot each harness connected in series to determine which contains the open return circuit. Repair the OEM harness. Refer to Procedure 019-071 in Section 19. | 4A |  |

#### STEP 3C. Check for a pin-to-pin short circuit in the OEM harness.

| **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness from the ECM connector. Disconnect the OEM pressure sensor from the OEM harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for a pin-to-pin short. Measure the resistance between the OEM pressure SUPPLY pin in the OEM harness ECM connector and all other pins in the ECM OEM connector. Refer to the circuit diagram or the wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Greater than 100K ohms? **YES** | 3E |
| Greater than 100K ohms? **NORepair:** A pin-to-pin short circuit on the SUPPLY wire has been detected in the OEM harness. Troubleshoot each harness connected in series to determine which contains the pin-to-pin shorted supply circuit. Repair the OEM harness. Refer to Procedure 019-071 in Section 19. | 4A |  |

#### STEP 3D. Check for a pin-to-pin short circuit in the OEM harness.

| **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness from the ECM connector. Disconnect the OEM pressure sensor from the OEM harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for a pin-to-pin short. Measure the resistance between the OEM pressure SUPPLY pin in the OEM harness ECM connector and all other pins in the ECM OEM connector. Refer to the circuit diagram or the wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Greater than 100K ohms? **YES** | 3E |
| Greater than 100K ohms? **NORepair:** A pin-to-pin short circuit on the SUPPLY wire has been detected in the OEM harness. Troubleshoot each harness connected in series to determine which contains the shorted signal circuit to ground. Repair the OEM harness. Refer to Procedure 019-071 in Section 19. | 4A |  |

#### STEP 3E. Check for an inactive fault code.

| **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for the appropriate circuit response after 30 seconds. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 1542 inactive? **YESRepair:** None. The removal and installation of the connector corrected the fault. | 4A |
| Fault Code 1542 inactive? **NORepair:** Replace the ECM. Refer to Procedure 019-031 in Section 19. | 4A |  |

### STEP 4. Clear the fault codes.

#### STEP 4A. Disable the fault code

| **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Disable the fault code. Use INSITE™ electronic service tool to verify that the fault code is inactive. | Fault Code 1542 inactive? **YES** | 4B |
| Fault Code 1542 inactive? **NORepair:** Return to the troubleshooting steps or contact a Cummins® Authorized Repair Location if all steps have been completed and checked again. | 1A |  |

#### STEP 4B. Clear the inactive fault codes.

| **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Clear the inactive fault codes. Use INSITE™ electronic service tool to clear the inactive fault codes. | All fault codes cleared? **YES** | Repair complete. |
| All fault codes cleared? **NORepair:** Go to the appropriate troubleshooting steps. | 1A |  |
