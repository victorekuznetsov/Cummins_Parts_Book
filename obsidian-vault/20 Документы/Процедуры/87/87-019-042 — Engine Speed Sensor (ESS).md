---
aliases:
  - "Датчик частоты вращения двигателя (ESS)"
type: "Процедура"
doc: "87-019-042"
title_en: "Engine Speed Sensor (ESS)"
title_ru: "Датчик частоты вращения двигателя (ESS)"
modified: "2003-02-10"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666214"
figures: 12
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-019-042.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-019-042.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
  - "перевод/машинный"
---

# Engine Speed Sensor (ESS)
**Датчик частоты вращения двигателя (ESS)**

> [!abstract] Процедура · `87-019-042`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-02-10
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-019-042.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-019-042.pdf)

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

### Проверка при повторном использовании

Осмотрите датчик скорости двигателя на предмет обломков, трещин или сколов горшка, экструдированного горшка и повреждения от контакта с маховиком.

Если на датчике скорости двигателя есть мусор, очистите датчик.

Если датчик сколот, треснул, выдавил или повредил, замените датчик на новый.

![[19800369.png]]

### Установка

> [!note] Примечание
> Убедитесь, что датчик скорости двигателя находится непосредственно над зубцом кольцевой передачи маховика.

Установите датчик скорости двигателя, пока он не свяжется с маховиком. Отключите датчик, пока отверстие замка не выровняется.

Установите замки и затяните.

> [!tip] Момент затяжки
> 7 Н·м [62 фунт-дюйм]

![[00a00106.png]]

> [!warning] ОСТОРОЖНО
> Используйте только рекомендованную Cummins смазку DS-ES, номер детали 3822934. Другие смазочные материалы, такие как моторное масло или смазка, в разъемах могут вызвать повреждение ECM, плохую производительность двигателя или преждевременный контактный износ разъема.

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

Измерить сопротивление от контакта А до контакта В. Мультиметр ** должен измерять от 1000 до 2000 Ом. Если оба значения сопротивления соответствуют спецификациям, датчик ** должен быть проверен на короткое замыкание на землю.

Если какая-либо из предыдущих проверок не срабатывает, замените датчик скорости двигателя.

![[19a00269.png]]

### Проверка на замыкание на массу

Измерьте сопротивление от контакта А до блока двигателя. Мультиметр ** должен** показывать открытую схему (10 М Ом и более).

> [!note] Примечание
> Спецификация открытой цепи (10 м Ом) для датчика скорости двигателя выше, чем спецификация открытой цепи, используемая во всем руководстве из-за чувствительности датчика скорости двигателя.

![[19a00270.png]]

Измерить сопротивление от контакта C до блока двигателя. Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Если один из предыдущих измерительн не сработал, замените датчик скорости двигателя.

![[19a00271.png]]

### Проверка на замыкание между контактами

Измерить сопротивление от контакта А до контакта С. Мультиметр **должен** показать обрыв цепи (100 кОм и более). Если какая-либо из предыдущих проверок сопротивления ** не** в пределах спецификаций, датчик не сработал.

Замените датчик.

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
> ### Inspect for Reuse
>
> Inspect the engine speed sensor for debris, cracked or chipped potting, extruded potting, and damage from contact with the flywheel.
>
> If there is debris on the engine speed sensor, clean the sensor.
>
> If the sensor is chipped, cracked, extruded, or damaged, replace the sensor with a new one.
>
> ### Install
>
> **Note · Примечание**
> Check that the engine speed sensor is directly above a flywheel ring gear tooth.
>
> Install the engine speed sensor until it contacts the flywheel. Back the sensor off until the lock hole is aligned.
>
> Install the lock capscrew and tighten.
>
> **Момент затяжки · Torque Value**
> 7 n•m [62 in-lb]
>
> **CAUTION · Осторожно**
> Use only Cummins-recommended lubricant DS-ES, Part Number 3822934. Other lubricants, such as lubricating oil or grease, in the connectors can cause ECM damage, poor engine performance, or premature connector pin wear.
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
> Measure the resistance from pin A to pin B. The multimeter **must** measure between 1000 and 2000 ohms. If both resistance values are within the specifications, the sensor **must** still be checked for short circuit to ground.
>
> If any of the preceding checks fail, replace the engine speed sensor.
>
> ### Check for Short Circuit to Ground
>
> Measure the resistance from pin A to the engine block. The multimeter **must** show an open circuit (10M ohms or more).
>
> **Note · Примечание**
> The open circuit specification (10M ohms) for the engine speed sensor is higher than the open circuit specification used throughout the manual due to the sensitivity of the engine speed sensor.
>
> Measure the resistance from pin C to the engine block. The multimeter **must** show an open circuit (100k ohms or more).
>
> If either of the preceding tests fails, replace the engine speed sensor.
>
> ### Check for Short Circuit from Pin to Pin
>
> Measure the resistance from pin A to pin C. The multimeter **must** show an open circuit (100k ohms or more). If any of the previous resistance checks are **not** within specifications, the sensor has failed.
>
> Replace the sensor.
