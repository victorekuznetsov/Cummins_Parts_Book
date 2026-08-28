---
type: "Процедура"
doc: "19-t05-514"
title_en: "FAULT CODE 514 - Rail Fueling Flow Mismatch"
modified: "2014-12-02"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
  - "85017333"
families:
  - "QSK23"
  - "QSK60"
manuals:
  - "3666113"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-t05-514.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-t05-514.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
---

# FAULT CODE 514 - Rail Fueling Flow Mismatch

> [!abstract] Процедура · `19-t05-514`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2014-12-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-t05-514.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-t05-514.pdf)

Printable Version

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Verify the complaint. |  |
|  | **STEP 1A.** Check for active fault codes other than Fault Code 514. | Fault codes active? |
|  | **STEP 1B.** Interview the driver for engine symptoms present. | Symptoms present? |
|  | **STEP 1C.** Monitor the rail parameters for over-pressurization of the rail fuel. | Over-pressurizing the rail fuel? |
| STEP 2. | Check the inlet side of the fuel system. |  |
|  | **STEP 2A.** Check the fuel tank level. | Fuel in tank? |
|  | **STEP 2B.** Inspect the fuel system for leaks, broken lines, and loose fittings. | Broken lines, loose fittings or fuel leaks? |
|  | **STEP 2C.** Check the fuel inlet restriction. | Greater than 203 mm Hg \[8 in Hg\]? |
|  | **STEP 2D.** Check for air in the fuel. | Air in fuel? |
|  | **STEP 2E.** Inspect the fuel shutoff solenoid for excessive wear. | Excessive wear? |
| STEP 3. | Check the fuel system components. |  |
|  | **STEP 3A.** Check the fuel pump output pressure. | Fuel pump output pressure correct? |
|  | **STEP 3A-1.** Check the injector o-rings. | Drain output equal from front and rear halves? |
|  | **STEP 3A-2.** Check for fuel in the oil or coolant. | Fuel in oil or coolant? |
|  | **STEP 3B.** Inspect the actuator screen for debris. | Debris on inlet actuator screen? |
|  | **STEP 3C.** Inspect the actuator for corrosion. | Corrosion on actuator? |
| STEP 4. | Clear the fault codes. |  |
|  | **STEP 4A.** Disable the fault code. | Fault Code 514 inactive? |
|  | **STEP 4B.** Clear the inactive fault codes. | Fault codes cleared? |

### STEP 1. Verify the complaint.

#### STEP 1A. Check for active fault codes other than Fault Code 514.

| **Conditions:** Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for active fault codes other than Fault Code 514. Use INSITE™ electronic service tool to read the fault codes. | Fault codes active? **YESRepair:** Investigate other fault codes first. | Appropriate fault code procedure |
| Fault codes active? **NO** | 1B |  |

#### STEP 1B. Interview the driver for engine symptoms present.

| **Conditions:** Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Interview the driver for the following: Ask the operator if specific symptoms or shutdowns/derates due to Fault Code 112 are present. | Symptoms present? **YES** | 1C |
| Symptoms present? **NORepair:** Clear the fault code. Inactive faults have been logged. Since the customer is **not** experiencing a problem, clear the fault code. | 4B |  |

#### STEP 1C. Monitor the rail parameters for over-pressurization of the rail fuel.

| **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Monitor the rail parameters for over-pressurization of the rail fuel. Use INSITE™ electronic service tool to monitor the desired timing fueling and the estimated rail fueling parameters. Is the estimated rail fueling consistently higher than the desired rail fueling? If it is higher, it is over-pressurizing the rail fueling. | Rail fuel over-pressurized? **YESRepair:** Replace the rail actuator. [[19-019-339 — Timing Actuator\|Refer to Procedure 019-339 in Section 19.]] | 2A |
| Rail fuel over-pressurized? **NO** | 4A |  |

### STEP 2. Check the inlet side of the fuel system.

#### STEP 2A. Check the fuel tank level.

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the fuel tank level for the following: Fuel in the tank? | Fuel in tank? **YES** | 2B |
| Fuel in tank? **NORepair:** Fill the fuel tank. | 4A |  |

