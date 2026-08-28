---
aliases:
  - "Цепь датчика давления OEM"
type: "Процедура"
doc: "82-fc298"
title_en: "OEM Pressure Sensor Circuit"
title_ru: "Цепь датчика давления OEM"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc298.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc298.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# OEM Pressure Sensor Circuit
**Цепь датчика давления OEM**

> [!abstract] Процедура · `82-fc298`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc298.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc298.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 298 (ИНДУСТРИАЛ)

### Цепь датчика давления OEM

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 298 PID(P): S223 SPN: 1084 FMI: 4/4 лампы: Желтая СТО: | Низкое напряжение, обнаруженное при контакте сигнала датчика давления OEM 31-контактного OEM-разъема. | Отсутствие защиты двигателя от давления OEM. |

![[19200386.png]]

Цепь датчика давления OEM

### Описание цепи

Сигнал датчика OEM используется ECM для мониторинга давления OEM. Давление OEM используется ECM для системы защиты двигателя. Датчик, который вышел из строя низко, может быть вызван коротким замыканием на землю на сигнальном проводе или внутренне заземленным (неисправным) датчиком.

### Расположение компонента

Месторасположение варьируется в зависимости от OEM. См. руководство изготовителя машины по диагностике и ремонту.

### Практические замечания

Сопротивление всех датчиков давления изменяется в зависимости от давления. См. руководство по устранению неполадок и ремонту OEM для спецификаций.

См. Код устранения неполадок t05-298


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 298 (INDUSTRIAL)
>
> ### OEM Pressure Sensor Circuit
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 298 PID(P): S223 SPN: 1084 FMI: 4/4 Lamp: Yellow SRT: | Low voltage detected at the OEM pressure sensor signal pin of the 31-pin OEM connector. | No engine protection for OEM pressure. |
>
> OEM Pressure Sensor Circuit
>
> ### Circuit Description
>
> The OEM sensor signal is used by the ECM to monitor the OEM pressure. The OEM pressure is used by the ECM for the engine protection system. A sensor that has failed low can be caused by a short circuit to ground on the signal wire, or an internally grounded (faulty) sensor.
>
> ### Component Location
>
> The location varies with the OEM. Refer to the OEM troubleshooting and repair manual.
>
> ### Shoptalk
>
> The resistance of all pressure sensors varies with the pressure. Refer to the OEM troubleshooting and repair manual for specifications.
>
> Refer to Troubleshooting Fault Code t05-298
