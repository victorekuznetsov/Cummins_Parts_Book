---
aliases:
  - "Цепь электромагнита клапана впрыска Centinel™ — неверное напряжение"
type: "Процедура"
doc: "01-fc223"
title_en: "Centinel™ Burn Valve Solenoid Circuit - Voltage Incorrect"
title_ru: "Цепь электромагнита клапана впрыска Centinel™ — неверное напряжение"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc223.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc223.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Centinel™ Burn Valve Solenoid Circuit - Voltage Incorrect
**Цепь электромагнита клапана впрыска Centinel™ — неверное напряжение**

> [!abstract] Процедура · `01-fc223`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc223.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc223.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 223

### Цепь электромагнита клапана впрыска Centinel™ — неверное напряжение

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 223 PID(P): S85 SPN: 1265 FMI: 4 лампы: Желтая СТО: | Схема соленоида горящего клапана CentinelTM открыта или коротковата. Менее 18,0 VDC, обнаруженных на сгоревшем клапане CentinelTM, контакт подачи соленоида с жгутом проводов двигателя или сопротивление соленоида упало ниже 80 Ом. | ECM отключает напряжение питания горящего клапана, и система CentinelTM отключена. |

![[19803602.png]]

Сжигать соленоидную цепь клапан

### Описание цепи

Соленоид горящего клапана контролирует поток масла в клапане управления маслом во время цикла горения.

### Расположение компонента

Сольноид горящего клапана расположен поверх клапана управления маслом.

См. Код устранения неполадок t05-223


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 223
>
> ### Centinel™ Burn Valve Solenoid Circuit - Voltage Incorrect
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 223 PID(P): S85 SPN: 1265 FMI: 4 Lamp: Yellow SRT: | The Centinel™ burn valve solenoid circuit is open or shorted. Less than 18.0 VDC detected at the Centinel™ burn valve solenoid supply pin of the engine harness or resistance of the solenoid has dropped below 80 ohms. | ECM turns off the burn valve supply voltage and the Centinel™ system is disabled. |
>
> Burn Valve Solenoid Circuit
>
> ### Circuit Description
>
> The burn valve solenoid controls the flow of oil in the oil control valve during the burn cycle.
>
> ### Component Location
>
> The burn valve solenoid is located on top of the oil control valve.
>
> Refer to Troubleshooting Fault Code t05-223
