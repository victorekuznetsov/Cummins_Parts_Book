---
aliases:
  - "Датчик скорости машины, цифровой вход"
type: "Процедура"
doc: "99-019-090"
title_en: "Vehicle Speed Sensor, Digital Input"
title_ru: "Датчик скорости машины, цифровой вход"
modified: "2015-06-29"
engines:
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 7
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-090.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/99-019-090.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/99"
  - "перевод/машинный"
---

# Vehicle Speed Sensor, Digital Input
**Датчик скорости машины, цифровой вход**

> [!abstract] Процедура · `99-019-090`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section 19 - Electronic Engine Controls
> **Даты:** изменён 2015-06-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-090.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/99-019-090.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Устройство цифрового входного сигнала является опциональной частью OEM. Он изменяет импульсы сигнала от переменного тока до постоянного тока. Эта часть находится рядом с трансмиссией или в кабине транспортного средства. Затем импульсы напряжения постоянного тока отправляются в ECM и вычисляются в мили в час.

![[ee8mpgd.png]]

Цифровая схема датчика скорости транспортного средства состоит из датчика скорости, цифрового датчика скорости транспортного средства + 5 вольт провода питания, цифрового датчика скорости транспортного средства сигнала провода и цифрового датчика скорости транспортного средства обратной провода.

![[nobox.png]]

> [!warning] ОСТОРОЖНО
> Когда установленный на OEM-устройстве кондиционер сигнала заземлен внутри, не подключайте к ECM сигнал отрицательного (-) провода датчика скорости транспортного средства. Это создаст заземление в системе, которое будет вводить нежелательный электрический шум в систему. В этом случае требуется только цифровой датчик скорости транспортного средства +5 вольт.

![[nobox.png]]

### Проверка сопротивления

> [!warning] ОСТОРОЖНО
> Правильные провода и/или одобренный Cummins® инструмент для тестирования цепи должны использоваться при работе с электрическими разъемами для предотвращения расширения штифта и повреждения разъема.

Отключите разъем интерфейса оригинального производителя оборудования (OEM) проводов жгута проводов двигателя. Чтобы определить местоположение разъема, см. соответствующую схему проводов двигателя.

Отключите цифровой датчик скорости автомобиля от электропроводки OEM.

Вставьте измерительный щуп в цифровой датчик скорости транспортного средства +5 вольт контакта питания в разъеме проводов OEM-проводов и подключите его к многометровому щупу.

![[19c01387.png]]

Вставьте другой испытательный щуп в цифровой датчик скорости транспортного средства +5 вольт в разъем датчика скорости транспортного средства и соедините зажим аллигатора с другим многометровым щупом. Настройте мультиметр на установку сопротивления и измерьте сопротивление.

Мультиметр **должен** показать замкнутую цепь (10 Ом и менее).

Если схема ** не ** закрыта, то имеется открытая схема. Ремонт или замена провода, подключенного к цифровому датчику скорости транспортного средства +5 вольт, в проводной упряжке OEM в соответствии с процедурами производителя транспортного средства.

Удалите свинец из цифрового датчика скорости транспортного средства +5 вольт контакта питания и вставьте его в цифровой датчик скорости транспортного средства сигнал контакта проводов OEM разъема. Удалите многометровый свинец из цифрового датчика скорости транспортного средства +5 вольт на разъеме датчика скорости и соедините его с цифровым датчиком скорости транспортного средства, контактирующим с сигналом датчика скорости в разъеме датчика скорости транспортного средства. Измерьте сопротивление.

Мультиметр **должен** показать замкнутую цепь (10 Ом и менее).

Если схема ** не ** закрыта, то имеется открытая схема. Ремонт или замена провода, подключенного к контакту сигнала датчика скорости транспортного средства в электропроводке OEM в соответствии с процедурами производителя транспортного средства.

Удалите свинец из контакта с сигналом датчика скорости цифрового транспортного средства и вставьте его в цифровой датчик скорости транспортного средства обратного контакта разъёма проводов OEM-подключателя. Удалите многометровый свинец из контакта с датчиком скорости цифрового транспортного средства на разъеме датчика скорости и соедините его с цифровым датчиком скорости транспортного средства обратным контактом в разъеме датчика скорости транспортного средства. Измерьте сопротивление.

Мультиметр **должен** показать замкнутую цепь (10 Ом и менее).

Если схема ** не ** закрыта, то имеется открытая схема. Ремонт или замена провода, подключенного к датчику скорости транспортного средства, обратного контакта в электропроводке OEM в соответствии с процедурами производителя транспортного средства.

Если значения верны, схема ** должна быть проверена на короткое замыкание на землю и короткое замыкание от контакта к контакту.

