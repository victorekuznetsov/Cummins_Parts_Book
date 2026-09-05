---
aliases:
  - "Цепь входа блокировки"
type: "Процедура"
doc: "82-019-307"
title_en: "Interlock Input Circuit"
title_ru: "Цепь входа блокировки"
modified: "2005-01-28"
engines:
  - "41343322"
  - "41370103"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 31
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-307.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-019-307.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# Interlock Input Circuit
**Цепь входа блокировки**

> [!abstract] Процедура · `82-019-307`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section 19 - Electronic Engine Controls
> **Даты:** изменён 2005-01-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-307.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-019-307.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Проверка сопротивления

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Для уменьшения возможности дуги сначала удалите отрицательный (-) кабель батареи и прикрепите отрицательный (-) кабель батареи последним.

Переведите замок зажигания в положение OFF.

Отсоедините кабели аккумулятора автомобиля от батареи.

> [!note] Примечание
> Отключение аккумуляторных батарей автомобиля может потребовать сброса часов ECM в режиме реального времени с помощью INSITETM.

![[ea8coha.png]]

> [!warning] ОСТОРОЖНО
> Для уменьшения возможности повреждения штифта и проводов жгута проводов используйте пробный щуп, номер детали 3822758 и 3822917, при проведении измерений.

Проверьте часть цепи с помощью проводов двигателя.

Отсоедините разъем электропроводки привода и разъем электропроводки датчика от ECM.

Убедитесь, что шортинговая вилка ICONTM подключена к 6-контактному разъему для проводов двигателя. Отключите 31-контактный OEM-разъем.

Установите мультиметр для измерения сопротивления.

![[19c00892.png]]

> [!note] Примечание
> Убедитесь, что все переключатели блокировки закрыты, прежде чем приступить к следующей электрической проверке.

Прикосновение к одному из мультиметров приводит к контакту 14 привода проводов ремня разъема.

Прикосновение к другому мультиметру приводит к контакту 27 с 31-контактным OEM-разъемом проводов жгута проводов, сбоку ремня электропроводки двигателя

Считайте показания мультиметра.

![[19c00728.png]]

Мультиметр **должен **отображать значение менее 10 Ом, что является замкнутой схемой.

Если схема **не **закрыта, проверьте шортинг-розетку ICONTM.

![[19801619.png]]

Отсоедините шортинговый штепсель ICONTM от 6-контактного разъема проводов двигателя.

Прикосновение к мультиметру приводит к контакту 5 шортинга ICONTM. Прикосновение к другому мультиметру приводит к контакту 4 шортинга ICONTM. Считайте показания мультиметра.

Мультиметр **должен** отображать показания менее 10 Ом (замкнутая схема).

Если цепь **не **закрыта, замените штепсельную вилку. См. руководство изготовителя машины по диагностике и ремонту. Если шортинг пробка тесты хорошо, ремонт или замена двигателя проводов жгута. См. процедуру[[99-019-206 — Deutsch DTM and DTP Connector Series|019-206]]для ремонта жгутов проводов и процедуры[[82-019-043-tr — Engine Wiring Harness|019-043]]Замена проводов на упряжь.

![[19c00730.png]]

Проверьте OEM проводку жгута стороны цепи.

Отсоедините стартовую реле ICONTM от электропроводки OEM. Отсоедините разъём OEM-проводов от ECM.

Прикосновение к одному из мультиметров приводит к контакту 27 с 31-контактным OEM-разъемом, OEM-проводкой с жгутом проводов. Прикосновение к другому мультиметру приводит к разъему реле реле ICONTM, 31-контактному разъему. Считайте показания мультиметра.

Мультиметр **должен **показывать показания менее 10 Ом, что является замкнутой схемой. Если цепь **не** закрыта, отремонтируйте или замените электропроводку OEM. См. процедуру 019-071.

![[19c00731.png]]

