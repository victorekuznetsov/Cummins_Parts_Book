---
aliases:
  - "Загрузка ПЗУ ЭБУ (ROM boot)"
type: "Процедура"
doc: "122-019-427"
title_en: "Engine Control Module ROM Boot"
title_ru: "Загрузка ПЗУ ЭБУ (ROM boot)"
modified: "2019-12-11"
engines:
  - "33239746"
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
manuals:
  - "4022102"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-019-427.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/122-019-427.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/122"
---

# Engine Control Module ROM Boot
**Загрузка ПЗУ ЭБУ (ROM boot)**

> [!abstract] Процедура · `122-019-427`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Входит в руководства:** [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M|4022102]]
> **Секции:** Section 19 - Electronic Controls
> **Даты:** изменён 2019-12-11
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-019-427.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/122-019-427.pdf)

### General Information

> [!note] Note · Примечание
> When performing the ROM boot procedure on engines with multiple electronic control modules, a Multiple Module Harness Kit must be used. For additional information, see the Installation of Multiple Module Harness section below or service tool, Part Number 3163151.

Each switch sends power to the correct pair of engine control module (ECM) contacts, so INSITE™ electronic service tool can read the switch locations.

Install the Multiple Module Harness Kit on the appropriate calibration cable with ROM boot switch. Connect the calibration cable with ROM boot switch to the ECM desired to be ROM booted. Select ECM to ROM boot, use the 3 position switch on the multiple module box.

- When switched to “PRIM” mode, the primary ECM is read, as well as any single ECM.
- When switched to “SEC1” mode, the first secondary ECM is read.
- When switched to “SEC2” mode, will enable the second secondary ECM is read.

The bench calibration harness works with the appropriate ROM boot cable to enable ROM booting and the calibration of engines with multiple ECMs.

Install the calibration cable with ROM boot switch.

With the keyswitch (2) in the OFF position, press the ROM boot switch (1), located on the ECM specific calibration adapter harness, and hold.

Switch the keyswitch to the ON position while holding the ROM boot switch down; wait for 5 seconds.

Release the ROM boot switch.

Calibrate the ECM. [[105-019-032 — Engine Control Module Calibration Code|Refer to Procedure 019-032 in Section 19.]]

Remove the ROM boot cable from the ECM.

![[22d00162.png]]
