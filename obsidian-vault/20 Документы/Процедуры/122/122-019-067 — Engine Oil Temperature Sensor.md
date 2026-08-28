---
aliases:
  - "Датчик температуры моторного масла"
type: "Процедура"
doc: "122-019-067"
title_en: "Engine Oil Temperature Sensor"
title_ru: "Датчик температуры моторного масла"
modified: "2017-04-21"
engines:
  - "33239746"
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
manuals:
  - "4022102"
figures: 7
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-019-067.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/122-019-067.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/122"
  - "перевод/машинный"
---

# Engine Oil Temperature Sensor
**Датчик температуры моторного масла**

> [!abstract] Процедура · `122-019-067`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Входит в руководства:** [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M|4022102]]
> **Секции:** Section 19 - Electronic Controls
> **Даты:** изменён 2017-04-21
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-019-067.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/122-019-067.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Датчик температуры масла отправляет информацию о температуре масла двигателя в модуль управления двигателем (ECM). Точное местоположение датчика варьируется в зависимости от семейства двигателей. Смотрите соответствующее руководство по базовому двигателю.

![[19801851.png]]

### Снятие

> [!danger] ОПАСНО
> Некоторые государственные и федеральные агентства в Соединенных Штатах Америки определили, что используемое моторное масло может быть канцерогенным и может вызывать репродуктивную токсичность. Не вдыхайте пары, не допускайте попадания внутрь и длительного контакта с отработанным моторным маслом. Всегда используйте надлежащие экологические процедуры для утилизации масла.

Частично осушить систему моторного масла двигателя. См. процедуру 007-037 в разделе 7.

Поднимите на запирающую вкладку и разберите электрические разъемы.

Удалите датчик.

![[19800823.png]]

### Проверка сопротивления

Отключите разъем датчика.

Выберите функцию сопротивления на мультиметре.

Прикрепите соответствующий испытательный щуп к многометровым зондам.

Прикоснитесь к двум испытательным зондам на датчике. Измерьте сопротивление.

Мультиметр **должен **показывать от 115 до 244k ом. Значение сопротивления зависит от температуры, как показано в таблице ниже.

| температура | диапазон |  |
|---|---|---|
| °C | градус | Омс |
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

Мультиметр **должен **показывать более 100k ом, что является открытой схемой. Если цепь **не **закрыта, то внутри датчика есть короткое расстояние до земли шасси. Замените датчик.

![[19801621.png]]

### Установка

Убедитесь, что новый датчик имеет кольцо.

Смазать сенсорное кольцо чистым моторным маслом.

Установите датчик в двигатель.

Затяните датчик.

> [!tip] Момент затяжки
> 15 Н·м [11 фунт-фут]

Соедините разъёмы до фиксации.

Заполните двигатель до надлежащего уровня моторным маслом и работайте с двигателем, чтобы проверить наличие утечек.

![[19800824.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> The oil temperature sensor sends engine oil temperature information to the engine control module (ECM). The exact location of the sensor varies with engine family. Refer to the appropriate base engine manual.
>
> ### Remove
>
> **WARNING · Опасно**
> Some state and federal agencies in the United States of America have determined that used engine oil can be carcinogenic and can cause reproductive toxicity. Avoid inhalation of vapors, ingestion, and prolonged contact with used engine oil. Always use the proper environmental procedures to dispose of the oil.
>
> Partially drain the engine lubricating oil system. Refer to Procedure 007-037 in Section 7.
>
> Lift up on the locking tab and pull the electrical connectors apart.
>
> Remove the sensor.
>
> ### Resistance Check
>
> Disconnect the sensor connector.
>
> Select the resistance function on the multimeter.
>
> Attach the appropriate test leads to the multimeter probes.
>
> Touch the two test leads to the two terminals on the sensor. Measure the resistance.
>
> The multimeter **must** show between 115 and 244k ohms. The resistance value is temperature-dependent as shown in the table below.
>
> | Temperature | Range |  |
> |---|---|---|
> | °C | °F | Ohms |
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
> The multimeter **must** show greater than 100k ohms, which is an open circuit. If the circuit is **not** closed, then there is a short within the sensor to chassis ground. Replace the sensor.
>
> ### Install
>
> Verify that the new sensor has an o-ring.
>
> Lubricate the sensor o-ring with clean engine oil.
>
> Install the sensor into the engine.
>
> Tighten the sensor.
>
> **Момент затяжки · Torque Value**
> 15 n•m [11 ft-lb]
>
> Push the connectors together until they lock.
>
> Fill the engine to the proper level with lubricating oil and operate the engine to check for leaks.
