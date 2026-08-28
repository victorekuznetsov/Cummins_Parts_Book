---
aliases:
  - "Датчик давления моторного масла"
type: "Процедура"
doc: "98-019-066"
title_en: "Engine Oil Pressure Sensor"
title_ru: "Датчик давления моторного масла"
modified: "2003-04-01"
engines:
  - "37269910"
  - "37280605"
families:
  - "K19"
manuals:
  - "3666070"
figures: 14
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-019-066.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-019-066.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K19"
  - "группа/98"
  - "перевод/машинный"
---

# Engine Oil Pressure Sensor
**Датчик давления моторного масла**

> [!abstract] Процедура · `98-019-066`
> **Двигатели:** [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]]
> **Семейство:** K19
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-04-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-019-066.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-019-066.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Датчик давления масла (OPS) отправляет информацию о давлении моторного масла в ECM.

Расположение датчика варьируется в зависимости от семейства двигателей. Смотрите соответствующее руководство по базовому двигателю.

> [!note] Примечание
> Не все приложения CENTRYTM будут использовать этот датчик. См. руководство OEM для системных функций.

![[nobox.png]]

### Снятие

Отсоедините датчик давления моторного масла от основной проводов двигателя.

Используя 1-1/4-дюймовый разъем, удалите датчик давления масла.

![[19900794.png]]

### Установка

Убедитесь, что на датчике есть кольцо. Смажьте уплотнительное кольцо чистым моторным маслом.

Используя 1-1/4-дюймовую розетку, установите датчик давления масла.

> [!tip] Момент затяжки
> 11 Н·м [97 фунт-дюйм]

Подключите OPS к основной проводах двигателя. Убедитесь, что разъем запирается на месте.

![[19900794.png]]

### Проверка напряжения

Отсоедините датчик давления масла от проводной упряжки OEM.

![[19801861.png]]

> [!warning] ОСТОРОЖНО
> Чтобы избежать повреждения штифта и проводов, используйте следующий измерительный щуп при измерении: Номер детали. 3824775 — проводка жгута ветвленного кабеля.

Подключите проводку кабеля ветки жгута, номер детали. 3824775, датчику давления масла и проводной упряжке OEM.

Установите мультиметр для показаний VDC.

Включите зажигание.

![[19802632.png]]

Установите подачу (контакт А) и возврат (контакт В) в мультиметр.

Напряжение должно измеряться между 4,75 ВДК и 5,25 ВДК.

Если напряжение находится между 4,75 ВДК и 5,25 ВДК, проверьте напряжение питания с отключенным датчиком.

![[19802633.png]]

Отсоедините датчик давления масла от проводной упряжки OEM.

![[19801861.png]]

> [!warning] ОСТОРОЖНО
> Чтобы избежать повреждения штифта и проводов, используйте следующий измерительный щуп при измерении: Номер детали. 3824775 — проводка жгута ветвленного кабеля.

Подключите проводку кабеля ветки жгута, номер детали. 3824775, к проводной ремне OEM. Не подключайте датчик.

Установите мультиметр для показаний VDC.

Включите зажигание.

![[19802632.png]]

Установите подачу (контакт А) и возврат (контакт В) в мультиметр.

Напряжение должно измеряться между 4,75 ВДК и 5,25 ВДК.

Если напряжение между 4,75 ВДК и 5,25 ВДК, замените датчик давления масла. См. руководство изготовителя машины по диагностике и ремонту.

Если напряжение **не** между 4,75 ВДК и 5,25 ВДК, устраните неисправность проводов OEM или ECM. См. руководство изготовителя машины по диагностике и ремонту.

![[19802633.png]]

После ремонта подсоедините все компоненты.

![[nobox.png]]

Отсоедините датчик давления масла от проводной упряжки OEM.

![[19801861.png]]

