---
aliases:
  - "Цепь питания датчиков 2 — напряжение выше нормы или замыкание на плюс"
type: "Процедура"
doc: "123-fc227"
title_en: "Sensor Supply 2 Circuit - Voltage Above Normal or Shorted to High Source"
title_ru: "Цепь питания датчиков 2 — напряжение выше нормы или замыкание на плюс"
modified: "2026-02-06"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4022094"
figures: 4
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/123/123-fc227.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/123-fc227.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/123"
  - "перевод/машинный"
---

# Sensor Supply 2 Circuit - Voltage Above Normal or Shorted to High Source
**Цепь питания датчиков 2 — напряжение выше нормы или замыкание на плюс**

> [!abstract] Процедура · `123-fc227`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4022094 — QSK19 CM2150 and CM2670 Electronic Control System Troubleshooting and Repair Manual|4022094]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2026-02-06
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/123/123-fc227.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/123-fc227.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 227

### Цепь питания датчиков 2 — напряжение выше нормы или замыкание на плюс

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 227 P(P): СПН: 3510 FMI: 3/3 лампы: Янтарная СРТ: | Высокое напряжение, обнаруженное в цепи питания датчика № 2. | Потеря некоторых функций датчика. |

![[19401776.png]]

QSK19 CM2150 Industrial - Сенсорная схема 2

![[00k00263.png]]

QSK19 CM2150 Морской/Морской Двигатель - Сенсорная схема 2

![[00k00264.png]]

QSK19 CM2150 Морской/Морской вспомогательный - Сенсорная схема 2

![[00k00265.png]]

QSK19 CM2150 Power Generation - схема поставки датчиков 2

### Описание цепи

Схема подачи датчика 2 модуля управления двигателем (ECM) обеспечивает подачу 5 вольт на различные датчики.

### Расположение компонента

Схема подачи датчика 2 модуля управления двигателем (ECM) обеспечивает подачу 5 вольт на различные датчики. См. диаграмму проводов для идентификации подачи датчика.

### Практические замечания

Возможные причины этого кода неисправности:

- Неисправность или повреждение OEM-проводов.

- Неисправный или повреждённый жгут проводов двигателя.

См. Код устранения неполадок t05-227.


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 227
>
> ### Sensor Supply 2 Circuit - Voltage Above Normal or Shorted to High Source
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 227 PID(P): SPN: 3510 FMI: 3/3 Lamp: Amber SRT: | High voltage detected at sensor supply number 2 circuit. | Loss of some sensor functionality. |
>
> QSK19 CM2150 Industrial - Sensor Supply 2 Circuit
>
> QSK19 CM2150 Marine/Marine Propulsion - Sensor Supply 2 Circuit
>
> QSK19 CM2150 Marine/Marine Auxiliary - Sensor Supply 2 Circuit
>
> QSK19 CM2150 Power Generation - Sensor Supply 2 Circuit
>
> ### Circuit Description
>
> The sensor supply 2 circuit of the engine control module (ECM) provides a 5 volt supply to various sensors.
>
> ### Component Location
>
> The sensor supply 2 circuit of the engine control module (ECM) provides a 5 volt supply to various sensors. Refer to the wiring diagram for sensor supply identification.
>
> ### Shoptalk
>
> Possible causes of this fault code include:
>
> - Malfunctioning or damaged OEM wiring harness.
>
> - Malfunctioning or damaged engine wiring harness.
>
> Refer to Troubleshooting Fault Code t05-227.
