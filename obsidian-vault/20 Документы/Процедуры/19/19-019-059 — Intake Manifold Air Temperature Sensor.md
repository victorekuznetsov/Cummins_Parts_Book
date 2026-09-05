---
aliases:
  - "Датчик температуры воздуха во впускном коллекторе"
type: "Процедура"
doc: "19-019-059"
title_en: "Intake Manifold Air Temperature Sensor"
title_ru: "Датчик температуры воздуха во впускном коллекторе"
modified: "2002-08-20"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
  - "85017333"
families:
  - "QSK23"
  - "QSK60"
manuals:
  - "3666113"
figures: 6
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-019-059.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-019-059.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
  - "перевод/машинный"
---

# Intake Manifold Air Temperature Sensor
**Датчик температуры воздуха во впускном коллекторе**

> [!abstract] Процедура · `19-019-059`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2002-08-20
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-019-059.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-019-059.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Снятие

Поднимите на запирающую вкладку и разберите электрические разъемы.

Удалите датчик из двигателя.

![[19400434.png]]

### Установка

Убедитесь, что новый датчик имеет кольцо вокруг поверхности, где он уплотняет блок двигателя.

Установите датчик в блок двигателя.

> [!tip] Момент затяжки
> 14 Н·м [124 фунт-дюйм]

![[19400435.png]]

Скрепляйте разъёмы, пока они не заблокируются.

![[19400436.png]]

### Проверка сопротивления

Поднимите на запирающую вкладку и разберите электрические разъемы.

![[19400436.png]]

Используйте мультиметр для измерения сопротивления между двумя штифтами датчика температуры воздуха. Сопротивление **должно быть от 600 до 36k ом. Если сопротивление **не** правильно, замените датчик. Если сопротивление правильное, датчик **должен быть проверен на короткое замыкание на землю.

* Значение сопротивления зависит от температуры следующим образом:

| Температура градуса | Темп F | Допустимая дальность сопротивления (Омс) |
|---|---|---|
| 0 | 32 | 30k до 36k |
| 25 | 77 | 9k до 11k |
| 50 | 122 | 3k - 4k |
| 75 | 167 | 1350—1500 |
| 100 | 212 | 600-675 |

![[19800980.png]]

### Проверка на замыкание на массу

Измерьте сопротивление от штифта датчика температуры воздуха на входе в блок двигателя. Мультиметр **должен** показывать открытую схему (более 100k ом). Если схема **не** открыта, замените датчик.

![[19800981.png]]


> [!quote]- Original (English) · английский оригинал
> ### Remove
>
> Lift up on the locking tab and pull the electrical connectors apart.
>
> Remove the sensor from the engine.
>
> ### Install
>
> Make sure the new sensor has an o-ring around the surface where it seals against the engine block.
>
> Install the sensor in the engine block.
>
> **Момент затяжки · Torque Value**
> 14 n•m [124 in-lb]
>
> Push connectors together until they lock.
>
> ### Resistance Check
>
> Lift up on the locking tab and pull the electrical connectors apart.
>
> Use a multimeter to measure the resistance between the two pins of the intake air temperature sensor. The resistance **must** be 600 ohms to 36k ohms\*. If the resistance is **not** correct, replace the sensor. If the resistance is correct, the sensor **must** still be checked for a short circuit to ground.
>
> \* The resistance value is temperature-dependent as follows:
>
> | Temp C° | Temp F° | Acceptable Resistance Range (ohms) |
> |---|---|---|
> | 0 | 32 | 30k to 36k |
> | 25 | 77 | 9k to 11k |
> | 50 | 122 | 3k to 4k |
> | 75 | 167 | 1350 to 1500 |
> | 100 | 212 | 600 to 675 |
>
> ### Check for Short Circuit to Ground
>
> Measure the resistance from a pin of the intake air temperature sensor to the engine block. The multimeter **must** show an open circuit (more than 100k ohms). If the circuit is **not** open, replace the sensor.
