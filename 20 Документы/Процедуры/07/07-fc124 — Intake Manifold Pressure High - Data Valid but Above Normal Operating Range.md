---
aliases:
  - "Высокое давление во впускном коллекторе — выше нормы"
type: "Процедура"
doc: "07-fc124"
title_en: "Intake Manifold Pressure High - Data Valid but Above Normal Operating Range"
title_ru: "Высокое давление во впускном коллекторе — выше нормы"
modified: "2012-12-18"
engines:
  - "93058669"
families:
  - "C8.3 · 6C8.3"
manuals:
  - "4021442"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-fc124.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/07-fc124.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "группа/07"
  - "перевод/машинный"
---

# Intake Manifold Pressure High - Data Valid but Above Normal Operating Range
**Высокое давление во впускном коллекторе — выше нормы**

> [!abstract] Процедура · `07-fc124`
> **Двигатели:** [[93058669 — 6C8.3 CPL 3105|93058669]]
> **Семейство:** C8.3 · 6C8.3
> **Входит в руководства:** [[4021442 — C8.3 Marine Electronic Control System Troubleshooting and Repair Manual|4021442]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-12-18
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-fc124.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/07-fc124.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 124

### Высокое давление во впускном коллекторе — выше нормы

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 124 PID(P): P102 SPN: 102 FMI: 16 ламп: Янтарная СРТ: | Давление впуска многообразия высокое - данные действительны, но выше нормального диапазона работы - умеренно тяжелый уровень. | Никаких действий. |

![[19900354.png]]

Цепь датчика давления во впускном коллекторе

### Описание цепи

Датчик давления впускного коллектора используется электронным модулем управления (ECM) для мониторинга давления впускного коллектора двигателя. ECM контролирует напряжение на контакте сигнала давления впускного коллектора и преобразует это в значение давления. Значение давления впускного коллектора используется ECM для системы защиты двигателя.

### Расположение компонента

Справочный раздел E для подробного описания местоположения компонента. Датчик давления впускного коллектора расположен рядом с нагревателем воздухозаборника за ECM.

### Практические замечания

Возможные причины:

- Неисправный турбонаддув турбины обходного клапана.[[41-010-050 — Turbocharger Wastegate Actuator|См. процедуру 010-050]]Руководство по устранению неполадок и ремонту, двигатели серии C, бюллетень 3666003.

- Неисправный датчик.

Устранение неполадок код t05-124


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 124
>
> ### Intake Manifold Pressure High - Data Valid but Above Normal Operating Range
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 124 PID(P): P102 SPN: 102 FMI: 16 Lamp: Amber SRT: | Intake manifold pressure high - data valid but above normal operating range - moderately severe level. | No action taken. |
>
> Intake Manifold Pressure Sensor Circuit
>
> ### Circuit Description
>
> The intake manifold pressure sensor is used by the electronic control module (ECM) to monitor the engine intake manifold pressure. The ECM monitors the voltage on the intake manifold pressure signal pin and converts this to a pressure value. The intake manifold pressure value is used by the ECM for the engine protection system.
>
> ### Component Location
>
> Reference Section E for a detailed component location view. The intake manifold pressure sensor is located next to the air intake heater behind the ECM.
>
> ### Shoptalk
>
> Possible causes:
>
> - Malfunctioning turbocharger wastegate. [[41-010-050 — Turbocharger Wastegate Actuator|Refer to Procedure 010-050]] in the Troubleshooting and Repair Manual, C Series Engines, Bulletin 3666003.
>
> - A faulty sensor.
>
> Refer to Troubleshooting Fault Code t05-124
