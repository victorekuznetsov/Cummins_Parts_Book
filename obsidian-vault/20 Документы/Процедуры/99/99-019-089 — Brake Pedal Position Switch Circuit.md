---
aliases:
  - "Цепь выключателя положения педали тормоза"
type: "Процедура"
doc: "99-019-089"
title_en: "Brake Pedal Position Switch Circuit"
title_ru: "Цепь выключателя положения педали тормоза"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-089.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/99-019-089.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/99"
  - "перевод/машинный"
---

# Brake Pedal Position Switch Circuit
**Цепь выключателя положения педали тормоза**

> [!abstract] Процедура · `99-019-089`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section 19 - Electronic Engine Controls
> **Даты:** изменён 2015-06-25
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-089.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/99-019-089.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Проверка сопротивления

> [!warning] ОСТОРОЖНО
> Правильные провода и/или одобренный Cummins® инструмент для тестирования цепи должны использоваться при работе с электрическими разъемами для предотвращения расширения штифта и повреждения разъема.

Если имеется электронный инструмент обслуживания, следите за переключателем положения педали тормоза для правильной работы. Если **не**, следуйте процедурам устранения неполадок в этом разделе.

Отключите разъем интерфейса оригинального производителя оборудования (OEM) проводов жгута проводов двигателя. Чтобы определить местоположение разъема, см. соответствующую схему проводов двигателя.

![[19803969.png]]

Убедитесь, что переключатель положения педали тормоза подключен к цепи.

Включить испытательный щуп в контакт сигнала переключателя положения педали тормоза разъёма проводов OEM. Прикрепите свинец к многометровому щупу. Вставьте другой испытательный щуп в переключатель обратного контакта разъёма и прикрепите его к другому щупу.

Настройте мультиметр на установку сопротивления и измерьте сопротивление. Мультиметр **должен** показывать замкнутую цепь (10 Ом или меньше), когда тормоза **не** включены (выпущена педаль тормоза). Если цепь **не** закрыта, возникает проблема с проводкой OEM при условии, что переключатель положения педали тормоза был ранее проверен.

![[19c01262.png]]

> [!warning] ОСТОРОЖНО
> Автомобиль должен иметь достаточное давление воздуха для активации тормозов.

Нажмите на педаль тормоза автомобиля и повторите проверку сопротивления. Мультиметр **должен** показать обрыв цепи (100 кОм и более). Если схема **не** открыта, возникает проблема с проводкой OEM при условии, что переключатель положения педали тормоза был ранее проверен.

Если значения верны, схема **должна*** все еще проверяться на короткое замыкание на землю, короткое замыкание от штифта до штифта и короткое замыкание до внешнего источника напряжения.

![[19c01263.png]]

### Проверка на замыкание на массу

Чтобы изолировать цепь переключателя положения педали тормоза при проверке на короткое замыкание, поверните все переключатели панели кабины в положение выключения или нейтральное положение.

Отсоедините разъём проводов OEM от ECM и проводку OEM от переключателя положения педали тормоза.

Установите рабочий тормоз с помощью ручного клапана прицепа.

Отключите педаль сцепления, переключатель положения ускорителя и выключатель валидации холостого хода.

![[19200292.png]]

Включить испытательный щуп в контакт сигнала переключателя положения педали тормоза разъёма проводов OEM. Подключите свинец к многометровому щупу. Удалите зажим аллигатора из другого многометрового щупа и прикоснитесь к пробе к блоку двигателя.

Мультиметр **должен** показать обрыв цепи (100 кОм и более). Если цепь **не** открыта, в проводе сигнала переключателя положения педали тормоза имеется короткое замыкание для заземления при условии, что переключатель был предварительно проверен.

Ремонт или замена провода, подключенного к контакту сигнала переключения положения педали тормоза в электропроводке OEM в соответствии с процедурами изготовителя транспортного средства.

Измерьте сопротивление.

![[19c01241.png]]

### Проверка на замыкание между контактами

Изолировать цепь переключателя положения педали тормоза путем отсоединения разъема переключателя положения педали тормоза и разъема проводов OEM на ECM. Включить испытательный щуп в контакт сигнала переключателя положения педали тормоза разъёма проводов OEM. Вставьте другой испытательный щуп в обратный контакт переключателя разъёма проводов OEM. Подключите аллигаторы к многометровым зондам. Измерьте сопротивление. Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Удалите свинец из обратного контакта переключателя и протестируйте все другие контакты в разъеме. Мультиметр **должен** показывать открытую схему (100к Ом или более) на всех штифтах. Если цепь **не** открыта, между проводом, подключенным к контакту сигнала переключателя рабочего тормоза, и любым штифтом, который **не** показывает открытую цепь, есть короткое замыкание.

Ремонт или замена проводов в электропроводке OEM в соответствии с процедурами производителя транспортного средства.

![[19c01155.png]]

### Проверьте короткое замыкание на источнике внешнего напряжения

