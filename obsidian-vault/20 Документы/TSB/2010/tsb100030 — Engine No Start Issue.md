---
aliases:
  - "Двигатель не запускается"
type: "TSB"
doc: "tsb100030"
title_en: "Engine No Start Issue"
title_ru: "Двигатель не запускается"
released: "2010-04-06"
modified: "2010-04-06"
group: "19 - Electronic Engine Controls"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
parts:
  - "3658780"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2010/tsb100030.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/tsb/tsb100030.pdf"
tags:
  - "документ/tsb"
  - "двигатель/QST30"
  - "год/2010"
  - "перевод/машинный"
  - "тема/electronic-engine-controls"
---

# Engine No Start Issue
**Двигатель не запускается**

> [!abstract] TSB · `tsb100030`
> **Раздел Cummins:** 19 - Electronic Engine Controls
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Даты:** выпущен 2010-04-06 · изменён 2010-04-06
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2010/tsb100030.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/tsb/tsb100030.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


## Двигатель не запускается

### Суть проблемы

Этот бюллетень технической службы предупреждает поле о проблеме с двигателями QST30, построенными с неправильным реле в электропроводке насоса подъемника двигателя. Двигатели были построены с 12-вольтным реле, номером части 3658948, а не с указанным 24-вольтным реле, номером части.[[3658780]]. Это приводит к тому, что реле 12 вольт перегружается и выходит из строя. Это предотвращает подачу энергии на насосы подъемника двигателя и вызывает нежелательное состояние при следующей попытке запуска двигателя.

### Подтверждение

Это касается всех двигателей QST30. Подозреваемый диапазон строительства оценивается в октябре 2009 года по март 2010 года.

Этот вопрос рассматривается как условие отсутствия начала. 12-вольтовое реле перегружается и обычно выходит из строя в течение первых нескольких часов работы нового двигателя. В зависимости от установки топливного бака двигатель может продолжать работать после того, как реле неисправно. Однако при следующей попытке запуска двигателя появится условие «нет старта».

Реле 12 вольт, установленное на двигателе, будет иметь более низкое сопротивление, чем реле 24 вольт на контактах 85 и 86 на разъёме ремня подъемного насоса. Сопротивление между контактами 85 и 86 с установленным реле 24 вольт будет находиться в диапазоне 360-380 Ом. Сопротивление с установленным реле 12 вольт будет составлять примерно 75 Ом.

Поставщик подъемного насоса электропроводки жгута установил неправильную реле в электропроводке жгута.

Перегретая эстафета. Прогрессивного ущерба не ожидается.

### Решение

Если реле 12 вольт повреждено или низкое сопротивление обнаружено на контактах 85 и 86 реле подъемного насоса, замените реле реле 24 вольт, номер детали[[3658780]].

### Положение о гарантии

Сведения в этом документе не изменяют действующие гарантийные обязательства и практику ремонта и не дают оснований для работ по программам TRP или Campaign.

## Детали, упомянутые в документе

| Артикул | Наименование | Русское название |
|---|---|---|
| [[3658780]] | RELAY | Реле |

> [!quote]- Original (English) · английский оригинал
> ## Engine No Start Issue
>
> ### Core Issue
>
> This Technical Service Bulletin alerts the field to an issue with QST30 engines being built with the wrong relay in the engine lift pump harness. Engines were built with a 12 volt relay, Part Number 3658948, rather than the specified 24 volt relay, Part Number [[3658780]]. This causes the 12 volt relay to become overloaded and fail. This prevents power from being supplied to the engine lift pumps and causes a no start condition at the next attempt to start the engine.
>
> ### Confirmation
>
> This issue affects all QST30 engines. The suspected build range is estimated to be October 2009 to March 2010.
>
> This issue is observed as a no start condition. The 12 volt relay becomes overloaded and typically fails within the first few running hours of a new engine. Depending on the fuel tank set up, the engine can remain running after the relay has malfunctioned. However, at the next attempt to start the engine, the no start condition will appear.
>
> A 12 volt relay installed on the engine will show a lower resistance than the 24 volt relay across pins 85 and 86 on the lift pump harness connector. The resistance across pins 85 and 86 with the proper 24 volt relay installed will be in the range of 360-380 ohms. The resistance with the 12 volt relay installed will be approximately 75 ohms.
>
> The supplier of the lift pump wiring harness installed the incorrect relay in the harness.
>
> Overheated relay. No progressive damage is expected.
>
> ### Resolution
>
> If a 12 volt relay is found damaged, or a low resistance is found across pins 85 and 86 of the lift pump harness, replace the relay with the 24 volt relay, Part Number [[3658780]].
>
> ### Warranty Statement
>
> The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.
