---
aliases:
  - "Цепь выключателя моторного тормоза"
type: "Процедура"
doc: "99-019-035"
title_en: "Engine Brake ON/OFF Switch Circuit"
title_ru: "Цепь выключателя моторного тормоза"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-035.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/99-019-035.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/99"
  - "перевод/машинный"
---

# Engine Brake ON/OFF Switch Circuit
**Цепь выключателя моторного тормоза**

> [!abstract] Процедура · `99-019-035`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section 19 - Electronic Engine Controls
> **Даты:** изменён 2015-06-25
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-035.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/99-019-035.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Проверка сопротивления

> [!warning] ОСТОРОЖНО
> Правильные провода и/или одобренный Cummins® инструмент для тестирования цепи должны использоваться при работе с электрическими разъемами для предотвращения расширения штифта и повреждения разъема.

Если имеется электронное оборудование для обслуживания, следите за схемой переключения тормозов двигателя для правильной работы. Если **не**, следуйте процедурам устранения неполадок в этом разделе.

Отключите разъем интерфейса оригинального производителя оборудования (OEM) проводов жгута проводов двигателя. Чтобы определить местоположение разъема, см. соответствующую схему проводов двигателя.

Вставьте один из измерительных щупов в выключатель возврата разъёма проводов OEM-системы и соедините зажим аллигатора с многометровым щупом. Вставьте другой свинец в сигнал селектора тормозов двигателя № 1 разъёма проводов OEM-системы и соедините зажим аллигатора с другим многометровым щупом.

![[19803969.png]]

Переместить тормоз двигателя ON/OFF в положение ON. Переместить переключатель уровня тормоза двигателя в положение № 1 для шестипозиционного переключателя или в положение № 2 для трехпозиционного переключателя. Мультиметр **должен** показать замкнутую цепь (10 Ом и менее). Если цепь **не** закрыта, проверьте возврат выключателя и сигнал селектора тормозов двигателя № 1 для открытой цепи при условии, что выключатель был предварительно проверен. См. руководство по устранению неполадок и ремонту OEM для процедур ремонта. Если сопротивление находится в пределах спецификации, сигнал возврата переключателя и селектор тормозов двигателя № 1  должен быть проверен на короткое замыкание на землю, короткое замыкание от штифта до штифта и короткое замыкание к внешнему источнику напряжения.

Удалите свинец из сигнала селектора тормозов двигателя № 1 и вставьте его в сигнал селектора тормозов двигателя № 2 разъёма проводов OEM-подключателя.

Переместить тормоз двигателя ON/OFF в положение ON. Переместить переключатель уровня тормоза двигателя в положение № 2 для шестипозиционного переключателя или в положение № 1 для трехпозиционного переключателя.

Мультиметр **должен** показать замкнутую цепь (10 Ом и менее). Если цепь **не** закрыта, проверьте сигнал селектора тормозов двигателя № 2 для провода с открытым контуром при условии, что выключатель был предварительно проверен. См. руководство по устранению неполадок и ремонту OEM для процедур ремонта.

Если сопротивление находится в пределах спецификации, сигнал селектора тормоза двигателя № 2 провод должен быть проверен на короткое замыкание на землю, короткое замыкание от штифта до штифта и короткое замыкание к внешнему источнику напряжения.

Удалите свинец из сигнала селектора тормозов двигателя № 2 и вставьте его в сигнал селектора тормозов двигателя № 3 проводной упряжки OEM.

Переместить тормоз двигателя ON/OFF в положение ON. Переместить уровень тормоза двигателя в положение № 3.

Мультиметр **должен** показать замкнутую цепь (10 Ом и менее). Если цепь **не** закрыта, проверьте сигнал селектора тормозов двигателя № 3 для провода с открытым контуром при условии, что выключатель был предварительно проверен. См. руководство по устранению неполадок и ремонту OEM для процедур ремонта.

Если сопротивление находится в пределах спецификации, сигнал селектора тормоза двигателя № 3 провод должен быть проверен на короткое замыкание на землю, короткое замыкание от штифта до штифта и короткое замыкание к внешнему источнику напряжения.

