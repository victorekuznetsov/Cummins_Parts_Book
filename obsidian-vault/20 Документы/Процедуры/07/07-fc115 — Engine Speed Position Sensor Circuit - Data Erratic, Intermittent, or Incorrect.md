---
aliases:
  - "Цепь датчика частоты/положения — данные нестабильны или неверны"
type: "Процедура"
doc: "07-fc115"
title_en: "Engine Speed/Position Sensor Circuit - Data Erratic, Intermittent, or Incorrect"
title_ru: "Цепь датчика частоты/положения — данные нестабильны или неверны"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-fc115.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/07-fc115.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "группа/07"
  - "перевод/машинный"
---

# Engine Speed/Position Sensor Circuit - Data Erratic, Intermittent, or Incorrect
**Цепь датчика частоты/положения — данные нестабильны или неверны**

> [!abstract] Процедура · `07-fc115`
> **Двигатели:** [[93058669 — 6C8.3 CPL 3105|93058669]], [[93087701 — 6C8.3 CPL 3105|93087701]]
> **Семейство:** C8.3 · 6C8.3
> **Входит в руководства:** [[4021442 — C8.3 Marine Electronic Control System Troubleshooting and Repair Manual|4021442]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-12-18
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-fc115.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/07-fc115.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 115

### Цепь датчика частоты/положения — данные нестабильны или неверны

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 115 P(P): P190 SPN: 190 FMI: 2 лампы: Красная СТО: | Схема датчика скорости/положения двигателя потеряла два сигнала от магнитного датчика пикапа. Данные являются неустойчивыми, прерывистыми или неверными. Как первичные, так и вторичные датчики скорости являются датчиками эффекта Холла. | Двигатель умрет и не будет перезагружаться. |

![[19901358.png]]

Скорость двигателя / позиционная схема датчика

### Описание цепи

Основной датчик скорости двигателя обеспечивает сигнал скорости двигателя к электронному модулю управления (ECM) через электропроводку двигателя. Датчик генерирует сигнал, чувствуя движение зубьев-мишеней маховика.

### Расположение компонента

Основной датчик скорости двигателя расположен в корпусе маховика.

### Практические замечания

Датчик скорости двигателя обеспечивает основной сигнал скорости двигателя к ECM через проводку двигателя. Сигнал скорости двигателя генерируется, когда датчик скорости двигателя обнаруживает зубы на кольцевой передаче. ECM определяет скорость двигателя, подсчитывая количество переключателей напряжения за определенный период времени.

Устранение неполадок код t05-115


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 115
>
> ### Engine Speed/Position Sensor Circuit - Data Erratic, Intermittent, or Incorrect
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 115 PID(P): P190 SPN: 190 FMI: 2 Lamp: Red SRT: | Engine speed/position sensor circuit lost both of two signals from the magnetic pickup sensor. Data is erratic, intermittent, or incorrect. Both the primary and secondary speed sensors are hall effect sensors. | Engine will die and will **not** restart. |
>
> Engine Speed/Position Sensor Circuit
>
> ### Circuit Description
>
> The primary engine speed sensor provides the engine speed signal to the electronic control module (ECM) through the engine harness. The sensor generates a signal by sensing the movement of the target teeth of the flywheel.
>
> ### Component Location
>
> The primary engine speed sensor is located in the flywheel housing.
>
> ### Shoptalk
>
> The engine speed sensor provides the main engine speed signal to the ECM through the engine harness. The engine speed signal is generated when the engine speed sensor detects teeth on the ring gear. The ECM determines the engine speed by counting the number of voltage switches for a given period of time.
>
> Refer to Troubleshooting Fault Code t05-115
