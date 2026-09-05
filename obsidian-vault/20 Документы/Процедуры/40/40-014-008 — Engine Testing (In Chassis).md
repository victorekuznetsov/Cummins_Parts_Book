---
aliases:
  - "Испытание двигателя на машине"
type: "Процедура"
doc: "40-014-008"
title_en: "Engine Testing (In Chassis)"
title_ru: "Испытание двигателя на машине"
modified: "2006-04-24"
engines:
  - "93047320"
families:
  - "6B5.9"
manuals:
  - "3666087"
figures: 17
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/40/40-014-008.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/40-014-008.pdf"
tags:
  - "документ/процедура"
  - "двигатель/6B5.9"
  - "группа/40"
  - "перевод/машинный"
---

# Engine Testing (In Chassis)
**Испытание двигателя на машине**

> [!abstract] Процедура · `40-014-008`
> **Двигатели:** [[93047320 — 6B5.9 CPL 3111|93047320]]
> **Семейство:** 6B5.9
> **Входит в руководства:** [[3666087 — B3.9, B4.5, B4.5 RGT, and B5.9 Service Manual|3666087]]
> **Секции:** Section 14 - Engine Testing - Group 14
> **Даты:** изменён 2006-04-24
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/40/40-014-008.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/40-014-008.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Первичная проверка

Двигатели B3.9, B5.9 и B4.5

Удаление внутренних компонентов двигателя для диагностики сбоев требует много времени и затрат. Калибр сжатия и адаптер могут использоваться в качестве помощи в проверке на сбои.

![[oi900vp.png]]

Используйте калибр сжатия и адаптер для проверки следующих отказов компонентов:

1. Запечатывание кольца Пистона
2. Уплотнение впускного и выпускного клапанов
3. Уплотнение прокладки цилиндрической головки
4. Голова цилиндра треснула.

См. соответствующие процедуры замены неисправных компонентов.

![[kn9bdka.png]]

> [!note] Примечание
> Из-за таких переменных, как условия запуска и батареи, которые влияют на скорость вращения двигателя, трудно установить абсолютное значение давления сжатия; однако в качестве руководящих принципов могут использоваться следующие значения:

- Новый двигатель (скорость вращения @ 250 об/мин) 2413 кПа[350 psi]
- Используемый двигатель (скорость прокрутки @ 250 об/мин) 2068 кПа \[300 psi\].

Рекомендуется проверить давление сжатия на всех цилиндрах и затем сравнить с техническими характеристиками. Все цилиндры должны находиться в пределах 690 кПа[100 psi] друг от друга.

![[oi900kn.png]]

Пистонское кольцо Sealing

Если сжатие низкое, но может быть значительно увеличено путем впрыскивания масла в цилиндр, причиной является неадекватная уплотнение между кольцами и стенками цилиндра.

Видишь?[[40-001-054-tr — Piston and Connecting Rod Assembly|Процедура 001-054]]Замена поршневого кольца.

![[oi900ka.png]]

Уплотнение и выхлопная клапанная уплотнение

Если сжатие низкое на одном или нескольких несмежных цилиндрах, и давление может **не** быть увеличено путем смазывания колец, подозревается плохая уплотнение клапана.

Видишь?[[40-002-004-tr — Cylinder Head|Процедура 002-004]]Замена головки цилиндра.

![[oi900kb.png]]

Утечка клапанов часто является слышимым звуком из впускных и выхлопных коллекторов.

![[oi900kc.png]]

Запечатывание цилиндрической головки

Если сжатие низкое на соседних цилиндрах, и давление может **не** быть увеличено путем смазывания колец, прокладка головки цилиндра, вероятно, протекает между цилиндрами.

Видишь?[[40-002-021-tr — Cylinder Head Gasket|Процедура 002-021]]Замена прокладки цилиндров.

![[oi900kd.png]]

> [!note] Примечание
> Низкое сжатие на одном цилиндре может быть вызвано внешней утечкой или утечкой в проход охлаждающей жидкости. Утечка в проход охлаждающей жидкости такой величины также приведет к образованию охлаждающей жидкости в цилиндре.

![[oi900ke.png]]

Утечка сжатия в охлаждающую жидкость обычно обнаруживается потерей охлаждающей жидкости, когда охлаждающая жидкость выдувается из системы охлаждения.

