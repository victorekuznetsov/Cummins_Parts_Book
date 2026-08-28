---
aliases:
  - "Цепь датчика частоты/положения — потеряны оба сигнала индуктивного датчика"
type: "Процедура"
doc: "01-fc115"
title_en: "Engine Speed/Position Sensor Circuit - Lost Both of Two Signals From the Magnetic Pickup Sensor"
title_ru: "Цепь датчика частоты/положения — потеряны оба сигнала индуктивного датчика"
modified: "2012-05-08"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc115.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc115.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Engine Speed/Position Sensor Circuit - Lost Both of Two Signals From the Magnetic Pickup Sensor
**Цепь датчика частоты/положения — потеряны оба сигнала индуктивного датчика**

> [!abstract] Процедура · `01-fc115`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-05-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc115.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc115.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 115

### Цепь датчика частоты/положения — потеряны оба сигнала индуктивного датчика

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 115 P(P): СПН: ФМИ: Лампа: Отключение SRT: | Сигнал о скорости двигателя не был обнаружен с датчиков основной и резервной скорости. | Двигатель выключен и может **не** работать. |

![[19803593.png]]

Цепь датчика частоты вращения двигателя

### Описание цепи

Датчик скорости двигателя представляет собой схему с двумя катушками, которая обеспечивает сигнал скорости двигателя к модулю управления двигателем (ECM) через электропроводку двигателя.

### Расположение компонента

Используйте следующую процедуру для определения местоположения компонентов. См. процедуру 100-002 в разделе E.

### Практические замечания

Если проблема возникает только при определенной температуре двигателя, обязательно проверьте схему датчика скорости двигателя, пока двигатель находится при этой конкретной температуре. Проверьте правильный воздушный зазор датчика скорости двигателя на зуб маховика.[[01-019-042 — Engine Speed Sensor (ESS)|См. процедуру 019-042 в разделе 19.]]. Некоторые датчики скорости могут использовать один разъем проводов DeutschTM вместо двух разъемов Weather-PackTM.

См. Код устранения неполадок t05-115.


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 115
>
> ### Engine Speed/Position Sensor Circuit - Lost Both of Two Signals From the Magnetic Pickup Sensor
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 115 PID(P): SPN: FMI: Lamp: Shutdown SRT: | No engine speed signal detected from the main and backup speed sensors. | Engine is shut down and can **not** be run. |
>
> Engine Speed Sensor Circuit
>
> ### Circuit Description
>
> The engine speed sensor is a dual-coil circuit that provides the engine speed signal to the engine control module (ECM) through the engine harness.
>
> ### Component Location
>
> Use the following procedure for component location. Refer to Procedure 100-002 in Section E.
>
> ### Shoptalk
>
> If the problem occurs **only** at a certain engine temperature, be sure to check the engine speed sensor circuit while the engine is at that particular temperature. Check for correct air gap of engine speed sensor to flywheel tooth. [[01-019-042 — Engine Speed Sensor (ESS)|Refer to Procedure 019-042 in Section 19]]. Some speed sensors can use a single Deutsch™ harness connector instead of the two Weather-Pack™ connectors.
>
> Refer to Troubleshooting Fault Code t05-115.
