---
aliases:
  - "Цепь датчика температуры ОЖ 1 — напряжение выше нормы"
type: "Процедура"
doc: "98-fc144"
title_en: "Engine Coolant Temperature 1 Sensor Circuit - Voltage Above Normal or Shorted to High Source"
title_ru: "Цепь датчика температуры ОЖ 1 — напряжение выше нормы"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-fc144.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-fc144.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K19"
  - "группа/98"
---

# Engine Coolant Temperature 1 Sensor Circuit - Voltage Above Normal or Shorted to High Source
**Цепь датчика температуры ОЖ 1 — напряжение выше нормы**

> [!abstract] Процедура · `98-fc144`
> **Двигатели:** [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]]
> **Семейство:** K19
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2021-09-10
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-fc144.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-fc144.pdf)

### Fault Code: 144

### Engine Coolant Temperature 1 Sensor Circuit - Voltage Above Normal or Shorted to High Source

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 144 PID(P): P110 SPN: FMI: 3 Lamp: On SRT: 00-626 | High signal voltage detected at the engine coolant temperature sensor circuit. | None on performance. |

![[19802305.png]]

Coolant Temperature Sensor Circuit

### Circuit Description

The engine coolant temperature sensor is a variable resistor sensor used by the ECM to monitor the engine coolant temperature. Signals from the engine coolant temperature sensor are not used by the CENTRY™ ECM to control the engine. The engine coolant temperature sensor has two circuits: signal, and return circuits. The signal voltage indicates the coolant temperature.

### Component Location

The location of the coolant temperature sensor may vary and is OEM dependent.

### Conditions For Running The Diagnostics

This diagnostic runs continuously when the keyswitch is in the ON position.

### Conditions For Setting The Fault Codes

The Engine Control Module (ECM) detected that the engine coolant temperature sensor signal voltage was out of range high.

### Action Taken When The Fault Code Is Active

- The ECM illuminates the amber CHECK ENGINE light when the diagnostic runs and fails.

- No engine protection for engine coolant temperature.

For Power Generation Applications:

- The generator set controller displays the fault immediately when the diagnostics runs and fails.

- No engine protection for engine coolant temperature.

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

Possible causes of this fault code include:

- Malfunctioning or damaged engine wiring harness.

- Malfunctioning or damaged OEM wiring harness.

- Damaged or loose connectors.

- Malfunctioning or damaged engine coolant temperature sensor.

Refer to Troubleshooting Fault Code t05-144
