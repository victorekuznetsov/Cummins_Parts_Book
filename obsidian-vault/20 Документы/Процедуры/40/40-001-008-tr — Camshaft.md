---
aliases:
  - "Распределительный вал"
type: "Процедура"
doc: "40-001-008-tr"
title_en: "Camshaft"
title_ru: "Распределительный вал"
modified: "2024-03-27"
engines:
  - "93047320"
families:
  - "6B5.9"
manuals:
  - "3666087"
figures: 41
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/40/40-001-008-tr.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/40-001-008-tr.pdf"
tags:
  - "документ/процедура"
  - "двигатель/6B5.9"
  - "группа/40"
  - "перевод/машинный"
---

# Camshaft
**Распределительный вал**

> [!abstract] Процедура · `40-001-008-tr`
> **Двигатели:** [[93047320 — 6B5.9 CPL 3111|93047320]]
> **Семейство:** 6B5.9
> **Входит в руководства:** [[3666087 — B3.9, B4.5, B4.5 RGT, and B5.9 Service Manual|3666087]]
> **Секции:** Section 1 - Cylinder Block · Section 1 - Cylinder Block - Group 01
> **Даты:** изменён 2024-03-27
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/40/40-001-008-tr.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/40-001-008-tr.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Первичная проверка

Эта процедура охватывает как двигатели задних передач, так и двигатели передних передач.

Перед началом этой процедуры убедитесь, что имеется достаточный зазор для удаления распределительного вала с задней части двигателя для двигателей задних зубчатых составов и с передней части двигателя для двигателей передних зубчатых составов.

| Задняя гильза / Front/Rear Gear |  |  |  |
|---|---|---|---|
|  | мм |  | в |
| 4 Цилиндр | 60.96 | Мин | 24 |
| 6 Цилиндр | 81.28 | Мин | 32 |

> [!note] Примечание
> Для доступа может потребоваться удаление компонентов изготовителя оригинального оборудования (радиатор, сборка охладителя заряда воздуха и т. Д.). Смотрите инструкции OEM.

Если можно получить достаточный зазор, двигатель должен быть удален.

![[nobox.png]]

### Подготовительные операции

Поезд Rear Gear

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Чтобы снизить риск искрения, минусовой (-) провод аккумуляторной батареи снимайте первым, а подсоединяйте последним.

> [!danger] ОПАСНО
> Поддерживайте заднюю часть двигателя с использованием задней опоры, прикрепленной к задней части блока цилиндров. Неспособность поддерживать двигатель может привести к травмам.

> [!note] Примечание
> Распредвал должен быть удален с конца маховика двигателя.

- Отсоедините аккумуляторные батареи.
- Удалите трансмиссию и все связанные с ней компоненты, если они оборудованы. См. сервисное руководство изготовителя машины.
- Удалите маховик.[[40-016-005-tr — Flywheel|См. процедуру 016-005 в разделе 16.]]
- Удалите флешку.[[40-016-004-tr — Flexplate|См. процедуру 016-004 в разделе 16.]]
- Снимите кожух маховика.[[40-016-006-tr — Flywheel Housing|См. процедуру 016-006 в разделе 16.]]
- Удалите насос для подъёма топлива. См. процедуру 005-045 в разделе 5.
- Снимите крышку коромысел.[[40-003-011-tr — Rocker Lever Cover|См. процедуру 003-011 в разделе 3.]]
- Удалите рычаги коромысла.[[40-003-008-tr — Rocker Lever|См. процедуру 003-008 в разделе 3.]]
- Удалите толкатели.[[40-004-014-tr — Push Rods or Tubes|См. процедуру 004-014 в разделе 4.]]
- Поднимите краны.[[40-004-015-tr — Tappet|См. процедуру 004-015 в разделе 4.]]
- Заблокируйте топливный насос.[[40-005-014-tr — Fuel Injection Pump, Rotary|См. процедуру 005-014 в разделе 5.]].

> [!note] Примечание
> Несрабатывание топливного насоса может привести к неправильному синхронизации топливного насоса во время сборки.

![[ck800wa.png]]

Поезд Front Gear

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Чтобы снизить риск искрения, минусовой (-) провод аккумуляторной батареи снимайте первым, а подсоединяйте последним.

> [!note] Примечание
> Распредвал должен быть удален из вибрационного амортизатора двигателя.

- Отсоедините аккумуляторные батареи.
- Снимите крышку коромысел.[[40-003-011-tr — Rocker Lever Cover|См. процедуру 003-011 в разделе 3.]]
- Удалите рычаги коромысла.[[40-003-008-tr — Rocker Lever|См. процедуру 003-008 в разделе 3.]]
- Удалите толкатели.[[40-004-014-tr — Push Rods or Tubes|См. процедуру 004-014 в разделе 4.]]
- Удалите насос для подъёма топлива. См. процедуру 005-045 в разделе 5.
- Снимите жгут проводов.[[40-008-002-tr — Drive Belt, Cooling Fan|См. процедуру 008-002 в разделе 8.]]
- Удалите фан-хаб, если это необходимо.[[40-008-039-tr — Fan Spacer and Pulley|См. процедуру 008-039 в разделе 8.]]
- Удалите вибрационный демпфер. Используйте следующую процедуру, если оборудованы вязким демпфером.[[40-001-052-tr — Vibration Damper, Viscous|См. процедуру 001-052 в разделе 1.]]
- Удалите вибрационный демпфер. Используйте следующую процедуру, если оборудованы резиновым демпфером.[[40-016-004-tr — Flexplate|См. процедуру 016-004 в разделе 16.]]
- Снимите переднюю крышку передних колес.[[40-001-031-tr — Gear Cover, Front|См. процедуру 001-031 в разделе 1.]]
- Поднимите краны.[[40-004-015-tr — Tappet|См. процедуру 004-015 в разделе 4.]]

