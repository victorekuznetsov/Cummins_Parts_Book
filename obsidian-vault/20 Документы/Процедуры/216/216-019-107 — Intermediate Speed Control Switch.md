---
aliases:
  - "Выключатель промежуточной частоты вращения"
type: "Процедура"
doc: "216-019-107"
title_en: "Intermediate Speed Control Switch"
title_ru: "Выключатель промежуточной частоты вращения"
modified: "2013-04-16"
engines:
  - "82099327"
families:
  - "QSB6.7"
manuals:
  - "4326168"
figures: 18
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/216/216-019-107.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/216-019-107.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSB6.7"
  - "группа/216"
  - "перевод/машинный"
---

# Intermediate Speed Control Switch
**Выключатель промежуточной частоты вращения**

> [!abstract] Процедура · `216-019-107`
> **Двигатели:** [[82099327 — QSB6.7 CM2150 B109 CPL 4375|82099327]]
> **Семейство:** QSB6.7
> **Входит в руководства:** [[4326168 — QSB6.7 CM2150 B109 Service Manual|4326168]]
> **Секции:** Section 19 - Electronic Controls - Group 19
> **Даты:** изменён 2013-04-16
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/216/216-019-107.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/216-019-107.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Схема переключателя управления средней скоростью (ISC) сигнализирует модулю управления двигателем (ECM), что оператор запрашивает двигатель для работы с заданной скоростью двигателя между низким и высоким холостым ходом. В зависимости от конфигурации, доступно до восьми скоростей. Эта процедура может охватывать не все возможные конфигурации, но проверки функциональности, предусмотренные в этой процедуре, будут одинаковыми для всех из них.

![[19400281.png]]

Схема ISC показана для функций ISC 1 и ISC 2. Калибровка может иметь только один активный признак ISC. Схема ISC соединена с двойным полюсом, двойным броском (DPDT), трехпозиционным переключателем.

![[19d03212.png]]

Функции переключателя с двойным полюсом, двойным броском (DPDT) для выборочного заземления трех входных проводов ISC на ECM. Смотрите схему проводов для местоположений терминала. Показывается логика переключателя.

Линии, которые соединяют терминалы переключателей в трех положениях рычага, являются линиями непрерывности между терминалами.

В позиции 1, переключатели терминалов No. 2, 3 и 5, 6 соединены, что сокращает ISC 2 и ISC валидацию (контакты 25 и 33) до земли.

В положении 2, никакие штифты не заземлены.

В позиции 3 переключатели No. 1, 2 и 4, 5 соединены, что сокращает ISC 1 и ISC валидацию (контакты 23 и 33) до земли.

![[19400283.png]]

### Проверка сопротивления

Используйте следующие шаги для переключателя управления скоростью:

Если имеется электронный сервисный инструмент INSITETM, проверьте коммутатор ISC на предмет правильной работы. Если **не**, следуйте процедурам устранения неполадок в этом разделе.

Удалите четыре разъема из коммутатора. Пометьте провода местоположением переключателя и номерами проводов, прежде чем удалить их из переключателя.

![[19d03213.png]]

С помощью переключателя в положении 1, измеряют сопротивление от переключателя терминала 2 к переключателю терминала 3. Сопротивление должно быть 10 Ом или меньше.

Измерить сопротивление от переключателя 5 к переключателю 6. Сопротивление должно быть 10 Ом или меньше.

Измерьте сопротивление от переключателя 1 ко всем переключателям. Сопротивление должно быть 100 К Ом или более.

Измерьте сопротивление от переключателя 4 до всех других терминалов. Сопротивление должно быть 100 К Ом или более.

![[19400285.png]]

Переместите рычаг переключателя в положение 2.

Измерьте сопротивление от переключателя 1 до всех других терминалов. Сопротивление должно быть 100 К Ом или более.

Измерьте сопротивление от переключателя 2 ко всем другим терминалам. Сопротивление должно быть 100 К Ом или более.

![[19400286.png]]

Переместить рычаг переключателя в положение 3.

Измерьте сопротивление от переключателя 1 к терминалу 2. Сопротивление должно быть 10 Ом или меньше.

