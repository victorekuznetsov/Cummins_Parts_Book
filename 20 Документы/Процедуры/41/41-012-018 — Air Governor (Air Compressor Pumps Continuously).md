---
aliases:
  - "Регулятор давления воздуха (компрессор нагнетает непрерывно)"
type: "Процедура"
doc: "41-012-018"
title_en: "Air Governor (Air Compressor Pumps Continuously)"
title_ru: "Регулятор давления воздуха (компрессор нагнетает непрерывно)"
modified: "2004-12-07"
engines:
  - "93058669"
families:
  - "C8.3 · 6C8.3"
manuals:
  - "3666003"
figures: 8
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/41/41-012-018.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/41-012-018.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "группа/41"
---

# Air Governor (Air Compressor Pumps Continuously)
**Регулятор давления воздуха (компрессор нагнетает непрерывно)**

> [!abstract] Процедура · `41-012-018`
> **Двигатели:** [[93058669 — 6C8.3 CPL 3105|93058669]]
> **Семейство:** C8.3 · 6C8.3
> **Входит в руководства:** [[3666003 — C Troubleshooting and Repair Manual|3666003]]
> **Секции:** Section 12 - Compressed Air System - Group 12
> **Даты:** изменён 2004-12-07
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/41/41-012-018.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/41-012-018.pdf)

### Test

Remove the accessory air lines from the air governor unloader port.

> [!note] Note · Примечание
> Do **not** disconnect the line from the air compressor unloader valve. Do **not** disconnect the reservoir air line from the air governor.

![[cp900ka.png]]

Install pipe plugs in the air governor unloader ports where the accessory air lines were removed.

Operate the engine to activate the air compressor.

If the air compressor stops pumping (air pressure stops rising) at the governed air pressure, there is a leak in an accessory or an accessory air line. Refer to the OEM's instructions for troubleshooting and repair instructions.

![[gv900kd.png]]

If the air compressor does **not** stop pumping (air pressure continues to rise) at the governed air pressure, connect a regulated shop air pressure line to the air compressor unloader valve port.

> [!note] Note · Примечание
> Make sure the signal line from the air governor to the compressor unloader is **not** leaking.

![[gv900kb.png]]

> [!note] Note · Примечание
> Make sure the air pressure gauge is accurate and the supply line and fittings are in good condition before performing any air pressure checks.

Use a master gauge of known accuracy to measure the air pressure gauge.

![[cp8tosa.png]]

Apply 690 kPa \[100 psi\] air pressure to the unloader port.

If the air compressor stops pumping (air pressure stops rising), the air governor is malfunctioning and **must** be repaired or replaced. Refer to the OEM's instructions.

![[gv900kc.png]]

If the air compressor continues to pump (air pressure continues to rise), the unloader valve is malfunctioning and **must** be repaired or replaced. Remove the air compressor for repair; refer to Procedure 012-014.

![[gv900ke.png]]

Remove the pipe plug from the governor port used for the accessory air line.

Remove the regulated shop air.

Install and tighten the accessory air line.

Connect the line between the compressor unloader valve and the air governor.

![[gv900kf.png]]

Operate the engine and inspect for air leaks.

![[oi901kn.png]]
