---
type: "Процедура"
doc: "56-007-110-tr"
title_en: "Fuel Pump Drive Lubricating Oil Filter"
modified: "2020-05-14"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
  - "33239746"
families:
  - "QSK60"
  - "QSK60 CM2150 MCRS"
manuals:
  - "4021530"
figures: 7
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/56/56-007-110-tr.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/56-007-110-tr.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK60"
  - "двигатель/QSK60CM2150MCRS"
  - "группа/56"
  - "перевод/машинный"
---

# Fuel Pump Drive Lubricating Oil Filter

> [!abstract] Процедура · `56-007-110-tr`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]]
> **Семейство:** QSK60, QSK60 CM2150 MCRS
> **Входит в руководства:** [[4021530 — QSK45 and QSK60 Service Manual|4021530]]
> **Секции:** Section 7 - Lubricating Oil System - Group 07
> **Даты:** изменён 2020-05-14
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/56/56-007-110-tr.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/56-007-110-tr.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Взрывной вид

![[07800463.png]]

Фильтр моторного масла Fuel Pump Drive Exploded View

1. Масляный фильтр

### Выбор сервисного инструмента

#### Рекомендованный сервисный инструмент Cummins®

- Масляный фильтр, номер детали 3400157, или эквивалент

#### Дополнительные сервисные позиции

- Не требуется никаких дополнительных услуг

### Общие сведения

Выделенный фильтр для моторного масла полного потока используется для обеспечения дополнительной защиты критически важных компонентов в топливном насосе высокого давления.

Фильтр устанавливается на специальном головке фильтра на верхней части привода адаптера топливного насоса. Некоторые двигатели могут иметь головку фильтра, установленную удаленно.

Все компоненты, обработанные в этой процедуре, весят менее 23 кг [50 фунтов].

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

Удалите фильтр для фильтрации топливных насосов на выходе из порта давления (2).

Установите CompuchekTM в порт M14.

Подключите датчик давления и мультиметр к установке CompuchekTM.

![[07800464.png]]

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Чтобы снизить риск искрения, минусовой (-) провод аккумуляторной батареи снимайте первым, а подсоединяйте последним.

- Подключите батареи и источники питания. См. сервисную документацию изготовителя оборудования.
- Подключите линию подачи воздуха от воздушного пускового двигателя, если он оборудован. См. процедуру 012-022 в разделе 12.

Подключите инструмент электронного сервиса INSITETM к шине данных CAN.

Запускайте двигатель и бегите на холостом ходу.

Неработающий двигатель не менее 5 минут, чтобы обеспечить стабилизацию давления масла.

Минимальный порог для датчика давления масла топливного насоса при скорости двигателя выше 1400 об/мин составляет 250 кПа[37 psi].

Минимальный порог для датчика давления масла топливного насоса при скорости двигателя ниже 1000 об/мин составляет 150 кПа[22 psi].

Если показания давления масла топливного насоса ниже минимального порога при номинальной оборотной массе, замените фильтр моторного масла на привод топливного насоса.

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
> 11 Н·м [96 фунт-дюйм]

![[07800464.png]]

### Подготовительные операции

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Чтобы снизить риск искрения, минусовой (-) провод аккумуляторной батареи снимайте первым, а подсоединяйте последним.

- Отключите батареи и источники питания. См. сервисную документацию изготовителя оборудования.
- Отключите линию подачи воздуха от двигателя запуска воздуха, если он оборудован. См. процедуру 012-022 в разделе 12.

### Снятие

> [!danger] ОПАСНО
> Чтобы снизить риск травмы, не допускайте попадания горячего масла на кожу.

> [!danger] ОПАСНО
> По заключению ряда государственных органов отработанное моторное масло может обладать канцерогенным действием и вредить репродуктивной функции. Не вдыхайте пары, не допускайте попадания внутрь и длительного контакта с отработанным моторным маслом. Если деталь не используется повторно, утилизируйте её по местным природоохранным требованиям.

Удалите масляный фильтр. Используйте гаечный ключ масляного фильтра, номер детали 3400157 или эквивалент.

Фильтр для сброса, если **не** требуется для анализа.

![[07800461.png]]

### Очистка и проверка при повторном использовании

Чистая масляная фильтрующая головка уплотняющая поверхность. Используйте безмятежную ткань.

Проверить масляный фильтр головки.

Заменить головку фильтра, если:

- Разбитый
- поврежденный резьба

![[07x00164.png]]

### Установка

