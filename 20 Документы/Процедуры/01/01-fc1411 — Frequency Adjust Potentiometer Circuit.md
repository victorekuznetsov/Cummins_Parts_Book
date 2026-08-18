---
aliases:
  - "Цепь потенциометра регулировки частоты"
type: "Процедура"
doc: "01-fc1411"
title_en: "Frequency Adjust Potentiometer Circuit"
title_ru: "Цепь потенциометра регулировки частоты"
modified: "2010-07-29"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1411.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1411.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Frequency Adjust Potentiometer Circuit
**Цепь потенциометра регулировки частоты**

> [!abstract] Процедура · `01-fc1411`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1411.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1411.pdf)

### Fault Code: 1411

### Frequency Adjust Potentiometer Circuit

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 1411 PID(P): SPN: FMI: Lamp: Warning SRT: | Frequency adjust potentiometer signal is shorted high. | The frequency adjustment feature will be disabled and a default value of zero will be used. Possible loss of performance. |

![[19802448.png]]

Frequency Adjust Potentiometer Circuit

### Circuit Description

The frequency adjust potentiometer is so the operator can adjust the breakpoint frequency for the 100-percent 0.8 power factor load acceptance. This is the frequency at which the generator set output voltage starts to drop. The ECM monitors the voltage and expects to see the voltage vary between 0.5 and 4.5 VDC during normal operation. High voltage will trip Fault Code 1411 and can be caused by shorts in the signal wire, an open in the return wire, or a failed potentiometer.

### Component Location

Refer to the OEM manual for location.

### Shoptalk

Potentiometers are very sensitive to the environment. Clean the potentiometer and check its resistance first.

Refer to Troubleshooting Fault Code t05-1411
