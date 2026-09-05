---
aliases:
  - "Цепь сигнализации пуска двигателя"
type: "Процедура"
doc: "82-019-310"
title_en: "Engine Start Alarm Circuit"
title_ru: "Цепь сигнализации пуска двигателя"
modified: "2005-01-28"
engines:
  - "41343322"
  - "41370103"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 21
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-310.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-019-310.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# Engine Start Alarm Circuit
**Цепь сигнализации пуска двигателя**

> [!abstract] Процедура · `82-019-310`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section 19 - Electronic Engine Controls
> **Даты:** изменён 2005-01-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-310.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-019-310.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Проверка сопротивления

Переведите замок зажигания в положение OFF.

Отключите сигнализацию запуска двигателя от электропроводки OEM.

Отключите 31-контактный OEM-разъем.

Установите мультиметр для измерения сопротивления.

![[19c00737.png]]

> [!warning] ОСТОРОЖНО
> Для уменьшения возможности повреждения штифта и проводов жгута проводов используйте пробный щуп, номер детали 3822917 и 3822758, при проведении измерений.

Прикосновение одного из мультиметров приводит к подаче провода, контакту В (или 2), к разъему пусковой сигнализации двигателя. Прикосновение к другому мультиметру приводит к контакту 29 с 31-контактным OEM-разъемом, OEM-проводкой с жгутом проводов. Считайте показания мультиметра.

Повторите проверку сопротивления для обратного провода. Измерьте сопротивление от обратного провода, контакт A (или 1), от разъема аварийной проводов двигателя до контакта 28 с 31-контактным разъемом OEM, стороны проводной ремни OEM. Считайте показания мультиметра.

![[19c00738.png]]

Для обеих проверок пин-кодов мультиметр **должен **отображать значение менее 10 Ом, что является замкнутой схемой.

Если цепь **не** закрыта, отремонтируйте или замените электропроводку OEM. См. процедуру[[99-019-202 — Metripack Connector Series|019-202]]019-071.

![[19801619.png]]

Отсоедините разъем электропроводки привода от ECM.

Прикосновение к одному из мультиметров приводит к контакту 29 31-контактного OEM-разъема, проводов двигателя с ремнями безопасности.

Прикосновение к другому мультиметру приводит к контакту 25 привода проводов ремня разъема.

Считайте показания мультиметра.

![[19c00728.png]]

Мультиметр **должен **отображать значение менее 10 Ом, что является замкнутой схемой.

Если цепь **не** закрыта, отремонтируйте или замените электропроводку OEM. См. процедуру[[82-019-043-tr — Engine Wiring Harness|019-043]].

![[19801619.png]]

Затем проверьте сопротивление обратного провода. Прикосновение к одному из мультиметров приводит к контакту 28 31-контактного OEM-разъема, проводов двигателя с жгутом проводов. Прикосновение к другому мультиметру приводит к контакту 32 привода проводов ремня разъема. Считайте показания мультиметра.

Мультиметр **должен **отображать значение менее 10 Ом, что является замкнутой схемой. Если цепь **не** закрыта, отремонтируйте или замените электропроводку двигателя.

См. процедуру[[82-019-043-tr — Engine Wiring Harness|019-043]].

После ремонта подсоедините все компоненты.

![[19c00728.png]]

### Проверка на замыкание на массу

Переведите замок зажигания в положение OFF.

Отключите сигнализацию запуска двигателя от электропроводки OEM.

Отсоедините разъем электропроводки привода от ECM.

Установите мультиметр для измерения сопротивления.

![[19c00746.png]]

> [!warning] ОСТОРОЖНО
> Для уменьшения возможности повреждения штифта и проводов жгута проводов используйте пробный щуп, номер детали 3822917 и 3822758, при проведении измерений.

Прикосновение к одному из мультиметров приводит к контакту 25 привода проводов ремня разъема.

Прикоснитесь к другому мультиметру, который приведет к заземлению блока двигателя.

