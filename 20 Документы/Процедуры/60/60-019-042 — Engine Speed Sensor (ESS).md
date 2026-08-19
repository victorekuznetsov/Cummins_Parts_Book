---
aliases:
  - "Датчик частоты вращения двигателя (ESS)"
type: "Процедура"
doc: "60-019-042"
title_en: "Engine Speed Sensor (ESS)"
title_ru: "Датчик частоты вращения двигателя (ESS)"
modified: "2009-06-09"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021674"
figures: 12
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-019-042.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-019-042.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
  - "перевод/машинный"
---

# Engine Speed Sensor (ESS)
**Датчик частоты вращения двигателя (ESS)**

> [!abstract] Процедура · `60-019-042`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section 19 — Electronic Engine Controls — Group 19
> **Даты:** изменён 2009-06-09
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-019-042.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-019-042.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Снятие

Отсоедините разъемы датчика скорости двигателя от электропроводки двигателя.

![[19a00245.png]]

Уберите болты.

Удалите датчик скорости двигателя из корпуса маховика.

![[19a00246.png]]

### Очистка и проверка при повторном использовании

Очистите любой мусор на датчике скорости двигателя.

Осмотрите датчик скорости двигателя на предмет обломков, трещин или сколов, экструдированного горшка и повреждения от контакта с маховиком.

Если датчик скорости двигателя сколот, треснул, выдавил или иным образом повредил, датчик ** должен быть заменен.

![[19800369.png]]

### Установка

Убедитесь, что датчик скорости двигателя находится непосредственно над зубцом кольцевой передачи маховика.

Установите датчик скорости двигателя, поворачивая его ** по часовой стрелке **, пока он не свяжется с маховиком.

Выключите датчик, повернув его ** против часовой стрелки** на 180 градусов.

Продолжайте поворачивать датчик скорости двигателя ** против часовой стрелки ** до выравнивания отверстия замка.

Установите замки и затяните.

> [!tip] Момент затяжки
> 7 Н·м [62 фунт-дюйм]

![[00a00106.png]]

> [!warning] ОСТОРОЖНО
> Используйте только смазку LubriplateTM DS-ES, номер детали 3822934, рекомендованную Cummins Inc. Другие смазочные материалы, такие как моторное масло или смазка, в разъемах могут вызвать повреждение ECM, плохую производительность двигателя или преждевременный контактный износ разъема.

Нанесите небольшое количество смазки на соединительные терминалы. Перед установкой заполните всю полость разъема смазкой.

![[cel29.png]]

Подключите датчик к проводах датчика. Соедините разъёмы до фиксации.

![[19a00245.png]]

### Проверка сопротивления

Отделите трехсторонний разъем. Поднимите вкладку и разберите разъем. Установите соединительный разъем с коротким испытательным щупом на разъем датчика.

> [!note] Примечание
> Цель установки соединительного разъема заключается в том, чтобы позволить электрическим проводам датчика мягко сгибаться для проверки поврежденных или частично сломанных резьб провода под изоляцией.

![[19a00245.png]]

Используйте мультиметр для измерения сопротивления от контакта C до контакта B.

Мультиметр ** должен ** показывать от 1000 до 2000 Ом.

![[19a00268.png]]

Используйте мультиметр для измерения сопротивления от контакта А до контакта В.

Мультиметр ** должен ** показывать от 1000 до 2000 Ом. Если оба значения сопротивления соответствуют спецификациям, датчик ** должен быть проверен на короткое замыкание на землю.

Если какая-либо из проверок сопротивления ** не** в пределах спецификаций, замените датчик скорости двигателя.

![[19a00269.png]]

### Проверка на замыкание на массу

Измерьте сопротивление от контакта А до заземления блока двигателя. Мультиметр ** должен** показывать открытую схему (10 М Ом и более).