> [!warning] ОСТОРОЖНО
> Чтобы избежать повреждения штифта и проводов, используйте следующий измерительный щуп при измерении: Номер детали. 3824775 — проводка жгута ветвленного кабеля.

Подключите проводку кабеля ветки жгута, номер детали. 3824775, датчику давления масла и проводной упряжке OEM.

Установите мультиметр для показаний VDC.

Включите зажигание.

![[19802632.png]]

Установите сигнал (контакт C) и верните (контакт B) в мультиметр.

Напряжение должно измеряться между 0,46 ВДК и 0,58 ВДК.

Если напряжение находится между 0,46 ВДК и 0,58 ВДК, замените датчик давления масла. См. руководство изготовителя машины по диагностике и ремонту.

![[19802634.png]]

После ремонта подсоедините все компоненты.

![[nobox.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> The oil pressure sensor (OPS) sends engine oil pressure information to the ECM.
>
> The location of the sensor varies with engine family. Refer to the appropriate base engine manual.
>
> **Note · Примечание**
> **Not** all CENTRY™ applications will use this sensor. Refer to the OEM manual for system features.
>
> ### Remove
>
> Disconnect the lubricating oil pressure sensor from the main engine harness.
>
> Using a 1-1/4-inch socket, remove the oil pressure sensor.
>
> ### Install
>
> Verify that there is an o-ring on the sensor. Lubricate the o-ring with clean engine oil.
>
> Using a 1-1/4-inch socket, install the oil pressure sensor.
>
> **Момент затяжки · Torque Value**
> 11 n•m [97 in-lb]
>
> Connect the OPS to the main engine harness. Make sure the connector locks in place.
>
> ### Voltage Check
>
> Disconnect the oil pressure sensor from the OEM harness.
>
> **CAUTION · Осторожно**
> To avoid pin and harness damage, use the following test lead when taking a measurement:Part No. 3824775 - breakout cable.
>
> Connect the breakout cable, Part No. 3824775, to the oil pressure sensor and the OEM harness.
>
> Set multimeter to read VDC.
>
> Turn keyswitch ON.
>
> Install supply (pin A) and return (pin B) into the multimeter.
>
> The voltage should measure between 4.75 VDC and 5.25 VDC.
>
> If the voltage is between 4.75 VDC and 5.25 VDC check the supply voltage with the sensor disconnected.
>
> Disconnect the oil pressure sensor from the OEM harness.
>
> **CAUTION · Осторожно**
> To avoid pin and harness damage, use the following test lead when taking a measurement:Part No. 3824775 - breakout cable.
>
> Connect the breakout cable, Part No. 3824775, to the OEM harness. Do **not** connect the sensor.
>
> Set multimeter to read VDC.
>
> Turn keyswitch ON.
>
> Install supply (pin A) and return (pin B) into the multimeter.
>
> The voltage should measure between 4.75 VDC and 5.25 VDC.
>
> If the voltage is between 4.75 VDC and 5.25 VDC replace the oil pressure sensor. Refer to the OEM troubleshooting and repair manual.
>
> If the voltage is **not** between 4.75 VDC and 5.25 VDC troubleshoot the OEM harness or ECM. Refer to the OEM troubleshooting and repair manual.
>
> Connect all components after completing the repair.
>
> Disconnect the oil pressure sensor from the OEM harness.
>
> **CAUTION · Осторожно**
> To avoid pin and harness damage, use the following test lead when taking a measurement:Part No. 3824775 - breakout cable.
>
> Connect the breakout cable, Part No. 3824775, to the oil pressure sensor and the OEM harness.
>
> Set multimeter to read VDC.
>
> Turn keyswitch ON.
>
> Install signal (pin C) and return (pin B) into the multimeter.
>
> The voltage should measure between 0.46 VDC and 0.58 VDC.
>
> If the voltage is **not** between 0.46 VDC and 0.58 VDC, replace the oil pressure sensor. Refer to the OEM troubleshooting and repair manual.
>
> Connect all components after completing the repair.
