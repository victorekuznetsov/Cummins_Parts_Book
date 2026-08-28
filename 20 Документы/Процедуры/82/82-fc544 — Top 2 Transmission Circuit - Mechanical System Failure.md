---
aliases:
  - "Цепь двух высших передач — отказ механической системы"
type: "Процедура"
doc: "82-fc544"
title_en: "Top 2 Transmission Circuit - Mechanical System Failure"
title_ru: "Цепь двух высших передач — отказ механической системы"
modified: "2010-09-02"
engines:
  - "41343322"
  - "41370103"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc544.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc544.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# Top 2 Transmission Circuit - Mechanical System Failure
**Цепь двух высших передач — отказ механической системы**

> [!abstract] Процедура · `82-fc544`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc544.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc544.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 544

### Цепь двух высших передач — отказ механической системы

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 544 PID(P): S151 SPN: 611 FMI: 7/7 Лампа: Желтая СТО: | Неудачи в автосмены, по крайней мере, три попытки смены были пропущены. | Топ-2 передачи будет **не** управляться правильно. Передача остается в ручном режиме. |

![[19c00352.png]]

ТОП 2 Трансмиссионные схемы

### Описание цепи

Схема передачи Top 2 управляет передачей Top 2 для автоматического переключения между передачами Top 2.

### Расположение компонента

Топ-2 сдвига/блокировки соленоидов находятся на верхней стороне передачи, рядом с задней частью. Смотрите диаграмму OEM для точного местоположения.

Устранение неполадок код t05-544


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 544
>
> ### Top 2 Transmission Circuit - Mechanical System Failure
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 544 PID(P): S151 SPN: 611 FMI: 7/7 Lamp: Yellow SRT: | Autoshift failure; at least three shift attempts were missed. | Top 2 transmission will **not** be controlled correctly. Transmission remains in manual mode. |
>
> Top 2 Transmission Circuit
>
> ### Circuit Description
>
> The Top 2 transmission circuit controls a Top 2 transmission to autoshift between the Top 2 gears.
>
> ### Component Location
>
> The Top 2 shift/lockout solenoids are on the topside of the transmission, near the back. Refer to an OEM diagram for the exact location.
>
> Refer to Troubleshooting Fault Code t05-544
