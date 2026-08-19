---
aliases:
  - "Диагностика драйвера топливной рампы"
type: "Процедура"
doc: "01-fc1419"
title_en: "Fuel Rail Driver Diagnostic"
title_ru: "Диагностика драйвера топливной рампы"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1419.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1419.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Fuel Rail Driver Diagnostic
**Диагностика драйвера топливной рампы**

> [!abstract] Процедура · `01-fc1419`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1419.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1419.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 1419

### Диагностика драйвера топливной рампы

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 1419 P(P): СПН: ФМИ: Лампа: Предупреждение СТО: | Диагностика водителя топливного рельса выявила ошибку. | Никаких действий со стороны ЕКМ не предпринимается. Возможная потеря производительности. |

![[19803582.png]]

Схема привода топливных рельсов

### Описание цепи

ECM проверяет водителей привода топливного рельса на предмет правильной работы. Приводы топливной рельсы приводятся в действие электронным модулем управления (ECM) для управления замером топлива. Каждый топливный привод соединен с ECM посредством подачи и обратной проволоки. Электрический импульс отправляется в топливный привод от ECM на подаче провода и возвращается в ECM на обратном проводе. Каждый соленоидный клапан обычно закрыт, и он открыт только электрическим импульсом от ECM во время измерения. ECM контролирует напряжение, напряжение не будет срабатывать с кодом 1419 по умолчанию и может быть вызвано шортами, открываниями или неисправным водителем привода топливного рельса в ECM.

### Расположение компонента

Водители топливных рельсов содержатся в ECM.

### Практические замечания

Возможные режимы отказа - это открытая цепь, короткая к земле, высокое сопротивление привода и потеря напряжения наддува внутри ECM.

См. Код устранения неисправностей t05-1419


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 1419
>
> ### Fuel Rail Driver Diagnostic
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 1419 PID(P): SPN: FMI: Lamp: Warning SRT: | Fuel rail driver diagnostic has detected an error. | No action is taken by the ECM. Possible loss of performance. |
>
> Fuel Rail Actuator Circuit
>
> ### Circuit Description
>
> The ECM checks the fuel rail actuator drivers to sustain correct operation. The fuel rail actuators are actuated by the electronic control module (ECM) to control fuel metering. Each fuel actuator is connected to the ECM by a supply and a return wire. An electrical pulse is sent to the fuel actuator from the ECM on the supply wire and returns to the ECM on the return wire. Each solenoid valve is normally closed, and it is **only** opened by an electrical pulse from the ECM during metering. The ECM monitors the voltage, no voltage will trip Fault Code 1419, and can be caused by shorts, opens, or a failed fuel rail actuator driver in the ECM.
>
> ### Component Location
>
> The fuel rail drivers are contained in the ECM.
>
> ### Shoptalk
>
> The possible failure modes are open circuit, short to ground, high actuator resistance, and loss of boost voltage inside the ECM.
>
> Refer to Troubleshooting Fault Code t05-1419
