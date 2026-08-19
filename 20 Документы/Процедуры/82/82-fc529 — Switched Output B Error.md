---
aliases:
  - "Ошибка коммутируемого выхода B"
type: "Процедура"
doc: "82-fc529"
title_en: "Switched Output B Error"
title_ru: "Ошибка коммутируемого выхода B"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc529.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc529.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# Switched Output B Error
**Ошибка коммутируемого выхода B**

> [!abstract] Процедура · `82-fc529`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc529.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc529.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 529 (Индустриальный)

### Ошибка коммутируемого выхода B

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 529 PID(P): S51 SPN: 703 FMI: 3/3 лампы: Желтая СТО: | Менее +17 ВДК, обнаруженных при переключенном выходе В сигнала контакта в электронном модуле управления (ЭУУ). | Никаких действий со стороны ЕКМ не предпринималось. |

![[19c00574.png]]

Выключенный выход B Circuit

### Описание цепи

Водитель соленоида будет управлять двигателем и функциями транспортного средства, закрывая или открывая переключаемый выход соленоида, на основе 11 выбранных параметров двигателя. Выход соленоидов будет контролировать такие функции, как сцепление вентилятора, нагреватель впускной сетки, индикатор ограничения очистки воздуха или индикатор дифференциального давления масляного фильтра.

### Расположение компонента

Соленоидный драйвер является OEM-устройством, и местоположение соленоида зависит от OEM-устройства.

См. Код устранения неполадок t05-529


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 529 (INDUSTRIAL)
>
> ### Switched Output B Error
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 529 PID(P): S51 SPN: 703 FMI: 3/3 Lamp: Yellow SRT: | Less than + 17 VDC detected at the switched output B signal pin at the electronic control module (ECM). | No action taken by the ECM. |
>
> Switched Output B Circuit
>
> ### Circuit Description
>
> The solenoid driver will control engine and vehicle functions by closing or opening a switched solenoid output, based on 11 selected engine parameters. The solenoid output will control functions such as a fan clutch, intake grid heater, air cleaner restriction indicator, or an oil filter differential pressure indicator.
>
> ### Component Location
>
> The solenoid driver is an OEM device, and the location of the solenoid is dependent upon the OEM.
>
> Refer to Troubleshooting Fault Code t05-529
