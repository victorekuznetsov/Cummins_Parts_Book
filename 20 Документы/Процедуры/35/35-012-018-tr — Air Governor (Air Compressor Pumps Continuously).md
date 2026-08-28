---
aliases:
  - "Регулятор давления воздуха (компрессор нагнетает непрерывно)"
type: "Процедура"
doc: "35-012-018-tr"
title_en: "Air Governor (Air Compressor Pumps Continuously)"
title_ru: "Регулятор давления воздуха (компрессор нагнетает непрерывно)"
modified: "2013-03-01"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "3666322"
figures: 9
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/35/35-012-018-tr.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/35-012-018-tr.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/35"
---

# Air Governor (Air Compressor Pumps Continuously)
**Регулятор давления воздуха (компрессор нагнетает непрерывно)**

> [!abstract] Процедура · `35-012-018-tr`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[3666322 — ISM, ISMe, and QSM11 Service Manual|3666322]]
> **Секции:** Section 12 - Compressed Air System - Group 12
> **Даты:** изменён 2013-03-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/35/35-012-018-tr.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/35-012-018-tr.pdf)

### Initial Check

Verify the unused unloader port, if applicable, on the air compressor has a pipe plug installed.

![[12a00013.png]]

> [!note] Note · Примечание
> The illustrations shown will be of the SS model single cylinder air compressor. Differences in procedures for Holset® models SS, QE, ST, and Cummins air compressors will be shown where necessary.

Remove and inspect the air governor signal line from the air compressor for kinks, cuts, nicks or plugging inside the line.

![[cp8tbmg.png]]

Install pipe plugs in the air governor unloader ports where accessory air lines were removed.

Operate the engine to activate the air compressor.

If air pressure stops rising, there is a leak in an accessory or an accessory air line. Refer to the OEM service manual for troubleshooting and repair.

![[cp8tbkd.png]]

If the air compressor does **not** stop pumping (air pressure continues to rise) at the governed air pressure, connect a regulated shop air pressure line to one of the following:

- The air compressor unloader valve port
- One of the air governor unloader valve ports.

![[cp8tokd.png]]

Make sure the air pressure gauge is accurate, and the supply lines and fittings are in good condition before performing any air pressure checks.

Use a master gauge of known accuracy to check the air pressure gauge.

![[cp8tosa.png]]

Apply 690 kPa \[100 psi\] air pressure to the unloader port.

If the air compressor stops pumping (air pressure stops rising), the air governor is malfunctioning and **must** be repaired or replaced, or the air governor mounting gasket is leaking. Refer to the OEM service manual.

![[gv800kc.png]]

If the air compressor continues to pump (air pressure continues to rise), the unloader valve is malfunctioning and **must** be repaired or replaced. [[35-012-013-tr — Air Compressor Unloader and Valve Assembly|Refer to Procedure 012-013 in Section 12.]]

![[cp8vakb.png]]

Remove the pipe plugs from the unloader ports used for accessory air lines.

Install and tighten the accessory air lines.

Connect the line to the unloader valve.

![[gv8ppmb.png]]

Operate the engine and check for air leaks.

![[ca800db.png]]
