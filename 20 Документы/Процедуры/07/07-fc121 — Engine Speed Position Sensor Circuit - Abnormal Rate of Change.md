---
aliases:
  - "Цепь датчика частоты/положения — недопустимая скорость изменения"
type: "Процедура"
doc: "07-fc121"
title_en: "Engine Speed/Position Sensor Circuit - Abnormal Rate of Change"
title_ru: "Цепь датчика частоты/положения — недопустимая скорость изменения"
modified: "2012-12-18"
engines:
  - "93058669"
families:
  - "C8.3 · 6C8.3"
manuals:
  - "4021442"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-fc121.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/07-fc121.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "группа/07"
  - "перевод/машинный"
---

# Engine Speed/Position Sensor Circuit - Abnormal Rate of Change
**Цепь датчика частоты/положения — недопустимая скорость изменения**

> [!abstract] Процедура · `07-fc121`
> **Двигатели:** [[93058669 — 6C8.3 CPL 3105|93058669]]
> **Семейство:** C8.3 · 6C8.3
> **Входит в руководства:** [[4021442 — C8.3 Marine Electronic Control System Troubleshooting and Repair Manual|4021442]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-12-18
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-fc121.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/07-fc121.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 121

### Цепь датчика частоты/положения — недопустимая скорость изменения

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 121 PID(P): P190 SPN: 190 FMI: 10 ламп: Янтарная СРТ: | Схема датчика скорости/положения двигателя потеряла один из двух сигналов от магнитного датчика пикапа — аномальную скорость изменения. Как первичные, так и вторичные датчики скорости являются датчиками эффекта Холла. | Потеря резервного датчика скорости двигателя. Никаких действий со стороны ЕКМ не предпринимается. |

![[19901358.png]]

Скорость двигателя / позиционная схема датчика

### Описание цепи

Вторичный датчик скорости двигателя обеспечивает резервный сигнал скорости двигателя к электронному модулю управления (ECM) через электропроводку двигателя. Датчик генерирует сигнал, чувствуя движение зубьев-мишеней маховика.

### Расположение компонента

Вторичная датчик скорости двигателя расположена в корпусе маховика.

### Практические замечания

Датчик скорости двигателя обеспечивает основной сигнал скорости двигателя к ECM через проводку двигателя. Сигнал скорости двигателя генерируется, когда датчик скорости двигателя обнаруживает зубы на кольцевой передаче. ECM определяет скорость двигателя, подсчитывая количество переключателей напряжения за определенный период времени.

См. Код устранения неполадок t05-121


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 121
>
> ### Engine Speed/Position Sensor Circuit - Abnormal Rate of Change
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 121 PID(P): P190 SPN: 190 FMI: 10 Lamp: Amber SRT: | Engine speed/position sensor circuit lost one of two signals from the magnetic pickup sensor - abnormal rate of change. Both the primary and secondary speed sensors are hall effect sensors. | Loss of backup engine speed sensor. No action by the ECM is taken. |
>
> Engine Speed/Position Sensor Circuit
>
> ### Circuit Description
>
> The secondary engine speed sensor provides a backup engine speed signal to the electronic control module (ECM) through the engine harness. The sensor generates a signal by sensing the movement of the target teeth of the flywheel.
>
> ### Component Location
>
> The secondary engine speed sensor is located in the flywheel housing.
>
> ### Shoptalk
>
> The engine speed sensor provides the main engine speed signal to the ECM through the engine harness. The engine speed signal is generated when the engine speed sensor detects teeth on the ring gear. The ECM determines the engine speed by counting the number of voltage switches for a given period of time.
>
> Refer to Troubleshooting Fault Code t05-121
