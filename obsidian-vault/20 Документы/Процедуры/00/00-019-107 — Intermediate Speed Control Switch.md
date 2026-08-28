---
aliases:
  - "Выключатель промежуточной частоты вращения"
type: "Процедура"
doc: "00-019-107"
title_en: "Intermediate Speed Control Switch"
title_ru: "Выключатель промежуточной частоты вращения"
modified: "2021-08-05"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
  - "37292556"
  - "37295879"
  - "41343322"
  - "41370103"
  - "82099327"
  - "85017333"
families:
  - "NT/NTA855 · ISM/QSM11"
  - "QSB6.7"
  - "QSK23"
  - "QSK60"
  - "QST30"
manuals:
  - "3666113"
  - "3666214"
  - "3666266"
  - "4326168"
figures: 14
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/00/00-019-107.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/00-019-107.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "двигатель/QSB6.7"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "двигатель/QST30"
  - "группа/00"
  - "перевод/машинный"
---

# Intermediate Speed Control Switch
**Выключатель промежуточной частоты вращения**

> [!abstract] Процедура · `00-019-107`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]], [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]], [[82099327 — QSB6.7 CM2150 B109 CPL 4375|82099327]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** NT/NTA855 · ISM/QSM11, QSB6.7, QSK23, QSK60, QST30
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]], [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]], [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]], [[4326168 — QSB6.7 CM2150 B109 Service Manual|4326168]]
> **Секции:** Section 19 - Electronic Controls - Group 19
> **Даты:** изменён 2021-08-05
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/00/00-019-107.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/00-019-107.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Выбор сервисного инструмента

#### Рекомендованный сервисный инструмент Cummins®

- Электронный сервисный инструмент Cummins® или эквивалент

#### Дополнительные сервисные позиции

- многомерный

### Общие сведения

Схема переключателя управления средней скоростью сигнализирует модулю управления двигателем (ECM), что оператор запрашивает двигатель для работы с заданной скоростью двигателя между низким и высоким холостым ходом. В зависимости от конфигурации, доступно до восьми скоростей. Эта процедура может охватывать не все возможные конфигурации, но проверки функциональности, предусмотренные в этой процедуре, будут одинаковыми для всех из них.

![[19400281.png]]

Схема управления промежуточной скоростью показана для функций управления промежуточной скоростью 1 и управления промежуточной скоростью 2. Калибровка может иметь только один активный элемент управления промежуточной скоростью. Промежуточная схема управления скоростью соединена с двойным полюсом, двойным броском, трехпозиционным переключателем.

![[19d03212.png]]

Двойной столб, двойной бросок, три переключателя положения, функционирует для выборочного заземления трех промежуточных проводов управления скоростью на ECM. Ссылка на схему проводов для местоположений терминала. Показывается логика переключателя.

Линии, которые соединяют терминалы переключателей в трех положениях рычага, являются линиями непрерывности между терминалами.

В положении 1, переключатели номер 2, 3 и 5, 6 соединены, что замыкает промежуточный контроль скорости 2 и промежуточное управление скоростью проверки (контакты 25 и 33) на землю.

В положении 2, никакие штифты не заземлены.

В положении 3 переключатели номер 1, 2 и 4, 5 соединены, что замыкает промежуточный контроль скорости 1 и промежуточное управление скоростью проверки (контакты 23 и 33) на землю.

![[19400283.png]]

### Первичная проверка

Подключите электронный инструмент к шине данных CAN транспортного средства.

Переведите замок зажигания в положение ON.

Управляйте промежуточным переключателем управления скоростью при мониторинге с помощью рекомендованной электронной системы обслуживания Cummins® или эквивалентной. Считывание электронных инструментов должно меняться с положением переключателя.

![[19900524.png]]

### Проверка сопротивления

Используйте следующие шаги для переключателя управления средней скоростью:

- Если электронный сервисный инструмент доступен, проследите за промежуточным переключателем управления скоростью для правильной работы. Если **не**, следуйте процедурам устранения неполадок в этом разделе.
- Удалите четыре разъема из коммутатора. Пометьте провода местоположением переключателя и номерами проводов, прежде чем удалить их из переключателя.

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

Если мультиметр показывает **не** правильные значения, переключатель неисправен. Проверьте тип переключателя и номера местонахождения терминала. См. руководство по эксплуатации изготовителя оригинального оборудования (OEM) для замены и проверки типа переключателя и местоположения терминала.

