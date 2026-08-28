---
aliases:
  - "Дерево диагностики отсутствия связи с ЭБУ"
type: "Процедура"
doc: "00-ttecm"
title_en: "ECM - No Communication Troubleshooting Tree"
title_ru: "Дерево диагностики отсутствия связи с ЭБУ"
modified: "2025-07-22"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
  - "33239746"
  - "33239899"
  - "37269910"
  - "37280605"
  - "37292556"
  - "37295879"
  - "41343322"
  - "41349633"
  - "41353297"
  - "41370103"
  - "85017333"
  - "93058669"
  - "93087701"
  - "93948840"
families:
  - "C8.3 · 6C8.3"
  - "K19"
  - "K38/K50 · QSK38, QSK50, QSK60"
  - "NT/NTA855 · ISM/QSM11"
  - "QSK19"
  - "QSK23"
  - "QSK60"
  - "QST30"
  - "QSZ13"
manuals:
  - "3666070"
  - "3666113"
  - "3666214"
  - "3666266"
  - "4021442"
  - "4021592"
  - "4021674"
  - "4022094"
  - "4022102"
  - "4358369"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/00/00-ttecm.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/00-ttecm.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "двигатель/K19"
  - "двигатель/K38/K50"
  - "двигатель/NT/NTA855"
  - "двигатель/QSK19"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "двигатель/QST30"
  - "двигатель/QSZ13"
  - "группа/00"
---

# ECM - No Communication Troubleshooting Tree
**Дерево диагностики отсутствия связи с ЭБУ**

> [!abstract] Процедура · `00-ttecm`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]], [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]], [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]], [[41343322 — NH NT 855 CPL 3362|41343322]], [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]], [[41370103 — NH NT 855 CPL 3362|41370103]], [[85017333 — QSK23 CM500 CPL 2858|85017333]], [[93058669 — 6C8.3 CPL 3105|93058669]], [[93087701 — 6C8.3 CPL 3105|93087701]], [[93948840 — QSZ13 CM2150 Z102 CPL 4858|93948840]]
> **Семейство:** C8.3 · 6C8.3, K19, K38/K50 · QSK38, QSK50, QSK60, NT/NTA855 · ISM/QSM11, QSK19, QSK23, QSK60, QST30, QSZ13
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]], [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]], [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]], [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]], [[4021442 — C8.3 Marine Electronic Control System Troubleshooting and Repair Manual|4021442]], [[4021592 — QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual|4021592]], [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]], [[4022094 — QSK19 CM2150 and CM2670 Electronic Control System Troubleshooting and Repair Manual|4022094]], [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M|4022102]], [[4358369 — QSZ13 CM2150 Z102 Service Manual|4358369]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format) · Section TT — Troubleshooting Symptoms (New Format) · Section TT- Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2025-07-22
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/00/00-ttecm.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/00-ttecm.pdf)

Printable Version

### Symptoms

- No communication and engine will **not** start

- No communication and engine will start

- No communication related the recommended Cummins® electronic service tool, or equivalent errors

- Communication with some engine control module (ECM)s but **not** all ECMs on a multi-module engine.

### How To Use This Tree

This troubleshooting procedure can be used to troubleshoot J1939 and J1587 data link communication issues between the electronic service tool and the ECM. There are four procedures that can be used to support this troubleshooting tree:

Procedure 022-999 (Service Tools and Hardware - Overview) in Section F, in the appropriate troubleshooting and repair manual.

Procedure 019-165 (Data Link Circuit, SAE J1939) in Section 19 in the appropriate troubleshooting and repair manual.

Procedure 019-166 (Data Link Circuit, SAE J1587) in Section 19 in the appropriate troubleshooting and repair manual.

The troubleshooting steps in this procedure build upon information obtained in previous steps. The troubleshooting steps **must** be performed in the sequence specified in the troubleshooting procedure.

