---
aliases:
  - "Регулятор давления воздуха (компрессор нагнетает непрерывно)"
type: "Процедура"
doc: "20-012-018"
title_en: "Air Governor (Air Compressor Pumps Continuously)"
title_ru: "Регулятор давления воздуха (компрессор нагнетает непрерывно)"
modified: "2006-06-30"
engines:
  - "41349633"
families:
  - "QSK19"
manuals:
  - "4021592"
figures: 8
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/20/20-012-018.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/20-012-018.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/20"
  - "перевод/машинный"
---

# Air Governor (Air Compressor Pumps Continuously)
**Регулятор давления воздуха (компрессор нагнетает непрерывно)**

> [!abstract] Процедура · `20-012-018`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021592 — QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual|4021592]]
> **Секции:** Section 12 - Compressed Air System - Group 12
> **Даты:** изменён 2006-06-30
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/20/20-012-018.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/20-012-018.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Первичная проверка

> [!note] Примечание
> На изображенных иллюстрациях будет показан одноцилиндровый воздушный компрессор модели SS. При необходимости будут показаны различия в процедурах для воздушных компрессоров Holset® моделей SS, QE, ST и Cummins®.

Удалите воздушную присадку линии сжатого воздуха от воздухокомпрессорного регулятора.

![[cp8tbmg.png]]

Установите трубные пробки в портах разгрузчика воздуховодов, где была удалена вспомогательная линия сжатого воздуха.

Управляйте двигателем, чтобы активировать воздушный компрессор.

Если воздушный компрессор прекращает перекачку (давление воздуха перестает повышаться) при регулируемом давлении воздуха, происходит утечка в вспомогательной или вспомогательной линии сжатого воздуха. См. руководство изготовителя машины по диагностике и ремонту.

![[cp8tbkd.png]]

> [!danger] ОПАСНО
> При работе со сжатым воздухом применяйте защиту глаз и лица. Разлетающиеся частицы и грязь могут привести к травме.

Если воздушный компрессор прекращает перекачку (давление воздуха продолжает расти) при регулируемом давлении воздуха, подсоедините регулируемую линию давления подачи сжатого воздуха к одной из следующих линий:

Порт разгрузочного клапана воздушного компрессора

Один из портов разгрузочного клапана воздуховодного управляющего.

![[cp8tokd.png]]

Убедитесь, что измеритель давления воздуха точен, а линии подачи и фитинги находятся в хорошем состоянии, прежде чем выполнять какие-либо проверки давления воздуха.

Используйте мастер-измеритель известной точности для проверки измерителя давления воздуха.

![[cp8tosa.png]]

Применить давление воздуха 690 кПа[100 psi] к порту разгрузчика.

Если воздушный компрессор прекращает перекачку (давление воздуха перестает расти), воздухоотводчик выходит из строя и ** должен быть отремонтирован или заменен, или воздухоотводчик, устанавливающий прокладку, протекает. См. руководство изготовителя машины по диагностике и ремонту.

![[gv800kc.png]]

Если воздушный компрессор продолжает накачивать (давление воздуха продолжает повышаться), клапан разгрузчика выходит из строя и должен быть отремонтирован или заменен. См. процедуру[[20-012-013 — Air Compressor Unloader and Valve Assembly|012-013]].

![[cp8vakb.png]]

Удалите трубные пробки из портов разгрузчика, используемых для вспомогательной линии сжатого воздуха.

Установите и затяните аксессуар линии сжатого воздуха.

Подключите линию к разгрузочному клапану.

![[gv8ppmb.png]]

Управляйте двигателем и проверяйте наличие утечек воздуха.

![[ca800db.png]]


> [!quote]- Original (English) · английский оригинал
> ### Initial Check
>
> **Note · Примечание**
> The illustrations shown will be of the SS model single cylinder air compressor. Differences in procedures for Holset® models SS, QE, ST, and Cummins® air compressors will be shown where necessary.
>
> Remove the air accessory air lines from the air compressor governor.
>
> Install pipe plugs in the air governor unloader ports where accessory air lines were removed.
>
> Operate the engine to activate the air compressor.
>
> If the air compressor stops pumping (air pressure stops rising) at the governed air pressure, there is a leak in an accessory or an accessory air line. Refer to the OEM troubleshooting and repair manual.
>
> **WARNING · Опасно**
> Wear appropriate eye and face protection when using compressed air. Flying debris and dirt can cause personal injury.
>
> If the air compressor does **not** stop pumping (air pressure continues to rise) at the governed air pressure, connect a regulated shop air pressure line to one of the following:
>
> The air compressor unloader valve port
>
> One of the air governor unloader valve ports.
>
> Be sure the air pressure gauge is accurate, and the supply lines and fittings are in good condition before performing any air pressure checks.
>
> Use a master gauge of known accuracy to check the air pressure gauge.
>
> Apply 690 kPa \[100 psi\] air pressure to the unloader port.
>
> If the air compressor stops pumping (air pressure stops rising), the air governor is malfunctioning and **must** be repaired or replaced, or the air governor mounting gasket is leaking. Refer to the OEM troubleshooting and repair manual.
>
> If the air compressor continues to pump (air pressure continues to rise), the unloader valve is malfunctioning and **must** be repaired or replaced. Refer to Procedure [[20-012-013 — Air Compressor Unloader and Valve Assembly|012-013]].
>
> Remove the pipe plugs from the unloader ports used for accessory air lines.
>
> Install and tighten the accessory air lines.
>
> Connect the line to the unloader valve.
>
> Operate the engine and check for air leaks.
