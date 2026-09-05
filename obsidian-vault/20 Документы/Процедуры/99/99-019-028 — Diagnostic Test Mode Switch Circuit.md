---
aliases:
  - "Цепь переключателя режима диагностики"
type: "Процедура"
doc: "99-019-028"
title_en: "Diagnostic Test Mode Switch Circuit"
title_ru: "Цепь переключателя режима диагностики"
modified: "2015-06-25"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
  - "37269910"
  - "37280605"
  - "37292556"
  - "37295879"
  - "41343322"
  - "41370103"
  - "85017333"
  - "93058669"
  - "93087701"
families:
  - "C8.3 · 6C8.3"
  - "K19"
  - "NT/NTA855 · ISM/QSM11"
  - "QSK23"
  - "QSK60"
  - "QST30"
manuals:
  - "3666070"
  - "3666113"
  - "3666214"
  - "3666266"
  - "4021419"
  - "4021442"
  - "4021674"
figures: 7
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-028.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/99-019-028.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "двигатель/K19"
  - "двигатель/NT/NTA855"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "двигатель/QST30"
  - "группа/99"
  - "перевод/машинный"
---

# Diagnostic Test Mode Switch Circuit
**Цепь переключателя режима диагностики**

> [!abstract] Процедура · `99-019-028`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]], [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]], [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]], [[85017333 — QSK23 CM500 CPL 2858|85017333]], [[93058669 — 6C8.3 CPL 3105|93058669]], [[93087701 — 6C8.3 CPL 3105|93087701]]
> **Семейство:** C8.3 · 6C8.3, K19, NT/NTA855 · ISM/QSM11, QSK23, QSK60, QST30
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]], [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]], [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]], [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]], [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]], [[4021442 — C8.3 Marine Electronic Control System Troubleshooting and Repair Manual|4021442]], [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section 19 - Electronic Engine Controls · Section 19 - Electronic Engine Controls - Group 19 · Section 19 — Electronic Engine Controls — Group 19
> **Даты:** изменён 2015-06-25
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-028.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/99-019-028.pdf)

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

Отключите разъем интерфейса оригинального производителя оборудования (OEM) проводов жгута проводов двигателя. Чтобы определить местоположение разъема, см. соответствующую схему проводов двигателя. Вставьте измерительный щуп в диагностический режим испытания переключателя сигнала контакта в разъеме проводов OEM-проводов и соедините его с многометровым щупом.

Прикоснитесь к другому щупу к блоку двигателя или земле шасси.

Переместить переключатель ON/OFF в положение ON.

Если OEM-привод переключателя возвращается на землю шасси, мультиметр **должен **показать замкнутую цепь (10 Ом или меньше). Если схема **не** закрыта, проверьте провод сигнала переключателя режима диагностического испытания на открытую схему.

Если OEM проводной переключатель возвращается к OEM проводной проводной ремне, мультиметр **должен **показать открытую схему (100k Ом или более). Если схема **не** открыта, проверьте провод сигнала переключателя режима диагностического испытания на замкнутую схему.

См. руководство изготовителя машины по диагностике и ремонту.

Если сопротивление находится в заданных пределах, то провод сигнала переключателя в режиме диагностического испытания должен быть проверен на короткое замыкание на землю, короткое замыкание от терминала к терминалу и короткое замыкание к внешнему источнику напряжения.

![[19c01167.png]]

### Проверка на замыкание на массу

Чтобы изолировать схему сигнала переключателя диагностического режима при проверке на электрическую короткость, поверните все переключатели кабины в положение выключения или нейтральное положение.

Установите рабочий тормоз с помощью ручного клапана прицепа.

Отключите переключатель положения педали сцепления.

Отключите выключатель проверки бездействия.

> [!note] Примечание
> Некоторые устройства могут варьироваться в зависимости от применения OEM.

![[ee8swsb.png]]

Отсоедините разъем OEM-проводов от электронного блока управления. Установить режим диагностического тестирования переключателем в положение OFF.

Включить один из измерительных щупов в диагностический измерительный режим переключения сигнала контакта разъема проводов OEM-проводов и подключить его к многометровому щупу.

Прикоснитесь к другому щупу к блоку двигателя или земле шасси.

Мультиметр **должен** показать обрыв цепи (100 кОм и более).

![[19c01211.png]]

### Проверка на замыкание между контактами

Проверьте короткое замыкание от контакта к контакту. Выделите схему переключателя, установив переключатели панели кабины, как описано в предыдущем разделе. Установить режим диагностического тестирования переключателем в положение OFF. Вставьте измерительный щуп в переключатель обратного контакта разъёма проводов OEM-системы и соедините его с многометровым щупом. С другим свинцом, вставленным в режим диагностического испытания переключателем сигнала контакта разъема, измеряют сопротивление. Мультиметр **должен** показать обрыв цепи (100 кОм и более).

![[19c01168.png]]

