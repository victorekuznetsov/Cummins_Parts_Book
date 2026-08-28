---
aliases:
  - "Датчик температуры моторного масла"
type: "Процедура"
doc: "60-019-067"
title_en: "Engine Oil Temperature Sensor"
title_ru: "Датчик температуры моторного масла"
modified: "2007-12-14"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021674"
figures: 7
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-019-067.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-019-067.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
  - "перевод/машинный"
---

# Engine Oil Temperature Sensor
**Датчик температуры моторного масла**

> [!abstract] Процедура · `60-019-067`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section 19 — Electronic Engine Controls — Group 19
> **Даты:** изменён 2007-12-14
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-019-067.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-019-067.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Снятие

[[60-100-002 — Engine Diagrams|См. процедуру 100-002 (Диаграммы двигателя) в разделе E для информации о местоположении датчика.]]

Отсоедините датчик температуры масла двигателя от электропроводки двигателя.

Удалите датчик температуры масла двигателя из двигателя.

![[19900794.png]]

### Очистка и проверка при повторном использовании

Осмотрите разъём ремня электропроводки двигателя и датчик температуры масла двигателя на предмет:

- Разбитая или разбитая соединительная оболочка
- Пропавшие или поврежденные соединительные уплотнения
- Грязь, мусор или влага в или на контактах разъема
- Коррозийные, согнутые, отодвинутые назад или расширенные булавки
- Повреждённый уплотнитель кольца
- Повреждение струны.

![[19600483.png]]

### Установка

Установите новое кольцо на датчик, если это необходимо.

Установите датчик температуры масла двигателя.

> [!tip] Момент затяжки
> 14 Н·м [124 фунт-дюйм]

Подключите датчик к жгуту проводов двигателя. Клик будет услышан, когда разъем заблокируется на месте.

![[19900794.png]]

### Проверка сопротивления

Отключите разъем датчика. Выберите функцию сопротивления на мультиметре. Прикрепите соответствующий испытательный щуп к многометровым зондам. Прикоснитесь к двум испытательным зондам на датчике. Измерьте сопротивление. Мультиметр **должен** показывать от 115 до 244k ом. Значение сопротивления зависит от температуры, как показано в таблице ниже.

| температура | температура | диапазон |
|---|---|---|
| (°C) | \[°F\] | (Омс) |
| 0 | 32 | 33k до 36k |
| 25 | 77 | 9k до 11k |
| 50 | 122 | 3k - 4k |
| 75 | 167 | 1350—1500 |
| 100 | 212 | 600-675 |

![[19801852.png]]

Если сопротивление находится вне диапазона, то датчик вышел из строя.

Замените датчик.

![[19801853.png]]

### Проверка на замыкание на массу

Прикоснитесь к многометровому свинцу с помощью прикрепленного соответствующего испытательного щупа к любому терминалу на датчике. Прикосновение к другому мультиметру приводит к хорошей, чистой поверхности на блоке двигателя.

![[19801854.png]]

Измерьте сопротивление.

Мультиметр **должен** показывать более 100k ом, что является открытой схемой. Если цепь **не** закрыта, то внутри датчика есть короткое расстояние до земли шасси.

Замените датчик.

![[19801621.png]]


> [!quote]- Original (English) · английский оригинал
> ### Remove
>
> [[60-100-002 — Engine Diagrams|Refer to Procedure 100-002 (Engine Diagrams) in Section E for sensor location information.]]
>
> Disconnect the engine oil temperature sensor from the engine harness.
>
> Remove the engine oil temperature sensor from the engine.
>
> ### Clean and Inspect for Reuse
>
> Inspect the engine harness connector and the engine oil temperature sensor for the following:
>
> - Cracked or broken connector shell
> - Missing or damaged connector seals
> - Dirt, debris, or moisture in or on the connector pins
> - Corroded, bent, pushed back, or expanded pins
> - Damaged o-ring seal
> - Thread damage.
>
> ### Install
>
> Install a new o-ring onto the sensor, if necessary.
>
> Install the engine oil temperature sensor.
>
> **Момент затяжки · Torque Value**
> 14 n•m [124 in-lb]
>
> Connect the sensor to the engine harness. A click will be heard when the connector locks in place.
>
> ### Resistance Check
>
> Disconnect the sensor connector. Select the resistance function on the multimeter. Attach the appropriate test leads to the multimeter probes. Touch the two test leads to the two terminals on the sensor. Measure the resistance. The multimeter **must** show between 115 and 244k ohms. The resistance value is temperature-dependent as shown in the table below.
>
> | Temperature | Temperature | Range |
> |---|---|---|
> | (°C) | \[°F\] | (ohms) |
> | 0 | 32 | 33k to 36k |
> | 25 | 77 | 9k to 11k |
> | 50 | 122 | 3k to 4k |
> | 75 | 167 | 1350 to 1500 |
> | 100 | 212 | 600 to 675 |
>
> If the resistance is out of range, then the sensor has failed.
>
> Replace the sensor.
>
> ### Check for Short Circuit to Ground
>
> Touch the multimeter lead with the attached appropriate test lead to either terminal on the sensor. Touch the other multimeter lead to a good, clean surface on the engine block.
>
> Measure the resistance.
>
> The multimeter **must** show greater than 100k ohms, which is an open circuit. If the circuit is **not** closed, then there is a short within the sensor to chassis ground.
>
> Replace the sensor.
