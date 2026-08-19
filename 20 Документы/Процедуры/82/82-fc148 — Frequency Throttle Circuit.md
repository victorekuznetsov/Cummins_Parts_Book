---
aliases:
  - "Цепь частотного задания подачи"
type: "Процедура"
doc: "82-fc148"
title_en: "Frequency Throttle Circuit"
title_ru: "Цепь частотного задания подачи"
modified: "2010-09-02"
engines:
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc148.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc148.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# Frequency Throttle Circuit
**Цепь частотного задания подачи**

> [!abstract] Процедура · `82-fc148`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc148.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc148.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 148 (Промышленный)

### Цепь частотного задания подачи

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 148 PID(P): P091 SPN: 91 ФМИ: 8/8 лампы: Красная СТО: | Частота более 100 Гц была обнаружена при частотном дроссельном сигнале контакта разъема электропроводки привода на ECM. | Калибровочная зависимость мощности и скорости снижается. |

![[19c00516.png]]

Цепь частотного задания подачи

### Описание цепи

Частотный дроссел обеспечивает команду дросселя водителя к электронному модулю управления (ECM) через OEM-моторную проводку и приводную проводку. ECM использует этот сигнал для определения команды заправки.

### Расположение компонента

Местоположение дроссельной заслонки варьируется в зависимости от каждого OEM. См. руководство изготовителя машины по диагностике и ремонту.

### Практические замечания

Частотный дроссел может использоваться либо в сочетании с дроссельным напряжением, либо сам по себе.

Устранение неполадок код t05-148


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 148 (Industrial)
>
> ### Frequency Throttle Circuit
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 148 PID(P): P091 SPN: 91 FMI: 8/8 Lamp: Red SRT: | A frequency of more than 100 Hz was detected at the frequency throttle signal pin of the actuator harness connector at the ECM. | Calibration-dependent power and speed derate. |
>
> Frequency Throttle Circuit
>
> ### Circuit Description
>
> The frequency throttle provides the driver's throttle command to the electronic control module (ECM) through the OEM engine harness and the actuator harness. The ECM uses this signal to determine the fueling command.
>
> ### Component Location
>
> Throttle location varies with each OEM. Refer to the OEM troubleshooting and repair manual.
>
> ### Shoptalk
>
> The frequency throttle can be used either in conjunction with a voltage throttle or by itself.
>
> Refer to Troubleshooting Fault Code t05-148
