---
aliases:
  - "Цепь датчика давления коллектора 1 — замыкание на массу"
type: "Процедура"
doc: "01-fc123"
title_en: "Intake Manifold Pressure Sensor 1 Circuit - Shorted Low"
title_ru: "Цепь датчика давления коллектора 1 — замыкание на массу"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc123.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc123.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Intake Manifold Pressure Sensor 1 Circuit - Shorted Low
**Цепь датчика давления коллектора 1 — замыкание на массу**

> [!abstract] Процедура · `01-fc123`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc123.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc123.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 123

### Цепь датчика давления коллектора 1 — замыкание на массу

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 123 P(P): СПН: ФМИ: Лампа: Предупреждение СТО: | Цепь датчика давления коллектора 1 — замыкание на массу. | Никаких действий со стороны ЕКМ не предпринимается. Возможная потеря производительности. |

![[19803594.png]]

Схема датчика давления Manifold 1

### Описание цепи

Датчик давления впускного коллектора контролирует давление повышения и передает информацию в электронный модуль управления (ECM). Низкое напряжение будет сбивать Код 123 по умолчанию и может быть вызвано шортами в подаче, сигнале или возвратных проводах, открытым в подаче или сигнальных проводах, низким напряжением питания от ECM или неисправным датчиком.

### Расположение компонента

См. схемы двигателя. 100-002 для расположения компонентов.

### Практические замечания

Проверьте наличие высокого ограничения в впускном коллекторе воздуха из-за засорения воздушных фильтров или выключателя в коллекторе. **Не удаляйте это устройство, если двигатель работает в легковоспламеняющейся атмосфере. Устройство является важной функцией безопасности.

Убедитесь, что турбокомпрессор работает правильно. Проверьте положительное давление коллектора потребления.

См. конкретную схему проводов двигателя для выходного напряжения датчика давления.

Примечание: Некоторые модели двигателей будут использовать разъем типа Metri-Pack на этом датчике давления, а некоторые будут использовать разъем типа DanfossTM. Контактные обозначения разъема Metri-Pack являются альфа-контактными, а контактные обозначения разъема DanfossTM числовыми. Шаги, изображенные в этом коде неисправности, показывают разъем типа Metri-Pack с вызывными альфа-пинами. См. конкретные схемы проводов двигателя, чтобы определить правильные указатели контактов для типа разъема.

См. Устранение неполадок код t05-123


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 123
>
> ### Intake Manifold Pressure Sensor 1 Circuit - Shorted Low
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 123 PID(P): SPN: FMI: Lamp: Warning SRT: | Intake manifold pressure sensor 1 circuit - shorted low. | No action is taken by the ECM. Possible loss of performance. |
>
> Intake Manifold Pressure Sensor 1 Circuit
>
> ### Circuit Description
>
> The intake manifold pressure sensor monitors boost pressure and passes information to the electronic control module (ECM). Low voltage will trip Fault Code 123 and can be caused by shorts in the supply, signal, or return wires, an open in the supply or signal wires, low supply voltage from the ECM, or a failed sensor.
>
> ### Component Location
>
> Refer to the Engine Diagrams. 100-002 for the component location.
>
> ### Shoptalk
>
> Check for high restriction in the intake air manifold due to clogged air filters or a shutdown device in the manifold. Do **not** remove this device, if the engine is operated in a flammable atmosphere. The device is an essential safety feature.
>
> Make sure the turbocharger is working correctly. Check for a positive intake manifold pressure.
>
> Refer to specific engine wiring diagram for the output voltage of the pressure sensor.
>
> Note: Some engine models will use the Metri-Pack type connector on this pressure sensor, and some will use the Danfoss™ type connector. The Metri-Pack connector pin designators are alpha and the Danfoss™ connector pin designators are numeric. The steps depicted in this fault code show the Metri-Pack type connector with alpha pin callouts. Refer to specific engine wiring diagrams to determine the correct pin designators for the type of connector.
>
> Refer to Troubleshooting Fault Code t05-123
