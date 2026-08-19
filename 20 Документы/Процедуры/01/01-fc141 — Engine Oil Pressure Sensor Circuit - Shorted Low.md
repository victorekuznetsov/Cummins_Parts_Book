---
aliases:
  - "Цепь датчика давления масла — замыкание на массу"
type: "Процедура"
doc: "01-fc141"
title_en: "Engine Oil Pressure Sensor Circuit - Shorted Low"
title_ru: "Цепь датчика давления масла — замыкание на массу"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc141.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc141.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Engine Oil Pressure Sensor Circuit - Shorted Low
**Цепь датчика давления масла — замыкание на массу**

> [!abstract] Процедура · `01-fc141`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc141.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc141.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 141

### Цепь датчика давления масла — замыкание на массу

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 141 PID(P): СПН: ФМИ: Лампа: Предупреждение СТО: | Цепь датчика давления масла — замыкание на массу. | Отсутствие защиты двигателя от давления масла. |

![[19803594.png]]

Цепь датчика давления масла

### Описание цепи

Датчик давления масла контролирует давление масла и передает информацию в электронный модуль управления (ECM). ECM контролирует напряжение на контактном сигнале давления масла и ожидает, что напряжение будет варьироваться между 0,46 и 4,56 ВДК во время нормальной работы двигателя. Низкое напряжение будет сбивать Код 141 по умолчанию и может быть вызвано шортами в подаче, сигнале или возвратных проводах, открытым в подаче или сигнальных проводах, низким напряжением питания от ECM или неисправным датчиком.

### Расположение компонента

См. схемы двигателя. 100-002 для расположения компонентов.

### Практические замечания

Если код 143 или 415 неисправности присутствует, проблема связана с базовым двигателем.

См. конкретную схему проводов двигателя для выходного напряжения датчика давления.

Примечание: Некоторые модели двигателей будут использовать разъем типа Metri-Pack на этом датчике давления, а некоторые будут использовать разъем типа DanfossTM. Контактные обозначения разъема Metri-Pack являются альфа-контактными, а контактные обозначения разъема DanfossTM числовыми. Шаги, изображенные в этом коде неисправности, показывают разъем типа Metri-Pack с вызывными альфа-пинами. См. конкретные схемы проводов двигателя, чтобы определить правильные указатели контактов для типа разъема.

Устранение неполадок код t05-141


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 141
>
> ### Engine Oil Pressure Sensor Circuit - Shorted Low
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 141 PID(P): SPN: FMI: Lamp: Warning SRT: | Engine oil pressure sensor circuit - shorted low. | No engine protection for oil pressure. |
>
> Oil Pressure Sensor Circuit
>
> ### Circuit Description
>
> The oil pressure sensor monitors oil pressure and passes information to the electronic control module (ECM). The ECM monitors the voltage on the oil pressure signal pin and expects to see the voltage vary between 0.46 and 4.56 VDC during normal engine operation. Low voltage will trip Fault Code 141 and can be caused by shorts in the supply, signal, or return wires, an open in the supply or signal wires, low supply voltage from the ECM, or a failed sensor.
>
> ### Component Location
>
> Refer to the Engine Diagrams. 100-002 for the component location.
>
> ### Shoptalk
>
> If Fault Code 143 or 415 is **not** present, the problem is **not** base engine related.
>
> Refer to specific engine wiring diagram for the output voltage of the pressure sensor.
>
> Note: Some engine models will use the Metri-Pack type connector on this pressure sensor, and some will use the Danfoss™ type connector. The Metri-Pack connector pin designators are alpha and the Danfoss™ connector pin designators are numeric. The steps depicted in this fault code show the Metri-Pack type connector with alpha pin callouts. Refer to specific engine wiring diagrams to determine the correct pin designators for the type of connector.
>
> Refer to Troubleshooting Fault Code t05-141
