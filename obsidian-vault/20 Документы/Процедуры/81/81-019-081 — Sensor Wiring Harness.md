---
type: "Процедура"
doc: "81-019-081"
title_en: "Sensor Wiring Harness"
modified: "2007-10-30"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
families:
  - "QSK60"
manuals:
  - "3666410"
figures: 51
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/81/81-019-081.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/81-019-081.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK60"
  - "группа/81"
  - "перевод/машинный"
---

# Sensor Wiring Harness

> [!abstract] Процедура · `81-019-081`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]]
> **Семейство:** QSK60
> **Входит в руководства:** [[3666410 — QSK45 and QSK60 CENSE™ Electronic Control System Troubleshooting and Repair Manual|3666410]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2007-10-30
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/81/81-019-081.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/81-019-081.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Двигатели, оснащенные CENSETM, используют три отдельных жгута проводов:

- CENSETM проводка, основные / левобережные датчики

![[19802602.png]]

- CENSETM проводная упряжка, датчики правого берега

![[19802606.png]]

- J1939 Коммуникационная проводка жгут (backbone Wiring Grund).

![[19802603.png]]

### Снятие

Левый берег

Снимите крышки левого берега.

![[19601202.png]]

Отсоедините проводку главного/левого банка CENSETM от датчика температуры масла (1).

![[19801294.png]]

Отключите 23-контактный разъем OEM-проводов.

![[19800837.png]]

Отключите 40-контактные разъемы A и B ECM.

![[19800828.png]]

Отсоедините 23-контактные и 33-контактные датчики с правой стороны проводов разъёмов ремня.

![[19800847.png]]

Отключите все датчики температуры выхлопных газов левого берега.

![[19801442.png]]

Отсоедините левый задний датчик температуры входного впуска турбокомпрессора.

![[19800845.png]]

Отключите 2-контактный левобережный задний датчик температуры коллектора.

![[19400436.png]]

Отсоедините блок двигателя от блока двигателя. Для отключения может быть один или несколько кольцевых терминалов.

> [!note] Примечание
> Некоторые проводные упряжки имеют одну общую почву.

![[19400393.png]]

Отсоедините 2-хсторонний межрежимный разъем QSK45/60 (CAN data bus) от электропроводки системы управления двигателем.

- Удалите болты.
- Вытащите разъем шины данных CAN из крепежного слота в скобке.

> [!note] Примечание
> Скобка может отличаться от иллюстрации.

![[19801069.png]]

Отсоедините 3-контактный разъем шины данных RS232 от опорной скобки.

![[19801208.png]]

Отсоедините разъем предупредительных ламп от разъема лампы QSK45/60.

![[19a00484.png]]

Отсоедините 3-контактную шину данных Deutsch J1939 CAN от ремня проводов связи (backbone).

![[19802604.png]]

Отсоедините 6-контактные разъемы DeutschTM от 6-сторонних межконтактных разъемов QSK45/60.

![[19801070.png]]

Удалите главный/левый берег проводов упряжкой (1) и магистральной проводов упряжкой (2) из опорной скобки.

Отрежьте все нейлоновые проводные связи от основной / левобережной проводной упряжки CENSETM.

Удалите проводные ремни из опорных скобок.

![[19601203.png]]

Снимите скобки поддержки проводов.

![[19601204.png]]

Правый Банк

Удалите правый чехол для проводов.

![[19601205.png]]

Отсоедините 23-контактные и 33-контактные разъемы DeutschTM на правой стороне проводов датчика.

![[19800838.png]]

Отключите датчик давления моторного масла предварительного фильтра и датчик давления моторного масла после фильтра.

> [!note] Примечание
> Этот шаг применяется только к двигателям с датчиками давления моторного масла на правом берегу.

![[19800840.png]]

Отключите все правильные датчики температуры выхлопных газов.

![[19801442.png]]

Отсоедините правый передний и задний впускной коллектор датчика температуры 2-контактных разъемов.

![[19400436.png]]

Отключите датчик давления на правом берегу 3-контактного разъема.

Датчик давления на подъёмник правого берега расположен в заднем впускном коллекторе правого берега.

![[19400452.png]]

Удалите проводку жгутов t-штуков и p-клипов из опорных скобок.

Отрежьте все нейлоновые проводные связи от правой кольцевой проводов CENSETM.

![[19601206.png]]

Удалите правую берег проводку с помощью опорных скобок.

![[19601207.png]]

### Установка

Левый берег

Прикрепите проводные скобки для поддержки к впускным коллекторам в показанных местах.

Применять Loctite® 243 или эквивалент к болтам.

Вставьте и затяните болты.

> [!tip] Момент затяжки
> 23 Н·м [204 фунт-дюйм]

![[19601204.png]]

Прикрепить главный/левый берег проводов ремня (1) и магистральной проводов ремня (2) к опорной скобке. Вставьте крепежные гайки и затяните.

> [!tip] Момент затяжки
> 10 Н·м [89 фунт-дюйм]

Используйте нейлоновые проводные стяжки, где это необходимо, чтобы обеспечить проводку ремня к двигателю.

![[19601203.png]]

> [!warning] ОСТОРОЖНО
> Используйте только рекомендованную Cummins® смазку DS-ES, номер детали 3822934. Другие смазочные материалы, такие как моторное масло или смазка, в разъемах могут вызвать повреждение ECM, плохую производительность двигателя или преждевременный износ разъема.

Нанесите небольшое количество смазки на соединительные терминалы. Перед установкой заполните всю полость разъема смазкой.

Смазать все проводов жгут разъемы.

![[cel28.png]]

Установите 23-контактные и 33-контактные датчики правого берега, проводящие разъёмы жгута на монтажную пластину.

> [!tip] Момент затяжки
> 20 Н·м [177 фунт-дюйм]

Подключите 23-контактные и 33-контактные разъемы.

![[19800847.png]]

Подключите 40-контактные разъемы A и B ECM.

![[19800828.png]]

Подключите 2-контактный левобережный задний датчик температуры коллектора.

![[19400436.png]]

Подключите все датчики температуры выхлопных газов левого берега.

[[81-019-013 — Exhaust Temperature Sensor|См. процедуру 019-013 (Датчик температуры выхлопа) в разделе 19.]]

![[19801442.png]]

Установите 3-контактный разъем шины данных RS232 в опорную кронштейн.

![[19801208.png]]

Подключите левобережный задний датчик температуры сжатия турбокомпрессора.

![[19800845.png]]

Подключите 23-контактный OEM-разъем для проводов.

![[19800837.png]]

Подключите 6-контактные разъемы DeutschTM к 6-контактным межконтактным разъемам QSK45/60.

![[19801073.png]]

Подключите 3-контактную шину данных Deutsch J1939 CAN к ремню проводов связи (backbone).

![[19802604.png]]

Подключите к разъему лампы предупреждения разъем лампы QSK45/60.

![[19a00484.png]]

Подключите 2-хсторонний межповоротный разъем QSK45/60 (шина данных CAN).

- Сдвиньте разъем в опорную кронштейн.
- Закрепите разъём с помощью винтов.

> [!tip] Момент затяжки
> 1.2 Н·м [11 фунт-дюйм]

> [!note] Примечание
> Скобка может отличаться от иллюстрации.

![[19802605.png]]

Подключите датчик температуры масла (1).

![[19801294.png]]

Прикрепите левобережную проводку к крышкам.

> [!tip] Момент затяжки
> 45 Н·м [33 фунт-фут]

![[19601202.png]]

Правый Банк

Прикрепите проводные скобки для поддержки к впускным коллекторам в показанных местах.

Применять Loctite® 243 или эквивалент к болтам.

Вставьте и затяните болты.

> [!tip] Момент затяжки
> 23 Н·м [204 фунт-дюйм]

![[19601207.png]]

Прикрепите проводку упряжки t-штукатур и p-клипы к опорным скобкам.

> [!tip] Момент затяжки
> 10 Н·м [89 фунт-дюйм]

Вставьте крепежные гайки и затяните.

Используйте нейлоновые проводные стяжки, где это необходимо, чтобы обеспечить проводку ремня к двигателю.

![[19601206.png]]

Подключите датчик давления моторного масла предварительного фильтра и датчик давления моторного масла после фильтра.

![[19800840.png]]

Подключите 23-контактные и 33-контактные разъемы DeutschTM на правой стороне проводов датчика.

![[19800838.png]]

Подключите датчик давления 3-контактного разъема правого берега, расположенный в заднем впускном коллекторе правого берега.

![[19400452.png]]

Подключите правый передний берег и правый задний впускной коллектор датчика температуры 2-контактных разъемов.

![[19400436.png]]

Подключите датчики температуры выхлопных газов правого берега.

[[81-019-013 — Exhaust Temperature Sensor|См. процедуру 019-013 (Датчик температуры выхлопа) в разделе 19.]]

![[19801442.png]]

Прикрепите правый берег проводов обложки.

> [!tip] Момент затяжки
> 45 Н·м [33 фунт-фут]

![[19601205.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> CENSE™-equipped engines use three separate wiring harnesses:
>
> - CENSE™ harness, main/left bank sensors
>
> - CENSE™ harness, right bank sensors
>
> - J1939 communication harness (backbone harness).
>
> ### Remove
>
> Left Bank
>
> Remove the left bank harness covers.
>
> Disconnect the main/left bank CENSE™ harness from the oil temperature sensor (1).
>
> Disconnect the 23-pin OEM harness connector.
>
> Disconnect the 40-pin A and B ECM connectors.
>
> Disconnect the 23-pin and the 33-pin right bank sensor harness connectors.
>
> Disconnect all of the left bank exhaust temperature sensors.
>
> Disconnect the left bank rear turbocharger compressor inlet temperature sensor.
>
> Disconnect the 2-pin left bank rear intake manifold temperature sensor.
>
> Disconnect the engine block ground from the engine block. There may be one or more ring terminals to disconnect.
>
> **Note · Примечание**
> Some harnesses have one common ground.
>
> Disconnect the QSK45/60 2-way interharness connector (data link) from the engine control system harness.
>
> - Remove the capscrews.
> - Slide the data link connector out of the mounting slot in the bracket.
>
> **Note · Примечание**
> The bracket may differ from the illustration.
>
> Disconnect the RS232 3-pin data link connector from the support bracket.
>
> Disconnect the warning lamps connector from the QSK45/60 lamp connector.
>
> Disconnect the 3-pin Deutsch™ J1939 data link from the communication harness (backbone).
>
> Disconnect the 6-pin Deutsch™ connectors from the QSK45/60 6-way interharness connectors.
>
> Remove the main/left bank harness (1) and backbone harness (2) from the support bracket.
>
> Cut all of the nylon wire ties from the CENSE™ main/left bank harness.
>
> Remove the harnesses from the support brackets.
>
> Remove the harness support brackets.
>
> Right Bank
>
> Remove the right bank harness covers.
>
> Disconnect the 23-pin and the 33-pin Deutsch™ connectors on the right bank sensor harness.
>
> Disconnect the pre-filter lubricating oil pressure sensor and the post-filter lubricating oil pressure sensor.
>
> **Note · Примечание**
> This step **only** applies for engines with pre-filter and post-filter lubricating oil pressure sensors on the right bank.
>
> Disconnect all of the right bank exhaust temperature sensors.
>
> Disconnect the right bank front and right bank rear intake manifold temperature sensor 2-pin connectors.
>
> Disconnect the right bank boost pressure sensor 3-pin connector.
>
> The right bank boost pressure sensor is located in the right bank rear intake manifold.
>
> Remove the harness t-pieces and p-clips from the support brackets.
>
> Cut all of the nylon wire ties from the CENSE™ right bank harness.
>
> Remove the right bank harness support brackets.
>
> ### Install
>
> Left Bank
>
> Attach the harness support brackets to the intake manifolds in the locations shown.
>
> Apply Loctite® 243, or equivalent, to the capscrews.
>
> Insert and tighten the capscrews.
>
> **Момент затяжки · Torque Value**
> 23 n•m [204 in-lb]
>
> Attach the main/left bank harness (1) and backbone harness (2) to the support bracket. Insert the mounting nuts and tighten.
>
> **Момент затяжки · Torque Value**
> 10 n•m [89 in-lb]
>
> Use nylon wire ties, where required, to secure the harness to the engine.
>
> **CAUTION · Осторожно**
> Use only Cummins®-recommended lubricant DS-ES, Part Number 3822934. Other lubricants, such as lubricating oil or grease, in the connectors can cause ECM damage, poor engine performance, or premature connector wear.
>
> Apply a small amount of lubricant to the connector terminals. Before installing, fill the entire connector cavity with lubricant.
>
> Lubricate all harness connectors.
>
> Install the 23-pin and the 33-pin right bank sensor harness connectors on the mounting plate.
>
> **Момент затяжки · Torque Value**
> 20 n•m [177 in-lb]
>
> Connect the 23-pin and the 33-pin connectors.
>
> Connect the 40-pin A and B ECM connectors.
>
> Connect the 2-pin left bank rear intake manifold temperature sensor.
>
> Connect all of the left bank exhaust temperature sensors.
>
> [[81-019-013 — Exhaust Temperature Sensor|Refer to Procedure 019-013 (Exhaust Temperature Sensor) in Section 19.]]
>
> Install the RS232 3-pin data link connector into the support bracket.
>
> Connect the left bank rear turbocharger compression inlet temperature sensor.
>
> Connect the 23-pin OEM harness connector.
>
> Connect the 6-pin Deutsch™ connectors to the QSK45/60 6-way interharness connectors.
>
> Connect the 3-pin Deutsch™ J1939 data link to the communication harness (backbone).
>
> Connect the warning lamp connector to the QSK45/60 lamp connector.
>
> Connect the QSK45/60 2-way interharnsss connector (data link).
>
> - Slide the connector into the support bracket.
> - Secure the connector with screws.
>
> **Момент затяжки · Torque Value**
> 1.2 n•m [11 in-lb]
>
> **Note · Примечание**
> The bracket may differ from the illustration.
>
> Connect the oil temperature sensor (1).
>
> Attach the left bank harness covers.
>
> **Момент затяжки · Torque Value**
> 45 n•m [33 ft-lb]
>
> Right Bank
>
> Attach the harness support brackets to the intake manifolds in the locations shown.
>
> Apply Loctite® 243, or equivalent, to the capscrews.
>
> Insert and tighten the capscrews.
>
> **Момент затяжки · Torque Value**
> 23 n•m [204 in-lb]
>
> Attach the harness t-pieces and p-clips to the support brackets.
>
> **Момент затяжки · Torque Value**
> 10 n•m [89 in-lb]
>
> Insert the mounting nuts and tighten.
>
> Use nylon wire ties, where required, to secure the harness to the engine.
>
> Connect the pre-filter lubricating oil pressure sensor and the post-filter lubricating oil pressure sensor.
>
> Connect the 23-pin and the 33-pin Deutsch™ connectors on the right bank sensor harness.
>
> Connect the right bank boost pressure sensor 3-pin connector, located in the right bank rear intake manifold.
>
> Connect the right bank front and the right bank rear intake manifold temperature sensor 2-pin connectors.
>
> Connect the right bank exhaust temperature sensors.
>
> [[81-019-013 — Exhaust Temperature Sensor|Refer to Procedure 019-013 (Exhaust Temperature Sensor) in Section 19.]]
>
> Attach the right bank harness covers.
>
> **Момент затяжки · Torque Value**
> 45 n•m [33 ft-lb]
