---
aliases:
  - "Клапан отсечки топлива"
type: "Процедура"
doc: "35-005-043-tr"
title_en: "Fuel Shutoff Valve"
title_ru: "Клапан отсечки топлива"
modified: "2022-08-29"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "3666322"
  - "4021942"
figures: 9
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/35/35-005-043-tr.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/35-005-043-tr.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/35"
  - "перевод/машинный"
---

# Fuel Shutoff Valve
**Клапан отсечки топлива**

> [!abstract] Процедура · `35-005-043-tr`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[3666322 — ISM, ISMe, and QSM11 Service Manual|3666322]], [[4021942 — QSM11 Industrial Operation and Maintenance Manual|4021942]]
> **Секции:** Section 5 - Fuel System - Group 05 · Section A - Adjustment, Repair, and Replacement
> **Даты:** изменён 2022-08-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/35/35-005-043-tr.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/35-005-043-tr.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Проверка сопротивления

Проверьте, является ли катушка запорного клапана правильным напряжением (12 или 24 VDC).

Напряжение катушки запорного клапана и номер детали отбрасываются в конец концевого соединения катушки запорного клапана.

![[19c01393.png]]

Удали провод.

Проверьте, что оставшийся проводной соединительный гайка плотный. Затяните гайку, если это необходимо.

> [!tip] Момент затяжки
> 3 Н·м [27 фунт-дюйм]

Проверьте, что пост плотный и безопасный в катушке.

> [!note] Примечание
> На топливной системе могут использоваться только одиночные стойкие катушки. Две стойки катушек будут мешать линии охлаждения.

![[fv2swka.png]]

Используйте проволочную щетку для очистки любой коррозии от терминала катушки.

![[fp8vaea.png]]

Проверьте, что катушка провода **не** подключен перед проверкой сопротивления катушки.

Измерить сопротивление катушки с помощью мультиметра, номер детали 3377161, или эквивалента.

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
> Если соленоидное сопротивление равно 0 Ом, то в катушке имеется электрический шорт.

Если сопротивление катушки запорного клапана правильное, сборку клапана **необходимо проверить. Если сопротивление катушки запорного клапана **не соответствует спецификации, катушка запорного клапана должна быть заменена.

![[fv2swkc.png]]

Переключатель зажигания транспортного средства в положение Включения.

Прикоснитесь к проводу к терминалу катушки.

Слушайте, чтобы клапан щелкнул, когда провод прикасается к терминалу катушки. Если клапан **не** щелкнет, отремонтируйте или замените клапан отключения топлива.

![[fv8elka.png]]

### Проверка напряжения

> [!warning] ОСТОРОЖНО
> Чтобы избежать повреждения ECM, подсоедините к топливу только один провод, выключающий соленоид.

Подключите провод.

Напряжение катушки и номер детали отбрасываются в конец терминального соединения катушки.

![[05200178.png]]

Переключатель зажигания транспортного средства в положение Включения.

Проверьте напряжение на катушке с помощью мультиметра, номер детали 3377161 или эквивалента.

Напряжение должно быть таким же, как напряжение батареи.

Переключатель зажигания транспортного средства в положение выключения.

![[fv2swkb.png]]

### Снятие

Очистите клапан отключения топлива и окружающую область.

Отсоедините кольцевой терминал от запорного клапана соленоида.

Удалите крепежные болты, обеспечивающие запорный клапан соленоида.

Удалите выключаемый клапан соленоид.

![[19200408.png]]

### Установка

Установите новое кольцо на клапан отключения топлива.

Установите запорный клапан и болты.

> [!tip] Момент затяжки
> 4 Н·м [35 фунт-дюйм]

Подсоедините запорный клапан к электропроводке привода.

> [!tip] Момент затяжки
> 3 Н·м [27 фунт-дюйм]

![[19200408.png]]


> [!quote]- Original (English) · английский оригинал
> ### Resistance Check
>
> Verify the shutoff valve coil is the correct voltage (12 or 24 VDC).
>
> The shutoff valve coil voltage and part number are cast into the terminal connection end of the shutoff valve coil.
>
> Remove the wire.
>
> Verify the remaining wire connection nut is tight. Tighten the nut, if required.
>
> **Момент затяжки · Torque Value**
> 3 n•m [27 in-lb]
>
> Verify the post is tight and secure in the coil.
>
> **Note · Примечание**
> Only single post coils can be used on the fuel system. Two post coils will interfere with the cooling line.
>
> Use a wire brush to clean any corrosion from the coil terminal.
>
> Verify the coil wire is **not** connected before checking the coil resistance.
>
> Measure the coil resistance with a multimeter, Part Number 3377161, or equivalent.
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
> If the solenoid resistance is 0 ohms, there is an electrical short in the coil.
>
> If the shutoff valve coil resistance is correct, the assembly of the valve **must** be checked. If the shutoff valve coil resistance does **not** meet specification, the shutoff valve coil **must** be replaced.
>
> Turn the vehicle keyswitch to the ON position.
>
> Touch the wire to the coil terminal.
>
> Listen for the valve to click when the wire is touched to the coil terminal. If the valve does **not** click, repair or replace the fuel shutoff valve.
>
> ### Voltage Check
>
> **CAUTION · Осторожно**
> To avoid damage to the ECM, connect only one wire to the fuel shut off solenoid.
>
> Connect the wire.
>
> The coil voltage and part number are cast into the terminal connection end of the coil.
>
> Turn the vehicle keyswitch to the ON position.
>
> Check the voltage to the coil with a multimeter, Part Number 3377161 or equivalent.
>
> The voltage **must** be the same as the battery voltage.
>
> Turn the vehicle keyswitch to the OFF position.
>
> ### Remove
>
> Clean the fuel shutoff valve and surrounding area.
>
> Disconnect the ring terminal from the fuel shutoff valve solenoid.
>
> Remove the mounting capscrews securing the shutoff valve solenoid.
>
> Remove the shutoff valve solenoid.
>
> ### Install
>
> Install a new o-ring on the fuel shutoff valve.
>
> Install the fuel shutoff valve and the capscrews.
>
> **Момент затяжки · Torque Value**
> 4 n•m [35 in-lb]
>
> Connect the fuel shutoff valve to the actuator harness.
>
> **Момент затяжки · Torque Value**
> 3 n•m [27 in-lb]
