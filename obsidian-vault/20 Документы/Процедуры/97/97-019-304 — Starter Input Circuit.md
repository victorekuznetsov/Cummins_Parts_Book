---
type: "Процедура"
doc: "97-019-304"
title_en: "Starter Input Circuit"
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
figures: 25
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-019-304.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-019-304.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "двигатель/QSX15"
  - "группа/97"
  - "перевод/машинный"
---

# Starter Input Circuit

> [!abstract] Процедура · `97-019-304`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSM11, QSX15
> **Входит в руководства:** [[3666415 — ICON Idle Control System Master Repair Manual|3666415]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-06-13
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-019-304.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-019-304.pdf)

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
> Отключение аккумуляторных соединений автомобиля может потребовать сброса часов ECM в режиме реального времени с помощью INSITETM.

![[ea8coha.png]]

> [!warning] ОСТОРОЖНО
> Чтобы избежать повреждения штифта и проводов, используйте пробный щуп, номер детали 3822758 и 3822917, при проведении измерения.

Отключите модуль управления ICONTM Idle Разъем А.

Установите мультиметр для измерения сопротивления.

![[19c00928.png]]

Прикосновение к одному из мультиметров приводит к контакту 8 с неработающим модулем управления ICONTM Разъем проводной упряжки.

Прикосновение к другому мультиметру приводит к посту стартового терминала в сборке переключателя зажигания.

Считайте показания мультиметра.

![[19802887.png]]

Мультиметр **должен **отображать значение менее 10 Ом, что является замкнутой схемой.

Если цепь **не** закрыта, проверьте упряжку электропроводки двигателя ICONTM и части электропроводки кабины.

![[19801619.png]]

Отсоедините 14-контактный проходной разъем на брандмауэре автомобиля.

Прикосновение одного из мультиметров приводит к контакту M 14-контактного пропускного разъема, проводов двигателя с ремнями безопасности.

Прикосновение к другому мультиметру приводит к контакту 8 с неработающим модулем управления ICONTM Разъем жгута проводов.

Считайте показания мультиметра.

![[19c00930.png]]

Мультиметр **должен **отображать значение менее 10 Ом, что является замкнутой схемой.

Если цепь закрыта, отремонтируйте или замените электропроводку двигателя ICONTM. См. процедуру 019-208, 019-200 или[[97-019-043 — Engine Wiring Harness|019-043]].

![[19801619.png]]

Прикосновение к одному из мультиметров приводит к контакту M 14-контактного пропускного разъема, кабины проводов упряжки борта.

Прикосновение к другому мультиметру приводит к посту стартового терминала в сборке переключателя зажигания.

Считайте показания мультиметра.

![[19802888.png]]

Мультиметр **должен **отображать значение менее 10 Ом, что является замкнутой схемой.

Если цепь она **не** закрылась, отремонтируйте или замените проводку кабины.

См. процедуру 019-197, 019-200 или[[97-019-305 — Cab Wiring Harness|019-305]].

После ремонта подсоедините все компоненты.

![[19801619.png]]

### Проверка на замыкание на массу

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы избежать травм, всегда проветривайте моторное отделение перед обслуживанием батарей. Чтобы избежать дуги, сначала удалите отрицательный (-) кабель батареи и прикрепите отрицательный (-) кабель батареи последним.

Переведите замок зажигания в положение OFF. Отсоедините кабели аккумулятора автомобиля от батареи. Отсоедините разъемы ICONTM от батареи.

> [!note] Примечание
> Отключение аккумуляторных батарей автомобиля может потребовать сброса часов ECM в режиме реального времени с помощью INSITETM.

![[ea8coha.png]]

Установите мультиметр для измерения сопротивления.

Прикосновение к одному из мультиметров приводит к посту стартового терминала в сборке переключателя зажигания.

Прикоснитесь к другому мультиметру, который ведет на землю.

Считайте показания мультиметра.

![[19802889.png]]

Мультиметр **must** отображает показания более 100k ом, что является открытой схемой. Если схема **не **открыта, есть короткое замыкание на землю.

Изолируйте короткое замыкание от проводной упряжки кабины или части проводной упряжки двигателя ICONTM цепи.

![[19801621.png]]

Отсоедините 14-контактный проходной разъем на брандмауэре автомобиля.

Прикосновение к одному из мультиметров приводит к контакту M 14-контактного пропускного разъема, кабины проводов упряжки борта.

Прикоснитесь к другому мультиметру, который ведет на землю.

Считайте показания мультиметра.

![[19c00933.png]]

Мультиметр **must** отображает показания более 100k ом, что является открытой схемой.

Если схема **не **открыта, проверьте проводку двигателя на стороне цепи.

Если цепь открыта, отремонтируйте или замените проводку кабины. См. процедуру 019-197 или[[97-019-043 — Engine Wiring Harness|019-043]].

