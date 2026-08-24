---
aliases:
  - "Цепь датчика давления подачи топлива — замыкание на массу"
type: "Процедура"
doc: "01-fc547"
title_en: "Fuel Delivery Pressure Sensor Circuit - Shorted Low"
title_ru: "Цепь датчика давления подачи топлива — замыкание на массу"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc547.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc547.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Fuel Delivery Pressure Sensor Circuit - Shorted Low
**Цепь датчика давления подачи топлива — замыкание на массу**

> [!abstract] Процедура · `01-fc547`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc547.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc547.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 547

### Цепь датчика давления подачи топлива — замыкание на массу

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 547 PID(P): СПН: ФМИ: Лампа: Предупреждение СТО: | Цепь датчика давления подачи топлива — замыкание на массу. | Никаких действий со стороны ЕКМ не предпринималось. Возможная потеря производительности. |

![[19803583.png]]

Схема датчика давления топлива

### Описание цепи

Датчик давления топлива обеспечивает сигнал давления подачи топлива к электронному модулю управления (ECM).

### Расположение компонента

См. схемы двигателя. 100-002 для расположения компонентов.

### Практические замечания

См. конкретную схему проводов двигателя для выходного напряжения датчика давления.

Примечание: Некоторые модели двигателей будут использовать разъем типа Metri-Pack на этом датчике давления, а некоторые будут использовать разъем типа DanfossTM. Контактные обозначения разъема Metri-Pack являются альфа-контактными, а контактные обозначения разъема DanfossTM числовыми. Шаги, изображенные в этом коде неисправности, показывают разъем типа Metri-Pack с вызывными альфа-пинами. См. конкретные схемы проводов двигателя, чтобы определить правильные указатели контактов для типа разъема.

См. Код устранения неполадок t05-547


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 547
>
> ### Fuel Delivery Pressure Sensor Circuit - Shorted Low
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 547 PID(P): SPN: FMI: Lamp: Warning SRT: | Fuel supply pressure sensor circuit - shorted low. | No action taken by the ECM. Possible loss of performance. |
>
> Fuel Supply Pressure Sensor Circuit
>
> ### Circuit Description
>
> The fuel pressure sensor provides the fuel supply pressure signal to the electronic control module (ECM).
>
> ### Component Location
>
> Refer to the Engine Diagrams. 100-002 for the component location.
>
> ### Shoptalk
>
> Refer to specific engine wiring diagram for the output voltage of the pressure sensor.
>
> Note: Some engine models will use the Metri-Pack type connector on this pressure sensor, and some will use the Danfoss™ type connector. The Metri-Pack connector pin designators are alpha and the Danfoss™ connector pin designators are numeric. The steps depicted in this fault code show the Metri-Pack type connector with alpha pin callouts. Refer to specific engine wiring diagrams to determine the correct pin designators for the type of connector.
>
> Refer to Troubleshooting Fault Code t05-547
