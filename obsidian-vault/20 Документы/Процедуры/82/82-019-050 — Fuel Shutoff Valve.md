---
aliases:
  - "Клапан отсечки топлива"
type: "Процедура"
doc: "82-019-050"
title_en: "Fuel Shutoff Valve"
title_ru: "Клапан отсечки топлива"
modified: "2004-12-15"
engines:
  - "41343322"
  - "41370103"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 6
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-050.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-019-050.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# Fuel Shutoff Valve
**Клапан отсечки топлива**

> [!abstract] Процедура · `82-019-050`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section 19 - Electronic Engine Controls
> **Даты:** изменён 2004-12-15
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-050.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-019-050.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Проверка сопротивления

Убедитесь, что катушка запорного клапана имеет правильное напряжение (12 или 24 ВДК).

Напряжение катушки и номер детали отбрасываются в конец терминального соединения катушки.

![[19c01393.png]]

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

Если сопротивление катушки правильное, то сборку клапана  необходимо проверить. Если сопротивление катушки не соответствует спецификации, катушка должна быть заменена. См. процедуру 005-043 в руководстве ISM/QSM11 по устранению неполадок и ремонту, Бюллетень [[3666322 — ISM, ISMe, and QSM11 Service Manual\|3666322]], для проверки клапана.

Установите соленоидный провод после завершения ремонта.

![[19c00709.png]]

### Проверка напряжения

Убедитесь, что катушка запорного клапана имеет правильное напряжение (12 или 24 ВДК).

Напряжение катушки и номер детали отбрасываются в конец терминального соединения катушки.

![[19c01393.png]]

Включите замок зажигания автомобиля.

Используйте мультиметр для проверки напряжения на катушке.

Напряжение должно быть таким же, как напряжение батареи.

Выключите зажигание автомобиля.

![[19c00708.png]]

### Снятие

Отсоедините кольцевой терминал от запорного клапана соленоида.

Удалите крепежные болты, обеспечивающие соленоид.

Удалите соленоид.

![[19200408.png]]

### Установка

Установите новое кольцо на соленоид.

Установите соленоид и болты.

> [!tip] Момент затяжки
> 3.4 Н·м [30 фунт-дюйм]

Подключите кольцевой терминал к запорному клапану соленоида.

![[19200408.png]]


> [!quote]- Original (English) · английский оригинал
> ### Resistance Check
>
> Make sure the shutoff valve coil is the correct voltage (12 or 24 VDC).
>
> The coil voltage and part number are cast into the terminal connection end of the coil.
>
> Remove the solenoid wire.
>
> Use the multimeter meter to check the coil resistance.
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
> If the coil resistance is correct, the assembly of the valve **must** be checked. If the coil resistance does **not** meet specification, the coil **must** be replaced. Refer to Procedure [[35-005-043 — Fuel Shutoff Valve|005-043]] in the ISM/QSM11 Troubleshooting and Repair Manual, Bulletin [[3666322 — ISM, ISMe, and QSM11 Service Manual\|3666322]], for inspection of the valve.
>
> Install the solenoid wire after completing the repair.
>
> ### Voltage Check
>
> Make sure the shutoff valve coil is the correct voltage (12 or 24 VDC).
>
> The coil voltage and part number are cast into the terminal connection end of the coil.
>
> Turn the vehicle keyswitch on.
>
> Use a multimeter to check the voltage to the coil.
>
> The voltage **must** be the same as the battery voltage.
>
> Turn the vehicle keyswitch off.
>
> ### Remove
>
> Disconnect the ring terminal from the fuel shutoff valve solenoid.
>
> Remove the mounting capscrews securing the solenoid.
>
> Remove the solenoid.
>
> ### Install
>
> Install a new o-ring on the solenoid.
>
> Install the solenoid and capscrews.
>
> **Момент затяжки · Torque Value**
> 3.4 n•m [30 in-lb]
>
> Connect the ring terminal to the fuel shutoff valve solenoid.
