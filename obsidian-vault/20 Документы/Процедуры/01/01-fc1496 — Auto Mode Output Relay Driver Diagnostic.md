---
aliases:
  - "Диагностика драйвера реле автоматического режима"
type: "Процедура"
doc: "01-fc1496"
title_en: "Auto Mode Output Relay Driver Diagnostic"
title_ru: "Диагностика драйвера реле автоматического режима"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1496.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1496.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Auto Mode Output Relay Driver Diagnostic
**Диагностика драйвера реле автоматического режима**

> [!abstract] Процедура · `01-fc1496`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1496.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1496.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 1496

### Диагностика драйвера реле автоматического режима

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 1496 PID(P): СПН: ФМИ: Лампа: Предупреждение СТО: | Диагностика драйвера реле Auto Mode выявила ошибку. | Любые функции клиента, зависящие от выхода в автоматическом режиме, будут работать ** не**. Никаких действий со стороны ЕКМ не предпринимается. Никаких потерь в производительности. |

![[19802921.png]]

Автоматический режим Output Relay Driver Circuit

### Описание цепи

ECM проверяет драйвер выходного реле Auto Mode, чтобы обеспечить правильную работу. ECM использует выходной режим Auto Mode для информирования любого клиента / функций, зависящих от ECM, о том, когда работает генераторная установка. ECM контролирует напряжение (без увеличения напряжения будет срабатывать код 1496 по умолчанию), вызванное короткими замыканиями, открытыми цепями или неисправным драйвером выходного реле Auto Mode в ECM.

### Расположение компонента

См. раздел E для определения местоположения выходного режима авто.

### Практические замечания

Когда управление находится в автоматическом режиме, схема будет обеспечивать B положительное (+) напряжение. Когда управление **не*** в автоматическом режиме, схема будет открыта. Возможные режимы отказа - короткие замыкания, короткие к земле и потеря напряжения питания внутри ECM.

См. Код устранения неисправностей t05-1496


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 1496
>
> ### Auto Mode Output Relay Driver Diagnostic
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 1496 PID(P): SPN: FMI: Lamp: Warning SRT: | The Auto Mode output relay driver diagnostic has detected an error. | Any customer features dependent on Auto Mode output will **not** function correctly. No action taken by ECM. No loss of performance. |
>
> Auto Mode Output Relay Driver Circuit
>
> ### Circuit Description
>
> The ECM checks the Auto Mode output relay driver to ensure correct operation. The ECM uses the Auto Mode output to inform any customer/features dependent on the ECM for knowledge of when the generator set is running.The ECM monitors the voltage (no voltage increase will trip Fault Code 1496) caused by short circuits, open circuits, or failed Auto Mode output relay driver in the ECM.
>
> ### Component Location
>
> Refer to Section E for location of the output Auto Mode.
>
> ### Shoptalk
>
> When the control is in auto mode, the circuit will provide B positive (+) voltage. When the control is **not** in auto mode, the circuit will be open. Possible failure modes are short circuits, short to ground, and loss of supply voltage inside the ECM.
>
> Refer to Troubleshooting Fault Code t05-1496
