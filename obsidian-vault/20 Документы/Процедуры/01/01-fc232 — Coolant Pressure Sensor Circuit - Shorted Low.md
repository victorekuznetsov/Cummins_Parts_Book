---
aliases:
  - "Цепь датчика давления ОЖ — замыкание на массу"
type: "Процедура"
doc: "01-fc232"
title_en: "Coolant Pressure Sensor Circuit - Shorted Low"
title_ru: "Цепь датчика давления ОЖ — замыкание на массу"
modified: "2012-05-08"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc232.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc232.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Coolant Pressure Sensor Circuit - Shorted Low
**Цепь датчика давления ОЖ — замыкание на массу**

> [!abstract] Процедура · `01-fc232`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-05-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc232.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc232.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 232

### Цепь датчика давления ОЖ — замыкание на массу

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 232 PID(P): СПН: ФМИ: Лампа: Предупреждение СТО: | Схема датчика давления охлаждающей жидкости двигателя - низкое закороченное. | Отсутствие защиты двигателя от давления охлаждающей жидкости. |

![[19803583.png]]

Цепь датчика давления охлаждающей жидкости

### Описание цепи

Датчик давления охлаждающей жидкости контролирует давление охлаждающей жидкости и передает информацию в модуль управления двигателем (ECM). Низкое напряжение будет сбивать Код 232 по умолчанию и может быть вызвано шортами в проводах подачи, сигнала или возврата, открытым в проводах возврата или неисправным датчиком.

### Расположение компонента

Используйте следующую процедуру для определения местоположения компонентов. См. процедуру 100-002 в разделе E.

### Практические замечания

Подтвердите, что крышка радиатора установлена правильно.

Проверьте крышку радиатора для правильной работы.

См. конкретную схему проводов двигателя для выходного напряжения датчика давления.

Примечание: Некоторые модели двигателей будут использовать разъем типа Metri-PackTM на этом датчике давления, а некоторые будут использовать разъем типа DanfossTM. Контактные обозначения разъемов Metri-PackTM являются альфа-контактными, а контактные обозначения разъемов DanfossTM - числовыми. Шаги, изображенные в этом коде неисправности, показывают разъем типа Metri-PackTM с вызывными альфа-пинами. Справочные конкретные схемы проводов двигателя для определения правильных указателей контактов для типа разъема.

См. Код устранения неполадок t05-232.


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 232
>
> ### Coolant Pressure Sensor Circuit - Shorted Low
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 232 PID(P): SPN: FMI: Lamp: Warning SRT: | Engine coolant pressure sensor circuit - shorted low. | No engine protection for coolant pressure. |
>
> Coolant Pressure Sensor Circuit
>
> ### Circuit Description
>
> The coolant pressure sensor monitors coolant pressure and passes information to the engine control module (ECM). Low voltage will trip Fault Code 232 and can be caused by shorts in the supply, signal, or return wires, an open in the return wires, or a failed sensor.
>
> ### Component Location
>
> Use the following procedure for component location. Refer to Procedure 100-002 in Section E.
>
> ### Shoptalk
>
> Confirm that the radiator cap is installed correctly.
>
> Check the radiator cap for proper operation.
>
> Refer to specific engine wiring diagram for the output voltage of the pressure sensor.
>
> Note: Some engine models will use the Metri-Pack™ type connector on this pressure sensor, and some will use the Danfoss™ type connector. The Metri-Pack™ connector pin designators are alpha and the Danfoss™ connector pin designators are numeric. The steps depicted in this fault code show the Metri-Pack™ type connector with alpha pin callouts. Reference specific engine wiring diagrams to determine the correct pin designators for the type of connector.
>
> Refer to Troubleshooting Fault Code t05-232.
