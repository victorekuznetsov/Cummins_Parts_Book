---
type: "Процедура"
doc: "98-fc445"
title_en: "Intermediate-Speed/Alternate Droop Validation Signal Circuit - Voltage Below Normal or Shorted to Low Source"
modified: "2021-09-10"
engines:
  - "37269910"
  - "37280605"
families:
  - "K19"
manuals:
  - "3666070"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-fc445.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-fc445.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K19"
  - "группа/98"
---

# Intermediate-Speed/Alternate Droop Validation Signal Circuit - Voltage Below Normal or Shorted to Low Source

> [!abstract] Процедура · `98-fc445`
> **Двигатели:** [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]]
> **Семейство:** K19
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2021-09-10
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-fc445.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-fc445.pdf)

### Fault Code: 445

### Intermediate-Speed/Alternate Droop Validation Signal Circuit - Voltage Below Normal or Shorted to Low Source

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 445 PID(P): S254 SPN: FMI: 3 Lamp: On SRT: 00-639 | The intermediate-speed/alternate droop validation signal is on and the intermediate-speed signal or alternate droop signal is off. | Loss of intermediate-speed and alternate droop features. |

![[19802310.png]]

Intermediate-Speed/Alternate Droop Validation Signal Circuit

### Circuit Description

The intermediate-speed/alternate droop validation signal is a safety feature that enables the intermediate-speed and alternate droop features while the validation signal is detected as a high voltage. The intermediate-speed switch and alternate droop switch provide the intermediate-speed, alternate droop, and intermediate-speed/alternate droop validation signals to the ECM through the OEM harness and the main engine harness.

### Component Location

The intermediate-speed switch and the alternate droop switch location may vary and is OEM dependent.

### Conditions For Running The Diagnostics

This diagnostic runs continuously when the engine is running.

### Conditions For Setting The Fault Codes

The Engine Control Module (ECM) detected low voltage at the intermediate-speed/alternate droop validation signal, and high voltage detected at the intermediate-speed signal or high voltage detected at the alternate droop signal.

### Action Taken When The Fault Code Is Active

- The ECM illuminates the amber CHECK ENGINE light when the diagnostic runs and fails.

- No engine protection for engine oil pressure.

For Power Generation Applications:

- The generator set controller displays the fault immediately when the diagnostics runs and fails.

- No engine protection for engine engine oil pressure.

### Conditions For Clearing The Fault Code

- To validate the repair, perform a key cycle, start the engine and let it idle for 1 minute.

- The fault code status displayed by the recommended Cummins® electronic service tool or equivalent will change to INACTIVE immediately after the diagnostic runs and passes.

- The ECM will turn off the amber CHECK ENGINE lamp immediately after the diagnostic runs and passes.

- The “Reset All Faults” command in the recommended Cummins® electronic service tool or equivalent can be used to clear active and inactive faults.

For Power Generation Applications:

- To validate the repair, start the engine and let it run for 1 minute at no load.

- The generator set controller will turn off the indicator immediately after the user presses reset.

- The “Reset All Faults” command in the recommended Cummins® electronic service tool or equivalent can be used to clear active faults.

### Shoptalk

- This fault code will **not** be active while the intermediate-speed or alternate droop switches are in the OFF position.

Possible causes of this fault code include:

- Malfunctioning or damaged engine wiring harness.

- Malfunctioning or damaged OEM wiring harness.

- Damaged or loose connectors.

- Malfunctioning or damaged alternate torque idle switch.

- Malfunctioning or damaged intermediate-speed switch (retard).

- Malfunctioning or damaged alternate droop switch.

Refer to Troubleshooting Fault Code t05-445
