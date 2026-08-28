---
aliases:
  - "Датчик температуры охлаждающей жидкости"
type: "Процедура"
doc: "87-019-019"
title_en: "Engine Coolant Temperature Sensor"
title_ru: "Датчик температуры охлаждающей жидкости"
modified: "2010-08-02"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666214"
figures: 8
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-019-019.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-019-019.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
  - "перевод/машинный"
---

# Engine Coolant Temperature Sensor
**Датчик температуры охлаждающей жидкости**

> [!abstract] Процедура · `87-019-019`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2010-08-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-019-019.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-019-019.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Первичная проверка

Подключите электронный инструмент к шине данных CAN транспортного средства.

Переведите замок зажигания в положение ON.

Запустите двигатель и запускайте его на холостом ходу.

![[19900524.png]]

Контролируйте температуру охлаждающей жидкости с помощью электронного инструментария.

Сравните значение температуры охлаждения с калибром температуры воды в приборной панели транспортного средства или подсоедините датчик температуры к двигателю рядом с датчиком температуры охлаждающей жидкости и сравните показания на служебной оснастке с показаниями датчика температуры.

Если температура охлаждающей жидкости на электронном сервисном оборудовании чрезмерно выше температуры воды, замените датчик температуры охлаждающей жидкости.

Если температура охлаждающей жидкости на электронном сервисном оборудовании **не** увеличивается с температурой воды, замените датчик температуры охлаждающей жидкости.

![[19400068.png]]

Удалите датчик температуры охлаждающей жидкости.[[87-019-019 — Engine Coolant Temperature Sensor|См. процедуру 019-019]].

Подключите датчик температуры охлаждающей жидкости к электропроводке двигателя.

![[19400380.png]]

Подключите электронный инструмент к шине данных CAN транспортного средства.

Переведите замок зажигания в положение ON.

Контролируйте температуру охлаждающей жидкости с помощью электронного инструментария.

Если температура охлаждающей жидкости **не** снижается до текущей температуры окружающего воздуха, замените датчик температуры охлаждающей жидкости.

![[19900524.png]]

### Снятие

> [!danger] ОПАСНО
> Не снимайте пробку радиатора с горячего двигателя. Снимайте пробку радиатора только после того, как температура охлаждающей жидкости опустится ниже 50 °C \[120 °F\]. Струя горячей охлаждающей жидкости или пар могут привести к травме.

Слейте охлаждающую жидкость.

Используйте следующую процедуру в руководстве по обслуживанию QST30, в бюллетене [[4021539 — QST30 Service Manual\|4021539]].[[57-008-018 — Cooling System|См. процедуру 008-018 в разделе 8.]]

![[ra800qa.png]]

Поднимите на запирающую вкладку и разберите электрические разъемы.

Удалите датчик.

![[19400380.png]]

### Установка

Убедитесь, что новый датчик имеет установленное кольцо.

Смажьте уплотнительное кольцо чистым моторным маслом.

Установите новый датчик в двигатель. Затяните датчик.

> [!tip] Момент затяжки
> 14 Н·м [124 фунт-дюйм]

![[19400381.png]]

Соедините разъёмы до фиксации.

Заполните систему охлаждения и работайте с двигателем, чтобы проверить наличие утечек.

Используйте следующую процедуру в руководстве по обслуживанию QST30, в бюллетене [[4021539 — QST30 Service Manual\|4021539]].[[57-008-018 — Cooling System|См. процедуру 008-018 в разделе 8.]]

![[19400382.png]]


> [!quote]- Original (English) · английский оригинал
> ### Initial Check
>
> Connect an electronic service tool to the vehicle datalink.
>
> Turn the keyswitch to the ON position.
>
> Start the engine and let it idle.
>
> Monitor the coolant temperature with the electronic service tool.
>
> Compare the cool temperature value with the water temperature gauge in the vehicle dash, or connect a temperature probe to the engine near the coolant temperature sensor and compare the reading on the service tool with the temperature probe reading.
>
> If the coolant temperature on the electronic service tool is excessively higher than the water temperature, replace the coolant temperature sensor.
>
> If the coolant temperature on the electronic service tool does **not** increase with the water temperature, replace the coolant temperature sensor.
>
> Remove the coolant temperature sensor. [[87-019-019 — Engine Coolant Temperature Sensor|Refer to Procedure 019-019]].
>
> Connect the coolant temperature sensor to the engine harness.
>
> Connect an electronic service tool to the vehicle datalink.
>
> Turn the keyswitch to the ON position.
>
> Monitor the coolant temperature with the electronic service tool.
>
> If the coolant temperature does **not** decrease to the present ambient air temperature, replace the coolant temperature sensor.
>
> ### Remove
>
> **WARNING · Опасно**
> Do not remove the pressure cap from a hot engine. Wait until the coolant temperature is below 50°C \[120°F\] before removing the pressure cap. Heated coolant spray or steam can cause personal injury.
>
> Drain the cooling system.
>
> Use the following procedure in the QST30 Service Manual, Bulletin [[4021539 — QST30 Service Manual\|4021539]]. [[57-008-018 — Cooling System|Refer to Procedure 008-018 in Section 8.]]
>
> Lift up on the locking tab and pull the electrical connectors apart.
>
> Remove the sensor.
>
> ### Install
>
> Make sure the new sensor has an o-ring installed.
>
> Lubricate the o-ring with clean engine oil.
>
> Install the new sensor into the engine. Tighten the sensor.
>
> **Момент затяжки · Torque Value**
> 14 n•m [124 in-lb]
>
> Push the connectors together until they lock.
>
> Fill the cooling system and operate the engine to check for leaks.
>
> Use the following procedure in the QST30 Service Manual, Bulletin [[4021539 — QST30 Service Manual\|4021539]]. [[57-008-018 — Cooling System|Refer to Procedure 008-018 in Section 8.]]
