---
aliases:
  - "Обкатка двигателя (на стенде с беговыми барабанами)"
type: "Процедура"
doc: "20-014-003"
title_en: "Engine Run-in (Chassis Dynamometer)"
title_ru: "Обкатка двигателя (на стенде с беговыми барабанами)"
modified: "2006-06-30"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4021592"
figures: 13
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/20/20-014-003.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/20-014-003.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/20"
  - "перевод/машинный"
---

# Engine Run-in (Chassis Dynamometer)
**Обкатка двигателя (на стенде с беговыми барабанами)**

> [!abstract] Процедура · `20-014-003`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021592 — QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual|4021592]]
> **Секции:** Section 14 - Engine Testing - Group 14
> **Даты:** изменён 2006-06-30
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/20/20-014-003.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/20-014-003.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

> [!warning] ОСТОРОЖНО
> Система моторного масла должна быть заряжена перед работой двигателя после реконструкции, чтобы избежать повреждения внутренних компонентов. Не загружайте систему из обходного фильтра, так как фильтр будет поврежден.

Удалите большую пробку из корпуса масляного охладителя.

![[14400011.png]]

Используйте насос, способный подавать 207 кПа \[30 psi\] непрерывного давления. Подключите насос к передней части охладителя моторного масла, как показано.

Используйте запас чистого масла. Поверните насос в положение ON. Проверьте датчик давления масла в двигателе. Когда калибр указывает на давление масла, начните мониторинг уровня масла в масляной кастрюле.

![[pl4hoha.png]]

Проверьте уровень моторного масла двигателя, чтобы убедиться, что оно заполнено до нужного уровня.

![[oi8dsva.png]]

Проверьте уровень охлаждающей жидкости двигателя, чтобы убедиться, что он заполнен до надлежащего уровня. См. процедуру[[20-008-018-tr — Cooling System|008-018]].

> [!danger] ОПАСНО
> Не снимайте пробку радиатора с горячего двигателя. Снимайте пробку радиатора только после того, как температура охлаждающей жидкости опустится ниже 50 °C \[120 °F\]. Нагретый спрей охлаждающей жидкости или системный пар может привести к травмам.

> [!warning] ОСТОРОЖНО
> Не добавляйте холодную охлаждающую жидкость в горячий двигатель. Это может привести к повреждению литья двигателя. Позвольте двигателю охладиться до температуры ниже 50°C \[120°F\] перед добавлением охлаждающей жидкости.

![[ra200sa.png]]

Используйте известный источник дизельного топлива № 2 хорошего качества.

Это очень важно, поскольку дизельное топливо № 1, наряду с большинством других альтернативных видов топлива, легче (более низкая удельная гравитация, более высокая гравитация API), чем дизельное топливо № 2. Чем легче топливо, тем ниже содержание энергии (BTU) на галлон (литр и т.д.).

![[nobox.png]]

### Запуск инструкций

См. динамометр шасси - операция, процедура[[20-014-002-tr — Engine Testing (Chassis Dynamometer)|014-002]]Для общих операционных процедур и мер безопасности.

![[oi100vo.png]]

Используйте эту диаграмму для определения испытательной нагрузки.

Пример: Испытательная нагрузка для двигателя мощностью 475 л.с., рассчитанного на 2000 об/мин с 15-процентным увеличением крутящего момента, составляет 225 футов в фунтах.

> [!note] Примечание
> Эта диаграмма предполагает, что постоянная динамометра составляет 5252. Если постоянная динамометра составляет **не**5252, то для определения правильной испытательной нагрузки используйте следующую формулу:

Правильная испытательная нагрузка = (константа динамометра) x (испытательная нагрузка) /d 5252.

Пример: Константа динамометра для испытания двигателя в приведенном выше примере составляет 4000.

Правильная испытательная нагрузка = (4000 x 225) /d 5252 = 171 фут-лб.

> [!note] Примечание
> Эта диаграмма предполагает включение автомобиля на динамометрическом шасси.

