---
type: "Процедура"
doc: "40-005-037-tr"
title_en: "Fuel Pump Timing"
modified: "2007-06-22"
engines:
  - "93047320"
families:
  - "6B5.9"
manuals:
  - "3666087"
figures: 30
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/40/40-005-037-tr.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/40-005-037-tr.pdf"
tags:
  - "документ/процедура"
  - "двигатель/6B5.9"
  - "группа/40"
  - "перевод/машинный"
---

# Fuel Pump Timing

> [!abstract] Процедура · `40-005-037-tr`
> **Двигатели:** [[93047320 — 6B5.9 CPL 3111|93047320]]
> **Семейство:** 6B5.9
> **Входит в руководства:** [[3666087 — B3.9, B4.5, B4.5 RGT, and B5.9 Service Manual|3666087]]
> **Секции:** Section 5 - Fuel System - Group 05
> **Даты:** изменён 2007-06-22
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/40/40-005-037-tr.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/40-005-037-tr.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Время откачки до двигателя чрезвычайно важно. Время выключения насоса, которое выключено только на несколько градусов коленчатого вала, вызовет:

1. Плохая производительность — старт и мощность.
2. Чрезмерный дым.
3. Плохая экономия топлива.

![[oi901vm.png]]

### Время

Время работы насоса двигателя начинается с момента включения приводной передачи насоса впрыска топлива в распределительную передачу.

Первым шагом является расположение TDC хода сжатия для цилиндра № 1.

Затем, в зависимости от конфигурации двигателя, альфа-символ на приводной передаче насоса для впрыска, возможно, потребуется выровнять с отметкой на распределительной передаче.

![[it900wa.png]]

Эта таблица **должна** использоваться для поддержания правильного времени впрыска топлива насосом в двигатель. Номер списка контрольных частей (CPL) на табличке с данными двигателя и руководство по списку контрольных частей, бюллетень 3379133 или 4021327, должны использоваться для определения того, сертифицирован ли двигатель, и если да, то в каком году и регулирующее агентство (EPA или CARB).

Учитывая эту информацию, используйте следующую таблицу, чтобы определить, какая буква на приводе насоса впрыска топлива выровнена с приводом распределительного вала.

> [!note] Примечание
> Выравнивание маркировки времени не требуется для встроенной приводной передачи Nippondenso EP-9 или Bosch®.

> [!note] Примечание
> Знаки времени не требуются для Bosch® VE и DP210, используемых на промышленных двигателях Tier II. Для этих двигателей, варьируйте время, используя процедуру проверки времени.

| Оригинальное название: Pump Gear | Модель двигателя | Насос для инъекций | Сертификация |
|---|---|---|---|
| А. | 4B3.9, 4BT3.9 | насос из станадина | несертифицированный |
| А. | 4B3.9, 4BT3.9, 4BTA3.9 | Lucas CAV DPA насос | Все несертифицированные |
| B | 4B3.9, 4BTA3.9 | Bosch® VE | 1986, 1987 EPA, Все до 1986, Все не сертифицированы |
| C | 6BT5.9, 6BTA5.9 | Bosch® VE | 1986, 1987 EPA, Все до 1986, Все несертифицированные, CPL 600 |
| D | 6B5.9, 6BT5.9 | Станадин | несертифицированный |
| D | 6B5.9, 6BT5.9, 6BTA5.9 | Лукас Кав ДПА | Все несертифицированные |
| Е | 6BT5.9, 6BTA5.9 | Bosch® VE | 1986, 1987, 1988, 1989, 1990, 1991, 1992 CARB |
| F | 4BT3.9, 4BTA3.9 | Bosch® VE | 1986, 1987, 1988, 1989, 1990, 1991, 1992 CARB, 1988, 1989, 1990, 1991, 1992 EPA |
| GGG | 6BTA5.9 | Лукас Кав ДПА | Все пожарные насосы |
| Hе | Не используется в настоящее время | Не применяется | Не применяется |

Чтобы убедиться, что насос для впрыска топлива правильно рассчитан, сначала проверьте знаки выравнивания на фланце насоса и коробке передач.

