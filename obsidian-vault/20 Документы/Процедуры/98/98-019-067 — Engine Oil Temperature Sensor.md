---
aliases:
  - "Датчик температуры моторного масла"
type: "Процедура"
doc: "98-019-067"
title_en: "Engine Oil Temperature Sensor"
title_ru: "Датчик температуры моторного масла"
modified: "2003-04-01"
engines:
  - "37269910"
  - "37280605"
families:
  - "K19"
manuals:
  - "3666070"
figures: 8
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-019-067.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-019-067.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K19"
  - "группа/98"
  - "перевод/машинный"
---

# Engine Oil Temperature Sensor
**Датчик температуры моторного масла**

> [!abstract] Процедура · `98-019-067`
> **Двигатели:** [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]]
> **Семейство:** K19
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-04-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-019-067.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-019-067.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Датчик температуры масла отправляет информацию о температуре масла двигателя в ECM. Расположение датчика варьируется в зависимости от семейства двигателей. Смотрите соответствующее руководство по базовому двигателю.

> [!note] Примечание
> Не все приложения CENTRYTM будут использовать этот датчик. См. руководство OEM для системных функций.

![[19801851.png]]

### Снятие

Убедитесь, что разъем датчика отключен. Удалите датчик.

![[19801853.png]]

### Установка

Убедитесь, что новый датчик имеет кольцо. Смажьте уплотнительное кольцо чистым моторным маслом.

Установите новый датчик в двигатель. Затяните датчик.

> [!tip] Момент затяжки
> 35 Н·м [26 фунт-фут]

![[19801860.png]]

Подключите разъем датчика. Убедитесь, что разъём запирается на месте.

![[19801861.png]]

### Проверка сопротивления

Отключите разъем датчика. Выберите функцию сопротивления на мультиметре. Прикрепите соответствующий испытательный щуп к многометровым зондам. Прикоснитесь к двум испытательным зондам на датчике. Измерьте сопротивление. Мультиметр **должен **показывать от 115 до 244k ом. Значение сопротивления зависит от температуры, как показано в таблице ниже.

| температура | температура | диапазон |
|---|---|---|
| (°C) | \[°F\] | (Омс) |
| 0 | 32 | 33k до 36k |
| 25 | 77 | 9k до 11k |
| 50 | 122 | 3k - 4k |
| 75 | 167 | 1350—1500 |
| 100 | 212 | 600-675 |

![[19801852.png]]

Если сопротивление находится вне диапазона, то датчик вышел из строя.

Замените датчик.

![[19801853.png]]

### Проверка на замыкание на массу

Прикоснитесь к многометровому свинцу с помощью прикрепленного соответствующего испытательного щупа к любому терминалу на датчике. Прикосновение к другому мультиметру приводит к хорошей, чистой поверхности на блоке двигателя.

![[19801854.png]]

Измерьте сопротивление.

Мультиметр **должен **показывать более 100k ом, что является открытой схемой. Если цепь **не **закрыта, то внутри датчика есть короткое расстояние до земли шасси.

Замените датчик.

![[19801621.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> The oil temperature sensor sends engine oil temperature information to the ECM. The location of the sensor varies with engine family. Refer to the appropriate base engine manual.
>
> **Note · Примечание**
> **Not** all CENTRY™ applications will use this sensor. Refer to the OEM manual for system features.
>
> ### Remove
>
> Make sure the sensor connector is disconnected. Remove the sensor.
>
> ### Install
>
> Verify that the new sensor has an o-ring. Lubricate the o-ring with clean engine oil.
>
> Install the new sensor into the engine. Tighten the sensor.
>
> **Момент затяжки · Torque Value**
> 35 n•m [26 ft-lb]
>
> Connect the sensor connector. Make sure the connector locks into place.
>
> ### Resistance Check
>
> Disconnect the sensor connector. Select the resistance function on the multimeter. Attach the appropriate test leads to the multimeter probes. Touch the two test leads to the two terminals on the sensor. Measure the resistance. The multimeter **must** show between 115 and 244k ohms. The resistance value is temperature-dependent as shown in the table below.
>
> | Temperature | Temperature | Range |
> |---|---|---|
> | (°C) | \[°F\] | (ohms) |
> | 0 | 32 | 33k to 36k |
> | 25 | 77 | 9k to 11k |
> | 50 | 122 | 3k to 4k |
> | 75 | 167 | 1350 to 1500 |
> | 100 | 212 | 600 to 675 |
>
> If the resistance is out of range, then the sensor has failed.
>
> Replace the sensor.
>
> ### Check for Short Circuit to Ground
>
> Touch the multimeter lead with the attached appropriate test lead to either terminal on the sensor. Touch the other multimeter lead to a good, clean surface on the engine block.
>
> Measure the resistance.
>
> The multimeter **must** show greater than 100k ohms, which is an open circuit. If the circuit is **not** closed, then there is a short within the sensor to chassis ground.
>
> Replace the sensor.
