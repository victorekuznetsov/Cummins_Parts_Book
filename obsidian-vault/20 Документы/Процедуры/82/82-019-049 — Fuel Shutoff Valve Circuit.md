---
aliases:
  - "Цепь клапана отсечки топлива"
type: "Процедура"
doc: "82-019-049"
title_en: "Fuel Shutoff Valve Circuit"
title_ru: "Цепь клапана отсечки топлива"
modified: "2005-01-28"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-049.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-019-049.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# Fuel Shutoff Valve Circuit
**Цепь клапана отсечки топлива**

> [!abstract] Процедура · `82-019-049`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section 19 - Electronic Engine Controls
> **Даты:** изменён 2005-01-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-049.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-019-049.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Топливный отключающий соленоидный клапан, расположенный на корпусе топливной системы. Соленоид контролируется ECM.

> [!note] Примечание
> Только один провод из ECM будет прикреплен к соленоидному посту. ECM не способен подавать энергию для других вспомогательных компонентов. Если внешний источник напряжения подключен, будет индуцироваться код неисправности.

![[19c01393.png]]

Включение переключателя зажигания транспортного средства сигнализирует ECM об открытии запорного соленоидного клапана. Соленоид закрывается, когда ECM чувствует, что замок зажигания автомобиля выключен, или когда ECM чувствует перегрузку двигателя.

Для получения дополнительной информации о клапане отключения топлива обратитесь к процедуре 005-043 в Руководстве по устранению неполадок и ремонту, двигателях серии ISM и QSM11, Бюллетень [[3666322 — ISM, ISMe, and QSM11 Service Manual\|3666322]].

![[fv2swkb.png]]

### Проверка сопротивления

Схема запорного клапана топлива представляет собой сигнальный провод, контакт 33, разъёма проводов привода с запорным клапаном соленоида. Клапан заземляется через двигатель.

Отсоедините разъем электропроводки привода от ECM. Проверьте наличие поврежденных контактов.

Отсоедините отключающий соленоидный провод от клапанного терминала.

![[fv2swkc.png]]

> [!warning] ОСТОРОЖНО
> Не используйте щупы или провода, отличные от Части № 3822758. Разъём будет повреждён. Лиды должны плотно помещаться в разъеме без расширения штифтов разъема.

Включить испытательный щуп в контакт 33 разъёма проводов привода. Подключите аллигатор к многометровому щупу.

![[19200337.png]]

Прикоснитесь к другому многометровому щупу к запорному клапану соленоидной проволоки. Измерьте сопротивление.

Мультиметр **должен** показать замкнутую цепь (10 Ом и менее). Если цепь **не** закрыта, отремонтируйте или замените электропроводку привода. См. процедуру[[82-019-043-tr — Engine Wiring Harness|019-043]].

Если цепь закрыта, она **должна **все еще проверяться на короткое замыкание на землю и короткое замыкание от пин-кодов до пин-кодов.

![[19200337.png]]

### Проверка на замыкание на массу

Вставьте пробный щуп в контакт 33 привода проводов жгута разъема и подсоедините его к мультиметру. Прикоснитесь к другому многометровому щупу, чтобы блокировать двигатель. Кольцевой терминал в соленоиде **должен быть отключен и может **не касаться ничего, что заземлено. Измерьте сопротивление. Мультиметр **должен** показывать открытую схему (более 100k ом). Если цепь не открыта, в проводе, подключенном к контакту 33, есть короткое замыкание для заземления. Ремонт или замена привода проводов жгута.

См. процедуру[[82-019-043-tr — Engine Wiring Harness|019-043]].

![[19900627.png]]

### Проверка на замыкание между контактами

Проверьте короткое замыкание от контакта 33 до всех других контактов разъёма проводов привода. Вставьте испытательный щуп в контакт 33 разъёма проводов привода и соедините свинец с многометровым щупом. Вставьте другой испытательный щуп во все другие штифты разъёма проводов привода, по одному за раз.