Измерить сопротивление от переключателя 4 к терминалу 5. Сопротивление должно быть 10 Ом или меньше.

Измерьте сопротивление от переключателя 3 ко всем другим терминалам. Сопротивление должно быть 100 К Ом или более.

Измерьте сопротивление от переключателя 6 ко всем другим терминалам. Сопротивление должно быть 100 К Ом или более.

Если мультиметр показывает **не** правильные значения, переключатель неисправен. Проверьте тип переключателя и номера местонахождения терминала. См. руководство по обслуживанию OEM для замены и проверки типа переключателя и местоположения терминала.

![[19400287.png]]

> [!warning] ОСТОРОЖНО
> Лиды должны плотно поместиться в разъеме без расширения штифтов в разъеме, иначе разъем будет поврежден.

Используйте следующие шаги для переменного переключателя управления средней скоростью.

Отсоедините разъем электропроводки от производителя оригинального оборудования (OEM) от ECM. Отсоедините переменный промежуточный переключатель управления скоростью от проводной упряжки OEM. Установите мультиметр для измерения сопротивления.

Включить испытательный щуп в переменный промежуточный сигнал управления скоростью контакта разъёма проводов OEM-подключателя. Подключите клип аллигатора к многометровому щупу. Вставьте второй испытательный щуп в сигнальный контакт переключателя управления промежуточной скоростью и соедините зажим с другим многометровым щупом. Измерьте сопротивление.

![[19c01269.png]]

Мультиметр **должен** показывать измерение 10 Ом или меньше (замкнутая схема).

Если измеренное значение превышает 10 Ом, в сигнальном проводе имеется открытая схема.

Ремонт или замена OEM проводов жгута.[[99-019-071 — OEM Wiring Harness|См. процедуру 019-071 в разделе 19.]]

![[19c01235.png]]

Повторите проверку сопротивления для обратного провода. Измерить сопротивление переменного контакта возврата выключателя управления средней скоростью разъёма проводов OEM к переменному контакту возврата выключателя управления средней скоростью выключателя.

Мультиметр **должен** показывать измерение 10 Ом или меньше (замкнутая схема).

Если измеренное значение больше 10 Ом, в проводе ВПЕРЕДЕНИЯ имеется открытая цепь.

Ремонт или замена OEM проводов жгута.[[99-019-071 — OEM Wiring Harness|См. процедуру 019-071 в разделе 19.]]

![[19c01235.png]]

### Проверка на замыкание на массу

Отсоедините разъём OEM-проводов от ECM. Отсоедините переменный промежуточный переключатель управления скоростью от проводной упряжки OEM. Установите мультиметр для измерения сопротивления.

Включить испытательный щуп в переменный промежуточный сигнал управления скоростью контакта разъёма проводов OEM-привода. Прикоснитесь к другому многометровому щупу, чтобы блокировать двигатель. Измерьте сопротивление.

![[19c01166.png]]

Мультиметр **должен **показывать измерение 100k Ом или более (открытая схема).

Если измеренное значение меньше 100k Ом, в проводе SIGNAL есть короткое замыкание на землю.

Ремонт или замена OEM проводов жгута.[[99-019-071 — OEM Wiring Harness|См. процедуру 019-071 в разделе 19.]]

![[19c01248.png]]

Повторите проверку провода RETURN с точностью до земли. Измерить сопротивление переменного промежуточного выключателя управления скоростью обратного контакта разъёма проводов OEM-системы с заземлением блока двигателя.

Мультиметр **должен **показывать измерение 100k Ом или более (открытая схема).

Если измеренное значение меньше 100k Ом, в проводе ВПЕРЕДЕНИЯ есть короткое замыкание на землю.

Ремонт или замена OEM проводов жгута.[[99-019-071 — OEM Wiring Harness|См. процедуру 019-071 в разделе 19.]]

![[19c01248.png]]

### Проверка на замыкание между контактами

Отсоедините разъём OEM-проводов от ECM. Отсоедините переменный промежуточный переключатель управления скоростью от проводной упряжки OEM. Установите мультиметр для измерения сопротивления.

