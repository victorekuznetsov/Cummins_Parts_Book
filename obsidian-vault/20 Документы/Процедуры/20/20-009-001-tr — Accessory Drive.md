---
aliases:
  - "Привод вспомогательного оборудования"
type: "Процедура"
doc: "20-009-001-tr"
title_en: "Accessory Drive"
title_ru: "Привод вспомогательного оборудования"
modified: "2015-08-20"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4021592"
figures: 36
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/20/20-009-001-tr.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/20-009-001-tr.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/20"
  - "перевод/машинный"
---

# Accessory Drive
**Привод вспомогательного оборудования**

> [!abstract] Процедура · `20-009-001-tr`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021592 — QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual|4021592]]
> **Секции:** Section 9 - Drive Units - Group 09
> **Даты:** изменён 2015-08-20
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/20/20-009-001-tr.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/20-009-001-tr.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

> [!note] Примечание
> Эта процедура применяется для двигателей с механически приводимым в действие топливным форсункой **только**.

Используйте следующую процедуру для двигателей с электронным топливным форсункой.[[20-009-011 — Fuel Pump Drive|См. процедуру 009-011 в разделе 9.]]

![[ck800wa.png]]

> [!warning] ОСТОРОЖНО
> Если опора без бурения или без надлежащего бурения используется с компрессором или топливным насосом с электронным приводом, воздушный компрессор или топливный насос могут быть повреждены из-за отсутствия смазки.

> [!note] Примечание
> Составные опоры привода отличаются, если двигатель оснащен воздушным компрессором или топливным форсункой с электронным приводом. Поддержка, используемая с воздушным компрессором, имеет бурение для подачи моторного масла на компрессор.

Существуют две различные вспомогательные опоры привода, используемые на двигателях QSK19 с механически приводимым в действие топливным форсункой:

- Привод аксессуара на двигателях без воздушных компрессоров, но с механически приводимым в действие топливным форсункой не имеет масляных бурений.
- Привод аксессуара на двигателях с воздушным компрессором и механически приводимым в действие топливным форсункой содержит масляный подачу (1) и дренажные бурения (2).

![[09400012.png]]

### Подготовительные операции

> [!danger] ОПАСНО
> Не снимайте пробку радиатора с горячего двигателя. Снимайте пробку радиатора только после того, как температура охлаждающей жидкости опустится ниже 50 °C \[120 °F\]. Струя горячей охлаждающей жидкости или пар могут привести к травме.

> [!danger] ОПАСНО
> Охлаждающая жидкость токсична. Хранить в недоступном для детей и животных месте. Если деталь не используется повторно, утилизируйте её по местным природоохранным требованиям.

> [!note] Примечание
> Если воздушный компрессор **не** установлен на двигателе, то для слива системы охлаждения не потребуется.

- Отсоедините аккумуляторные батареи. См. сервисную документацию изготовителя оборудования.
- Слейте охлаждающую жидкость.[[20-008-018-tr — Cooling System|См. процедуру 008-018 в разделе 8.]]
- Удалите топливный насос.[[20-005-016-tr — Fuel Pump|См. процедуру 005-016 в разделе 5.]]
- Удалите воздушный компрессор.[[20-012-014-tr — Air Compressor|См. процедуру 012-014 в разделе 12.]]
- Удалите дополнительный приводной шкив.[[20-009-004 — Accessory Drive Pulley|См. процедуру 009-004 в разделе 9.]]
- Снимите уплотнение привода аксессуара.[[20-001-003-tr — Accessory Drive Seal|См. процедуру 001-003 в разделе 1.]]

![[ck800wa.png]]

### Первичная проверка

Проверьте привод аксессуара на предмет повреждения.

Измерить конечный зазор для двигателей с механически приводимым в действие топливным форсункой.

| Аксессуарный привод - End Clearance |  |  |
|---|---|---|
| мм |  | в |
| 0.05 | Мин | 0.002 |
| 0.30 | Макс | 0.012 |

![[dp6drca.png]]

