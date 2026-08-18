---
aliases:
  - "Давление масла в главной магистрали — ниже нормы — умеренный уровень"
type: "Процедура"
doc: "82-fc143"
title_en: "Engine Oil Rifle Pressure - Data Valid But Below Normal Operating Range - Moderately Severe Level"
title_ru: "Давление масла в главной магистрали — ниже нормы — умеренный уровень"
modified: "2010-10-07"
engines:
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc143.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc143.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# Engine Oil Rifle Pressure - Data Valid But Below Normal Operating Range - Moderately Severe Level
**Давление масла в главной магистрали — ниже нормы — умеренный уровень**

> [!abstract] Процедура · `82-fc143`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-10-07
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc143.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc143.pdf)

### Fault Code: 143

### Engine Oil Rifle Pressure - Data Valid But Below Normal Operating Range - Moderately Severe Level

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 143 PID(P): P100 SPN: 100 FMI: 1/18 Lamp: Amber SRT: | Engine Oil Rifle Pressure - Data Valid but Below Normal Operating Range - Moderately Severe Level. Engine oil pressure signal indicates engine oil pressure is below the engine protection warning limit. | Progressive power derate increasing in severity from time of alert. |

![[19202670.png]]

ISM - Engine Oil Rifle Pressure 1

### Circuit Description

The electronic control module (ECM) provides a 5 volt supply to the engine oil pressure sensor on the sensor SUPPLY 1 circuit. The ECM also provides a ground on the sensor RETURN circuit. The engine oil pressure sensor provides a signal to the ECM on the engine oil pressure sensor SIGNAL circuit. This sensor signal voltage changes based on the pressure in the oil rifle. The ECM will detect a low signal voltage at operating conditions when the oil pressure may be slightly lower. The ECM will detect a high signal voltage during high engine speeds or operating conditions when the oil temperature is low.

If the ECM detects low signal voltage indicating a low engine oil pressure, this fault code sets.

### Component Location

The engine oil pressure sensor is located on the left side of the engine block. Use the following procedure for a detailed component location view. Refer to Procedure 100-002 in Section.E.

### Conditions For Running The Diagnostics

This diagnostic runs continuously when the keyswitch is in the ON position.

### Conditions For Setting The Fault Codes

The ECM detects that the engine oil pressure is less than 55 kPa \[8 psi\] at 800 rpm for more than 5 seconds.

### Action Taken When The Fault Code Is Active

- The ECM illuminates the amber CHECK ENGINE light immediately when the diagnostic runs and fails.

- A torque derate is issued by the ECM limiting the power output of the engine.

### Conditions For Clearing The Fault Code

The ECM will turn OFF the amber CHECK ENGINE light and the torque derate will be removed when the oil pressure reading is detected to be within the normal operating range.

### Shoptalk

Verify the electronic control module (ECM) calibration is correct. Check the calibration revision history found on QuickServe™ Online for applicable fixes to the calibration stored in the ECM. If necessary, calibrate the ECM. [[105-019-032 — Engine Control Module Calibration Code|Refer to Procedure 019-032 in Section 19.]]

This fault code goes active when the engine oil pressure drops below the engine protection limit. Troubleshoot the engine for low oil pressure.

Refer to Troubleshooting Fault Code t05-143
