---
aliases:
  - "Датчик давления опережения впрыска"
type: "Процедура"
doc: "105-019-191"
title_en: "Timing Pressure Sensor"
title_ru: "Датчик давления опережения впрыска"
modified: "2004-04-06"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/105/105-019-191.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/105-019-191.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/105"
  - "перевод/машинный"
---

# Timing Pressure Sensor
**Датчик давления опережения впрыска**

> [!abstract] Процедура · `105-019-191`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2004-04-06
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/105/105-019-191.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/105-019-191.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Первичная проверка

Подключите электронный инструмент к шине данных CAN транспортного средства.

![[19400357.png]]

Переведите замок зажигания в положение ON.

Мониторинг давления с помощью электронного инструментария обслуживания.

Давление должно быть нулевым psi.

![[19800978.png]]

Запустите двигатель и запускайте его на холостом ходу.

Мониторинг давления с помощью электронного инструментария обслуживания.

Давление в синхронизации должно составлять 60 psi.

![[19800979.png]]

### Снятие

Удалить ECM. См. процедуру[[01-019-031 — Engine Control Module|019-031]]Руководство по устранению неполадок и ремонту системы управления электрогенерацией, двигатели серии QSK60, QSK45, QSX15, QSK23, QSK15, бюллетень [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst\|4021419]] или процедура[[19-019-031 — Engine Control Module|019-031]]Руководство по устранению неполадок и ремонту в электронной системе управления, двигатели серии QSK60, QSK23, QSK19 и QSK78, бюллетень [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R\|3666113]].

![[19400295.png]]

Очистите корпус управляющего клапана вокруг датчика давления.

Отсоедините разъем датчика от жгута проводов двигателя.

![[19400306.png]]

Удалите датчик давления с помощью 1 1/4-дюймовой фланговой розетки, части 3823843 и скобы.

![[19400307.png]]

### Установка

Осмотрите новый датчик на наличие кольца.

Установите новый датчик давления и затяните.

> [!tip] Момент затяжки
> 14 Н·м [124 фунт-дюйм]

Подключите сенсорное соединение.

![[19400308.png]]

Установите ECM. См. процедуру[[01-019-031 — Engine Control Module|019-031]]Руководство по устранению неполадок и ремонту системы управления электрогенерацией, двигатели серии QSK60, QSK45, QSX15, QSK23, QSK15, бюллетень [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst\|4021419]] или процедура[[19-019-031 — Engine Control Module|019-031]]Руководство по устранению неполадок и ремонту в электронной системе управления, двигатели серии QSK60, QSK23, QSK19 и QSK78, бюллетень [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R\|3666113]].

![[19400295.png]]


> [!quote]- Original (English) · английский оригинал
> ### Initial Check
>
> Connect an electronic service tool to the vehicle datalink.
>
> Turn the keyswitch to the ON position.
>
> Monitor the timing pressure with the electronic service tool.
>
> Timing pressure should be zero psi.
>
> Start the engine and let it idle.
>
> Monitor the timing pressure with the electronic service tool.
>
> The timing pressure should be 60 psi.
>
> ### Remove
>
> Remove the ECM. Refer to Procedure [[01-019-031 — Engine Control Module|019-031]] in the Power Generation Control System Troubleshooting and Repair Manual, QSX15, QSK23, QSK45, QSK60 and QSK78 Series Engines, Bulletin [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst\|4021419]] or Procedure [[19-019-031 — Engine Control Module|019-031]] in the Electronic Control System Troubleshooting and Repair Manual, QSK19, QSK23, QSK60 and QSK78 Series Engines, Bulletin [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R\|3666113]].
>
> Clean the control valve body around the pressure sensor.
>
> Disconnect the sensor connector from the engine harness.
>
> Remove the pressure sensor with a 1 1/4-inch deep flank drive socket, Part Number 3823843, and a ratchet.
>
> ### Install
>
> Inspect the new sensor for an o-ring.
>
> Install the new pressure sensor and tighten.
>
> **Момент затяжки · Torque Value**
> 14 n•m [124 in-lb]
>
> Connect the sensor connection.
>
> Install the ECM. Refer to Procedure [[01-019-031 — Engine Control Module|019-031]] in the Power Generation Control System Troubleshooting and Repair Manual, QSX15, QSK23, QSK45, QSK60 and QSK78 Series Engines, Bulletin [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst\|4021419]] or Procedure [[19-019-031 — Engine Control Module|019-031]] in the Electronic Control System Troubleshooting and Repair Manual, QSK19, QSK23, QSK60 and QSK78 Series Engines, Bulletin [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R\|3666113]].
