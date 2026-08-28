---
aliases:
  - "Цепь драйвера электромагнита клапана впрыска масла — напряжение выше нормы"
type: "Процедура"
doc: "60-fc224"
title_en: "Engine Oil Burn Valve Solenoid Driver Circuit - Voltage Above Normal or Shorted to High Source"
title_ru: "Цепь драйвера электромагнита клапана впрыска масла — напряжение выше нормы"
modified: "2020-09-28"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021674"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc224.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-fc224.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
---

# Engine Oil Burn Valve Solenoid Driver Circuit - Voltage Above Normal or Shorted to High Source
**Цепь драйвера электромагнита клапана впрыска масла — напряжение выше нормы**

> [!abstract] Процедура · `60-fc224`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section TF — Troubleshooting Fault Codes
> **Даты:** изменён 2020-09-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc224.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-fc224.pdf)

### Fault Code: 224

### Engine Oil Burn Valve Solenoid Driver Circuit - Voltage Above Normal or Shorted to High Source

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 224 PID(P): S85 SPN: 1265 FMI: 3/3 Lamp: Amber SRT: | High signal voltage detected at the engine oil burn valve solenoid driver circuit | Engine control module (ECM) turns off the engine oil burn valve solenoid driver supply voltage and the system is disabled. |

![[19a00860.png]]

Engine Oil Burn Valve Solenoid Driver Circuit.

### Circuit Description

The engine oil burn valve solenoid driver controls the flow of oil in the oil control valve during the burn cycle.

### Component Location

The engine oil burn valve solenoid is located in the top of the engine oil burn valve. The location of the burn valve is OEM dependent.

### Conditions For Running The Diagnostics

This diagnostic runs continuously when the generator set controller is active.

### Conditions For Setting The Fault Codes

The Engine Control Module (ECM) detected the engine oil burn valve solenoid driver circuit was at system voltage when the driver was off.

### Action Taken When The Fault Code Is Active

- The generator set controller displays a warning fault immediately when the diagnostics runs and fails.

### Conditions For Clearing The Fault Code

- To validate the repair, perform a keycycle, start the engine and perform the Centinel™ Operational Test using the recommended Cummins® electronic service tool or equivalent.

- The generator set controller will turn off the warning indicator immediately after the user presses reset.

- The “Reset All Faults” command in the recommended Cummins® electronic service tool or equivalent can be used to clear active faults.

### Shoptalk

Possible causes of this fault code include:

- A damaged or malfunctioning engine oil burn valve solenoid

- Malfunctioning or damaged engine wiring harness.

- Malfunctioning or damaged OEM wiring harness.

Refer to Troubleshooting Fault Code 224.
