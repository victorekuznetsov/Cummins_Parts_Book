---
aliases:
  - "Клапан отсечки топлива"
type: "Процедура"
doc: "98-019-050"
title_en: "Fuel Shutoff Valve"
title_ru: "Клапан отсечки топлива"
modified: "2004-12-14"
engines:
  - "37269910"
  - "37280605"
families:
  - "K19"
manuals:
  - "3666070"
figures: 14
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-019-050.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-019-050.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K19"
  - "группа/98"
  - "перевод/машинный"
---

# Fuel Shutoff Valve
**Клапан отсечки топлива**

> [!abstract] Процедура · `98-019-050`
> **Двигатели:** [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]]
> **Семейство:** K19
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2004-12-14
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-019-050.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-019-050.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Клапан отключения топлива устанавливается поверх электронного модуля управления топливом.

Проверьте клапан, чтобы убедиться, что он имеет правильный рейтинг напряжения. На корпусе клапана проштампованы напряжение и номер детали.

![[19801709.png]]

### Первичная проверка

Проверьте винт переопределения, чтобы убедиться, что клапан открыт.

- Поверните винт **по часовой стрелке**, чтобы запереть клапан в открытом положении.
- Поверните винт **против часовой стрелки**, чтобы отключить механический переоборудование клапана.

> [!note] Примечание
> Для запуска двигателя в случае электрического сбоя поверните ручку клапана на запорном клапане **по часовой стрелке**, чтобы открыть клапан. Это позволит вручную открыть клапан.

![[19802008.png]]

Большинство клапанов заземлены внутри. Если клапан имеет длинный и короткий столб, короткий столб заземлен внутри.

> [!note] Примечание
> Если есть только один столб, клапан заземлен внутри. Большинство приложений CENTRYTM будут использовать однопостовый клапан.

![[19802009.png]]

Убедитесь, что все гайки проводного соединения плотные, независимо от того, подключен ли провод или нет.

![[19802010.png]]

Используйте проволочную щетку для очистки коррозийных терминальных столбов.

![[19802011.png]]

Убедитесь, что катушка запорного клапана имеет правильное напряжение.

Напряжение катушки и номер детали отбрасываются в конец терминального соединения катушки.

![[19802012.png]]

### Снятие

Отсоедините топливные трубки от клапана отключения топлива.

Отсоедините провод питания напряжением от отключения топлива соленоида.

![[19801965.png]]

Удалите два болта, мойки и шайбы, обеспечивающие запорный клапан топлива к модулю EFC.

Удалите клапан отключения топлива.

![[19801966.png]]

### Разборка

Удалите четыре крепежных болта, обеспечивающих запорный клапан топлива соленоид, на запорный клапан топлива.

Удалите соленоидный корпус, топливный щит, пружинную шайбу, клапанный диск, приводной диск и приводной корпус. Уплотнительные кольца утилизируйте.

![[19800920.png]]

### Очистка и проверка при повторном использовании

> [!danger] ОПАСНО
> При очистке растворителями, кислотами и щелочными составами соблюдайте указания их изготовителя. Работайте в защитных очках и защитной одежде, чтобы снизить риск травмы.

> [!danger] ОПАСНО
> Некоторые растворители огнеопасны и токсичны. Перед применением прочитайте указания изготовителя.

> [!danger] ОПАСНО
> При работе со сжатым воздухом применяйте защиту глаз и лица. Разлетающиеся частицы и грязь могут привести к травме.

> [!note] Примечание
> **не** получить раствор на соленоиде. Очистите соленоид сухой тканью. Используйте 200-гритовую салфетку на плоской поверхности, чтобы отполировать соленоидную поверхность.

Используйте растворитель для очистки всех частей**, кроме **соленоида.

Просушите сжатым воздухом.

Проверьте топливный щит, пружинную шайбу, клапанный диск, приводной диск и корпус привода для грязи, разделения склеивания, коррозии, трещин или износа. Проверка диска (5) и электронного органа управления (8) на предмет чрезмерного износа. Замените любые части, если это необходимо.