Измерьте сопротивление от переменного контакта сигнала переключателя управления средней скоростью в разъёме OEM-проводов с жгутом проводов ко всем другим штифтам в разъёме.

![[19c01194.png]]

Мультиметр **должен **показывать измерение 100k Ом или более (открытая схема).

Если измеренное значение меньше 100k Ом, между проводом SIGNAL и любым другим штифтом, который измерял замкнутую цепь, есть короткое замыкание.

Ремонт или замена OEM проводов жгута.[[99-019-071 — OEM Wiring Harness|См. процедуру 019-071 в разделе 19.]]

![[19c01215.png]]

### Проверьте короткое замыкание на источнике внешнего напряжения

Отсоедините разъём OEM-проводов от ECM. Отсоедините переменный промежуточный переключатель управления скоростью от проводной упряжки OEM. Установите мультиметр для измерения VDC. Переключатель зажигания транспортного средства в положение Включения.

Включить испытательный щуп, соединенный с положительным (+) многометровым щупом, в переменный контакт сигнала переключателя управления средней скоростью разъёма проводов OEM-подключателя. Прикоснитесь к отрицательному (-) многометровому щупу, чтобы блокировать землю двигателя и измерить напряжение.

![[19c01158.png]]

Если присутствует напряжение, то есть короткое замыкание от провода SIGNAL к внешнему источнику напряжения.

Ремонт или замена OEM проводов жгута.[[99-019-071 — OEM Wiring Harness|См. процедуру 019-071 в разделе 19.]]

![[19c01158.png]]

Повторите короткую проверку источника внешнего напряжения для провода RETURN. Измерьте напряжение от переменного среднего выключателя управления скоростью обратного контакта разъёма проводов OEM-системы с заземлением блока двигателя.

Если присутствует напряжение, то есть короткое замыкание от провода RETURN к внешнему источнику напряжения.

Ремонт или замена OEM проводов жгута.[[99-019-071 — OEM Wiring Harness|См. процедуру 019-071 в разделе 19.]]

