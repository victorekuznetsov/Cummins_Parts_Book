---
aliases:
  - "Датчик давления моторного масла"
type: "Процедура"
doc: "60-019-066"
title_en: "Engine Oil Pressure Sensor"
title_ru: "Датчик давления моторного масла"
modified: "2007-12-14"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021674"
figures: 6
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-019-066.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-019-066.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
  - "перевод/машинный"
---

# Engine Oil Pressure Sensor
**Датчик давления моторного масла**

> [!abstract] Процедура · `60-019-066`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section 19 — Electronic Engine Controls — Group 19
> **Даты:** изменён 2007-12-14
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-019-066.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-019-066.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Подготовительные операции

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Чтобы уменьшить возможность дуги, сначала удалите отрицательный (-) кабель батареи и прикрепите отрицательный кабель батареи последним.

> [!danger] ОПАСНО
> Чтобы снизить риск травмы, не допускайте попадания горячего масла на кожу.

> [!danger] ОПАСНО
> По заключению ряда государственных органов отработанное моторное масло может обладать канцерогенным действием и вредить репродуктивной функции. Не вдыхайте пары, не допускайте попадания внутрь и длительного контакта с отработанным моторным маслом. Если деталь не используется повторно, утилизируйте её по местным природоохранным требованиям.

- Отсоедините аккумуляторные батареи. См. процедуру 013-009 (Кабели и соединения аккумуляторов) в разделе 13 в руководстве по обслуживанию QST30, Бюллетень 4021539.
- Моторное масло высушивать из двигателя. См. процедуру 007-037 (Система моторного масла) в разделе 7 в Руководстве по обслуживанию QST30, Вестник 4021539.

![[ck800wa.png]]

### Снятие

[[60-100-002 — Engine Diagrams|См. процедуру 100-002 (Диаграммы двигателя) в разделе Е для местоположений датчиков.]]

Отсоедините разъем жгута проводов двигателя от датчика давления масла двигателя.

Удалите датчик давления масла двигателя из блока двигателя с глубоководной розеткой, Номер детали 3823843 или эквивалент.

![[19801029.png]]

### Установка

Убедитесь, что датчик давления масла в двигателе имеет установленное кольцо.

Установите датчик давления масла в двигателе.

Затянуть датчик давления масла двигателя с глубоким гнездом скважины, Номер детали 3823843, или эквивалент.

> [!tip] Момент затяжки
> 14 Н·м [124 фунт-дюйм]

Подключите разъём ремня электропроводки двигателя к датчику давления масла двигателя.

![[19801029.png]]

### Проверка

Подключите инструмент электронного обслуживания INSITETM к разъему шины данных J1939 CAN.

![[19800902.png]]

Удалите датчик давления масла в двигателе.

Подключите жгут электропроводки двигателя к датчику давления масла двигателя.

Дайте датчику и проводах свободно висеть.

Мониторинг давления моторного масла с помощью электронного инструментария INSITETM.

Если датчик ** не** находится в пределах ±17,2 кПа \[2,5 psi\] давления окружающей среды, его *** необходимо заменить.

![[08600402.png]]

### Завершающие операции

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Чтобы уменьшить возможность дуги, сначала удалите отрицательный (-) кабель батареи и прикрепите отрицательный кабель батареи последним.

> [!danger] ОПАСНО
> Чтобы снизить риск травмы, не допускайте попадания горячего масла на кожу.

> [!danger] ОПАСНО
> По заключению ряда государственных органов отработанное моторное масло может обладать канцерогенным действием и вредить репродуктивной функции. Не вдыхайте пары, не допускайте попадания внутрь и длительного контакта с отработанным моторным маслом. Если деталь не используется повторно, утилизируйте её по местным природоохранным требованиям.

- Заполните двигатель моторным маслом. См. процедуру 007-037 (Система моторного масла) в разделе 7 в Руководстве по обслуживанию QST30, Вестник 4021539.
- Подсоедините аккумуляторные батареи. См. процедуру 013-009 (Кабели и соединения аккумуляторов) в разделе 13 в руководстве по обслуживанию QST30, Бюллетень 4021539.

![[ck800wa.png]]


> [!quote]- Original (English) · английский оригинал
> ### Preparatory Steps
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative battery cable last.
>
> **WARNING · Опасно**
> To reduce the possibility of personal injury, avoid direct contact of hot oil with your skin.
>
> **WARNING · Опасно**
> Some state and federal agencies have determined that used engine oil can be carcinogenic and cause reproductive toxicity. Avoid inhalation of vapors, ingestion, and prolonged contact with used engine oil. If not reused, dispose of in accordance with local environmental regulations.
>
> - Disconnect the batteries. Refer to Procedure 013-009 (Battery Cables and Connections) in Section 13 in the QST30 Service Manual, Bulletin 4021539.
> - Drain lubricating oil from the engine. Refer to Procedure 007-037 (Lubricating Oil System) in Section 7 in the QST30 Service Manual, Bulletin 4021539.
>
> ### Remove
>
> [[60-100-002 — Engine Diagrams|Refer to Procedure 100-002 (Engine Diagrams) in Section E for sensor locations.]]
>
> Disconnect the engine harness connector from the engine oil pressure sensor.
>
> Remove the engine oil pressure sensor from the engine block with a deep-well socket, Part Number 3823843, or equivalent.
>
> ### Install
>
> Make sure the engine oil pressure sensor has an o-ring installed.
>
> Install the engine oil pressure sensor.
>
> Tighten the engine oil pressure sensor with deep well socket, Part Number 3823843, or equivalent.
>
> **Момент затяжки · Torque Value**
> 14 n•m [124 in-lb]
>
> Connect the engine harness connector to the engine oil pressure sensor.
>
> ### Test
>
> Connect INSITE™ electronic service tool to the J1939 data link connector.
>
> Remove the engine oil pressure sensor.
>
> Connect the engine harness to the engine oil pressure sensor.
>
> Allow the sensor and harness to hang freely.
>
> Monitor the lubricating oil pressure with the INSITE™ electronic service tool.
>
> If the sensor is **not** within ±17.2 kPa \[2.5 psi\] of the ambient pressure, it **must** be replaced.
>
> ### Finishing Steps
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative battery cable last.
>
> **WARNING · Опасно**
> To reduce the possibility of personal injury, avoid direct contact of hot oil with your skin.
>
> **WARNING · Опасно**
> Some state and federal agencies have determined that used engine oil can be carcinogenic and cause reproductive toxicity. Avoid inhalation of vapors, ingestion, and prolonged contact with used engine oil. If not reused, dispose of in accordance with local environmental regulations.
>
> - Fill the engine with lubricating oil. Refer to Procedure 007-037 (Lubricating Oil System) in Section 7 in the QST30 Service Manual, Bulletin 4021539.
> - Connect the batteries. Refer to Procedure 013-009 (Battery Cables and Connections) in Section 13 in the QST30 Service Manual, Bulletin 4021539.
