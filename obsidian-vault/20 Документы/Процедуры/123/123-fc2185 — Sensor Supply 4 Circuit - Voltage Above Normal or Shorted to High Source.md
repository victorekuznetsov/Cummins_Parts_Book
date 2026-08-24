---
aliases:
  - "Цепь питания датчиков 4 — напряжение выше нормы"
type: "Процедура"
doc: "123-fc2185"
title_en: "Sensor Supply 4 Circuit - Voltage Above Normal or Shorted to High Source"
title_ru: "Цепь питания датчиков 4 — напряжение выше нормы"
modified: "2026-02-06"
engines:
  - "41349633"
families:
  - "QSK19"
manuals:
  - "4022094"
figures: 3
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/123/123-fc2185.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/123-fc2185.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/123"
  - "перевод/машинный"
---

# Sensor Supply 4 Circuit - Voltage Above Normal or Shorted to High Source
**Цепь питания датчиков 4 — напряжение выше нормы**

> [!abstract] Процедура · `123-fc2185`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4022094 — QSK19 CM2150 and CM2670 Electronic Control System Troubleshooting and Repair Manual|4022094]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2026-02-06
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/123/123-fc2185.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/123-fc2185.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 2185

### Цепь питания датчиков 4 — напряжение выше нормы

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 2185 PID(P): СПН: 3512 FMI: 3 лампы: Янтарная СРТ: | Высокое напряжение, обнаруженное на цепи питания 4 датчика. | Потеря некоторых функций датчика. |

![[19401837.png]]

QSK19 CM2150 Industrial - Сенсорная схема поставки 4

![[00a00243.png]]

QSK19 CM2150 Marine - 4-х станковая схема поставки датчиков

![[00a00244.png]]

QSK19 CM2150 Power Generation - 4 схема поставки датчиков

### Описание цепи

Датчик питания 4 модуля управления двигателем (ECM) обеспечивает 5 VDC питания для различных датчиков.

### Расположение компонента

Схема подачи 4 датчика модуля управления двигателем (ECM) обеспечивает подачу 5 вольт на различные датчики. См. диаграмму проводов для идентификации подачи датчика.

### Практические замечания

Возможные причины этого кода неисправности:

- Неисправный или повреждённый жгут проводов двигателя.

См. Код устранения неполадок t05-2185.


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 2185
>
> ### Sensor Supply 4 Circuit - Voltage Above Normal or Shorted to High Source
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 2185 PID(P): SPN: 3512 FMI: 3 Lamp: Amber SRT: | High voltage detected at the sensor supply 4 circuit. | Loss of some sensor functionality. |
>
> QSK19 CM2150 Industrial - Sensor Supply 4 Circuit
>
> QSK19 CM2150 Marine - Sensor Supply 4 Circuit
>
> QSK19 CM2150 Power Generation - Sensor Supply 4 Circuit
>
> ### Circuit Description
>
> Sensor supply 4 of the engine control module (ECM) provides a 5 VDC supply to various sensors.
>
> ### Component Location
>
> The sensor supply 4 circuit of the engine control module (ECM) provides a 5 volt supply to various sensors. Refer to the wiring diagram for sensor supply identification.
>
> ### Shoptalk
>
> Possible causes of this fault code include:
>
> - Malfunctioning or damaged engine wiring harness.
>
> Refer to Troubleshooting Fault Code t05-2185.
