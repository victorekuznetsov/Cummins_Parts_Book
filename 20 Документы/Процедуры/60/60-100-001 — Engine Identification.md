---
aliases:
  - "Идентификация двигателя"
type: "Процедура"
doc: "60-100-001"
title_en: "Engine Identification"
title_ru: "Идентификация двигателя"
modified: "2007-12-14"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021674"
figures: 4
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-100-001.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-100-001.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
  - "перевод/машинный"
---

# Engine Identification
**Идентификация двигателя**

> [!abstract] Процедура · `60-100-001`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section E — Engine and System Identification
> **Даты:** изменён 2007-12-14
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-100-001.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-100-001.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Cummins® Номенклатура двигателей

Название модели предоставляет идентификационные данные для двигателя. Смотрите иллюстрацию для идентификации имени модели.

Коды приложений:

A = Сельскохозяйственная

С = строительство

D = привод генератора

F = пожарный насос

G = набор генераторов

L = локомотив

M = морской

P = Силовая установка

R = Railcar

T = тактическая военная

![[00a00134.png]]

### Заводская табличка двигателя

Диаграмма двигателя ** не должна быть изменена, если она не одобрена Cummins Inc.

На табличке с данными двигателя показана конкретная информация о двигателе и представлена информация для заказа деталей и для потребностей в обслуживании.

1. Серийный номер двигателя (ESN)
2. Список контрольных частей (CPL)
3. Модель двигателя
4. Верхняя сила и рейтинг rpm.

[[60-100-002 — Engine Diagrams|См. процедуру 100-002 (Диаграммы двигателя) в разделе E для определения местоположения таблички.]]

![[ew6plga.png]]

### Таблица данных топливного насоса

Это иллюстрация таблички на насосе впрыска топлива Bosch®. Табличка данных установлена на боковой стороне корпуса насоса для впрыска.

1. Серийный номер насоса для инжекций
2. Bosch® часть номера
3. Идентификационный код насоса Bosch®
4. Номер детали Cummins® (первые семь цифр на этой строке).

![[05a00094.png]]

### ECM Dataplate

Электронный модуль управления (ECM) показывает информацию о ECM и о том, как он был запрограммирован. Эта табличка расположена на передней части ECM.

На табличках данных ECM (CM552) (1) и ECM (CM850) (2) имеется следующая информация:

- Номер детали ECM (PN)
- Серийный номер ECM (SN)
- Код даты ECM (DC)
- Серийный номер двигателя (ESN)
- код ECM (определяет программное обеспечение в ECM);

Иметь код ECM от двигателя, доступный при общении с авторизованным местом ремонта Cummins®.

![[00a00135.png]]


> [!quote]- Original (English) · английский оригинал
> ### Cummins® Engine Nomenclature
>
> The model name provides identification data for the engine. See the illustration for the model name identification.
>
> The application codes are:
>
> A = Agricultural
>
> C = Construction
>
> D = Generator Drive
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
> T = Tactical Military
>
> ### Engine Dataplate
>
> The engine dataplate **must not** be changed unless approved by Cummins Inc.
>
> The engine dataplate shows specific information about the engine and provides information for ordering parts and for service needs.
>
> 1. Engine serial number (ESN)
> 2. Control Parts List (CPL)
> 3. Engine model
> 4. Horsepower and rpm rating.
>
> [[60-100-002 — Engine Diagrams|Refer to Procedure 100-002 (Engine Diagrams) in Section E for dataplate location.]]
>
> ### Fuel Pump Dataplate
>
> This is an illustration of the dataplate on the Bosch® fuel injection pump. The dataplate is mounted on the outboard side of the injection pump housing.
>
> 1. Injection pump serial number
> 2. Bosch® part number
> 3. Bosch® pump identification code
> 4. Cummins® part number (first seven digits on this line).
>
> ### ECM Dataplate
>
> The electronic control module (ECM) dataplate shows information about the ECM and how the ECM was programmed. This dataplate is located on the front of the ECM.
>
> The following information is available on the ECM (CM552) dataplate (1) and ECM (CM850) (2) dataplate:
>
> - ECM part number (PN)
> - ECM serial number (SN)
> - ECM date code (DC)
> - Engine serial number (ESN)
> - ECM code (identifies the software in the ECM).
>
> Have the ECM code from the engine available when communicating with a Cummins® Authorized Repair Location.