![[19400287.png]]

> [!warning] ОСТОРОЖНО
> Лиды должны плотно поместиться в разъеме без расширения штифтов в разъеме, иначе разъем будет поврежден.

Используйте следующие шаги для переменного переключателя управления средней скоростью.

Отсоедините разъём OEM-проводов от ECM. Отсоедините переменный промежуточный переключатель управления скоростью от проводной упряжки OEM. Установите мультиметр для измерения сопротивления.

Включить испытательный щуп в переменный промежуточный сигнал управления скоростью контакта разъёма проводов OEM-подключателя. Подключите клип аллигатора к многометровому щупу. Вставьте второй испытательный щуп в сигнальный контакт переключателя управления промежуточной скоростью и соедините зажим с другим многометровым щупом. Измерьте сопротивление.

![[19c01269.png]]

Мультиметр **должен** показывать измерение 10 Ом или меньше (замкнутая схема).

Если измеренное значение больше 10 Ом, в проводе SIGNAL имеется открытая схема.

Ремонт или замена OEM проводов жгута.[[99-019-071 — OEM Wiring Harness|См. процедуру 019-071 в разделе 19.]]

![[19c01235.png]]

Повторите проверку сопротивления для провода RETURN. Измерить сопротивление переменного контакта возврата выключателя управления средней скоростью разъёма проводов OEM к переменному контакту возврата выключателя управления средней скоростью выключателя.

Мультиметр **должен** показывать измерение 10 Ом или меньше (замкнутая схема).

Если измеренное значение больше 10 Ом, в проводе ВПЕРЕДЕНИЯ имеется открытая цепь.

Ремонт или замена OEM проводов жгута.[[99-019-071 — OEM Wiring Harness|См. процедуру 019-071 в разделе 19.]]

Повторите проверку сопротивления для 5-вольтового провода. Измерить сопротивление переменного межскоростного управляющего переключателя 5 вольт контакта питания OEM-проводов ремня разъема к переменному межскоростному управляющему переключателю 5 вольт контакта питания переключателя.

Мультиметр **должен** показывать измерение 10 Ом или меньше (замкнутая схема).

Если измеренное значение больше 10 Ом, то в 5-вольтовом проводе имеется открытая схема.

Ремонт или замена OEM проводов жгута.[[99-019-071 — OEM Wiring Harness|См. процедуру 019-071 в разделе 19.]]

### Проверка на замыкание на массу

Отсоедините разъём OEM-проводов от ECM. Отсоедините переменный промежуточный переключатель управления скоростью от проводной упряжки OEM. Установите мультиметр для измерения сопротивления.

Включить испытательный щуп в переменный промежуточный сигнал управления скоростью контакта разъёма проводов OEM-привода. Прикоснитесь к другому многометровому щупу, чтобы блокировать двигатель. Измерьте сопротивление.

![[19c01166.png]]

Мультиметр **должен** показывать измерение 100k Ом или более (открытая схема).

Если измеренное значение меньше 100k Ом, в проводе SIGNAL есть короткое замыкание на землю.

Ремонт или замена OEM проводов жгута.[[99-019-071 — OEM Wiring Harness|См. процедуру 019-071 в разделе 19.]]

![[19c01248.png]]

Повторите проверку провода RETURN с точностью до земли. Измерить сопротивление переменного промежуточного выключателя управления скоростью обратного контакта разъёма проводов OEM-системы с заземлением блока двигателя.

Мультиметр **должен** показывать измерение 100k Ом или более (открытая схема).

Если измеренное значение меньше 100k Ом, в проводе ВПЕРЕДЕНИЯ есть короткое замыкание на землю.

Ремонт или замена OEM проводов жгута.[[99-019-071 — OEM Wiring Harness|См. процедуру 019-071 в разделе 19.]]

Повторите проверку на проволоку 5 вольт. Измерить сопротивление переменного промежуточного регулятора скорости 5 вольт контакта питания разъёма проводов OEM-привода к заземлению блока двигателя.

Мультиметр **должен** показывать измерение 100k Ом или более (открытая схема).

Если измеренное значение меньше 100k Ом, есть короткое замыкание на землю в 5-вольтовом проводе.

