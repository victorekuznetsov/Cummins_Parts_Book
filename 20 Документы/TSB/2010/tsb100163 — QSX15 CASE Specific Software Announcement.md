---
type: "TSB"
doc: "tsb100163"
title_en: "QSX15 CASE Specific Software Announcement"
modified: "2002-05-31"
engines:
  - "80141463"
  - "80248213"
families:
  - "QSX15"
figures: 2
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2010/tsb100163.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb100163.pdf"
tags:
  - "документ/tsb"
  - "двигатель/QSX15"
  - "перевод/машинный"
---

# QSX15 CASE Specific Software Announcement

> [!abstract] TSB · `tsb100163`
> **Двигатели:** [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSX15
> **Даты:** изменён 2002-05-31
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2010/tsb100163.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb100163.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


## QSX15 CASE - Специальное программное обеспечение

### Положение о гарантии

Сведения в этом документе не изменяют действующие гарантийные обязательства и практику ремонта и не дают оснований для работ по программам TRP или Campaign.

### Содержание

В этом бюллетене технической службы анонсирована модификация трактора Case STX 450 и трактора New Holland TJ 450, что требует изменения калибровки электронного модуля управления (ECM).

Информация, содержащаяся в этом бюллетене технической службы, затрагивает только тракторы STX 450 лошадиных сил и TJ 450 лошадиных сил. Это не влияет на CNH 375 или 425 лошадиных сил трактора.

Начиная с Tier II 425 и 450 HP, CNH использует гидравлический вентилятор охлаждения. Скорость, с которой работает вентилятор, определяется следующими тремя температурами:

1. температура охлаждающей жидкости
2. температура коллектора
3. Температура гидравлического масла.

В начале февраля 2002 года CNH представила новый воздушный охладитель с улучшенной эффективностью на тракторах STX 450 и TJ 450. Улучшенная эффективность CAC позволяет вентилятору двигателя работать реже и / или на более медленной скорости, что, в свою очередь, позволяет получить больше доступной мощности и лучшую экономию топлива. Для реализации этого преимущества калибровка ECM была модифицирована для снижения спроса на охлаждение вентилятора, при этом контролируя максимальную температуру впускного коллектора до желаемого уровня.

> [!note] Примечание
> Новый CAC и новая калибровка не применяются к тракторам STX 425 и TJ 425.

В оригинальном Tier II QSX15 450 HP для CNH использовалась опция Customer Interface Software DO 1165. Новый вариант DO для использования с улучшенным CAC — DO 1259. При выборе калибровки для трактора STX 450 или TJ 450 поле DO-комментариев будет направлять пользователя к правильной калибровке. В частности, на диске ESDN INCAL за апрель 2002 года будет представлена следующая записка в поле комментариев DO 1259: Комментарий: ТРАКТОРЫ С УСЛУГИРОВАННОЙ СИСТЕМОЙ ОХЛАДКИ (см. Рисунок 1).

![[19c01391.png]]

Рисунок 1

Для CD-ROM ESDN INCAL в мае 2002 года стал известен серийный номер двигателя (ESNF) для нового CAC, поэтому поля комментариев будут читаться следующим образом: До ESN 14027676 или после ESN 14027676 (см. Рисунок 2).

![[19c01392.png]]

Рисунок 2

> [!note] Примечание
> Если DO 1165 будет установлен в двигателях, построенных после 14027676, преимущество улучшенного CAC будет потеряно, но температура впускного коллектора будет поддерживаться на приемлемом уровне для поддержания стандартов выбросов Tier II.

> [!note] Примечание
> Если DO 1269 установлен в двигателях, построенных до 14027676, температура впускного коллектора может превышать максимально допустимую температуру и, возможно, поставить под угрозу соблюдение норм выбросов Tier II. Не используйте DO 1269 в двигателях, построенных до ESN 14027676.


> [!quote]- Original (English) · английский оригинал
> ## QSX15 CASE Specific Software Announcement
>
> ### Warranty Statement
>
> The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.
>
> ### Contents
>
> This Technical Service Bulletin announces a modification to the Case STX 450 tractor and the New Holland TJ 450 tractor that necessitates a change in the electronic control module (ECM) calibration.
>
> The information in This Technical Service Bulletin affects **only** the STX 450 horsepower, and TJ 450 horsepower tractors. It does **not** affect the CNH 375 or 425 horsepower tractor.
>
> Beginning with the Tier II 425 and 450 HP product, CNH utilizes a hydraulically driven cooling fan. The speed at which the fan runs is determined by the following three temperatures:
>
> 1. coolant temperature
> 2. intake manifold temperature
> 3. hydraulic oil temperature.
>
> In early February 2002, CNH introduced a new charge air cooler with improved efficiency on both the STX 450 and TJ 450 tractors. The improved efficiency of the CAC allows the engine fan to run less often and/or at slower speed, which in turn allows for more available horsepower and better fuel economy. In order to realize this benefit, the ECM calibration was modified to reduce the demand for fan cooling while still controlling the maximum intake manifold temperature to the desired level.
>
> **Note · Примечание**
> The new CAC and new calibration does **not** apply to the STX 425 and TJ 425 tractors.
>
> The original Tier II QSX15 450 HP for CNH used Customer Interface Software option DO 1165. The new DO option for use with the improved CAC is DO 1259. When selecting the calibration for a STX 450 or TJ 450 tractor, the DO comment field will guide the user to the correct calibration. Specifically, the April 2002 ESDN INCAL CD will have the following note in the DO 1259 comment field: COMMENT: TRACTORS WITH IMPROVED COOLING SYSTEM (see Figure 1).
>
> Figure 1
>
> For the May 2002 ESDN INCAL CD-ROM, the engine serial number first (ESNF) for the new CAC became known, so the comment fields will read as follows; Before ESN 14027676 or After ESN 14027676 (see Figure 2).
>
> Figure 2
>
> **Note · Примечание**
> If DO 1165 is installed in engines built after 14027676, the benefit of the improved CAC will be lost, but the intake manifold temperature will be maintained at an acceptable level to maintain Tier II emissions standards.
>
> **Note · Примечание**
> If DO 1269 is installed in engines built before 14027676, the intake manifold temperature could exceed the maximum allowable temperature and possibly jeopardize compliance of Tier II emission standards. Do **not** use DO 1269 in engines built prior to ESN 14027676.
