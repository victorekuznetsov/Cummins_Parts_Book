---
type: "Процедура"
doc: "1016-019-099"
title_en: "Intake Manifold Absolute Pressure and Temperature Sensor"
modified: "2022-12-14"
engines:
  - "77804810"
families:
  - "15N"
manuals:
  - "5659763"
figures: 4
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/1016/1016-019-099.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/1016-019-099.pdf"
tags:
  - "документ/процедура"
  - "двигатель/15N"
  - "перевод/машинный"
---

# Intake Manifold Absolute Pressure and Temperature Sensor

> [!abstract] Процедура · `1016-019-099`
> **Двигатели:** [[77804810 — 15N CM2380 M104B CPL 5977|77804810]]
> **Семейство:** 15N
> **Входит в руководства:** [[5659763 — 15N CM2380 M104B Service Manual|5659763]]
> **Секции:** Section 19 - Electronic Controls - Group 19
> **Даты:** изменён 2022-12-14
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/1016/1016-019-099.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/1016-019-099.pdf)

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

### Подготовительные операции

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Чтобы снизить риск искрения, минусовой (-) провод аккумуляторной батареи снимайте первым, а подсоединяйте последним.

- Отсоедините аккумуляторные батареи. См. сервисную документацию изготовителя оборудования.

### Снятие

Датчик абсолютного давления/температуры впускного коллектора измеряет давление/температуру впускного коллектора.

Поднимите на запирающую вкладку и разберите электрические разъемы.

Удалите датчик из двигателя, повернув датчик **против часовой стрелки**.

![[19s00155.png]]

### Очистка и проверка при повторном использовании

> [!danger] ОПАСНО
> При работе со сжатым воздухом применяйте защиту глаз и лица. Разлетающиеся частицы и грязь могут привести к травме.

Если впускной коллектор абсолютного давления и температуры датчика заморожен, разморозьте датчик с использованием теплого воздуха, который ниже 60°C \[140°F \].

Просушите сжатым воздухом.

Осмотрите разъём ремня электропроводки двигателя и датчик для следующего:

- Разбитая или разбитая соединительная оболочка
- Пропавшие или поврежденные соединительные уплотнения
- Грязь, мусор или влага в или на контактах разъема
- Корродированные, согнутые, сломанные, отодвинутые назад или расширенные булавки.

Ремонт или замена разъёма и датчика ремня электропроводки двигателя.

![[19s00234.png]]

### Проверка

Отсоедините впускной коллектор от абсолютного датчика давления/температуры от электропроводки двигателя.

Измерить сопротивление между температурным сигнальным контактом и обратным контактом на впускном коллекторе абсолютного давления/температурного датчика разъема.

Если сопротивление не соответствует спецификации, замените впускной коллектор абсолютным датчиком давления/температуры.

| Температура vs сопротивление |  |  |  |
|---|---|---|---|
| температура | Сопротивление (Омс) |  |  |
| °C | градус | Мин | Макс |
| -50 | -58 | 607,265 | 843,786 |
| -40 | -40 | 302,255 | 419,979 |
| -30 | -22 | 157,596 | 218,978 |
| -20 | -4 | 85,643 | 119,000 |
| -10 | 14 | 48,298 | 67,109 |
| 0 | 32 | 30,683 | 36,605 |
| 10 | 50 | 18,472 | 22,036 |
| 20 | 68 | 11,462 | 13,674 |
| 30 | 86 | 7456 | 8578 |
| 40 | 104 | 4876 | 5610 |
| 50 | 122 | 3263 | 3754 |
| 60 | 140 | 2233 | 2569 |
| 70 | 158 | 1560 | 1795 |
| 80 | 176 | 1111 | 1278 |
| 90 | 194 | 814 | 917 |
| 100 | 212 | 605 | 669 |
| 110 | 230 | 450 | 502 |
| 120 | 248 | 339 | 383 |
| 130 | 266 | 259 | 396 |
| 140 | 284 | 201 | 231 |
| 150 | 302 | 157 | 183 |

![[3377161.png]]

### Установка

Убедитесь, что на новом датчике установлено кольцо.

