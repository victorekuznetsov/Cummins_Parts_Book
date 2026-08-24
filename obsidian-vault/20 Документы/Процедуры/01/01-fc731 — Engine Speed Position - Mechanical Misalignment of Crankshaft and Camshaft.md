---
aliases:
  - "Частота/положение — механическое рассогласование коленчатого и распределительного валов"
type: "Процедура"
doc: "01-fc731"
title_en: "Engine Speed/Position - Mechanical Misalignment of Crankshaft and Camshaft"
title_ru: "Частота/положение — механическое рассогласование коленчатого и распределительного валов"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc731.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc731.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Engine Speed/Position - Mechanical Misalignment of Crankshaft and Camshaft
**Частота/положение — механическое рассогласование коленчатого и распределительного валов**

> [!abstract] Процедура · `01-fc731`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc731.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc731.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 731

### Частота/положение — механическое рассогласование коленчатого и распределительного валов

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 731 P(P): СПН: ФМИ: Лампа: Предупреждение СТО: | Между распределительным валом и коленчатым валом произошло механическое несоответствие. Произойдет синхронная ошибка. | Никаких действий со стороны ЕКМ не предпринимается. Возможная потеря производительности. |

![[19803589.png]]

Цепь датчика частоты вращения двигателя

### Описание цепи

Датчик скорости двигателя - это твердотельный датчик, который обеспечивает сигнал скорости двигателя электронному модулю управления (ECM) через электропроводку двигателя.

### Расположение компонента

См. схемы двигателя. 100-002 для расположения компонентов.

### Практические замечания

Если проблема возникает только при определенной температуре двигателя, обязательно проверьте схему датчика скорости двигателя, пока двигатель находится при этой конкретной температуре.

См. Код устранения неполадок t05-731


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 731
>
> ### Engine Speed/Position - Mechanical Misalignment of Crankshaft and Camshaft
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 731 PID(P): SPN: FMI: Lamp: Warning SRT: | A mechanical misalignment has occurred between the camshaft and crankshaft. A sync error will occur. | No action is taken by the ECM. Possible loss of performance. |
>
> Engine Speed Sensor Circuit
>
> ### Circuit Description
>
> The engine speed sensor is a solid-state sensor that provides the engine speed signal to the electronic control module (ECM), through the engine harness.
>
> ### Component Location
>
> Refer to the Engine Diagrams. 100-002 for the component location.
>
> ### Shoptalk
>
> If the problem occurs **only** at a certain engine temperature, be sure to check the engine speed sensor circuit while the engine is at that particular temperature.
>
> Refer to Troubleshooting Fault Code t05-731