![[gr8vaka.png]]

Измерить сопротивление отключения топлива клапанной катушки. Отключите провод питания напряжением. Выберите функцию сопротивления на мультиметре. Прикосновение к одному из мультиметров приводит к терминалу запорного клапана топлива. Прикосновение к другому мультиметру приводит к хорошей, чистой поверхности на блоке двигателя. Измерьте сопротивление. Если сопротивление **не** в пределах спецификаций, замените клапан.

| Топливная система Shutoff клапан Solenoid |  |  |
|---|---|---|
| Напряжение | Минимум сопротивления (Омс) | Максимальное сопротивление (Омс) |
| 6 VDC | 1 | 5 |
| 12 VDC | 6 | 15 |
| 24 VDC | 24 | 50 |
| 32 VDC | 42 | 80 |
| 36 VDC | 46 | 87 |
| 48 VDC | 92 | 145 |
| 74 VDC | 315 | 375 |
| 115 ВАС | 645 | 735 |

> [!note] Примечание
> Если соленоид показывает 0 Ом, в катушке есть электрический шорт.

![[19801712.png]]

### Сборка

> [!warning] ОСТОРОЖНО
> Очистить все компоненты перед сборкой. Грязные компоненты могут привести к тому, что двигатель не выключится.

Собрать запорный клапан следующим образом:

Установите новое о-кольцо (6) между прокладкой (7) и электронным корпусом клапана управления (8).

Установите прокладку (7), кольцевой канавкой к катушке. Установите приводной диск (5) со стороной чашки в сторону соленоида. Установите пружинную шайбу (3) с боковой стороны чашки в сторону соленоида.

Выровнять приводной диск (5), прокладку (7) и клапанный диск (4) на корпусе электронного управляющего клапана (8). Установите новое кольцо (6) между прокладкой (7) и приводным диском (5).

Положите пружинную шайбу (3) на клапанный диск (4), причем полость боковой расположена вверх, в положении вокруг клапанного локатора.

> [!note] Примечание
> Соленоид должен быть ориентирован с электрическим соединительным стойкой на дне.

Установите топливный экран (2) и соленоид (1) на корпус электронного управляющего клапана (8). Установите новые болты o-кольцев и затяните болты.

> [!tip] Момент затяжки
> 8 Н·м [71 фунт-дюйм]

![[19800921.png]]

### Установка

Установите топливный выключатель соленоид и затяните два болта.

> [!tip] Момент затяжки
> 14 Н·м [124 фунт-дюйм]

![[19801966.png]]

Подключите топливный трубопровод к клапану отключения топлива.

Подключите провод питания напряжения к соленоиду отключения топлива.

