---
aliases:
  - "Датчик атмосферного давления"
type: "Процедура"
doc: "82-fc295"
title_en: "Ambient Air Pressure Sensor"
title_ru: "Датчик атмосферного давления"
modified: "2010-09-02"
engines:
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc295.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc295.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# Ambient Air Pressure Sensor
**Датчик атмосферного давления**

> [!abstract] Процедура · `82-fc295`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc295.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc295.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 295

### Датчик атмосферного давления

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 295 PID(P): P108 SPN: 108 FMI: 2 лампы: Желтая СТО: | Ошибка в сигнале датчика давления окружающего воздуха была обнаружена ECM. | Двигатель не имеет параметра для установки воздуха. |

![[19c00652.png]]

Датчик атмосферного давления

### Описание цепи

### Расположение компонента

Датчик давления окружающего воздуха расположен ниже ECM.

### Практические замечания

При включении клавиш сравниваются показания для давления окружающей среды от датчика давления окружающего воздуха, датчика давления впускного коллектора и датчика давления масла. Этот код неисправности возникает, если показания датчика давления окружающего воздуха отличаются от двух других.

См. Код устранения неполадок t05-295


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 295
>
> ### Ambient Air Pressure Sensor
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 295 PID(P): P108 SPN: 108 FMI: 2 Lamp: Yellow SRT: | An error in the ambient air pressure sensor signal was detected by the ECM. | Engine is derated to no air setting. |
>
> Ambient Air Pressure Sensor
>
> ### Circuit Description
>
> ### Component Location
>
> The ambient air pressure sensor is located below the ECM.
>
> ### Shoptalk
>
> At key-on, the readings for ambient pressure from the ambient air pressure sensor, intake manifold pressure sensor, and oil pressure sensor are compared. This fault code occurs if the ambient air pressure sensor reading is different from the other two.
>
> Refer to Troubleshooting Fault Code t05-295
