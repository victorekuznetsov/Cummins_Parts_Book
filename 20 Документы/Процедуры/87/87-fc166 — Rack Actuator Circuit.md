---
aliases:
  - "Цепь привода рейки"
type: "Процедура"
doc: "87-fc166"
title_en: "Rack Actuator Circuit"
title_ru: "Цепь привода рейки"
modified: "2010-07-29"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666214"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc166.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-fc166.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
  - "перевод/машинный"
---

# Rack Actuator Circuit
**Цепь привода рейки**

> [!abstract] Процедура · `87-fc166`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc166.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-fc166.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 166

### Цепь привода рейки

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 166 PID (P): S024 SPN: 733 FMI: 3 лампы: Желтая СТО: | Отзывы привода стойки, измеренные электронным модулем управления (ECM), больше, чем калиброванное значение. | Никаких действий со стороны ЕКМ не предпринимается. |

![[19a00103.png]]

Цепь привода рейки

### Описание цепи

Реечный привод снабжен переменным источником тока от ECM. Редуктор стойки использует этот ток для изменения положения управляющей стойки, которая регулирует количество топлива, подаваемого от топливного насоса. Датчик обратной связи положения стойки ретранслирует положение стойки привода обратно в ECM.

### Расположение компонента

Реечный привод является неотъемлемой частью топливного насоса RP39.

### Практические замечания

- Подтвердите, что разъем привода прочно на месте.

- Когда нет питания на приводе, привод закрывается и поток топлива останавливается.

Устранение неполадок код t05-166


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 166
>
> ### Rack Actuator Circuit
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 166 PID(P): S024 SPN: 733 FMI: 3 Lamp: Yellow SRT: | The rack actuator feedback, measured by the electronic control module (ECM), is greater than the calibrated value. | No action is taken by the ECM. |
>
> Rack Actuator Circuit
>
> ### Circuit Description
>
> The rack actuator is supplied with a varying current source from the ECM. The rack actuator uses this current to change the position of the control rack, which regulates the amount of fuel delivered from the fuel pump. The rack position feedback sensor relays the actuator rack position back to the ECM.
>
> ### Component Location
>
> The rack actuator is an integral part of the RP39 fuel pump.
>
> ### Shoptalk
>
> - Confirm that the actuator connector is firmly in place.
>
> - When there is no power to the actuator, the actuator closes and fuel flow stops.
>
> Refer to Troubleshooting Fault Code t05-166