> [!missing]- Иллюстрация `19c01385.png` не извлечена — смотрите PDF-оригинал документа

### Проверка на замыкание на массу

Отсоедините датчик скорости автомобиля от проводной ремни OEM. Отключите разъем интерфейса оригинального производителя оборудования (OEM) проводов жгута проводов двигателя. Чтобы определить местоположение разъема, см. соответствующую схему проводов двигателя.

Вставьте измерительный щуп в цифровой датчик скорости транспортного средства, который возвращает контакт с разъемом OEM-проводов и подключите его к многометровому щупу. Прикоснитесь к другому многометровому щупу к заземлению блока двигателя. Измерьте сопротивление.

Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Удалите измерительный щуп из цифрового датчика скорости транспортного средства и вставьте его в цифровой датчик скорости транспортного средства +5 вольт контакта питания разъёма проводов OEM. Прикоснитесь к другому многометровому щупу к заземлению блока двигателя. Измерьте сопротивление.

Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Удалите испытательный щуп из цифрового датчика скорости транспортного средства +5 вольт контакта питания и вставьте его в цифровой датчик скорости транспортного средства контакта сигнала проводов OEM разъема. Прикоснитесь к другому многометровому щупу к заземлению блока двигателя. Измерьте сопротивление.

Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Если схема ** не открыта в любой из этих проверок, в схеме датчика скорости цифрового транспортного средства в электропроводке OEM есть короткое замыкание.

Ремонт проводов, имеющих короткое замыкание, в соответствии с процедурами изготовителя транспортного средства.

![[19c01154.png]]

### Проверка на замыкание между контактами

Отсоедините датчик скорости автомобиля от проводной ремни OEM.

Отключите разъем интерфейса оригинального производителя оборудования (OEM) проводов жгута проводов двигателя. Чтобы определить местоположение разъема, см. соответствующую схему проводов двигателя.

Вставьте один испытательный щуп в цифровой датчик скорости транспортного средства +5 вольт контакта питания разъема проводов OEM-приемника и соедините его с многометровым щупом. Подключите другой испытательный щуп к другому многометровому щупу и проверьте все штифты в разъеме OEM-проводов.Измерьте сопротивление.

Мультиметр ** должен** показывать открытую схему на всех штифтах (100к Ом или более).

Удалите измерительный щуп из цифрового датчика скорости транспортного средства +5 вольт контакта питания и вставьте его в цифровой датчик скорости транспортного средства сигнал обратного контакта.

Используйте другой измерительный щуп для проверки всех штифтов в разъеме. Измерьте сопротивление.

Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Удалите измерительный щуп из цифрового датчика скорости транспортного средства обратного контакта и вставьте его в цифровой датчик скорости датчика сигнала контакта.

Используйте другой измерительный щуп для проверки всех штифтов в разъеме. Измерьте сопротивление.

Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Если схема ** не** открыта в любой из проверок, отремонтируйте провода, которые имеют короткое замыкание в соответствии с процедурами производителя транспортного средства.

> [!note] Примечание
> Если значения верны для всех проверок схемы в Процедуре 019-090, схема датчика скорости транспортного средства хороша.

Проблема заключается в датчике скорости автомобиля. Ремонт или замена датчика скорости транспортного средства в соответствии с процедурами изготовителя транспортного средства.

