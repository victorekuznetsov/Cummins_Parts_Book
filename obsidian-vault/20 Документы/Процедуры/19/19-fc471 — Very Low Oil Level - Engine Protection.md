---
type: "Процедура"
doc: "19-fc471"
title_en: "Very Low Oil Level - Engine Protection"
modified: "2015-10-27"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
  - "85017333"
families:
  - "QSK23"
  - "QSK60"
manuals:
  - "3666113"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc471.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc471.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
  - "перевод/машинный"
---

# Very Low Oil Level - Engine Protection

> [!abstract] Процедура · `19-fc471`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2015-10-27
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc471.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc471.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 471

### Очень низкий уровень масла - защита двигателя

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 471 PID(P): S98 SPN: 098 FMI: 1/17 лампа: Обслуживание SRT: QU-471 | Очень низкий уровень масла - защита двигателя. Выявлен очень низкий уровень масла. Сигнал напряжения на уровне масла, контакт 12 проводов двигателя, указывает на очень низкий уровень масла в двигателе. | Калибровка-зависимая прогрессивная мощность ухудшается и выключение двигателя с увеличением времени после оповещения. Функция CentinelTM отключена. |

![[19400642.png]]

Сенсорная схема уровня масла

### Описание цепи

Датчик уровня масла используется модулем управления двигателем (ECM) для мониторинга количества масла в двигателе.

### Расположение компонента

Датчик уровня масла расположен в масляной панели на левой стороне двигателя.

См. Код устранения неполадок t05-471.


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 471
>
> ### Very Low Oil Level - Engine Protection
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 471 PID(P): S98 SPN: 098 FMI: 1/17 Lamp: Maintenance SRT: QU-471 | Very Low Oil Level - Engine Protection. Very low oil level is detected. Voltage signal on the oil level signal pin 12 of the engine harness indicates very low oil level in the engine. | Calibration-dependent progressive power derate and engine shutdown with increasing time after alert. Centinel™ feature is disabled. |
>
> Oil Level Sensor Circuit
>
> ### Circuit Description
>
> The oil level sensor is used by the engine control module (ECM) to monitor the amount of oil in the engine.
>
> ### Component Location
>
> The oil level sensor is located in the oil pan on the left side of the engine.
>
> Refer to Troubleshooting Fault Code t05-471.
