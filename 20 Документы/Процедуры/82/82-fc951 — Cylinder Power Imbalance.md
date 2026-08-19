---
aliases:
  - "Разбаланс мощности по цилиндрам"
type: "Процедура"
doc: "82-fc951"
title_en: "Cylinder Power Imbalance"
title_ru: "Разбаланс мощности по цилиндрам"
modified: "2010-09-02"
engines:
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc951.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc951.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# Cylinder Power Imbalance
**Разбаланс мощности по цилиндрам**

> [!abstract] Процедура · `82-fc951`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc951.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc951.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 951

### Разбаланс мощности по цилиндрам

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 951 PID(P): P166 SPN: 166 ФМИ: 2/2 лампы: Нет, не srt: | Дисбаланс мощности цилиндров между цилиндрами. Дисбаланс мощности между цилиндрами был обнаружен электронным модулем управления (ECM). | Двигатель может иметь грубое холостое или неисправное огни. |

![[19202458.png]]

Разбаланс мощности по цилиндрам

### Описание цепи

ECM рассчитывает выходную мощность каждого цилиндра на холостых оборотах двигателя.

### Расположение компонента

ECM расположен на стороне топливной системы двигателя. Он крепится на головке цилиндра между цилиндрами 2 и 3.

### Практические замечания

На скоростях холостого хода двигателя ECM измеряет мгновенное ускорение каждого цилиндра при его запуске, чтобы определить мощность цилиндра. ECM регулирует подпитку отдельных цилиндров, если дисбаланс находится в заранее определенных пределах. Если дисбаланс превышает заранее определенные пределы, код 951 ошибки будет активен.

См. Код устранения неисправностей t05-951


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 951
>
> ### Cylinder Power Imbalance
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 951 PID(P): P166 SPN: 166 FMI: 2/2 Lamp: None SRT: | Cylinder Power Imbalance Between Cylinders. A power imbalance between cylinders was detected by the electronic control module (ECM). | Engine can have rough idle or misfire. |
>
> Cylinder Power Imbalance
>
> ### Circuit Description
>
> The ECM calculates the power output of each cylinder at engine idle speeds.
>
> ### Component Location
>
> The ECM is located on the fuel system side of the engine. It is attached at the cylinder head between cylinders 2 and 3.
>
> ### Shoptalk
>
> At engine idle speeds, the ECM measures the instantaneous acceleration of each cylinder as it fires, to determine the cylinder's power. The ECM adjusts fueling to individual cylinders if the imbalance is within pre-defined limits. If the imbalance is greater than the pre-defined limits, Fault Code 951 will be set active.
>
> Refer to Troubleshooting Fault Code t05-951
