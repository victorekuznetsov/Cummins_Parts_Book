---
type: "Процедура"
doc: "97-019-306"
title_en: "Keyswitch Input Circuit"
modified: "2004-10-19"
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
figures: 37
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-019-306.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-019-306.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "двигатель/QSX15"
  - "группа/97"
  - "перевод/машинный"
---

# Keyswitch Input Circuit

> [!abstract] Процедура · `97-019-306`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSM11, QSX15
> **Входит в руководства:** [[3666415 — ICON Idle Control System Master Repair Manual|3666415]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2004-10-19
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-019-306.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-019-306.pdf)

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
> Отключение аккумуляторных батарей автомобиля может потребовать сброса часов ECM двигателя в режиме реального времени с помощью инструментария электронного обслуживания INSITETM.

![[ea8coha.png]]

Удалить и осмотреть предохранитель на схеме зажигания переключателя зажигания ICONTM для коррозии, повреждения или взрываемого предохранителя.

Замените предохранитель, если это необходимо.

![[19400445.png]]

> [!warning] ОСТОРОЖНО
> Чтобы избежать повреждения штифта и проводов, используйте пробный щуп, номер детали 3822758 и 3822917, при проведении измерения.

Отключите модуль управления ICONTM Idle Разъем А.

Установите мультиметр для измерения сопротивления.

![[19c00928.png]]

Прикосновение к одному из мультиметров приводит к контакту 7 с неработающим модулем управления ICONTM Разъем проводной упряжки.

Прикосновение к другому мультиметру приводит к посту терминала зажигания в сборке переключателя зажигания.

Считайте показания мультиметра.

![[19c00938.png]]

Мультиметр **должен **отображать значение менее 10 Ом, что является замкнутой схемой.

Если цепь **не **закрыта, изолируйте проблемную область от жгута кабины или части ремня жгута двигателя.

![[19801619.png]]

Отсоедините 14-контактный проходной разъем на брандмауэре автомобиля.

Прикосновение к одному из мультиметров приводит к контакту Е 14-контактного пропускного разъема, проводов двигателя с ремнями безопасности.

Прикосновение к другому мультиметру приводит к контакту 7 с неработающим модулем управления ICONTM Разъем проводов жгута.

Считайте показания мультиметра.

![[19c00930.png]]

Мультиметр **должен **отображать значение менее 10 Ом, что является замкнутой схемой.

Если схема **не** закрыта, отремонтируйте или замените электропроводку двигателя ICONTM.

См. процедуру[[99-019-206 — Deutsch DTM and DTP Connector Series|019-206]]или[[97-019-043 — Engine Wiring Harness|019-043]].

![[19801619.png]]

Прикосновение к одному из мультиметров приводит к контакту Е 14-контактного пропускного разъема, проводов кабины с ремнями безопасности.

Прикосновение к другому мультиметру приводит к посту терминала зажигания в сборке переключателя зажигания.

Считайте показания мультиметра.

![[19c00939.png]]

Мультиметр **должен **отображать значение менее 10 Ом, что является замкнутой схемой.

Если цепь **не** закрыта, отремонтируйте или замените проводку кабины. См. процедуру[[99-019-207 — Deutsch HD10 Connector Series|019-207]]или[[97-019-305 — Cab Wiring Harness|019-305]].

![[19801619.png]]

Отсоедините термостат кабины от термостата кабины.

Прикосновение к одному из мультиметров приводит к посту зажигания в сборке переключателя зажигания.

Прикосновение к другому мультиметру приводит к контакту 4 кабины термостата с прыгунной проводкой разъема ремня.

Считайте показания мультиметра.

![[19c00937.png]]

Мультиметр **должен **отображать значение менее 10 Ом, что является замкнутой схемой.

Если схема **не** закрыта, отремонтируйте или замените электропроводку кабины термостата. См. процедуру[[99-019-204 — Deutsch DRC Connector Series|019-204]]или[[97-019-295 — Cab Thermostat Harness|019-295]].

