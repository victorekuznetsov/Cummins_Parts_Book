---
aliases:
  - "Цепь датчика давления коллектора — замыкание на плюс"
type: "Процедура"
doc: "01-fc122"
title_en: "Intake Manifold Pressure Sensor Circuit - Shorted High"
title_ru: "Цепь датчика давления коллектора — замыкание на плюс"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc122.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc122.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Intake Manifold Pressure Sensor Circuit - Shorted High
**Цепь датчика давления коллектора — замыкание на плюс**

> [!abstract] Процедура · `01-fc122`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc122.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc122.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 122

### Цепь датчика давления коллектора — замыкание на плюс

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 122 P(P): СПН: ФМИ: Лампа: Предупреждение СТО: | Датчик давления коллектора 1 цепи - закороченный высоко. | Никаких действий со стороны ЕКМ не предпринимается. Возможная потеря производительности. |

![[19803594.png]]

Схема датчика давления Manifold 1 Circuit

### Описание цепи

Датчик давления впускного коллектора контролирует давление повышения и передает информацию в электронный модуль управления (ECM). Высокое напряжение будет сбивать Код 122 по умолчанию и может быть вызвано шортами в проводах подачи, сигнала или возврата, открытым в обратном проводе или неисправным датчиком.

### Расположение компонента

См. схемы двигателя. 100-002 для расположения компонентов.

### Практические замечания

Определите, если двигатель перегружается.

Подтвердите, что используется правильный номер детали датчика давления в коллекторе приема.

Подтвердите, что используется правильный турбокомпрессор.

Подозревают, что холодный воздух может быть причиной высокого давления впускного коллектора, испытывают двигатель при подаче теплого впускного воздуха. Осмотрите цепь датчика давления впускного коллектора на наличие признаков подделки. Удалите любые дополнительные провода из схемы. См. конкретную схему проводов двигателя для выходного напряжения датчика давления.

Примечание: Некоторые модели двигателей будут использовать разъем типа Metri-Pack на этом датчике давления, а некоторые будут использовать разъем типа DanfossTM. Контактные обозначения разъема Metri-Pack являются альфа-контактными, а контактные обозначения разъема DanfossTM числовыми. Шаги, изображенные в этом коде неисправности, показывают разъем типа Metri-Pack с вызывными альфа-пинами. См. конкретные схемы проводов двигателя, чтобы определить правильные указатели контактов для типа разъема.

См. Код устранения неполадок t05-122


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 122
>
> ### Intake Manifold Pressure Sensor Circuit - Shorted High
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 122 PID(P): SPN: FMI: Lamp: Warning SRT: | Intake manifold pressure sensor 1 circuit - shorted high. | No action is taken by the ECM. Possible loss of performance. |
>
> Intake Manifold Pressure Sensor 1 Circuit
>
> ### Circuit Description
>
> The intake manifold pressure sensor monitors boost pressure and passes information to the electronic control module (ECM). High voltage will trip Fault Code 122 and can be caused by shorts in the supply, signal, or return wires, an open in the return wire, or a failed sensor.
>
> ### Component Location
>
> Refer to the Engine Diagrams. 100-002 for the component location.
>
> ### Shoptalk
>
> Determine if the engine is being over fueled.
>
> Confirm that the correct Intake Manifold Pressure Sensor part number is being used.
>
> Confirm that the correct turbocharger is being used.
>
> It is suspected that cold intake air can be the cause of the high intake manifold pressure, test the engine while feeding warm intake air. Inspect the intake manifold pressure sensor circuit for signs of tampering. Remove any extra wires from the circuit. Refer to specific engine wiring diagram for the output voltage of the pressure sensor.
>
> Note: Some engine models will use the Metri-Pack type connector on this pressure sensor, and some will use the Danfoss™ type connector. The Metri-Pack connector pin designators are alpha and the Danfoss™ connector pin designators are numeric. The steps depicted in this fault code show the Metri-Pack type connector with alpha pin callouts. Refer to specific engine wiring diagrams to determine the correct pin designators for the type of connector.
>
> Refer to Troubleshooting Fault Code t05-122
