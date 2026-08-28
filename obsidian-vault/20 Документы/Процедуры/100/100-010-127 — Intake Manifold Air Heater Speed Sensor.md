---
aliases:
  - "Датчик частоты вращения подогревателя впускного воздуха"
type: "Процедура"
doc: "100-010-127"
title_en: "Intake Manifold Air Heater Speed Sensor"
title_ru: "Датчик частоты вращения подогревателя впускного воздуха"
modified: "2003-08-26"
engines:
  - "93047320"
  - "93058669"
  - "93087701"
families:
  - "6B5.9"
  - "C8.3 · 6C8.3"
manuals:
  - "3666003"
  - "3666087"
figures: 10
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/100/100-010-127.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/100-010-127.pdf"
tags:
  - "документ/процедура"
  - "двигатель/6B5.9"
  - "двигатель/C8.3"
  - "группа/100"
  - "перевод/машинный"
---

# Intake Manifold Air Heater Speed Sensor
**Датчик частоты вращения подогревателя впускного воздуха**

> [!abstract] Процедура · `100-010-127`
> **Двигатели:** [[93047320 — 6B5.9 CPL 3111|93047320]], [[93058669 — 6C8.3 CPL 3105|93058669]], [[93087701 — 6C8.3 CPL 3105|93087701]]
> **Семейство:** 6B5.9, C8.3 · 6C8.3
> **Входит в руководства:** [[3666003 — C Troubleshooting and Repair Manual|3666003]], [[3666087 — B3.9, B4.5, B4.5 RGT, and B5.9 Service Manual|3666087]]
> **Секции:** Section 10 - Air Intake System - Group 10
> **Даты:** изменён 2003-08-26
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/100/100-010-127.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/100-010-127.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Первичная проверка

От датчика поступают два соединения, одно для тахометра двигателя, а другое для системы воздухозаборника.

1. Белый и зеленый: Для движка с помощью электропроводки
2. Красный и черный: для управления воздухом нагревателя электропроводки ремня.

Проверьте, чтобы убедиться, что они подключены.

![[10900311.png]]

### Снятие

Отсоедините датчик скорости двигателя от электропроводки двигателя.

![[10900312.png]]

Удалите датчик из корпуса маховика.

![[10900313.png]]

### Проверка при повторном использовании

Осмотрите датчик скорости двигателя на предмет обломков, трещин или сколов горшка и повреждения от контакта с маховиком.

При необходимости очистите или замените датчик скорости двигателя.

![[19800369.png]]

### Проверка

1. Короткая трасса к земле: Измерьте сопротивление каждого разъёма (Pin A или B) обеих цепей к земле (сенсорному корпусу) с помощью мультиметра. Мультиметр **должен** показать обрыв цепи (100 кОм и более). Если измеряется менее 100k Ом, то датчику необходимо сделать короткое замыкание. Замените датчик.

![[10900314.png]]

1. Короткая кольцевая развязка между катушками: Проверьте сопротивление между разъемами (Pin A - Pin A и Pin B - Pin B) с помощью мультиметра. Мультиметр **должен** показать обрыв цепи (100 кОм и более). Если измеряется менее 100k Ом, в датчике есть короткое замыкание. Замените датчик.

![[10900315.png]]

1. Сопротивление катушке: Проверьте сопротивление между контактами каждого разъема (Pin A - Pin B).

| Спецификация сопротивления |  |
|---|---|
| Первая катушка | 750-1100 Ом |
| Вторая катушка | 1100-1500 Ом |

![[10900316.png]]

### Установка

Используйте поворотную передачу двигателя, номер детали 3377371, чтобы вращать коленчатый вал так, чтобы зубчатая зубчатая передача находилась в центре отверстия для датчика скорости двигателя.

![[10900317.png]]

Вставьте датчик скорости двигателя и поверните его до тех пор, пока конец не коснется зубца кольцевой передачи.

Отключите полуоборот и затяните локон, удерживая датчик положения двигателя.

> [!tip] Момент затяжки
> 34-47 Н·м [25-35 футов-lb]

Затяжка повредит датчик.

![[10900318.png]]

Установите датчик скорости двигателя сосудом с красным и черным щупом на впускной нагреватель управления проводкой жгута.

Белая и зеленая проволочная пробка соединена с проводной упряжкой для датчика тахометра.

1. Белый и зеленый: Для движка с помощью электропроводки
2. Красный и черный: для управления воздухом нагревателя электропроводки ремня.

![[10900311.png]]


> [!quote]- Original (English) · английский оригинал
> ### Initial Check
>
> There are two connections coming from the sensor, one is for the engine tachometer and the other is for the air intake heater system.
>
> 1. White and green: to engine wiring harness
> 2. Red and black: to air heater control harness.
>
> Check to verify they are connected.
>
> ### Remove
>
> Disconnect the engine speed sensor from the engine wiring harness.
>
> Remove the sensor from the flywheel housing.
>
> ### Inspect for Reuse
>
> Inspect the engine speed sensor for debris, cracked or chipped potting, and damage from contact with the flywheel.
>
> Clean or replace the engine speed sensor if necessary.
>
> ### Test
>
> 1. Short Circuit to Ground: Measure the resistance of each connector (Pin A or B) of both circuits to ground (sensor body) with a multimeter. The multimeter **must** show an open circuit (100k ohms or more). If fewer than 100k ohms are measured, there is a short circuit to the sensor. Replace the sensor.
>
> 1. Short Circuit Between Coils: Check the resistance between connectors (Pin A to Pin A and Pin B to Pin B) with a multimeter. The multimeter **must** show an open circuit (100k ohms or more). If fewer than 100k ohms are measured, there is a short circuit in the sensor. Replace the sensor.
>
> 1. Coil Resistance: Check the resistance between the pins of each connector (Pin A to Pin B).
>
> | Resistance Specification |  |
> |---|---|
> | First coil | 750 to 1100 ohms |
> | Second coil | 1100 to 1500 ohms |
>
> ### Install
>
> Use a barring gear, Part Number 3377371, to rotate the crankshaft so that a ring gear tooth is at the center of the hole for the engine speed sensor.
>
> Insert the engine speed sensor and turn it until the end touches the ring gear tooth.
>
> Back off a half turn and tighten the locknut while holding the engine position sensor.
>
> **Момент затяжки · Torque Value**
> 34 to 47 n•m [25 to 35 ft-lb]
>
> Overtightening will damage the sensor.
>
> Install the engine speed sensor receptacle with red and black leads on the air intake heater control harness plug.
>
> The white and green wire plug is connected to the wiring harness for the tachometer sensing.
>
> 1. White and green: to engine wiring harness
> 2. Red and black: to air heater control harness.
