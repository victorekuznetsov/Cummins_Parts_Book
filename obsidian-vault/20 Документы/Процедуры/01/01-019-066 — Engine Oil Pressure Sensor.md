---
aliases:
  - "Датчик давления моторного масла"
type: "Процедура"
doc: "01-019-066"
title_en: "Engine Oil Pressure Sensor"
title_ru: "Датчик давления моторного масла"
modified: "2003-07-08"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 6
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-019-066.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-019-066.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Engine Oil Pressure Sensor
**Датчик давления моторного масла**

> [!abstract] Процедура · `01-019-066`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-07-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-019-066.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-019-066.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Снятие

Отсоедините жгут электропроводки двигателя от датчика.

![[19400437.png]]

Удалите датчик давления масла из блока двигателя с глубоководной розеткой, номер детали 3823843.

![[19801029.png]]

### Проверка

Подключите инструмент электронного сервиса к шине данных CAN.

![[19800902.png]]

Подключите жгут электропроводки двигателя к датчику давления моторного масла.

Дайте датчику и проводах висеть в воздухе.

![[08600402.png]]

Мониторинг давления моторного масла с помощью электронного инструментария.

Для двигателей QSK23, QSK45 и QSK60 датчик давления моторного масла **должен **находиться в пределах ±17,2 кПа \[2,5 psi\] (измерительный датчик) нуля.

Для двигателей QSX15, QST30 и QSK78 датчик давления моторного масла **должен **находиться в пределах ±17,2 кПа \[2,5 psi\] (абсолютно) значения барометрического датчика давления.

Если датчик давления моторного масла **не** в пределах спецификаций, датчик давления моторного масла должен быть заменен.

Отсоедините датчик давления моторного масла от электропроводки двигателя.

Отключите инструмент электронного сервиса.

![[19800902.png]]

### Установка

Если используется новый датчик давления моторного масла, убедитесь, что установлено кольцо.

Установите датчик давления моторного масла в блок двигателя.

Используйте глубоководную розетку, номер детали 3823843, чтобы затянуть датчик давления моторного масла.

> [!tip] Момент затяжки
> 14 Н·м [124 фунт-дюйм]

Подключите жгут электропроводки двигателя к датчику давления моторного масла.

![[19400438.png]]


> [!quote]- Original (English) · английский оригинал
> ### Remove
>
> Disconnect the engine harness from the sensor.
>
> Remove the oil pressure sensor from the engine block with a deep-well socket, Part Number 3823843.
>
> ### Test
>
> Connect the electronic service tool to the datalink.
>
> Connect the engine harness to the lubricating oil pressure sensor.
>
> Allow the sensor and harness to hang in air.
>
> Monitor the lubricating oil pressure with the electronic service tool.
>
> For the QSK23, QSK45, and QSK60 engines the lubricating oil pressure sensor **must** be within ±17.2 kPa \[2.5 psi\] (gauge) of zero.
>
> For the QSX15, QST30 and QSK78 engines the lubricating oil pressure sensor **must** be within ±17.2 kPa \[2.5 psi\] (absolute) of the barometric pressure sensor value.
>
> If the lubricating oil pressure sensor is **not** within specifications the lubricating oil pressure sensor **must** be replaced.
>
> Disconnect the lubricating oil pressure sensor from the engine harness.
>
> Disconnect the electronic service tool.
>
> ### Install
>
> If a new lubricating oil pressure sensor is used make sure the o-ring is installed.
>
> Install the lubricating oil pressure sensor into the engine block.
>
> Use a deep-well socket, Part Number 3823843 to tighten the lubricating oil pressure sensor.
>
> **Момент затяжки · Torque Value**
> 14 n•m [124 in-lb]
>
> Connect the engine harness to the lubricating oil pressure sensor.
