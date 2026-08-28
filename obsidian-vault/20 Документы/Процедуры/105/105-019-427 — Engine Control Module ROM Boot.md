---
aliases:
  - "Загрузка ПЗУ ЭБУ (ROM boot)"
type: "Процедура"
doc: "105-019-427"
title_en: "Engine Control Module ROM Boot"
title_ru: "Загрузка ПЗУ ЭБУ (ROM boot)"
modified: "2023-08-21"
engines:
  - "37292556"
  - "37295879"
  - "41343322"
  - "41370103"
families:
  - "NT/NTA855 · ISM/QSM11"
  - "QST30"
manuals:
  - "3666266"
  - "4021674"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/105/105-019-427.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/105-019-427.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "двигатель/QST30"
  - "группа/105"
---

# Engine Control Module ROM Boot
**Загрузка ПЗУ ЭБУ (ROM boot)**

> [!abstract] Процедура · `105-019-427`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]], [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11, QST30
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]], [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section 19 - Electronic Engine Controls · Section 19 — Electronic Engine Controls — Group 19
> **Даты:** изменён 2023-08-21
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/105/105-019-427.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/105-019-427.pdf)

### Select Service Tools

#### Recommended Cummins® Service Tools

- Cummins® ECM bench calibration harness, Part Number 3163151.

- No additional service items required.

### General Information

Engine Control Module (ECM) ROM Boot Procedure:

- Install the calibration cable with ROM boot switch.
- With the keyswitch (2) in the OFF position, press the ROM boot switch (1), located on the ECM-specific calibration adapter harness, and hold.
- Switch the keyswitch to the ON position while holding the ROM boot switch down, wait for five seconds.
- Release the ROM boot switch.
- Recalibrate the ECM. [[105-019-032 — Engine Control Module Calibration Code|Refer to Procedure 019-032 in Section 19.]]
- Remove the ROM boot cable from the ECM.

For general tool information, including the correct installation configuration, see the ECM-specific calibration adapter cable with ROM boot switch in the ECM Bench Calibration Base Harness, Service Tool Instruction 3377791.

![[19r00161.png]]