![[ck800wa.png]]

### Снятие

Поезд Rear Gear

> [!note] Примечание
> Двигатель может иметь либо отметку на коленчатом валу, либо зубчатый зуб.

Поверните двигатель, чтобы выровнять временные метки на распределительном валу и коленчатом валу.

Совет по обслуживанию: Двигатель можно повернуть, установив два маховика/разгибающихся крепежных болта на полпути. Затем используйте прыжок между двумя болтами, чтобы повернуть двигатель.

Совет по обслуживанию: Двигатели, оснащенные воздушными компрессорами, могут требовать привязки воздушного компрессора к двигателю. Чтобы убедиться, что воздушный компрессор правильно рассчитан по времени, когда распределительная передача позже установлена, пропишите линию выравнивания на воздушном компрессоре и распределительной передаче перед удалением распределительной передачи.

![[01d00253.png]]

На двигателях, оснащенных воздушным компрессором/приводом, может потребоваться ослабить/удалить часть оборудования для крепления воздушного компрессора/привода, чтобы снять передачу распределительного вала. не требуется полностью удалять воздушный компрессор/привод.

Ослабление/удаление некоторых воздушных компрессоров/приводных устройств для монтажа даст достаточный зазор для удаления распределительного механизма.

Устранить крепления для крепления воздушного компрессора (1).

Удалите два болта, обеспечивающие поддержку воздушного компрессора (2).

Если гидравлический насос оснащен гидравлическим насосом, вытесненным из воздушного компрессора, может потребоваться снять и/или ослабить некоторые или все крепежные элементы. Смотрите инструкции OEM.

![[12900080.png]]

Удалите болты распределительного вала и удалите распределительную передачу.

[[40-001-012-tr — Camshaft Gear (Camshaft Installed)|См. процедуру 001-012 в разделе 1.]].

> [!note] Примечание
> На двигателях, оснащенных воздушным компрессором/приводом, может потребоваться удаление воздушного компрессора/привода для получения зазора для удаления распределительного механизма.

![[01d00157.png]]

Удалите болты тяговой пластины и удалите пластину тяги.

![[01d00150.png]]

> [!warning] ОСТОРОЖНО
> Распредвал упадет, как только расчистит последний втулку, если не поддерживается. Это может привести к повреждению журнала распредвалов или, если он оборудован, кольца индикатора скорости распредвалов.

Используйте съёмник, сервисный инструментальный элемент под номером ST647 или эквивалент, чтобы прикрепить к концу распределительного вала, где крепится распределительное устройство, в качестве ручки. Это даст правильное рычаг и облегчит удаление распредвала.

Вытащите распредвал из цилиндра с помощью установленного съёмника.

![[12900081.png]]

Поезд Front Gear

Используйте инструмент баррикинга, номер детали 3824591, чтобы повернуть коленчатый вал, чтобы выровнять коленчатый вал к знакам времени передачи распределительного вала.

![[ks9geda.png]]

Удалите болты с пластины тяги.

Удалите пластину тяги.

![[cg9csma.png]]

Удалить распредвал и распредвал в качестве сборки.

> [!note] Примечание
> Поверните распредвал, когда он удаляется. Используйте крайнюю осторожность, чтобы убедиться, что втулки не повреждены во время этого процесса.

![[cg9shma.png]]

### Разборка

Поезд Front Gear

Удалите распределительную передачу и ключ поиска.[[40-001-013 — Camshaft Gear (Camshaft Removed)|См. процедуру 001-013 в разделе 1.]].

![[01d00327.png]]

### Очистка и проверка при повторном использовании

Проверьте распределительную передачу.

Для двигателей задних зубчатых колес,[[40-001-012-tr — Camshaft Gear (Camshaft Installed)|См. процедуру 001-012 в разделе 1.]].

Для передних передних тяговых двигателей,[[40-001-013 — Camshaft Gear (Camshaft Removed)|См. процедуру 001-013 в разделе 1.]].

![[cg9gesc.png]]

Проверьте втулку распределительного вала.[[40-001-010-tr — Camshaft Bushings|См. процедуру 001-010 в разделе 1.]].

> [!note] Примечание
> Передние двигатели передних зубчатых поездов будут иметь передний вал втулки. Двигатели задних зубчатых составов будут иметь заднюю втулку распределительного вала. Некоторые двигатели могут быть оснащены обоими.

Осмотрите только втулку распределительного вала, которая находится на том же конце двигателя, из которого был удален распределительный вал.

> [!note] Примечание
> Осмотр остальных втулок распределительного вала и заготовок распределительного вала не требуется, если только во время осмотра распределительного вала не было отмечено повреждение в журналах распределительного вала.

![[01d00152.png]]

> [!danger] ОПАСНО
> При очистке растворителями, кислотами и щелочными составами соблюдайте указания их изготовителя. Работайте в защитных очках и защитной одежде, чтобы снизить риск травмы.

> [!danger] ОПАСНО
> При работе со сжатым воздухом применяйте защиту глаз и лица. Разлетающиеся частицы и грязь могут привести к травме.

Очистить распределительный вал растворителями и высушить сжатым воздухом.

![[01d00222.png]]

Осмотрите доли клапана и журналы подшипников для растрескивания, питтинга или забивания.

Осмотрите поверхность установки распределительного устройства на распределительном вале, чтобы убедиться, что гнездо для размещения распределительного устройства находится на месте и **не **согнуто, срезано или треснуло.

![[01d00144.png]]

См. Service Bulletin 3666475, Camshaft and Tappet Reuse Guidelines, for reuse guidelines for cast iron camshafts.

![[cg9shsb.png]]

Критерии ухудшения (разбивки) края

Площадь износа края **не должна** быть больше эквивалентной площади круга 2 мм \[0,079-в\] в пределах ±20 градусов носа доли распредвала.

![[cg900sf.png]]

