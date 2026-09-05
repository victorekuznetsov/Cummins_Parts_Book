---
type: "Процедура"
doc: "98-019-102"
title_en: "Fuel Control Valve"
modified: "2022-08-09"
engines:
  - "37269910"
  - "37280605"
families:
  - "K19"
manuals:
  - "3666070"
figures: 28
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-019-102.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-019-102.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K19"
  - "группа/98"
  - "перевод/машинный"
---

# Fuel Control Valve

> [!abstract] Процедура · `98-019-102`
> **Двигатели:** [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]]
> **Семейство:** K19
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]]
> **Секции:** Section 19 - Electronic Controls - Group 19 · Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2022-08-09
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-019-102.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-019-102.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Клапан EFC содержится в модуле EFC, который устанавливается непосредственно на топливный насос.

Схема состоит из клапана EFC и проводов подачи и возврата клапана EFC, которые соединены с основным соединительным разъемом 21 и 10 проводов двигателя соответственно.

![[19801790.png]]

### Проверка

Инструменты электронной службы INSITETM, CompulinkTM или EchekTM могут использоваться для выполнения испытания на приведение в действие клапана EFC, который производит звуковой щелчок звука от EFC, если он движется свободно. Этот тест может быть использован для определения того, прилипает ли клапан EFC.

Используя INSITETM, в меню «Тесты» выберите «Актуатор управления топливом». Следуйте инструкциям в окне.

![[19800109.png]]

Дисплеи CompulinkTM будут использоваться на следующих этапах, но дисплеи EchekTM будут похожими.

Из главного меню нажмите клавишу «1», чтобы ввести устранение неполадок.

Выберите опцию главного меню CompulinkTM:

1. устранение неполадок

2. Параметры и корректировки

3. Идентификация системы и датаплате

4. CompulinkTM File Manager

5. Калибровочные переводы

6. коммунальные услуги

Активные ключи: 1-6, Вернуться, Помогите.

![[nobox.png]]

Затем нажмите клавишу «4», чтобы ввести специальные функции.

Выберите опцию меню устранения неполадок:

1. Информация о коде ошибки

2. Монитор

3. Устранение неполадок дерево

4. Специальные функции

Активные ключи: 1-4, Вернуться, Помогите.

![[nobox.png]]

Для того чтобы ввести тест на привод управления топливом, нажмите «1» в меню «Специальные функции».

Выберите опцию меню Специальные функции:

1. Испытание привода управления топливом

2. Читать Аудиторский след

Активные ключи: 1 к 2, Вернуться, Помочь, СПНК.

![[nobox.png]]

> [!note] Примечание
> Двигатель **не должен** работать при выполнении испытания привода управления топливом.

Чтобы запустить тест, убедитесь, что замок зажигания включен с двигателем **не**. Нажмите кнопку «*» на CompulinkTM. Слышный щелкающий звук должен быть слышен из клапана EFC.

Испытание привода управления топливом

Нажмите клавишу «*», чтобы открыть и закрыть клапан EFC звуковым щелчком.

Положение клапана -> - -[ ] - -

Активные ключи: "*", CNCL.

![[nobox.png]]

Если звуковой щелчок **не** слышен из клапана EFC, то клапан прилипает. После проверки электропроводки цепи EFC на клапан и подачу и возврат клапана ([[98-019-030 — EFC Module|См. процедуру 019-030]]в разделе 19) клапан следует снять и осмотреть.

> [!note] Примечание
> Этот тест **не** определит, является ли клапан EFC только частично прилипшим. Если есть подозрение, что его движение ограничено, то клапан следует снять и осмотреть.

![[19801969.png]]

### Тест на утечку

Проверьте клапан EFC, чтобы убедиться, что он не застрял в открытом состоянии или не допускает чрезмерную утечку.

Запустите двигатель и нагрейте температуру охлаждающей жидкости до по меньшей мере 65 ° C \[150°F\]. При холостом ходу двигателя отсоедините **один** клапана главного разъема электропроводки двигателя.

