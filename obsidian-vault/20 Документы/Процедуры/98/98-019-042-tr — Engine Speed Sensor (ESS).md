---
aliases:
  - "Датчик частоты вращения двигателя (ESS)"
type: "Процедура"
doc: "98-019-042-tr"
title_en: "Engine Speed Sensor (ESS)"
title_ru: "Датчик частоты вращения двигателя (ESS)"
modified: "2009-01-12"
engines:
  - "37269910"
  - "37280605"
families:
  - "K19"
manuals:
  - "3666070"
figures: 12
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-019-042-tr.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-019-042-tr.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K19"
  - "группа/98"
  - "перевод/машинный"
---

# Engine Speed Sensor (ESS)
**Датчик частоты вращения двигателя (ESS)**

> [!abstract] Процедура · `98-019-042-tr`
> **Двигатели:** [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]]
> **Семейство:** K19
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2009-01-12
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-019-042-tr.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-019-042-tr.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Датчик скорости двигателя расположен в корпусе маховика.

![[19801626.png]]

Если OEM имеет установленный датчик с одним выходом и он имеет резьбу 3/4 x 16, удалите датчик с одним выходом из корпуса маховика.

![[19200417.png]]

### Снятие

Отсоедините разъемы датчика скорости двигателя от основной проводов двигателя.

Ослабьте локон.

Удалите датчик скорости двигателя из корпуса маховика.

![[19801632.png]]

### Проверка при повторном использовании

Осмотрите датчик скорости двигателя на предмет обломков, трещин или сколов горшка, экструдированного горшка и повреждения от контакта с кольцевой передачей.

Если на датчике скорости двигателя есть мусор, очистите датчик.

Если датчик сколот, треснул, выдавливался или повреждался, замените датчик.

![[19800369.png]]

### Установка

Убедитесь, что зубчатая передача выровнена с отверстием в корпусе маховика.

Установите датчик скорости двигателя в отверстие, пока он не коснется зуба зубчатой передачи.

> [!note] Примечание
> Если датчик скорости двигателя **не** включается под давлением пальца, проверьте резьбу резьбы корпуса маховика и резьбу датчика на предмет повреждения.

![[19801633.png]]

Выключите датчик скорости двигателя от 1/2 до 3/4 поворота **против часовой стрелки**.

![[19801634.png]]

> [!warning] ОСТОРОЖНО
> Затягивание локона может повредить датчик.

Затяните локон против корпуса маховика.

> [!tip] Момент затяжки
> 31 Н·м [23 фунт-фут]

Установите оба разъема. Убедитесь, что они заперты на месте.

Разъемы могут быть взаимозаменяемы друг с другом без изменения производительности системы.

![[19801635.png]]

### Проверка сопротивления

Разделите два разъема. Поднимите вкладку на разъемы и разберите их.

> [!note] Примечание
> При измерении значений сопротивления катушек датчика скорости двигателя подключите спаривающийся разъем с короткими свинцовыми удлинителями. Это позволит мягко сгибать электрические провода датчика для проверки поврежденных или частично сломанных резьб провода под изоляцией.

![[19801627.png]]

Используйте мультиметр для измерения сопротивления между двумя штифтами каждого разъема на датчике скорости двигателя. Значение сопротивления одной катушки **должно быть от 750 до 1100 Ом. Значение сопротивления другой катушки **должно быть от 1100 до 1500 Ом. Если сопротивление **не** правильно, замените датчик скорости двигателя.

Если значение сопротивления правильное, датчик скорости двигателя **должен **все еще проверяться на короткое замыкание на землю и короткое замыкание между катушками.

Значения сопротивления катушке измеряются при 25°C \[77°F\].

![[19801628.png]]

### Проверка на замыкание на массу

Для измерения сопротивления между контактом В и заземлением блока двигателя:

- Прикрепить один мультиметр к соединительному разъёму датчика. Прикосновение к другому мультиметру приводит к заземлению блока двигателя.
- Измерьте сопротивление. Мультиметр **должен **показывать 100k Ом или больше, что является открытой схемой.

Если схема не открыта, датчик скорости двигателя вышел из строя.

Замените датчик скорости двигателя.

![[19801629.png]]

Для измерения сопротивления между контактом В другого разъема и блоком двигателя заземляется.