This troubleshooting procedure supports several engine families, therefore some instructions are stated in a general manner. Apply the requested procedures and actions to the specific engine family with the support of engine specific documentation that can be found in the troubleshooting and repair manuals for the specific engine family.

### Shoptalk

Three basic principles were used to define and sequence the troubleshooting steps that are listed in this tree.

- Verify high level system operation prior to troubleshooting individual components of the system. The purpose of this is to learn from the behavior of the system in order to direct the next steps for troubleshooting.

- Use the bench top harness to separate the ECM from the vehicle so the ECM can be isolated from vehicle issues that could be causing no communication.

- Use a second vehicle or a second ECM to isolate high level system issues before troubleshooting individual components of the system.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Electronic service tool error code check |  |
|  | **STEP 1A.** Check for electronic service tool error code 5023. | Electronic service tool error code 5023 present? |
|  | **STEP 1B.** Electronic service tool error code 5080 or 5081 check. | Electronic service tool error code 5080 or 5081 present? |
|  | **STEP 1C.** Electronic service tool other error code checks. | Electronic service tool error codes present other than 5023, 5080, or 5081? |
|  | **STEP 1D.** ECM password check. | Electronic service tool indicates the ECM is password protected? |
| STEP 2. | Initial data link adapter and electronic service tool check |  |
|  | **STEP 2A.** Initial data link adapter check. | Communication lights on the data link adapter flashing? |
|  | **STEP 2B.** Data link adapter reset check. | ECM communicates? |
|  | **STEP 2C.** Initial electronic service tool check. | ECM communicates? |
| STEP 3. | Bench communication setup checks |  |
|  | **STEP 3A.** Bench setup availability check. | Bench setup available? |
|  | **STEP 3A-1.** Engine start check. | Engine starts? |
|  | **STEP 3B.** Initial bench setup communication check. | ECM communicates using bench setup? |
|  | **STEP 3B-1.** Engine start check. | Engine starts? |
|  | **STEP 3C.** Second vehicle or second ECM availability check for bench setup. | Second vehicle or second ECM available to connect to the bench setup? |
|  | **STEP 3D.** Initial bench setup functionality check. | Second ECM communicates using bench setup? |
|  | **STEP 3E.** Troubleshoot bench setup. | Bench setup check OK? |
|  | **STEP 3F.** Data link adapter replacement check. | Bench setup communicates with the second ECM using a replacement data link adapter? |
| STEP 4. | ECM power up circuit check |  |
|  | **STEP 4A.** Engine configuration check. | Engine equipped with a fuel shutoff valve? |
|  | **STEP 4A-1.** Check fuel shutoff valve voltage. | Fuel shutoff valve voltage within 1 VDC of vehicle system voltage? |
|  | **STEP 4A-2.** Coolant temperature sensor signal voltage check. | Coolant temperature signal voltage greater than 4.5 VDC? |
|  | **STEP 4B.** ECM keyswitch voltage check. | Keyswitch voltage within 1 VDC or vehicle system voltage? |
|  | **STEP 4C.** Check the ECM power and ground. | ECM battery supply voltage equal to the battery voltage? |
| STEP 5. | Initial electronic tool check |  |
|  | **STEP 5A.** Bench setup previously used for troubleshooting check. | In Step 3 checks, bench setup used to successfully communicate with the ECM? |
|  | **STEP 5B.** Second vehicle availability check for electronic tool. | Second vehicle available to connect to the electronic tool? |
|  | **STEP 5C.** Initial electronic tool functionality check. | Second ECM communicates using electronic tool? |
| STEP 6. | Data link adapter power check |  |
|  | **STEP 6A.** Data link adapter determination check. | Is the serial port being used to communicate with the electronic service tool? |
|  | **STEP 6B.** Check data link adapter power. | Data link adapter power light on? |
|  | **STEP 6C.** Determine if communication is being attempted at original equipment manufacturer (OEM) dash connector. | Communication being attempted at the OEM data link dash connector? |
|  | **STEP 6D.** OEM data link dash connector voltage check. | Voltage equal to or greater than 9 VDC? |
|  | **STEP 6E.** Check voltage at data link adapter auxiliary power supply. | Voltage equal to or greater than 9 VDC? |
|  | **STEP 6F.** Check voltage at vehicle battery. | Voltage equal or greater than 11 VDC? |
|  | **STEP 6G.** Computer serial port voltage check. | Minimum of 5 VDC available? |
| STEP 7. | Data link circuit check |  |
|  | **STEP 7A.** Check J1939 or J1587 circuits. | Circuit check OK? |
| STEP 8. | Initial electronic tool check |  |
|  | **STEP 8A.** Second vehicle availability check for electronic tool. | Second vehicle available to connect to the electronic tool? |
|  | **STEP 8B.** Initial electronic tool functionality check. | Second ECM communicates using the electronic tool? |
| STEP 9. | Detailed electronic tool check |  |
|  | **STEP 9A.** Troubleshoot electronic tool hardware. | Electronic tool hardware check OK? |
| STEP 10. | Serial cable and computer check |  |
|  | **STEP 10A.** Troubleshoot serial cable and computer. | Serial cable and computer check OK? |
| STEP 11. | ROM boot ECM |  |
|  | **STEP 11A.** ROM boot tool availability check. | ROM boot tool available? |
|  | **STEP 11B.** ROM boot ECM. | ECM communicates? |

