---
aliases:
  - "Датчик температуры отработавших газов"
type: "Процедура"
doc: "122-019-013"
title_en: "Exhaust Temperature Sensor"
title_ru: "Датчик температуры отработавших газов"
modified: "2021-07-28"
engines:
  - "33239746"
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
manuals:
  - "4022102"
figures: 28
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-019-013.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/122-019-013.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/122"
  - "перевод/машинный"
---

# Exhaust Temperature Sensor
**Датчик температуры отработавших газов**

> [!abstract] Процедура · `122-019-013`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Входит в руководства:** [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M|4022102]]
> **Секции:** Section 19 - Electronic Controls
> **Даты:** изменён 2021-07-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-019-013.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/122-019-013.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Датчики температуры выхлопных газов (EGTS) расположены на выхлопном коллекторе на двигателях QSK38 и QSK50. Датчики температуры выхлопных газов (EGTS) расположены на стороне головки цилиндра на двигателях QSK60.

Этот двигатель может использовать либо полный комплект двигателя термистора, либо термопару EGTS. Обратите внимание, что терморезистор и термопара EGTS должны быть смешанными и должны работать правильно на данном двигателе.

Двигатели, использующие терморезистор EGTS, не требуют блоков преобразователя сигнала, поскольку температура измеряется непосредственно модулем управления двигателем (ECM). Для двигателей с термопарой EGTS температура измеряется с помощью преобразователей, которые взаимодействуют с ECM.

После получения ECM каждое отдельное измерение сравнивается с глобальным предупреждением, серьезным и критическим порогом для обнаружения в температурных условиях.

Кроме того, берется среднее значение всех температур выхлопных газов, и рассчитывается отклонение каждой температуры цилиндра от средней. Если отклонение от среднего слишком велико (либо слишком высоко, либо слишком низко), то устанавливается ошибка.

![[00r01593.png]]

QSK38, QSK50 Термистор EGTS

![[00r01622.png]]

QSK50 Термопара EGTS

![[00r01618.png]]

QSK60 Термистор EGTS

![[00r01619.png]]

QSK60 Термопара EGTS

### Снятие

Термистор

**Q38Термистор**

Отсоедините разъём (1) датчика температуры выхлопных газов от топливного форсунка и датчика температуры выхлопных газов от проводной системы (2).

![[00r01594.png]]

Удалите два зажимных болта.

Освободите и удалите датчик температуры выхлопных газов.

![[00r01595.png]]

**Q50 Термистор**

Отсоедините разъём (1) датчика температуры выхлопных газов от топливного форсунка и датчика температуры выхлопных газов от проводной системы (2).

![[00r01594.png]]

Удалите два зажимных болта.

Освободите и удалите датчик температуры выхлопных газов.

![[00r01595.png]]

**Q60 Термистор**

Отсоедините разъём (1) датчика температуры выхлопных газов от топливного форсунка и датчика температуры выхлопных газов от проводной системы (2).

![[00r01620.png]]

Удалите зажимные болты провода.

Освободите и удалите датчик температуры выхлопных газов.

![[00r01621.png]]

Термопара

**Q50 Термопара**

Существует четыре разных номера деталей EGTS с различными профилями изгиба. Каждая из четырех частей используется на определенных местах цилиндров. Перед удалением EGTS из местоположения цилиндра, пометьте расположение цилиндра на EGTS.

Отсоедините разъём (1) датчика температуры выхлопных газов от топливного форсунка и датчика температуры выхлопных газов от проводной системы (2).

![[00r01623.png]]

Удалите зажимные болты провода.

Снимите накидку и двухсекционную скобу.

![[00r01624.png]]

Освободите и удалите датчик температуры выхлопных газов.

![[00r01625.png]]

**Q60 Термопара**

Отсоедините разъём (1) датчика температуры выхлопных газов от топливного форсунка и датчика температуры выхлопных газов от проводной системы (2).

![[00r01620.png]]

Удалите зажимные болты провода.

Освободите и удалите датчик температуры выхлопных газов.

![[00r01632.png]]

### Очистка и проверка при повторном использовании

**Q38**, **Q50 и Q60 Термисторы и термопары**

Очистите датчик температуры выхлопных газов. Используйте чистую, свободную от винта ткань.

Проверьте датчик.

Заменить датчик, если:

- Провод датчика поврежден или истиран
- поврежденный или коррозийный
- Сенсорный наконечник согнут или треснул.

Проверьте скобки, шайбы и болты.

Заменить компонент, если:

- Щелкунчик
- Разбит.

![[00r01616.png]]

### Установка

Термистор

**Q38 и Q50 Термисторы**

Применять антисептик на основе несвинцового соединения, номер детали 3824732, или эквивалент, к резьбе датчика температуры выхлопных газов и устанавливать датчик температуры выхлопных газов.

Затяните гайку, которая обеспечивает датчик температуры выхлопных газов.

> [!tip] Момент затяжки
> 44 Н·м [32 фунт-фут]

![[00r01617.png]]

Установите два зажимных болта.

> [!tip] Момент затяжки
> 20 Н·м [177 фунт-дюйм]

![[00r01595.png]]

Подключите разъем датчика температуры выхлопа в проводной упряжке, сжимая его вместе, пока он не щелкнет.

![[00r01628.png]]

**Q60 Термистор**

Применять антисептик на основе несвинцового соединения, номер детали 3824732, или эквивалент, к резьбе датчика температуры выхлопных газов и устанавливать датчик температуры выхлопных газов.

Затяните гайку, которая обеспечивает датчик температуры выхлопных газов.

> [!tip] Момент затяжки
> 44 Н·м [32 фунт-фут]

![[00r01629.png]]

Установите болты зажима провода.

> [!tip] Момент затяжки
> 20 Н·м [177 фунт-дюйм]

![[00r01630.png]]

Подключите разъем датчика температуры выхлопа в проводной упряжке, сжимая его вместе, пока он не щелкнет.

![[00r01631.png]]

Термопара

**Q50 Термопара**

Применять антисептик на основе несвинцового соединения, номер детали 3824732, или эквивалент, к резьбе датчика температуры выхлопных газов и устанавливать датчик температуры выхлопных газов.

Затяните гайку, которая обеспечивает датчик температуры выхлопных газов.

> [!tip] Момент затяжки
> 44 Н·м [32 фунт-фут]

![[00r01626.png]]

Установите ношение рукава и двухсекундной скобки

Установите болты зажима провода.

> [!tip] Момент затяжки
> 20 Н·м [177 фунт-дюйм]

![[00r01624.png]]

Подключите разъем датчика температуры выхлопа в проводной упряжке, сжимая его вместе, пока он не щелкнет.

> [!missing]- Иллюстрация `00r01627.png` не извлечена — смотрите PDF-оригинал документа

**Q60 Термопара**

Применять антисептик на основе несвинцового соединения, номер детали 3824732, или эквивалент, к резьбе датчика температуры выхлопных газов и устанавливать датчик температуры выхлопных газов.

Затяните гайку, которая обеспечивает датчик температуры выхлопных газов.

> [!tip] Момент затяжки
> 44 Н·м [32 фунт-фут]

> [!missing]- Иллюстрация `00r01633.png` не извлечена — смотрите PDF-оригинал документа

Установите болты зажима провода.

> [!tip] Момент затяжки
> 20 Н·м [177 фунт-дюйм]

> [!missing]- Иллюстрация `00r01634.png` не извлечена — смотрите PDF-оригинал документа

Подключите разъем датчика температуры выхлопа в проводной упряжке, сжимая его вместе, пока он не щелкнет.