Если двигатель не выключен, замените клапан EFC. Если двигатель действительно выключен, клапан все еще может быть причиной повышенного низкого холостого хода. Устранение этого симптома. См. раздел TS для соответствующей диаграммы симптомов устранения неполадок.

![[19801959.png]]

### Снятие

Если имеется электронный инструмент обслуживания, выполните тест привода EFC.

Если клапан EFC **не** щелкает, то удалите и проверьте клапан EFC.

![[19800109.png]]

Отсоедините электрические провода от клапана.

![[19801959.png]]

> [!warning] ОСТОРОЖНО
> Не нажимайте и не вытягивайте клапан. Если клапан застрял в модуле, удалите модуль, чтобы получить более прочное сцепление с клапаном. См. процедуру 019-030.

Удалите три болта, которые удерживают клапан в модуле EFC.

Осторожно вытащите клапан из модуля EFC.

![[19801960.png]]

### Проверка при повторном использовании

Осмотрите привод, чтобы убедиться, что он **не **прилипает. Удерживайте крепежный фланж EFC и поверните внутреннее ядро, которое крепится к пружине. Ядро должно свободно поворачиваться и возвращаться в исходное положение силой пружины. Если он делает **не** или если рукав имеет трещины в нем, замените привод EFC.

> [!note] Примечание
> **Не** Удалить пружины возврата из привода клапана. Клапан EFC может быть поврежден.

![[19801969.png]]

Осмотрите клеммные столбы привода EFC на наличие трещин, коррозии и повреждений от дуги. Если повреждение терминала существует, замените клапан EFC.

![[19801969.png]]

Осмотрите крепежный цилиндр EFC в модуле CENTRYTM на предмет повреждения, которое может вызвать утечку. Осмотрите мусор в цилиндре для крепления. Если повреждены или повреждены обломки, очистите или замените модуль EFC.

![[19801971.png]]

Установите новое о-кольцо на 2-дюймовый диаметр клапана EFC. Установите два новых кольца на ствол клапана EFC.

> [!note] Примечание
> Углы на стволе клапана EFC имеют разные размеры.

![[19801972.png]]

Используйте чистое моторное масло для смазки колец.

#### Почтовые стойки:

- Каждый привод EFC немного отличается по своей производительности. Ручной рычаг согнут для настройки привода EFC в соответствии с требованиями к калибровке, предъявляемыми производителем. Пост рычага может быть согнут в нескольких направлениях для калибровки производительности EFC.
- Если рычаг рычага согнут к центру клапана EFC, это изменение уменьшает количество силы, которую рычаг рычага пружина может оказывать на ротор.
- Если столб согнут за борт, это изменение добавляет весеннее напряжение и увеличивает силу, которую рычаг рычага пружина может оказывать на ротор.
- Некоторые сообщения могут быть прямыми, в зависимости от индивидуальной производительности привода EFC.

#### Сломанный рычаг оружия:

- Если рычаг ручки разбит, не заменяйте пружину, так как клапан EFC будет не калиброван. Должна быть заменена EFC клапан.

#### Играть в Governor Shaft:

- Если есть опасения, что существует чрезмерная игра между вращающимся клапанным валом и вращающимся корпусом клапанного вала (золотой секцией). Клапан EFC должен быть заменен. В настоящее время нет никаких спецификаций для установления чрезмерной игры, кроме того, что не должно быть большой разницы между подозрительным клапаном EFC и новым клапаном EFC.

#### Cracks & Fractures:

- Осмотрите вращающийся корпус вала клапана (золотой секцией) на наличие переломов волосяного покрова, которые предполагают, что корпус выходит из строя и позволяет топливу просачиваться. Если обнаружены переломы, клапан EFC должен быть заменен.

Установите клапан EFC в модуль EFC. Фланец клапана будет находиться на расстоянии около 9,5 мм \[3/8 дюйма \] от корпуса.

![[19801973.png]]