Установите новый датчик в двигатель, повернув датчик **по часовой стрелке**.

> [!tip] Момент затяжки
> 24 Н·м [212 фунт-дюйм]

Соедините разъёмы до фиксации.

![[19s00155.png]]

### Завершающие операции

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Чтобы снизить риск искрения, минусовой (-) провод аккумуляторной батареи снимайте первым, а подсоединяйте последним.

- Подсоедините аккумуляторные батареи. См. сервисную документацию изготовителя оборудования.
- Используйте рекомендованную электронный сервисный инструмент Cummins® или эквивалент для сброса топливных столов, если впускной коллектор заменяют абсолютным датчиком давления/температуры. См. процедуру 005-263 в разделе 5.
- Управляйте двигателем. Проверьте правильность операции.


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
> ### Preparatory Steps
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> - Disconnect the batteries. See equipment manufacturer service information.
>
> ### Remove
>
> The intake manifold absolute pressure/temperature sensor measures the pressure/temperature of the intake manifold.
>
> Lift up on the locking tab and pull the electrical connectors apart.
>
> Remove the sensor from the engine by turning the sensor **counterclockwise**.
>
> ### Clean and Inspect for Reuse
>
> **WARNING · Опасно**
> Wear appropriate eye and face protection when using compressed air. Flying debris and dirt can cause personal injury.
>
> If the intake manifold absolute pressure and temperature sensor has frozen, defrost the sensor using warm air that is below 60°C \[ 140°F \].
>
> Dry with compressed air.
>
> Inspect the engine wiring harness connector and the sensor for the following:
>
> - Cracked or broken connector shell
> - Missing or damaged connector seals
> - Dirt, debris, or moisture in or on the connector pins
> - Corroded, bent, broken, pushed back, or expanded pins.
>
> Repair or replace the engine wiring harness connector and sensor.
>
> ### Test
>
> Disconnect the intake manifold absolute pressure/temperature sensor from the engine wiring harness.
>
> Measure the resistance between the temperature signal pin and return pin at the intake manifold absolute pressure/temperature sensor connector.
>
> If the resistance does **not** meet the specification, replace the intake manifold absolute pressure/temperature sensor.
>
> | Temperature vs Resistance |  |  |  |
> |---|---|---|---|
> | Temperature | Resistance (Ohms) |  |  |
> | °C | °F | MIN | MAX |
> | -50 | -58 | 607,265 | 843,786 |
> | -40 | -40 | 302,255 | 419,979 |
> | -30 | -22 | 157,596 | 218,978 |
> | -20 | -4 | 85,643 | 119,000 |
> | -10 | 14 | 48,298 | 67,109 |
> | 0 | 32 | 30,683 | 36,605 |
> | 10 | 50 | 18,472 | 22,036 |
> | 20 | 68 | 11,462 | 13,674 |
> | 30 | 86 | 7456 | 8578 |
> | 40 | 104 | 4876 | 5610 |
> | 50 | 122 | 3263 | 3754 |
> | 60 | 140 | 2233 | 2569 |
> | 70 | 158 | 1560 | 1795 |
> | 80 | 176 | 1111 | 1278 |
> | 90 | 194 | 814 | 917 |
> | 100 | 212 | 605 | 669 |
> | 110 | 230 | 450 | 502 |
> | 120 | 248 | 339 | 383 |
> | 130 | 266 | 259 | 396 |
> | 140 | 284 | 201 | 231 |
> | 150 | 302 | 157 | 183 |
>
> ### Install
>
> Make sure the new sensor has an o-ring installed on it.
>
> Install the new sensor into the engine by turning the sensor **clockwise**.
>
> **Момент затяжки · Torque Value**
> 24 n•m [212 in-lb]
>
> Push the connectors together until they lock.
>
> ### Finishing Steps
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> - Connect the batteries. See equipment manufacturer service information.
> - Use the recommended Cummins® electronic service tool, or equivalent, to reset the fuel tables if intake manifold absolute pressure/temperature sensor is replaced. Refer to Procedure 005-263 in Section 5.
> - Operate the engine. Check for proper operation.
