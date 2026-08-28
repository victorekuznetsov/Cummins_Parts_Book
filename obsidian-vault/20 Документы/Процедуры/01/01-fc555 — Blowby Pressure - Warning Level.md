---
aliases:
  - "Давление прорыва газов — уровень предупреждения"
type: "Процедура"
doc: "01-fc555"
title_en: "Blowby Pressure - Warning Level"
title_ru: "Давление прорыва газов — уровень предупреждения"
modified: "2010-07-29"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc555.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc555.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Blowby Pressure - Warning Level
**Давление прорыва газов — уровень предупреждения**

> [!abstract] Процедура · `01-fc555`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc555.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc555.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 555

### Давление прорыва газов — уровень предупреждения

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 555 PID(P): СПН: ФМИ: Лампа: Предупреждение СТО: | Двигатель продувки - уровень предупреждения. Сигнал напряжения указывает на то, что давление надувательства превысило пороговое значение для высокого надува. | Зависимое от калибровки отключение двигателя или отсутствие действий со стороны ECM. |

![[19803587.png]]

Схема датчика давления Blowby Pressure Sensor Circuit

### Описание цепи

Датчик давления в продувке используется электронным модулем управления (ECM) для мониторинга давления в картере двигателя. ECM контролирует напряжение на контакте сигнала и преобразует его в значение давления. Значение давления продувки используется ECM для системы защиты двигателя.

### Расположение компонента

См. схемы двигателя. 100-002 для расположения компонентов.

### Практические замечания

Подтвердите, что дыхательные пути и дыхательные трубки **не** затрудняются.

Устранение неполадок код t05-555


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 555
>
> ### Blowby Pressure - Warning Level
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 555 PID(P): SPN: FMI: Lamp: Warning SRT: | Engine blowby - warning level. Voltage signal indicates blowby pressure has exceeded the warning threshold for high blowby. | Calibration-dependent engine shutdown or no action is taken by ECM. |
>
> Blowby Pressure Sensor Circuit
>
> ### Circuit Description
>
> The blowby pressure sensor is used by the electronic control module (ECM) to monitor the engine crankcase pressure. The ECM monitors the voltage on the signal pin and converts this to a pressure value. The blowby pressure value is used by the ECM for the engine protection system.
>
> ### Component Location
>
> Refer to the Engine Diagrams. 100-002 for the component location.
>
> ### Shoptalk
>
> Confirm that the crankcase breathers and breather tubes are **not** obstructed.
>
> Refer to Troubleshooting Fault Code t05-555