![[19801621.png]]

Прикосновение одного из мультиметров приводит к контакту M 14-контактного пропускного разъема, проводов двигателя с ремнями безопасности.

Прикоснитесь к другому мультиметру, который ведет на землю.

Считайте показания мультиметра.

![[19c00940.png]]

Мультиметр **must** отображает показания более 100k ом, что является открытой схемой.

Если схема **не** открыта, отремонтируйте или замените электропроводку двигателя. См. процедуру 019-200, 019-208 или[[97-019-043 — Engine Wiring Harness|019-043]].

Если цепь открыта, отремонтируйте или замените проводку кабины. См. процедуру 019-200 или[[97-019-305 — Cab Wiring Harness|019-305]].

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

Отсоедините 14-контактный проходной разъем на брандмауэре автомобиля.

Установите мультиметр для измерения сопротивления.

![[15800040.png]]

Прикосновение к одному из мультиметров приводит к контакту M 14-контактного пропускного разъема, кабины проводов упряжки борта.

Прикосновение к другому мультиметру приводит ко всем другим штифтам разъема, кабинной проводов с упряжкой стороны, по одному за раз.

Считайте показания мультиметра. Мультиметр **must** отображает показания более 100k ом, что является открытой схемой. Если схема **не** открыта, то в разъеме есть короткое замыкание от контакта М до любого другого штифта, который зарегистрировал замкнутую цепь. Ремонт или замена кабины проводов ремня. См. процедуру 019-200 или[[97-019-305 — Cab Wiring Harness|019-305]].

![[19c00935.png]]

Проверьте проводку двигателя на стороне разъема.

Прикосновение одного из мультиметров приводит к контакту M 14-контактного пропускного разъема, проводов двигателя с ремнями безопасности.

Прикосновение к другому мультиметру приводит ко всем другим штифтам в разъеме, по одному за раз.

Считайте показания мультиметра.

![[19c00942.png]]

Мультиметр **must** отображает показания более 100k ом, что является открытой схемой.

Если схема **не** открыта, то в разъеме есть короткое замыкание от контакта М до любого другого штифта, который зарегистрировал замкнутую цепь.

Ремонт или замена ремня электропроводки двигателя ICONTM. См. процедуру 019-200 или[[97-019-043 — Engine Wiring Harness|019-043]].

![[19801621.png]]

Отключите модуль управления ICONTM Idle Разъем А.

Прикосновение к одному из мультиметров приводит к контакту 8 с неработающим модулем управления ICONTM Разъем проводной упряжки.

Прикосновение к другому мультиметру приводит ко всем другим штифтам в разъеме, по одному за раз.

Считайте показания мультиметра.

![[19c00943.png]]

Мультиметр **must** отображает показания более 100k ом, что является открытой схемой. Если схема **не** открыта, то в разъеме есть короткое замыкание от контакта 8 до любого другого штифта, который зарегистрировал замкнутую цепь.

Ремонт или замена ремня электропроводки двигателя ICONTM. См. процедуру 019-208 или[[97-019-043 — Engine Wiring Harness|019-043]].

После ремонта подсоедините все компоненты.

![[19801621.png]]

### Проверьте короткое замыкание на источнике внешнего напряжения

Установите мультиметр для измерения VDC.

Переведите замок зажигания в положение ON.

![[19c00963.png]]

Прикосновение к одному из мультиметров приводит к посту стартового терминала в сборке переключателя зажигания.

Прикоснитесь к другому мультиметру, который ведет на землю.

Считайте показания мультиметра.

![[19802889.png]]

Мультиметр **must** отображает показания менее 0,5 VDC.

Если напряжение **не** меньше 0,5 ВДК, то происходит короткое замыкание к внешнему источнику напряжения.