После ремонта подсоедините все компоненты.

![[19801619.png]]

### Проверка на замыкание на массу

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы избежать травм, всегда проветривайте моторное отделение перед обслуживанием батарей. Чтобы избежать дуги, сначала удалите отрицательный (-) кабель батареи и прикрепите отрицательный (-) кабель батареи последним.

Переведите замок зажигания в положение OFF. Отсоедините кабели аккумулятора автомобиля от батареи. Отсоедините разъемы ICONTM от батареи.

> [!note] Примечание
> Отключение аккумуляторных батарей автомобиля может потребовать сброса часов ECM двигателя в режиме реального времени с помощью инструментария электронного обслуживания INSITETM.

![[ea8coha.png]]

Отключите модуль управления ICONTM Idle Разъем А.

Установите мультиметр для измерения сопротивления.

![[19c00928.png]]

Прикосновение к одному из мультиметров приводит к контакту 7 с неработающим модулем управления ICONTM Разъем проводной упряжки.

Прикоснитесь к другому мультиметру, который ведет на землю.

Считайте показания мультиметра.

![[19c00932.png]]

Мультиметр **must** отображает показания более 100k ом, что является открытой схемой. Если схема **не **открыта, есть короткое замыкание на землю.

Изолируйте короткое замыкание к электропроводке двигателя ICONTM, электропроводке кабины или электропроводке термостата кабины.

![[19801621.png]]

Отсоедините 14-контактный проходной разъем на брандмауэре автомобиля.

Прикосновение к одному из мультиметров приводит к контакту Е 14-контактного пропускного разъема, проводов двигателя с ремнями безопасности.

Прикоснитесь к другому мультиметру, который ведет на землю.

Считайте показания мультиметра.

![[19c00940.png]]

Мультиметр **must** отображает показания более 100k ом, что является открытой схемой.

Если схема **не** открыта, отремонтируйте или замените электропроводку двигателя ICONTM.

См. процедуру[[99-019-206 — Deutsch DTM and DTP Connector Series|019-206]],[[99-019-207 — Deutsch HD10 Connector Series|019-207]]или[[97-019-043 — Engine Wiring Harness|019-043]]. Если схема открыта, проверьте электропроводку кабины и электропроводку термостата кабины.

![[19801621.png]]

Отсоедините термостат кабины от термостата кабины.

Прикосновение к одному из мультиметров приводит к контакту Е 14-контактного пропускного разъема, проводов кабины с ремнями безопасности.

Прикоснитесь к другому мультиметру, который ведет на землю.

Считайте показания мультиметра.

![[19c00933.png]]

Мультиметр **must** отображает показания более 100k ом, что является открытой схемой.

Если схема **не** открыта, отремонтируйте или замените проводку кабины.

См. процедуру[[99-019-208 — Deutsch HDP20 and HD30 Connector Series|019-208]]или[[97-019-305 — Cab Wiring Harness|019-305]]. Если схема открыта, проверьте электропроводку кабины термостата.

![[19801621.png]]

Прикосновение к одному из мультиметров приводит к контакту 4 кабины термостата с прыгунной проводкой разъема ремня.

Прикоснитесь к другому мультиметру, который ведет на землю.

Считайте показания мультиметра.

![[19802892.png]]

Мультиметр **must** отображает показания более 100k ом, что является открытой схемой.

Если схема **не** открыта, отремонтируйте или замените электропроводку кабины термостата.

См. процедуру[[99-019-204 — Deutsch DRC Connector Series|019-204]]или[[97-019-295 — Cab Thermostat Harness|019-295]].

После ремонта подсоедините все компоненты.

![[19801621.png]]

### Проверка на замыкание между контактами

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы избежать травм, всегда проветривайте моторное отделение перед обслуживанием батарей. Чтобы избежать дуги, сначала удалите отрицательный (-) кабель батареи и прикрепите отрицательный (-) кабель батареи последним.

Переведите замок зажигания в положение OFF. Отсоедините кабели аккумулятора автомобиля от батареи. Отсоедините разъемы ICONTM от батареи.

