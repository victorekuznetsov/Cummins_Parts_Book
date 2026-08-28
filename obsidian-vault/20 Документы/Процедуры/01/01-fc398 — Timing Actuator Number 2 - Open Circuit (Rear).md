---
aliases:
  - "Привод опережения №2 — обрыв (задний)"
type: "Процедура"
doc: "01-fc398"
title_en: "Timing Actuator Number 2 - Open Circuit (Rear)"
title_ru: "Привод опережения №2 — обрыв (задний)"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc398.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc398.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Timing Actuator Number 2 - Open Circuit (Rear)
**Привод опережения №2 — обрыв (задний)**

> [!abstract] Процедура · `01-fc398`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc398.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc398.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 398

### Привод опережения №2 — обрыв (задний)

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 398 P(P): СПН: ФМИ: Лампа: Отключение SRT: | Схема срабатывания № 2 — открытая схема. (задний) | Двигатель отключится. |

![[19c01394.png]]

Схема срабатывания привода № 2

### Описание цепи

Приводы синхронизации приводятся в действие ECM для управления замером топлива. Каждый привод синхронизации соединен с ECM посредством подачи и возвратного провода. Электрический импульс отправляется в привод синхронизации от ECM на подаче провода и возвращается в ECM на обратном проводе. Каждый соленоидный клапан обычно закрыт, и он открыт только электрическим импульсом от ECM во время измерения.

### Расположение компонента

Задний привод синхронизации установлен на корпусе подачи топлива. Это третий привод с передней части двигателя QSX15.

### Практические замечания

Возможные режимы отказа - открытая цепь, короткое к земле и высокое сопротивление привода.

См. Код устранения неполадок t05-398


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 398
>
> ### Timing Actuator Number 2 - Open Circuit (Rear)
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 398 PID(P): SPN: FMI: Lamp: Shutdown SRT: | Timing actuator Number 2 circuit - open circuit. (rear) | Engine will shut down. |
>
> Timing Actuator Number 2 Circuit
>
> ### Circuit Description
>
> The timing actuators are actuated by the ECM to control fuel metering. Each timing actuator is connected to the ECM by a supply and a return wire. An electrical pulse is sent to the timing actuator from the ECM on the supply wire and returns to the ECM on the return wire. Each solenoid valve is normally closed, and it is **only** opened by an electrical pulse from the ECM during metering.
>
> ### Component Location
>
> The rear timing actuator is mounted on the fuel delivery housing. It is the third actuator from the front of the QSX15 engine.
>
> ### Shoptalk
>
> The possible failure modes are open circuit, short to ground, and high actuator resistance.
>
> Refer to Troubleshooting Fault Code t05-398