> [!warning] ОСТОРОЖНО
> Не заставляйте клапан входить в модуль; чрезмерная сила может повредить клапан или кольца.

Используя ладонь руки, толкайте и вращайте клапан EFC на 30 градусов. Вращайте клапан до тех пор, пока не выровняются монтажные отверстия.

![[19801974.png]]

Установите три шестиглавых болта. Эти болты имеют пленные пружинные шайбы и не требуют стопорных шайб.

Затягивайте болты, пока они не станут жесткими.

![[19801975.png]]

Затворы клапана EFC должны быть сжаты в следующей последовательности:

1. Затягивайте болты 1/8 поворота в последовательности, показанной на рисунке, пока они не усаживаются.

![[19801976.png]]

1. Затягивайте болты в показанной последовательности.

> [!tip] Момент затяжки
> 2.8 Н·м [25 фунт-дюйм]

![[19801977.png]]

1. Затягивайте болты в показанной последовательности.

> [!tip] Момент затяжки
> 5.6 Н·м [50 фунт-дюйм]

![[19801978.png]]

1. Полностью выключите все три болта.

![[19801979.png]]

1. Затягивайте болты снова в показанной последовательности.

> [!tip] Момент затяжки
> 2.8 Н·м [25 фунт-дюйм]

![[19801977.png]]

1. Снова затягивай болты.

> [!tip] Момент затяжки
> 5.6 Н·м [50 фунт-дюйм]

Эта процедура позволит убедиться, что привод правильно установлен.

![[19801978.png]]

Установите модуль на топливный насос, если это необходимо.[[98-019-030 — EFC Module|См. процедуру 019-030]].

![[19801967.png]]

### Проверка сопротивления

Убедитесь, что цифровой мультиметр используется для измерения всех электронных параметров клапанов EFC.

Отсоедините разъемы клапанных терминалов.

Измерить сопротивление клапана EFC. Выберите функцию сопротивления на мультиметре. Прикосновение к одному из мультиметров приводит к одному из клапанных терминалов. Прикосновение к другому мультиметру приводит к другому клапанному терминалу.

![[19801791.png]]

Измерьте сопротивление. Измеренное сопротивление должно падать в диапазонах, показанных ниже. Если измеренное сопротивление **не** в этих диапазонах, то заменить клапан EFC.

|  | 12-VDC клапан | 24-VDC клапан |
|---|---|---|
| Сопротивление при 22,2°C[72°F] | 2,0-2,2 Ом | 7.1-7.3 Ом |
| Сопротивление при -93,2°C \[-40°F\] | 1,5-1,7 Ом | 5,3-5,5 Ом |
| Сопротивление при 121,1 °C[250°F] | 2.8 - 3,0 Ом | 9.9-10.1 Ом |

![[19801792.png]]

### Проверка на замыкание на массу

Прикосновение к одному из мультиметров приводит к любому клапанному терминалу. Прикосновение к другому мультиметру приводит к корпусу клапана.

Измерьте сопротивление.

Мультиметр **должен **показывать более 100k ом, что является открытой схемой. Если схема **не** открыта, то клапан должен быть заменен.

