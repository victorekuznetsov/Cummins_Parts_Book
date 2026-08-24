---
aliases:
  - "Цепь клапана отсечки топлива"
type: "Процедура"
doc: "01-019-049"
title_en: "Fuel Shutoff Valve Circuit"
title_ru: "Цепь клапана отсечки топлива"
modified: "2003-12-04"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 14
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-019-049.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-019-049.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Fuel Shutoff Valve Circuit
**Цепь клапана отсечки топлива**

> [!abstract] Процедура · `01-019-049`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-12-04
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-019-049.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-019-049.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Первичная проверка

Проверьте затвор топлива соленоидного поста для дополнительных проводов, которые, возможно, подключены к питанию к другому устройству. Удалите дополнительные провода, которые найдены связанными с соленоидным столбом.

![[19400454.png]]

Убедитесь, что терминал находится в контакте с любым металлическим объектом, кроме проводного терминала. Включение переключателя Run/Stop в Run сигнализирует ECM об открытии запорного соленоидного клапана. Соленоид закрывается, когда ECM чувствует, что выключатель Run/Stop установлен на Stop, или когда ECM чувствует состояние защиты двигателя.

![[19400742.png]]

### Проверка сопротивления

Клапан отключения топлива представляет собой двухпостовый соленоид. Поэтому он имеет как сигнальный провод, так и наземный провод через проводную упряжку к ECM. Отсоедините отсоединительные клеммы соленоидов топливного клапана от терминальных постов. Проверьте поврежденные терминалы.

![[19802549.png]]

Отсоедините жгут проводов двигателя от удлинителя проводов. Проверьте наличие поврежденных контактов.

![[19802479.png]]

Отсоедините удлинитель проводов от ECM. Проверьте наличие поврежденных контактов.

![[19802479.png]]

> [!warning] ОСТОРОЖНО
> Не используйте щупы или провода, кроме Части № 3822917. Разъём будет повреждён. Лиды должны плотно помещаться в разъеме без расширения штифтов разъема.

Включить испытательный щуп в контакт сигнала запорного клапана топлива на удлинительной проводах. Подключите аллигатор к многометровому щупу.

![[19802550.png]]

Прикосновение к другому мультиметру приводит к сигнальному терминалу запорного клапана топлива. Измерьте сопротивление. Мультиметр **должен** показать замкнутую цепь (10 Ом и менее). Если схема **не** закрыта, повторите эту процедуру на разъеме ремня электропроводки двигателя. Если он все еще показывает замкнутую цепь, отремонтируйте или замените жгут электропроводки двигателя. См. процедуры[[99-019-197 — Ring Terminal|019-197]],[[99-019-199 — Connector, Butt Splice|019-199]],[[99-019-219 — Danfoss™ (Circular DIN Series) Connector|019-219]]и[[01-019-043 — Engine Wiring Harness|019-043]]. Если в ходе испытания на электропроводке двигателя в жгуте проводов показана замкнутая цепь, отремонтируйте или замените удлинительную электропроводку жгута проводов. См. процедуры[[99-019-219 — Danfoss™ (Circular DIN Series) Connector|019-219]],[[99-019-213 — D-Sub Miniature Connector Series|019-213]]и[[01-019-175 — Extension Wiring Harness|019-175]]. Если цепь закрыта, ее **** все равно нужно проверить на короткое расстояние до земли и короткое расстояние от пин-кодов до пин-кодов.

![[19802550.png]]

Включить испытательный щуп в обратный контакт запорного клапана топлива на удлинительной проводах. Подключите аллигатор к многометровому щупу.

Прикосновение к другому мультиметру приводит к возвратному терминалу запорного клапана топлива. Измерьте сопротивление. Мультиметр **должен** показать замкнутую цепь (10 Ом и менее). Если схема **не** закрыта, повторите эту процедуру на разъеме ремня электропроводки двигателя. Если он все еще показывает замкнутую цепь, отремонтируйте или замените жгут электропроводки двигателя. См. процедуры[[99-019-197 — Ring Terminal|019-197]],[[99-019-199 — Connector, Butt Splice|019-199]],[[99-019-219 — Danfoss™ (Circular DIN Series) Connector|019-219]]и[[01-019-043 — Engine Wiring Harness|019-043]]. Если в ходе испытания на электропроводке двигателя в жгуте проводов показана замкнутая цепь, отремонтируйте или замените удлинительную электропроводку жгута проводов. См. процедуру[[99-019-219 — Danfoss™ (Circular DIN Series) Connector|019-219]],[[99-019-213 — D-Sub Miniature Connector Series|019-213]]и[[01-019-175 — Extension Wiring Harness|019-175]]. Если цепь закрыта, ее **** все равно нужно проверить на короткое расстояние до земли и короткое расстояние от пин-кодов до пин-кодов.

![[19802550.png]]

### Проверка на замыкание на массу

