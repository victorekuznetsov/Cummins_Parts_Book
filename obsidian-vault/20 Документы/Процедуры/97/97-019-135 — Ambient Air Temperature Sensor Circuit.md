---
aliases:
  - "Цепь датчика температуры наружного воздуха"
type: "Процедура"
doc: "97-019-135"
title_en: "Ambient Air Temperature Sensor Circuit"
title_ru: "Цепь датчика температуры наружного воздуха"
modified: "2003-06-13"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
  - "80141463"
  - "80248213"
families:
  - "QSM11"
  - "QSX15"
manuals:
  - "3666415"
figures: 18
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-019-135.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-019-135.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "двигатель/QSX15"
  - "группа/97"
  - "перевод/машинный"
---

# Ambient Air Temperature Sensor Circuit
**Цепь датчика температуры наружного воздуха**

> [!abstract] Процедура · `97-019-135`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSM11, QSX15
> **Входит в руководства:** [[3666415 — ICON Idle Control System Master Repair Manual|3666415]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-06-13
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-019-135.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-019-135.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Проверка сопротивления

> [!warning] ОСТОРОЖНО
> Чтобы избежать повреждения штифта и проводов, используйте пробный щуп, номер детали 3822758, при проведении измерения.

Переведите замок зажигания в положение OFF. Отсоедините датчик температуры окружающего воздуха от проводов датчика температуры.

Установите мультиметр для измерения сопротивления.

![[19c00945.png]]

Отсоедините проводку датчика температуры от термостата кабины.

![[19c00949.png]]

Прикосновение к одному из мультиметров приводит к контакту 1 датчика температуры проводов с помощью разъёма жгута проводов на стороне датчика температуры окружающего воздуха.

Прикосновение к другому мультиметру приводит к контакту 1 датчика температуры с проводкой ремня разъема, кабины термостата боковой.

Считайте показания мультиметра.

![[19c00950.png]]

Мультиметр **должен **отображать значение менее 10 Ом, что является замкнутой схемой.

Если схема **не** закрыта, отремонтируйте неисправный разъём датчика температуры или замените проводку датчика температуры. См. процедуру 019-202, 019-203 или[[97-019-296 — Temperature Sensor Harness|019-296]].

Повторите проверку сопротивления для обратного провода.

![[19801619.png]]

Прикосновение к одному из мультиметров приводит к контакту 2 датчика температуры с проводкой ремня разъема, датчика боковой стороны. Прикосновение к другому мультиметру приводит к контакту 3 датчика температуры с проводкой ремня разъема, кабины термостата боковой. Считайте показания мультиметра.

Мультиметр **должен отображать значение менее 10 Ом. Если схема **не закрыта, отремонтируйте дефектный разъём проводов датчика или замените проводку датчика температуры. См. процедуру 019-202, 019-203 или[[97-019-296 — Temperature Sensor Harness|019-296]].

После ремонта подсоедините все компоненты.

![[19c00950.png]]

### Проверка на замыкание на массу

> [!warning] ОСТОРОЖНО
> Чтобы избежать повреждения штифта и проводов, используйте пробный щуп, номер детали 3822758, при проведении измерения.

Переведите замок зажигания в положение OFF.

Отсоедините датчик температуры окружающего воздуха от проводов датчика температуры.

![[19c00945.png]]

Отсоедините проводку датчика температуры от термостата кабины.

Установите мультиметр для измерения сопротивления.

![[19c00949.png]]

Прикосновение к одному из мультиметров приводит к контакту 1 датчика температуры проводов с помощью разъёма жгута проводов на стороне датчика температуры окружающего воздуха.

Прикоснитесь к другому мультиметру, который ведет на землю.

Считайте показания мультиметра.

![[19c00951.png]]

Мультиметр **must** отображает более 100k ом, что является открытой схемой. Если схема **не **открыта, есть короткое замыкание на землю.

Ремонт или замена датчика температуры проводов жгута. См. процедуру 019-202 или[[97-019-296 — Temperature Sensor Harness|019-296]].

![[19801621.png]]

Прикосновение к одному из мультиметров приводит к контакту 2 датчика температуры проводов разъема жгута на стороне датчика температуры окружающего воздуха. Прикоснитесь к другому мультиметру, который ведет на землю.

Считайте показания мультиметра.

Мультиметр **must** отображает более 100k ом (открытая схема). Если схема **не **открыта, есть короткое замыкание на землю. Ремонт или замена датчика температуры проводов жгута. См. процедуру 019-202 или[[97-019-296 — Temperature Sensor Harness|019-296]].

После ремонта подсоедините все компоненты.

![[19c00951.png]]

### Проверка на замыкание между контактами

> [!warning] ОСТОРОЖНО
> Чтобы избежать повреждения штифта и проводов, используйте пробный щуп, номер детали 3822758, при проведении измерения.

Переведите замок зажигания в положение OFF.

Отсоедините датчик температуры окружающего воздуха от проводов датчика температуры.

![[19c00945.png]]

Отсоедините проводку датчика температуры от термостата кабины.

Установите мультиметр для измерения сопротивления.

![[19c00949.png]]

Прикосновение к одному из мультиметров приводит к контакту 1 датчика температуры с проводкой ремня разъема, кабины термостата боковой. Прикосновение к другому мультиметру приводит к каждому из трех других контактов в разъеме. Повторите проверку контакта с контактом для других 3 контактов в разъеме.

Считайте показания мультиметра.

![[19c00952.png]]

Мультиметр **must** отображает более 100k ом, что является открытой схемой. Если цепь не открыта, между двумя штифтами есть короткое замыкание.

Ремонт или замена датчика температуры проводов жгута. См. процедуру 019-203 или[[97-019-296 — Temperature Sensor Harness|019-296]].

После ремонта подсоедините все компоненты.

![[19801621.png]]

### Проверьте короткое замыкание на источнике внешнего напряжения

> [!warning] ОСТОРОЖНО
> Чтобы избежать повреждения штифта и проводов, используйте пробный щуп, номер детали 3822758, при проведении измерения.

Отсоедините проводку датчика температуры от термостата кабины.

Установите мультиметр для измерения VDC.

Переведите замок зажигания в положение ON.

![[19c00949.png]]

Прикосновение к одному из мультиметров приводит к контакту 1 датчика температуры с проводкой разъема жгута на стороне термостата кабины.

Прикоснитесь к другому мультиметру, который ведет на землю.

Считайте показания мультиметра.

![[19c00953.png]]

Мультиметр **must** отображает менее 0,5 VDC. Если контур **не **менее 0,5 ВДК, то имеется короткое замыкание к внешнему источнику напряжения.

Удалите внешний источник напряжения.

> [!note] Примечание
> Внешним источником напряжения является любой провод в проводах датчика температуры, который несет напряжение.

![[19c00954.png]]

Повторите проверку на обратный провод.

Прикосновение к одному из мультиметров приводит к контакту 3 датчика температуры с проводкой разъема жгута на стороне термостата кабины. Прикоснитесь к другому мультиметру, который ведет на землю.

Считайте показания мультиметра.

Мультиметр **must** отображает менее 0,5 VDC. Если контур **не **менее 0,5 ВДК, то имеется короткое замыкание к внешнему источнику напряжения. Удалите внешний источник напряжения.

После ремонта подсоедините все компоненты.

![[19c00953.png]]


> [!quote]- Original (English) · английский оригинал
> ### Resistance Check
>
> **CAUTION · Осторожно**
> To avoid pin and harness damage, use test lead, Part Number 3822758, when taking a measurement.
>
> Turn the keyswitch to the OFF position. Disconnect the ambient air temperature sensor from the temperature sensor harness.
>
> Set the multimeter to measure resistance.
>
> Disconnect the temperature sensor harness from the cab thermostat.
>
> Touch one of the multimeter leads to pin 1 of the temperature sensor harness connector on the ambient air temperature sensor side.
>
> Touch the other multimeter lead to pin 1 of the temperature sensor harness connector, cab thermostat side.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of less than 10 ohms, which is a closed circuit.
>
> If the circuit is **not** closed, repair the defective temperature sensor harness connector or replace the temperature sensor harness. Refer to Procedure 019-202, 019-203, or [[97-019-296 — Temperature Sensor Harness|019-296]].
>
> Repeat the resistance check for the return wire.
>
> Touch one of the multimeter leads to pin 2 of the temperature sensor harness connector, sensor side. Touch the other multimeter lead to pin 3 of the temperature sensor harness connector, cab thermostat side. Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of less than 10 ohms. If the circuit is **not** closed, repair the defective sensor harness connector or replace the temperature sensor harness. Refer to Procedure 019-202, 019-203, or [[97-019-296 — Temperature Sensor Harness|019-296]].
>
> Connect all components after completing the repair.
>
> ### Check for Short Circuit to Ground
>
> **CAUTION · Осторожно**
> To avoid pin and harness damage, use test lead, Part Number 3822758, when taking a measurement.
>
> Turn the keyswitch to the OFF position.
>
> Disconnect the ambient air temperature sensor from the temperature sensor harness.
>
> Disconnect the temperature sensor harness from the cab thermostat.
>
> Set the multimeter to measure resistance.
>
> Touch one of the multimeter leads to pin 1 of the temperature sensor harness connector on the ambient air temperature sensor side.
>
> Touch the other multimeter lead to ground.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display more than 100k ohms, which is an open circuit. If the circuit is **not** open, there is a short circuit to ground.
>
> Repair or replace the temperature sensor harness. Refer to Procedure 019-202 or [[97-019-296 — Temperature Sensor Harness|019-296]].
>
> Touch one of the multimeter leads to pin 2 of the temperature sensor harness connector on the ambient air temperature sensor side. Touch the other multimeter lead to ground.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display more than 100k ohms (open circuit). If the circuit is **not** open, there is a short circuit to ground. Repair or replace the temperature sensor harness. Refer to Procedure 019-202 or [[97-019-296 — Temperature Sensor Harness|019-296]].
>
> Connect all components after completing the repair.
>
> ### Check for Short Circuit from Pin to Pin
>
> **CAUTION · Осторожно**
> To avoid pin and harness damage, use test lead, Part Number 3822758, when taking a measurement.
>
> Turn the keyswitch to the OFF position.
>
> Disconnect the ambient air temperature sensor from the temperature sensor harness.
>
> Disconnect the temperature sensor harness from the cab thermostat.
>
> Set the multimeter to measure resistance.
>
> Touch one of the multimeter leads to pin 1 of the temperature sensor harness connector, cab thermostat side. Touch the other multimeter lead to each of the other three pins in the connector. Repeat the pin-to-pin check for the other 3 pins in the connector.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display more than 100k ohms, which is an open circuit. If the circuit is **not** open, there is a short circuit between the two pins.
>
> Repair or replace the temperature sensor harness. Refer to Procedure 019-203 or [[97-019-296 — Temperature Sensor Harness|019-296]].
>
> Connect all components after completing the repair.
>
> ### Check for Short Circuit to External Voltage Source
>
> **CAUTION · Осторожно**
> To avoid pin and harness damage, use test lead, Part Number 3822758, when taking a measurement.
>
> Disconnect the temperature sensor harness from the cab thermostat.
>
> Set the multimeter to measure VDC.
>
> Turn the keyswitch to the ON position.
>
> Touch one of the multimeter leads to pin 1 of temperature sensor harness connector on the cab thermostat side.
>
> Touch the other multimeter lead to ground.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display less than 0.5 VDC. If the circuit is **not** less than 0.5 VDC, there is a short circuit to an external voltage source.
>
> Remove the external voltage source.
>
> **Note · Примечание**
> An external voltage source is any wire in the temperature sensor harness that carries voltage.
>
> Repeat the check for the return wire.
>
> Touch one of the multimeter leads to pin 3 of temperature sensor harness connector on the cab thermostat side. Touch the other multimeter lead to ground.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display less than 0.5 VDC. If the circuit is **not** less than 0.5 VDC, there is a short circuit to an external voltage source. Remove the external voltage source.
>
> Connect all components after completing the repair.
