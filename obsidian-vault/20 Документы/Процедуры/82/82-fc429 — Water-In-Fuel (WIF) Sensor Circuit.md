---
aliases:
  - "Цепь датчика воды в топливе (WIF)"
type: "Процедура"
doc: "82-fc429"
title_en: "Water-In-Fuel (WIF) Sensor Circuit"
title_ru: "Цепь датчика воды в топливе (WIF)"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc429.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc429.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# Water-In-Fuel (WIF) Sensor Circuit
**Цепь датчика воды в топливе (WIF)**

> [!abstract] Процедура · `82-fc429`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc429.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc429.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 429

### Цепь датчика воды в топливе (WIF)

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 429 PID(P): P097 SPN: 97 ФМИ: 4/4 лампы: Желтая СТО: | Низкое напряжение, обнаруженное в цепи датчика воды в топливе (WIF). | Ни одного на выступление. |

![[19c00273.png]]

WIF Sensor Circuit

### Описание цепи

Датчик WIF прикреплен к топливному фильтру. Датчик WIF посылает сигнал электронному модулю управления (ECM), когда в топливном фильтре накопился заданный объем воды. Схема WIF содержит два провода: Возвратный заземление (контакт 10) и сигнальный провод (контакт 9).

### Расположение компонента

Датчик WIF установлен в топливном фильтре и расположен на боковой стороне головки примерно на среднем двигателе.

### Практические замечания

Датчик WIF использует тот же внутренний источник питания ECM, что и датчики на ремне электропроводки двигателя. Если код 352 ошибки также активен, используйте эту логику устранения неполадок и дерево.

См. Код устранения неполадок t05-429


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 429
>
> ### Water-In-Fuel (WIF) Sensor Circuit
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 429 PID(P): P097 SPN: 97 FMI: 4/4 Lamp: Yellow SRT: | Low voltage detected at water-in-fuel (WIF) sensor circuit. | None on performance. |
>
> WIF Sensor Circuit
>
> ### Circuit Description
>
> The WIF sensor is attached to the fuel filter. The WIF sensor sends a signal to the electronic control module (ECM) when a set volume of water has accumulated in the fuel filter. The WIF circuit contains two wires: A return ground (pin 10) and a signal wire (pin 9).
>
> ### Component Location
>
> The WIF sensor is installed in the fuel filter and is located on the side of the head approximately midengine.
>
> ### Shoptalk
>
> The WIF sensor uses the same internal ECM power supply as sensors on engine harness. If Fault Code 352 is also active, use that troubleshooting logic and tree.
>
> Refer to Troubleshooting Fault Code t05-429