> [!note] Примечание
> Отключение аккумуляторных батарей автомобиля может потребовать сброса часов ECM в режиме реального времени с помощью инструментария электронного обслуживания INSITETM.

![[ea8coha.png]]

> [!warning] ОСТОРОЖНО
> Чтобы избежать повреждения штифта и проводов, используйте пробный щуп, номер детали 3822758 и 3822917, при проведении измерения.

Отключите модуль управления ICONTM Idle Разъем А.

Установите мультиметр для измерения сопротивления.

![[19c00928.png]]

Прикосновение к одному из мультиметров приводит к контакту 7 с неработающим модулем управления A проводкой жгута разъема.

Прикосновение к другому мультиметру приводит ко всем другим штифтам в разъеме, по одному за раз.

Считайте показания мультиметра.

![[19c00943.png]]

Мультиметр **must** отображает показания более 100k ом, что является открытой схемой.

Если схема **не** открыта, то в разъеме есть короткое замыкание от контакта 7 до любого другого штифта, который зарегистрировал замкнутую цепь.

Ремонт или замена ремня электропроводки двигателя ICONTM. См. процедуру[[99-019-206 — Deutsch DTM and DTP Connector Series|019-206]]или[[97-019-043 — Engine Wiring Harness|019-043]].

![[19801621.png]]

Отсоедините 14-контактный проходной разъем на брандмауэре автомобиля.

Прикосновение к одному из мультиметров приводит к контакту Е 14-контактного пропускного разъема, проводов двигателя с ремнями безопасности.

Прикосновение к другому мультиметру приводит ко всем другим штифтам в разъеме, по одному за раз.

Считайте показания мультиметра.

![[19c00942.png]]

Мультиметр **must** отображает показания более 100k ом, что является открытой схемой.

Если схема **не** открыта, то в разъеме есть короткое замыкание от контакта Е до любого другого штифта, который зарегистрировал замкнутую цепь.

Ремонт или замена ремня электропроводки двигателя ICONTM. См. процедуру[[99-019-206 — Deutsch DTM and DTP Connector Series|019-206]]или[[97-019-043 — Engine Wiring Harness|019-043]].

![[19801621.png]]

Отсоедините коннектор кабины термостата от коннектора кабины.

Прикосновение к одному из мультиметров приводит к контакту Е 14-контактного пропускного разъема, проводов кабины с ремнями безопасности.

Прикосновение к другому мультиметру приводит ко всем другим штифтам разъема, по одному за раз.

Считайте показания мультиметра.

![[19c00935.png]]

Мультиметр **must** отображает показания более 100k ом, что является открытой схемой.

Если схема **не** открыта, то в разъеме есть короткое замыкание от контакта Е до любого другого штифта, который зарегистрировал замкнутую цепь.

Ремонт или замена кабины проводов ремня. См. процедуру[[99-019-207 — Deutsch HD10 Connector Series|019-207]]или[[97-019-305 — Cab Wiring Harness|019-305]].

![[19801621.png]]

Прикосновение к одному из мультиметров приводит к контакту 4 кабины термостата с прыгунной проводкой разъема ремня.

Прикосновение к другому мультиметру приводит ко всем другим штифтам в разъеме, по одному за раз.

Считайте показания мультиметра.

![[19c00941.png]]

Мультиметр **must** отображает показания более 100k ом, что является открытой схемой.

Если схема **не** открыта, то в разъеме есть короткое замыкание от контакта 4 до любого другого штифта, который зарегистрировал замкнутую цепь.

Ремонт или замена кабины термостата прыгуна проводов. См. процедуру[[99-019-204 — Deutsch DRC Connector Series|019-204]]или[[97-019-295 — Cab Thermostat Harness|019-295]].

После ремонта подсоедините все компоненты.

![[19801621.png]]

### Проверьте короткое замыкание на источнике внешнего напряжения

