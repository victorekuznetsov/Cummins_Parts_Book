---
type: "TSB"
doc: "tsb190215"
title_en: "Proper Troubleshooting for Misfire Fault Codes"
modified: "2025-01-17"
engines:
  - "77804810"
families:
  - "15N"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2019/tsb190215.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb190215.pdf"
tags:
  - "документ/tsb"
  - "двигатель/15N"
  - "перевод/машинный"
---

# Proper Troubleshooting for Misfire Fault Codes

> [!abstract] TSB · `tsb190215`
> **Двигатели:** [[77804810 — 15N CM2380 M104B CPL 5977|77804810]]
> **Семейство:** 15N
> **Даты:** изменён 2025-01-17
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2019/tsb190215.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb190215.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


## Правильная устранение неполадок для кодов ошибок Misfire

### Положение о гарантии

Сведения в этом документе не изменяют действующие гарантийные обязательства и практику ремонта и не дают оснований для работ по программам TRP или Campaign.

### Содержание

**Затронутая продукция**

- 15N MM2380 M104B
- 15N MM2380 M105B
- 6.7N CM2380 D109B
- B6.7N CM2380 B150B
- B6.7N CM2380 B183B
- ISX12N CM2380 X120B
- L9N M2380 L124B
- L9N M2380 L130B
- X15N M2380 X150B

**Проблема**

Симптом:

- Коды ошибок: 5914, 5895, 5896, 5897, 5898, 5899, 5911, 6413, 6425, 6426, 6427, 6428, 6429, 6431.

Первопричина:

- Потенциальный неправильный диагноз при устранении неисправностей при использовании следующих кодов неисправностей, приводящих к замене неисправных компонентов или неправильному ремонту.

**Проверка**

- Проверьте наличие любого из следующих кодов неисправностей:

**Решение**

- Коды 5914 и 6413 являются общими кодами неисправностей, которые регистрируются даже при одноцилиндровом неисправном срабатывании. Если код 5914 или 6413 неисправности регистрируется в отсутствие каких-либо других кодов неисправности одного цилиндра, это указывает на то, что ни один цилиндр не достиг своего индивидуального порога неисправности, даже если все цилиндры могут быть неисправными.
- Если код 5914 или 6413 ошибки регистрируется только в случае отсутствия других кодов ошибок при одиночном осечке цилиндра:
- Если два или более одноцилиндровых кодов неисправности оседают:
- Если код 5914 или 6413 ошибки регистрируется вместе с кодом ошибки только один цилиндр:

**Публикации затронуты**

Пересмотрены коды ошибок 5914, 5895, 5896, 5897, 5898, 5899, 5911, 6413, 6425, 6426, 6427, 6428, 6429 и 6431. См. соответствующее Руководство по устранению неполадок кода ошибки. Справочный раздел TF.

### История изменений документа


> [!quote]- Original (English) · английский оригинал
> ## Proper Troubleshooting for Misfire Fault Codes
>
> ### Warranty Statement
>
> The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.
>
> ### Contents
>
> **Product Affected**
>
> - 15N CM2380 M104B
> - 15N CM2380 M105B
> - 6.7N CM2380 D109B
> - B6.7N CM2380 B150B
> - B6.7N CM2380 B183B
> - ISX12N CM2380 X120B
> - L9N CM2380 L124B
> - L9N CM2380 L130B
> - X15N CM2380 X150B
>
> **Issue**
>
> Symptom:
>
> - Fault codes: 5914, 5895, 5896, 5897, 5898, 5899, 5911, 6413, 6425, 6426, 6427, 6428, 6429, 6431.
>
> Root Cause:
>
> - Potential misdiagnosis during troubleshooting the following fault codes leading to replacement of non-malfunctioning components or incorrect repair.
>
> **Verification**
>
> - Verify any of the following fault codes are present:
>
> **Resolution**
>
> - Fault Codes 5914 and 6413 are generic fault codes that log even during single cylinder misfire. When either Fault Code 5914 or 6413 logs in the absence of any other single cylinder misfire fault codes this indicates that no one cylinder has reached its individual misfire threshold, even though all cylinders may be misfiring.
> - If **only** Fault Code 5914 or 6413 logs in the absence of any other single cylinder misfire fault codes:
> - If two or more single cylinder misfire fault codes log:
> - If Fault Code 5914 or 6413 logs along with **only** one cylinder misfire fault code:
>
> **Publications Affected**
>
> Fault Code 5914, 5895, 5896, 5897, 5898, 5899, 5911, 6413, 6425, 6426, 6427, 6428, 6429, and 6431 Troubleshooting Trees have been revised. See the corresponding Fault Code Troubleshooting Manual. Reference Section TF.
>
> ### Document History
