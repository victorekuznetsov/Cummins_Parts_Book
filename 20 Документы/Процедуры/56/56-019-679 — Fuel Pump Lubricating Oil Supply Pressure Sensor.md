---
aliases:
  - "Датчик давления подачи масла к топливному насосу"
type: "Процедура"
doc: "56-019-679"
title_en: "Fuel Pump Lubricating Oil Supply Pressure Sensor"
title_ru: "Датчик давления подачи масла к топливному насосу"
modified: "2020-05-14"
engines:
  - "33239746"
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
manuals:
  - "4022102"
figures: 8
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/56/56-019-679.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/56-019-679.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/56"
  - "перевод/машинный"
---

# Fuel Pump Lubricating Oil Supply Pressure Sensor
**Датчик давления подачи масла к топливному насосу**

> [!abstract] Процедура · `56-019-679`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Входит в руководства:** [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M|4022102]]
> **Секции:** Section 19 - Electronic Controls - Group 19
> **Даты:** изменён 2020-05-14
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/56/56-019-679.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/56-019-679.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Диаграмма компонентов

![[07e00235.png]]

Двигатель топливный насос моторное масло датчик давления

### Выбор сервисного инструмента

#### Рекомендованный сервисный инструмент Cummins®

- Инструмент электронного обслуживания INSITETM

#### Дополнительные сервисные позиции

- Никаких дополнительных предметов обслуживания не требуется.

### Общие сведения

Датчик давления моторного масла топливного насоса двигателя измеряет давление моторного масла топливного насоса на выходе головки фильтра моторного масла. Датчик давления моторного масла топливного насоса двигателя расположен в головке фильтра моторного масла топливного насоса двигателя, установленной на верхней части привода адаптера топливного насоса. Некоторые двигатели могут иметь головку фильтра, установленную удаленно.

Разъем для спаривания на ремне проводов двигателя является разъемом ITT CannonTM.

Параметр оснастки электронного сервиса INSITETM для этого датчика — давление моторного масла топливного насоса. Значение датчика отображается как измерительное давление.

### Первичная проверка

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Чтобы снизить риск искрения, минусовой (-) провод аккумуляторной батареи снимайте первым, а подсоединяйте последним.

Отключите батареи и источники питания. См. сервисную документацию изготовителя оборудования.

Отключите линию подачи воздуха от двигателя запуска воздуха, если он оборудован. См. процедуру 012-022 в разделе 12.

> [!danger] ОПАСНО
> По заключению ряда государственных органов отработанное моторное масло может обладать канцерогенным действием и вредить репродуктивной функции. Не вдыхайте пары, не допускайте попадания внутрь и длительного контакта с отработанным моторным маслом. Если деталь не используется повторно, утилизируйте её по местным природоохранным требованиям.

> [!danger] ОПАСНО
> Чтобы снизить риск травмы, не допускайте попадания горячего масла на кожу.

> [!note] Примечание
> Некоторое масло может стекать из порта в головке фильтра, когда пробка удаляется.

Удалите фильтр для фильтрации топливных насосов напорного отверстия для розетки (2).

Установите CompuchekTM в порт M14.

Подключите датчик давления и мультиметр к установке CompuchekTM.

![[07800464.png]]

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Чтобы снизить риск искрения, минусовой (-) провод аккумуляторной батареи снимайте первым, а подсоединяйте последним.

Подключите батареи и источники питания. См. сервисную документацию изготовителя оборудования.

Подключите линию подачи воздуха к пусковому двигателю, если он оборудован. См. процедуру 012-022 в разделе 12.

Подключите инструмент электронного сервиса INSITETM к шине данных CAN.

Запускайте двигатель и бегите на холостом ходу.

Неработающий двигатель не менее 5 минут, чтобы обеспечить стабилизацию давления масла.

Если значение давления моторного масла топливного насоса в электронном сервисном оборудовании INSITETM составляет **не** в пределах 48 кПа \[7 psi\] измерения давления преобразователя, замените датчик давления моторного масла топливного насоса двигателя.

![[19203975.png]]

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Чтобы снизить риск искрения, минусовой (-) провод аккумуляторной батареи снимайте первым, а подсоединяйте последним.

Выключи двигатель.

Отключите батареи и источники питания. См. информацию о сервисе производителя оборудования

