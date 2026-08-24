---
aliases:
  - "Датчик барометрического давления"
type: "Процедура"
doc: "122-019-004"
title_en: "Barometric Pressure Sensor"
title_ru: "Датчик барометрического давления"
modified: "2020-07-17"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-019-004.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/122-019-004.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/122"
  - "перевод/машинный"
---

# Barometric Pressure Sensor
**Датчик барометрического давления**

> [!abstract] Процедура · `122-019-004`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Входит в руководства:** [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M|4022102]]
> **Секции:** Section 19 - Electronic Controls - Group 19
> **Даты:** изменён 2020-07-17
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-019-004.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/122-019-004.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

** С механически приводимым в действие топливным форсункой**:

В общем, барометрический датчик может быть установлен на двигателе рядом или вокруг ECM. Однако барометрический датчик может перемещаться в зависимости от

Двигатель и применение.

** С помощью электронно-приводного форсунки**:

Барометрический датчик может быть установлен на любой из двигателей проводов жгутов проводов. Обычно устанавливается в направлении передней части двигателя

на левом берегу основной проводной упряжь, но может быть установлена на правом берегу главной проводной упряжкой или даже передней и задней

Кроссоверные проводов. Существует два способа крепления датчика в зависимости от типа проводов, установленной на двигателе.

- Bolted - алюминиевые экструзионные проводные ремни
- Zip/Cable tied – плетеные/гибкие проводные ремни.

### Первичная проверка

Подключите электронный инструмент к шине данных CAN транспортного средства.

Переведите замок зажигания в положение ON.

Мониторинг барометрического давления. Если барометрическое давление меньше или равно 523 мм рт.ст. \[20,6 в рт.ст.] и настоящее возвышение составляет менее 10 000 футов, замените датчик барометрического давления.

![[19400357.png]]

### Снятие

** С механически приводимым в действие топливным форсункой**:

Поднимите на вкладку и отсоедините разъем от датчика.

Удалите крепежные болты и датчик из двигателя.

![[19400379.png]]

** С помощью форсунки с электронным приводом и впрыскиваемых барометрических датчиков: **

Найдите барометрический датчик и отсоедините его от разъёма проводов.

Удалите три «нилоковых ореха», удерживающих пластину и датчик, в алюминиевую экструзионную проводку, и поместите нилоковые орехи и удерживающую пластину в одну сторону для переустановки. Нилоковые орехи можно использовать до 5 раз, прежде чем потребуется замена. Если вы не уверены, замените «орешки» на новые.

Откажитесь от неисправного барометрического датчика.

![[19300068.png]]

** С помощью форсунки с электронным приводом и барометрических датчиков с зип/кабельным шнуром:**

Найдите барометрический датчик и отсоедините его от разъёма проводов.

Использование набора боковых резцов срезать зип/кабель галстук, чтобы освободить неисправный барометрический датчик.

Откажитесь от неисправного барометрического датчика.

![[19300068.png]]

### Установка

** С механически приводимым в действие топливным форсункой**:

Установите новый датчик на двигатель. Затяните болты.

> [!tip] Момент затяжки
> 23 Н·м [204 фунт-дюйм]

Соедините разъёмы до фиксации.

![[19400379.png]]

** С помощью форсунки с электронным приводом и впрыскиваемых барометрических датчиков: **

Скользите новый барометрический датчик по шпильному столбу M3 и поместите удерживающую пластину поверх сеньора, используя два

M6 и одиночные M3-штукатурные посты для ориентации.

Обеспечьте безопасность гаек с использованием приведенных ниже спецификаций крутящего момента, так как это обеспечит достаточный зазор для Air Gap между ними.

Датчик и проводка жгута.

М3: 3 Н·м (2 фута-лб) - Secure First

М6: 8 Н·м (6 футов-лб) — Secure Last

Подсоедините барометрический датчик давления к разъёму проводов.

![[19300068.png]]

** С помощью форсунки с электронным приводом и барометрических датчиков с зип/кабельным шнуром:**

В том же месте, что и выброшенный барометрический датчик, надежно прикрепите новый барометрический датчик к проводах с помощью кабельного галстука.

![[19300068.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> **With Mechanically Actuated Injectors**:
>
> In general, a barometric sensor can be fitted to the engine close to or around the ECM. However, the barometric sensor could move depending on
>
> engine and application.
>
> **With Electronically Actuated Injectors**:
>
> A barometric sensor can be fitted to any of the engines wiring harnesses. Generally mounted towards the front of the engine
>
> on the left bank main wiring harness, but can be fitted on the Right Bank Main Wiring Harness or even the Front and Rear
>
> Crossover harnesses. There are two ways to mount the sensor depending on the type of harness installed on the engine.
>
> - Bolted – Aluminium Extrusion Harnesses
> - Zip/Cable tied – Braided/ Flexible Harnesses.
>
> ### Initial Check
>
> Connect an electronic service tool to the vehicle data link.
>
> Turn the keyswitch to the ON position.
>
> Monitor the barometric pressure. If the barometric pressure is less than or equal to 523 mm Hg \[20.6 in Hg\] and the present elevation is less than 10,000 feet, replace the barometric pressure sensor.
>
> ### Remove
>
> **With Mechanically Actuated Injectors**:
>
> Lift up on the tab and disconnect the connector from the sensor.
>
> Remove the mounting capscrews and sensor from the engine.
>
> **With Electronically Actuated Injectors and Bolted Barometric Sensors:**
>
> Locate the barometric sensor, and disconnect it from the wiring harness connector.
>
> Remove the three ‘nyloc nuts' holding retaining plate and sensor to the aluminium extrusion harness, and put the nyloc nuts and retaining plate to one side for reinstallation. The nyloc nuts can be used up to 5 times before requiring replacement. If unsure replace the ‘nyloc nuts' with new ones.
>
> Discard the failed Barometric Sensor.
>
> **With Electronically Actuated Injectors and Zip/Cable Tied Barometric Sensors:**
>
> Locate the barometric sensor, and disconnect it from the wiring harness connector.
>
> Using a set of side cutters snip the zip/ cable tie to release the failed barometric sensor.
>
> Discard the failed barometric sensor.
>
> ### Install
>
> **With Mechanically Actuated Injectors**:
>
> Install a new sensor on the engine. Tighten the capscrews.
>
> **Момент затяжки · Torque Value**
> 23 n•m [204 in-lb]
>
> Push the connectors together until they lock.
>
> **With Electronically Actuated Injectors and Bolted Barometric Sensors:**
>
> Slide the new Barometric sensor over the M3 stud post and place the retaining plate over the top of the senor using the two
>
> M6 and single M3 stud posts for orientation.
>
> Secure the nuts using the torque specifications below, as this will ensure there is enough clearance for the Air Gap between
>
> the sensor and the wiring harness.
>
> M3: 3 N⋅m (2 ft-lb) – Secure First
>
> M6: 8 N⋅m (6 ft-lb) – Secure Last
>
> Reconnect the barometric pressure sensor to the wiring harness connector.
>
> **With Electronically Actuated Injectors and Zip/Cable Tied Barometric Sensors:**
>
> In the same location as the discarded barometric sensor, secure the new barometric sensor to the wiring harness with a cable tie securely.