Отсоедините переключатель положения педали тормоза от электропроводки OEM и отсоедините электропроводку OEM от ECM. Переключатель зажигания транспортного средства в положение Включения. Настройте мультиметр для измерения VDC. Вставьте испытательный щуп в контакт сигнала переключателя положения педали тормоза и соедините его с положительным многометровым щупом. Удалите свинец из отрицательного многометрового щупа и прикоснитесь к щупу, чтобы заземлить блок двигателя. Измерьте напряжение. Напряжение должно быть 1.5 VDC или меньше.

> [!note] Примечание
> Внешним источником напряжения является любой провод в OEM-проводах, который несет напряжение.

Если напряжение превышает 1,5 ВДК, то между проводом, подключенным к контакту с сигналом переключателя положения педали тормоза, и проводом, несущим мощность в электропроводке OEM, имеется короткое замыкание. Ремонт проводной упряжки OEM в соответствии с процедурами производителя транспортного средства.

После ремонта подсоедините все компоненты.

![[19c01266.png]]


> [!quote]- Original (English) · английский оригинал
> ### Resistance Check
>
> **CAUTION · Осторожно**
> Proper leads and/or a Cummins® approved circuit testing tool must be used when working with electrical connectors to prevent pin expansion and damage to the connector.
>
> If electronic service tool is available, monitor the brake pedal position switch for proper operation. If **not**, follow the troubleshooting procedures in this section.
>
> Disconnect the original equipment manufacturer (OEM) harness engine interface connector. To determine the location of the connector, see the corresponding engine wiring diagram.
>
> Make sure the brake pedal position switch is connected to the circuit.
>
> Insert a test lead into the brake pedal position switch signal pin of the OEM harness connector. Attach the lead to a multimeter probe. Insert the other test lead into the switch return pin of the connector and attach it to the other probe.
>
> Adjust the multimeter to the resistance setting and measure the resistance. The multimeter **must** show a closed circuit (10 ohms or less) when the brakes are **not** engaged (brake pedal released). If the circuit is **not** closed, there is a problem with the OEM harness, provided the brake pedal position switch has been previously checked.
>
> **CAUTION · Осторожно**
> The vehicle must have enough air pressure to activate the brakes.
>
> Depress the vehicle brake pedal and repeat the resistance check. The multimeter **must** show an open circuit (100k ohms or more). If the circuit is **not** open, there is a problem with the OEM harness, provided the brake pedal position switch has been previously checked.
>
> If the values are correct, the circuit **must** still be checked for a short circuit to ground, a short circuit from pin to pin, and a short circuit to an external voltage source.
>
> ### Check for Short Circuit to Ground
>
> To isolate the brake pedal position switch circuit when checking for a short circuit, turn all cab panel switches to the OFF or neutral position.
>
> Disconnect the OEM harness connector from the ECM and the OEM harness from the brake pedal position switch.
>
> Set the service brake using the trailer brake hand valve.
>
> Disconnect the clutch pedal position switch, accelerator position switch and the idle validation on/off switch.
>
> Insert a test lead into the brake pedal position switch signal pin of the OEM harness connector. Connect the lead to the multimeter probe. Remove the alligator clip from the other multimeter probe and touch the probe to the engine block.
>
> The multimeter **must** show an open circuit (100k ohms or more). If the circuit is **not** open, there is a short circuit to ground in the brake pedal position switch signal wire, provided that the switch has been previously checked.
>
> Repair or replace the wire connected to the brake pedal position switch signal pin in the OEM harness according to the vehicle manufacturer's procedures.
>
> Measure the resistance.
>
> ### Check for Short Circuit from Pin to Pin
>
> Isolate the brake pedal position switch circuit by disconnecting the brake pedal position switch connector and the OEM harness connector at the ECM. Insert a test lead into the brake pedal position switch signal pin of the OEM harness connector. Insert the other test lead into the switch return pin of the OEM harness connector. Connect the alligator clips to the multimeter probes. Measure the resistance. The multimeter **must** show an open circuit (100k ohms or more).
>
> Remove the lead from the switch return pin and test all other pins in the connector. The multimeter **must** show an open circuit (100k ohms or more) at all pins. If the circuit is **not** open, there is a short circuit between the wire connected to the service brake switch signal pin and any pin that did **not** show an open circuit.
>
> Repair or replace the wires in the OEM harness according to the vehicle manufacturer's procedures.
>
> ### Check for Short Circuit to External Voltage Source
>
> Disconnect the brake pedal position switch from the OEM harness and disconnect the OEM harness from the ECM. Turn the vehicle keyswitch to the ON position. Adjust the multimeter to measure VDC. Insert a test lead into the brake pedal position switch signal pin and connect it to the positive multimeter probe. Remove the lead from the negative multimeter probe and touch the probe to the engine block ground. Measure the voltage. The voltage **must** be 1.5 VDC or less.
>
> **Note · Примечание**
> An external voltage source is any wire in the OEM wiring that carries voltage.
>
> If the voltage is more than 1.5 VDC, there is a short circuit between the wire connected to the brake pedal position switch signal pin and a wire carrying power in the OEM harness. Repair the OEM harness according to the vehicle manufacturer's procedures.
>
> Connect all components after completing the repair.