Проверьте шайбу. Он должен быть расположен плотно между муфтой и валом. Если шайба **не плотная, привод **должен быть заменен или перестроен.

![[dp6drcb.png]]

### Снятие

> [!warning] ОСТОРОЖНО
> Ключ от древесного дерева должен быть удален перед удалением вспомогательного привода. Повреждение куста может привести к

Удалите четыре крепежных болта и гайку (31).

Удалить сборку привода аксессуара.

![[sa400ma.png]]

### Разборка

> [!warning] ОСТОРОЖНО
> Установите болты обратно в приводной блок без шайбы, пока он не коснется вала, чтобы предотвратить повреждение вала.

Удалите специальные болты и шайбу.

![[dp6drfa.png]]

Используйте соединительный съёмник (1), Номер детали 3376663 или эквивалент, чтобы удалить соединение.

Используйте 3-мягкий съёмник для удаления гибкой связки типа челюсти.

Удалите соединение.

Удалите болты.

![[dp6drfb.png]]

Удалить следующее:

- Зажим шайбы (2)
- Внутренний подшипник тяги (3)
- Подшипник внешней тяги (4)
- Удалить шестерню и вал сборки
- Удалите трубу из корпуса.

> [!note] Примечание
> Алюминиевые кожухи **не** содержат подшипники тяги.

![[dp6drfc.png]]

Поддержите передачу.

Используйте пресс для арбора, чтобы удалить вал.

![[dw6gema.png]]

### Очистка и проверка при повторном использовании

> [!danger] ОПАСНО
> Некоторые растворители огнеопасны и токсичны. Перед применением прочитайте указания изготовителя.

> [!danger] ОПАСНО
> При очистке растворителями, кислотами и щелочными составами соблюдайте указания их изготовителя. Работайте в защитных очках и защитной одежде, чтобы снизить риск травмы.

Чистые детали с растворителем, номер детали 3824421 или эквивалент.

Просушите сжатым воздухом.

![[dp8bdeb.png]]

Измерьте шестерню внутри диаметра.

| Груша внутри диаметра |  |  |
|---|---|---|
| мм |  | в |
| 39.73 | Мин | 1.564 |
| 39.75 | Макс | 1.565 |

![[dp8geta.png]]

Удалите ключ и проверьте на наличие повреждений.

> [!note] Примечание
> Если обнаружена поломка, ключ должен быть заменен.

Измерьте внешний диаметр в месте расположения шестеренки.

| Вал вне диаметра |  |  |
|---|---|---|
| мм |  | в |
| 39.789 | Мин | 1.5665 |
| 39.803 | Макс | 1.5670 |

![[dp6shtb.png]]

Проверьте зубы зубчатой передачи на предмет повреждения.

Сцепная шайба **должна** располагаться плотно между сцепной машиной и валом.

![[09600057.png]]

Измерьте внутренний диаметр корпуса.

| Внутри диаметра внутри |  |  |
|---|---|---|
| мм |  | в |
| 33.43 | Мин | 1.316 |
| 33.50 | Макс | 1.319 |

> [!note] Примечание
> Алюминиевый корпус **не** содержит втулку. Измерьте корпус внутри диаметра. Он должен быть идентичен втулке внутри диаметра в чугунной оболочке.

![[dp6bsta.png]]

Проверьте бороздчатую поверхность подшипника тяги на предмет повреждения.

Измерить толщину подшипника тяги.

| Толщина, несущая струйку |  |  |
|---|---|---|
| мм |  | в |
| 2.36 | Мин | 0.093 |
| 2.41 | Макс | 0.095 |

![[dp8wata.png]]

> [!note] Примечание
> На алюминиевом корпусе **только**, проверьте две обработанные поверхности тяги на предмет повреждения.

Используйте микрометр глубины.

Измерьте глубину.

| Глубина глубь |  |  |
|---|---|---|
| мм |  | в |
| 45.54 | Мин | 1.793 |
| 45.67 | Макс | 1.798 |

![[09400002.png]]

