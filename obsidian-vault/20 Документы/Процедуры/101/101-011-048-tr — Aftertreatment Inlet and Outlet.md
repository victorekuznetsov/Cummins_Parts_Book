---
type: "Процедура"
doc: "101-011-048-tr"
title_en: "Aftertreatment Inlet and Outlet"
modified: "2009-04-29"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "3666322"
figures: 11
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/101/101-011-048-tr.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/101-011-048-tr.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/101"
  - "перевод/машинный"
---

# Aftertreatment Inlet and Outlet

> [!abstract] Процедура · `101-011-048-tr`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[3666322 — ISM, ISMe, and QSM11 Service Manual|3666322]]
> **Секции:** Section 11 - Exhaust System - Group 11
> **Даты:** изменён 2009-04-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/101/101-011-048-tr.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/101-011-048-tr.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

> [!danger] ОПАСНО
> Во время регенерации температура выхлопных газов может достигать 800 ° C \[1500 ° F \], а температура поверхности выхлопной системы может превышать 700° C \[1300° F \], которая достаточно горячая, чтобы воспламенить или расплавить обычные материалы и сжечь людей. Выхлопные и выхлопные компоненты могут оставаться горячими после того, как транспортное средство перестало двигаться. Чтобы избежать риска пожара, повреждения имущества, ожогов или других серьезных травм, позвольте выхлопной системе остыть перед началом этой процедуры или ремонта и убедитесь, что горючие материалы не находятся там, где они могут вступать в контакт с горячими выхлопными газами или компонентами выхлопных газов.

> [!warning] ОСТОРОЖНО
> Катализационные элементы, содержащиеся в системе последующей обработки, изготовлены из хрупкого материала. Не опускайте и не ударяйте по стороне системы последующей обработки, так как это может привести к повреждению катализатора.

Из-за количества различных применений после обработки выхлопных газов эта процедура была написана как общая. Иллюстрации в рамках этой процедуры будут **не **представлять все заявки.

Система послеоперационной обработки состоит из четырех секций. Эти разделы являются:

1. Впуск
2. После обработки дизельным катализатором окисления
3. После обработки дизельным фильтром твердых частиц
4. Выход.

> [!note] Примечание
> В некоторых применениях катализатор может быть интегрирован во входную систему последующей обработки выхлопных газов.

![[11c00100.png]]

### Подготовительные операции

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Чтобы снизить риск искрения, минусовой (-) провод аккумуляторной батареи снимайте первым, а подсоединяйте последним.

> [!warning] ОСТОРОЖНО
> Датчик дифференциального давления дизельного фильтра твердых частиц после обработки не будет работать должным образом, если трубки датчика дифференциального давления не подключены к правильному порту. Отметьте места соединения датчика дифференциального давления перед отсоединением.

- Отсоедините аккумуляторные батареи.[[99-013-009 — Battery Cables and Connections|См. процедуру 013-009 (Кабели и соединения аккумуляторов) в разделе 13.]]
- Отметьте направление потока выхлопных газов, чтобы помочь в сборке.
- Нарисуйте ориентировочную линию по каждому из зажимов v-диапазона, секций канистра после обработки и точек подключения к выхлопной трубе. Это поможет вернуть секции и зажимы v-диапазона в исходную ориентацию во время установки.
- Отметьте количество каждого разъема датчика температуры выхлопных газов перед отключением датчика температуры выхлопных газов от проводной ремни.
- Отключите датчики температуры газа после обработки проводкой разъёмов ремня. См. процедуру 019-449 (После обработки газом датчик температуры) в разделе 19 Руководства по устранению неполадок и ремонту, CM871 и CM876 Электронные системы управления, двигатели ISX и ISM, Бюллетень 4021560.
- Удалите крепежные ремни или болты из впускного отверстия, если это необходимо. См. руководство изготовителя машины по диагностике и ремонту.
- Удалите крепежные ремни или болты из розетки, если это необходимо. См. руководство изготовителя машины по диагностике и ремонту.
- Отсоедините послеочистку дизельного фильтра с фильтром дифференциального давления от розетки, если это необходимо.[[101-011-047-tr — Aftertreatment Diesel Particulate Filter Differential Pressure Sensor Tubes|См. процедуру 011-047 (Трубы с дифференцированным давлением дизельного фильтра твердых частиц) в разделе 11.]]

