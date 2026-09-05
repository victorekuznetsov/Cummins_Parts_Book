---
aliases:
  - "Маховик"
type: "Процедура"
doc: "40-016-005-tr"
title_en: "Flywheel"
title_ru: "Маховик"
modified: "2006-03-31"
engines:
  - "93047320"
families:
  - "6B5.9"
manuals:
  - "3666087"
figures: 31
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/40/40-016-005-tr.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/40-016-005-tr.pdf"
tags:
  - "документ/процедура"
  - "двигатель/6B5.9"
  - "группа/40"
  - "перевод/машинный"
---

# Flywheel
**Маховик**

> [!abstract] Процедура · `40-016-005-tr`
> **Двигатели:** [[93047320 — 6B5.9 CPL 3111|93047320]]
> **Семейство:** 6B5.9
> **Входит в руководства:** [[3666087 — B3.9, B4.5, B4.5 RGT, and B5.9 Service Manual|3666087]]
> **Секции:** Section 16 - Mounting Adaptations - Group 16
> **Даты:** изменён 2006-03-31
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/40/40-016-005-tr.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/40-016-005-tr.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Подготовительные операции

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Чтобы снизить риск искрения, минусовой (-) провод аккумуляторной батареи снимайте первым, а подсоединяйте последним.

- Отсоедините аккумуляторные батареи.

![[13900050.png]]

> [!note] Примечание
> Используйте контейнер, который может вместить не менее 26 литров моторного масла [27 квт].

- Если он оснащен мокрым корпусом маховика, выкачайте масло из корпуса маховика, удалив пробку в нижней части корпуса маховика.
- Удалить трансмиссию и все сопутствующие компоненты (при их оснащении). Смотрите инструкции OEM.

![[ck800wa.png]]

### Первичная проверка

Проверьте зубья кольцевой передачи маховика на предмет повреждения.

Если кольцевая передача маховика повреждена, обязательно проверьте следующие возможные причины перед заменой флакслата.

![[fh9gewb.png]]

механический

Механическая проблема обычно может быть идентифицирована путем обнаружения повреждения кольцевой передачи маховика в 3 различных местах для 6-цилиндровых двигателей (обычно называемых фрезерованием на 120 градусов) и 2 местах для 4-цилиндровых двигателей (обычно называемых фрезерованием на 180 градусов). Следующие причины могут быть причиной механических проблем:

1. После установки маховика обязательно проверьте правильное расстояние между стартером и мотором. Видишь?[[40-013-020-tr — Starting Motor|Процедура 013-020]]
2. Помехи между кольцевой передачей земли и стартовым сцеплением двигателя. Может быть установлен неправильный пусковой двигатель. См. спецификации производителя оригинального оборудования
3. Может быть дефект с прицепом стартера. Осмотрите пинион на никс и буррс. Если требуется замена стартового двигателя, обратитесь к[[40-013-020-tr — Starting Motor|Процедура 013-020]]
4. Кольцевое снаряжение может быть неправильно установлено или повреждено. Видишь?[[40-016-008 — Flywheel Ring Gear|Процедура 016-008]]
5. Вылет маховика может быть вне установленных пределов. См. раздел Меры этой процедуры
6. Неправильный стартовый прикол двигателя для маховика кольцевой передачи шаг/зубной матч. См. спецификации производителя оригинального оборудования.

![[13900028.png]]

электрический

Электрическая проблема обычно может быть идентифицирована путем обнаружения повреждения кольцевой передачи маховика на 360 градусов вокруг окружности кольцевой передачи (обычно называемой 360-градусной фрезерованием). Следующие причины могут быть причиной электрических проблем:

1. Оператор пытается запустить двигатель, пока двигатель уже работает. Проверьте, доступна ли функция блокировки стартера через OEM или производителя стартового двигателя.
2. Переключатель зажигания, вызывающий прерывистое зацепление двигателя при запуске двигателя. Проверьте замок зажигания. См. сервисное руководство изготовителя машины.
3. Ориентация стартового реле так, чтобы направление контакта притяжения было в направлении движения транспортного средства. Это приводит к прерывистому включению стартера при работе двигателя. Переместите стартовую эстафету. См. спецификации производителя оригинального оборудования
4. Проблемы с прокладкой стартового двигателя. См. спецификации производителя оригинального оборудования.

