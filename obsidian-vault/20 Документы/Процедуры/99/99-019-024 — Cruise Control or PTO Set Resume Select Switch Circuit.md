---
aliases:
  - "Цепь выключателя круиз-контроля или отбора мощности (Set/Resume)"
type: "Процедура"
doc: "99-019-024"
title_en: "Cruise Control or PTO Set/Resume Select Switch Circuit"
title_ru: "Цепь выключателя круиз-контроля или отбора мощности (Set/Resume)"
modified: "2015-06-25"
engines:
  - "41343322"
  - "41370103"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 10
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-024.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/99-019-024.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/99"
  - "перевод/машинный"
---

# Cruise Control or PTO Set/Resume Select Switch Circuit
**Цепь выключателя круиз-контроля или отбора мощности (Set/Resume)**

> [!abstract] Процедура · `99-019-024`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section 19 - Electronic Engine Controls
> **Даты:** изменён 2015-06-25
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-024.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/99-019-024.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

В дополнение к функциям круиз-контроля, коммутатор выбора круиз-контроля также предусматривает увеличение / уменьшение скорости простоя, скорости PTO, вспышки кода неисправности и ограничения скорости движения.

![[19200292.png]]

### Проверка сопротивления

> [!warning] ОСТОРОЖНО
> Правильные провода и/или одобренный Cummins® инструмент для тестирования цепи должны использоваться при работе с электрическими разъемами для предотвращения расширения штифта и повреждения разъема.

Если доступно электронное оборудование для обслуживания, проверьте схему коммутатора круиз-контроля / PTO set / resume select для правильной работы. Если **не**, следуйте процедурам устранения неполадок в этом разделе.

![[19803969.png]]

Отключите разъем интерфейса оригинального производителя оборудования (OEM) проводов жгута проводов двигателя. Чтобы определить местоположение разъема, см. соответствующую схему проводов двигателя.

Включить испытательный щуп в сигнал круиз-контроля/PTO set/coast переключателя разъёма проводов OEM и подключить зажим аллигатора к многометровому щупу.

Прикоснитесь к другому щупу, чтобы заземлить двигатель.

![[19c01182.png]]

Держите переключатель круиз-контроля в положении SET/COAST. Мультиметр **должен** показывать замкнутую цепь (10 Ом или менее) при удерживании переключателя в положении SET/COAST и возвращаться к открытой цепи (100 К Ом или более), когда переключатель выпущен. Схема **должна **оставаться открытой схемой (100к Ом или более), когда переключатель находится в положении RESUME/ACCEL.

Если значения сопротивления **не** верны, убедитесь, что входные данные круиз-контроля/PTO-набора/побережья и провода ввода круиз-контроля/PTO-резюме/ускорения правильно установлены на выключателе круиз-контроля. Если оба провода управления правильно установлены, проверьте ввод в систему круиз-контроля / PTO/ побережье и провода круиз-контроля / PTO резюме / ускорения для открытой цепи при условии, что выключатель выбора круиз-контроля был ранее проверен.

![[19c01183.png]]

Удалите свинец из сигнала круиз-контроля / PTO set / Coast switch и вставьте его в сигнал круиз-контроля / PTO resume /accel switch.

![[19c01184.png]]

Держите переключатель выбора круиз-контроля в положении RESUME / ACCEL. Мультиметр **должен** показывать замкнутую цепь (10 Ом или меньше), когда переключатель находится в положении RESUME/ACCEL, и открытую цепь (100 К Ом или более), когда переключатель высвобождается.

Схема **должна** оставаться открытой схемой (100к Ом или более), когда переключатель удерживается в положении SET/COAST.

![[19c01185.png]]

Если значения сопротивления **не** верны, убедитесь, что провод круиз-контроля / PTO resume /accel правильно установлен на выключателе круиз-контроля. Если провод круиз-контроля/PTO resume/accel установлен на коммутаторе выбора круиз-контроля, проверьте сигнал круиз-контроля/PTO resume/accel для открытой цепи при условии, что коммутатор выбора круиз-контроля был ранее проверен.

Если значения сопротивления верны в предыдущих проверках, круиз-контроль / PTO-набор / погрузочный сигнал и круиз-контроль / PTO-резюме / сигнал ускорения должны быть все еще проверены на короткое замыкание на землю, короткое замыкание от штифта до штифта и короткое замыкание к внешнему источнику напряжения.

![[19c01185.png]]

### Проверка на замыкание между контактами