Считайте показания мультиметра.

![[19c00741.png]]

Мультиметр **must** отображает показания более 100k ом, что является открытой схемой.

Если схема **не **открыта, есть короткое замыкание на землю.

Изолируйте короткое замыкание к OEM-проводах или электропроводке двигателя.

![[19801621.png]]

Отключите 31-контактный OEM-разъем.

Прикосновение к одному из мультиметров приводит к контакту 29 31-контактного OEM-разъема, OEM-проводов с жгутом проводов.

Прикоснитесь к другому мультиметру, который приведет к заземлению блока двигателя.

Считайте показания мультиметра.

![[19c00742.png]]

Мультиметр **must** отображает показания более 100k ом, что является открытой схемой.

Если схема **не** открыта, отремонтируйте или замените проводку OEM. См. процедуру 019-071. Если цепь открыта, то короткая находится в жгуте проводов двигателя. Ремонт или замена ремня электропроводки двигателя. См. процедуру[[82-019-043-tr — Engine Wiring Harness|019-043]].

После ремонта подсоедините все компоненты.

![[19801621.png]]

### Проверка на замыкание между контактами

Переведите замок зажигания в положение OFF.

Отключите сигнализацию запуска двигателя от электропроводки OEM.

Отсоедините разъем электропроводки привода от ECM.

Установите мультиметр для измерения сопротивления.

![[19c00746.png]]

> [!warning] ОСТОРОЖНО
> Для уменьшения возможности повреждения штифта и проводов жгута проводов используйте пробный щуп, номер детали 3822917 и 3822758, при проведении измерений.

Прикосновение к одному из мультиметров приводит к контакту 25 привода проводов ремня разъема.

Прикосновение к другому мультиметру приводит ко всем другим штифтам в разъеме, по одному за раз.

Считайте показания мультиметра.

![[19c00735.png]]

Мультиметр **must** отображает показания более 100k ом, что является открытой схемой.

Если какое-либо измерение контакта с контактом регистрирует замкнутую цепь, то есть короткое замыкание от контакта 25 до этого штифта.

Изолируйте короткую к OEM или проводах двигателя.

![[19801621.png]]

Отключите 31-контактный OEM-разъем.

Прикосновение к одному из мультиметров приводит к контакту 29 31-контактного OEM-разъема проводов жгута проводов, OEM-проводов жгута проводов стороны.

Прикосновение к другому мультиметру приводит ко всем другим штифтам в разъеме, по одному за раз.

Считайте показания мультиметра.

![[19c00744.png]]

Мультиметр **must** отображает показания более 100k ом, что является открытой схемой.

Если какой-либо контактно-контактный калибр регистрирует замкнутую цепь, то между контактом 29 и этим штифтом имеется электрическое соединение.

Ремонт или замена OEM проводов жгута. См. процедуру 019-071.

Если цепь на всех штифтах измеряет открытую цепь, проблема заключается в стороне проводов двигателя. Ремонт или замена ремня электропроводки двигателя. См. процедуру[[82-019-043-tr — Engine Wiring Harness|019-043]].

После ремонта подсоедините все компоненты.

![[19801621.png]]

### Проверьте короткое замыкание на источнике внешнего напряжения

Отключите сигнализацию запуска двигателя от электропроводки OEM.

Отсоедините разъем электропроводки привода от ECM.

Установите мультиметр для измерения VDC.

Переведите замок зажигания в положение ON.

![[19c00746.png]]

> [!warning] ОСТОРОЖНО
> Для уменьшения возможности повреждения штифта и проводов жгута проводов используйте пробный щуп, номер детали 3822917 и 3822758, при проведении измерений.

Прикосновение к одному из мультиметров приводит к контакту 25 привода проводов ремня разъема.

Прикоснитесь к другому мультиметру, который приведет к заземлению блока двигателя.

Считайте показания мультиметра.

![[19c00741.png]]

Мультиметр **must** отображает показания менее 1,5 VDC.

