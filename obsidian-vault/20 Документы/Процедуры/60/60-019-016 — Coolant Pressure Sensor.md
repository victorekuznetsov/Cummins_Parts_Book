---
aliases:
  - "Датчик давления охлаждающей жидкости"
type: "Процедура"
doc: "60-019-016"
title_en: "Coolant Pressure Sensor"
title_ru: "Датчик давления охлаждающей жидкости"
modified: "2007-12-14"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021674"
figures: 9
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-019-016.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-019-016.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
  - "перевод/машинный"
---

# Coolant Pressure Sensor
**Датчик давления охлаждающей жидкости**

> [!abstract] Процедура · `60-019-016`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section 19 — Electronic Engine Controls — Group 19
> **Даты:** изменён 2007-12-14
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-019-016.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-019-016.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Подготовительные операции

> [!danger] ОПАСНО
> Охлаждающая жидкость токсична. Хранить в недоступном для детей и животных месте. Если деталь не используется повторно, утилизируйте её по местным природоохранным требованиям.

> [!danger] ОПАСНО
> Не снимайте пробку радиатора с горячего двигателя. Снимайте пробку радиатора только после того, как температура охлаждающей жидкости опустится ниже 50 °C \[120 °F\]. Нагретый спрей охлаждающей жидкости или поток может вызвать личную травму.

- Слейте охлаждающую жидкость.[[57-008-018 — Cooling System|См. процедуру 008-018 (Система охлаждения) в разделе 8 Руководства по обслуживанию QST30, Бюллетень 4021539.]]

![[ck800wa.png]]

### Снятие

> [!note] Примечание
> Двигатель QSK19 используется на следующих примерах. Шаги удаления и установки одинаковы.

Отсоедините проводку двигателя от датчика давления охлаждающей жидкости.

![[19400387.png]]

Удалите датчик давления охлаждающей жидкости.

Используйте розетку Deep Well, номер детали 3823843, чтобы удалить датчик давления охлаждающей жидкости.

![[19801029.png]]

### Проверка

Подключите инструмент электронного сервиса INSITETM к шине данных CAN.

![[19800902.png]]

Подключите жгут проводов двигателя к датчику давления охлаждающей жидкости.

Позвольте датчику и проводах висеть в воздухе.

![[08600402.png]]

Мониторинг датчика давления охлаждающей жидкости с помощью электронного инструментария обслуживания.

Давление охлаждающей жидкости должно быть в пределах 17,2 кПа \[2,5 psi\] от значения барометрического датчика давления.

Если давление охлаждающей жидкости **не** в пределах спецификаций, датчик давления охлаждающей жидкости  должен быть заменен.

Отключите электронный сервис INSITETM.

Отсоедините датчик давления охлаждающей жидкости от электропроводки двигателя.

![[19800902.png]]

### Установка

Установите датчик давления охлаждающей жидкости в корпус термостата.

Затянуть датчик давления охлаждающей жидкости.

> [!tip] Момент затяжки
> 14 Н·м [124 фунт-дюйм]

![[19801029.png]]

Подключите жгут проводов двигателя к датчику давления охлаждающей жидкости.

![[19801028.png]]

### Завершающие операции

> [!danger] ОПАСНО
> Охлаждающая жидкость токсична. Хранить в недоступном для детей и животных месте. Если деталь не используется повторно, утилизируйте её по местным природоохранным требованиям.

- Заправьте систему охлаждения.[[57-008-018 — Cooling System|См. процедуру 008-018 (Система охлаждения) в разделе 8 Руководства по обслуживанию QST30, Бюллетень 4021539.]]

![[ck800wa.png]]


> [!quote]- Original (English) · английский оригинал
> ### Preparatory Steps
>
> **WARNING · Опасно**
> Coolant is toxic. Keep away from children and pets. If not reused, dispose of in accordance with local environmental regulations.
>
> **WARNING · Опасно**
> Do not remove the pressure cap from a hot engine. Wait until the coolant temperature is below 50°C \[120°F\] before removing the pressure cap. Heated coolant spray or stream can cause personal injury.
>
> - Drain the cooling system. [[57-008-018 — Cooling System|Refer to Procedure 008-018 (Cooling System) in Section 8 of the QST30 Service Manual, Bulletin 4021539.]]
>
> ### Remove
>
> **Note · Примечание**
> The QSK19 engine is used in the following illustrations. The remove and install steps are the same.
>
> Disconnect the engine harness from the coolant pressure sensor.
>
> Remove the coolant pressure sensor.
>
> Use the Deep Well Socket, Part Number 3823843, to remove the coolant pressure sensor.
>
> ### Test
>
> Connect the INSITE™ electronic service tool to the data link.
>
> Connect the engine harness to the coolant pressure sensor.
>
> Allow the sensor and harness to hang in the air.
>
> Monitor the coolant pressure sensor with the electronic service tool.
>
> The coolant pressure **must** be within 17.2 kPa \[2.5 psi\] of the barometric pressure sensor value.
>
> If the coolant pressure is **not** within specifications, the coolant pressure sensor **must** be replaced.
>
> Disconnect INSITE™ electronic service tool.
>
> Disconnect the coolant pressure sensor from the engine harness.
>
> ### Install
>
> Install the coolant pressure sensor into the thermostat housing.
>
> Tighten the coolant pressure sensor.
>
> **Момент затяжки · Torque Value**
> 14 n•m [124 in-lb]
>
> Connect the engine harness to the coolant pressure sensor.
>
> ### Finishing Steps
>
> **WARNING · Опасно**
> Coolant is toxic. Keep away from children and pets. If not reused, dispose of in accordance with local environmental regulations.
>
> - Fill the cooling system. [[57-008-018 — Cooling System|Refer to Procedure 008-018 (Cooling System) in Section 8 of the QST30 Service Manual, Bulletin 4021539.]]