Кольцевой терминал в соленоиде **должен быть отключен и может **не касаться ничего, что заземлено. Подача напряжения батареи должна быть отключена.

> [!missing]- Иллюстрация `19c00435.png` не извлечена — смотрите PDF-оригинал документа

Измерьте сопротивление. Мультиметр **должен** показывать открытую схему (более 100k ом). Если схема не открыта, между контактом 33 и любым штифтом, который измеряет замкнутую цепь, есть короткое расстояние.

Ремонт или замена привода проводов жгута. См. процедуру[[82-019-043-tr — Engine Wiring Harness|019-043]].

После ремонта подсоедините все компоненты.

> [!missing]- Иллюстрация `19c00435.png` не извлечена — смотрите PDF-оригинал документа


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> The fuel shutoff solenoid valve located on the fuel system housing. The solenoid is controlled by the ECM.
>
> **Note · Примечание**
> **Only** one wire from the ECM will be attached to the solenoid post. The ECM is **not** capable of supplying power for other auxiliary components. If an external voltage source is attached, a fault code will be induced.
>
> Turning the vehicle keyswitch on signals the ECM to open the fuel shutoff solenoid valve. The solenoid closes when the ECM senses the vehicle keyswitch is turned off or when the ECM senses an engine overspeed.
>
> For more information on the fuel shutoff valve, refer to Procedure [[35-005-043 — Fuel Shutoff Valve|005-043]] in the Troubleshooting and Repair Manual, ISM and QSM11 Series Engines, Bulletin [[3666322 — ISM, ISMe, and QSM11 Service Manual\|3666322]].
>
> ### Resistance Check
>
> The fuel shutoff valve circuit is a signal wire, pin 33, of the actuator harness connector to the shutoff valve solenoid. The valve is grounded through the engine.
>
> Disconnect the actuator harness connector from the ECM. Check for damaged pins.
>
> Disconnect the fuel shutoff solenoid wire from the valve terminal post.
>
> **CAUTION · Осторожно**
> Do not use probes or leads other than Part Number 3822758. The connector will be damaged. The leads must fit tightly in the connector without expanding the pins of the connector.
>
> Insert a test lead into pin 33 of the actuator harness connector. Connect the alligator clip to the multimeter probe.
>
> Touch the other multimeter probe to the fuel shutoff valve solenoid wire. Measure the resistance.
>
> The multimeter **must** show a closed circuit (10 ohms or less). If the circuit is **not** closed, repair or replace the actuator harness. Refer to Procedure [[82-019-043-tr — Engine Wiring Harness|019-043]].
>
> If the circuit is closed, it **must** still be checked for a short circuit to ground and a short circuit from pin to pin.
>
> ### Check for Short Circuit to Ground
>
> Insert a test lead into pin 33 of the actuator harness connector and connect it to the multimeter. Touch the other multimeter probe to engine block ground. The ring terminal at the solenoid **must** be disconnected and can **not** touch anything that is grounded. Measure the resistance. The multimeter **must** show an open circuit (more than 100k ohms). If the circuit is **not** open, there is a short circuit to ground in the wire connected to pin 33. Repair or replace the actuator harness.
>
> Refer to Procedure [[82-019-043-tr — Engine Wiring Harness|019-043]].
>
> ### Check for Short Circuit from Pin to Pin
>
> Check for a short circuit from pin 33 to all other pins of the actuator harness connector. Insert a test lead into pin 33 of the actuator harness connector, and connect the lead to the multimeter probe. Insert the other test lead into all other pins of the actuator harness connector, one at a time.
>
> The ring terminal at the solenoid **must** be disconnected and can **not** touch anything that is grounded. The battery voltage supply **must** be disconnected.
>
> Measure the resistance. The multimeter **must** show an open circuit (more than 100k ohms). If the circuit is **not** open, there is a short between pin 33 and any pin that measured a closed circuit.
>
> Repair or replace the actuator harness. Refer to Procedure [[82-019-043-tr — Engine Wiring Harness|019-043]].
>
> Connect all components after completing the repair.