![[13900029.png]]

### Снятие

> [!note] Примечание
> Используйте инструмент для заграждения, номер детали 3824591, чтобы удерживать маховик, чтобы предотвратить вращение.

Удалите два болта на 180 градусов друг от друга.

Установите два направляющих штифта M12 x 1,25 x 90 мм.

> [!note] Примечание
> Если в оборудовании используется сцепление, резьба в отверстиях для крепления болтов сцепления в пластинах давления может быть метрической или стандартной. Обязательно используйте правильные болты.

Определите конструкцию и размер резьбы болтов, а также установите две Т-ручки в маховик в точках (1 и 2).

Удалите оставшиеся шесть болтов для крепления маховика.

![[fw9csmb.png]]

> [!danger] ОПАСНО
> Этот компонент весит 23 кг[50 фунтов] или более. Чтобы уменьшить вероятность получения травмы, используйте подъемник или получите помощь в подъеме этого компонента.

Удалите маховик из направляющих штифтов.

![[fw900ma.png]]

### Разборка

> [!note] Примечание
> Удаление подшипника пилота необходимо только при повреждении или при установке нового или восстановленного сцепления.

Если они оборудованы, удалите подшипник пилота.

Используйте багряницу и молоток, чтобы снять подшипник пилота.

Используйте абразивную прокладку, номер детали 3823258 или эквивалент, для очистки цилиндра пилота.

![[fw1bema.png]]

### Очистка и проверка при повторном использовании

> [!danger] ОПАСНО
> При работе с пароочистителем надевайте защитные очки или щиток и защитную одежду. Горячий пар может привести к тяжёлой травме.

> [!danger] ОПАСНО
> При очистке растворителями, кислотами и щелочными составами соблюдайте указания их изготовителя. Работайте в защитных очках и защитной одежде, чтобы снизить риск травмы.

> [!danger] ОПАСНО
> Некоторые растворители огнеопасны и токсичны. Перед применением прочитайте указания изготовителя.

> [!danger] ОПАСНО
> Сжатый воздух, используемый для очистки, не должен превышать 207 кПа[30 psi]. При работе со сжатым воздухом применяйте защиту глаз и лица. Разлетающиеся частицы и грязь могут привести к травме.

Если подшипник пилота был удален, используйте проволочную щетку для очистки цилиндра пилота коленчатого вала.

Используйте пар или растворитель для очистки маховика.

Просушите сжатым воздухом.

![[fw1brea.png]]

Проверка на наличие никсов или заусенцев.

Используйте абразивную прокладку Scotch-BriteTM 7448 или эквивалентную для удаления мелких галочек и заусениц.

![[fw800sa.png]]

> [!danger] ОПАСНО
> Не используйте треснувший или всплывший маховик. Они могут сломаться, вызывая серьезные личные травмы или имущественный ущерб.

Используйте набор для обнаружения трещин, часть 3375432, чтобы проверить наличие трещин в маховике. Следуйте инструкциям, предоставленным с помощью комплекта.

![[fw1bdsa.png]]

Проверьте зубья маховика для зубчатых колес на наличие трещин и чипсов.

Если зубья кольцевой передачи сломаны или сломаны, кольцевую передачу следует заменить. Видишь?[[40-016-008 — Flywheel Ring Gear|Процедура 016-008]].

![[fw800sc.png]]

### Сборка

Если вы удалите, установите новый подшипник пилота.

Используйте багряницу и молоток для установки подшипника пилота. Пилотный подшипник должен быть установлен равномерно с поверхностью цилиндра пилота.

![[fw1beha.png]]

### Установка

Установите два направляющих штифта M12 x 1,25 x 90 мм в фланце коленчатого вала на расстоянии 180 градусов друг от друга.

> [!note] Примечание
> Если в оборудовании используется сцепление, резьба в отверстиях для крепления болтов сцепления в пластинах давления может быть метрической или стандартной. Будьте уверены, что вы используете правильные болты.