> [!warning] ОСТОРОЖНО
> Чтобы избежать повреждения штифта и проводов, используйте пробный щуп, номер детали 3822758 и 3822917, при проведении измерения.

Переведите замок зажигания в положение OFF.

Отключите модуль управления ICONTM Idle Разъем А.

Установите мультиметр для измерения VDC.

![[19c00963.png]]

Прикосновение к одному из мультиметров приводит к контакту 7 с неработающим модулем управления ICONTM Разъем проводной упряжки.

Прикоснитесь к другому мультиметру, который ведет на землю.

Считайте показания мультиметра.

![[19c00932.png]]

Мультиметр **must** отображает показания менее 0,5 VDC. Если напряжение **не** меньше 0,5 ВДК, то происходит короткое замыкание к внешнему источнику напряжения.

> [!note] Примечание
> Внешним источником напряжения является любой провод в кабине или проводах двигателя, который несет напряжение.

Удалите внешний источник напряжения.

![[19c00954.png]]

Отсоедините термостат кабины от электропроводки прыгуна от термостата. Отсоедините 14-контактный проходной разъем на брандмауэре автомобиля.

Прикосновение к одному из мультиметров приводит к контакту Е 14-контактного пропускного разъема, проводов кабины с ремнями безопасности. Прикоснитесь к другому мультиметру, который ведет на землю.

Считайте показания мультиметра. Мультиметр **must** отображает показания менее 0,5 VDC. Если напряжение **не** меньше 0,5 ВДК, то происходит короткое замыкание к внешнему источнику напряжения.

Удалите внешний источник напряжения.

![[19c00933.png]]

Прикосновение к одному из мультиметров приводит к контакту 4 кабины термостата с проводкой ремня разъема. Прикоснитесь к другому мультиметру, который ведет на землю.

Считайте показания мультиметра. Мультиметр **must** отображает показания менее 0,5 VDC. Если напряжение **не** меньше 0,5 ВДК, то происходит короткое замыкание к внешнему источнику напряжения.

Удалите внешний источник напряжения.

![[19802892.png]]

Прикосновение к одному из мультиметров приводит к посту зажигания в сборке переключателя зажигания. Прикоснитесь к другому мультиметру, который ведет на землю.

Считайте показания мультиметра. Мультиметр **must** отображает показания менее 0,5 VDC. Если напряжение **не** меньше 0,5 ВДК, то происходит короткое замыкание к внешнему источнику напряжения.

Удалите внешний источник напряжения.

После ремонта подсоедините все компоненты.

![[19c00946.png]]


