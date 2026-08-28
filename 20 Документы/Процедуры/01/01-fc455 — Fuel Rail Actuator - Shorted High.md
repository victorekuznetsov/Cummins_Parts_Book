---
aliases:
  - "Привод топливной рампы — замыкание на плюс"
type: "Процедура"
doc: "01-fc455"
title_en: "Fuel Rail Actuator - Shorted High"
title_ru: "Привод топливной рампы — замыкание на плюс"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc455.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc455.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Fuel Rail Actuator - Shorted High
**Привод топливной рампы — замыкание на плюс**

> [!abstract] Процедура · `01-fc455`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc455.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc455.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 455

### Привод топливной рампы — замыкание на плюс

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 455 PID(P): СПН: ФМИ: Лампа: Отключение SRT: | Замыкание клапана управления топливом — короткое высокое. Ранее это называлось цепью привода топливного рельса. Схема привода топливного рельса открыта, контакт сигнала привода топливного рельса закорочен до напряжения батареи или земли, или обратный контакт привода топливного рельса закорочен до напряжения батареи или земли. | Двигатель будет работать на одной скорости или отключится. Код 514 ошибки также может быть зарегистрирован. |

![[19803582.png]]

Схема привода топливных рельсов

### Описание цепи

Привод топливной рельсы представляет собой устройство, используемое электронным модулем управления (ECM) для управления подачей топлива в двигатель. ECM может отключить двигатель, отключив питание топливного рельсового привода.

### Расположение компонента

См. схемы двигателя. 100-002 для расположения компонентов.

### Практические замечания

Подтвердите, что клапанный разъем прочно на месте. Когда к приводу закорочена мощность, привод открывается и поток топлива не контролируется. Это приведет к несоответствию кода 234, скорости двигателя или кода 514, что приведет к несоответствию потока.

Устранение неполадок код t05-455


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 455
>
> ### Fuel Rail Actuator - Shorted High
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 455 PID(P): SPN: FMI: Lamp: Shutdown SRT: | Fuel control valve circuit - shorted high. This was formerly called the fuel rail actuator circuit. Fuel rail actuator circuit is open, the fuel rail actuator signal pin is shorted to battery voltage or ground, or the fuel rail actuator return pin is shorted to battery voltage or ground. | Engine will run at one speed or will shutdown. Fault Code 514 may also be logged. |
>
> Fuel Rail Actuator Circuit
>
> ### Circuit Description
>
> The fuel rail actuator is a device used by the electronic control module (ECM) to control the engine fuel supply. The ECM can shut down the engine by cutting off the power to the fuel rail actuator.
>
> ### Component Location
>
> Refer to the Engine Diagrams. 100-002 for the component location.
>
> ### Shoptalk
>
> Confirm that the valve connector is firmly in place. When there is shorted power to the actuator, the actuator opens and fuel flow is uncontrolled. This will cause Fault Code 234, engine overspeed, or Fault Code 514, fueling flow mismatch.
>
> Refer to Troubleshooting Fault Code t05-455
