---
aliases:
  - "Цепь датчика атмосферного давления"
type: "Процедура"
doc: "87-fc221"
title_en: "Ambient Air Pressure Sensor Circuit"
title_ru: "Цепь датчика атмосферного давления"
modified: "2010-07-29"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc221.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-fc221.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
  - "перевод/машинный"
---

# Ambient Air Pressure Sensor Circuit
**Цепь датчика атмосферного давления**

> [!abstract] Процедура · `87-fc221`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc221.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-fc221.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 221

### Цепь датчика атмосферного давления

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 221 P(P): P108 SPN: 108 FMI: 3 лампы: Желтая СТО: | Более 4,69 ВДК обнаружено при контакте датчика давления окружающего воздуха 32 проводов двигателя ремня. | Электронный модуль управления (ECM) не выполняет никаких действий. |

![[19a00125.png]]

Цепь датчика атмосферного давления

### Описание цепи

Датчик давления окружающего воздуха обеспечивает сигнал давления окружающего воздуха к ECM через электропроводку двигателя. ECM использует датчик давления окружающего воздуха для регулировки заправки топливом в зависимости от высоты.

### Расположение компонента

Датчик давления окружающего воздуха расположен с левой стороны двигателя, на скобке ECM.

### Практические замечания

Мониторинг показания давления окружающего воздуха с помощью электронного инструментария службы, чтобы подтвердить, что показания давления соответствуют фактическому давлению воздуха.

См. Код устранения неполадок t05-221


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 221
>
> ### Ambient Air Pressure Sensor Circuit
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 221 PID(P): P108 SPN: 108 FMI: 3 Lamp: Yellow SRT: | More than 4.69 VDC detected at the ambient air pressure sensor signal pin 32 of the engine harness. | No action is taken by the electronic control module (ECM). |
>
> Ambient Air Pressure Sensor Circuit
>
> ### Circuit Description
>
> The ambient air pressure sensor provides the ambient air pressure signal to the ECM, through the engine harness. The ECM uses the ambient air pressure sensor to adjust fueling based on the altitude.
>
> ### Component Location
>
> The ambient air pressure sensor is located on the left-hand side of the engine, on the ECM bracket.
>
> ### Shoptalk
>
> Monitor the ambient air pressure reading with an electronic service tool to confirm that the pressure reading matches the actual air pressure.
>
> Refer to Troubleshooting Fault Code t05-221
