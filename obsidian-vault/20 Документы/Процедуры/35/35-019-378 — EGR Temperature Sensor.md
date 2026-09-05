---
type: "Процедура"
doc: "35-019-378"
title_en: "EGR Temperature Sensor"
modified: "2022-04-26"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "3666322"
figures: 9
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/35/35-019-378.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/35-019-378.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/35"
  - "перевод/машинный"
---

# EGR Temperature Sensor

> [!abstract] Процедура · `35-019-378`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[3666322 — ISM, ISMe, and QSM11 Service Manual|3666322]]
> **Секции:** Section 19 - Electronic Controls - Group 19
> **Даты:** изменён 2022-04-26
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/35/35-019-378.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/35-019-378.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Датчик температуры выпускного отверстия для рециркуляции выхлопных газов (EGR) используется для измерения температуры выхлопных газов, выходящих из охладителя EGR. ECM использует эту температуру для контроля уровня выбросов двигателя.

Датчик температуры выходного отверстия EGR расположен на впускном воздушном роге в передней части двигателя.

Датчик температуры EGR используется для измерения температуры выхлопных газов, которые выходят из охладителя EGR.

Датчик температуры EGR расположен на кроссовере EGR.

![[nobox.png]]

### Первичная проверка

Используйте электронный сервисный инструмент для мониторинга значения датчика температуры EGR с ключом в положении ON и выключенным двигателем.

> [!note] Примечание
> Значение датчика температуры EGR должно быть проверено, когда двигатель холодный.

Значение датчика температуры EGR должно считываться в пределах 5,5°C или 10°F от температуры окружающего воздуха.

Заменить датчик температуры EGR, если значение находится за пределами указанных пределов.

![[19804012.png]]

### Подготовительные операции

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Чтобы снизить риск искрения, минусовой (-) провод аккумуляторной батареи снимайте первым, а подсоединяйте последним.

- Отсоедините аккумуляторные батареи. См. сервисное руководство изготовителя машины.
- Очистите область вокруг датчика температуры EGR.

![[ck800wa.png]]

### Снятие

Поднимите вкладку и отсоедините разъем от датчика.

Удалите датчик из соединения воздухозаборника.

![[19d01885.png]]

Отсоедините датчик температуры EGR от электропроводки двигателя.

Удалите датчик из двигателя.

![[19d01885.png]]

### Очистка и проверка при повторном использовании

Осмотрите разъём и датчик для проводов двигателя для следующего:

- Разбитая или разбитая соединительная оболочка
- Пропавшие или поврежденные соединительные уплотнения
- Грязь, мусор или влага в или на контактах разъема
- Коррозийные, согнутые, сломанные, отодвинутые назад или расширенные булавки
- Измельченный, треснувший, экструдированный или поврежденный датчик.

Ремонт или замена деталей по мере необходимости.

![[19d03002.png]]

### Установка

Убедитесь, что новый датчик имеет кольцо.

Смажьте уплотнительное кольцо чистым моторным маслом.

Установите новый датчик в двигатель. Затяните датчик.

> [!tip] Момент затяжки
> 15 Н·м [133 фунт-дюйм]

Подключите разъём жгута проводов двигателя к новому датчику.

![[19d01886.png]]

Проверьте, чтобы убедиться, что датчик имеет металлическую герметичную шайбу.

Установите датчик в трубку кроссовера EGR.

Затяните датчик.

> [!tip] Момент затяжки
> 34 Н·м [25 фунт-фут]

Подключите к датчику разъём ремня электропроводки двигателя.

![[19d01886.png]]

### Завершающие операции

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Чтобы снизить риск искрения, минусовой (-) провод аккумуляторной батареи снимайте первым, а подсоединяйте последним.

- Подсоедините аккумуляторные батареи. См. сервисное руководство изготовителя машины.
- Запустите двигатель и проверьте на отсутствие утечек.

![[ck800wa.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> The exhaust gas recirculation (EGR) cooler outlet temperature sensor is used to measure the temperature of the exhaust gas that exits the EGR cooler. The ECM uses this temperature to control the emission levels of the engine.
>
> The EGR cooler outlet temperature sensor is located at the intake air horn at the front of the engine.
>
> The EGR temperature sensor is used to measure the temperature of the exhaust gas that exits the EGR cooler.
>
> The EGR temperature sensor is located on the EGR crossover tube.
>
> ### Initial Check
>
> Use an electronic service tool to monitor the value of the EGR temperature sensor with the key in the ON position and the engine off.
>
> **Note · Примечание**
> The value of the EGR temperature sensor should be checked when the engine is cold.
>
> The value of the EGR temperature sensor should read within 5.5°C or 10°F of the local ambient air temperature.
>
> Replace the EGR temperature sensor if the value is out of specification.
>
> ### Preparatory Steps
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> - Disconnect the batteries. Refer to the OEM service manual.
> - Clean the area around the EGR temperature sensor.
>
> ### Remove
>
> Lift the tab and detach the connector from the sensor.
>
> Remove the sensor from the air intake connection.
>
> Disconnect the EGR temperature sensor from the engine harness.
>
> Remove the sensor from the engine.
>
> ### Clean and Inspect for Reuse
>
> Inspect the engine harness connector and sensor for the following:
>
> - Cracked or broken connector shell
> - Missing or damaged connector seals
> - Dirt, debris, or moisture in or on the connector pins
> - Corroded, bent, broken, pushed back, or expanded pins
> - Chipped, cracked, extruded, or damaged sensor.
>
> Repair or replace parts as necessary.
>
> ### Install
>
> Check to make sure the new sensor has an o-ring.
>
> Lubricate the o-ring with clean engine oil.
>
> Install the new sensor into the engine. Tighten the sensor.
>
> **Момент затяжки · Torque Value**
> 15 n•m [133 in-lb]
>
> Connect the engine harness connector to the new sensor.
>
> Check to make sure the sensor has a metal sealing washer.
>
> Install the sensor into the EGR crossover tube.
>
> Tighten the sensor.
>
> **Момент затяжки · Torque Value**
> 34 n•m [25 ft-lb]
>
> Connect the engine harness connector to the sensor.
>
> ### Finishing Steps
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> - Connect the batteries. Refer to the OEM service manual.
> - Operate the engine and check for leaks.
