---
type: "Процедура"
doc: "97-019-309"
title_en: "Thermostat Signal Circuit"
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
figures: 36
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-019-309.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-019-309.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "двигатель/QSX15"
  - "группа/97"
  - "перевод/машинный"
---

# Thermostat Signal Circuit

> [!abstract] Процедура · `97-019-309`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSM11, QSX15
> **Входит в руководства:** [[3666415 — ICON Idle Control System Master Repair Manual|3666415]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-06-13
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-019-309.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-019-309.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Проверка сопротивления

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы избежать травм, всегда проветривайте моторное отделение перед обслуживанием батарей. Чтобы избежать дуги, сначала удалите отрицательный (-) кабель батареи и прикрепите отрицательный (-) кабель батареи последним.

Переведите замок зажигания в положение OFF. Отсоедините кабели аккумулятора автомобиля от батареи.

> [!note] Примечание
> Отключение аккумуляторных батарей автомобиля может потребовать сброса часов ECM в режиме реального времени с помощью INSITETM.

![[ea8coha.png]]

Отсоедините термостат кабины от термостата кабины.

Отключите модуль управления ICONTM Idle Разъем А.

Установите мультиметр для измерения сопротивления.

![[19802871.png]]

> [!warning] ОСТОРОЖНО
> Чтобы избежать повреждения штифта и проводов, используйте пробный щуп, номер детали 3822758 и 3822917, при проведении измерения.

Прикосновение к одному из мультиметров приводит к контакту 3 кабины термостата с прыжком проводов жгута разъема (на конце, который соединяется с термостатом).

Прикосновение к другому мультиметру приводит к контакту 4 с неработающим модулем управления ICONTM Разъем проводов жгута.

Прочитайте значение, отображаемое на многометровом дисплее.

![[19802928.png]]

Мультиметр **должен **отображать значение менее 10 Ом, что является замкнутой схемой.

Если цепь **не** закрыта, изолируйте проблемную область от жгута кабины или части жгута двигателя ICONTM.

![[19801619.png]]

Отсоедините 14-контактный проходной разъем на брандмауэре автомобиля.

Прикосновение к одному из мультиметров приводит к контакту 4 с неработающим модулем управления ICONTM Разъем проводной упряжки.

Прикосновение к другому мультиметру приводит к контакту В 14-контактного пропускного разъема, проводов двигателя с ремнями безопасности.

Прочитайте значение, отображаемое на многометровом дисплее.

![[19c00930.png]]

Мультиметр **должен **отображать значение менее 10 Ом, что является замкнутой схемой. Если схема **не** закрыта, отремонтируйте или замените электропроводку двигателя ICONTM. См. процедуру 019-200, 019-208 или[[97-019-043 — Engine Wiring Harness|019-043.]]

Если цепь закрыта, изолируйте проблему от электропроводки кабины или термостата кабины.

![[19801619.png]]

Отсоедините термостат кабины от электропроводки кабины.

Прикосновение к одному из мультиметров приводит к контакту 3 кабины проводов ремня термостата с проводкой ремня разъема, 4-контактного разъёма, который крепится к кабине проводов ремня.

Прикосновение к другому мультиметру приводит к контакту В 14-контактного пропускного разъема, проводов кабины с ремнями безопасности.

Прочитайте значение, отображаемое на многометровом дисплее.

![[19802929.png]]

Мультиметр **должен **отображать значение менее 10 Ом, что является замкнутой схемой.

Если цепь **не** закрыта, отремонтируйте или замените проводку кабины. См. процедуру 019-200, 019-204 или[[97-019-305 — Cab Wiring Harness|019-305]].

![[19801619.png]]

Проверьте термостат кабины прыгуна проводов.

Прикосновение к одному из мультиметров приводит к контакту 3 кабины термостата с прыжком проводов жгута разъема на конце, который соединяется с термостатом.

Прикосновение к другому мультиметру приводит к контакту 3 кабины термостата с прыжком проводов разъема жгута на конце, который соединяется с кабины проводов жгута.

Считайте показания мультиметра.

![[19c00971.png]]

Мультиметр **должен **отображать значение менее 10 Ом, что является замкнутой схемой.

Если схема **не** закрыта, отремонтируйте или замените электропроводку кабины термостата. См. процедуру 019-204 или[[97-019-295 — Cab Thermostat Harness|019-295]].

После ремонта подсоедините все компоненты.

![[19801619.png]]

### Проверка на замыкание на массу

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы избежать травм, всегда проветривайте моторное отделение перед обслуживанием батарей. Чтобы избежать дуги, сначала удалите отрицательный (-) кабель батареи и прикрепите отрицательный (-) кабель батареи последним.

Переведите замок зажигания в положение OFF. Отсоедините кабели аккумулятора автомобиля от батареи.

> [!note] Примечание
> Отключение аккумуляторных батарей автомобиля может потребовать сброса часов ECM в режиме реального времени с помощью INSITETM.

![[ea8coha.png]]

Отключите модуль управления ICONTM Idle Разъем А.

Отсоедините термостат кабины от электропроводки прыгуна от термостата.

Установите мультиметр для измерения сопротивления.

![[19c00928.png]]

> [!warning] ОСТОРОЖНО
> Чтобы избежать повреждения штифта и проводов, используйте пробный щуп, номер детали 3822758 и 3822917, при проведении измерения.

Прикосновение к одному из мультиметров приводит к контакту 4 с неработающим модулем управления ICONTM Разъем проводной упряжки.

Прикоснитесь к другому мультиметру, который ведет на землю.

Прочитайте значение, отображаемое на многометровом дисплее.

![[19c00932.png]]

Мультиметр **must** отображает показания более 100k ом, что является открытой схемой.

Если схема **не **открыта, есть короткое замыкание на землю.

Изолируйте короткое замыкание от проводной упряжки кабины, проводной упряжки термостата кабины или части проводной упряжки двигателя ICONTM.

![[19801621.png]]

Отсоедините 14-контактный проходной разъем на брандмауэре автомобиля.

Прикосновение к одному из мультиметров приводит к контакту В 14-контактного пропускного разъема, проводов двигателя с ремнями безопасности.

Прикоснитесь к другому мультиметру, который ведет на землю.

Прочитайте значение, отображаемое на многометровом дисплее.

![[19c00940.png]]

Мультиметр **must** отображает показания более 100k ом, что является открытой схемой.

Если схема **не **открыта, в ремне электропроводки двигателя ICONTM есть короткое замыкание. Ремонт или замена ремня электропроводки двигателя ICONTM. См. процедуру 019-200 или[[97-019-043 — Engine Wiring Harness|019-043]].

Если цепь открыта, короткое замыкание находится на стороне проводов кабины / кабины термостата. Изолируйте короткую к соответствующей проводах упряжку.

![[19801621.png]]

Отсоедините коннектор кабины термостата от проводов кабины.

Прикосновение к одному из мультиметров приводит к контакту 3 кабины термостата с проводным разъемом (на кабине проводной ремни).

Прикоснитесь к другому мультиметру, который ведет на землю.

Считайте показания мультиметра.

![[19802892.png]]

Мультиметр **must** отображает показания более 100k ом, что является открытой схемой. Если схема **не **открыта, в кабине электропроводки есть короткое замыкание для заземления. Ремонт или замена кабины проводов ремня. См. процедуру 019-204 или[[97-019-305 — Cab Wiring Harness|019-305]].

Если цепь открыта, то короткое находится в кабине термостата прыгуна проводов. Ремонт или замена кабины термостата прыгуна проводов. См. процедуру 019-204 или[[97-019-295 — Cab Thermostat Harness|019-295]].

После ремонта подсоедините все компоненты.

![[19801621.png]]

### Проверка на замыкание между контактами

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы избежать травм, всегда проветривайте моторное отделение перед обслуживанием батарей. Чтобы избежать дуги, сначала удалите отрицательный (-) кабель батареи и прикрепите отрицательный (-) кабель батареи последним.

Переведите замок зажигания в положение OFF. Отсоедините кабели аккумулятора автомобиля от батареи.

> [!note] Примечание
> Отключение соединений автомобиля может потребовать сброса часов ECM двигателя в режиме реального времени с помощью INSITE.

![[ea8coha.png]]

> [!warning] ОСТОРОЖНО
> Чтобы избежать повреждения штифта и проводов, используйте пробный щуп, номер детали 3822758 и 3822917, при проведении измерения.

Отключите модуль управления ICONTM Idle Разъем А.

Прикосновение к одному из мультиметров приводит к контакту 4 с неработающим модулем управления ICONTM Разъем проводной упряжки.

Прикосновение к другому мультиметру приводит ко всем другим штифтам в разъеме, по одному за раз.

Считайте показания мультиметра.

![[19c00943.png]]

Мультиметр **must** отображает показания более 100k ом, что является открытой схемой.

Если схема **не** открыта, то есть короткое замыкание от контакта 4 до любого другого штифта, который зарегистрировал замкнутую цепь.

Изолируйте короткое замыкание к кабине электропроводки, кабине термостата прыгуна проводов, или ICONTM двигатель проводов ремня.

![[19801621.png]]

Отсоедините 14-контактный проходной разъем на брандмауэре автомобиля.

Прикосновение к одному из мультиметров приводит к контакту В 14-контактного пропускного разъема, проводов двигателя с ремнями безопасности.

Прикосновение к другому мультиметру приводит ко всем другим штифтам в разъеме, по одному за раз.

Считайте показания мультиметра.

![[19c00942.png]]

Мультиметр **must** отображает показания более 100k ом, что является открытой схемой. Если схема не открыта, между контактом В и любым другим штифтом, который зарегистрировал замкнутую цепь, есть короткое замыкание.

Ремонт или замена ремня электропроводки двигателя ICONTM. См. процедуру 019-200, 019-208 или[[97-019-043 — Engine Wiring Harness|019-043]].

Если схема открыта, проверьте упряжку кабины и термостатную часть проводов кабины.

![[19801621.png]]

Отсоедините термостат кабины от электропроводки кабины.

Прикосновение к одному из мультиметров приводит к контакту В 14-контактного пропускного разъема, проводов кабины с ремнями безопасности.

Прикосновение к другому мультиметру приводит ко всем другим штифтам в разъеме, по одному за раз.

Считайте показания мультиметра.

![[19c00935.png]]

Мультиметр **must** отображает показания более 100k ом, что является открытой схемой.

Если схема не открыта, между контактом В и любым другим штифтом, который зарегистрировал замкнутую цепь, есть короткое замыкание.

Ремонт или замена кабины проводов ремня. См. процедуру 019-200 или[[97-019-305 — Cab Wiring Harness|019-305]].

Если все проверки контакта с контактом открыты, изолируйте короткое замыкание от электропроводки термостата кабины.

![[19801621.png]]

Отсоедините коннектор кабины термостата от проводов кабины.

Прикосновение к одному из мультиметров приводит к контакту 3 кабины термостата с прыжком проводов жгута разъема, на стороне, которая соединяется с кабины проводов жгута.

Прикосновение к другому мультиметру приводит ко всем другим штифтам в разъеме.

Считайте показания мультиметра.

![[19c00941.png]]

Мультиметр должен отображать показания более 100k ом. Если цепь закрыта, между контактом 3 и любым другим штифтом, который зарегистрировал замкнутую цепь, есть короткое замыкание. Ремонт или замена кабины термостата прыгуна проводов. См. процедуру 019-204 или[[97-019-295 — Cab Thermostat Harness|019-295]].

После ремонта проводов кабины жгута соединительной части кабины термостата смыкающего жгута, повторите контактно-контактную проверку, свяжитесь 3 со всеми другими штифтами. Если цепь все еще закрыта, концом термостата кабины термостата является проблемный разъем. Ремонт разъема или замена кабины термостата прыгуна проводов.

После ремонта подсоедините все компоненты.

![[19801621.png]]

### Проверьте короткое замыкание на источнике внешнего напряжения

> [!warning] ОСТОРОЖНО
> Чтобы избежать повреждения штифта и проводов, используйте пробный щуп, номер детали 3822758 и 3822917, при проведении измерения.

Переведите замок зажигания в положение OFF.

Отключите модуль управления ICONTM Idle Разъем А.

Установите мультиметр для измерения VDC.

![[19c00928.png]]

Переведите замок зажигания в положение ON.

Прикосновение к одному из мультиметров приводит к контакту 4 с неработающим модулем управления ICONTM Разъем проводной упряжки.

Прикоснитесь к другому мультиметру, который ведет на землю.

Считайте показания мультиметра.

![[19c00932.png]]

Мультиметр **must** отображает показания менее 0,5 VDC. Если напряжение **не** меньше 0,5 ВДК, то происходит короткое замыкание к внешнему источнику напряжения.

> [!note] Примечание
> Внешним источником напряжения является любой провод в кабине или проводка двигателя ICONTM, которая несет напряжение.

Изолируйте область короткого к внешнему источнику напряжения.

![[19c00954.png]]

Отсоедините 14-контактный проходной разъем на брандмауэре автомобиля.

Прикосновение к одному из мультиметров приводит к контакту В 14-контактного пропускного разъема, проводов двигателя с ремнями безопасности.

Прикоснитесь к другому мультиметру, который ведет на землю.

Считайте показания мультиметра.

![[19c00940.png]]

Мультиметр **must** отображает показания менее 0,5 VDC. Если напряжение **не **менее 0,5 ВДК, на стороне ремня электропроводки двигателя ICONTM имеется короткое замыкание к внешнему источнику напряжения. Удалите внешний источник напряжения.

Если напряжение составляет 0,5 ВДК или менее, внешний источник напряжения находится на стороне проводов кабины. Проверьте проводку кабины на стороне цепи.

![[19c00954.png]]

Прикосновение к одному из мультиметров приводит к контакту В 14-контактного пропускного разъема, проводов кабины с ремнями безопасности.

Прикоснитесь к другому мультиметру, который ведет на землю.

Считайте показания мультиметра.

![[19c00935.png]]

Мультиметр **must** отображает показания менее 0,5 VDC. Если напряжение **не** менее 0,5 ВДК, изолируйте короткое замыкание от внешнего источника напряжения к кабине электропроводки или кабине термостата электропроводки ремня.

![[19c00954.png]]

Отсоедините термостат кабины от электропроводки кабины.

Прикосновение к одному из мультиметров приводит к контакту 3 кабины термостата с прыгунной проводкой разъема жгута на кабину жгута проводов.

Прикоснитесь к другому мультиметру, который ведет на землю.

Считайте показания мультиметра.

![[19802892.png]]

Мультиметр **must** отображает показания менее 0,5 VDC. Если напряжение **не** менее 0,5 ВДК, то в кабинной электропроводке имеется короткое замыкание к внешнему источнику напряжения.

Если напряжение составляет 0,5 ВДК или менее, короткое замыкание к внешнему источнику напряжения происходит от кабины термостата прыгуна проводов.

Удалите внешний источник напряжения.

После ремонта подсоедините все компоненты.

![[19c00954.png]]


> [!quote]- Original (English) · английский оригинал
> ### Resistance Check
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To avoid personal injury, always ventilate the compartment before servicing the batteries. To avoid arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> Turn the keyswitch to the OFF position. Disconnect the vehicle battery cables from the battery.
>
> **Note · Примечание**
> Disconnecting the vehicle battery connections can require that the engine ECM real-time clock be reset using INSITE™.
>
> Disconnect the cab thermostat jumper harness from the cab thermostat.
>
> Disconnect the ICON™ idle control module A connector.
>
> Set the multimeter to measure resistance.
>
> **CAUTION · Осторожно**
> To avoid pin and harness damage, use test leads, Part Number 3822758 and 3822917, when taking a measurement.
>
> Touch one of the multimeter leads to pin 3 of the cab thermostat jumper harness connector (on the end that connects to the thermostat).
>
> Touch the other multimeter lead to pin 4 of the ICON™ idle control module A harness connector.
>
> Read the value displayed on the multimeter display.
>
> The multimeter **must** display a reading of less than 10 ohms, which is a closed circuit.
>
> If the circuit is **not** closed, isolate the problem area to the cab harness or ICON™ engine harness portion of the circuit.
>
> Disconnect the 14-pin pass-through connector at the vehicle's firewall.
>
> Touch one of the multimeter leads to pin 4 of the ICON™ idle control module A harness connector.
>
> Touch the other multimeter lead to pin B of the 14-pin pass-through connector, engine harness side.
>
> Read the value displayed on the multimeter display.
>
> The multimeter **must** display a reading of less than 10 ohms, which is a closed circuit. If the circuit is **not** closed, repair or replace the ICON™ engine harness. Refer to Procedure 019-200, 019-208, or [[97-019-043 — Engine Wiring Harness|019-043.]]
>
> If the circuit is closed, isolate the problem to the cab harness or cab thermostat jumper harness.
>
> Disconnect the cab thermostat jumper harness from the cab harness.
>
> Touch one of the multimeter leads to pin 3 of the cab harness thermostat harness connector, the 4-pin connector that is attached to the cab harness.
>
> Touch the other multimeter lead to pin B of the 14-pin pass-through connector, cab harness side.
>
> Read the value displayed on the multimeter display.
>
> The multimeter **must** display a reading of less than 10 ohms, which is a closed circuit.
>
> If the circuit is **not** closed, repair or replace the cab harness. Refer to Procedure 019-200, 019-204, or [[97-019-305 — Cab Wiring Harness|019-305]].
>
> Check the cab thermostat jumper harness.
>
> Touch one of the multimeter leads to pin 3 of the cab thermostat jumper harness connector on the end that connects to the thermostat.
>
> Touch the other multimeter lead to pin 3 of the cab thermostat jumper harness connector on the end that connects to the cab harness.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of less than 10 ohms, which is a closed circuit.
>
> If the circuit is **not** closed, repair or replace the cab thermostat jumper harness. Refer to Procedure 019-204 or [[97-019-295 — Cab Thermostat Harness|019-295]].
>
> Connect all components after completing the repair.
>
> ### Check for Short Circuit to Ground
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To avoid personal injury, always ventilate the compartment before servicing the batteries. To avoid arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> Turn the keyswitch to the OFF position. Disconnect the vehicle battery cables from the battery.
>
> **Note · Примечание**
> Disconnecting the vehicle battery connections can require that the engine ECM real-time clock be reset using INSITE™.
>
> Disconnect the ICON™ idle control module A connector.
>
> Disconnect the cab thermostat jumper harness from the thermostat.
>
> Set the multimeter to measure resistance.
>
> **CAUTION · Осторожно**
> To avoid pin and harness damage, use test leads, Part Number 3822758 and 3822917, when taking a measurement.
>
> Touch one of the multimeter leads to pin 4 of the ICON™ idle control module A harness connector.
>
> Touch the other multimeter lead to ground.
>
> Read the value displayed on the multimeter display.
>
> The multimeter **must** display a reading of more than 100k ohms, which is an open circuit.
>
> If the circuit is **not** open, there is a short circuit to ground.
>
> Isolate the short circuit to the cab harness, cab thermostat jumper harness, or ICON™ engine harness portion of the circuit.
>
> Disconnect the 14-pin pass-through connector at the vehicle's firewall.
>
> Touch one of the multimeter leads to pin B of the 14-pin pass-through connector, engine harness side.
>
> Touch the other multimeter lead to ground.
>
> Read the value displayed on the multimeter display.
>
> The multimeter **must** display a reading of more than 100k ohms, which is an open circuit.
>
> If the circuit is **not** open, there is a short circuit to ground in the ICON™ engine harness. Repair or replace the ICON™ engine harness. Refer to Procedure 019-200 or [[97-019-043 — Engine Wiring Harness|019-043]].
>
> If the circuit is open, the short circuit is on the cab harness/cab thermostat harness side of the circuit. Isolate the short to the appropriate harness.
>
> Disconnect the cab thermostat jumper harness connector from the cab harness.
>
> Touch one of the multimeter leads to pin 3 of the cab thermostat harness connector (on the cab harness).
>
> Touch the other multimeter lead to ground.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of more than 100k ohms, which is an open circuit. If the circuit is **not** open, there is a short circuit to ground in the cab harness. Repair or replace the cab harness. Refer to Procedure 019-204 or [[97-019-305 — Cab Wiring Harness|019-305]].
>
> If the circuit is open, the short is in the cab thermostat jumper harness. Repair or replace the cab thermostat jumper harness. Refer to Procedure 019-204 or [[97-019-295 — Cab Thermostat Harness|019-295]].
>
> Connect all components after completing the repair.
>
> ### Check for Short Circuit from Pin to Pin
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To avoid personal injury, always ventilate the compartment before servicing the batteries. To avoid arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> Turn the keyswitch to the OFF position. Disconnect the vehicle battery cables from the battery.
>
> **Note · Примечание**
> Disconnecting the vehicle connections can require that the engine ECM real-time clock be reset using INSITE.
>
> **CAUTION · Осторожно**
> To avoid pin and harness damage, use test leads, Part Number 3822758 and 3822917, when taking a measurement.
>
> Disconnect the ICON™ idle control module A connector.
>
> Touch one of the multimeter leads to pin 4 of the ICON™ idle control module A harness connector.
>
> Touch the other multimeter lead to all other pins in the connector, one at a time.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of more than 100k ohms, which is an open circuit.
>
> If the circuit is **not** open, there is a short circuit from pin 4 to any other pin that registered a closed circuit.
>
> Isolate the short circuit to the cab harness, cab thermostat jumper harness, or ICON™ engine harness.
>
> Disconnect the 14-pin pass-through connector at the vehicle's firewall.
>
> Touch one of the multimeter leads to pin B of the 14-pin pass-through connector, engine harness side.
>
> Touch the other multimeter lead to all other pins in the connector, one at a time.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of more than 100k ohms, which is an open circuit. If the circuit is **not** open, there is a short circuit between pin B and any other pin that registered a closed circuit.
>
> Repair or replace the ICON™ engine harness. Refer to Procedure 019-200, 019-208, or [[97-019-043 — Engine Wiring Harness|019-043]].
>
> If the circuit is open, check the cab harness and cab thermostat jumper harness portion of the circuit.
>
> Disconnect the cab thermostat jumper harness from the cab harness.
>
> Touch one of the multimeter leads to pin B of the 14-pin pass-through connector, cab harness side.
>
> Touch the other multimeter lead to all other pins in the connector, one at a time.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of more than 100k ohms, which is an open circuit.
>
> If the circuit is **not** open, there is a short circuit between pin B and any other pin that registered a closed circuit.
>
> Repair or replace the cab harness. Refer to Procedure 019-200 or [[97-019-305 — Cab Wiring Harness|019-305]].
>
> If all pin-to-pin checks are open, isolate the short circuit to the cab thermostat jumper harness.
>
> Disconnect the cab thermostat jumper harness connector from the cab harness.
>
> Touch one of the multimeter leads to pin 3 of the cab thermostat jumper harness connector, on the side that connects to the cab harness.
>
> Touch the other multimeter lead to all other pins in the connector.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of more than 100k ohms. If the circuit is closed, there is a short circuit between pin 3 and any other pin that registered a closed circuit. Repair or replace the cab thermostat jumper harness. Refer to Procedure 019-204 or [[97-019-295 — Cab Thermostat Harness|019-295]].
>
> After repairing the cab harness connection end of the cab thermostat jumper harness, repeat the pin-to-pin check, pin 3 to all other pins. If the circuit is still closed, the thermostat end of the cab thermostat harness is the problem connector. Repair the connector or replace the cab thermostat jumper harness.
>
> Connect all components after completing the repair.
>
> ### Check for Short Circuit to External Voltage Source
>
> **CAUTION · Осторожно**
> To avoid pin and harness damage, use test leads, Part Number 3822758 and 3822917, when taking a measurement.
>
> Turn the keyswitch to the OFF position.
>
> Disconnect the ICON™ idle control module A connector.
>
> Set the multimeter to measure VDC.
>
> Turn the keyswitch to the ON position.
>
> Touch one of the multimeter leads to pin 4 of the ICON™ idle control module A harness connector.
>
> Touch the other multimeter lead to ground.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of less than 0.5 VDC. If the voltage is **not** less than 0.5 VDC, there is a short circuit to an external voltage source.
>
> **Note · Примечание**
> An external voltage source is any wire in the cab or ICON™ engine harness wiring that carries voltage.
>
> Isolate the area of the short to external voltage source.
>
> Disconnect the 14-pin pass-through connector at the vehicle's firewall.
>
> Touch one of the multimeter leads to pin B of the 14-pin pass-through connector, engine harness side.
>
> Touch the other multimeter lead to ground.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of less than 0.5 VDC. If the voltage is **not** less than 0.5 VDC, there is a short circuit to an external voltage source on the ICON™ engine harness side of the circuit. Remove the external voltage source.
>
> If the voltage is 0.5 VDC or less, the external voltage source is on the cab harness side of the circuit. Check the cab harness side of the circuit.
>
> Touch one of the multimeter leads to pin B of the 14-pin pass-through connector, cab harness side.
>
> Touch the other multimeter lead to ground.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of less than 0.5 VDC. If the voltage is **not** less than 0.5 VDC, isolate the short circuit to external voltage source to the cab harness or the cab thermostat jumper harness.
>
> Disconnect the cab thermostat jumper harness from the cab harness.
>
> Touch one of the multimeter leads to pin 3 of the cab thermostat jumper harness connector on the cab harness.
>
> Touch the other multimeter lead to ground.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of less than 0.5 VDC. If the voltage is **not** less than 0.5 VDC, there is a short circuit to an external voltage source in the cab harness.
>
> If the voltage is 0.5 VDC or less, the short circuit to the external voltage source is originating from the cab thermostat jumper harness.
>
> Remove the external voltage source.
>
> Connect all components after completing the repair.
