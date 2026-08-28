---
aliases:
  - "Цепь педали акселератора"
type: "Процедура"
doc: "82-fc432"
title_en: "Accelerator Pedal Circuit"
title_ru: "Цепь педали акселератора"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc432.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc432.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# Accelerator Pedal Circuit
**Цепь педали акселератора**

> [!abstract] Процедура · `82-fc432`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc432.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc432.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 432

### Цепь педали акселератора

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 432 PID(P): S230 SPN: 558 FMI: 13/13 Лампа: Красная СТО: | Напряжение, обнаруженное при холостом валидировании на холостом ходу, когда напряжение на дроссельном ходу указывает, что педаль **не **на холостом ходу **или **напряжение, обнаруженное на холостом ходу валидации вне холостого хода, когда напряжение на дроссельном ходу указывает, что педаль находится в покое. | Двигатель будет только  простаивать. |

![[19c00644.png]]

Цепь педали акселератора

### Описание цепи

Ускоритель педалей в сборе ретранслирует процентное содержание ускорителя, запрошенное оператором, в электронный модуль управления (ECM).

### Расположение компонента

Датчик положения ускорителя расположен на педали ускорителя.

### Практические замечания

Подтвердите, что выключатель проверки бездействия (IVS) правильно откалиброван. См. инструкции изготовителя педали акселератора для информации о регулировке.

Устранение неполадок код t05-432


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 432
>
> ### Accelerator Pedal Circuit
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 432 PID(P): S230 SPN: 558 FMI: 13/13 Lamp: Red SRT: | Voltage detected at idle validation on-idle circuit when voltage at throttle position circuit indicates the pedal is **not** at idle **or** voltage detected at idle validation off-idle circuit when voltage at throttle position circuit indicates the pedal is at rest. | Engine will **only** idle. |
>
> Accelerator Pedal Circuit
>
> ### Circuit Description
>
> The accelerator pedal assembly relays the accelerator percentage requested by the operator to the electronic control module (ECM).
>
> ### Component Location
>
> The accelerator position sensor is located on the accelerator pedal.
>
> ### Shoptalk
>
> Confirm that the idle validation switch (IVS) is properly calibrated. Refer to the accelerator pedal manufacturer's instructions for adjustment information.
>
> Refer to Troubleshooting Fault Code t05-432
