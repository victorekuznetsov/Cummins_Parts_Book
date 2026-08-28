---
aliases:
  - "Цепь выключателя подтверждения холостого хода"
type: "Процедура"
doc: "82-fc431iss"
title_en: "Idle Validation Switch Circuit"
title_ru: "Цепь выключателя подтверждения холостого хода"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc431iss.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc431iss.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# Idle Validation Switch Circuit
**Цепь выключателя подтверждения холостого хода**

> [!abstract] Процедура · `82-fc431iss`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc431iss.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc431iss.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 431

### Цепь выключателя подтверждения холостого хода

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 431 PID(P): S230 SPN: 558 FMI: 2/2 лампы: Желтая СТО: | Нет напряжения, обнаруженного одновременно как на холостых валидирующих отключаемых, так и на холостых сигнальных штифтах. | Ни одного на выступление. |

![[19c00644.png]]

Цепь выключателя подтверждения холостого хода

### Описание цепи

Переключатель проверки бездействия используется электронным модулем управления (ECM) для указания, когда педаль акселератора выпущена (на холостом ходу) или подавлена (вне холостом ходу). Переключатель настраивается на заводе для переключения с on-idle на off-idle в правильном положении педали акселератора.

### Расположение компонента

Интегрированный сенсорный переключатель (ISS) расположен на педальном сборе ускорителя.

### Практические замечания

- Этот код неисправности обычно вызван свободным соединением, некалиброванной педалью ускорителя или неправильно проводным переключателем проверки.

- Интегрированный сенсорный переключатель (ISS) имеет другую спецификацию сопротивления холостого валидационного переключателя (IVS) (125 Ом) по сравнению с неинтегрированным сенсорным переключателем (NISS) (10 Ом).

См. Код устранения неполадок t05-431iss


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 431
>
> ### Idle Validation Switch Circuit
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 431 PID(P): S230 SPN: 558 FMI: 2/2 Lamp: Yellow SRT: | No voltage detected simultaneously on both the idle validation off-idle and on-idle signal pins. | None on performance. |
>
> Idle Validation Switch Circuit
>
> ### Circuit Description
>
> The idle validation switch is used by the electronic control module (ECM) to indicate when the accelerator pedal is released (on-idle) or depressed (off-idle). The switch is adjusted at the factory to switch from on-idle to off-idle at the correct accelerator pedal position.
>
> ### Component Location
>
> The integrated sensor switch (ISS) is located on the accelerator pedal assembly.
>
> ### Shoptalk
>
> - This fault code is usually caused by a loose connection, uncalibrated accelerator pedal, or miswired idle validation switch.
>
> - The integrated sensor switch (ISS) has a different idle validation switch (IVS) resistance specification (125 ohms) as compared to nonintegrated sensor switch (NISS) (10 ohms).
>
> Refer to Troubleshooting Fault Code t05-431iss
