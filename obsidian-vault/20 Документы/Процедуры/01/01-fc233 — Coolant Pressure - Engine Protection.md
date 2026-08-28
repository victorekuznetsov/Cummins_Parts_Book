---
aliases:
  - "Давление охлаждающей жидкости — защита двигателя"
type: "Процедура"
doc: "01-fc233"
title_en: "Coolant Pressure - Engine Protection"
title_ru: "Давление охлаждающей жидкости — защита двигателя"
modified: "2010-07-29"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc233.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc233.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Coolant Pressure - Engine Protection
**Давление охлаждающей жидкости — защита двигателя**

> [!abstract] Процедура · `01-fc233`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc233.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc233.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 233

### Давление охлаждающей жидкости — защита двигателя

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 233 PID(P): СПН: ФМИ: Лампа: Предупреждение СТО: | Давление охлаждающей жидкости двигателя низкое - предупреждение. Сигнал напряжения указывает на то, что давление охлаждающей жидкости упало ниже порога предупреждения о низком давлении охлаждающей жидкости. | Выключение двигателя, зависящее от калибровки, происходит, или ECM принимает меры. |

![[19803583.png]]

Цепь датчика давления охлаждающей жидкости

### Описание цепи

Датчик давления охлаждающей жидкости используется электронным модулем управления (ECM) для мониторинга давления охлаждающей жидкости. ECM контролирует напряжение на контакте сигнала и преобразует его в значение давления. Значение давления охлаждающей жидкости используется ECM для системы защиты двигателя.

### Расположение компонента

См. схемы двигателя. 100-002 для расположения компонентов.

### Практические замечания

Подтвердите, что источник питания датчика охлаждающей жидкости находится между 4,75 и 5,25 ВДК на датчике. См. Код 232.

См. конкретную схему проводов двигателя для выходного напряжения датчика давления.

Примечание: Некоторые модели двигателей будут использовать разъем типа Metri-Pack на этом датчике давления, а некоторые будут использовать разъем типа DanfossTM. Контактные обозначения разъема Metri-Pack являются альфа-контактными, а контактные обозначения разъема DanfossTM числовыми. Шаги, изображенные в этом коде неисправности, показывают разъем типа Metri-Pack с вызывными альфа-пинами. См. конкретные схемы проводов двигателя, чтобы определить правильные указатели контактов для типа разъема.

См. Код устранения неполадок t05-233


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 233
>
> ### Coolant Pressure - Engine Protection
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 233 PID(P): SPN: FMI: Lamp: Warning SRT: | Engine coolant pressure low - warning. Voltage signal indicates coolant pressure has dropped below the warning threshold for low coolant pressure. | Calibration-dependent engine shutdown occurs, or **not** action is taken by ECM. |
>
> Coolant Pressure Sensor Circuit
>
> ### Circuit Description
>
> The coolant pressure sensor is used by the electronic control module (ECM) to monitor coolant pressure. The ECM monitors the voltage on the signal pin and converts this to a pressure value. The coolant pressure value is used by the ECM for the engine protection system.
>
> ### Component Location
>
> Refer to the Engine Diagrams. 100-002 for the component location.
>
> ### Shoptalk
>
> Confirm that the coolant sensor supply is between 4.75 and 5.25 VDC at the sensor. See Fault Code 232.
>
> Refer to specific engine wiring diagram for the output voltage of the pressure sensor.
>
> NOTE: Some engine models will use the Metri-Pack type connector on this pressure sensor, and some will use the Danfoss™ type connector. The Metri-Pack connector pin designators are alpha and the Danfoss™ connector pin designators are numeric. The steps depicted in this fault code show the Metri-Pack type connector with alpha pin callouts. Refer to specific engine wiring diagrams to determine the correct pin designators for the type of connector.
>
> Refer to Troubleshooting Fault Code t05-233