За пределами ±20 градусов носа доли распредвала области ухудшения края не должны быть больше эквивалентной площади окружности 6 мм \[0,236 в \].

> [!note] Примечание
> Если вал показывает какую-либо питтинг или износ, удалите и проверьте краны перед установкой вала. См. процедуру 004-015 в разделе 4. Если установлен новый распределительный вал, то должны быть установлены также новые краны и толкатели.

![[cg900si.png]]

### Измерение

Измерить пик доли клапана распределительного вала.

| 4 цилиндра (поезд с задним сиденьем) диаметр пика Лобе |  |  |  |
|---|---|---|---|
|  | мм |  | в |
| принимать | 46.132 | Мин | 1.8162 |
| выхлоп | 45.632 | Мин | 1.797 |

| 4 цилиндр (поезд с передним расположением) пик двигателя диаметра лоба по номеру части вала Camshaft |  |  |
|---|---|---|
| Номер детали | Минимальный расход | Минимальный выхлоп |
|  | \[in\] | \[in\] |
| 3929039 | 47.392 \[ 1.866 \] | 47.122 \[ 1.855 \] |
| 3925582 | 47.392 \[ 1.866 \] | 47.122 \[ 1.855 \] |
| 3914638 | 47.392 \[ 1.866 \] | 47.122 \[ 1.855 \] |
| 3929885 | 47.803 \[ 1.882 \] | 46.609 \[ 1.835 \] |
| 3929038 | 47.803 \[ 1.882 \] | 47.122 \[ 1.855 \] |
| 3924574 | 47.803 \[ 1.882 \] | 47.122 \[ 1.855 \] |
| 3931281 | 47.392 \[ 1.866 \] | 46.609 \[ 1.835 \] |
| 3930346 | 47.392 \[ 1.866 \] | 46.609 \[ 1.835 \] |

| 6 цилиндр (поезд с передним расположением) пик двигателя диаметра лоба по номеру части вала Camshaft |  |  |
|---|---|---|
| Номер детали | Минимальный расход | Минимальный выхлоп |
|  | \[in\] | \[in\] |
| 3283179 | 47.803 \[ 1.882 \] | 46.609 \[ 1.835 \] |
| 3929734 | 47.803 \[ 1.882 \] | 47.122 \[ 1.855 \] |
| 3929040 | 47.803 \[ 1.882 \] | 47.122 \[ 1.855 \] |
| 3926671 | 47.803 \[ 1.882 \] | 47.122 \[ 1.855 \] |
| 3924109 | 42.811 \[ 1.685 \] | 47.122 \[ 1.855 \] |
| 3929041 | 47.392 \[ 1.866 \] | 47.122 \[ 1.855 \] |
| 3921953 | 47.392 \[ 1.866 \] | 47.122 \[ 1.855 \] |
| 3919608 | 47.392 \[ 1.866 \] | 47.122 \[ 1.855 \] |
| 3929042 | 47.392 \[ 1.866 \] | 47.122 \[ 1.855 \] |
| 3914639 | 47.392 \[ 1.866 \] | 47.122 \[ 1.855 \] |
| 3929886 | 47.803 \[ 1.882 \] | 46.609 \[ 1.835 \] |
| 3930378 | 47.392 \[ 1.866 \] | 46.609 \[ 1.835 \] |
| 3283179 | 47.803 \[ 1.882 \] | 46.609 \[ 1.835 \] |

![[cg900tb.png]]

Измерьте вал подшипников журналов.

| Журнал Диаметр |  |  |
|---|---|---|
| мм |  | в |
| 53.962 | Мин | 2.1245 |
| 54.013 | Макс | 2.1265 |

![[cg900tc.png]]

Измерить долю насоса для переноса топлива:

| Диаметр насоса для переноса топлива Lobe |  |  |
|---|---|---|
| мм |  | в |
| 35.50 | Мин | 1.398 |
| 36.26 | Макс | 1.428 |

![[cg900ta.png]]

Измерить толщину пластины тяги распределительного вала:

| Толщина хвостовой части хвостовой части поезда Camshaft Thrust Plate |  |  |
|---|---|---|
| мм |  | в |
| 5.25 | Мин | 0.207 |
| 5.35 | Макс | 0.211 |

| Толщина лобовой пластины Front Gear Train Camshaft Thrust Plate Thickness |  |  |
|---|---|---|
| мм |  | в |
| 9.40 | Мин | 0.370 |
| 9.60 | Макс | 0.378 |

Если пластина тяги распределительного вала находится за пределами указанных пределов, замените пластину тяги.

> [!note] Примечание
> Двигатели Front Gear Train и Rear Gear Train используют **не** одну и ту же тяговую пластину распредвала. Толщина пластины тяги кулачного вала также может быть проверена путем проверки осевого зазора кулачного вала во время установки.

![[01d00068.png]]

### Сборка

Поезд Front Gear

Установите распредвальную передачу, определяющую местонахождение ключа и распредвальную передачу.[[40-001-013 — Camshaft Gear (Camshaft Removed)|См. процедуру 001-013 в разделе 1.]].

![[cg9gehb.png]]

### Установка

Поезд Rear Gear

Нанесите сборочный смазочный материал, номер детали 3163087, на задний цилиндрический вал.

![[01d00146.png]]

Смазать доли распределительного вала, журналы и шайбу с помощью сборочного смазочного материала, номер детали 3163087.

![[01d00147.png]]

Используйте съёмник, инструмент для обслуживания, часть номер ST647 или эквивалент, чтобы прикрепить к концу распределительного вала, где крепится распределительное устройство, чтобы действовать как ручка. Это даст правильное рычаг и облегчит установку распределительного вала.

![[ad8toga.png]]

> [!warning] ОСТОРОЖНО
> Не заставляйте распределительный вал в цилиндрический вал, так как может возникнуть повреждение втулки распределительного вала.