Совет по обслуживанию: Удалите приводной ремень из водяного насоса. Видишь?[[40-008-002-tr — Drive Belt, Cooling Fan|Процедура 008-002]]для снятия и установки приводного ремня.

Запускайте двигатель в течение одной-двух минут и проверяйте, чтобы охлаждающая жидкость выдувалась из радиатора с помощью сжатия газов.

![[oi900kf.png]]

Двигатели B4.5 RGT

Для двигателей B4.5 RGT не доступны инструменты службы сжатия. Для проверки на потерю сжатия следует провести проверку на удар. Видишь?[[100-014-010 — Crankcase Blowby, Measure|Процедура 014-010]].

![[nobox.png]]

### Проверка

> [!note] Примечание
> Нагрузка сжатого воздуха в сопроводительной иллюстрации должна быть прикреплена к выходу воздушного компрессора (2).

Убедитесь, что воздушный компрессор будет разгружен во время проверки производительности.

Применять регулируемое давление воздуха 655 кПа[95 psi] к разгрузчику воздушного компрессора (1).

![[cp900va.png]]

> [!warning] ОСТОРОЖНО
> Не запускайте двигатель более 30 секунд. Избыточное тепло повредит стартовый двигатель.

Прокрутите двигатель и наблюдайте давление масла при запуске двигателя. Если двигатель не запускается в течение 30 секунд, позвольте стартовому двигателю остыть в течение двух минут, прежде чем снова запустить двигатель.

![[st8bdba.png]]

> [!warning] ОСТОРОЖНО
> Если давление моторного масла не соответствует спецификациям, немедленно выключите двигатель. Низкое давление моторного масла приведет к повреждению двигателя. Исправьте проблему, если давление моторного масла не соответствует спецификациям.

Давление моторного масла двигателя должно быть не менее 69 кПа \[10 psi\] при приблизительно 700 об/мин.

![[oi902vv.png]]

> [!note] Примечание
> Показатели мощности будут **не** быть точными, если температура моторного масла и температура топлива **не** в пределах спецификаций.

Убедитесь, что двигатель находится при рабочей температуре.

Переместить рычаг дроссельной заслонки в положение «полностью открыт». Регулируйте нагрузку на динамометр до тех пор, пока двигатель не выдержит номинальную оборотную силу.

Позволяйте показаниям стабилизироваться. Читайте о лошадиных силах.

Проверьте все датчики и запишите показания.

| Измерения |  |  |
|---|---|---|
|  | целий | Фаренгейт |
| Температура моторного масла | 90 | 194 |

| Измерения |  |  |
|---|---|---|
|  | целий | Фаренгейт |
| Температура топлива | 32 | 90 |

![[oi901vt.png]]

> [!warning] ОСТОРОЖНО
> Не выключайте двигатель сразу после его загрузки. Необходимо дать ему достаточно остыть. Невыполнение этого требования приведет к повреждению двигателя.

> [!note] Примечание
> Следует избегать периодов простоя, превышающих пять минут.

Снимите нагрузку на динамометр полностью и работайте с двигателем на холостом ходу в течение трех-пяти минут. Это позволит охладить турбокомпрессор и другие компоненты.

![[oi804vm.png]]

Выключите двигатель после периода охлаждения.

![[oi802vx.png]]

> [!note] Примечание
> Если двигатель должен храниться временно и не имеет постоянного антифриза, необходимо слить всю охлаждающую жидкость.

Удалите все измерительные приборы.

Удалите двигатель с динамометра.

![[bp9gama.png]]


