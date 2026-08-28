---
type: "Процедура"
doc: "81-fc633"
title_en: "Exhaust Gas Temperature Deviation Low for Cylinder 6 - Data Valid But Below Normal Operating Range - Least Severe Level"
modified: "2015-07-10"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
families:
  - "QSK60"
manuals:
  - "3666410"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/81/81-fc633.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/81-fc633.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK60"
  - "группа/81"
---

# Exhaust Gas Temperature Deviation Low for Cylinder 6 - Data Valid But Below Normal Operating Range - Least Severe Level

> [!abstract] Процедура · `81-fc633`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]]
> **Семейство:** QSK60
> **Входит в руководства:** [[3666410 — QSK45 and QSK60 CENSE™ Electronic Control System Troubleshooting and Repair Manual|3666410]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2015-07-10
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/81/81-fc633.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/81-fc633.pdf)

### Fault Code: 633

### Exhaust Gas Temperature Deviation Low for Cylinder 6 - Data Valid But Below Normal Operating Range - Least Severe Level

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 633 PID(P): SPN: 1328 FMI: 0/17 Lamp: Maintenance SRT: | Exhaust Gas Temperature Deviation Low for Cylinder 6 - Data Valid But Below Normal Operating Range - Least Severe Level. | Possible low power. No engine protection for exhaust gas temperature. |

![[19903744.png]]

Exhaust Gas Temperature Sensor Circuit Cylinder 6 - QSK45 and QSK60 Engines

### Circuit Description

The exhaust gas temperature sensor circuit cylinder 6 monitors exhaust gas temperature and passes information to the engine control module (ECM) through the engine harness.

### Component Location

The exhaust gas temperature sensor circuit cylinder 6 for this fault code is located in the exhaust manifold at the cylinder head 6 to exhaust manifold interface.

### Shoptalk

There are multiple CENSE™ ECMs for the engine models included in this manual. The ECM model displays when INSITE™ electronic service tool is connected. When troubleshooting a fault code, use the ECM model displayed in INSITE™ electronic service tool to determine which cylinder is affected. For engines with the present CM2330 ECM, the cylinder numbering sequence is described in the General Engine procedure of Section V in the QSK45 and QSK60 Service Manual, Bulletin [[4021530 — QSK45 and QSK60 Service Manual\|4021530]]. [[56-018-015-tr — General Engine|Refer to Procedure 018-015 in Section V.]]

The exhaust gas temperature sensor circuit cylinder 6 measures the exhaust temperature of cylinder 6. The ECM monitors the temperature and compares it to the exhaust gas temperatures of other cylinders.

It is possible that the exhaust gas temperature sensor 5 volt supply can be open and a fault will **not** be set. If this happens, the temperature of the exhaust gas temperature sensor will read 474°C \[885°F\] for the entire bank of sensors connected to that exhaust gas temperature sensor converter. See the Engine Performance Troubleshooting Tree in Section TT of the QSK45 and QSK60 Service Manual, Bulletin [[4021530 — QSK45 and QSK60 Service Manual\|4021530]], to troubleshoot this condition.

Possible causes of this fault include:

- Restricted aftercooler.

- Damaged, valves, rings, or piston.

- Injector damage.

Refer to Troubleshooting Fault Code t05-633.
