---
aliases:
  - "Датчик давления охлаждающей жидкости"
type: "Процедура"
doc: "01-019-016"
title_en: "Coolant Pressure Sensor"
title_ru: "Датчик давления охлаждающей жидкости"
modified: "2003-07-08"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 7
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-019-016.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-019-016.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Coolant Pressure Sensor
**Датчик давления охлаждающей жидкости**

> [!abstract] Процедура · `01-019-016`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-07-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-019-016.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-019-016.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Снятие

Отсоедините проводку двигателя от датчика давления охлаждающей жидкости.

![[19400387.png]]

Удалите датчик давления охлаждающей жидкости.

![[19801029.png]]

### Проверка

Подключите инструмент электронного сервиса к шине данных CAN.

![[19800902.png]]

Подключите жгут проводов двигателя к датчику давления охлаждающей жидкости.

Дайте датчику и проводах висеть в воздухе.

![[08600402.png]]

Мониторинг датчика давления охлаждающей жидкости с помощью электронного инструментария обслуживания.

Давление охлаждающей жидкости должно быть в пределах 17,2 кПа \[2,5 psi\] от значения барометрического датчика давления.

Если давление охлаждающей жидкости является датчиком **не** в пределах спецификаций, датчик давления охлаждающей жидкости  должен быть заменен.

Отключите инструмент электронного сервиса.

Отсоедините датчик давления охлаждающей жидкости от электропроводки двигателя.

![[19800902.png]]

### Установка

Установите датчик давления охлаждающей жидкости в блок двигателя.

Затянуть датчик давления охлаждающей жидкости.

> [!tip] Момент затяжки
> 14 Н·м [124 фунт-дюйм]

![[19801029.png]]

Подключите жгут проводов двигателя к датчику давления охлаждающей жидкости.

![[19801028.png]]


> [!quote]- Original (English) · английский оригинал
> ### Remove
>
> Disconnect the engine harness from the coolant pressure sensor.
>
> Remove the coolant pressure sensor.
>
> ### Test
>
> Connect the electronic service tool to the datalink.
>
> Connect the engine harness to the coolant pressure sensor.
>
> Allow the sensor and harness to hang in air.
>
> Monitor the coolant pressure sensor with the electronic service tool.
>
> The coolant pressure **must** be within 17.2 kPa \[2.5 psi\] of the barometric pressure sensor value.
>
> If the coolant pressure is sensor **not** within specifications, the coolant pressure sensor **must** be replaced.
>
> Disconnect the electronic service tool.
>
> Disconnect the coolant pressure sensor from the engine harness.
>
> ### Install
>
> Install the coolant pressure sensor into the engine block.
>
> Tighten the coolant pressure sensor.
>
> **Момент затяжки · Torque Value**
> 14 n•m [124 in-lb]
>
> Connect the engine harness to the coolant pressure sensor.