Ремонт или замена OEM проводов жгута.[[99-019-071 — OEM Wiring Harness|См. процедуру 019-071 в разделе 19.]]

### Проверьте короткое замыкание от контакта к контакту

Отсоедините разъём OEM-проводов от ECM. Отсоедините переменный промежуточный переключатель управления скоростью от проводной упряжки OEM. Установите мультиметр для измерения сопротивления.

Измерьте сопротивление от переменного контакта сигнала переключателя управления средней скоростью в разъёме OEM-проводов с жгутом проводов ко всем другим штифтам в разъёме.

![[19c01215.png]]

Мультиметр **должен** показывать измерение 100k Ом или более (открытая схема).

Если измеренное значение меньше 100k Ом, между проводом SIGNAL и любым другим штифтом, который измерял замкнутую цепь, есть короткое замыкание.

Ремонт или замена OEM проводов жгута.[[99-019-071 — OEM Wiring Harness|См. процедуру 019-071 в разделе 19.]]

### Проверьте короткое замыкание на источнике внешнего напряжения

Отсоедините разъём OEM-проводов от ECM. Отсоедините переменный промежуточный переключатель управления скоростью от проводной упряжки OEM. Установите мультиметр для измерения вольт постоянного тока (VDC). Переключатель зажигания транспортного средства в положение Включения.

Включить испытательный щуп, соединенный с положительным (+) многометровым щупом, в переменный контакт сигнала переключателя управления средней скоростью разъёма проводов OEM-подключателя. Прикоснитесь к отрицательному (-) многометровому щупу, чтобы блокировать землю двигателя и измерить напряжение.

![[19c01158.png]]

Если присутствует напряжение, то есть короткое замыкание от провода SIGNAL к внешнему источнику напряжения.

Ремонт или замена OEM проводов жгута.[[99-019-071 — OEM Wiring Harness|См. процедуру 019-071 в разделе 19.]]

Повторите короткую проверку источника внешнего напряжения для провода RETURN. Измерьте напряжение от переменного среднего выключателя управления скоростью обратного контакта разъёма проводов OEM-системы с заземлением блока двигателя.

Если присутствует напряжение, то есть короткое замыкание от провода RETURN к внешнему источнику напряжения.

Ремонт или замена OEM проводов жгута.[[99-019-071 — OEM Wiring Harness|См. процедуру 019-071 в разделе 19.]]

Повторите короткую проверку источника внешнего напряжения для провода 5 вольт. Измерьте напряжение от переменного промежуточного регулятора скорости 5 вольт контакта питания разъёма проводов OEM-системы с заземлением блока двигателя.

Мультиметр **должен** показывать напряжение менее 5,5-VDC. Если напряжение больше 5,5-VDC, то происходит короткое замыкание от 5-вольтового провода SUPPLY к внешнему источнику напряжения.

Ремонт или замена OEM проводов жгута.[[99-019-071 — OEM Wiring Harness|См. процедуру 019-071 в разделе 19.]]


