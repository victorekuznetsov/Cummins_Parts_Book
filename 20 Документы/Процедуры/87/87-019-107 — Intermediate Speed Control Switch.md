---
aliases:
  - "Выключатель промежуточной частоты вращения"
type: "Процедура"
doc: "87-019-107"
title_en: "Intermediate Speed Control Switch"
title_ru: "Выключатель промежуточной частоты вращения"
modified: "2003-02-10"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666214"
figures: 7
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-019-107.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-019-107.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
  - "перевод/машинный"
---

# Intermediate Speed Control Switch
**Выключатель промежуточной частоты вращения**

> [!abstract] Процедура · `87-019-107`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section 19 - Electronic Controls - Group 19 · Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-02-10
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-019-107.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-019-107.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Система управления с промежуточной скоростью (ISC) ON, OFF и ON сигнализирует системе QST, что оператор запрашивает переход на одну из двух предустановленных скоростей между низким и высоким холостым ходом. Существует один трехпозиционный переключатель, который выбирает ISC 1, OFF и ISC 2.

![[19400281.png]]

Схема ISC показана для функций ISC 1 и ISC 2. Схема ISC соединена с двухполюсным, двухслойным (называемым переключателем DPDT), трехпозиционным переключателем.

![[19a00341.png]]

Трехпозиционный переключатель DPDT выборочно заземляет проводные номера 35 и 37 или проводные номера 38 и 37 или не имеет проводов. Показывается логика переключателя.

Линии, которые соединяют терминалы переключателей в трех положениях рычага, являются линиями непрерывности между терминалами.

В положении 1, переключатели 2, 3 и 5, 6 соединены, что замыкает ISC 2 и ISC валидацию (контакты 38 и 37) на землю.

В положении 2, никакие штифты не заземлены.

В позиции 3, переключатели терминалов 1, 2 и 4, 5 соединены, что сокращает ISC 1 и ISC валидацию (контакты 35 и 37) до земли.

![[19400283.png]]

### Проверка сопротивления

Если InsiteTM, номер 3824801, доступен, проверьте переключатель ISC для правильной работы. Если **не**, следуйте процедурам устранения неполадок в этом разделе.

Удалите четыре разъема из коммутатора.

Пометьте провода местоположением переключателя и номерами проводов.

![[19a00342.png]]

С помощью переключателя в положении 1, измеряют сопротивление от переключателя терминала 2 к переключателю терминала 3. Сопротивление должно быть 10 Ом или меньше.

Измерить сопротивление от переключателя 5 к переключателю 6. Сопротивление должно быть 10 Ом или меньше.

Измерьте сопротивление от переключателя 1 ко всем переключателям. Сопротивление должно быть 100k Ом или более.

Измерьте сопротивление от переключателя 4 до всех других терминалов. Сопротивление должно быть 100k Ом или более.

![[19400285.png]]

Переместите рычаг переключателя в положение 2.

Измерьте сопротивление от переключателя 1 до всех других терминалов. Сопротивление должно быть 100k Ом или более.

Измерьте сопротивление от переключателя 2 ко всем другим терминалам. Сопротивление должно быть 100k Ом или более.

![[19400286.png]]

Переместить рычаг переключателя в положение 3.

Измерьте сопротивление от переключателя 1 к терминалу 2. Сопротивление должно быть 10 Ом или меньше.

Измерить сопротивление от переключателя 4 к терминалу 5. Сопротивление должно быть 10 Ом или меньше.

Измерьте сопротивление от переключателя 3 ко всем другим терминалам. Сопротивление должно быть 100k Ом или более.

Измерьте сопротивление от переключателя 6 ко всем другим терминалам. Сопротивление должно быть 100k Ом или более.

Если мультиметр показывает **не** правильные значения, переключатель не работает. Проверьте тип переключателя и номера местонахождения терминала. См. руководство по устранению неполадок и ремонту OEM для процедур замены переключателей, а также для проверки типа переключателя и местоположения терминала.

![[19400287.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> The intermediate-speed control (ISC) ON, OFF, and ON switch circuit signals the QST system that the operator is requesting to go to one of two preset speeds between low idle and high idle. There is one three-position switch that selects ISC 1, OFF, and ISC 2.
>
> The ISC circuit is shown for ISC 1 and ISC 2 features. The ISC circuit is wired with a double-pole, double-throw (called a DPDT switch), three-position switch.
>
> The DPDT three-position switch selectively grounds wire numbers 35 and 37, or wire numbers 38 and 37, or no wires. The logic of the switch is shown.
>
> The lines that connect the switch terminals at the three lever positions are lines of continuity between the terminals.
>
> In position 1, switch terminal numbers 2, 3 and 5, 6 are connected, which shorts ISC 2 and ISC validation (pins 38 and 37) to ground.
>
> In position 2, no pins are grounded.
>
> In position 3, switch terminal numbers 1, 2 and 4, 5 are connected, which shorts ISC 1 and ISC validation (pins 35 and 37) to ground.
>
> ### Resistance Check
>
> If INSITE™, Part Number 3824801, is available, monitor the ISC switch for proper operation. If **not**, follow the troubleshooting procedures in this section.
>
> Remove the four connectors from the switch.
>
> Label the wires with the switch location and the wire numbers.
>
> With the switch in position 1, measure the resistance from switch terminal 2 to switch terminal 3. The resistance **must** be 10 ohms or less.
>
> Measure the resistance from switch terminal 5 to switch terminal 6. The resistance **must** be 10 ohms or less.
>
> Measure the resistance from switch terminal 1 to all switch terminals. The resistance **must** be 100k ohms or more.
>
> Measure the resistance from switch terminal 4 to all other terminals. The resistance **must** be 100k ohms or more.
>
> Move the switch lever to position 2.
>
> Measure the resistance from switch terminal 1 to all other terminals. The resistance **must** be 100k ohms or more.
>
> Measure the resistance from switch terminal 2 to all other terminals. The resistance **must** be 100k ohms or more.
>
> Move the switch lever to position 3.
>
> Measure the resistance from switch terminal 1 to terminal 2. The resistance **must** be 10 ohms or less.
>
> Measure the resistance from switch terminal 4 to terminal 5. The resistance **must** be 10 ohms or less.
>
> Measure the resistance from switch terminal 3 to all other terminals. The resistance **must** be 100k ohms or more.
>
> Measure the resistance from switch terminal 6 to all other terminals. The resistance **must** be 100k ohms or more.
>
> If the multimeter does **not** show the correct values, the switch has failed. Verify the switch type and terminal location numbers. Refer to the OEM troubleshooting and repair manual for switch replacement procedures, and to verify the switch type and terminal location.
