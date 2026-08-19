---
aliases:
  - "Диагностика драйвера общего реле останова"
type: "Процедура"
doc: "01-fc1425"
title_en: "Common Shutdown Relay Driver Diagnostic"
title_ru: "Диагностика драйвера общего реле останова"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1425.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1425.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Common Shutdown Relay Driver Diagnostic
**Диагностика драйвера общего реле останова**

> [!abstract] Процедура · `01-fc1425`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1425.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1425.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 1425

### Диагностика драйвера общего реле останова

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 1425 P(P): СПН: ФМИ: Лампа: Предупреждение СТО: | Диагностика драйвера реле выключения обнаружила ошибку. | Общее реле отключения будет ** не** работать правильно. Никаких действий со стороны ЕКМ не предпринимается. Никаких потерь в производительности. |

![[19802449.png]]

Распространенная схема ретранслятора Shutdown Relay Driver Circuit

### Описание цепи

ECM проверяет общий драйвер реле отключения для поддержания правильной работы. ECM использует общее реле отключения для информирования оператора о некритической неисправности. ECM контролирует напряжение, падение напряжения не будет сбивать код 1425 по умолчанию и может быть вызвано шортами, открытиями, плохими реле или неисправным общим драйвером выключения реле в ECM.

### Расположение компонента

См. руководство по OEM для определения местоположения ECM. См. руководство OEM для определения местоположения панели пользовательского интерфейса и общего реле выключения.

### Практические замечания

Возможные режимы отказа - это открытая цепь, короткая к земле, выгоревшая реле и потеря напряжения питания внутри ECM.

См. Код устранения неисправностей t05-1425


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 1425
>
> ### Common Shutdown Relay Driver Diagnostic
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 1425 PID(P): SPN: FMI: Lamp: Warning SRT: | Common shutdown relay driver diagnostic has detected an error. | The common shutdown relay will **not** function correctly. No action is taken by the ECM. No loss of performance. |
>
> Common Shutdown Relay Driver Circuit
>
> ### Circuit Description
>
> The ECM checks the common shutdown relay driver to sustain correct operation. The ECM uses the common shutdown relay to inform the operator of a noncritical fault. The ECM monitors the voltage, no voltage drop will trip Fault Code 1425, and can be caused by shorts, opens, bad relays, or a failed common shutdown relay driver in the ECM.
>
> ### Component Location
>
> Refer to the OEM manual for location of the ECM. Refer to the OEM manual for location of the user interface panel and the common shutdown relay.
>
> ### Shoptalk
>
> The possible failure modes are open circuit, short to ground, burned-out relay, and loss of supply voltage inside the ECM.
>
> Refer to Troubleshooting Fault Code t05-1425