### STEP 1. Electronic service tool error code check

#### STEP 1A. Electronic service tool error code 5023 check.

| **Conditions:** Connect the electronic service tool. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for electronic service tool error code 5023. Use the electronic service tool to read the error codes. | Electronic service tool error code 5023 present? **YES** | 2A |
| Electronic service tool error code 5023 present? **NO** | 1B |  |

#### STEP 1B. Electronic service tool error code 5080 or 5081 check.

| **Conditions:** Connect the electronic service tool. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for electronic service tool error code 5080 or 5081. Use the electronic service tool to read the error codes. | Electronic service tool error code 5080 or 5081 present? **YESRepair:** Perform the ECM calibration download. | Repair complete. |
| Electronic service tool error code 5080 or 5081 present? **NO** | 1C |  |

#### STEP 1C. Electronic service tool other error code checks.

| **Conditions:** Connect the electronic service tool. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Are any electronic service tool error codes present other than 5023, 5080, or 5081? Use the electronic service tool to read the error codes. | Electronic service tool error codes present other than 5023, 5080, or 5081? **YESRepair:** See the electronic service tool manual for troubleshooting guidelines. | Repair complete. |
| Electronic service tool error codes present other than 5023, 5080, or 5081? **NO** | 1D |  |

#### STEP 1D. ECM password check.

| **Conditions:** Connect the electronic service tool. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Does the electronic service tool indicate the ECM is password protected? Use the electronic service tool. | Electronic service tool indicates the ECM is password protected? **YESRepair:** Enter correct password If password is unavailable, contact customer to request password information. If customer can **not** supply password information, see the electronic service tool manual for password removal information. Normal warranty guidelines will apply if ECM password removal is required. | Repair complete. |
| Electronic service tool indicates the ECM is password protected? **NO** | 2A |  |

### STEP 2. Initial data link adapter and electronic service tool check

#### STEP 2A. Initial data link adapter check.

| **Conditions:** Connect data link adapter to OEM data link connector in vehicle. Do not connect the electronic service tool computer. Continue to Step 2B, if connected to the 3 pin engine data link connector. The communication lights will not blink. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Turn keyswitch on. | Communication lights on the data link adapter flashing? J1708 or J1939 for Inline 4, 5, 6, and 7. **YESRepair:** No Repair | 2C |
| Communication lights on the data link adapter flashing? J1708 or J1939 for Inline 4, 5, 6, and 7. **NO** | 2B |  |

#### STEP 2B. Data link adapter reset check.

