---
aliases:
  - "Цепь датчика давления подачи топливного насоса — замыкание на плюс"
type: "Процедура"
doc: "01-fc118"
title_en: "Fuel Pump Delivery Pressure Sensor Circuit - Shorted High"
title_ru: "Цепь датчика давления подачи топливного насоса — замыкание на плюс"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc118.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc118.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Fuel Pump Delivery Pressure Sensor Circuit - Shorted High
**Цепь датчика давления подачи топливного насоса — замыкание на плюс**

> [!abstract] Процедура · `01-fc118`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc118.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc118.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 118

### Цепь датчика давления подачи топливного насоса — замыкание на плюс

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 118 PID(P): СПН: ФМИ: Лампа: Предупреждение СТО: | Цепь датчика давления подачи топливного насоса — замыкание на плюс. | Никаких действий со стороны ЕКМ не предпринимается. Возможная потеря производительности. |

![[19803583.png]]

Схема датчика давления топливного насоса

### Описание цепи

Датчик давления топливного насоса обеспечивает сигнал давления топливного насоса к ECM через электропроводку двигателя. ECM использует сигнал давления топливного насоса для контроля давления топливного насоса, идущего к корпусу управляющего клапана.

### Расположение компонента

Датчик давления топливного насоса расположен на топливных насосах чуть выше исполнительного механизма топливного насоса.

### Практические замечания

См. конкретную схему проводов двигателя для выходного напряжения датчика давления.

Примечание: Некоторые модели двигателей будут использовать разъем типа Metri-Pack на этом датчике давления, а некоторые будут использовать разъем типа DanfossTM. Контактные обозначения разъема Metri-Pack являются альфа-контактными, а контактные обозначения разъема DanfossTM числовыми. Шаги, изображенные в этом коде неисправности, показывают разъем типа Metri-Pack с вызывными альфа-пинами. См. конкретные схемы проводов двигателя, чтобы определить правильные указатели контактов для типа разъема.

См. Код устранения неполадок t05-118


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 118
>
> ### Fuel Pump Delivery Pressure Sensor Circuit - Shorted High
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 118 PID(P): SPN: FMI: Lamp: Warning SRT: | Fuel pump delivery pressure sensor circuit - shorted high. | No action is taken by the ECM. Possible loss of performance. |
>
> Fuel Pump Pressure Sensor Circuit
>
> ### Circuit Description
>
> The fuel pump pressure sensor provides the fuel pump pressure signal to the ECM, through the engine harness. The ECM uses the fuel pump pressure signal to monitor the fuel pump pressure going to the control valve body.
>
> ### Component Location
>
> The fuel pump pressure sensor is located on the fuel pumps just above the fuel pump actuator.
>
> ### Shoptalk
>
> Refer to specific engine wiring diagram for the output voltage of the pressure sensor.
>
> Note: Some engine models will use the Metri-Pack type connector on this pressure sensor, and some will use the Danfoss™ type connector. The Metri-Pack connector pin designators are alpha and the Danfoss™ connector pin designators are numeric. The steps depicted in this fault code show the Metri-Pack type connector with alpha pin callouts. Refer to specific engine wiring diagrams to determine the correct pin designators for the type of connector.
>
> Refer to Troubleshooting Fault Code t05-118
