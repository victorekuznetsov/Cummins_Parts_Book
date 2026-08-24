---
aliases:
  - "Цепь датчика положения коленчатого вала"
type: "Процедура"
doc: "82-fc121"
title_en: "Engine Position Sensor Circuit"
title_ru: "Цепь датчика положения коленчатого вала"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc121.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc121.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# Engine Position Sensor Circuit
**Цепь датчика положения коленчатого вала**

> [!abstract] Процедура · `82-fc121`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc121.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc121.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 121

### Цепь датчика положения коленчатого вала

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 121 PID(P): P190 SPN: 190 FMI: 10/10 лампа: Желтая СТО: | Сигнал о скорости двигателя не был обнаружен в одной из цепей датчика положения двигателя. | Ни одного на выступление. |

![[19200127.png]]

Цепь датчика положения коленчатого вала

### Описание цепи

Датчик положения двигателя контролирует положение двигателя и скорость двигателя и передает эту информацию электронному модулю управления (ECM) через датчик проводов ремня.

### Расположение компонента

Датчик положения двигателя расположен над вспомогательным приводом.

### Практические замечания

- Если неисправность возникает только при определенной температуре двигателя, проверьте схему датчика положения двигателя, пока двигатель находится при этой конкретной температуре.

- Проверьте осевой зазор распределительного вала, чтобы убедиться, что передача распределительного вала ** не ** движется слишком далеко от конца датчика положения двигателя.

- Проверьте влажность в разъёме датчика проводов жгута проводов на ECM.

- Возможные причины этой неисправности включают поврежденный датчик положения двигателя, короткое замыкание на землю или открытую цепь.

См. Код устранения неполадок t05-121


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 121
>
> ### Engine Position Sensor Circuit
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 121 PID(P): P190 SPN: 190 FMI: 10/10 Lamp: Yellow SRT: | No engine speed signal detected at one of the engine position sensor circuits. | None on performance. |
>
> Engine Position Sensor Circuit
>
> ### Circuit Description
>
> The engine position sensor monitors the engine position and the engine speed and passes this information to the electronic control module (ECM) through the sensor harness.
>
> ### Component Location
>
> The engine position sensor is located above the accessory drive.
>
> ### Shoptalk
>
> - If the fault occurs **only** at a certain engine temperature, check the engine position sensor circuit while the engine is at that particular temperature.
>
> - Check the camshaft end play to make sure the camshaft gear is **not** moving too far away from the end of the engine position sensor.
>
> - Check for moisture in the sensor harness connector at the ECM.
>
> - Possible causes for this fault include a damaged engine position sensor, a short circuit to ground, or an open circuit.
>
> Refer to Troubleshooting Fault Code t05-121
