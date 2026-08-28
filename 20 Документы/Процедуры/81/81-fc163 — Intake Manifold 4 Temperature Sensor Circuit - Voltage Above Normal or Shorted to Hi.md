---
type: "Процедура"
doc: "81-fc163"
title_en: "Intake Manifold 4 Temperature Sensor Circuit - Voltage Above Normal or Shorted to High Source"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/81/81-fc163.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/81-fc163.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK60"
  - "группа/81"
  - "перевод/машинный"
---

# Intake Manifold 4 Temperature Sensor Circuit - Voltage Above Normal or Shorted to High Source

> [!abstract] Процедура · `81-fc163`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]]
> **Семейство:** QSK60
> **Входит в руководства:** [[3666410 — QSK45 and QSK60 CENSE™ Electronic Control System Troubleshooting and Repair Manual|3666410]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2015-07-07
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/81/81-fc163.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/81-fc163.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 163

### 4-х температурный датчик: напряжение выше нормального или короткое до высокого источника

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 163 P(P): 105 SPN: 1133 FMI: 3 лампы: Желтая СТО: 00-698 | 4-х градусная схема датчика поглощения - напряжение выше нормального или короткое к высокому источнику. Высокое напряжение, обнаруженное на контакте SIGNAL 14 основной проводов ремня разъема A ECM. | Код 165 неисправности отключен. |

![[19800871.png]]

Right Bank Rear Intake Manifold Температурный датчик

### Описание цепи

Схема датчика температуры заднего впускного коллектора правого берега обеспечивает сигнал температуры воздуха заднего впуска правого берега для ECM. Сопротивление датчика варьируется в зависимости от температуры. ECM обнаруживает изменение сопротивления датчика, контролируя напряжение на внутреннем резисторе, который последовательно с датчиком. Изменение напряжения на внутреннем резисторе переводится в изменение температуры.

### Расположение компонента

Датчик температуры заднего впускного коллектора правого берега расположен на заднем впускном коллекторе правого берега. Датчик расположен ниже по течению от послеохладителя.

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

Устранение неполадок код t05-163


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 163
>
> ### Intake Manifold 4 Temperature Sensor Circuit - Voltage Above Normal or Shorted to High Source
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 163 PID(P): 105 SPN: 1133 FMI: 3 Lamp: Yellow SRT: 00-698 | Intake Manifold 4 Temperature Sensor Circuit - Voltage Above Normal or Shorted to High Source. High voltage detected on SIGNAL pin 14 of the main harness A ECM connector. | Fault Code 165 is disabled. |
>
> Right Bank Rear Intake Manifold Temperature Sensor Circuit
>
> ### Circuit Description
>
> The right bank rear intake manifold temperature sensor circuit provides the right bank rear intake air temperature signal to the ECM. The resistance of the sensor varies with temperature. The ECM detects the change in resistance of the sensor by monitoring the voltage across an internal resistor that is in series with the sensor. The change in voltage across the internal resistor is translated into a temperature change.
>
> ### Component Location
>
> The right bank rear intake manifold temperature sensor is located on the right bank rear intake manifold. The sensor is located downstream of the aftercooler.
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
> Refer to Troubleshooting Fault Code t05-163
