---
aliases:
  - "Индуктивный датчик частоты вращения вала"
type: "Процедура"
doc: "82-019-312"
title_en: "Shaft Speed Sensor, Magnetic Pick Up"
title_ru: "Индуктивный датчик частоты вращения вала"
modified: "2002-06-03"
engines:
  - "41343322"
  - "41370103"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 12
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-312.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-019-312.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# Shaft Speed Sensor, Magnetic Pick Up
**Индуктивный датчик частоты вращения вала**

> [!abstract] Процедура · `82-019-312`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section 19 - Electronic Engine Controls
> **Даты:** изменён 2002-06-03
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-312.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-019-312.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Датчик скорости вала определяет скорость вала, подсчитывая зубья зубчатой передачи. Затем ECM вычисляет скорость вала на основе количества зубов на оборот. Вспомогательный управляющий может управлять заправкой двигателя для поддержания постоянной скорости вала.

![[19200261.png]]

Датчик скорости вала имеет две катушки. Одна катушка соединена с ECM, а другая катушка может быть соединена с каким-либо другим устройством транспортного средства.

> [!note] Примечание
> Дизайн датчика варьируется в зависимости от приложения. Посмотрите руководство производителя оборудования, чтобы понять, какой тип датчика скорости вала используется в данном месте.

> [!note] Примечание
> Некоторые приложения могут использовать только один разъем *.

![[19200262.png]]

### Снятие

Отсоедините жгут электропроводки двигателя от датчика скорости вала.

Ослабьте локон. Выключите датчик скорости вала из корпуса.

![[19900797.png]]

### Проверка при повторном использовании

Осмотрите кончик датчика скорости вала на предмет грязи, мусора или физического повреждения (треснутый горшок и т. Д.).

Очистите наконечник, если он грязный, или замените датчик скорости вала, если он поврежден.

![[19900798.png]]

### Установка

> [!warning] ОСТОРОЖНО
> Убедитесь, что зубчатая передача выровнена с отверстием в корпусе.

Установите датчик скорости вала в отверстие, пока он не коснется зуба зубчатой передачи.

> [!note] Примечание
> Если датчик скорости вала **не** включается с давлением пальца, проверьте резьбу обсадного отверстия и резьбу датчика на предмет грязи или повреждений.

![[19900799.png]]

Выключите датчик скорости вала от 1/2 до 3/4 поворота.

![[19900800.png]]

Затяните каштан на корпус.

> [!tip] Момент затяжки
> 47 Н·м [35 фунт-фут]

Установите оба разъема вместе, пока разъемы не «застегнутся» в положение. Разъемы могут быть взаимозаменяемы друг с другом без изменения производительности системы.

> [!note] Примечание
> Некоторые приложения могут использовать только один разъем *.

![[19900801.png]]

### Проверка сопротивления

Поднимите вкладку на разъемы и разберите их.

> [!note] Примечание
> При измерении значения сопротивления катушек датчика скорости вала используйте два гнездовых испытательных щупа, номер детали. 3822996. Это позволит мягко сгибать электрические провода датчика для проверки поврежденных или частично сломанных резьб провода под изоляцией.

![[19900802.png]]

Используйте мультиметр для измерения сопротивления между двумя штифтами каждого разъема на датчике скорости вала. Значение сопротивления одной катушки **должно быть от 750 до 1100 Ом. Значение сопротивления другой катушки** должно быть от 1100 до 1500 Ом (хотя значения сопротивления разные, катушки взаимозаменяемы).

Если сопротивление **не** правильно, замените датчик скорости вала. Если значение сопротивления правильное, датчик скорости вала **должен *** все еще проверяться на короткое замыкание на землю и короткое замыкание между катушками.

![[19900803.png]]

### Проверка на замыкание на массу

Измерьте сопротивление между контактом В одного из разъемов и блоком двигателя. Мультиметр **должен** показать обрыв цепи (100 кОм и более).

> [!note] Примечание
> Спецификация открытой цепи (100к Ом или более) для датчика скорости вала выше, чем спецификация открытой цепи, используемая во всем руководстве из-за чувствительности сигнала датчика скорости вала.