Прикосновение к одному из мультиметров приводит к контакту 33 50-контактного OEM-разъема проводов ремня. Прикосновение к другому мультиметру приводит к контакту 86 разъема реле реле ICONTM стартера, стороны ECM или эквивалентного штифта на стороне ECM реле. См. диаграмму проводов ISM, Бюллетень 3666269. Считайте показания мультиметра.

Мультиметр **должен **показывать показания менее 10 Ом, что является замкнутой схемой. Если цепь **не** закрыта, отремонтируйте или замените электропроводку OEM. См. процедуру 019-071.

![[19c00726.png]]

Прикосновение к одному из мультиметров приводит к контакту 20 с 31-контактным OEM-разъемом, OEM-проводкой с жгутом проводов. Прикосновение к другому мультиметру приводит к контакту 33 с 50-контактным разъемом OEM-проводов. Считайте показания мультиметра.

Мультиметр **должен **показывать показания менее 10 Ом, что является замкнутой схемой. Если цепь **не **закрыта, проверьте каждый переключатель блокировки, чтобы увидеть, является ли дефектный переключатель причиной открытой цепи.

![[19c00727.png]]

Проверьте переключатели блокировки.

Отключите выключатель стояночного тормоза от проводной упряжки OEM. Прикосновение к одному из мультиметров приводит к контакту 1 (или А) разъема коммутатора, переключателя сбоку. Прикосновение к другому мультиметру приводит к контакту 2 (или B) разъема. Считайте показания мультиметра.

Мультиметр **должен **показывать показания менее 10 Ом, что является замкнутой схемой. Если схема **не** закрыта, замените выключатель. См. руководство по OEM.

Если цепь закрыта, то проверьте два других переключателя блокировки для открытой цепи таким же образом. Замените любые дефектные переключатели. Если все три переключателя показывают замкнутую цепь, отремонтируйте или замените проводку OEM. См. процедуру 019-071.

После ремонта подсоедините все компоненты.

![[19c00753.png]]

### Проверка на замыкание на массу

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Чтобы снизить риск искрения, минусовой (-) провод аккумуляторной батареи снимайте первым, а подсоединяйте последним.

Переведите замок зажигания в положение OFF. Отсоедините кабели аккумулятора автомобиля от батареи.

> [!note] Примечание
> Отключение аккумуляторных батарей автомобиля может потребовать сброса часов ECM в режиме реального времени с помощью INSITETM.

![[ea8coha.png]]

> [!warning] ОСТОРОЖНО
> Для уменьшения возможности повреждения штифта и проводов жгута проводов используйте пробный щуп, номер детали 3822758 и 3822917, при проведении измерений.

Отсоедините переключатель блокировки нейтрального положения, переключатель блокировки наклона капота и переключатель блокировки стояночного тормоза от электропроводки OEM.

Установите мультиметр для измерения сопротивления.

![[19c00732.png]]

Проверьте нейтральное положение переключателя блокировки.

Прикосновение к одному из мультиметров приводит к контакту А (или 1) нейтрального переключателя положения, на стороне переключателя разъема. Прикоснитесь к другому мультиметру, который приведет к заземлению блока двигателя. Считайте показания мультиметра.

Затем касание одного из мультиметров приводит к контакту В (или 2) нейтрального переключателя положения, на стороне переключателя разъема. Прикоснитесь к другому мультиметру, который приведет к заземлению блока двигателя. Считайте показания мультиметра.

![[19c00733.png]]

Для обеих проверок пин-кодов мультиметр **должен **отображать показания более 100k ом, что является открытой схемой.

Если схема **не **открыта, есть короткое замыкание на землю.

Замените нейтральный переключатель. См. руководство изготовителя машины по диагностике и ремонту.

![[19801621.png]]

Проверьте переключатель блокировки наклона капота.

Прикосновение к одному из мультиметров приводит к контакту А (или 1) выключателя наклона капота, на стороне переключателя разъема. Прикоснитесь к другому мультиметру, который приведет к заземлению блока двигателя. Считайте показания мультиметра.

