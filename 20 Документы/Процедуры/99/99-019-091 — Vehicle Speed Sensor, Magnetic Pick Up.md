---
aliases:
  - "Индуктивный датчик скорости машины"
type: "Процедура"
doc: "99-019-091"
title_en: "Vehicle Speed Sensor, Magnetic Pick Up"
title_ru: "Индуктивный датчик скорости машины"
modified: "2008-05-30"
engines:
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 12
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-091.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/99-019-091.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/99"
  - "перевод/машинный"
---

# Vehicle Speed Sensor, Magnetic Pick Up
**Индуктивный датчик скорости машины**

> [!abstract] Процедура · `99-019-091`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section 19 - Electronic Engine Controls
> **Даты:** изменён 2008-05-30
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-091.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/99-019-091.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Датчик скорости транспортного средства (VSS) определяет скорость выходного вала трансмиссии. Скорость движения автомобиля рассчитывается на основе этих данных с помощью электронного модуля управления (ECM). ECM использует запрограммированные данные о шестерни и размере шин для расчета скорости движения.

![[19c01291.png]]

Датчик скорости транспортного средства расположен в задней части корпуса трансмиссии.

Датчик скорости автомобиля имеет две катушки. Одна катушка соединена с ECM, а другая катушка соединена со спидометром транспортного средства или каким-либо другим устройством транспортного средства.

> [!note] Примечание
> Конструкция датчика скорости транспортного средства варьируется в зависимости от применения. См. руководство по устранению неполадок и ремонту оригинального оборудования (OEM), чтобы понять, какой тип датчика скорости транспортного средства используется в данном месте.

![[19200262.png]]

### Снятие

Отсоедините проводку двигателя от датчика скорости автомобиля.

Ослабьте локон. Выключите датчик скорости автомобиля из корпуса трансмиссии.

![[19900797.png]]

### Проверка при повторном использовании

Осмотрите кончик датчика скорости транспортного средства на предмет грязи, мусора или физического повреждения (треснутый горшок и т. Д.).

Очистите наконечник, если он грязный, или замените датчик скорости автомобиля, если он поврежден.

![[19900798.png]]

### Установка

> [!warning] ОСТОРОЖНО
> Убедитесь, что зубчатая передача выровнена с отверстием в корпусе. Установите датчик скорости автомобиля в отверстие, пока он не коснется зуба передачи.

> [!note] Примечание
> Если датчик скорости транспортного средства ** не** включается с давлением пальца, проверьте резьбу в передаточном отверстии и резьбу датчика на предмет грязи или повреждений.

![[19900799.png]]

Выключите датчик скорости автомобиля от 1/2 до 3/4 поворота.

![[19900800.png]]

Затяните локон против коробки передач.

Вращение датчика в соответствии с OEM или спецификациями передачи. См. руководство по устранению неполадок и ремонту OEM для подробных процедур.

Установите оба разъема вместе, пока разъемы не «застегнутся» в положение. Разъемы могут быть взаимозаменяемы друг с другом без изменения производительности системы.

![[19900801.png]]

### Проверка сопротивления

Поднимите вкладку на разъемы и разберите их.

> [!note] Примечание
> При измерении значения сопротивления катушек датчика скорости транспортного средства используйте два испытательных щупа гнездового пола. Это позволит мягко сгибать электрические провода датчика для проверки поврежденных или частично сломанных резьб провода под изоляцией.

![[19900802.png]]

Используйте мультиметр для измерения сопротивления между двумя штифтами каждого разъема на датчике скорости автомобиля. См. руководство по устранению неполадок и ремонту OEM для подробных процедур. Если сопротивление ** не** правильно, замените датчик скорости транспортного средства. Если значение сопротивления правильное, датчик скорости транспортного средства ** должен** все еще проверяться на короткое замыкание на землю и короткое замыкание между катушками.

![[19900803.png]]

### Проверка на замыкание на массу

