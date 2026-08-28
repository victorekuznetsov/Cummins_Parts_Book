---
type: "Процедура"
doc: "19-fc553"
title_en: "Rail Pressure Over Limits"
modified: "2011-03-01"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
  - "85017333"
families:
  - "QSK23"
  - "QSK60"
manuals:
  - "3666113"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc553.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc553.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
  - "перевод/машинный"
---

# Rail Pressure Over Limits

> [!abstract] Процедура · `19-fc553`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2011-03-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc553.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc553.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 553

### Железнодорожное давление превышено

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 553 PID(P): P157 SPN: 157 ФМИ: 0 лампочка: Красная СТО: 00-382 | Давление на железной дороге превышает нормальный предел. | Запорный клапан отключения топлива обесточен (закрывается клапан). Клапан активизируется (открывается клапан), когда давление на рельсах падает ниже допустимого предела для текущей скорости двигателя. |

![[19400316.png]]

ЭКМ

### Описание цепи

Вторичный процессор ECM контролирует давление в рельсах. Когда он чувствует давление выше кривой крутящего момента, с ускорителем без крутящего момента, или давление выше 103 кПа \[15 psi \], с ускорителем на холостом ходу, и скорость двигателя выше холостого хода, он будет выключать двигатель. Проблема в ЭКМ является наиболее вероятной причиной этой ситуации.

### Расположение компонента

ECM устанавливается на корпусе управляющего клапана.

### Практические замечания

Если код 514 неисправности зарегистрирован, но двигатель не выключен, будет развиваться ситуация избыточного давления, в результате чего код 553 неисправности будет зарегистрирован. Если это так, то исполнительный механизм не открылся, и сначала нужно исследовать код 514.

См. Код устранения неполадок t05-553


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 553
>
> ### Rail Pressure Over Limits
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 553 PID(P): P157 SPN: 157 FMI: 0 Lamp: Red SRT: 00-382 | Rail pressure exceeds a normal limit. | Fuel shutoff valve de-energized (valve closes). The valve reenergizes (valve opens) when rail pressure falls below acceptable limit for present engine speed. |
>
> ECM
>
> ### Circuit Description
>
> The ECM secondary processor monitors the rail pressure. When it senses a pressure above the torque curve, with the accelerator off-idle, or a pressure above 103 kPa \[15 psi\], with the accelerator on-idle, and engine speed is above idle, it will shut the engine down. A problem in the ECM is the most likely cause of this situation.
>
> ### Component Location
>
> The ECM is mounted on the control valve body.
>
> ### Shoptalk
>
> If Fault Code 514 is logged but the engine is **not** shut down, an overpressure situation will develop, causing Fault Code 553 to be logged. If this is the case, the actuator has failed to open; investigate Fault Code 514 first.
>
> Refer to Troubleshooting Fault Code t05-553