Изолируйте схему коммутатора круиз-контроля/PTO set/resume select, как описано в предыдущем разделе. Включить испытательный щуп в систему круиз-контроля/PTO set/coast switch signal contact разъёма проводной ремни OEM. Вставьте другой свинец в первый штифт в разъеме. Подключите аллигаторы к многометровым зондам. Измерьте сопротивление.

Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Удалите свинец из первого штифта в разъеме и проверьте все остальные штифты. Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Если схема **не** открыта, то имеется короткое замыкание от провода, подключенного к контакту сигнала круиз-контроля/PTO-набора/поперечного переключателя и любого штифта, который измеряется менее 100k Ом.

Ремонт или замена проводов в OEM проводах.[[99-019-071 — OEM Wiring Harness|См. процедуру 019-071]].

Удалите свинец из контакта с сигналом круиз-контроля / PTO set / Coast и вставьте его в контакт с сигналом круиз-контроля / PTO resume /accel switch. Вставьте другой свинец в первый штифт в разъеме.

Измерьте сопротивление. Мультиметр **должен** показать обрыв цепи (100 кОм и более).

![[19c01186.png]]

Удалите свинец из первого штифта в разъеме и измерьте сопротивление всем другим штифтам. Мультиметр **должен** показать обрыв цепи (100 кОм и более). Если схема **не** открыта, между проводом, подключенным к контакту с сигналом круиз-контроля/PTO-резюме/ускорителя, и любым штифтом, который измеряется менее 100k Ом, есть короткое замыкание.

Ремонт или замена проводов в OEM проводах.[[99-019-071 — OEM Wiring Harness|См. процедуру 019-071]].

![[19c01187.png]]

### Проверьте короткое замыкание на источнике внешнего напряжения

Изолируйте схему коммутатора круиз-контроля / PTO resume /accel, как описано в предыдущем разделе. Переключатель зажигания транспортного средства в положение Включения. Настройте мультиметр для измерения VDC. Включить испытательный щуп в сигнал круиз-контроля/PTO resume/accel switch разъема проводов OEM. Подключите зажим аллигатора испытательного щупа к положительному (+) многометровому щупу. Прикоснитесь к отрицательному (-) многометровому щупу к заземлению блока двигателя и измерьте напряжение. Мультиметр **must** показывает менее 1,5 VDC.

Если значение напряжения **не** правильно, в электропроводке OEM имеется короткое замыкание внешнего источника напряжения к сигналу круиз-контроля / PTO-набора / поперечного переключателя. Удалите источник напряжения. Ремонт или замена провода в OEM проводах.[[99-019-071 — OEM Wiring Harness|См. процедуру 019-071]].

Удалите свинец из штифта ввода круиз-контроля / PTO set / Coast switch и вставьте его в штифт ввода круиз-контроля / PTO resume / Acccel switch. Прикоснитесь к отрицательному многометровому щупу, чтобы блокировать землю двигателя и измерить напряжение. Мультиметр **must** показывает менее 1,5 VDC.

Если значение напряжения **не** правильно, в штыре проводов OEM имеется короткое замыкание внешнего источника напряжения на входной штифт круиз-контроля / PTO resume /accel switch. Удалите источник напряжения. Ремонт или замена провода в OEM проводах.[[99-019-071 — OEM Wiring Harness|См. процедуру 019-071]].

После ремонта подсоедините все компоненты.

