---
aliases:
  - "Низкое выходное напряжение генератора"
type: "Процедура"
doc: "01-fc1447"
title_en: "Generator AC Output Voltage - Low"
title_ru: "Низкое выходное напряжение генератора"
modified: "2012-05-08"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1447.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1447.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Generator AC Output Voltage - Low
**Низкое выходное напряжение генератора**

> [!abstract] Процедура · `01-fc1447`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-05-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1447.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1447.pdf)

### Fault Code: 1447

### Generator AC Output Voltage - Low

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 1447 PID(P): SPN: FMI: Lamp: Shutdown SRT: | Generator AC output voltage is low. | Generator set will shut down. |

![[19802905.png]]

Generator Circuit

### Circuit Description

The generator set produces electric power. This power is in the form of three-phase AC. The engine control module (ECM) monitors the performance and operation of the generator set. The threshold for a low AC output voltage condition is that one or more of the phase voltages has dropped below 85 percent of nominal for at least 10 seconds.

The ECM uses this fault code to tell the operator when he generator set AC output voltage is low.

### Component Location

Refer to customer/facility/installation documentation for diagrams on the generator set/electrical bus setup.

### Shoptalk

If output voltage is low, the control can **not** drive the output voltage high enough. This fault can be caused by a failed voltage regulator, PT/CT board, bad PMG on field wirings, or an open or short circuit in one of the harnesses.

If the voltages at the output leads of the alternator are significantly higher than the voltages read by INSITE™ electronic service tool, the problem can be in the voltage sensing circuits.

If the voltage regulator is getting B positive (+). but the isolated supply LED is **not** lit, the problem is with the voltage regulator.

Check for overload.

Refer to Troubleshooting Fault Code t05-1447.