![[19c01236.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> The digital input signal device is an OEM optional part. It changes the signal pulses from AC to DC. This part is near the transmission or in the vehicle cab. The DC voltage pulses are then sent to the ECM and computed into miles per hour.
>
> The digital vehicle speed sensor circuit consists of the speed sensor, the digital vehicle speed sensor +5 volt supply wire, the digital vehicle speed sensor signal wire, and the digital vehicle speed sensor return wire.
>
> **CAUTION · Осторожно**
> When the OEM-supplied signal conditioner is internally grounded, do not connect the vehicle speed sensor signal negative (-) wire to the ECM. This will create a ground loop in the system that will inject unwanted electrical noise into the system. Only the digital vehicle speed sensor +5 volt supply wire is required in this case.
>
> ### Resistance Check
>
> **CAUTION · Осторожно**
> Proper leads and/or a Cummins® approved circuit testing tool must be used when working with electrical connectors to prevent pin expansion and damage to the connector.
>
> Disconnect the original equipment manufacturer (OEM) harness engine interface connector. To determine the location of the connector, see the corresponding engine wiring diagram.
>
> Disconnect the digital vehicle speed sensor from the OEM harness.
>
> Insert a test lead into the digital vehicle speed sensor +5 volt supply pin in the OEM harness connector, and connect it to the multimeter probe.
>
> Insert the other test lead to the digital vehicle speed sensor +5 volt supply in the vehicle speed sensor connector and connect the alligator clip to the other multimeter probe. Adjust the multimeter to the resistance setting and measure the resistance.
>
> The multimeter **must** show a closed circuit (10 ohms or less).
>
> If the circuit is **not** closed, there is an open circuit. Repair or replace the wire connected to the digital vehicle speed sensor +5 volt supply pin in the OEM harness according to the vehicle manufacturer's procedures.
>
> Remove the lead from the digital vehicle speed sensor +5 volt supply pin and insert it into the digital vehicle speed sensor signal pin of the OEM harness connector. Remove the multimeter lead from the digital vehicle speed sensor +5 volt supply at the speed sensor connector and connect it to the digital vehicle speed sensor signal pin in the vehicle speed sensor connector. Measure the resistance.
>
> The multimeter **must** show a closed circuit (10 ohms or less).
>
> If the circuit is **not** closed, there is an open circuit. Repair or replace the wire connected to the vehicle speed sensor signal pin in the OEM harness according to the vehicle manufacturer's procedures.
>
> Remove the lead from the digital vehicle speed sensor signal pin and insert it into the digital vehicle speed sensor return pin of the OEM harness connector. Remove the multimeter lead from the digital vehicle speed sensor signal pin at the speed sensor connector and connect it to the digital vehicle speed sensor return pin in the vehicle speed sensor connector. Measure the resistance.
>
> The multimeter **must** show a closed circuit (10 ohms or less).
>
> If the circuit is **not** closed, there is an open circuit. Repair or replace the wire connected to the vehicle speed sensor return pin in the OEM harness according to the vehicle manufacturer's procedures.
>
> If the values are correct, the circuit **must** still be checked for a short circuit to ground and a short circuit from pin-to-pin.
>
> ### Check for Short Circuit to Ground
>
> Disconnect the vehicle speed sensor from the OEM harness. Disconnect the original equipment manufacturer (OEM) harness engine interface connector. To determine the location of the connector, see the corresponding engine wiring diagram.
>
> Insert a test lead into the digital vehicle speed sensor signal return pin of the OEM harness connector, and connect it to the multimeter probe. Touch the other multimeter probe to the engine block ground. Measure the resistance.
>
> The multimeter **must** show an open circuit (100k ohms or more).
>
> Remove the test lead from the digital vehicle speed sensor signal return pin and insert it into the digital vehicle speed sensor +5 volt supply pin of the OEM harness connector. Touch the other multimeter probe to the engine block ground. Measure the resistance.
>
> The multimeter **must** show an open circuit (100k ohms or more).
>
> Remove the test lead from the digital vehicle speed sensor signal +5 volt supply pin and insert it into the digital vehicle speed sensor signal pin of the OEM harness connector. Touch the other multimeter probe to the engine block ground. Measure the resistance.
>
> The multimeter **must** show an open circuit (100k ohms or more).
>
> If the circuit is **not** open in either of these checks, there is a short circuit to ground in the digital vehicle speed sensor circuit in the OEM harness.
>
> Repair the wires which have a short circuit according to the vehicle manufacturer's procedures.
>
> ### Check for Short Circuit from Pin to Pin
>
> Disconnect the vehicle speed sensor from the OEM harness.
>
> Disconnect the original equipment manufacturer (OEM) harness engine interface connector. To determine the location of the connector, see the corresponding engine wiring diagram.
>
> Insert one test lead into the digital vehicle speed sensor +5 volt supply pin of the OEM harness connector, and connect it to the multimeter probe. Connect the other test lead to the other multimeter probe and check all pins in the OEM harness connector.Measure the resistance.
>
> The multimeter **must** show an open circuit at all pins (100k ohms or more).
>
> Remove the test lead from the digital vehicle speed sensor +5 volt supply pin, and insert it into the digital vehicle speed sensor signal return pin.
>
> Use the other test lead to check all pins in the connector. Measure the resistance.
>
> The multimeter **must** show an open circuit (100k ohms or more).
>
> Remove the test lead from the digital vehicle speed sensor return pin, and insert it into the digital vehicle speed sensor signal signal pin.
>
> Use the other test lead to check all pins in the connector. Measure the resistance.
>
> The multimeter **must** show an open circuit (100k ohms or more).
>
> If the circuit is **not** open in any of the checks, repair the wires that have the short circuit according to the vehicle manufacturer's procedures.
>
> **Note · Примечание**
> If the values are correct for all of the circuit checks in Procedure 019-090, the vehicle speed sensor circuit is good.
>
> The problem is in the vehicle speed sensor. Repair or replace the vehicle speed sensor according to the vehicle manufacturer's procedures.