#### STEP 2B. Inspect the fuel system for leaks, broken lines, and loose fittings.

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the fuel system for the following: Leaks Broken lines Loose fittings. | Broken lines, loose fittings, or fuel leaks? **YESRepair:** Repair the leak. Tighten or replace the leaking fitting or fuel line. Replace the fuel line. Use the following procedure in the QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual, Bulletin [[4021592 — QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual\|4021592]]. Refer to Procedure 006-024 in Section 6. Use the following procedure in the QSK23 Troubleshooting and Repair Manual, Bulletin [[4021375 — QSK23 Troubleshooting and Repair Manual\|4021375]]. Refer to Procedure 006-024 in Section 6. Use the following procedure in the QSK45 and QSK60 Service Manual, Bulletin [[4021530 — QSK45 and QSK60 Service Manual\|4021530]]. Refer to Procedure 006-024 in Section 6. Use the following procedure in the QSK78 Troubleshooting and Repair Manual, Bulletin 3666727. Refer to Procedure 006-024 in Section 6. | 4A |
| Broken lines, loose fittings, or fuel leaks? **NO** | 2C |  |

#### STEP 2C. Check the fuel inlet restriction.

| **Conditions:** Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the fuel inlet restriction as follows: Measure the inlet restriction. Use the following procedure in the QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual, Bulletin [[4021592 — QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual\|4021592]]. Refer to Procedure 005-016 in Section 5. Use the following procedure in the QSK23 Troubleshooting and Repair Manual, Bulletin [[4021375 — QSK23 Troubleshooting and Repair Manual\|4021375]]. Refer to Procedure 005-016 in Section 5. Use the following procedure in the QSK45 and QSK60 Service Manual, Bulletin [[4021530 — QSK45 and QSK60 Service Manual\|4021530]]. Refer to Procedure 005-016 in Section 5. Use the following procedure in the QSK78 Troubleshooting and Repair Manual, Bulletin 3666727. Refer to Procedure 005-016 in Section 5. | Greater than 203 mm Hg \[8 in Hg\]? **YESRepair:** Find the cause of restriction and remove restriction. Check for clogged fuel filters, debris in the fuel tank, fuel tank vents clogged, collapsed or faulty fuel lines, or faulty check valves. | 4A |
| Greater than 203 mm Hg \[8 in Hg\]? **NO** | 2D |  |

#### STEP 2D. Check for air in the fuel.

| **Conditions:** Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for air in the fuel. Check for air in the fuel system. Use the following procedure in the QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual, Bulletin [[4021592 — QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual\|4021592]]. Refer to Procedure 005-016 in Section 5. Use the following procedure in the QSK23 Troubleshooting and Repair Manual, Bulletin [[4021375 — QSK23 Troubleshooting and Repair Manual\|4021375]]. Refer to Procedure 005-016 in Section 5. Use the following procedure in the QSK45 and QSK60 Service Manual, Bulletin [[4021530 — QSK45 and QSK60 Service Manual\|4021530]]. Refer to Procedure 005-016 in Section 5. Use the following procedure in the QSK78 Troubleshooting and Repair Manual, Bulletin 3666727. Refer to Procedure 005-016 in Section 5. | Air in fuel? **YESRepair:** Find the cause of air in the fuel. Check for missing o-ring seals in the inlet fuel fittings, loose or broken fittings, and broken lines. | 4A |
| Air in fuel? **NO** | 3A |  |

#### STEP 2E. Inspect the fuel shutoff solenoid for excessive wear.

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the fuel shutoff solenoid for excessive wear. Remove the fuel shutoff solenoid and inspect the spacer for excessive wear. Refer to Procedure 019-050 in Section 19. | Excessive wear? **YESRepair:** Repair or replace the fuel shutoff valve. [[19-019-050 — Fuel Shutoff Valve\|Refer to Procedure 019-050 in Section 19.]] | 4A |
| Excessive wear? **NO** | 4A |  |

### STEP 3. Check the fuel system components.

#### STEP 3A. Check the fuel pump output pressure.