| Вал вне диаметра |  |  |  |
|---|---|---|---|
|  | мм |  | в |
| (5) | 34.963 | Мин | 1.3765 |
|  | 34.976 | Макс | 1.3770 |
| (6) | 39.662 | Мин | 1.5616 |
|  | 39.674 | Макс | 1.5620 |
| (7) | 33.300 | Мин | 1.300 |
|  | 33.330 | Макс | 1.312 |
| (8) | 25.476 | Мин | 1.0030 |
|  | 25.489 | Макс | 1.0035 |

![[dp6shta.png]]

Измерьте внутренний диаметр шкива.

| Пулли внутри диаметра |  |  |
|---|---|---|
| мм |  | в |
| 34.912 | Мин | 1.3745 |
| 34.938 | Макс | 1.3755 |

![[ad8brta.png]]

Измерьте внутренний диаметр сцепления.

| Сплинирование внутри диаметра |  |  |
|---|---|---|
| мм |  | в |
| 25.400 | Мин | 1.0000 |
| 25.425 | Макс | 1.0010 |

| Lovejoy спаривается внутри диаметра |  |  |
|---|---|---|
| мм |  | в |
| 25.425 | Мин | 1.0010 |
| 25.438 | Макс | 1.0015 |

![[dp8cpta.png]]

### Сборка

Поддержите передачу.

Используйте чистое моторное масло для смазки вала.

Выровняйте ключ с помощью слота ключа в шестеренок. Используйте пресс-конструкцию арбора, чтобы нажать вал через передачу, пока плечо вала не коснется передачи.

![[dp6geha.png]]

> [!note] Примечание
> Если достаточное нажатие не доступно, можно использовать духовку.

> [!danger] ОПАСНО
> Носите защитную одежду, чтобы уменьшить вероятность получения травм от ожогов.

> [!warning] ОСТОРОЖНО
> Не превышайте заданное время или температуру. Повреждение зубьев зубчатой передачи будет иметь последствия.

Нагрейте шестерню при температуре 235 ° C (450° F) **не менее**, чем 1 час, и **не более**, чем 6 часов.

![[dp8gewa.png]]

> [!danger] ОПАСНО
> Носите защитную одежду, чтобы уменьшить вероятность получения травм от ожогов.

Сдвиньте вал в шестерне.

![[dp6gehb.png]]

> [!warning] ОСТОРОЖНО
> Позвольте воздуху охлаждать передачу. Не используйте воду или масло, чтобы уменьшить время охлаждения. Повреждение шестерни может привести к этому.

Используйте калибр для измерения расстояния между плечом вала и передачей.

| Топливный насос Drive Gear to Shaft |  |  |
|---|---|---|
| мм |  | в |
| 0.05 | Макс | 0.002 |

> [!note] Примечание
> Если расстояние между шестерней и валом находится **не** в пределах спецификации, нажмите на шестерню до тех пор, пока не будут выполнены технические характеристики.

![[dp6geda.png]]

Поместите выгнутую поверхность подшипника тяги, как проиллюстрировано. Установите подшипник тяги.

> [!note] Примечание
> Алюминиевый корпус **не** содержит подшипники тяги.

![[dp6draa.png]]

Используйте LubriplateTM номер 105 или эквивалент. Смазать канавку поверхности подшипника тяги (3).

> [!note] Примечание
> Алюминиевый корпус **не** содержит подшипники тяги. Смазать обработанную поверхность тяги.

При вытянутой поверхности, расположенной вверх, скользите подшипником (3) тяги по валу.

Перед установкой зажимной шайбы (2) скошенный край должен быть расположен так, как показано на рисунке.

![[dp6drac.png]]

Поддерживайте передачу или вал.

Установите соединение.

Используйте пресс для беседки и подружку, чтобы подтолкнуть сцепление, пока оно не коснется зажимной шайбы.

Зажимная шайба **должна** располагаться плотно между сцеплением и плечом вала.

Установите трубную пробку в корпус.

Затяните трубку.

> [!tip] Момент затяжки
> 8 Н·м [71 фунт-дюйм]

![[dp6drad.png]]

