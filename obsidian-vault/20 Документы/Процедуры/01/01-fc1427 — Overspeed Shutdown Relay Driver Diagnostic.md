---
aliases:
  - "Диагностика драйвера реле останова по разносу"
type: "Процедура"
doc: "01-fc1427"
title_en: "Overspeed Shutdown Relay Driver Diagnostic"
title_ru: "Диагностика драйвера реле останова по разносу"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1427.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1427.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Overspeed Shutdown Relay Driver Diagnostic
**Диагностика драйвера реле останова по разносу**

> [!abstract] Процедура · `01-fc1427`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1427.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1427.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 1427

### Диагностика драйвера реле останова по разносу

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 1427 P(P): СПН: ФМИ: Лампа: Предупреждение СТО: | Диагностика драйвера реле сверхскоростного отключения выявила ошибку. | Реле отключения скорости не будет работать правильно. Никаких действий со стороны ЕКМ не предпринимается. Никаких потерь в производительности. |

![[19802449.png]]

Overspeed Shutdown Relay Driver Circuit (недоступная ссылка)

### Описание цепи

ECM проверяет драйвер реле отключения сверхскоростной скорости для поддержания правильной работы. ECM использует реле отключения сверхскоростной скорости, чтобы сообщить оператору о некритической неисправности. ECM контролирует напряжение, падение напряжения не будет сбивать код 1427 по умолчанию и может быть вызвано шортами, открытиями, плохими реле или неисправным драйвером реле выключения сверхскоростной скорости в ECM.

### Расположение компонента

См. руководство по OEM для определения местоположения ECM. См. руководство OEM для определения местоположения панели пользовательского интерфейса и реле перескоростного отключения.

### Практические замечания

Возможные режимы отказа - это открытая цепь, короткая к земле, выгоревшая реле и потеря напряжения питания внутри ECM.

См. Код устранения неисправностей t05-1427


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 1427
>
> ### Overspeed Shutdown Relay Driver Diagnostic
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 1427 PID(P): SPN: FMI: Lamp: Warning SRT: | Overspeed shutdown relay driver diagnostic has detected an error. | The overspeed shutdown relay will **not** function correctly. No action is taken by the ECM. No loss of performance. |
>
> Overspeed Shutdown Relay Driver Circuit
>
> ### Circuit Description
>
> The ECM checks the overspeed shutdown relay driver to sustain correct operation. The ECM uses the overspeed shutdown relay to inform the operator of a noncritical fault. The ECM monitors the voltage, no voltage drop will trip Fault Code 1427, and can be caused by shorts, opens, bad relays, or a failed overspeed shutdown relay driver in the ECM.
>
> ### Component Location
>
> Refer to the OEM manual for location of the ECM. Refer to the OEM manual for location of the user interface panel and the overspeed shutdown relay.
>
> ### Shoptalk
>
> The possible failure modes are open circuit, short to ground, burned-out relay, and loss of supply voltage inside the ECM.
>
> Refer to Troubleshooting Fault Code t05-1427
