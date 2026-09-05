---
aliases:
  - "Датчик давления прорыва газов"
type: "Процедура"
doc: "56-019-011"
title_en: "Blowby Pressure Sensor"
title_ru: "Датчик давления прорыва газов"
modified: "2021-11-08"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
  - "33239746"
families:
  - "QSK60"
  - "QSK60 CM2150 MCRS"
manuals:
  - "4021530"
figures: 5
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/56/56-019-011.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/56-019-011.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK60"
  - "двигатель/QSK60CM2150MCRS"
  - "группа/56"
  - "перевод/машинный"
---

# Blowby Pressure Sensor
**Датчик давления прорыва газов**

> [!abstract] Процедура · `56-019-011`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]]
> **Семейство:** QSK60, QSK60 CM2150 MCRS
> **Входит в руководства:** [[4021530 — QSK45 and QSK60 Service Manual|4021530]]
> **Секции:** Section 19 - Electronic Controls - Group 19
> **Даты:** изменён 2021-11-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/56/56-019-011.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/56-019-011.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Первичная проверка

Используйте инструмент для обдувки и водный манометр, часть номер ST-1111-3. Максимальная мощность измерительной шкалы составляет 1270 мм Н 2 0 \[50 в Н 2 0 \].

| **Номер детали инструмента**| **Размеры зданий** |
|---|---|
| 3822568 | 10 мм \[0.406 in\] |

![[eg8toga.png]]

Используйте длинный шланг (1), чтобы прикрепить инструмент для продувки к одному из задувных воздухозаборников.

Прикрепить манометр к указанному месту (2).

![[14400010.png]]

Подключите электронный инструмент к шине данных CAN.

Мониторинг результатов от сервисного инструментария. Если результаты отличаются более чем на 10 мм H2O \[0,394 в\], то замените датчик продува.

![[19400357.png]]

### Снятие

Удалите зажимы шланга, которые прикрепляют датчик давления продува к двигателю.

Поднимите на запирающую вкладку и разберите электрические разъемы.

Удалите датчик.

![[19800826.png]]

### Установка

Установите датчик на двигатель. Установите и затяните зажимы шланга.

Соедините разъёмы до фиксации.

![[19800826.png]]


> [!quote]- Original (English) · английский оригинал
> ### Initial Check
>
> Use the blowby service tool and a water manometer, Part Number ST-1111-3. Maximum gauge capacity is 1270 mm H 2 0 \[50 in H 2 0\].
>
> | **Blowby Tool Part Number** | **Orifice Size** |
> |---|---|
> | 3822568 | 10 mm \[0.406 in\] |
>
> Use a length of hose (1) to attach the blowby tool to one of the crankcase breathers.
>
> Attach a manometer to the location shown (2).
>
> Connect an electronic service tool to the data link.
>
> Monitor results from service tool. If the results are different by more than 10 mm H2O \[0.394 in\] then replace the blowby sensor.
>
> ### Remove
>
> Remove the hose clamps that attach the blowby pressure sensor to the engine.
>
> Lift up on the locking tab and pull the electrical connectors apart.
>
> Remove the sensor.
>
> ### Install
>
> Install the sensor on the engine. Install and tighten the hose clamps.
>
> Push the connectors together until they lock.