![[19801965.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> The fuel shutoff valve is mounted on top of the electronic fuel control module.
>
> Check the valve to make sure it has the correct voltage rating. The voltage and part number are stamped on the case of the valve.
>
> ### Initial Check
>
> Check the override screw to be sure the valve is open.
>
> - Turn the screw **clockwise** to lock the valve in the open position.
> - Turn the screw **counterclockwise** to disable the valve mechanical override.
>
> **Note · Примечание**
> To start the engine, in case of an electrical failure, turn the valve knob on the shutoff valve **clockwise** to open the valve. This will manually open the valve.
>
> Most of the valves are internally grounded. If the valve has a long post and a short post, the short post is internally grounded.
>
> **Note · Примечание**
> If there is **only** one post, the valve is internally grounded. Most CENTRY™ applications will use a single-post valve.
>
> Make sure all of the wire connection nuts are tight, whether a wire is attached or **not**.
>
> Use a wire brush to clean corroded terminal posts.
>
> Make sure the shutoff valve coil is the correct voltage.
>
> The coil voltage and part number are cast into the terminal connection end of the coil.
>
> ### Remove
>
> Disconnect the fuel tubing from the fuel shutoff valve.
>
> Disconnect the voltage supply wire from the fuel shutoff solenoid.
>
> Remove the two capscrews, lockwashers, and washers securing the fuel shutoff valve to the EFC module.
>
> Remove the fuel shutoff valve.
>
> ### Disassemble
>
> Remove the four mounting capscrews securing the fuel shutoff valve solenoid to the fuel shutoff valve.
>
> Remove the solenoid housing, fuel shield, spring washer, valve disc, actuator disc, and actuator housing. Discard the o-rings.
>
> ### Clean and Inspect for Reuse
>
> **WARNING · Опасно**
> When using solvents, acids, or alkaline materials for cleaning, follow the manufacturer's recommendations for use. Wear goggles and protective clothing to reduce the possibility of personal injury.
>
> **WARNING · Опасно**
> Some solvents are flammable and toxic. Read the manufacturer's instructions before using.
>
> **WARNING · Опасно**
> Wear appropriate eye and face protection when using compressed air. Flying debris and dirt can cause personal injury.
>
> **Note · Примечание**
> Do **not** get solution on the solenoid. Clean the solenoid with a dry cloth. Use 200-grit emery cloth on a flat surface to polish the solenoid surface.
>
> Use solvent to clean all of the parts **except** the solenoid.
>
> Dry with compressed air.
>
> Check the fuel shield, spring washer, valve disc, actuator disc, and actuator housing for dirt, bonding separation, corrosion, cracks, or wear. Inspect disk (5) and electronic control body (8) for excessive wear. Replace any parts if necessary.
>
> Measure the resistance of the fuel shutoff valve coil. Disconnect the voltage supply wire. Select the resistance function on the multimeter. Touch one of the multimeter leads to the fuel shutoff valve terminal. Touch the other multimeter lead to a good, clean surface on the engine block. Measure the resistance. If the resistance is **not** within specifications, replace the valve.
>
> | Fuel System Shutoff Valve Solenoid Specifications |  |  |
> |---|---|---|
> | Voltage | Resistance Minimum (Ohms) | Resistance Maximum (Ohms) |
> | 6 VDC | 1 | 5 |
> | 12 VDC | 6 | 15 |
> | 24 VDC | 24 | 50 |
> | 32 VDC | 42 | 80 |
> | 36 VDC | 46 | 87 |
> | 48 VDC | 92 | 145 |
> | 74 VDC | 315 | 375 |
> | 115 VAC | 645 | 735 |
>
> **Note · Примечание**
> If the solenoid shows 0 ohms, there is an electrical short in the coil.
>
> ### Assemble
>
> **CAUTION · Осторожно**
> Clean all components before assembly. Dirty components can cause the engine not to shut down.
>
> Reassemble the shutoff valve as follows:
>
> Install a new o-ring (6) between the spacer (7) and the electronic control valve body (8).
>
> Install the spacer (7), o-ring groove toward the coil. Install the actuator disc (5) with the cup side toward the solenoid. Install the spring washer (3) with the cup side toward the solenoid.
>
> Align the actuator disc (5), spacer (7), and valve disc (4) on the electronic control valve body (8). Install a new o-ring (6) between the spacer (7) and the actuator disc (5).
>
> Put the spring washer (3) on the valve disc (4), with the cavity side positioned upward, in a position around the valve locator.
>
> **Note · Примечание**
> The solenoid **must** be orientated with the electrical connection post on the bottom.
>
> Install the fuel shield (2) and solenoid (1) on the electronic control valve body (8). Install new capscrew o-rings and tighten the capscrews.
>
> **Момент затяжки · Torque Value**
> 8 n•m [71 in-lb]
>
> ### Install
>
> Install the fuel shutoff solenoid and tighten the two capscrews.
>
> **Момент затяжки · Torque Value**
> 14 n•m [124 in-lb]
>
> Connect the fuel tubing to the fuel shutoff valve.
>
> Connect the voltage supply wire to the fuel shutoff solenoid.
