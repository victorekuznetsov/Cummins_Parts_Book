---
aliases:
  - "Давление масла в главной магистрали ниже нормы — наивысший уровень"
type: "Процедура"
doc: "82-fc415"
title_en: "Engine Oil Rifle Pressure - Data Valid But Below Normal Operating Range - Most Severe Level"
title_ru: "Давление масла в главной магистрали ниже нормы — наивысший уровень"
modified: "2017-06-19"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc415.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc415.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# Engine Oil Rifle Pressure - Data Valid But Below Normal Operating Range - Most Severe Level
**Давление масла в главной магистрали ниже нормы — наивысший уровень**

> [!abstract] Процедура · `82-fc415`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2017-06-19
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc415.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc415.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 415

### Давление масла в главной магистрали ниже нормы — наивысший уровень

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 415 PID(P): СПН: ФМИ: Лампа: Отключение SRT: | Давление масла в главной магистрали ниже нормы — наивысший уровень. Сигнал напряжения указывает на то, что давление масла упало ниже порога отключения для низкого давления масла. | Двигатель отключится. Водитель реле низкого давления масла под напряжением. |

![[19c00506.png]]

Цепь датчика давления масла

### Описание цепи

Датчик давления масла используется электронным модулем управления (ECM) для мониторинга давления моторного масла. ECM контролирует напряжение на контакте сигнала и преобразует его в значение давления. Значение давления масла используется ECM для системы защиты двигателя.

### Расположение компонента

См. схемы двигателя.[[82-100-002 — Engine Diagrams|См. процедуру 100-002 в разделе E.]]месторасположение компонента.

### Практические замечания

Подтвердите, что напряжение питания датчика давления масла составляет от 4,75 до 5,25 ВДК на датчике. См. Код 141. Проверьте с оператором, на какой скорости двигателя происходит неисправность. Если двигатель работает со скоростью до низкой под нагрузкой (вход), давление масла может опускаться ниже пределов защиты двигателя из-за температуры масла. Давление масла является функцией скорости двигателя, уровня масла и функции регулятора. Работа двигателя на низкой скорости под нагрузкой будет **не** привести к низкому давлению масла, если масло не нагревается, на низком уровне, регулятор неисправен, или потери происходят где-то в системе.

- См. конкретную схему проводов двигателя для выходного напряжения датчика давления.

- Примечание: Некоторые модели двигателей будут использовать разъем типа Metri-Pack на этом датчике давления, а некоторые будут использовать разъем типа DanfossTM. Контактные обозначения разъема Metri-Pack являются альфа-контактными, а контактные обозначения разъема DanfossTM числовыми. Шаги, изображенные в этом коде неисправности, показывают разъем типа Metri-Pack с вызывными альфа-пинами. См. конкретные схемы проводов двигателя, чтобы определить правильные указатели контактов для типа разъема.

См. Код устранения неполадок t05-415.


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 415
>
> ### Engine Oil Rifle Pressure - Data Valid But Below Normal Operating Range - Most Severe Level
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 415 PID(P): SPN: FMI: Lamp: Shutdown SRT: | Engine Oil Rifle Pressure - Data Valid But Below Normal Operating Range - Most Severe Level. Voltage signal indicates oil pressure has dropped below the shutdown threshold for low oil pressure. | Engine will shut down. Low oil pressure relay driver is energized. |
>
> Oil Pressure Sensor Circuit
>
> ### Circuit Description
>
> The oil pressure sensor is used by the electronic control module (ECM) to monitor the lubricating oil pressure. The ECM monitors the voltage on the SIGNAL pin and converts this to a pressure value. The oil pressure value is used by the ECM for the engine protection system.
>
> ### Component Location
>
> Refer to the Engine Diagrams. [[82-100-002 — Engine Diagrams|Refer to Procedure 100-002 in Section E]] for the component location.
>
> ### Shoptalk
>
> Confirm that the oil pressure sensor supply voltage is between 4.75 and 5.25 VDC at the sensor. See Fault Code 141. Verify with the operator at what engine speed the fault occurs. If the engine is being operated a speed to low under load (lugging), the oil pressure can drop below the engine protection limits because of the oil temperature. Oil pressure is a function of engine speed, oil level, and regulator function. Operating the engine at a low speed under load will **not** cause the oil pressure to be low unless the oil is hot, at a low level, regulator has malfunctioned, or a loss is occurring somewhere in the system.
>
> - Refer to specific engine wiring diagram for the output voltage of the pressure sensor.
>
> - NOTE: Some engine models will use the Metri-Pack type connector on this pressure sensor, and some will use the Danfoss™ type connector. The Metri-Pack connector pin designators are alpha and the Danfoss™ connector pin designators are numeric. The steps depicted in this fault code show the Metri-Pack type connector with alpha pin callouts. Refer to specific engine wiring diagrams to determine the correct pin designators for the type of connector.
>
> Refer to Troubleshooting Fault Code t05-415.
