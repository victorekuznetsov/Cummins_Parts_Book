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
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/41/41-012-018.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/41-012-018.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "группа/41"
  - "перевод/машинный"
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

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Проверка

Удалите вспомогательную линию сжатого воздуха из порта разгрузчика воздуховодного управления.

> [!note] Примечание
> **Не** отсоедините линию от клапана разгрузчика воздушного компрессора. Делайте **не** отсоединяйте водохранилище линии сжатого воздуха от воздухоотводчика.

![[cp900ka.png]]

Установите трубные пробки в портах разгрузчика воздуховодов, где была удалена вспомогательная линия сжатого воздуха.

Управляйте двигателем, чтобы активировать воздушный компрессор.

Если воздушный компрессор прекращает перекачку (давление воздуха перестает повышаться) при регулируемом давлении воздуха, происходит утечка в вспомогательной или вспомогательной линии сжатого воздуха. См. инструкции OEM по устранению неполадок и инструкциям по ремонту.

![[gv900kd.png]]

Если воздушный компрессор прекращает перекачку (давление воздуха продолжает расти) при регулируемом давлении воздуха, подсоедините регулируемую линию давления подачи сжатого воздуха к порту клапана разгрузчика воздушного компрессора.

> [!note] Примечание
> Убедитесь, что сигнальная линия от воздухоуправителя до разгрузчика компрессора не протекает.

![[gv900kb.png]]

> [!note] Примечание
> Убедитесь, что измеритель давления воздуха точен, а линия подачи и фитинги находятся в хорошем состоянии, прежде чем выполнять какие-либо проверки давления воздуха.

Используйте мастер-измеритель известной точности для измерения давления воздуха.

![[cp8tosa.png]]

Применить давление воздуха 690 кПа[100 psi] к порту разгрузчика.

Если воздушный компрессор перестает перекачивать (давление воздуха перестает расти), то воздухоотводчик выходит из строя и должен быть отремонтирован или заменен. Смотрите инструкции OEM.

![[gv900kc.png]]

Если воздушный компрессор продолжает накачивать (давление воздуха продолжает повышаться), клапан разгрузчика выходит из строя и должен быть отремонтирован или заменен. Удалите воздушный компрессор для ремонта; обратитесь к процедуре 012-014.

![[gv900ke.png]]

Удалите трубную пробку из порта губернатора, используемого для вспомогательной линии сжатого воздуха.

Удалите регулируемый сжатый воздух.

Установите и затяните аксессуар линии сжатого воздуха.

Соедините линию между клапаном разгрузчика компрессора и воздухоотводом.

![[gv900kf.png]]

Управляйте двигателем и проверяйте наличие утечек воздуха.

![[oi901kn.png]]


> [!quote]- Original (English) · английский оригинал
> ### Test
>
> Remove the accessory air lines from the air governor unloader port.
>
> **Note · Примечание**
> Do **not** disconnect the line from the air compressor unloader valve. Do **not** disconnect the reservoir air line from the air governor.
>
> Install pipe plugs in the air governor unloader ports where the accessory air lines were removed.
>
> Operate the engine to activate the air compressor.
>
> If the air compressor stops pumping (air pressure stops rising) at the governed air pressure, there is a leak in an accessory or an accessory air line. Refer to the OEM's instructions for troubleshooting and repair instructions.
>
> If the air compressor does **not** stop pumping (air pressure continues to rise) at the governed air pressure, connect a regulated shop air pressure line to the air compressor unloader valve port.
>
> **Note · Примечание**
> Make sure the signal line from the air governor to the compressor unloader is **not** leaking.
>
> **Note · Примечание**
> Make sure the air pressure gauge is accurate and the supply line and fittings are in good condition before performing any air pressure checks.
>
> Use a master gauge of known accuracy to measure the air pressure gauge.
>
> Apply 690 kPa \[100 psi\] air pressure to the unloader port.
>
> If the air compressor stops pumping (air pressure stops rising), the air governor is malfunctioning and **must** be repaired or replaced. Refer to the OEM's instructions.
>
> If the air compressor continues to pump (air pressure continues to rise), the unloader valve is malfunctioning and **must** be repaired or replaced. Remove the air compressor for repair; refer to Procedure 012-014.
>
> Remove the pipe plug from the governor port used for the accessory air line.
>
> Remove the regulated shop air.
>
> Install and tighten the accessory air line.
>
> Connect the line between the compressor unloader valve and the air governor.
>
> Operate the engine and inspect for air leaks.
