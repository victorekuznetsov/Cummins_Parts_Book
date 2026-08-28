---
aliases:
  - "Диагностика драйвера реле сброса нагрузки"
type: "Процедура"
doc: "01-fc1492"
title_en: "Load Dump Output Relay Driver Diagnostic"
title_ru: "Диагностика драйвера реле сброса нагрузки"
modified: "2011-11-03"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1492.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1492.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Load Dump Output Relay Driver Diagnostic
**Диагностика драйвера реле сброса нагрузки**

> [!abstract] Процедура · `01-fc1492`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2011-11-03
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1492.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1492.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 1492

### Диагностика драйвера реле сброса нагрузки

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 1492 PID(P): СПН: ФМИ: Лампа: Предупреждение СТО: | Диагностика драйвера реле Load Dump выявила ошибку. | Любая система/функции клиента, зависящие от вывода Load Dump, будут работать **не**. Никаких действий со стороны ЕКМ не предпринимается. Никаких потерь в производительности. |

![[19802917.png]]

Схема управления реле Load Dump Output

### Описание цепи

ECM проверяет драйвер выходного реле Load Dump, чтобы обеспечить правильную работу. ECM использует выходной насос нагрузки, чтобы информировать любых клиентов / характеристики, зависящие от ECM, о том, когда генераторная установка должна сбросить нагрузку. ECM контролирует напряжение (без увеличения напряжения будет сбивать код 1492 по умолчанию), вызванное короткими замыканиями, открытыми цепями или неисправным драйвером выходного реле Load Dump в ECM.

### Расположение компонента

См. раздел E для определения местоположения выхода для сброса нагрузки.

### Практические замечания

Возможные режимы отказа - это открытые цепи, короткие замыкания, короткие к земле и потеря напряжения питания внутри ECM.

См. Код устранения неполадок t05-1492


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 1492
>
> ### Load Dump Output Relay Driver Diagnostic
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 1492 PID(P): SPN: FMI: Lamp: Warning SRT: | The Load Dump output relay driver diagnostic has detected an error. | Any customer system/features dependent on the Load Dump output will **not** function correctly. No action taken by ECM. No loss of performance. |
>
> The Load Dump Output Relay Driver Circuit
>
> ### Circuit Description
>
> The ECM checks the Load Dump output relay driver to ensure correct operation. The ECM uses the Load Dump output to inform any customers/feature dependent on the ECM for knowledge of when the generator set has to dump a load. The ECM monitors the voltage (no voltage increase will trip Fault Code 1492) caused by short circuits, open circuits, or failed Load Dump output relay driver in the ECM.
>
> ### Component Location
>
> Refer to Section E for location of the output for the Load Dump.
>
> ### Shoptalk
>
> Possible failure modes are open circuits, short circuits, short to ground, and loss of supply voltage inside the ECM.
>
> Refer to Troubleshooting Fault Code t05-1492
