---
aliases:
  - "Диагностика драйвера светодиода дистанционного пуска"
type: "Процедура"
doc: "01-fc1499"
title_en: "Remote Start LED Driver Diagnostic"
title_ru: "Диагностика драйвера светодиода дистанционного пуска"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1499.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1499.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Remote Start LED Driver Diagnostic
**Диагностика драйвера светодиода дистанционного пуска**

> [!abstract] Процедура · `01-fc1499`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1499.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1499.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 1499

### Диагностика драйвера светодиода дистанционного пуска

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 1499 PID(P): СПН: ФМИ: Лампа: Предупреждение СТО: | Дистанционная диагностика драйвера с дистанционным запуском выявила ошибку. | Дистанционный стартовый светодиод будет работать ** не** правильно. Никаких действий со стороны ЕКМ не предпринимается. Никаких потерь в производительности. |

![[19802924.png]]

Дистанционный запуск LED Driver Circuit

### Описание цепи

ECM проверяет светодиодный драйвер с дистанционным запуском, чтобы обеспечить правильную работу. ECM использует лампу дистанционного запуска, чтобы сообщить оператору, находится ли генераторная установка в режиме дистанционного запуска. ECM контролирует напряжение (без падения напряжения будет сбивать код 1499 по умолчанию), вызванное короткими замыканиями, открытыми цепями, плохим светодиодом или неисправным драйвером светодиода с дистанционным запуском в ECM.

### Расположение компонента

См. раздел E для определения местоположения панели переключателя и лампы дистанционного запуска.

### Практические замечания

Возможные режимы отказа - открытые цепи, короткие к земле, выгоревшие - выключенный светодиод и потеря напряжения питания внутри ECM.

Правильная работа диагностического светильника может быть проверена путем проверки, чтобы увидеть, что лампы кратковременно загораются при включении ECM.

См. Код устранения неисправностей t05-1499


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 1499
>
> ### Remote Start LED Driver Diagnostic
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 1499 PID(P): SPN: FMI: Lamp: Warning SRT: | Switch panel Remote Start LED driver diagnostic has detected an error. | The Remote Start LED will **not** function correctly. No action taken by ECM. No loss of performance. |
>
> Remote Start LED Driver Circuit
>
> ### Circuit Description
>
> The ECM checks the Remote Start LED driver to ensure correct operation. The ECM uses the Remote Start lamp to inform the operator if the generator set is in Remote Start mode. The ECM monitors the voltage (no voltage drop will trip Fault Code 1499) caused by short circuits, open circuits, bad LED, or failed Remote Start LED driver in the ECM.
>
> ### Component Location
>
> Refer to section E for location of the switch panel and Remote Start lamp.
>
> ### Shoptalk
>
> Possible failure modes are open circuits, short to ground, burned - out LED, and loss of supply voltage inside the ECM.
>
> Proper diagnostic lamp operation can be verified by checking to see that the lamps briefly light when the ECM is powered up.
>
> Refer to Troubleshooting Fault Code t05-1499
