---
aliases:
  - "Цепь датчика давления масла — напряжение выше нормы"
type: "Процедура"
doc: "07-fc135"
title_en: "Oil Pressure Sensor Circuit - Voltage Above Normal or Shorted to High Source"
title_ru: "Цепь датчика давления масла — напряжение выше нормы"
modified: "2012-12-18"
engines:
  - "93058669"
  - "93087701"
families:
  - "C8.3 · 6C8.3"
manuals:
  - "4021442"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-fc135.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/07-fc135.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "группа/07"
  - "перевод/машинный"
---

# Oil Pressure Sensor Circuit - Voltage Above Normal or Shorted to High Source
**Цепь датчика давления масла — напряжение выше нормы**

> [!abstract] Процедура · `07-fc135`
> **Двигатели:** [[93058669 — 6C8.3 CPL 3105|93058669]], [[93087701 — 6C8.3 CPL 3105|93087701]]
> **Семейство:** C8.3 · 6C8.3
> **Входит в руководства:** [[4021442 — C8.3 Marine Electronic Control System Troubleshooting and Repair Manual|4021442]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-12-18
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-fc135.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/07-fc135.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 135

### Цепь датчика давления масла — напряжение выше нормы

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 135 PID (P): P100 SPN: 100 FMI: 3 лампы: Янтарная СРТ: | Цепь датчика давления масла — напряжение выше нормы. | Защита двигателя от давления масла отключена. |

![[19a00194.png]]

Цепь датчика давления масла

### Описание цепи

Датчик давления масла контролирует давление масла и передает информацию в электронный модуль управления (ECM) через контакт сигнала давления масла в проводах двигателя. ECM контролирует напряжение на контакте сигнала давления масла. Напряжение, превышающее контрольный порог, будет превышать код 135 по умолчанию.

### Расположение компонента

Справочный раздел E для подробного описания местоположения компонента. Датчик давления масла расположен между фильтром охлаждающей жидкости и соленоидами нагревателя.

### Практические замечания

Если неисправность возникает только в холодную погоду, позвольте маслу прогреться и посмотрите, не активизируется ли неисправность.

Если код 143 или 415 неисправности присутствует, проблема связана с базовым двигателем.

Устранение неполадок код t05-135


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 135
>
> ### Oil Pressure Sensor Circuit - Voltage Above Normal or Shorted to High Source
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 135 PID(P): P100 SPN: 100 FMI: 3 Lamp: Amber SRT: | Oil pressure sensor circuit - voltage above normal or shorted to high source. | Engine protection for oil pressure disabled. |
>
> Oil Pressure Sensor Circuit
>
> ### Circuit Description
>
> The oil pressure sensor monitors oil pressure and passes information to the electronic control module (ECM) through the oil pressure signal pin of the engine harness. The ECM monitors the voltage on the oil pressure signal pin. Voltage exceeding the control threshold will trip Fault Code 135.
>
> ### Component Location
>
> Reference Section E for a detailed component location view. The oil pressure sensor is located between the coolant filter and the heater solenoids.
>
> ### Shoptalk
>
> If the fault occurs **only** in cold weather, allow the oil to warm up and see if the fault goes inactive.
>
> If Fault Code 143 or 415 is **not** present, the problem is **not** base engine related.
>
> Refer to Troubleshooting Fault Code t05-135