Измерить сопротивление между магнитным датчиком скорости транспортного средства сигналом отрицательного (-) штифта одного из разъемов и блока двигателя. См. руководство по устранению неполадок и ремонту OEM для подробных процедур.

![[19200262.png]]

Измерить сопротивление между магнитным датчиком скорости транспортного средства сигналом отрицательного (-) штифта другого разъема и блока двигателя. См. руководство по устранению неполадок и ремонту OEM для подробных процедур.

![[19200263.png]]

Проверьте короткое замыкание между катушками

Используйте мультиметр для измерения сопротивления между отрицательным (-) штифтом одного из разъемов датчика скорости магнитного транспортного средства и (-) штифтом другого разъема датчика скорости магнитного транспортного средства. См. руководство по устранению неполадок и ремонту OEM для подробных процедур.

![[19200264.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> The vehicle speed sensor (VSS) senses the speed of the output shaft of the transmission. The vehicle's road speed is computed from this data by the electronic control module (ECM). The ECM uses programmed gearing and tire size data to compute the road speed.
>
> The vehicle speed sensor is located in the rear of the transmission housing.
>
> The vehicle speed sensor has two coils. One coil is connected to the ECM and the other coil is connected to the vehicle speedometer, or some other vehicle device.
>
> **Note · Примечание**
> Vehicle speed sensor design varies with the application. Refer to the original equipment manufacturer (OEM) troubleshooting and repair manual to understand which type of vehicle speed sensor is being used in a given location.
>
> ### Remove
>
> Disconnect the engine harness from the vehicle speed sensor.
>
> Loosen the locknut. Turn the vehicle speed sensor out of the transmission housing.
>
> ### Inspect for Reuse
>
> Inspect the tip of the vehicle speed sensor for dirt, debris, or physical damage (cracked potting, and so forth).
>
> Clean the tip if dirty, or replace the vehicle speed sensor if damaged.
>
> ### Install
>
> **CAUTION · Осторожно**
> Make sure a gear tooth is aligned with the hole in the housing. Install the vehicle speed sensor into the hole until it touches the gear tooth.
>
> **Note · Примечание**
> If the vehicle speed sensor does **not** turn in with finger pressure, check the transmission hole threads and the sensor threads for dirt or damage.
>
> Turn the vehicle speed sensor out 1/2 to 3/4 of a turn.
>
> Tighten the locknut against the transmission housing.
>
> Torque the sensor according to the OEM or transmission specifications. Refer to the OEM troubleshooting and repair manual for detailed procedures.
>
> Install both of the connectors together until connectors "snap" into position. The connectors can be interchanged with each other without changing the performance of the system.
>
> ### Resistance Check
>
> Lift the tab on the connectors and pull them apart.
>
> **Note · Примечание**
> When measuring the resistance value of the vehicle speed sensor coils, use two female test leads. This will allow the electrical leads of the sensor to be softly flexed to check for damaged or partially broken wire strands under the insulation.
>
> Use a multimeter to measure the resistance between the two pins of each connector on the vehicle speed sensor. Refer to the OEM troubleshooting and repair manual for detailed procedures. If the resistance is **not** correct, replace the vehicle speed sensor. If the resistance value is correct, the vehicle speed sensor **must** still be checked for a short circuit to ground and a short circuit between coils.
>
> ### Check for Short Circuit to Ground
>
> Measure the resistance between the magnetic vehicle speed sensor signal negative (-) pin of one of the connectors and the engine block. Refer to the OEM troubleshooting and repair manual for detailed procedures.
>
> Measure the resistance between the magnetic vehicle speed sensor signal negative (-) pin of the other connector and the engine block. Refer to the OEM troubleshooting and repair manual for detailed procedures.
>
> Check for a short circuit between coils
>
> Use a multimeter to measure the resistance between the magnetic vehicle speed sensor signal negative (-) pin of one of the connectors and the magnetic vehicle speed sensor signal (-) pin of the other connector. Refer to the OEM troubleshooting and repair manual for detailed procedures.
