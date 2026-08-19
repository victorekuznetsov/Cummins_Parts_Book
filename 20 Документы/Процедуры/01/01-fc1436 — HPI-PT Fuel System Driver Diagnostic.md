---
aliases:
  - "Диагностика драйверов топливной системы HPI-PT"
type: "Процедура"
doc: "01-fc1436"
title_en: "HPI-PT Fuel System Driver Diagnostic"
title_ru: "Диагностика драйверов топливной системы HPI-PT"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1436.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1436.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# HPI-PT Fuel System Driver Diagnostic
**Диагностика драйверов топливной системы HPI-PT**

> [!abstract] Процедура · `01-fc1436`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1436.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1436.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 1436

### Диагностика драйверов топливной системы HPI-PT

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 1436 PID(P): СПН: ФМИ: Лампа: Предупреждение СТО: | Водитель топливной системы HPI-PT, который является обычным диагностическим средством, обнаружил ошибку. | Никаких действий со стороны ЕКМ не предпринимается. Возможная потеря производительности. |

![[19803591.png]]

HPI-PT Топливная система Драйвер Диагностическая схема

### Описание цепи

Электронный модуль управления (ECM) проверяет приводы приводов топливной системы HPI-PT для поддержания правильной работы. Приводы топливной системы приводятся в действие ECM для управления замером топлива. Каждый топливный привод соединен с ECM посредством подачи и обратной проволоки. Электрический импульс отправляется в топливный привод от ECM на подаче провода и возвращается в ECM на обратном проводе. Каждый соленоидный клапан обычно закрыт, и он открыт только электрическим импульсом от ECM во время измерения.

ECM контролирует напряжение, никакое напряжение не будет срабатывать с кодом 1436 по умолчанию и может быть вызвано шортами, открываниями или неисправным приводом привода топливного насоса в ECM.

### Расположение компонента

См. руководство по OEM для определения местоположения ECM. См. процедуру 100-002 для определения местоположения компонента.

### Практические замечания

Возможные режимы отказа - это открытая цепь, короткая к земле, высокое сопротивление привода и потеря напряжения наддува внутри ECM.

См. Код устранения неисправностей t05-1436


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 1436
>
> ### HPI-PT Fuel System Driver Diagnostic
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 1436 PID(P): SPN: FMI: Lamp: Warning SRT: | HPI-PT fuel system driver common diagnostic has detected an error. | No action is taken by the ECM. Possible loss of performance. |
>
> HPI-PT Fuel System Driver Diagnostic Circuit
>
> ### Circuit Description
>
> The electronic control module (ECM) checks the HPI-PT fuel system actuator drivers to sustain correct operation. The fuel system actuators are actuated by the ECM to control fuel metering. Each fuel actuator is connected to the ECM by a supply and a return wire. An electrical pulse is sent to the fuel actuator from the ECM on the supply wire and returns to the ECM on the return wire. Each solenoid valve is normally closed, and it is **only** opened by an electrical pulse from the ECM during metering.
>
> The ECM monitors the voltage, no voltage will trip Fault Code 1436, and can be caused by shorts, opens, or a failed fuel pump actuator driver in the ECM.
>
> ### Component Location
>
> Refer to the OEM manual for location of the ECM. Refer to Procedure 100-002 for the component location.
>
> ### Shoptalk
>
> The possible failure modes are open circuit, short to ground, high actuator resistance, and loss of boost voltage inside the ECM.
>
> Refer to Troubleshooting Fault Code t05-1436