Если напряжение превышает 1,5 ВДК, то происходит короткое замыкание к внешнему источнику напряжения.

> [!note] Примечание
> Внешним источником напряжения является любой провод в OEM или проводах двигателя, который несет напряжение.

Изолируйте короткое замыкание к OEM-проводах или электропроводке двигателя.

![[19c00724.png]]

Выключите зажигание для подключения/отключения соответствующих разъемов. Отключите 31-контактный OEM-разъем.

Переведите замок зажигания в положение ON.

Прикосновение к одному из мультиметров приводит к контакту 29 31-контактного OEM-разъема проводов жгута проводов, OEM-проводов жгута проводов стороны.

Прикоснитесь к другому мультиметру, который приведет к заземлению блока двигателя.

Считайте показания мультиметра.

![[19c00742.png]]

Мультиметр **must** отображает показания менее 1,5 VDC.

Если напряжение превышает 1,5 ВДК, на стороне OEM-проводов есть короткое замыкание к внешнему источнику напряжения. Если напряжение меньше 1,5 ВДК, короткое замыкание к внешнему источнику напряжения находится на стороне проводов двигателя.

> [!note] Примечание
> Внешним источником напряжения является любой провод в OEM или проводах двигателя, который несет напряжение.

Удалите внешний источник напряжения.

После ремонта подсоедините все компоненты.

![[19c00724.png]]


