---
aliases:
  - "Цепь клапана отсечки топлива 2 — первопричина не определена (правый ряд)"
type: "Процедура"
doc: "01-fc1212"
title_en: "Fuel Shutoff Valve 2 Circuit - Root Cause Not Known (Right Bank)"
title_ru: "Цепь клапана отсечки топлива 2 — первопричина не определена (правый ряд)"
modified: "2010-07-29"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1212.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1212.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Fuel Shutoff Valve 2 Circuit - Root Cause Not Known (Right Bank)
**Цепь клапана отсечки топлива 2 — первопричина не определена (правый ряд)**

> [!abstract] Процедура · `01-fc1212`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1212.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1212.pdf)

### Fault Code: 1212

### Fuel Shutoff Valve 2 Circuit - Root Cause Not Known (Right Bank)

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 1212 PID(P): SPN: FMI: Lamp: Shutdown SRT: | Fuel shutoff valve 2 circuit - root cause **not** known (right bank). | Engine will shut down. |

![[19803752.png]]

Fuel Shutoff Valve Solenoid Circuit

### Circuit Description

The fuel shutoff valve solenoid is a device used by the electronic control module (ECM) to control the engine fuel supply. The ECM can shut down the engine by cutting off the power to the fuel shutoff valve solenoid. This fault code can be caused by the signal shorted to low or ground, signal open, or return open.

### Component Location

Refer to the Engine Diagrams. 100-002 for the component location.

### Shoptalk

Inspect the fuel shutoff supply circuit for external wires that are, perhaps, spliced in to power another device. Remove any extra wires that are found in the circuit. If there is an external shutdown system on the vehicle that uses the fuel shutoff valve for engine shutdown, make sure it has **not** failed and lowered the voltage on the fuel shutoff circuit. Inspect the engine block to chassis ground wire to make sure it is securely fastened to a clean, dry conductive surface. Check the starter solenoid positive (+) terminal for a loose connector or accessory wiring with damaged insulation.

The diagnostic is enabled when the Run/Stop Switch is in the Run position and the engine is cranking. The fail mode **must** be corrected and the fault **must** be cleared and acknowledged before the engine will restart.

Refer to Troubleshooting Fault Code t05-1212
