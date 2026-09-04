---
aliases:
  - "Идентификация двигателя"
type: "Процедура"
doc: "28-100-001-om"
title_en: "Engine Identification"
title_ru: "Идентификация двигателя"
modified: "2010-05-26"
engines:
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50"
manuals:
  - "3667180"
  - "3810497"
figures: 6
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/28/28-100-001-om.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/28-100-001-om.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/28"
  - "перевод/машинный"
---

# Engine Identification
**Идентификация двигателя**

> [!abstract] Процедура · `28-100-001-om`
> **Двигатели:** [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50
> **Входит в руководства:** [[3667180 — K38, K50, QSK38 and QSK50 Owners Manual|3667180]], [[3810497 — K38, K50, QSK38 and QSK50 Operation and Maintenance Manual|3810497]]
> **Секции:** Section E - Engine Identification · Section E - Engine and System Identification
> **Даты:** изменён 2010-05-26
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/28/28-100-001-om.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/28-100-001-om.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Заводская табличка двигателя

На табличке с данными двигателя указана конкретная информация о двигателе. Серийный номер двигателя (ESN) (1), список элементов управления (CPL) (2), модель (3) и номинальные значения мощности и оборотов в минуту (4) предоставляют информацию для заказа деталей и потребностей в обслуживании.

> [!note] Примечание
> Диаграмма двигателя не должна быть изменена, если она не одобрена Cummins Inc.

Диапазон данных двигателя для более старых двигателей K38 и K50 расположен сзади правой боковой стороны двигателя. Диаграмма на современных двигателях К38 и К50 расположена на левобережной стороне передней крышки передней передачи.[[28-100-002-om — Engine Diagrams|См. процедуру 100-002 (Диаграммы двигателя) в разделе Е.]]

![[ew6plga.png]]

### Cummins® Номенклатура двигателей

Название модели предоставляет идентификационные данные для двигателя. Смотрите иллюстрацию для идентификации имени модели.

Коды приложений:

С = строительство

D = привод генератора

F = пожарный насос

G = набор генераторов

L = локомотив

M = морской

P = Силовая установка

R = Railcar

![[00600233.png]]

### Таблица данных топливного насоса

с форсункой механического управления

> [!note] Примечание
> Калибровка топливного насоса требует специального оборудования и должна быть выполнена в авторизованном месте ремонта Cummins®.

Таблица данных топливного насоса расположена на верхней части топливного насоса.

Таблица данных топливного насоса содержит информацию для калибровки топливного насоса.

![[fp8plga.png]]

с форсункой электронного управления

Модульная общая железнодорожная система Cummins® расположена на стороне топливного насоса высокого давления. Таблица содержит следующую информацию.

1. Серийный номер
2. Код даты
3. Cummins® Part Number.

![[05600196.png]]

### ECM Dataplate

с форсункой механического управления

Внешний блок данных расположен в верхней части электронного модуля управления (ECM).

В табличке с данными содержится следующее:

- Номер детали
- Серийный номер
- Код даты производителя
- Идентификатор поставщика
- Рейтинг входного напряжения электронного модуля управления (ECM).

![[19400316.png]]

с форсункой электронного управления

Электронный модуль управления (ECM) показывает информацию о ECM и о том, как он был запрограммирован. Таблица данных расположена на передней части ECM.

На табличке ECM содержится следующая информация:

1. Номер детали ECM (PN)
2. Серийный номер ECM (SN)
3. Код данных ECM (DC)
4. Серийный номер двигателя (ESN)
5. код ECM (определяет программное обеспечение в ECM);

> [!note] Примечание
> Иметь код ECM от двигателя, доступный при общении с авторизованным местом ремонта CumminsTM.

![[00d00074.png]]


> [!quote]- Original (English) · английский оригинал
> ### Engine Dataplate
>
> The engine dataplate shows specific information about the engine. The engine serial number (ESN) (1), controls parts list (CPL) (2), model (3), and horsepower and rpm ratings (4) provide information for ordering parts and service needs.
>
> **Note · Примечание**
> The engine dataplate **must not** be changed unless approved by Cummins Inc.
>
> The engine dataplate for the older K38 and K50 engines is located on the rear of the right bank side of the engine. The dataplate on the present K38 and K50 engines is located on the left bank side of the front gear cover. [[28-100-002-om — Engine Diagrams|Refer to Procedure 100-002 (Engine Diagrams) in Section E.]]
>
> ### Cummins® Engine Nomenclature
>
> The model name provides identification data for the engine. See the illustration for the model name identification.
>
> The application codes are:
>
> C = Construction
>
> D = Generator-Drive
>
> F = Fire Pump
>
> G = Generator Set
>
> L = Locomotive
>
> M = Marine
>
> P = Power Unit
>
> R = Railcar
>
> ### Fuel Pump Dataplate
>
> with Mechanically Actuated Injector
>
> **Note · Примечание**
> Calibration of the fuel pump requires special equipment and **must** be performed at a Cummins® Authorized Repair Location.
>
> The fuel pump dataplate is located on the top of the fuel pump.
>
> The fuel pump dataplate provides information for fuel pump calibration.
>
> with Electronically Actuated Injector
>
> The Cummins® Modular Common Rail System dataplate is located on the side of the high pressure fuel pump. The dataplate contains the following information.
>
> 1. Serial Number
> 2. Date Code
> 3. Cummins® Part Number.
>
> ### ECM Dataplate
>
> with Mechanically Actuated Injector
>
> The external dataplate is located on the top of the electronic control module (ECM).
>
> The dataplate contains the following:
>
> - Part number
> - Serial number
> - Manufacturer date code
> - Supplier identifier
> - Input voltage rating of the electronic control module (ECM).
>
> with Electronically Actuated Injector
>
> The electronic control module (ECM) dataplate shows information about the ECM and how the ECM was programmed. The dataplate is located on the front of the ECM.
>
> The following information is found on the ECM dataplate:
>
> 1. ECM part number (PN)
> 2. ECM serial number (SN)
> 3. ECM data code (DC)
> 4. Engine serial number (ESN)
> 5. ECM code (identifies software in the ECM).
>
> **Note · Примечание**
> Have the ECM code from the engine available when communicating with a Cummins™ Authorized Repair Location.