> [!warning] ОСТОРОЖНО
> Болты должны содержать бурение масла, если на двигателе должен быть установлен воздушный компрессор.

Установите шайбу и болты.

Проверьте размер болтов, чтобы определить правильное момент затяжки.

> [!tip] Момент затяжки
> болты 9,525 мм [0,375 в] 45 Н·м [33 фут-лб]

> [!tip] Момент затяжки
> болты 12,7 мм [0,5 дюйма] 100 Н·м [74 фут-лб]

![[dp6drae.png]]

Проверьте конечный допуск. Если **не** в установленных пределах, проверьте сборку.

| Сборка завершает зазор |  |  |
|---|---|---|
| мм |  | в |
| 0.05 | Мин | .002 |
| 0.30 | Макс | .012 |

![[dp6drca.png]]

### Установка

Удалите две прямолинейные кольцевые пробки из отверстия синхронизации в передней крышке.

Проверьте выравнивание индексных знаков.

![[gc4ppha.png]]

> [!warning] ОСТОРОЖНО
> Не используйте "A" на стойке бездействия распределителя распределительного вала для выравнивания привода аксессуара, если метки "X" на распределительном валу и стойки бездействия распределительного вала не выровнены и не центрированы в верхнем отверстии високосного вибратора. Если отметки "X" не видны в верхнем отверстии, поверните двигатель до тех пор, пока метки "X" на шасси распределительного вала и шасси бездействия распределительного вала не будут выровнены и центрированы в верхнем отверстии високосного вибратора.

Установите дополнительный привод так, чтобы «А» на вспомогательном приводном механизме был сосредоточен в нижнем временном отверстии.

![[sa400hb.png]]

Смазать втулку в передней чехле передач чистым моторным маслом.

Установите прокладку, болты и гайку. Затяните болты и гайку.

> [!tip] Момент затяжки
> 48 Н·м [35 фунт-фут]

Используйте приведенное выше момент затяжки, чтобы затянуть болты во второй раз.

![[sa400ha.png]]

Установите прямолинейные кольцевые заглушки. Затягивайте кольцевые заглушки.

> [!tip] Момент затяжки
> 25 Н·м [221 фунт-дюйм]

![[gc4ppha.png]]

Установите уплотнение привода аксессуара.[[20-001-003-tr — Accessory Drive Seal|См. процедуру 001-003 в разделе 1.]]

![[01400041.png]]

> [!note] Примечание
> Уплотнение ключа должно быть установлено до установки ключа и вспомогательного шкива привода.

Установите герметичность ключа (1).

Установите дополнительный привод шкивом ключа древесного волокита (2).

![[09400011.png]]

### Завершающие операции

- Установите дополнительный приводной шкив.[[20-009-004 — Accessory Drive Pulley|См. процедуру 009-004 в разделе 9.]]
- Установите воздушный компрессор, если он оборудован.[[20-012-014-tr — Air Compressor|См. процедуру 012-014 в разделе 12.]]
- Установите топливный насос и связанные с ним компоненты.[[20-005-016-tr — Fuel Pump|См. процедуру 005-016 в разделе 5.]]
- Заправьте систему охлаждения.[[20-008-018-tr — Cooling System|См. процедуру 008-018 в разделе 8.]]
- Подсоедините аккумуляторные батареи. См. сервисную документацию изготовителя оборудования.
- Управляйте двигателем до 70 ° C \[160° F \]. Проверьте на отсутствие утечек.

