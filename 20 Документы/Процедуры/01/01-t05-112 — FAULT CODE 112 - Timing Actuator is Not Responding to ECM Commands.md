---
aliases:
  - "Код 112 — привод опережения не отвечает на команды ЭБУ"
type: "Процедура"
doc: "01-t05-112"
title_en: "FAULT CODE 112 - Timing Actuator is Not Responding to ECM Commands"
title_ru: "Код 112 — привод опережения не отвечает на команды ЭБУ"
modified: "2012-02-14"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-t05-112.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-t05-112.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# FAULT CODE 112 - Timing Actuator is Not Responding to ECM Commands
**Код 112 — привод опережения не отвечает на команды ЭБУ**

> [!abstract] Процедура · `01-t05-112`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-02-14
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-t05-112.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-t05-112.pdf)

Printable Version

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Verify the complaint. |  |
|  | **STEP 1A.** Are other fault codes active besides Fault Code 112? | Other fault codes inactive |
|  | **STEP 1B.** Interview the operator. Are engine symptoms present? | Symptoms present |
| STEP 2. | Check the wiring harness. |  |
|  | **STEP 2A.** Check for an external power source on the engine harness or generator control system. | Remove the external power supply from the harness. |
| STEP 3. | Check the suction side of the fuel system flow. |  |
|  | **STEP 3A.** Check the fuel tank level. | Fuel in tank |
|  | **STEP 3B.** Inspect the fuel system for leaks, broken lines, and loose fittings. | No leaks, broken lines, or loose fittings |
|  | **STEP 3C.** Check the fuel inlet restriction. | Less than 203 mm-Hg \[8 in-Hg\] |
|  | **STEP 3D.** Check for air in the fuel. | Minimal air in the fuel |
| STEP 4. | Check the pressure-side fuel system flow. |  |
|  | **STEP 4A.** Check the fuel pump output pressure. | QSK45 140 ± 20 psi @ 750 rpm, 255 ± 30 psi @ 1500 rpm, 300 ± 30 psi @ 1800 rpm. QSK60 140 ± 20 psi @ 750 rpm, 280 ± 30 psi @ 1500 rpm, 350 ± 30 psi @ 1800 rpm |
|  | **STEP 4A-1.** Check the injector o-rings. | Drain output equal from front and rear halves |
|  | **STEP 4A-2.** Check for fuel in the oil or coolant. | No fuel in the oil or coolant |
|  | **STEP 4B.** Inspect the actuator screen for debris. | No debris |
|  | **STEP 4C.** Inspect the actuator for corrosion. | No corrosion |
| STEP 5. | Clear the fault codes. |  |
|  | **STEP 5A.** Disable the fault code. | Fault Code 112 inactive |
|  | **STEP 5B.** Clear the inactive fault codes. | All fault codes cleared |

### STEP 1. Verify the complaint.

#### STEP 1A. Are other fault codes active besides Fault Code 112?

| **Conditions:** Place the run/stop/auto switch in the STOP position. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for other active fault codes. Use INSITE™ electronic service tool to read the fault codes. | Other faults inactive. | 1B |
| Investigate other fault codes first. | Appropriate fault tree |  |

#### STEP 1B. Interview the operator. Are engine symptoms present?

| **Conditions:** Place the run/stop/auto switch in the RUN position. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Interview the operator for the following: Are engine symptoms present? Is the operator complaining about specific symptoms or shutdowns/derates due to Fault Code 112? | Symptoms present | 2A |
| Clear the fault code. Inactive faults have been logged. Since operator is not experiencing a problem, clear the fault. | 5B |  |

### STEP 2. Check the wiring harness.

#### STEP 2A. Check for external power source on the engine harness or generator control system.

| **Conditions:** Place run/stop/auto switch in the STOP position. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for external power supply (such as a battery charger) on the engine harness or generator control system. Refer to the wiring diagram for proper wiring connections. Use the following procedure for additional service literature for wiring diagram bulletin numbers. [[01-205-001 — Additional Service Literature\|Refer to Procedure 205-001 in Section L.]] |  | 3A |
| Remove the external power supply from the harness. | 5A |  |

### STEP 3. Check the suction side of the fuel system flow.

#### STEP 3A. Check the fuel tank level.

| **Conditions:** Place run/stop/auto switch in the STOP position. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the fuel tank level. | Fuel in tank | 3B |
| Fill the tank with fuel | 5A |  |

#### STEP 3B. Inspect the fuel system for leaks, broken lines, and loose fittings.

| **Conditions:** Place run/stop/auto switch in the STOP position. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the fuel system for the following: Leaks Broken lines Loose fittings. | No leaks, broken lines, or loose fittings | 3C |
| Tighten or replace the leaking fitting or fuel line. Replace the fuel line. Use the following procedure for Signature™, ISX, and QSX15 engines. Refer to Procedure 006-024 in Section 6. Use the following procedure for QSK23 engine. Refer to Procedure 006-024 in Section 6. Use the following procedure for QST30 engine. Refer to Procedure 006-024 in Section 6. Use the following procedure for QSK45 and QSK60 engines. Refer to Procedure 006-024 in Section 6. Use the following procedure for QSK78 engine. Refer to Procedure 006-024 in Section 6. | 5A |  |

#### STEP 3C. Check the fuel inlet restriction.

