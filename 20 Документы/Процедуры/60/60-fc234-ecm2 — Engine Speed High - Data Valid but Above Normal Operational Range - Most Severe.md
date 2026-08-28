---
aliases:
  - "Высокая частота вращения — выше нормы — наивысший уровень"
type: "Процедура"
doc: "60-fc234-ecm2"
title_en: "Engine Speed High - Data Valid but Above Normal Operational Range - Most Severe Level"
title_ru: "Высокая частота вращения — выше нормы — наивысший уровень"
modified: "2018-06-19"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021674"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc234-ecm2.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-fc234-ecm2.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
  - "перевод/машинный"
---

# Engine Speed High - Data Valid but Above Normal Operational Range - Most Severe Level
**Высокая частота вращения — выше нормы — наивысший уровень**

> [!abstract] Процедура · `60-fc234-ecm2`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section TF — Troubleshooting Fault Codes
> **Даты:** изменён 2018-06-19
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc234-ecm2.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-fc234-ecm2.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 234-ECM2

### Высокая частота вращения — выше нормы — наивысший уровень

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 234 PID(P): СПН: 190 FMI: 0 лампочка: Красная СТО: | Высокая частота вращения — выше нормы — наивысший уровень | Запорный клапан топлива обесточен (закрыт). Запорный клапан топлива повторно активируется (открывается), когда скорость двигателя падает ниже калиброванного значения (2130 об/мин). |

![[19a00863.png]]

Высокоскоростной движок QST30 Power Generation Interface Engine

### Описание цепи

Датчик скорости двигателя контролирует положение двигателя и скорость двигателя и передает эту информацию электронному модулю управления (ECM) через электропроводку двигателя.

### Расположение компонента

Датчик скорости двигателя и датчик положения двигателя расположены в корпусе маховика.

### Практические замечания

- Проверить впускной коллектор на наличие источников легковоспламеняющихся паров. Проверьте уплотнения турбокомпрессора, чтобы убедиться, что нет утечек масла.

- Проверьте датчик скорости двигателя на наличие признаков повреждения или подделки.

См. Код устранения неполадок t05-234


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 234-ECM2
>
> ### Engine Speed High - Data Valid but Above Normal Operational Range - Most Severe Level
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 234 PID(P): SPN: 190 FMI: 0 Lamp: Red SRT: | Engine Speed High - Data Valid but Above Normal Operational Range - Most Severe Level | The fuel shutoff valve is de-energized (closed). The fuel shutoff valve is re-engergized (opened) when engine speed falls below the calibrated value (2130 rpm). |
>
> Engine Speed High Circuit - QST30 Power Generation Interface Engine
>
> ### Circuit Description
>
> The engine speed sensor monitors the engine position and the engine speed and passes this information to the electronic control module (ECM) through the engine harness.
>
> ### Component Location
>
> The engine speed sensor and the engine position sensor are located in the flywheel housing.
>
> ### Shoptalk
>
> - Inspect the intake manifold for sources of flammable vapors. Check the turbocharger seals to verify that there are no oil leaks.
>
> - Inspect the engine speed sensor for signs of damage or tampering.
>
> Refer to Troubleshooting Fault Code t05-234