Определите конструкцию и размер резьбы болтов, а также установите две Т-ручки в маховик (в точках 1 и 2).

![[fw900wa.png]]

> [!danger] ОПАСНО
> Компонент весит 23 кг[50 фунтов] или более. Чтобы уменьшить вероятность получения травмы, используйте подъемник или получите помощь в поднятии компонента.

Осмотрите заднюю поверхность коленчатого вала и маховика, устанавливающего фланж, на чистоту и поднятые ника или заусеницы.

Установите маховик на направляющие штифты.

![[16900095.png]]

Смазать резьба болтов и поверхность шайб чистым смазочным моторным маслом.

![[fw1cswa.png]]

Установите шесть болтов.

Удалите T-ручки и направляющие булавки.

Установите оставшиеся болты в отверстия, из которых были удалены направляющие штифты.

![[fw9csmc.png]]

> [!note] Примечание
> Используйте инструмент для заграждения, номер детали 3824591, чтобы удерживать маховик, чтобы предотвратить вращение.

Затягивай болты в звездном узоре.

Задние моторы Gear Train Flywheel bolts

| Front Gear Train Engines Flywheel болты | 137 Н·м | [101 фунт-фут] |
|---|---|---|

![[fh900oa.png]]

### Измерение

цилиндровый рулон Runout

Используйте циферблатный индикаторный калибр (1), номер детали 3376050 или его эквивалент, и набор измерительных приборов (2), номер детали ST-1325, чтобы осмотреть цилиндр маховика (3) и поверхность (4) сток.

Установите крепление к корпусу маховика.

Установите калибр на крепление.

Установите контактный наконечник индикатора против внутреннего диаметра цилиндра маховика и установите индикатор циферблата на ноль.

![[fw1iaha.png]]

Используйте инструмент заграждения, номер детали 3824591, чтобы повернуть коленчатый вал в одну полную революцию.

| мм |  | в |
|---|---|---|
| 0.127 | Макс | 0.0050 |

![[16900096.png]]

> [!danger] ОПАСНО
> Компонент весит 23 кг[51 фунт] или более. Чтобы уменьшить вероятность получения травмы, используйте подъемник или получите помощь в поднятии компонента.

Если общий показатель считывания общего показателя считывания больше, чем спецификация, сделайте следующее:

- Удалите маховик.

![[16900097.png]]

- Осмотрите поверхность маховика для грязи или повреждений.

![[fw1bdsb.png]]

- Осмотрите коленчатый вал на предмет грязи или повреждений.

![[ks900sb.png]]

> [!danger] ОПАСНО
> Компонент весит 23 кг[50 фунтов] или более. Чтобы уменьшить вероятность получения травмы, используйте подъемник или получите помощь в поднятии компонента.

- Установите маховик.
- Проверьте снова разряд цилиндра.

![[fw900ma.png]]

- Замените маховик, если вылет не соответствует спецификациям.

| мм |  | в |
|---|---|---|
| 0.127 | Макс | 0.005 |

![[fw900he.png]]

Лицевой вылет

Установите контактный наконечник индикатора против лица маховика.

При поиске контактного наконечника см. таблицу общего показаний индикатора Flywheel Face Runout позже в этой процедуре. Найдите контактный наконечник так, чтобы он соответствовал радиусу, указанному в таблице, но все же максимально приближен к внешнему диаметру маховика, чтобы осмотреть грань маховика (1) вылета.

Нажмите маховик вперед, чтобы удалить зазор конца коленчатого вала. Настройте циферблат на индикаторе до тех пор, пока игла не укажет ноль.

![[16900098.png]]

Используйте инструмент заграждения, номер детали 3824591, чтобы повернуть коленчатый вал в одну полную революцию. Измерьте и запишите взлет маховика в четырех равных точках на маховике.

Маховик должен быть подталкиван к передней части двигателя, чтобы удалить зазор конца коленчатого вала каждый раз, когда измеряется точка.

Определить общее значение показателя (TIR).

МДП определяется путем расчета разницы между самым высоким и самым низким измерением из четырех измеренных мест.

