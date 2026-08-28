---
aliases:
  - "Останов: проверка достоверности"
type: "Процедура"
doc: "330-t02-1015"
title_en: "Sd Rationality Check"
title_ru: "Останов: проверка достоверности"
modified: "2024-08-13"
engines:
  - "33239746"
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
manuals:
  - "4358403"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/330/330-t02-1015.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/330-t02-1015.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/330"
---

# Sd Rationality Check
**Останов: проверка достоверности**

> [!abstract] Процедура · `330-t02-1015`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Входит в руководства:** [[4358403 — Dual Fuel Technology DF101 Master Repair Manual|4358403]]
> **Секции:** Section TA - Troubleshooting Alarm Codes
> **Даты:** изменён 2024-08-13
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/330/330-t02-1015.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/330-t02-1015.pdf)

Printable Version

### Symptoms

Dual Fuel operation will stop. Engine will continue to operate in diesel **only** mode.

### How To Use This Tree

**Circuit Description:**

Alarm is activated if difference between engine power based on diesel consumption and engine power based on value transmitted from OEM/ECM is greater than 25 percent of engine rated power at given rpm and altitude for at least 4s prior to start of the gas substitution.

**Conditions for Running the Diagnostics:**

Only active in MAN and AUT before transition to Dual Fuel operation, when all condition for running in Dual fuel are met **.Conditions for Activating the Fault Message:**

Alarm is activated if difference between engine power based on diesel consumption and engine power based on value transmitted from OEM/ECM is greater than 25 percent of engine rated power at given rpm and altitude for at least 4s prior to start of the gas substitution.

**Conditions for Clearing the Fault Code Automatically:**

None.

**Conditions for Clearing the Fault Code Manually:**

Latching fault, reset is required. Once Sd message is activated controller switches to Diesel only state, and the message will become inactive. When problem is solved it can be cleared from IMON or IV5 by pressing fault reset.

### Shoptalk

Possible causes include:

- Incorrect power reading

- Incorrect fuel consumption reading due to injector drift

- Engine fuel system failure.

| **Fault Message FLS DetonationAnalog 4-20 mA Signal is Missing from IBF CU Input at Analog Input Channel** |  |  |
|---|---|---|
| **Code or Message** | **Reason** | **Effect** |
| Sd Rationality Check | Rationality Check indicates the calculated diesel power (kW) is out of tolerance. | Dual fuel control system will **not** allow gas operations. Dual fuel controller will stop gas flow. |

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check for errors. |  |
|  | **STEP 1A.** Check the engine ECM for engine fault codes. | Engine ECM indicates fault codes? |
|  | **STEP 1B.** Review the fault message(s). | Sd RationalCheck alarm code present? |
|  | **STEP 1C.** Review the fault message(s). | Alarm Codes other than Sd RationalCheck present? |
| STEP 2. | Engine load **not** within set limit. |  |
|  | **STEP 2A.** Verify source for engine power value. | Pump using Real Power message shown in J1939? |
|  | **STEP 2B.** Verify Real Power transmitted value (J1939). | Do J1939 transmitted power limits correspond with pump power rating? |
|  | **STEP 2C.** Verify engine load limits (Converted). | Do power limits correspond with pump power rating? |
| STEP 3. | Check for fault messages. |  |
|  | **STEP 3A.** Reset the fault. | Fault returns? |

### STEP 1. Check for errors.

#### STEP 1A. Check the engine ECM for engine fault codes.

| **Conditions:** Turn keyswitch ON. Connect the recommended Cummins® electronic service tool or equivalent. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Use the recommended Cummins® electronic service tool or equivalent to read the fault code. | Engine ECM indicates fault codes? **YES** | Troubleshoot engine fault codes prior to Troubleshooting Alarm Codes. |
| Engine ECM indicates fault codes? **NO** | 1B |  |

#### STEP 1B. Review the fault message(s).

| **Conditions:** Power ON dual fuel control module. Connect InteliMonitor to the dual fuel control panel. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check local display panel or IntelliMonitor for fault messages in alarm list and history. | Sd RationalCheck alarm code present? **YES** | 1C |
| Sd RationalCheck alarm code present? **NO** | Return the pump to service and monitor. |  |

#### STEP 1C. Review the fault message(s).

| **Conditions:** Power ON dual fuel control module. Connect InteliMonitor to the dual fuel control panel. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check local display panel or IntelliMonitor for fault messages in alarm list and history. | Alarm Codes other than Sd RationalCheck present? **YES** | Troubleshoot all other error codes prior to troubleshooting Sd RationalCheck. |
| Alarm Codes other than Sd RationalCheck present? **NO** | 2A |  |

### STEP 2. Engine load **not** within set limit.

#### STEP 2A. Verify source for engine power value.

| **Conditions:** Power ON dual fuel control module. Connect InteliMonitor to the dual fuel control panel. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Verify power source in PLC Monitor. (Converted or J1939). | Pump using Real Power message shown in J1939? **YES** | 2B |
| Pump using Real Power message shown in J1939? **NO** | 2C |  |

#### STEP 2B. Verify Real Power transmitted value (J1939).

| **Conditions:** Power ON dual fuel control module. Connect InteliMonitor to the dual fuel control panel. Connect the recommended Cummins® electronic service tool or equivalent |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Monitor value for Real Power transmitted via J1939 on IV5 screen 7 OR IMON – ECU – Pwr-Real R. Verify engine is operating within power limits. (2250 HP engine 373-1578 kW) (2500 HP engine: 373-1748 kW) If both 4-20ma input and J1939 message are present, the J1939 message takes priority and control ignores the converted signal. All limits should still be in the same range. | Do J1939 transmitted power limits correspond with pump power rating? **YES** | 3A |
| Do J1939 transmitted power limits correspond with pump power rating? **NORepair:** For pump with J1939 Real Power Value: Connect the recommended Cummins® electronic service tool or equivalent and verify that power rating transmitted through the ECM is correct. If value is incorrect from the OEM, then the OEM or customer needs to correct this value. | Contact a Cummins® Authorized Repair Location. |  |

#### STEP 2C. Verify engine load limits (Converted).

| **Conditions:** Power ON dual fuel control module. Connect InteliMonitor to the dual fuel control panel. Connect the recommended Cummins® electronic service tool or equivalent. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Compare the value the OEM is transmitting for Engine HP matches value read in IMON -Analog CU - FracPumpHP OEM sends linear signal as 4-20 mA corresponding to 0-2500 HP (based on engine rating). | Do power limits correspond with pump power rating? **YES** | 3A |
| Do power limits correspond with pump power rating? **NORepair:For pumps with converted power limits:** Using a DMM ensure that power rating signal on BF1-A2 is correct. If value is incorrect from the OEM, then the OEM or customer needs to correct this value. If value from OEM is correct and error persists replace IBF Module. | Repair complete |  |

### STEP 3. Check for fault messages.

#### STEP 3A. Reset the fault.

| **Conditions:** Engine not operating. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Reset the fault on the control panel or through InteliMonitor. Operate the engine under conditions to allow gas substitution. | Fault returns? **YESRepair:** Verify all engine systems are working correctly. Correct any malfunctions on the engine. Attempt to reset the fault. Return to the troubleshooting steps or contact a Cummins® Authorized Repair Location if all steps have been completed and checked again. | 1A |
| Fault returns? **NO** | Repair complete. |  |
