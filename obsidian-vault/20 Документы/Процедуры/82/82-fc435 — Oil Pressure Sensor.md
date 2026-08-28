---
aliases:
  - "Датчик давления масла"
type: "Процедура"
doc: "82-fc435"
title_en: "Oil Pressure Sensor"
title_ru: "Датчик давления масла"
modified: "2010-09-02"
engines:
  - "41343322"
  - "41370103"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc435.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc435.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# Oil Pressure Sensor
**Датчик давления масла**

> [!abstract] Процедура · `82-fc435`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc435.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc435.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 435

### Датчик давления масла

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 435 PID(P): P100 SPN: 100 FMI: 2 лампы: Желтая СТО: | Ошибка в сигнале датчика давления масла была обнаружена ECM. | Ни на производительность, ни на защиту двигателя от давления масла. |

![[19c00506.png]]

Датчик давления масла

### Описание цепи

### Расположение компонента

Датчик давления/температуры масла расположен на блоке двигателя слева от топливного фильтра, позади воздушного компрессора.

### Практические замечания

При включении клавиш сравниваются показания для давления окружающей среды от датчика давления окружающего воздуха, датчика давления впускного коллектора и датчика давления масла. Этот код неисправности возникает, если показания датчика давления масла отличаются от двух других.

Устранение неполадок код t05-435


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 435
>
> ### Oil Pressure Sensor
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 435 PID(P): P100 SPN: 100 FMI: 2 Lamp: Yellow SRT: | An error in the oil pressure sensor signal was detected by the ECM. | None on performance; no engine protection for oil pressure. |
>
> Oil Pressure Sensor
>
> ### Circuit Description
>
> ### Component Location
>
> The oil pressure/temperature sensor is located on the engine block to the left of the fuel filter, behind the air compressor.
>
> ### Shoptalk
>
> At key-on, the readings for ambient pressure from the ambient air pressure sensor, intake manifold pressure sensor, and oil pressure sensor are compared. This fault code occurs if the oil pressure sensor reading is different from the other two.
>
> Refer to Troubleshooting Fault Code t05-435