> [!note] Примечание
> 1 мм вращения за отметкой времени будет продвигаться или замедлять (в зависимости от направления вращения) время насоса на 1 градус.

![[it900wc.png]]

Lucas CAV DPA, DPS, Delphi DP210, Stanadyne DB4 и насосы для впрыска топлива Bosch® VE имеют положение для блокировки вала насоса в положении, соответствующем верхней мертвой точке цилиндра № 1. Новые и восстановленные топливные насосы для впрыска топлива должны быть получены с валами, расположенными в этом положении.

![[fp9shwb.png]]

В точке впрыска ключ вала будет выровнен с клапаном подачи, принимающим впрыск, и проиллюстрированным хеш-меткой на корпусе уплотнения.

> [!note] Примечание
> Проиллюстрированная отметка предназначена для справки **только **и не должна использоваться для установки времени впрыска топливного насоса.

![[fp9shwc.png]]

Клапан подачи цилиндров № 1 обозначен как проиллюстрированный.

Четыре цилиндра = А

Шесть цилиндров = D

| Огнестрельное предписание |  |
|---|---|
| Четыре цилиндра | Шесть цилиндров |
| A = 1 | D = 1 |
| B = 3 | E = 5 |
| C = 4 | F = 3 |
| D = 2 | A = 6 |
|  | B = 2 |
|  | C = 4 |

![[fp9pgga.png]]

Двигатель оснащен штифтом блокировки коленчатого вала для определения верхней мёртвой точки (TDC) для цилиндра № 1.

![[cg9gega.png]]

> [!warning] ОСТОРОЖНО
> Если штифт блокировки коленчатого вала неправильно расположен на корпусе зубчатой передачи, насос не будет правильно рассчитан по времени.

После точного определения TDC для цилиндра № 1, завод размещает блокировочный штифт коленчатого вала в корпусе передач, используя штифт блокировки коленчатого вала и отверстие в распределительной шестерне. Если корпус зубчатой коробки или фиксатор ВМТ сняты, то для его перемещения требуется такая же точность.

Если фиксатор ВМТ сборка расположена неправильно, переставьте штифт блокировки коленчатого вала.

![[cg9gewa.png]]

Фланец сменного насоса должен быть маркирован так, чтобы он соответствовал отметке на корпусе передач после установки.

Во время производства, после того, как заблокированный насос установлен на двигателе с цилиндром № 1 в верхней мертвой точке (TDC), на корпусе зубчатой коробки и фланце насоса проставляется отметка. После этого, когда эти метки выровнены, насос правильно приурочен к двигателю.

> [!note] Примечание
> Отметки на корпусе зубчатой передачи и фланце насоса уникальны для каждого двигателя.

![[fp900wl.png]]

См. Инструкцию по инструменту обслуживания, Бюллетень 3400196 и Каталог инструментов обслуживания, Бюллетень 3377710 для определения соответствующего инструмента времени Bosch® и номеров деталей комплекта адаптера.

Специальный индикатор может использоваться для измерения положения плунжера насоса впрыска топлива Bosch® VE для проверки времени работы насоса.

![[fs900wn.png]]

Stanadyne DB4 Fuel Injection Pump Timing (Тарифный впрыск топлива)

Очистите все обломки вокруг крышки окна впрыска топливного насоса.

![[ip900ea.png]]

Удалите крышку синхронизации насоса для впрыска топлива.

![[ip9cvmb.png]]

Вращайте вал впрыска топлива в направлении вращения насоса, чтобы выровнять линию времени на концентраторе удерживающего веса с линией на кулачном кольце.

![[ip900wb.png]]

Поместите вал впрыска топлива, запирающий ключ в заблокированном положении. Включите запирающий винт до тех пор, пока не будет установлен контакт с валом привода.

> [!tip] Момент затяжки
> 11.9 Н·м [105 фунт-дюйм]

![[ip9waha.png]]

Проверьте, выровнены ли временные метки после того, как время заблокировано.

![[ip900wb.png]]

Установите крышку синхронизации насоса для впрыска топлива.

![[ip9cvmb.png]]

CAV DPA/DPS Тормоз для впрыска топлива

