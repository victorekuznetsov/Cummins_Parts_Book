---
aliases:
  - "Датчик температуры охлаждающей жидкости"
type: "Процедура"
doc: "98-019-019"
title_en: "Engine Coolant Temperature Sensor"
title_ru: "Датчик температуры охлаждающей жидкости"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-019-019.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-019-019.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K19"
  - "группа/98"
  - "перевод/машинный"
---

# Engine Coolant Temperature Sensor
**Датчик температуры охлаждающей жидкости**

> [!abstract] Процедура · `98-019-019`
> **Двигатели:** [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]]
> **Семейство:** K19
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-04-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-019-019.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-019-019.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Датчик отправляет информацию о температуре охлаждающей жидкости двигателя в ECM. Расположение датчика варьируется в зависимости от семейства двигателей.

> [!note] Примечание
> Не все приложения CENTRYTM будут использовать этот датчик. Смотрите руководство по устранению неполадок и ремонту OEM для функций системы.

![[19801851.png]]

### Снятие

> [!danger] ОПАСНО
> Подождите, пока температура охлаждающей жидкости не будет ниже 50°C \[120°F\], прежде чем удалять крышку радиатора системы охлаждающей жидкости. Неспособность сделать это может привести к личным травмам от нагреваемого спрея охлаждающей жидкости или пара.

Слейте охлаждающую жидкость. См. соответствующее руководство по устранению неполадок и ремонту базового двигателя для процедуры.

![[19801858.png]]

Убедитесь, что разъем датчика отключен.

Удалите датчик.

![[19801853.png]]

### Установка

Убедитесь, что новый датчик имеет кольцо. Смазать кольцо с помощью чистого моторного масла. Установите новый датчик в двигатель. Затяните датчик.

> [!tip] Момент затяжки
> 35 Н·м [26 фунт-фут]

![[19801860.png]]

Промыть и очистить контактные контакты разъёма жгута проводов с помощью контактного очистителя, номер детали. 3824510.

> [!warning] ОСТОРОЖНО
> Используйте только рекомендованную Cummins смазку DS-ES, номер детали. 3822934. Другие смазочные материалы, такие как моторное масло или смазка, в разъемах могут вызвать повреждение ECM, плохую производительность двигателя или преждевременный контактный износ разъема.

Нанесите небольшое количество смазки на соединительные терминалы. **не** заполнять всю полость разъема смазкой. Подключите разъем датчика. Убедитесь, что разъём запирается на месте. Заполните систему охлаждения и работайте с двигателем, чтобы проверить наличие утечек.

![[19801861.png]]

### Проверка сопротивления

Отключите разъем датчика.

Выберите функцию сопротивления на мультиметре. Прикосновение к двум мультиметрам приводит к двум терминалам на датчике.

Измерьте сопротивление. Мультиметр **должен **показывать от 175 до 244k ом.

Значение сопротивления зависит от температуры, как показано в таблице ниже.

![[19801852.png]]

| температура | температура | Диапазон сопротивления |
|---|---|---|
| (°C) | \[°F\] | (Омс) |
| 0 | 32 | 30k до 36k |
| 25 | 77 | 9k до 11k |
| 50 | 122 | 3k - 4k |
| 75 | 167 | 1350—1500 |
| 100 | 212 | 600-675 |

Если сопротивление находится вне диапазона, датчик выходит из строя.

Замените датчик.

![[19801853.png]]

### Проверка на замыкание на массу

Прикосновение к одному из мультиметров приводит к любому из штифтов на стороне датчика разъема датчика. Прикосновение к другому мультиметру приводит к хорошей, чистой поверхности на блоке двигателя.

Измерьте сопротивление. Мультиметр **должен **показывать более 100k ом, что является открытой схемой. Если цепь **не** открыта, внутри датчика есть короткое расстояние до земли шасси.

Замените датчик.

![[19801854.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> The sensor sends engine coolant temperature information to the ECM. The sensor location varies with engine family.
>
> **Note · Примечание**
> **Not** all CENTRY™ applications will use this sensor. Refer to the OEM troubleshooting and repair manual for system features.
>
> ### Remove
>
> **WARNING · Опасно**
> Wait until the coolant temperature is below 50°C \[120°F\] before removing the coolant system pressure cap. Failure to do so can cause personal injury from heated coolant spray or steam.
>
> Drain the cooling system. Refer to the appropriate base engine troubleshooting and repair manual for the procedure.
>
> Make sure the sensor connector is disconnected.
>
> Remove the sensor.
>
> ### Install
>
> Verify that the new sensor has an o-ring. Lubricate the o-ring using clean engine oil. Install the new sensor into the engine. Tighten the sensor.
>
> **Момент затяжки · Torque Value**
> 35 n•m [26 ft-lb]
>
> Flush and clean the harness connector pins using contact cleaner, Part No. 3824510.
>
> **CAUTION · Осторожно**
> Use only Cummins-recommended lubricant DS-ES, Part No. 3822934. Other lubricants, such as lubricating oil or grease, in the connectors can cause ECM damage, poor engine performance, or premature connector pin wear.
>
> Apply a small amount of lubricant to the connector terminals. Do **not** fill the entire connector cavity with lubricant. Connect the sensor connector. Make sure the connector locks into place. Fill the cooling system and operate the engine to check for leaks.
>
> ### Resistance Check
>
> Disconnect the sensor connector.
>
> Select the resistance function on the multimeter. Touch the two multimeter leads to the two terminals on the sensor.
>
> Measure the resistance. The multimeter **must** show between 175 and 244k ohms.
>
> The resistance value is temperature dependent as shown in the table below.
>
> | Temperature | Temperature | Resistance Range |
> |---|---|---|
> | (°C) | \[°F\] | (ohms) |
> | 0 | 32 | 30k to 36k |
> | 25 | 77 | 9k to 11k |
> | 50 | 122 | 3k to 4k |
> | 75 | 167 | 1350 to 1500 |
> | 100 | 212 | 600 to 675 |
>
> If the resistance is out of range, the sensor has failed.
>
> Replace the sensor.
>
> ### Check for Short Circuit to Ground
>
> Touch one of the multimeter leads to either of the pins on the sensor side of the sensor connector. Touch the other multimeter lead to a good, clean surface on the engine block.
>
> Measure the resistance. The multimeter **must** show greater than 100k ohms, which is an open circuit. If the circuit is **not** open, there is a short within the sensor to chassis ground.
>
> Replace the sensor.
