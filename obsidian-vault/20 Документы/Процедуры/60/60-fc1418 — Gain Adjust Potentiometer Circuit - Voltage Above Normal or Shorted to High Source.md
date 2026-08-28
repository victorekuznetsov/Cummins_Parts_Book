---
aliases:
  - "Цепь потенциометра усиления — напряжение выше нормы"
type: "Процедура"
doc: "60-fc1418"
title_en: "Gain Adjust Potentiometer Circuit - Voltage Above Normal or Shorted to High Source"
title_ru: "Цепь потенциометра усиления — напряжение выше нормы"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc1418.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-fc1418.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
---

# Gain Adjust Potentiometer Circuit - Voltage Above Normal or Shorted to High Source
**Цепь потенциометра усиления — напряжение выше нормы**

> [!abstract] Процедура · `60-fc1418`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section TF — Troubleshooting Fault Codes
> **Даты:** изменён 2020-09-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc1418.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-fc1418.pdf)

### Fault Code: 1418

### Gain Adjust Potentiometer Circuit - Voltage Above Normal or Shorted to High Source

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 1418 PID(P): S151 SPN: 4184 FMI: 3/3 Lamp: Amber SRT: | High signal voltage detected at the gain adjust potentiometer circuit. | None. |

![[19a00875.png]]

Gain Adjust Potentiometer Circuit

### Circuit Description

The gain adjust potentiometer is a potentiometer used by the ECM to regulate the governor gains. The potentiometer has three circuits: 5 volt supply, return, and signal circuits. The signal circuit voltage indicates the gain adjust potentiometer input to the ECM.

### Component Location

The gain adjust potentiometer is located on the generator set control panel.

### Conditions For Running The Diagnostics

This diagnostic runs continuously when the generator set controller is active.

### Conditions For Setting The Fault Codes

The Engine Control Module (ECM) detected the gain adjust potentiometer signal voltage was out of range high.

### Action Taken When The Fault Code Is Active

- The generator set controller displays a warning fault immediately when the diagnostics runs and fails.

- The engine control module (ECM) gain adjust potentiometer will go to the default value.

### Conditions For Clearing The Fault Code

- To validate the repair, start the engine and let it run for 1 minute at no load.

- The generator set controller will turn off the warning indicator immediately after the user presses reset.

- The “Reset All Faults” command in the recommended Cummins® electronic service tool or equivalent can be used to clear active faults.

### Shoptalk

Possible causes of this fault code include:

- A dirty gain adjust potentiometer.

- Malfunctioning gain adjust potentiometer.

- Malfunctioning or damaged engine wiring harness.

- Malfunctioning or damaged OEM wiring harness.

Refer to Troubleshooting Fault Code 1418.
