---
aliases:
  - "Цепь датчика давления подачи топлива — замыкание на плюс"
type: "Процедура"
doc: "01-fc546"
title_en: "Fuel Delivery Pressure Sensor Circuit - Shorted High"
title_ru: "Цепь датчика давления подачи топлива — замыкание на плюс"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc546.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc546.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Fuel Delivery Pressure Sensor Circuit - Shorted High
**Цепь датчика давления подачи топлива — замыкание на плюс**

> [!abstract] Процедура · `01-fc546`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc546.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc546.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 546

### Цепь датчика давления подачи топлива — замыкание на плюс

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 546 PID(P): СПН: ФМИ: Лампа: Предупреждение СТО: | Сигнал датчика давления подачи топлива - закороченный высокий. | Никаких действий со стороны ЕКМ не предпринимается. Возможная потеря производительности. |

![[19803583.png]]

Схема датчика давления топлива

### Описание цепи

Датчик давления топлива обеспечивает сигнал подачи давления топлива в электронный модуль управления (ECM). Эта неисправность указывает на то, что контакт сигнала на ECM был сокращен до по меньшей мере 5 ВДК.

### Расположение компонента

См. схемы двигателя. 100-002 для расположения компонентов.

### Практические замечания

См. конкретную схему проводов двигателя для выходного напряжения датчика давления.

Примечание: Некоторые модели двигателей будут использовать разъем типа Metri-Pack на этом датчике давления, а некоторые будут использовать разъем типа DanfossTM. Контактные обозначения разъема Metri-Pack являются альфа-контактными, а контактные обозначения разъема DanfossTM числовыми. Шаги, изображенные в этом коде неисправности, показывают разъем типа Metri-Pack с вызывными альфа-пинами. См. конкретные схемы проводов двигателя, чтобы определить правильные указатели контактов для типа разъема.

Устранение неполадок код t05-546


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 546
>
> ### Fuel Delivery Pressure Sensor Circuit - Shorted High
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 546 PID(P): SPN: FMI: Lamp: Warning SRT: | Fuel supply pressure sensor signal - shorted high. | No action take by the ECM. Possible loss of performance. |
>
> Fuel Supply Pressure Sensor Circuit
>
> ### Circuit Description
>
> The fuel pressure sensor provides the fuel pressure supply signal to the electronic control module (ECM). This fault indicates that the signal pin on the ECM has been shorted to at least 5 VDC.
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
> Refer to Troubleshooting Fault Code t05-546