Отключите линию подачи воздуха от двигателя запуска воздуха, если он оборудован. См. процедуру 012-022 в разделе 12.

> [!danger] ОПАСНО
> По заключению ряда государственных органов отработанное моторное масло может обладать канцерогенным действием и вредить репродуктивной функции. Не вдыхайте пары, не допускайте попадания внутрь и длительного контакта с отработанным моторным маслом. Если деталь не используется повторно, утилизируйте её по местным природоохранным требованиям.

> [!danger] ОПАСНО
> Чтобы снизить риск травмы, не допускайте попадания горячего масла на кожу.

Удалить CompuchekTM fitting.

Установите M14 прямой резьбовой уплотнитель. Используйте новое уплотнение.

> [!tip] Момент затяжки
> 11 Н·м [98 фунт-дюйм]

![[07800464.png]]

### Подготовительные операции

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Чтобы снизить риск искрения, минусовой (-) провод аккумуляторной батареи снимайте первым, а подсоединяйте последним.

- Отключите батареи и источники питания. См. сервисную документацию изготовителя оборудования.
- Отключите линию подачи воздуха от двигателя запуска воздуха, если он оборудован. См. процедуру 012-022 в разделе 12.

### Снятие

Отсоедините электропроводку двигателя от датчика давления моторного масла топливного насоса двигателя, повернув разъем **против часовой стрелки**.

Удалить датчик.

Удалить и выбросить уплотнение.

![[07e00235.png]]

### Очистка и проверка при повторном использовании

Датчик давления моторного масла с чистым топливным насосом двигателя. Используйте чистую, без винта ткань.

Проверьте датчик.

Заменить датчик, если:

- Скорлупа коннектора треснула или сломалась
- Уплотнение разъёма отсутствует или повреждено
- Коннекторные терминалы, загрязненные грязью, мусором или влагой
- Коннекторные терминалы корродированы, согнуты, сломаны, отодвинуты назад или расширены
- Поврежденные или разъединенные.

![[19j00113.png]]

Проверьте разъём жгута с электропроводкой двигателя.

Заменить разъем, если:

- Снаряд треснул или сломался
- Тюлени отсутствуют или повреждены
- Терминалы, загрязненные грязью, мусором или влагой
- Терминалы разъединены, согнуты, сломаны, отодвинуты назад или расширены.

[[99-019-209 — ITT Cannon Connector Series|См. процедуру 019-209]]В разделе 19.

![[19j00114.png]]

### Установка

Установите датчик давления моторного масла топливного насоса двигателя. Используйте новое уплотнение.

> [!tip] Момент затяжки
> 11 Н·м [98 фунт-дюйм]

Подключите проводку расширения к датчику.

![[07e00235.png]]

### Завершающие операции

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Чтобы снизить риск искрения, минусовой (-) провод аккумуляторной батареи снимайте первым, а подсоединяйте последним.

- Подключите линию подачи воздуха к пусковому двигателю, если он оборудован. См. процедуру 012-022 в разделе 12.
- Подключите батареи и источники питания. См. сервисную документацию изготовителя оборудования.
- Заполните моторное масло, если это необходимо.[[56-007-037-tr — Lubricating Oil System|См. процедуру 007-037]]В разделе 7.
- Операционный двигатель. Проверьте на отсутствие утечек.


