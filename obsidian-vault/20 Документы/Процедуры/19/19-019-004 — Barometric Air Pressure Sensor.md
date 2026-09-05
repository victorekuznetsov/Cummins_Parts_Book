---
aliases:
  - "Датчик барометрического давления"
type: "Процедура"
doc: "19-019-004"
title_en: "Barometric Air Pressure Sensor"
title_ru: "Датчик барометрического давления"
modified: "2002-08-20"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
  - "85017333"
families:
  - "QSK23"
  - "QSK60"
manuals:
  - "3666113"
figures: 3
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-019-004.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-019-004.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
  - "перевод/машинный"
---

# Barometric Air Pressure Sensor
**Датчик барометрического давления**

> [!abstract] Процедура · `19-019-004`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2002-08-20
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-019-004.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-019-004.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Первичная проверка

Подключите электронный инструмент к шине данных CAN транспортного средства.

Переведите замок зажигания в положение ON.

Контролируйте давление окружающего воздуха. Если давление окружающего воздуха меньше или равно 523 мм рт.ст. \[20,6 в рт.ст.] и текущее возвышение составляет менее 10 000 футов, замените датчик давления окружающего воздуха.

![[19400357.png]]

### Снятие

Поднимите на вкладку и отсоедините разъем от датчика.

Удалите крепежные болты и датчик из двигателя.

![[19400379.png]]

### Установка

Установите новый датчик на двигатель. Затяните болты.

> [!tip] Момент затяжки
> 23 Н·м [204 фунт-дюйм]

Соедините разъёмы до фиксации.

![[19400379.png]]


> [!quote]- Original (English) · английский оригинал
> ### Initial Check
>
> Connect an electronic service tool to the vehicle datalink.
>
> Turn the keyswitch to the ON position.
>
> Monitor the ambient air pressure. If an ambient air pressure is less than or equal to 523 mm Hg \[20.6 in Hg\] and the current elevation is less than 10,000 feet, replace the ambient air pressure sensor.
>
> ### Remove
>
> Lift up on the tab and disconnect the connector from the sensor.
>
> Remove the mounting capscrews and sensor from the engine.
>
> ### Install
>
> Install a new sensor on the engine. Tighten the capscrews.
>
> **Момент затяжки · Torque Value**
> 23 n•m [204 in-lb]
>
> Push the connectors together until they lock.
