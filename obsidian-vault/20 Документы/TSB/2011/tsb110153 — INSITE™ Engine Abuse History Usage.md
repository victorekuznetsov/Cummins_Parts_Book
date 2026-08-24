---
aliases:
  - "Использование журнала нарушений эксплуатации в INSITE™"
type: "TSB"
doc: "tsb110153"
title_en: "INSITE™ Engine Abuse History Usage"
title_ru: "Использование журнала нарушений эксплуатации в INSITE™"
released: "2011-06-01"
modified: "2011-06-01"
group: "23 - Information Products"
engines:
  - "33239746"
  - "33239899"
  - "37292556"
  - "37295879"
  - "41349633"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
  - "QSK19"
  - "QST30"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2011/tsb110153.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/tsb/tsb110153.pdf"
tags:
  - "документ/tsb"
  - "двигатель/K38/K50"
  - "двигатель/QSK19"
  - "двигатель/QST30"
  - "год/2011"
  - "перевод/машинный"
  - "тема/information-products"
---

# INSITE™ Engine Abuse History Usage
**Использование журнала нарушений эксплуатации в INSITE™**

> [!abstract] TSB · `tsb110153`
> **Раздел Cummins:** 23 - Information Products
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]], [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]], [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60, QSK19, QST30
> **Даты:** выпущен 2011-06-01 · изменён 2011-06-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2011/tsb110153.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/tsb/tsb110153.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


## Использование журнала нарушений эксплуатации в INSITE™

### Суть проблемы

Параметр истории злоупотребления двигателем «Двигательное давление масла» должен ** не** использоваться в качестве основы для рассмотрения гарантийного требования.

Когда возникает претензия или проблема, связанная с использованием двигателя, ремонтом или гарантией; технические специалисты, оценивающие ситуацию, должны ** не ** рассматривать параметр «Давление масла в двигателе» в функции истории злоупотребления двигателем в электронном сервисе INSITETM в качестве основы для определения первопричины проблемы. Время в этих состояниях тяжести вводит в заблуждение и не представляет истинное состояние давления масла в двигателе, поскольку оно измеряется начиная с ключевого состояния ON. Это время будет накапливаться в категории «Суровня 3» с каждым включенным ключом и может привести техника к выводу, что двигатель провел слишком много времени в состоянии сильного давления масла в двигателе.

### Подтверждение

Не применяется

### Решение

Технические специалисты должны сначала определить, была ли проблема с давлением масла в двигателе, используя защиту двигателя. Эта функция записывает ошибки, которые вызывают ухудшение условий. Коды неисправностей, связанные с серьезной проблемой давления масла в двигателе, составляют 0415 и 0143. Техник может расширить эти неисправности и просмотреть количество раз, когда произошла неисправность, и сколько времени было потрачено в каждом случае.

### Положение о гарантии

Сведения в этом документе не изменяют действующие гарантийные обязательства и практику ремонта и не дают оснований для работ по программам TRP или Campaign.

### История изменений документа


> [!quote]- Original (English) · английский оригинал
> ## INSITE™ Engine Abuse History Usage
>
> ### Core Issue
>
> INSITE™ electronic service tool Engine Abuse History parameter “Engine Oil Pressure” should **not** be used as a basis for warranty claim consideration.
>
> When a claim or an issue comes in related to engine usage, repair, or warranty; technicians evaluating the situation should **not** consider the parameter “Engine Oil Pressure” in the Engine Abuse History feature in INSITE™ electronic service tool as a basis of determining the root cause of an issue. The time in these severity states is misleading and does **not** represent the true state of Engine Oil Pressure, since it measures starting from the key ON state. This time will accumulate in the Severity 3 category with every key ON and could lead a technician to conclude the engine spent what falsely appears to be an excessive amount of time in a severe Engine Oil Pressure state.
>
> ### Confirmation
>
> N/A
>
> ### Resolution
>
> Technicians should first determine if there was an Engine Oil Pressure issue using INSITE Engine Protection. This feature records the faults that cause derate conditions. The fault codes related to severe Engine Oil Pressure issue are 0415 and 0143. A technician can expand these faults and view the number of times the fault occurred and how much time was spent in each occurrence.
>
> ### Warranty Statement
>
> The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.
>
> ### Document History