После ремонта подсоедините все компоненты.

![[19c01194.png]]

### Проверка на замыкание на массу

Чтобы изолировать цепь тормозов двигателя при проверке на электрическую короткость, поверните все переключатели кабины в положение выключения или нейтральное положение.

![[19200292.png]]

Переместить переключатель уровня тормоза двигателя в положение № 1 для шестипозиционного переключателя или положение № 2 для трехпозиционного переключателя.

Включить испытательный щуп в селектор тормозного сигнала двигателя № 1 штифта разъёма проводов OEM-системы и подключить его к многометровому щупу.

Прикоснитесь к другому многометровому щупу к заземлению блока двигателя.

Переключите тормоз двигателя Включено/Выключено переключение в положение Выключено.

Измерьте сопротивление.

Мультиметр **должен** показать обрыв цепи (100 кОм и более). Если цепь не открыта, в тормозной цепи двигателя есть короткое замыкание, при условии, что переключатель ON/OFF тормоза двигателя и переключатель селектора тормоза двигателя были ранее проверены.

Ремонт или замена провода, подключенного к обратному выключателю или селектору тормозного сигнала двигателя контакт 1 в разъёме проводной упряжки OEM в соответствии с процедурами изготовителя транспортного средства.

Удалите свинец из селектора тормозов двигателя сигнал № 1 и вставьте его в селектор тормозов двигателя сигнал № 2 штифта проводов OEM разъема.

Переместить переключатель уровня тормоза двигателя в положение № 2 для шестипозиционного переключателя или в положение № 1 для трехпозиционного переключателя.

Переключите тормоз двигателя на включение/выключение на выключение.

Измерьте сопротивление.

Мультиметр **должен** показать обрыв цепи (100 кОм и более). Если цепь не открыта, в тормозной цепи двигателя есть короткое замыкание, при условии, что переключатель ON / OFF тормоза двигателя был ранее проверен.

Ремонт или замена провода, подключенного к штифту селектора тормозов двигателя № 2 в проводной упряжке OEM в соответствии с процедурами изготовителя транспортного средства.

![[19c01222.png]]

Удалите свинец из селектора тормозов двигателя сигнал № 2 и вставьте его в селектор тормозов двигателя сигнал № 3 штифта проводов OEM разъема.

Переместить уровень тормоза двигателя в положение № 3.

Переключите тормоз двигателя Включено/Выключено переключение в положение Выключено.

Измерьте сопротивление с помощью мультиметра.

Мультиметр **должен** показать обрыв цепи (100 кОм и более). Если цепь не открыта, в тормозной цепи двигателя есть короткое замыкание, при условии, что переключатель ON / OFF тормоза двигателя был ранее проверен.

Ремонт или замена провода, подключенного к селектору тормозного сигнала двигателя № 3, в электропроводке OEM в соответствии с процедурами производителя транспортного средства.

![[19c01211.png]]

### Проверка на замыкание между контактами

Выделите схему, установив переключатели панели кабины, как описано в предыдущем разделе. Установите переключатель ON/OFF на положение ON. Поместите уровень тормоза двигателя в положение № 6 для шестипозиционного переключателя или положение № 3 для трехпозиционного переключателя.

Включить испытательный щуп в возврат переключателя разъёма проводов OEM и проверить все контакты, кроме возврата переключателя, сигнала селектора тормоза двигателя № 1 и сигнала селектора тормоза двигателя № 3.

Измерьте сопротивление. Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Удалите свинец из возврата переключателя и вставьте его в селектор тормозного сигнала двигателя № 2. Проверьте все штифты, кроме выключателя возвратного двигателя, штифта селектора тормозов № 1 и штифта селектора тормозов двигателя № 3. Измерьте сопротивление.

Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Удалите свинец из селектора тормозов двигателя сигнал № 2 и вставьте его в селектор тормозов двигателя сигнал № 3. Проверьте все контакты, кроме возврата переключателя. Измерьте сопротивление.

Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Удалите свинец из селектора тормозов двигателя сигнал № 3 и инерционно вставьте его в селектор тормозов двигателя сигнал № 1. Проверьте все контакты, кроме возврата переключателя. Измерьте сопротивление.

