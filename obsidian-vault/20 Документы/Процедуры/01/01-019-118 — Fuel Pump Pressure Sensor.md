---
aliases:
  - "Датчик давления топливного насоса"
type: "Процедура"
doc: "01-019-118"
title_en: "Fuel Pump Pressure Sensor"
title_ru: "Датчик давления топливного насоса"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-019-118.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-019-118.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Fuel Pump Pressure Sensor
**Датчик давления топливного насоса**

> [!abstract] Процедура · `01-019-118`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-07-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-019-118.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-019-118.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Снятие

Отсоедините проводку двигателя от датчика давления.

Удалите датчик давления топливного насоса из топливного насоса.

![[19e00169.png]]

### Проверка

Подключите инструмент электронного сервиса к шине данных CAN.

![[19800902.png]]

Подключите электропроводку двигателя к датчику давления топливного насоса.

Дайте датчику и проводах висеть в воздухе.

![[19e00170.png]]

Мониторинг давления топливного насоса с помощью электронного инструментария.

Давление топливного насоса должно быть в пределах ±110,3 кПа \[16 psi\] от значения барометрического датчика давления.

Если давление топливного насоса **не** в пределах спецификации, датчик давления топливного насоса  должен быть заменен.

Отключите инструмент электронного сервиса.

Отсоедините датчик давления топливного насоса от электропроводки двигателя.

![[19800902.png]]

### Установка

Если используется новый датчик давления топливного насоса, убедитесь, что установлено кольцо.

![[19e00171.png]]

Установите датчик давления топливного насоса.

> [!tip] Момент затяжки
> 14 Н·м [124 фунт-дюйм]

Подключите электропроводку двигателя к датчику давления топливного насоса.

![[19e00169.png]]


> [!quote]- Original (English) · английский оригинал
> ### Remove
>
> Disconnect the engine harness from the pressure sensor.
>
> Remove the fuel pump pressure sensor from the fuel pump.
>
> ### Test
>
> Connect the electronic service tool to the datalink.
>
> Connect the engine harness to the fuel pump pressure sensor.
>
> Allow the sensor and harness to hang in air.
>
> Monitor the fuel pump pressure with the electronic service tool.
>
> The fuel pump pressure **must** be within ±110.3 kPa \[16 psi\] of the barometric pressure sensor value.
>
> If the fuel pump pressure is **not** within specification, the fuel pump pressure sensor **must** be replaced.
>
> Disconnect the electronic service tool.
>
> Disconnect the fuel pump pressure sensor from the engine harness.
>
> ### Install
>
> If a new fuel pump pressure sensor is used, make sure the o-ring is installed.
>
> Install the fuel pump pressure sensor.
>
> **Момент затяжки · Torque Value**
> 14 n•m [124 in-lb]
>
> Connect the engine harness to the fuel pump pressure sensor.