Затем касание одного из мультиметров приводит к контакту В (или 2) выключателя наклона капота, на стороне переключателя разъема. Прикоснитесь к другому мультиметру, который приведет к заземлению блока двигателя. Считайте показания мультиметра.

![[19c00733.png]]

Для обеих проверок пин-кодов мультиметр **должен **отображать показания более 100k ом, что является открытой схемой.

Если схема **не **открыта, есть короткое замыкание на землю.

Замените выключатель наклона капота. См. руководство изготовителя машины по диагностике и ремонту.

![[19801621.png]]

Проверьте переключатель блокировки стояночного тормоза.

Прикосновение к одному из мультиметров приводит к контакту А (или 1) переключателя стояночного тормоза, на стороне переключателя разъема. Прикоснитесь к другому мультиметру, который приведет к заземлению блока двигателя. Считайте показания мультиметра.

Затем касание одного из мультиметров приводит к контакту В (или 2) с выключателем стояночного тормоза, на стороне переключателя разъема. Прикоснитесь к другому мультиметру, который приведет к заземлению блока двигателя. Считайте показания мультиметра.

![[19c00733.png]]

Для обеих проверок пин-кодов мультиметр **должен **отображать показания более 100k ом, что является открытой схемой.

Если схема **не **открыта, есть короткое замыкание на землю.

Замените выключатель стояночного тормоза. См. руководство изготовителя машины по диагностике и ремонту.

После ремонта подсоедините все компоненты.

![[19801621.png]]

### Проверка на замыкание между контактами

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Чтобы снизить риск искрения, минусовой (-) провод аккумуляторной батареи снимайте первым, а подсоединяйте последним.

Переведите замок зажигания в положение OFF. Отсоедините кабели аккумулятора автомобиля от батареи.

> [!note] Примечание
> Отключение аккумуляторных батарей автомобиля может потребовать сброса часов ECM в режиме реального времени с помощью INSITETM.

![[ea8coha.png]]

> [!warning] ОСТОРОЖНО
> Для уменьшения возможности повреждения штифта и проводов жгута проводов используйте пробный щуп, номер детали 3822758, при проведении измерений.

Отсоедините проводку привода и разъёмы проводов датчика от ECM.

Отключите 31-контактный OEM-разъем.

Убедитесь, что шортинговая вилка ICONTM подключена к 6-контактному разъему для проводов двигателя.

Установите мультиметр для измерения сопротивления.

![[19c00892.png]]

Прикосновение к одному из мультиметров приводит к контакту 14 привода проводов ремня разъема.

Прикосновение к другому мультиметру приводит ко всем другим штифтам в разъеме электропроводки привода, по одному за раз.

Затем повторите проверку контакта с контактом от контакта 14 разъёма проводов привода к разъему ремня со всеми штифтами в разъеме проводов датчика.

Считайте показания мультиметра.

![[19c00893.png]]

Мультиметр **must** отображает показания более 100k ом, что является открытой схемой. Если схема не открыта, между контактом 14 и любым штифтом в любом разъёме жгута проводов есть короткое замыкание, которое зарегистрировало замкнутую цепь.

Ремонт или замена ремня электропроводки двигателя. См. процедуру[[82-019-043-tr — Engine Wiring Harness|019-043]].

![[19801621.png]]

Повторите проверку контакта с контактом из контакта 46 разъёма проводов привода со всеми другими штифтами в разъеме проводов привода.

Считайте показания мультиметра.

Мультиметр **must** отображает показания более 100k ом, что является открытой схемой. Если схема не открыта, между контактом 46 и любым другим штифтом, который зарегистрировал замкнутую цепь, есть короткое замыкание.

Ремонт или замена ремня электропроводки двигателя. См. процедуру[[82-019-043-tr — Engine Wiring Harness|019-043]].

![[19c00735.png]]

Отсоедините разъём OEM-проводов от ECM.

Прикосновение к одному из мультиметров приводит к контакту 33 с OEM-разъемом проводов ремня.