![[19801793.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> The EFC valve is contained within the EFC module, which is mounted directly on top of the fuel pump.
>
> The circuit consists of the EFC valve and the EFC valve supply and return wires, which are connected to the main engine harness connector pins 21 and 10, respectively.
>
> ### Test
>
> The electronic service tool INSITE™, Compulink™, or Echek™, can be used to perform an actuation test on the EFC valve, which produces an audible clicking sound from the EFC if it is moving freely. This test can be used to determine if the EFC valve is sticking.
>
> Using INSITE™, from the Tests menu, select Fuel Control Actuator. Then, follow the instructions in the window.
>
> The Compulink™ displays will be used in the following steps, but the Echek™ displays will be similar.
>
> From the Main menu, press the “1” key to enter troubleshooting.
>
> Select Compulink™ Main menu option:
>
> 1. Troubleshooting
>
> 2. Parameter & Adjustments
>
> 3. System Identification & Dataplate
>
> 4. Compulink™ File Manager
>
> 5. Calibration Transfers
>
> 6. Utilities
>
> Active Keys: 1 to 6, BACK, HELP.
>
> Next, press the “4” key to enter the special functions.
>
> Select Troubleshooting menu option:
>
> 1. Fault Code Information
>
> 2. Monitor
>
> 3. Troubleshooting Tree
>
> 4. Special Functions
>
> Active Keys: 1 to 4, BACK, HELP.
>
> To enter the fuel control actuator test, press the “1” in the Special Functions menu.
>
> Select Special Functions menu option:
>
> 1. Fuel Control Actuator Test
>
> 2. Read Audit Trail
>
> Active Keys: 1 to 2, BACK, HELP, CNCL.
>
> **Note · Примечание**
> The engine **mustnot** be running when performing the fuel control actuator test.
>
> To run the test, make sure the keyswitch is on with the engine **not** running. Press the “\*” button on the Compulink™. An audible clicking sound should be heard coming from the EFC valve.
>
> Fuel Control Actuator Test
>
> Press the "\*" key to cause the EFC valve to open and close with an audible click.
>
> Valve Position --\> - -\[ \] - -
>
> Active Keys: "\*," CNCL.
>
> If an audible click is **not** heard from the EFC valve, then the valve is sticking. After checking the EFC circuit wiring for the valve and the valve supply and return ([[98-019-030 — EFC Module|Refer to Procedure 019-030]] in Section 19), the valve should be removed and inspected.
>
> **Note · Примечание**
> This test will **not** determine whether or **not** the EFC valve is **only** partially sticking. If it is suspected that its motion is restricted, then the valve should be removed and inspected.
>
> ### Leak Test
>
> Check the EFC valve to make sure it is **not** stuck open or allowing excessive leakage.
>
> Start the engine and warm the coolant temperature to at least 65°C \[ 150°F\]. With the engine idling, disconnect **one** of the EFC valve main engine harness connectors.
>
> If the engine does **not** shut down, replace the EFC valve. If the engine does shut down, the valve can still be the cause of a raised low idle. Troubleshoot this symptom. Refer to Section TS for the appropriate troubleshooting symptom chart.
>
> ### Remove
>
> If an electronic service tool is available, perform the EFC actuator test.
>
> If the EFC valve is **not** clicking, then remove and inspect the EFC valve.
>
> Disconnect the electrical leads from the valve.
>
> **CAUTION · Осторожно**
> Do not force or pry the valve. If the valve is stuck in the module, remove the module to get a firmer grip on the valve. Refer to Procedure 019-030 .
>
> Remove the three capscrews that hold the valve in the EFC module.
>
> Carefully, pull the valve out of the EFC module.
>
> ### Inspect for Reuse
>
> Inspect the actuator to make sure it is **not** sticking. Hold the mounting flange of the EFC and turn the inner core, which is attached to the spring. The core **must** turn freely and return to the original position by spring force. If it does **not** or if the sleeve has cracks in it, replace the EFC actuator.
>
> **Note · Примечание**
> Do **not** remove the return springs from the valve actuator. The EFC valve can be damaged.
>
> Inspect the EFC actuator terminal posts for cracks, corrosion, and damage from arcing. If terminal damage exists, replace the EFC valve.
>
> Inspect the mounting bore of the EFC in the CENTRY™ module for damage, which can cause leakage. Inspect for debris in the mounting bore. If damage or debris exists, clean or replace the EFC module.
>
> Install a new o-ring on the 2-inch diameter of the EFC valve. Install two new o-rings on the EFC valve barrel.
>
> **Note · Примечание**
> The o-rings on the EFC valve barrel are different sizes.
>
> Use clean engine oil to lubricate the o-rings.
>
> #### Lever Arm Posts:
>
> - Each EFC actuator is slightly different in its performance as built. The lever arm post is bent to tune the EFC actuator within its calibration requirements by the manufacturer. The lever arm post can be bent in multiple directions to calibrate the EFC's performance.
> - If the lever arm post is bent towards the center of the EFC valve this change decreases the amount of force that the lever arm spring can exert on the rotor.
> - If the post is bent out-board this change adds spring tension and increases the amount of force that the lever arm spring can exert on the rotor.
> - Some posts can be straight as well depending the individual EFC actuator performance.
>
> #### Broken Lever Arms Springs:
>
> - If the Lever Arm Spring is broken do **not** replace the spring as the EFC valve will be out of calibration. The EFC Valve must be replaced.
>
> #### Play in the Governor Shaft:
>
> - If there is concern that there is excessive play between the rotating valve shaft and the rotating valve shaft housing (gold section). The EFC valve should be replaced. Currently there are no specifications for establishing excessive play other than there should be little difference between the suspect EFC valve and a new EFC valve.
>
> #### Cracks & Fractures:
>
> - Inspect the rotating valve shaft housing (gold section) for hairline fractures that suggest the housing is failing and allowing fuel to leak through. If fractures are found the EFC valve should be replaced.
>
> Install the EFC valve into the EFC module. The valve flange will be about 9.5 mm \[3/8 in\] from the body.
>
> **CAUTION · Осторожно**
> Do not force the valve into the module; excessive force can damage the valve or o-rings.
>
> Using the palm of the hand, push and rotate the EFC valve 30 degrees. Rotate the valve until the mounting holes are aligned.
>
> Install the three hex head capscrews. These capscrews have captive spring washers and do **not** require lock washers.
>
> Tighten the capscrews until they are finger-tight.
>
> The EFC valve capscrews **must** be tightened in the following sequence:
>
> 1. Tighten the capscrews 1/8 of a turn in the sequence shown in the figure until they are seated.
>
> 1. Tighten the capscrews in sequence shown.
>
> **Момент затяжки · Torque Value**
> 2.8 n•m [25 in-lb]
>
> 1. Tighten the capscrews in sequence shown.
>
> **Момент затяжки · Torque Value**
> 5.6 n•m [50 in-lb]
>
> 1. Loosen all three capscrews completely.
>
> 1. Tighten the capscrews again in the sequence shown.
>
> **Момент затяжки · Torque Value**
> 2.8 n•m [25 in-lb]
>
> 1. Tighten the capscrews again.
>
> **Момент затяжки · Torque Value**
> 5.6 n•m [50 in-lb]
>
> This procedure will make sure that the actuator is properly installed.
>
> Install the module onto the fuel pump, if necessary. [[98-019-030 — EFC Module|Refer to Procedure 019-030]].
>
> ### Resistance Check
>
> Ensure that a digital multimeter is used to measure all the EFC valves electronic parameters.
>
> Disconnect the valve terminal connectors.
>
> Measure the resistance of the EFC valve. Select the resistance function on the multimeter. Touch one of the multimeter leads to one of the valve terminals. Touch the other multimeter lead to the other valve terminal.
>
> Measure the resistance. The measured resistance should fall in the ranges shown below. If the measured resistance is **not** in these ranges, then replace the EFC valve.
>
> |  | 12-VDC Valve | 24-VDC Valve |
> |---|---|---|
> | Resistance at 22.2°C \[72°F\] | 2.0 to 2.2 ohms | 7.1 to 7.3 ohms |
> | Resistance at -93.2°C \[-40°F\] | 1.5 to 1.7 ohms | 5.3 to 5.5 ohms |
> | Resistance at 121.1°C \[250°F\] | 2.8 to 3.0 ohms | 9.9 to 10.1 ohms |
>
> ### Check for Short Circuit to Ground
>
> Touch one of the multimeter leads to either valve terminal. Touch the other multimeter lead to the body of the valve.
>
> Measure the resistance.
>
> The multimeter **must** show more than 100k ohms, which is an open circuit. If the circuit is **not** open, then the valve **must** be replaced.