| RPM Rating RPM | Рейтинг лошадиных сил | Восстание крутящего момента | Испытательная нагрузка |
|---|---|---|---|
| 1200 | Все | Все | 305 Н•м \[225 фунт-фут\] |
| 1500 | Все | Все | 305 Н•м \[225 фунт-фут\] |
| 1800 | 0 до 499 | Все | 305 Н•м \[225 фунт-фут\] |
| 1800 | 500 и выше | Все | 380 Н•м[280 фунт-фут] |
| 1900 | 0 до 474 | Все | 305 Н•м \[225 фунт-фут\] |
| 1900 | 475 и выше | Все | 380 Н•м[280 фунт-фут] |
| 2000 | 0 до 499 | 0-24% | 305 Н•м \[225 фунт-фут\] |
| 2000 | 0 до 499 | 25% и выше | 380 Н•м[280 фунт-фут] |
| 2000 | 500 и выше | Все | 380 Н•м[280 фунт-фут] |
| 2100 | 0 до 474 | 0 - 32% | 305 Н•м \[225 фунт-фут\] |
| 2100 | 0 до 474 | 33% плюс | 305 Н•м \[225 фунт-фут\] |
| 2100 | 475-530 до 575 | От 0 до 15% | 305 Н•м \[225 фунт-фут\] |
| 2100 | 475-530 до 575 | 16% и выше | 380 Н•м[280 фунт-фут] |
| 2100 | 531-649 | Все | 380 Н•м[280 фунт-фут] |
| 2100 | 650 и выше | Все | 405 Н•м \[300 футов-лб\] |

Настройка двигателя rpm до 1200 rpm. Нагрузка динамометра должна быть отрегулирована до испытательной нагрузки, как определено ранее. Работайте с двигателем при этой установке до тех пор, пока температура охлаждающей жидкости не покажет 71 ° C \[160° F \].

Проверьте на отсутствие утечек. Исправь все утечки.

Проверьте все датчики и запишите показания.

**Не** переходите к следующему шагу, пока продувка не станет стабильной в пределах спецификаций.

![[oi800vk.png]]

Настройка оборотов двигателя на пиковый крутящий момент оборотов. Нагрузка динамометра должна быть в два раза больше испытательной нагрузки.

Работайте с двигателем при этой нагрузке в течение 2 минут.

Проверьте все датчики и запишите показания.

**Не** переходите к следующему шагу, пока продувка не станет стабильной в пределах спецификаций.

![[oi800vl.png]]

Поддерживайте обороты двигателя на пике крутящего момента оборотов в минуту. Увеличить нагрузку на динамометр до трехкратной испытательной нагрузки.

Работайте с двигателем при этой нагрузке в течение 2 минут.

Проверьте все датчики и запишите показания.

**Не** переходите к следующему шагу, пока продувка не станет стабильной в пределах спецификаций.

![[oi800vm.png]]

Переместить рычаг дроссельной заслонки в полностью открытое положение. Увеличьте нагрузку до тех пор, пока обороты двигателя не достигнут пикового крутящего момента оборотов в минуту.

Работайте с двигателем в этой установке в течение 10 минут или до тех пор, пока продувка не станет стабильной в соответствии со спецификациями.

Проверьте все датчики и запишите показания.

![[oi800vn.png]]

Уменьшите нагрузку на динамометр до тех пор, пока обороты двигателя не увеличатся до номинальной RPM.

Работайте с двигателем при этой нагрузке в течение 5 минут.

Проверьте все датчики и запишите показания.

![[oi800vo.png]]

Полностью снизить нагрузку на динамометр.

> [!warning] ОСТОРОЖНО
> Не выключайте двигатель немедленно. Двигатель должен быть охлажден или может возникнуть повреждение турбокомпрессора.

Переведите рычаг дроссельной заслонки в положение LOW IDLE. Работайте с двигателем в этой установке в течение 3-5 минут. Это позволит охладить турбокомпрессор и другие компоненты двигателя.

> [!warning] ОСТОРОЖНО
> Не используйте двигатель в IDLE дольше, чем указано. Чрезмерное образование углерода может привести к повреждению двигателя.

![[oi800vj.png]]

Выключите двигатель.

