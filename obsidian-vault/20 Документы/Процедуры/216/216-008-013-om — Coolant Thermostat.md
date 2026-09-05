---
aliases:
  - "Термостат системы охлаждения"
type: "Процедура"
doc: "216-008-013-om"
title_en: "Coolant Thermostat"
title_ru: "Термостат системы охлаждения"
modified: "2017-02-09"
engines:
  - "82099327"
families:
  - "QSB6.7"
manuals:
  - "4326167"
figures: 15
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/216/216-008-013-om.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/216-008-013-om.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSB6.7"
  - "группа/216"
  - "перевод/машинный"
---

# Coolant Thermostat
**Термостат системы охлаждения**

> [!abstract] Процедура · `216-008-013-om`
> **Двигатели:** [[82099327 — QSB6.7 CM2150 B109 CPL 4375|82099327]]
> **Семейство:** QSB6.7
> **Входит в руководства:** [[4326167 — QSB6.7 CM2150 B109 Operation and Maintenance Manual|4326167]]
> **Секции:** Section A - Adjustment, Repair, and Replacement
> **Даты:** изменён 2017-02-09
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/216/216-008-013-om.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/216-008-013-om.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Термостат контролирует температуру охлаждающей жидкости двигателя. Когда температура охлаждающей жидкости ниже рабочего диапазона, охлаждающая жидкость двигателя обходится обратно на вход водяного насоса. Когда температура охлаждающей жидкости двигателя достигает рабочего диапазона, термостат открывается, закрывает шунтирование и заставляет охлаждающую жидкость двигателя поступать в радиатор или теплообменник.

Неправильный или неисправный термостат может привести к тому, что двигатель будет работать слишком горячим или слишком холодным.

![[08900038.png]]

> [!warning] ОСТОРОЖНО
> Никогда не работайте с двигателем без термостата. Без термостата путь наименьшего сопротивления для охлаждающей жидкости проходит через обход на вход водяного насоса. Это может привести к перегреву двигателя.

![[08d00078.png]]

> [!warning] ОСТОРОЖНО
> Отсутствие контрольного шара может привести к тому, что двигатель застынет, что приведет к повреждению двигателя.

Термостат содержит два контрольных шара, чтобы пропускать воздух мимо термостата, когда он закрыт. Это помогает выпускать воздух во время процесса заполнения системы охлаждения.

> [!note] Примечание
> Некоторые внедорожные приложения используют термостат с одним чековым шаром. При замене термостата всегда используйте один и тот же номер детали. Хотя неправильный термостат будет физически исправен, это приведет к неправильной работе двигателя.

![[08d00094.png]]

### Тест на утечку

Если термостат подозревается в утечке, можно выполнить следующие шаги для проверки утечки.

Следующая проверка должна быть выполнена с термостатом, закрытым в течение 1 минуты работы двигателя.

Используйте электронный инструмент для мониторинга температуры охлаждающей жидкости. Температура охлаждающей жидкости должна быть менее 38 ° C \[100° F \], чтобы убедиться, что термостат не открывается во время испытания.

![[08d00099.png]]

Отсоедините верхний шланг радиатора от соединения с водоотводом.

Установите шланг такого же размера на водоотводное соединение. Он должен быть достаточно длинным, чтобы добраться до удаленного сухого контейнера, который будет использоваться для сбора охлаждающей жидкости.

Установите и затяните зажим шланга на выходном соединении.

Поместите другой конец шланга в сухой контейнер.

![[08900049.png]]

Температура охлаждающей жидкости должна контролироваться во время этого испытания, чтобы определить, достигает ли температура охлаждающей жидкости номинальной температуры открытия термостата. См. раздел Измерения этой процедуры для номинальной температуры открытия. Если термостат открывается во время этого испытания, то испытание является недействительным и должно быть повторено.

Работайте с двигателем при номинальной оборотах в течение 1 минуты.

Остановите двигатель и измерьте количество охлаждающей жидкости, собранной в контейнере.

Количество охлаждающей жидкости **не должно **превышать 100 куб.см. \[3.3 фл. унции\].

Если собрано более 100 куб.см \[3.3 fl oz\] теплоносителя, термостат протекает и должен быть заменен.

![[08d00100.png]]

### Подготовительные операции

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Чтобы снизить риск искрения, минусовой (-) провод аккумуляторной батареи снимайте первым, а подсоединяйте последним.

> [!danger] ОПАСНО
> Охлаждающая жидкость токсична. Хранить в недоступном для детей и животных месте. Если деталь не используется повторно, утилизируйте её по местным природоохранным требованиям.

> [!danger] ОПАСНО
> Не снимайте пробку радиатора с горячего двигателя. Снимайте пробку радиатора только после того, как температура охлаждающей жидкости опустится ниже 50 °C \[120 °F\]. Струя горячей охлаждающей жидкости или пар могут привести к травме.

