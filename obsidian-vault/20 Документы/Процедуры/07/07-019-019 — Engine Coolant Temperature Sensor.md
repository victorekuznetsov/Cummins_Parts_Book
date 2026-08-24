---
aliases:
  - "Датчик температуры охлаждающей жидкости"
type: "Процедура"
doc: "07-019-019"
title_en: "Engine Coolant Temperature Sensor"
title_ru: "Датчик температуры охлаждающей жидкости"
modified: "2004-03-15"
engines:
  - "93058669"
families:
  - "C8.3 · 6C8.3"
manuals:
  - "4021442"
figures: 9
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-019-019.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/07-019-019.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "группа/07"
  - "перевод/машинный"
---

# Engine Coolant Temperature Sensor
**Датчик температуры охлаждающей жидкости**

> [!abstract] Процедура · `07-019-019`
> **Двигатели:** [[93058669 — 6C8.3 CPL 3105|93058669]]
> **Семейство:** C8.3 · 6C8.3
> **Входит в руководства:** [[4021442 — C8.3 Marine Electronic Control System Troubleshooting and Repair Manual|4021442]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2004-03-15
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-019-019.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/07-019-019.pdf)

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
> Не снимайте пробку радиатора с горячего двигателя. Снимайте пробку радиатора только после того, как температура охлаждающей жидкости опустится ниже 50 °C \[120 °F\]. Струя горячей охлаждающей жидкости или пар могут привести к травме.

- Слейте охлаждающую жидкость. См. процедуру 008-018 в Руководстве по устранению неполадок и ремонту, Двигатели серии С, Вестник [[3666003 — C Troubleshooting and Repair Manual\|3666003]].

![[ck800wa.png]]

### Первичная проверка

Холодный двигатель

Подключите электронный инструмент к шине данных CAN.

Переведите замок зажигания в положение ON.

Запустите двигатель и запускайте его на холостом ходу.

![[19900524.png]]

Контролируйте температуру охлаждающей жидкости с помощью электронного инструментария.

Сравните значение температуры охлаждающей жидкости с калибром температуры воды в рулевом колесе или подсоедините датчик температуры к двигателю рядом с датчиком температуры охлаждающей жидкости и сравните показания на служебной оснастке с показаниями датчика температуры.

Если температура охлаждающей жидкости на электронном сервисном оборудовании чрезмерно выше температуры воды, замените датчик температуры охлаждающей жидкости.

Если температура охлаждающей жидкости на электронном сервисном оборудовании ** не** увеличивается с температурой воды, замените датчик температуры охлаждающей жидкости.

![[19400068.png]]

Теплый двигатель

Удалите датчик температуры охлаждающей жидкости, как описано в этой процедуре.

Подключите датчик температуры охлаждающей жидкости к электропроводке двигателя.

![[19901360.png]]

Подключите электронный инструмент к шине данных CAN.

Переведите замок зажигания в положение ON.

Контролируйте температуру охлаждающей жидкости с помощью электронного инструментария.

Если температура охлаждающей жидкости ** не** снижается до текущей температуры окружающего воздуха, замените датчик температуры охлаждающей жидкости.

![[19900524.png]]

### Снятие

Поднимите запирающую вкладку и разберите электрические разъемы.

Удалите датчик.

![[19901388.png]]

### Установка

Убедитесь, что новый датчик имеет установленное кольцо.

Смажьте уплотнительное кольцо чистым моторным маслом.

Установите новый датчик в двигатель.

Затяните датчик.

> [!tip] Момент затяжки
> 14 Н·м [124 фунт-дюйм]

![[19901389.png]]

Соедините разъёмы до фиксации.

![[19901390.png]]

### Завершающие операции

> [!danger] ОПАСНО
> Охлаждающая жидкость токсична. Хранить в недоступном для детей и животных месте. Если деталь не используется повторно, утилизируйте её по местным природоохранным требованиям.

- Заправьте систему охлаждения. См. процедуру 008-018 в Руководстве по устранению неполадок и ремонту, Двигатели серии С, Вестник [[3666003 — C Troubleshooting and Repair Manual\|3666003]].
- Запустите двигатель и проверьте на отсутствие утечек.

![[ck800wa.png]]


> [!quote]- Original (English) · английский оригинал
> ### Preparatory Steps
>
> **WARNING · Опасно**
> Coolant is toxic. Keep away from children and pets. If not reused, dispose of in accordance with local environmental regulations.
>
> **WARNING · Опасно**
> Do not remove the pressure cap from a hot engine. Wait until the coolant temperature is below 50°C \[120°F\] before removing the pressure cap. Heated coolant spray or steam can cause personal injury.
>
> - Drain the cooling system. Refer to Procedure 008-018 in the Troubleshooting and Repair Manual, C Series Engines, Bulletin [[3666003 — C Troubleshooting and Repair Manual\|3666003]].
>
> ### Initial Check
>
> Cold Engine
>
> Connect an electronic service tool to the vessel datalink.
>
> Turn the keyswitch to the ON position.
>
> Start the engine and let it idle.
>
> Monitor the coolant temperature with the electronic service tool.
>
> Compare the coolant temperature value with the water temperature gauge in the helm, or connect a temperature probe to the engine near the coolant temperature sensor and compare the reading on the service tool with the temperature probe reading.
>
> If the coolant temperature on the electronic service tool is excessively higher than the water temperature, replace the coolant temperature sensor.
>
> If the coolant temperature on the electronic service tool does **not** increase with the water temperature, replace the coolant temperature sensor.
>
> Warm Engine
>
> Remove the coolant temperature sensor as described in this procedure.
>
> Connect the coolant temperature sensor to the engine harness.
>
> Connect an electronic service tool to the vessel datalink.
>
> Turn the keyswitch to the ON position.
>
> Monitor the coolant temperature with the electronic service tool.
>
> If the coolant temperature does **not** decrease to the current ambient air temperature, replace the coolant temperature sensor.
>
> ### Remove
>
> Lift the locking tab and pull the electrical connectors apart.
>
> Remove the sensor.
>
> ### Install
>
> Make sure the new sensor has an o-ring installed.
>
> Lubricate the o-ring with clean engine oil.
>
> Install the new sensor into the engine.
>
> Tighten the sensor.
>
> **Момент затяжки · Torque Value**
> 14 n•m [124 in-lb]
>
> Push the connectors together until they lock.
>
> ### Finishing Steps
>
> **WARNING · Опасно**
> Coolant is toxic. Keep away from children and pets. If not reused, dispose of in accordance with local environmental regulations.
>
> - Fill the cooling system. Refer to Procedure 008-018 in the Troubleshooting and Repair Manual, C Series Engines, Bulletin [[3666003 — C Troubleshooting and Repair Manual\|3666003]].
> - Operate the engine and check for leaks.