Установите распределительный вал. При слегкам нажатии поверните распределительный вал и тщательно проведите работу распределительного вала через втулки распределительного вала. По мере того, как каждый журнал распределительного вала проходит через втулку, распределительный вал будет слегка падать, и доли распределительного вала будут ловить на втулках. Вращение распределительного вала освободит доли от втулки и позволит установить распределительный вал.

![[01d00148.png]]

Установите тяговую пластину.

Установите болты тяговых пластин.

> [!tip] Момент затяжки
> 24 Н·м [212 фунт-дюйм]

![[01d00150.png]]

> [!warning] ОСТОРОЖНО
> Чтобы уменьшить вероятность повреждения двигателя, убедитесь, что распределительный вал вращается свободно.

> [!note] Примечание
> Двигатель может иметь либо отметку на коленчатом валу, либо зубчатый зуб.

Выровнять временные метки на распределительной передаче с временными метками на коленчатой передаче.

> [!note] Примечание
> Если он оснащен воздушным компрессором, убедитесь, что выровняли линию, которая была прописана на шасси и воздушной передаче компрессора во время шага удаления шасси.[[40-012-014-tr — Air Compressor|См. процедуру 012-014 в разделе 12.]]Если бы это было сделано **не**

![[01d00253.png]]

Поверните распределительный вал так, чтобы штифт с дюбелем распределительного вала выравнивался с щелью на шестерене распределительного вала. Установите распределительную передачу и болты.

Затяните болты.

> [!tip] Момент затяжки
> 36 Н·м [27 фунт-фут]

![[01d00161.png]]

Используйте калибр, Номер детали 3824564 и магнитное основание, Номер детали 3377399, чтобы проверить, что распределительный вал имеет правильную обратную реакцию и конечный зазор.

| Осевой зазор вала (А) |  |  |
|---|---|---|
| мм |  | в |
| 0.10 | Мин | 0.004 |
| 0.36 | Макс | 0.014 |

| Camshaft Gear Backlash Limits (B) (недоступная ссылка) |  |  |
|---|---|---|
| мм |  | в |
| 0.076 | Мин | 0.003 |
| 0.280 | Макс | 0.011 |

![[01d00151.png]]

Поезд Front Gear

Нанесите сборочный смазочный материал, номер детали 3163087, на передний цилиндрический вал.

![[cg9brwb.png]]

Смазать доли распределительного вала, журналы и пластину тяги с помощью сборочного смазочного материала, номер детали 3163087.

![[cg900wa.png]]

> [!warning] ОСТОРОЖНО
> Не пытайтесь заставить распределительный вал в цилиндрический вал, так как может возникнуть повреждение втулки распределительного вала.

Установите распределительный вал. При слегкам нажатии поверните распределительный вал и тщательно проведите работу распределительного вала через втулки распределительного вала. По мере того, как каждый журнал распределительного вала проходит через втулку, распределительный вал будет слегка падать, и доли распределительного вала будут ловить на втулках. Вращение распределительного вала освободит доли от втулки и позволит установить распределительный вал.

![[cg900hb.png]]

> [!warning] ОСТОРОЖНО
> Чтобы уменьшить вероятность повреждения двигателя, убедитесь, что распределительный вал вращается свободно.

Перед тем, как распредвал задействует коленчатый вал, проверьте распредвал на удобство вращения. При правильной установке распредвал **должен** свободно вращаться.

![[cg900wb.png]]

Выровнять временные метки, как проиллюстрировано, и закончить установку распределительного вала.

![[ks9geda.png]]

Установите тяговую пластину.

Установите болты тяговых пластин.

> [!tip] Момент затяжки
> 24 Н·м [18 фунт-фут]

![[cg9csma.png]]

Используйте калибр, Номер детали 3824564 и магнитное основание, Номер детали 3377399, чтобы проверить, что распределительный вал имеет правильную обратную реакцию и конечный зазор.

| Осевой зазор вала (А) |  |  |
|---|---|---|
| мм |  | в |
| 0.12 | Мин | 0.005 |
| 0.47 | Макс | 0.018 |

| Camshaft Gear Backlash Limits (B) (недоступная ссылка) |  |  |
|---|---|---|
| мм |  | в |
| 0.076 | Мин | 0.003 |
| 0.280 | Макс | 0.011 |

![[cg900nb.png]]

### Завершающие операции

Поезд Rear Gear

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Чтобы снизить риск искрения, минусовой (-) провод аккумуляторной батареи снимайте первым, а подсоединяйте последним.

- Разблокируйте топливный насос. См. процедуру 005-014 в разделе 5.
- Опустите краны.[[40-004-015-tr — Tappet|См. процедуру 004-015 в разделе 4.]]
- Установите толкатели.[[40-004-014-tr — Push Rods or Tubes|См. процедуру 004-014 в разделе 4.]]
- Установите рычаги коромысла.[[40-003-008-tr — Rocker Lever|См. процедуру 003-008 в разделе 3.]]
- Отрегулируйте ресницу клапана.[[40-003-004-tr — Overhead Set|См. процедуру 003-004 в разделе 3.]]
- Установите крышку коромысел.[[40-003-011-tr — Rocker Lever Cover|См. процедуру 003-011 в разделе 3.]]
- Установите насос для подъёма топлива. См. процедуру 005-045 в разделе 5.
- Установите корпус маховика.[[40-016-006-tr — Flywheel Housing|См. процедуру 016-006 в разделе 16.]]
- Установите маховик.[[40-016-005-tr — Flywheel|См. процедуру 016-005 в разделе 16.]]
- Установите флешлейт.[[40-016-004-tr — Flexplate|См. процедуру 016-004 в разделе 16.]]
- Установите трансмиссию и все сопутствующие компоненты, если они оборудованы. См. сервисное руководство изготовителя машины.
- Установите воздушный компрессор.[[40-012-014-tr — Air Compressor|См. процедуру 012-014 в разделе 12.]]
- Подключите батареи
- Запустите двигатель и проверьте на отсутствие утечек.

