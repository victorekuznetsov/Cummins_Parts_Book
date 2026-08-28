---
type: "Процедура"
doc: "81-fc694"
title_en: "Turbocharger 2 Compressor Intake Temperature Circuit - Voltage Above Normal or Shorted to High Source"
modified: "2015-07-07"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
families:
  - "QSK60"
manuals:
  - "3666410"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/81/81-fc694.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/81-fc694.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK60"
  - "группа/81"
  - "перевод/машинный"
---

# Turbocharger 2 Compressor Intake Temperature Circuit - Voltage Above Normal or Shorted to High Source

> [!abstract] Процедура · `81-fc694`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]]
> **Семейство:** QSK60
> **Входит в руководства:** [[3666410 — QSK45 and QSK60 CENSE™ Electronic Control System Troubleshooting and Repair Manual|3666410]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2015-07-07
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/81/81-fc694.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/81-fc694.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 694

### Турбокомпрессор 2 Тормозная схема поглощения - напряжение выше нормального или короткое до высокого источника

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 694 PID(P): СПН: 1173 ФМИ: 3 лампы: Нет, не srt: 00-513 | Турбокомпрессор 2 Компрессорная схема поглощения температуры - напряжение выше нормального или короткое до высокого источника. Высокое напряжение, обнаруженное на контакте SIGNAL 15 основной проводов ремня разъема A ECM. | Код 616 неисправности отключен. |

![[19802519.png]]

Левобережный задний турбокомпрессор Впускной датчик температуры

### Описание цепи

Датчик температуры входного впуска заднего турбонагнетателя левого берега обеспечивает температуру входного впуска заднего турбокомпрессора в ECM. Сопротивление датчика варьируется в зависимости от температуры. ECM обнаруживает изменение сопротивления датчика, контролируя напряжение на внутреннем резисторе, который последовательно с датчиком. Изменение напряжения на внутреннем резисторе переводится в изменение температуры.

### Расположение компонента

Датчик температуры входного впуска турбокомпрессора левого берега расположен на заднем входном впуске турбокомпрессора левого берега.

### Практические замечания

- Сопротивление датчика изменяется в зависимости от температуры. Считывание, которое вы наблюдаете, должно быть сопоставимо со следующей таблицей, если датчик работает должным образом.

| температура | температура | Сопротивление |
|---|---|---|
| (°C) | (°F) | (Омс) |
| 0 | 32 | 30k до 36k |
| 25 | 77 | 9k до 11k |
| 50 | 122 | 3k - 4k |
| 75 | 167 | 1350—1500 |
| 100 | 212 | 600-675 |

Устранение неполадок код t05-694


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 694
>
> ### Turbocharger 2 Compressor Intake Temperature Circuit - Voltage Above Normal or Shorted to High Source
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 694 PID(P): SPN: 1173 FMI: 3 Lamp: None SRT: 00-513 | Turbocharger 2 Compressor Intake Temperature Circuit - Voltage Above Normal or Shorted to High Source. High voltage detected on SIGNAL pin 15 of the main harness A ECM connector. | Fault Code 616 is disabled. |
>
> Left Bank Rear Turbocharger Compressor Inlet Temperature Sensor Circuit
>
> ### Circuit Description
>
> The left bank rear turbocharger compressor inlet temperature sensor provides the left bank rear turbocharger compressor inlet temperature to the ECM. The resistance of the sensor varies with temperature. The ECM detects the change in resistance of the sensor by monitoring the voltage across an internal resistor that is in series with the sensor. The change in voltage across the internal resistor is translated into a temperature change.
>
> ### Component Location
>
> The left bank rear turbocharger compressor inlet temperature sensor is located on the left bank rear turbocharger inlet.
>
> ### Shoptalk
>
> - The resistance of the sensor varies with the temperature. The reading that you observe should compare to the following table if the sensor is functioning properly.
>
> | Temperature | Temperature | Resistance |
> |---|---|---|
> | (°C) | (°F) | (ohms) |
> | 0 | 32 | 30k to 36k |
> | 25 | 77 | 9k to 11k |
> | 50 | 122 | 3k to 4k |
> | 75 | 167 | 1350 to 1500 |
> | 100 | 212 | 600 to 675 |
>
> Refer to Troubleshooting Fault Code t05-694
