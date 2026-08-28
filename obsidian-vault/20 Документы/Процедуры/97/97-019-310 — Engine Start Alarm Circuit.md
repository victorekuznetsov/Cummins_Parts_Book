---
aliases:
  - "Цепь сигнализации пуска двигателя"
type: "Процедура"
doc: "97-019-310"
title_en: "Engine Start Alarm Circuit"
title_ru: "Цепь сигнализации пуска двигателя"
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
figures: 35
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-019-310.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-019-310.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "двигатель/QSX15"
  - "группа/97"
  - "перевод/машинный"
---

# Engine Start Alarm Circuit
**Цепь сигнализации пуска двигателя**

> [!abstract] Процедура · `97-019-310`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSM11, QSX15
> **Входит в руководства:** [[3666415 — ICON Idle Control System Master Repair Manual|3666415]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2004-10-14
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-019-310.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-019-310.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Проверка

Переведите замок зажигания в положение ON.

Подключите инструмент ICONTM для электронных услуг (системы Aftermarket или OEM) или инструмент для электронных услуг INSITETM (интегрированные системы).

Инициировать тест на сигнализацию.

Если сигнализация звучит, сигнализация прошла испытание и ремонт не требуется.

![[nobox.png]]

### Проверка сопротивления

Переведите замок зажигания в положение OFF.

Удалите и проверьте предохранитель питания на ремне проводов двигателя ICONTM для коррозии, повреждения или взрываемого предохранителя.

Замените предохранитель, если это необходимо.

![[15800036.png]]

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы избежать травм, всегда проветривайте моторное отделение перед обслуживанием батарей. Чтобы избежать дуги, сначала удалите отрицательный (-) кабель батареи и прикрепите отрицательный (-) кабель батареи последним.

Отсоедините кабели аккумулятора автомобиля от батареи. Удалите проводку двигателя ICONTM с положительного (+) разъема батареи с стойки аккумуляторного терминала.

> [!note] Примечание
> Отключение аккумуляторных батарей автомобиля может потребовать сброса часов ECM в режиме реального времени с помощью INSITETM.

![[ea8coha.png]]

> [!warning] ОСТОРОЖНО
> Чтобы избежать повреждения штифта и проводов, используйте пробный щуп, номер детали 3822758 и 3822917, при проведении измерения.

Отключите разъем аварийной сигнализации двигателя от электропроводки ICONTM. Отключите разъемы ICONTM idle Control module A и B.

Установите мультиметр для измерения сопротивления.

![[19c00920.png]]

Прикосновение к одному из мультиметров приводит к положительному (+) клемму кольца разъема для проводов двигателя ICONTM.

Прикосновение к другому мультиметру приводит к контакту В двигателя с пуском сигнализации проводов ремня разъема.

Считайте показания мультиметра.

![[19802930.png]]

Мультиметр **должен **отображать значение менее 10 Ом, что является замкнутой схемой.

Если схема **не** закрыта, отремонтируйте или замените электропроводку двигателя ICONTM.

См. процедуру[[99-019-197 — Ring Terminal|019-197]],[[99-019-202 — Metripack Connector Series|019-202]]или[[97-019-043 — Engine Wiring Harness|019-043]].

![[19801619.png]]

Прикосновение к одному из мультиметров приводит к контакту 1 с неработающим модулем управления ICONTM Разъем проводной упряжки.

Прикосновение к другому мультиметру приводит к контакту В двигателя с пуском сигнализации проводов ремня разъема.

Считайте показания мультиметра.

![[19802894.png]]

Мультиметр **должен **отображать значение менее 10 Ом, что является замкнутой схемой.

Если схема **не** закрыта, отремонтируйте или замените электропроводку двигателя ICONTM.

См. процедуру[[99-019-206 — Deutsch DTM and DTP Connector Series|019-206]],[[99-019-202 — Metripack Connector Series|019-202]]или[[97-019-043 — Engine Wiring Harness|019-043]].

![[19801619.png]]

Прикосновение к одному из мультиметров приводит к контакту 3 с неработающим модулем управления ICONTM B проводов жгута разъема.

Прикосновение к другому мультиметру приводит к контакту А двигателя с пусковой сигнализацией проводов ремня разъема.

Считайте показания мультиметра.

![[19802895.png]]

Мультиметр **должен **отображать значение менее 10 Ом, что является замкнутой схемой.

Если схема **не** закрыта, отремонтируйте или замените электропроводку двигателя ICONTM.

См. процедуру[[99-019-206 — Deutsch DTM and DTP Connector Series|019-206]],[[99-019-202 — Metripack Connector Series|019-202]]или[[97-019-043 — Engine Wiring Harness|019-043]].

После ремонта подсоедините все компоненты.

![[19801619.png]]

### Проверка на замыкание на массу

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы избежать травм, всегда проветривайте моторное отделение перед обслуживанием батарей. Чтобы избежать дуги, сначала удалите отрицательный (-) кабель батареи и прикрепите отрицательный (-) кабель батареи последним.

Переведите замок зажигания в положение OFF. Отсоедините кабели аккумулятора автомобиля от батареи. Удалите проводку двигателя ICONTM с положительного (+) разъема батареи с положительного (+) клеммного поста батареи.

> [!note] Примечание
> Отключение аккумуляторных батарей автомобиля может потребовать сброса часов ECM в режиме реального времени с помощью INSITETM.

![[ea8coha.png]]

> [!warning] ОСТОРОЖНО
> Чтобы избежать повреждения штифта и проводов, используйте пробный щуп, номер детали 3822758 и 3822917, при проведении измерения.

Отключите сигнализацию двигателя от электропроводки ICONTM. Отключите разъемы ICONTM idle Control module A и B.

Установите мультиметр для измерения сопротивления.

![[19c00920.png]]

Прикосновение к одному из мультиметров приводит к тому, что в двигатель ICONTM вводится электропроводка с помощью положительного (+) разъема клеммного кольца батареи. Прикоснитесь к другому мультиметру, который ведет на землю.

Считайте показания мультиметра.

![[19802931.png]]

Мультиметр **must** отображает показания более 100k ом, что является открытой схемой.

Если схема **не **открыта, есть короткое замыкание на землю. Ремонт или замена ремня электропроводки двигателя ICONTM. См. процедуру[[99-019-197 — Ring Terminal|019-197]]или[[97-019-043 — Engine Wiring Harness|019-043]].

![[19801621.png]]

Прикосновение к одному из мультиметров приводит к контакту А разъема электропроводки двигателя. Прикоснитесь к другому мультиметру, который ведет на землю. Считайте показания мультиметра.

Затем касание одного из мультиметров приводит к контакту В разъема жгутов проводов двигателя. Прикоснитесь к другому мультиметру, который ведет на землю. Считайте показания мультиметра.

![[19802899.png]]

Для обеих проверок с помощью штифта на землю мультиметр **должен **отображать показания более 100k ом, что является открытой схемой.

Если схема **не **открыта, есть короткое замыкание на землю. Ремонт или замена ремня электропроводки двигателя ICONTM. См. процедуру[[99-019-202 — Metripack Connector Series|019-202]]или[[97-019-043 — Engine Wiring Harness|019-043]].

![[19801621.png]]

Прикосновение к одному из мультиметров приводит к контакту 1 с неработающим модулем управления ICONTM Разъем проводной упряжки. Прикоснитесь к другому мультиметру, который ведет на землю.

Считайте показания мультиметра.

![[19c00932.png]]

Мультиметр **must** отображает показания более 100k ом, что является открытой схемой.

Если схема **не **открыта, есть короткое замыкание на землю. Ремонт или замена ремня электропроводки двигателя ICONTM. См. процедуру[[99-019-206 — Deutsch DTM and DTP Connector Series|019-206]]или[[97-019-043 — Engine Wiring Harness|019-043]].

![[19801621.png]]

Прикосновение к одному из мультиметров приводит к контакту 3 с неработающим модулем управления ICONTM B проводов жгута разъема. Прикоснитесь к другому мультиметру, который ведет на землю.

Считайте показания мультиметра.

![[19802900.png]]

Мультиметр **must** отображает показания более 100k ом, что является открытой схемой.

Если схема **не **открыта, есть короткое замыкание на землю. Ремонт или замена ремня электропроводки двигателя ICONTM. См. процедуру[[99-019-206 — Deutsch DTM and DTP Connector Series|019-206]]или[[97-019-043 — Engine Wiring Harness|019-043]].

После ремонта подсоедините все компоненты.

![[19801621.png]]

### Проверка на замыкание между контактами

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы избежать травм, всегда проветривайте моторное отделение перед обслуживанием батарей. Чтобы избежать дуги, сначала удалите отрицательный (-) кабель батареи и прикрепите отрицательный (-) кабель батареи последним.

Переведите замок зажигания в положение OFF. Отсоедините кабели аккумулятора автомобиля от батареи. Удалите проводку двигателя ICONTM с положительного (+) разъема батареи с положительного (+) клеммного поста батареи.

Установите мультиметр для измерения сопротивления.

> [!note] Примечание
> Отключение аккумуляторных батарей автомобиля может потребовать сброса часов ECM в режиме реального времени с помощью INSITETM.

![[ea8coha.png]]

> [!warning] ОСТОРОЖНО
> Чтобы избежать повреждения штифта и проводов, используйте пробный щуп, номер детали 3822758 и 3822917, при проведении измерения.

Отключите разъемы ICONTM idle Control module A и B.

Отключите сигнализацию запуска двигателя от электропроводки ICONTM.

![[19c00917.png]]

Прикосновение к одному из мультиметров приводит к контакту 1 с неработающим модулем управления ICONTM Разъем проводной упряжки.

Прикосновение к другому мультиметру приводит ко всем другим штифтам в разъеме.

Считайте показания мультиметра.

![[19c00943.png]]

Мультиметр **must** отображает показания более 100k ом, что является открытой схемой.

Если схема **не** открыта, то в неработающем модуле управления ICONTM имеется короткое замыкание от контакта 1 к любому другому штифту в разъеме, который зарегистрировал замкнутую цепь.

Ремонт или замена ремня электропроводки двигателя ICONTM. См. процедуру[[99-019-206 — Deutsch DTM and DTP Connector Series|019-206]]или[[97-019-043 — Engine Wiring Harness|019-043]].

![[19801621.png]]

Прикосновение к одному из мультиметров приводит к контакту 3 с неработающим модулем управления ICONTM B проводов жгута разъема.

Прикосновение к другому мультиметру приводит ко всем другим штифтам в разъеме.

Считайте показания мультиметра.

![[19c00962.png]]

Мультиметр **must** отображает показания более 100k ом, что является открытой схемой.

Если схема **не** открыта, то в неработающем модуле управления B-проводов ICONTM idle разъём с контактом 3 имеет короткое замыкание с любым другим штифтом в разъеме, который зарегистрировал замкнутую цепь.

Ремонт или замена ремня электропроводки двигателя ICONTM. См. процедуру[[99-019-206 — Deutsch DTM and DTP Connector Series|019-206]]или[[97-019-043 — Engine Wiring Harness|019-043]].

![[19801621.png]]

Прикосновение одного из мультиметров приводит к контакту А двигателя с пусковой сигнализацией проводов ремня разъема.

Прикосновение к другому мультиметру приводит к контакту B разъема.

Считайте показания мультиметра.

![[19802901.png]]

Мультиметр **must** отображает показания более 100k ом, что является открытой схемой.

Если схема **не** открыта, то в разъеме будильника запускается короткое замыкание от контакта А до контакта В. Ремонт или замена ремня электропроводки двигателя ICONTM. См. процедуру[[99-019-202 — Metripack Connector Series|019-202]]или[[97-019-043 — Engine Wiring Harness|019-043]].

После ремонта подсоедините все компоненты.

![[19801621.png]]

### Проверьте короткое замыкание на источнике внешнего напряжения

> [!warning] ОСТОРОЖНО
> Чтобы избежать повреждения штифта и проводов, используйте пробный щуп, номер детали 3822758 и 3822917, при проведении измерения.

Отключите кольцевой разъем с заряжаемой батареей ICONTM от положительного (+) заряда батареи. Отключите разъемы ICONTM idle Control module A и B. Отключите сигнализацию запуска двигателя от электропроводки ICONTM.

Установите мультиметр для измерения VDC.

Переведите замок зажигания в положение ON.

![[19c00917.png]]

Прикосновение к одному из мультиметров приводит к контакту 1 с неработающим модулем управления ICONTM Разъем проводной упряжки.

Прикоснитесь к другому мультиметру, который ведет на землю.

Считайте показания мультиметра.

![[19c00932.png]]

Мультиметр **must** отображает показания менее 0,5 VDC.

Если напряжение **не** меньше 0,5 ВДК, то происходит короткое замыкание к внешнему источнику напряжения.

> [!note] Примечание
> Внешним источником напряжения является любой провод в кабине проводной упряжке или проводной упряжке двигателя, который несет напряжение.

Удалите внешний источник напряжения.

![[19c00954.png]]

Прикосновение к одному из мультиметров приводит к контакту 3 с неработающим модулем управления ICONTM B проводов жгута разъема.

Прикоснитесь к другому мультиметру, который ведет на землю.

Считайте показания мультиметра.

![[19802900.png]]

Мультиметр **must** отображает показания менее 0,5 VDC.

Если напряжение **не** меньше 0,5 ВДК, то происходит короткое замыкание к внешнему источнику напряжения.

> [!note] Примечание
> Внешним источником напряжения является любой провод в кабине проводной упряжке или проводной упряжке двигателя, который несет напряжение.

Удалите внешний источник напряжения.

![[19c00954.png]]

Прикосновение одного из мультиметров приводит к контакту А двигателя с пусковой сигнализацией проводов ремня разъема. Прикоснитесь к другому мультиметру, который ведет на землю.

Считайте показания мультиметра.

Повторите проверку от контакта B до основания. Прикосновение одного из мультиметров приводит к контакту В двигателя с пусковой сигнализацией проводов ремня разъема. Прикоснитесь к другому мультиметру, который ведет на землю.

Считайте показания мультиметра.

![[19802899.png]]

Для обеих проверок мультиметр **должен** отображать показания менее 0,5 VDC.

Если напряжение **не** меньше 0,5 ВДК, то происходит короткое замыкание к внешнему источнику напряжения.

> [!note] Примечание
> Внешним источником напряжения является любой провод в кабине проводной упряжке или проводной упряжке двигателя, который несет напряжение.

Удалите внешний источник напряжения.

После ремонта подсоедините все компоненты.

![[19c00954.png]]


> [!quote]- Original (English) · английский оригинал
> ### Test
>
> Turn the keyswitch to the ON position.
>
> Connect the ICON™ electronic service tool (Aftermarket or OEM systems), or INSITE™ electronic service tool (Integrated systems).
>
> Initiate the Alarm Test.
>
> If the alarm sounds, the alarm circuit passed the test and no repairs are needed.
>
> ### Resistance Check
>
> Turn the keyswitch to the OFF position.
>
> Remove and inspect the power fuse on the ICON™ engine harness for corrosion, damage, or a blown fuse.
>
> Replace the fuse if necessary.
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To avoid personal injury, always ventilate the compartment before servicing the batteries. To avoid arcing, remove the negative (-) battery cable first and attach the negative (--) battery cable last.
>
> Disconnect the vehicle battery cables from the battery. Remove the ICON™ engine harness positive (+) battery connector from the battery terminal post.
>
> **Note · Примечание**
> Disconnecting the vehicle battery connections can require that the engine ECM real-time clock be reset using INSITE™.
>
> **CAUTION · Осторожно**
> To avoid pin and harness damage, use test leads, Part Number 3822758 and 3822917, when taking a measurement.
>
> Disconnect the engine start alarm connector from the ICON™ engine harness. Disconnect the ICON™ idle control module A and B connectors.
>
> Set the multimeter to measure resistance.
>
> Touch one of the multimeter leads to the positive (+) ICON™ engine harness connector ring terminal.
>
> Touch the other multimeter lead to pin B of the engine start alarm harness connector.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of less than 10 ohms, which is a closed circuit.
>
> If the circuit is **not** closed, repair or replace the ICON™ engine harness.
>
> Refer to Procedure [[99-019-197 — Ring Terminal|019-197]], [[99-019-202 — Metripack Connector Series|019-202]], or [[97-019-043 — Engine Wiring Harness|019-043]].
>
> Touch one of the multimeter leads to pin 1 of the ICON™ idle control module A harness connector.
>
> Touch the other multimeter lead to pin B of the engine start alarm harness connector.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of less than 10 ohms, which is a closed circuit.
>
> If the circuit is **not** closed, repair or replace the ICON™ engine harness.
>
> Refer to Procedure [[99-019-206 — Deutsch DTM and DTP Connector Series|019-206]], [[99-019-202 — Metripack Connector Series|019-202]], or [[97-019-043 — Engine Wiring Harness|019-043]].
>
> Touch one of the multimeter leads to pin 3 of the ICON™ idle control module B harness connector.
>
> Touch the other multimeter lead to pin A of the engine start alarm harness connector.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of less than 10 ohms, which is a closed circuit.
>
> If the circuit is **not** closed, repair or replace the ICON™ engine harness.
>
> Refer to Procedure [[99-019-206 — Deutsch DTM and DTP Connector Series|019-206]], [[99-019-202 — Metripack Connector Series|019-202]], or [[97-019-043 — Engine Wiring Harness|019-043]].
>
> Connect all components after completing the repair.
>
> ### Check for Short Circuit to Ground
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To avoid personal injury, always ventilate compartment before servicing the batteries. To avoid arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> Turn the keyswitch to the OFF position. Disconnect the vehicle battery cables from the battery. Remove the ICON™ engine harness positive (+) battery connector from the positive (+) battery terminal post.
>
> **Note · Примечание**
> Disconnecting the vehicle battery connections can require that the engine ECM real-time clock be reset using INSITE™.
>
> **CAUTION · Осторожно**
> To avoid pin and harness damage, use test leads, Part Number 3822758 and 3822917, when taking a measurement.
>
> Disconnect the engine alarm from the ICON™ engine harness. Disconnect the ICON™ idle control module A and B connectors.
>
> Set the multimeter to measure resistance.
>
> Touch one of the multimeter leads to the ICON™ engine harness positive (+) battery ring terminal connector. Touch the other multimeter lead to ground.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of more than 100k ohms, which is an open circuit.
>
> If the circuit is **not** open, there is a short circuit to ground. Repair or replace the ICON™ engine harness. Refer to Procedure [[99-019-197 — Ring Terminal|019-197]] or [[97-019-043 — Engine Wiring Harness|019-043]].
>
> Touch one of the multimeter leads to pin A of the engine alarm harness connector. Touch the other multimeter lead to ground. Read the value displayed on the multimeter.
>
> Then, touch one of the multimeter leads to pin B of the engine alarm harness connector. Touch the other multimeter lead to ground. Read the value displayed on the multimeter.
>
> For both pin-to-ground checks, the multimeter **must** display a reading of more than 100k ohms, which is an open circuit.
>
> If the circuit is **not** open, there is a short circuit to ground. Repair or replace the ICON™ engine harness. Refer to Procedure [[99-019-202 — Metripack Connector Series|019-202]] or [[97-019-043 — Engine Wiring Harness|019-043]].
>
> Touch one of the multimeter leads to pin 1 of the ICON™ idle control module A harness connector. Touch the other multimeter lead to ground.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of more than 100k ohms, which is an open circuit.
>
> If the circuit is **not** open, there is a short circuit to ground. Repair or replace the ICON™ engine harness. Refer to Procedure [[99-019-206 — Deutsch DTM and DTP Connector Series|019-206]] or [[97-019-043 — Engine Wiring Harness|019-043]].
>
> Touch one of the multimeter leads to pin 3 of the ICON™ idle control module B harness connector. Touch the other multimeter lead to ground.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of more than 100k ohms, which is an open circuit.
>
> If the circuit is **not** open, there is a short circuit to ground. Repair or replace the ICON™ engine harness. Refer to Procedure [[99-019-206 — Deutsch DTM and DTP Connector Series|019-206]] or [[97-019-043 — Engine Wiring Harness|019-043]].
>
> Connect all components after completing the repair.
>
> ### Check for Short Circuit from Pin to Pin
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To avoid personal injury, always ventilate the compartment before servicing the batteries. To avoid arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> Turn the keyswitch to the OFF position. Disconnect the vehicle battery cables from the battery. Remove the ICON™ engine harness positive (+) battery connector from the positive (+) battery terminal post.
>
> Set the multimeter to measure resistance.
>
> **Note · Примечание**
> Disconnecting the vehicle battery connections can require that the engine ECM real-time clock be reset using INSITE™.
>
> **CAUTION · Осторожно**
> To avoid pin and harness damage, use test leads, Part Number 3822758 and 3822917, when taking a measurement.
>
> Disconnect the ICON™ idle control module A and B connectors.
>
> Disconnect the engine start alarm from the ICON™ engine harness.
>
> Touch one of the multimeter leads to pin 1 of the ICON™ idle control module A harness connector.
>
> Touch the other multimeter lead to all other pins in the connector.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of more than 100k ohms, which is an open circuit.
>
> If the circuit is **not** open, there is a short circuit from pin 1 in the ICON™ idle control module A harness connector to any other pin in the connector that registered a closed circuit.
>
> Repair or replace the ICON™ engine harness. Refer to Procedure [[99-019-206 — Deutsch DTM and DTP Connector Series|019-206]] or [[97-019-043 — Engine Wiring Harness|019-043]].
>
> Touch one of the multimeter leads to pin 3 of the ICON™ idle control module B harness connector.
>
> Touch the other multimeter lead to all other pins in the connector.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of more than 100k ohms, which is an open circuit.
>
> If the circuit is **not** open, there is a short circuit from pin 3 in the ICON™ idle control module B harness connector to any other pin in the connector that registered a closed circuit.
>
> Repair or replace the ICON™ engine harness. Refer to Procedure [[99-019-206 — Deutsch DTM and DTP Connector Series|019-206]] or [[97-019-043 — Engine Wiring Harness|019-043]].
>
> Touch one of the multimeter leads to pin A of the engine start alarm harness connector.
>
> Touch the other multimeter lead to pin B of the connector.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of more than 100k ohms, which is an open circuit.
>
> If the circuit is **not** open, there is a short circuit from pin A to pin B in the engine start alarm harness connector. Repair or replace the ICON™ engine harness. Refer to Procedure [[99-019-202 — Metripack Connector Series|019-202]] or [[97-019-043 — Engine Wiring Harness|019-043]].
>
> Connect all components after completing the repair.
>
> ### Check for Short Circuit to External Voltage Source
>
> **CAUTION · Осторожно**
> To avoid pin and harness damage, use test leads, Part Number 3822758 and 3822917, when taking a measurement.
>
> Disconnect the ICON™ engine harness ring terminal positive (+) battery connector from the positive (+) battery post. Disconnect the ICON™ idle control module A and B connectors. Disconnect the engine start alarm from the ICON™ engine harness.
>
> Set the multimeter to measure VDC.
>
> Turn the keyswitch to the ON position.
>
> Touch one of the multimeter leads to pin 1 of the ICON™ idle control module A harness connector.
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
> An external voltage source is any wire in the cab harness or engine harness wiring that carries voltage.
>
> Remove the external voltage source.
>
> Touch one of the multimeter leads to pin 3 of the ICON™ idle control module B harness connector.
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
> An external voltage source is any wire in the cab harness or engine harness wiring that carries voltage.
>
> Remove the external voltage source.
>
> Touch one of the multimeter leads to pin A of the engine start alarm harness connector. Touch the other multimeter lead to ground.
>
> Read the value displayed on the multimeter.
>
> Repeat the pin-to-ground check from pin B. Touch one of the multimeter leads to pin B of the engine start alarm harness connector. Touch the other multimeter lead to ground.
>
> Read the value displayed on the multimeter.
>
> For both checks, the multimeter **must** display a reading of less than 0.5 VDC.
>
> If the voltage is **not** less than 0.5 VDC, there is a short circuit to an external voltage source.
>
> **Note · Примечание**
> An external voltage source is any wire in the cab harness or engine harness wiring that carries voltage.
>
> Remove the external voltage source.
>
> Connect all components after completing the repair.
