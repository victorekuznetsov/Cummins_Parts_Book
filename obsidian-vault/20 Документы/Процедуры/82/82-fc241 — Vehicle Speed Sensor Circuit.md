---
aliases:
  - "Цепь датчика скорости машины"
type: "Процедура"
doc: "82-fc241"
title_en: "Vehicle Speed Sensor Circuit"
title_ru: "Цепь датчика скорости машины"
modified: "2010-09-02"
engines:
  - "41343322"
  - "41370103"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc241.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc241.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# Vehicle Speed Sensor Circuit
**Цепь датчика скорости машины**

> [!abstract] Процедура · `82-fc241`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc241.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc241.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 241

### Цепь датчика скорости машины

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 241 PID(P): P084 SPN: 84 ФМИ: 2/2 лампы: Желтая СТО: | ECM потерял сигнал скорости автомобиля. | Скорость двигателя ограничена максимальной скоростью двигателя без значения параметра датчика скорости транспортного средства. Круиз-контроль, защита от переключения передач и управление скоростью движения не будут работать (только автомобильные). |

![[19c00033.png]]

Цепь датчика скорости машины

### Описание цепи

Датчик скорости транспортного средства (VSS) использует две отдельные катушки провода для подсчета зубьев передач, когда они проходят перед датчиком. Одна катушка используется электронным модулем управления (ECM) для определения скорости транспортного средства. Другая катушка иногда используется для отправки сигнала скорости транспортного средства на спидометр.

### Расположение компонента

VSS устанавливается в задней части трансмиссии.

### Практические замечания

- Отключите разъем датчика скорости транспортного средства, который соединяется со спидометром OEM или регистратором движения, и переместите грузовик. Если неисправность неактивна, вероятно, в цепь датчика скорости транспортного средства из OEM-устройства подается электрический шум.

- Проверьте провода датчика скорости транспортного средства в OEM-проводах, чтобы они были скрученными парами.

См. Код устранения неполадок t05-241


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 241
>
> ### Vehicle Speed Sensor Circuit
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 241 PID(P): P084 SPN: 84 FMI: 2/2 Lamp: Yellow SRT: | The ECM lost the vehicle speed signal. | Engine speed limited to Maximum Engine Speed without Vehicle Speed Sensor parameter value. Cruise control, gear-down protection, and road speed governor will **not** work (automotive **only**). |
>
> Vehicle Speed Sensor Circuit
>
> ### Circuit Description
>
> The vehicle speed sensor (VSS) uses two separate coils of wire to count gear teeth as they pass in front of the sensor. One coil is used by the electronic control module (ECM) to sense vehicle speed. The other coil is sometimes used to send a vehicle speed signal to the speedometer.
>
> ### Component Location
>
> The VSS is installed in the rear of the transmission.
>
> ### Shoptalk
>
> - Disconnect the vehicle speed sensor connector that connects to the OEM speedometer, or trip recorder, and move the truck. If the fault goes inactive, there is probably electrical noise being fed into the vehicle speed sensor circuit from the OEM device.
>
> - Verify the vehicle speed sensor wires in the OEM harness are twisted pairs.
>
> Refer to Troubleshooting Fault Code t05-241
