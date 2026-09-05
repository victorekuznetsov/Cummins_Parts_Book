---
aliases:
  - "Диагностика драйвера светодиода останова"
type: "Процедура"
doc: "01-fc1489"
title_en: "Shutdown LED Driver Diagnostic"
title_ru: "Диагностика драйвера светодиода останова"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1489.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1489.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Shutdown LED Driver Diagnostic
**Диагностика драйвера светодиода останова**

> [!abstract] Процедура · `01-fc1489`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1489.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1489.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 1489

### Диагностика драйвера светодиода останова

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 1489 PID(P): СПН: ФМИ: Лампа: Предупреждение СТО: | Диагностика выключения панели коммутатора LED-драйвера выявила ошибку. | Светодиод выключения **не** работает правильно. Никаких действий со стороны ЕКМ не предпринимается. Никаких потерь в производительности. |

![[19802915.png]]

Выключение LED Driver Circuit

### Описание цепи

ECM проверяет выключаемый светодиодный драйвер, чтобы убедиться в правильной работе. ECM использует лампу отключения, чтобы сообщить оператору, что с генераторной установкой произошел критический сбой.

ECM контролирует напряжение (никакое падение напряжения не будет сбивать Код 1489 по умолчанию) и может быть вызвано шортами, отверстиями, плохими лампами или неисправным светодиодным драйвером выключения в ECM.

### Расположение компонента

См. раздел E для определения местоположения панели переключателя и выключателя.

### Практические замечания

Возможные режимы отказа - открытая цепь, короткая к земле, выгоревшая лампа и потеря питания.

Правильная работа диагностического светильника может быть проверена путем проверки, чтобы увидеть, что лампы кратковременно загораются при включении ECM.

См. Код устранения неполадок t05-1489


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 1489
>
> ### Shutdown LED Driver Diagnostic
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 1489 PID(P): SPN: FMI: Lamp: Warning SRT: | Switch panel shutdown LED driver diagnostic has detected an error. | The shutdown LED will **not** function correctly. No action is taken by the ECM. No loss of performance. |
>
> Shutdown LED Driver Circuit
>
> ### Circuit Description
>
> The ECM checks the shutdown LED driver to be sure of correct operation. The ECM uses the shutdown lamp to inform the operator that a critical fault has occurred with the generator set.
>
> The ECM monitors the voltage (no voltage drop will trip Fault Code 1489) and can be caused by shorts, opens, bad bulbs, or a failed shutdown LED driver in the ECM.
>
> ### Component Location
>
> Refer to Section E for location of the switch panel and the shutdown lamp.
>
> ### Shoptalk
>
> The possible failure modes are open circuit, short to ground, burned-out bulb, and loss of supply.
>
> Proper diagnostic lamp operation can be verified by checking to see that the lamps briefly light when the ECM is powered up.
>
> Refer to Troubleshooting Fault Code t05-1489
