---
aliases:
  - "Цепь датчика положения коленвала (EPS)"
type: "Процедура"
doc: "82-019-039"
title_en: "Engine Position Sensor (EPS) Circuit"
title_ru: "Цепь датчика положения коленвала (EPS)"
modified: "2005-01-28"
engines:
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 12
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-039.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-019-039.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# Engine Position Sensor (EPS) Circuit
**Цепь датчика положения коленвала (EPS)**

> [!abstract] Процедура · `82-019-039`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section 19 - Electronic Engine Controls
> **Даты:** изменён 2005-01-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-039.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-019-039.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Проверка сопротивления

> [!warning] ОСТОРОЖНО
> Не используйте щупы или провода, отличные от Части № 3822758. Разъём будет повреждён. Заводы должны плотно поместиться без расширения штифтов разъема.

Отсоедините разъем датчика проводов ремня от ECM. Вставьте измерительный щуп в контакт 47 разъёма проводов датчика. Вставьте другой испытательный щуп в контакт 48 разъема.

![[19200210.png]]

Убедитесь, что EPS подключен к проводах датчика.

Подключите испытательный щуп к многометровым зондам. Измерьте сопротивление. Значение сопротивления ** должно быть от 1000 до 2000 Ом. Если значение сопротивления ** не** правильно, возникает проблема с проводкой датчика при условии, что датчик был предварительно проверен.

![[19200210.png]]

Вставьте провода в контакты 50 и 49 разъёма проводов датчика. Измерьте сопротивление. Мультиметр ** должен ** показывать от 1000 до 2000 Ом. Если сопротивление ** не правильно, возникает проблема с проводкой датчика при условии, что датчик был предварительно проверен. Ремонт или замена датчика проводов жгута. См. процедуру[[82-019-043-tr — Engine Wiring Harness|019-043]]. Если обе проверки сопротивления находятся в пределах спецификации, схема датчика ** должна *** все еще проверяться на короткое замыкание на землю и короткое замыкание от пин-кодов до пин-кодов.

![[19200212.png]]

### Проверка на замыкание на массу

Проверьте короткое замыкание на землю. Настройте мультиметр на установку сопротивления. Вставьте измерительный щуп в контакт 47 датчика проводов ремня разъема, и подсоедините его к многометровому щупу. Прикоснитесь к другому многометровому щупу к заземлению блока двигателя. Измерьте сопротивление.

Мультиметр ** должен** показывать открытую схему (более 100k ом).

Если цепь ** не открыта, в проводе, подключенном к контакту 47, есть короткое замыкание для заземления.

Ремонт или замена датчика проводов жгута. См. процедуру[[82-019-043-tr — Engine Wiring Harness|019-043]].

![[19200406.png]]

Удалите пробный щуп из контакта 47 разъёма проводов датчика и вставьте его в контакт 50 разъёма. Прикоснитесь к другому многометровому щупу к заземлению блока двигателя. Измерьте сопротивление.

Мультиметр ** должен** показывать открытую схему (более 100k ом).

Если цепь ** не** открыта, в проводе, подключенном к контакту 50, есть короткое замыкание для заземления.

Ремонт или замена датчика проводов жгута. См. процедуру[[82-019-043-tr — Engine Wiring Harness|019-043]].

![[19200407.png]]

### Проверка на замыкание между контактами

Отсоедините датчик положения двигателя от датчика проводов ремня. Включить измерительный щуп в контакт 48 разъёма проводов датчика. Вставьте другой испытательный щуп в контакт 45 разъёма. Установите мультиметр на установку сопротивления и измерьте сопротивление.

Мультиметр ** должен** показывать открытую схему (более 100k ом).

![[19200392.png]]

Удалите пробный щуп из контакта 45 датчика проводов ремня разъема и проверьте все остальные штифты в разъеме. Измерьте сопротивление.

Мультиметр ** должен** показывать открытую схему (более 100k ом).

![[19200213.png]]

Вставьте измерительный щуп в контакт 49 разъёма проводов датчика и проверьте все другие штифты в разъеме. Измерьте сопротивление.

Мультиметр ** должен** показывать открытую схему (более 100k ом).

![[19200214.png]]

Удалите пробный щуп из контакта 49 разъёма проводов датчика и вставьте его в контакт 50 разъёма. Вставьте другой свинец в контакт 48. Измерьте сопротивление.

Мультиметр ** должен** показывать открытую схему (более 100k ом).

![[19200393.png]]

Удалите пробный щуп из контакта 48 датчика проводов ремня разъема и проверьте все остальные штифты в разъеме. Измерьте сопротивление.

Мультиметр ** должен** показывать открытую схему (более 100k ом).

![[19200215.png]]

Удалите пробный щуп из контакта 50 разъёма проводов датчика и вставьте его в контакт 47 разъёма. Вставьте другой испытательный щуп в контакт 48. Измерьте сопротивление.

