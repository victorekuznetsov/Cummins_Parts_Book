---
aliases:
  - "Ошибка соответствия калибровки"
type: "Процедура"
doc: "87-fc342"
title_en: "Calibration Match Error"
title_ru: "Ошибка соответствия калибровки"
modified: "2011-03-18"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666214"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc342.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-fc342.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
  - "перевод/машинный"
---

# Calibration Match Error
**Ошибка соответствия калибровки**

> [!abstract] Процедура · `87-fc342`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2011-03-18
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc342.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-fc342.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 342

### Ошибка соответствия калибровки

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 342 P(P): S253 SPN: 630 FMI: 13 ламп: Красная СТО: | Первичные и вторичные калибровки ECM не совпадают. | Двигатель не запускается. |

![[19900397.png]]

Электронный модуль управления (ECM)

### Описание цепи

Код 342 ошибки указывает, что калибровки в первичных и вторичных ЭКМ **не** одинаковы.

### Расположение компонента

На борту двигателя QST30 находятся два ECM, по одному с каждой стороны.

### Практические замечания

Этот код ошибки может произойти путем изменения или калибровки одного ECM. Калибровка одного модуля **не** поддерживается электронным сервисным оборудованием INSITETM для модулей CM552 на промышленных двигателях QST30. Оба модуля должны быть откалиброваны вместе.[[87-019-032 — ECM Calibration Code|См. процедуру 019-032 в разделе 19.]]

См. Код устранения неполадок t05-342.


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 342
>
> ### Calibration Match Error
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 342 PID(P): S253 SPN: 630 FMI: 13 Lamp: Red SRT: | The primary and secondary ECM calibrations do **not** match. | The engine will **not** start. |
>
> Electronic Control Module (ECM)
>
> ### Circuit Description
>
> Fault Code 342 indicates that the calibrations in the primary and secondary ECMs are **not** the same.
>
> ### Component Location
>
> Two ECMs are aboard the QST30 engine, one on each side.
>
> ### Shoptalk
>
> This fault code can occur by changing or calibrating a single ECM. Single module calibration is **not** supported by INSITE™ electronic service tool for CM552 modules on QST30 Industrial engines. Both modules **must** be calibrated together. [[87-019-032 — ECM Calibration Code|Refer to Procedure 019-032 in Section 19.]]
>
> Refer to Troubleshooting Fault Code t05-342.