![[ck800wa.png]]

### Снятие

> [!danger] ОПАСНО
> Масса этого узла больше 23 кг \[50 фунтов\]. Чтобы не получить тяжёлую травму, поднимайте этот узел с помощником или подходящим грузоподъёмным оборудованием.

> [!warning] ОСТОРОЖНО
> Катализационные элементы, содержащиеся в системе последующей обработки, изготовлены из хрупкого материала. Не опускайте и не ударяйте по стороне системы последующей обработки, так как это может привести к повреждению катализатора.

В некоторых применениях катализатор интегрируется в вход после обработки.[[101-011-046-tr — Aftertreatment Diesel Particulate Filter Differential Pressure Sensor Mounting|См. процедуру 011-046 (Дизельная фильтрация дизельных частиц Дифференциальный датчик давления Монтажная кронштейн) в разделе 11 для удаления крепежной кронштейн датчика дифференциального давления.]]

Поддерживают катализатор и после обработки дизельный фильтр твердых частиц, чтобы избежать нанесения консольной нагрузки на соединения v-диапазона.

Удалите зажим TorcaTM или v-диапазон, используемый для подключения системы последующей обработки к выхлопной трубе, если это необходимо.

Удалите зажим v-диапазона, соединяющий вход с катализатором, если это необходимо.

Удалите зажим v-диапазона, соединяющий выход с фильтром для твердых частиц дизельного топлива после обработки, если это необходимо.

Удалить и выбросить прокладки.

![[11c00132.png]]

### Разборка

Удалите датчик температуры газа после обработки от босса во входе и / или выходе, если это необходимо. См. процедуру 019-449 (После обработки газом датчик температуры) в разделе 19 Руководства по устранению неполадок и ремонту, CM871 и CM876 Электронные системы управления, двигатели ISX и ISM, Бюллетень 4021560.

![[11d00112.png]]

### Очистка и проверка при повторном использовании

Осмотрите впускные и выпускные канистры для последующей обработки на наличие трещин или других повреждений.

Осмотрите после обработки датчик температуры газа босса резьбы для повреждения, если датчик был удален.

Осмотрите после обработки дизельный фильтр твердых частиц дифференциального давления на резьбу босса трубы на предмет повреждения, если трубка была удалена.

Если повреждение резьбы обнаружено на резьбе главного датчика температуры газа после обработки или резьбе босса датчика дифференциального давления, спираль должна использоваться для ремонта.

![[11d00107.png]]

Подготовка к облицовке - Используйте закладной нож для удаления любого остаточного прокладочного материала из фланцев на фильтре для твердых частиц дизельного топлива после обработки.

Избегайте сброса фрагментов прокладочного материала в фильтр для твердых частиц дизельного топлива после обработки.

Не использовать сжатый воздух для удаления фрагментов прокладочного материала, которые упали в фильтр во время удаления прокладки.

Делайте **не** шлифовку на поверхности фланга, так как это может повредить фланец и вызвать утечку соединения.

![[11c00102.png]]

Осмотрите зажимы v-диапазона и крепежные ремни на наличие признаков чрезмерного расширения.

Группа не должна быть согнута или повреждена.

Осмотрите зажим v-диапазона и крепление резьбы ремня на предмет повреждения.

Заменить зажим v-диапазона или крепежный ремень, если обнаружено повреждение.

![[11d00092.png]]

### Сборка

Установите датчик температуры газа после обработки в боссе на входе и / или выходе. См. процедуру 019-449 (После обработки газом датчик температуры) в разделе 19 Руководства по устранению неполадок и ремонту, CM871 и CM876 Электронные системы управления, двигатели ISX и ISM, Бюллетень 4021560.

![[11d00112.png]]

### Установка

Нанесите на протекторы зажимов v-диапазона и зажимов TorcaTM слой антисептического соединения.

Секция после обработки содержит дисперсный датчик давления трубки босса. Выровнять регулятор дифференциального давления с помощью гайки датчика дифференциального давления перед зажимом v-диапазона или зажимом TorcaTM.

> [!note] Примечание
> Если зажим TorcaTM заменен во время обслуживания, обязательно замените его другим зажимом TorcaTM. **не** использовать u-болт в качестве зажима для замены. Зажимы U-bolt могут раздавить выхлопную трубу и затруднить удаление системы последующей обработки для будущей службы.

