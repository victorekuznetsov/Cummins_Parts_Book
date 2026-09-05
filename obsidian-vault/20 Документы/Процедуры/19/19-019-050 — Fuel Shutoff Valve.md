---
aliases:
  - "Клапан отсечки топлива"
type: "Процедура"
doc: "19-019-050"
title_en: "Fuel Shutoff Valve"
title_ru: "Клапан отсечки топлива"
modified: "2004-12-07"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
  - "85017333"
families:
  - "QSK23"
  - "QSK60"
manuals:
  - "3666113"
figures: 15
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-019-050.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-019-050.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
  - "перевод/машинный"
---

# Fuel Shutoff Valve
**Клапан отсечки топлива**

> [!abstract] Процедура · `19-019-050`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2004-12-07
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-019-050.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-019-050.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Снятие

Удалить ECM. См. процедуру[[19-019-031 — Engine Control Module|019-031]].

![[05400015.png]]

Очистите клапан отключения топлива и окружающую область.

![[05400016.png]]

Удалите гайки, обеспечивающие электрические соединения запорного клапана топлива соленоида. Удалите связи.

![[05400020.png]]

Удалите четыре крепежных болта.

Удалите соленоидный корпус, топливный щит, пружинную шайбу, клапанный диск, приводной диск и приводной корпус.

Уплотнительные кольца утилизируйте.

![[19800920.png]]

### Проверка при повторном использовании

Используйте минеральные спирты для очистки всех частей, кроме соленоида.

> [!note] Примечание
> **не** получить раствор на соленоиде. Очистите соленоид сухой тканью. Используйте 200-гритовую салфетку и плоскую поверхность для полировки соленоидной поверхности.

Проверьте топливный щит, пружинную шайбу, клапанный диск, приводной диск и корпус привода для грязи, разделения склеивания, коррозии, трещин или износа. Замените любые части, если это необходимо.

![[gr8vaka.png]]

Осмотрите прокладку клапана отключения топлива на предмет повреждения или износа.

Если есть повреждения или износ, замените часть.

![[19400741.png]]

Используйте проволочную щетку для очистки любой коррозии от соленоидных терминальных столбов.

![[fp8vaea.png]]

Проверьте соленоид с помощью мультиметра. Замените соленоид, если сопротивление **не** по спецификации.

| Топливная система Shutoff клапан Спецификация |  |  |
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

![[19400895.png]]

Затяните гайки, которые удерживают электрические соединительные столбы на соленоиде топливного отключающего клапана.

> [!tip] Момент затяжки
> 3 Н·м [27 фунт-дюйм]

![[05400022.png]]

### Установка

Установите новое кольцо (6) в корпус электронного клапана (8).

Установите кожух (7) привода с помощью канавки с кольцом по направлению к катушке (1).

Установите приводной диск (5) со стороной чашки в сторону катушки (1).

Поместите резиновую сторону на клапанный диск (4) на приводной диск (5).

Установите пружину (3) клапана со стороной чашки к катушке. Внутренний диаметр пружины (3)** должен** опираться на диаметр лоцмана клапанного диска (4).

Установите новое о-кольцо (6) в корпус привода (7).

Установите топливный экран (2) и катушку (1) на переднюю крышку (8).

Затяните четыре болта.

> [!tip] Момент затяжки
> 8 Н·м [71 фунт-дюйм]

![[19800921.png]]

Установите электрические соединения на клапан отключения топлива. Установите гайку на резьбовый столб соленоида.

Используйте два 3/8 в гаечных ключах. Держите пост гайки крепко, затягивая при этом соединение гайки. Повторите для второго терминала.

> [!tip] Момент затяжки
> 2 Н·м [18 фунт-дюйм]

![[05400020.png]]

Установите ECM. См. процедуру[[19-019-031 — Engine Control Module|019-031]].

![[05400015.png]]

### Проверка сопротивления

Убедитесь, что катушка запорного клапана имеет правильное напряжение (24 VDC).

Напряжение катушки и номер детали отбрасываются в конец терминального соединения катушки.

![[19400490.png]]

Удалите соленоидные провода.

Используйте мультиметр для проверки сопротивления катушки.

| Топливная система Shutoff клапан Спецификация |  |  |
|---|---|---|
| Напряжение | Минимум сопротивления (Омс) | Максимальное сопротивление (Омс) |
| 6 VDC | 1.72 | 2.02 |
| 12 VDC | 6 | 15 |
| 24 VDC | 24 | 50 |
| 32 VDC | 42 | 80 |
| 36 VDC | 54.5 | 61.5 |
| 48 VDC | 105 | 125 |
| 74 VDC | 323 | 367 |
| 115 ВАС | 645 | 735 |

