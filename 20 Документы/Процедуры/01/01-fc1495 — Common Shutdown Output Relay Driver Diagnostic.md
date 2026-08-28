---
aliases:
  - "Диагностика драйвера общего выходного реле останова"
type: "Процедура"
doc: "01-fc1495"
title_en: "Common Shutdown Output Relay Driver Diagnostic"
title_ru: "Диагностика драйвера общего выходного реле останова"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1495.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1495.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Common Shutdown Output Relay Driver Diagnostic
**Диагностика драйвера общего выходного реле останова**

> [!abstract] Процедура · `01-fc1495`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1495.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1495.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 1495

### Диагностика драйвера общего выходного реле останова

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 1495 PID(P): СПН: ФМИ: Лампа: Предупреждение СТО: | Диагностика драйвера реле Common Shutdown выявила ошибку. | Любые функции клиента, зависящие от выходного сигнала Common Shutdown, будут работать **не**. Никаких действий со стороны ЕКМ не предпринимается. Никаких потерь в производительности. |

![[19802920.png]]

Распространенная схема ретранслятора выходного вывода Shutdown Output

### Описание цепи

ECM проверяет общий драйвер выходного реле отключения, чтобы обеспечить правильную работу. ECM использует общий выходной сигнал отключения для информирования любого клиента / функций, зависящих от ECM, о критической неисправности генераторной установки. ECM контролирует напряжение (без увеличения напряжения будет срабатывать код 1495 неисправности), вызванное короткими замыканиями, открытыми цепями или неисправным общим драйвером выключения выходного реле в ECM.

### Расположение компонента

См. раздел E для определения местоположения выхода для общего отключения.

### Практические замечания

Возможные режимы отказа - это открытые цепи, короткие замыкания, короткие к земле и потеря напряжения питания внутри ECM.

См. Код устранения неисправностей t05-1495


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 1495
>
> ### Common Shutdown Output Relay Driver Diagnostic
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 1495 PID(P): SPN: FMI: Lamp: Warning SRT: | The Common Shutdown output relay driver diagnostic has detected an error. | Any customer features dependent on Common Shutdown output will **not** function correctly. No action taken by ECM. No loss of performance. |
>
> Common Shutdown Output Relay Driver Circuit
>
> ### Circuit Description
>
> The ECM checks the common shutdown output relay driver to ensure correct operation. The ECM uses common shutdown output to inform any customer/features dependent on the ECM for knowledge of a critical fault with the generator set. The ECM monitors the voltage (no voltage increase will trip Fault Code 1495) caused by short circuits, open circuits, or failed common shutdown output relay driver in the ECM.
>
> ### Component Location
>
> Refer to section E for location of the output for the common shutdown.
>
> ### Shoptalk
>
> Possible failure modes are open circuits, short circuits, short to ground, and loss of supply voltage inside the ECM.
>
> Refer to Troubleshooting Fault Code t05-1495
