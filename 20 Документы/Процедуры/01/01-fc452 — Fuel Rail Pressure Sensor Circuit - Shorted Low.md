---
aliases:
  - "Цепь датчика давления в топливной рампе — замыкание на массу"
type: "Процедура"
doc: "01-fc452"
title_en: "Fuel Rail Pressure Sensor Circuit - Shorted Low"
title_ru: "Цепь датчика давления в топливной рампе — замыкание на массу"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc452.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc452.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Fuel Rail Pressure Sensor Circuit - Shorted Low
**Цепь датчика давления в топливной рампе — замыкание на массу**

> [!abstract] Процедура · `01-fc452`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-05-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc452.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc452.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 452

### Цепь датчика давления в топливной рампе — замыкание на массу

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 452 PID (P): СПН: ФМИ: Лампа: Предупреждение СТО: | форсунка с измерительным рельсом 1 цепи датчика давления - низкокороткий. Ранее он назывался датчиком давления в топливной рельсе. | Выключение двигателя, зависящее от калибровки, происходит, или ECM не предпринимает никаких действий. |

![[19803583.png]]

Форсунка Metering Rail 1 Pressure Sensor Circuit

### Описание цепи

Датчик давления топливной рельсы обеспечивает сигнал давления топливной рельсы к модулю управления двигателем (ECM) через ремень электропроводки двигателя. ECM использует сигнал давления топливного рельса для контроля давления топливного рельса, идущего в камеру учета топливного форсунка от корпуса управляющего клапана.

### Расположение компонента

Используйте следующую процедуру для определения местоположения компонента. См. процедуру 100-002 в разделе E.

### Практические замечания

См. конкретную схему проводов двигателя для выходного напряжения датчика давления.

Примечание: Некоторые модели двигателей будут использовать разъем типа Metri-PackTM на этом датчике давления, а некоторые будут использовать разъем типа DanfossTM. Контактные обозначения разъемов Metri-PackTM являются альфа-контактными, а контактные обозначения разъемов DanfossTM - числовыми. Шаги, изображенные в этом коде неисправности, показывают разъем типа Metri-PackTM с вызывными альфа-пинами. См. конкретные схемы проводов двигателя, чтобы определить правильные указатели контактов для типа разъема.

См. Код устранения неполадок t05-452.


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 452
>
> ### Fuel Rail Pressure Sensor Circuit - Shorted Low
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 452 PID(P): SPN: FMI: Lamp: Warning SRT: | Injector metering rail 1 pressure sensor circuit - shorted low. This was formerly called the fuel rail pressure sensor. | Calibration-dependent engine shutdown occurs, or no action is taken by ECM. |
>
> Injector Metering Rail 1 Pressure Sensor Circuit
>
> ### Circuit Description
>
> The fuel rail pressure sensor provides the fuel rail pressure signal to the engine control module (ECM), through the engine harness. The ECM uses the fuel rail pressure signal to monitor the fuel rail pressure going to the injector's metering chamber from the control valve body.
>
> ### Component Location
>
> Use the following procedure for the component location. Refer to Procedure 100-002 in Section E.
>
> ### Shoptalk
>
> Refer to specific engine wiring diagram for the output voltage of the pressure sensor.
>
> Note: Some engine models will use the Metri-Pack™ type connector on this pressure sensor, and some will use the Danfoss™ type connector. The Metri-Pack™ connector pin designators are alpha and the Danfoss™ connector pin designators are numeric. The steps depicted in this fault code show the Metri-Pack™ type connector with alpha pin callouts. Refer to specific engine wiring diagrams to determine the correct pin designators for the type of connector.
>
> Refer to Troubleshooting Fault Code t05-452.
