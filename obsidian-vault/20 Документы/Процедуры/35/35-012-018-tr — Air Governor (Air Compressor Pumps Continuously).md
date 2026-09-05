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
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/35/35-012-018-tr.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/35-012-018-tr.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/35"
  - "перевод/машинный"
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

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Первичная проверка

Проверьте, неиспользуемый порт разгрузчика, если применимо, на воздушном компрессоре установлена трубная пробка.

![[12a00013.png]]

> [!note] Примечание
> На изображенных иллюстрациях будет показан одноцилиндровый воздушный компрессор модели SS. При необходимости будут показаны различия в процедурах для воздушных компрессоров Holset® моделей SS, QE, ST и Cummins.

Удалите и проверьте сигнальную линию воздуховодного компрессора для изломов, порезов, галочек или подключения внутри линии.

![[cp8tbmg.png]]

Установите трубные пробки в портах разгрузчика воздуховодов, где была удалена вспомогательная линия сжатого воздуха.

Управляйте двигателем, чтобы активировать воздушный компрессор.

Если давление воздуха перестает расти, происходит утечка в аксессуаре или вспомогательной линии сжатого воздуха. См. руководство по обслуживанию OEM для устранения неполадок и ремонта.

![[cp8tbkd.png]]

Если воздушный компрессор прекращает перекачку (давление воздуха продолжает расти) при регулируемом давлении воздуха, подсоедините регулируемую линию давления подачи сжатого воздуха к одной из следующих линий:

- Порт разгрузочного клапана воздушного компрессора
- Один из портов разгрузочного клапана воздуховодного управляющего.

![[cp8tokd.png]]

Убедитесь, что измеритель давления воздуха точен, а линии подачи и фитинги находятся в хорошем состоянии, прежде чем выполнять какие-либо проверки давления воздуха.

Используйте мастер-измеритель известной точности для проверки измерителя давления воздуха.

![[cp8tosa.png]]

Применить давление воздуха 690 кПа[100 psi] к порту разгрузчика.

Если воздушный компрессор прекращает перекачку (давление воздуха перестает расти), воздухоотводчик выходит из строя и должен быть отремонтирован или заменен, или воздухоотводчик, устанавливающий прокладку, протекает. См. сервисное руководство изготовителя машины.

![[gv800kc.png]]

Если воздушный компрессор продолжает накачивать (давление воздуха продолжает повышаться), клапан разгрузчика выходит из строя и должен быть отремонтирован или заменен.[[35-012-013-tr — Air Compressor Unloader and Valve Assembly|См. процедуру 012-013 в разделе 12.]]

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
> Verify the unused unloader port, if applicable, on the air compressor has a pipe plug installed.
>
> **Note · Примечание**
> The illustrations shown will be of the SS model single cylinder air compressor. Differences in procedures for Holset® models SS, QE, ST, and Cummins air compressors will be shown where necessary.
>
> Remove and inspect the air governor signal line from the air compressor for kinks, cuts, nicks or plugging inside the line.
>
> Install pipe plugs in the air governor unloader ports where accessory air lines were removed.
>
> Operate the engine to activate the air compressor.
>
> If air pressure stops rising, there is a leak in an accessory or an accessory air line. Refer to the OEM service manual for troubleshooting and repair.
>
> If the air compressor does **not** stop pumping (air pressure continues to rise) at the governed air pressure, connect a regulated shop air pressure line to one of the following:
>
> - The air compressor unloader valve port
> - One of the air governor unloader valve ports.
>
> Make sure the air pressure gauge is accurate, and the supply lines and fittings are in good condition before performing any air pressure checks.
>
> Use a master gauge of known accuracy to check the air pressure gauge.
>
> Apply 690 kPa \[100 psi\] air pressure to the unloader port.
>
> If the air compressor stops pumping (air pressure stops rising), the air governor is malfunctioning and **must** be repaired or replaced, or the air governor mounting gasket is leaking. Refer to the OEM service manual.
>
> If the air compressor continues to pump (air pressure continues to rise), the unloader valve is malfunctioning and **must** be repaired or replaced. [[35-012-013-tr — Air Compressor Unloader and Valve Assembly|Refer to Procedure 012-013 in Section 12.]]
>
> Remove the pipe plugs from the unloader ports used for accessory air lines.
>
> Install and tighten the accessory air lines.
>
> Connect the line to the unloader valve.
>
> Operate the engine and check for air leaks.