| **Conditions:** Connect the electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Data link adapter reset check. Disconnect power from the data link adapter. Leave disconnected for 30 seconds. Connect power again to the data link adapter. Turn keyswitch ON. | ECM communicates? **YES** | Repair complete. |
| ECM communicates? **NO** | 3A |  |

#### STEP 2C. Initial electronic service tool check.

| **Conditions:** Connect the electronic service tool. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Reboot the electronic service tool PC. Launch the electronic service tool. Check for communication. | ECM communicates? **YES** | Repair complete. |
| ECM communicates? **NO** | 8A |  |

### STEP 3. Bench communication setup checks

#### STEP 3A. Bench setup availability check.

| **Conditions:** Check that bench setup is available. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Verify bench setup is available. | Bench setup available? **YES** | 3B |
| Bench setup available? **NO** | 3A-1 |  |

#### STEP 3A-1. Engine start check.

| **Conditions:** None |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Verify if engine will start. | Engine starts? **YES** | 5A |
| Engine starts? **NO** | 4A |  |

#### STEP 3B. Initial bench setup communication check.

| **Conditions:** Use the same electronic service tool personal computer (PC) as was used for the previous checks Connect bench setup to ECM Turn bench top calibration harness keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Attempt to communicate with the ECM using bench setup. | ECM communicates using bench setup? **YES** | 3B-1 |
| ECM communicates using bench setup? **NO** | 3C |  |

#### STEP 3B-1. Engine start check.

| **Conditions:** None |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Disconnect the bench top calibration cable from the ECM. Reconnect the ECM to the original engine or OEM wiring harness connector. Verify if the engine will start. | Engine starts? **YES** | 5A |
| Engine starts? **NO** | 4A |  |

#### STEP 3C. Second vehicle or second ECM availability check for bench setup.

| **Conditions:** Check for second vehicle or second ECM available for testing. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Verify if a second vehicle or second ECM is available to connect to the bench setup. | Second vehicle or second ECM available to connect to the bench setup? **YES** | 3D |
| Second vehicle or second ECM available to connect to the bench setup? **NO** | 3E |  |

#### STEP 3D. Initial bench setup functionality check

| **Conditions:** Use the same electronic service tool PC and bench setup tools that were originally used on the problem vehicle. Connect bench setup to second vehicle or second ECM Turn bench top calibration harness keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Attempt to communicate with the ECM on the second vehicle or a spare ECM using bench setup. | Second ECM communicates using bench setup? **YES** | 11A |
| Second ECM communicates using bench setup? **NO** | 3E |  |

#### STEP 3E. Troubleshoot bench setup hardware.

| **Conditions:** None |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Troubleshoot bench calibration cable, bench calibration harness, and serial cable. Perform troubleshooting procedures for evaluating the bench calibration cable, bench calibration harness, and serial cable. Reference Procedure 022-999 (Service Tools and Hardware - Overview) in Section F, for Resistance Check - serial cable, benchtop calibration harness, benchtop calibration cable, in the appropriate Electronic Control System Troubleshooting and Repair manual. | Bench setup check OK? **YES** | 3F |
| Bench setup check OK? **NORepair:** Repair or replace bench calibration cable, bench calibration harness, or serial cable. | 3B |  |

#### STEP 3F. Data link adapter replacement check.

| **Conditions:** None. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Try to communicate with the bench setup using a replacement data link. | Bench setup communicates with the second ECM using a replacement data link adapter? **YESRepair:** Use replacement data link adapter. | 3B |
| Bench setup communicates with the second ECM using a replacement data link adapter? **NORepair:** Issue with bench setup should have been found. Troubleshoot the bench setup again. | 3E |  |

### STEP 4. ECM power up circuit check

#### STEP 4A. Engine configuration check.

| **Conditions:** None. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Determine if the engine is equipped with a fuel shutoff valve | Engine equipped with a fuel shutoff valve? **YES** | 4A-1 |
| Engine equipped with a fuel shutoff valve? **NO** | 4A-2 |  |