> [!quote]- Original (English) · английский оригинал
> ### Component Diagram
>
> Engine Fuel Pump Lubricating Oil Pressure Sensor
>
> ### Select Service Tools
>
> #### Recommended Cummins® Service Tools
>
> - INSITE™ electronic service tool
>
> #### Additional Service Items
>
> - No additional service items required.
>
> ### General Information
>
> The Engine fuel pump lubricating oil pressure sensor measures fuel pump lubricating oil pressure at the outlet of the lubricating oil filter head. The engine fuel pump lubricating oil pressure sensor is located in the engine fuel pump lubricating oil filter head mounted to the top of the fuel pump adapter drive. Certain engines may have the filter head mounted remotely.
>
> The mating connector on the engine wiring harness is an ITT Cannon™ connector.
>
> The INSITE™ electronic service tool parameter for this sensor is fuel pump lubricating oil pressure. The sensor value is displayed as gauge pressure.
>
> ### Initial Check
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> Disconnect batteries and power supplies. See equipment manufacturer service information.
>
> Disconnect air supply line from air starting motor, if equipped. Refer to Procedure 012-022 in Section 12.
>
> **WARNING · Опасно**
> Some state and federal agencies have determined that used engine oil can be carcinogenic and cause reproductive toxicity. Avoid inhalation of vapors, ingestion, and prolonged contact with used engine oil. If not reused, dispose of in accordance with local environmental regulations.
>
> **WARNING · Опасно**
> To reduce the possibility of personal injury, avoid direct contact of hot oil with your skin.
>
> **Note · Примечание**
> Some oil may drain from port in filter head when plug is removed.
>
> Remove the Fuel Pump Lubricating Oil Filter Head Outlet Pressure Port (2).
>
> Install Compuchek™ fitting into M14 port.
>
> Connect pressure transducer and multimeter to Compuchek™ fitting.
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> Connect batteries and power supplies. See equipment manufacturer service information.
>
> Connect air supply line to air starting motor, if equipped. Refer to Procedure 012-022 in Section 12.
>
> Connect INSITE™ electronic service tool to engine data link.
>
> Start engine and run at idle.
>
> Idle engine for at least 5 minutes to allow oil pressure to stabilize.
>
> If fuel pump lubricating oil pressure value in INSITE™ electronic service tool is **not** within 48 kPa \[7 psi\] of pressure transducer measurement, replace Engine fuel pump lubricating oil pressure sensor.
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> Shut engine OFF.
>
> Disconnect batteries and power supplies. See equipment manufacturer service information
>
> Disconnect air supply line from air starting motor, if equipped. Refer to Procedure 012-022 in Section 12.
>
> **WARNING · Опасно**
> Some state and federal agencies have determined that used engine oil can be carcinogenic and cause reproductive toxicity. Avoid inhalation of vapors, ingestion, and prolonged contact with used engine oil. If not reused, dispose of in accordance with local environmental regulations.
>
> **WARNING · Опасно**
> To reduce the possibility of personal injury, avoid direct contact of hot oil with your skin.
>
> Remove Compuchek™ fitting.
>
> Install M14 straight thread o-ring plug. Use new o-ring seal.
>
> **Момент затяжки · Torque Value**
> 11 n•m [98 in-lb]
>
> ### Preparatory Steps
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> - Disconnect batteries and power supplies. See equipment manufacturer service information.
> - Disconnect air supply line from air starting motor, if equipped. Refer to Procedure 012-022 in Section 12.
>
> ### Remove
>
> Disconnect engine wiring harness from Engine fuel pump lubricating oil pressure sensor by turning connector **counterclockwise**.
>
> Remove sensor.
>
> Remove and discard o-ring seal.
>
> ### Clean and Inspect for Reuse
>
> Clean Engine fuel pump lubricating oil pressure sensor. Use clean, lint-free cloth.
>
> Inspect sensor.
>
> Replace sensor if:
>
> - Connector shell cracked or broken
> - Connector seal missing or damaged
> - Connector terminals contaminated with dirt, debris, or moisture
> - Connector terminals corroded, bent, broken, pushed back, or expanded
> - Threads damaged or corroded.
>
> Inspect engine wiring harness connector.
>
> Replace connector if:
>
> - Shell cracked or broken
> - Seals missing or damaged
> - Terminals contaminated with dirt, debris, or moisture
> - Terminals corroded, bent, broken, pushed back, or expanded.
>
> [[99-019-209 — ITT Cannon Connector Series|Refer to Procedure 019-209]] in Section 19.
>
> ### Install
>
> Install Engine fuel pump lubricating oil pressure sensor. Use new o-ring seal.
>
> **Момент затяжки · Torque Value**
> 11 n•m [98 in-lb]
>
> Connect extension wiring harness to sensor.
>
> ### Finishing Steps
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> - Connect air supply line to air starting motor, if equipped. Refer to Procedure 012-022 in Section 12.
> - Connect batteries and power supplies. See equipment manufacturer service information.
> - Fill lubricating oil pan, if necessary. [[56-007-037-tr — Lubricating Oil System|Refer to Procedure 007-037]] in Section 7.
> - Operate engine. Check for leaks.
