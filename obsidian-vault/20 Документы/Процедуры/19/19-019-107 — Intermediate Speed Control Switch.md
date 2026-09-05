---
aliases:
  - "Выключатель промежуточной частоты вращения"
type: "Процедура"
doc: "19-019-107"
title_en: "Intermediate Speed Control Switch"
title_ru: "Выключатель промежуточной частоты вращения"
modified: "2002-11-07"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
  - "85017333"
families:
  - "QSK23"
  - "QSK60"
manuals:
  - "3666113"
figures: 8
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-019-107.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-019-107.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
  - "перевод/машинный"
---

# Intermediate Speed Control Switch
**Выключатель промежуточной частоты вращения**

> [!abstract] Процедура · `19-019-107`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section 19 - Electronic Controls - Group 19 · Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2002-11-07
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-019-107.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-019-107.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Промежуточная схема управления скоростью ON, OFF и ON сигнализирует системе QSK, что оператор запрашивает переход на одну из двух предустановленных скоростей между низким и высоким холостым ходом. Существует один трехпозиционный переключатель, который выбирает ISC1, OFF и ISC2.

![[19400281.png]]

Схема управления промежуточной скоростью показана для функций управления промежуточной скоростью 1 и управления промежуточной скоростью 2. Калибровка может **только **иметь одну активную функцию управления скоростью. Промежуточная схема управления скоростью соединена с двойным полюсом, двойным броском (DPDT), трехпозиционным переключателем.

![[19400282.png]]

Функции трехпозиционного переключателя DPDT для выборочно заземляемых проводов № 35 и 37, или проводов № 38 и 37, или проводов заземляемых номеров. Показывается логика переключателя.

Линии, которые соединяют терминалы переключателей в трех положениях рычага, являются линиями непрерывности между терминалами.

В положении 1, переключатели номер 2, 3 и 5, 6 соединены, что замыкает промежуточный контроль скорости 2 и промежуточное управление скоростью проверки (контакты 38 и 37) на землю.

В положении 2, никакие штифты не заземлены.

В положении 3 переключатели номеров 1, 2 и 4, 5 соединены между собой, что позволяет осуществлять контроль промежуточной скорости 1 и проверку контроля промежуточной скорости (контакты 35 и 37) на земле.

![[19400283.png]]

### Первичная проверка

Подключите электронный инструмент к шине данных CAN транспортного средства.

Переведите замок зажигания в положение ON.

Управляйте промежуточным выключателем управления скоростью при мониторинге с помощью INSITETM. Считывание INSITETM должно меняться с переключателем.

![[19900524.png]]

### Проверка сопротивления

Если InsiteTM, номер 3824801, доступен, проверьте промежуточный выключатель управления скоростью для правильной работы. Если **не**, следуйте процедурам устранения неполадок в этом разделе.

Удалите четыре разъема из коммутатора. Пометьте провода местоположением переключателя и номерами проводов.

![[19400284.png]]

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

Если мультиметр показывает **не** правильные значения, переключатель не работает. Проверьте тип переключателя и номера местонахождения терминала. См. руководство по ремонту OEM для замены и проверки типа переключателя и местоположения терминала.

![[19400287.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> The intermediate speed control ON, OFF, and ON switch circuit signals the QSK system that the operator is requesting to go to one of two preset speeds between low idle and high idle. There is one three-position switch that selects ISC1, OFF, and ISC2.
>
> The intermediate speed control circuit is shown for intermediate speed control 1 and intermediate speed control 2 features. The calibration can **only** have one intermediate speed control active feature. The intermediate speed control circuit is wired with a double pole, double throw (DPDT), three-position switch.
>
> The DPDT three-position switch functions to selectively ground wires number 35 and 37, or wires number 38 and 37, or ground number wires. The logic of the switch is shown.
>
> The lines that connect the switch terminals at the three lever positions are lines of continuity between the terminals.
>
> In position 1, switch terminals number 2, 3 and 5, 6 are connected which shorts intermediate speed control 2 and intermediate speed control validation (pins 38 and 37) to ground.
>
> In position 2, no pins are grounded.
>
> In position 3, switch terminals number 1, 2 and 4, 5 are connected which shorts intermediate speed control 1 and intermediate speed control validation (pins 35 and 37) to ground.
>
> ### Initial Check
>
> Connect an electronic service tool to the vehicle datalink.
>
> Turn the keyswitch to the ON position.
>
> Operate the intermediate speed control switch while monitoring with INSITE™. The INSITE™ reading should change with the switch position.
>
> ### Resistance Check
>
> If INSITE™, Part Number 3824801, is available, monitor the intermediate speed control switch for proper operation. If **not**, follow the troubleshooting procedures in this section.
>
> Remove the four connectors from the switch. Label the wires with the switch location and the wire numbers.
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
> If the multimeter does **not** show the correct values, the switch has failed. Verify the switch type and terminal location numbers. Refer to the OEM repair manual for replacement and to verify the switch type and terminal location.