> [!note] Примечание
> Спецификация открытой цепи (10 м Ом) для датчика скорости двигателя выше, чем спецификация открытой цепи, используемая во всем руководстве из-за чувствительности датчика скорости двигателя.

![[19a00270.png]]

Измерьте сопротивление от контакта C до заземления блока двигателя. Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Если какая-либо из проверок сопротивления ** не** в пределах спецификаций, замените датчик скорости двигателя.

![[19a00271.png]]

### Проверка на замыкание между контактами

Измерить сопротивление от контакта А до контакта С. Мультиметр **должен** показать обрыв цепи (100 кОм и более). Если какая-либо из проверок сопротивления ** не** в пределах спецификаций, датчик поврежден.

Замените датчик скорости двигателя.

> [!missing]- Иллюстрация `19a00272.png` не извлечена — смотрите PDF-оригинал документа


> [!quote]- Original (English) · английский оригинал
> ### Remove
>
> Disconnect the engine speed sensor connectors from the engine harness.
>
> Loosen the capscrew.
>
> Remove the engine speed sensor from the flywheel housing.
>
> ### Clean and Inspect for Reuse
>
> Clean any debris on the engine speed sensor.
>
> Inspect the engine speed sensor for debris, cracks, or chipped potting, extruded potting, and damage from contact with the flywheel.
>
> If the engine speed sensor is chipped, cracked, extruded, or otherwise damaged, the sensor **must** be replaced.
>
> ### Install
>
> Check that the engine speed sensor is directly above a flywheel ring gear tooth.
>
> Install the engine speed sensor by turning it **clockwise** until it contacts the flywheel.
>
> Back out the sensor by turning it **counterclockwise** 180 degrees.
>
> Continue turning the engine speed sensor **counterclockwise** until the lock hole is aligned.
>
> Install the lock capscrew and tighten.
>
> **Момент затяжки · Torque Value**
> 7 n•m [62 in-lb]
>
> **CAUTION · Осторожно**
> Only use lubricant Lubriplate™ DS-ES, Part Number 3822934, recommended by Cummins Inc. Other lubricants, such as lubricating oil or grease, in the connectors can cause ECM damage, poor engine performance, or premature connector pin wear.
>
> Apply a small amount of lubricant to the connector terminals. Before installing, fill the entire connector cavity with lubricant.
>
> Connect the sensor to the sensor harness. Push the connectors together until they lock.
>
> ### Resistance Check
>
> Separate the three-way connector. Lift the tab and pull the connector apart. Install a mating connector with short test leads on the sensor connector.
>
> **Note · Примечание**
> The purpose of installing a mating connector is to allow the electrical leads of the sensor to be softly flexed to check for damaged or partially broken wire strands under the insulation.
>
> Use a multimeter to measure the resistance from pin C to pin B.
>
> The multimeter **must** show between 1000 and 2000 ohms.
>
> Use a multimeter to measure the resistance from pin A to pin B.
>
> The multimeter **must** show between 1000 and 2000 ohms. If both resistance values are within the specifications, the sensor **must** still be checked for short circuit to ground.
>
> If any of the resistance checks are **not** within specifications, replace the engine speed sensor.
>
> ### Check for Short Circuit to Ground
>
> Measure the resistance from pin A to the engine block ground. The multimeter **must** show an open circuit (10M ohms or more).
>
> **Note · Примечание**
> The open circuit specification (10M ohms) for the engine speed sensor is higher than the open circuit specification used throughout the manual due to the sensitivity of the engine speed sensor.
>
> Measure the resistance from pin C to the engine block ground. The multimeter **must** show an open circuit (100k ohms or more).
>
> If any of the resistance checks are **not** within specifications, replace the engine speed sensor.
>
> ### Check for Short Circuit from Pin to Pin
>
> Measure the resistance from pin A to pin C. The multimeter **must** show an open circuit (100k ohms or more). If any of the resistance checks are **not** within specifications, the sensor is damaged.
>
> Replace the engine speed sensor.