![[ck800wa.png]]

Поезд Front Gear

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Чтобы снизить риск искрения, минусовой (-) провод аккумуляторной батареи снимайте первым, а подсоединяйте последним.

- Установите переднюю крышку передних передач.[[40-001-031-tr — Gear Cover, Front|См. процедуру 001-031 в разделе 1.]]
- Установите вибрационный демпфер. Используйте следующую процедуру, если оборудованы вязким демпфером.[[40-001-052-tr — Vibration Damper, Viscous|См. процедуру 001-052 в разделе 1.]].
- Используйте следующую процедуру, если оборудованы резиновым демпфером.[[40-016-004-tr — Flexplate|См. процедуру 016-004 в разделе 1.]]
- Отпустите краны.[[40-004-015-tr — Tappet|См. процедуру 004-015 в разделе 4.]]
- Установите толкатели.[[40-004-014-tr — Push Rods or Tubes|См. процедуру 004-014 в разделе 4.]]
- Установите рычаги коромысла.[[40-003-008-tr — Rocker Lever|См. процедуру 003-008 в разделе 3.]]
- Отрегулируйте ресницу клапана.[[40-003-004-tr — Overhead Set|См. процедуру 003-004 в разделе 3.]]
- Установите крышку коромысел.[[40-003-011-tr — Rocker Lever Cover|См. процедуру 003-011 в разделе 3.]]
- Установите насос для подъёма топлива. См. процедуру 005-045 в разделе 5.
- Установите фан-центр, если это необходимо.[[40-008-039-tr — Fan Spacer and Pulley|См. процедуру 008-039 в разделе 8.]]
- Установите приводной ремень.[[40-008-002-tr — Drive Belt, Cooling Fan|См. процедуру 008-002 в разделе 8.]].
- Подключите батареи
- Запустите двигатель и проверьте на отсутствие утечек.

![[ck800wa.png]]


