---
aliases:
  - "Цепь выключателя круиз-контроля или отбора мощности"
type: "Процедура"
doc: "99-019-022"
title_en: "Cruise Control or PTO ON/OFF Switch Circuit"
title_ru: "Цепь выключателя круиз-контроля или отбора мощности"
modified: "2015-06-25"
engines:
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 8
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-022.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/99-019-022.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/99"
  - "перевод/машинный"
---

# Cruise Control or PTO ON/OFF Switch Circuit
**Цепь выключателя круиз-контроля или отбора мощности**

> [!abstract] Процедура · `99-019-022`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section 19 - Electronic Engine Controls
> **Даты:** изменён 2015-06-25
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-022.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/99-019-022.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Проверка сопротивления

> [!warning] ОСТОРОЖНО
> Правильные провода и/или одобренный Cummins® инструмент для тестирования цепи должны использоваться при работе с электрическими разъемами для предотвращения расширения штифта и повреждения разъема.

Если доступно электронное сервисное оборудование, проверьте схему коммутатора для правильной работы. Если **не**, следуйте процедурам устранения неполадок в этом разделе.

![[19803969.png]]

Отключите разъем интерфейса оригинального производителя оборудования (OEM) проводов жгута проводов двигателя. Чтобы определить местоположение разъема, см. соответствующую схему проводов двигателя.

Включить испытательный щуп в контактный сигнал коммутатора круиз-контроля ON/OFF изготовителя оригинального оборудования (OEM) и прикрепить его к многометровому щупу. Прикоснитесь к другому щупу к заземлению блока двигателя.

![[19c01166.png]]

Переместить переключатель ON/OFF в положение ON. Мультиметр **должен** показать замкнутую цепь (10 Ом и менее). Если схема ** не** закрыта, проверьте входной сигнал переключателя круиз-контроля для открытой цепи. См. руководство изготовителя машины по диагностике и ремонту.

Если сопротивление находится в заданных пределах, то входной сигнал переключателя круиз-контроля ON/OFF** должен быть проверен на короткое замыкание на землю, короткое замыкание от терминала к терминалу и короткое замыкание к внешнему источнику напряжения.

![[19c01167.png]]

### Проверка на замыкание на массу

Чтобы изолировать цепь круиз-контроля при проверке на короткое замыкание, отсоедините разъем OEM-проводов от ECM и OEM-проводку от коммутатора круиз-контроля.

Отключите переключатель положения педали сцепления, переключатель валидации холостого хода в/выключенном режиме и переключатель положения педали акселератора. Установите все переключатели кабины в положение OFF или нейтральное.

Установите рабочий тормоз с помощью ручного клапана прицепа.

![[19200292.png]]

Настройте мультиметр для измерения сопротивления. Включить испытательный щуп в входной сигнал круиз-контроля ON/OFF разъёма проводов OEM и прикрепить его к многометровому щупу. Удалите другой многометровый щуп из зажима аллигатора и прикоснитесь к нему до основания блока двигателя.

Измерьте сопротивление.

Мультиметр **должен** показать обрыв цепи (100 кОм и более). Если схема ** не открыта, в схеме круиз-контроля есть короткое замыкание, при условии, что переключатель был ранее проверен.

Ремонт или замена провода, подключенного к входу переключателя круиз-контроля ON/OFF в электропроводке OEM в соответствии с процедурами производителя транспортного средства.

![[19c01166.png]]

### Проверка на замыкание между контактами

Проверьте короткое замыкание от контакта к контакту. Изолируйте схему круиз-контроля, установив переключатели, как в предыдущем разделе. Установите переключение круиз-контроля / PTO ON / OFF на положение OFF. Включить свинец в входной переключатель круиз-контроля ON/OFF. Подключите клип аллигатора к мультиметру. С другой свинец, вставленный в выключатель возвратного провода (проводов), измеряют сопротивление.

Мультиметр **должен** показать обрыв цепи (100 кОм и более).

![[19c01168.png]]

Удалите свинец из входящего в коммутатор круиз-контроля ON/OFF и проверьте все другие контакты. Измерьте сопротивление. Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Если схема **не** открыта, между схемой ввода коммутатора круиз-контроля ON/OFF и любым штифтом, который показывает замкнутую цепь, существует короткое замыкание при условии, что выключатель ранее был проверен.

Ремонт или замена проводов в электропроводке OEM в соответствии с процедурами производителя транспортного средства.

![[19c01155.png]]

### Проверьте короткое замыкание на источнике внешнего напряжения

Переключатель зажигания транспортного средства в положение Включения. Установите переключение круиз-контроля / PTO ON / OFF на ON. Настройте мультиметр для измерения VDC. Вставьте измерительный щуп в входной сигнал круиз-контроля ON/OFF и прикрепите его к многометровому щупу. Отсоедините другой многометровый щуп от другого свинца и прикоснитесь к нему к заземлению блока двигателя. Измерьте напряжение. Напряжение ** должно быть 1.5 VDC или меньше.

