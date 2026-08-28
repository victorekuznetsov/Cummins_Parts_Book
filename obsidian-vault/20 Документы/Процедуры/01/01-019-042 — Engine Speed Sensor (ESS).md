---
aliases:
  - "Датчик частоты вращения двигателя (ESS)"
type: "Процедура"
doc: "01-019-042"
title_en: "Engine Speed Sensor (ESS)"
title_ru: "Датчик частоты вращения двигателя (ESS)"
modified: "2002-12-05"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 11
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-019-042.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-019-042.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Engine Speed Sensor (ESS)
**Датчик частоты вращения двигателя (ESS)**

> [!abstract] Процедура · `01-019-042`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2002-12-05
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-019-042.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-019-042.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Снятие

Отсоедините разъемы датчика скорости двигателя от электропроводки двигателя.

![[19a00245.png]]

Ослабьте локон.

Удалите датчик скорости двигателя из корпуса маховика.

![[19a00246.png]]

### Проверка при повторном использовании

Осмотрите датчик скорости двигателя на предмет обломков, трещин или сколов горшка, экструдированного горшка и повреждения от контакта с маховиком.

Если на датчике скорости двигателя есть мусор, очистите датчик.

Если датчик сколот, треснул, выдавил или повредил, замените датчик на новый.

![[19800369.png]]

### Установка

Убедитесь, что зубчатая передача выровнена с отверстием в корпусе маховика.

Установите датчик скорости двигателя в отверстие, пока он не коснется зуба зубчатой передачи.

> [!note] Примечание
> Если датчик скорости двигателя **не** включается с давлением пальца, проверьте обшивку маховика и резьбу датчика на предмет повреждения.

Выключите ESS 1/2 до 3/4 поворота **против часовой стрелки**.

![[19a00246.png]]

Затяните локон против корпуса маховика.

> [!tip] Момент затяжки
> 34-47 Н·м [25-35 футов-lb]

> [!note] Примечание
> Затягивание локона может повредить датчик.

![[19a00246.png]]

Подключите датчик к проводах датчика. Соедините разъёмы до фиксации.

![[19a00245.png]]

### Проверка сопротивления

Отделите четырехсторонний разъем. Поднимите вкладку и разберите разъем. Установите соединительный разъем с коротким испытательным щупом на разъем датчика.

> [!note] Примечание
> Цель установки соединительного разъема заключается в том, чтобы позволить электрическим проводам датчика мягко сгибаться для проверки поврежденных или частично сломанных резьб провода под изоляцией.

![[19a00245.png]]

Измерьте сопротивление от контакта А до контакта В для каждой катушки. Мультиметр **должен измерять от 700 до 2000 Ом. Если оба значения сопротивления соответствуют спецификациям, датчик **должен быть проверен на короткое замыкание на землю.

Если какая-либо из предыдущих проверок не срабатывает, замените датчик скорости двигателя.

![[19a00269.png]]

### Проверка на замыкание на массу

Измерьте сопротивление от контакта А до блока двигателя. Мультиметр **должен** показывать открытую схему (10 М Ом и более).

> [!note] Примечание
> Спецификация открытой цепи (10 м Ом) для датчика скорости двигателя выше, чем спецификация открытой цепи, используемая во всем руководстве из-за чувствительности датчика положения двигателя.

![[19a00270.png]]

Измерить сопротивление от контакта В до блока двигателя. Мультиметр **должен** показывать открытую схему (10 М Ом и более).

Если один из предыдущих измерительн не сработал, замените датчик скорости двигателя.

![[19a00271.png]]

### Проверка на замыкание между контактами

Измерьте сопротивление от датчика 1 оборота двигателя сигнала (контакт A) к датчику 2 оборота двигателя сигнала (контакт A) и датчика 2 оборота двигателя сигнала (контакт B).

Сопротивление должно показывать открытую схему (10 М Ом или более).

Измерение от датчика 1 оборота двигателя возврата (контакт B) к датчику 2 оборота двигателя сигнал (контакт A) и датчику 2 оборота двигателя сигнал (контакт B).

Если какая-либо из предыдущих проверок сопротивления не соответствует спецификациям, датчик выходит из строя. Замените датчик.

![[19a00272.png]]


> [!quote]- Original (English) · английский оригинал
> ### Remove
>
> Disconnect the engine speed sensor connectors from the engine harness.
>
> Loosen the locknut.
>
> Remove the engine speed sensor from the flywheel housing.
>
> ### Inspect for Reuse
>
> Inspect the engine speed sensor for debris, cracked, or chipped potting, extruded potting, and damage from contact with the flywheel.
>
> If there is debris on the engine speed sensor, clean the sensor.
>
> If the sensor is chipped, cracked, extruded, or damaged, replace the sensor with a new one.
>
> ### Install
>
> Make sure a gear tooth is aligned with the hole in the flywheel housing.
>
> Install the engine speed sensor into the hole until it touches the gear tooth.
>
> **Note · Примечание**
> If the engine speed sensor does **not** turn in with finger pressure, check the flywheel housing hold threads and sensor threads for damage.
>
> Turn the ESS out 1/2 to 3/4 of a turn **counterclockwise**.
>
> Tighten the locknut against the flywheel housing.
>
> **Момент затяжки · Torque Value**
> 34 to 47 n•m [25 to 35 ft-lb]
>
> **Note · Примечание**
> Overtightening the locknut can damage the sensor.
>
> Connect the sensor to the sensor harness. Push the connectors together until they lock.
>
> ### Resistance Check
>
> Separate the four-way connector. Lift the tab and pull the connector apart. Install a mating connector with short test leads on the sensor connector.
>
> **Note · Примечание**
> The purpose of installing a mating connector is to allow the electrical leads of the sensor to be softly flexed to check for damaged or partially broken wire strands under the insulation.
>
> Measure the resistance from pin A to pin B for each coil. The multimeter **must** measure between 700 and 2000 ohms. If both resistance values are within the specifications, the sensor **must** still be checked for short circuit to ground.
>
> If any of the preceding checks fail, replace the engine speed sensor.
>
> ### Check for Short Circuit to Ground
>
> Measure the resistance from pin A to the engine block. The multimeter **must** show an open circuit (10M ohms or more).
>
> **Note · Примечание**
> The open circuit specification (10M ohms) for the engine speed sensor is higher than the open circuit specification used throughout the manual due to the sensitivity of the engine position sensor.
>
> Measure the resistance from pin B to the engine block. The multimeter **must** show an open circuit (10M ohms or more).
>
> If either of the preceding tests fail, replace the engine speed sensor.
>
> ### Check for Short Circuit from Pin to Pin
>
> Measure the resistance from engine speed sensor 1 signal (pin A) to engine speed sensor 2 signal (pin A) and engine speed sensor 2 signal (pin B).
>
> The resistance must show an open circuit (10M ohms or more).
>
> Measure from engine speed sensor 1 return (pin B) to engine speed sensor 2 signal (pin A) and engine speed sensor 2 signal (pin B).
>
> If any of the previous resistance checks are not within specifications, the sensor has failed. Replace the sensor.
