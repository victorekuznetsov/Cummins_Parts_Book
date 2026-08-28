---
aliases:
  - "Цепь датчика температуры наружного воздуха"
type: "Процедура"
doc: "82-019-135"
title_en: "Ambient Air Temperature Sensor Circuit"
title_ru: "Цепь датчика температуры наружного воздуха"
modified: "2006-05-12"
engines:
  - "41343322"
  - "41370103"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 15
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-135.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-019-135.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# Ambient Air Temperature Sensor Circuit
**Цепь датчика температуры наружного воздуха**

> [!abstract] Процедура · `82-019-135`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section 19 - Electronic Engine Controls
> **Даты:** изменён 2006-05-12
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-135.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-019-135.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Проверка сопротивления

Система ICONTM

> [!warning] ОСТОРОЖНО
> Чтобы избежать повреждения штифта и проводов, используйте пробный щуп, номер детали 3822758 и 3822917, при проведении измерения.

Переведите замок зажигания в положение OFF.

Отсоедините датчик температуры окружающего воздуха от проводов датчика температуры.

Отсоедините проводку датчика температуры от термостата кабины.

Установите мультиметр для измерения сопротивления.

![[19c00719.png]]

Прикосновение к одному из мультиметров приводит к проводу питания датчика, контакту 1 (или A), коннектора проводов датчика температуры на конце датчика температуры окружающего воздуха проводов.

Прикосновение к другому мультиметру приводит к датчику питания провода, контакту 1 (или A), от датчика температуры проводов жгута разъёма на кабине термостата конца проводов жгута.

Считайте показания мультиметра.

![[19c00720.png]]

Мультиметр **должен** отображать значение менее 10 Ом, что является замкнутой схемой.

Если цепь открыта, отремонтируйте или замените проводку датчика температуры. См. процедуру[[99-019-202 — Metripack Connector Series|019-202]]Процедура 019-071.

![[19801619.png]]

Повторите проверку на обратный провод. Измерьте сопротивление от обратного провода, контакт 2 (или B), на конце датчика температуры датчика проводов ремня к обратному проводу, контакт 3 (или C), на конце термостата проводов ремня. Считайте показания мультиметра.

Мультиметр **должен** отображать значение менее 10 Ом, что является замкнутой схемой.

Если цепь открыта, отремонтируйте или замените проводку датчика температуры. См. процедуру[[99-019-202 — Metripack Connector Series|019-202]]Процедура 019-071.

После ремонта подсоедините все компоненты.

![[19c00720.png]]

### Проверка на замыкание на массу

Система ICONTM

> [!warning] ОСТОРОЖНО
> Чтобы избежать повреждения штифта и проводов, используйте пробный щуп, номер детали 3822758 и 3822917, при проведении измерения.

Переведите замок зажигания в положение OFF.

Отсоедините датчик температуры окружающего воздуха ICONTM от проводов датчика температуры.

Отсоедините проводку датчика температуры от термостата кабины.

Установите мультиметр для измерения сопротивления.

![[19c00719.png]]

Прикосновение одного из мультиметров приводит к подаче провода, контакту 1 (или А), от датчика температуры проводов жгута разъема на кабину термостата конца проводов жгута.

Прикоснитесь к другому мультиметру, который ведет на землю.

Считайте показания мультиметра.

![[19c00721.png]]

Мультиметр **must** отображает более 100k ом, что является открытой схемой. Если схема **не** открыта, есть короткое замыкание на землю.

Ремонт или замена датчика температуры проводов жгута. См. процедуру[[99-019-202 — Metripack Connector Series|019-202]]Процедура 019-071.

![[19801621.png]]

Прикосновение одного из мультиметров приводит к возвратному проводу, контакту 2 (или B), от датчика температуры проводов жгута разъема на кабине термостата конца проводов жгута. Прикоснитесь к другому мультиметру, который ведет на землю. Считайте показания мультиметра.

Мультиметр **must** отображает более 100k ом (открытая схема). Если схема **не** открыта, есть короткое замыкание на землю.

Ремонт или замена датчика температуры проводов жгута. См. процедуру[[99-019-202 — Metripack Connector Series|019-202]]Процедура 019-071.