![[ck800wa.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> **Note · Примечание**
> This procedure is for engines with mechanically actuated injectors **only**.
>
> Use the following procedure for engines with electronically actuated injectors. [[20-009-011 — Fuel Pump Drive|Refer to Procedure 009-011 in Section 9.]]
>
> **CAUTION · Осторожно**
> If a support without drillings or without proper drillings is used with a compressor or electronically actuated injector fuel pump, the air compressor or fuel pump can be damaged from lack of lubrication.
>
> **Note · Примечание**
> The accessory drive supports are different if the engine is equipped with an air compressor or electronically actuated injectors. The support used with an air compressor has a drilling to supply engine oil to the compressor.
>
> There are two different accessory drive supports used on QSK19 engines with mechanically actuated injectors:
>
> - The accessory drive on engines without air compressors but with mechanically actuated injectors has no oil drillings.
> - The accessory drive on engines with an air compressor and mechanically actuated injectors contains an oil feed (1) and drain drillings (2).
>
> ### Preparatory Steps
>
> **WARNING · Опасно**
> Do not remove the pressure cap from a hot engine. Wait until the coolant temperature is below 50°C \[120°F\] before removing the pressure cap. Heated coolant spray or steam can cause personal injury.
>
> **WARNING · Опасно**
> Coolant is toxic. Keep away from children and pets. If not reused, dispose of in accordance with local environmental regulations.
>
> **Note · Примечание**
> If an air compressor is **not** mounted on the engine, it will **not** be necessary to drain the cooling system.
>
> - Disconnect the batteries. See equipment manufacturer service information.
> - Drain the cooling system. [[20-008-018-tr — Cooling System|Refer to Procedure 008-018 in Section 8.]]
> - Remove the fuel pump. [[20-005-016-tr — Fuel Pump|Refer to Procedure 005-016 in Section 5.]]
> - Remove the air compressor. [[20-012-014-tr — Air Compressor|Refer to Procedure 012-014 in Section 12.]]
> - Remove the accessory drive pulley. [[20-009-004 — Accessory Drive Pulley|Refer to Procedure 009-004 in Section 9.]]
> - Remove the accessory drive seal. [[20-001-003-tr — Accessory Drive Seal|Refer to Procedure 001-003 in Section 1.]]
>
> ### Initial Check
>
> Inspect the accessory drive for damage.
>
> Measure the end clearance for engines with mechanically actuated injectors.
>
> | Accessory Drive - End Clearance |  |  |
> |---|---|---|
> | mm |  | in |
> | 0.05 | MIN | 0.002 |
> | 0.30 | MAX | 0.012 |
>
> Inspect the coupling washer. It **must** be positioned tightly between the coupling and the shaft. If the washer is **not** tight, the drive **must** be replaced or rebuilt.
>
> ### Remove
>
> **CAUTION · Осторожно**
> The woodruff key must be removed before removing the accessory drive assembly. Damage to the bushing can result.
>
> Remove the four mounting capscrews and the nut (31).
>
> Remove the accessory drive assembly.
>
> ### Disassemble
>
> **CAUTION · Осторожно**
> Install the capscrew back into the drive unit without the washer until it touches the shaft to prevent damage to the shaft.
>
> Remove the special capscrew and the washer.
>
> Use a coupling puller (1), Part Number 3376663, or equivalent, to remove the coupling.
>
> Use a 3-jaw puller to remove the flexible jaw type coupling.
>
> Remove the coupling.
>
> Remove the capscrew.
>
> Remove the following:
>
> - Clamping washer (2)
> - Inner thrust bearing (3)
> - Outer thrust bearing (4)
> - Remove the gear and the shaft assembly
> - Remove the pipe plug from the housing.
>
> **Note · Примечание**
> Aluminum housings do **not** contain thrust bearings.
>
> Support the gear.
>
> Use an arbor press to remove the shaft.
>
> ### Clean and Inspect for Reuse
>
> **WARNING · Опасно**
> Some solvents are flammable and toxic. Read the manufacturer's instructions before using.
>
> **WARNING · Опасно**
> When using solvents, acids, or alkaline materials for cleaning, follow the manufacturer's recommendations for use. Wear goggles and protective clothing to reduce the possibility of personal injury.
>
> Clean parts with solvent, Part Number 3824421, or equivalent.
>
> Dry with compressed air.
>
> Measure the gear inside diameter.
>
> | Gear Inside Diameter |  |  |
> |---|---|---|
> | mm |  | in |
> | 39.73 | MIN | 1.564 |
> | 39.75 | MAX | 1.565 |
>
> Remove the key and check for damage.
>
> **Note · Примечание**
> If damage is found, the key **must** be replaced.
>
> Measure the outside diameter at the gear location.
>
> | Shaft Outside Diameter |  |  |
> |---|---|---|
> | mm |  | in |
> | 39.789 | MIN | 1.5665 |
> | 39.803 | MAX | 1.5670 |
>
> Check the teeth of the gear for damage.
>
> The coupling washer **must** be positioned tightly between the coupling and the shaft.
>
> Measure the inside diameter of the housing.
>
> | Housing Inside Diameter |  |  |
> |---|---|---|
> | mm |  | in |
> | 33.43 | MIN | 1.316 |
> | 33.50 | MAX | 1.319 |
>
> **Note · Примечание**
> An aluminum housing does **not** contain a bushing. Measure the housing inside diameter. It **must** be identical to the bushing inside diameter in a cast iron housing.
>
> Check the grooved surface of the thrust bearing for damage.
>
> Measure the thrust bearing thickness.
>
> | Thrust Bearing Thickness |  |  |
> |---|---|---|
> | mm |  | in |
> | 2.36 | MIN | 0.093 |
> | 2.41 | MAX | 0.095 |
>
> **Note · Примечание**
> On an aluminum housing **only**, check the two machined thrust surfaces for damage.
>
> Use a depth micrometer.
>
> Measure the depth.
>
> | Housing Depth |  |  |
> |---|---|---|
> | mm |  | in |
> | 45.54 | MIN | 1.793 |
> | 45.67 | MAX | 1.798 |
>
> | Shaft Outside Diameter |  |  |  |
> |---|---|---|---|
> |  | mm |  | in |
> | (5) | 34.963 | MIN | 1.3765 |
> |  | 34.976 | MAX | 1.3770 |
> | (6) | 39.662 | MIN | 1.5616 |
> |  | 39.674 | MAX | 1.5620 |
> | (7) | 33.300 | MIN | 1.300 |
> |  | 33.330 | MAX | 1.312 |
> | (8) | 25.476 | MIN | 1.0030 |
> |  | 25.489 | MAX | 1.0035 |
>
> Measure the inside diameter of the pulley.
>
> | Pulley Inside Diameter |  |  |
> |---|---|---|
> | mm |  | in |
> | 34.912 | MIN | 1.3745 |
> | 34.938 | MAX | 1.3755 |
>
> Measure the inside diameter of the coupling.
>
> | Spline Coupling Inside Diameter |  |  |
> |---|---|---|
> | mm |  | in |
> | 25.400 | MIN | 1.0000 |
> | 25.425 | MAX | 1.0010 |
>
> | Lovejoy Coupling Inside Diameter |  |  |
> |---|---|---|
> | mm |  | in |
> | 25.425 | MIN | 1.0010 |
> | 25.438 | MAX | 1.0015 |
>
> ### Assemble
>
> Support the gear.
>
> Use clean engine oil to lubricate the shaft.
>
> Align the key with the key slot in the gear. Use an arbor press to press the shaft through the gear until the shoulder of the shaft touches the gear.
>
> **Note · Примечание**
> If an adequate press is **not** available, an oven can be used.
>
> **WARNING · Опасно**
> Wear protective clothing to reduce the possibility of personal injury from burns.
>
> **CAUTION · Осторожно**
> Do not exceed the specified time or temperature. Damage to the gear teeth will result.
>
> Heat the gear at 235°C (450°F) for **no less** than 1 hour, and **no more** than 6 hours.
>
> **WARNING · Опасно**
> Wear protective clothing to reduce the possibility of personal injury from burns.
>
> Slide the shaft in the gear.
>
> **CAUTION · Осторожно**
> Allow the air to cool the gear. Do not use water or oil to reduce the cooling time. Damage to the gear can result.
>
> Use a feeler gauge to measure the distance between the shoulder of the shaft and the gear.
>
> | Fuel Pump Drive Gear to Shaft |  |  |
> |---|---|---|
> | mm |  | in |
> | 0.05 | MAX | 0.002 |
>
> **Note · Примечание**
> If the distance between the gear and the shaft is **not** within specification, press the gear on until the specifications are meet.
>
> Position the grooved surface of the thrust bearing as illustrated. Install the thrust bearing.
>
> **Note · Примечание**
> An aluminum housing does **not** contain thrust bearings.
>
> Use Lubriplate™ Number 105, or equivalent. Lubricate the grooved surface of the thrust bearing (3).
>
> **Note · Примечание**
> An aluminum housing does **not** contain thrust bearings. Lubricate the machined thrust surface.
>
> With the grooved surface positioned up, slide the thrust bearing (3) over the shaft.
>
> Before installing the clamping washer (2), the beveled edge **must** be positioned as illustrated.
>
> Support the gear or the shaft.
>
> Install the coupling.
>
> Use an arbor press and a mandrel to push the coupling until it touches the clamping washer.
>
> The clamping washer **must** be positioned tightly between the coupling and the shoulder of the shaft.
>
> Install the pipe plug into the housing.
>
> Tighten the pipe plug.
>
> **Момент затяжки · Torque Value**
> 8 n•m [71 in-lb]
>
> **CAUTION · Осторожно**
> The capscrew must contain an oil drilling if an air compressor is to be mounted on the engine.
>
> Install the washer and the capscrew.
>
> Check the capscrew size to determine the correct torque value.
>
> **Момент затяжки · Torque Value**
> Capscrew 9.525 mm [0.375 in] 45 n•m [33 ft-lb]
>
> **Момент затяжки · Torque Value**
> Capscrew 12.7 mm [0.5 in] 100 n•m [74 ft-lb]
>
> Check the end clearance. If **not** within specification, inspect the assembly.
>
> | Assembly End Clearance |  |  |
> |---|---|---|
> | mm |  | in |
> | 0.05 | MIN | .002 |
> | 0.30 | MAX | .012 |
>
> ### Install
>
> Remove the two straight-threaded o-ring plugs from the timing holes in the front cover.
>
> Check the index mark alignment.
>
> **CAUTION · Осторожно**
> Do not use the "A" on the camshaft idler gear for the accessory drive alignment unless the "X" marks on the camshaft and the camshaft idler gears are aligned and centered in the upper timing plug hole. If the "X" marks are not visible in the upper hole, rotate the engine until the "X" marks on the camshaft gear and camshaft idler gear are aligned and centered in the upper timing plug hole.
>
> Install the accessory drive so that the "A" on the accessory drive gear is centered in the lower timing plug hole.
>
> Lubricate the bushing in the front gear cover with clean engine oil.
>
> Install the gasket, capscrews, and nut. Tighten the capscrews and the nut.
>
> **Момент затяжки · Torque Value**
> 48 n•m [35 ft-lb]
>
> Use the above torque value to tighten the capscrews a second time.
>
> Install the straight-threaded o-ring plugs. Tighten the o-ring plugs.
>
> **Момент затяжки · Torque Value**
> 25 n•m [221 in-lb]
>
> Install the accessory drive seal. [[20-001-003-tr — Accessory Drive Seal|Refer to Procedure 001-003 in Section 1]]
>
> **Note · Примечание**
> The keyway seal **must** be installed prior to installation of the key and the accessory drive pulley.
>
> Install the keyway seal (1).
>
> Install the accessory drive pulley woodruff key (2).
>
> ### Finishing Steps
>
> - Install the accessory drive pulley. [[20-009-004 — Accessory Drive Pulley|Refer to Procedure 009-004 in Section 9.]]
> - Install the air compressor, if equipped. [[20-012-014-tr — Air Compressor|Refer to Procedure 012-014 in Section 12.]]
> - Install the fuel pump and related components. [[20-005-016-tr — Fuel Pump|Refer to Procedure 005-016 in Section 5.]]
> - Fill the cooling system. [[20-008-018-tr — Cooling System|Refer to Procedure 008-018 in Section 8.]]
> - Connect the batteries. See equipment manufacturer service information.
> - Operate the engine to 70°C \[160°F\]. Check for leaks.