![[fw900tc.png]]

Измерьте расстояние от центра маховика до контактного кончика индикатора (А). Используйте это измерение, чтобы определить, какую спецификацию использовать из таблицы ниже.

Общий показатель, указывающий на, не должен превышать следующие характеристики:

| Flywheel Radius (A) (недоступная ссылка) | Максимальное общее значение показателя показаний лица на летучей колесе |  |  |
|---|---|---|---|
| мм | в | мм | в |
| 101.6 | 4 | 0.140 | 0.004 |
| 127 | 5 | 0.13 | 0.005 |
| 152.4 | 6 | 0.156 | 0.006 |
| 177.8 | 7 | 0.182 | 0.007 |
| 203.2 | 8 | 0.208 | 0.008 |
| 228.6 | 9 | 0.234 | 0.009 |
| 254 | 10 | 0.26 | 0.01 |

![[fw900td.png]]

Если посадочная полоса на лице маховика **не **в пределах спецификаций, удалите маховик. Сначала проверьте наличие никсов, заусенцев или посторонних материалов между поверхностью маховика и фланцем коленчатого вала.

Заменить маховик, если вылет **не** в пределах спецификации.

![[16900099.png]]

### Завершающие операции

- Установите трансмиссию и все сопутствующие компоненты (при их оснащении). Смотрите инструкции OEM
- Если оснащается мокрым корпусом маховика, наполните корпус маховика маслом. См. Инструкции OEM.

![[ck800wa.png]]

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Чтобы снизить риск искрения, минусовой (-) провод аккумуляторной батареи снимайте первым, а подсоединяйте последним.

- Подключите батареи
- Управляйте двигателем и проверяйте шум или вибрацию

![[13900050.png]]


