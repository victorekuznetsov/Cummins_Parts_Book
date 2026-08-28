---
aliases:
  - "Цепь датчика уровня охлаждающей жидкости"
type: "Процедура"
doc: "19-fc422"
title_en: "Coolant Level Sensor Circuit"
title_ru: "Цепь датчика уровня охлаждающей жидкости"
modified: "2011-03-01"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
  - "85017333"
families:
  - "QSK23"
  - "QSK60"
manuals:
  - "3666113"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc422.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc422.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
  - "перевод/машинный"
---

# Coolant Level Sensor Circuit
**Цепь датчика уровня охлаждающей жидкости**

> [!abstract] Процедура · `19-fc422`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2011-03-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc422.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc422.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 422

### Цепь датчика уровня охлаждающей жидкости

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 422 PID(P): P111 SPN: 111 FMI: 2 лампы: Желтая СТО: 00-368 | Напряжение, обнаруживаемое одновременно как на уровне охлаждающей жидкости, так и на низком и высоком сигнальных контактах 14 и 23 проводов OEM-интерфейса, или на любом из контактов не обнаруживается напряжение. | Отсутствие защиты двигателя для уровня охлаждающей жидкости. |

![[19600211.png]]

Цепь датчика уровня охлаждающей жидкости

### Описание цепи

Датчик уровня охлаждающей жидкости контролирует уровень охлаждающей жидкости в системе охлаждающей жидкости и передает информацию в ECM через проводную упряжку OEM.

### Расположение компонента

Датчик уровня охлаждающей жидкости расположен в верхнем резервуаре радиатора или резервуаре для перенапряжения.

### Практические замечания

Это компонент, поставляемый OEM, и он будет варьироваться в зависимости от местоположения датчика.

- Если в цепи уровня охлаждающей жидкости используется штепсель, убедитесь, что он правильно подключен.

- Осмотрите проводную упряжку между четырехсторонним разъемом Weather-Pack и датчиком уровня охлаждающей жидкости на предмет повреждения.

- Убедитесь, что датчик уровня охлаждающей жидкости расположен в середине резервуара, а не с одной стороны, где уровень охлаждающей жидкости может измениться, когда транспортное средство делает поворот.

Существует дополнительная конфигурация схемы датчика уровня охлаждающей жидкости, которая включает в себя датчик воды в топливе. Эта дополнительная конфигурация проиллюстрирована выше.

См. Код устранения неполадок t05-422


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 422
>
> ### Coolant Level Sensor Circuit
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 422 PID(P): P111 SPN: 111 FMI: 2 Lamp: Yellow SRT: 00-368 | Voltage detected simultaneously on both the coolant level high and low signal pins 14 and 23 of the OEM interface harness, or no voltage detected on either pin. | No engine protection for coolant level. |
>
> Coolant Level Sensor Circuit
>
> ### Circuit Description
>
> The coolant level sensor monitors the coolant level within the coolant system and passes information to the ECM through the OEM harness.
>
> ### Component Location
>
> The coolant level sensor is located in the radiator top tank or surge tank.
>
> ### Shoptalk
>
> This is an OEM-supplied component and will vary in sensor location.
>
> - If a shorting plug is used in the coolant level circuit, verify that it is wired correctly.
>
> - Inspect the wiring harness between the Weather-Pack four-way connector and the coolant level sensor for damage.
>
> - Make sure the coolant level sensor is located in the middle of the tank rather than off to one side where the coolant level can change when the vehicle makes a turn.
>
> There is an optional configuration of the coolant level sensor circuit that includes a water-in-fuel sensor. This optional configuration is illustrated above.
>
> Refer to Troubleshooting Fault Code t05-422
