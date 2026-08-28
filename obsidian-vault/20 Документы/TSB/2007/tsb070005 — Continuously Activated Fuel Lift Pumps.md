---
aliases:
  - "Постоянно работающие топливоподкачивающие насосы"
type: "TSB"
doc: "tsb070005"
title_en: "Continuously Activated Fuel Lift Pumps"
title_ru: "Постоянно работающие топливоподкачивающие насосы"
released: "2007-02-05"
modified: "2007-02-05"
group: "19 - Electronic Engine Controls"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2007/tsb070005.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb070005.pdf"
tags:
  - "документ/tsb"
  - "двигатель/QST30"
  - "год/2007"
  - "перевод/машинный"
  - "тема/electronic-engine-controls"
---

# Continuously Activated Fuel Lift Pumps
**Постоянно работающие топливоподкачивающие насосы**

> [!abstract] TSB · `tsb070005`
> **Раздел Cummins:** 19 - Electronic Engine Controls
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Даты:** выпущен 2007-02-05 · изменён 2007-02-05
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2007/tsb070005.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb070005.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


## Постоянно работающие топливоподкачивающие насосы

### Суть проблемы

Электронные насосы для подъёма топлива на двигателях QST30 работают в положении KEY ON без работы двигателя. Продленные периоды в этом состоянии могут привести к повреждению и возможному выходу из строя насоса топливного подъемника.

### Подтверждение

Все двигатели QST30 оснащены электронными насосами для подъема топлива в промышленных целях.

Двигатель **не** запускается или регистрирует низкую мощность, как только насос подъемного устройства выходит из строя.

Ссылка на дерево симптомов «Нет старта».

Если подъемный насос работает без охлаждения потока топлива в течение более 30 секунд, щетка и коммутатор внутри насоса будут поддерживать повреждение и в конечном итоге потерпят неудачу.

Если топливный насос не работает, его необходимо заменить.

### Решение

Не ставьте двигатель в положение KEY ON более 30 секунд без работы двигателя. Если двигатель необходимо оставить в положении KEY ON для устранения неполадок, отсоедините насос топливного подъемника. Подключите насос для подъёма топлива, когда двигатель готов к нормальной работе.

### Положение о гарантии

Сведения в этом документе не изменяют действующие гарантийные обязательства и практику ремонта и не дают оснований для работ по программам TRP или Campaign.


> [!quote]- Original (English) · английский оригинал
> ## Continuously Activated Fuel Lift Pumps
>
> ### Core Issue
>
> Electronic fuel lift pumps on QST30 engines operate in the KEY ON position without the engine operating. Extended periods in this state can cause damage to and eventual failure of the fuel lift pump.
>
> ### Confirmation
>
> All QST30 engines equipped with electronic fuel lift pumps in industrial applications.
>
> Engine will **not** start or registers low power, once the fuel lift pump fails.
>
> Reference the No Start symptom tree.
>
> If the lift pump is operating without a cooling fuel flow for more than 30 seconds, the brush and commutator within the pump will sustain damage and eventually fail.
>
> If the fuel pump fails, it **must** be replaced.
>
> ### Resolution
>
> Do not have the engine in KEY ON position for more than 30 seconds without operating the engine. If the engine needs to be left in the KEY ON position for troubleshooting purposes, disconnect the fuel lift pump. Connect the fuel lift pump when the engine is ready for normal operation.
>
> ### Warranty Statement
>
> The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.