> [!missing]- Иллюстрация `00r01635.png` не извлечена — смотрите PDF-оригинал документа


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> The Exhaust Gas Temperature Sensors (EGTS) are located on the exhaust manifold connection on the QSK38 and QSK50 engines. The Exhaust Gas Temperature Sensors (EGTS) are located on the side of the cylinder head on the QSK60 engines.
>
> This engine can use either a full engine set of thermistor or thermocouple EGTS. Note that thermistor and thermocouple EGTS should **not** be mixed and will **not** work properly on a given engine.
>
> Engines that use thermistor EGTS do **not** require the signal converter boxes as the temperature is measured directly by the Engine Control Module (ECM). For engines with thermocouple EGTS, the temperature is measured by using converter boxes which communicate with the ECMs.
>
> After being received by the ECM, each individual measurement is compared to a global warning, serious and critical threshold to detect over or under temperature conditions.
>
> In addition, an average is taken of all exhaust port temperatures, and the deviation of each cylinder temperature from average is calculated. If the deviation from the average is too great (either too high or too low), then an error is set.
>
> QSK38, QSK50 Thermistor EGTS
>
> QSK50 Thermocouple EGTS
>
> QSK60 Thermistor EGTS
>
> QSK60 Thermocouple EGTS
>
> ### Remove
>
> Thermistor
>
> **Q38Thermistor**
>
> Disconnect the connector (1) of the exhaust temperature sensor from the injector and exhaust temperature sensor harness (2).
>
> Remove the two wire clamp capscrews.
>
> Loosen and remove the exhaust temperature sensor.
>
> **Q50 Thermistor**
>
> Disconnect the connector (1) of the exhaust temperature sensor from the injector and exhaust temperature sensor harness (2).
>
> Remove the two wire clamp capscrews.
>
> Loosen and remove the exhaust temperature sensor.
>
> **Q60 Thermistor**
>
> Disconnect the connector (1) of the exhaust temperature sensor from the injector and exhaust temperature sensor harness (2).
>
> Remove the wire clamp capscrews.
>
> Loosen and remove the exhaust temperature sensor.
>
> Thermocouple
>
> **Q50 Thermocouple**
>
> There are four different EGTS part numbers with different bend profiles. Each of the four parts are used on specific cylinder locations. Prior to removing an EGTS from a cylinder location, label the cylinder location on the EGTS.
>
> Disconnect the connector (1) of the exhaust temperature sensor from the injector and exhaust temperature sensor harness (2).
>
> Remove the wire clamp capscrew.
>
> Remove wear sleeve and two-piece bracket.
>
> Loosen and remove the exhaust temperature sensor.
>
> **Q60 Thermocouple**
>
> Disconnect the connector (1) of the exhaust temperature sensor from the injector and exhaust temperature sensor harness (2).
>
> Remove the wire clamp capscrews.
>
> Loosen and remove the exhaust temperature sensor.
>
> ### Clean and Inspect for Reuse
>
> **Q38**, **Q50, and Q60 Thermistors and Thermocouples**
>
> Clean the exhaust gas temperature sensor. Use a clean, lint-free cloth.
>
> Inspect the sensor.
>
> Replace the sensor if:
>
> - Sensor wire damaged or abraded
> - Threads damaged or corroded
> - Sensor tip bent or cracked.
>
> Inspect the brackets, washers, and capscrews.
>
> Replace the component if:
>
> - Bent
> - Cracked.
>
> ### Install
>
> Thermistor
>
> **Q38and Q50Thermistors**
>
> Apply non-lead based anti-seize compound, Part Number 3824732, or equivalent, to the exhaust temperature sensor threads and install the exhaust temperature sensor.
>
> Tighten the nut that secures the exhaust temperature sensor.
>
> **Момент затяжки · Torque Value**
> 44 n•m [32 ft-lb]
>
> Install the two wire clamp capscrews.
>
> **Момент затяжки · Torque Value**
> 20 n•m [177 in-lb]
>
> Connect the exhaust temperature sensor connector in the harness, pushing it together until it clicks.
>
> **Q60 Thermistor**
>
> Apply non-lead based anti-seize compound, Part Number 3824732, or equivalent, to the exhaust temperature sensor threads and install the exhaust temperature sensor.
>
> Tighten the nut that secures the exhaust temperature sensor.
>
> **Момент затяжки · Torque Value**
> 44 n•m [32 ft-lb]
>
> Install the wire clamp capscrews.
>
> **Момент затяжки · Torque Value**
> 20 n•m [177 in-lb]
>
> Connect the exhaust temperature sensor connector in the harness, pushing it together until it clicks.
>
> Thermocouple
>
> **Q50 Thermocouple**
>
> Apply non-lead based anti-seize compound, Part Number 3824732, or equivalent, to the exhaust temperature sensor threads and install the exhaust temperature sensor.
>
> Tighten the nut that secures the exhaust temperature sensor.
>
> **Момент затяжки · Torque Value**
> 44 n•m [32 ft-lb]
>
> Install wear sleeve and two-piece bracket
>
> Install the wire clamp capscrew.
>
> **Момент затяжки · Torque Value**
> 20 n•m [177 in-lb]
>
> Connect the exhaust temperature sensor connector in the harness, pushing it together until it clicks.
>
> **Q60 Thermocouple**
>
> Apply non-lead based anti-seize compound, Part Number 3824732, or equivalent, to the exhaust temperature sensor threads and install the exhaust temperature sensor.
>
> Tighten the nut that secures the exhaust temperature sensor.
>
> **Момент затяжки · Torque Value**
> 44 n•m [32 ft-lb]
>
> Install the wire clamp capscrews.
>
> **Момент затяжки · Torque Value**
> 20 n•m [177 in-lb]
>
> Connect the exhaust temperature sensor connector in the harness, pushing it together until it clicks.