Если напряжение ** не** правильно, то к цепи подключен внешний источник напряжения или между коммутаторной схемой круиз-контроля / PTO ON / OFF и проводом, несущим мощность в электропроводке OEM, есть короткое замыкание. Удалите источник напряжения или отремонтируйте проводку в OEM-проводах в соответствии с процедурами производителя транспортного средства. После ремонта подсоедините все компоненты.

> [!note] Примечание
> Если схема коммутатора круиз-контроля/PTO ON/OFF была одобрена во всех предыдущих испытаниях, она функционирует правильно.

![[19c01169.png]]


> [!quote]- Original (English) · английский оригинал
> ### Resistance Check
>
> **CAUTION · Осторожно**
> Proper leads and/or a Cummins® approved circuit testing tool must be used when working with electrical connectors to prevent pin expansion and damage to the connector.
>
> If electronic service tool is available, monitor the switch circuit for proper operation. If **not**, follow the troubleshooting procedures in this section.
>
> Disconnect the original equipment manufacturer (OEM) harness engine interface connector. To determine the location of the connector, see the corresponding engine wiring diagram.
>
> Insert the test lead into the cruise control ON/OFF switch signal pin of the original equipment manufacturer (OEM) harness connector and attach it to the multimeter probe. Touch the other probe to the engine block ground.
>
> Move the ON/OFF switch to the ON position. The multimeter **must** show a closed circuit (10 ohms or less). If the circuit is **not** closed, inspect the cruise control ON/OFF switch input for an open circuit. Refer to the OEM troubleshooting and repair manual.
>
> If the resistance is within specification, the cruise control ON/OFF switch input **must** be checked for a short circuit to ground, a short circuit from terminal to terminal, and a short circuit to an external voltage source.
>
> ### Check for Short Circuit to Ground
>
> To isolate the cruise control circuit when checking for a short circuit, disconnect the OEM harness connector from the ECM and the OEM harness from the cruise control switch.
>
> Disconnect the clutch pedal position switch, idle validation on/off switch, and the accelerator pedal position switch. Set all cab panel switches to the OFF or neutral position.
>
> Set the service brake using the trailer brake hand valve.
>
> Adjust the multimeter to measure resistance. Insert a test lead into the cruise control ON/OFF switch input of the OEM harness connector and attach it to a multimeter probe. Remove the other multimeter probe from the alligator clip and touch it to the engine block ground.
>
> Measure the resistance.
>
> The multimeter **must** show an open circuit (100k ohms or more). If the circuit is **not** open, there is a short circuit to ground in the cruise control circuit, provided that the switch has been previously checked.
>
> Repair or replace the wire connected to the cruise control ON/OFF switch input in the OEM harness according to the vehicle manufacturer's procedures.
>
> ### Check for Short Circuit from Pin to Pin
>
> Check for a short circuit from pin-to-pin. Isolate the cruise control circuit by setting the switches as in the previous section. Set the cruise control/PTO ON/OFF switch to the OFF position. Insert the lead into the cruise control ON/OFF switch input. Connect the alligator clip to the multimeter. With the other lead inserted into the switch return wire(s), measure the resistance.
>
> The multimeter **must** show an open circuit (100k ohms or more).
>
> Remove the lead from the cruise control ON/OFF switch input and check all other pins. Measure the resistance. The multimeter **must** show an open circuit (100k ohms or more).
>
> If the circuit is **not** open, there is a short circuit between the cruise control ON/OFF switch input circuit and any pin that shows a closed circuit, provided the switch has previously been checked.
>
> Repair or replace the wires in the OEM harness according to the vehicle manufacturer's procedures.
>
> ### Check for Short Circuit to External Voltage Source
>
> Turn the vehicle keyswitch to the ON position. Set the cruise control/PTO ON/OFF switch to ON. Adjust the multimeter to measure VDC. Insert a test lead into the cruise control ON/OFF switch input and attach it to a multimeter probe. Disconnect the other multimeter probe from the other lead and touch it to the engine block ground. Measure the voltage. The voltage **must** be 1.5 VDC or less.
>
> If the voltage is **not** correct, there is an external voltage source connected to the circuit, or there is a short circuit between the cruise control/PTO ON/OFF switch circuit and a wire carrying power in the OEM harness. Remove the voltage source or repair the wiring in the OEM harness according to the vehicle manufacturer's procedures. Connect all components after completing the repair.
>
> **Note · Примечание**
> If the cruise control/PTO ON/OFF switch circuit was approved in all of the previous tests, it is functioning correctly.
