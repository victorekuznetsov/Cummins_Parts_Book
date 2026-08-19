---
aliases:
  - "Магистральный жгут проводов"
type: "Процедура"
doc: "60-019-174"
title_en: "Backbone Wiring Harness"
title_ru: "Магистральный жгут проводов"
modified: "2008-01-17"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021674"
figures: 13
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-019-174.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-019-174.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
  - "перевод/машинный"
---

# Backbone Wiring Harness
**Магистральный жгут проводов**

> [!abstract] Процедура · `60-019-174`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section 19 — Electronic Engine Controls — Group 19
> **Даты:** изменён 2008-01-17
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-019-174.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-019-174.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Стержневой упряжкой J1939 соединены первичные и вторичные ECM, а также обеспечивается интерфейсный разъем для инструментальных средств обслуживания.

Стержневой упряжкой проводов J1939 требуется наличие двух конечных резисторов (120 Ом каждый) параллельно с положительными (+) шинами данных J1939 CAN и отрицательными линиями шины данных J1939 CAN. Эти конечные резисторы находятся на каждом конце магистральной проводов.

![[19a00542.png]]

Кроме того, магистральная проводка защищена для уменьшения электрических помех на шине данных CAN. Эта экранированная линия заземлена до блока двигателя.

![[19a00545.png]]

Корневая проводка QST30 состоит из четырех интерфейсных разъемов, которые представляют собой треугольные 3-контактные соединительные корпуса DeutschTM.

Корневая проводка QST30 также состоит из двух завершающих резисторов. Резисторы вставляются в колпачок и подключаются к цепи шины данных CAN при подключении к терминалу.

![[19a00542.png]]

Чтобы определить, является ли защелка с защелкой интерфейсом службы или заглубленной резисторной заглушкой, удалите крышку и исследуйте внутреннюю часть. Концевые резисторы имеют синий цвет, с двумя штифтами, видимыми внутри.

Концевые крышки интерфейса интерфейса службы оранжевого цвета и не имеют контактов в крышке. Это подходящее место для подключения инструментария службы для связи с ECM.

> [!note] Примечание
> Подключаясь к любому из двух разъемов интерфейса инструментария обслуживания, шина данных CAN поддерживает связь с обоими ECM.

![[19802397.png]]

Два 6-контактных разъема шины данных CAN на стороне двигателя ** не используются с сервисной оснасткой. Они представляют собой порты шины данных J1587/1708 CAN и используются только для общего инструмента. Для оснащения двигателей QST30 электронным сервисом INSITETM требуется протокол связи J1939 с адаптером INLINETM II.

На двигателях с 9-контактным разъемом шины данных CAN были удалены терминалы интерфейса сервисной оснастки на магистрали J1939. Используйте этот 9-контактный разъем шины данных CAN с помощью инструментария службы для связи с обоими ECM.

> [!note] Примечание
> Двигатели с двумя круглыми 6-контактными разъемами DeutschTM ** должны ** использовать треугольный 3-контактный интерфейсный разъем для инструментов Deutsch. 6-контактные разъемы ** не** будут работать с электронным сервисным оборудованием INSITETM.

![[19802393.png]]

### Снятие

Отсоедините 3-контактные разъёмы магистральной проводов J1939 от J1939 CAN шины передачи данных.

![[19a00546.png]]

Отсоедините блок двигателя от блока.

![[19a00545.png]]

Перережьте галстуки на магистральной проводах J1939.

Удалите из двигателя магистральную проводку J1939.

![[19a00547.png]]

### Проверка при повторном использовании

Ремонт или замена жгута проводов двигателя, если есть открытая цепь или короткое замыкание, обнаруженное под защитным покрытием корпуса жгута проводов.

![[19a00542.png]]

### Установка

Установите на двигатель магистральную проводку J1939.

![[19a00542.png]]

Подключите 3-контактные разъёмы магистральной проводов J1939 к лево- и правобережной проводах.

![[19a00546.png]]

Подключите блок двигателя к блоку.

![[19a00545.png]]

Обеспечьте цепь магистральной проводов J1939 к двигателю с использованием покрытых проводных связей.

![[19a00547.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> The J1939 backbone harness connects the primary and secondary ECMs in addition to providing a service tool interface connector.
>
> The J1939 backbone harness is required to have two terminating resistors (120 ohms each) in parallel with the J1939 data link positive (+) and J1939 data link negative lines. These terminating resistors are on each end of the backbone harness.
>
> In addition, the backbone harness is shielded to reduce electrical interference on the data link. This shielded line is grounded to the engine block.
>
> The QST30 backbone harness consists of four interface connectors, which are triangular 3-pin Deutsch™ connector bodies.
>
> The QST30 backbone harness also consists of two terminating resistor plugs. The resistors are inserted into the cap and connect through to the data link circuit when plugged into a terminal.
>
> To determine if a capped plug is a service tool interface plug or a terminating resistor plug, remove the cap and examine the inside. The terminating resistor caps are blue in color, with two pins visible on the inside.
>
> The service tool interface terminal caps are orange in color and have no pins in the cap. This is the proper place to connect the service tool to communicate with the ECMs.
>
> **Note · Примечание**
> By plugging into either of the two service tool interface connectors, the data link has communication with both ECMs.
>
> The two 6-pin engine-side data link connectors are **not** used with the service tool. They are J1587/1708 data link ports and are **only** used for a generic tool. INSITE™ electronic service tool for QST30 engines requires a J1939 communication protocol with an INLINE™ II adapter.
>
> On engines with a 9-pin engine-side data link connector, the service tool interface terminals on the J1939 backbone have been removed. Use this 9-pin data link connector with the service tool to communicate with both ECMs.
>
> **Note · Примечание**
> Engines with two round 6-pin Deutsch™ connectors **must** use the triangular 3-pin Deutsch service tool interface connector. The 6-pin connectors will **not** work with the INSITE™ electronic service tool.
>
> ### Remove
>
> Disconnect the 3-pin J1939 backbone harness connectors from the J1939 data link harness.
>
> Disconnect the engine block ground from the block.
>
> Cut the ties on the J1939 backbone harness.
>
> Remove the J1939 backbone harness from the engine.
>
> ### Inspect for Reuse
>
> Repair or replace the engine harness if there is an open circuit or a short circuit found under the protective covering of the harness body.
>
> ### Install
>
> Install the J1939 backbone harness onto the engine.
>
> Connect the 3-pin J1939 backbone harness connectors to the left- and right-bank harnesses.
>
> Connect the engine block ground to the block.
>
> Secure the J1939 backbone harness to the engine using coated wire ties.
