---
aliases:
  - "Цепь питания электромагнита отсечки топлива"
type: "Процедура"
doc: "82-fc255"
title_en: "Fuel Shutoff Solenoid Supply Circuit"
title_ru: "Цепь питания электромагнита отсечки топлива"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc255.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc255.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# Fuel Shutoff Solenoid Supply Circuit
**Цепь питания электромагнита отсечки топлива**

> [!abstract] Процедура · `82-fc255`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc255.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc255.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 255

### Цепь питания электромагнита отсечки топлива

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 255 PID (P): S017 SPN: 632 FMI: 3/3 лампы: Желтая СТО: | Внешне подаваемое напряжение, обнаруженное для отключения цепи подачи соленоидов. | Ни одного на выступление. Запорный клапан остается включенным. |

![[19c00264.png]]

Схема отключения топлива

### Описание цепи

Если напряжение подается наружу в клапан отключения топлива, он останется открытым.

### Расположение компонента

Соленоид отключения топлива расположен на корпусе топливного насоса вблизи линии розетки топлива. В неустановленных более ранних версиях использовался специальный обратный провод (контакт 32), который крепится к одному из выключенных соленоидных крепежных болтов. В новых моделях используется только  провод отключения подачи топлива (контакт 33).

### Практические замечания

Если на транспортном средстве установлена внешняя система отключения, убедитесь, что она **не** неправильно подключена и питает напряжение в цепи подачи топлива.

См. Код устранения неполадок t05-255


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 255
>
> ### Fuel Shutoff Solenoid Supply Circuit
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 255 PID(P): S017 SPN: 632 FMI: 3/3 Lamp: Yellow SRT: | Externally supplied voltage detected going to fuel shutoff solenoid supply circuit. | None on performance. Fuel shutoff valve stays on. |
>
> Fuel Shutoff Circuit
>
> ### Circuit Description
>
> If voltage is externally supplied to the fuel shutoff valve, it will stay open.
>
> ### Component Location
>
> The fuel shutoff solenoid is located on the fuel pump housing near the fuel outlet line. Unspecified earlier versions used a dedicated return wire (pin 32) that is mounted to one of the shutoff solenoid mounting bolts. Newer models use **only** a fuel shutoff supply wire (pin 33).
>
> ### Shoptalk
>
> If there is an external shutdown system on the vehicle, make sure it is **not** wired incorrectly and feeding voltage into the fuel shutoff supply circuit.
>
> Refer to Troubleshooting Fault Code t05-255