> [!note] Примечание
> Внешним источником напряжения является любой провод в кабине или проводка двигателя ICONTM, которая несет напряжение.

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
> Disconnecting the vehicle battey connections can require that the ECM real-time clock be reset using INSITE™.
>
> **CAUTION · Осторожно**
> To avoid pin and harness damage, use test leads, Part Number 3822758 and 3822917, when taking a measurement.
>
> Disconnect the ICON™ idle control module A connector.
>
> Set the multimeter to measure resistance.
>
> Touch one of the multimeter leads to pin 8 of the ICON™ idle control module A harness connector.
>
> Touch the other multimeter lead to the starter terminal post in the keyswitch assembly.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of less than 10 ohms, which is a closed circuit.
>
> If the circuit is **not** closed, check the ICON™ engine harness and cab harness portions of the circuit.
>
> Disconnect the 14-pin pass-through connector at the vehicle's firewall.
>
> Touch one of the multimeter leads to pin M of the 14-pin pass-through connector, engine harness side.
>
> Touch the other multimeter lead to pin 8 of the ICON™ idle control module A harness connector.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of less than 10 ohms, which is a closed circuit.
>
> If the circuit it **not** closed, repair or replace the ICON™ engine harness. Refer to Procedure 019-208, 019-200, or [[97-019-043 — Engine Wiring Harness|019-043]].
>
> Touch one of the multimeter leads to pin M of the 14-pin pass-through connector, cab harness side.
>
> Touch the other multimeter lead to the starter terminal post in the keyswitch assembly.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of less than 10 ohms, which is a closed circuit.
>
> If the circuit it **not** closed, repair or replace the cab harness.
>
> Refer to Procedure 019-197, 019-200, or [[97-019-305 — Cab Wiring Harness|019-305]].
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
> Set the multimeter to measure resistance.
>
> Touch one of the multimeter leads to the starter terminal post in the keyswitch assembly.
>
> Touch the other multimeter lead to ground.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of more than 100k ohms, which is an open circuit. If the circuit is **not** open, there is a short circuit to ground.
>
> Isolate the short circuit to the cab harness or ICON™ engine harness portion of the circuit.
>
> Disconnect the 14-pin pass-through connector at the vehicle's firewall.
>
> Touch one of the multimeter leads to pin M of the 14-pin pass-through connector, cab harness side.
>
> Touch the other multimeter lead to ground.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of more than 100k ohms, which is an open circuit.
>
> If the circuit is **not** open, check the engine harness side of the circuit.
>
> If the circuit is open, repair or replace the cab harness. Refer to Procedure 019-197 or [[97-019-043 — Engine Wiring Harness|019-043]].
>
> Touch one of the multimeter leads to pin M of the 14-pin pass-through connector, engine harness side.
>
> Touch the other multimeter lead to ground.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of more than 100k ohms, which is an open circuit.
>
> If the circuit is **not** open, repair or replace the engine harness. Refer to Procedure 019-200, 019-208, or [[97-019-043 — Engine Wiring Harness|019-043]].
>
> If the circuit is open, repair or replace the cab harness. Refer to Procedure 019-200 or [[97-019-305 — Cab Wiring Harness|019-305]].
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
> Disconnecting the vehicle battery connections may require that the engine ECM real-time clock be reset using INSITE™.
>
> **CAUTION · Осторожно**
> To avoid pin and harness damage, use test leads, Part Number 3822758 and 3822917, when taking a measurement.
>
> Disconnect the 14-pin pass-through connector at the vehicle's firewall.
>
> Set the multimeter to measure resistance.
>
> Touch one of the multimeter leads to pin M of the 14-pin pass-through connector, cab harness side.
>
> Touch the other multimeter lead to all other pins of the connector, cab harness side, one at a time.
>
> Read the value displayed on the multimeter. The multimeter **must** display a reading of more than 100k ohms, which is an open circuit. If the circuit is **not** open, there is a short circuit from pin M to any other pin in the connector that registered a closed circuit. Repair or replace the cab harness. Refer to Procedure 019-200 or [[97-019-305 — Cab Wiring Harness|019-305]].
>
> Check the engine harness side of the connector.
>
> Touch one of the multimeter leads to pin M of the 14-pin pass-through connector, engine harness side.
>
> Touch the other multimeter lead to all other pins in the connector, one at a time.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of more than 100k ohms, which is an open circuit.
>
> If the circuit is **not** open, there is a short circuit from pin M to any other pin in the connector that registered a closed circuit.
>
> Repair or replace the ICON™ engine harness. Refer to Procedure 019-200 or [[97-019-043 — Engine Wiring Harness|019-043]].
>
> Disconnect the ICON™ idle control module A connector.
>
> Touch one of the multimeter leads to pin 8 of the ICON™ idle control module A harness connector.
>
> Touch the other multimeter lead to all other pins in the connector, one at a time.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of more than 100k ohms, which is an open circuit. If the circuit is **not** open, there is a short circuit from pin 8 to any other pin in the connector that registered a closed circuit.
>
> Repair or replace the ICON™ engine harness. Refer to Procedure 019-208 or [[97-019-043 — Engine Wiring Harness|019-043]].
>
> Connect all components after completing the repair.
>
> ### Check for Short Circuit to External Voltage Source
>
> Set the multimeter to measure VDC.
>
> Turn the keyswitch to the ON position.
>
> Touch one of the multimeter leads to the starter terminal post in the keyswitch assembly.
>
> Touch the other multimeter lead to ground.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of less than 0.5 VDC.
>
> If the voltage is **not** less than 0.5 VDC, there is a short circuit to an external voltage source.
>
> **Note · Примечание**
> An external voltage source is any wire in the cab or ICON™ engine harness wiring that carries voltage.
>
> Remove the external voltage source.
>
> Connect all components after completing the repair.
