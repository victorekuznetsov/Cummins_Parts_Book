---
aliases:
  - "Цепь датчика температуры коллектора 2 — замыкание на плюс"
type: "Процедура"
doc: "01-fc159"
title_en: "Intake Manifold Temperature Sensor Number 2 Circuit - Shorted High"
title_ru: "Цепь датчика температуры коллектора 2 — замыкание на плюс"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc159.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc159.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Intake Manifold Temperature Sensor Number 2 Circuit - Shorted High
**Цепь датчика температуры коллектора 2 — замыкание на плюс**

> [!abstract] Процедура · `01-fc159`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc159.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc159.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 159

### Цепь датчика температуры коллектора 2 — замыкание на плюс

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 159 P(P): СПН: ФМИ: Лампа: Предупреждение СТО: | Сигнал датчика температуры коллектора двигателя высоко закорачивается. | Отсутствие защиты двигателя от температуры воздуха впускного коллектора. Возможен белый дым. |

![[19803595.png]]

Цепь датчика температуры во впускном коллекторе

### Описание цепи

Датчик температуры впускного коллектора № 2 используется ECM для мониторинга температуры воздуха в впускном коллекторе после охладителя. Датчик температуры впускного коллектора № 2 используется ECM для управления временем и заправкой. Если напряжение высокое, ECM регистрирует код 159 ошибки. Высокое напряжение может быть вызвано открытиями в сигнале или обратных проводах, шортами напряжения к сигналу или обратным проводам или неисправным открытым датчиком.

### Расположение компонента

См. диаграммы двигателя в разделе E этого руководства для определения местоположения компонента.

### Практические замечания

Сопротивление датчика изменяется в зависимости от температуры.

Устранение неполадок код t05-159


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 159
>
> ### Intake Manifold Temperature Sensor Number 2 Circuit - Shorted High
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 159 PID(P): SPN: FMI: Lamp: Warning SRT: | Engine intake manifold temperature sensor signal is shorted high. | No engine protection for the intake manifold air temperature. Possible white smoke. |
>
> Intake Manifold Temperature Sensor Circuit
>
> ### Circuit Description
>
> The intake manifold temperature sensor Number 2 is used by the ECM to monitor the temperature of the air in the intake manifold after the aftercooler. The intake manifold temperature sensor Number 2 is used by the ECM for the timing and fueling control. If the voltage is high, the ECM will log Fault Code 159. Voltage high can be caused by opens in the signal or return wires, voltage shorts to the signal or return wires, or a failed open sensor.
>
> ### Component Location
>
> Refer to the Engine Diagrams in Section E of this manual for the component location.
>
> ### Shoptalk
>
> The resistance of the sensor varies with the temperature.
>
> Refer to Troubleshooting Fault Code t05-159
