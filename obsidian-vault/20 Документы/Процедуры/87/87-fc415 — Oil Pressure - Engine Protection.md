---
aliases:
  - "Давление масла — защита двигателя"
type: "Процедура"
doc: "87-fc415"
title_en: "Oil Pressure - Engine Protection"
title_ru: "Давление масла — защита двигателя"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc415.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-fc415.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
  - "перевод/машинный"
---

# Oil Pressure - Engine Protection
**Давление масла — защита двигателя**

> [!abstract] Процедура · `87-fc415`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc415.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-fc415.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 415

### Давление масла — защита двигателя

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 415 PID(P): P100 SPN: 100 FMI: 1 лампа: Защита двигателя SRT: | Было обнаружено низкое давление масла. Сигнал напряжения при контакте 33 с сигналом давления масла в ремне электропроводки двигателя указывает, что давление масла ниже калиброванных пределов (менее 34 кПа \[5 psi\] при скоростях двигателя менее 600 об/мин; 207 кПа \[30 psi\] при скоростях двигателя более 1600 об/мин). | Калибровочная зависимость прогрессивной мощности и скорости ухудшается, а выключение двигателя увеличивается с увеличением времени после оповещения. |

![[19900357.png]]

Цепь датчика давления масла

### Описание цепи

Датчик давления масла используется электронным модулем управления (ECM) для мониторинга давления моторного масла. ECM контролирует напряжение на контакте сигнала и преобразует его в значение давления. Значение давления масла используется ECM для системы защиты двигателя.

### Расположение компонента

Датчик давления масла расположен на левой стороне блока двигателя, позади топливного насоса.

### Практические замечания

- Подтвердите, что напряжение питания датчика давления масла составляет от 4,75 до 5,25 ВДК на датчике. См. Код 141.

- Проверьте с водителем, на какой скорости двигателя происходит неисправность. Если двигатель работает со слишком низкой скоростью под нагрузкой (вспашка), давление масла может опускаться ниже пределов защиты двигателя из-за температуры масла.

- Давление масла является функцией скорости двигателя, уровня масла и функции регулятора. Работа двигателя на низкой скорости при нагрузке не приведет к низкому давлению масла, если масло не нагревается на низком уровне, регулятор неисправен или где-то в системе происходит потеря.

Примечание: Количество неисправных ламп может быть сокращено до двух для некоторых OEM-производителей. Защита двигателя и стоп-сигналы соединены вместе как красная лампа. Предупреждающая лампа остается желтой лампой.

Устранение неполадок код t05-415


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 415
>
> ### Oil Pressure - Engine Protection
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 415 PID(P): P100 SPN: 100 FMI: 1 Lamp: Engine Protection SRT: | Low oil pressure has been detected. Voltage signal at oil pressure signal pin 33 of the engine harness indicates the oil pressure is lower than calibrated limits (less than 34 kPa \[5 psi\] at engine speeds less than 600 rpm; 207 kPa \[30 psi\] at engine speeds greater than 1600 rpm). | Calibration-dependent progressive power and speed derate and engine shutdown with increasing time after the alert. |
>
> Oil Pressure Sensor Circuit
>
> ### Circuit Description
>
> The oil pressure sensor is used by the electronic control module (ECM) to monitor the lubricating oil pressure. The ECM monitors the voltage on the signal pin and converts this to a pressure value. The oil pressure value is used by the ECM for the engine protection system.
>
> ### Component Location
>
> The oil pressure sensor is located on the left-hand side of the engine block, behind the fuel pump.
>
> ### Shoptalk
>
> - Confirm that the oil pressure sensor supply voltage is between 4.75 and 5.25 VDC at the sensor. Refer to Fault Code 141.
>
> - Verify with the driver at what engine speed the fault occurs. If the engine is being operated at too low a speed under load (lugging), the oil pressure can drop below the engine protection limits because of the oil temperature.
>
> - Oil pressure is a function of the engine speed, oil level, and regulator function. Operating the engine at a low speed under load will **not** cause the oil pressure to be low unless the oil is hot at a low level, regulator has malfunctioned, or a loss is occurring somewhere in the system.
>
> Note: The number of fault lamps could be reduced to two for certain OEMs. The engine protection and stop lamps are wired together as a red lamp. The warning lamp remains a yellow lamp.
>
> Refer to Troubleshooting Fault Code t05-415
