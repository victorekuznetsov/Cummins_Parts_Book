---
aliases:
  - "Уровень охлаждающей жидкости — защита двигателя"
type: "Процедура"
doc: "87-fc235"
title_en: "Engine Coolant Level - Engine Protection"
title_ru: "Уровень охлаждающей жидкости — защита двигателя"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc235.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-fc235.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
  - "перевод/машинный"
---

# Engine Coolant Level - Engine Protection
**Уровень охлаждающей жидкости — защита двигателя**

> [!abstract] Процедура · `87-fc235`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc235.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-fc235.pdf)

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
| Код неисправности: 235 PID(P): P111 SPN: 111 FMI: 1 лампа: Защита двигателя SRT: | Обнаружен низкий уровень охлаждающей жидкости. Сигнал напряжения на уровне охлаждающей жидкости, контакт 37 проводов двигателя, указывает на низкий уровень охлаждающей жидкости радиатора на транспортном средстве. | Калибровочная зависимость прогрессивной мощности и скорости ухудшается, а выключение двигателя увеличивается с увеличением времени после оповещения. |

![[19a00217.png]]

Цепь датчика уровня охлаждающей жидкости

### Описание цепи

Датчик уровня охлаждающей жидкости контролирует уровень охлаждающей жидкости в системе охлаждающей жидкости и передает информацию в электронный модуль управления (ECM) через электропроводку двигателя.

### Расположение компонента

Датчик уровня охлаждающей жидкости расположен в верхнем резервуаре радиатора или резервуаре для перенапряжения.

### Практические замечания

Это компонент, поставляемый OEM, и он будет варьироваться в зависимости от местоположения датчика.

- Когда уровень охлаждающей жидкости падает ниже определенного уровня, происходит снижение мощности, снижение скорости или отключение.

- Если в цепи уровня охлаждающей жидкости используется штепсель, убедитесь, что он правильно подключен.

- Проверьте проводку между 4-контактным разъемом Weather-Pack и датчиком уровня охлаждающей жидкости на предмет повреждения.

- Убедитесь, что датчик уровня охлаждающей жидкости расположен в середине резервуара, а не с одной стороны, где уровень охлаждающей жидкости может измениться, когда автомобиль поворачивает угол.

Примечание: Количество неисправных ламп может быть сокращено до двух для некоторых OEM-производителей. Защита двигателя и стоп-сигналы соединены вместе как красная лампа. Предупреждающая лампа остается желтой лампой.

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
> | Fault Code: 235 PID(P): P111 SPN: 111 FMI: 1 Lamp: Engine Protection SRT: | Low coolant level has been detected. Voltage signal on the coolant level signal pin 37 of the engine harness indicates low radiator coolant level on the vehicle. | Calibration-dependent progressive power and speed derate and engine shutdown with increasing time after alert. |
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
> - When the coolant level drops below a certain level, a power derate, speed derate, or shutdown will be activated.
>
> - If a shorting plug is used in the coolant level circuit, verify that it is wired correctly.
>
> - Inspect the wiring harness between the 4-pin Weather-Pack connector and the coolant level sensor for damage.
>
> - Make sure the coolant level sensor is located in the middle of the tank rather than off to one side where the coolant level can change when the vehicle turns a corner.
>
> Note: The number of fault lamps could be reduced to two for certain OEMs. The engine protection and stop lamps are wired together as a red lamp. The warning lamp remains a yellow lamp.
>
> Refer to Troubleshooting Fault Code t05-235
