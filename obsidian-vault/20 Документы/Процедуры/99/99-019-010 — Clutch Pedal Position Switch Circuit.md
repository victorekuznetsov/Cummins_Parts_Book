---
aliases:
  - "Цепь выключателя положения педали сцепления"
type: "Процедура"
doc: "99-019-010"
title_en: "Clutch Pedal Position Switch Circuit"
title_ru: "Цепь выключателя положения педали сцепления"
modified: "2015-06-22"
engines:
  - "41343322"
  - "41370103"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 8
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-010.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/99-019-010.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/99"
  - "перевод/машинный"
---

# Clutch Pedal Position Switch Circuit
**Цепь выключателя положения педали сцепления**

> [!abstract] Процедура · `99-019-010`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section 19 - Electronic Engine Controls
> **Даты:** изменён 2015-06-22
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-010.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/99-019-010.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Проверка сопротивления

> [!warning] ОСТОРОЖНО
> Правильные провода и/или одобренный Cummins® инструмент для тестирования цепи должны использоваться при работе с электрическими разъемами для предотвращения расширения штифта и повреждения разъема.

Если доступна электронная сервисная оснастка, проверьте схему переключения положения педали сцепления для правильной работы. Если **не**, следуйте процедурам устранения неполадок в этом разделе.

Отключите разъем интерфейса оригинального производителя оборудования (OEM) проводов жгута проводов двигателя. Чтобы определить местоположение разъема, см. соответствующую схему проводов двигателя.

Включить испытательный щуп в педаль сцепления переключателя положения обратного контакта в зависимости от OEM-приложения разъема OEM. Включить другой испытательный щуп в контакт сигнала переключения положения педали сцепления разъёма OEM.

![[19803969.png]]

Подключите аллигаторы к двум зондам мультиметра. Настройте мультиметр для измерения сопротивления.

Мультиметр **должен** показывать замкнутую цепь (10 Ом или меньше), когда педаль сцепления (1) выпущена.

![[19c01151.png]]

Ударить педалью сцепления (1). Мультиметр **должен** показать обрыв цепи (100 кОм и более). Если значения сопротивления **не** верны, то сигнальный провод переключателя положения сцепления и обратный провод * должны быть проверены на наличие открытой цепи при условии, что переключатель положения педали сцепления был предварительно проверен.

Если значения верны, схема **должна*** все еще проверяться на короткое замыкание на землю, короткое замыкание от штифта до штифта и короткое замыкание до внешнего источника напряжения.

![[19c01152.png]]

### Проверка на замыкание на массу

Чтобы изолировать цепь переключателя положения педали сцепления при проверке короткого замыкания на землю, поверните все переключатели панели кабины в положение выключения или нейтральное положение.

Установите рабочий тормоз с помощью ручного клапана прицепа.

Отсоедините педаль сцепления с переключателем положения, переключателем проверки бездействия и педалью дроссельной заслонки.

![[ee8swsb.png]]

Удалите измерительный щуп от обратного контакта переключателя.

Отсоедините многометровый щуп от клипа аллигатора.

![[19c01153.png]]

Прикоснитесь к другому многометровому щупу к заземлению блока двигателя. Измерьте сопротивление. Мультиметр **должен** показать обрыв цепи (100 кОм и более). Если схема **не** открыта, в схеме переключателя положения педали сцепления есть короткое замыкание для заземления.

Ремонт или замена провода, подключенного к контакту с переключателем положения педали сцепления в проводной упряжке OEM в соответствии с процедурами производителя транспортного средства.

Подключите все компоненты, когда ремонт будет завершен.

![[19c01154.png]]

### Проверка на замыкание между контактами

Изолируйте цепь переключателя положения педали сцепления, как описано на предыдущем этапе. Установите все переключатели кабины в положение OFF или нейтральное положение и отсоедините переключатель положения педали сцепления и педаль дроссельной заслонки.

Настройте мультиметр для измерения сопротивления. Затем вставьте один испытательный щуп в контакт сигнала переключения положения педали сцепления разъёма проводов OEM-подключателя. Вставьте другой испытательный щуп в педаль сцепления, положение переключателя обратного контакта. Подключите аллигаторы к многометровым зондам.

