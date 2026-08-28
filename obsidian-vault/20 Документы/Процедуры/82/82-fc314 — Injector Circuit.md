---
aliases:
  - "Цепь форсунки"
type: "Процедура"
doc: "82-fc314"
title_en: "Injector Circuit"
title_ru: "Цепь форсунки"
modified: "2010-09-02"
engines:
  - "41343322"
  - "41370103"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc314.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc314.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# Injector Circuit
**Цепь форсунки**

> [!abstract] Процедура · `82-fc314`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc314.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc314.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 314

### Цепь форсунки

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 314 PID(P): S006 SPN: 656 FMI: 6/6 Лампа: Желтая СТО: | Ток, обнаруженный на топливном форсунке для цилиндра No. 6 когда напряжение выключено. | Форсунка для цилиндра No. 6 выключен. |

![[19200154.png]]

Цепь форсунки

### Описание цепи

Соленоидные клапаны форсунки приводятся в действие электронным модулем управления (ECM) для управления замером и временем расхода топлива. Каждый соленоид форсунки соединен с ECM по питающей и обратной проволоке. Электрический импульс отправляется в форсунка от ECM на подаче провода и возвращается в ECM на обратном проводе после приведения в действие соленоида. Каждый соленоидный клапан обычно открыт, и он закрыт только электрическим импульсом от ECM во время впрыска топлива и измерения.

### Расположение компонента

Есть две части для привода привода ISM / QSM жгута проводов - одна внутренняя и другая внешняя. Внешняя часть проводов привода упряжки простирается от порта разъема в ECM до задней стороны корпуса рычага качения клапана. Наружная проводка жгута соединяется с внутренней проводкой жгута с 15-контактным разъемом на задней стороне корпуса клапанного клапана. Внутренняя проводка привода проходит вдоль внутренней части корпуса рычага качения клапана с правой стороны. Он имеет шесть разъемов, расположенных вдоль его длины - по одному для каждого соленоида форсунки. Эти разъёмы крепятся к коннектору на каждом топливном форсунке.

### Практические замечания

Возможные причины этого кода неисправности включают низкое сопротивление соленоидов форсунки, короткое напряжение батареи и короткое между соленоидными проводами форсунки.

Устранение неполадок код t05-314


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 314
>
> ### Injector Circuit
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 314 PID(P): S006 SPN: 656 FMI: 6/6 Lamp: Yellow SRT: | Current detected at the injector for cylinder No. 6 when voltage is turned off. | The injector for cylinder No. 6 is turned off. |
>
> Injector Circuit
>
> ### Circuit Description
>
> The injector solenoid valves are actuated by the electronic control module (ECM) to control fuel metering and timing. Each injector solenoid is connected to the ECM by a supply and a return wire. An electrical pulse is sent to the injector from the ECM on the supply wire and returns to the ECM on the return wire after actuating the solenoid. Each solenoid valve is normally open, and it is **only** closed by an electrical pulse from the ECM during fuel injection and metering.
>
> ### Component Location
>
> There are two pieces to an ISM/QSM actuator harness - one internal and the other external. The external portion of the actuator harness extends from the connector port in the ECM to the backside of the rocker lever housing. The external harness connects to the internal harness with a 15-pin connector at the backside of the rocker lever housing. The internal actuator harness runs along the inside of the rocker lever housing on the right side. It has six connectors spaced along its length - one for each injector solenoid. These connectors attach to the pigtail connector on each injector.
>
> ### Shoptalk
>
> Possible causes for this fault code include low injector solenoid resistance, a short to battery voltage, and a short between injector solenoid wires.
>
> Refer to Troubleshooting Fault Code t05-314