Правильное время работы насоса для впрыска топлива Lucas CAV DPA/DPS можно проверить, удалив контрольную табличку.

> [!note] Примечание
> Специальное оборудование в авторизованном цехе требуется для точного времени впрыска топлива Lucas CAV DPA. Однако для устранения неполадок и в чрезвычайной ситуации визуальное выравнивание метки времени достаточно близко для работы двигателя.

Обе эти проверки описаны в замене насоса для впрыска топлива.[[40-005-012-tr — Fuel Injection Pumps, In-Line|См. процедуру 005-012 (насосы для инъекций топлива, в линию) в разделе 5.]]

[[40-005-014-tr — Fuel Injection Pump, Rotary|См. процедуру 005-014 (насосы для инъекций топлива, ротационные) в разделе 5.]]

[[40-005-013 — Fuel Injection Pump, In-Line, Spill Port Timing|См. процедуру 005-013 (насосы для инъекций топлива, In-Line, время разлива порта) в разделе 5 для установки штифта блокировки коленчатого вала.]]

![[ap9plwa.png]]

Проверка времени (Bosch® VE Pump)

Поверните коленчатый вал в верхняя мёртвая точка (TDC).

![[cg9piwa.png]]

Удалите пробку с конца насоса.

![[fp9pxma.png]]

> [!warning] ОСТОРОЖНО
> Не перегибайте топливные линии. Это может привести к отказу топливной системы.

См. Инструкцию по инструменту обслуживания, Бюллетень 3400196 и Каталог инструментов обслуживания, Бюллетень 3377710 для определения соответствующего инструмента времени Bosch® и номеров деталей комплекта адаптера.

Установите индикатор времени. Обязательно допустите адекватные поездки для индикатора.

Для установки индикатора времени часто необходимо отсоединить одну или несколько топливных линий от топливного насоса.

> [!note] Примечание
> Индикатор помечается шагом 0,01 мм. 1 оборот иглы индикатора равен 0,50 мм.

![[fp9towa.png]]

Задний вал коленчатого вала в направлении, противоположном вращению двигателя, пока игла индикатора не перестанет двигаться. Настройте индикатор лицом, чтобы прочитать 0.

Поверните коленчатый вал обратно в верхняя мёртвая точка (TDC) и посчитайте количество оборотов иглы индикатора. Считывание, показанное при включении штифта блокировки коленчатого вала, представляет собой количество плунжерного подъема, которое насос имеет в этой точке.

![[er900wg.png]]

Насосы Bosch® VE со слоцированными монтажными отверстиями

Поверните насос на крепежные шпильки до тех пор, пока индикатор не считывает правильное значение для подъема плунжера. Эта иллюстрация дает пример показаний индикатора для различных значений подъема плунжера.

Затяните фланцевые крепежные гайки.

> [!tip] Момент затяжки
> 24 Н·м [18 фунт-фут]

![[fp900wm.png]]

Насосы Bosch® VE с круглыми монтажными отверстиями

Вращайте двигатель до тех пор, пока плунжер не окажется в нужном месте.

Заблокируйте топливный насос.[[40-005-014-tr — Fuel Injection Pump, Rotary|См. процедуру 005-014 (насосы для инъекций топлива, ротационные) в разделе 5.]]

![[05900806.png]]

Отделите приводную передачу топливного насоса от вала насоса.[[40-005-014-tr — Fuel Injection Pump, Rotary|См. процедуру 005-014 (насосы для инъекций топлива, ротационные) в разделе 5]]

С запирающимся насосом поверните двигатель обратно в TDC.

![[05900807.png]]

Закрутите гайку топливного насоса.[[40-005-014-tr — Fuel Injection Pump, Rotary|См. процедуру 005-014 (насосы для инъекций топлива, ротационные) в разделе 5.]]

Разблокируйте топливный насос.

Проверить правильность времени удалось путем измерения статического времени.

![[fp9nuhd.png]]

Удалите индикатор времени. Установите вилку.

> [!tip] Момент затяжки
> 10 Н·м [89 фунт-дюйм]

![[fp9toma.png]]