После ремонта подсоедините все компоненты.

![[19c00721.png]]

### Проверка на замыкание между контактами

Система ICONTM

> [!warning] ОСТОРОЖНО
> Чтобы избежать повреждения штифта и проводов, используйте пробный щуп, номер детали 3822758 и 3822917, при проведении измерения.

Переведите замок зажигания в положение OFF.

Отсоедините датчик температуры окружающего воздуха ICONTM от проводов датчика температуры.

Отсоедините проводку датчика температуры от термостата кабины.

Установите мультиметр для измерения сопротивления.

![[19c00719.png]]

Прикосновение одного из мультиметров приводит к подаче провода, контакту 1 (или А), датчика температуры проводов жгута разъёма, кабины термостата конца проводов жгута.

Прикоснитесь к другому мультиметру, который ведет к обратному проводу, контакту 3 (или C) разъема.

Считайте показания мультиметра.

![[19c00722.png]]

Мультиметр **must** отображает более 100k ом, что является открытой схемой. Если цепь не открыта, между двумя штифтами есть короткое замыкание.

Ремонт или замена датчика температуры проводов жгута. См. процедуру[[99-019-202 — Metripack Connector Series|019-202]]Процедура 019-071.

После ремонта подсоедините все компоненты.

![[19801621.png]]

### Проверьте короткое замыкание на источнике внешнего напряжения

Система ICONTM

> [!warning] ОСТОРОЖНО
> Чтобы избежать повреждения штифта и проводов, используйте пробный щуп, номер детали 3822758 и 3822917, при проведении измерения.

Отсоедините проводку датчика температуры от термостата кабины.

Установите мультиметр для измерения VDC.

Переведите замок зажигания в положение ON.

![[19c00723.png]]

Прикосновение одного из мультиметров приводит к подаче провода, контакту 1 (или А), от датчика температуры проводов жгута разъема на кабину термостата конца проводов жгута.

Прикоснитесь к другому мультиметру, который ведет на землю.

Считайте показания мультиметра.

![[19c00721.png]]

Мультиметр **must** отображает менее 1,5 VDC. Если контур **не** менее 1,5 ВДК, то имеется короткое замыкание к внешнему источнику напряжения.

Удалите внешний источник напряжения.

> [!note] Примечание
> Внешним источником напряжения является любой провод в проводах датчика температуры, который несет напряжение.

![[19c00724.png]]

Повторите проверку на обратный провод.

Прикосновение одного из мультиметров приводит к возвратному проводу, контакту 3 (или C), датчика температуры проводов жгута разъёма на кабину термостата конца проводов жгута. Прикоснитесь к другому мультиметру, который ведет на землю.

Считайте показания мультиметра.

Мультиметр **must** отображает менее 1,5 VDC. Если контур **не** менее 1,5 ВДК, то имеется короткое замыкание к внешнему источнику напряжения. Удалите внешний источник напряжения.

После ремонта подсоедините все компоненты.

![[19c00721.png]]