#### STEP 4A-1. Check fuel shutoff valve voltage.

| **Conditions:** Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the voltage from the fuel shutoff valve post to engine block ground. There are 12 and 24 volt systems. The fuel shutoff valve voltage needs to be within 1 VDC of the vehicle system voltage. | Fuel shutoff valve voltage within 1 VDC of vehicle system voltage? **YES** | 5A |
| Fuel shutoff valve voltage within 1 VDC of vehicle system voltage? **NO** | 4B |  |

#### STEP 4A-2. Coolant temperature sensor signal voltage check

| **Conditions:** Turn keyswitch ON. Disconnect the coolant temperature sensor connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the voltage across the two pins of the coolant temperature sensor on the wiring harness connector. Use the wiring diagram or circuit diagram for connector pin identification. | Coolant temperature signal voltage greater than 4.5 VDC? **YES** | 5A |
| Coolant temperature signal voltage greater than 4.5 VDC? **NO** | 4B |  |

#### STEP 4B. ECM keyswitch voltage check.

| **Conditions:** Turn keyswitch OFF. Disconnect the wiring harness connector that contains the keyswitch signal from the ECM. Turn the keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the voltage from the keyswitch input SIGNAL wire of the wiring harness to engine block ground. Reference the wiring diagram or circuit diagram for connector pin identification. | Keyswitch voltage within 1 VDC or vehicle system voltage? **YES** | 4C |
| Keyswitch voltage within 1 VDC or vehicle system voltage? **NORepair:** Repair or replace the wiring harness that contains the keyswitch signal, repair or replace the keyswitch, or check the battery connection. Reference Procedure 019-064 (Key Switch Power Supply Circuit) in Section 19 in the appropriate troubleshooting and repair manual. See the Engine Performance Troubleshooting Tree in the appropriate troubleshooting and repair manual, if the no start condition is still present. | Repair complete. |  |

#### STEP 4C. Check the ECM power and ground.

| **Conditions:** Turn keyswitch OFF Disconnect from the ECM the wiring harness connector that contains the ECM battery SUPPLY (-) and SUPPLY (+) wiring. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the voltage from each ECM battery SUPPLY (+) pin to all battery SUPPLY (-) pins in the wiring harness connector. Use the wiring diagram or circuit diagram for connector pin identification. | ECM battery supply voltage equal to the battery voltage? **YESRepair:** Replace the ECM. Reference Procedure 019-031 (Engine Control Module) in Section 19 in the appropriate troubleshooting and repair manual. | Repair complete. |
| ECM battery supply voltage equal to the battery voltage? **NORepair:** Repair or replace the wiring harness that contains the ECM battery SUPPLY (+) and battery SUPPLY (-) wiring. See the Engine Performance Troubleshooting Tree or troubleshooting symptom tree if no start condition is still present. | Repair complete. |  |

### STEP 5. Initial electronic tool check

#### STEP 5A. Bench setup previously used for troubleshooting check.

| **Conditions:** None. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| In Step 3 checks, was bench setup used to successfully communicate with the ECM? | In Step 3 checks, bench setup used to successfully communicate with the ECM? **YESRepair:** ECM is OK. Repair complete if communication is **not** required through OEM data link connector or harness. If communication is required through the OEM data link connector or harness continue to Step 6A. | 6A |
| In Step 3 checks, bench setup used to successfully communicate with the ECM? **NO** | 5B |  |

#### STEP 5B. Second vehicle availability check for electronic tool.

| **Conditions:** Verify second vehicle available for testing |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Verify a second vehicle is available to connect to the electronic tool. | Second vehicle available to connect to the electronic tool? **YES** | 5C |
| Second vehicle available to connect to the electronic tool? **NO** | 6A |  |

#### STEP 5C. Initial electronic tool functionality check.