Насосное время - Lucas CAV DPA, Stanadyne DB4, Delphi DP210, Nippondenso EP-9 и Bosch® P7100

Поверните двигатель в верхняя мёртвая точка (TDC).

![[cg9piwa.png]]

Правильное время работы насоса для впрыска топлива Lucas CAV DPA и Stanadyne DB4 можно проверить, удалив пластину с временной оконной крышкой.

Насосы для впрыска топлива Nippondenso EP-9 и Bosch® P-7100 проверяются путем удаления запирающего штифта коленчатого вала и проверки прорези в штифте, которая будет помещаться на зубе синхронизации в насосе для впрыска топлива.

> [!note] Примечание
> Специальное оборудование в авторизованном цехе требуется для точного времени впрыска топлива Lucas CAV DPA. Однако для устранения неполадок и в чрезвычайной ситуации визуальное выравнивание метки времени достаточно близко для работы двигателя.

Чтобы исправить время на Bosch P-7100 и Nippondenso EP-9, см. процедуру замены соответствующего насоса.

![[fp900wn.png]]

Два индикатора времени впрыска насоса используются на Stanadyne DB4 для впрыска топлива в цилиндр № 1. Одна отметка расположена на губернаторском узле удержания веса. Другой расположен на внутреннем кулачном кольце. Эти две метки должны быть выровнены по центру TDC (верхняя мёртвая точка цилиндра № 1).

![[ip900wb.png]]

На Lucas CAV DPA правильная временная буква может быть расположена на табличке с данными двигателя, как показано.

Указанное буквой G относится к правильному выравниванию букв синхронизации, как показано в предыдущем кадре.

