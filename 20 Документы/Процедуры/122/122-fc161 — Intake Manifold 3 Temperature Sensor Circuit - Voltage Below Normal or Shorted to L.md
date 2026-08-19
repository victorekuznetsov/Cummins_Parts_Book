---
aliases:
  - "Цепь датчика температуры коллектора 3 — напряжение ниже нормы"
type: "Процедура"
doc: "122-fc161"
title_en: "Intake Manifold 3 Temperature Sensor Circuit - Voltage Below Normal or Shorted to Low Source"
title_ru: "Цепь датчика температуры коллектора 3 — напряжение ниже нормы"
modified: "2015-09-03"
engines:
  - "33239746"
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
manuals:
  - "4022102"
figures: 3
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-fc161.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/122-fc161.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/122"
  - "перевод/машинный"
---

# Intake Manifold 3 Temperature Sensor Circuit - Voltage Below Normal or Shorted to Low Source
**Цепь датчика температуры коллектора 3 — напряжение ниже нормы**

> [!abstract] Процедура · `122-fc161`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Входит в руководства:** [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M|4022102]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2015-09-03
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-fc161.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/122-fc161.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 161

### Цепь датчика температуры коллектора 3 — напряжение ниже нормы

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 161 PID(P): СПН: 1132 FMI: 4/4 лампы: Янтарная СРТ: | Цепь датчика температуры коллектора 3 — напряжение ниже нормы. Низкое напряжение сигнала, обнаруженное в впускном коллекторе 3 температурной цепи. | Возможен белый дым. Вентилятор останется включенным, если он будет контролироваться ECM. ** Нет** Защита двигателя от температуры впускного коллектора. |

![[19601969.png]]

QSK38 CM2150 Industrial - Впускной коллектор 3 с температурным датчиком

![[19602280.png]]

QSK50 CM2150 Power Generation с усовершенствованным мониторингом двигателя - схема впуска коллектора 3 с датчиком температуры

![[19601970.png]]

QSK50 и QSK60 CM2150 Industrial/QSK50 и QSK60 CM2150 Marine/QSK60 CM2150 Drill Rig - Intake Manifold 3 Temperature Sensor Circuit

### Описание цепи

Датчик температуры впускного коллектора 3 контролирует температуру воздуха впускного коллектора и передает информацию модулям управления двигателем (ECM) через электропроводку двигателя.

### Расположение компонента

Датчик температуры впускного коллектора 3 расположен в левобережном заднем коллекторе воздухозаборника. См. процедуру 100-002 в разделе E Руководства по обслуживанию K38, K50, QSK38 и QSK50, Бюллетень 4021528, для подробного обзора местоположения компонентов.

### Практические замечания

У моделей двигателей, охваченных этим руководством, несколько электронных блоков управления. У каждого блока управления свой адрес источника, который отображается при подключении INSITE™. При поиске неисправности по коду определяйте затронутый блок управления и цепь по адресу источника, который показывает INSITE™.

Впускной коллектор 3 датчика температуры делит провода возврата в ремне проводов двигателя с другими датчиками. Открытия и шорты в ремне проводов двигателя могут привести к активации нескольких кодов неисправностей. Сначала проверьте коды ошибок с несколькими счетами.

Возможные причины этого кода неисправности:

- Схема сигнала закорочена до земли в проводной упряжке.

- Схема сигнала закорочена, чтобы вернуться или заземлиться в датчике.

| Температура (°C) | Температура \[°F\] | Сопротивление (Омс) |
|---|---|---|
| 0 | 32 | 29k до 36k |
| 25 | 77 | 9k до 11k |
| 40 | 104 | 4,9k до 5,8k |
| 100 | 212 | 600-700 |

См. код 161 устранения неполадок.


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 161
>
> ### Intake Manifold 3 Temperature Sensor Circuit - Voltage Below Normal or Shorted to Low Source
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 161 PID(P): SPN: 1132 FMI: 4/4 Lamp: Amber SRT: | Intake Manifold 3 Temperature Sensor Circuit - Voltage Below Normal or Shorted to Low Source. Low signal voltage detected at intake manifold 3 temperature circuit. | Possible white smoke. Fan will stay ON if controlled by the ECM. **No** engine protection for intake manifold temperature. |
>
> QSK38 CM2150 Industrial - Intake Manifold 3 Temperature Sensor Circuit
>
> QSK50 CM2150 Power Generation with Advanced Engine Monitoring - Intake Manifold 3 Temperature Sensor Circuit
>
> QSK50 and QSK60 CM2150 Industrial/QSK50 and QSK60 CM2150 Marine/QSK60 CM2150 Drill Rig - Intake Manifold 3 Temperature Sensor Circuit
>
> ### Circuit Description
>
> The intake manifold 3 temperature sensor monitors intake manifold air temperature and passes information to the engine control modules (ECMs) through the engine harness.
>
> ### Component Location
>
> The intake manifold 3 temperature sensor is located in the left bank rear air intake manifold. Refer to Procedure 100-002 in Section E of the K38, K50, QSK38, and QSK50 Service Manual, Bulletin 4021528, for a detailed component location view.
>
> ### Shoptalk
>
> There are multiple ECMs for the engine models included in this manual. Each ECM has an individual source address that displays when INSITE™ electronic service tool is connected. When troubleshooting a fault code, use the source address displayed in INSITE™ electronic service tool to determine which ECM and circuit is affected.
>
> The intake manifold 3 temperature sensor shares return wires in the engine harness with other sensors. Opens and shorts in the engine harness can cause multiple fault codes to be active. Check fault codes with multiple counts first.
>
> Possible causes of this fault code include:
>
> - Signal circuit shorted to ground in the harness.
>
> - Signal circuit shorted to return or ground in the sensor.
>
> | Temperature (°C) | Temperature \[°F\] | Resistance (ohms) |
> |---|---|---|
> | 0 | 32 | 29k to 36k |
> | 25 | 77 | 9k to 11k |
> | 40 | 104 | 4.9k to 5.8k |
> | 100 | 212 | 600 to 700 |
>
> Refer to Troubleshooting Fault Code 161.