Мультиметр ** должен** показывать открытую схему (более 100k ом).

![[19200210.png]]

Удалите пробный щуп из контакта 48 разъёма проводов датчика и проверьте все другие штифты. Измерьте сопротивление. Мультиметр ** должен** показывать открытую схему (более 100k ом).

Если значения сопротивления в любом из предыдущих измерительн не соответствуют спецификации, то существует короткое замыкание от контактов 47, 48, 49 или 50 до любого штифта, который измеряет менее 100k Ом. Ремонт или замена датчика проводов жгута. См. процедуру[[82-019-043-tr — Engine Wiring Harness|019-043]].

После ремонта подсоедините все компоненты.

> [!missing]- Иллюстрация `19200216.png` не извлечена — смотрите PDF-оригинал документа


> [!quote]- Original (English) · английский оригинал
> ### Resistance Check
>
> **CAUTION · Осторожно**
> Do not use probes or leads other than Part Number 3822758. The connector will be damaged. The leads must fit tightly without expanding the pins of the connector.
>
> Disconnect the sensor harness connector from the ECM. Insert a test lead into pin 47 of the sensor harness connector. Insert another test lead into pin 48 of the connector.
>
> Make sure the EPS is connected to the sensor harness.
>
> Connect the test leads to the multimeter probes. Measure the resistance. The resistance value **must** be 1000 to 2000 ohms. If the resistance value is **not** correct, there is a problem with the sensor harness, provided the sensor has been previously checked.
>
> Insert the leads into pins 50 and 49 of the sensor harness connector. Measure the resistance. The multimeter **must** show between 1000 and 2000 ohms. If the resistance is **not** correct, there is a problem with the sensor harness, provided that the sensor has been previously checked. Repair or replace the sensor harness. Refer to Procedure [[82-019-043-tr — Engine Wiring Harness|019-043]]. If both resistance checks are within specification, the sensor circuit **must** still be checked for a short circuit to ground and a short circuit from pin to pin.
>
> ### Check for Short Circuit to Ground
>
> Check for a short circuit to ground. Adjust the multimeter to the resistance setting. Insert a test lead into pin 47 of the sensor harness connector, and connect it to a multimeter probe. Touch the other multimeter probe to the engine block ground. Measure the resistance.
>
> The multimeter **must** show an open circuit (more than 100k ohms).
>
> If the circuit is **not** open, there is a short circuit to ground in the wire connected to pin 47.
>
> Repair or replace the sensor harness. Refer to Procedure [[82-019-043-tr — Engine Wiring Harness|019-043]].
>
> Remove the test lead from pin 47 of the sensor harness connector and insert it into pin 50 of the connector. Touch the other multimeter probe to the engine block ground. Measure the resistance.
>
> The multimeter **must** show an open circuit (more than 100k ohms).
>
> If the circuit is **not** open, there is a short circuit to ground in the wire connected to pin 50.
>
> Repair or replace the sensor harness. Refer to Procedure [[82-019-043-tr — Engine Wiring Harness|019-043]].
>
> ### Check for Short Circuit from Pin to Pin
>
> Disconnect the engine position sensor from the sensor harness. Insert test lead into pin 48 of the sensor harness connector. Insert other test lead into pin 45 of the connector. Set the multimeter to the resistance setting and measure the resistance.
>
> The multimeter **must** show an open circuit (more than 100k ohms).
>
> Remove the test lead from pin 45 of the sensor harness connector and check all other pins in the connector. Measure the resistance.
>
> The multimeter **must** show an open circuit (more than 100k ohms).
>
> Insert the test lead into pin 49 of the sensor harness connector and test all other pins in the connector. Measure the resistance.
>
> The multimeter **must** show an open circuit (more than 100k ohms).
>
> Remove the test lead from pin 49 of the sensor harness connector and insert it into pin 50 of the connector. Insert the other lead into pin 48. Measure the resistance.
>
> The multimeter **must** show an open circuit (more than 100k ohms).
>
> Remove the test lead from pin 48 of the sensor harness connector and check all other pins in the connector. Measure the resistance.
>
> The multimeter **must** show an open circuit (more than 100k ohms).
>
> Remove the test lead from pin 50 of the sensor harness connector and insert it into pin 47 of the connector. Insert the other test lead into pin 48. Measure the resistance.
>
> The multimeter **must** show an open circuit (more than 100k ohms).
>
> Remove the test lead from pin 48 of the sensor harness connector and test all other pins. Measure the resistance. The multimeter **must** show an open circuit (more than 100k ohms).
>
> If the resistance values in any of the previous tests are **not** within the specification, there is a short circuit from pins 47, 48, 49, or 50 to any pin that measures less than 100k ohms. Repair or replace the sensor harness. Refer to Procedure [[82-019-043-tr — Engine Wiring Harness|019-043]].
>
> Connect all components after completing the repair.
