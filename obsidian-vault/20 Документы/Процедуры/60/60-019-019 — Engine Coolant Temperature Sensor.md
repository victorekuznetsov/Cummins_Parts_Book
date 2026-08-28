---
aliases:
  - "Датчик температуры охлаждающей жидкости"
type: "Процедура"
doc: "60-019-019"
title_en: "Engine Coolant Temperature Sensor"
title_ru: "Датчик температуры охлаждающей жидкости"
modified: "2007-12-14"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021674"
figures: 8
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-019-019.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-019-019.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
  - "перевод/машинный"
---

# Engine Coolant Temperature Sensor
**Датчик температуры охлаждающей жидкости**

> [!abstract] Процедура · `60-019-019`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section 19 — Electronic Engine Controls — Group 19
> **Даты:** изменён 2007-12-14
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-019-019.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-019-019.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Проверка

Подключите инструмент электронного сервиса INSITETM к разъему шины данных CAN.

Поместите переключатель RUN/STOP в положение RUN.

Контроллер **не** в диагностическом режиме.

Запустите двигатель и запускайте его на холостом ходу.

![[19800902.png]]

Поместите датчик температуры в непосредственной близости от датчика температуры охлаждающей жидкости.

Запись температуры охлаждающей жидкости с помощью электронного инструментария INSITETM.

Сравните температуру щупа и инструментальную оснастку электронного сервиса INSITETM.

Если температура охлаждающей жидкости на электронном сервисном оборудовании чрезмерно выше температуры воды, замените датчик температуры охлаждающей жидкости.

Смотрите шаг удаления в этой процедуре.

Если температура охлаждающей жидкости на электронном сервисном оборудовании **не** увеличивается с температурой воды, замените датчик температуры охлаждающей жидкости.

Смотрите шаг удаления в этой процедуре.

![[19400068.png]]

Поместите переключатель RUN/STOP в положение STOP.

Контролируйте температуру охлаждающей жидкости с помощью электронного инструментария.

Если температура охлаждающей жидкости не снижается до температуры окружающего воздуха, замените датчик температуры охлаждающей жидкости.

Смотрите шаг удаления в этой процедуре.

![[19800902.png]]

### Подготовительные операции

> [!danger] ОПАСНО
> Не снимайте пробку радиатора с горячего двигателя. Подождите, пока температура охлаждающей жидкости не будет ниже 50°C \[120°F\], прежде чем удалять крышку давления радиатора или датчик температуры охлаждающей жидкости. Струя горячей охлаждающей жидкости или пар могут привести к травме.

- Слейте охлаждающую жидкость.[[57-008-018 — Cooling System|См. процедуру 008-018 (Система охлаждения) в разделе 8 в Руководстве по обслуживанию QST30, Бюллетень 4021539.]]

![[ck800wa.png]]

### Снятие

Поднимите на запирающую вкладку и разберите электрические разъемы.

Удалите датчик.

![[19c00247.png]]

### Установка

Убедитесь, что новый датчик имеет установленное кольцо.

Смазать кольцо чистым растительным маслом.

Установите новый датчик в двигатель. Затяните датчик.

> [!tip] Момент затяжки
> 14 Н·м [124 фунт-дюйм]

![[19c00247.png]]

Соедините разъёмы до фиксации.

![[19c00248.png]]

### Завершающие операции

> [!danger] ОПАСНО
> Не снимайте пробку радиатора с горячего двигателя. Подождите, пока температура охлаждающей жидкости не будет ниже 50°C \[120°F\], прежде чем удалять крышку давления радиатора или датчик температуры охлаждающей жидкости. Струя горячей охлаждающей жидкости или пар могут привести к травме.

- Заполните систему охлаждения и проверьте наличие утечек охлаждающей жидкости.[[57-008-018 — Cooling System|См. процедуру 008-018 (Система охлаждения) в разделе 8 в Руководстве по обслуживанию QST30, Бюллетень 4021539.]]

![[ck800wa.png]]


> [!quote]- Original (English) · английский оригинал
> ### Test
>
> Connect an INSITE™ electronic service tool to the data link connector.
>
> Place the RUN/STOP switch in the RUN position.
>
> Controller **not** in the diagnostic mode.
>
> Start the engine and let it idle.
>
> Place a temperature probe in close proximity of the coolant temperature sensor.
>
> Record the coolant temperature from the INSITE™ electronic service tool.
>
> Compare the temperature of the probe and the INSITE™ electronic service tool.
>
> If the coolant temperature on the electronic service tool is excessively higher than the water temperature, replace the coolant temperature sensor.
>
> Refer to the Remove step in this procedure.
>
> If the coolant temperature on the electronic service tool does **not** increase with the water temperature, replace the coolant temperature sensor.
>
> Refer to the Remove step in this procedure.
>
> Place the RUN/STOP switch in the STOP position.
>
> Monitor the coolant temperature with the electronic service tool.
>
> If the coolant temperature does not decrease to the ambient air temperature, replace the coolant temperature sensor.
>
> Refer to the Remove step in this procedure.
>
> ### Preparatory Steps
>
> **WARNING · Опасно**
> Do not remove the pressure cap from a hot engine. Wait until the coolant temperature is below 50°C \[120°F\] before removing the pressure cap or the coolant temperature sensor. Heated coolant spray or steam can cause personal injury.
>
> - Drain the cooling system. [[57-008-018 — Cooling System|Refer to Procedure 008-018 (Cooling System) in Section 8 in the QST30 Service Manual, Bulletin 4021539.]]
>
> ### Remove
>
> Lift up on the locking tab and pull the electrical connectors apart.
>
> Remove the sensor.
>
> ### Install
>
> Make sure the new sensor has an o-ring installed.
>
> Lubricate the o-ring with clean vegetable oil.
>
> Install the new sensor into the engine. Tighten the sensor.
>
> **Момент затяжки · Torque Value**
> 14 n•m [124 in-lb]
>
> Push the connectors together until they lock.
>
> ### Finishing Steps
>
> **WARNING · Опасно**
> Do not remove the pressure cap from a hot engine. Wait until the coolant temperature is below 50°C \[120°F\] before removing the pressure cap or the coolant temperature sensor. Heated coolant spray or steam can cause personal injury.
>
> - Fill the cooling system and check for coolant leaks. [[57-008-018 — Cooling System|Refer to Procedure 008-018 (Cooling System) in Section 8 in the QST30 Service Manual, Bulletin 4021539.]]