> [!quote]- Original (English) · английский оригинал
> ### Resistance Check
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To avoid personal injury, always ventilate the compartment before servicing the batteries. To avoid arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> Turn the keyswitch to the OFF position. Disconnect the vehicle battery cables from the battery. Disconnect the ICON™ battery harness connectors from the battery.
>
> **Note · Примечание**
> Disconnecting the vehicle battery connections may require that the engine ECM real-time clock be reset using INSITE™ electronic service tool.
>
> Remove and inspect the fuse on the ICON™ keyswitch ignition circuit for corrosion, damage or blown fuse.
>
> Replace the fuse if necessary.
>
> **CAUTION · Осторожно**
> To avoid pin and harness damage, use test leads, Part Number 3822758 and 3822917, when taking a measurement.
>
> Disconnect the ICON™ idle control module A connector.
>
> Set the multimeter to measure resistance.
>
> Touch one of the multimeter leads to pin 7 of the ICON™ idle control module A harness connector.
>
> Touch the other multimeter lead to the ignition terminal post in the keyswitch assembly.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of less than 10 ohms, which is a closed circuit.
>
> If the circuit is **not** closed, isolate the problem area to the cab harness or engine harness portion of the circuit.
>
> Disconnect the 14-pin pass-through connector at the vehicle's firewall.
>
> Touch one of the multimeter leads to pin E of the 14-pin pass-through connector, engine harness side.
>
> Touch the other multimeter lead to pin 7 of the ICON™ idle control module A harness connector.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of less than 10 ohms, which is a closed circuit.
>
> If the circuit is **not** closed, repair or replace the ICON™ engine harness.
>
> Refer to Procedure [[99-019-206 — Deutsch DTM and DTP Connector Series|019-206]] or [[97-019-043 — Engine Wiring Harness|019-043]].
>
> Touch one of the multimeter leads to pin E of the 14-pin pass-through connector, cab harness side.
>
> Touch the other multimeter lead to the ignition terminal post in the keyswitch assembly.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of less than 10 ohms, which is a closed circuit.
>
> If the circuit is **not** closed, repair or replace the cab harness. Refer to Procedure [[99-019-207 — Deutsch HD10 Connector Series|019-207]] or [[97-019-305 — Cab Wiring Harness|019-305]].
>
> Disconnect the cab thermostat jumper harness from the cab thermostat.
>
> Touch one of the multimeter leads to the ignition terminal post in the keyswitch assembly.
>
> Touch the other multimeter lead to pin 4 of the cab thermostat jumper harness connector.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of less than 10 ohms, which is a closed circuit.
>
> If the circuit is **not** closed, repair or replace the cab thermostat jumper harness. Refer to Procedure [[99-019-204 — Deutsch DRC Connector Series|019-204]] or [[97-019-295 — Cab Thermostat Harness|019-295]].
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
> Disconnecting the vehicle battery connections may require that the engine ECM real-time clock be reset using INSITE™ electronic service tool.
>
> Disconnect the ICON™ idle control module A connector.
>
> Set the multimeter to measure resistance.
>
> Touch one of the multimeter leads to pin 7 of the ICON™ idle control module A harness connector.
>
> Touch the other multimeter lead to ground.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of more than 100k ohms, which is an open circuit. If the circuit is **not** open, there is a short circuit to ground.
>
> Isolate the short circuit to the ICON™ engine harness, cab harness, or cab thermostat jumper harness.
>
> Disconnect the 14-pin pass-through connector at the vehicle's firewall.
>
> Touch one of the multimeter leads to pin E of the 14-pin pass-through connector, engine harness side.
>
> Touch the other multimeter lead to ground.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of more than 100k ohms, which is an open circuit.
>
> If the circuit is **not** open, repair or replace the ICON™ engine harness.
>
> Refer to Procedure [[99-019-206 — Deutsch DTM and DTP Connector Series|019-206]], [[99-019-207 — Deutsch HD10 Connector Series|019-207]], or [[97-019-043 — Engine Wiring Harness|019-043]]. If the circuit is open, check the cab harness and cab thermostat jumper harness.
>
> Disconnect the cab thermostat jumper harness from the cab thermostat.
>
> Touch one of the multimeter leads to pin E of the 14-pin pass-through connector, cab harness side.
>
> Touch the other multimeter lead to ground.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of more than 100k ohms, which is an open circuit.
>
> If the circuit is **not** open, repair or replace the cab harness.
>
> Refer to Procedure [[99-019-208 — Deutsch HDP20 and HD30 Connector Series|019-208]] or [[97-019-305 — Cab Wiring Harness|019-305]]. If the circuit is open, check the cab thermostat jumper harness.
>
> Touch one of the multimeter leads to pin 4 of the cab thermostat jumper harness connector.
>
> Touch the other multimeter lead to ground.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of more than 100k ohms, which is an open circuit.
>
> If the circuit is **not** open, repair or replace the cab thermostat jumper harness.
>
> Refer to Procedure [[99-019-204 — Deutsch DRC Connector Series|019-204]] or [[97-019-295 — Cab Thermostat Harness|019-295]].
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
> Disconnecting the vehicle battery connections can require that the engine ECM real-time clock be reset using INSITE™ electronic service tool.
>
> **CAUTION · Осторожно**
> To avoid pin and harness damage, use test leads, Part Number 3822758 and 3822917, when taking a measurement.
>
> Disconnect the ICON™ idle control module A connector.
>
> Set the multimeter to measure resistance.
>
> Touch one of the multimeter leads to pin 7 of the idle control module A harness connector.
>
> Touch the other multimeter lead to all other pins in the connector, one at a time.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of more than 100k ohms, which is an open circuit.
>
> If the circuit is **not** open, there is a short circuit from pin 7 to any other pin in the connector that registered a closed circuit.
>
> Repair or replace the ICON™ engine harness. Refer to Procedure [[99-019-206 — Deutsch DTM and DTP Connector Series|019-206]] or [[97-019-043 — Engine Wiring Harness|019-043]].
>
> Disconnect the 14-pin pass-through connector at the vehicle's firewall.
>
> Touch one of the multimeter leads to pin E of the 14-pin pass-through connector, engine harness side.
>
> Touch the other multimeter lead to all other pins in the connector, one at a time.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of more than 100k ohms, which is an open circuit.
>
> If the circuit is **not** open, there is a short circuit from pin E to any other pin in the connector that registered a closed circuit.
>
> Repair or replace the ICON™ engine harness. Refer to Procedure [[99-019-206 — Deutsch DTM and DTP Connector Series|019-206]] or [[97-019-043 — Engine Wiring Harness|019-043]].
>
> Disconnect the cab thermostat jumper harness connector from the cab thermostat.
>
> Touch one of the multimeter leads to pin E of the 14-pin pass-through connector, cab harness side.
>
> Touch the other multimeter lead to all other pins of the connector, one at a time.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of more than 100k ohms, which is an open circuit.
>
> If the circuit is **not** open, there is a short circuit from pin E to any other pin in the connector that registered a closed circuit.
>
> Repair or replace the cab harness. Refer to Procedure [[99-019-207 — Deutsch HD10 Connector Series|019-207]] or [[97-019-305 — Cab Wiring Harness|019-305]].
>
> Touch one of the multimeter leads to pin 4 of the cab thermostat jumper harness connector.
>
> Touch the other multimeter lead to all other pins in the connector, one at a time.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of more than 100k ohms, which is an open circuit.
>
> If the circuit is **not** open, there is a short circuit from pin 4 to any other pin in the connector that registered a closed circuit.
>
> Repair or replace the cab thermostat jumper harness. Refer to Procedure [[99-019-204 — Deutsch DRC Connector Series|019-204]] or [[97-019-295 — Cab Thermostat Harness|019-295]].
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
> Touch one of the multimeter leads to pin 7 of the ICON™ idle control module A harness connector.
>
> Touch the other multimeter lead to ground.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of less than 0.5 VDC. If the voltage is **not** less than 0.5 VDC, there is a short circuit to an external voltage source.
>
> **Note · Примечание**
> An external voltage source is any wire in the cab or engine harness wiring that carries voltage.
>
> Remove the external voltage source.
>
> Disconnect the cab thermostat jumper harness from the thermostat. Disconnect the 14-pin pass-through connector at the vehicle's firewall.
>
> Touch one of the multimeter leads to pin E of the 14-pin pass-through connector, cab harness side. Touch the other multimeter lead to ground.
>
> Read the value displayed on the multimeter. The multimeter **must** display a reading of less than 0.5 VDC. If the voltage is **not** less than 0.5 VDC, there is a short circuit to an external voltage source.
>
> Remove the external voltage source.
>
> Touch one of the multimeter leads to pin 4 of the cab thermostat harness connector. Touch the other multimeter lead to ground.
>
> Read the value displayed on the multimeter. The multimeter **must** display a reading of less than 0.5 VDC. If the voltage is **not** less than 0.5 VDC, there is a short circuit to an external voltage source.
>
> Remove the external voltage source.
>
> Touch one of the multimeter leads to the ignition terminal post in the keyswitch assembly. Touch the other multimeter lead to ground.
>
> Read the value displayed on the multimeter. The multimeter **must** display a reading of less than 0.5 VDC. If the voltage is **not** less than 0.5 VDC, there is a short circuit to an external voltage source.
>
> Remove the external voltage source.
>
> Connect all components after completing the repair.
