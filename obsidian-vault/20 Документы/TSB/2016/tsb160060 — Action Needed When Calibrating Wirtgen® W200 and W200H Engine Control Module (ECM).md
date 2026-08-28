---
type: "TSB"
doc: "tsb160060"
title_en: "Action Needed When Calibrating Wirtgen® W200 and W200H Engine Control Module (ECM) to Retain Low Idle Speed and Grid Heater Parameter Settings"
modified: "2016-07-06"
engines:
  - "80141463"
  - "80248213"
families:
  - "QSX15"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2016/tsb160060.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb160060.pdf"
tags:
  - "документ/tsb"
  - "двигатель/QSX15"
  - "перевод/машинный"
---

# Action Needed When Calibrating Wirtgen® W200 and W200H Engine Control Module (ECM) to Retain Low Idle Speed and Grid Heater Parameter Settings

> [!abstract] TSB · `tsb160060`
> **Двигатели:** [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSX15
> **Даты:** изменён 2016-07-06
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2016/tsb160060.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb160060.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


## При калибровке модуля управления двигателем Wirtgen® W200 и W200H (ECM) необходимо соблюдать низкие параметры скорости холостого хода и параметров нагревателя сетки

### Положение о гарантии

Сведения в этом документе не изменяют действующие гарантийные обязательства и практику ремонта и не дают оснований для работ по программам TRP или Campaign.

### Содержание

**Затронутая продукция**

Двигатель:

- QSX15 CM570

Производитель оригинального оборудования (OEM):

- Вирген®

Модели:

- W200
- W200H

**Проблема**

- Выберите модуль управления двигателем (ECM) калибровочные коды имеют различные значения по умолчанию для параметров низкой скорости холостого хода и нагревателя сетки, чем те, которые требуются оригинальным производителем оборудования OEM.
- Если функция сохранения и восстановления ECM заменена или функция сохранения и восстановления ECM не используется или прерывается во время загрузки калибровки ECM, параметры ECM будут восстановлены до правильных значений. Это может привести к неправильной скорости холостого хода и ухудшить функцию нагревателя сетки.

**Проверка**

Для затронутых кодов калибровки ECM см. Таблицу 1.

| Таблица 1 Поврежденные коды калибровки ECM |  |  |  |  |  |
|---|---|---|---|---|---|
| Калибровочный код ЭБУ | Общий/таможенный | Делай выбор | SC Option | FR Вариант | наличие |
| N12028 | дженерики | 1684 | SC11374 | FR10577 | Только сервис |
| N 11835 | дженерики | 1412 | SC11374 | FR10577 | Только сервис |

**Решение**

- Если функция сохранения и восстановления ECM заменена или функция сохранения и восстановления ECM не используется или прерывается во время загрузки кода калибровки ECM, технические специалисты должны проверить, что параметры верны. Для настроек параметров Wirtgen по умолчанию см. таблицу 2 ниже.
- Если требуется обновление кода калибровки ECM, то коды калибровки ECM должны обновляться на аналогичной основе без изменения базового калибровочного кода ECM.

| Таблица 2, Параметры ECM по умолчанию Wirtgen® |  |
|---|---|
| Параметр | Номинальный Wirtgen® Setting |
| Низкая скорость холостого хода | 950 об/мин |
| Сетчатый нагреватель | Над |

**Статус в производстве**

Все двигатели, построенные после 7 марта 2016 года, будут загружены с помощью калибровочного кода ECM N12213.

### История изменений документа


> [!quote]- Original (English) · английский оригинал
> ## Action Needed When Calibrating Wirtgen® W200 and W200H Engine Control Module (ECM) to Retain Low Idle Speed and Grid Heater Parameter Settings
>
> ### Warranty Statement
>
> The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.
>
> ### Contents
>
> **Product Affected**
>
> Engine:
>
> - QSX15 CM570
>
> Original Equipment Manufacturer (OEM):
>
> - Wirtgen®
>
> Models:
>
> - W200
> - W200H
>
> **Issue**
>
> - Select engine control module (ECM) calibration codes have different default values for the Low Idle Speed and Grid Heater parameters than those required by the original equipment manufacturer OEM.
> - If the ECM is replaced or ECM save and restore function is not used or is interrupted during ECM calibration download, ECM parameter settings will **not** be restored to the correct values. This can result in incorrect idle speed and impair grid heater function.
>
> **Verification**
>
> For affected ECM calibration codes, see Table 1.
>
> | Table 1, ECM Calibration Codes Affected |  |  |  |  |  |
> |---|---|---|---|---|---|
> | ECM Calibration Code | Generic/Custom | DO Option | SC Option | FR Option | Availability |
> | N12028 | Generic | DO1684 | SC11374 | FR10577 | Service Only |
> | N11835 | Generic | DO1412 | SC11374 | FR10577 | Service Only |
>
> **Resolution**
>
> - If the ECM is replaced or ECM save and restore function is **not** used or is interrupted during ECM calibration code download, technicians **must** verify that the parameters are correct. For default Wirtgen® parameters settings, See Table 2 below.
> - If an ECM calibration code update is required, ECM calibration codes **must** be updated on a like-for-like basis, with no change in the ECM base calibration code.
>
> | Table 2, Default Wirtgen® ECM Parameters |  |
> |---|---|
> | Parameter | Nominal Wirtgen® Setting |
> | Low Idle Speed | 950 rpm |
> | Grid Heater | On |
>
> **Production Status**
>
> All engines built after 7 March 2016 will be loaded with ECM calibration code N12213.
>
> ### Document History
