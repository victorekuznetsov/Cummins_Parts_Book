---
aliases:
  - "Цепь датчика частоты/положения — потеря сигнала"
type: "Процедура"
doc: "01-fc236"
title_en: "Engine Speed/Position Sensor Circuit - Loss of Signal"
title_ru: "Цепь датчика частоты/положения — потеря сигнала"
modified: "2010-07-29"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc236.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc236.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Engine Speed/Position Sensor Circuit - Loss of Signal
**Цепь датчика частоты/положения — потеря сигнала**

> [!abstract] Процедура · `01-fc236`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc236.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc236.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 236

### Цепь датчика частоты/положения — потеря сигнала

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 236 P(P): СПН: ФМИ: Лампа: Отключение SRT: | Сигнал датчика скорости двигателя/положения не обнаруживается. | Двигатель отключится. |

![[19802445.png]]

Скорость двигателя / позиционные сенсорные схемы

### Описание цепи

Датчик положения коленчатого вала и распредвала двигателя обеспечивает информацию о скорости двигателя и положении электронному модулю управления (ECM) через жгут проводов двигателя.

### Расположение компонента

См. схемы двигателя. 100-002 для расположения компонентов.

### Практические замечания

Возможные причины этого кода неисправности включают поврежденный датчик положения двигателя распределительного вала, открытый или короткое замыкание и отказ напряжения питания.

См. Код устранения неполадок t05-236


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 236
>
> ### Engine Speed/Position Sensor Circuit - Loss of Signal
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 236 PID(P): SPN: FMI: Lamp: Shutdown SRT: | Engine speed/position sensors signal is **not** detected. | Engine will shut down. |
>
> Engine Speed/Position Sensor Circuits
>
> ### Circuit Description
>
> The crankshaft and camshaft engine position sensor provides engine speed and position information to the electronic control module (ECM) through the engine harness.
>
> ### Component Location
>
> Refer to the Engine Diagrams. 100-002 for the component location.
>
> ### Shoptalk
>
> Possible causes of this fault code include damaged camshaft engine position sensor, open or shorted circuit, and power supply voltage failure.
>
> Refer to Troubleshooting Fault Code t05-236
