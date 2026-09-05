---
type: "Процедура"
doc: "1016-019-461"
title_en: "EGR Orifice Pressure Sensor"
modified: "2022-12-14"
engines:
  - "77804810"
families:
  - "15N"
manuals:
  - "5659763"
figures: 7
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/1016/1016-019-461.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/1016-019-461.pdf"
tags:
  - "документ/процедура"
  - "двигатель/15N"
  - "перевод/машинный"
---

# EGR Orifice Pressure Sensor

> [!abstract] Процедура · `1016-019-461`
> **Двигатели:** [[77804810 — 15N CM2380 M104B CPL 5977|77804810]]
> **Семейство:** 15N
> **Входит в руководства:** [[5659763 — 15N CM2380 M104B Service Manual|5659763]]
> **Секции:** Section 19 - Electronic Controls - Group 19
> **Даты:** изменён 2022-12-14
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/1016/1016-019-461.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/1016-019-461.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Выбор сервисного инструмента

#### Рекомендованный сервисный инструмент Cummins®

- Электронный сервисный инструмент Cummins® или эквивалент

#### Дополнительные сервисные позиции

- Никаких дополнительных предметов обслуживания не требуется.

### Снятие

Датчик давления выхлопных газов (EGR) (1) установлен на кроссоверной трубке EGR.

![[19s00158.png]]

Отсоедините жгут электропроводки двигателя от датчика давления EGR.

Удалите датчик давления EGR.

![[19s00159.png]]

### Очистка и проверка при повторном использовании

> [!danger] ОПАСНО
> При работе со сжатым воздухом применяйте защиту глаз и лица. Разлетающиеся частицы и грязь могут привести к травме.

Если датчик давления EGR заморожен, разморозьте датчик, используя теплый воздух ниже 60°C[140°F].

Просушите сжатым воздухом.

Осмотрите разъём ремня электропроводки двигателя и датчик для следующего:

- Разбитая или разбитая соединительная оболочка
- Пропавшие или поврежденные соединительные уплотнения
- Грязь, мусор или влага в или на контактах разъема
- Корродированные, согнутые, сломанные, отодвинутые назад или расширенные булавки.

Ремонт или замена разъёма и датчика проводов двигателя по мере необходимости.

![[19s00235.png]]

### Проверка

Подключите рекомендуемую электронную сервисную инструментальную установку Cummins® или эквивалентную шину данных CAN.

![[19c01526.png]]

Подключите жгут электропроводки двигателя к датчику давления EGR.

Оставьте датчик подвешенным к проводах.

![[19c01525.png]]

Мониторинг давления EGR отверстия с помощью электронного инструментария обслуживания.

Датчик давления EGR отверстия **должен **находиться в пределах ±17,2 кПа \[2,5 psi \] нуля.

Если датчик давления EGR в пределах спецификаций **не**, датчик давления в отверстии EGR должен быть заменен.

Отсоедините датчик давления EGR от электропроводки двигателя.

Отключите инструмент электронного сервиса.

![[05s00033.png]]

### Установка

Проверьте, установлено ли кольцо на датчике.

Установите датчик давления EGR.

> [!tip] Момент затяжки
> 14 Н·м [124 фунт-дюйм]

Подключите жгут электропроводки двигателя к датчику давления EGR. Слышный щелчок будет слышен, когда разъем запирается на месте.

![[19s00159.png]]


> [!quote]- Original (English) · английский оригинал
> ### Select Service Tools
>
> #### Recommended Cummins® Service Tools
>
> - Cummins® electronic service tool, or equivalent
>
> #### Additional Service Items
>
> - No additional service items required.
>
> ### Remove
>
> The Exhaust Gas Recirculation (EGR) orifice pressure sensor (1) is mounted on the EGR crossover tube.
>
> Disconnect the engine wiring harness from the EGR orifice pressure sensor.
>
> Remove the EGR orifice pressure sensor.
>
> ### Clean and Inspect for Reuse
>
> **WARNING · Опасно**
> Wear appropriate eye and face protection when using compressed air. Flying debris and dirt can cause personal injury.
>
> If the EGR orifice pressure sensor has frozen, defrost the sensor using warm air that is below 60°C \[ 140°F \].
>
> Dry with compressed air.
>
> Inspect the engine harness connector and the sensor for the following:
>
> - Cracked or broken connector shell
> - Missing or damaged connector seals
> - Dirt, debris, or moisture in or on the connector pins
> - Corroded, bent, broken, pushed back, or expanded pins.
>
> Repair or replace the engine harness connector and sensor as needed.
>
> ### Test
>
> Connect the recommended Cummins® electronic service tool, or equivalent, to the data link.
>
> Connect the engine wiring harness to the EGR orifice pressure sensor.
>
> Leave the sensor suspended from the harness.
>
> Monitor the EGR orifice pressure with the electronic service tool.
>
> The EGR orifice pressure sensor **must** be within ±17.2 kPa \[ 2.5 psi \] of zero.
>
> If the EGR orifice pressure sensor is **not** within specifications, the EGR orifice pressure sensor **must** be replaced.
>
> Disconnect the EGR orifice pressure sensor from the engine wiring harness.
>
> Disconnect the electronic service tool.
>
> ### Install
>
> Verify the o-ring is installed on the sensor.
>
> Install the EGR orifice pressure sensor.
>
> **Момент затяжки · Torque Value**
> 14 n•m [124 in-lb]
>
> Connect the engine wiring harness to the EGR orifice pressure sensor. An audible click will be heard when the connector locks in place.
