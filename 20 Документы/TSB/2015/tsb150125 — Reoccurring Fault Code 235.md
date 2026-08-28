---
aliases:
  - "Повторяющийся код неисправности 235"
type: "TSB"
doc: "tsb150125"
title_en: "Reoccurring Fault Code 235"
title_ru: "Повторяющийся код неисправности 235"
released: "2015-08-03"
modified: "2015-08-03"
group: "19 - Electronic Engine Controls"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2015/tsb150125.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb150125.pdf"
tags:
  - "документ/tsb"
  - "двигатель/QST30"
  - "год/2015"
  - "перевод/машинный"
  - "тема/electronic-engine-controls"
---

# Reoccurring Fault Code 235
**Повторяющийся код неисправности 235**

> [!abstract] TSB · `tsb150125`
> **Раздел Cummins:** 19 - Electronic Engine Controls
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Даты:** выпущен 2015-08-03 · изменён 2015-08-03
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2015/tsb150125.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb150125.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


## Повторяющийся код неисправности 235

### Положение о гарантии

Сведения в этом документе не изменяют действующие гарантийные обязательства и практику ремонта и не дают оснований для работ по программам TRP или Campaign.

### Содержание

**Проблема**

Повторяющийся код 235 неисправности на правом берегу модуля управления двигателем CM552 (ECM).

Код ошибки 235: Уровень ОЖ ниже нормы — наивысший уровень

**Затронутая продукция**

- QST30 CM552

**Проверка**

Код ошибки 235 на правом берегу виден только с помощью калибровочного программного обеспечения фазы 4. Используя инструмент для электронных услуг INSITETM под заголовком «Информация о калибровке», проверьте этап программного обеспечения для калибровки. Проверить код ошибки **только** видно на правом берегу ECM.

**Решение**

Если следующее будет подтверждено.

- Код ошибки 235 активен на правом берегу ECM.
- Двигатель имеет калибровочную программную фазу 4.

Изменение проводов может быть сделано, чтобы предотвратить повторный код неисправности. Выполните следующее на разъеме ремня электропроводки двигателя для правого берега ECM.

- Перейдите по ссылке 27, чтобы связаться с 10 (5 VDC).
- Перейдите по ссылке 37 на страницу 30 (земля).

Это создаст шортинг и отключит код неисправности на правом берегу.

Для инструкций по замене штифта используйте следующую процедуру в руководстве по устранению неполадок и ремонту промышленной электронной системы управления QST30, в бюллетене [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual\|3666214]].[[99-019-217 — Bosch™ ECM OEM Connector Series|См. процедуру 019-217 в разделе 19.]]

На фазу 5 калибровочного программного обеспечения **не** влияет повторяющийся код 235 ошибки правого берега.

### История изменений документа


> [!quote]- Original (English) · английский оригинал
> ## Reoccurring Fault Code 235
>
> ### Warranty Statement
>
> The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.
>
> ### Contents
>
> **Issue**
>
> Reoccurring fault code 235 on the right bank CM552 engine control module (ECM).
>
> Fault code 235: Coolant Level - Data Valid But Below Normal Operating Range - Most Severe Level
>
> **Product Affected**
>
> - QST30 CM552
>
> **Verification**
>
> Fault Code 235 on the right bank is **only** seen with calibration software phase 4. Using INSITE™ electronic service tool, under the Calibration Information heading, verify the calibration software phase. Verify the fault code is **only** seen on the right bank ECM.
>
> **Resolution**
>
> If the following are confirmed.
>
> - Fault code 235 active on the right bank ECM.
> - Engine has a calibration software phase 4.
>
> A wiring change can be made to prevent the reoccurring fault code. Perform the following on the engine harness connector for the right bank ECM.
>
> - Jump pin 27 to pin 10 (5 VDC).
> - Jump pin 37 to pin 30 (ground).
>
> This will create a shorting plug and disable the fault code on the right bank.
>
> For pin replacement instructions, use the following procedure in the QST30 Industrial Electronic Control System Troubleshooting and Repair Manual, Bulletin [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual\|3666214]]. [[99-019-217 — Bosch™ ECM OEM Connector Series|Refer to Procedure 019-217 in Section 19.]]
>
> Calibration software phase 5 is **not** affected by the reoccurring right bank fault code 235.
>
> ### Document History