Измерьте сопротивление. Мультиметр **должен** показать обрыв цепи (100 кОм и более).

При первом испытательном щупе, все еще касающемся контакта с переключателем положения педали сцепления, удалите испытательный щуп из переключателя положения педали сцепления и коснитесь его всех других контактов, по одному за раз. Мультиметр **должен** показывать открытую схему (100к Ом или более) на всех штифтах.

Если схема **не** открыта, между проводом, подключенным к контакту с переключателем положения педали сцепления, и любым штифтом, который показывает замкнутую цепь, есть короткое замыкание. Ремонт или замена проводов в электропроводке OEM в соответствии с процедурами производителя транспортного средства.

Удалите пробный щуп из контакта с переключателем положения сцепления и прикоснитесь к нему, чтобы вернуть контакт с переключателем положения сцепления. Прикоснитесь к другому испытательному щупу со всеми другими штифтами, по одному за раз. Измерьте сопротивление. Мультиметр **должен** показывать открытую схему (100км и более), за исключением обратного контакта с переключателем положения педали сцепления.

Если цепь **не** открыта, между проводом, подключенным к проводу обратного переключателя положения сцепления, и любым штифтом, который измерял замкнутую цепь, есть короткое замыкание. Ремонт или замена проводов в электропроводке OEM в соответствии с процедурами производителя транспортного средства.

![[19c01155.png]]

### Проверьте короткое замыкание на источнике внешнего напряжения

Изолируйте цепь переключателя положения педали сцепления, как описано на предыдущих шагах. Установите переключатели панели кабины в положение OFF или нейтральное положение и отсоедините переключатель положения педали сцепления и педаль дроссельной заслонки. Переведите замок зажигания в положение ON. Настройте мультиметр для измерения VDC.

Включить испытательный щуп, соединенный с положительным многометровым щупом, в контакт с переключателем педалей сцепления. Отсоедините отрицательный многометровый щуп от испытательного щупа и прикоснитесь к нему до основания блока двигателя. Измерьте напряжение. Напряжение должно быть 1.5 VDC или меньше.

> [!note] Примечание
> Внешним источником напряжения является любой провод в OEM-проводах, который несет напряжение.

Если значение напряжения превышает 1,5 ВДК, то между проводом, подключенным к контакту с переключателем положения педали сцепления, и проводом, несущим мощность в электропроводке OEM, имеется короткое замыкание. Ремонт проводной упряжки OEM в соответствии с процедурами производителя транспортного средства.

Удалите пробный щуп из контакта с переключателем положения сцепления и вставьте его в обратный контакт переключателя положения сцепления. С помощью многометрового щупа, все еще касающегося земли блока двигателя, измерьте напряжение. Напряжение **должно быть 1.5 VDC или меньше. Если значение напряжения **не правильно, между проводом, подключенным к возврату педалей сцепления, и проводом, несущим мощность в электропроводке OEM, есть короткое замыкание. Ремонт проводной упряжки OEM в соответствии с процедурами производителя транспортного средства.

Подключите все компоненты после завершения ремонта.

![[19c01158.png]]


