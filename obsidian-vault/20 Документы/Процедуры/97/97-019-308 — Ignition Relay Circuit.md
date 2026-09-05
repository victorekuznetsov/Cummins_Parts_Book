---
aliases:
  - "Цепь реле зажигания"
type: "Процедура"
doc: "97-019-308"
title_en: "Ignition Relay Circuit"
title_ru: "Цепь реле зажигания"
modified: "2004-10-14"
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
figures: 40
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-019-308.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-019-308.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "двигатель/QSX15"
  - "группа/97"
  - "перевод/машинный"
---

# Ignition Relay Circuit
**Цепь реле зажигания**

> [!abstract] Процедура · `97-019-308`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSM11, QSX15
> **Входит в руководства:** [[3666415 — ICON Idle Control System Master Repair Manual|3666415]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2004-10-14
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-019-308.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-019-308.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Проверка сопротивления

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы избежать травм, всегда проветривайте моторное отделение перед обслуживанием батарей. Чтобы избежать дуги, сначала удалите отрицательный (-) кабель батареи и прикрепите отрицательный (-) кабель батареи последним.

Переведите замок зажигания в положение OFF. Отсоедините кабели аккумулятора автомобиля от батареи. Отсоедините разъемы ICONTM от батареи.

> [!note] Примечание
> Отключение аккумуляторных батарей автомобиля может потребовать сброса часов ECM в режиме реального времени с помощью INSITETM.

![[ea8coha.png]]

Отсоедините реле шины зажигания от электропроводки ICONTM.

Измерить сопротивление от контакта 85 до контакта 86 на реле.

Считайте показания мультиметра. Мультиметр **должен **отображать значение от 70 до 100 Ом.

Измерить сопротивление от контакта 85 реле шины зажигания до контакта 30, 87 и 87А.

Считайте показания мультиметра. Мультиметр должен отображать показания более 100k ом (открытая схема).

![[19803846.png]]

> [!warning] ОСТОРОЖНО
> Чтобы избежать повреждения штифта и проводов, используйте пробный щуп, номер детали 3822758 и 3822917, при проведении измерения.

Отключите разъем B модуля управления ICONTM.

Отключите 14-контактный проход через разъем на брандмауэре автомобиля.

Отсоедините реле зажигания от проводов кабины.

Установите мультиметр для измерения сопротивления.

![[19c00961.png]]

Проверьте выходной провод.

Прикосновение к одному из мультиметров приводит к контакту 4 с неработающим модулем управления ICONTM B проводов ремня разъема.

Прикосновение к другому мультиметру приводит к контакту F 14-контактного пропускного разъема, проводов двигателя с ремнями безопасности.

Считайте показания мультиметра.

![[19c00955.png]]

Мультиметр **должен **отображать значение менее 10 Ом, что является замкнутой схемой.

Если схема **не** закрыта, отремонтируйте или замените электропроводку двигателя ICONTM. См. процедуру[[99-019-208 — Deutsch HDP20 and HD30 Connector Series|019-208]]или[[97-019-043 — Engine Wiring Harness|019-043]].

![[19801619.png]]

Прикосновение к одному из мультиметров приводит к контакту F 14-контактного пропускного разъема, проводов кабины с ремнями безопасности.

Прикосновение к другому мультиметру приводит к контакту 85 с разъемом релейной проводов зажигания шины.

Считайте показания мультиметра.

![[19802925.png]]

Мультиметр **должен **отображать значение менее 10 Ом, что является замкнутой схемой.

Если цепь **не** закрыта, отремонтируйте или замените проводку кабины. См. процедуру[[99-019-204 — Deutsch DRC Connector Series|019-204]]или[[97-019-305 — Cab Wiring Harness|019-305]].

![[19801619.png]]

Проверьте обратный провод.

Прикосновение одного из мультиметров приводит к контакту С 14-контактного пропускного разъема, проводов двигателя с ремнями безопасности.

Прикосновение к другому мультиметру приводит к отрицательному (-) посту терминала батареи.

Считайте показания мультиметра.

![[19802926.png]]

Мультиметр **должен **отображать значение менее 10 Ом, что является замкнутой схемой.

Если схема **не** закрыта, отремонтируйте или замените электропроводку двигателя ICONTM. См. процедуру[[99-019-197 — Ring Terminal|019-197]]или[[97-019-043 — Engine Wiring Harness|019-043]].

![[19801619.png]]

Прикосновение к одному из мультиметров приводит к контакту С 14-контактного пропускного разъема, кабины проводов упряжки.

Прикосновение к другому мультиметру приводит к контакту 86 с разъемом релейной проводов шины зажигания.

Считайте показания мультиметра.

![[19802925.png]]

Мультиметр **должен **отображать значение менее 10 Ом, что является замкнутой схемой.

Если цепь **не** закрыта, отремонтируйте или замените проводку кабины. См. процедуру[[99-019-204 — Deutsch DRC Connector Series|019-204]]или[[97-019-305 — Cab Wiring Harness|019-305]].

После ремонта подсоедините все компоненты.

![[19801619.png]]

### Проверка на замыкание на массу

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы избежать травм, всегда проветривайте моторное отделение перед обслуживанием батарей. Чтобы избежать дуги, сначала удалите отрицательный (-) кабель батареи и прикрепите отрицательный (-) кабель батареи последним.

Переведите замок зажигания в положение OFF. Отсоедините кабели аккумулятора автомобиля от батареи. Отсоедините разъемы ICONTM от батареи.

> [!note] Примечание
> Отключение аккумуляторных батарей автомобиля может потребовать сброса часов ECM в режиме реального времени с помощью INSITETM.

![[ea8coha.png]]

> [!warning] ОСТОРОЖНО
> Чтобы избежать повреждения штифта и проводов, используйте пробный щуп, номер детали 3822758 и 3822917, при проведении измерения.

Отключите разъем B модуля управления ICONTM.

Отсоедините 14-контактный проходной разъем на брандмауэре автомобиля.

Отсоедините реле зажигания от проводов кабины.

Установите мультиметр для измерения сопротивления.

![[19c00961.png]]

Прикосновение к одному из мультиметров приводит к контакту 4 с неработающим модулем управления ICONTM B проводов ремня разъема.

Прикоснитесь к другому мультиметру, который ведет на землю.

Считайте показания мультиметра.

![[19802900.png]]

Мультиметр **must** отображает показания более 100k ом, что является открытой схемой.

Если схема **не** открыта, отремонтируйте или замените электропроводку двигателя ICONTM. См. процедуру[[99-019-208 — Deutsch HDP20 and HD30 Connector Series|019-208]]или[[97-019-043 — Engine Wiring Harness|019-043]].

![[19801621.png]]

Прикосновение к одному из мультиметров приводит к контакту F 14-контактного пропускного разъема, ICONTM с проводкой двигателя с ремнями безопасности.

Прикоснитесь к другому мультиметру, который ведет на землю.

Считайте показания мультиметра.

![[19c00940.png]]

Мультиметр **must** отображает показания более 100k ом, что является открытой схемой.

Если схема **не** открыта, отремонтируйте или замените электропроводку двигателя ICONTM. См. процедуру[[97-019-043 — Engine Wiring Harness|019-043]].

![[19801621.png]]

Прикосновение к одному из мультиметров приводит к контакту F 14-контактного пропускного разъема, проводов кабины с ремнями безопасности.

Прикоснитесь к другому мультиметру, который ведет на землю.

Считайте показания мультиметра.

![[19c00933.png]]

Мультиметр **must** отображает показания более 100k ом, что является открытой схемой.

Если цепь **не** закрыта, отремонтируйте или замените проводку кабины. См. процедуру[[97-019-305 — Cab Wiring Harness|019-305]].

![[19801621.png]]

Прикосновение к одному из мультиметров приводит к контакту 86 ретранслятора зажигания шины с проводкой ремня разъема.

Прикоснитесь к другому мультиметру, который ведет на землю.

Считайте показания мультиметра.

![[19802927.png]]

Мультиметр **must** отображает показания более 100k ом, что является открытой схемой.

Если схема **не** открыта, отремонтируйте или замените проводку кабины. См. процедуру[[99-019-204 — Deutsch DRC Connector Series|019-204]]или[[97-019-305 — Cab Wiring Harness|019-305]].

После ремонта подсоедините все компоненты.

![[19801621.png]]

### Проверка на замыкание между контактами

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы избежать травм, всегда проветривайте моторное отделение перед обслуживанием батарей. Чтобы избежать дуги, сначала удалите отрицательный (-) кабель батареи и прикрепите отрицательный (-) кабель батареи последним.

Переведите замок зажигания в положение OFF. Отсоедините кабели аккумулятора автомобиля от батареи. Отсоедините разъемы ICONTM от батареи.

> [!note] Примечание
> Отключение аккумуляторных батарей автомобиля может потребовать сброса часов ECM в режиме реального времени с помощью INSITETM.

![[ea8coha.png]]

> [!warning] ОСТОРОЖНО
> Чтобы избежать повреждения штифта и проводов, используйте пробный щуп, номер детали 3822758 и 3822917, при проведении измерения.

Отключите разъемы ICONTM idle Control module A и B.

Отключите 14-контактный проход через разъем на брандмауэре автомобиля.

Отсоедините реле зажигания от проводов кабины.

Установите мультиметр для измерения сопротивления.

![[19c00917.png]]

Прикосновение к одному из мультиметров приводит к контакту 4 с неработающим модулем управления ICONTM B проводов ремня разъема. Прикосновение к другому мультиметру приводит ко всем другим штифтам в разъеме, по одному за раз.

Считайте показания мультиметра.

![[19c00962.png]]

Затем касание одного из мультиметров приводит к контакту 2 с неработающим модулем управления ICONTM Разъем проводной упряжки. Прикосновение к другому мультиметру приводит ко всем другим штифтам в разъеме, по одному за раз.

Считайте показания мультиметра.

![[19c00943.png]]

Для обеих проверок «контакт-контакт» мультиметр должен отображать показания более 100k ом, что является открытой схемой.

Если схема **не** открыта, отремонтируйте или замените электропроводку двигателя ICONTM. См. процедуру[[99-019-208 — Deutsch HDP20 and HD30 Connector Series|019-208]]или[[97-019-043 — Engine Wiring Harness|019-043]].

![[19801621.png]]

Прикосновение к одному из мультиметров приводит к контакту F 14-контактного пропускного разъема, ICONTM с проводкой двигателя с ремнями безопасности. Прикосновение к другому мультиметру приводит ко всем другим штифтам в разъеме, по одному за раз.

Считайте показания мультиметра.

Повторите контактную проверку от контакта С. Прикосновение к одному из мультиметров приводит к контакту С 14-контактного пропускного разъема, сцепленного с двигателем ICONTM. Прикосновение к другому мультиметру приводит ко всем другим штифтам в разъеме, по одному за раз.

Считайте показания мультиметра.

![[19c00942.png]]

Для обеих проверок «контакт-контакт» мультиметр должен отображать показания более 100k ом, что является открытой схемой.

Если схема **не** открыта, отремонтируйте или замените электропроводку двигателя ICONTM. См. процедуру[[97-019-043 — Engine Wiring Harness|019-043]].

![[19801621.png]]

Прикосновение к одному из мультиметров приводит к контакту F 14-контактного пропускного разъема, проводов кабины с ремнями безопасности. Прикосновение к другому мультиметру приводит ко всем другим штифтам в разъеме, по одному за раз.

Считайте показания мультиметра.

Повторите контактную проверку от контакта С. Прикосновение к одному из мультиметров приводит к контакту С 14-контактного пропускного разъема, кабины проводов упряжки. Прикосновение к другому мультиметру приводит ко всем другим штифтам в разъеме, по одному за раз.

Считайте показания мультиметра.

![[19c00935.png]]

Мультиметр **must** отображает показания более 100k ом, что является открытой схемой.

Если цепь **не** закрыта, отремонтируйте или замените проводку кабины. См. процедуру[[97-019-305 — Cab Wiring Harness|019-305]].

![[19801621.png]]

Прикосновение к одному из мультиметров приводит к контакту 86 ретранслятора зажигания шины с проводкой ремня разъема.

Прикосновение к другому мультиметру приводит ко всем другим штифтам в разъеме релейной проводов ремня, по одному за раз.

Считайте показания мультиметра.

![[19802885.png]]

Мультиметр **must** отображает показания более 100k ом, что является открытой схемой.

Если схема **не** открыта, отремонтируйте или замените проводку кабины. См. процедуру[[99-019-204 — Deutsch DRC Connector Series|019-204]]или[[97-019-305 — Cab Wiring Harness|019-305]].

После ремонта подсоедините все компоненты.

![[19801621.png]]

### Проверка напряжения

> [!warning] ОСТОРОЖНО
> Чтобы избежать повреждения штифта и проводов, используйте пробный щуп, номер детали 3822917, при проведении измерения.

Отсоедините 14-контактный проходной разъем на брандмауэре автомобиля.

Установите мультиметр для измерения VDC.

Переведите замок зажигания в положение ON.

![[15800040.png]]

Прикосновение к одному из мультиметров приводит к контакту F 14-контактного пропускного разъема, проводов кабины с ремнями безопасности.

Прикоснитесь к другому мультиметру, который ведет на землю.

Считайте показания мультиметра.

![[19c00935.png]]

Мультиметр **must** отображает показания менее 0,5 VDC.

Если напряжение **не** менее 0,5 ВДК, отремонтируйте или замените реле шины зажигания. См. процедуру[[99-019-204 — Deutsch DRC Connector Series|019-204]]или[[97-019-301 — Ignition Bus Relay 1 and 2|019-301]].

После ремонта подсоедините все компоненты.

![[19c00954.png]]

### Проверьте короткое замыкание на источнике внешнего напряжения

Переведите замок зажигания в положение OFF. Отключите разъем B модуля управления ICONTM. Установите мультиметр для измерения VDC.

![[19c00961.png]]

> [!warning] ОСТОРОЖНО
> Чтобы избежать повреждения штифта и проводов, используйте пробный щуп, номер детали 3822917, при проведении измерения.

Переведите замок зажигания в положение ON.

Прикосновение к одному из мультиметров приводит к контакту 4 с неработающим модулем управления ICONTM B проводов ремня разъема. Прикоснитесь к другому мультиметру, который ведет на землю.

Измерьте напряжение.

![[19802900.png]]

Мультиметр **must** отображает показания менее 0,5 VDC.

Если напряжение **не** меньше 0,5 ВДК, то происходит короткое замыкание к внешнему источнику напряжения.

> [!note] Примечание
> Внешним источником напряжения является любой провод в кабине или проводах двигателя, который несет напряжение.

Изолируйте короткую часть цепи до нужной.

![[19c00954.png]]

Отсоедините 14-контактный проходной разъем на брандмауэре автомобиля.

Прикосновение к одному из мультиметров приводит к контакту F 14-контактного пропускного разъема, проводов кабины с ремнями безопасности.

Прикоснитесь к другому мультиметру, который ведет на землю.

Считайте показания мультиметра.

![[19c00933.png]]

Мультиметр **must** отображает показания менее 0,5 VDC.

Если напряжение **не** менее 0,5 ВДК, на стороне проводов кабины цепи имеется короткое замыкание к внешнему источнику напряжения.

Если VDC меньше 0,5 VDC, короткое замыкание находится на стороне ремня электропроводки двигателя ICONTM.

Удалите внешний источник напряжения.

После ремонта подсоедините все компоненты.

![[19c00954.png]]


> [!quote]- Original (English) · английский оригинал
> ### Resistance Check
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To avoid personal injury, always ventilate the compartment before servicing the batteries. To avoid arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> Turn the keyswitch to the OFF position. Disconnect the vehicle battery cables from the battery. Disconnect the ICON™ battery harness connectors from the battery.
>
> **Note · Примечание**
> Disconnecting the vehicle battery connections can require that the engine ECM real-time clock be reset using INSITE™.
>
> Disconnect the ignition bus relay from the ICON™ cab wiring harness.
>
> Measure the resistance from pin 85 to pin 86 on the relay.
>
> Read the value displayed on the multimeter. The multimeter **must** display a reading of 70 to 100 ohms.
>
> Measure the resistance from pin 85 of the ignition bus relay(s) to pin 30, 87, and 87A.
>
> Read the value displayed on the multimeter. The multimeter **must** display a reading of more than 100k ohms (open circuit).
>
> **CAUTION · Осторожно**
> To avoid pin and harness damage, use test leads, Part Number 3822758 and 3822917, when taking a measurement.
>
> Disconnect the ICON™ idle control module B connector.
>
> Disconnect the 14-pin pass through connector at the vehicle's firewall.
>
> Disconnect the ignition bus relay from the cab harness.
>
> Set the multimeter to measure resistance.
>
> Check the output wire.
>
> Touch one of the multimeter leads to pin 4 of the ICON™ idle control module B harness connector.
>
> Touch the other multimeter lead to pin F of the 14-pin pass-through connector, engine harness side.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of less than 10 ohms, which is a closed circuit.
>
> If the circuit is **not** closed, repair or replace the ICON™ engine harness. Refer to Procedure [[99-019-208 — Deutsch HDP20 and HD30 Connector Series|019-208]] or [[97-019-043 — Engine Wiring Harness|019-043]].
>
> Touch one of the multimeter leads to pin F of the 14-pin pass-through connector, cab harness side.
>
> Touch the other multimeter lead to pin 85 of the ignition bus relay harness connector.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of less than 10 ohms, which is a closed circuit.
>
> If the circuit is **not** closed, repair or replace the cab harness. Refer to Procedure [[99-019-204 — Deutsch DRC Connector Series|019-204]] or [[97-019-305 — Cab Wiring Harness|019-305]].
>
> Check the return wire.
>
> Touch one of the multimeter leads to pin C of the 14-pin pass-through connector, engine harness side.
>
> Touch the other multimeter lead to the negative (-) battery terminal post.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of less than 10 ohms, which is a closed circuit.
>
> If the circuit is **not** closed, repair or replace the ICON™ engine harness. Refer to Procedure [[99-019-197 — Ring Terminal|019-197]] or [[97-019-043 — Engine Wiring Harness|019-043]].
>
> Touch one of the multimeter leads to pin C of the 14-pin pass-through connector, cab harness side.
>
> Touch the other multimeter lead to pin 86 of the ignition bus relay harness connector.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of less than 10 ohms, which is a closed circuit.
>
> If the circuit is **not** closed, repair or replace the cab harness. Refer to Procedure [[99-019-204 — Deutsch DRC Connector Series|019-204]] or [[97-019-305 — Cab Wiring Harness|019-305]].
>
> Connect all components after completing the repair.
>
> ### Check for Short Circuit to Ground
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To avoid personal injury, always ventilate the compartment before servicing the batteries. To avoid arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> Turn the keyswitch to the OFF position. Disconnect the vehicle battery cables from the battery. Disconnect the ICON™ battery harness connectors from the battery.
>
> **Note · Примечание**
> Disconnecting the vehicle battery connections can require that the engine ECM real-time clock be reset using INSITE™.
>
> **CAUTION · Осторожно**
> To avoid pin and harness damage, use test leads, Part Number 3822758 and 3822917, when taking a measurement.
>
> Disconnect the ICON™ idle control module B connector.
>
> Disconnect the 14-pin pass-through connector at the vehicle's firewall.
>
> Disconnect the ignition bus relay from the cab harness.
>
> Set the multimeter to measure resistance.
>
> Touch one of the multimeter leads to pin 4 of the ICON™ idle control module B harness connector.
>
> Touch the other multimeter lead to ground.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of more than 100k ohms, which is an open circuit.
>
> If the circuit is **not** open, repair or replace the ICON™ engine harness. Refer to Procedure [[99-019-208 — Deutsch HDP20 and HD30 Connector Series|019-208]] or [[97-019-043 — Engine Wiring Harness|019-043]].
>
> Touch one of the multimeter leads to pin F of the 14-pin pass-through connector, ICON™ engine harness side.
>
> Touch the other multimeter lead to ground.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of more than 100k ohms, which is an open circuit.
>
> If the circuit is **not** open, repair or replace the ICON™ engine harness. Refer to Procedure [[97-019-043 — Engine Wiring Harness|019-043]].
>
> Touch one of the multimeter leads to pin F of the 14-pin pass-through connector, cab harness side.
>
> Touch the other multimeter lead to ground.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of more than 100k ohms, which is an open circuit.
>
> If the circuit is **not** closed, repair or replace the cab harness. Refer to Procedure [[97-019-305 — Cab Wiring Harness|019-305]].
>
> Touch one of the multimeter leads to pin 86 of the ignition bus relay harness connector.
>
> Touch the other multimeter lead to ground.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of more than 100k ohms, which is an open circuit.
>
> If the circuit is **not** open, repair or replace the cab harness. Refer to Procedure [[99-019-204 — Deutsch DRC Connector Series|019-204]] or [[97-019-305 — Cab Wiring Harness|019-305]].
>
> Connect all components after completing the repair.
>
> ### Check for Short Circuit from Pin to Pin
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To avoid personal injury, always ventilate the compartment before servicing the batteries. To avoid arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> Turn the keyswitch to the OFF position. Disconnect the vehicle battery cables from the battery. Disconnect the ICON™ battery harness connectors from the battery.
>
> **Note · Примечание**
> Disconnecting the vehicle battery connections can require that the engine ECM real-time clock be reset using INSITE™.
>
> **CAUTION · Осторожно**
> To avoid pin and harness damage, use test leads, Part Number 3822758 and 3822917, when taking a measurement.
>
> Disconnect the ICON™ idle control module A and B connectors.
>
> Disconnect the 14-pin pass through connector at the vehicle's firewall.
>
> Disconnect the ignition bus relay from the cab harness.
>
> Set the multimeter to measure resistance.
>
> Touch one of the multimeter leads to pin 4 of the ICON™ idle control module B harness connector. Touch the other multimeter lead to all other pins in the connector, one at a time.
>
> Read the value displayed on the multimeter.
>
> Then, touch one of the multimeter leads to pin 2 of the ICON™ idle control module A harness connector. Touch the other multimeter lead to all other pins in the connector, one at a time.
>
> Read the value displayed on the multimeter.
>
> For both pin-to-pin checks, the multimeter **must** display a reading of more than 100k ohms, which is an open circuit.
>
> If the circuit is **not** open, repair or replace the ICON™ engine harness. Refer to Procedure [[99-019-208 — Deutsch HDP20 and HD30 Connector Series|019-208]] or [[97-019-043 — Engine Wiring Harness|019-043]].
>
> Touch one of the multimeter leads to pin F of the 14-pin pass-through connector, ICON™ engine harness side. Touch the other multimeter lead to all other pins in the connector, one at a time.
>
> Read the value displayed on the multimeter.
>
> Repeat the pin-to-pin check from pin C. Touch one of the multimeter leads to pin C of the 14-pin pass-through connector, ICON™ engine harness side. Touch the other multimeter lead to all other pins in the connector, one at a time.
>
> Read the value displayed on the multimeter.
>
> For both pin-to-pin checks, the multimeter **must** display a reading of more than 100k ohms, which is an open circuit.
>
> If the circuit is **not** open, repair or replace the ICON™ engine harness. Refer to Procedure [[97-019-043 — Engine Wiring Harness|019-043]].
>
> Touch one of the multimeter leads to pin F of the 14-pin pass-through connector, cab harness side. Touch the other multimeter lead to all other pins in the connector, one at a time.
>
> Read the value displayed on the multimeter.
>
> Repeat the pin-to-pin check from pin C. Touch one of the multimeter leads to pin C of the 14-pin pass-through connector, cab harness side. Touch the other multimeter lead to all other pins in the connector, one at a time.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of more than 100k ohms, which is an open circuit.
>
> If the circuit is **not** closed, repair or replace the cab harness. Refer to Procedure [[97-019-305 — Cab Wiring Harness|019-305]].
>
> Touch one of the multimeter leads to pin 86 of the ignition bus relay harness connector.
>
> Touch the other multimeter lead to all other pins in the relay harness connector, one at a time
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of more than 100k ohms, which is an open circuit.
>
> If the circuit is **not** open, repair or replace the cab harness. Refer to Procedure [[99-019-204 — Deutsch DRC Connector Series|019-204]] or [[97-019-305 — Cab Wiring Harness|019-305]].
>
> Connect all components after completing the repair.
>
> ### Voltage Check
>
> **CAUTION · Осторожно**
> To avoid pin and harness damage, use test lead, Part Number 3822917, when taking a measurement.
>
> Disconnect the 14-pin pass-through connector at the vehicle's firewall.
>
> Set the multimeter to measure VDC.
>
> Turn the keyswitch to the ON position.
>
> Touch one of the multimeter leads to pin F of the 14-pin pass-through connector, cab harness side.
>
> Touch the other multimeter lead to ground.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of less than 0.5 VDC.
>
> If the voltage is **not** less than 0.5 VDC, repair or replace the ignition bus relay. Refer to Procedure [[99-019-204 — Deutsch DRC Connector Series|019-204]] or [[97-019-301 — Ignition Bus Relay 1 and 2|019-301]].
>
> Connect all components after completing the repair.
>
> ### Check for Short Circuit to External Voltage Source
>
> Turn the keyswitch to the OFF position. Disconnect the ICON™ idle control module B connector. Set the multimeter to measure VDC.
>
> **CAUTION · Осторожно**
> To avoid pin and harness damage, use test lead, Part Number 3822917, when taking a measurement.
>
> Turn the keyswitch to the ON position.
>
> Touch one of the multimeter leads to pin 4 of the ICON™ idle control module B harness connector. Touch the other multimeter lead to ground.
>
> Measure the voltage.
>
> The multimeter **must** display a reading of less than 0.5 VDC.
>
> If the voltage is **not** less than 0.5 VDC, there is a short circuit to an external voltage source.
>
> **Note · Примечание**
> An external voltage source is any wire in the cab or engine harness that carries voltage.
>
> Isolate the short to the proper portion of the circuit.
>
> Disconnect the 14-pin pass-through connector at the vehicle's firewall.
>
> Touch one of the multimeter leads to pin F of the 14-pin pass-through connector, cab harness side.
>
> Touch the other multimeter lead to ground.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of less than 0.5 VDC.
>
> If the voltage is **not** less than 0.5 VDC, there is a short circuit to an external voltage source on the cab harness side of the circuit.
>
> If the VDC is less than 0.5 VDC, the short circuit is on the ICON™ engine harness side of the circuit.
>
> Remove the external voltage source.
>
> Connect all components after completing the repair.