> [!quote]- Original (English) · английский оригинал
> ### Initial Check
>
> This procedure covers both rear gear train engines and front gear train engines.
>
> Prior to starting this procedure, make sure there is adequate clearance to remove the camshaft from the rear of the engine for rear gear train engines and from the front of the engine for front gear train engines.
>
> | Clearance from Front/Rear Gear Housing |  |  |  |
> |---|---|---|---|
> |  | mm |  | in |
> | 4 Cylinder | 60.96 | MIN | 24 |
> | 6 Cylinder | 81.28 | MIN | 32 |
>
> **Note · Примечание**
> It may be necessary to remove original equipment manufacturer (OEM) components (radiator, charge-air cooler assembly, etc.) for access. Refer to the OEM instructions.
>
> If adequate clearance can **not** be obtained, the engine **must** be removed.
>
> ### Preparatory Steps
>
> Rear Gear Train
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> **WARNING · Опасно**
> Support the rear of the engine using the rear support attached to the rear of the cylinder block. Failure to support the engine can cause personal injury.
>
> **Note · Примечание**
> The camshaft **must** be removed from the flywheel end of the engine.
>
> - Disconnect the batteries.
> - Remove the transmission and all related components, if equipped. Refer to the OEM service manual.
> - Remove the flywheel. [[40-016-005-tr — Flywheel|Refer to Procedure 016-005 in Section 16.]]
> - Remove the flexplate. [[40-016-004-tr — Flexplate|Refer to Procedure 016-004 in Section 16.]]
> - Remove the flywheel housing. [[40-016-006-tr — Flywheel Housing|Refer to Procedure 016-006 in Section 16]]
> - Remove the fuel lift pump. Refer to Procedure 005-045 in Section 5
> - Remove the rocker lever cover. [[40-003-011-tr — Rocker Lever Cover|Refer to Procedure 003-011 in Section 3]]
> - Remove the rocker levers. [[40-003-008-tr — Rocker Lever|Refer to Procedure 003-008 in Section 3]]
> - Remove the push rods. [[40-004-014-tr — Push Rods or Tubes|Refer to Procedure 004-014 in Section 4]]
> - Raise the tappets. [[40-004-015-tr — Tappet|Refer to Procedure 004-015 in Section 4.]]
> - Lock the fuel pump. [[40-005-014-tr — Fuel Injection Pump, Rotary|Refer to Procedure 005-014 in Section 5]].
>
> **Note · Примечание**
> Failure to lock the fuel pump may result in improper fuel pump timing during reassembly.
>
> Front Gear Train
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> **Note · Примечание**
> The camshaft **must** be removed from the vibration damper end of the engine.
>
> - Disconnect the batteries.
> - Remove the rocker lever cover. [[40-003-011-tr — Rocker Lever Cover|Refer to Procedure 003-011 in Section 3.]]
> - Remove the rocker levers. [[40-003-008-tr — Rocker Lever|Refer to Procedure 003-008 in Section 3.]]
> - Remove the push rods. [[40-004-014-tr — Push Rods or Tubes|Refer to Procedure 004-014 in Section 4.]]
> - Remove the fuel lift pump. Refer to Procedure 005-045 in Section 5.
> - Remove the drive belt. [[40-008-002-tr — Drive Belt, Cooling Fan|Refer to Procedure 008-002 in Section 8.]]
> - Remove the fan hub, if required. [[40-008-039-tr — Fan Spacer and Pulley|Refer to Procedure 008-039 in Section 8.]]
> - Remove the vibration damper. Use the following procedure, if equipped with a viscous damper. [[40-001-052-tr — Vibration Damper, Viscous|Refer to Procedure 001-052 in Section 1.]]
> - Remove the vibration damper. Use the following procedure, if equipped with a rubber damper. [[40-016-004-tr — Flexplate|Refer to Procedure 016-004 in Section 16.]]
> - Remove the front gear cover. [[40-001-031-tr — Gear Cover, Front|Refer to Procedure 001-031 in Section 1]]
> - Raise the tappets. [[40-004-015-tr — Tappet|Refer to Procedure 004-015 in Section 4]]
>
> ### Remove
>
> Rear Gear Train
>
> **Note · Примечание**
> The engine can have either a mark on the crankshaft gear or a chamfered tooth.
>
> Rotate the engine to align the timing marks on the camshaft and crankshaft gear.
>
> Service Tip: The engine can be rotated by installing two of the flywheel/flexplate mounting capscrews half way. Then use a pry bar in between the two capscrews to rotate the engine.
>
> Service Tip: Engines equipped with air compressors may require the air compressor be timed to the engine. To make sure that the air compressor is properly timed when the camshaft gear is later installed, scribe an alignment line on the air compressor and camshaft gear before removing the camshaft gear.
>
> On engines equipped with an air compressor/accessory drive, it may be necessary to loosen/remove some of the air compressor/accessory drive mounting hardware in order to remove the camshaft gear. It is **not** necessary to remove the air compressor/accessory drive completely.
>
> Loosening/removing some of the air compressor/accessory drive mounting hardware will give enough clearance to remove the camshaft gear.
>
> Loosen the air compressor mounting fasteners (1).
>
> Remove the two capscrews securing the air compressor support (2).
>
> If equipped with a hydraulic pump driven off of the air compressor, it may be necessary to remove and/or loosen some or all of the mounting fasteners. Refer to the OEM instructions.
>
> Remove the camshaft gear capscrews and remove the camshaft gear.
>
> [[40-001-012-tr — Camshaft Gear (Camshaft Installed)|Refer to Procedure 001-012 in Section 1]].
>
> **Note · Примечание**
> On engines equipped with an air compressor/accessory drive, it may be necessary to remove the air compressor/accessory drive to gain clearance to remove the camshaft gear.
>
> Remove the thrust plate capscrews and remove the thrust plate.
>
> **CAUTION · Осторожно**
> The camshaft will drop once the camshaft clears the last bushing if not supported. This can cause damage to the camshaft journal or, if equipped, the camshaft speed indicator ring.
>
> Use a gear puller, service tool part number ST647, or equivalent, to attach to the end of the camshaft where the camshaft gear mounts, to act as a handle. This will give proper leverage and make it easier to remove the camshaft.
>
> Slide the camshaft out of the bore using the installed gear puller.
>
> Front Gear Train
>
> Use barring tool, Part Number 3824591, to rotate the crankshaft to align the crankshaft to the camshaft gear timing marks.
>
> Remove the capscrews from the thrust plate.
>
> Remove the thrust plate.
>
> Remove the camshaft and camshaft gear as an assembly.
>
> **Note · Примечание**
> Rotate the camshaft as it is being removed. Use extreme care to make sure that the bushings are **not** damaged during this process.
>
> ### Disassemble
>
> Front Gear Train
>
> Remove the camshaft gear and locating key. [[40-001-013 — Camshaft Gear (Camshaft Removed)|Refer to Procedure 001-013 in Section 1]].
>
> ### Clean and Inspect for Reuse
>
> Inspect the camshaft gear.
>
> For rear gear train engines, [[40-001-012-tr — Camshaft Gear (Camshaft Installed)|Refer to Procedure 001-012 in Section 1]].
>
> For front gear train engines, [[40-001-013 — Camshaft Gear (Camshaft Removed)|Refer to Procedure 001-013 in Section 1]].
>
> Inspect the camshaft bushing. [[40-001-010-tr — Camshaft Bushings|Refer to Procedure 001-010 in Section 1]].
>
> **Note · Примечание**
> Front gear train engines will have a front camshaft bushing. Rear gear train engines will have a rear camshaft bushing. Some engines may be equipped with both.
>
> Only inspect the camshaft bushing that is on the same end of the engine from which the camshaft was removed.
>
> **Note · Примечание**
> Inspection of the rest of the camshaft bushings and camshaft block bores is **not** necessary unless, during the inspection of the camshaft, damage was noted on the camshaft journals.
>
> **WARNING · Опасно**
> When using solvents, acids, or alkaline materials for cleaning, follow the manufacturer's recommendations for use. Wear goggles and protective clothing to reduce the possibility of personal injury.
>
> **WARNING · Опасно**
> Wear appropriate eye and face protection when using compressed air. Flying debris and dirt can cause personal injury.
>
> Clean the camshaft with solvents and dry with compressed air.
>
> Inspect the valve lobes and bearing journals for cracking, pitting, or scoring.
>
> Inspect the camshaft gear mounting surface on the camshaft to ensure the camshaft gear locating dowel pin is in place and **not** bent, sheared, or cracked.
>
> See Service Bulletin 3666475, Camshaft and Tappet Reuse Guidelines, for reuse guidelines for cast iron camshafts.
>
> Edge Deterioration (breakdown) Criteria
>
> The area of edge deterioration **must not** be greater than the equivalent area of a 2-mm \[0.079-in\] circle within ±20 degrees of the nose of the camshaft lobe.
>
> Outside of the ±20 degrees of the nose of the camshaft lobe, the areas of edge deterioration **must not** be greater than the equivalent area of a 6 mm \[ 0.236 in \] circle.
>
> **Note · Примечание**
> If the camshaft shows any pitting or wear, remove and inspect the tappets before installing the camshaft. Refer to Procedure 004-015 in Section 4. If a new camshaft is installed, new tappets and push rods **must** be installed also.
>
> ### Measure
>
> Measure the peak of the camshaft valve lobes.
>
> | 4 Cylinder (Rear Gear Train) Diameter of Peak of Lobe |  |  |  |
> |---|---|---|---|
> |  | mm |  | in |
> | Intake | 46.132 | MIN | 1.8162 |
> | Exhaust | 45.632 | MIN | 1.797 |
>
> | 4 Cylinder (Front Gear Train) Engine Peak of Lobe Diameter by Camshaft Part Number |  |  |
> |---|---|---|
> | Part Number | Minimum Intake | Minimum Exhaust |
> |  | mm \[in\] | mm \[in\] |
> | 3929039 | 47.392 \[ 1.866 \] | 47.122 \[ 1.855 \] |
> | 3925582 | 47.392 \[ 1.866 \] | 47.122 \[ 1.855 \] |
> | 3914638 | 47.392 \[ 1.866 \] | 47.122 \[ 1.855 \] |
> | 3929885 | 47.803 \[ 1.882 \] | 46.609 \[ 1.835 \] |
> | 3929038 | 47.803 \[ 1.882 \] | 47.122 \[ 1.855 \] |
> | 3924574 | 47.803 \[ 1.882 \] | 47.122 \[ 1.855 \] |
> | 3931281 | 47.392 \[ 1.866 \] | 46.609 \[ 1.835 \] |
> | 3930346 | 47.392 \[ 1.866 \] | 46.609 \[ 1.835 \] |
>
> | 6 Cylinder (Front Gear Train) Engine Peak of Lobe Diameter by Camshaft Part Number |  |  |
> |---|---|---|
> | Part Number | Minimum Intake | Minimum Exhaust |
> |  | mm \[in\] | mm \[in\] |
> | 3283179 | 47.803 \[ 1.882 \] | 46.609 \[ 1.835 \] |
> | 3929734 | 47.803 \[ 1.882 \] | 47.122 \[ 1.855 \] |
> | 3929040 | 47.803 \[ 1.882 \] | 47.122 \[ 1.855 \] |
> | 3926671 | 47.803 \[ 1.882 \] | 47.122 \[ 1.855 \] |
> | 3924109 | 42.811 \[ 1.685 \] | 47.122 \[ 1.855 \] |
> | 3929041 | 47.392 \[ 1.866 \] | 47.122 \[ 1.855 \] |
> | 3921953 | 47.392 \[ 1.866 \] | 47.122 \[ 1.855 \] |
> | 3919608 | 47.392 \[ 1.866 \] | 47.122 \[ 1.855 \] |
> | 3929042 | 47.392 \[ 1.866 \] | 47.122 \[ 1.855 \] |
> | 3914639 | 47.392 \[ 1.866 \] | 47.122 \[ 1.855 \] |
> | 3929886 | 47.803 \[ 1.882 \] | 46.609 \[ 1.835 \] |
> | 3930378 | 47.392 \[ 1.866 \] | 46.609 \[ 1.835 \] |
> | 3283179 | 47.803 \[ 1.882 \] | 46.609 \[ 1.835 \] |
>
> Measure the camshaft bearing journals.
>
> | Journal Diameter |  |  |
> |---|---|---|
> | mm |  | in |
> | 53.962 | MIN | 2.1245 |
> | 54.013 | MAX | 2.1265 |
>
> Measure the fuel transfer pump lobe:
>
> | Fuel Transfer Pump Lobe Diameter |  |  |
> |---|---|---|
> | mm |  | in |
> | 35.50 | MIN | 1.398 |
> | 36.26 | MAX | 1.428 |
>
> Measure the camshaft thrust plate thickness:
>
> | Rear Gear Train Camshaft Thrust Plate Thickness |  |  |
> |---|---|---|
> | mm |  | in |
> | 5.25 | MIN | 0.207 |
> | 5.35 | MAX | 0.211 |
>
> | Front Gear Train Camshaft Thrust Plate Thickness |  |  |
> |---|---|---|
> | mm |  | in |
> | 9.40 | MIN | 0.370 |
> | 9.60 | MAX | 0.378 |
>
> If the camshaft thrust plate is out of specification, replace the thrust plate.
>
> **Note · Примечание**
> Front Gear Train and Rear Gear Train engines do **not** use the same camshaft thrust plate. The camshaft thrust plate thickness can also be verified by checking camshaft end play during installation.
>
> ### Assemble
>
> Front Gear Train
>
> Install the camshaft gear locating key and camshaft gear. [[40-001-013 — Camshaft Gear (Camshaft Removed)|Refer to Procedure 001-013 in Section 1]].
>
> ### Install
>
> Rear Gear Train
>
> Apply assembly lubricant, Part Number 3163087, to the rear camshaft bore.
>
> Lubricate the camshaft lobes, journals, and thrust washer with assembly lubricant, Part Number 3163087.
>
> Use a gear puller, service tool Part Number ST647, or equivalent, to attach to the end of the camshaft where the camshaft gear mounts, to act as a handle. This will give proper leverage and ease installing the camshaft.
>
> **CAUTION · Осторожно**
> Do not force the camshaft into the camshaft bore as damage to the camshaft bushing can result.
>
> Install the camshaft. While pushing in slightly, rotate the camshaft and carefully work the camshaft through the camshaft bushings. As each camshaft journal passes through a bushing, the camshaft will drop slightly and the camshaft lobes will catch on the bushings. Rotating the camshaft will free the lobe from the bushing and allow the camshaft to be installed.
>
> Install the thrust plate.
>
> Install the thrust plate capscrews.
>
> **Момент затяжки · Torque Value**
> 24 n•m [212 in-lb]
>
> **CAUTION · Осторожно**
> To reduce the possibility of engine damage, make sure the camshaft rotates freely.
>
> **Note · Примечание**
> The engine can have either a mark on the crankshaft gear or a chamfered tooth.
>
> Align the timing marks on the camshaft gear with the timing marks on the crankshaft gear.
>
> **Note · Примечание**
> If equipped with an air compressor, make sure to align the line that was scribed on the camshaft gear and air compressor gear during the camshaft gear removal step. [[40-012-014-tr — Air Compressor|Refer to Procedure 012-014 in section 12.]] If this was **not** done.
>
> Rotate the camshaft so that the camshaft dowel pin aligns with the slot on the camshaft gear. Install the camshaft gear and capscrews.
>
> Tighten the capscrews.
>
> **Момент затяжки · Torque Value**
> 36 n•m [27 ft-lb]
>
> Use gauge, Part Number 3824564, and magnetic base, Part Number 3377399, to verify the camshaft has proper backlash and end clearance.
>
> | Camshaft End Play (A) |  |  |
> |---|---|---|
> | mm |  | in |
> | 0.10 | MIN | 0.004 |
> | 0.36 | MAX | 0.014 |
>
> | Camshaft Gear Backlash Limits (B) |  |  |
> |---|---|---|
> | mm |  | in |
> | 0.076 | MIN | 0.003 |
> | 0.280 | MAX | 0.011 |
>
> Front Gear Train
>
> Apply assembly lubricant, Part Number 3163087, to the front camshaft bore.
>
> Lubricate the camshaft lobes, journals, and thrust plate with assembly lubricant, Part Number 3163087.
>
> **CAUTION · Осторожно**
> Do not try to force the camshaft into the camshaft bore as damage to the camshaft bushing can result.
>
> Install the camshaft. While pushing in slightly, rotate the camshaft and carefully work the camshaft through the camshaft bushings. As each camshaft journal passes through a bushing, the camshaft will drop slightly and the camshaft lobes will catch on the bushings. Rotating the camshaft will free the lobe from the bushing and allow the camshaft to be installed.
>
> **CAUTION · Осторожно**
> To reduce the possibility of engine damage, make sure the camshaft rotates freely.
>
> Before the camshaft gear engages the crankshaft gear, check the camshaft for ease of rotation. When installed properly, the camshaft **must** rotate freely.
>
> Align the timing marks as illustrated and finish installing the camshaft.
>
> Install the thrust plate.
>
> Install the thrust plate capscrews.
>
> **Момент затяжки · Torque Value**
> 24 n•m [18 ft-lb]
>
> Use gauge, Part Number 3824564, and magnetic base, Part Number 3377399, to verify the camshaft has proper backlash and end clearance.
>
> | Camshaft End Play (A) |  |  |
> |---|---|---|
> | mm |  | in |
> | 0.12 | MIN | 0.005 |
> | 0.47 | MAX | 0.018 |
>
> | Camshaft Gear Backlash Limits (B) |  |  |
> |---|---|---|
> | mm |  | in |
> | 0.076 | MIN | 0.003 |
> | 0.280 | MAX | 0.011 |
>
> ### Finishing Steps
>
> Rear Gear Train
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> - Unlock the fuel pump. Refer to Procedure 005-014 in Section 5.
> - Lower the tappets. [[40-004-015-tr — Tappet|Refer to Procedure 004-015 in Section 4]]
> - Install the push rods. [[40-004-014-tr — Push Rods or Tubes|Refer to Procedure 004-014 in Section 4]]
> - Install the rocker levers. [[40-003-008-tr — Rocker Lever|Refer to Procedure 003-008 in Section 3]]
> - Adjust the valve lash. [[40-003-004-tr — Overhead Set|Refer to Procedure 003-004 in Section 3]]
> - Install the rocker lever cover. [[40-003-011-tr — Rocker Lever Cover|Refer to Procedure 003-011 in Section 3]]
> - Install the fuel lift pump. Refer to Procedure 005-045 in Section 5.
> - Install the flywheel housing. [[40-016-006-tr — Flywheel Housing|Refer to Procedure 016-006 in Section 16]]
> - Install the flywheel. [[40-016-005-tr — Flywheel|Refer to Procedure 016-005 in Section 16]]
> - Install the flexplate. [[40-016-004-tr — Flexplate|Refer to Procedure 016-004 in Section 16.]]
> - Install the transmission and all related components, if equipped. Refer to the OEM service manual.
> - Install the air compressor. [[40-012-014-tr — Air Compressor|Refer to Procedure 012-014 in Section 12.]]
> - Connect the batteries
> - Operate the engine and check for leaks.
>
> Front Gear Train
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> - Install the front gear cover. [[40-001-031-tr — Gear Cover, Front|Refer to Procedure 001-031 in Section 1]]
> - Install the vibration damper. Use the following procedure, if equipped with a viscous damper. [[40-001-052-tr — Vibration Damper, Viscous|Refer to Procedure 001-052 in Section 1]].
> - Use the following procedure, if equipped with a rubber damper. [[40-016-004-tr — Flexplate|Refer to Procedure 016-004 in Section 1.]]
> - Release the tappets. [[40-004-015-tr — Tappet|Refer to Procedure 004-015 in Section 4]]
> - Install the push rods. [[40-004-014-tr — Push Rods or Tubes|Refer to Procedure 004-014 in section 4]]
> - Install the rocker levers. [[40-003-008-tr — Rocker Lever|Refer to Procedure 003-008 in Section 3]]
> - Adjust the valve lash. [[40-003-004-tr — Overhead Set|Refer to Procedure 003-004 in Section 3]]
> - Install the rocker lever cover. [[40-003-011-tr — Rocker Lever Cover|Refer to Procedure 003-011 in Section 3]]
> - Install the fuel lift pump. Refer to Procedure 005-045 in Section 5.
> - Install the fan hub, if required. [[40-008-039-tr — Fan Spacer and Pulley|Refer to Procedure 008-039 in Section 8]]
> - Install the drive belt. [[40-008-002-tr — Drive Belt, Cooling Fan|Refer to Procedure 008-002 in Section 8]].
> - Connect the batteries
> - Operate the engine and check for leaks.