![[19c01189.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> In addition to cruise control functions, the cruise control select switch also provides for increasing/decreasing idle speed, PTO speed, fault code flashout, and road speed governor limit.
>
> ### Resistance Check
>
> **CAUTION · Осторожно**
> Proper leads and/or a Cummins® approved circuit testing tool must be used when working with electrical connectors to prevent pin expansion and damage to the connector.
>
> If electronic service tool is available, monitor the cruise control/PTO set/resume select switch circuit for proper operation. If **not**, follow the troubleshooting procedures in this section.
>
> Disconnect the original equipment manufacturer (OEM) harness engine interface connector. To determine the location of the connector, see the corresponding engine wiring diagram.
>
> Insert a test lead into the cruise control/PTO set/coast switch signal of the OEM harness connector and connect the alligator clip to the multimeter probe.
>
> Touch the other probe to engine block ground.
>
> Hold the cruise control select switch in the SET/COAST position. The multimeter **must** show a closed circuit (10 ohms or less) while holding the switch in the SET/COAST position and return to an open circuit (100k ohms or more) when the switch is released. The circuit **must** remain an open circuit (100k ohms or more) when the switch is in the RESUME/ACCEL position.
>
> If the resistance values are **not** correct, make sure the cruise control/PTO set/coast input and the cruise control/PTO resume/accel input wires are properly installed on the cruise control select switch. If both control wires are correctly installed, inspect the cruise control/PTO set/coast input and the cruise control/PTO resume/accel wires for an open circuit, provided the cruise control select switch has been previously checked.
>
> Remove the lead from the cruise control/PTO set/coast switch signal and insert it into the cruise control/PTO resume/accel switch signal.
>
> Hold the cruise control select switch in the RESUME/ACCEL position. The multimeter **must** show a closed circuit (10 ohms or less) when the switch is in the RESUME/ACCEL position and an open circuit (100k ohms or more) when the switch is released.
>
> The circuit **must** remain an open circuit (100k ohms or more) when the switch is held in the SET/COAST position.
>
> If the resistance values are **not** correct, make sure the cruise control/PTO resume/accel wire is properly installed on the cruise control select switch. If the cruise control/PTO resume/accel wire is properly installed on the cruise control select switch, inspect the cruise control/PTO resume/accel signal for an open circuit, provided the cruise control select switch has been previously checked.
>
> If the resistance values are correct in the previous checks, the cruise control/PTO set/coast signal and cruise control/PTO resume/accel signal **must** still be checked for a short circuit to ground, a short circuit from pin to pin, and a short circuit to an external voltage source.
>
> ### Check for Short Circuit from Pin to Pin
>
> Isolate the cruise control/PTO set/resume select switch circuit as described in the previous section. Insert a test lead into the cruise control/PTO set/coast switch signal pin of the OEM harness connector. Insert the other lead into the first pin in the connector. Connect the alligator clips to the multimeter probes. Measure the resistance.
>
> The multimeter **must** show an open circuit (100k ohms or more).
>
> Remove the lead from the first pin in the connector and check all other pins. The multimeter **must** show an open circuit (100k ohms or more).
>
> If the circuit is **not** open, there is a short circuit from the wire connected to the cruise control/PTO set/coast switch signal pin and any pin that measured less than 100k ohms.
>
> Repair or replace the wires in the OEM harness. [[99-019-071 — OEM Wiring Harness|Refer to Procedure 019-071]].
>
> Remove the lead from the cruise control/PTO set/coast signal pin and insert it into the cruise control/PTO resume/accel switch signal pin. Insert the other lead into the first pin in the connector.
>
> Measure the resistance. The multimeter **must** show an open circuit (100k ohms or more).
>
> Remove the lead from the first pin in the connector and measure the resistance to all other pins. The multimeter **must** show an open circuit (100k ohms or more). If the circuit is **not** open, there is a short circuit between the wire connected to the cruise control/PTO resume/accel switch signal pin and any pin that measured less than 100k ohms.
>
> Repair or replace the wires in the OEM harness. [[99-019-071 — OEM Wiring Harness|Refer to Procedure 019-071]].
>
> ### Check for Short Circuit to External Voltage Source
>
> Isolate the cruise control/PTO resume/accel switch circuit as described in the previous section. Turn the vehicle keyswitch to the ON position. Adjust the multimeter to measure VDC. Insert a test lead into the cruise control/PTO resume/accel switch signal of the OEM harness connector. Connect the test lead alligator clip to the positive (+) multimeter probe. Touch the negative (-) multimeter probe to the engine block ground and measure the voltage. The multimeter **must** show less than 1.5 VDC.
>
> If the voltage value is **not** correct, there is an external voltage source short circuit to the cruise control/PTO set/coast switch signal in the OEM harness. Remove the voltage source. Repair or replace the wire in the OEM harness. [[99-019-071 — OEM Wiring Harness|Refer to Procedure 019-071]].
>
> Remove the lead from the cruise control/PTO set/coast switch input pin and insert it into the cruise control/PTO resume/accel switch input pin. Touch the negative multimeter probe to the engine block ground and measure the voltage. The multimeter **must** show less than 1.5 VDC.
>
> If the voltage value is **not** correct, there is an external voltage source short circuit to the cruise control/PTO resume/accel switch input pin in the OEM harness. Remove the voltage source. Repair or replace the wire in the OEM harness. [[99-019-071 — OEM Wiring Harness|Refer to Procedure 019-071]].
>
> Connect all components after completing the repair.
