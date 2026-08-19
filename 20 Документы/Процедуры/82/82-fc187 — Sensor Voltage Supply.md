---
aliases:
  - "Питание датчиков"
type: "Процедура"
doc: "82-fc187"
title_en: "Sensor Voltage Supply"
title_ru: "Питание датчиков"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc187.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc187.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# Sensor Voltage Supply
**Питание датчиков**

> [!abstract] Процедура · `82-fc187`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc187.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc187.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 187

### Питание датчиков

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 187 PID(P): S232 SPN: 620 FMI: 4/4 лампы: Желтая СТО: | Низкое напряжение, обнаруженное на линии подачи напряжения ECM, на некоторых датчиках (подача VSEN 2). | Двигатель будет работать с поломкой. Отсутствие защиты двигателя от давления масла или уровня охлаждающей жидкости. |

![[19200194.png]]

Сенсорная схема напряжения питания

### Описание цепи

ECM поставляет каждый из этих датчиков с +5-VDC. Если линия подачи на любой датчик повреждена, датчик будет работать неправильно.

### Расположение компонента

Датчик ограничения впуска топлива расположен на входе топливного насоса.

Датчик давления/температуры масла расположен перед воздушным компрессором.

Датчик уровня масла расположен в масляной кастрюле.

Датчик давления в мокром баке расположен на воздушном компрессоре

Датчик уровня охлаждения. См. руководство OEM для правильного местоположения.

Топ-2 датчика положения передачи - расположен на трансмиссии, если транспортное средство имеет трансмиссию SpicerTM Top 2 Automate. См. руководство OEM для правильного местоположения.

### Практические замечания

Низкое напряжение на датчике + 5-вольтовая линия питания будет вызвано коротким заземлением в линии питания, коротким замыканием между линией питания или обратной линией, неисправным датчиком или неисправным источником питания ECM.

Во время теста на ответ кода неисправности, описанного для каждого датчика, подключенного к датчику питания № 2, код 187 по умолчанию должен быть активным перед отключением каждого датчика. Если код неисправности ** не активен, но может быть легко продублирован при работе двигателя, то можно выполнить следующее:

- Работайте с двигателем в условиях, которые заставят код 187 по умолчанию активироваться, даже если он регистрируется в течение короткого периода времени, отключайте один датчик за раз, пока код 187 по умолчанию не прекратит регистрацию в условиях испытаний. Каждый датчик может быть отключен при работе двигателя. Примечание: Двигатель может **не** запускаться, если датчик положения распредвала отключен.

См. Код устранения неполадок t05-187


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 187
>
> ### Sensor Voltage Supply
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 187 PID(P): S232 SPN: 620 FMI: 4/4 Lamp: Yellow SRT: | Low voltage detected on the ECM voltage supply line to some sensors (VSEN 2 supply). | Engine will run derated. No engine protection for oil pressure or coolant level. |
>
> Sensor Supply Voltage Circuit
>
> ### Circuit Description
>
> The ECM supplies each of these sensors with +5-VDC. If the supply line to any sensor is damaged, the sensor will **not** work correctly.
>
> ### Component Location
>
> Fuel inlet restriction sensor is located on the fuel pump inlet.
>
> Oil pressure/temperature sensor is located in front of the air compressor.
>
> Oil level sensor is located in the oil pan.
>
> Wet tank pressure sensor is located on the air compressor
>
> Coolant level sensor. Refer to the OEM manual for proper location.
>
> Top 2 transmission position sensor - located on the transmission if vehicle has a Spicer™ Top 2 Automate transmission. Refer to the OEM manual for proper location.
>
> ### Shoptalk
>
> Low voltage on the sensor + 5-volt supply line will be caused by a short to ground in a supply line, a short circuit between a supply line or a return line, a failed sensor, or a failed ECM power supply.
>
> During the fault code response test outlined for each sensor connected to sensor supply number 2, Fault Code 187 **must** be active before unplugging each sensor. If the fault code is **not** active, but can be easily duplicated by operating the engine, the following can be performed:
>
> - Operate the engine under the conditions that will cause Fault Code 187 to become active, even if it logs for a short period of time, unplug one sensor at a time until Fault Code 187 stops logging under the test conditions. Each sensor can be unplugged with the engine running. Note: The engine may **not** start if the camshaft position sensor is unplugged.
>
> Refer to Troubleshooting Fault Code t05-187