> [!quote]- Original (English) · английский оригинал
> ### Initial Check
>
> B3.9, B5.9, and B4.5 Engines
>
> It is very time consuming and expensive to remove internal engine components to diagnose failures. A compression gauge and adapter can be used as an aid in checking for failures.
>
> Use the compression gauge and adapter to check for following component failures:
>
> 1. Piston ring sealing
> 2. Intake and exhaust valve sealing
> 3. Cylinder head gasket sealing
> 4. Cylinder head cracked.
>
> See the appropriate procedures for the replacement of failed components.
>
> **Note · Примечание**
> Due to variables such as starter and battery conditions that affect engine cranking speed, it is difficult to establish an absolute value for compression pressure; however, the following values can be used as guidelines:
>
> - New engine (cranking speed @ 250 rpm) 2413 kPa \[350 psi\]
> - Used engine (cranking speed @ 250 rpm) 2068 kPa \[300 psi\].
>
> It is recommended that the compression pressure be checked on all cylinders and then compared to specification. All cylinders **must** be within 690 kPa \[100 psi\] of each other.
>
> Piston Ring Sealing
>
> If the compression is low but can be increased significantly by squirting oil into the cylinder, the cause is inadequate sealing between the rings and the cylinder walls.
>
> Refer to [[40-001-054-tr — Piston and Connecting Rod Assembly|Procedure 001-054]] for piston ring replacement.
>
> Intake and Exhaust Valve Sealing
>
> If the compression is low on one or more nonadjacent cylinders, and the pressure can **not** be increased by oiling the rings, poor valve sealing is suspected.
>
> Refer to [[40-002-004-tr — Cylinder Head|Procedure 002-004]] for cylinder head replacement.
>
> Valve leakage is often an audible sound from the intake and exhaust manifolds.
>
> Cylinder Head Gasket Sealing
>
> If the compression is low on adjacent cylinders, and the pressure can **not** be increased by oiling the rings, the cylinder head gasket is probably leaking between the cylinders.
>
> Refer to [[40-002-021-tr — Cylinder Head Gasket|Procedure 002-021]] for cylinder gasket replacement.
>
> **Note · Примечание**
> Low compression on a single cylinder can be caused by an external leak or a leak to a coolant passage. A leak to a coolant passage of this magnitude will also result in coolant in the cylinder.
>
> A compression leak to the coolant will normally be detected by a loss of coolant as the coolant is blown from the cooling system.
>
> Service Tip: Remove the drive belt from the water pump. Refer to [[40-008-002-tr — Drive Belt, Cooling Fan|Procedure 008-002]] for removal and installation of drive belt.
>
> Run the engine for one to two minutes, and check for coolant being blown from the radiator by compression gases.
>
> B4.5 RGT Engines
>
> For B4.5 RGT engines, no compression service tools are available. To inspect for loss of compression, a blow-by check should be performed. Refer to [[100-014-010 — Crankcase Blowby, Measure|Procedure 014-010]].
>
> ### Test
>
> **Note · Примечание**
> The compressed air load in the accompanying illustration **must** be attached to the air compressor outlet (2).
>
> Make sure the air compressor will be unloaded during the performance check.
>
> Apply regulated air pressure of 655 kPa \[95 psi\] to the air compressor unloader (1).
>
> **CAUTION · Осторожно**
> Do not crank the engine for more than 30 seconds. Excessive heat will damage the starting motor.
>
> Crank the engine and observe the oil pressure when the engine starts. If the engine fails to start within 30 seconds, allow the starting motor to cool for two minutes before cranking the engine again.
>
> **CAUTION · Осторожно**
> If the lubricating oil pressure is not within specifications, shut off the engine immediately. Low lubricating oil pressure will cause engine damage. Correct the problem if lubricating oil pressure is not within specifications.
>
> Engine lubricating oil pressure **must** be at least 69 kPa \[10 psi\] at approximately 700 rpm.
>
> **Note · Примечание**
> The horsepower readings will **not** be accurate if the lubricating oil temperature and fuel temperature are **not** within specifications.
>
> Make sure the engine is at operating temperature.
>
> Move the throttle lever to the FULL-OPEN position. Adjust the dynamometer load until the engine maintains the rated rpm.
>
> Allow the readings to stabilize. Read the horsepower.
>
> Check all gauges, and record the readings.
>
> | Measurements |  |  |
> |---|---|---|
> |  | celsius | fahrenheit |
> | Lubricating Oil Temperature | 90 | 194 |
>
> | Measurements |  |  |
> |---|---|---|
> |  | celsius | fahrenheit |
> | Fuel Temperature | 32 | 90 |
>
> **CAUTION · Осторожно**
> Do not shut off the engine immediately after it has been loaded. It must be allowed to cool sufficiently. Failure to do so will result in engine damage.
>
> **Note · Примечание**
> Idle periods longer than five minutes are to be avoided.
>
> Remove the dynamometer load completely, and operate the engine at idle speed for three to five minutes. This will allow the turbocharger and other components to cool.
>
> Shut off the engine after the cool-down period.
>
> **Note · Примечание**
> If the engine is to be stored temporarily and does **not** have permanent-type antifreeze, it is necessary to drain all coolant.
>
> Remove all test instrumentation.
>
> Remove the engine from the dynamometer.
