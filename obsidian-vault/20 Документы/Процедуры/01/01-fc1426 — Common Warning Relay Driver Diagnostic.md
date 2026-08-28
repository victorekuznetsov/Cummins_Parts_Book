---
aliases:
  - "Диагностика драйвера общего реле предупреждения"
type: "Процедура"
doc: "01-fc1426"
title_en: "Common Warning Relay Driver Diagnostic"
title_ru: "Диагностика драйвера общего реле предупреждения"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1426.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1426.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Common Warning Relay Driver Diagnostic
**Диагностика драйвера общего реле предупреждения**

> [!abstract] Процедура · `01-fc1426`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1426.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1426.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 1426

### Диагностика драйвера общего реле предупреждения

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 1426 PID(P): СПН: ФМИ: Лампа: Предупреждение СТО: | Диагностика водителя реле с предупреждением обнаружила ошибку. | Реле предупреждения будет работать **не**. Никаких действий со стороны ЕКМ не предпринимается. Никаких потерь в производительности. |

![[19802449.png]]

Обычный реле-реле Driver Circuit

### Описание цепи

ECM проверяет общий драйвер реле предупреждения для поддержания правильной работы. ECM использует общее реле предупреждения для информирования оператора о некритической неисправности. ECM контролирует напряжение, падение напряжения не будет сбивать код 1426 по умолчанию и может быть вызвано шортами, открытиями, плохими реле или отказом общего драйвера реле предупреждения в ECM.

### Расположение компонента

См. руководство по OEM для определения местоположения ECM. См. руководство OEM для определения местоположения панели пользовательского интерфейса и общего реле предупреждения.

### Практические замечания

Возможные режимы отказа - это открытая цепь, короткая к земле, выгоревшая реле и потеря напряжения питания внутри ECM.

См. Код устранения неисправностей t05-1426


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 1426
>
> ### Common Warning Relay Driver Diagnostic
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 1426 PID(P): SPN: FMI: Lamp: Warning SRT: | Common warning relay driver diagnostic has detected an error. | The warning relay will **not** function correctly. No action is taken by the ECM. No loss of performance. |
>
> Common Warning Relay Driver Circuit
>
> ### Circuit Description
>
> The ECM checks the common warning relay driver to sustain correct operation. The ECM uses the common warning relay to inform the operator of a noncritical fault. The ECM monitors the voltage, no voltage drop will trip Fault Code 1426, and can be caused by shorts, opens, bad relays, or a failed common warning relay driver in the ECM.
>
> ### Component Location
>
> Refer to the OEM manual for location of the ECM. Refer to the OEM manual for location of the user interface panel and the common warning relay.
>
> ### Shoptalk
>
> The possible failure modes are open circuit, short to ground, burned-out relay, and loss of supply voltage inside the ECM.
>
> Refer to Troubleshooting Fault Code t05-1426
