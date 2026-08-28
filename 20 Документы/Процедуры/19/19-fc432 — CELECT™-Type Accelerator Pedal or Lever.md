---
type: "Процедура"
doc: "19-fc432"
title_en: "CELECT™-Type Accelerator Pedal or Lever"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc432.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc432.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
  - "перевод/машинный"
---

# CELECT™-Type Accelerator Pedal or Lever

> [!abstract] Процедура · `19-fc432`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2011-03-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc432.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc432.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 432

### Педаль или рычаг ускорителя CELECTTM-Type

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 432 PID(P): P91 SPN: 091 ФМИ: 13 ламп: Красная СТО: 00-371 | Напряжение, обнаруженное при валидации холостого хода на контакте 13 неработающего сигнала проводов OEM, когда напряжение на контакте 29 сигнала положения ускорителя проводов OEM указывает, что педаль находится **не** на холостом ходу или напряжение, обнаруженное при контакте 12 неработающего сигнала валидации вне холостого хода проводов OEM, когда напряжение на контакте 29 сигнала положения ускорителя электропроводки OEM указывает, что педаль находится в покое. | Двигатель будет по умолчанию до 0-процентного ускорителя. |

![[19400175.png]]

Педаль или рычаг ускорителя CELECTTM-Type

### Описание цепи

Педаль или рычаг акселератора обеспечивает команду акселератора водителя к ECM через OEM-проводку и OEM-интерфейс. ECM использует этот сигнал для определения команды заправки клапана привода топливной рельсы.

### Расположение компонента

Расположение педали или рычага ускорителя варьируется в зависимости от каждого OEM. См. руководство по OEM.

### Практические замечания

- Этот код неисправности обычно вызван неправильной проводкой цепи ускорителя, схемы проверки бездействия или проводов OEM.

Примечание: Если датчик положения ускорителя или акселератора изменен или после калибровочной загрузки, проведите цикл педали акселератора или рычага (переключатель зажигания поворота) через его полное путешествие три раза. Эта процедура калибрует новую педаль акселератора или рычаг с помощью ECM.

Устранение неполадок код t05-432


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 432
>
> ### CELECT™-Type Accelerator Pedal or Lever
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 432 PID(P): P91 SPN: 091 FMI: 13 Lamp: Red SRT: 00-371 | Voltage detected at the idle validation on idle signal pin 13 of the OEM harness when voltage at accelerator position signal pin 29 of the OEM harness indicates pedal is **not** at idle or voltage detected at idle validation off-idle signal pin 12 of the OEM harness when voltage at accelerator position signal pin 29 of the OEM harness indicates pedal is at rest. | Engine will default to 0-percent accelerator. |
>
> CELECT™-Type Accelerator Pedal or Lever
>
> ### Circuit Description
>
> The accelerator pedal or lever provides the driver's accelerator command to the ECM through the OEM harness and the OEM interface harness. The ECM uses this signal to determine the fueling command for the fuel rail actuator valve.
>
> ### Component Location
>
> The accelerator pedal or lever location varies with each OEM. Refer to the OEM manual.
>
> ### Shoptalk
>
> - This fault code is usually caused by the improper wiring of the accelerator circuit, the idle validation circuit, or the OEM harness.
>
> Note: If the accelerator or accelerator position sensor is changed or after a calibration download, cycle the accelerator pedal or lever (turn keyswitch ON) through its complete travel three times. This procedure calibrates the new accelerator pedal or lever with the ECM.
>
> Refer to Troubleshooting Fault Code t05-432
