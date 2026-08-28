---
aliases:
  - "Клапан отсечки топлива"
type: "Процедура"
doc: "01-019-050"
title_en: "Fuel Shutoff Valve"
title_ru: "Клапан отсечки топлива"
modified: "2004-12-15"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 12
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-019-050.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-019-050.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Fuel Shutoff Valve
**Клапан отсечки топлива**

> [!abstract] Процедура · `01-019-050`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2004-12-15
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-019-050.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-019-050.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Проверка сопротивления

Убедитесь, что катушка запорного клапана имеет правильное напряжение (24 или 12 ВДК).

Напряжение катушки и номер детали отбрасываются в конец терминального соединения катушки.

![[fp8vacf.png]]

Удалите соленоидный провод.

Используйте мультиметр для проверки сопротивления катушки.

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

Если сопротивление катушки не соответствует спецификации, катушка должна быть заменена.

Установите соленоидный провод, когда ремонт завершен.

![[19802552.png]]

### Проверка напряжения

Убедитесь, что катушка запорного клапана имеет правильное напряжение (12 или 24 ВДК).

Напряжение катушки и номер детали отбрасываются в конец терминального соединения катушки.

![[fp8vacf.png]]

Установите переключатель Run/Stop в положение Run.

Используйте мультиметр для проверки напряжения на катушке.

Напряжение должно быть таким же, как напряжение батареи.

Установите переключатель Run/Stop в положение Stop.

![[19802553.png]]

### Снятие

> [!note] Примечание
> Соленоид отключения топлива является средним приводом на топливной системе HPI-TP. Он расположен на корпусе подачи топлива.

Очистите клапан отключения топлива и окружающую область.

Отсоедините клапан отключения топлива от электропроводки двигателя.

Удалите крепежные болты.

![[05c00046.png]]

> [!note] Примечание
> Соленоид отключения топлива устанавливается на корпусе клапана управления топливной системой QST30.

> [!note] Примечание
> Соленоид отключения топлива устанавливается на корпусе управляющего клапана топливной системы HPI-PT.

Очистите клапан отключения топлива и окружающую область.

Отсоедините клапан отключения топлива от электропроводки двигателя.

Удалите крепежные болты.

![[19800920.png]]

### Проверка при повторном использовании

> [!danger] ОПАСНО
> При очистке растворителями, кислотами и щелочными составами соблюдайте указания их изготовителя. Работайте в защитных очках и защитной одежде, чтобы снизить риск травмы.

> [!danger] ОПАСНО
> Некоторые растворители огнеопасны и токсичны. Перед применением прочитайте указания изготовителя.

> [!danger] ОПАСНО
> При работе со сжатым воздухом применяйте защиту глаз и лица. Разлетающиеся частицы и грязь могут привести к травме.

Используйте минеральные спирты для очистки всех частей, кроме соленоида.

Просушите сжатым воздухом.

> [!note] Примечание
> **не*** получить раствор на соленоиде. Очистите соленоид сухой тканью. Используйте 200-гритовую салфетку и плоскую поверхность для полировки соленоидной поверхности.

Проверьте топливный щит, пружинную стиральную машину, клапанный диск, приводной диск и корпус привода для грязи, разделения склеивания, коррозии, трещин или износа. Замените любые части, если это необходимо.

![[gr8vaka.png]]

Осмотрите прокладку клапана отключения топлива на предмет повреждения или износа. Если есть повреждения или износ, замените часть.

![[19400741.png]]

Используйте проволочную щетку для очистки любой коррозии от соленоидного терминала.

![[19802551.png]]

Проверьте соленоид с помощью мультиметра.

Используйте мультиметр для проверки сопротивления катушки.

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

Если сопротивление катушки не соответствует спецификациям, катушка должна быть заменена.

Установите соленоидный провод, когда ремонт завершен.

![[19802552.png]]

### Установка

Соберите запорный клапан, как показано. Установите эти части следующим образом.

Установите новое о-кольцо (6) между прокладкой (7) и электронным корпусом клапана управления (8).

Установите прокладку (7) кольцевой канавки по направлению к катушке. Установите приводной диск (5) со стороной чашки в сторону соленоида. Установите пружинную шайбу (3) с боковой стороны чашки в сторону соленоида.

Выровнять приводной диск (5), прокладку (7) и клапанный диск (4) на корпусе электронного управляющего клапана (8). Установите новое кольцо (6).

Положите пружинную шайбу (3) на клапанный диск (4), причем полость боковой расположена вверх, в положении вокруг клапанного локатора.

