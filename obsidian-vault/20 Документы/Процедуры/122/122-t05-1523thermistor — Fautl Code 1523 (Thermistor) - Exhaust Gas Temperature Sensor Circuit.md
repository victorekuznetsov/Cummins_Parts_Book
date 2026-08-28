---
aliases:
  - "Код 1523 (термистор) — цепь датчика температуры ОГ цилиндра 7 — напряжение выше нормы"
type: "Процедура"
doc: "122-t05-1523thermistor"
title_en: "Fautl Code 1523 (Thermistor) - Exhaust Gas Temperature Sensor Circuit Cylinder 7 - Voltage Above Normal or Shorted to High Source"
title_ru: "Код 1523 (термистор) — цепь датчика температуры ОГ цилиндра 7 — напряжение выше нормы"
modified: "2014-05-15"
engines:
  - "33239746"
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
manuals:
  - "4022102"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-t05-1523thermistor.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/122-t05-1523thermistor.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/122"
---

# Fautl Code 1523 (Thermistor) - Exhaust Gas Temperature Sensor Circuit Cylinder 7 - Voltage Above Normal or Shorted to High Source
**Код 1523 (термистор) — цепь датчика температуры ОГ цилиндра 7 — напряжение выше нормы**

> [!abstract] Процедура · `122-t05-1523thermistor`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Входит в руководства:** [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M|4022102]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2014-05-15
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-t05-1523thermistor.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/122-t05-1523thermistor.pdf)

Printable Version

## Warnings and Cautions

> [!warning] CAUTION · Осторожно
> To reduce the possibility of damaging a new engine control module (ECM), all other active fault codes must be investigated prior to replacing the ECM.

> [!warning] CAUTION · Осторожно
> To reduce the possibility of pin and harness damage, use the following test leads when taking a measurement: Part Number 3824811 - male Deutsch™ test lead Part Number 3824812 - female Deutsch™ test leak Part Number 3822758 - male Deutsch™/AMP™/Metri-Pack™ test lead Part Number 3822917 - female Deutsch™/AMP™/Metri-Pack™ test lead.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the fault codes. |  |
|  | **STEP 1A.** Check for an inactive fault code. | Fault Code 1523 inactive? |
| STEP 2. | Check the exhaust gas temperature sensor cylinder 7 circuit and connector pins. |  |
|  | **STEP 2A.** Inspect the engine harness and exhaust gas temperature sensor cylinder 7 and circuit. | Dirty or damaged pins? |
|  | **STEP 2B.** Check the circuit response. | Fault Code 674 active? |
|  | **STEP 2C.** Check the fault codes and verify sensor condition. | Fault Code 1523 active? |
| STEP 3. | Inspect the ECM and check the engine harness. |  |
|  | **STEP 3A.** Inspect the ECM and engine harness connector pins. | Dirty or damaged pins? |
|  | **STEP 3B.** Check for an open RETURN circuit in the engine wiring harness. | Less than 10 ohms? |
|  | **STEP 3C.** Check for an open SIGNAL circuit in the engine wiring harness. | Less than 10 ohms? |
|  | **STEP 3D.** Check for a pin-to-pin short circuit in the wiring harness. | Greater than 100k ohms? |
|  | **STEP 3E.** Check for an inactive fault code. | Fault Code 1523 inactive? |
|  | **STEP 3F.** Check if an ECM calibration update is available. | If a calibration update for this fault code is available, does the ECM contain that revision or higher? |
| STEP 4. | Clear the fault codes. |  |
|  | **STEP 4A.** Disable the fault code. | Fault Code 1523 inactive? |
|  | **STEP 4B.** Clear the inactive fault codes. | All fault codes cleared? |

### STEP 1. Check the fault codes.

#### STEP 1A. Check for an inactive fault code.

| **Conditions:** Keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for an inactive fault code. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 1523 inactive? **YES** | [[99-019-362 — Inactive or Intermittent Fault Code\|Refer to Procedure 019-362 in Section 19.]] |
| Fault Code 1523 inactive? **NO** | 2A |  |