Мультиметр **должен** показать обрыв цепи (100 кОм и более).

![[19c01155.png]]

### Проверьте короткое замыкание на источнике внешнего напряжения

Переключатель зажигания транспортного средства в положение Включения. Установите переключатель ON/OFF на положение ON.

Настройте мультиметр для измерения VDC.

Включить испытательный щуп в контакт сигнала переключателя разъёма проводов OEM.

Отсоедините многометровый щуп от испытательного щупа и прикоснитесь к нему до основания блока двигателя. Измерьте напряжение. Напряжение должно быть 1.5 VDC или меньше.

Если напряжение **не** правильно, то к цепи подключен внешний источник напряжения или между цепью включения/выключения двигателя и проводом, несущим мощность в электропроводке OEM, имеется короткое замыкание. Удалите источник напряжения или отремонтируйте проводку в OEM-проводах в соответствии с процедурами производителя транспортного средства.

После ремонта подсоедините все компоненты.

![[19c01189.png]]


> [!quote]- Original (English) · английский оригинал
> ### Resistance Check
>
> **CAUTION · Осторожно**
> Proper leads and/or a Cummins® approved circuit testing tool must be used when working with electrical connectors to prevent pin expansion and damage to the connector.
>
> If electronic service tool is available, monitor the engine brake switch circuit for proper operation. If **not**, follow the troubleshooting procedures in this section.
>
> Disconnect the original equipment manufacturer (OEM) harness engine interface connector. To determine the location of the connector, see the corresponding engine wiring diagram.
>
> Insert one of the test leads into the switch return of the OEM harness connector and connect the alligator clip to the multimeter probe. Insert the other lead into engine brake selector signal number 1 of the OEM harness connector and connect the alligator clip to the other multimeter probe.
>
> Move the engine brake ON/OFF switch to the ON position. Move the engine brake level switch to position number 1 for a six-position switch or to position number 2 for a three-position switch. The multimeter **must** show a closed circuit (10 ohms or less). If the circuit is **not** closed, inspect the switch return and engine brake selector signal number 1 for an open circuit, provided that the switch has been previously checked. Refer to the OEM troubleshooting and repair manual for repair procedures. If the resistance is within the specification, the switch return and engine brake selector signal number 1 **must** be checked for a short circuit to ground, a short circuit from pin to pin, and a short circuit to an external voltage source.
>
> Remove the lead from engine brake selector signal number 1 and insert it into engine brake selector signal number 2 of the OEM harness connector.
>
> Move the engine brake ON/OFF switch to the ON position. Move the engine brake level switch to position number 2 for a six-position switch or to position number 1 for a three-position switch.
>
> The multimeter **must** show a closed circuit (10 ohms or less). If the circuit is **not** closed, inspect engine brake selector signal number 2 wire for an open circuit, provided that the switch has been previously checked. Refer to the OEM troubleshooting and repair manual for repair procedures.
>
> If the resistance is within the specification, engine brake selector signal number 2 wire **must** be checked for a short circuit to ground, a short circuit from pin to pin, and a short circuit to an external voltage source.
>
> Remove the lead from engine brake selector signal number 2 and insert it into engine brake selector signal number 3 of the OEM harness.
>
> Move the engine brake ON/OFF switch to the ON position. Move engine brake level switch to position number 3.
>
> The multimeter **must** show a closed circuit (10 ohms or less). If the circuit is **not** closed, inspect the engine brake selector signal number 3 wire for an open circuit, provided that the switch has been previously checked. Refer to the OEM troubleshooting and repair manual for repair procedures.
>
> If the resistance is within the specification, the engine brake selector signal number 3 wire **must** be checked for a short circuit to ground, a short circuit from pin to pin, and a short circuit to an external voltage source.
>
> Connect all components after completing the repair.
>
> ### Check for Short Circuit to Ground
>
> To isolate the engine brake circuit when checking for an electrical short, turn all cab panel switches to the OFF or neutral position.
>
> Move the engine brake level switch to position number 1 for a six-position switch or position number 2 for a three-position switch.
>
> Insert a test lead into engine brake selector signal number 1 pin of the OEM harness connector and connect it to a multimeter probe.
>
> Touch the other multimeter probe to the engine block ground.
>
> Switch the engine brake ON/OFF switch to the OFF position.
>
> Measure the resistance.
>
> The multimeter **must** show an open circuit (100k ohms or more). If the circuit is **not** open, there is a short circuit to ground in the engine brake circuit, provided the engine brake ON/OFF switch and engine brake selector switch have been previously checked.
>
> Repair or replace the wire connected to the switch return or engine brake selector signal number pin 1 in the OEM harness connector according to the vehicle manufacturer's procedures.
>
> Remove the lead from engine brake selector signal number 1 pin and insert it into engine brake selector signal number 2 pin of the OEM harness connector.
>
> Move engine brake level switch to position number 2 for a six-position switch or to position number 1 for a three-position switch.
>
> Switch the engine brake ON/OFF switch to OFF.
>
> Measure the resistance.
>
> The multimeter **must** show an open circuit (100k ohms or more). If the circuit is **not** open, there is a short circuit to ground in the engine brake circuit, provided the engine brake ON/OFF switch has been previously checked.
>
> Repair or replace the wire connected to engine brake selector signal number 2 pin in the OEM harness according to the vehicle manufacturer's procedures.
>
> Remove the lead from engine brake selector signal number 2 pin and insert it into engine brake selector signal number 3 pin of the OEM harness connector.
>
> Move engine brake level switch to position number 3.
>
> Switch the engine brake ON/OFF switch to the OFF position.
>
> Measure the resistance with the multimeter.
>
> The multimeter **must** show an open circuit (100k ohms or more). If the circuit is **not** open, there is a short circuit to ground in the engine brake circuit, provided the engine brake ON/OFF switch has been previously checked.
>
> Repair or replace the wire connected to engine brake selector signal number 3 pin in the OEM harness according to the vehicle manufacturer's procedures.
>
> ### Check for Short Circuit from Pin to Pin
>
> Isolate the circuit by setting the cab panel switches as described in the previous section. Set the engine brake ON/OFF switch to the ON position. Place engine brake level to position number 6 for a six-position switch or position number 3 for a three-position switch.
>
> Insert a test lead into the switch return of the OEM harness connector and check all pins except the switch return, engine brake selector signal number 1 pin, and engine brake selector signal number 3 pin.
>
> Measure the resistance. The multimeter **must** show an open circuit (100k ohms or more).
>
> Remove the lead from the switch return and insert it into engine brake selector signal number 2 pin. Check all pins except the switch return engine, brake selector signal number 1 pin and engine brake selector signal number 3 pin. Measure the resistance.
>
> The multimeter **must** show an open circuit (100k ohms or more).
>
> Remove the lead from engine brake selector signal number 2 pin and insert it into engine brake selector signal number 3 pin. Check all pins except the switch return. Measure the resistance.
>
> The multimeter **must** show an open circuit (100k ohms or more).
>
> Remove the lead from the engine brake selector signal number 3 pin and inert it in the engine brake selector signal number 1 pin. Check all pins except the switch return. Measure the resistance.
>
> The multimeter **must** show an open circuit (100k ohms or more).
>
> ### Check for Short Circuit to External Voltage Source
>
> Turn the vehicle keyswitch to the ON position. Set the engine brake ON/OFF switch to the ON position.
>
> Adjust the multimeter to measure the VDC.
>
> Insert a test lead into the switch signal pin of the OEM harness connector.
>
> Disconnect the multimeter probe from the test lead and touch it to the engine block ground. Measure the voltage. The voltage **must** be 1.5 VDC or less.
>
> If the voltage is **not** correct, there is an external voltage source connected to the circuit, or there is a short circuit between the engine brake on/off circuit and a wire carrying power in the OEM harness. Remove the voltage source or repair the wiring in the OEM harness according to the vehicle manufacturer's procedures.
>
> Connect all components after completing the repair.