| **Conditions:** Connect electronic tool to a second vehicle. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Attempt to communicate with the ECM on the second vehicle using the same electronic tool hardware used on the problem vehicle. | Second ECM communicates using electronic tool? **YES** | 6A |
| Second ECM communicates using electronic tool? **NO** | 9A |  |

### STEP 6. Data link adapter power check

#### STEP 6A. Data link adapter determination check.

| **Conditions:** None |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Determine if an Inline I data link adapter is being used to communicate with the electronic service tool. Reference Procedure 022-999 (Service Tools and Hardware - Overview) in Section F, for General Information - data link adapter, in the appropriate troubleshooting and repair manual. | Is the serial port being used to communicate with the electronic service tool? **YES** | 6G |
| Is the serial port being used to communicate with the electronic service tool? **NO** | 6B |  |

#### STEP 6B. Check data link adapter power.

| **Conditions:** Connect the electronic tool hardware to the vehicle. Launch the electronic service tool. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| For all data link adapters except Inline I. Attempt to communicate with the electronic service tool and check to see if the data link adapter power light is on. Reference Procedure 022-999 (Service Tools and Hardware - Overview) in Section F, for general information - data link adapter, in the appropriate troubleshooting and repair manual. | Data link adapter power light on? **YES** | 7A |
| Data link adapter power light on? **NO** | 6C |  |

#### STEP 6C. Determination if communication is being attempted at the OEM data link dash connector

| **Conditions:** None |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check to see if communication is being attempted at the OEM data link dash connector. | Communication being attempted at the OEM data link dash connector? **YES** | 6D |
| Communication being attempted at the OEM data link dash connector? **NO** | 6E |  |

#### STEP 6D. OEM data link dash connector voltage check.

| **Conditions:** Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure voltage across the SUPPLY and ground pins of the OEM data link connector. Reference Procedure 022-999 (Service Tools and Hardware - Overview) in Section F, for in-cab data link connector, in the appropriate troubleshooting and repair manual for pin locations. | Voltage equal to or greater than 9 VDC? **YESRepair:** Replace data link adapter. | Repair complete. |
| Voltage equal to or greater than 9 VDC? **NO** | 6F |  |

#### STEP 6E. Check voltage at data link adapter auxiliary power supply.

| **Conditions:** Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the data link adapter supply voltage at the data link adapter harness connector. Reference Procedure 022-999 (Service Tools and Hardware - Overview) in Section F, for 3-pin data link cable, in the appropriate eectronic control system troubleshooting and repair manual for pin locations. | Voltage equal to or greater than 9 VDC? **YESRepair:** Replace data link adapter. | Repair complete. |
| Voltage equal to or greater than 9 VDC? **NO** | 6F |  |

#### STEP 6F. Check voltage at vehicle battery.

| **Conditions:** None |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the voltage at the vehicle battery. | Voltage equal to or greater than 11 VDC? **YESRepair:** Repair or replace damaged wiring. | Repair complete. |
| Voltage equal to or greater than 11 VDC? **NORepair:** Clean the battery connections or replace the batteries. | Repair complete. |  |

#### STEP 6G. Computer serial port voltage check

| **Conditions:** None |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| For Inline I only: Measure voltage across the SIGNAL ground pin and the data terminal ready pin and the SIGNAL ground pin and the request to send pin on the computer serial port. Reference Procedure 022-999 (Service Tools and Hardware - Overview) in Section F, for serial cable, in the appropriate troubleshooting and repair manual for pin locations. | Minimum of 5 VDC available? **YESRepair:** Replace data link adapter. | Repair complete. |
| Minimum of 5 VDC available? **NORepair:** Contact PC administration support. | Repair complete. |  |

### STEP 7. Data link circuit check

#### STEP 7A. Check J1939 or J1587 circuits.