### STEP 2. Check the exhaust gas temperature sensor cylinder 7 and circuit.

#### STEP 2A. Check the exhaust gas temperature sensor cylinder 7 circuit and connector pins.

| **Conditions:** Keyswitch OFF. Disconnect the exhaust gas temperature sensor cylinder 7 connector from the engine harness connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the engine harness connector and exhaust gas temperature sensor cylinder 7 connector pins for the following: Loose connector. Corroded pins. Bent or broken pins. Pushed back or expanded pins. Moisture in or on the connector. Missing or damaged connector seals. Dirt or debris in or on the connector pins. Connector shell broken. Wire insulation damage. Damaged connector locking tab. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19]] for general inspection techniques. | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the exhaust gas temperature sensor cylinder 7 connector or engine harness connector. Clean the connector and pins. Repair the damaged harness, connector, or pins, if possible. Replace the damaged section of the engine harness or damaged exhaust gas temperature sensor cylinder 7 connector, if repair is **not** possible. Check all harnesses connected in series. Refer to the circuit diagram or wiring diagram for all harness interconnections. Replace the engine harness. Refer to Procedure 019-043 in Section 19. | 4A |
| Dirty or damaged pins? **NO** | 2B |  |

#### STEP 2B. Check the circuit response.

| **Conditions:** Keyswitch OFF. Disconnect the exhaust gas temperature sensor cylinder 7 connector from the engine harness. Place a jumper wire between the exhaust gas temperature sensor 7 SIGNAL and RETURN pin at the sensor connector of the engine harness. Keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for the appropriate ECM response after 2 minutes idling the engine above 600 rpm. Use INSITE™ electronic service tool to read the fault codes. After reading the fault codes, switch OFF the engine. Remove the jumper wire between the exhaust gas temperature sensor 7 SIGNAL and RETURN pin at the sensor connector of the engine harness. | Fault Code 674 active? **YES** | 2C |
| Fault Code 674 active? **NO** | 3A |  |

#### STEP 2C. Check the fault codes and verify sensor condition.

| **Conditions:** Keyswitch OFF. Connect the exhaust gas temperature sensor 7 to the engine harness. Keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for the appropriate ECM response after 2 minutes idling the engine above 600 rpm. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 1523 active? **YESRepair:** Replace the exhaust gas temperature sensor. Refer to Procedure 019-013 in Section 19. | 4A |
| Fault Code 1523 active? **NORepair:** None. The removal and installation of the connector corrected the fault. | 4A |  |

### STEP 3. Inspect the ECM and check the engine harness.

#### STEP 3A. Inspect the ECM and engine harness connector pins.

| **Conditions:** Keyswitch OFF. Disconnect the engine harness connector from the ECM 60 pin connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the engine harness and ECM connector pins for the following: Loose connector. Corroded pins. Bent or broken pins. Pushed back or expanded pins. Moisture in or on the connector. Missing or damaged connector seals. Dirt or debris in or on the connector pins. Connector shell broken. Wire insulation damage. Damaged connector locking tab. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19]] for general inspection techniques. | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the ECM connector or the engine harness connector. Clean the connector and pins. Repair the damaged harness, connector, or pins, if possible. Replace the damaged section of harness, if repair is **not** possible. Check all harnesses connected in series. Replace the engine harness. Refer to Procedure 019-043 in Section 19. Replace the ECM if the ECM connector is damaged. Refer to Procedure 019-031 in Section 19. | 4A |
| Dirty or damaged pins? **NO** | 3B |  |

#### STEP 3B. Check for an open RETURN circuit in the engine wiring harness.

| **Conditions:** Keyswitch OFF. Disconnect the engine harness connector from the ECM 60 pin connector. Disconnect the exhaust gas temperature sensor cylinder 7 from the wiring harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for an open circuit. Measure the resistance between the exhaust gas temperature sensor cylinder 5 RETURN pin in the engine harness ECM 60 pin connector and the exhaust gas temperature sensor cylinder 7 RETURN pin in the engine harness exhaust gas temperature sensor connector. Refer to the circuit diagram or wiring diagram for connector pin identification. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19]] for general resistance measurement techniques. | Less than 10 ohms? **YES** | 3C |
| Less than 10 ohms? **NORepair:** An open RETURN circuit has been detected in the engine harness. Repair or replace the engine harness. Replace the engine harness. Refer to Procedure 019-043 in Section 19. | 4A |  |

