---
aliases:
  - "Диагностика драйвера предупреждающего светодиода"
type: "Процедура"
doc: "01-fc1488"
title_en: "Warning LED Driver Diagnostic"
title_ru: "Диагностика драйвера предупреждающего светодиода"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1488.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1488.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Warning LED Driver Diagnostic
**Диагностика драйвера предупреждающего светодиода**

> [!abstract] Процедура · `01-fc1488`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1488.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1488.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 1488

### Диагностика драйвера предупреждающего светодиода

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 1488 PID(P): СПН: ФМИ: Лампа: Предупреждение СТО: | Диагностика светодиодного драйвера с предупреждением панели коммутатора обнаружила ошибку. | Предупреждающий светодиод будет работать **не** правильно. Никаких действий со стороны ЕКМ не предпринимается. Никаких потерь в производительности. |

![[19802914.png]]

Предупреждение светодиодной цепи водителя

### Описание цепи

ECM проверяет предупреждающий светодиодный драйвер, чтобы убедиться, что он работает правильно. ECM использует предупредительную лампу, чтобы сообщить оператору, что с генераторной установкой произошла некритическая неисправность.

ECM контролирует напряжение (ни одно падение напряжения не будет сбивать код 1488) и может быть вызвано шортами, отверстиями, плохими лампами или неисправным светодиодным драйвером в ECM.

### Расположение компонента

См. раздел E для определения местоположения панели переключателя и предупреждающей лампы.

### Практические замечания

Возможные режимы отказа - это открытая цепь, короткая к земле, выгоревшая лампа и потеря напряжения питания внутри ECM.

Правильная работа диагностического светильника может быть проверена путем проверки, чтобы увидеть, что лампы кратковременно загораются при включении ECM.

См. Код устранения неисправностей t05-1488


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 1488
>
> ### Warning LED Driver Diagnostic
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 1488 PID(P): SPN: FMI: Lamp: Warning SRT: | Switch panel warning LED driver diagnostic has detected an error. | The warning LED will **not** function correctly. No action is taken by the ECM. No loss of performance. |
>
> Warning LED Driver Circuit
>
> ### Circuit Description
>
> The ECM checks the warning LED driver to make certain it is operating correctly. The ECM uses the warning lamp to inform the operator that a noncritical fault has occurred with the generator set.
>
> The ECM monitors the voltage, (no voltage drop will trip Fault Code 1488) and can be caused by shorts, opens, bad bulbs, or a failed warning LED driver in the ECM.
>
> ### Component Location
>
> Refer to Section E for location of the switch panel and the warning lamp.
>
> ### Shoptalk
>
> The possible failure modes are open circuit, short to ground, burned out bulb, and loss of supply voltage inside the ECM.
>
> Proper diagnostic lamp operation can be verified by checking to see that the lamps briefly light when the ECM is powered up.
>
> Refer to Troubleshooting Fault Code t05-1488