![[11c00223.png]]

Закрепите зажимы TorcaTM или зажимы v-диапазона, используемые для обеспечения входа и выхода последующей обработки на выхлопную трубу.

Момент затяжки:

Зажим Torca

Момент затяжки:

Зажим для V-диапазона

Установите новую прокладку между зажимными соединениями v-диапазона, которые были отключены.

Установите зажим v-диапазона, используемый для подключения розетки к фильтру для твердых частиц дизельного топлива после обработки, если это необходимо.

Установите зажим v-диапазона, чтобы при необходимости подключить вход к катализатору.

Зажимы v-диапазона затягиваются.

> [!tip] Момент затяжки
> 20 Н·м [177 фунт-дюйм]

![[11c00132.png]]

### Завершающие операции

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Чтобы снизить риск искрения, минусовой (-) провод аккумуляторной батареи снимайте первым, а подсоединяйте последним.

> [!warning] ОСТОРОЖНО
> Если разъёмы проводов датчика температуры не подключены к надлежащим местам после установки, может возникнуть повреждение системы последующей обработки.

> [!warning] ОСТОРОЖНО
> Датчик дифференциального давления дизельного фильтра твердых частиц после обработки не будет работать должным образом, если трубки датчика дифференциального давления не подключены к правильному порту. Установите датчики дифференциального давления, как это было отмечено при разборке.

- Установите крепежные ремни или болты на входе, если это необходимо. См. руководство изготовителя машины по диагностике и ремонту.
- Установите крепежные ремни или болты от розетки, если это необходимо. См. руководство изготовителя машины по диагностике и ремонту.
- Подключите датчик температуры газа после обработки проводкой разъёмы жгута, если это необходимо. См. процедуру 019-449 (После обработки газом датчик температуры) в разделе 19 Руководства по устранению неполадок и ремонту, CM871 и CM876 Электронные системы управления, двигатели ISX и ISM, Бюллетень 4021560.
- Подключите после обработки дизельный фильтр с дифференцированным давлением к выходу, если это необходимо.[[101-011-047-tr — Aftertreatment Diesel Particulate Filter Differential Pressure Sensor Tubes|См. процедуру 011-047 (Трубы с дифференцированным давлением дизельного фильтра твердых частиц) в разделе 11.]]
- Подключите аккумуляторы автомобиля.[[99-013-009 — Battery Cables and Connections|См. процедуру 013-009 (Кабели и соединения аккумуляторов) в разделе 13.]]
- Управляйте транспортным средством на динамометре или выполняйте дорожные испытания с двигателем при номинальной нагрузке в течение как минимум 5 минут, чтобы убедиться, что система последующей обработки работает должным образом. См. процедуру для двигателей ISX, 010-024 (утечки воздуха, системы всасывания и выхлопа) в разделе 10 в руководстве по обслуживанию SignatureTM, ISX и QSX15, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]].[[35-010-024-tr — Air Leaks, Air Intake and Exhaust Systems|См. процедуру для двигателей ISM, 010-024 (системы воздухозаборников, воздухозаборников и выхлопных газов) в разделе 10 в руководстве по обслуживанию двигателей ISM, ISMe и QSM11, Бюллетень 3666322.]]

