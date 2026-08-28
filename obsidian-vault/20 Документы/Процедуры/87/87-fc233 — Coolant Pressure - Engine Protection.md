---
aliases:
  - "Давление охлаждающей жидкости — защита двигателя"
type: "Процедура"
doc: "87-fc233"
title_en: "Coolant Pressure - Engine Protection"
title_ru: "Давление охлаждающей жидкости — защита двигателя"
modified: "2010-07-29"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666214"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc233.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-fc233.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
  - "перевод/машинный"
---

# Coolant Pressure - Engine Protection
**Давление охлаждающей жидкости — защита двигателя**

> [!abstract] Процедура · `87-fc233`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc233.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-fc233.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 233

### Давление охлаждающей жидкости — защита двигателя

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 233 PID(P): P109 SPN: 109 FMI: 1 лампа: Защита двигателя SRT: | Было обнаружено низкое давление охлаждающей жидкости. Сигнал напряжения при контакте 24 давления охлаждающей жидкости с проводкой двигателя указывает на давление охлаждающей жидкости ниже 28 кПа \[4 psi\] при 800 об/мин; 41 кПа \[6 psi\] при 1300 об/мин; 76 кПа \[11 psi\] при 1800 об/мин; 96 кПа \[14 psi\] при 2000 об/мин; и 103 кПа \[15 psi\] при 2100 об/мин. | Калибровочная зависимость прогрессивной мощности и скорости ухудшается, а выключение двигателя увеличивается с увеличением времени после оповещения. |

![[19a00129.png]]

Цепь датчика давления охлаждающей жидкости

### Описание цепи

Датчик давления охлаждающей жидкости используется электронным модулем управления (ECM) для мониторинга давления охлаждающей жидкости. ECM контролирует напряжение на контакте сигнала и преобразует его в значение давления. Значение давления охлаждающей жидкости используется ECM для системы защиты двигателя.

### Расположение компонента

Датчик давления охлаждающей жидкости расположен с левой стороны двигателя в корпусе термостата.

### Практические замечания

- Подтвердите, что напряжение питания датчика давления охлаждающей жидкости составляет от 4,75 до 5,25 ВДК на датчике. См. Код 232.

- Проверьте с оператором, на какой скорости двигателя происходит неисправность. Если двигатель работает со слишком низкой скоростью под нагрузкой, давление охлаждающей жидкости может опускаться ниже пределов защиты двигателя.

Примечание: Количество неисправных ламп может быть сокращено до двух для некоторых OEM-производителей. Защита двигателя и стоп-сигналы соединены вместе как красная лампа. Предупреждающая лампа остается желтой лампой.

См. Код устранения неполадок t05-233


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 233
>
> ### Coolant Pressure - Engine Protection
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 233 PID(P): P109 SPN: 109 FMI: 1 Lamp: Engine Protection SRT: | Low coolant pressure has been detected. Voltage signal at coolant pressure signal pin 24 of the engine harness indicates coolant pressure lower than 28 kPa \[4 psi\] at 800 rpm; 41 kPa \[6 psi\] at 1300 rpm; 76 kPa \[11 psi\] at 1800 rpm; 96 kPa \[14 psi\] at 2000 rpm; and 103 kPa \[15 psi\] at 2100 rpm. | Calibration-dependent progressive power and speed derate and engine shutdown with increasing time after alert. |
>
> Coolant Pressure Sensor Circuit
>
> ### Circuit Description
>
> The coolant pressure sensor is used by the electronic control module (ECM) to monitor the coolant pressure. The ECM monitors the voltage on the signal pin and converts this to a pressure value. The coolant pressure value is used by the ECM for the engine protection system.
>
> ### Component Location
>
> The coolant pressure sensor is located on the left side of the engine in the thermostat housing.
>
> ### Shoptalk
>
> - Confirm that the coolant pressure sensor supply voltage is between 4.75 and 5.25 VDC at the sensor. Refer to Fault Code 232.
>
> - Verify with the operator at what engine speed the fault occurs. If the engine is being operated at too low a speed under load, the coolant pressure can drop below the engine protection limits.
>
> Note: The number of fault lamps could be reduced to two for certain OEMs. The engine protection and stop lamps are wired together as a red lamp. The warning lamp remains a yellow lamp.
>
> Refer to Troubleshooting Fault Code t05-233
