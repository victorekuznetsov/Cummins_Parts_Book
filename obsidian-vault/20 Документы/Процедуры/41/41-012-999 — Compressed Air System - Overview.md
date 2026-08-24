---
aliases:
  - "Система сжатого воздуха — обзор"
type: "Процедура"
doc: "41-012-999"
title_en: "Compressed Air System - Overview"
title_ru: "Система сжатого воздуха — обзор"
modified: "2003-05-13"
engines:
  - "93058669"
families:
  - "C8.3 · 6C8.3"
manuals:
  - "3666003"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/41/41-012-999.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/41-012-999.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "группа/41"
  - "перевод/машинный"
---

# Compressed Air System - Overview
**Система сжатого воздуха — обзор**

> [!abstract] Процедура · `41-012-999`
> **Двигатели:** [[93058669 — 6C8.3 CPL 3105|93058669]]
> **Семейство:** C8.3 · 6C8.3
> **Входит в руководства:** [[3666003 — C Troubleshooting and Repair Manual|3666003]]
> **Секции:** Section F - Familiarization
> **Даты:** изменён 2003-05-13
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/41/41-012-999.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/41-012-999.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Система сжатого воздуха обычно состоит из шестерённого воздушного компрессора, воздухоуправителя, воздушных баков и всей необходимой сантехники.

![[ca901gc.png]]

Холсет QE296 одноцилиндровый воздушный компрессор является двигателем, поршневого типа компрессор, который поставляет сжатый воздух для работы воздухоактивированных устройств. Компрессор работает непрерывно, но имеет загруженные и разгруженные режимы работы. Режим работы контролируется регулятором, работающим под давлением, и компрессорным разгрузочным агрегатом.

Воздушный компрессор QE296, используемый на двигателях серии C, использует разгрузчик (E-type). Экономичная (E-type) разгрузочная система была разработана для уменьшения потерь насоса и снижения давления двигателя через впускной клапан компрессора при работе в режиме разгрузки.

Когда воздушная система достигает заданного давления, регулятор наносит воздушный сигнал на сборку разгрузчика воздушного компрессора, в результате чего разгрузочный колпачок закрывает входящий воздух на впускном клапане, и сжатый воздух перестает поступать в воздушную систему.

> [!note] Примечание
> Давление системы ** должно** поддерживаться на выпускной стороне разгрузочного клапана для обеспечения его закрытости.

Когда воздух в системе используется, давление падает. При заданном давлении регулятор выдыхает воздушный сигнал на компрессорный разгрузочный агрегат, позволяя компрессору снова накачивать сжатый воздух в воздушную систему.

> [!warning] ОСТОРОЖНО
> Транспортные средства, оснащенные воздушными сушилками, вентилируемыми в атмосферу во время работы разгруженного компрессора, с использованием воздушного компрессора Holset® (E-type), требуют установки клапана Econ для предотвращения чрезмерного потребления масла.

Если давление в системе воздуха ** не** поддерживается на разрядном клапане во время разгрузочной работы, воздух будет выкачиваться из цилиндра компрессора, вызывая низкое давление (вакуумное) состояние, которое образуется в цилиндре. Поскольку впускной клапан запечатан разгрузочным колпачком, а выпускной клапан представляет собой односторонний клапан с приводом давления, в цилиндр не будет допускаться попадание воздуха. Когда давление цилиндра воздушного компрессора падает ниже давления картерного ящика, масло будет протягиваться мимо поршневых колец и закачиваться в воздушную систему.

Другие марки воздушных компрессоров могут использоваться на двигателях серии C. Процедуры устранения неполадок очень похожи для этих воздушных компрессоров по сравнению с Holset QE296. См. руководство производителя воздушного компрессора для получения подробной информации о ремонте и спецификациях крутящего момента.

Тяжеловесные (HD) воздушные компрессоры Holset® были разработаны для двигателя серии C. Приложения включают промышленные рынки, такие как транзитные автобусы, мусоровозы, внедорожные строительные транспортные средства и другие.

Модели воздушных компрессоров большой мощности Holset® представляют собой непрерывную версию модели QE, уже выпущенную для двигателей серии C. Корпус и головка воздушного компрессора одинаковы; однако, модель Holset® с большой грузоподъемностью ** не имеет встроенного разгрузчика. Разгрузка контролируется в воздушной сушилке через внутренний или внешний воздухоотводчик. Для установок ** без** воздушных сушилок требуется разгрузчик линии разгрузки.

Преимущество этого воздушного компрессора заключается в том, что водопроводная труба упрощена из-за устранения разгрузочного клапана. Стандартные клапаны были заменены на клапаны Reed, чтобы позволить воздушному компрессору работать непрерывно без проблем с выносливостью клапана.

Во время незагруженных операций воздух, выделяемый компрессором, непрерывно поступает в атмосферу через порт очистки воздухоочистителя.

Тяжеловесные воздушные компрессоры Holset® могут ** не** использовать воздух с турбонаддувом и ** должны ** естественным образом вздуваться, чтобы предотвратить потерю мощности двигателя. Впускной воздух для воздушного компрессора ** должен** поступать непосредственно из воздухоочистителя двигателя, как можно ближе к воздухоочистителю.