Удалите свинец из возврата переключателя и протестируйте все контакты в разъеме. Измерьте сопротивление. Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Если схема **не** открыта, между схемой переключателя и любым штифтом, который показывает замкнутую цепь, существует короткое замыкание при условии, что переключатель ранее был проверен. Ремонт или замена проводов в OEM проводах.[[99-019-071 — OEM Wiring Harness|См. процедуру 019-071]].

![[19c01215.png]]

### Проверьте короткое замыкание на источнике внешнего напряжения

Переключатель зажигания транспортного средства в положение Включения. Установите режим диагностического теста на включение. Настройте мультиметр для измерения VDC. Включить измерительный щуп в диагностический режим испытания переключателя сигнала контакта разъёма проводов OEM-приемника. Прикоснитесь к другому приводу к блоку двигателя или земле шасси. Измерьте напряжение. Напряжение должно быть 1.5 VDC или меньше.

Если напряжение **не** правильно, то к цепи подключен внешний источник напряжения или между коммутационной цепью и проводом, несущим мощность в электропроводке OEM, имеется короткое замыкание. Удалите источник напряжения или отремонтируйте проводку в OEM-проводах.[[99-019-071 — OEM Wiring Harness|См. процедуру 019-071]].

После ремонта подсоедините все компоненты.

![[19c01216.png]]


> [!quote]- Original (English) · английский оригинал
> ### Resistance Check
>
> **CAUTION · Осторожно**
> Proper leads and/or a Cummins® approved circuit testing tool must be used when working with electrical connectors to prevent pin expansion and damage to the connector.
>
> If electronic service tool is available, monitor the switch circuit for proper operation. If **not**, follow the troubleshooting procedures in this section.
>
> Disconnect the original equipment manufacturer (OEM) harness engine interface connector. To determine the location of the connector, see the corresponding engine wiring diagram. Insert the test lead into the diagnostic test mode switch signal pin in the OEM harness connector and connect it to the multimeter probe.
>
> Touch the other probe to the engine block or chassis ground.
>
> Move the ON/OFF switch to the ON position.
>
> If the OEM wired the switch return to chassis ground, the multimeter **must** show a closed circuit (10 ohms or less). If the circuit is **not** closed, inspect the diagnostic test mode switch signal wire for an open circuit.
>
> If the OEM wired the switch return to the OEM wire harness, the multimeter **must** show an open circuit (100k ohms or more). If the circuit is **not** open, inspect the diagnostic test mode switch signal wire for a closed circuit.
>
> Refer to the OEM troubleshooting and repair manual.
>
> If the resistance is within specification, the diagnostic test mode switch signal wire **must** be checked for a short circuit to ground, a short circuit from terminal to terminal, and a short circuit to an external voltage source.
>
> ### Check for Short Circuit to Ground
>
> To isolate the diagnostic test mode switch signal circuit when checking for an electrical short, turn all cab panel switches to the OFF or neutral position.
>
> Set the service brake using the trailer brake hand valve.
>
> Disconnect the clutch pedal position switch.
>
> Disconnect the idle validation switch.
>
> **Note · Примечание**
> Some equipment may vary, depending on OEM application.
>
> Disconnect the OEM harness connector from the electronic control unit. Set the diagnostic test mode switch to the OFF position.
>
> Insert one of the test leads into the diagnostic test mode switch signal pin of the OEM harness connector and connect it to a multimeter probe.
>
> Touch the other probe to engine block or chassis ground.
>
> The multimeter **must** show an open circuit (100k ohms or more).
>
> ### Check for Short Circuit from Pin to Pin
>
> Check for a short circuit from pin-to-pin. Isolate the switch circuit by setting the cab panel switches as described in the previous section. Set the diagnostic test mode switch to the OFF position. Insert a test lead into the switch return pin of the OEM harness connector and connect it to the multimeter probe. With the other lead inserted into the diagnostic test mode switch signal pin of the connector, measure the resistance. The multimeter **must** show an open circuit (100k ohms or more).
>
> Remove the lead from the switch return and test all pins in the connector. Measure the resistance. The multimeter **must** show an open circuit (100k ohms or more).
>
> If the circuit is **not** open, there is a short circuit between the switch circuit and any pin that shows a closed circuit, provided the switch has previously been checked. Repair or replace the wires in the OEM harness. [[99-019-071 — OEM Wiring Harness|Refer to Procedure 019-071]].
>
> ### Check for Short Circuit to External Voltage Source
>
> Turn the vehicle keyswitch to the ON position. Set the diagnostic test mode switch to ON. Adjust the multimeter to measure VDC. Insert a test lead into the diagnostic test mode switch signal pin of the OEM harness connector. Touch the other lead to the engine block or chassis ground. Measure the voltage. The voltage **must** be 1.5 VDC or less.
>
> If the voltage is **not** correct, there is an external voltage source connected to the circuit or there is a short circuit between the switch circuit and a wire carrying power in the OEM harness. Remove the voltage source or repair the wiring in the OEM harness. [[99-019-071 — OEM Wiring Harness|Refer to Procedure 019-071]].
>
> Connect all components after completing the repair.