| **Conditions:** None. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Use the following procedures to perform J1939 or J1587 circuit checks depending on the data link circuit being used. Reference Procedure 019-165 (Data Link Circuit, SAE J1939) in Section 19 in the appropriate troubleshooting and repair manual. This procedure gives information for a complete resistance check. Check for short circuit to ground. Check for short circuit from pin-to-pin. Reference Procedure 019-166 (Data Link Circuit, SAE J1587) in Section 19 in the appropriate troubleshooting and repair manual. This procedure gives information for a complete resistance check. Check for short circuit to ground. Check for short circuit from pin-to-pin. Measure the voltage. Reference Procedure 019-428 (Engine data links) in Section 19 in the appropriate troubleshooting and repair manual. Complete resistance check. Check for short circuit to ground. Check for short circuit from pin-to-pin. | Circuit check OK? **YES** | 11A |
| Circuit check OK? **NORepair:** Repair or replace the harness with the data link problem, either the engine or OEM harness. | Repair complete. |  |

### STEP 8. Initial electronic tool check

#### STEP 8A. Second vehicle availability check for electronic tool.

| **Conditions:** Verify second vehicle available for testing. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Verify if a second vehicle is available to connect to electronic tool? | Second vehicle available to connect to the electronic tool? **YES** | 8B |
| Second vehicle available to connect to the electronic tool? **NO** | 10A |  |

#### STEP 8B. Initial electronic tool functionality check.

| **Conditions:** Connect electronic tool to second vehicle. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Attempt to communicate with the ECM on the second vehicle using the electronic tool. | Second ECM communicate using the electronic tool? **YES** | 11A |
| Second ECM communicate using the electronic tool? **NO** | 10A |  |

### STEP 9. Detailed electronic tool check

#### STEP 9A. Troubleshoot electronic tool hardware.

| **Conditions:** None. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Perform troubleshooting procedures for evaluating electronic tool hardware: Data link adapter cable Data link adapter power supply cable Data link adapter Serial or universal serial bus (USB) cable Computer. Reference Procedure 022-999 (Service Tools and Hardware - Overview) in Section F, in the appropriate troubleshooting and repair manual. Complete the following checks: Initial Check - electronic service tool Initial Check - data link adapters Try another USB or serial cable Resistance Check for data link adapter cable and data link adapter power supply cable. | Electronic tool hardware check OK? **YESRepair:** Communication issue found. | 11A |
| Electronic tool hardware check OK? **NORepair:** Repair or replace damaged hardware. | Repair complete. |  |

### STEP 10. Serial cable and computer check

#### STEP 10A. Troubleshoot serial cable and computer.

| **Conditions:** None |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Perform troubleshooting procedures for evaluating the serial cable and computer. Reference Procedure 022-999 (Service Tools and Hardware - Overview) in Section F, in the appropriate troubleshooting and repair manual. Complete the following checks: Initial Check - electronic service tool Try another USB or serial Cable. | Serial cable and computer check OK? **YESRepair:** Communication issue found. | 11A |
| Serial cable and computer check OK? **NORepair:** Repair or replace damaged hardware. | Repair complete. |  |

### STEP 11. ROM boot ECM

#### STEP 11A. ROM boot tool availability check.

| **Conditions:** None |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Verify if ROM boot tool is available for specific ECM. | ROM boot tool available? **YES** | 11B |
| ROM boot tool available? **NORepair:** Replace the ECM. Reference Procedure 019-031 (Electronic Control Module (ECM)) in Section 19 in the appropriate troubleshooting and repair manual. | Repair complete. |  |

#### STEP 11B. ROM boot the ECM.

| **Conditions:** None |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| ROM boot the ECM. Reference Procedure 019-427 (ECM ROM Boot) in Section 19 in the appropriate troubleshooting and repair manual. | ECM communicates? **YESRepair:** Calibrate the ECM again. | Repair complete. |
| ECM communicates? **NORepair:** Replace the ECM. Reference Procedure 019-031 (Engine Control Module) in Section 19 in the appropriate troubleshooting and repair manual. | Repair complete. |  |
