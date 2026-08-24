---
aliases:
  - "Цепь положения привода рейки 1 — обрыв (левый ряд)"
type: "Процедура"
doc: "01-fc168"
title_en: "Fuel Rack Actuator Position 1 Circuit - Open Circuit (Left Bank)"
title_ru: "Цепь положения привода рейки 1 — обрыв (левый ряд)"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc168.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc168.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Fuel Rack Actuator Position 1 Circuit - Open Circuit (Left Bank)
**Цепь положения привода рейки 1 — обрыв (левый ряд)**

> [!abstract] Процедура · `01-fc168`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc168.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc168.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 168

### Цепь положения привода рейки 1 — обрыв (левый ряд)

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 168 PID(P): СПН: ФМИ: Лампа: Отключение SRT: | Цепь положения привода рейки 1 — обрыв (левый ряд). | Двигатель может быть отключен из-за состояния сверхскоростной скорости. Код 171 также может быть активирован. |

![[19803597.png]]

Завод привода топливного бака 1 позиция

### Описание цепи

Приводы топливной стойки приводятся в действие ECM для управления замером топлива. Каждый привод стойки соединен с ECM посредством подачи и возвратного провода. Электрический импульс отправляется в привод стойки от ECM на подаче провода и возвращается в ECM на обратном проводе. Каждый соленоидный клапан обычно закрыт, и он открыт только электрическим импульсом от ECM во время измерения. Этот тест проверяет, чтобы увидеть, что ток, подаваемый от ECM к приводу, подается обратно в ECM на обратной цепи.

### Расположение компонента

Положение 1 привода топливной стойки является частью топливного насоса левого берега.

### Практические замечания

Возможные режимы отказа для этой неисправности представляют собой открытую цепь или короткую к земле на приводе топливной стойки цепь питания PWM 1 или открытую цепь или короткую к батарее подачу на приводе топливной стойки PWM 1 обратную цепь.

Для этого требуется, чтобы скорость двигателя была больше нуля, прежде чем неисправность начнет работать. Если положение топливной стойки контролируется, то положение правой стойки будет примерно вдвое больше, чем положение левой стойки. Если двигатель регистрирует код 234 по умолчанию (перегрузка двигателя) и код 168 по умолчанию, сначала устраните код 168 по умолчанию.

Код 171 ошибки может активироваться после исправления кода 168 ошибки. Если это так, выключите ключ и код 171 ошибки будет неактивным и может быть очищен.

Устранение неполадок код t05-168


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 168
>
> ### Fuel Rack Actuator Position 1 Circuit - Open Circuit (Left Bank)
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 168 PID(P): SPN: FMI: Lamp: Shutdown SRT: | Fuel rack actuator position 1 circuit - open circuit (left bank). | Engine can possibly shut down due to an overspeed condition. Fault Code 171 can also activate. |
>
> Fuel Rack Actuator Position 1 Circuit
>
> ### Circuit Description
>
> The fuel rack actuators are actuated by the ECM to control fuel metering. Each rack actuator is connected to the ECM by a supply and a return wire. An electrical pulse is sent to the rack actuator from the ECM on the supply wire and returns to the ECM on the return wire. Each solenoid valve is normally closed, and it is **only** opened by an electrical pulse from the ECM during metering. This test checks to see that the current being supplied from the ECM to the actuator is being fed back to the ECM on the return circuit.
>
> ### Component Location
>
> The fuel rack actuator position 1 is part of the left bank fuel pump.
>
> ### Shoptalk
>
> The possible failure modes for this fault are an open circuit or short to ground on the fuel rack actuator PWM 1 supply circuit or an open circuit or short to battery supply on the fuel rack actuator PWM 1 return circuit.
>
> This fault requires engine speed greater than zero before the fault will go active. If fuel rack position is being monitored, the right rack position will be roughly twice that of the left rack position. If the engine logs a Fault Code 234 (engine overspeed) and a Fault Code 168, troubleshoot Fault Code 168 first.
>
> Fault Code 171 can go active after Fault Code 168 is corrected. If this is the case, key off and Fault Code 171 will go inactive and can be cleared.
>
> Refer to Troubleshooting Fault Code t05-168
