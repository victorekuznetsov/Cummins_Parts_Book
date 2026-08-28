---
aliases:
  - "Разнос двигателя (превышение частоты вращения)"
type: "Процедура"
doc: "19-fc234"
title_en: "Engine Overspeed"
title_ru: "Разнос двигателя (превышение частоты вращения)"
modified: "2011-03-01"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc234.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc234.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
---

# Engine Overspeed
**Разнос двигателя (превышение частоты вращения)**

> [!abstract] Процедура · `19-fc234`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2011-03-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc234.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc234.pdf)

### Fault Code: 234

### Engine Overspeed

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 234 PID(P): P190 SPN: 190 FMI: 0 Lamp: Red SRT: 00-363 | Engine speed signal on pin 27 and pin 28 and/or pin 37 and pin 38 of the engine harness indicates an engine speed greater than the safe operation rpm limit. The limit is 2450 rpm for the QSK19 and 2190 rpm for the QSK60. | Fuel shutoff valve de-energizes (valve closes). The valve reenergizes (fuel shutoff valve opens) when engine speed falls below its upper rpm threshold. |

![[19400001.png]]

Engine Overspeed

### Circuit Description

The engine position sensor monitors the engine position and the engine speed. It then passes this information to the ECM through the engine harness.

### Component Location

The engine position sensor is located above the accessory drive.

### Shoptalk

Inspect the intake manifold for sources of flammable vapors. Check the turbocharger seals to verify that there are no oil leaks.

- Inspect the engine position sensor for signs of damage or tampering.

Refer to Troubleshooting Fault Code t05-234