Прикосновение к другому мультиметру приводит ко всем другим штифтам в разъеме, по одному за раз.

Считайте показания мультиметра.

![[19c00754.png]]

Мультиметр **must** отображает показания более 100k ом, что является открытой схемой. Если схема не открыта, между контактом 33 и любым другим штифтом, который зарегистрировал замкнутую цепь, есть короткое замыкание.

Ремонт или замена OEM проводов жгута. См. процедуру 019-071.

После ремонта подсоедините все компоненты.

![[19801621.png]]

### Проверьте короткое замыкание на источнике внешнего напряжения

> [!warning] ОСТОРОЖНО
> Для уменьшения возможности повреждения штифта и проводов жгута проводов используйте пробный щуп, номер детали 3822758 и 3822917, при проведении измерений.

Отключите нейтральный переключатель положения от проводной ремни OEM. Отключите выключатель стояночного тормоза от проводной упряжки OEM. Отсоедините переключатель наклона капота от электропроводки OEM.

Установите мультиметр для измерения VDC.

Переведите замок зажигания в положение ON.

![[19c00732.png]]

Проверьте нейтральное положение переключателя блокировки.

Прикосновение к одному из мультиметров приводит к контакту А (или 1) с нейтральным положением коммутатора проводов ремня разъема. Прикоснитесь к другому мультиметру, который приведет к заземлению блока двигателя. Считайте показания мультиметра.

Затем касание одного из мультиметров приводит к контакту В (или 2) с нейтральным положением коммутатора проводов ремня разъема. Прикоснитесь к другому мультиметру, который приведет к заземлению блока двигателя. Считайте показания мультиметра.

![[19c00733.png]]

Для обеих проверок пин-кодов мультиметр **должен отображать показания менее 1,5 VDC. Если напряжение **не менее 1,5 ВДК, то происходит короткое замыкание к внешнему источнику напряжения.

> [!note] Примечание
> Внешним источником напряжения является любой провод в OEM или проводах двигателя, который несет напряжение.

Удалите внешний источник напряжения.

![[19c00724.png]]

Проверьте переключатель блокировки наклона капота.

Прикосновение к одному из мультиметров приводит к контакту А (или 1) с разъемом наклонной проводов вытяжки. Прикоснитесь к другому мультиметру, который приведет к заземлению блока двигателя. Считайте показания мультиметра.

Затем касание одного из мультиметров приводит к контакту В (или 2) с вытяжным переключателем наклона проводов жгута разъема. Прикоснитесь к другому мультиметру, который приведет к заземлению блока двигателя. Считайте показания мультиметра.

![[19c00733.png]]

Для обеих проверок пин-кодов мультиметр **должен отображать показания менее 1,5 VDC. Если напряжение **не менее 1,5 ВДК, то происходит короткое замыкание к внешнему источнику напряжения.

> [!note] Примечание
> Внешним источником напряжения является любой провод в OEM или проводах двигателя, который несет напряжение.

Удалите внешний источник напряжения.

![[19c00724.png]]

Проверьте переключатель блокировки стояночного тормоза.

Прикосновение к одному из мультиметров приводит к контакту А (или 1) разъема жгута с автостоянкой тормозного переключателя. Прикоснитесь к другому мультиметру, который приведет к заземлению блока двигателя. Считайте показания мультиметра.

Затем касание одного из мультиметров приводит к контакту В (или 2) с разъемом жгута автостояночного тормоза. Прикоснитесь к другому мультиметру, который приведет к заземлению блока двигателя. Считайте показания мультиметра.

![[19c00733.png]]

Для обеих проверок пин-кодов мультиметр **должен отображать показания менее 1,5 VDC. Если напряжение **не менее 1,5 ВДК, то происходит короткое замыкание к внешнему источнику напряжения.

> [!note] Примечание
> Внешним источником напряжения является любой провод в OEM или проводах двигателя, который несет напряжение.

Удалите внешний источник напряжения.

