---
aliases:
  - "Заклинивание рейки управления подачей"
type: "Процедура"
doc: "87-fc172"
title_en: "Fuel Control Rack Stuck"
title_ru: "Заклинивание рейки управления подачей"
modified: "2018-02-19"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666214"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc172.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-fc172.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
  - "перевод/машинный"
---

# Fuel Control Rack Stuck
**Заклинивание рейки управления подачей**

> [!abstract] Процедура · `87-fc172`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2018-02-19
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc172.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-fc172.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 172

### Заклинивание рейки управления подачей

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 172 PID(P): S023 SPN: 638 FMI: 7 ламп: Красная СТО: | Реестр управления топливом застрял в положении, командующем чрезмерным заправкой двигателя. | Останов двигателя. |

![[19a00103.png]]

Цепь привода рейки

### Описание цепи

Реестр управления топливом и соленоид определяют количество топлива, отмеренное для двигателя.

### Расположение компонента

Реестр управления топливом и соленоид являются неотъемлемыми частями топливного насоса RP39.

### Практические замечания

- Подтвердите, что разъем привода прочно на месте.

См. Код устранения неполадок t05-172


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 172
>
> ### Fuel Control Rack Stuck
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 172 PID(P): S023 SPN: 638 FMI: 7 Lamp: Red SRT: | Fuel control rack is stuck in a position commanding excessive fueling to the engine. | Engine shutdown. |
>
> Rack Actuator Circuit
>
> ### Circuit Description
>
> The fuel control rack and solenoid determine the quantity of fuel metered to the engine.
>
> ### Component Location
>
> The fuel control rack and solenoid are integral parts of the RP39 fuel pump.
>
> ### Shoptalk
>
> - Confirm that the actuator connector is firmly in place.
>
> Refer to Troubleshooting Fault Code t05-172
