---
aliases:
  - "Цепь вспомогательного датчика давления 1 — напряжение выше нормы"
type: "Процедура"
doc: "122-fc1542"
title_en: "Auxiliary Pressure Sensor Input 1 Circuit - Voltage Above Normal or Shorted to High Source"
title_ru: "Цепь вспомогательного датчика давления 1 — напряжение выше нормы"
modified: "2017-11-15"
engines:
  - "33239746"
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
manuals:
  - "4022102"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-fc1542.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/122-fc1542.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/122"
  - "перевод/машинный"
---

# Auxiliary Pressure Sensor Input 1 Circuit - Voltage Above Normal or Shorted to High Source
**Цепь вспомогательного датчика давления 1 — напряжение выше нормы**

> [!abstract] Процедура · `122-fc1542`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Входит в руководства:** [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M|4022102]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2017-11-15
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-fc1542.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/122-fc1542.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 1542

### Цепь вспомогательного датчика давления 1 — напряжение выше нормы

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 1542 P(P): P137 SPN: 1387 FMI: 3/3 лампы: Янтарная СРТ: | Цепь вспомогательного датчика давления 1 — напряжение выше нормы. Высокое напряжение сигнала, обнаруженное в цепи датчика давления оригинального производителя оборудования (OEM). | Ни одного на выступление. |

![[19e02111.png]]

QSK60 CM2150 Промышленный - Вспомогательный датчик давления Ввод 1 цепи

### Описание цепи

OEM имеет возможность подключения вспомогательного датчика давления к модулю управления двигателем (ECM). См. руководство по обслуживанию OEM для получения информации о вспомогательном датчике давления.

### Расположение компонента

Ввод датчика давления OEM будет варьироваться в зависимости от применения. См. руководство по обслуживанию OEM для определения местоположения датчика.

### Условия выполнения диагностики

Эта диагностика выполняется непрерывно, когда переключатель зажигания находится в положении Включения.

### Условия установки кодов неисправностей

ECM обнаружил, что цепь сигнала давления OEM была вне диапазона.

### Действия системы при активном коде неисправности

- ECM освещает белую лампу MAINTENANCE или мигает лампой янтарной CHECK ENGINE, указывая на состояние обслуживания, сразу после диагностических прогонов и сбоев.

### Условия сброса кода неисправности

- Для проверки ремонта выполните цикл ключей и оставьте ключ в положении Включено на 1 минуту.

- Состояние кода ошибки, отображаемого инструментами электронного сервиса INSITETM, будет изменено на INACTIVE сразу после запуска и прохождения диагностики.

- ECM отключит мигающую лампу CHECK ENGINE / MAINTENANCE сразу после диагностических прогонов и проходов.

- Команда Reset All Faults в инструменте электронного сервиса INSITETM может использоваться для устранения активных и неактивных ошибок.

### Практические замечания

Возможные причины этого кода неисправности:

- Открытая обратная цепь в электропроводке, разъемах или датчике

- Схема сигнала, сокращенная до подачи датчика или напряжения батареи.

См. Код 1542 устранения неполадок.


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 1542
>
> ### Auxiliary Pressure Sensor Input 1 Circuit - Voltage Above Normal or Shorted to High Source
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 1542 PID(P): P137 SPN: 1387 FMI: 3/3 Lamp: Amber SRT: | Auxiliary Pressure Sensor Input 1 Circuit - Voltage Above Normal or Shorted to High Source. High signal voltage detected at theoriginal equipment manufacturer (OEM) pressure sensor circuit. | None on performance. |
>
> QSK60 CM2150 Industrial - Auxiliary Pressure Sensor Input 1 Circuit
>
> ### Circuit Description
>
> The OEM has the option of wiring an auxiliary pressure sensor input to the engine control module (ECM). Refer to the OEM service manual for information about the auxiliary pressure sensor.
>
> ### Component Location
>
> The OEM pressure sensor input will vary depending on application. Refer to the OEM service manual for sensor location.
>
> ### Conditions For Running The Diagnostics
>
> This diagnostic runs continuously when the keyswitch is in the ON position.
>
> ### Conditions For Setting The Fault Codes
>
> The ECM detected the OEM pressure signal circuit was out of range high.
>
> ### Action Taken When The Fault Code Is Active
>
> - The ECM illuminates the white MAINTENANCE lamp or flashes the amber CHECK ENGINE lamp, indicating a maintenance condition, immediately after the diagnostic runs and fails.
>
> ### Conditions For Clearing The Fault Code
>
> - To validate the repair, perform a key cycle, and leave the key in the ON position for 1 minute.
>
> - The fault code status displayed by INSITE™ electronic service tool will change to INACTIVE immediately after the diagnostic runs and passes.
>
> - The ECM will turn off the flashing amber CHECK ENGINE lamp / MAINTENANCE lamp immediately after the diagnostic runs and passes.
>
> - The Reset All Faults command in INSITE™ electronic service tool can be used to clear active and inactive faults.
>
> ### Shoptalk
>
> Possible causes of this fault code include:
>
> - Open return circuit in the harness, connectors, or sensor
>
> - Signal circuit shorted to sensor supply or battery voltage.
>
> Refer to Troubleshooting Fault Code 1542.
