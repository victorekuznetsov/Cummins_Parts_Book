---
aliases:
  - "Цепь датчика скорости машины"
type: "Процедура"
doc: "82-fc242"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc242.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc242.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# Vehicle Speed Sensor Circuit
**Цепь датчика скорости машины**

> [!abstract] Процедура · `82-fc242`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc242.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc242.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 242

### Цепь датчика скорости машины

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 242 PID(P): P084 SPN: 84 ФМИ: 10/10 лампа: Желтая СТО: | Недействительный или неподходящий сигнал скорости автомобиля. Сигнал указывает на прерывистое соединение или VSS-подделку. | Скорость двигателя ограничена максимальной скоростью двигателя без значения параметра датчика скорости транспортного средства. Круиз-контроль, прогрессивная переключение, защита от переключения передач и регулятор скорости движения не будут работать. |

![[19c00033.png]]

Цепь датчика скорости машины

### Описание цепи

Датчик скорости транспортного средства (VSS) использует две отдельные катушки провода для подсчета зубьев передач, когда они проходят перед датчиком. Одна катушка используется ECM для определения скорости транспортного средства. Другой иногда используется OEM для отправки сигнала скорости транспортного средства на спидометр.

### Расположение компонента

Датчик скорости транспортного средства устанавливается в задней части трансмиссии.

### Практические замечания

- Убедитесь, что настройки функции для VSS Anti-tampering (код ошибки 242), тип приложения и автоматическая передача установлены правильно. Если какой-либо из них установлен неправильно, код 242 ошибки может произойти ошибочно.

Примечание: Методы вождения, такие как вождение в течение длительных периодов времени на более низких передачах, могут регистрировать код 242 ошибки.

- Код 242 ошибки может быть зарегистрирован, если водитель пытается победить регулятор скорости дороги, неоднократно ездя на велосипеде переключателя зажигания.

- Проведите собеседование с водителем, чтобы узнать, что произошло, когда был зарегистрирован код ошибки. Объясните действия водителя, которые могут привести к регистрации кода 242 ошибки.

- При деактивации неисправности убедитесь, что транспортное средство остановлено и двигатель выключен.

- Убедитесь, что переключатель зажигания был цикличен и оставался в положении Включения в течение 30 секунд после исправления недействительного сигнала. Эта неисправность будет оставаться активной до тех пор, пока переключатель зажигания не будет циклически запущен, и ECM не увидит нулевую скорость транспортного средства и нулевую скорость двигателя в течение 30 секунд.

См. Код устранения неполадок t05-242


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 242
>
> ### Vehicle Speed Sensor Circuit
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 242 PID(P): P084 SPN: 84 FMI: 10/10 Lamp: Yellow SRT: | Invalid or inappropriate vehicle speed signal detected. Signal indicates an intermittent connection or VSS tampering. | Engine speed limited to maximum engine speed without vehicle speed sensor parameter value. Cruise control, progressive shifting, gear-down protection, and road speed governor will **not** work. |
>
> Vehicle Speed Sensor Circuit
>
> ### Circuit Description
>
> The vehicle speed sensor (VSS) uses two separate coils of wire to count gear teeth as they pass in front of the sensor. One coil is used by the ECM to sense vehicle speed. The other is sometimes used by the OEM to send a vehicle speed signal to the speedometer.
>
> ### Component Location
>
> The vehicle speed sensor is installed in the rear of the transmission.
>
> ### Shoptalk
>
> - Verify that the feature settings for VSS Anti-tampering (Fault Code 242), Application Type, and Automatic Transmission are set correctly. If any of these are set incorrectly, Fault Code 242 could occur erroneously.
>
> Note: Driving techniques, such as driving for extended periods of time in lower gears, could log Fault Code 242.
>
> - Fault Code 242 can be logged if the driver attempts to defeat the road speed governor by repeatedly cycling the keyswitch.
>
> - Interview the driver to discover what occurred when the fault code was logged. Explain the driver actions that can cause Fault Code 242 to be logged.
>
> - When deactivating the fault, verify that the vehicle is stopped and the engine is shut down.
>
> - Verify that the keyswitch has been cycled and has remained in the ON position for 30 seconds after the invalid signal has been corrected. This fault will remain active until the keyswitch is cycled and the ECM sees zero vehicle speed and zero engine speed for 30 seconds.
>
> Refer to Troubleshooting Fault Code t05-242