| **Conditions:** Place run/stop/auto switch in the RUN position. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the inlet restriction as follows: Measure the inlet restriction. Use the following procedure for Signature™, ISX, and QSX15 engines. Refer to Procedure 005-016 in Section 5. Use the following procedure for QSK23 engine. Refer to Procedure 005-016 in Section 5. Use the following procedure for QSK45 and QSK60 engines. Refer to Procedure 005-016 in Section 5. Use the following procedure for QSK78 engine. Refer to Procedure 005-016 in Section 5. | Less than 203 mm-Hg \[8 in-Hg\] | 3D |
| Find cause of restriction and remove restriction. Check for clogged fuel filters, debris in the fuel tank, fuel tank vents clogged, collapsed or faulty fuel lines, or faulty check valves. | 5A |  |

#### STEP 3D. Check for air in the fuel.

| **Conditions:** Place run/stop/auto switch in the RUN position. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for air in the fuel. Use the following procedure for Signature™, ISX, and QSX15 engines. Refer to Procedure 005-016 in Section 5. Use the following procedure for QSK23 engine. Refer to Procedure 005-016 in Section 5. Use the following procedure for QSK45 and QSK60 engines. Refer to Procedure 005-016 in Section 5. Use the following procedure for QSK78 engine. Refer to Procedure 005-016 in Section 5. | Minimal air in the fuel | 4A |
| Find cause of air in the fuel. Check for missing o-ring seals in the inlet fuel fittings or loose or broken fittings and lines. | 5A |  |

### STEP 4. Check the pressure-side fuel system flow.

#### STEP 4A. Check the fuel pump output pressure.

| **Conditions:** Place run/stop/auto switch in the RUN position. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the fuel pump output pressure. Measure the output pressure of the pump at the Compuchek® fitting. Use the following procedure for Signature™, ISX, and QSX15 engines. Refer to Procedure 005-016 in Section 5. Use the following procedure for QSK23 engine. Refer to Procedure 005-016 in Section 5. Use the following procedure for QSK45 and QSK60 engines. Refer to Procedure 005-016 in Section 5. Use the following procedure for QSK78 engine. Refer to Procedure 005-016 in Section 5. | QSK45: 140 ± 20 psi @ 750 rpm, 255 ± 30 psi @ 1500 rpm, 300 ± 30 psi @ 1800 rpm. QSK60: 140 ± 20 psi @ 750 rpm, 280 ± 30 psi @ 1500 rpm, 350 ± 30 psi @ 1800 rpm. | 4B |
|  | 4A-1 |  |

#### STEP 4A-1. Check the injector o-rings.

| **Conditions:** Place run/stop/auto switch in the RUN position. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the injector o-rings. The o-rings can be checked by observing the drain output of the front three versus the rear three cylinders. Disconnect the drain lines at the T-junction. Place each half into separate, equal-size buckets. Operate the engine at rated speed for enough time to determine if output is equal from each half. | Drain output equal from front and rear halves | 4A-2 |
| Replace the injector o-rings on faulty bank. Use the following procedure for Signature™, ISX, and QSX15 enegines. Refer to Procedure 006-026 in Section 6. Use the following procedure for QSK23 engine. Refer to Procedure 006-026 in Section 6. Use the following procedure for QST30 engine. Refer to Procedure 006-026 in Section 6. Use the following procedure for QSK45 and QSK60 engines. Refer to Procedure 006-026 in Section 6. Use the following procedure for QSK78 engine. Refer to Procedure 006-026 in Section 6. | 5A |  |

#### STEP 4A-2. Check for fuel in the oil or coolant.

| **Conditions:** Place run/stop/auto switch in the STOP position. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for fuel in the oil or coolant. | No fuel in the oil or coolant | 5A |
| Fuel in the oil or coolant | Appropriate Symptom Tree |  |

#### STEP 4B. Inspect the actuator screen for debris.

| **Conditions:** Place run/stop/auto switch in the STOP position. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the actuator screen(s) for debris. Remove the timing rail actuator(s) Number 1 and 2. Refer to Procedure 019-111 in Section 19. | No debris | 4C |
| Replace the timing rail actuator(s) screen. Refer to Procedure 019-111 in Section 19. | 5A |  |

#### STEP 4C. Inspect the actuator for corrosion.

| **Conditions:** Place run/stop/auto switch in the STOP position. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the actuator(s) for corrosion. Remove the timing actuator(s) Number 1 and 2. Refer to Procedure 019-111 in Section 19. | No corrosion | 5A |
| Replace the timing actuator(s). Refer to Procedure 019-111 in Section 19. | 5A |  |

### STEP 5. Clear the fault codes.

#### STEP 5A. Disable the fault code.

| **Conditions:** Connect all components. Connect INSITE™ electronic service tool. Place run/stop/auto switch in the STOP position. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Disable the fault code. Start the engine and run throughout the operating range to verify the Fault Code 112 stays inactive. | Fault Code 112 inactive | 5B |
| Return to the Troubleshooting Steps or contact the nearest Cummins® Authorized Repair Location if all steps have been completed and checked again. | 1A |  |

#### STEP 5B. Clear the inactive fault codes.

| **Conditions:** Place run/stop/auto switch in the STOP position. Connect all components. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Clear the inactive fault codes. Use INSITE™ electronic service tool to clear the inactive fault codes. | All fault codes cleared | Repair complete |
| Troubleshoot any remaining active fault codes. | Appropriate troubleshooting charts |  |
