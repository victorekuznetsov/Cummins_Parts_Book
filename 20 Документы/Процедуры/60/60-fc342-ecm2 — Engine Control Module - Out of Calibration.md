---
aliases:
  - "Электронный блок управления — вне калибровки"
type: "Процедура"
doc: "60-fc342-ecm2"
title_en: "Engine Control Module - Out of Calibration"
title_ru: "Электронный блок управления — вне калибровки"
modified: "2012-12-20"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021674"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc342-ecm2.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-fc342-ecm2.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
  - "перевод/машинный"
---

# Engine Control Module - Out of Calibration
**Электронный блок управления — вне калибровки**

> [!abstract] Процедура · `60-fc342-ecm2`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section TF — Troubleshooting Fault Codes
> **Даты:** изменён 2012-12-20
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc342-ecm2.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-fc342-ecm2.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 342-ECM2

### Электронный блок управления — вне калибровки

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 342 P(P): Нет SPN: ФМИ: 13 ламп: Красная СТО: | Электронный блок управления — вне калибровки. Калибровка ECM ** не совпадает. | Двигатель не запускается **. |

![[19a00867.png]]

Электронный модуль управления (ECM2)

### Описание цепи

Код 342 ошибки указывает, что калибровки в ECM ** не** одинаковы.

### Расположение компонента

ECM1, ECM2 и ECM3 установлены над корпусом маховика на задней части двигателя. ECM1 расположен (слева направо) на левом берегу, затем ECM2 в середине и ECM3 на правом берегу.[[60-100-002 — Engine Diagrams|См. процедуру 100-002 в разделе F.]]

### Практические замечания

Эта проблема может возникнуть при изменении одного ECM.

См. Код устранения неполадок t05-342


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 342-ECM2
>
> ### Engine Control Module - Out of Calibration
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 342 PID(P): None SPN: FMI: 13 Lamp: Red SRT: | Engine Control Module - Out of Calibration. ECM calibrations do **not** match. | Engine will **not** start. |
>
> Electronic Control Module (ECM2)
>
> ### Circuit Description
>
> Fault Code 342 indicates the calibrations in the ECMs are **not** the same.
>
> ### Component Location
>
> ECM1, ECM2, and ECM3 are mounted above the flywheel housing on the rear of the engine. ECM1 is located (from left to right) on the left bank, followed by ECM2 in the middle, and ECM3 on the right bank. [[60-100-002 — Engine Diagrams|Refer to Procedure 100-002 in Section F.]]
>
> ### Shoptalk
>
> This problem can occur by changing a single ECM.
>
> Refer to Troubleshooting Fault Code t05-342
