---
aliases:
  - "Новые дочерние калибровки ЭБУ: карьерная техника Hitachi™"
type: "TSB"
doc: "tsb210093"
title_en: "New Child Engine Control Module (ECM) Calibration Codes: Hitachi™ Mining Equipment"
title_ru: "Новые дочерние калибровки ЭБУ: карьерная техника Hitachi™"
released: "2021-04-30"
modified: "2023-09-26"
group: "19 - Electronic Engine Controls"
engines:
  - "33224404"
  - "33239746"
  - "33239899"
  - "41340468"
families:
  - "K38/K50 · QSK38, QSK50"
  - "QSK50"
  - "QSK60 CM2150 MCRS"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2021/tsb210093.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb210093.pdf"
tags:
  - "документ/tsb"
  - "двигатель/K38/K50"
  - "двигатель/QSK50"
  - "двигатель/QSK60CM2150MCRS"
  - "год/2021"
  - "перевод/машинный"
  - "тема/electronic-engine-controls"
---

# New Child Engine Control Module (ECM) Calibration Codes: Hitachi™ Mining Equipment
**Новые дочерние калибровки ЭБУ: карьерная техника Hitachi™**

> [!abstract] TSB · `tsb210093`
> **Раздел Cummins:** 19 - Electronic Engine Controls
> **Двигатели:** [[33224404 — QSK50 CM2150 MCRS CPL 3391|33224404]], [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]], [[41340468 — QSK50 CM2150 MCRS CPL 3728|41340468]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK50, QSK60 CM2150 MCRS
> **Даты:** выпущен 2021-04-30 · изменён 2023-09-26
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2021/tsb210093.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb210093.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


## Новый модуль управления детским двигателем (ECM) - Калибровочные коды: Горнодобывающее оборудование HitachiTM

### Положение о гарантии

Сведения в этом документе не изменяют действующие гарантийные обязательства и практику ремонта и не дают оснований для работ по программам TRP или Campaign.

### Содержание

**Затронутая продукция**

Двигатели:

- QSK50 CM2150
- QSK50 CM850
- QSK60 CM2150
- QSK60 CM850

Производитель оригинального оборудования (OEM)

- HitachiTM

Применение

- Горнодобывающая промышленность

**Описание изменения**

- Выпущены новые коды специального модуля управления двигателем (ECM) HitachiTM.
- Правильный код ECM для детей устанавливается с помощью инструментария электронного обслуживания INSITETM в зависимости от: применение, рейтинг топлива, оптимизированный по топливной эффективности (FEO) калибровочный номер и спин-он масляные фильтры или использование элиминаторного масляного фильтра.

**Причина изменения**

- Родительские коды калибровки ECM для горнодобывающего оборудования были обновлены, чтобы технический специалист мог выбрать, работает ли двигатель с фильтрами для масла спин-он или элиминатора.
- Это изменение не совместимо с OEM-оборудованием Hitachi, поскольку оно не может считывать коды неисправностей от родительской ECM. В связи с этим были созданы специальные коды калибровки ECM для детей, чтобы транслировать коды ошибок от ребенка 1 ECM.

**Клиентская коммуникация**

Дистрибьюторы и дилеры Cummins® должны информировать клиентов, обслуживающих себя, о требовании иметь электронный сервис INSITETM с подпиской уровня Pro для установки калибровочных кодов на ECM CM850/2150.

**Указания по обслуживанию**

Инструкция QSK50:

Выберите соответствующие коды ECM для детей из таблиц 1 и 2 ниже в соответствии с существующим кодом ECM для родителей и типом фильтра для моторного масла.

| Таблица 1, QSK50 Вращение на фильтре моторного масла ECM Калибровочные коды |  |  |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|
|  | Коды калибровки FEO ECM | Коды калибровки Tier 2 ECM |  |  |  |  |  |  |  |  |  |
| Машинная модель HitachiTM | Модель двигателя | Настройка подачи топлива | Делай. | Код ECM родителей | Ребенок 1 ECM код | Ребенок 2 ECM | Настройка подачи топлива | Делай. | Код ECM родителей | Ребенок 1 ECM код | Ребенок 2 ECM |
| EH 3500 | QSK50 | FR6905 | 61204 | AQ60901 | AR60674 | AR60675 | FR6734 | 6976 | AQ60296 | AR60674 | AR60675 |
| EX2500/EX5500 | QSK50 | FR6856 | 61199 | AQ60934 | AR60674 | AR60675 | FR6795 | 6871 | AQ60289 | AR60674 | AR60675 |
| EX2600/5600-6 | QSK50 | FR6858 | 61190 | AQ60911 | AR60674 | AR60675 | FR6790 | 6866 | AQ60288 | AR60674 | AR60675 |
| EX2600/5600-6 T | QSK50 | FR6858 | 61191 | AQ60912 | AR60674 | AR60675 | FR6790 | 61094 | AQ60888 | AR60674 | AR60675 |

| Таблица 2, QSK50 Элиминатор фильтра ECM Калибровочные коды |  |  |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|
|  | Коды калибровки FEO ECM | Коды калибровки Tier 2 ECM |  |  |  |  |  |  |  |  |  |
| Машинная модель HitachiTM | Модель двигателя | Настройка подачи топлива | Делай. | Код ECM родителей | Ребенок 1 ECM код | Ребенок 2 ECM | Настройка подачи топлива | Делай. | Код ECM родителей | Ребенок 1 ECM код | Ребенок 2 ECM |
| EH 3500 | QSK50 | FR6905 | 61204 | AQ60901 | AR60676 | AR60677 | FR6734 | 6976 | AQ60296 | AR60676 | AR60677 |
| EX2500/EX5500 | QSK50 | FR6856 | 61199 | AQ60934 | AR60676 | AR60677 | FR6795 | 6871 | AQ60289 | AR60676 | AR60677 |
| EX2600/5600-6 | QSK50 | FR6858 | 61190 | AQ60911 | AR60676 | AR60677 | FR6790 | 6866 | AQ60288 | AR60676 | AR60677 |
| EX2600/5600-6 T | QSK50 | FR6858 | 61191 | AQ60912 | AR60676 | AR60677 | FR6790 | 61094 | AQ60888 | AR60676 | AR60677 |

Инструкция QSK60:

Выберите соответствующие коды ECM для детей из таблиц 3 и 4 ниже в соответствии с существующими родительскими калибровочными кодами ECM и типом фильтра для моторного масла.

| Таблица 3, QSK60 Спин на фильтре моторного масла ECM Калибровочные коды |  |  |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|
|  | Коды калибровки FEO ECM | Коды калибровки Tier 2 ECM |  |  |  |  |  |  |  |  |  |
| Машинная модель HitachiTM | Модель двигателя | Настройка подачи топлива | Делай. | Код ECM родителей | Ребенок 1 ECM код | Ребенок 2 ECM | Настройка подачи топлива | Делай. | Код ECM родителей | Ребенок 1 ECM код | Ребенок 2 ECM |
| EH4000 | QSK60 | FR6898 | 61215 | AQ60922 | AR60678 | AR60679 | FR6746 | 6975 | AQ60295 | AR60678 | AR60679 |
| EH5000 | QSK60 | FR6938 | ДО 61222 | AQ60929 | AR60680 | AR60681 | FR6773 | 6839 | AQ60238 | AR60680 | AR60681 |
| EH5000 | QSK60 | FR6938 | 61349 | AQ61003 | AR60680 | AR60681 | FR6773 | ДО 60198 | AQ60415 | AR60680 | AR60681 |
| EX3600/EX8000 | QSK60 | FR6896 | 6192 | AQ60913 | AR60678 | AR60679 | FR6796 | 6872 | AQ60303 | AR60678 | AR60679 |

| Таблица 4, QSK60 Элиминатор Фильтр ECM Калибровочные коды |  |  |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|
|  | Коды калибровки FEO ECM | Коды калибровки Tier 2 ECM |  |  |  |  |  |  |  |  |  |
| Машинная модель HitachiTM | Модель двигателя | Настройка подачи топлива | Делай. | Код ECM родителей | Ребенок 1 ECM код | Ребенок 2 ECM | Настройка подачи топлива | Делай. | Код ECM родителей | Ребенок 1 ECM код | Ребенок 2 ECM |
| EH4000 | QSK60 | FR6898 | 61215 | AQ60922 | AR60684 | AR60685 | FR6746 | 6975 | AQ60295 | AR60684 | AR60685 |
| EH5000 | QSK60 | FR6938 | ДО 61222 | AQ60929 | AR60682 | AR60683 | FR6773 | 6839 | AQ60238 | AR60682 | AR60683 |
| EH5000 | QSK60 | FR6938 | 61349 | AQ61003 | AR60682 | AR60683 | FR6773 | ДО 60198 | AQ60415 | AR60682 | AR60683 |
| EX3600/EX8000 | QSK60 | FR6896 | 6192 | AQ60913 | AR60684 | AR60685 | FR6796 | 6872 | AQ60303 | AR60684 | AR60685 |
| EX3600/EX8000 | QSK60 | FR6896 | ДО 61080 | AQ60947 | AR60684 | AR60685 |  |  |  |  |  |
| EX3600/EX8000 | QSK60 | FR6896 | ДО61164 | AQ60948 | AR60684 | AR60685 |  |  |  |  |  |

**Совместимость частей**

Коды калибровки ECM должны быть правильно подобраны для вашего двигателя и приложения. Если выбран неправильный код калибровки ECM, могут произойти выключения и выключения двигателя из-за неправильных порогов кода неисправности.

### История изменений документа


> [!quote]- Original (English) · английский оригинал
> ## New Child Engine Control Module (ECM) Calibration Codes: Hitachi™ Mining Equipment
>
> ### Warranty Statement
>
> The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.
>
> ### Contents
>
> **Product Affected**
>
> Engines:
>
> - QSK50 CM2150
> - QSK50 CM850
> - QSK60 CM2150
> - QSK60 CM850
>
> Original Equipment Manufacturer (OEM)
>
> - Hitachi™
>
> Application
>
> - Mining
>
> **Description of Change**
>
> - New Hitachi™ specific child engine control module (ECM) codes have been released.
> - The correct child ECM code is to be installed via INSITE™ electronic service tool depending on: application, fuel rating, fuel efficiency optimized (FEO) calibrations number and spin-on oil filters or eliminator oil filter utilization.
>
> **Reason for Change**
>
> - Parent ECM calibration codes for mining equipment have been updated to enable a technician to select if the engine is operating with spin-on or eliminator oil filters.
> - This change is **not** compatible with Hitachi™ OEM equipment as they are unable to read fault codes from the parent ECM. Because of this, customer specific child ECM calibration codes have been created to broadcast the fault codes from the child 1 ECM.
>
> **Customer Communication**
>
> Cummins® distribution and dealers are to inform self-servicing customers of requirement to have INSITE™ electronic service tool with a Pro level subscription to install calibration codes on CM850/2150 ECMs.
>
> **Service Instructions**
>
> QSK50 Instructions:
>
> Select the relevant child ECM codes from Table 1 and 2 below according to the existing parent ECM code and lubricating oil filter type.
>
> | Table 1, QSK50 Spin On Lubricating Oil Filter ECM Calibration Codes |  |  |  |  |  |  |  |  |  |  |  |
> |---|---|---|---|---|---|---|---|---|---|---|---|
> |  | FEO ECM Calibration Codes | Tier 2 ECM Calibration Codes |  |  |  |  |  |  |  |  |  |
> | Hitachi™ Machine Model | Engine Model | Fuel Rating | DO | Parent ECM Code | Child 1 ECM Code | Child 2 ECM Code | Fuel Rating | DO | Parent ECM Code | Child 1 ECM Code | Child 2 ECM Code |
> | EH 3500 | QSK50 | FR6905 | 61204 | AQ60901 | AR60674 | AR60675 | FR6734 | 6976 | AQ60296 | AR60674 | AR60675 |
> | EX2500/EX5500 | QSK50 | FR6856 | 61199 | AQ60934 | AR60674 | AR60675 | FR6795 | 6871 | AQ60289 | AR60674 | AR60675 |
> | EX2600/5600-6 | QSK50 | FR6858 | 61190 | AQ60911 | AR60674 | AR60675 | FR6790 | 6866 | AQ60288 | AR60674 | AR60675 |
> | EX2600/5600-6 T | QSK50 | FR6858 | 61191 | AQ60912 | AR60674 | AR60675 | FR6790 | 61094 | AQ60888 | AR60674 | AR60675 |
>
> | Table 2, QSK50 Eliminator Filter ECM Calibration Codes |  |  |  |  |  |  |  |  |  |  |  |
> |---|---|---|---|---|---|---|---|---|---|---|---|
> |  | FEO ECM Calibration Codes | Tier 2 ECM Calibration Codes |  |  |  |  |  |  |  |  |  |
> | Hitachi™ Machine Model | Engine Model | Fuel Rating | DO | Parent ECM Code | Child 1 ECM Code | Child 2 ECM Code | Fuel Rating | DO | Parent ECM Code | Child 1 ECM Code | Child 2 ECM Code |
> | EH 3500 | QSK50 | FR6905 | 61204 | AQ60901 | AR60676 | AR60677 | FR6734 | 6976 | AQ60296 | AR60676 | AR60677 |
> | EX2500/EX5500 | QSK50 | FR6856 | 61199 | AQ60934 | AR60676 | AR60677 | FR6795 | 6871 | AQ60289 | AR60676 | AR60677 |
> | EX2600/5600-6 | QSK50 | FR6858 | 61190 | AQ60911 | AR60676 | AR60677 | FR6790 | 6866 | AQ60288 | AR60676 | AR60677 |
> | EX2600/5600-6 T | QSK50 | FR6858 | 61191 | AQ60912 | AR60676 | AR60677 | FR6790 | 61094 | AQ60888 | AR60676 | AR60677 |
>
> QSK60 Instructions:
>
> Select the relevant child ECM codes from the Table 3 and 4 below according to the existing parent ECM calibration code and lubricating oil filter type.
>
> | Table 3, QSK60 Spin on Lubricating Oil Filter ECM Calibration Codes |  |  |  |  |  |  |  |  |  |  |  |
> |---|---|---|---|---|---|---|---|---|---|---|---|
> |  | FEO ECM Calibration Codes | Tier 2 ECM Calibration Codes |  |  |  |  |  |  |  |  |  |
> | Hitachi™ Machine Model | Engine Model | Fuel Rating | DO | Parent ECM Code | Child 1 ECM Code | Child 2 ECM Code | Fuel Rating | DO | Parent ECM Code | Child 1 ECM Code | Child 2 ECM Code |
> | EH4000 | QSK60 | FR6898 | DO61215 | AQ60922 | AR60678 | AR60679 | FR6746 | DO6975 | AQ60295 | AR60678 | AR60679 |
> | EH5000 | QSK60 | FR6938 | DO61222 | AQ60929 | AR60680 | AR60681 | FR6773 | DO6839 | AQ60238 | AR60680 | AR60681 |
> | EH5000 | QSK60 | FR6938 | DO61349 | AQ61003 | AR60680 | AR60681 | FR6773 | DO60198 | AQ60415 | AR60680 | AR60681 |
> | EX3600/EX8000 | QSK60 | FR6896 | DO61192 | AQ60913 | AR60678 | AR60679 | FR6796 | DO6872 | AQ60303 | AR60678 | AR60679 |
>
> | Table 4, QSK60 Eliminator Filter ECM Calibration Codes |  |  |  |  |  |  |  |  |  |  |  |
> |---|---|---|---|---|---|---|---|---|---|---|---|
> |  | FEO ECM Calibration Codes | Tier 2 ECM Calibration Codes |  |  |  |  |  |  |  |  |  |
> | Hitachi™ Machine Model | Engine Model | Fuel Rating | DO | Parent ECM Code | Child 1 ECM Code | Child 2 ECM Code | Fuel Rating | DO | Parent ECM Code | Child 1 ECM Code | Child 2 ECM Code |
> | EH4000 | QSK60 | FR6898 | DO61215 | AQ60922 | AR60684 | AR60685 | FR6746 | DO6975 | AQ60295 | AR60684 | AR60685 |
> | EH5000 | QSK60 | FR6938 | DO61222 | AQ60929 | AR60682 | AR60683 | FR6773 | DO6839 | AQ60238 | AR60682 | AR60683 |
> | EH5000 | QSK60 | FR6938 | DO61349 | AQ61003 | AR60682 | AR60683 | FR6773 | DO60198 | AQ60415 | AR60682 | AR60683 |
> | EX3600/EX8000 | QSK60 | FR6896 | DO61192 | AQ60913 | AR60684 | AR60685 | FR6796 | DO6872 | AQ60303 | AR60684 | AR60685 |
> | EX3600/EX8000 | QSK60 | FR6896 | DO61080 | AQ60947 | AR60684 | AR60685 |  |  |  |  |  |
> | EX3600/EX8000 | QSK60 | FR6896 | DO61164 | AQ60948 | AR60684 | AR60685 |  |  |  |  |  |
>
> **Part Compatibility**
>
> ECM calibration codes **must** be selected correctly for your engine and application. If the incorrect ECM calibration code is selected engine de-rates and shutdowns due to incorrect fault code thresholds can occur.
>
> ### Document History
