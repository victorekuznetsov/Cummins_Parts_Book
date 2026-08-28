---
aliases:
  - "Датчик давления прорыва газов — замыкание на массу"
type: "Процедура"
doc: "01-fc729"
title_en: "Blowby Pressure Sensor - Shorted Low"
title_ru: "Датчик давления прорыва газов — замыкание на массу"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc729.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc729.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Blowby Pressure Sensor - Shorted Low
**Датчик давления прорыва газов — замыкание на массу**

> [!abstract] Процедура · `01-fc729`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc729.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc729.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 729

### Датчик давления прорыва газов — замыкание на массу

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 729 PID(P): СПН: ФМИ: Лампа: Предупреждение СТО: | Для этого используется схема с датчиком давления с закороченным газом. | Отсутствие защиты двигателя от давления продува. |

![[19803587.png]]

Схема датчика давления Blowby Pressure Sensor Circuit

### Описание цепи

Датчик давления продувки контролирует давление продувки и передает информацию в электронный модуль управления (ECM). Низкое напряжение будет сбивать Код 729 по умолчанию и может быть вызвано шортами в проводах подачи, сигнала или возврата, открытым в проводах возврата или неисправным датчиком.

### Расположение компонента

См. схемы двигателя. 100-002 для расположения компонентов.

### Практические замечания

Подтвердите, что дыхательные аппараты, дыхательные трубки и датчик продува **не *** затрудняются.

См. Код устранения неполадок t05-729


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 729
>
> ### Blowby Pressure Sensor - Shorted Low
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 729 PID(P): SPN: FMI: Lamp: Warning SRT: | Crankcase blowby pressure sensor circuit - shorted low. | No engine protection for blowby pressure. |
>
> Blowby Pressure Sensor Circuit
>
> ### Circuit Description
>
> The blowby pressure sensor monitors blowby pressure and passes information to the electronic control module (ECM). Low voltage will trip Fault Code 729 and can be caused by shorts in the supply, signal, or return wires, an open in the return wires, or a failed sensor.
>
> ### Component Location
>
> Refer to the Engine Diagrams. 100-002 for the component location.
>
> ### Shoptalk
>
> Confirm that the crankcase breathers, breather tubes, and blowby sensor are **not** obstructed.
>
> Refer to Troubleshooting Fault Code t05-729