![[oi800vp.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> **CAUTION · Осторожно**
> The lubricating oil system must be primed before operating the engine after rebuild to avoid internal component damage. Do not prime the system from the bypass filter, as the filter will be damaged.
>
> Remove the large plug from the oil cooler housing.
>
> Use a pump capable of supplying 207 kPa \[30 psi\] continuous pressure. Connect the pump to the front of the engine oil cooler as shown.
>
> Use a supply of clean oil. Turn the pump to the ON position. Check the engine oil pressure gauge. When the gauge indicates oil pressure, begin monitoring the oil level in the oil pan.
>
> Check the engine lubricating oil level to be sure it is filled to the proper level.
>
> Check the engine coolant level to make sure it is filled to the proper level. Refer to Procedure [[20-008-018-tr — Cooling System|008-018]].
>
> **WARNING · Опасно**
> Do not remove the pressure cap from a hot engine. Wait until the coolant temperature is below 50°C \[120°F\] before removing the pressure cap. Heated coolant spray or system steam can cause personal injury.
>
> **CAUTION · Осторожно**
> Do not add cold coolant to a hot engine. This can cause engine casting damage. Allow the engine to cool to below 50°C \[120°F\] before adding coolant.
>
> Use a known source of good quality Number 2 diesel fuel.
>
> This is very important since Number 1 diesel fuels, along with most other alternate fuels, are lighter (lower specific gravity, higher API gravity) than Number 2 diesel fuel. The lighter the fuel, the lower the energy content (BTU) per gallon (liter, etc.).
>
> ### Run-In Instructions
>
> Refer to Chassis Dynamometer - Operation, Procedure [[20-014-002-tr — Engine Testing (Chassis Dynamometer)|014-002]], for general operating procedures and safety precautions.
>
> Use this chart to determine the test load.
>
> Example: The test load for a 475 HP engine rated at 2000 rpm with a 15 percent torque rise is 225 ft-lb.
>
> **Note · Примечание**
> This chart assumes the dynamometer constant is 5252. If the dynamometer constant is **not** 5252, use the following formula to determine the correct test load:
>
> Correct test load = (Dynamometer constant) x (Test load) /d 5252.
>
> Example: The dynamometer constant for testing the engine in the above example is 4000.
>
> Correct test load = (4000 x 225) /d 5252 = 171 ft-lb.
>
> **Note · Примечание**
> This chart assumes vehicle run-in on a chassis dynamometer.
>
> | Rated RPM | Rated Horsepower | Torque Rise | Test Load |
> |---|---|---|---|
> | 1200 | All | All | 305 N•m \[225 ft-lb\] |
> | 1500 | All | All | 305 N•m \[225 ft-lb\] |
> | 1800 | 0 to 499 | All | 305 N•m \[225 ft-lb\] |
> | 1800 | 500 and ABOVE | All | 380 N•m \[280 ft-lb\] |
> | 1900 | 0 to 474 | All | 305 N•m \[225 ft-lb\] |
> | 1900 | 475 and ABOVE | All | 380 N•m \[280 ft-lb\] |
> | 2000 | 0 to 499 | 0 to 24% | 305 N•m \[225 ft-lb\] |
> | 2000 | 0 to 499 | 25% and ABOVE | 380 N•m \[280 ft-lb\] |
> | 2000 | 500 and ABOVE | All | 380 N•m \[280 ft-lb\] |
> | 2100 | 0 to 474 | 0 to 32% | 305 N•m \[225 ft-lb\] |
> | 2100 | 0 to 474 | 33% Plus | 305 N•m \[225 ft-lb\] |
> | 2100 | 475 to 530 | 0 to 15% | 305 N•m \[225 ft-lb\] |
> | 2100 | 475 to 530 | 16% and ABOVE | 380 N•m \[280 ft-lb\] |
> | 2100 | 531 to 649 | All | 380 N•m \[280 ft-lb\] |
> | 2100 | 650 and ABOVE | All | 405 N•m \[300 ft-lb\] |
>
> Adjust the engine rpm to 1200 rpm. Adjust the dynamometer load to the test load as previously determined. Operate the engine at this setting until the coolant temperature indicates 71°C \[160°F\].
>
> Check for leaks. Fix all leaks.
>
> Check all of the gauges and record the readings.
>
> Do **not** proceed to the next step until the blowby becomes stable within specifications.
>
> Adjust the engine rpm to the torque peak rpm. Adjust the dynamometer load to equal two times the test load.
>
> Operate the engine at this load for 2 minutes.
>
> Check all the gauges and record the readings.
>
> Do **not** proceed to the next step until the blowby becomes stable within specifications.
>
> Maintain the engine rpm at torque peak rpm. Increase the dynamometer load to equal three times the test load.
>
> Operate the engine at this load for 2 minutes.
>
> Check all the gauges and record the readings.
>
> Do **not** proceed to the next step until the blowby becomes stable within specifications.
>
> Move the throttle lever to the FULL OPEN position. Increase the load until the engine rpm is at torque peak rpm.
>
> Operate the engine at this setting for 10 minutes or until the blowby becomes stable within specifications.
>
> Check all the gauges and record the readings.
>
> Decrease the dynamometer load until the engine rpm increases to the rated RPM.
>
> Operate the engine at this load for 5 minutes.
>
> Check all the gauges and record the readings.
>
> Decrease the dynamometer load completely.
>
> **CAUTION · Осторожно**
> Do not turn the engine OFF immediately. The engine must be allowed to cool or damage to the turbocharger may result.
>
> Move the throttle lever to the LOW IDLE position. Operate the engine at this setting for 3 to 5 minutes. This will allow the turbocharger and the other engine components to cool.
>
> **CAUTION · Осторожно**
> Do not operate the engine at IDLE longer than specified. Excessive carbon formation can cause engine damage.
>
> Turn the engine OFF.