| **Conditions:** Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the fuel pump output pressure. Measure the output pressure of the pump at the Compuchek™ fitting. Use the following procedure in the QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual, Bulletin [[4021592 — QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual\|4021592]]. Refer to Procedure 005-016 in Section 5. Use the following procedure in the QSK23 Troubleshooting and Repair Manual, Bulletin [[4021375 — QSK23 Troubleshooting and Repair Manual\|4021375]]. Refer to Procedure 005-016 in Section 5. Use the following procedure in the QSK45 and QSK60 Service Manual, Bulletin [[4021530 — QSK45 and QSK60 Service Manual\|4021530]]. Refer to Procedure 005-016 in Section 5. Use the following procedure in the QSK78 Troubleshooting and Repair Manual, Bulletin 3666727. Refer to Procedure 005-016 in Section 5. | Fuel pump output pressure correct? **YESRepair:** Minimum Output Pressure for QSK19: Minimum 379 kPa \[55 psi\] @ 600 rpm Minimum 1207 kPa \[175 psi\] @ 1300 rpm Minimum 1724 kPa \[250 psi\] @ 2100 rpm Minimum 1827 kPa \[265 psi\] @ 2350 rpm. Minimum Output Pressure for QSK23: Minimum 689 kPa \[100 psi\] @ 600 rpm Minimum 910 kPa \[132 psi\] @ 1000 rpm Minimum 1207 kPa \[175 psi\] @ 1400 rpm Minimum 1434 kPa \[208 psi\] @1500 rpm Minimum 1779 kPa \[258 psi\] @ 1800 rpm Minimum 1999 kPa \[290 psi\] @ 2100 rpm. Minimum Output Pressure for QSK45 and QSK60: Minimum 758 kPa \[110 psi\] @ 600 rpm Minimum 1379 kPa \[200 psi\] @ 1300 rpm Minimum 1724 kPa \[250 psi\] @ 1900 rpm Minimum 1793 kPa \[260 psi\] @ 2300 rpm. Minimum Output Pressure for QSK78: Minimum 793 kPa \[115 psi\] @ 600 rpm Minimum 1689 kPa \[245 psi\] @ 1300 rpm Minimum 2068 kPa \[300 psi\] @ 1900 rpm Minimum 2482 kPa \[360 psi\] @ 2300 rpm. | 3B |
| Fuel pump output pressure correct? **NORepair:** Continue troubleshooting. | 3A-1 |  |

#### STEP 3A-1. Check the injector o-rings.

| **Conditions:** Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the injector o-rings. The o-rings can be checked by observing the drain output of the front three versus the rear three cylinders on the QSK19 series engines and by observing the drain output of the left bank of cylinders versus the right bank of cylinders on the QSK45 and QSK60 series engines. Disconnect the drain lines at the T-junction. Place each half into separate, equal-size buckets. Operate the engine at rated speed for enough time to determine if output is equal from each half. | Drain output equal from front and rear halves? **YES** | 3A-2 |
| Drain output equal from front and rear halves? **NORepair:** Replace the injector o-rings on faulty bank. Replace the injector. Use the following procedure in the QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual, Bulletin [[4021592 — QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual\|4021592]]. Refer to Procedure 006-026 in Section 6. Use the following procedure in the QSK23 Troubleshooting and Repair Manual, Bulletin [[4021375 — QSK23 Troubleshooting and Repair Manual\|4021375]]. Refer to Procedure 006-026 in Section 6. Use the following procedure in the QSK45 and QSK60 Service Manual, Bulletin [[4021530 — QSK45 and QSK60 Service Manual\|4021530]]. Refer to Procedure 006-026 in Section 6. Use the following procedure in the QSK78 Troubleshooting and Repair Manual, Bulletin 3666727. Refer to Procedure 006-026 in Section 6. | 4A |  |

#### STEP 3A-2. Check for fuel in the oil or coolant.

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for fuel in the oil or coolant. Investigate for fuel or oil in coolant. | Fuel in oil or coolant? **YESRepair:** Replace the rail actuator. [[19-019-339 — Timing Actuator\|Refer to Procedure 019-339 in Section 19.]] | Appropriate troubleshooting symptom tree |
| Fuel in oil or coolant? **NO** | 4A |  |

#### STEP 3B. Inspect the actuator screen for debris.

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the actuator screen for debris Remove the rail actuator to inspect the screen for debris. Refer to Procedure 019-339 in Section 19. | Debris on inlet actuator screen? **YESRepair:** Replace the rail actuator screen. Refer to Procedure 019-112 in Section 19. | 4A |
| Debris on inlet actuator screen? **NO** | 3C |  |

#### STEP 3C. Inspect the actuator for corrosion.

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the actuator for corrosion. Remove the rail actuator to inspect for corrosion. Refer to Procedure 019-339 in Section 19. | Corrosion on actuator? **YESRepair:** Replace the rail actuator. Refer to Procedure 019-112 in Section 19. | 4A |
| Corrosion on actuator? **NO** | 4A |  |

### STEP 4. Clear the fault code.

#### STEP 4A. Disable the fault code.

| **Conditions:** Connect all components. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Disable the fault code. Start the engine and run throughout the operating range to verify that Fault Code 514 stays inactive. | Fault Code 514 inactive? **YES** | 4B |
| Fault Code 514 inactive? **NORepair:** Return to the troubleshooting steps or contact a Cummins® Authorized Repair Location if all steps have been completed and checked again. | 1A |  |

#### STEP 4B. Clear the inactive fault codes.

| **Conditions:** Connect all components. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Clear the inactive fault codes. Use INSITE™ electronic service tool to clear the inactive fault codes. | Fault codes cleared? **YESRepair:** Troubleshoot any remaining active fault codes. | Repair complete |
| Fault codes cleared? **NO** | Appropriate troubleshooting charts |  |
