---
aliases:
  - "Датчик давления во впускном коллекторе"
type: "Процедура"
doc: "87-019-061"
title_en: "Intake Manifold Pressure Sensor"
title_ru: "Датчик давления во впускном коллекторе"
modified: "2003-02-10"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666214"
figures: 9
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-019-061.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-019-061.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
  - "перевод/машинный"
---

# Intake Manifold Pressure Sensor
**Датчик давления во впускном коллекторе**

> [!abstract] Процедура · `87-019-061`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-02-10
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-019-061.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-019-061.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Первичная проверка

Подключите электронный инструмент к шине данных CAN транспортного средства.

![[19900524.png]]

Установите манометр (или калибр) от 0 до 2030 мм Hg \[0- до 80-дюймовых Hg\] в 3/8-дюймовом пробочном отверстии трубы в корпусе послеохладителя.

Сделайте **не** сверлить и нажмите отверстие в крышке послеохладителя. Неправильное считывание может привести к утечке ядра после охлаждения.

![[19a00340.png]]

Работайте с двигателем при номинальной оборотах и полной нагрузке. Сравните показания с электронным инструментом обслуживания с показаниями измерительной шкалы. Если показания электронного инструментария отличаются более чем на 50 мм рт.ст. \[2 в рт.ст.] от показаний калибра, то замените датчик давления впускного коллектора.

![[10400033.png]]

### Снятие

Поднимите на вкладку и отсоедините разъем от датчика.

![[19a00243.png]]

Удалите датчик из коллектора воздухозаборника с глубокой фланцевой розеткой, номер детали 3823843.

![[19a00244.png]]

### Установка

Убедитесь, что новый датчик имеет кольцо вокруг поверхности, где он уплотняет коллектор воздухозаборника.

Смажьте уплотнительное кольцо чистым моторным маслом.

![[19a00253.png]]

Установите датчик в коллектор воздухозаборника, повернув его ** по часовой стрелке**.

> [!tip] Момент затяжки
> 14 Н·м [124 фунт-дюйм]

![[19a00244.png]]

> [!warning] ОСТОРОЖНО
> Используйте только рекомендованную Cummins смазку DS-ES, Part Number, 3822934. Другие смазочные материалы, такие как моторное масло или смазка, в разъемах могут вызвать повреждение ECM, плохую производительность двигателя или преждевременный контактный износ разъема.

Нанесите небольшое количество смазки на соединительные терминалы. Перед установкой наполните всю полость смазкой.

![[cel29.png]]

Подтолкните проводку разъёма жгута к датчику, пока он не заблокируется.

![[19a00243.png]]


> [!quote]- Original (English) · английский оригинал
> ### Initial Check
>
> Connect an electronic service tool to the vehicle datalink.
>
> Install a 0- to 2030-mm Hg \[0- to 80-in Hg\] manometer (or gauge) in the 3/8-inch pipe plug hole in the aftercooler housing.
>
> Do **not** drill and tap a hole in the aftercooler cover. A faulty reading can result if the aftercooler core is leaking.
>
> Operate the engine at rated rpm and full load. Compare the reading from the electronic service tool to the gauge reading. If the electronic service tool reading differs by more than 50 mm Hg \[2 in Hg\] from the gauge reading, then replace the intake manifold pressure sensor.
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
> Lubricate the o-ring with clean engine oil.
>
> Install the sensor into the air intake manifold by turning it **clockwise**.
>
> **Момент затяжки · Torque Value**
> 14 n•m [124 in-lb]
>
> **CAUTION · Осторожно**
> Use only Cummins-recommended lubricant DS-ES, Part Number, 3822934. Other lubricants, such as lubricating oil or grease, in the connectors can cause ECM damage, poor engine performance, or premature connector pin wear.
>
> Apply a small amount of lubricant to the connector terminals. Before installing, fill the entire cavity with lubricant.
>
> Push the harness connector into the sensor until it locks.