Если сопротивление катушки не соответствует спецификации, катушка должна быть заменена.

Установите соленоидные провода после завершения ремонта.

![[19400895.png]]

### Проверка напряжения

Используйте мультиметр для проверки напряжения на катушке. Измерьте напряжение от подсоединения соленоида к заземлению блока двигателя. Мультиметр **должен** показывать напряжение батареи.

Прокрутите двигатель, чтобы обеспечить напряжение к клеммам запорного клапана топлива.

После того, как ECM получил сигнал 50 об/мин, напряжение будет оставаться поданным в клапан отключения топлива до тех пор, пока переключатель зажигания не будет приведен в положение выключения.

![[fv2swkb.png]]


> [!quote]- Original (English) · английский оригинал
> ### Remove
>
> Remove the ECM. Refer to Procedure [[19-019-031 — Engine Control Module|019-031]].
>
> Clean the fuel shutoff valve and surrounding area.
>
> Remove the nuts securing the electrical connections of the fuel shutoff valve solenoid. Remove the connections.
>
> Remove the four mounting capscrews.
>
> Remove the solenoid housing, fuel shield, spring washer, valve disc, actuator disc, and actuator housing.
>
> Discard the o-rings.
>
> ### Inspect for Reuse
>
> Use mineral spirits to clean all of the parts except the solenoid.
>
> **Note · Примечание**
> Do **not** get solution on the solenoid. Clean the solenoid with a dry cloth. Use 200-grit emery cloth and a flat surface to polish the solenoid surface.
>
> Check the fuel shield, spring washer, valve disc, actuator disc, and actuator housing for dirt, bonding separation, corrosion, cracks, or wear. Replace any parts if necessary.
>
> Inspect the fuel shutoff valve spacer for damage or wear.
>
> If damage or wear is present, replace the part.
>
> Use a wire brush to clean any corrosion from the solenoid terminal posts.
>
> Check the solenoid with a multimeter. Replace the solenoid if the resistance is **not** to specification.
>
> | Fuel System Shutoff Valve Specifications |  |  |
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
> Tighten the nuts that hold the electrical connection posts on the fuel shutoff valve solenoid.
>
> **Момент затяжки · Torque Value**
> 3 n•m [27 in-lb]
>
> ### Install
>
> Install a new o-ring (6) into the electronic control valve body (8).
>
> Install the actuator housing (7) with the o-ring groove toward the coil (1).
>
> Install the actuator disc (5) with the cup side toward the coil (1).
>
> Place the rubber side to the valve disc (4) on the actuator disc (5).
>
> Install the valve spring (3) with the cup side toward the coil. The inner diameter of the spring (3) **must** rest on the pilot diameter of the valve disc (4).
>
> Install a new o-ring (6) into the actuator housing (7).
>
> Install the fuel shield (2) and coil (1) on to the front cover (8).
>
> Tighten the four capscrews.
>
> **Момент затяжки · Torque Value**
> 8 n•m [71 in-lb]
>
> Install the electrical connections on the fuel shutoff valve. Install the nut on the threaded post of the solenoid.
>
> Use two 3/8 in wrenches. Hold the post of the nut firmly while tightening the connection nut. Repeat for second terminal.
>
> **Момент затяжки · Torque Value**
> 2 n•m [18 in-lb]
>
> Install the ECM. Refer to Procedure [[19-019-031 — Engine Control Module|019-031]].
>
> ### Resistance Check
>
> Make sure the shutoff valve coil is the correct voltage (24 VDC).
>
> The coil voltage and part number are cast into the terminal connection end of the coil.
>
> Remove the solenoid wires.
>
> Use the multimeter to check the coil resistance.
>
> | Fuel System Shutoff Valve Specifications |  |  |
> |---|---|---|
> | Voltage | Resistance Minimum (Ohms) | Resistance Maximum (Ohms) |
> | 6 VDC | 1.72 | 2.02 |
> | 12 VDC | 6 | 15 |
> | 24 VDC | 24 | 50 |
> | 32 VDC | 42 | 80 |
> | 36 VDC | 54.5 | 61.5 |
> | 48 VDC | 105 | 125 |
> | 74 VDC | 323 | 367 |
> | 115 VAC | 645 | 735 |
>
> If the coil resistance does **not** meet specification, the coil **must** be replaced.
>
> Install the solenoid wires after completing the repair.
>
> ### Voltage Check
>
> Use a multimeter to check the voltage to the coil. Measure the voltage from the solenoid's supply connection to the engine block ground. The multimeter **must** show battery voltage.
>
> Crank the engine to provide voltage to the fuel shutoff valve terminals.
>
> Once the ECM has received the 50-rpm signal, the voltage will remain supplied to the fuel shutoff valve until the keyswitch is cycled to the OFF position.
