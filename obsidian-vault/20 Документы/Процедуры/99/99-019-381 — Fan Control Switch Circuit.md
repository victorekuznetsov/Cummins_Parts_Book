---
aliases:
  - "Цепь выключателя управления вентилятором"
type: "Процедура"
doc: "99-019-381"
title_en: "Fan Control Switch Circuit"
title_ru: "Цепь выключателя управления вентилятором"
modified: "2015-06-25"
engines:
  - "41343322"
  - "41370103"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 7
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-381.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/99-019-381.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/99"
  - "перевод/машинный"
---

# Fan Control Switch Circuit
**Цепь выключателя управления вентилятором**

> [!abstract] Процедура · `99-019-381`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section 19 - Electronic Engine Controls
> **Даты:** изменён 2015-06-25
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-381.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/99-019-381.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Проверка сопротивления

> [!warning] ОСТОРОЖНО
> Правильные провода и/или одобренный Cummins® инструмент для тестирования цепи должны использоваться при работе с электрическими разъемами для предотвращения расширения штифта и повреждения разъема.

Если доступна электронная сервисная оснастка, проверьте схему переключателя управления вентилятором для правильной работы. Если **не**, следуйте процедурам устранения неполадок в этом разделе.

![[19803969.png]]

Отключите разъем интерфейса оригинального производителя оборудования (OEM) проводов жгута проводов двигателя. Чтобы определить местоположение разъема, см. соответствующую схему проводов двигателя. Вставьте один из испытательных щупов в выключатель обратного контакта разъёма проводов OEM-системы и соедините зажим аллигатора с многометровым щупом. Вставьте другой свинец в контакт сигнала переключателя управления вентилятором разъёма проводов OEM-подключателя и соедините зажим аллигатора с другим многометровым щупом.

Переместить переключатель управления вентилятором в положение выключения. Мультиметр **должен** показать замкнутую цепь (10 Ом и менее). Если цепь **не** закрыта, проверьте переключатель управления вентилятором, провод возврата переключателя и провод сигнала переключателя управления вентилятором для открытой цепи при условии, что переключатель был предварительно проверен. См. руководство по устранению неполадок и ремонту OEM для процедур ремонта. Если сопротивление находится в пределах спецификации, переключатель управления вентилятором, провод возврата переключателя (-) и провод сигнала управления вентилятором должны быть проверены на короткое замыкание на землю, короткое замыкание от контакта к контакту и короткое замыкание к внешнему источнику напряжения.

![[19c01194.png]]

### Проверка на замыкание на массу

Чтобы изолировать цепь переключателя управления вентилятором при проверке на электрическую короткость, отсоедините проводку OEM от ECM и переключателя управления вентилятором. Отсоедините переключатель положения сцепления/защитный переключатель двигателя и педаль акселератора. Установите все переключатели кабины в положение OFF или нейтральное. Установите рабочий тормоз с помощью ручного клапана прицепа.

![[19200292.png]]

Настройте мультиметр для измерения сопротивления. Вставьте измерительный щуп в контакт сигнала переключателя управления вентилятором разъёма проводов OEM-упряжи и соедините его с многометровым щупом. Прикоснитесь к другому многометровому щупу к заземлению блока двигателя. Измерьте сопротивление.

Мультиметр **должен** показать обрыв цепи (100 кОм и более). Если схема **не** открыта, в цепи управления переключателем вентилятора есть короткое замыкание, при условии, что переключатель был предварительно проверен. Ремонт или замена провода, подключенного к сигналу переключателя управления вентилятором в электропроводке OEM-привода в соответствии с процедурой производителя транспортного средства.

![[19c01241.png]]

### Проверка на замыкание между контактами

Изолируйте цепь переключателя управления вентилятором, установив переключатели, как в предыдущем разделе. Установите переключатель управления вентилятором в положение ON. Вставьте свинец в контакт сигнала вентилятора с переключателем управления. Подключите клип аллигатора к мультиметру. С другим свинцом, вставленным в обратный контакт переключателя, измеряйте сопротивление. Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Удалите свинец из контакта с сигналом переключателя управления вентилятором и проверьте все другие контакты. Измерьте сопротивление. Мультиметр **должен** показать обрыв цепи (100 кОм и более). Если схема **не** открыта, между схемой переключателя управления вентилятором и любым штифтом, который показывает замкнутую цепь, существует короткое замыкание при условии, что переключатель ранее был проверен. Ремонт или замена проводов в OEM проводах.[[99-019-071 — OEM Wiring Harness|См. процедуру 019-071]].

![[19c01236.png]]

### Проверьте короткое замыкание на источнике внешнего напряжения

