---
aliases:
  - "Датчик давления топлива в рампе"
type: "Процедура"
doc: "98-019-115"
title_en: "Rail Fuel Pressure Sensor"
title_ru: "Датчик давления топлива в рампе"
modified: "2003-04-01"
engines:
  - "37269910"
  - "37280605"
families:
  - "K19"
manuals:
  - "3666070"
figures: 13
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-019-115.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-019-115.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K19"
  - "группа/98"
  - "перевод/машинный"
---

# Rail Fuel Pressure Sensor
**Датчик давления топлива в рампе**

> [!abstract] Процедура · `98-019-115`
> **Двигатели:** [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]]
> **Семейство:** K19
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-04-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-019-115.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-019-115.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Датчик давления в рельсах устанавливается в железнодорожной линии между топливным насосом и входом в блок. Этот датчик контролирует давление топлива в железнодорожной линии.

> [!note] Примечание
> Каждый тип двигателя будет иметь датчик, установленный в другом месте. Смотрите соответствующее руководство по базовому двигателю.

![[19801765.png]]

### Снятие

Отсоедините датчик, подняв запирающую вкладку и разъединив разъем.

![[19801786.png]]

Удалите датчик.

![[19801787.png]]

### Установка

Убедитесь, что новый датчик имеет кольцо. Смажьте уплотнительное кольцо чистым моторным маслом.

Установите новый датчик. Затяните датчик.

> [!tip] Момент затяжки
> 16 Н·м [142 фунт-дюйм]

![[19801788.png]]

> [!warning] ОСТОРОЖНО
> Используйте только рекомендованную Cummins смазку DS-ES, номер детали. 38232934. Другие смазочные материалы, такие как моторное масло или смазка в разъемах, могут вызвать повреждение ECM, плохую производительность двигателя или преждевременный контактный износ разъема.

Нанесите небольшое количество смазки на соединительные терминалы. **не** заполнять всю полость разъема смазкой.

Подключите разъем датчика. Убедитесь, что блокировка вкладки нажимает на место.

![[19801786.png]]

### Проверка напряжения

Отсоедините датчик давления рельса от основной проводов двигателя.

![[19801786.png]]

> [!warning] ОСТОРОЖНО
> Чтобы избежать повреждения штифта и проводов, используйте следующий испытательный щуп при проведении измерения: Часть нет. 3824774 — проводка жгута ветвленного кабеля.

Подключите проводку кабеля ветки жгута, номер детали. 3824774, к датчику давления рельса и к основной проводах двигателя.

Установите мультиметр для показаний VDC.

Включите зажигание.

![[19802632.png]]

Установите подачу (контакт А) и возврат (контакт В) в мультиметр.

Напряжение должно измеряться между 4,75 ВДК и 5,25 ВДК.

Если напряжение находится между 4,75 ВДК и 5,25 ВДК, устраните неисправности основной проводов двигателя. См. Процедуры 019-250 и 019-043.

![[19802633.png]]

После ремонта подсоедините все компоненты.

![[nobox.png]]

Отсоедините датчик давления рельса от основной проводов двигателя.

![[19801786.png]]

> [!warning] ОСТОРОЖНО
> Чтобы избежать повреждения штифта и проводов, используйте следующий испытательный щуп при проведении измерения: Часть нет. 3824774 — проводка жгута ветвленного кабеля.

Подключите проводку кабеля ветки жгута, номер детали. 3824774, к датчику давления рельса и к основной проводах двигателя.

Установите мультиметр для показаний VDC.

Включите зажигание.

![[19802632.png]]

Установите сигнал (контакт C) и верните (контакт B) в мультиметр.

Напряжение должно измеряться между 0,46 ВДК и 4,56 ВДК.

Если напряжение составляет **не** между 0,46 ВДК и 4,56 ВДК, замените датчик давления в рельсах. См. процедуру 019-115.

![[19802634.png]]

После ремонта подсоедините все компоненты.

![[nobox.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> The rail pressure sensor is mounted in the rail line between the fuel pump and the rail inlet to the block. This sensor monitors the fuel pressure in the rail line.
>
> **Note · Примечание**
> Each engine type will have the sensor mounted in a different location. Refer to the appropriate base engine manual.
>
> ### Remove
>
> Disconnect the sensor by lifting the locking tab and pulling apart the connector.
>
> Remove the sensor.
>
> ### Install
>
> Verify that the new sensor has an o-ring. Lubricate the o-ring with clean engine oil.
>
> Install the new sensor. Tighten the sensor.
>
> **Момент затяжки · Torque Value**
> 16 n•m [142 in-lb]
>
> **CAUTION · Осторожно**
> Use only Cummins recommended lubricant DS-ES, Part No. 38232934. Other lubricants, such as lubricating oil or grease in the connectors, can cause ECM damage, poor engine performance, or premature connector pin wear.
>
> Apply a small amount of lubricant to the connector terminals. Do **not** fill the entire connector cavity with lubricant.
>
> Connect the sensor connector. Make sure the locking tab clicks into place.
>
> ### Voltage Check
>
> Disconnect the rail pressure sensor from the main engine harness.
>
> **CAUTION · Осторожно**
> To avoid pin and harness damage, use the following test lead when taking a measurement: Part No. 3824774 - breakout cable.
>
> Connect the breakout cable, Part No. 3824774, to the rail pressure sensor and the main engine harness.
>
> Set multimeter to read VDC.
>
> Turn keyswitch ON.
>
> Install supply (pin A) and return (pin B) into the multimeter.
>
> The voltage should measure between 4.75 VDC and 5.25 VDC.
>
> If the voltage is **not** between 4.75 VDC and 5.25 VDC, troubleshoot the main engine harness. Refer to Procedures 019-250 and 019-043.
>
> Connect all components after completing the repair.
>
> Disconnect the rail pressure sensor from the main engine harness.
>
> **CAUTION · Осторожно**
> To avoid pin and harness damage, use the following test lead when taking a measurement: Part No. 3824774 - breakout cable.
>
> Connect the breakout cable, Part No. 3824774, to the rail pressure sensor and the main engine harness.
>
> Set multimeter to read VDC.
>
> Turn keyswitch ON.
>
> Install signal (pin C) and return (pin B) into the multimeter.
>
> The voltage should measure between 0.46 VDC and 4.56 VDC.
>
> If the voltage is **not** between 0.46 VDC and 4.56 VDC, replace the rail pressure sensor. Refer to Procedure 019-115.
>
> Connect all components after completing the repair.
