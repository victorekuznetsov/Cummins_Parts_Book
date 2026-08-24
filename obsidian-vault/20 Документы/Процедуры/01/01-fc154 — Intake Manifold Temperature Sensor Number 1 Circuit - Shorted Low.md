---
aliases:
  - "Цепь датчика температуры коллектора 1 — замыкание на массу"
type: "Процедура"
doc: "01-fc154"
title_en: "Intake Manifold Temperature Sensor Number 1 Circuit - Shorted Low"
title_ru: "Цепь датчика температуры коллектора 1 — замыкание на массу"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc154.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc154.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Intake Manifold Temperature Sensor Number 1 Circuit - Shorted Low
**Цепь датчика температуры коллектора 1 — замыкание на массу**

> [!abstract] Процедура · `01-fc154`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc154.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc154.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 154

### Цепь датчика температуры коллектора 1 — замыкание на массу

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 154 PID(P): СПН: ФМИ: Лампа: Предупреждение СТО: | Сигнал датчика температуры коллектора двигателя закорачивается низко. | Отсутствие защиты двигателя от температуры впускного коллектора.Возможно, белый дым. |

![[19803595.png]]

Цепь датчика температуры во впускном коллекторе

### Описание цепи

Датчик температуры впускного коллектора используется ECM для мониторинга температуры воздуха в впускном коллекторе ниже по течению от элемента послеохладителя. Температура впускного коллектора используется ECM для системы защиты двигателя, управления временем и заправкой. Если напряжение низкое, ECM регистрирует код 154 ошибки. Низкое напряжение может быть вызвано шортами для блокировки двигателя на податочных или обратных проводах или внутренне заземленным неисправным датчиком.

### Расположение компонента

См. диаграммы двигателя в разделе E этого руководства для определения местоположения компонента.

### Практические замечания

Сопротивление датчика изменяется в зависимости от температуры.

Устранение неполадок код t05-154


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 154
>
> ### Intake Manifold Temperature Sensor Number 1 Circuit - Shorted Low
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 154 PID(P): SPN: FMI: Lamp: Warning SRT: | Engine intake manifold temperature sensor signal is shorted low. | No engine protection for the intake manifold temperature.Possible white smoke. |
>
> Intake Manifold Temperature Sensor Circuit
>
> ### Circuit Description
>
> The intake manifold temperature sensor is used by the ECM to monitor the temperature of the air in the intake manifold downstream of the aftercooler element. The intake manifold temperature is used by the ECM for the engine protection system, timing, and fueling control. If the voltage is low, the ECM will log Fault Code 154. Low voltage can be caused by shorts to engine block ground on the supply or return wires or an internally grounded failed sensor.
>
> ### Component Location
>
> Refer to the Engine Diagrams in Section E of this manual for the component location.
>
> ### Shoptalk
>
> The resistance of the sensor varies with the temperature.
>
> Refer to Troubleshooting Fault Code t05-154
