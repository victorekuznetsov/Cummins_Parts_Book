---
aliases:
  - "Цепь педали акселератора и выключателя подтверждения холостого хода"
type: "Процедура"
doc: "87-fc432"
title_en: "Accelerator Pedal/Idle Validation Switch Circuit"
title_ru: "Цепь педали акселератора и выключателя подтверждения холостого хода"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc432.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-fc432.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
  - "перевод/машинный"
---

# Accelerator Pedal/Idle Validation Switch Circuit
**Цепь педали акселератора и выключателя подтверждения холостого хода**

> [!abstract] Процедура · `87-fc432`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc432.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-fc432.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 432

### Цепь педали акселератора и выключателя подтверждения холостого хода

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 432 PID(P): P091 SPN: 091 ФМИ: 13 ламп: Красная СТО: | Напряжение, обнаруженное при контакте 26 сигнала холостого хода проводов OEM, когда напряжение при контакте 30 сигнала положения ускорителя проводов OEM указывает, что педаль **не*** находится в холостом ходу, или напряжение, обнаруженное при контакте 25 сигнала холостого хода валидации вне холостого хода проводов OEM, когда напряжение при контакте 30 сигнала положения ускорителя проводов OEM указывает, что педаль находится в покое. | Двигатель не будет реагировать на акселератор. Двигатель будет простаивать только *. |

![[19a00759.png]]

Цепь педали акселератора

### Описание цепи

Педаль акселератора обеспечивает команду акселератора водителя электронному модулю управления (ECM) через OEM-проводник и OEM-интерфейс. ECM использует этот сигнал для определения команды заправки топливного насоса.

### Расположение компонента

Расположение педали ускорителя варьируется в зависимости от каждого OEM. См. руководство по OEM.

### Практические замечания

Этот код неисправности обычно вызван неправильной проводкой цепи ускорителя, схемы проверки бездействия или проводов OEM.

Примечание: Если датчик положения ускорителя или акселератора изменен или после калибровочной загрузки, проведите педаль акселератора (переключатель зажигания поворота) через его полное путешествие три раза. Эта процедура калибрует новый ускоритель с помощью ECM.

Устранение неполадок код t05-432


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 432
>
> ### Accelerator Pedal/Idle Validation Switch Circuit
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 432 PID(P): P091 SPN: 091 FMI: 13 Lamp: Red SRT: | Voltage detected at the idle validation on-idle signal pin 26 of the OEM harness when voltage at the accelerator position signal pin 30 of the OEM harness indicates the pedal is **not** at idle, or voltage detected at idle validation off-idle signal pin 25 of the OEM harness when voltage at accelerator position signal pin 30 of the OEM harness indicates pedal is at rest. | Engine will **not** respond to accelerator. Engine will idle **only**. |
>
> Accelerator Pedal Circuit
>
> ### Circuit Description
>
> The accelerator pedal provides the driver's accelerator command to the electronic control module (ECM) through the OEM harness and the OEM interface harness. The ECM uses this signal to determine the fueling command for the fuel pump.
>
> ### Component Location
>
> The accelerator pedal location varies with each OEM. Refer to the OEM manual.
>
> ### Shoptalk
>
> This fault code is usually caused by the improper wiring of the accelerator circuit, the idle validation circuit, or the OEM harness.
>
> Note: If the accelerator or accelerator position sensor is changed, or after a calibration download, cycle the accelerator pedal (turn keyswitch ON) through its complete travel three times. This procedure calibrates the new accelerator with the ECM.
>
> Refer to Troubleshooting Fault Code t05-432