Моторное масло фильтрует резиновые уплотнения. Используйте чистое моторное масло.

**не** фильтр для масла.

![[07j00132.png]]

> [!warning] ОСТОРОЖНО
> Механическое затяжение может исказить резьбу или повредить уплотнение фильтрующего элемента.

> [!warning] ОСТОРОЖНО
> Найдите гаечный ключ масляного фильтра рядом с верхней частью канистра масляного фильтра. Это уменьшит вероятность повреждения масляного фильтра.

Установите масляный фильтр. Поверните, пока не соприкасаются уплотнительные контакты фильтра головки уплотняющей поверхности.

Поверните масляный фильтр дополнительно 3⁄4 поворота. Используйте гаечный ключ масляного фильтра, номер детали 3400157 или эквивалент.

![[07800465.png]]

### Завершающие операции

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Чтобы снизить риск искрения, минусовой (-) провод аккумуляторной батареи снимайте первым, а подсоединяйте последним.

- Подключите линию подачи воздуха к пусковому двигателю, если он оборудован. См. процедуру 012-022 в разделе 12.
- Подключите батареи и источники питания. См. сервисную документацию изготовителя оборудования.
- Заполните моторное масло, если это необходимо.[[56-007-037-tr — Lubricating Oil System|См. процедуру 007-037]]В разделе 7.
- Операционный двигатель. Проверьте на отсутствие утечек.


> [!quote]- Original (English) · английский оригинал
> ### Exploded View
>
> Fuel Pump Drive Lubricating Oil Filter Exploded View
>
> 1. Lubricating oil filter
>
> ### Select Service Tools
>
> #### Recommended Cummins® Service Tools
>
> - Oil filter wrench, Part Number 3400157, or equivalent
>
> #### Additional Service Items
>
> - No additional service items required
>
> ### General Information
>
> A dedicated full flow lubricating oil filter is used to provide added protection to critical components in the high-pressure fuel pump.
>
> The filter is mounted on a dedicated filter head on the top of the fuel pump adapter drive. Certain engines may have the filter head mounted remotely.
>
> All components handled in this procedure weigh less than 23 kg \[50 lb\].
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
> Remove the Fuel Pump Oil Filter Head Outlet Pressure Port (2).
>
> Install Compuchek™ fitting into M14 port.
>
> Connect pressure transducer and multimeter to Compuchek™ fitting.
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> - Connect batteries and power supplies. See equipment manufacturer service information.
> - Connect air supply line from air starting motor, if equipped. Refer to Procedure 012-022 in Section 12.
>
> Connect INSITE™ electronic service tool to engine data link.
>
> Start engine and run at idle.
>
> Idle engine for at least 5 minutes to allow oil pressure to stabilize.
>
> The minimum threshold for fuel pump oil pressure sensor at engine speed above 1400 rpm is 250 kPa \[37 psi\].
>
> The minimum threshold for fuel pump oil pressure sensor at engine speed below 1000 rpm is 150 kPa \[22 psi\].
>
> If the fuel pump oil pressure reading is below the minimum threshold at rated rpm, replace the fuel pump drive lubricating oil filter.
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
> 11 n•m [96 in-lb]
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
> **WARNING · Опасно**
> To reduce the possibility of personal injury, avoid direct contact of hot oil with your skin.
>
> **WARNING · Опасно**
> Some state and federal agencies have determined that used engine oil can be carcinogenic and cause reproductive toxicity. Avoid inhalation of vapors, ingestion, and prolonged contact with used engine oil. If not reused, dispose of in accordance with local environmental regulations.
>
> Remove oil filter. Use oil filter wrench, Part Number 3400157, or equivalent.
>
> Discard filter if **not** required for analysis.
>
> ### Clean and Inspect for Reuse
>
> Clean oil filter head sealing surface. Use lint-free cloth.
>
> Inspect oil filter head.
>
> Replace filter head if:
>
> - Cracked
> - Threads damaged
>
> ### Install
>
> Lubricate oil filter rubber seals. Use clean engine oil.
>
> Do **not** prefill oil filter.
>
> **CAUTION · Осторожно**
> Mechanical overtightening can distort threads or damage filter element seal.
>
> **CAUTION · Осторожно**
> Locate oil filter wrench near top of oil filter canister. This will reduce possibility of damaging oil filter.
>
> Install the oil filter. Turn until seal contacts filter head sealing surface.
>
> Turn oil filter additional ¾ turn. Use oil filter wrench, Part Number 3400157, or equivalent.
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
