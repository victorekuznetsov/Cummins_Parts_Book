---
type: "Процедура"
doc: "19-fc2364"
title_en: "Engine Cold Start Aid - Condition Exists"
modified: "2020-01-27"
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
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc2364.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc2364.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
---

# Engine Cold Start Aid - Condition Exists

> [!abstract] Процедура · `19-fc2364`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2020-01-27
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc2364.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc2364.pdf)

### Fault Code: 2364

### Engine Cold Start Aid - Condition Exists

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 2364 PID(P): SPN: 854 FMI: 11/31 Lamp: Red SRT: | An open or short circuit has been detected on the ether injection circuit. | Ether start functionality will be disabled. Engine may **not** start or may be difficult to start. |

![[19400679.png]]

Ether Injection Start Circuit

### Circuit Description

The ether injection circuit is a device used by the engine to control the ether injection operation. The ether injection circuit utilizes a Pulse Width Modulated (PWM) signal. A PWM signal is pulsed voltage signal between 0-VDC and system voltage. The frequency of the pulsed voltage signal is dependent on the application requirement.

### Component Location

The control solenoid location varies by OEM. Refer to the appropriate OEM service manual to determine the location.

### Conditions For Running The Diagnostics

This diagnostic runs when the keyswitch is in the ON position and when the pulse width modulated (PWM) device is getting energized or de-energized. In some cases, the diagnostics can also run at some fixed intervals.

### Conditions For Setting The Fault Codes

The ether injection circuit pulse width modulated (PWM) signal voltage was greater than 0-VDC when the PWM signal was turned OFF by the ECM.

The ether injection circuit pulse width modulated (PWM) signal was not at system voltage when the PWM signal was turned ON.

### Action Taken When The Fault Code Is Active

The ECM illuminates the white MAINTENANCE lamp or flashes the amber CHECK ENGINE lamp, indicating a maintenance condition, immediately after the diagnostic runs and fails.

The ether injection operation will be disabled.

### Conditions For Clearing The Fault Code

- To validate the repair, perform a key cycle, and leave the key in the ON position for 1 minute.

- The fault code status displayed by the recommended Cummins electronic service tool or equivalent will change to INACTIVE immediately after the diagnostic runs and passes.

- The ECM will turn off the flashing amber CHECK ENGINE lamp / MAINTENANCE lamp immediately after the diagnostic runs and passes.

- The “Reset All Faults” command in the recommended Cummins electronic service tool or equivalent can be used to clear active and inactive faults.

### Shoptalk

Possible causes of this fault code include:

- Open signal or return circuit in the solenoid or harness.

- Signal circuit shorted to voltage source.

- Short circuit to ground in the harness or solenoid.

Refer to Troubleshooting Fault Code t05-384