> [!quote]- Original (English) · английский оригинал
> ### Select Service Tools
>
> #### Recommended Cummins® Service Tools
>
> - Cummins® electronic service tool, or equivalent
>
> #### Additional Service Items
>
> - Multimeter
>
> ### General Information
>
> The intermediate speed control switch circuit signals the engine control module (ECM) that the operator is requesting the engine to run at a preset engine speed between low idle and high idle. Depending on the configuration, up to eight speeds are available. This procedure can **not** cover every possible configuration, but the functionality checks provided in this procedure will be similar for all of them.
>
> The intermediate speed control circuit is shown for intermediate speed control 1 and intermediate speed control 2 features. The calibration can have **only** one intermediate speed control active feature. The intermediate speed control circuit is wired with a double pole, double throw, three-position switch.
>
> The double pole, double throw, three position switch, functions to selectively ground the three intermediate speed control input wires to the ECM. Reference the wiring diagram for terminal locations. The logic of the switch is shown.
>
> The lines that connect the switch terminals at the three lever positions are lines of continuity between the terminals.
>
> In position 1, switch terminals number 2, 3 and 5, 6 are connected, which shorts intermediate speed control 2 and intermediate speed control validation (pins 25 and 33) to ground.
>
> In position 2, no pins are grounded.
>
> In position 3, switch terminals number 1, 2 and 4, 5 are connected, which shorts intermediate speed control 1 and intermediate speed control validation (pins 23 and 33) to ground.
>
> ### Initial Check
>
> Connect an electronic service tool to the vehicle data link.
>
> Turn the keyswitch to the ON position.
>
> Operate the intermediate speed control switch while monitoring with the recommended Cummins® electronic service tool or equivalent. The electronic service tool reading should change with the switch position.
>
> ### Resistance Check
>
> Use the following steps for the intermediate speed control switch:
>
> - If the electronic service tool is available, monitor the intermediate speed control switch for proper operation. If **not**, follow the troubleshooting procedures in this section.
> - Remove the four connectors from the switch. Label the wires with the switch location and the wire numbers before removing them from the switch.
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
> If the multimeter does **not** show the correct values, the switch has malfunctioned. Verify the switch type and terminal location numbers. Refer to the original equipment manufacturer (OEM) service manual for replacement and to verify the switch type and terminal location.
>
> **CAUTION · Осторожно**
> The leads must fit tightly in the connector without expanding the pins in the connector, otherwise the connector will be damaged.
>
> Use the following steps for the variable intermediate speed control switch.
>
> Disconnect the OEM harness connector from the ECM. Disconnect the variable intermediate speed control switch from the OEM harness. Set the multimeter to measure resistance.
>
> Insert a test lead into the variable intermediate speed control switch SIGNAL pin of the OEM harness connector. Connect the alligator clip to a multimeter probe. Insert the second test lead to the SIGNAL pin of the intermediate speed control switch and connect the clip to the other multimeter probe. Measure the resistance.
>
> The multimeter **must** show a measurement of 10 ohms or less (closed circuit).
>
> If the measured value is more than 10 ohms, there is an open circuit in the SIGNAL wire.
>
> Repair or replace the OEM harness. [[99-019-071 — OEM Wiring Harness|Refer to Procedure 019-071 in Section 19.]]
>
> Repeat the resistance check for the RETURN wire. Measure the resistance from the variable intermediate speed control switch RETURN pin of the OEM harness connector to the variable intermediate speed control switch RETURN pin of the switch.
>
> The multimeter **must** show a measurement of 10 ohms or less (closed circuit).
>
> If the measured value is more than 10 ohms, there is an open circuit in the RETURN wire.
>
> Repair or replace the OEM harness. [[99-019-071 — OEM Wiring Harness|Refer to Procedure 019-071 in Section 19.]]
>
> Repeat the resistance check for the 5 volt SUPPLY wire. Measure the resistance from the variable intermediate speed control switch 5 volt SUPPLY pin of the OEM harness connector to the variable intermediate speed control switch 5 volt SUPPLY pin of the switch.
>
> The multimeter **must** show a measurement of 10 ohms or less (closed circuit).
>
> If the measured value is more than 10 ohms, there is an open circuit in the 5 volt SUPPLY wire.
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
> Repeat the short-to-ground check for the 5 volt SUPPLY wire. Measure the resistance from the variable intermediate speed control switch 5 volt SUPPLY pin of the OEM harness connector to engine block ground.
>
> The multimeter **must** show a measurement of 100k ohms or more (open circuit).
>
> If the measured value is less than 100k ohms, there is a short circuit to ground in the 5 volt SUPPLY wire.
>
> Repair or replace the OEM harness. [[99-019-071 — OEM Wiring Harness|Refer to Procedure 019-071 in Section 19.]]
>
> ### Check for Short Circuit from Pin-to-Pin
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
> Disconnect the OEM harness connector from the ECM. Disconnect the variable intermediate speed control switch from the OEM harness. Set the multimeter to measure volts of direct current (VDC). Turn the vehicle keyswitch to the ON position.
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
>
> Repeat the short to external voltage source check for the 5 volt SUPPLY wire. Measure the voltage from the variable intermediate speed control switch 5 volt SUPPLY pin of the OEM harness connector to engine block ground.
>
> The multimeter **must** show a voltage of less than 5.5-VDC. If the voltage is greater than 5.5-VDC, there is a short circuit from the 5 volt SUPPLY wire to an external voltage source.
>
> Repair or replace the OEM harness. [[99-019-071 — OEM Wiring Harness|Refer to Procedure 019-071 in Section 19.]]
