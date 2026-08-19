---
aliases:
  - "Ошибка датчика давления в топливной рампе"
type: "Процедура"
doc: "01-fc554"
title_en: "Fuel Rail Pressure Sensor Error"
title_ru: "Ошибка датчика давления в топливной рампе"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc554.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc554.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Fuel Rail Pressure Sensor Error
**Ошибка датчика давления в топливной рампе**

> [!abstract] Процедура · `01-fc554`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc554.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc554.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 554

### Ошибка датчика давления в топливной рампе

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 554 PID(P): СПН: ФМИ: Лампа: Предупреждение СТО: | Ошибка датчика давления топлива. Ошибка датчика давления в топливной рельсе, обнаруженная при включении ключа. Сигнал напряжения указывает на то, что сигнал датчика давления в топливном рельсе может быть ** не** точным. | Никаких действий со стороны ЕКМ не предпринималось. Возможная потеря производительности. |

![[19803583.png]]

Схема датчика давления в топливной рельсовой магистрали

### Описание цепи

Датчик давления топливной рельсы обеспечивает сигнал давления топливной рельсы к электронному модулю управления (ECM) через электропроводку двигателя. ECM использует сигнал давления рельсов топлива для контроля давления топлива, идущего к топливной форсунке от корпуса управляющего клапана.

### Расположение компонента

См. схемы двигателя. 100-002 для расположения компонентов.

Датчик давления топливной рельсы расположен с правой стороны, к нижней части ECVA, напротив привода топливной рельсы.

### Практические замечания

См. конкретную схему проводов двигателя для выходного напряжения датчика давления.

Примечание: Некоторые модели двигателей будут использовать разъем типа Metri-Pack на этом датчике давления, а некоторые будут использовать разъем типа DanfossTM. Контактные обозначения разъема Metri-Pack являются альфа-контактными, а контактные обозначения разъема DanfossTM числовыми. Шаги, изображенные в этом коде неисправности, показывают разъем типа Metri-Pack с вызывными альфа-пинами. См. конкретные схемы проводов двигателя, чтобы определить правильные указатели контактов для типа разъема.

См. Код устранения неполадок t05-554


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 554
>
> ### Fuel Rail Pressure Sensor Error
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 554 PID(P): SPN: FMI: Lamp: Warning SRT: | Fuel pressure sensor error. Fuel rail pressure sensor in-range error detected at key-on. Voltage signal indicates that the fuel rail pressure sensor signal can possibly **not** be accurate. | No action taken by the ECM. Possible loss of performance. |
>
> Fuel Rail Pressure Sensor Circuit
>
> ### Circuit Description
>
> The fuel rail pressure sensor provides the fuel rail pressure signal to the electronic control module (ECM), through the engine harness. The ECM uses the fuel rail pressure signal to monitor the fuel pressure going to the injectors from the control valve body.
>
> ### Component Location
>
> Refer to the Engine Diagrams. 100-002 for the component location.
>
> The fuel rail pressure sensor is located on the right side, toward the bottom of the ECVA, across from the fuel rail actuator.
>
> ### Shoptalk
>
> Refer to specific engine wiring diagram for the output voltage of the pressure sensor.
>
> Note: Some engine models will use the Metri-Pack type connector on this pressure sensor, and some will use the Danfoss™ type connector. The Metri-Pack connector pin designators are alpha and the Danfoss™ connector pin designators are numeric. The steps depicted in this fault code show the Metri-Pack type connector with alpha pin callouts. Refer to specific engine wiring diagrams to determine the correct pin designators for the type of connector.
>
> Refer to Troubleshooting Fault Code t05-554
