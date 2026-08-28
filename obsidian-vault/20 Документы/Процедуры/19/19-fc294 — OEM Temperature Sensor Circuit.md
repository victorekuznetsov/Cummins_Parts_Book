---
aliases:
  - "Цепь датчика температуры OEM"
type: "Процедура"
doc: "19-fc294"
title_en: "OEM Temperature Sensor Circuit"
title_ru: "Цепь датчика температуры OEM"
modified: "2011-03-01"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc294.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc294.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
  - "перевод/машинный"
---

# OEM Temperature Sensor Circuit
**Цепь датчика температуры OEM**

> [!abstract] Процедура · `19-fc294`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2011-03-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc294.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc294.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 294

### Цепь датчика температуры OEM

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 294 PID(P): P223 SPN: 1083 FMI: 4 лампы: Желтая СТО: | VDC, обнаруженный при контакте 27 датчика температуры OEM с проводкой интерфейса OEM, указывает на то, что датчик вышел из строя. | Отсутствие защиты двигателя от температуры OEM. |

![[19400674.png]]

ОЭМ температурный контур

### Описание цепи

Сигнал датчика OEM используется ECM для мониторинга температуры OEM. Температура OEM используется ECM для системы защиты двигателя. Датчик, который вышел из строя с низким уровнем, может быть вызван шортами, заземляющимися на проводах подачи и возврата, или внутренним заземленным (неисправным) датчиком.

### Расположение компонента

Месторасположение варьируется в зависимости от OEM. См. руководство по OEM.

### Практические замечания

Сопротивление всех датчиков температуры изменяется в зависимости от температуры. Проверьте температурные пороги с помощью INSITETM для двигателей серии QSK.

См. Код устранения неполадок t05-294


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 294
>
> ### OEM Temperature Sensor Circuit
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 294 PID(P): P223 SPN: 1083 FMI: 4 Lamp: Yellow SRT: | VDC detected at the OEM temperature sensor signal pin 27 of the OEM interface harness indicates the sensor has failed low. | No engine protection for OEM temperature. |
>
> OEM Temperature Circuit
>
> ### Circuit Description
>
> The OEM sensor signal is used by the ECM to monitor the OEM temperature. The OEM temperature is used by the ECM for the engine protection system. A sensor that has failed low can be caused by shorts to ground on the supply and return wires, or an internally grounded (faulty) sensor.
>
> ### Component Location
>
> The location varies with the OEM. Refer to the OEM manual.
>
> ### Shoptalk
>
> The resistance of all temperature sensors varies with the temperature. Check the temperature thresholds using INSITE™ for QSK Series engines.
>
> Refer to Troubleshooting Fault Code t05-294