- Прикрепить один мультиметр к другому разъёму датчика спаривания. Прикоснитесь к другому мультиметру, который приведет к заземлению блока двигателя.
- Измерьте сопротивление. Мультиметр **должен **показывать 100k Ом или больше.

Если схема не открыта в любой из этих проверок, датчик скорости двигателя не работает.

Замените датчик скорости двигателя.

![[19801630.png]]

### Проверка на замыкание между контактами

Чтобы проверить короткое замыкание между катушками датчика:

- Прикрепите один мультиметровый свинец к контакту B любого соединительного разъёма датчика.
- Прикрепление другого мультиметра приводит к контакту B другого соединительного разъёма датчика.
- Измерьте сопротивление.

Мультиметр **должен **показывать 100k Ом или больше.

Если схема **не** открыта, замените датчик скорости двигателя.

Если значения верны для всех проверок датчика скорости двигателя, датчик хорош.

![[19801631.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> The engine speed sensor is located in the flywheel housing.
>
> If the OEM has a single-output sensor installed and it is 3/4 x 16 thread, remove the single-output sensor from the flywheel housing.
>
> ### Remove
>
> Disconnect the engine speed sensor connectors from the main engine harness.
>
> Loosen the locknut.
>
> Remove the engine speed sensor from the flywheel housing.
>
> ### Inspect for Reuse
>
> Inspect the engine speed sensor for debris, cracked or chipped potting, extruded potting, and damage from contact with the ring gear.
>
> If there is debris on the engine speed sensor, clean the sensor.
>
> If the sensor is chipped, cracked, extruded, or damaged, replace the sensor.
>
> ### Install
>
> Make sure a gear tooth is aligned with the hole in the flywheel housing.
>
> Install the engine speed sensor into the hole until it touches the gear tooth.
>
> **Note · Примечание**
> If the engine speed sensor does **not** turn in with finger-pressure, check the flywheel housing hole threads and sensor threads for damage.
>
> Turn the engine speed sensor out 1/2 to 3/4 of a turn **counterclockwise**.
>
> **CAUTION · Осторожно**
> Overtightening the locknut can damage the sensor.
>
> Tighten the locknut against the flywheel housing.
>
> **Момент затяжки · Torque Value**
> 31 n•m [23 ft-lb]
>
> Install both of the connectors. Make sure they lock into place.
>
> The connectors can be interchanged with each other without changing the performance of the system.
>
> ### Resistance Check
>
> Separate the two connectors. Lift the tab on the connectors and pull them apart.
>
> **Note · Примечание**
> When measuring the resistance values of the engine speed sensor coils, connect a mating connector with short lead extensions. This will allow the electrical leads of the sensor to be softly flexed to check for damaged or partially broken wire strands under the insulation.
>
> Use a multimeter to measure the resistance between the two pins of each connector on the engine speed sensor. The resistance value of one coil **must** be between 750 and 1100 ohms. The resistance value of the other coil **must** be 1100 to 1500 ohms. If the resistance is **not** correct, replace the engine speed sensor.
>
> If the resistance value is correct, the engine speed sensor **must** still be checked for a short circuit to ground and a short circuit between coils.
>
> The coil resistance values are measured at 25°C \[77°F\].
>
> ### Check for Short Circuit to Ground
>
> To measure the resistance between pin B and the engine block ground:
>
> - Attach one multimeter lead to the mating sensor connector lead. Touch the other multimeter lead to the engine block ground.
> - Measure the resistance. The multimeter **must** show 100k ohms or greater, which is an open circuit.
>
> If the circuit is **not** open, the engine speed sensor has failed.
>
> Replace the engine speed sensor.
>
> To measure the resistance between pin B of the other connector and engine block ground.
>
> - Attach one multimeter lead to the other mating sensor connector lead. Touch the other multimeter lead to engine block ground.
> - Measure the resistance. The multimeter **must** show 100k ohms or greater.
>
> If the circuit is **not** open in either of these checks, the engine speed sensor has failed.
>
> Replace the engine speed sensor.
>
> ### Check for Short Circuit from Pin to Pin
>
> To check for a short circuit between the sensor coils:
>
> - Attach one multimeter lead to pin B of either mating sensor connector lead.
> - Attach the other multimeter lead to pin B of the other mating sensor connector lead.
> - Measure the resistance.
>
> The multimeter **must** show 100k ohms or greater.
>
> If the circuit is **not** open, replace the engine speed sensor.
>
> If the values are correct for all engine speed sensor checks, the sensor is good.
