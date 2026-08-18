---
aliases:
  - "Электронный блок управления двигателем"
type: "Процедура"
doc: "60-019-031"
title_en: "Engine Control Module"
title_ru: "Электронный блок управления двигателем"
modified: "2014-04-17"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021674"
figures: 3
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-019-031.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-019-031.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
---

# Engine Control Module
**Электронный блок управления двигателем**

> [!abstract] Процедура · `60-019-031`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section 19 - Electronic Controls · Section 19 — Electronic Engine Controls — Group 19
> **Даты:** изменён 2014-04-17
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-019-031.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-019-031.pdf)

### Initial Check

The QST30 Power Generation Engine has two CM552 ECMs and one CM850 ECM. The procedure for the two CM552 engine control modules (ECMs) is the same as for the CM850 ECM.

Turn the Run/Stop switch to the Stop position.

> [!note] Note · Примечание
> Communicate with the CM850 ECM first.

Connect INSITE™ electronic service tool to the CM850 (public data link) SAE J1939 data link service connector.

INSITE™ electronic service tool **must** be able to communicate with the ECM. If INSITE™ electronic service tool does **not** communicate with the ECM, refer to the INSITE™ Electronic Service Tool User's manual or to the ECM No Communication troubleshooting tree.

Record all programmable parameters. This information will be used to calibrate the ECM. Refer to the INSITE™ Electronic Service Tool User's manual.

![[19800902.png]]

### Remove

Disconnect the ECM engine harness connectors.

Remove the ECM mounting capscrews.

Remove the ECM.

![[19a00833.png]]

### Install

> [!warning] CAUTION · Осторожно
> Do not use compressed air to clean the ECM connectors or the engine harness connectors. Compressed air can contain moisture that can damage the components.

Place the ECM on the mounting plate and install the capscrews.

Tighten the capscrews.

Use an inch-pound torque wrench, Part Number 3376592, with 4 mm \[5/32-in\] hex head adapter to tighten the connector jackscrew.

> [!tip] Момент затяжки · Torque Value
> 2.8 n•m [25 in-lb]

> [!note] Note · Примечание
> Do **not** over-torque as connector damage can occur.

Use electrical contact cleaner, Part Number 3824510, to remove all dirt and moisture from the ECM and engine harness connectors.

Connect the ECM engine harness connectors.

Calibrate the ECM. Refer to Procedure 019-032 (ECM Calibration Code) in Section 19.

![[19a00833.png]]
