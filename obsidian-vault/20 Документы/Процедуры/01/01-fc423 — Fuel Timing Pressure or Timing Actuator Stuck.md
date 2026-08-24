---
aliases:
  - "Заклинивание давления или привода опережения впрыска"
type: "Процедура"
doc: "01-fc423"
title_en: "Fuel Timing Pressure or Timing Actuator Stuck"
title_ru: "Заклинивание давления или привода опережения впрыска"
modified: "2023-06-09"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc423.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc423.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Fuel Timing Pressure or Timing Actuator Stuck
**Заклинивание давления или привода опережения впрыска**

> [!abstract] Процедура · `01-fc423`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2023-06-09
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc423.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc423.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 423

### Заклинивание давления или привода опережения впрыска

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 423 PID(P): СПН: ФМИ: Лампа: Предупреждение СТО: | Заклинивание давления или привода опережения впрыска. Обнаружена ошибка датчика давления в диапазоне. Сигнал напряжения указывает на то, что сигнал датчика давления во времени может быть ** не** точным. | Никаких действий со стороны ЕКМ не предпринималось. Возможная потеря производительности. |

![[19803583.png]]

Схема датчика давления на железной дороге

### Описание цепи

Датчик давления рельсов синхронизации обеспечивает сигнал давления рельсов синхронизации электронному модулю управления (ECM) через ремень электропроводки двигателя. ECM использует сигнал давления рельсов синхронизации для контроля давления топлива синхронизации, идущего в камеру синхронизации топливного форсунка от корпуса управляющего клапана.

### Расположение компонента

Датчик давления синхронизации топлива расположен справа, в верхней части ECVA. Вне привода временной рельсовой дороги.

### Практические замечания

См. конкретную схему проводов двигателя для выходного напряжения датчика давления.

Примечание: Некоторые модели двигателей будут использовать разъем типа Metri-Pack на этом датчике давления, а некоторые будут использовать разъем типа DanfossTM. Контактные обозначения разъема Metri-Pack являются альфа-контактными, а контактные обозначения разъема DanfossTM числовыми. Шаги, изображенные в этом коде неисправности, показывают разъем типа Metri-Pack с вызывными альфа-пинами. См. конкретные схемы проводов двигателя, чтобы определить правильные указатели контактов для типа разъема.

См. Код устранения неполадок t05-423


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 423
>
> ### Fuel Timing Pressure or Timing Actuator Stuck
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 423 PID(P): SPN: FMI: Lamp: Warning SRT: | Fuel timing pressure or timing actuator stuck. Timing pressure sensor in-range error detected. Voltage signal indicates that the timing pressure sensor signal can possibly **not** be accurate. | No action taken by the ECM. Possible loss of performance. |
>
> Timing Rail Pressure Sensor Circuit
>
> ### Circuit Description
>
> The timing rail pressure sensor provides the timing rail pressure signal to the electronic control module (ECM), through the engine harness. The ECM uses the timing rail pressure signal to monitor the timing fuel pressure going to the injector's timing chamber from the control valve body.
>
> ### Component Location
>
> The fuel timing pressure sensor is located on the right, towards the top of the ECVA. Across from the timing rail actuator.
>
> ### Shoptalk
>
> Refer to specific engine wiring diagram for the output voltage of the pressure sensor.
>
> Note: Some engine models will use the Metri-Pack type connector on this pressure sensor, and some will use the Danfoss™ type connector. The Metri-Pack connector pin designators are alpha and the Danfoss™ connector pin designators are numeric. The steps depicted in this fault code show the Metri-Pack type connector with alpha pin callouts. Refer to specific engine wiring diagrams to determine the correct pin designators for the type of connector.
>
> Refer to Troubleshooting Fault Code t05-423