![[ck800wa.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> **WARNING · Опасно**
> During regeneration, exhaust gas temperature could reach 800°C \[1500°F\], and exhaust system surface temperature could exceed 700°C \[1300°F\], which is hot enough to ignite or melt common materials, and to burn people. The exhaust and exhaust components can remain hot after the vehicle has stopped moving. To avoid the risk of fire, property damage, burns or other serious personal injury, allow the exhaust system to cool before beginning this procedure or repair and make sure that no combustible materials are located where they are likely to come in contact with hot exhaust or exhaust components.
>
> **CAUTION · Осторожно**
> The catalyst elements contained in the aftertreatment system are made of brittle material. Do not drop or strike the side of the aftertreatment system as damage to the catalyst element can result.
>
> Due to the number of various exhaust aftertreatment applications, this procedure has been written to be generic. Illustrations within this procedure will **not** represent all applications.
>
> The aftertreatment system is composed of four sections. These sections are:
>
> 1. Inlet
> 2. Aftertreatment diesel oxidation catalyst
> 3. Aftertreatment diesel particulate filter
> 4. Outlet.
>
> **Note · Примечание**
> In some applications, the catalyst can be integrated into the inlet of the exhaust aftertreatment system.
>
> ### Preparatory Steps
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> **CAUTION · Осторожно**
> The aftertreatment diesel particulate filter differential pressure sensor will not operate properly if the differential pressure sensor tubes are not connected to the correct port. Mark the differential pressure sensor tube connection locations before disconnecting.
>
> - Disconnect the batteries. [[99-013-009 — Battery Cables and Connections|Refer to Procedure 013-009 (Battery Cables and Connections) in Section 13.]]
> - Mark the direction of exhaust flow to aid in assembly.
> - Draw an orientation reference line across each of the v-band clamps, aftertreatment canister sections, and connection points to the tailpipe. This will aid in returning the sections and the v-band clamps to their original orientation during installation.
> - Mark the number of each exhaust gas temperature sensor connector prior to disconnecting the exhaust temperature sensor from the wiring harness.
> - Disconnect the aftertreatment gas temperature sensor wiring harness connectors. Refer to Procedure 019-449 (Aftertreatment Gas Temperature Sensor) in Section 19 of the Troubleshooting and Repair Manual, CM871 and CM876 Electronic Control Systems, ISX and ISM Engines, Bulletin 4021560.
> - Remove the mounting straps or bolts from the inlet, if necessary. Refer to the OEM troubleshooting and repair manual.
> - Remove the mounting straps or bolts from the outlet, if necessary. Refer to the OEM troubleshooting and repair manual.
> - Disconnect the aftertreatment diesel particulate filter differential pressure sensor tube from the outlet, if necessary. [[101-011-047-tr — Aftertreatment Diesel Particulate Filter Differential Pressure Sensor Tubes|Refer to Procedure 011-047 (Aftertreatment Diesel Particulate Filter Differential Pressure Sensor Tubes) in Section 11.]]
>
> ### Remove
>
> **WARNING · Опасно**
> This component or assembly weighs greater than 23 kg \[50 lb\]. To prevent serious personal injury, be sure to have assistance or use appropriate lifting equipment to lift this component or assembly.
>
> **CAUTION · Осторожно**
> The catalyst elements contained in the aftertreatment system are made of brittle material. Do not drop or strike the side of the aftertreatment system as damage to the catalyst element can result.
>
> In some applications, the catalyst is integrated into the aftertreatment inlet. [[101-011-046-tr — Aftertreatment Diesel Particulate Filter Differential Pressure Sensor Mounting|Refer to Procedure 011-046 (Aftertreatment Diesel Particulate Filter Differential Pressure Sensor Mounting Bracket) in Section 11 for removal of the differential pressure sensor mounting bracket.]]
>
> Support the catalyst and aftertreatment diesel particulate filter to avoid applying a cantilevered load on the v-band joints.
>
> Remove the Torca™ or v-band clamp used to connect the aftertreatment system to the exhaust pipe, if necessary.
>
> Remove the v-band clamp connecting the inlet to the catalyst, if necessary.
>
> Remove the v-band clamp connecting the outlet to the aftertreatment diesel particulate filter, if necessary.
>
> Remove and discard the gaskets.
>
> ### Disassemble
>
> Remove the aftertreatment gas temperature sensor from the boss in the inlet and/or outlet, if necessary. Refer to Procedure 019-449 (Aftertreatment Gas Temperature Sensor) in Section 19 of the Troubleshooting and Repair Manual, CM871 and CM876 Electronic Control Systems, ISX and ISM Engines, Bulletin 4021560.
>
> ### Clean and Inspect for Reuse
>
> Inspect the aftertreatment inlet and outlet canisters for cracks or other damage.
>
> Inspect the aftertreatment gas temperature sensor boss threads for damage, if the sensor was removed.
>
> Inspect the aftertreatment diesel particulate filter differential pressure sensor tube boss threads for damage, if the tube was removed.
>
> If thread damage is found on the aftertreatment gas temperature sensor boss threads or differential pressure sensor tube boss threads, a helicoil **must** be used for repair.
>
> Flange Preparation - Use a putty knife to remove any residual gasket material from the flanges on the aftertreatment diesel particulate filter.
>
> Avoid dropping fragments of gasket material into the aftertreatment diesel particulate filter.
>
> Do **not** use compressed air to remove fragments of gasket material that have fallen into the filter during gasket removal.
>
> Do **not** grind on the flange surface, as this can damage the flange and cause the connection to leak.
>
> Inspect the v-band clamps and mounting straps for signs of over-extension.
>
> The band **must not** be bent or damaged.
>
> Inspect the v-band clamp and mounting strap threads for damage.
>
> Replace the v-band clamp or mounting strap if damage is found.
>
> ### Assemble
>
> Install the aftertreatment gas temperature sensor in the boss on the inlet and/or outlet. Refer to Procedure 019-449 (Aftertreatment Gas Temperature Sensor) in Section 19 of the Troubleshooting and Repair Manual, CM871 and CM876 Electronic Control Systems, ISX and ISM Engines, Bulletin 4021560.
>
> ### Install
>
> Apply a coat of anti-seize compound on the treads of the v-band clamps and Torca™ clamps.
>
> The aftertreatment outlet section contains a differential pressure sensor tube boss. Align the differential pressure sensor tube boss with the differential pressure sensor tube nut prior to tightening the v-band clamp or the Torca™ clamp.
>
> **Note · Примечание**
> If the Torca™ clamp is replaced during service, be sure to replace it with another Torca™ clamp. Do **not** use a u-bolt as a replacement clamp. U-bolt clamps can crush the tailpipe and make it difficult to remove the aftertreatment system for future service.
>
> Tighten the Torca™ clamps or v-band clamps used to secure the inlet and outlet of the aftertreatment to the exhaust pipe.
>
> Torque Value:
>
> Torca™ Clamp
>
> Torque Value:
>
> V-Band Clamp
>
> Install a new gasket between the v-band clamp joints that have been disconnected.
>
> Install the v-band clamp used to connect the outlet to the aftertreatment diesel particulate filter, if necessary.
>
> Install the v-band clamp use to connect the inlet to the catalyst, if necessary.
>
> Tighten the v-band clamps.
>
> **Момент затяжки · Torque Value**
> 20 n•m [177 in-lb]
>
> ### Finishing Steps
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> **CAUTION · Осторожно**
> If the temperature sensor wire connectors are not connected to the proper locations after installation, aftertreatment system damage can result.
>
> **CAUTION · Осторожно**
> The aftertreatment diesel particulate filter differential pressure sensor will not operate properly if the differential pressure sensor tubes are not connected to the correct port. Install the differential pressure sensor tubes as noted during disassembly.
>
> - Install the mounting straps or bolts to the inlet, if necessary. Refer to the OEM troubleshooting and repair manual.
> - Install the mounting straps or bolts from the outlet, if necessary. Refer to the OEM troubleshooting and repair manual.
> - Connect the aftertreatment gas temperature sensor wiring harness connectors, if necessary. Refer to Procedure 019-449 (Aftertreatment Gas Temperature Sensor) in Section 19 of the Troubleshooting and Repair Manual, CM871 and CM876 Electronic Control Systems, ISX and ISM Engines, Bulletin 4021560.
> - Connect the aftertreatment diesel particulate filter differential pressure sensor tube to the outlet, if necessary. [[101-011-047-tr — Aftertreatment Diesel Particulate Filter Differential Pressure Sensor Tubes|Refer to Procedure 011-047 (Aftertreatment Diesel Particulate Filter Differential Pressure Sensor Tubes) in Section 11.]]
> - Connect the vehicle batteries. [[99-013-009 — Battery Cables and Connections|Refer to Procedure 013-009 (Battery Cables and Connections) in Section 13.]]
> - Operate the vehicle on a dynamometer or perform a road test with the engine at rated load for a minimum of 5 minutes to make sure the aftertreatment system is performing properly. Refer to Procedure For ISX engines, 010-024 (Air Leaks, Air Intake and Exhaust Systems) in Section 10 in the Signature™, ISX, and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. [[35-010-024-tr — Air Leaks, Air Intake and Exhaust Systems|Refer to Procedure For ISM engines, 010-024 (Air Leaks, Air Intake and Exhaust Systems) in Section 10 in the ISM, ISMe, and QSM11 Engines Service Manual, Bulletin 3666322.]]
