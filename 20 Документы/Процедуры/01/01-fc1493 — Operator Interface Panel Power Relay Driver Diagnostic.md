---
aliases:
  - "Диагностика драйвера реле питания панели оператора"
type: "Процедура"
doc: "01-fc1493"
title_en: "Operator Interface Panel Power Relay Driver Diagnostic"
title_ru: "Диагностика драйвера реле питания панели оператора"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1493.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1493.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Operator Interface Panel Power Relay Driver Diagnostic
**Диагностика драйвера реле питания панели оператора**

> [!abstract] Процедура · `01-fc1493`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1493.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1493.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 1493

### Диагностика драйвера реле питания панели оператора

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 1493 PID(P): СПН: ФМИ: Лампа: Предупреждение СТО: | Диагностика драйвера реле питания операторского интерфейса выявила ошибку. | Панель интерфейса оператора будет работать ** не**. Никаких действий со стороны ЕКМ не предпринимается. Никаких потерь в производительности. |

![[19802918.png]]

Operator Interface Panel Power Relay Driver Circuit (недоступная ссылка)

### Описание цепи

ECM проверяет драйвер реле питания панели оператора, чтобы обеспечить правильную работу. ECM использует панель интерфейса оператора, чтобы информировать оператора о работе генераторной установки, производительности, настройке и диагностике. ECM контролирует напряжение (без увеличения напряжения будет срабатывать код 1493 по умолчанию), вызванное короткими замыканиями, открытыми цепями или неисправным драйвером реле питания панели оператора в ECM.

### Расположение компонента

См. раздел E для определения местоположения панели интерфейса оператора.

### Практические замечания

Возможные режимы отказа - это открытые цепи, короткие замыкания, короткие к земле и потеря напряжения питания внутри ECM.

См. Код устранения неполадок t05-1493


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 1493
>
> ### Operator Interface Panel Power Relay Driver Diagnostic
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 1493 PID(P): SPN: FMI: Lamp: Warning SRT: | Operator interface panel power relay driver diagnostic has detected an error. | Operator interface panel will **not** function correctly. No action taken by ECM. No loss of performance. |
>
> Operator Interface Panel Power Relay Driver Circuit
>
> ### Circuit Description
>
> The ECM checks the operator interface panel power relay driver to ensure correct operation. The ECM uses the operator interface panel to inform the operator about generator set operation, performance, setup, and diagnostics. The ECM monitors the voltage (no voltage increase will trip Fault Code 1493) caused by short circuits, open circuits, or failed operator interface panel power relay driver in the ECM.
>
> ### Component Location
>
> Refer to section E for location of the operator interface panel.
>
> ### Shoptalk
>
> Possible failure modes are open circuits, short circuits, short to ground, and loss of supply voltage inside the ECM.
>
> Refer to Troubleshooting Fault Code t05-1493