#### STEP 3C. Check for an open SIGNAL circuit in the engine wiring harness.

| **Conditions:** Keyswitch OFF. Disconnect the engine harness connector from the ECM 60 pin connector. Disconnect the exhaust gas temperature sensor cylinder 7 from the wiring harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for an open circuit. Measure the resistance between the exhaust gas temperature sensor cylinder 7 SIGNAL pin in the ECM 60 pin connector and the exhaust gas temperature sensor cylinder 7 SIGNAL pin in the engine harness exhaust gas temperature sensor connector. Refer to the circuit diagram or wiring diagram for connector pin identification. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19]] for general resistance measurement techniques. | Less than 10 ohms? **YES** | 3D |
| Less than 10 ohms? **NORepair:** An open SIGNAL circuit has been detected in the engine wiring harness. Repair or replace the engine harness. Replace the engine harness. Refer to Procedure 019-043 in Section 19. | 4A |  |

#### STEP 3D. Check for a pin-to-pin short circuit.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness connector from the ECM 60 pin connector. Disconnect the exhaust gas temperature sensor cylinder 7 from the engine harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for a pin-to-pin short circuit. Measure the resistance between the exhaust gas temperature sensor 7 SIGNAL pin in the engine harness ECM 60 pin connector and all other pins in the connector. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Greater than 100k ohms? **YES** | 3E |
| Greater than 100k ohms? **NORepair:** A pin-to-pin short circuit on the SIGNAL wire has been detected in the engine harness. Repair or replace the engine harness. Refer to Procedure 019-043 in Section 19. | 4A |  |

#### STEP 3E. Check for an inactive fault code.

| **Conditions:** Turn keyswitch OFF. Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for the appropriate circuit response. Operate the engine with an idle speed greater than 600 rpm for 2 minutes. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 1523 inactive? **YESRepair:** None. The removal and installation of the connector corrected the fault. | 4A |
| Fault Code 1523 inactive? **NORepair:** Check if an ECM calibration update is available. | 3F |  |

#### STEP 3F. Check if an ECM calibration update is available.

| **Conditions:** Connect all components. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Compare the ECM code and revision number in the ECM to the calibration revisions listed in the ECM Calibration Revision History for applicable changes related to this fault code. Use INSITE™ electronic service tool to find the present ECM code and revision number in the ECM. The ECM code and revision number are found in the Calibration Information section of System ID and Dataplate in Features and Parameters. | If a calibration update for this fault code is available, does the ECM contain that revision or higher? **YESRepair:** Replace the malfunctioning ECM. Refer to Procedure 019-031 in Section 19. | 4A |
| If a calibration update for this fault code is available, does the ECM contain that revision or higher? **NORepair:** If necessary, calibrate the ECM. Refer to Procedure 019-032 in Section 19. | 4A |  |

### STEP 4. Clear the fault codes.

#### STEP 4A. Disable the fault code.

| **Conditions:** Connect all components. Keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Disable the fault code. Use INSITE™ electronic service tool to verify the fault code is inactive. | Fault Code 1523 inactive? **YES** | 4B |
| Fault Code 1523 inactive? **NORepair:** Return to the troubleshooting steps or contact a Cummins® Authorized Repair Location if all steps have been completed and checked again. | 1A |  |

#### STEP 4B. Clear the inactive fault codes.

| **Conditions:** Connect all components. Keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Clear the inactive fault codes. Use INSITE™ electronic service tool to clear the inactive fault codes. | All fault codes cleared? **YES** | Repair complete |
| All fault codes cleared? **NORepair:** Troubleshoot any remaining active fault codes. | Appropriate troubleshooting steps |  |