> [!warning] ОСТОРОЖНО
> Используйте осторожность при сливе охлаждающей жидкости, чтобы охлаждающая жидкость не пролилась или не слилась в зону трюма. Не перекачивайте охлаждающую жидкость за борт. Если охлаждающая жидкость не используется повторно, она должна быть выброшена в соответствии с местными экологическими нормами.

- Отсоедините аккумуляторные батареи. См. руководство по обслуживанию производителя оригинального оборудования (OEM).
- Слить охлаждающую жидкость ниже уровня термостата. См. процедуру 008-018 в разделах 5 и 7.
- Отсоедините верхний шланг радиатора от водоотводного соединения. См. сервисное руководство изготовителя машины.

![[ck800wa.png]]

### Снятие

Удалите болты подключения к розетке.

Удалите соединение с водоотводом.

Удалите термостат.

![[08x00055.png]]

### Очистка и проверка при повторном использовании

> [!warning] ОСТОРОЖНО
> Не допускайте попадания обломков в полость термостата при очистке поверхностей прокладки. Повреждения системы охлаждения и двигателя могут произойти.

Очистите спаривающиеся поверхности абразивной подушкой, номером 3823258 или эквивалентом, и чистой тканью.

![[08d00369.png]]

Проверить термостат на предмет внешнего повреждения. Также проверьте наличие трещин, вложенного мусора, недостающих контрольных шаров, поврежденного сиденья и других повреждений.

Замените термостат, если обнаружены какие-либо повреждения.

![[08900044.png]]

### Измерение

Если предполагается, что термостат неисправен, следует измерить температуру открытия термостата, чтобы определить, функционирует ли термостат должным образом.

> [!note] Примечание
> Не позволяйте термостату или термометру касаться контейнера.

Приостановите термостат и термометр на 100°C[212°F] в емкости с водой.

![[08900045.png]]

Нагрейте воду и проверьте термостат следующим образом:

Термостат должен соответствовать следующим критериям:

82.2°C \[180°F\] Номинальный термостат температуры

| Температура открытия термостата |  |  |  |
|---|---|---|---|
|  | целий |  | Фаренгейт |
| Первоначальное открытие | 79.4 | Мин | 175 |
| 83.3 | Макс | 182 |  |
| Полностью открыт | 95 | Макс | 203 |

> [!note] Примечание
> Полностью открытый зазор между клапаном потока термостата и фланцевым клапаном должен быть не менее 9,1 мм \[0,36 дюйма \].

![[08d00054.png]]

### Установка

> [!warning] ОСТОРОЖНО
> Всегда используйте правильный термостат и не работайте с двигателем без установленного термостата. Двигатель может перегреться, если он работает без термостата, потому что путь наименьшего сопротивления для охлаждающей жидкости проходит через обход на входе насоса. Неправильный термостат может привести к перегреву двигателя или слишком холодному движению.

> [!note] Примечание
> Если используется ранее установленный термостат, убедитесь, что используется новый термостат.

Установите термостат в корпус термостата.

![[08d00101.png]]

Установите водоотводное соединение и крепежные болты.

Затяните болты.

> [!tip] Момент затяжки
> 10 Н·м [89 фунт-дюйм]

![[08x00055.png]]

### Завершающие операции

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Чтобы снизить риск искрения, минусовой (-) провод аккумуляторной батареи снимайте первым, а подсоединяйте последним.

> [!warning] ОСТОРОЖНО
> Всегда вентилируйте двигатель во время наполнения, чтобы удалить воздух из системы охлаждения, или может возникнуть перегрев.

- Подключите верхний шланг радиатора к соединению с водоотводом. См. сервисное руководство изготовителя машины.
- Подсоедините аккумуляторные батареи. См. сервисное руководство изготовителя машины.
- Заправьте систему охлаждения. См. процедуру 008-018 в разделах 5 и 7.
- Запустите двигатель и проверьте на отсутствие утечек.

