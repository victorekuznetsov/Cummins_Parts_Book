---
aliases:
  - "Цепь датчика уровня охлаждающей жидкости"
type: "Процедура"
doc: "82-fc422"
title_en: "Coolant Level Sensor Circuit"
title_ru: "Цепь датчика уровня охлаждающей жидкости"
modified: "2010-09-02"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc422.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc422.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# Coolant Level Sensor Circuit
**Цепь датчика уровня охлаждающей жидкости**

> [!abstract] Процедура · `82-fc422`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc422.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc422.pdf)

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
| Код неисправности: 422 PID(P): P111 SPN: 111 FMI: 2/2 лампы: Желтая СТО: | Напряжение, обнаруживаемое одновременно как на высоко-, так и на низко-сигнальных цепях уровня охлаждающей жидкости **или**, не обнаруживается на **обеих цепях***. | Отсутствие защиты двигателя для уровня охлаждающей жидкости. |

![[19c00538.png]]

Цепь датчика уровня охлаждающей жидкости

### Описание цепи

Датчик уровня охлаждающей жидкости контролирует уровень охлаждающей жидкости в системе охлаждающей жидкости и передает информацию в электронный модуль управления (ECM) через проводку датчика. Этот датчик очень сложный. Не используйте мультиметр для проверки датчика уровня охлаждающей жидкости. Если уровень охлаждающей жидкости радиатора падает ниже определенного уровня, произойдет снижение мощности и со временем станет больше.

### Расположение компонента

Датчик уровня охлаждающей жидкости расположен в верхнем резервуаре радиатора или резервуаре для перенапряжения.

### Практические замечания

Возможные причины этого кода неисправности включают:

- Открытая схема

- Короткое замыкание на землю

- Короткое замыкание на другой провод.

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
> | Fault Code: 422 PID(P): P111 SPN: 111 FMI: 2/2 Lamp: Yellow SRT: | Voltage detected simultaneously on both the coolant level high and low signal circuits **or** no voltage detected on **both** circuits. | No engine protection for coolant level. |
>
> Coolant Level Sensor Circuit
>
> ### Circuit Description
>
> The coolant level sensor monitors the coolant level within the coolant system and passes information to the electronic control module (ECM) through the sensor harness. This sensor is very complex. Do **not** use a multimeter to check the coolant level sensor. If the radiator coolant level drops below a certain level, a power derate will occur and become greater as time goes by.
>
> ### Component Location
>
> The coolant level sensor is located in the radiator top tank or surge tank.
>
> ### Shoptalk
>
> Possible causes for this fault code include:
>
> - Open circuit
>
> - Short circuit to ground
>
> - Short circuit to another wire.
>
> Refer to Troubleshooting Fault Code t05-422
