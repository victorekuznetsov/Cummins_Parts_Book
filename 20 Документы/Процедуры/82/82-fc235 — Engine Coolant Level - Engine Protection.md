---
aliases:
  - "Уровень охлаждающей жидкости — защита двигателя"
type: "Процедура"
doc: "82-fc235"
title_en: "Engine Coolant Level - Engine Protection"
title_ru: "Уровень охлаждающей жидкости — защита двигателя"
modified: "2010-09-02"
engines:
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc235.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc235.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# Engine Coolant Level - Engine Protection
**Уровень охлаждающей жидкости — защита двигателя**

> [!abstract] Процедура · `82-fc235`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc235.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc235.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 235

### Уровень охлаждающей жидкости — защита двигателя

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 235 PID(P): P111 SPN: 111 FMI: 1/1 лампа: Красная СТО: | Сигнал уровня охлаждающей жидкости при контакте 22 разъёма проводов датчика указывает на то, что уровень охлаждающей жидкости ниже нормального диапазона. | Прогрессивная мощность и скорость снижаются с увеличением времени после оповещения. Если выключено отключение защиты двигателя, двигатель отключается через 30 секунд после того, как лампа защиты двигателя начинает мигать. |

![[19c00538.png]]

Уровень охлаждающей жидкости — защита двигателя

### Описание цепи

Датчик уровня охлаждающей жидкости контролирует уровень охлаждающей жидкости в системе охлаждающей жидкости и передает информацию в электронный модуль управления (ECM) через электропроводку двигателя. Поскольку этот датчик сложен, не используйте мультиметр для его проверки. Если уровень охлаждающей жидкости радиатора падает ниже определенного уровня, происходит постепенное снижение мощности и/или скорости. Двигатель может отключиться, если включена функция защиты двигателя.

### Расположение компонента

Датчик уровня охлаждающей жидкости расположен в верхнем резервуаре радиатора или резервуаре для перенапряжения.

### Практические замечания

Это компонент, поставляемый OEM, и может варьироваться в зависимости от местоположения.

- Если в цепи уровня охлаждающей жидкости используется штепсель, убедитесь, что он правильно подключен.

- Осмотрите проводную упряжку между четырехсторонним разъемом Weather-Pack и датчиком уровня охлаждающей жидкости на предмет повреждения.

- Убедитесь, что датчик уровня охлаждающей жидкости расположен в середине резервуара, а не с одной стороны, где уровень охлаждающей жидкости может измениться, когда автомобиль поворачивает угол.

См. Код устранения неполадок t05-235


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 235
>
> ### Engine Coolant Level - Engine Protection
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 235 PID(P): P111 SPN: 111 FMI: 1/1 Lamp: Red SRT: | Coolant level signal at pin 22 of the sensor harness connector indicates coolant level is below the normal range. | Progressive power and speed derate with increasing time after alert. If engine protection shutdown is enabled, engine will shut down 30 seconds after the engine protection lamp starts flashing. |
>
> Engine Coolant Level - Engine Protection
>
> ### Circuit Description
>
> The coolant level sensor monitors the coolant level within the coolant system and passes information to the electronic control module (ECM) through the engine harness. Because this sensor is complex, do **not** use a multimeter to check it. If the radiator coolant level drops below a certain level, a progressive power and/or speed derate will occur. Engine can shut down if the engine protection shutdown feature is enabled.
>
> ### Component Location
>
> The coolant level sensor is located in the radiator top tank or surge tank.
>
> ### Shoptalk
>
> This is an OEM-supplied component and can vary in location.
>
> - If a shorting plug is used in the coolant level circuit, verify that it is wired correctly.
>
> - Inspect the wiring harness between the Weather-Pack four-way connector and the coolant level sensor for damage.
>
> - Make sure the coolant level sensor is located in the middle of the tank rather than off to one side where the coolant level can change when the vehicle turns a corner.
>
> Refer to Troubleshooting Fault Code t05-235
