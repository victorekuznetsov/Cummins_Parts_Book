---
aliases:
  - "Цепь питания электромагнита отсечки топлива"
type: "Процедура"
doc: "82-fc254"
title_en: "Fuel Shutoff Solenoid Supply Circuit"
title_ru: "Цепь питания электромагнита отсечки топлива"
modified: "2010-09-02"
engines:
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc254.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc254.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# Fuel Shutoff Solenoid Supply Circuit
**Цепь питания электромагнита отсечки топлива**

> [!abstract] Процедура · `82-fc254`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc254.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc254.pdf)

### Fault Code: 254

### Fuel Shutoff Solenoid Supply Circuit

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 254 PID(P): S017 SPN: 632 FMI: 4/4 Lamp: Red SRT: | Less than Positive (+) 6 VDC detected at fuel shutoff circuit or an excessive current draw from the electronic control module (ECM) or faulty ECM output circuit. | The ECM turns off the fuel shutoff supply voltage. The engine will shut down. |

![[19c00264.png]]

Fuel Shutoff Solenoid Circuit

### Circuit Description

The fuel shutoff solenoid is a device used by the ECM to control the engine fuel supply. The ECM can shut down the engine by cutting off the power to the fuel shutoff solenoid.

### Component Location

The fuel shutoff solenoid is located on the fuel pump housing near the fuel outlet line. Unspecified earlier versions used a dedicated return wire (pin 32) that is mounted to one of the shutoff solenoid mounting bolts. Newer models use **only** a fuel shutoff supply wire (pin 33).

### Shoptalk

- Inspect the fuel shutoff supply circuit for external wires that can be spliced in to power another device. Remove any extra wires that are found in the circuit.

- If there is an external shutdown system on the vehicle that uses the fuel shutoff valve for engine shutdown, make sure it has **not** failed and pulled down the voltage on the fuel shutoff circuit.

- Inspect the engine-block-to-chassis ground wire to make sure it is securely fastened to a clean, dry, conductive surface.

- Check the starter solenoid Positive (+) terminal for a loose connector or accessory wiring with damaged insulation.

Refer to Troubleshooting Fault Code t05-254