![[ck800wa.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> The thermostat controls the engine coolant temperature. When the coolant temperature is below the operating range, engine coolant is bypassed back to the inlet of the water pump. When the engine coolant temperature reaches the operating range, the thermostat opens, seals off the bypass, and forces engine coolant to flow to the radiator or the heat exchanger.
>
> An incorrect or malfunctioning thermostat can cause the engine to run too hot or too cold.
>
> **CAUTION · Осторожно**
> Never operate the engine without a thermostat. Without a thermostat, the path of least resistance for the coolant is through the bypass to the water pump inlet. This can cause the engine to overheat.
>
> **CAUTION · Осторожно**
> A missing check ball can cause the engine to run cold, resulting in engine damage.
>
> The thermostat contains two check balls to vent air past the thermostat when it is closed. This helps to vent air during the cooling system fill process.
>
> **Note · Примечание**
> Some off-highway applications use a thermostat with one check ball. When replacing a thermostat, always be sure to use the same part number. Though an incorrect thermostat will physically fit, it will lead to improper engine operation.
>
> ### Leak Test
>
> If the thermostat is suspected to be leaking, the following steps can be performed to check for leakage.
>
> The following check **must** be performed with the thermostat closed for 1 minute of engine operation.
>
> Use an electronic service tool to monitor the coolant temperature. The coolant temperature should be less than 38°C \[100°F\] to make sure the thermostat does **not** open during the test.
>
> Disconnect the radiator top hose from the water outlet connection.
>
> Install a hose of the same size on the water outlet connection. It must be long enough to reach a remote, dry container that will be used to collect coolant.
>
> Install and tighten a hose clamp on the outlet connection.
>
> Place the other end of the hose in the dry container.
>
> The coolant temperature should be monitored during this test to determine if the coolant temperature reaches the nominal opening temperature of the thermostat. See the Measurement section of this procedure for nominal opening temperature. If the thermostat opens during this test, the test is invalid and **must** be repeated.
>
> Operate the engine at rated rpm for 1 minute.
>
> Stop the engine and measure the amount of coolant collected in the container.
>
> The amount of coolant **must not** be more than 100 cc \[3.3 fl oz\].
>
> If more than 100 cc \[3.3 fl oz\] of coolant is collected, the thermostat is leaking and **must** be replaced.
>
> ### Preparatory Steps
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> **WARNING · Опасно**
> Coolant is toxic. Keep away from children and pets. If not reused, dispose of in accordance with local environmental regulations.
>
> **WARNING · Опасно**
> Do not remove the pressure cap from a hot engine. Wait until the coolant temperature is below 50°C \[120°F\] before removing the pressure cap. Heated coolant spray or steam can cause personal injury.
>
> **CAUTION · Осторожно**
> Use caution when draining coolant that coolant is not spilled or drained into the bilge area. Do not pump the coolant overboard. If the coolant is not reused, it must be discarded in accordance with local environmental regulations.
>
> - Disconnect the batteries. Refer to the original equipment manufacturer (OEM) service manual.
> - Drain the coolant below the level of the thermostat. Refer to Procedure 008-018 in Sections 5 and 7.
> - Disconnect the upper radiator hose from the water outlet connection. Refer to the OEM service manual.
>
> ### Remove
>
> Remove the water outlet connection capscrews.
>
> Remove the water outlet connection.
>
> Remove the thermostat.
>
> ### Clean and Inspect for Reuse
>
> **CAUTION · Осторожно**
> Do not let any debris fall into the thermostat cavity when cleaning the gasket surfaces. Damage to the cooling system and engine can occur.
>
> Clean the mating surfaces with an abrasive pad, Part Number 3823258, or equivalent, and a clean cloth.
>
> Inspect the thermostat for external damage. Also inspect for cracks, embedded debris, missing check balls, damaged seat, and other damage.
>
> Replace the thermostat if any damage is found.
>
> ### Measure
>
> If the thermostat is suspected to be malfunctioning, the opening temperature of the thermostat should be measured to determine if the thermostat is functioning properly.
>
> **Note · Примечание**
> Do **not** allow the thermostat or thermometer to touch the container.
>
> Suspend the thermostat and a 100°C \[212°F\] thermometer in a container of water.
>
> Heat the water and check the thermostat as follows:
>
> The thermostat **must** meet the following criteria:
>
> 82.2°C \[180°F\] Nominal Temperature Thermostat
>
> | Thermostat Opening Temperature |  |  |  |
> |---|---|---|---|
> |  | celsius |  | fahrenheit |
> | Initial Opening | 79.4 | MIN | 175 |
> | 83.3 | MAX | 182 |  |
> | Fully Opened | 95 | MAX | 203 |
>
> **Note · Примечание**
> The fully open clearance between the thermostat flow valve and flange must be 9.1 mm \[0.36 in\] minimum.
>
> ### Install
>
> **CAUTION · Осторожно**
> Always use the correct thermostat and do not operate the engine without a thermostat installed. The engine can overheat if operated without a thermostat because the path of least resistance for the coolant is through the bypass to the pump inlet. An incorrect thermostat can cause the engine to overheat or run too cold.
>
> **Note · Примечание**
> If a previously installed thermostat is being used, make sure a new thermostat seal is used.
>
> Install the thermostat into the thermostat housing.
>
> Install the water outlet connection and mounting capscrews.
>
> Tighten the capscrews.
>
> **Момент затяжки · Torque Value**
> 10 n•m [89 in-lb]
>
> ### Finishing Steps
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> **CAUTION · Осторожно**
> Always vent the engine during filling to remove air from the coolant system, or overheating can result.
>
> - Connect the upper radiator hose to the water outlet connection. Refer to the OEM service manual.
> - Connect the batteries. Refer to the OEM service manual.
> - Fill the cooling system. Refer to Procedure 008-018 in Sections 5 and 7.
> - Operate the engine and check for leaks.
