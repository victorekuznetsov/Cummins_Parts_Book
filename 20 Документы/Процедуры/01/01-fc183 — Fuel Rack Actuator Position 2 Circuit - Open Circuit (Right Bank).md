---
aliases:
  - "Цепь положения привода рейки 2 — обрыв (правый ряд)"
type: "Процедура"
doc: "01-fc183"
title_en: "Fuel Rack Actuator Position 2 Circuit - Open Circuit (Right Bank)"
title_ru: "Цепь положения привода рейки 2 — обрыв (правый ряд)"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc183.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc183.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Fuel Rack Actuator Position 2 Circuit - Open Circuit (Right Bank)
**Цепь положения привода рейки 2 — обрыв (правый ряд)**

> [!abstract] Процедура · `01-fc183`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc183.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc183.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 183

### Цепь положения привода рейки 2 — обрыв (правый ряд)

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 183 P(P): СПН: ФМИ: Лампа: Отключение SRT: | Цепь положения привода рейки 2 — обрыв (правый ряд). | Двигатель может отключиться из-за превышения скорости. Код 174 ошибки также может быть активирован. |

![[19803599.png]]

Завод привода топливных тяг 2

### Описание цепи

Приводы топливной стойки приводятся в действие ECM для управления замером топлива. Каждый привод стойки соединен с ECM посредством подачи и возвратного провода. Электрический импульс отправляется в привод стойки от ECM на подаче провода и возвращается в ECM на обратном проводе. Каждый соленоидный клапан обычно закрыт, и он открыт только электрическим импульсом от ECM во время измерения. Этот тест проверяет, чтобы увидеть, что ток, подаваемый от ECM к приводу, подается обратно в ECM на обратной цепи.

### Расположение компонента

Положение привода 2 топливной стойки является частью топливного насоса правого берега.

### Практические замечания

Возможные режимы отказа для этой неисправности представляют собой открытую цепь или короткую к земле на приводе топливной стойки цепь питания PWM 2 или открытую цепь или короткую к батарее подачу на приводе топливной стойки PWM 2 обратную цепь.

Для этого требуется, чтобы скорость двигателя была больше нуля, прежде чем неисправность начнет работать. Если положение топливной стойки контролируется, то положение правой стойки будет примерно вдвое больше, чем положение левой стойки. Если двигатель регистрирует код 234 по умолчанию (перегрузка двигателя) и код 168 по умолчанию, сначала устраните код 183 по умолчанию.

Код 174 ошибки может активироваться после исправления кода 183 ошибки. Если это так, выключите ключ и код 174 ошибки будет неактивным и может быть очищен.

См. Код устранения неполадок t05-183


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 183
>
> ### Fuel Rack Actuator Position 2 Circuit - Open Circuit (Right Bank)
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 183 PID(P): SPN: FMI: Lamp: Shutdown SRT: | Fuel rack actuator position 2 circuit - open circuit (right bank). | Engine can shut down due to an overspeed. Fault Code 174 can also activate. |
>
> Fuel Rack Actuator Position 2 Circuit
>
> ### Circuit Description
>
> The fuel rack actuators are actuated by the ECM to control fuel metering. Each rack actuator is connected to the ECM by a supply and a return wire. An electrical pulse is sent to the rack actuator from the ECM on the supply wire and returns to the ECM on the return wire. Each solenoid valve is normally closed, and it is **only** opened by an electrical pulse from the ECM during metering. This test checks to see that the current being supplied from the ECM to the actuator is being fed back to the ECM on the return circuit.
>
> ### Component Location
>
> The fuel rack actuator position 2 is part of the right bank fuel pump.
>
> ### Shoptalk
>
> The possible failure modes for this fault are an open circuit or short to ground on the fuel rack actuator PWM 2 supply circuit or an open circuit or short to battery supply on the fuel rack actuator PWM 2 return circuit.
>
> This fault requires engine speed greater than zero before the fault will go active. If fuel rack position is being monitored, the right rack position will be roughly twice that of the left rack position. If the engine logs a Fault Code 234 (engine overspeed) and a Fault Code 168, troubleshoot Fault Code 183 first.
>
> Fault Code 174 can go active after Fault Code 183 is corrected. If this is the case, key off and Fault Code 174 will go inactive and can be cleared.
>
> Refer to Troubleshooting Fault Code t05-183