Модели воздушных компрессоров большой мощности Holset® будут обозначены как HD650 (производное QE296) и HD850 (производное QE338). Модели с большой грузоподъемностью Holset® будут использовать ту же самую водопроводную систему охлаждающей жидкости, что и соответствующая модель QE.

В следующей таблице показано, какой воздушный компрессор модели Holset® большой мощности и номер детали, который заменит текущий воздушный компрессор модели QE:

| Модель HD | Часть нет. | Новый вариант No. | Заменить модель QE |
|---|---|---|---|
| HD650B | 3558127 | CP9202 | 3558049 |
| HD650B | 3558128 | CP9203 | 3558097 |
| HD850B | 3558120 | CP9204 | 3558050 |
| HD850 | 3558121 | CP9209 | 3558098 |
| HD650C | 3558129 | CP9205 и CP9206 | 3558052 |
| HD850C | 3558122 | CP9207 и CP9208 | 3558051 |

> [!note] Примечание
> Модель воздушного компрессора QE ** не устаревает. Модель Holset® будет доступна там, где QE не способен обеспечить достаточное качество воздуха для конкретных применений.


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> The compressed air system normally consists of a gear-driven air compressor, an air governor, air tanks, and all necessary plumbing.
>
> The Holset® QE296 single-cylinder air compressor is an engine-driven, piston-type compressor that supplies compressed air to operate air-activated devices. The compressor runs continuously but has loaded and unloaded operating modes. The operating mode is controlled by a pressure-activated governor and the compressor unloading assembly.
>
> The QE296 air compressor used on C Series engines uses an (E-type) unloader. The economy (E-type) unloader system was designed to reduce pumping losses and engine boost pressure losses through the compressor intake valve while operating in unloading mode.
>
> When the air system reaches a predetermined pressure, the governor applies an air signal to the air compressor unloader assembly, causing the unloader cap to seal off incoming air at the intake valve, and compressed air stops flowing into the air system.
>
> **Note · Примечание**
> System pressure **must** be maintained on the outlet side of the discharge valve to keep the discharge valve closed.
>
> As the air in the air system is used, the pressure drops. At a predetermined pressure, the governor exhausts the air signal to the compressor unloader assembly, allowing the compressor to again pump compressed air into the air system.
>
> **CAUTION · Осторожно**
> Vehicles equipped with air dryers vented to atmosphere during unloaded compressor operation, using the Holset® (E-type) air compressor, require the installation of an Econ valve to prevent excessive oil consumption.
>
> If the air system pressure is **not** maintained on the discharge valve during unloaded operation, air will be pumped out of the compressor cylinder causing a low pressure (vacuum) condition to form in the cylinder. With the intake valve sealed off by the unloader cap and the exhaust valve being a one-way pressure actuated valve, no air will be allowed to enter the cylinder. When the air compressor cylinder pressure falls below crankcase pressure, oil will be drawn past the piston rings and pumped into the air system.
>
> Other brands of air compressors can be used on C Series engines. Troubleshooting procedures are very similar for these air compressors compared to the Holset® QE296. Refer to the specific air compressor manufacturer's manual for detailed repair information and torque specifications.
>
> The Holset® heavy-duty (HD) air compressors was designed for the C Series engine. Applications include industrial markets, such as transit buses, refuse trucks, on-off highway construction vehicles, and other.
>
> The Holset® heavy-duty model air compressor is a continuous pump version of the QE model already released for the C Series engines. The air compressor crank housing and head are the same; however, the Holset® heavy-duty model does **not** have an integral unloader. Unloading is controlled at the air dryer by way of an internal or external air governor. A discharge line unloader is required for installations **without** air dryers.
>
> The advantage of this air compressor is that the downstream plumbing is simplified because of the elimination of the unloader valve. Standard valves have been replaced with Reed valves to enable the air compressor to run continuously without valve endurance issues.
>
> During unloaded operations, the air compressor's discharge air is continuously vented to the atmosphere through the air dryer's purge port.
>
> The Holset® heavy-duty air compressors can **not** use turbocharged air and **must** be naturally aspirated to prevent loss of engine power. Inlet air for the air compressor **must** be sourced directly from the engine air cleaner, as close to the air cleaner as possible.
>
> The Holset® heavy-duty model air compressors will be designated as the HD650 (QE296 derivative), and HD850 (QE338 derivative). The Holset® heavy-duty models will use the same coolant plumbing as the corresponding QE model.
>
> The following table shows what Holset® heavy-duty model air compressor and part number that will replace the current QE model air compressor:
>
> | HD Model | Part No. | New Option No. | Replaces QE Model |
> |---|---|---|---|
> | HD650B | 3558127 | CP9202 | 3558049 |
> | HD650B | 3558128 | CP9203 | 3558097 |
> | HD850B | 3558120 | CP9204 | 3558050 |
> | HD850 | 3558121 | CP9209 | 3558098 |
> | HD650C | 3558129 | CP9205 and CP9206 | 3558052 |
> | HD850C | 3558122 | CP9207 and CP9208 | 3558051 |
>
> **Note · Примечание**
> The QE model air compressor is **not** becoming obsolete. The Holset® heavy-duty model will be available where the QE is **not** capable of supplying sufficient air quality on specific applications.
