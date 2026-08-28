---
aliases:
  - "Система охлаждения"
type: "Процедура"
doc: "10-018-018-om-auto"
title_en: "Cooling System"
title_ru: "Система охлаждения"
modified: "2011-10-17"
engines:
  - "80141463"
  - "80248213"
families:
  - "QSX15"
manuals:
  - "3666251"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/10/10-018-018-om-auto.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/10-018-018-om-auto.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSX15"
  - "группа/10"
  - "перевод/машинный"
---

# Cooling System
**Система охлаждения**

> [!abstract] Процедура · `10-018-018-om-auto`
> **Двигатели:** [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSX15
> **Входит в руководства:** [[3666251 — Signature and ISX Operation and Maintenance Manual|3666251]]
> **Секции:** Section V - Maintenance Specifications
> **Даты:** изменён 2011-10-17
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/10/10-018-018-om-auto.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/10-018-018-om-auto.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Cummins Inc. рекомендует использовать полностью сформированный антифриз или охлаждающую жидкость, содержащую предварительный заряд дополнительной добавки к охлаждающей жидкости (SCA). Антифриз или охлаждающая жидкость должны соответствовать спецификациям, изложенным в Рекомендуемой практике Совета по технологиям и техническому обслуживанию (TMC) 329 (этиленгликоль) или Рекомендуемой практике (RP) 330 (пропиленгликоль). Использование полностью сформированного антифриза или охлаждающей жидкости значительно упрощает обслуживание системы охлаждения.

Копии спецификаций Совета по технологиям и техническому обслуживанию (TMC) можно получить через Cummins Inc. или связавшись с:

Совет по технологиям и техническому обслуживанию

Американская ассоциация грузоперевозок

2200 Милл-роуд

Александрия, ВА 33314-5388

Телефон: (703) 838-1763

Факс (703) 836-6070

Полностью сформированный антифриз содержит сбалансированное количество антифризов, SCA и буферных соединений, но не содержит 50% воды. Полностью сформированная охлаждающая жидкость содержит сбалансированное количество антифриза, SCA и буферных соединений, уже предварительно смешанных 50/50 с деионизированной водой.

На следующих страницах объясняется, как использовать воду, антифриз и SCA, а также как тестировать уровни антифризов и SCA.

В этом разделе также содержится информация о техническом обслуживании системы охлаждения и схема обработки охлаждающей жидкости, которая используется для определения правильного сервисного фильтра SCA.

Альтернативные методы технического обслуживания систем охлаждения можно найти в Cummins® Coolant Requirements and Maintenance, Bulletin 3666132.

### Спецификации

Автомобильное применение

#### Мощность охлаждающей жидкости (только двигатель)

| С EGR | 33,1 литра[35 квт] |
|---|---|

| Без ЭКГ | 24 литра[25 квт] |
|---|---|

#### Стандартный модулирующий термостат

| Диапазон температур | 82-93°C[180-200°F] |
|---|---|

#### Максимальное давление охлаждающей жидкости (исключая крышку радиатора - закрытый термостат с максимальной скоростью без нагрузки)

| ISX CM871 | 434 кПа[63psi] |
|---|---|

| ISX CM870 | 400 кПа[38 psi] |
|---|---|

| ISX без EGR и QSX | 227 кПа[33 psi] |
|---|---|

#### Температура активации охлаждающей сигнализации

| С EGR - Рейтинги ниже 565 лошадиных сил | 107°C[225°F] |
|---|---|

| С EGR - Рейтинги 565/600 лошадиных сил | 110°C[230°F] |
|---|---|

| Без ЭКГ | 107°C[225°F] |
|---|---|

#### Максимально допустимая температура топового танка

| Рейтинг ниже 565 лошадиных сил с EGR и без двигателей EGR | 107°C[225°F] |
|---|---|

| Рейтинги 565/600 лошадиных сил с EGR | 110°C[230°F] |
|---|---|

#### Минимальная рекомендуемая температура топового танка

| Минимальная температура | 70°C[160°F] |
|---|---|

#### Минимально допустимый скачок

| С EGR | 11 процентов |
|---|---|

| Без ЭКГ | 2,4 литра [2,5 квт] или 10% емкости системы (в зависимости от того, что больше) |
|---|---|

#### Минимальный рекомендуемый предел давления радиатора

| ISX с EGR | 103 кПа[15 psi] |
|---|---|

| ISX без ЭКГ | 50 кПа[7 psi] |
|---|---|

#### Минимальная ставка заполнения

| Без сигнализации низкого уровня | 19 литров/мин.[5 гпм] |
|---|---|

#### Максимальное время деаэрации

| Максимальное время | 25 минут |
|---|---|

#### Вентилятор на температуре охлаждения

| С EGR | 99°C[210°F] |
|---|---|

| Без ЭКГ | 99°C[210°F] |
|---|---|

#### Вентилятор на входе Температура воздуха

| С EGR | 93°C[200°F] |
|---|---|

| Без ЭКГ | 88°C[190°F] |
|---|---|

#### Затвор открывает температуру

| Охлаждающий - с EGR | 96°C[205°F] |
|---|---|

| Охлаждение - без EGR | 85°C[185°F] |
|---|---|

| Взятие воздуха - с EGR | 104 °C[220°F] |
|---|---|

| Взятие воздуха - без EGR | 66°C[150°F] |
|---|---|

#### Зимние фронты

| Зона воздушного прохода | 774 см 2 \[120 в 2 \] |
|---|---|


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> Cummins Inc. recommends the use of fully-formulated antifreeze or coolant containing a precharge of supplemental coolant additive (SCA). The antifreeze or coolant **must** meet the specifications outlined in the Technology and Maintenance Council (TMC) Recommended Practice (RP) 329 (ethylene glycol) or Recommended Practice (RP) 330 (propylene glycol). The use of fully-formulated antifreeze or coolant significantly simplifies cooling system maintenance.
>
> Copies of Technology and Maintenance Council (TMC) specifications can be obtained through Cummins Inc., or by contacting:
>
> Technology and Maintenance Council
>
> American Trucking Association
>
> 2200 Mill Road
>
> Alexandria, VA 33314-5388
>
> Phone: (703) 838-1763
>
> Fax (703) 836-6070
>
> Fully-formulated antifreeze contains balanced amounts of antifreeze, SCA, and buffering compounds, but does **not** contain 50 percent water. Fully-formulated coolant contains balanced amounts of antifreeze, SCA, and buffering compounds already premixed 50/50 with deionized water.
>
> The following pages explain water, antifreeze, and SCA's and how to test antifreeze and SCA levels.
>
> This section also contains information on cooling system maintenance and a coolant treatment chart that is used to determine the correct SCA service filter.
>
> Alternative maintenance practices for cooling systems can be found in Cummins® Coolant Requirements and Maintenance, Bulletin 3666132.
>
> ### Specifications
>
> Automotive Applications
>
> #### Coolant Capacity (engine only)
>
> | With EGR | 33.1 liters \[35 qt\] |
> |---|---|
>
> | Without EGR | 24 liters \[25 qt\] |
> |---|---|
>
> #### Standard Modulating Thermostat
>
> | Temperature Range | 82 to 93°C \[180 to 200°F\] |
> |---|---|
>
> #### Maximum Coolant Pressure (exclusive of pressure cap - closed thermostat at the maximum no-load governed speed)
>
> | ISX CM871 | 434 kPa \[63psi\] |
> |---|---|
>
> | ISX CM870 | 400 kPa \[38 psi\] |
> |---|---|
>
> | ISX Without EGR and QSX | 227 kPa \[33 psi\] |
> |---|---|
>
> #### Coolant Alarm Activation Temperature
>
> | With EGR - Ratings Below 565 Horsepower | 107°C \[225°F\] |
> |---|---|
>
> | With EGR - Ratings of 565/600 Horsepower | 110°C \[230°F\] |
> |---|---|
>
> | Without EGR | 107°C \[225°F\] |
> |---|---|
>
> #### Maximum Allowable Top Tank Temperature
>
> | Ratings Below 565 Horsepower with EGR and without EGR Engines | 107°C \[225°F\] |
> |---|---|
>
> | Ratings of 565/600 Horsepower with EGR only | 110°C \[230°F\] |
> |---|---|
>
> #### Minimum Recommended Top Tank Temperature
>
> | Minimum Temperature | 70°C \[160°F\] |
> |---|---|
>
> #### Minimum Allowable Draw Down
>
> | With EGR | 11 Percent |
> |---|---|
>
> | Without EGR | 2.4 liters \[2.5 qt\] or 10 Percent of System Capacity (whichever is greater) |
> |---|---|
>
> #### Minimum Recommended Pressure Cap
>
> | ISX With EGR | 103 kPa \[15 psi\] |
> |---|---|
>
> | ISX Without EGR | 50 kPa \[7 psi\] |
> |---|---|
>
> #### Minimum Fill Rate
>
> | Without Low-Level Alarm | 19 liters/min \[5 gpm\] |
> |---|---|
>
> #### Maximum Deaeration Time
>
> | Maximum Time | 25 minutes |
> |---|---|
>
> #### Fan-on Coolant Temperature
>
> | With EGR | 99°C \[210°F\] |
> |---|---|
>
> | Without EGR | 99°C \[210°F\] |
> |---|---|
>
> #### Fan-on Intake Air Temperature
>
> | With EGR | 93°C \[200°F\] |
> |---|---|
>
> | Without EGR | 88°C \[190°F\] |
> |---|---|
>
> #### Shutter Opening Temperature
>
> | Coolant - with EGR | 96°C \[205°F\] |
> |---|---|
>
> | Coolant - without EGR | 85°C \[185°F\] |
> |---|---|
>
> | Intake Air - with EGR | 104°C \[220°F\] |
> |---|---|
>
> | Intake Air - without EGR | 66°C \[150°F\] |
> |---|---|
>
> #### Winterfronts
>
> | Air passage area | 774 cm 2 \[120 in 2 \] |
> |---|---|