![[19200262.png]]

Измерьте сопротивление между контактом B другого разъема и блоком двигателя. Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Если схема не открыта (100к Ом или более) в любой из этих проверок, датчик скорости вала не работает.

Заменить датчик скорости вала.

![[19200263.png]]

**Проверка короткого замыкания между катушками**

Используйте мультиметр для измерения сопротивления между контактом B одного из разъемов и контактом B другого разъема. Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Если схема **не** открыта, замените датчик скорости вала.

![[19200264.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> The shaft speed sensor senses the speed of the shaft by counting gear teeth. The ECM then calculates the shaft speed based on the number of teeth per revolution. The auxiliary governor can control the engine fueling to maintain a constant shaft speed.
>
> The shaft speed sensor has two coils. One coil is connected to the ECM and the other coil may be connected to some other vehicle device.
>
> **Note · Примечание**
> Sensor design varies with the application. Refer to the equipment manufacturer's manual to understand which type of shaft speed sensor is being used in a given location.
>
> **Note · Примечание**
> Some applications may use **only** one connector.
>
> ### Remove
>
> Disconnect the engine harness from the shaft speed sensor.
>
> Loosen the locknut. Turn the shaft speed sensor out of the housing.
>
> ### Inspect for Reuse
>
> Inspect the tip of the shaft speed sensor for dirt, debris, or physical damage (cracked potting, and so forth).
>
> Clean the tip if it is dirty, or replace the shaft speed sensor if it is damaged.
>
> ### Install
>
> **CAUTION · Осторожно**
> Make sure a gear tooth is aligned with the hole in the housing.
>
> Install the shaft speed sensor into the hole until it touches the gear tooth.
>
> **Note · Примечание**
> If the shaft speed sensor does **not** turn in with finger pressure, check the housing hole threads and the sensor threads for dirt or damage.
>
> Turn the shaft speed sensor out 1/2 to 3/4 of a turn.
>
> Tighten the locknut against the housing.
>
> **Момент затяжки · Torque Value**
> 47 n•m [35 ft-lb]
>
> Install both of the connectors together until connectors "snap" into position. The connectors can be interchanged with each other without changing the performance of the system.
>
> **Note · Примечание**
> Some applications may use **only** one connector.
>
> ### Resistance Check
>
> Lift the tab on the connectors and pull them apart.
>
> **Note · Примечание**
> When measuring the resistance value of the shaft speed sensor coils, use two female test leads, Part No. 3822996. This will allow the electrical leads of the sensor to be softly flexed to check for damaged or partially broken wire strands under the insulation.
>
> Use a multimeter to measure the resistance between the two pins of each connector on the shaft speed sensor. The resistance value of one coil **must** be 750 to 1100 ohms. The resistance value of the other coil **must** be 1100 to 1500 ohms (although the resistance values are different, the coils are interchangeable).
>
> If the resistance is **not** correct, replace the shaft speed sensor. If the resistance value is correct, the shaft speed sensor **must** still be checked for a short circuit to ground and a short circuit between coils.
>
> ### Check for Short Circuit to Ground
>
> Measure the resistance between pin B of one of the connectors and the engine block. The multimeter **must** show an open circuit (100k ohms or more).
>
> **Note · Примечание**
> The open circuit specification (100k ohms or more) for the shaft speed sensor is higher than the open circuit specification used throughout the manual due to the sensitivity of the shaft speed sensor signal.
>
> Measure the resistance between pin B of the other connector and the engine block. The multimeter **must** show an open circuit (100k ohms or more).
>
> If the circuit is **not** open (100k ohms or more) in either of these checks, the shaft speed sensor has failed.
>
> Replace the shaft speed sensor.
>
> **Check for Short Circuit between Coils**
>
> Use a multimeter to measure the resistance between pin B of one of the connectors and pin B of the other connector. The multimeter **must** show an open circuit (100k ohms or more).
>
> If the circuit is **not** open, replace the shaft speed sensor.