> [!note] Примечание
> Соленоид должен быть ориентирован с электрическим соединительным стойкой на дне.

Установите топливный экран (2) и соленоид (1) на корпус электронного управляющего клапана (8). Установите новое о-кольцо и затяните болты.

> [!tip] Момент затяжки
> 8 Н·м [72 фунт-дюйм]

![[19800921.png]]

Установите электрическое соединение клапана отключения топлива. Установите гайку на резьбовый столб соленоида.

Используйте два гаечных ключа. Держите пост ореха крепко, затягивая при этом соединение ореха.

> [!tip] Момент затяжки
> 3 Н·м [27 фунт-дюйм]

![[05400020.png]]


> [!quote]- Original (English) · английский оригинал
> ### Resistance Check
>
> Make sure the shutoff valve coil is the correct voltage (24 or 12 VDC).
>
> The coil voltage and part number are cast into the terminal connection end of the coil.
>
> Remove the solenoid wire.
>
> Use the multimeter to check the coil resistance.
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
> If the coil resistance does **not** meet specification, the coil **must** be replaced.
>
> Install the solenoid wire when the repair is complete.
>
> ### Voltage Check
>
> Make sure the shutoff valve coil is the correct voltage (12 or 24 VDC).
>
> The coil voltage and part number are cast into the terminal connection end of the coil.
>
> Set the Run/Stop switch to the Run position.
>
> Use a multimeter to check the voltage to the coil.
>
> The voltage **must** be the same as the battery voltage.
>
> Set the Run/Stop switch to the Stop position.
>
> ### Remove
>
> **Note · Примечание**
> The fuel shutoff solenoid is the middle actuator on the HPI-TP fuel system. It is located on the fuel delivery housing.
>
> Clean the fuel shutoff valve and surrounding area.
>
> Disconnect the fuel shutoff valve from the engine harness.
>
> Remove the mounting capscrews.
>
> **Note · Примечание**
> The fuel shutoff solenoid is mounted on the control valve body on the QST30 fuel system.
>
> **Note · Примечание**
> The fuel shutoff solenoid is mounted on the control valve body on the HPI-PT fuel system.
>
> Clean the fuel shutoff valve and surrounding area.
>
> Disconnect the fuel shutoff valve from the engine harness.
>
> Remove the mounting capscrews.
>
> ### Inspect for Reuse
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
> Use mineral spirits to clean all of the parts except the solenoid.
>
> Dry with compressed air.
>
> **Note · Примечание**
> Do **not** get solution on the solenoid. Clean the solenoid with a dry cloth. Use 200-grit emery cloth and a flat surface to polish the solenoid surface.
>
> Check the fuel shield, spring washer, valve disc, actuator disc, and actuator housing for dirt, bonding separation, corrosion, cracks, or wear. Replace any parts if necessary.
>
> Inspect the fuel shutoff valve spacer for damage or wear. If damage or wear is present, replace the part.
>
> Use a wire brush to clean any corrosion from the solenoid terminal.
>
> Check the solenoid with a multimeter.
>
> Use the multimeter to check the coil resistance.
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
> If the solenoid shows 0 ohm, there is an electrical short in the coil.
>
> If the coil resistance does **not** meet specifications, the coil **must** be replaced.
>
> Install the solenoid wire when the repair is complete.
>
> ### Install
>
> Assemble the shutoff valve as shown. Install these parts as follows.
>
> Install a new o-ring (6) between the spacer (7) and the electronic control valve body (8).
>
> Install the spacer (7) o-ring groove toward the coil. Install the actuator disc (5) with the cup side toward the solenoid. Install the spring washer (3) with the cup side toward the solenoid.
>
> Align the actuator disc (5), spacer (7), and valve disc (4) on the electronic control valve body (8). Install a new o-ring (6).
>
> Put the spring washer (3) on the valve disc (4), with the cavity side positioned upward, in a position around the valve locator.
>
> **Note · Примечание**
> The solenoid **must** be orientated with the electrical connection post on the bottom.
>
> Install the fuel shield (2) and solenoid (1) on the electronic control valve body (8). Install a new o-ring and tighten the capscrews.
>
> **Момент затяжки · Torque Value**
> 8 n•m [72 in-lb]
>
> Install the electrical connection of the fuel shutoff valve. Install the nut on the threaded post of the solenoid.
>
> Use two wrenches. Hold the post of the nut firmly while tightening the connection nut.
>
> **Момент затяжки · Torque Value**
> 3 n•m [27 in-lb]