После ремонта подсоедините все компоненты.

![[19c00724.png]]


> [!quote]- Original (English) · английский оригинал
> ### Resistance Check
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first, and attach the negative (-) battery cable last.
>
> Turn the keyswitch to the OFF position.
>
> Disconnect the vehicle battery cables from the battery.
>
> **Note · Примечание**
> Disconnecting the vehicle battery connections can require that the engine ECM real-time clock be reset using INSITE™.
>
> **CAUTION · Осторожно**
> To reduce the possibility of pin and harness damage, use test leads, Part Number 3822758 and 3822917, when taking a measurement.
>
> Check the engine harness portion of the circuit.
>
> Disconnect the actuator harness connector and the sensor harness connector from the ECM.
>
> Make sure the ICON™ shorting plug is connected to the 6-pin engine harness connector. Disconnect the 31-pin OEM connector.
>
> Set the multimeter to measure resistance.
>
> **Note · Примечание**
> Verify that all interlock switches are closed before proceeding with the following electrical check.
>
> Touch one of the multimeter leads to pin 14 of the actuator harness connector.
>
> Touch the other multimeter lead to pin 27 of the 31-pin OEM harness connector, engine harness side
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of less than 10 ohms, which is a closed circuit.
>
> If the circuit is **not** closed, check the ICON™ shorting plug.
>
> Disconnect the ICON™ shorting plug from the 6-pin engine harness connector.
>
> Touch the multimeter lead to pin 5 of the ICON™ shorting plug. Touch the other multimeter lead to pin 4 of the ICON™ shorting plug. Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of less than 10 ohms (closed circuit).
>
> If the circuit is **not** closed, replace the shorting plug. Refer to the OEM troubleshooting and repair manual. If the shorting plug tests okay, repair or replace the engine harness. Refer to Procedure [[99-019-206 — Deutsch DTM and DTP Connector Series|019-206]] for harness repairs, and Procedure [[82-019-043-tr — Engine Wiring Harness|019-043]] for harness replacement.
>
> Check the OEM harness side of the circuit.
>
> Disconnect the ICON™ starter relay from the OEM harness. Disconnect the OEM harness connector from the ECM.
>
> Touch one of the multimeter leads to pin 27 of the 31-pin OEM connector, OEM harness side. Touch the other multimeter lead to the ICON™ starter relay harness connector, 31-pin connector side. Read the value displayed on the multimeter.
>
> The multimeter **must** show a reading of less than 10 ohms, which is a closed circuit. If the circuit is **not** closed, repair or replace the OEM harness. Refer to Procedure 019-071.
>
> Touch one of the multimeter leads to pin 33 of the 50-pin OEM harness connector. Touch the other multimeter lead to pin 86 of the ICON™ starter relay harness connector, ECM side, or the equivalent pin on the ECM side of the relay. Refer to the ISM wiring diagram, Bulletin 3666269. Read the value displayed on the multimeter.
>
> The multimeter **must** show a reading of less than 10 ohms, which is a closed circuit. If the circuit is **not** closed, repair or replace the OEM harness. Refer to Procedure 019-071.
>
> Touch one of the multimeter leads to pin 20 of the 31-pin OEM connector, OEM harness side. Touch the other multimeter lead to pin 33 of the 50-pin OEM harness connector. Read the value displayed on the multimeter.
>
> The multimeter **must** show a reading of less than 10 ohms, which is a closed circuit. If the circuit is **not** closed, check each interlock switch to see if a defective switch is the cause of the open circuit.
>
> Check the interlock switches.
>
> Disconnect the parking brake switch from the OEM harness. Touch one of the multimeter leads to pin 1 (or A) of the switch connector, switch side. Touch the other multimeter lead to pin 2 (or B) of the connector. Read the value displayed on the multimeter.
>
> The multimeter **must** show a reading of less than 10 ohms, which is a closed circuit. If the circuit is **not** closed, replace the switch. Refer to the OEM manual.
>
> If the circuit is closed, test the other two interlock switches for an open circuit in the same manner. Replace any defective switches. If all three switches show a closed circuit, repair or replace the OEM harness. Refer to Procedure 019-071.
>
> Connect all components after completing the repair.
>
> ### Check for Short Circuit to Ground
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> Turn the keyswitch to the OFF position. Disconnect the vehicle battery cables from the battery.
>
> **Note · Примечание**
> Disconnecting the vehicle battery connections can require that the engine ECM real-time clock be reset using INSITE™.
>
> **CAUTION · Осторожно**
> To reduce the possibility of pin and harness damage, use test leads, Part No 3822758 and 3822917, when taking a measurement.
>
> Disconnect the neutral position interlock switch, the hood tilt interlock switch, and the parking brake interlock switch from the OEM harness.
>
> Set the multimeter to measure resistance.
>
> Check the neutral position interlock switch.
>
> Touch one of the multimeter leads to pin A (or 1) of the neutral position switch, on the switch side of the connector. Touch the other multimeter lead to engine block ground. Read the value displayed on the multimeter.
>
> Then, touch one of the multimeter leads to pin B (or 2) of the neutral position switch, on the switch side of the connector. Touch the other multimeter lead to engine block ground. Read the value displayed on the multimeter.
>
> For both pin checks, the multimeter **must** display a reading of more than 100k ohms, which is an open circuit.
>
> If the circuit is **not** open, there is a short circuit to ground.
>
> Replace the neutral position switch. Refer to the OEM troubleshooting and repair manual.
>
> Check the hood tilt interlock switch.
>
> Touch one of the multimeter leads to pin A (or 1) of the hood tilt switch, on the switch side of the connector. Touch the other multimeter lead to engine block ground. Read the value displayed on the multimeter.
>
> Then, touch one of the multimeter leads to pin B (or 2) of the hood tilt switch, on the switch side of the connector. Touch the other multimeter lead to engine block ground. Read the value displayed on the multimeter.
>
> For both pin checks, the multimeter **must** display a reading of more than 100k ohms, which is an open circuit.
>
> If the circuit is **not** open, there is a short circuit to ground.
>
> Replace the hood tilt switch. Refer to the OEM troubleshooting and repair manual.
>
> Check the parking brake interlock switch.
>
> Touch one of the multimeter leads to pin A (or 1) of the parking brake switch, on the switch side of the connector. Touch the other multimeter lead to engine block ground. Read the value displayed on the multimeter.
>
> Then, touch one of the multimeter leads to pin B (or 2) of the parking brake switch, on the switch side of the connector. Touch the other multimeter lead to engine block ground. Read the value displayed on the multimeter.
>
> For both pin checks, the multimeter **must** display a reading of more than 100k ohms, which is an open circuit.
>
> If the circuit is **not** open, there is a short circuit to ground.
>
> Replace the parking brake switch. Refer to the OEM troubleshooting and repair manual.
>
> Connect all components after completing the repair.
>
> ### Check for Short Circuit from Pin to Pin
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> Turn the keyswitch to the OFF position. Disconnect the vehicle battery cables from the battery.
>
> **Note · Примечание**
> Disconnecting the vehicle battery connections can require that the engine ECM real-time clock be reset using INSITE™.
>
> **CAUTION · Осторожно**
> To reduce the possibility of pin and harness damage, use test lead, Part No 3822758, when taking a measurement.
>
> Disconnect the actuator harness and sensor harness connectors from the ECM.
>
> Disconnect the 31-pin OEM connector.
>
> Make sure the ICON™ shorting plug is connected to the 6-pin engine harness connector.
>
> Set the multimeter to measure resistance.
>
> Touch one of the multimeter leads to pin 14 of the actuator harness connector.
>
> Touch the other multimeter lead to all other pins in the actuator harness connector, one at a time.
>
> Then repeat the pin-to-pin check from pin 14 of the actuator harness connector to all pins in the sensor harness connector.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of more than 100k ohms, which is an open circuit. If the circuit is **not** open, there is a short circuit between pin 14 and any pin in either harness connector that registered a closed circuit.
>
> Repair or replace the engine harness. Refer to Procedure [[82-019-043-tr — Engine Wiring Harness|019-043]].
>
> Repeat the pin-to-pin check from pin 46 of the actuator harness connector to all other pins in the actuator harness connector.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of more than 100k ohms, which is an open circuit. If the circuit is **not** open, there is a short circuit between pin 46 and any other pin that registered a closed circuit.
>
> Repair or replace the engine harness. Refer to Procedure [[82-019-043-tr — Engine Wiring Harness|019-043]].
>
> Disconnect the OEM harness connector from the ECM.
>
> Touch one of the multimeter leads to pin 33 of the OEM harness connector.
>
> Touch the other multimeter lead to all other pins in the connector, one at a time.
>
> Read the value displayed on the multimeter.
>
> The multimeter **must** display a reading of more than 100k ohms, which is an open circuit. If the circuit is **not** open, there is a short circuit between pin 33 and any other pin that registered a closed circuit.
>
> Repair or replace the OEM harness. Refer to Procedure 019-071.
>
> Connect all components after completing the repair.
>
> ### Check for Short Circuit to External Voltage Source
>
> **CAUTION · Осторожно**
> To reduce the possibility of pin and harness damage, use test leads, Part Number 3822758 and 3822917, when taking a measurement.
>
> Disconnect the neutral position switch from the OEM harness. Disconnect the parking brake switch from the OEM harness. Disconnect the hood tilt switch from the OEM harness.
>
> Set the multimeter to measure VDC.
>
> Turn the keyswitch to the ON position.
>
> Check the neutral position interlock switch.
>
> Touch one of the multimeter leads to pin A (or 1) of the neutral position switch harness connector. Touch the other multimeter lead to engine block ground. Read the value displayed on the multimeter.
>
> Then, touch one of the multimeter leads to pin B (or 2) of the neutral position switch harness connector. Touch the other multimeter lead to engine block ground. Read the value displayed on the multimeter.
>
> For both pin checks, the multimeter **must** display a reading of less than 1.5 VDC. If the voltage is **not** less than 1.5 VDC, there is a short circuit to an external voltage source.
>
> **Note · Примечание**
> An external voltage source is any wire in the OEM or engine harness wiring that carries voltage.
>
> Remove the external voltage source.
>
> Check the hood tilt interlock switch.
>
> Touch one of the multimeter leads to pin A (or 1) of the hood tilt switch harness connector. Touch the other multimeter lead to engine block ground. Read the value displayed on the multimeter.
>
> Then, touch one of the multimeter leads to pin B (or 2) of the hood tilt switch harness connector. Touch the other multimeter lead to engine block ground. Read the value displayed on the multimeter.
>
> For both pin checks, the multimeter **must** display a reading of less than 1.5 VDC. If the voltage is **not** less than 1.5 VDC, there is a short circuit to an external voltage source.
>
> **Note · Примечание**
> An external voltage source is any wire in the OEM or engine harness wiring that carries voltage.
>
> Remove the external voltage source.
>
> Check the parking brake interlock switch.
>
> Touch one of the multimeter leads to pin A (or 1) of the parking brake switch harness connector. Touch the other multimeter lead to engine block ground. Read the value displayed on the multimeter.
>
> Then, touch one of the multimeter leads to pin B (or 2) of the parking brake switch harness connector. Touch the other multimeter lead to engine block ground. Read the value displayed on the multimeter.
>
> For both pin checks, the multimeter **must** display a reading of less than 1.5 VDC. If the voltage is **not** less than 1.5 VDC, there is a short circuit to an external voltage source.
>
> **Note · Примечание**
> An external voltage source is any wire in the OEM or engine harness wiring that carries voltage.
>
> Remove the external voltage source.
>
> Connect all components after completing the repair.
