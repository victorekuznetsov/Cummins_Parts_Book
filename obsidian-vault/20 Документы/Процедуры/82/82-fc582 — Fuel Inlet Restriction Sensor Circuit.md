---
aliases:
  - "Цепь датчика сопротивления на входе топлива"
type: "Процедура"
doc: "82-fc582"
title_en: "Fuel Inlet Restriction Sensor Circuit"
title_ru: "Цепь датчика сопротивления на входе топлива"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc582.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc582.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# Fuel Inlet Restriction Sensor Circuit
**Цепь датчика сопротивления на входе топлива**

> [!abstract] Процедура · `82-fc582`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc582.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc582.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 582

### Цепь датчика сопротивления на входе топлива

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 582 P(P): P015 SPN: 1381 FMI: 4/4 лампы: Желтая СТО: | Низкое напряжение, обнаруженное при контакте с датчиком ограничения впуска топлива. | Монитор ограничения впуска топлива отключен. |

![[19c00578.png]]

Цепь датчика сопротивления на входе топлива

### Описание цепи

Датчик ограничения впуска топлива обеспечивает сигнал давления топлива к электронному модулю управления (ECM).

### Расположение компонента

Датчик ограничения впуска топлива расположен на головке крепления топливного фильтра.

### Практические замечания

- Эта неисправность указывает на то, что напряжение при контакте 28 сигнала на ECM находится за пределами заданных пределов.

- ECM обеспечивает напряжение питания от +4,75 до 5,25 ВДК. Напряжение сигнала датчика к ECM составляет от +4,16 до 4,83 ВДК.

- Быстрая проверка, чтобы определить, работает ли датчик, заключается в измерении сопротивления контакта к контакту датчика.

| Наименование | Сопротивление контакт-контакт (k Ом) |
|---|---|
| Напряжение питания на землю | 13.35 |
| Напряжение подачи сигнала | 1.77 |
| Сигнал к земле | 14.68 |

См. Код устранения неполадок t05-582


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 582
>
> ### Fuel Inlet Restriction Sensor Circuit
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 582 PID(P): P015 SPN: 1381 FMI: 4/4 Lamp: Yellow SRT: | Low voltage detected at the fuel inlet restriction sensor signal pin. | Fuel inlet restriction monitor deactivated. |
>
> Fuel Inlet Restriction Sensor Circuit
>
> ### Circuit Description
>
> The fuel inlet restriction sensor provides a fuel pressure signal to the electronic control module (ECM).
>
> ### Component Location
>
> The fuel inlet restriction sensor is located on the fuel filter head.
>
> ### Shoptalk
>
> - This fault indicates that the voltage at signal pin 28 on the ECM is out of specification.
>
> - The ECM provides a supply voltage of + 4.75 to 5.25 VDC. The sensor signal voltage to the ECM is from + 4.16 to 4.83 VDC.
>
> - A quick check to determine if the sensor is functioning is to measure the pin-to-pin resistance of the sensor.
>
> | Description | Pin-to-Pin Resistance (k ohms) |
> |---|---|
> | Supply voltage to ground | 13.35 |
> | Supply voltage to signal | 1.77 |
> | Signal to ground | 14.68 |
>
> Refer to Troubleshooting Fault Code t05-582