> [!quote]- Original (English) · английский оригинал
> ### Preparatory Steps
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> - Disconnect the batteries.
>
> **Note · Примечание**
> Use a container that can hold at least 26 liters \[27 US qt\] of lubricating oil.
>
> - If equipped with a wet flywheel housing, drain the oil from the flywheel housing by removing the plug in the bottom of the flywheel housing
> - Remove the transmission and all related components (if equipped). Refer to the OEM instructions.
>
> ### Initial Check
>
> Inspect the flywheel ring gear teeth for damage.
>
> If the flywheel ring gear is damaged make sure to inspect the following possible causes prior to replacing the flexplate.
>
> Mechanical
>
> A mechanical issue can typically be identified by seeing damage to the ring gear of the flywheel in 3 distinct locations for 6 cylinder engines (commonly called 120 degree milling), and 2 locations for 4 cylinder engines (commonly called 180 degree milling). The following could be causes for mechanical issues:
>
> 1. Upon installation of the flywheel, make sure to check for proper starter motor spacing. Refer to [[40-013-020-tr — Starting Motor|Procedure 013-020]]
> 2. Interference between the ring gear land area and the starting motor pinion. The wrong starting motor may be installed. Refer to the original equipment manufacturer's specifications
> 3. There may be a defect with the starter motor pinion. Inspect the pinion for nicks and burrs. If replacement of the starting motor is necessary, refer to [[40-013-020-tr — Starting Motor|Procedure 013-020]]
> 4. The ring gear may be improperly installed or damaged. Refer to [[40-016-008 — Flywheel Ring Gear|Procedure 016-008]]
> 5. The flywheel face runout may be out of specification. See the Measure section of this procedure
> 6. Incorrect starting motor pinion to flywheel ring gear pitch/teeth match. Refer to the original equipment manufacturer's specifications.
>
> Electrical
>
> An electrical issue can typically be identified by seeing damage to the ring gear of the flywheel 360 degrees around the circumference of the ring gear (commonly called 360 degree milling). The following could be causes for electrical issues:
>
> 1. Operator is attempting to start engine while engine is already running. Check if a starter lockout feature is available through the OEM or the starting motor manufacturer
> 2. Key switch causing intermittent starting motor engagement when the engine is running. Inspect the key switch. Refer to the OEM service manual.
> 3. Orientation of the starter relay so that the direction of the pull contact is in the direction of the vehicle's travel. This results in intermittent starter motor engagement when the engine is running. Relocate the starter relay. Refer to the original equipment manufacturer's specifications
> 4. Intermittent starter motor wiring issues. Refer to the original equipment manufacturer's specifications.
>
> ### Remove
>
> **Note · Примечание**
> Use the barring tool, Part Number 3824591, to hold the flywheel to prevent rotation.
>
> Remove two capscrews 180 degrees apart.
>
> Install two M12 x 1.25 x 90-mm guide pins.
>
> **Note · Примечание**
> If a clutch is used in the equipment, the threads in the clutch pressure plate mounting capscrew holes can be metric or standard. Be sure to use the correct capscrews.
>
> Determine the capscrew thread design and size, and install two T-handles in the flywheel at points (1 and 2).
>
> Remove the remaining six flywheel mounting capscrews.
>
> **WARNING · Опасно**
> This component weighs 23 kg \[50 lb\] or more. To reduce the possibility of personal injury, use a hoist or get assistance to lift this component.
>
> Remove the flywheel from the guide pins.
>
> ### Disassemble
>
> **Note · Примечание**
> Removal of the pilot bearing is only necessary if damaged or when installing a new or rebuilt clutch.
>
> If equipped, remove the pilot bearing.
>
> Use a mandrel and hammer to remove the pilot bearing.
>
> Use an abrasive pad, Part Number 3823258, or equivalent, to clean the pilot bore
>
> ### Clean and Inspect for Reuse
>
> **WARNING · Опасно**
> When using a steam cleaner, wear safety glasses or a face shield, as well as protective clothing. Hot steam can cause serious personal injury.
>
> **WARNING · Опасно**
> When using solvents, acids, or alkaline materials for cleaning, follow the manufacturer's recommendations for use. Wear goggles and protective clothing to reduce the possibility of personal injury.
>
> **WARNING · Опасно**
> Some solvents are flammable and toxic. Read the manufacturer's instructions before using.
>
> **WARNING · Опасно**
> Compressed air used for cleaning should not exceed 207 kPa \[30 psi\]. Wear appropriate eye and face protection when using compressed air. Flying debris and dirt can cause personal injury.
>
> If the pilot bearing was removed, use a wire brush to clean the crankshaft pilot bore.
>
> Use steam or solvent to clean the flywheel.
>
> Dry with compressed air.
>
> Inspect for nicks or burrs.
>
> Use Scotch-Brite™ 7448 abrasive pad, or equivalent, to remove small nicks and burrs.
>
> **WARNING · Опасно**
> Do not use a cracked or resurfaced flywheel. These can break, causing serious personal injury or property damage.
>
> Use the crack detection kit, Part Number 3375432, to check for cracks in the flywheel. Follow the instructions provided with the kit.
>
> Inspect the flywheel ring gear teeth for cracks and chips.
>
> If the ring gear teeth are cracked or broken, the ring gear **must** be replaced. Refer to [[40-016-008 — Flywheel Ring Gear|Procedure 016-008]].
>
> ### Assemble
>
> If removed, install a new pilot bearing.
>
> Use a mandrel and hammer to install the pilot bearing. The pilot bearing **must** be installed evenly with the pilot bore surface.
>
> ### Install
>
> Install two M12 x 1.25 x 90-mm guide pins into the crankshaft flange 180 degrees apart.
>
> **Note · Примечание**
> If a clutch is used in the equipment, the threads in the clutch pressure plate mounting capscrew holes can be metric or standard. Be **sure** to use the correct capscrews.
>
> Determine the capscrew thread design and size, and install two T-handles into the flywheel (at points 1 and 2).
>
> **WARNING · Опасно**
> The component weighs 23 kg \[50 lb\] or more. To reduce the possibility of personal injury, use a hoist or get assistance to lift the component.
>
> Inspect the rear face of crankshaft and flywheel mounting flange for cleanliness and raised nicks or burrs.
>
> Install the flywheel on the guide pins.
>
> Lubricate the threads of the capscrews and the surface of the washers with clean lubricating engine oil.
>
> Install the six capscrews.
>
> Remove the T-handles and guide pins.
>
> Install the remaining capscrews into the holes from which the guide pins were removed.
>
> **Note · Примечание**
> Use the barring tool, Part Number 3824591, to hold the flywheel to prevent rotation.
>
> Tighten the capscrews in a star pattern.
>
> Rear Gear Train Engines Flywheel Capscrews
>
> | Front Gear Train Engines Flywheel Capscrews | 137 n.m | \[101 ft-lb\] |
> |---|---|---|
>
> ### Measure
>
> Bore Runout
>
> Use the dial indicator gauge (1), Part Number 3376050, or its equivalent, and dial gauge attachment (2), Part Number ST-1325, to inspect the flywheel bore (3) and the surface (4) runout.
>
> Install the attachment to the flywheel housing.
>
> Install the gauge on the attachment.
>
> Install the contact tip of the indicator against the inside diameter of the flywheel bore, and set the dial indicator at zero.
>
> Use the barring tool, Part Number 3824591, to rotate the crankshaft one complete revolution.
>
> | mm |  | in |
> |---|---|---|
> | 0.127 | MAX | 0.0050 |
>
> **WARNING · Опасно**
> The component weighs 23 kg \[51 lb\] or more. To reduce the possibility of personal injury, use a hoist or get assistance to lift the component.
>
> If the total indicator reading total indicator reading is greater than the specification, do the following:
>
> - Remove the flywheel.
>
> - Inspect the flywheel mounting surface for dirt or damage.
>
> - Inspect the crankshaft for dirt or damage.
>
> **WARNING · Опасно**
> The component weighs 23 kg \[50 lb\] or more. To reduce the possibility of personal injury, use a hoist or get assistance to lift the component.
>
> - Install the flywheel.
> - Inspect the bore runout again.
>
> - Replace the flywheel if the runout does **not** meet specifications.
>
> | mm |  | in |
> |---|---|---|
> | 0.127 | MAX | 0.005 |
>
> Face Runout
>
> Install the contact tip of the indicator against the flywheel face.
>
> When locating the contact tip, see the Flywheel Face Runout Total Indicator Reading Table later in this procedure. Locate the contact tip so that it corresponds with a radius listed in the table, but is still as close to the outside diameter of the flywheel as possible, to inspect the flywheel face (1) runout.
>
> Push the flywheel forward to remove the crankshaft end clearance. Adjust the dial on the indicator until the needle points to zero.
>
> Use the barring tool, Part Number 3824591, to rotate the crankshaft one complete revolution. Measure and record the flywheel runout at four equal points on the flywheel.
>
> The flywheel **must** be pushed toward the front of the engine to remove the crankshaft end clearance each time a point is measured.
>
> Determine the total indicator reading (TIR).
>
> TIR is determined by calculating the difference between the highest and lowest measurement from the four locations measured.
>
> Measure the distance from the center of the flywheel to the contact tip of the indicator (A). Use this measurement to determine which specification to use from the table below.
>
> The total indicator reading **must not** exceed the following specifications:
>
> | Flywheel Radius (A) | Maximum Total Indicator Reading of Flywheel Face |  |  |
> |---|---|---|---|
> | mm | in | mm | in |
> | 101.6 | 4 | 0.140 | 0.004 |
> | 127 | 5 | 0.13 | 0.005 |
> | 152.4 | 6 | 0.156 | 0.006 |
> | 177.8 | 7 | 0.182 | 0.007 |
> | 203.2 | 8 | 0.208 | 0.008 |
> | 228.6 | 9 | 0.234 | 0.009 |
> | 254 | 10 | 0.26 | 0.01 |
>
> If the flywheel face runout is **not** within specifications, remove the flywheel. First check for nicks, burrs, or foreign material between the flywheel mounting surface and the crankshaft flange.
>
> Replace the flywheel if the runout is **not** within specification.
>
> ### Finishing Steps
>
> - Install the transmission and all related components (if equipped). Refer to the OEM instructions
> - If equipped with a wet flywheel housing, fill the flywheel housing with oil. Refer to the OEM Instructions.
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> - Connect the batteries
> - Operate the engine and check for noise or vibration
