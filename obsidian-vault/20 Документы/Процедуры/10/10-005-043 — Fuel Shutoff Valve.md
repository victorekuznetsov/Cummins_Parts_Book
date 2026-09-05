---
aliases:
  - "Клапан отсечки топлива"
type: "Процедура"
doc: "10-005-043"
title_en: "Fuel Shutoff Valve"
title_ru: "Клапан отсечки топлива"
modified: "2022-08-29"
engines:
  - "80141463"
  - "80248213"
families:
  - "QSX15"
manuals:
  - "3666239"
  - "3666423"
figures: 8
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/10/10-005-043.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/10-005-043.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSX15"
  - "группа/10"
  - "перевод/машинный"
---

# Fuel Shutoff Valve
**Клапан отсечки топлива**

> [!abstract] Процедура · `10-005-043`
> **Двигатели:** [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSX15
> **Входит в руководства:** [[3666239 — Signature™, ISX, and QSX15 Service Manual|3666239]], [[3666423 — QSX15 Operation and Maintenance Manual|3666423]]
> **Секции:** Section 5 - Fuel System - Group 05 · Section A - Adjustment, Repair, and Replacement
> **Даты:** изменён 2022-08-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/10/10-005-043.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/10-005-043.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Проверка сопротивления

Используйте гаечный ключ, чтобы держать гайку у основания поста.

Используйте 3/8-дюймовый гаечный ключ для удаления гайки, удерживающей электрическое соединение катушки запорного клапана топлива.

Удалите соединение.

![[05c00162.png]]

Используйте проволочную щетку для очистки любой коррозии от терминала катушки.

![[05c00160.png]]

Проверьте сборку катушки с помощью мультиметра. Замените соленоид, если сопротивление **не** по спецификации.

| **Система отключения топлива клапан Solenoid Спецификация** |  |  |
|---|---|---|
| **Вольт** | **Минимальное сопротивление (Ом)** | **Максимальное сопротивление (Ом)** |
| 6 VDC | 1 | 5 |
| 12 VDC | 6 | 15 |
| 24 VDC | 24 | 50 |
| 32 VDC | 42 | 80 |
| 36 VDC | 46 | 87 |
| 48 VDC | 92 | 145 |
| 74 VDC | 315 | 375 |
| 115 ВАС | 645 | 735 |

> [!note] Примечание
> Если в узле катушки показано 0 Ом, в катушке есть электрический шорт.

![[fv8etka.png]]

### Снятие

Удалите четыре болта головы Аллена.

Удалите катушку (1) и топливный экран (2).

Удалите шайбу (3) клапанной пружины, клапанный диск (4) и приводной диск (5) из корпуса (7) привода от IFSM (8).

Откажитесь от колец (6).

![[05c00156.png]]

### Проверка при повторном использовании

> [!danger] ОПАСНО
> При очистке растворителями, кислотами и щелочными составами соблюдайте указания их изготовителя. Работайте в защитных очках и защитной одежде, чтобы снизить риск травмы.

> [!danger] ОПАСНО
> Некоторые растворители огнеопасны и токсичны. Перед применением прочитайте указания изготовителя.

Используйте минеральные спирты. Очистить все детали**, кроме **сборки катушки.

> [!note] Примечание
> Не надо, не надо, на катушку накачивать растворитель. Очистите катушку сухой тканью. Используйте 200-гритровую салфетку и плоскую поверхность для полировки поверхности катушки.

Проверьте клапанный диск, сиденье клапана и приводной диск на наличие грязи, металлических деталей, разделения склеивания, коррозии, трещин или износа. Заменить, если это необходимо.

![[gr8vaka.png]]

### Установка

Соберите запорный клапан, как показано. Установите эти части следующим образом.

Установите новое кольцо между прокладкой и электронным корпусом клапана управления.

Установите прокладку с кольцом прокладки к катушке.

Установите приводной диск со стороной чашки в сторону катушки.

Установите пружинную шайбу со стороной чашки к катушке.

![[05c00046.png]]

Выровнять приводной диск, прокладку и клапанный диск на корпусе электронного управляющего клапана.

Установите новое уплотнительное кольцо.

Положите пружинную шайбу на клапанный диск с стороной полости, расположенной вверх.

> [!note] Примечание
> Катушка **должна** быть ориентирована с помощью электрического соединительного поста на дне.

> [!note] Примечание
> Убедитесь, что катушка запорного клапана имеет правильное напряжение (12 VDC). Напряжение катушки и номер детали отбрасываются в конец терминального соединения катушки.

Установите топливный щит и катушку на переднюю крышку.

Установите новое кольцо и затяните затворы головы Аллена.

> [!tip] Момент затяжки
> 5.6 Н·м [50 фунт-дюйм]

![[05c00046.png]]

Установите электрическое соединение на клапан отключения топлива.

Установите гайку на резьбовый столб катушки.

Используйте гаечный ключ, чтобы крепко удерживать гайку у основания поста при затягивании соединительного гайки.

> [!tip] Момент затяжки
> 3 Н·м [25 фунт-дюйм]

![[05c00161.png]]


> [!quote]- Original (English) · английский оригинал
> ### Resistance Check
>
> Use a wrench to hold the nut at the base of the post.
>
> Use a 3/8-inch wrench to remove the nut holding the electrical connection of the fuel shutoff valve coil.
>
> Remove the connection.
>
> Use a wire brush to clean any corrosion from the coil terminal.
>
> Check the coil assembly with a multimeter. Replace the solenoid if the resistance is **not** to specification.
>
> | **Fuel System Shutoff Valve Solenoid Specifications** |  |  |
> |---|---|---|
> | **Voltage** | **Resistance Minimum (Ohms)** | **Resistance Maximum (Ohms)** |
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
> If the coil assembly shows 0 ohms, there is an electrical short in the coil.
>
> ### Remove
>
> Remove the four Allen head capscrews.
>
> Remove the coil (1) and the fuel shield (2).
>
> Remove the valve spring washer (3), valve disc (4), and actuator disc (5) from the actuator housing (7) from the IFSM (8).
>
> Discard the o-rings (6).
>
> ### Inspect for Reuse
>
> **WARNING · Опасно**
> When using solvents, acids, or alkaline materials for cleaning, follow the manufacturer's recommendations for use. Wear goggles and protective clothing to reduce the possibility of personal injury.
>
> **WARNING · Опасно**
> Some solvents are flammable and toxic. Read the manufacturer's instructions before using.
>
> Use mineral spirits. Clean all of the parts **except** the coil assembly.
>
> **Note · Примечание**
> Do **not** get solvent on the coil. Clean the coil with a dry cloth. Use a 200-grit emery cloth and a flat surface to polish the coil surface.
>
> Check the valve disc, valve seat, and actuator disc for dirt, metal parts, bonding separation, corrosion, cracks, or wear. Replace if necessary.
>
> ### Install
>
> Assemble the shutoff valve as shown. Install these parts as follows.
>
> Install a new o-ring between the spacer and the electronic control valve body.
>
> Install the spacer o-ring groove toward the coil.
>
> Install the actuator disc with the cup side toward the coil.
>
> Install the spring washer with the cup side toward the coil.
>
> Align the actuator disc, spacer, and valve disc on the electronic control valve body.
>
> Install a new o-ring.
>
> Put the spring washer on the valve disc with the cavity side positioned upward.
>
> **Note · Примечание**
> The coil **must** be oriented with the electrical connection post on the bottom.
>
> **Note · Примечание**
> Make sure the shutoff valve coil is the correct voltage (12 VDC). The coil voltage and part number are cast into the terminal connection end of the coil.
>
> Install the fuel shield and coil onto the front cover.
>
> Install a new o-ring and tighten the Allen head capscrews.
>
> **Момент затяжки · Torque Value**
> 5.6 n•m [50 in-lb]
>
> Install the electrical connection on the fuel shutoff valve.
>
> Install the nut onto the threaded post of the coil.
>
> Use a wrench to hold the nut at the base of the post firmly while tightening the connection nut.
>
> **Момент затяжки · Torque Value**
> 3 n•m [25 in-lb]
