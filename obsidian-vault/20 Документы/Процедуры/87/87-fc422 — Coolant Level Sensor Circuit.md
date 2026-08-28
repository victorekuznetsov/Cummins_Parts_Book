---
aliases:
  - "Цепь датчика уровня охлаждающей жидкости"
type: "Процедура"
doc: "87-fc422"
title_en: "Coolant Level Sensor Circuit"
title_ru: "Цепь датчика уровня охлаждающей жидкости"
modified: "2010-07-29"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc422.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-fc422.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
  - "перевод/машинный"
---

# Coolant Level Sensor Circuit
**Цепь датчика уровня охлаждающей жидкости**

> [!abstract] Процедура · `87-fc422`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc422.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-fc422.pdf)

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
| Код неисправности: 422 PID(P): P111 SPN: 111 FMI: 2 лампы: Желтая СТО: | Напряжение, обнаруженное одновременно как на уровне охлаждающей жидкости, так и на низком и высоком сигнальных контактах 27 и 37 электропроводки двигателя, или на любом из контактов напряжения, обнаруженного на штифте. | Защита двигателя от уровня охлаждающей жидкости отключена. |

![[19a00217.png]]

Цепь датчика уровня охлаждающей жидкости

### Описание цепи

Датчик уровня охлаждающей жидкости контролирует уровень охлаждающей жидкости в системе охлаждающей жидкости и передает информацию в электронный модуль управления (ECM) через электропроводку двигателя.

### Расположение компонента

Датчик уровня охлаждающей жидкости расположен в верхнем резервуаре радиатора или резервуаре для перенапряжения.

### Практические замечания

Это компонент, поставляемый OEM, и он будет варьироваться в зависимости от местоположения датчика.

- Если в цепи уровня охлаждающей жидкости используется штепсель, убедитесь, что он правильно подключен.

- Проверьте проводку между 4-контактным разъемом Weather-Pack и датчиком уровня охлаждающей жидкости на предмет повреждения.

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
> | Fault Code: 422 PID(P): P111 SPN: 111 FMI: 2 Lamp: Yellow SRT: | Voltage detected simultaneously on both the coolant level high and low signal pins 27 and 37 of the engine harness, or no voltage detected on either pin. | Engine protection for coolant level is disabled. |
>
> Coolant Level Sensor Circuit
>
> ### Circuit Description
>
> The coolant level sensor monitors the coolant level within the coolant system and passes information to the electronic control module (ECM) through the engine harness.
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
> - Inspect the wiring harness between the 4-pin Weather-Pack connector and the coolant level sensor for damage.
>
> Refer to Troubleshooting Fault Code t05-422
