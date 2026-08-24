---
aliases:
  - "Цепь датчика температуры OEM"
type: "Процедура"
doc: "82-fc294"
title_en: "OEM Temperature Sensor Circuit"
title_ru: "Цепь датчика температуры OEM"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc294.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc294.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# OEM Temperature Sensor Circuit
**Цепь датчика температуры OEM**

> [!abstract] Процедура · `82-fc294`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc294.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc294.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 294 (ИНДУСТРИАЛ)

### Цепь датчика температуры OEM

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 294 PID(P): S154 SPN: 1083 FMI: 4/4 лампы: Желтая СТО: | Низкое напряжение, обнаруженное при контакте датчика температуры OEM с 31-контактным OEM-разъемом. | Отсутствие защиты двигателя от температуры OEM. |

![[19c00675.png]]

Цепь датчика температуры OEM

### Описание цепи

Сигнал датчика OEM используется электронным модулем управления (ECM) для мониторинга температуры OEM. Температура OEM используется ECM для системы защиты двигателя. Датчик, который вышел из строя с низким уровнем, может быть вызван коротким замыканием на землю на подаче или возвратном проводе или внутренне заземленном (неисправном) датчике.

### Расположение компонента

Месторасположение варьируется в зависимости от OEM. См. руководство изготовителя машины по диагностике и ремонту.

### Практические замечания

Сопротивление всех датчиков температуры изменяется в зависимости от температуры. Проверьте температурные пороги с помощью INSITETM.

См. Код устранения неполадок t05-294


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 294 (INDUSTRIAL)
>
> ### OEM Temperature Sensor Circuit
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 294 PID(P): S154 SPN: 1083 FMI: 4/4 Lamp: Yellow SRT: | Low voltage detected at the OEM temperature sensor signal pin of the 31-pin OEM connector. | No engine protection for OEM temperature. |
>
> OEM Temperature Sensor Circuit
>
> ### Circuit Description
>
> The OEM sensor signal is used by the electronic control module (ECM) to monitor the OEM temperature. The OEM temperature is used by the ECM for the engine protection system. A sensor that has failed low can be caused by a short circuit to ground on a supply or return wire, or an internally grounded (faulty) sensor.
>
> ### Component Location
>
> The location varies with the OEM. Refer to the OEM troubleshooting and repair manual.
>
> ### Shoptalk
>
> The resistance of all temperature sensors varies with the temperature. Check the temperature thresholds using INSITE™.
>
> Refer to Troubleshooting Fault Code t05-294
