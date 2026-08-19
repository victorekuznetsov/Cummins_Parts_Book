---
aliases:
  - "Цепь привода перепускного клапана турбины №1"
type: "Процедура"
doc: "82-fc465"
title_en: "Wastegate Actuator Number 1 Circuit"
title_ru: "Цепь привода перепускного клапана турбины №1"
modified: "2012-07-05"
engines:
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc465.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc465.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# Wastegate Actuator Number 1 Circuit
**Цепь привода перепускного клапана турбины №1**

> [!abstract] Процедура · `82-fc465`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-07-05
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc465.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc465.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 465

### Цепь привода перепускного клапана турбины №1

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 465 PID(P): S032 SPN: 1188 FMI: 3/3 лампы: Желтая СТО: | Высокое напряжение, обнаруженное в цепи привода 1 обходного клапана турбины, когда напряжение не подавалось модулем управления двигателем (ECM). | Двигатель будет работать с поломкой. |

![[19c00361.png]]

Цепь привода перепускного клапана турбины №1

### Описание цепи

Вентиляционные приводы турбинного обхода - это устройства, используемые ECM для управления давлением наддува.

### Расположение компонента

Контроллер обходного клапана турбины расположен на впускном роге воздуха. Привод № 1 является самым задним соленоидом на контроллере.

### Практические замечания

Возможные причины этого кода неисправности:

- Короткое замыкание к источнику напряжения в электропроводке

- Открытая схема в проводной упряжке, разъёме или клапане управления обходным клапаном турбины

- Неправильно установленный турбинный шунтирующий клапан привода соленоид.

Устранение неполадок код t05-465


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 465
>
> ### Wastegate Actuator Number 1 Circuit
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 465 PID(P): S032 SPN: 1188 FMI: 3/3 Lamp: Yellow SRT: | High voltage detected at the wastegate actuator number 1 circuit when no voltage was being supplied by the engine control module (ECM). | Engine will run derated. |
>
> Wastegate Actuator number 1 Circuit
>
> ### Circuit Description
>
> The wastegate actuators are devices used by the ECM to control boost pressure.
>
> ### Component Location
>
> The wastegate controller is located on the air inlet horn. Actuator number 1 is the rear-most solenoid on the controller.
>
> ### Shoptalk
>
> Possible causes of this fault code include:
>
> - A short circuit to voltage source in the harness
>
> - An open circuit in the harness, connector, or wastegate control valve
>
> - Improperly mounted wastegate actuator solenoid.
>
> Refer to Troubleshooting Fault Code t05-465
