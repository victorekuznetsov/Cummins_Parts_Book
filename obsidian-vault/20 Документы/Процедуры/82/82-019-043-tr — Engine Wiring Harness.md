---
aliases:
  - "Жгут проводов двигателя"
type: "Процедура"
doc: "82-019-043-tr"
title_en: "Engine Wiring Harness"
title_ru: "Жгут проводов двигателя"
modified: "2002-06-28"
engines:
  - "41343322"
  - "41370103"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 9
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-043-tr.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-019-043-tr.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# Engine Wiring Harness
**Жгут проводов двигателя**

> [!abstract] Процедура · `82-019-043-tr`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section 19 - Electronic Engine Controls
> **Даты:** изменён 2002-06-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-043-tr.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-019-043-tr.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Двигатели ISM и QSM используют отдельные проводные ремни для управления двигателем и некоторыми операциями транспортного средства. Для проводов жгутов имеется три разъёма. На изображении следующие проводные ремни соединяются с ECM справа налево:

1. Сенсорная проводка
2. Снаряд для электропроводки
3. Упряжка для проводов OEM.

![[17c00003.png]]

### Снятие

Отсоедините проводную упряжку от датчиков и переключателей.

1. Датчик давления во впускном коллекторе
2. Датчик температуры коллектора
3. Датчик положения коленчатого вала или распредвала
4. Датчик температуры охлаждающей жидкости
5. Отключение топлива соленоид
6. 15-контактный проходной разъем

![[19200220.png]]

1. Разъем CentinelTM (если оборудован)
2. Датчик атмосферного давления
3. Датчик давления и температуры масла
4. Датчик давления ресивера
5. Датчик воды в топливе
6. турбинный обводной клапанный контроллер
7. Датчик ограничения впуска топлива (если он оборудован).

![[19200221.png]]

Отсоедините 31-контактный разъем Deutsch со стороны OEM проводов.

Удалите зажимы жгута проводов из опорного скобка блока двигателя.

Отсоедините электропроводку двигателя от ECM.

![[19400420.png]]

### Проверка при повторном использовании

Замените или отремонтируйте электропроводку двигателя, если есть открытая схема или короткое замыкание, обнаруженное под защитным покрытием корпуса электропроводки.

![[19400386.png]]

### Установка

Подключите жгуты электропроводки двигателя к ECM.

> [!tip] Момент затяжки
> 2.8 Н·м [25 фунт-дюйм]

![[17c00003.png]]

Подключите проводные ремни к датчикам и переключателям.

1. Датчик давления во впускном коллекторе
2. Датчик температуры коллектора
3. Датчик положения коленчатого вала или распредвала
4. Датчик температуры охлаждающей жидкости
5. Отключение топлива соленоид
6. 15-контактный проходной разъем

![[19200220.png]]

1. Разъем CentinelTM (если оборудован)
2. Датчик атмосферного давления
3. Датчик давления и температуры масла
4. Датчик давления ресивера
5. Датчик воды в топливе
6. турбинный обводной клапанный контроллер
7. Датчик ограничения впуска топлива (если он оборудован).

![[19200221.png]]

Подключите 31-контактный разъем Deutsch к ремню проводов двигателя.

Установите зажимы жгута проводов, которые удерживают жгут проводов двигателя на блоке.

![[19400420.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> The ISM and QSM engines use separate wiring harnesses to control the engine and some of the vehicle operations. There are three connectors for the wiring harnesses. In the picture shown, the following harnesses connect to the ECM from right to left:
>
> 1. Sensor harness
> 2. Actuator harness
> 3. OEM harness.
>
> ### Remove
>
> Disconnect the harness from the sensors and switches.
>
> 1. Intake manifold pressure sensor
> 2. Intake manifold temperature sensor
> 3. Crankshaft or camshaft position sensor
> 4. Coolant temperature sensor
> 5. Fuel shutoff solenoid
> 6. 15-pin pass-through connector
>
> 1. Centinel™ connector (if equipped)
> 2. Ambient air pressure sensor
> 3. Oil pressure/temperature sensor
> 4. Wet tank pressure sensor
> 5. Water-in-fuel sensor
> 6. Wastegate controller
> 7. Fuel inlet restriction sensor (if equipped).
>
> Disconnect the 31-pin Deutsch connector from the OEM side of the wiring harness.
>
> Remove the harness clamps from the support bracket of the engine block.
>
> Disconnect the engine harnesses from the ECM.
>
> ### Inspect for Reuse
>
> Replace or repair the engine harness if there is an open circuit or a short circuit found under the protective covering of the harness body.
>
> ### Install
>
> Connect the engine harnesses to the ECM.
>
> **Момент затяжки · Torque Value**
> 2.8 n•m [25 in-lb]
>
> Connect the harnesses to the sensors and switches.
>
> 1. Intake manifold pressure sensor
> 2. Intake manifold temperature sensor
> 3. Crankshaft or camshaft position sensor
> 4. Coolant temperature sensor
> 5. Fuel shutoff solenoid
> 6. 15-pin pass-through connector
>
> 1. Centinel™ connector (if equipped)
> 2. Ambient air pressure sensor
> 3. Oil pressure/temperature sensor
> 4. Wet tank pressure sensor
> 5. Water-in-fuel sensor
> 6. Wastegate controller
> 7. Fuel inlet restriction sensor (if equipped).
>
> Connect the 31-pin Deutsch connector to the engine harness.
>
> Install the harness clamps that hold the engine harness to the block.