Вставьте электрический свинец в сигнал отключения клапана топлива на контакте разъёма ремня электропроводки двигателя. Прикоснитесь к другому многометровому щупу, чтобы заблокировать двигатель. Кольцевой терминал в соленоиде ** должен быть отключен и может ** не касаться ничего, что заземлено. Измерьте сопротивление. Мультиметр ** должен** показывать открытую схему (более 100 К Ом). Если цепь ** не** открыта, в проводе сигнала отключения топлива есть короткое заземление. Ремонт или замена ремня электропроводки двигателя. См. процедуры[[99-019-197 — Ring Terminal|019-197]],[[99-019-199 — Connector, Butt Splice|019-199]],[[99-019-219 — Danfoss™ (Circular DIN Series) Connector|019-219]]и[[01-019-043 — Engine Wiring Harness|019-043]].

![[19802487.png]]

### Проверка на замыкание между контактами

Проверьте короткое замыкание от контакта с сигналом запорного клапана топлива до всех других контактов в разъеме ремня электропроводки двигателя. Подключите испытательный щуп от контакта сигнала запорного клапана в разъёме ремня электропроводки двигателя. Подключите аллигаторный клип второго испытательного щупа к другому многометровому щупу. Вставьте штифт свинца во все другие штифты в приводе.

Кольцевые терминалы в соленоиде должны быть отключены и могут не касаться ничего, что заземлено. Подача напряжения батареи ** должна быть отключена.

![[19802488.png]]

Измерьте сопротивление. Мультиметр ** должен** показывать открытую схему (более 100k ом). Если цепь ** не** открыта, между контактом сигнала отключения топлива и **любым значком ***, который измеряет замкнутую цепь, имеется короткое расстояние. Ремонт или замена ремня электропроводки двигателя. См. процедуры[[99-019-197 — Ring Terminal|019-197]],[[99-019-199 — Connector, Butt Splice|019-199]],[[99-019-219 — Danfoss™ (Circular DIN Series) Connector|019-219]]и[[01-019-043 — Engine Wiring Harness|019-043]].

![[19802488.png]]

Повторите вышеупомянутые шаги на удлинительной проводах. Если цепь ** не** открыта, между контактом сигнала отключения топлива и **любым значком ***, который измеряет замкнутую цепь, имеется короткое расстояние. Ремонт или замена удлинителя проводов жгута. См. процедуры[[99-019-219 — Danfoss™ (Circular DIN Series) Connector|019-219]],[[99-019-213 — D-Sub Miniature Connector Series|019-213]]и[[01-019-175 — Extension Wiring Harness|019-175]].

![[19802485.png]]

### Проверьте короткое замыкание на источнике внешнего напряжения

Проверьте короткое замыкание от цепи запорного клапана до источника +12 VDC. Отсоедините разъем удлинительной проводов от ECM. Подключите источник напряжения батареи, если он был отключен. Установите переключатель Run/Stop в положение Run. Настройте мультиметр для измерения VDC. Вставьте пробный щуп в контактный сигнал отключаемого клапана топлива; подсоедините его к мультиметру. Прикоснитесь к другому многометровому щупу к заземлению блока двигателя.

> [!note] Примечание
> Внешний источник напряжения - это ** любой ** провод в OEM-проводах, который несет напряжение.

![[19802487.png]]

Измерьте напряжение. Напряжение ** должно быть 1.5 VDC или меньше. Если напряжение ** не** правильно, между цепью запорного клапана топлива и внешним источником напряжения имеется короткое замыкание. Удалите внешний источник напряжения.

Подключите все компоненты после завершения ремонта.

![[19802487.png]]


