---
aliases:
  - "Цепь датчика давления масла"
type: "Процедура"
doc: "82-fc135"
title_en: "Oil Pressure Sensor Circuit"
title_ru: "Цепь датчика давления масла"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc135.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc135.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# Oil Pressure Sensor Circuit
**Цепь датчика давления масла**

> [!abstract] Процедура · `82-fc135`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc135.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc135.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 135

### Цепь датчика давления масла

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 135 PID (P): P100 SPN: 100 FMI: 3/3 лампы: Желтая СТО: | Высокое напряжение, обнаруженное в цепи давления масла. | Отсутствие защиты двигателя от давления масла. |

![[19c00506.png]]

Цепь датчика давления масла

### Описание цепи

Датчик давления/температуры масла используется электронным модулем управления (ECM) для контроля давления моторного масла. ECM контролирует напряжение на контакте сигнала и преобразует его в значение давления. Значение давления масла используется ECM для системы защиты двигателя.

### Расположение компонента

Датчик давления/температуры масла расположен на блоке двигателя слева от топливного фильтра, позади воздушного компрессора.

### Практические замечания

Происходит ли это в холодную погоду? Если это так, то дайте маслу разогреться и посмотрите, не активируется ли разлом.

Устранение неполадок код t05-135


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 135
>
> ### Oil Pressure Sensor Circuit
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 135 PID(P): P100 SPN: 100 FMI: 3/3 Lamp: Yellow SRT: | High voltage detected at the oil pressure circuit. | No engine protection for oil pressure. |
>
> Oil Pressure Sensor Circuit
>
> ### Circuit Description
>
> The oil pressure/temperature sensor is used by the electronic control module (ECM) to monitor the lubricating oil pressure. The ECM monitors the voltage on the signal pin and converts this to a pressure value. The oil pressure value is used by the ECM for the engine protection system.
>
> ### Component Location
>
> The oil pressure/temperature sensor is located on the engine block to the left of the fuel filter, behind the air compressor.
>
> ### Shoptalk
>
> Does the fault occur **only** in cold weather? If so, allow the oil to warm up and see if the fault goes inactive.
>
> Refer to Troubleshooting Fault Code t05-135
