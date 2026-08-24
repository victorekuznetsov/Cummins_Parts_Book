---
aliases:
  - "Цепь датчика барометрического давления — замыкание на массу"
type: "Процедура"
doc: "01-fc222"
title_en: "Barometric Pressure Sensor Circuit - Shorted Low"
title_ru: "Цепь датчика барометрического давления — замыкание на массу"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc222.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc222.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Barometric Pressure Sensor Circuit - Shorted Low
**Цепь датчика барометрического давления — замыкание на массу**

> [!abstract] Процедура · `01-fc222`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc222.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc222.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 222

### Цепь датчика барометрического давления — замыкание на массу

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 222 PID(P): СПН: ФМИ: Лампа: Предупреждение СТО: | Барометрический датчик давления низко закорочен. | Отсутствие защиты двигателя от барометрического давления. Возможная потеря производительности. |

![[19803608.png]]

Схема датчика барометрического давления

### Описание цепи

Датчик барометрического давления обеспечивает барометрический сигнал давления воздуха к электронному модулю управления (ECM). ECM использует барометрический датчик давления для регулировки заправки в зависимости от высоты.

### Расположение компонента

См. схемы двигателя. 100-002 для расположения компонентов.

### Практические замечания

Мониторинг показания барометрического давления с помощью электронного инструментария службы, чтобы подтвердить, что показания давления соответствуют фактическому давлению воздуха.

См. конкретную схему проводов двигателя для выходного напряжения датчика давления.

Примечание: Некоторые модели двигателей будут использовать разъем типа Metri-Pack на этом датчике давления, а некоторые будут использовать разъем типа DanfossTM. Контактные обозначения разъема Metri-Pack являются альфа-контактными, а контактные обозначения разъема DanfossTM числовыми. Шаги, изображенные в этом коде неисправности, показывают разъем типа Metri-Pack с вызывными альфа-пинами. См. конкретные схемы проводов двигателя, чтобы определить правильные указатели контактов для типа разъема.

См. Код устранения неполадок t05-222


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 222
>
> ### Barometric Pressure Sensor Circuit - Shorted Low
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 222 PID(P): SPN: FMI: Lamp: Warning SRT: | Barometric pressure sensor is shorted low. | No engine protection for barometric pressure. Possible loss of performance. |
>
> Barometric Pressure Sensor Circuit
>
> ### Circuit Description
>
> The barometric pressure sensor provides the barometric air pressure signal to the electronic control module (ECM). The ECM uses the barometric pressure sensor to adjust fueling based on the altitude.
>
> ### Component Location
>
> Refer to the Engine Diagrams. 100-002 for the component location.
>
> ### Shoptalk
>
> Monitor the barometric pressure reading with an electronic service tool to confirm that the pressure reading matches the actual air pressure.
>
> Refer to specific engine wiring diagram for the output voltage of the pressure sensor.
>
> Note: Some engine models will use the Metri-Pack type connector on this pressure sensor, and some will use the Danfoss™ type connector. The Metri-Pack connector pin designators are alpha and the Danfoss™ connector pin designators are numeric. The steps depicted in this fault code show the Metri-Pack type connector with alpha pin callouts. Refer to specific engine wiring diagrams to determine the correct pin designators for the type of connector.
>
> Refer to Troubleshooting Fault Code t05-222