> [!quote]- Original (English) · английский оригинал
> ### Initial Check
>
> Inspect the fuel shutoff solenoid post for extra wires that are possibly connected to supply power to another device. Remove the extra wires that are found connected to the solenoid post.
>
> Check that the terminal post is **not** in contact with any metallic object other than the harness terminal. Turning the Run/Stop switch to Run signals the ECM to open the fuel shutoff solenoid valve. The solenoid closes when the ECM senses the Run/Stop switch is set to Stop or when the ECM senses an engine protection condition.
>
> ### Resistance Check
>
> The fuel shutoff valve is a two-post solenoid. Therefore, it has both a signal wire and a ground wire through the harness to the ECM. Disconnect the fuel shutoff valve solenoid terminals from the terminal posts. Check for damaged terminals.
>
> Disconnect the engine harness from the extension harness. Check for damaged pins.
>
> Disconnect the extension harness from the ECM. Check for damaged pins.
>
> **CAUTION · Осторожно**
> Do not use probes or leads other than Part Number 3822917. The connector will be damaged. The leads must fit tightly in the connector without expanding the pins of the connector.
>
> Insert a test lead into the fuel shutoff valve signal pin at the extension harness. Connect the alligator clip to the multimeter probe.
>
> Touch the other multimeter lead to the fuel shutoff valve signal terminal. Measure the resistance. The multimeter **must** show a closed circuit (10 ohms or less). If the circuit is **not** closed, repeat this procedure at the engine harness connector. If it still does **not** show a closed circuit, repair or replace the engine harness. Refer to Procedures [[99-019-197 — Ring Terminal|019-197]], [[99-019-199 — Connector, Butt Splice|019-199]], [[99-019-219 — Danfoss™ (Circular DIN Series) Connector|019-219]], and [[01-019-043 — Engine Wiring Harness|019-043]]. If the test at the engine harness shows a closed circuit, repair or replace the extension harness. Refer to Procedures [[99-019-219 — Danfoss™ (Circular DIN Series) Connector|019-219]], [[99-019-213 — D-Sub Miniature Connector Series|019-213]], and [[01-019-175 — Extension Wiring Harness|019-175]]. If the circuit is closed, it **must** still be checked for a short to ground and a short from pin to pin.
>
> Insert a test lead into the fuel shutoff valve return pin at the extension harness. Connect the alligator clip to the multimeter probe.
>
> Touch the other multimeter lead to the fuel shutoff valve return terminal. Measure the resistance. The multimeter **must** show a closed circuit (10 ohms or less). If the circuit is **not** closed, repeat this procedure at the engine harness connector. If it still does **not** show a closed circuit, repair or replace the engine harness. Refer to Procedures [[99-019-197 — Ring Terminal|019-197]], [[99-019-199 — Connector, Butt Splice|019-199]], [[99-019-219 — Danfoss™ (Circular DIN Series) Connector|019-219]], and [[01-019-043 — Engine Wiring Harness|019-043]]. If the test at the engine harness shows a closed circuit, repair or replace the extension harness. Refer to Procedure [[99-019-219 — Danfoss™ (Circular DIN Series) Connector|019-219]], [[99-019-213 — D-Sub Miniature Connector Series|019-213]], and [[01-019-175 — Extension Wiring Harness|019-175]]. If the circuit is closed, it **must** still be checked for a short to ground and a short from pin to pin.
>
> ### Check for Short Circuit to Ground
>
> Insert the electrical lead into the fuel shutoff valve signal at the engine harness connector pin. Touch the other multimeter probe to engine block. The ring terminal at the solenoid **must** be disconnected and can **not** touch anything that is grounded. Measure the resistance. The multimeter **must** show an open circuit (more than 100K ohms). If the circuit is **not** open, there is a short to ground in the fuel shutoff value signal wire. Repair or replace the engine harness. Refer to Procedures [[99-019-197 — Ring Terminal|019-197]], [[99-019-199 — Connector, Butt Splice|019-199]], [[99-019-219 — Danfoss™ (Circular DIN Series) Connector|019-219]], and [[01-019-043 — Engine Wiring Harness|019-043]].
>
> ### Check for Short Circuit from Pin to Pin
>
> Check for a short circuit from the fuel shutoff valve signal pin to all other pins in the engine harness connector. Connect a test lead from the fuel shutoff valve signal pin in the engine harness connector. Connect the alligator clip of a second test lead to the other multimeter probe. Insert the pin of the lead into all of the other pins in the actuator.
>
> The ring terminals at the solenoid **must** be disconnected and can **not** touch anything that is grounded. The battery voltage supply **must** be disconnected.
>
> Measure the resistance. The multimeter **must** show an open circuit (more than 100k ohms). If the circuit is **not** open, there is a short between the fuel shutoff value signal pin and **any** pin that measured a closed circuit. Repair or replace the engine harness. Refer to Procedures [[99-019-197 — Ring Terminal|019-197]], [[99-019-199 — Connector, Butt Splice|019-199]], [[99-019-219 — Danfoss™ (Circular DIN Series) Connector|019-219]], and [[01-019-043 — Engine Wiring Harness|019-043]].
>
> Repeat the above steps at the extension harness. If the circuit is **not** open, there is a short between the fuel shutoff value signal pin and **any** pin that measured a closed circuit. Repair or replace the extension harness. Refer to Procedures [[99-019-219 — Danfoss™ (Circular DIN Series) Connector|019-219]], [[99-019-213 — D-Sub Miniature Connector Series|019-213]], and [[01-019-175 — Extension Wiring Harness|019-175]].
>
> ### Check for Short Circuit to External Voltage Source
>
> Check for a short circuit from the fuel shutoff valve circuit to a +12 VDC source. Disconnect the extension harness connector from the ECM. Connect the battery voltage supply if it has been disconnected. Set the Run/Stop switch to the Run position. Adjust the multimeter to measure VDC. Insert a test lead into the fuel shutoff valve signal pin; connect it to the multimeter. Touch the other multimeter probe to the engine block ground.
>
> **Note · Примечание**
> An external voltage source is **any** wire in the OEM wiring that carries voltage.
>
> Measure the voltage. The voltage **must** be 1.5 VDC or less. If the voltage is **not** correct, there is a short circuit between the fuel shutoff valve circuit and an external voltage source. Remove the external voltage source.
>
> Connect all components after the repair is complete.