> [!quote]- Original (English) · английский оригинал
> ### Resistance Check
>
> **CAUTION · Осторожно**
> Proper leads and/or a Cummins® approved circuit testing tool must be used when working with electrical connectors to prevent pin expansion and damage to the connector.
>
> If electronic service tool is available, monitor the clutch pedal position switch circuit for proper operation. If **not**, follow the troubleshooting procedures in this section.
>
> Disconnect the original equipment manufacturer (OEM) harness engine interface connector. To determine the location of the connector, see the corresponding engine wiring diagram.
>
> Insert a test lead into the clutch pedal position switch return pin depending on the OEM application of the OEM connector. Insert the other test lead into the clutch pedal position switch signal pin of the OEM connector.
>
> Connect the alligator clips to the two probes of the multimeter. Adjust the multimeter to measure resistance.
>
> The multimeter **must** show a closed circuit (10 ohms or less) when the clutch pedal (1) is released.
>
> Depress the clutch pedal (1). The multimeter **must** show an open circuit (100k ohms or more). If the resistance values are **not** correct, the clutch pedal position switch signal wire and the return wire **must** be checked for an open circuit, provided the clutch pedal position switch was previously checked.
>
> If the values are correct, the circuit **must** still be checked for a short circuit to ground, a short circuit from pin to pin, and a short circuit to an external voltage source.
>
> ### Check for Short Circuit to Ground
>
> To isolate the clutch pedal position switch circuit when checking for a short circuit to ground, turn all cab panel switches to the OFF or neutral position.
>
> Set the service brake using the trailer brake hand valve.
>
> Disconnect the clutch pedal position switch, the idle validation switch, and the throttle pedal.
>
> Remove the test lead from the switch return pin.
>
> Disconnect the multimeter probe from the alligator clip.
>
> Touch the other multimeter probe to the engine block ground. Measure the resistance. The multimeter **must** show an open circuit (100k ohms or more). If the circuit is **not** open, there is a short circuit to ground in the clutch pedal position switch circuit.
>
> Repair or replace the wire connected to the clutch pedal position switch signal pin in the OEM harness according to the vehicle manufacturer's procedures.
>
> Connect all components when the repair is complete.
>
> ### Check for Short Circuit from Pin to Pin
>
> Isolate the clutch pedal position switch circuit as described in previous step. Set all cab panel switches to the OFF or neutral position, and disconnect the clutch pedal position switch and the throttle pedal.
>
> Adjust the multimeter to measure resistance. Then insert one test lead into the clutch pedal position switch signal pin of the OEM harness connector. Insert the other test lead into the clutch pedal position switch return pin. Connect the alligator clips to the multimeter probes.
>
> Measure the resistance. The multimeter **must** show an open circuit (100k ohms or more).
>
> With the first test lead still touching the clutch pedal position switch signal pin, remove the test lead from the clutch pedal position switch return pin and touch it to all other pins, one at a time. The multimeter **must** show an open circuit (100k ohms or more) at all pins.
>
> If the circuit is **not** open, there is a short circuit between the wire connected to the clutch pedal position switch signal pin and any pin that shows a closed circuit. Repair or replace the wires in the OEM harness according to the vehicle manufacturer's procedures.
>
> Remove the test lead from the clutch pedal position switch signal pin and touch it to the clutch pedal position switch return pin. Touch the other test lead to all other pins, one at a time. Measure the resistance. The multimeter **must** show an open circuit (100k ohms or more), except for the clutch pedal position switch return pin.
>
> If the circuit is **not** open, there is a short circuit between the wire connected to the clutch pedal position switch return wire and any pin that measured a closed circuit. Repair or replace the wires in the OEM harness according to the vehicle manufacturer's procedures.
>
> ### Check for Short Circuit to External Voltage Source
>
> Isolate the clutch pedal position switch circuit as described in the previous steps. Set the cab panel switches to the OFF or neutral position, and disconnect the clutch pedal position switch and the throttle pedal. Turn the keyswitch to the ON position. Adjust the multimeter to measure VDC.
>
> Insert test lead connected to the positive multimeter probe into the clutch pedal position switch signal pin. Disconnect the negative multimeter probe from the test lead and touch it to the engine block ground. Measure the voltage. The voltage **must** be 1.5 VDC or less.
>
> **Note · Примечание**
> An external voltage source is any wire in the OEM wiring that carries voltage.
>
> If the voltage value is more than 1.5 VDC, there is a short circuit between the wire connected to the clutch pedal position switch signal pin and a wire carrying power in the OEM harness. Repair the OEM harness according to the vehicle manufacturer's procedures.
>
> Remove the test lead from clutch pedal position switch signal pin and insert it into the clutch pedal position switch return pin. With the multimeter probe still touching the engine block ground, measure the voltage. The voltage **must** be 1.5 VDC or less. If the voltage value is **not** correct, there is a short circuit between the wire connected to the clutch pedal position switch return and a wire carrying power in the OEM harness. Repair the OEM harness according to the vehicle manufacturer's procedures.
>
> Connect all components after completing the repairs.