Переведите замок зажигания в положение ON. Установите переключатель управления вентилятором на выключение. Настройте мультиметр для измерения VDC. Вставьте измерительный щуп в контакт сигнала переключателя управления вентилятором и прикрепите его к многометровому щупу. Прикоснитесь к другому многометровому щупу к заземлению блока двигателя. Измерьте напряжение. Напряжение должно быть 1.5 VDC или меньше.

![[19c01266.png]]

Если напряжение **не** правильно, то к цепи подключен внешний источник напряжения или между цепью переключателя управления вентилятором и проводом, несущим мощность в электропроводке OEM, имеется короткое замыкание. Удалите источник напряжения или отремонтируйте проводку в OEM-проводах в соответствии с процедурами производителя транспортного средства.

После ремонта подсоедините все компоненты.

> [!note] Примечание
> Если схема переключателя управления вентилятором была одобрена во всех предыдущих тестах, она работает правильно.

![[19c01181.png]]


> [!quote]- Original (English) · английский оригинал
> ### Resistance Check
>
> **CAUTION · Осторожно**
> Proper leads and/or a Cummins® approved circuit testing tool must be used when working with electrical connectors to prevent pin expansion and damage to the connector.
>
> If electronic service tool is available, monitor the fan control switch circuit for proper operation. If **not**, follow the troubleshooting procedures in this section.
>
> Disconnect the original equipment manufacturer (OEM) harness engine interface connector. To determine the location of the connector, see the corresponding engine wiring diagram. Insert one of the test leads into the switch return pin of the OEM harness connector and connect the alligator clip to the multimeter probe. Insert the other lead into the fan control switch signal pin of the OEM harness connector and connect the alligator clip to the other multimeter probe.
>
> Move the fan control switch to the OFF position. The multimeter **must** show a closed circuit (10 ohms or less). If the circuit is **not** closed, inspect the fan control switch, switch return wire, and the fan control switch signal wire for an open circuit, provided that the switch has been previously checked. Refer to the OEM troubleshooting and repair manual for repair procedures. If the resistance is within the specification, the fan control switch, switch return (-) wire, and the fan control signal wire **must** be checked for a short circuit to ground, a short circuit from pin-to-pin, and a short circuit to an external voltage source.
>
> ### Check for Short Circuit to Ground
>
> To isolate the fan control switch circuit when checking for an electrical short, disconnect the OEM harness from the ECM and fan control switch. Disconnect the clutch position switch/engine protection override switch and the accelerator pedal assembly. Set all cab panel switches to the OFF or neutral position. Set the service brake using the trailer brake hand valve.
>
> Adjust the multimeter to measure resistance. Insert a test lead into the fan control switch signal pin of the OEM harness connector and connect it to a multimeter probe. Touch the other multimeter probe to the engine block ground. Measure the resistance.
>
> The multimeter **must** show an open circuit (100k ohms or more). If the circuit is **not** open, there is a short circuit to ground in the fan switch control circuit, provided that the switch has been previously checked. Repair or replace the wire connected to the fan control switch signal in the OEM harness according to the vehicle manufacturer's procedure.
>
> ### Check for Short Circuit from Pin to Pin
>
> Isolate the fan control switch circuit by setting the switches as in the previous section. Set the fan control switch to the ON position. Insert the lead into the fan control switch signal pin. Connect the alligator clip to the multimeter. With the other lead inserted into the switch return pin, measure the resistance. The multimeter **must** show an open circuit (100k ohms or more).
>
> Remove the lead from the fan control switch signal pin and check all other pins. Measure the resistance. The multimeter **must** show an open circuit (100k ohms or more). If the circuit is **not** open, there is a short circuit between the fan control switch circuit and any pin that shows a closed circuit, provided the switch has previously been checked. Repair or replace the wires in the OEM harness. [[99-019-071 — OEM Wiring Harness|Refer to Procedure 019-071]].
>
> ### Check for Short Circuit to External Voltage Source
>
> Turn the keyswitch to the ON position. Set the fan control switch to OFF. Adjust the multimeter to measure VDC. Insert a test lead into the fan control switch signal pin and attach it to a multimeter probe. Touch the other multimeter probe to the engine block ground. Measure the voltage. The voltage **must** be 1.5 VDC or less.
>
> If the voltage is **not** correct, there is an external voltage source connected to the circuit, or there is a short circuit between the fan control switch circuit and a wire carrying power in the OEM harness. Remove the voltage source or repair the wiring in the OEM harness according to the vehicle manufacturer's procedures.
>
> Connect all components after completing the repair.
>
> **Note · Примечание**
> If the fan control switch circuit was approved in all of the previous tests, it is functioning correctly.