![[19c01158.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> The intermediate speed control (ISC) switch circuit signals the engine control module (ECM) that the operator is requesting the engine to run at a preset engine speed between low idle and high idle. Depending on the configuration, up to eight speeds are available. This procedure can **not** cover every possible configuration, but the functionality checks provided in this procedure will be similar for all of them.
>
> The ISC circuit is shown for ISC 1 and ISC 2 features. The calibration can have **only** one ISC active feature. The ISC circuit is wired with a double pole, double throw (DPDT), three-position switch.
>
> The double pole, double throw (DPDT) three-position switch functions to selectively ground the three ISC input wires to the ECM. Refer to the wiring diagram for terminal locations. The logic of the switch is shown.
>
> The lines that connect the switch terminals at the three lever positions are lines of continuity between the terminals.
>
> In position 1, switch terminals No. 2, 3 and 5, 6 are connected, which shorts ISC 2 and ISC validation (pins 25 and 33) to ground.
>
> In position 2, no pins are grounded.
>
> In position 3, switch terminals No. 1, 2 and 4, 5 are connected, which shorts ISC 1 and ISC validation (pins 23 and 33) to ground.
>
> ### Resistance Check
>
> Use the following steps for the intermedate speed control switch:
>
> If INSITE™ electronic service tool is available, monitor the ISC switch for proper operation. If **not**, follow the troubleshooting procedures in this section.
>
> Remove the four connectors from the switch. Label the wires with the switch location and the wire numbers before removing them from the switch.
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
> If the multimeter does **not** show the correct values, the switch has malfunctioned. Verify the switch type and terminal location numbers. Refer to the OEM service manual for replacement and to verify the switch type and terminal location.
>
> **CAUTION · Осторожно**
> The leads must fit tightly in the connector without expanding the pins in the connector otherwise the connector will be damaged.
>
> Use the following steps for the variable intermediate speed control switch.
>
> Disconnect the original equipment manufacturer (OEM) harness connector from the ECM. Disconnect the variable intermediate speed control switch from the OEM harness. Set the multimeter to measure resistance.
>
> Insert a test lead into the variable intermediate speed control switch signal pin of the OEM harness connector. Connect the alligator clip to a multimeter probe. Insert the second test lead to the signal pin of the intermediate speed control switch and connect the clip to the other multimeter probe. Measure the resistance.
>
> The multimeter **must** show a measurement of 10 ohms or less (closed circuit).
>
> If the measured value is more than 10 ohms, there is an open circuit in the signal wire.
>
> Repair or replace the OEM harness. [[99-019-071 — OEM Wiring Harness|Refer to Procedure 019-071 in Section 19.]]
>
> Repeat the resistance check for the return wire. Measure the resistance from the variable intermediate speed control switch RETURN pin of the OEM harness connector to the variable intermediate speed control switch return pin of the switch.
>
> The multimeter **must** show a measurement of 10 ohms or less (closed circuit).
>
> If the measured value is more than 10 ohms, there is an open circuit in the RETURN wire.
>
> Repair or replace the OEM harness. [[99-019-071 — OEM Wiring Harness|Refer to Procedure 019-071 in Section 19.]]
>
> ### Check for Short Circuit to Ground
>
> Disconnect the OEM harness connector from the ECM. Disconnect the variable intermediate speed control switch from the OEM harness. Set the multimeter to measure resistance.
>
> Insert the test lead into the variable intermediate speed control switch SIGNAL pin of the OEM harness connector. Touch the other multimeter probe to engine block ground. Measure the resistance.
>
> The multimeter **must** show a measurement of 100k ohms or more (open circuit).
>
> If the measured value is less than 100k ohms, there is a short circuit to ground in the SIGNAL wire.
>
> Repair or replace the OEM harness. [[99-019-071 — OEM Wiring Harness|Refer to Procedure 019-071 in Section 19.]]
>
> Repeat the short-to-ground check for the RETURN wire. Measure the resistance from the variable intermediate speed control switch RETURN pin of the OEM harness connector to engine block ground.
>
> The multimeter **must** show a measurement of 100k ohms or more (open circuit).
>
> If the measured value is less than 100k ohms, there is a short circuit to ground in the RETURN wire.
>
> Repair or replace the OEM harness. [[99-019-071 — OEM Wiring Harness|Refer to Procedure 019-071 in Section 19.]]
>
> ### Check for Short Circuit from Pin to Pin
>
> Disconnect the OEM harness connector from the ECM. Disconnect the variable intermediate speed control switch from the OEM harness. Set the multimeter to measure resistance.
>
> Measure the resistance from the variable intermediate speed control switch SIGNAL pin in the OEM harness connector to all other pins in the connector.
>
> The multimeter **must** show a measurement of 100k ohms or more (open circuit).
>
> If the measured value is less than 100k ohms, there is a short circuit between the SIGNAL wire and any other pin that measured a closed circuit.
>
> Repair or replace the OEM harness. [[99-019-071 — OEM Wiring Harness|Refer to Procedure 019-071 in Section 19.]]
>
> ### Check for Short Circuit to External Voltage Source
>
> Disconnect the OEM harness connector from the ECM. Disconnect the variable intermediate speed control switch from the OEM harness. Set the multimeter to measure VDC. Turn the vehicle keyswitch to the ON position.
>
> Insert the test lead connected to the positive (+) multimeter probe into the variable intermediate speed control switch SIGNAL pin of the OEM harness connector. Touch the negative (-) multimeter probe to engine block ground and measure the voltage.
>
> If there is voltage present, there is a short circuit from the SIGNAL wire to an external voltage source.
>
> Repair or replace the OEM harness. [[99-019-071 — OEM Wiring Harness|Refer to Procedure 019-071 in Section 19.]]
>
> Repeat the short to external voltage source check for the RETURN wire. Measure the voltage from the variable intermediate speed control switch RETURN pin of the OEM harness connector to engine block ground.
>
> If there is voltage present, there is a short circuit from the RETURN wire to an external voltage source.
>
> Repair or replace the OEM harness. [[99-019-071 — OEM Wiring Harness|Refer to Procedure 019-071 in Section 19.]]
