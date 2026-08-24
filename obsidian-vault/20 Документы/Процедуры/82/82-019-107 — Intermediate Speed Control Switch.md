---
aliases:
  - "Выключатель промежуточной частоты вращения"
type: "Процедура"
doc: "82-019-107"
title_en: "Intermediate Speed Control Switch"
title_ru: "Выключатель промежуточной частоты вращения"
modified: "2002-06-03"
engines:
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 7
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-107.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-019-107.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# Intermediate Speed Control Switch
**Выключатель промежуточной частоты вращения**

> [!abstract] Процедура · `82-019-107`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section 19 - Electronic Controls - Group 19 · Section 19 - Electronic Engine Controls
> **Даты:** изменён 2002-06-03
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-107.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-019-107.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Промежуточное управление скоростью (ISC) ON, OFF и ON сигнализирует ECM о том, что оператор просит перейти на одну из двух предустановленных скоростей между низким и высоким холостым ходом. Существует один трехпозиционный переключатель, который выбирает ISC 1, OFF и ISC 2.

![[19400281.png]]

Схема ISC показана для функций ISC 1 и ISC 2. Калибровка может иметь только один активный признак ISC. Схема ISC соединена с двойным полюсом, двойным броском (DPDT), трехпозиционным переключателем.

![[19c00906.png]]

Функции переключения DPDT в трех положениях для выборочно заземляемых проводов No. 23 и 33, или провода No. 25 и 33, или не заземляйте провода. Показывается логика переключателя.

Линии, которые соединяют терминалы переключателей в трех положениях рычага, являются линиями непрерывности между терминалами.

В позиции 1, переключатели терминалов No. 2, 3 и 5, 6 соединены, что шорты ISC 2 и ISC валидации (контакты 25 и 33) на землю.

В положении 2, никакие штифты не заземлены.

В позиции 3 переключатели No. 1, 2 и 4, 5 соединены, что шорты ISC 1 и ISC валидации (контакты 23 и 33) на землю.

![[19400283.png]]

### Проверка сопротивления

Если INSITETM доступен, проверьте переключатель ISC на предмет правильной работы. Если **не**, следуйте процедурам устранения неполадок в этом разделе.

Удалите четыре разъема из коммутатора. Пометьте провода местоположением переключателя и номерами проводов.

![[19c00907.png]]

С помощью переключателя в положении 1, измеряют сопротивление от переключателя терминала 2 к переключателю терминала 3. Сопротивление ** должно быть 10 Ом или меньше.

Измерить сопротивление от переключателя 5 к переключателю 6. Сопротивление ** должно быть 10 Ом или меньше.

Измерьте сопротивление от переключателя 1 ко всем переключателям. Сопротивление ** должно быть 100 К Ом или более.

Измерьте сопротивление от переключателя 4 до всех других терминалов. Сопротивление ** должно быть 100 К Ом или более.

![[19400285.png]]

Переместите рычаг переключателя в положение 2.

Измерьте сопротивление от переключателя 1 до всех других терминалов. Сопротивление ** должно быть 100 К Ом или более.

Измерьте сопротивление от переключателя 2 ко всем другим терминалам. Сопротивление ** должно быть 100 К Ом или более.

![[19400286.png]]

Переместить рычаг переключателя в положение 3.

Измерьте сопротивление от переключателя 1 к терминалу 2. Сопротивление ** должно быть 10 Ом или меньше.

Измерить сопротивление от переключателя 4 к терминалу 5. Сопротивление ** должно быть 10 Ом или меньше.

Измерьте сопротивление от переключателя 3 ко всем другим терминалам. Сопротивление ** должно быть 100 К Ом или более.

Измерьте сопротивление от переключателя 6 ко всем другим терминалам. Сопротивление ** должно быть 100 К Ом или более.

Если мультиметр показывает **не** правильные значения, переключатель не работает. Проверьте тип переключателя и номера местонахождения терминала. См. руководство по устранению неполадок и ремонту OEM для замены и проверки типа переключателя и местоположения терминала.

![[19400287.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> The intermediate speed control (ISC) ON, OFF, and ON switch circuit signals the ECM that the operator is requesting to go to one of two preset speeds between low idle and high idle. There is one three-position switch that selects ISC 1, OFF, and ISC 2.
>
> The ISC circuit is shown for ISC 1 and ISC 2 features. The calibration can have **only** one ISC active feature. The ISC circuit is wired with a double pole, double throw (DPDT), three-position switch.
>
> The DPDT three-position switch functions to selectively ground wires No. 23 and 33, or wires No. 25 and 33, or ground no wires. The logic of the switch is shown.
>
> The lines that connect the switch terminals at the three lever positions are lines of continuity between the terminals.
>
> In position 1, switch terminals No. 2, 3 and 5, 6 are connected which shorts ISC 2 and ISC validation (pins 25 and 33) to ground.
>
> In position 2, no pins are grounded.
>
> In position 3, switch terminals No. 1, 2 and 4, 5 are connected which shorts ISC 1 and ISC validation (pins 23 and 33) to ground.
>
> ### Resistance Check
>
> If INSITE™ is available, monitor the ISC switch for proper operation. If **not**, follow the troubleshooting procedures in this section.
>
> Remove the four connectors from the switch. Label the wires with the switch location and the wire numbers.
>
> With the switch in position 1, measure the resistance from switch terminal 2 to switch terminal 3. The resistance **must** be 10 ohms or less.
>
> Measure the resistance from switch terminal 5 to switch terminal 6. The resistance **must** be 10 ohms or less.
>
> Measure the resistance from switch terminal 1 to all switch terminals. The resistance **must** be 100K ohms or more.
>
> Measure the resistance from switch terminal 4 to all other terminals. The resistance **must** be 100K ohms or more.
>
> Move the switch lever to position 2.
>
> Measure the resistance from switch terminal 1 to all other terminals. The resistance **must** be 100K ohms or more.
>
> Measure the resistance from switch terminal 2 to all other terminals. The resistance **must** be 100K ohms or more.
>
> Move the switch lever to position 3.
>
> Measure the resistance from switch terminal 1 to terminal 2. The resistance **must** be 10 ohms or less.
>
> Measure the resistance from switch terminal 4 to terminal 5. The resistance **must** be 10 ohms or less.
>
> Measure the resistance from switch terminal 3 to all other terminals. The resistance **must** be 100K ohms or more.
>
> Measure the resistance from switch terminal 6 to all other terminals. The resistance **must** be 100K ohms or more.
>
> If the multimeter does **not** show the correct values, the switch has failed. Verify the switch type and terminal location numbers. Refer to the OEM troubleshooting and repair manual for replacement and to verify the switch type and terminal location.