> [!quote]- Original (English) · английский оригинал
> ### Resistance Check
>
> Turn the keyswitch to the OFF position.
>
> Disconnect the engine start alarm from the OEM harness.
>
> Disconnect the 31-pin OEM connector.
>
> Set the multimeter to measure resistance.
>
> **CAUTION · Осторожно**
> To reduce the possibility of pin and harness damage, use test leads, Part Number 3822917 and 3822758, when taking a measurement.
>
> Touch one of the multimeter leads to the supply wire, pin B (or 2), of the engine start alarm harness connector. Touch the other multimeter lead to pin 29 of the 31-pin OEM connector, OEM harness side. Read the value displayed on the multimeter.
>
> Repeat the resistance check for the return wire. Measure the resistance from the return wire, pin A (or 1), of the engine start alarm harness connector to pin 28 of the 31-pin OEM connector, OEM harness side. Read the value displayed on the multimeter.
>
> For both pin checks, the multimeter **must** display a reading of less than 10 ohms, which is a closed circuit.
>
> If the circuit is **not** closed, repair or replace the OEM harness. Refer to Procedure [[99-019-202 — Metripack Connector Series|019-202]] or 019-071.
>
> Disconnect the actuator harness connector from the ECM.
>
> Touch one of the multimeter leads to pin 29 of the 31-pin OEM connector, engine harness side.
>
> Touch the other multimeter lead to pin 25 of the actuator harness connector.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of less than 10 ohms, which is a closed circuit.
>
> If the circuit is **not** closed, repair or replace the OEM harness. Refer to Procedure [[82-019-043-tr — Engine Wiring Harness|019-043]].
>
> Then check the resistance of the return wire. Touch one of the multimeter leads to pin 28 of the 31-pin OEM connector, engine harness side. Touch the other multimeter lead to pin 32 of the actuator harness connector. Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of less than 10 ohms, which is a closed circuit. If the circuit is **not** closed, repair or replace the engine harness.
>
> Refer to Procedure [[82-019-043-tr — Engine Wiring Harness|019-043]].
>
> Connect all components after completing the repair.
>
> ### Check for Short Circuit to Ground
>
> Turn the keyswitch to the OFF position.
>
> Disconnect the engine start alarm from the OEM harness.
>
> Disconnect the actuator harness connector from the ECM.
>
> Set the multimeter to measure resistance.
>
> **CAUTION · Осторожно**
> To reduce the possibility of pin and harness damage, use test leads, Part Number 3822917 and 3822758, when taking a measurement.
>
> Touch one of the multimeter leads to pin 25 of the actuator harness connector.
>
> Touch the other multimeter lead to engine block ground.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of more than 100k ohms, which is an open circuit.
>
> If the circuit is **not** open, there is a short circuit to ground.
>
> Isolate the short circuit to the OEM harness or engine harness.
>
> Disconnect the 31-pin OEM connector.
>
> Touch one of the multimeter leads to pin 29 of the 31-pin OEM connector, OEM harness side.
>
> Touch the other multimeter lead to engine block ground.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of more than 100k ohms, which is an open circuit.
>
> If the circuit is **not** open, repair or replace the OEM harness. Refer to Procedure 019-071. If the circuit is open, the short is in the engine harness. Repair or replace the engine harness. Refer to Procedure [[82-019-043-tr — Engine Wiring Harness|019-043]].
>
> Connect all components after completing the repair.
>
> ### Check for Short Circuit from Pin to Pin
>
> Turn the keyswitch to the OFF position.
>
> Disconnect the engine start alarm from the OEM harness.
>
> Disconnect the actuator harness connector from the ECM.
>
> Set the multimeter to measure resistance.
>
> **CAUTION · Осторожно**
> To reduce the possibility of pin and harness damage, use test leads, Part Number 3822917 and 3822758, when taking a measurement.
>
> Touch one of the multimeter leads to pin 25 of the actuator harness connector.
>
> Touch the other multimeter lead to all other pins in the connector, one at a time
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of more than 100k ohms, which is an open circuit.
>
> If any pin-to-pin measurement registers a closed circuit, there is a short circuit from pin 25 to that pin.
>
> Isolate the short to the OEM or engine harness.
>
> Disconnect the 31-pin OEM connector.
>
> Touch one of the multimeter leads to pin 29 of the 31-pin OEM harness connector, OEM harness side.
>
> Touch the other multimeter lead to all other pins in the connector, one at a time
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of more than 100k ohms, which is an open circuit.
>
> If any pin-to-pin measurement registers a closed circuit, there is an electrical connection between pin 29 and that pin.
>
> Repair or replace the OEM harness. Refer to Procedure 019-071.
>
> If the circuit at all pins measures an open circuit, the problem is on the engine harness side. Repair or replace the engine harness. Refer to Procedure [[82-019-043-tr — Engine Wiring Harness|019-043]].
>
> Connect all components after completing the repair.
>
> ### Check for Short Circuit to External Voltage Source
>
> Disconnect the engine start alarm from the OEM harness.
>
> Disconnect the actuator harness connector from the ECM.
>
> Set the multimeter to measure VDC.
>
> Turn the keyswitch to the ON position.
>
> **CAUTION · Осторожно**
> To reduce the possibility of pin and harness damage, use test leads, Part Number 3822917 and 3822758, when taking a measurement.
>
> Touch one of the multimeter leads to pin 25 of the actuator harness connector.
>
> Touch the other multimeter lead to engine block ground.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of less than 1.5 VDC.
>
> If the voltage is more than 1.5 VDC, there is a short circuit to an external voltage source.
>
> **Note · Примечание**
> An external voltage source is any wire in the OEM or engine harness that carries voltage.
>
> Isolate the short circuit to the OEM harness or engine harness.
>
> Turn the keyswitch off to connect/disconnect the appropriate connectors. Disconnect the 31-pin OEM connector.
>
> Turn the keyswitch to the ON position.
>
> Touch one of the multimeter leads to pin 29 of the 31-pin OEM harness connector, OEM harness side.
>
> Touch the other multimeter lead to engine block ground.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of less than 1.5 VDC.
>
> If the voltage is more than 1.5 VDC, there is a short circuit to an external voltage source on the OEM harness side. If the voltage is less than 1.5 VDC, the short circuit to an external voltage source is on the engine harness side.
>
> **Note · Примечание**
> An external voltage source is any wire in the OEM or engine harness that carries voltage.
>
> Remove the external voltage source.
>
> Connect all components after completing the repair.
