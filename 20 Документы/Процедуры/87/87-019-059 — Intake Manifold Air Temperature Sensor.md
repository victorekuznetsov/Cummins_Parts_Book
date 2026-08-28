---
aliases:
  - "Датчик температуры воздуха во впускном коллекторе"
type: "Процедура"
doc: "87-019-059"
title_en: "Intake Manifold Air Temperature Sensor"
title_ru: "Датчик температуры воздуха во впускном коллекторе"
modified: "2004-02-06"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666214"
figures: 9
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-019-059.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-019-059.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
  - "перевод/машинный"
---

# Intake Manifold Air Temperature Sensor
**Датчик температуры воздуха во впускном коллекторе**

> [!abstract] Процедура · `87-019-059`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2004-02-06
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-019-059.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-019-059.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Снятие

Поднимите на запирающую вкладку и разберите электрические разъемы.

![[19a00247.png]]

Удалите датчик из двигателя.

![[19a00248.png]]

### Установка

Убедитесь, что новый датчик имеет кольцо вокруг поверхности, где он уплотняет блок двигателя.

Смажьте уплотнительное кольцо чистым моторным маслом.

![[19a00250.png]]

Установите датчик в блок двигателя.

> [!tip] Момент затяжки
> 14 Н·м [124 фунт-дюйм]

![[19a00248.png]]

> [!warning] ОСТОРОЖНО
> Используйте только рекомендованную Cummins смазку DS-ES, номер детали 3822934. Другие смазочные материалы, такие как моторное масло или смазка, в разъемах могут вызвать повреждение ECM, плохую производительность двигателя или преждевременный контактный износ разъема.

Нанесите небольшое количество смазки на соединительные терминалы. Перед установкой заполните всю полость разъема смазкой.

![[cel29.png]]

Скрепляйте разъёмы, пока они не заблокируются.

![[19a00247.png]]

### Проверка сопротивления

Поднимите на запирающую вкладку и разберите электрические разъемы.

![[19a00247.png]]

Используйте мультиметр для измерения сопротивления между двумя штифтами датчика температуры воздуха. Сопротивление **должно быть от 600 до 36k ом. Если сопротивление **не** правильно, замените датчик. Если сопротивление правильное, датчик **должен быть проверен на короткое замыкание на землю.

* Значение сопротивления зависит от температуры следующим образом:

| Температура градуса | Темп F | Допустимая дальность сопротивления (Омс) |
|---|---|---|
| 0 | 32 | 30k до 36k |
| 25 | 77 | 9k до 11k |
| 50 | 122 | 3k - 4k |
| 75 | 167 | 1350—1500 |
| 100 | 212 | 600-675 |

![[19a00251.png]]

### Проверка на замыкание на массу

Измерьте сопротивление от одного из штифтов датчика температуры воздуха на впускном блоке двигателя.

Мультиметр **должен** показывать открытую схему (более 100k ом).

Если схема **не** открыта, замените датчик.

![[19a00252.png]]


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
> Lubricate the o-ring with clean engine oil.
>
> Install the sensor in the engine block.
>
> **Момент затяжки · Torque Value**
> 14 n•m [124 in-lb]
>
> **CAUTION · Осторожно**
> Use only Cummins-recommended lubricant DS-ES, Part Number 3822934. Other lubricants, such as lubricating oil or grease, in the connectors can cause ECM damage, poor engine performance, or premature connector pin wear.
>
> Apply a small amount of lubricant to the connector terminals. Before installing, fill the entire connector cavity lubricant.
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
> Measure the resistance from one of the pins of the intake air temperature sensor to the engine block.
>
> The multimeter **must** show an open circuit (more than 100k ohms).
>
> If the circuit is **not** open, replace the sensor.
