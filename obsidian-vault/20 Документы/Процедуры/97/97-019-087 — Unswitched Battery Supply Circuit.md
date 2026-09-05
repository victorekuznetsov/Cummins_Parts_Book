---
aliases:
  - "Цепь постоянного питания от АКБ"
type: "Процедура"
doc: "97-019-087"
title_en: "Unswitched Battery Supply Circuit"
title_ru: "Цепь постоянного питания от АКБ"
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
figures: 27
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-019-087.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-019-087.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "двигатель/QSX15"
  - "группа/97"
  - "перевод/машинный"
---

# Unswitched Battery Supply Circuit
**Цепь постоянного питания от АКБ**

> [!abstract] Процедура · `97-019-087`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSM11, QSX15
> **Входит в руководства:** [[3666415 — ICON Idle Control System Master Repair Manual|3666415]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-06-13
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-019-087.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-019-087.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Проверка сопротивления

Общие сведения

Переведите замок зажигания в положение OFF.

Удалите и проверьте предохранитель питания на ремне проводов двигателя ICONTM для коррозии, повреждения или взрываемого предохранителя.

Замените предохранитель, если это необходимо.

![[15800036.png]]

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы избежать травм, всегда проветривайте моторное отделение перед обслуживанием батарей. Чтобы избежать дуги, сначала удалите отрицательный (-) кабель батареи и прикрепите отрицательный (-) кабель последним.

Отсоедините кабели аккумулятора автомобиля от батареи.

> [!note] Примечание
> Отключение аккумуляторных батарей автомобиля может потребовать сброса часов ECM в режиме реального времени с помощью INSITETM.

Удалите разъемы аккумуляторной батареи ICONTM с устройств вывода аккумулятора.

![[ea8coha.png]]

> [!warning] ОСТОРОЖНО
> Чтобы избежать повреждения штифта и проводов, используйте пробный щуп, номер детали 3822758 и 3822917, при проведении измерения.

Отключите модуль управления ICONTM Idle Разъем А.

Отсоедините 4-контактный термостат кабины от разъёма проводов жгута кабины от термостата кабины.

Установите мультиметр для измерения сопротивления.

![[19802871.png]]

← Двигатель электропроводки Узлы Check

Прикосновение к одному из мультиметров приводит к контакту 1 с неработающим модулем управления ICONTM Разъем проводной упряжки.

Прикосновение к другому мультиметру приводит к положительному (+) клемму кольца разъема для проводов двигателя ICONTM (обычно подключенному к аккумулятору автомобиля). Считайте показания мультиметра.

Затем касание одного из мультиметров приводит к контакту 1 термостата с прыгунной проводкой разъёма ремня (на конце, который соединяется с термостатом).

Прикосновение к другому приводит к положительному (+) клемму кольца разъема для проводов двигателя ICONTM. Считайте показания мультиметра.

![[19c00967.png]]

Для обеих проверок мультиметр **должен** отображать показания менее 10 Ом, что является замкнутой схемой.

Если цепь **не **закрыта, перепроверьте предохранитель проводов двигателя и замените, если это необходимо.

Если предохранитель хорош, замените электропроводку двигателя ICON или изолируйте проблему до правильного терминала кольца батареи или до разъема ICONTM с неработающим модулем управления A.

![[19801619.png]]

Прикосновение к одному из мультиметров приводит к контакту 1 кабины термостата с прыгунной проводкой 4-контактного разъема (разъема на кабине проводной упряжки).

Прикосновение к другому мультиметру приводит к положительному (+) кольцевому терминалу разъема аккумулятора ICONTM. Измерьте сопротивление. Мультиметр **должен отображать значение 10 Ом или меньше. Если схема **не закрыта, изолируйте проблему с двигателем ICONTM, кабиной или термостатом.

![[19c00968.png]]

Отсоедините 14-контактный проходной разъем на брандмауэре автомобиля.

Прикосновение к одному из мультиметров приводит к контакту А 14-контактного пропускного разъема, проводов двигателя с ремнями безопасности.

Прикосновение к другому мультиметру приводит к положительному (+) кольцевому терминалу разъема аккумулятора ICONTM.

Считайте показания мультиметра.

![[19c00969.png]]

Мультиметр **должен **отображать значение менее 10 Ом, что является замкнутой схемой.

Если схема **не** закрыта, отремонтируйте или замените электропроводку двигателя ICONTM. См. процедуру 019-200 или[[97-019-043 — Engine Wiring Harness|019-043]].

Если цепь закрыта, проверьте часть цепи кабины.

![[19801619.png]]

Подключите 14-контактный проходной разъем.

Прикосновение к одному из мультиметров приводит к контакту 2 с неработающим модулем управления ICONTM Разъем проводов жгута.

Прикосновение к другому мультиметру приводит к отрицательному (-) клемму кольца разъема ремня электропроводки двигателя ICONTM (обычно подключаемому к аккумулятору автомобиля). Считайте показания мультиметра.

Затем касание одного из мультиметров приводит к контакту 2 термостата с прыгунной проводкой разъема жгута (на конце, который соединяется с термостатом). Прикосновение к другому приводит к отрицательному (-) клемму кольца разъема для проводов двигателя ICONTM. Считайте показания мультиметра.

![[19c00967.png]]

Для обеих проверок мультиметр **должен **отображать значение 10 Ом или менее, что является замкнутой схемой. Если схема **не **закрыта, изолируйте проблему с двигателем ICONTM, кабиной или термостатом.

![[19801619.png]]

Прикосновение к одному из мультиметров приводит к контакту 2 с неработающим модулем управления ICONTM Разъем проводов жгута.

Прикосновение к другому мультиметру приводит к отрицательному (-) клемму кольца разъема ремня электропроводки двигателя ICONTM.

Считайте показания мультиметра.

![[19c00972.png]]

Мультиметр **должен **отображать значение менее 10 Ом, что является замкнутой схемой. Если схема **не** закрыта, отремонтируйте или замените электропроводку двигателя ICONTM.

Процедура 019-208 или 019-197 для ремонта электропроводки или Процедура[[97-019-043 — Engine Wiring Harness|019-043]]Замена проводов на упряжь.

![[19801619.png]]

Отсоедините 14-контактный проходной разъем на брандмауэре автомобиля.

Прикосновение одного из мультиметров приводит к контакту С 14-контактного пропускного разъема, проводов двигателя с ремнями безопасности.

Прикосновение к другому мультиметру приводит к отрицательному (-) клемму кольца разъема аккумулятора ICONTM.

Считайте показания мультиметра.

![[19c00969.png]]

Мультиметр **должен **отображать значение 10 Ом или менее, которое является замкнутой схемой. Если схема **не** закрыта, отремонтируйте или замените электропроводку двигателя ICONTM. Процедура 019-200 или 019-197 для ремонта электропроводки или Процедура[[97-019-043 — Engine Wiring Harness|019-043]]Замена проводов на упряжь.

Если цепь закрыта, проверьте часть цепи кабины.

![[19801619.png]]

Схема кабины Check

Отсоедините термостат кабины от электропроводки кабины. Прикосновение к одному из мультиметров приводит к контакту 1 кабины термостата с прыгунной проводкой 4-контактного разъема (разъем на кабине проводной ремни под приборной панелью).

Прикосновение к другому мультиметру приводит к контакту А 14-контактного пропускного разъема, проводов кабины с ремнями безопасности.

Считайте показания мультиметра.

Мультиметр **должен **отображать значение менее 10 Ом, что является замкнутой схемой. Если цепь **не** закрыта, отремонтируйте или замените проводку ICONTM. См. процедуру[[97-019-305 — Cab Wiring Harness|019-305]].

![[19c00970.png]]

Прикосновение к одному из мультиметров приводит к контакту 2 кабины термостата с прыгунной проводкой разъема жгута (разъем на кабине проводов жгута).

Прикосновение к другому мультиметру приводит к контакту С 14-контактного пропускного разъема, проводов кабины с ремнями безопасности.

Считайте показания мультиметра.

Мультиметр **должен **отображать значение менее 10 Ом, что является замкнутой схемой. Если цепь **не** закрыта, отремонтируйте или замените проводку кабины. См. процедуру[[97-019-305 — Cab Wiring Harness|019-305]].

![[19c00970.png]]

Cab Thermostat Jumper жгут проводов

Прикосновение к одному из мультиметров приводит к контакту 1 4-контактной кабины термостата с прыгунной проводкой разъема жгута, прыгунной проводов с ремешком стороны. Этот разъем расположен на конце проводов термостата кабины, которая соединяется с проводкой кабины.

Прикосновение к другому мультиметру приводит к контакту 1 коннектора кабины термостата с прыжком проводов на конце проводов ремня, который соединяется с 4-контактным разъемом мощности / данных термостата.

Считайте показания мультиметра.

![[19c00971.png]]

Мультиметр должен отображать значение 10 Ом или менее, которое является замкнутой схемой.

Если схема **не **закрыта, замените электропроводку кабины термостата. См. процедуру[[97-019-295 — Cab Thermostat Harness|019-295]].

![[19801619.png]]

Прикосновение к одному из мультиметров приводит к контакту 2 4-контактного термостата с прыгунной проводкой разъема жгута, прыгунной проводов с ремешком стороны. Этот разъем расположен на конце проводов термостата, которая соединяется с проводкой кабины.

Прикосновение к другому мультиметру приводит к контакту 2 с коннектором термостата с прыжком проводов ремня, разъемом, расположенным на конце проводов ремня, который соединяется с мощностью термостата и 4-контактным разъемом данных.

Считайте показания мультиметра.

![[19c00971.png]]

Мультиметр **должен **отображать значение 10 Ом или менее, которое является замкнутой схемой.

Если схема **не** закрыта, отремонтируйте или замените термостат прыгуна проводов. См. процедуру[[97-019-295 — Cab Thermostat Harness|019-295]].

![[19801619.png]]

ICONTM Battery Connectors для проверки шины данных

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы избежать травм, всегда проветривайте моторное отделение перед обслуживанием батарей. Чтобы избежать дуги, сначала удалите отрицательный (-) кабель батареи и прикрепите отрицательный (-) кабель последним.

Переведите замок зажигания в положение OFF. Отсоедините кабели аккумулятора автомобиля от батареи.

> [!note] Примечание
> Отключение аккумуляторных батарей автомобиля может потребовать сброса часов ECM в режиме реального времени с помощью INSITETM.

![[ea8coha.png]]

Удалите проводку двигателя ICONTM с положительного (+) разъема батареи с стойки аккумуляторного терминала.

Удалите шину данных OEM CAN (6-контактный или 9-контактный) разъем.

Установите мультиметр для измерения сопротивления.

![[15800045.png]]

> [!note] Примечание
> Проверьте схему проводов OEM, чтобы подтвердить положительные и отрицательные назначения контакта с шиной данных CAN. Следующие шаги описывают «типичную» конфигурацию транспортного средства, но, возможно, не будут соответствовать конфигурации вашего транспортного средства.

Прикосновение к одному из мультиметров приводит к положительному (+) шасси аккумуляторной проводов ремня разъемного кольца.

Прикосновение к другому мультиметру приводит к штифту, прикрепленному к положительному (+) проводу батареи в разъеме шины данных CAN (обычно, контакт C в 6-контактном разъеме Deutsch или контакт B в 9-контактном разъеме Deutsch).

Считайте показания мультиметра.

![[19c00973.png]]

Мультиметр **должен **отображать значение менее 10 Ом, что является замкнутой схемой.

Если схема **не** закрыта, отремонтируйте или замените проводку OEM, подключенную к разъему шины данных CAN.

См. руководство изготовителя машины по диагностике и ремонту.

![[19801619.png]]

Прикосновение к одному из мультиметров приводит к положительному (+) кольцевому терминалу разъема проводов аккумуляторной батареи. Прикосновение к другому мультиметру приводит к посту терминала батареи в сборке переключателя зажигания.

Считайте показания мультиметра.

Мультиметр **должен **отображать значение менее 10 Ом, что является замкнутой схемой. Если цепь **не** закрыта, отремонтируйте или замените электропроводку OEM.

См. руководство изготовителя машины по диагностике и ремонту.

![[19c00974.png]]

Удалите отрицательный (-) разъем батареи из стойки терминала батареи.

Прикосновение к одному из мультиметров приводит к отрицательному (-) OEM проводах ремня разъема кольца терминала.

Прикосновение к другому мультиметру приводит к штифту, прикрепленному к отрицательному (-) проводу батареи в разъеме шины данных CAN (обычно, контакт Е в 6-контактных разъемах Deutsch или контакт А в 9-контактном разъеме Deutsch).

Считайте показания мультиметра.

![[19c00973.png]]

Мультиметр **должен **отображать значение менее 10 Ом, что является замкнутой схемой.

Если цепь **не** закрыта, отремонтируйте или замените проводку OEM или изолируйте кабель от правой батареи.

См. руководство изготовителя машины по диагностике и ремонту.

![[19801619.png]]


> [!quote]- Original (English) · английский оригинал
> ### Resistance Check
>
> General Information
>
> Turn the keyswitch to the OFF position.
>
> Remove and inspect the power fuse on the ICON™ engine harness for corrosion, damage, or a blown fuse.
>
> Replace the fuse if necessary.
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To avoid personal injury, always ventilate the compartment before servicing the batteries. To avoid arcing, remove the negative (-) battery cable first and attach the negative (-) cable last.
>
> Disconnect the vehicle battery cables from the battery.
>
> **Note · Примечание**
> Disconnecting the vehicle battery connections can require that the engine ECM real-time clock be reset using INSITE™.
>
> Remove the ICON™ engine harness battery connectors from the battery terminal posts.
>
> **CAUTION · Осторожно**
> To avoid pin and harness damage, use test leads, Part Number 3822758 and 3822917, when taking a measurement.
>
> Disconnect the ICON™ idle control module A connector.
>
> Disconnect the 4-pin cab thermostat jumper harness connector from the cab thermostat.
>
> Set the multimeter to measure resistance.
>
> Engine Harness Check
>
> Touch one of the multimeter leads to pin 1 of the ICON™ idle control module A harness connector.
>
> Touch the other multimeter lead to the positive (+) ICON™ engine harness connector ring terminal (normally connected to the vehicle battery). Read the value displayed on the multimeter.
>
> Then, touch one of the multimeter leads to pin 1 of the thermostat jumper harness connector (on the end that connects to the thermostat).
>
> Touch the other lead to the positive (+) ICON™ engine harness connector ring terminal. Read the value displayed on the multimeter.
>
> For both checks, the multimeter **must** display a reading of less than 10 ohms, which is a closed circuit.
>
> If the circuit is **not** closed, recheck the engine harness fuse and replace, if necessary.
>
> If the fuse is good, replace the ICON engine harness, or isolate the problem to the correct battery ring terminal, or the ICON™ idle control module A connector.
>
> Touch one of the multimeter leads to pin 1 of the cab thermostat jumper harness 4-pin connector (the connector on the cab harness).
>
> Touch the other multimeter lead to the positive (+) ICON™ engine harness battery connector ring terminal. Measure the resistance. The multimeter **must** display a reading of 10 ohms or less. If the circuit is **not** closed, isolate the problem to the ICON™ engine, cab, or thermostat jumper harness.
>
> Disconnect the 14-pin pass-through connector at the vehicle's firewall.
>
> Touch one of the multimeter leads to pin A of the 14-pin pass-through connector, engine harness side.
>
> Touch the other multimeter lead to the positive (+) ICON™ engine harness battery connector ring terminal.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of less than 10 ohms, which is a closed circuit.
>
> If the circuit is **not** closed, repair or replace the ICON™ engine harness. Refer to Procedure 019-200 or [[97-019-043 — Engine Wiring Harness|019-043]].
>
> If the circuit is closed, check the cab harness portion of the circuit.
>
> Connect the 14-pin pass-through connector.
>
> Touch one of the multimeter leads to pin 2 of the ICON™ idle control module A harness connector.
>
> Touch the other multimeter lead to the negative (-) ICON™ engine harness connector ring terminal (normally connected to the vehicle battery). Read the value displayed on the multimeter.
>
> Then, touch one of the multimeter leads to pin 2 of the thermostat jumper harness connector (on the end that connects to the thermostat). Touch the other lead to the negative (-) ICON™ engine harness connector ring terminal. Read the value displayed on the multimeter.
>
> For both checks, the multimeter **must** display a reading of 10 ohms or less, which is a closed circuit. If the circuit is **not** closed, isolate the problem to the ICON™ engine, cab, or thermostat jumper harness.
>
> Touch one of the multimeter leads to pin 2 of the ICON™ idle control module A harness connector.
>
> Touch the other multimeter lead to the negative (-) ICON™ engine harness connector ring terminal.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of less than 10 ohms, which is a closed circuit. If the circuit is **not** closed, repair or replace the ICON™ engine harness.
>
> Refer to Procedure 019-208 or 019-197 for harness repair, or Procedure [[97-019-043 — Engine Wiring Harness|019-043]] for harness replacement.
>
> Disconnect the 14-pin pass-through connector at the vehicle's firewall.
>
> Touch one of the multimeter leads to pin C of the 14-pin pass-through connector, engine harness side.
>
> Touch the other multimeter lead to the negative (-) ICON™ engine harness battery connector ring terminal.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of 10 ohms or less, which is a closed circuit. If the circuit is **not** closed, repair or replace the ICON™ engine harness. Refer to Procedure 019-200 or 019-197 for harness repair, or Procedure [[97-019-043 — Engine Wiring Harness|019-043]] for harness replacement.
>
> If the circuit is closed, check the cab harness portion of the circuit.
>
> Cab Harness Check
>
> Disconnect the cab thermostat jumper harness from the cab harness. Touch one of the multimeter leads to pin 1 of the cab thermostat jumper harness 4-pin connector (the connector on the cab harness under the dash).
>
> Touch the other multimeter lead to pin A of the 14-pin pass-through connector, cab harness side.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of less than 10 ohms, which is a closed circuit. If the circuit is **not** closed, repair or replace the ICON™ cab harness. Refer to Procedure [[97-019-305 — Cab Wiring Harness|019-305]].
>
> Touch one of the multimeter leads to pin 2 of the cab thermostat jumper harness connector (the connector on the cab harness).
>
> Touch the other multimeter lead to pin C of the 14-pin pass-through connector, cab harness side.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of less than 10 ohms, which is a closed circuit. If the circuit is **not** closed, repair or replace the cab harness. Refer to Procedure [[97-019-305 — Cab Wiring Harness|019-305]].
>
> Cab Thermostat Jumper Harness Check
>
> Touch one of the multimeter leads to pin 1 of the 4-pin cab thermostat jumper harness connector, jumper harness side. This connector is located on the end of the cab thermostat jumper harness that connects to the cab harness.
>
> Touch the other multimeter lead to pin 1 of the cab thermostat jumper harness connector on the end of the harness that connects to the thermostat's power/data 4-pin connector.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of 10 ohms or less which is a closed circuit.
>
> If the circuit is **not** closed, replace the cab thermostat jumper harness. Refer to Procedure [[97-019-295 — Cab Thermostat Harness|019-295]].
>
> Touch one of the multimeter leads to pin 2 of the 4-pin thermostat jumper harness connector, jumper harness side. This connector is located on the end of the thermostat jumper harness that connects to the cab harness.
>
> Touch the other multimeter lead to pin 2 of the thermostat jumper harness connector, the connector located on the end of the harness that connects to the thermostat's power and data 4-pin connector.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of 10 ohms or less, which is a closed circuit.
>
> If the circuit is **not** closed, repair or replace the thermostat jumper harness. Refer to Procedure [[97-019-295 — Cab Thermostat Harness|019-295]].
>
> ICON™ Battery Connectors to Datalink Check
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To avoid personal injury, always ventilate the compartment before servicing the batteries. To avoid arcing, remove the negative (-) battery cable first and attach the negative (-) cable last.
>
> Turn the keyswitch to the OFF position. Disconnect the vehicle battery cables from the battery.
>
> **Note · Примечание**
> Disconnecting the vehicle battery connections can require that the engine ECM real-time clock be reset using INSITE™.
>
> Remove the ICON™ engine harness positive (+) battery connector from the battery terminal post.
>
> Remove the OEM datalink (6-pin or 9-pin) connector cap.
>
> Set the multimeter to measure resistance.
>
> **Note · Примечание**
> Check the OEM wiring diagram to confirm the positive and negative datalink connector pin assignments. The following steps describe a “typical” vehicle configuration, but possibly will **not** correspond to your vehicle's configuration.
>
> Touch one of the multimeter leads to the positive (+) chassis battery harness connector ring terminal.
>
> Touch the other multimeter lead to the pin attached to the positive (+) battery wire in the datalink connector (typically, pin C in the 6-pin Deutsch connector or pin B in the 9-pin Deutsch connector).
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of less than 10 ohms, which is a closed circuit.
>
> If the circuit is **not** closed, repair or replace the OEM wiring connected to the datalink connector.
>
> Refer to the OEM troubleshooting and repair manual.
>
> Touch one of the multimeter leads to the positive (+) OEM battery harness connector ring terminal. Touch the other multimeter lead to the battery terminal post in the keyswitch assembly.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of less than 10 ohms, which is a closed circuit. If the circuit is **not** closed, repair or replace the OEM harness.
>
> Refer to the OEM troubleshooting and repair manual.
>
> Remove the OEM harness negative (-) battery connector from the battery terminal post.
>
> Touch one of the multimeter leads to the negative (-) OEM harness connector ring terminal.
>
> Touch the other multimeter lead to the pin attached to the negative (-) battery wire in the datalink connector (typically, pin E in the 6-pin Deutsch connectors or pin A in the 9-pin Deutsch connector).
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of less than 10 ohms, which is a closed circuit.
>
> If the circuit is **not** closed, repair or replace the OEM harness or isolate cable to right battery.
>
> Refer to the OEM troubleshooting and repair manual.
