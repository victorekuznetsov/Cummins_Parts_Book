---
aliases:
  - "Низкое давление моторного масла — критично"
type: "Процедура"
doc: "01-fc415"
title_en: "Engine Oil Pressure Low - Critical"
title_ru: "Низкое давление моторного масла — критично"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc415.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc415.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Engine Oil Pressure Low - Critical
**Низкое давление моторного масла — критично**

> [!abstract] Процедура · `01-fc415`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc415.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc415.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 415

### Низкое давление моторного масла — критично

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 415 PID(P): СПН: ФМИ: Лампа: Отключение SRT: | Низкое давление моторного масла — критично. Сигнал напряжения указывает на то, что давление масла упало ниже порога отключения для низкого давления масла. | Двигатель отключится. Водитель реле низкого давления масла под напряжением. |

![[19803594.png]]

Цепь датчика давления масла

### Описание цепи

Датчик давления масла используется электронным модулем управления (ECM) для мониторинга давления моторного масла. ECM контролирует напряжение на контакте сигнала и преобразует его в значение давления. Значение давления масла используется ECM для системы защиты двигателя.

### Расположение компонента

См. схемы двигателя. 100-002 для расположения компонентов.

### Практические замечания

Подтвердите, что напряжение питания датчика давления масла составляет от 4,75 до 5,25 ВДК на датчике. См. Код 141.Проверить с оператором, на какой скорости двигателя происходит неисправность. Если двигатель работает на слишком низкой скорости под нагрузкой (вспышка), давление масла может опускаться ниже пределов защиты двигателя из-за температуры масла. Давление масла является функцией скорости двигателя, уровня масла и функции регулятора. Работа двигателя на низкой скорости под нагрузкой будет ** не** привести к низкому давлению масла, если масло не нагревается, на низком уровне, регулятор неисправен, или потери происходят где-то в системе.

См. конкретную схему проводов двигателя для выходного напряжения датчика давления.

Примечание: Некоторые модели двигателей будут использовать разъем типа Metri-Pack на этом датчике давления, а некоторые будут использовать разъем типа DanfossTM. Контактные обозначения разъема Metri-Pack являются альфа-контактными, а контактные обозначения разъема DanfossTM числовыми. Шаги, изображенные в этом коде неисправности, показывают разъем типа Metri-Pack с вызывными альфа-пинами. См. конкретные схемы проводов двигателя, чтобы определить правильные указатели контактов для типа разъема.

Устранение неполадок код t05-415


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 415
>
> ### Engine Oil Pressure Low - Critical
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 415 PID(P): SPN: FMI: Lamp: Shutdown SRT: | Engine oil pressure low - critical. Voltage signal indicates oil pressure has dropped below the shutdown threshold for low oil pressure. | Engine will shut down. Low oil pressure relay driver is energized. |
>
> Oil Pressure Sensor Circuit
>
> ### Circuit Description
>
> The oil pressure sensor is used by the electronic control module (ECM) to monitor the lubricating oil pressure. The ECM monitors the voltage on the signal pin and converts this to a pressure value. The oil pressure value is used by the ECM for the engine protection system.
>
> ### Component Location
>
> Refer to the Engine Diagrams. 100-002 for the component location.
>
> ### Shoptalk
>
> Confirm that the oil pressure sensor supply voltage is between 4.75 and 5.25 VDC at the sensor. See Fault Code 141.Verify with the operator at what engine speed the fault occurs. If the engine is being operated at too low of a speed under load (lugging), the oil pressure can drop below the engine protection limits because of the oil temperature. Oil pressure is a function of engine speed, oil level, and regulator function. Operating the engine at a low speed under load will **not** cause the oil pressure to be low unless the oil is hot, at a low level, regulator has malfunctioned, or a loss is occurring somewhere in the system.
>
> Refer to specific engine wiring diagram for the output voltage of the pressure sensor.
>
> NOTE: Some engine models will use the Metri-Pack type connector on this pressure sensor, and some will use the Danfoss™ type connector. The Metri-Pack connector pin designators are alpha and the Danfoss™ connector pin designators are numeric. The steps depicted in this fault code show the Metri-Pack type connector with alpha pin callouts. Refer to specific engine wiring diagrams to determine the correct pin designators for the type of connector.
>
> Refer to Troubleshooting Fault Code t05-415
