---
aliases:
  - "Цепь положения привода рейки 1 — короткое замыкание (левый ряд)"
type: "Процедура"
doc: "01-fc169"
title_en: "Fuel Rack Actuator Position 1 Circuit - Short Circuit (Left Bank)"
title_ru: "Цепь положения привода рейки 1 — короткое замыкание (левый ряд)"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc169.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc169.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Fuel Rack Actuator Position 1 Circuit - Short Circuit (Left Bank)
**Цепь положения привода рейки 1 — короткое замыкание (левый ряд)**

> [!abstract] Процедура · `01-fc169`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc169.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc169.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 169

### Цепь положения привода рейки 1 — короткое замыкание (левый ряд)

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 169 P(P): СПН: ФМИ: Лампа: Отключение SRT: | Цепь положения привода рейки 1 — короткое замыкание (левый ряд). | Двигатель может отключиться из-за превышения скорости. Код 2974 также может активировать |

![[19803597.png]]

Завод привода топливного бака 1 позиция

### Описание цепи

Приводы топливной стойки приводятся в действие ECM для управления замером топлива. Каждый привод стойки соединен с ECM посредством подачи и возвратного провода. Электрический импульс отправляется в привод стойки от ECM на подаче провода и возвращается в ECM на обратном проводе. Каждый соленоидный клапан обычно закрыт, и он открыт только электрическим импульсом от ECM во время измерения. Этот тест проверяет, чтобы увидеть, что ток, подаваемый от ECM к приводу, подается обратно в ECM на обратной цепи.

### Расположение компонента

Реечный привод является частью топливного насоса левого берега.

### Практические замечания

Эта неисправность требует, чтобы скорость двигателя была больше нуля, прежде чем неисправность будет активна.

Возможные режимы отказа - низкое сопротивление привода или привод топливной стойки PWM 1, подводимый к батарее.

Эта процедура кода неисправности также предусматривает устранение неполадок, когда привод топливной стойки PWM 1 закорачивается на землю. Этот тип отказа ** не ** вызовет код неисправности в это время, но вызовет грубый запуск двигателя.

Если код 2974 и код 169 ошибки активны, сначала устраните код 169 ошибки.

Устранение неполадок код t05-169


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 169
>
> ### Fuel Rack Actuator Position 1 Circuit - Short Circuit (Left Bank)
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 169 PID(P): SPN: FMI: Lamp: Shutdown SRT: | Fuel rack actuator position 1 circuit - short circuit (left bank). | Engine can possibly shut down due to an overspeed. Fault Code 2974 can also activate |
>
> Fuel Rack Actuator Position 1 Circuit
>
> ### Circuit Description
>
> The fuel rack actuators are actuated by the ECM to control fuel metering. Each rack actuator is connected to the ECM by a supply and a return wire. An electrical pulse is sent to the rack actuator from the ECM on the supply wire and returns to the ECM on the return wire. Each solenoid valve is normally closed, and it is **only** opened by an electrical pulse from the ECM during metering. This test checks to see that the current being supplied from the ECM to the actuator is being fed back to the ECM on the return circuit.
>
> ### Component Location
>
> The rack actuator is part of the left bank fuel pump.
>
> ### Shoptalk
>
> This fault requires engine speed greater than zero before the fault will go active
>
> The possible failure modes are low actuator resistance or the fuel rack actuator PWM 1 supply shorted to battery.
>
> This fault code procedure also provides for troubleshooting when the fuel rack actuator PWM 1 return is shorted to ground. This type of failure will **not** cause a fault code at this time, but will cause the engine to run rough.
>
> If Fault Code 2974 and Fault Code 169 are active, troubleshoot Fault Code 169 first.
>
> Refer to Troubleshooting Fault Code t05-169
