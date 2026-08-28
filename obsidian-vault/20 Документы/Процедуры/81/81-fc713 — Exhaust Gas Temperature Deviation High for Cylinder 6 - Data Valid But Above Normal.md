---
type: "Процедура"
doc: "81-fc713"
title_en: "Exhaust Gas Temperature Deviation High for Cylinder 6 - Data Valid But Above Normal Operating Range - Moderately Severe Level"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/81/81-fc713.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/81-fc713.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK60"
  - "группа/81"
---

# Exhaust Gas Temperature Deviation High for Cylinder 6 - Data Valid But Above Normal Operating Range - Moderately Severe Level

> [!abstract] Процедура · `81-fc713`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]]
> **Семейство:** QSK60
> **Входит в руководства:** [[3666410 — QSK45 and QSK60 CENSE™ Electronic Control System Troubleshooting and Repair Manual|3666410]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2015-07-10
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/81/81-fc713.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/81-fc713.pdf)

### Fault Code: 713

### Exhaust Gas Temperature Deviation High for Cylinder 6 - Data Valid But Above Normal Operating Range - Moderately Severe Level

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 713 PID(P): SPN: 1328 FMI: 0/16 Lamp: Amber SRT: CE-713 | Exhaust Gas Temperature Deviation High for Cylinder 6 - Data Valid But Above Normal Operating Range - Moderately Severe Level. Cylinder 6 exhaust temperature is above the normal operating range. | No action taken. |

![[19903744.png]]

Exhaust Gas Temperature Sensor Circuit Cylinder 6

### Circuit Description

The exhaust gas temperature sensor circuit monitors exhaust gas temperature for cylinder 6 and passes the information to the CENSE™ engine control module (ECM) through the engine harness. The ECM monitors the temperature and compares it to the exhaust gas temperatures of other cylinders.

### Component Location

The exhaust gas temperature sensor for cylinder 6 is located at the cylinder head-to-exhaust manifold interface.

### Shoptalk

There are multiple CENSE™ ECMs for the engine models included in this manual. The ECM model displays when INSITE™ electronic service tool is connected. When troubleshooting a fault code, use the ECM model displayed in INSITE™ electronic service tool to determine which cylinder is affected. For engines with the present CM2330 ECM, the cylinder numbering sequence is described in the General Engine procedure of Section V in the QSK45 and QSK60 Service Manual, Bulletin [[4021530 — QSK45 and QSK60 Service Manual\|4021530]]. [[56-018-015-tr — General Engine|Refer to Procedure 018-015 in Section V.]]

Refer to Troubleshooting Fault Code t05-713
