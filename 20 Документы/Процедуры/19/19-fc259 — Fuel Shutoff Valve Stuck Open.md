---
type: "Процедура"
doc: "19-fc259"
title_en: "Fuel Shutoff Valve Stuck Open"
modified: "2017-01-02"
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
figures: 2
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc259.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc259.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
---

# Fuel Shutoff Valve Stuck Open

> [!abstract] Процедура · `19-fc259`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2017-01-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc259.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc259.pdf)

### Fault Code: 259

### Fuel Shutoff Valve Stuck Open

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 259 PID(P): S17 SPN: 632 FMI: 7 Lamp: Red SRT: 00-396 | Fuel shutoff valve is open and will **not** close. | No action by the engine control module (ECM) is taken. |

![[19400833.png]]

QSK19, QSK45, and QSK78 - Fuel Shutoff Solenoid Circuit

![[19j00593.png]]

QSK23 - Fuel Shutoff Solenoid Circuit

### Circuit Description

The fuel shutoff solenoid is a device used by the ECM to control the fuel supply to the rail fueling circuit. The ECM can shut down the engine by cutting off the power to the fuel shutoff solenoid.

### Component Location

The fuel shutoff solenoid is located between the rail and timing actuators on the control valve body behind the ECM.

### Shoptalk

- The fuel shutoff solenoid **only** stops fuel to the rail circuit; the timing circuit bypasses the fuel shutoff solenoid.

- Inspect the fuel shutoff supply circuit for external wires that can be spliced in to power another device. Remove any extra wires that are found in the circuit.

- If there is an external shutdown system on the vehicle that uses the fuel shutoff valve for engine shutdown, make sure it has **not** failed and lowered the voltage on the fuel shutoff circuit.

- Inspect the engine block-to-chassis ground wire to make sure it is securely fastened to a clean, dry surface.

- Check the starter solenoid positive (+) terminal for a loose connector and/or accessory wiring with damaged insulation.

Refer to Troubleshooting Fault Code t05-259
