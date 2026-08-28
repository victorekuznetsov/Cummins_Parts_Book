---
aliases:
  - "Датчик давления опережения впрыска"
type: "Процедура"
doc: "01-019-113"
title_en: "Fuel Timing Pressure Sensor"
title_ru: "Датчик давления опережения впрыска"
modified: "2003-07-08"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 8
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-019-113.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-019-113.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Fuel Timing Pressure Sensor
**Датчик давления опережения впрыска**

> [!abstract] Процедура · `01-019-113`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-07-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-019-113.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-019-113.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Первичная проверка

Подключите инструмент электронного сервиса к шине данных CAN.

![[19800902.png]]

Переключатель Run/Stop переключается в положение Run.

Мониторинг давления с помощью электронного инструментария обслуживания.

Давление времени подачи топлива должно быть 101,4 кПа \[14,7 psi\], если оно находится на уровне моря или приблизительно равно барометрическому давлению.

Запустите двигатель и запускайте его на холостом ходу. Мониторинг давления с помощью электронного инструментария обслуживания. Давление времени подачи топлива **должно быть** 413,7 кПа[60 psi].

Если датчик давления в момент подачи топлива **не** в пределах спецификаций, датчик давления в момент подачи топлива  должен быть заменен.

![[19600070.png]]

### Снятие

Очистите корпус управляющего клапана вокруг датчика давления времени подачи топлива.

Отсоедините проводку двигателя от датчика давления времени подачи топлива.

![[19400306.png]]

Удалите датчик давления синхронизации топлива с помощью глубоководной розетки, номер детали 3823843.

![[19400307.png]]

### Проверка

Подключите инструмент электронного сервиса к шине данных CAN.

![[19800902.png]]

Подключите электропроводку двигателя к датчику давления времени подачи топлива.

Дайте датчику и проводах висеть на воздухе.

![[19e00166.png]]

Мониторинг давления времени подачи топлива с помощью электронного инструментария обслуживания.

Давление времени подачи топлива должно быть в пределах ±58,6 кПа \[8,5 psi\] от значения барометрического датчика давления.

Если датчик давления в момент подачи топлива **не** в пределах спецификаций, датчик давления в момент подачи топлива  должен быть заменен.

Отключите инструмент электронного сервиса.

Отсоедините датчик давления времени подачи топлива от электропроводки двигателя.

![[19800902.png]]

### Установка

Если используется новый датчик давления синхронизации топлива, убедитесь, что установлено кольцо.

Установите датчик в электронный клапан управления. Используйте розетку глубокого колодца, номер детали 3823843, чтобы затянуть датчик.

> [!tip] Момент затяжки
> 14 Н·м [124 фунт-дюйм]

Подключите жгут электропроводки двигателя к датчику давления рельсов времени.

![[19400308.png]]


> [!quote]- Original (English) · английский оригинал
> ### Initial Check
>
> Connect the electronic service tool to the datalink.
>
> Turn the Run/Stop switch to the Run position.
>
> Monitor the timing pressure with the electronic service tool.
>
> The fuel timing pressure **must** be 101.4 kPa \[14.7 psi\] if at sea level or approximately equal to the barometric pressure.
>
> Start the engine and let it idle. Monitor the timing pressure with the electronic service tool. The fuel timing pressure **must** be 413.7 kPa \[60 psi\].
>
> If the fuel timing pressure sensor is **not** within specifications, the fuel timing pressure sensor **must** be replaced.
>
> ### Remove
>
> Clean the control valve body around the fuel timing pressure sensor.
>
> Disconnect the engine harness from the fuel timing pressure sensor.
>
> Remove the fuel timing pressure sensor using a deep-well socket, Part Number 3823843.
>
> ### Test
>
> Connect the electronic service tool to the datalink.
>
> Connect the engine harness to the fuel timing pressure sensor.
>
> Allow the sensor and harness hang in air.
>
> Monitor the fuel timing pressure with the electronic service tool.
>
> The fuel timing pressure **must** be within ±58.6 kPa \[8.5 psi\] of the barometric pressure sensor value.
>
> If the fuel timing pressure sensor is **not** within specifications, the fuel timing pressure sensor **must** be replaced.
>
> Disconnect the electronic service tool.
>
> Disconnect the fuel timing pressure sensor from the engine harness.
>
> ### Install
>
> If a new fuel timing pressure sensor is used, make sure the o-ring is installed.
>
> Install the sensor into the electronic control valve assembly. Use a deep-well socket, Part Number 3823843, to tighten the sensor.
>
> **Момент затяжки · Torque Value**
> 14 n•m [124 in-lb]
>
> Connect the engine harness to the timing rail pressure sensor.
