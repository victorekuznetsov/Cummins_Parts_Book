---
aliases:
  - "Разнос двигателя (превышение частоты вращения)"
type: "Процедура"
doc: "87-fc234"
title_en: "Engine Overspeed"
title_ru: "Разнос двигателя (превышение частоты вращения)"
modified: "2010-07-29"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666214"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc234.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-fc234.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
  - "перевод/машинный"
---

# Engine Overspeed
**Разнос двигателя (превышение частоты вращения)**

> [!abstract] Процедура · `87-fc234`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc234.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-fc234.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 234

### Разнос двигателя (превышение частоты вращения)

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 234 PID(P): P190 SPN: 190 FMI: 0 лампочка: Красная СТО: | Сигнал скорости двигателя на контакте 17 и/или контакте 9 с электропроводкой двигателя, указанной в ремне, указывает, что скорость двигателя больше калиброванного значения (2650 об/мин). | EHAB (запорный клапан) обесточен (закрыт). EHAB (запорный клапан) восстанавливается (открывается), когда скорость двигателя падает ниже калиброванного значения (2130 об/мин). |

![[19a00572.png]]

Цепь датчика частоты вращения двигателя

### Описание цепи

Датчик скорости двигателя контролирует положение двигателя и скорость двигателя и передает эту информацию электронному модулю управления (ECM) через электропроводку двигателя.

### Расположение компонента

Датчик скорости двигателя и датчик положения двигателя расположены в корпусе маховика.

### Практические замечания

- Проверить впускной коллектор на наличие источников легковоспламеняющихся паров. Проверьте уплотнения турбокомпрессора, чтобы убедиться, что нет утечек масла.

- Проверьте датчик скорости двигателя на наличие признаков повреждения или подделки.

См. Код устранения неполадок t05-234


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 234
>
> ### Engine Overspeed
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 234 PID(P): P190 SPN: 190 FMI: 0 Lamp: Red SRT: | Engine speed signal on pin 17 and/or pin 9 of the engine harness indicated engine speed is greater than the calibrated value (2650 rpm). | The EHAB (fuel shutoff valve) is de-energized (closed). The EHAB (fuel shutoff valve) is reenergized (opened) when engine speed falls below the calibrated value (2130 rpm). |
>
> Engine Speed Sensor Circuit
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
