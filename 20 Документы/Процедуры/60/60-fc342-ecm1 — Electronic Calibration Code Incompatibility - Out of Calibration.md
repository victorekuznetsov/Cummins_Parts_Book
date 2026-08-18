---
aliases:
  - "Несовместимость калибровочного кода — вне калибровки"
type: "Процедура"
doc: "60-fc342-ecm1"
title_en: "Electronic Calibration Code Incompatibility - Out of Calibration"
title_ru: "Несовместимость калибровочного кода — вне калибровки"
modified: "2012-12-20"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021674"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc342-ecm1.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-fc342-ecm1.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
---

# Electronic Calibration Code Incompatibility - Out of Calibration
**Несовместимость калибровочного кода — вне калибровки**

> [!abstract] Процедура · `60-fc342-ecm1`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section TF — Troubleshooting Fault Codes
> **Даты:** изменён 2012-12-20
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc342-ecm1.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-fc342-ecm1.pdf)

### Fault Code: 342-ECM1

### Electronic Calibration Code Incompatibility - Out of Calibration

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 342 PID(P): 630 SPN: FMI: 13 Lamp: Red SRT: | Electronic Calibration Code Incompatibility - Out of Calibration. | Hard to start or no start. |

![[19a00867.png]]

Electronic Control Module (ECM) - QST30 Power Generation Interface Engine

### Circuit Description

The ECMs communicate via the wiring harness.

### Component Location

ECM1, ECM2, and ECM3 are mounted above the flywheel housing on the rear of the engine. ECM1 is located (from left to right) on the left bank, followed by ECM2 in the middle, and ECM3 on the right bank. [[60-100-002 — Engine Diagrams|Refer to Procedure 100-002 in Section E.]]

### Shoptalk

There are multiple ECMs on this engine. Each ECM has an individual source address that displays when INSITE™ electronic service tool is connected to the corresponding service port. When troubleshooting a fault code, use the source address displayed in INSITE™ electronic service tool along with which service port (CM850 or CM552) you are connected to in order to determine which ECM and circuit is affected.

ECM2 (CM850) contains status information about ECM1 (CM552) and ECM3 (CM552). At key on, if the data link in interrupted between ECM2 and ECM1 and/or ECM3, the communication will not update until the data link is established. If there is a communication or performance calibration incompatibility between ECM1, ECM2, or ECM3, a fault occurs that requires a recalibration of the modules identified with the fault and source address. This is for incompatibilities in calibrations between ECM1 and ECM2 or ECM3, and not related to accessibility. ECM1, ECM2, and ECM3 can communicate, but something in ECM1 or ECM3 calibration does not match with ECM2.

Possible causes:

- Wrong or corrupt calibration

- Wrong or damaged ECM

- Private terminating resistor damaged or disconnected.

Refer to Troubleshooting Fault Code t05-342
