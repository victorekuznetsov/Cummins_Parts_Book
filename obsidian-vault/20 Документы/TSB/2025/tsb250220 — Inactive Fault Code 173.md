---
aliases:
  - "Неактивный код неисправности 173"
type: "TSB"
doc: "tsb250220"
title_en: "Inactive Fault Code 173"
title_ru: "Неактивный код неисправности 173"
released: "2025-12-01"
modified: "2025-12-01"
group: "19 - Electronic Engine Controls"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2025/tsb250220.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb250220.pdf"
tags:
  - "документ/tsb"
  - "двигатель/QST30"
  - "год/2025"
  - "перевод/машинный"
  - "тема/electronic-engine-controls"
---

# Inactive Fault Code 173
**Неактивный код неисправности 173**

> [!abstract] TSB · `tsb250220`
> **Раздел Cummins:** 19 - Electronic Engine Controls
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Даты:** выпущен 2025-12-01 · изменён 2025-12-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2025/tsb250220.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb250220.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


## Неактивный код неисправности 173

### Положение о гарантии

Сведения в этом документе не изменяют действующие гарантийные обязательства и практику ремонта и не дают оснований для работ по программам TRP или Campaign.

### Содержание

**Затронутая продукция**

- QST30 CM552

**Резюме проблемы**

Симптом:

- Несколько пунктов кода 173 неисправности будут отображаться как неактивные после попытки запуска двигателя.

Первопричина:

- Некоторые калибровки активируют и деактивируют этот код неисправности при попытке запуска двигателя.

**Проверка**

Данная проблема касается двигателей с модулем управления двигателем (ECM) Коды K50042.XX, K50204.XX или K50220.XX. Подключитесь к ECM с помощью рекомендованного инструментария или эквивалента электронного сервиса Cummins® и проверьте код ECM.

**Решение**

- Если код 173 ошибки постоянно появляется как неактивный, это код неисправности, который может быть проигнорирован. Если код 173 ошибки отображается как активный, выполните стандартные шаги по устранению неполадок.

### История изменений документа


> [!quote]- Original (English) · английский оригинал
> ## Inactive Fault Code 173
>
> ### Warranty Statement
>
> The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.
>
> ### Contents
>
> **Product Affected**
>
> - QST30 CM552
>
> **Issue Summary**
>
> Symptom:
>
> - Multiple counts of Fault Code 173 will show as inactive after attempting to start the engine.
>
> Root Cause:
>
> - Some calibrations will activate and deactivate this fault code while attempting to start the engine.
>
> **Verification**
>
> This issue applies to engines with engine control module (ECM) Codes K50042.XX, K50204.XX or K50220.XX. Connect to the ECM with recommended Cummins® Electronic Service Tool or equivalent and verify the ECM Code.
>
> **Resolution**
>
> - If Fault Code 173 continually reappears as inactive, this is a nuisance fault code and can be ignored. If Fault Code173 is showing as active, follow the standard troubleshooting steps.
>
> ### Document History
