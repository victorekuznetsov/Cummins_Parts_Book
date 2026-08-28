---
aliases:
  - "Датчик температуры воздуха во впускном коллекторе"
type: "Процедура"
doc: "60-019-059"
title_en: "Intake Manifold Air Temperature Sensor"
title_ru: "Датчик температуры воздуха во впускном коллекторе"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-019-059.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-019-059.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
  - "перевод/машинный"
---

# Intake Manifold Air Temperature Sensor
**Датчик температуры воздуха во впускном коллекторе**

> [!abstract] Процедура · `60-019-059`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section 19 — Electronic Engine Controls — Group 19
> **Даты:** изменён 2007-12-14
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-019-059.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-019-059.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Снятие

Отсоедините разъем жгута проводов двигателя от датчика температуры воздуха впускного коллектора.

Удалите датчик температуры воздуха впускного коллектора из двигателя.

![[19400434.png]]

### Установка

Установите новое кольцо на датчик температуры впускного коллектора.

Установите датчик в впускном коллекторе.

Затяните датчик.

> [!tip] Момент затяжки
> 14 Н·м [124 фунт-дюйм]

![[19400435.png]]

Соедините разъёмы до фиксации.

![[19400436.png]]

### Проверка сопротивления

Отсоедините разъем жгута проводов двигателя от датчика температуры воздуха впускного коллектора.

![[19400436.png]]

Измерить сопротивление между впускным коллектором 1 температурного сигнала и впускным коллектором 1 температурного обратного контакта в датчике.

![[19800980.png]]

| температура | Допустимая дальность сопротивления |  |
|---|---|---|
| **°C** | **°F** | **(Ом)** |
| 0 | 32 | 30k до 36k |
| 25 | 77 | 9k до 11k |
| 50 | 122 | 3k - 4k |
| 75 | 167 | 1350—1500 |
| 100 | 212 | 600-675 |

Если сопротивление датчика температуры воздуха в впускном коллекторе **не** в пределах диапазона, его * необходимо заменить.

![[19800980.png]]

### Проверка на замыкание на массу

Измерьте сопротивление между впускным коллектором 1 температурного сигнала контакта и заземлением двигателя.

Замените датчик, если сопротивление **не** больше 100k Ом.

> [!missing]- Иллюстрация `19800981.png` не извлечена — смотрите PDF-оригинал документа


> [!quote]- Original (English) · английский оригинал
> ### Remove
>
> Disconnect the engine harness connector from the intake manifold air temperature sensor.
>
> Remove the intake manifold air temperature sensor from the engine.
>
> ### Install
>
> Install a new o-ring on the intake manifold temperature sensor.
>
> Install the sensor in the intake manifold.
>
> Tighten the sensor.
>
> **Момент затяжки · Torque Value**
> 14 n•m [124 in-lb]
>
> Push the connectors together until they lock.
>
> ### Resistance Check
>
> Disconnect the engine harness connector from the intake manifold air temperature sensor.
>
> Measure the resistance between the intake manifold 1 temperature signal and intake manifold 1 temperature RETURN pin in the sensor.
>
> | Temperature | Acceptable Resistance Range |  |
> |---|---|---|
> | **°C** | **°F** | **(ohms)** |
> | 0 | 32 | 30k to 36k |
> | 25 | 77 | 9k to 11k |
> | 50 | 122 | 3k to 4k |
> | 75 | 167 | 1350 to 1500 |
> | 100 | 212 | 600 to 675 |
>
> If the intake manifold air temperature sensor resistance is **not** within the range, it **must** be replaced.
>
> ### Check for Short Circuit to Ground
>
> Measure the resistance between the intake manifold 1 temperature SIGNAL pin and engine ground.
>
> Replace the sensor if the resistance is **not** greater than 100k ohms.