![[ap9plwb.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> Pump-to-engine timing is extremely critical. Pump timing that is off by **only** a few crankshaft degrees will cause:
>
> 1. Poor performance - starting and power.
> 2. Excessive smoke.
> 3. Poor fuel economy.
>
> ### Time
>
> Engine pump timing begins with the timing of the fuel injection pump drive gear to the camshaft gear.
>
> The first step is the location of TDC of the compression stroke for cylinder Number 1.
>
> Then, depending on the engine configuration, an alpha character on the injection pump drive gear will possibly need to be aligned with the mark on the camshaft gear.
>
> This table **must** be used to maintain proper fuel injection pump-to-engine timing. The Control Parts List (CPL) number from the engine dataplate and the Control Parts List Manual, Bulletin 3379133 or 4021327, **must** be used to determine whether the engine is certified, and if so, what year and regulating agency (EPA or CARB).
>
> Given this information, use the following table to determine which letter on the fuel injection pump drive gear is aligned with the camshaft gear.
>
> **Note · Примечание**
> Timing mark alignment is **not** required for the Nippondenso EP-9 or Bosch® in-line drive gear.
>
> **Note · Примечание**
> The timing mark is **not** required for Bosch® VE and DP210 used on Tier II Industrial engines. For these engines, vary timing by using the Timing Check procedure.
>
> | Letter on Pump Gear | Engine Model | Injection Pump | Certification |
> |---|---|---|---|
> | A | 4B3.9, 4BT3.9 | Stanadyne pump | Noncertified |
> | A | 4B3.9, 4BT3.9, 4BTA3.9 | Lucas CAV DPA pump | All noncertified |
> | B | 4B3.9, 4BTA3.9 | Bosch® VE | 1986, 1987 EPA, All pre-1986, All noncertified |
> | C | 6BT5.9, 6BTA5.9 | Bosch® VE | 1986, 1987 EPA, All pre-1986, All noncertified, CPL 600 |
> | D | 6B5.9, 6BT5.9 | Stanadyne | Noncertified |
> | D | 6B5.9, 6BT5.9, 6BTA5.9 | Lucas CAV DPA | All noncertified |
> | E | 6BT5.9, 6BTA5.9 | Bosch® VE | 1986, 1987, 1988, 1989, 1990, 1991, 1992 CARB |
> | F | 4BT3.9, 4BTA3.9 | Bosch® VE | 1986, 1987, 1988, 1989, 1990, 1991, 1992 CARB, 1988, 1989, 1990, 1991, 1992 EPA |
> | G | 6BTA5.9 | Lucas CAV DPA | All Fire Pumps |
> | H | **Not** used at this time | N/A | N/A |
>
> To verify that the fuel injection pump is timed correctly, first check the alignment marks on the pump flange and gear housing.
>
> **Note · Примечание**
> 1 mm of rotation past the timing mark will advance or retard (depending on direction of rotation) the pump timing by 1 degree.
>
> The Lucas CAV DPA, DPS, Delphi DP210, Stanadyne DB4, and the Bosch® VE fuel injection pumps all have a provision for locking the pump shaft at a position corresponding to top dead center for cylinder Number 1. New and reconditioned fuel injection pumps **must** be received with the shafts located in this position.
>
> At the point of injection, the keyway of the shaft will align with the delivery valve receiving the injection and the illustrated hash mark on the seal housing.
>
> **Note · Примечание**
> The illustrated mark is for reference **only** and **must not** be used for setting the fuel injection pump timing.
>
> The Number 1 cylinder delivery valve is marked as illustrated.
>
> Four cylinder = A
>
> Six cylinder = D
>
> | Firing Order |  |
> |---|---|
> | Four Cylinder | Six Cylinder |
> | A =1 | D = 1 |
> | B = 3 | E = 5 |
> | C = 4 | F = 3 |
> | D = 2 | A = 6 |
> |  | B = 2 |
> |  | C = 4 |
>
> The engine is equipped with an engine timing pin to locate top dead center (TDC) for cylinder Number 1.
>
> **CAUTION · Осторожно**
> If the timing pin is incorrectly located on the gear housing, the pump will not be timed correctly.
>
> After precisely locating TDC for cylinder Number 1, the factory positions the timing pin assembly to the gear housing, using the timing pin and the hole in the camshaft gear. If the gear housing or timing pin assembly are removed, the same precision is required to relocate it.
>
> If the timing pin assembly is incorrectly located, reposition the timing pin.
>
> The flange of a replacement pump **must** be marked to align with the mark on the gear housing after installation.
>
> During production, after the locked pump is fitted to the engine with cylinder Number 1 at top dead center (TDC), a mark is stamped on the gear housing and the pump flange. Thereafter, when these marks are aligned, the pump is correctly timed to the engine.
>
> **Note · Примечание**
> The marks on the gear housing and the pump flange are unique to each engine.
>
> See Service Tool Instruction, Bulletin 3400196 and Service Tool Catalog, Bulletin 3377710 to determine the appropriate Bosch® timing tool and adapter kit part numbers.
>
> A special indicator can be used to measure the position of the Bosch® VE fuel injection pump plunger to check pump timing.
>
> Stanadyne DB4 Fuel Injection Pump Timing
>
> Clean all debris from around the fuel injection pump timing window cover.
>
> Remove the fuel injection pump timing cover.
>
> Rotate the fuel injection pump driveshaft in the direction of pump rotation to align the timing line on the weight retainer hub with the line on the cam ring.
>
> Position the fuel injection driveshaft locking key plate in the locked position. Turn the locking screw in until contact is made with the driveshaft.
>
> **Момент затяжки · Torque Value**
> 11.9 n•m [105 in-lb]
>
> Verify the timing marks are aligned after timing is locked.
>
> Install the fuel injection pump timing cover.
>
> CAV DPA/DPS Fuel Injection Pump Timing
>
> Correct timing of the Lucas CAV DPA/DPS fuel injection pump can be verified by removing the inspection plate.
>
> **Note · Примечание**
> Special equipment in an authorized shop is required to time the Lucas CAV DPA fuel injection pump precisely. However, for troubleshooting and in an emergency, visual alignment of the timing mark is close enough for the engine to run.
>
> Both of these checks are described in the fuel injection pump replacement. [[40-005-012-tr — Fuel Injection Pumps, In-Line|Refer to Procedure 005-012 (Fuel Injection Pumps, In-Line) in Section 5.]]
>
> [[40-005-014-tr — Fuel Injection Pump, Rotary|Refer to Procedure 005-014 (Fuel Injection Pump, Rotary) in Section 5.]]
>
> [[40-005-013 — Fuel Injection Pump, In-Line, Spill Port Timing|Refer to Procedure 005-013 (Fuel Injection Pump, In-Line, Spill Port Timing) in Section 5 for installation of the timing pin.]]
>
> Timing Check - (Bosch® VE Pump)
>
> Rotate the crankshaft to top dead center (TDC).
>
> Remove the plug from the end of the pump.
>
> **CAUTION · Осторожно**
> Do not bend the fuel lines. Doing so can result in fuel system failure.
>
> See Service Tool Instruction, Bulletin 3400196 and Service Tool Catalog, Bulletin 3377710 to determine the appropriate Bosch® timing tool and adapter kit part numbers.
>
> Install the timing indicator. Be sure to allow adequate travel for the indicator.
>
> In order to install the timing indicator, it is often necessary to disconnect one or more of the fuel lines from the fuel pump.
>
> **Note · Примечание**
> The indicator is marked in increments of 0.01 mm. 1 revolution of the indicator needle is equal to 0.50 mm.
>
> Bar the crankshaft in the direction opposite engine rotation until the indicator needle stops moving. Adjust the indicator face to read 0.
>
> Rotate the crankshaft back to top dead center (TDC), and count the number of revolutions of the indicator needle. The reading shown when the engine timing pin engages is the amount of plunger lift the pump has at that point.
>
> Bosch® VE Pumps with Slotted Mounting Holes
>
> Rotate the pump on the mounting studs until the indicator reads the correct value for plunger lift. This illustration gives an example of the indicator readings for the various plunger lift values.
>
> Tighten the flange mounting nuts.
>
> **Момент затяжки · Torque Value**
> 24 n•m [18 ft-lb]
>
> Bosch® VE Pumps with Round Mounting Holes
>
> Rotate the engine until the plunger travel is at the desired location.
>
> Lock the fuel pump. [[40-005-014-tr — Fuel Injection Pump, Rotary|Refer to Procedure 005-014 (Fuel Injection Pump, Rotary) in Section 5.]]
>
> Separate the fuel pump drive gear from the pump shaft. [[40-005-014-tr — Fuel Injection Pump, Rotary|Refer to Procedure 005-014 (Fuel Injection Pump, Rotary) in Section 5]]
>
> With the pump locked, rotate the engine back to TDC.
>
> Torque the fuel pump drive nut. [[40-005-014-tr — Fuel Injection Pump, Rotary|Refer to Procedure 005-014 (Fuel Injection Pump, Rotary) in Section 5.]]
>
> Unlock the fuel pump.
>
> Verify the correct timing has been achieved by measuring the static timing.
>
> Remove the timing indicator. Install the plug.
>
> **Момент затяжки · Torque Value**
> 10 n•m [89 in-lb]
>
> Pump Timing - Lucas CAV DPA, Stanadyne DB4, Delphi DP210, Nippondenso EP-9, and Bosch® P7100
>
> Rotate the engine to top dead center (TDC).
>
> Correct timing of the Lucas CAV DPA and Stanadyne DB4 fuel injection pump can be verified by removing the timing window cover plate.
>
> The Nippondenso EP-9 and Bosch® P-7100 fuel injection pumps are checked by removing the timing pin access plug and verifying the slot in the pin will fit over the timing tooth in the fuel injection pump.
>
> **Note · Примечание**
> Special equipment in an authorized shop is required to time the Lucas CAV DPA fuel injection pump precisely. However, for troubleshooting and in an emergency, visual alignment of the timing mark is close enough for the engine to run.
>
> To correct the timing on the Bosch® P-7100 and Nippondenso EP-9, see the replacement procedure for the respective pump.
>
> Two injection pump timing marks are used on the Stanadyne DB4 for timing injection of fuel into the Number 1 cylinder. One mark is located on the governor weight retainer hub. The other is located on the internal cam ring. These two marks **must** be aligned at Number 1 cylinder top dead center (TDC).
>
> On the Lucas CAV DPA, the correct timing letter can be located on the engine dataplate as shown.
>
> The letter G indicated refers to the correct timing letter alignment as shown in the previous frame.
