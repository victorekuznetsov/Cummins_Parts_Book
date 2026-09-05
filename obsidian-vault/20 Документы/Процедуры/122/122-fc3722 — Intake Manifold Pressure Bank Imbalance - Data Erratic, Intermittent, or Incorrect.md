---
aliases:
  - "Разбаланс давления во впускных коллекторах рядов — данные нестабильны или неверны"
type: "Процедура"
doc: "122-fc3722"
title_en: "Intake Manifold Pressure Bank Imbalance - Data Erratic, Intermittent, or Incorrect"
title_ru: "Разбаланс давления во впускных коллекторах рядов — данные нестабильны или неверны"
modified: "2015-06-25"
engines:
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50"
manuals:
  - "4022102"
figures: 2
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-fc3722.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/122-fc3722.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/122"
  - "перевод/машинный"
---

# Intake Manifold Pressure Bank Imbalance - Data Erratic, Intermittent, or Incorrect
**Разбаланс давления во впускных коллекторах рядов — данные нестабильны или неверны**

> [!abstract] Процедура · `122-fc3722`
> **Двигатели:** [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50
> **Входит в руководства:** [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M|4022102]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2015-06-25
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-fc3722.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/122-fc3722.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 3722

### Разбаланс давления во впускных коллекторах рядов — данные нестабильны или неверны

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 3722 PID(P): СПН: ФМИ: Лампа: Обслуживание SRT: | Разбаланс давления во впускных коллекторах рядов — данные нестабильны или неверны. | Отключение двигателя или выключение. |

![[19601948.png]]

QSK50 CM2150 Power Generation с усовершенствованным мониторингом двигателя - схема датчика давления в коллекторе 1

![[19602218.png]]

QSK50 CM2150 Power Generation с усовершенствованным мониторингом двигателя - схема датчика давления в коллекторе 2

### Описание цепи

Датчики давления впускного коллектора 1 и 2 контролируют давление воздуха впускного коллектора и передают информацию в модуль управления двигателем (ECM) через электропроводку двигателя. ECM рассчитывает дифференциальное давление между левым и правым берегом на основе этой информации.

### Расположение компонента

Датчики давления впускного коллектора 1 расположены в левом и правом боковом переднем коллекторе воздухозаборника.

### Условия выполнения диагностики

- Эта диагностика выполняется непрерывно, когда переключатель зажигания ECM находится в положении Включения.

### Условия установки кодов неисправностей

- Если дифференциал давления наддува между датчиками давления впускного коллектора левого и правого берега превышает калиброванное значение за калиброванное количество времени, то неисправность активируется.

### Действия системы при активном коде неисправности

- Не применяется

### Условия сброса кода неисправности

- Не применяется

### Практические замечания

У моделей двигателей, охваченных этим руководством, несколько электронных блоков управления. У каждого блока управления свой адрес источника, который отображается при подключении INSITE™. При поиске неисправности по коду определяйте затронутый блок управления и цепь по адресу источника, который показывает INSITE™.

Возможные причины этого кода неисправности:

- Фильтры с ограниченным воздухозаборником

- Система впускного воздуха усиливает утечку

- Закрытый впускной клапан отключается

- Проблема с одним из турбокомпрессоров

- Многократный неисправный форсунка на одном берегу.

См. Код устранения неполадок t05-3722.


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 3722
>
> ### Intake Manifold Pressure Bank Imbalance - Data Erratic, Intermittent, or Incorrect
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 3722 PID(P): SPN: FMI: Lamp: Maintenance SRT: | Intake Manifold Pressure Bank Imbalance - Data Erratic, Intermittent, or Incorrect. | Engine shutdown or derate. |
>
> QSK50 CM2150 Power Generation with Advanced Engine Monitoring - Intake Manifold 1 Pressure Sensor Circuit
>
> QSK50 CM2150 Power Generation with Advanced Engine Monitoring - Intake Manifold 2 Pressure Sensor Circuits
>
> ### Circuit Description
>
> The intake manifold 1 and 2 pressure sensors monitor intake manifold air pressure and pass information to the engine control module (ECM) through the engine harness. The ECM calculates a differential pressure between the left and right bank based on this information.
>
> ### Component Location
>
> The intake manifold 1 pressure sensors are located in the left and right bank front air intake manifold.
>
> ### Conditions For Running The Diagnostics
>
> - This diagnostic runs continuously when the ECM keyswitch is in the ON position.
>
> ### Conditions For Setting The Fault Codes
>
> - If the boost pressure differential between the left and right bank intake manifold pressure sensors exceeded a calibrated value for a calibrated amount of time, the fault will activate.
>
> ### Action Taken When The Fault Code Is Active
>
> - N/A
>
> ### Conditions For Clearing The Fault Code
>
> - N/A
>
> ### Shoptalk
>
> There are multiple ECMs for the engine models included in this manual. Each ECM has an individual source address that displays when INSITE™ electronic service tool is connected. When troubleshooting a fault code, use the source address displayed in INSITE™ electronic service tool to determine which ECM and circuit is affected.
>
> Possible causes of this fault code include:
>
> - Restricted air intake filters
>
> - An intake air system boost leak
>
> - A closed intake air shut off valve
>
> - An issue with one of the turbochargers
>
> - Multiple malfunctioning injectors on one bank.
>
> Refer to Troubleshooting Fault Code t05-3722.