> [!quote]- Original (English) · английский оригинал
> ### Resistance Check
>
> ICON™ System
>
> **CAUTION · Осторожно**
> To avoid pin and harness damage, use test leads, Part Number 3822758 and 3822917, when taking a measurement.
>
> Turn the keyswitch to the OFF position.
>
> Disconnect the ambient air temperature sensor from the temperature sensor harness.
>
> Disconnect the temperature sensor harness from the cab thermostat.
>
> Set the multimeter to measure resistance.
>
> Touch one of the multimeter leads to the sensor supply wire, pin 1 (or A), of the temperature sensor harness connector on the ambient air temperature sensor end of the harness.
>
> Touch the other multimeter lead to the sensor supply wire, pin 1 (or A), of the temperature sensor harness connector on the cab thermostat end of the harness.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of less than 10 ohms, which is a closed circuit.
>
> If the circuit is open, repair or replace the temperature sensor harness. Refer to Procedure [[99-019-202 — Metripack Connector Series|019-202]] or Procedure 019-071.
>
> Repeat the check for the return wire. Measure the resistance from the return wire, pin 2 (or B), at the sensor end of the temperature sensor harness to the return wire, pin 3 (or C), at the thermostat end of the harness. Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of less than 10 ohms, which is a closed circuit.
>
> If the circuit is open, repair or replace the temperature sensor harness. Refer to Procedure [[99-019-202 — Metripack Connector Series|019-202]] or Procedure 019-071.
>
> Connect all components after completing the repair.
>
> ### Check for Short Circuit to Ground
>
> ICON™ System
>
> **CAUTION · Осторожно**
> To avoid pin and harness damage, use test leads, Part Number 3822758 and 3822917, when taking a measurement.
>
> Turn the keyswitch to the OFF position.
>
> Disconnect the ICON™ ambient air temperature sensor from the temperature sensor harness.
>
> Disconnect the temperature sensor harness from the cab thermostat.
>
> Set the multimeter to measure resistance.
>
> Touch one of the multimeter leads to the supply wire, pin 1 (or A), of the temperature sensor harness connector on the cab thermostat end of the harness.
>
> Touch the other multimeter lead to ground.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display more than 100k ohms, which is an open circuit. If the circuit is **not** open, there is a short circuit to ground.
>
> Repair or replace the temperature sensor harness. Refer to Procedure [[99-019-202 — Metripack Connector Series|019-202]] or Procedure 019-071.
>
> Touch one of the multimeter leads to the return wire, pin 2 (or B), of the temperature sensor harness connector on the cab thermostat end of the harness. Touch the other multimeter lead to ground. Read the value displayed on the multimeter.
>
> The multimeter **must** display more than 100k ohms (open circuit). If the circuit is **not** open, there is a short circuit to ground.
>
> Repair or replace the temperature sensor harness. Refer to Procedure [[99-019-202 — Metripack Connector Series|019-202]] or Procedure 019-071.
>
> Connect all components after completing the repair.
>
> ### Check for Short Circuit from Pin to Pin
>
> ICON™ System
>
> **CAUTION · Осторожно**
> To avoid pin and harness damage, use test leads, Part Number 3822758 and 3822917, when taking a measurement.
>
> Turn the keyswitch to the OFF position.
>
> Disconnect the ICON™ ambient air temperature sensor from the temperature sensor harness.
>
> Disconnect the temperature sensor harness from the cab thermostat.
>
> Set the multimeter to measure resistance.
>
> Touch one of the multimeter leads to the supply wire, pin 1 (or A), of the temperature sensor harness connector, cab thermostat end of the harness.
>
> Touch the other multimeter lead to the return wire, pin 3 (or C), of the connector.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display more than 100k ohms, which is an open circuit. If the circuit is **not** open, there is a short circuit between the two pins.
>
> Repair or replace the temperature sensor harness. Refer to Procedure [[99-019-202 — Metripack Connector Series|019-202]] or Procedure 019-071.
>
> Connect all components after completing the repair.
>
> ### Check for Short Circuit to External Voltage Source
>
> ICON™ System
>
> **CAUTION · Осторожно**
> To avoid pin and harness damage, use test leads, Part Number 3822758 and 3822917, when taking a measurement.
>
> Disconnect the temperature sensor harness from the cab thermostat.
>
> Set the multimeter to measure VDC.
>
> Turn the keyswitch to the ON position.
>
> Touch one of the multimeter leads to the supply wire, pin 1 (or A), of the temperature sensor harness connector on the cab thermostat end of the harness.
>
> Touch the other multimeter lead to ground.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display less than 1.5 VDC. If the circuit is **not** less than 1.5 VDC, there is a short circuit to an external voltage source.
>
> Remove the external voltage source.
>
> **Note · Примечание**
> An external voltage source is any wire in the temperature sensor harness that carries voltage.
>
> Repeat the check for the return wire.
>
> Touch one of the multimeter leads to the return wire, pin 3 (or C), of temperature sensor harness connector on the cab thermostat end of the harness. Touch the other multimeter lead to ground.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display less than 1.5 VDC. If the circuit is **not** less than 1.5 VDC, there is a short circuit to an external voltage source. Remove the external voltage source.
>
> Connect all components after completing the repair.
