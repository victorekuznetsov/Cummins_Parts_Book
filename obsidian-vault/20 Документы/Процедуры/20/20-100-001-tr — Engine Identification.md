---
aliases:
  - "Идентификация двигателя"
type: "Процедура"
doc: "20-100-001-tr"
title_en: "Engine Identification"
title_ru: "Идентификация двигателя"
modified: "2013-12-04"
engines:
  - "41349633"
families:
  - "QSK19"
manuals:
  - "4021592"
figures: 6
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/20/20-100-001-tr.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/20-100-001-tr.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/20"
  - "перевод/машинный"
---

# Engine Identification
**Идентификация двигателя**

> [!abstract] Процедура · `20-100-001-tr`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021592 — QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual|4021592]]
> **Секции:** Section E - Engine Identification
> **Даты:** изменён 2013-12-04
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/20/20-100-001-tr.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/20-100-001-tr.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Интерфейсная коробка заказчика

Все двигатели морской конфигурации поставляются с клиентским интерфейсом. Эта коробка варьируется в зависимости от выбранной системы панели. Базовая панельная система включает в себя окно клиентского интерфейса с выключателем выключения двигателя и отдельным дисплеем панели машинного отделения. Система премиум-панели включает в себя блок клиентского интерфейса со встроенным DCU410 (дизельный блок управления) и выключателем выключения двигателя. Панельная система с утвержденным типом включает в себя блок клиентского интерфейса с DCU410 и блок удаленного ввода-вывода, встроенный в блок клиентского интерфейса, в дополнение к переключателю с выключателем выключения двигателя.

### Cummins® Номенклатура двигателей

Название модели предоставляет идентификационные данные для двигателя. См. иллюстрацию для идентификации имени модели.

Коды приложений:

** А =** Сельскохозяйственная отрасль

**С =**Строительство

**D =**Двигатель генератора

**F =** Огненный насос

**G =** Набор генераторов

**L =** Локомотив

*** Морской пехотинец

**P =** Электростанция

**R =**Rilcar

*** Тактическая военная служба.

![[17400001.png]]

### Заводская табличка двигателя

На табличке с данными двигателя указана конкретная информация о двигателе. Серийный номер двигателя (ESN) (1), список контрольных частей (CPL) (2), модель (3) и номинальные мощности и обороты (4) предоставляют информацию для заказа деталей и потребностей в обслуживании.

> [!note] Примечание
> Диаграмма двигателя ** не должна быть изменена, если она не одобрена Cummins Inc.

![[ew4plga.png]]

### Таблица данных топливного насоса

с форсункой электронного управления

Модульная общая железнодорожная система Cummins® (MCRS) расположена на стороне топливного насоса высокого давления. В табличке с данными содержится следующая информация:

1. Серийный номер
2. Код даты
3. Номер детали Cummins®.

![[05400300.png]]

с форсункой механического управления

Таблица данных топливного насоса старого стиля расположена на верхней части топливного насоса. Он предоставляет информацию для калибровки топливного насоса.

![[fp8plga.png]]

### Модуль управления двигателем Dataplate

с форсункой электронного управления

Внешний модуль управления двигателем (ECM) расположен на передней части ECM.

На табличке ECM содержится следующая информация:

- Номер детали ECM (P/N)
- Серийный номер ECM (S/N)
- Код данных ECM (D/C)
- Серийный номер двигателя (ESN)
- код ECM (определяет программное обеспечение в ECM);

![[19c01295.png]]

с форсункой механического управления

Внешний регистрационный знак ECM расположен поверх ЭКМ.

В табличке с данными содержится следующее:

- Номер детали ECM (P/N)
- Серийный номер ECM (S/N)
- Код даты производителя (D/C)
- Идентификатор поставщика (S/I)
- Рейтинг входного напряжения ECM (V/R).

Таблица справа содержит информацию о двигателе и калибровке. Это включает серийный номер двигателя (ESN), дату калибровки ECM (дата) и код калибровки ECM.

![[19400316.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> Customer Interface Box
>
> All Marine configuration engines are shipped with a Customer Interface Box. This box varies based on the chosen panel system. The Basic Panel System includes a Customer Interface Box with an Engine Shut-Down switch and a separate Engine Room Panel display. The Premium Panel System includes a Customer Interface Box with a built-in DCU410 (Diesel Control Unit) and Engine Shut-Down switch. The Type-Approved Panel System includes a Customer Interface Box with both a DCU410 and an Remote Input-Output unit built into the Customer Interface Box, in addition to an Engine Shut-Down switch.
>
> ### Cummins® Engine Nomenclature
>
> The model name provides identification data for the engine. See the illustration for model name identification.
>
> The application codes are:
>
> **A =** Agricultural
>
> **C =** Construction
>
> **D =** Generator Drive
>
> **F =** Fire Pump
>
> **G =** Generator Set
>
> **L =** Locomotive
>
> **M =** Marine
>
> **P =** Power Unit
>
> **R =** Railcar
>
> **T =** Tactical Military.
>
> ### Engine Dataplate
>
> The engine dataplate shows specific information about the engine. The engine serial number (ESN) (1), Control Parts List (CPL) (2), model (3), and horsepower and rpm ratings (4) provide information for ordering parts and service needs.
>
> **Note · Примечание**
> The engine dataplate **must not** be changed unless approved by Cummins Inc.
>
> ### Fuel Pump Dataplate
>
> with Electronically Actuated Injector
>
> The Cummins® Modular Common Rail System (MCRS) dataplate is located on the side of the high pressure fuel pump. The dataplate contains the following information:
>
> 1. Serial number
> 2. Date code
> 3. Cummins® part number.
>
> with Mechanically Actuated Injector
>
> The old style fuel pump dataplate is located on the top of the fuel pump. It provides information for fuel pump calibration.
>
> ### Engine Control Module Dataplate
>
> with Electronically Actuated Injector
>
> The external engine control module (ECM) dataplate is located on the front of the ECM.
>
> The following information is found on the ECM dataplate:
>
> - ECM part number (P/N)
> - ECM serial number (S/N)
> - ECM data code (D/C)
> - Engine Serial Number (ESN)
> - ECM code (identifies software in the ECM).
>
> with Mechanically Actuated Injector
>
> The external ECM dataplate is located on top of the ECM.
>
> The dataplate contains the following:
>
> - ECM part number (P/N)
> - ECM serial number (S/N)
> - Manufacturer date code (D/C)
> - Supplier identifier (S/I)
> - Input voltage rating of the ECM (V/R).
>
> The dataplate on the right contains engine and calibration information. This includes the engine serial number (ESN), ECM calibration date (Date), and ECM calibration code.
