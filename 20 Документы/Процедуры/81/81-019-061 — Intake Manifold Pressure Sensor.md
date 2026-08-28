---
aliases:
  - "Датчик давления во впускном коллекторе"
type: "Процедура"
doc: "81-019-061"
title_en: "Intake Manifold Pressure Sensor"
title_ru: "Датчик давления во впускном коллекторе"
modified: "2003-08-26"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
families:
  - "QSK60"
manuals:
  - "3666410"
figures: 6
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/81/81-019-061.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/81-019-061.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK60"
  - "группа/81"
  - "перевод/машинный"
---

# Intake Manifold Pressure Sensor
**Датчик давления во впускном коллекторе**

> [!abstract] Процедура · `81-019-061`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]]
> **Семейство:** QSK60
> **Входит в руководства:** [[3666410 — QSK45 and QSK60 CENSE™ Electronic Control System Troubleshooting and Repair Manual|3666410]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-08-26
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/81/81-019-061.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/81-019-061.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Первичная проверка

Подключите электронный инструмент к шине данных CAN транспортного средства.

> [!note] Примечание
> Датчик давления впускного коллектора также называется датчиком давления наддува.

![[19a00042.png]]

Установите манометр (или калибр) от 0 до 2030 мм рт.ст. \[0 до 80 в рт.ст.] в отверстие \[3/8-в\] в корпусе охладителя.

Сделайте **не** сверлить и нажмите отверстие в крышке послеохладителя. Неправильное считывание может привести к утечке ядра после охлаждения.

![[10400032.png]]

Работайте с двигателем при номинальной оборотах и полной нагрузке. Сравните показания с электронным инструментом обслуживания с показаниями измерительной шкалы. Если показания электронного инструментария отличаются более чем на 2 рт.ст. от показаний калибра, замените датчик давления впускного коллектора.

![[10400033.png]]

### Снятие

Поднимите на вкладку и отсоедините разъем от датчика.

Удалите датчик из коллектора воздухозаборника с глубокой фланцевой розеткой привода, номер детали. 3823843.

![[19400439.png]]

### Установка

Убедитесь, что новый датчик имеет кольцо вокруг поверхности, где он уплотняет коллектор воздухозаборника. Смазать кольцо.

Установите датчик в коллектор воздухозаборника, повернув его **по часовой стрелке.**

> [!tip] Момент затяжки
> 14 Н·м [10 фунт-фут]

![[19400440.png]]

Подтолкните проводку разъёма жгута к датчику, пока он не заблокируется.

![[19400452.png]]


> [!quote]- Original (English) · английский оригинал
> ### Initial Check
>
> Connect an electronic service tool to the vehicle datalink.
>
> **Note · Примечание**
> The intake manifold pressure sensor is also referred to as boost pressure sensor.
>
> Install a 0 to 2030 mm Hg \[0 to 80 in Hg\] manometer (or gauge) in the \[3/8-in\] pipe plug hole in the aftercooler housing.
>
> Do **not** drill and tap a hole in the aftercooler cover. A faulty reading can result if the aftercooler core is leaking.
>
> Operate the engine at rated rpm and full load. Compare the reading from the electronic service tool to the gauge reading. If the electronic service tool reading differs by more than 2 in Hg from the gauge reading, replace the intake manifold pressure sensor.
>
> ### Remove
>
> Lift up on the tab, and disconnect the connector from the sensor.
>
> Remove the sensor from the air intake manifold with deep flank drive socket, Part No. 3823843.
>
> ### Install
>
> Make sure the new sensor has an o-ring around the surface where it seals against the air intake manifold. Lubricate the o-ring.
>
> Install the sensor into the air intake manifold by turning it **clockwise.**
>
> **Момент затяжки · Torque Value**
> 14 n•m [10 ft-lb]
>
> Push the harness connector into the sensor until it locks.
