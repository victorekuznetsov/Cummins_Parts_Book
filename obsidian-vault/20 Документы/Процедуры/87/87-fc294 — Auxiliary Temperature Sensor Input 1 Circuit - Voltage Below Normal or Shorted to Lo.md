---
aliases:
  - "Цепь вспомогательного датчика температуры 1 — напряжение ниже нормы"
type: "Процедура"
doc: "87-fc294"
title_en: "Auxiliary Temperature Sensor Input 1 Circuit - Voltage Below Normal or Shorted to Low Source"
title_ru: "Цепь вспомогательного датчика температуры 1 — напряжение ниже нормы"
modified: "2018-08-09"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc294.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-fc294.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
  - "перевод/машинный"
---

# Auxiliary Temperature Sensor Input 1 Circuit - Voltage Below Normal or Shorted to Low Source
**Цепь вспомогательного датчика температуры 1 — напряжение ниже нормы**

> [!abstract] Процедура · `87-fc294`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2018-08-09
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc294.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-fc294.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 294

### Цепь вспомогательного датчика температуры 1 — напряжение ниже нормы

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 294 PID(P): P441 SPN: 441 FMI: 4 лампы: Янтарная СРТ: | Цепь вспомогательного датчика температуры 1 — напряжение ниже нормы. Напряжение, обнаруженное у изготовителя оригинального оборудования (OEM), контакт питания вспомогательного датчика температуры с левобережной проводкой OEM-интерфейса указывает на то, что датчик вышел из строя. | Ни одного на выступление. |

![[19n00476.png]]

OEM Вспомогательная схема датчика температуры

### Описание цепи

Вспомогательный датчик температуры OEM используется модулем управления двигателем (ECM) для мониторинга вспомогательной температуры OEM. Вспомогательный датчик температуры OEM, который не справился с низким уровнем, может быть вызван шортами, которые заземляются или открываются в проводах подачи и возврата, или внутренне заземленным датчиком.

### Расположение компонента

Расположение компонентов будет варьироваться в зависимости от OEM. См. сервисную документацию изготовителя оборудования.

### Практические замечания

Сопротивление всех датчиков температуры изменяется в зависимости от температуры. Проверьте температурные пороги с помощью электронного инструментария INSITETM для двигателей серии QST.

См. Код устранения неполадок t05-294


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 294
>
> ### Auxiliary Temperature Sensor Input 1 Circuit - Voltage Below Normal or Shorted to Low Source
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 294 PID(P): P441 SPN: 441 FMI: 4 Lamp: Amber SRT: | Auxiliary Temperature Sensor Input 1 Circuit - Voltage Below Normal or Shorted to Low Source. Voltage detected at the original equipment manufacturer (OEM) auxiliary temperature sensor supply pin of the left bank OEM interface wiring harness indicates the sensor has failed low. | None on performance. |
>
> OEM Auxiliary Temperature Sensor Circuit
>
> ### Circuit Description
>
> The OEM auxiliary temperature sensor supply is used by the engine control module (ECM) to monitor OEM auxiliary temperature. An OEM auxiliary temperature sensor that has failed low can be caused by shorts to ground or opens in the supply and return wires, or an internally grounded sensor.
>
> ### Component Location
>
> The component location will vary depending on the OEM. See equipment manufacturer service information.
>
> ### Shoptalk
>
> The resistance of all temperature sensors varies with the temperature. Check the temperature thresholds using INSITE™ electronic service tool for QST Series engines.
>
> Refer to Troubleshooting Fault Code t05-294
