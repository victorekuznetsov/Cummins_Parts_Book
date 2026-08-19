---
aliases:
  - "Датчик температуры охлаждающей жидкости"
type: "Процедура"
doc: "94-019-019"
title_en: "Engine Coolant Temperature Sensor"
title_ru: "Датчик температуры охлаждающей жидкости"
modified: "2003-03-24"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666184"
figures: 8
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/94/94-019-019.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/94-019-019.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/94"
  - "перевод/машинный"
---

# Engine Coolant Temperature Sensor
**Датчик температуры охлаждающей жидкости**

> [!abstract] Процедура · `94-019-019`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual|3666184]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-03-24
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/94/94-019-019.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/94-019-019.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Первичная проверка

Подключите электронный инструмент к разъему шины данных CAN.

Поместите выключатель Stop/Run в положение «Run».

Контроллер **не** в диагностическом режиме.

Запустите двигатель и запускайте его на холостом ходу.

![[19a00042.png]]

Контролируйте температуру охлаждающей жидкости с помощью электронного инструментария.

Сравните значение температуры охлаждения с калибром температуры воды или подключите датчик температуры к двигателю рядом с датчиком температуры охлаждающей жидкости и сравните показания на служебной оснастке с показаниями датчика температуры.

Если температура охлаждающей жидкости на электронном сервисном оборудовании чрезмерно выше температуры воды, замените датчик температуры охлаждающей жидкости.

Если температура охлаждающей жидкости на электронном сервисном оборудовании ** не** увеличивается с температурой воды, замените датчик температуры охлаждающей жидкости.

![[19400068.png]]

Удалите датчик температуры охлаждающей жидкости. См. процедуру[[94-019-019 — Engine Coolant Temperature Sensor|019-019-002]].

Подключите датчик температуры охлаждающей жидкости к электропроводке двигателя.

![[19400380.png]]

Подключите электронный инструмент к шине данных CAN.

Поместите выключатель Stop/Run в положение «STOP».

Контроллер в диагностическом режиме.

Контролируйте температуру охлаждающей жидкости с помощью электронного инструментария.

Если температура охлаждающей жидкости не снижается до текущей температуры окружающего воздуха, замените датчик температуры охлаждающей жидкости.

![[19a00042.png]]

### Снятие

> [!danger] ОПАСНО
> Подождите, пока температура охлаждающей жидкости не будет ниже 50°C \[120°F\], прежде чем удалять крышку радиатора системы охлаждающей жидкости. Неспособность сделать это может привести к травмам от нагреваемого спрея охлаждающей жидкости.

Слейте охлаждающую жидкость. См. Руководство по устранению неполадок и ремонту базового двигателя.

![[ra800qa.png]]

Поднимите на запирающую вкладку и разберите электрические разъемы.

Удалите датчик.

![[19400380.png]]

### Установка

Убедитесь, что новый датчик имеет установленное кольцо.

Смажьте уплотнительное кольцо чистым моторным маслом.

Установите новый датчик в двигатель. Затяните датчик.

> [!tip] Момент затяжки
> 14 Н·м [10 фунт-фут]

![[19400381.png]]

Соедините разъёмы до фиксации.

Заполните систему охлаждения и работайте с двигателем, чтобы проверить наличие утечек. См. Руководство по устранению неполадок и ремонту базового двигателя для надлежащих процедур.

![[19400382.png]]


> [!quote]- Original (English) · английский оригинал
> ### Initial Check
>
> Connect an electronic Service Tool to the data link connector.
>
> Place the Stop/Run Switch in the “Run” position.
>
> Controller **not** in the diagnostic mode.
>
> Start the engine and let it idle.
>
> Monitor the coolant temperature with the electronic Service Tool.
>
> Compare the cool temperature value with the water temperature gauge, or connect a temperature probe to the engine near the coolant temperature sensor and compare the reading on the service tool with the temperature probe reading.
>
> If the coolant temperature on the electronic Service Tool is excessively higher than the water temperature, replace the coolant temperature sensor.
>
> If the coolant temperature on the electronic Service Tool does **not** increase with the water temperature, replace the coolant temperature sensor.
>
> Remove the coolant temperature sensor. Refer to Procedure [[94-019-019 — Engine Coolant Temperature Sensor|019-019-002]].
>
> Connect the coolant temperature sensor to the engine harness.
>
> Connect an electronic Service Tool to the data link.
>
> Place the Stop/Run switch in the “STOP” position.
>
> Controller in the diagnostic mode.
>
> Monitor the coolant temperature with the electronic Service Tool.
>
> If the coolant temperature does not decrease to the current ambient air temperature, replace the coolant temperature sensor.
>
> ### Remove
>
> **WARNING · Опасно**
> Wait until the coolant temperature is below 50° C \[120° F\] before removing the coolant system pressure cap. Failure to do so can cause personal injury from heated coolant spray.
>
> Drain the cooling system. Refer to the Base Engine Troubleshooting and Repair Manual.
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
> 14 n•m [10 ft-lb]
>
> Push the connectors together until they lock.
>
> Fill the cooling system and operate the engine to check for leaks. Refer to Base Engine Troubleshooting and Repair Manual for proper procedures.
