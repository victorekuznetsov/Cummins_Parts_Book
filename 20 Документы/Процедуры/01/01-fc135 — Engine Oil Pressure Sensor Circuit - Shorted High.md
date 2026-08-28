---
aliases:
  - "Цепь датчика давления масла — замыкание на плюс"
type: "Процедура"
doc: "01-fc135"
title_en: "Engine Oil Pressure Sensor Circuit - Shorted High"
title_ru: "Цепь датчика давления масла — замыкание на плюс"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc135.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc135.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Engine Oil Pressure Sensor Circuit - Shorted High
**Цепь датчика давления масла — замыкание на плюс**

> [!abstract] Процедура · `01-fc135`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc135.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc135.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 135

### Цепь датчика давления масла — замыкание на плюс

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 135 PID (P): СПН: ФМИ: Лампа: Предупреждение СТО: | Датчик давления масла двигателя высококороткий - высококороткий. | Отсутствие защиты двигателя от давления масла. |

![[19803594.png]]

Цепь датчика давления масла

### Описание цепи

Датчик давления масла контролирует давление масла и передает информацию в электронный модуль управления (ECM). ECM контролирует напряжение на контактном сигнале давления масла и ожидает, что напряжение будет варьироваться между 0,46 и 4,56 ВДК во время нормальной работы двигателя. Высокое напряжение будет сбивать Код 135 по умолчанию и может быть вызвано шортами в проводах подачи, сигнала или возврата, открытым в обратном проводе или неисправным датчиком.

### Расположение компонента

См. схемы двигателя. 100-002 для расположения компонентов.

### Практические замечания

Вредоносный код возникает только в холодную погоду? Если это так, то дайте маслу разогреться и посмотрите, не активируется ли код ошибки.

См. конкретную схему проводов двигателя для выходного напряжения датчика давления.

Примечание: Некоторые модели двигателей будут использовать разъем типа Metri-Pack на этом датчике давления, а некоторые будут использовать разъем типа DanfossTM. Контактные обозначения разъема Metri-Pack являются альфа-контактными, а контактные обозначения разъема DanfossTM числовыми. Шаги, изображенные в этом коде неисправности, показывают разъем типа Metri-Pack с вызывными альфа-пинами. См. конкретные схемы проводов двигателя, чтобы определить правильные указатели контактов для типа разъема.

Устранение неполадок код t05-135


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 135
>
> ### Engine Oil Pressure Sensor Circuit - Shorted High
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 135 PID(P): SPN: FMI: Lamp: Warning SRT: | Engine oil pressure sensor is shorted high - shorted high. | No engine protection for oil pressure. |
>
> Oil Pressure Sensor Circuit
>
> ### Circuit Description
>
> The oil pressure sensor monitors oil pressure and passes information to the electronic control module (ECM). The ECM monitors the voltage on the oil pressure signal pin and expects to see the voltage vary between 0.46 and 4.56 VDC during normal engine operation. High voltage will trip Fault Code 135 and can be caused by shorts in the supply, signal, or return wires, an open in the return wire, or a failed sensor.
>
> ### Component Location
>
> Refer to the Engine Diagrams. 100-002 for the component location.
>
> ### Shoptalk
>
> Does the fault code occur **only** in cold weather? If so, allow the oil to warm up and see if the fault code goes inactive.
>
> Refer to specific engine wiring diagram for the output voltage of the pressure sensor.
>
> Note: Some engine models will use the Metri-Pack type connector on this pressure sensor, and some will use the Danfoss™ type connector. The Metri-Pack connector pin designators are alpha and the Danfoss™ connector pin designators are numeric. The steps depicted in this fault code show the Metri-Pack type connector with alpha pin callouts. Refer to specific engine wiring diagrams to determine the correct pin designators for the type of connector.
>
> Refer to Troubleshooting Fault Code t05-135
