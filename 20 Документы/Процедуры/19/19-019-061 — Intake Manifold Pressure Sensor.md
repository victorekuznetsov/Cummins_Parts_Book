---
aliases:
  - "Датчик давления во впускном коллекторе"
type: "Процедура"
doc: "19-019-061"
title_en: "Intake Manifold Pressure Sensor"
title_ru: "Датчик давления во впускном коллекторе"
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
figures: 6
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-019-061.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-019-061.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
  - "перевод/машинный"
---

# Intake Manifold Pressure Sensor
**Датчик давления во впускном коллекторе**

> [!abstract] Процедура · `19-019-061`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2002-08-20
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-019-061.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-019-061.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Первичная проверка

Подключите электронный инструмент к шине данных CAN транспортного средства.

![[19400357.png]]

Установите манометр 0-2030 мм-Hg \[0-80 in-Hg\] (или калибр) в отверстие трубы в корпусе послеохладителя \[3/8-дюймовый\].

Сделайте **не** сверлить и нажмите отверстие в крышке послеохладителя. Неправильное считывание может привести к утечке ядра после охлаждения.

![[10400032.png]]

Работайте с двигателем при номинальной оборотах и полной нагрузке. Сравните показания с электронным инструментом обслуживания с показаниями измерительной шкалы. Если показания электронного инструментария отличаются более чем на 2 рт.ст. от показаний калибра, то замените датчик давления впускного коллектора.

![[10400033.png]]

### Снятие

Поднимите на вкладку и отсоедините разъем от датчика.

Удалите датчик из коллектора воздухозаборника с глубокой фланцевой розеткой, номер детали 3823843.

![[19400439.png]]

### Установка

Убедитесь, что новый датчик имеет кольцо вокруг поверхности, где он уплотняет коллектор воздухозаборника.

Установите датчик в коллектор воздухозаборника, повернув его **по часовой стрелке.**

> [!tip] Момент затяжки
> 14 Н·м [124 фунт-дюйм]

![[19400440.png]]

Подтолкните проводку разъёма жгута к датчику, пока он не заблокируется.

![[19400452.png]]


> [!quote]- Original (English) · английский оригинал
> ### Initial Check
>
> Connect an electronic service tool to the vehicle datalink.
>
> Install a 0-2030 mm-Hg \[0-80 in-Hg\] manometer (or gauge) in the \[3/8-inch\] pipe plug hole in the aftercooler housing.
>
> Do **not** drill and tap a hole in the aftercooler cover. A faulty reading can result if the aftercooler core is leaking.
>
> Operate the engine at rated rpm and full load. Compare the reading from the electronic service tool to the gauge reading. If the electronic service tool reading differs by more than 2 in Hg from the gauge reading, then replace the intake manifold pressure sensor.
>
> ### Remove
>
> Lift up on the tab and disconnect the connector from the sensor.
>
> Remove the sensor from the air intake manifold with deep flank drive socket, Part Number 3823843.
>
> ### Install
>
> Make sure the new sensor has an o-ring around the surface where it seals against the air intake manifold.
>
> Install the sensor into the air intake manifold by turning it **clockwise.**
>
> **Момент затяжки · Torque Value**
> 14 n•m [124 in-lb]
>
> Push the harness connector into the sensor until it locks.
