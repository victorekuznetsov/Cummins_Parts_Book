---
aliases:
  - "Датчик частоты вращения двигателя (ESS)"
type: "Процедура"
doc: "07-019-042"
title_en: "Engine Speed Sensor (ESS)"
title_ru: "Датчик частоты вращения двигателя (ESS)"
modified: "2003-12-09"
engines:
  - "93058669"
families:
  - "C8.3 · 6C8.3"
manuals:
  - "4021442"
figures: 10
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-019-042.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/07-019-042.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "группа/07"
  - "перевод/машинный"
---

# Engine Speed Sensor (ESS)
**Датчик частоты вращения двигателя (ESS)**

> [!abstract] Процедура · `07-019-042`
> **Двигатели:** [[93058669 — 6C8.3 CPL 3105|93058669]]
> **Семейство:** C8.3 · 6C8.3
> **Входит в руководства:** [[4021442 — C8.3 Marine Electronic Control System Troubleshooting and Repair Manual|4021442]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-12-09
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-019-042.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/07-019-042.pdf)

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

Если датчик сколот, треснул, выдавил или повредил, замените его на новый.

![[19800369.png]]

### Установка

Убедитесь, что датчик скорости двигателя находится непосредственно над зубцом кольцевой передачи маховика.

Установите датчик скорости двигателя, пока он не свяжется с маховиком.

Отключите датчик, пока отверстие замка не выровняется.

Установите замки и затяните.

> [!tip] Момент затяжки
> 7 Н·м [62 фунт-дюйм]

![[00a00106.png]]

Подключите датчик к проводах датчика.

Соедините разъёмы до фиксации.

![[19a00245.png]]

### Проверка сопротивления

Отсоедините разъем датчика от жгута проводов двигателя.

Поднимите вкладку и разберите разъем.

Установите соединительный разъем с коротким испытательным щупом на разъем датчика.

> [!note] Примечание
> Цель установки соединительного разъема заключается в том, чтобы позволить электрическим проводам датчика мягко сгибаться для проверки поврежденных или частично сломанных резьб провода под изоляцией.

![[19a00245.png]]

Используйте мультиметр для измерения сопротивления от первичного штифта сигнала скорости двигателя до возврата первичного штифта скорости двигателя.

Измерьте сопротивление от первичного штифта двигателя +5-VDC до обратного контакта с оборотом двигателя.

Мультиметр ** должен измерять от 1000 до 2000 Ом.

Если оба значения сопротивления находятся в пределах спецификаций, датчик ** должен быть проверен на короткое замыкание на землю.

Если какая-либо из предыдущих проверок не срабатывает, замените датчик скорости двигателя.

![[19901401.png]]

### Проверка на замыкание на массу

Измерьте сопротивление от первичного штифта двигателя +5-VDC до блока двигателя.

Мультиметр ** должен** показывать открытую схему (10 М Ом и более).

> [!note] Примечание
> Спецификация открытой цепи (10 м Ом) для датчика скорости двигателя выше, чем спецификация открытой цепи, используемая во всем руководстве из-за чувствительности датчика скорости двигателя.

![[19901403.png]]

Измерьте сопротивление от первичного штифта сигнала скорости двигателя к блоку двигателя.

Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Если одна из предыдущих проверок не сработала, замените датчик скорости двигателя.

![[19901404.png]]

### Проверка на замыкание между контактами

Измерьте сопротивление от первичного штифта двигателя +5-VDC до обратного контакта с оборотом двигателя.

Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Если какая-либо из предыдущих проверок сопротивления ** не** в пределах спецификаций, датчик не сработал.

Замените датчик.

> [!missing]- Иллюстрация `19901405.png` не извлечена — смотрите PDF-оригинал документа


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
> If the sensor is chipped, cracked, extruded, or damaged, replace it with a new one.
>
> ### Install
>
> Check that the engine speed sensor is directly above a flywheel ring gear tooth.
>
> Install the engine speed sensor until it contacts the flywheel.
>
> Back the sensor off until the lock hole is aligned.
>
> Install the lock capscrew and tighten.
>
> **Момент затяжки · Torque Value**
> 7 n•m [62 in-lb]
>
> Connect the sensor to the sensor harness.
>
> Push the connectors together until they lock.
>
> ### Resistance Check
>
> Disconnect the sensor connector from the engine harness.
>
> Lift the tab and pull the connector apart.
>
> Install a mating connector with short test leads on the sensor connector.
>
> **Note · Примечание**
> The purpose of installing a mating connector is to allow the electrical leads of the sensor to be softly flexed to check for damaged or partially broken wire strands under the insulation.
>
> Use a multimeter to measure the resistance from the engine speed signal primary pin to the engine speed return primary pin.
>
> Measure the resistance from the engine speed +5-VDC primary pin to the engine speed return pin.
>
> The multimeter **must** measure between 1000 and 2000 ohms.
>
> If both resistance values are within specifications, the sensor **must** still be checked for short circuit to ground.
>
> If any of the preceding checks fail, replace the engine speed sensor.
>
> ### Check for Short Circuit to Ground
>
> Measure the resistance from the engine speed +5-VDC primary pin to the engine block.
>
> The multimeter **must** show an open circuit (10M ohms or more).
>
> **Note · Примечание**
> The open circuit specification (10M ohms) for the engine speed sensor is higher than the open circuit specification used throughout the manual due to the sensitivity of the engine speed sensor.
>
> Measure the resistance from the engine speed signal primary pin to the engine block.
>
> The multimeter **must** show an open circuit (100k ohms or more).
>
> If either of the preceding checks fail, replace the engine speed sensor.
>
> ### Check for Short Circuit from Pin to Pin
>
> Measure the resistance from the engine speed +5-VDC primary pin to the engine speed return pin.
>
> The multimeter **must** show an open circuit (100k ohms or more).
>
> If any of the previous resistance checks are **not** within specifications, the sensor has failed.
>
> Replace the sensor.
