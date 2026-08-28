---
aliases:
  - "Цепь датчика положения коленвала (EPS)"
type: "Процедура"
doc: "87-019-039"
title_en: "Engine Position Sensor (EPS) Circuit"
title_ru: "Цепь датчика положения коленвала (EPS)"
modified: "2018-08-09"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666214"
figures: 19
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-019-039.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-019-039.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
  - "перевод/машинный"
---

# Engine Position Sensor (EPS) Circuit
**Цепь датчика положения коленвала (EPS)**

> [!abstract] Процедура · `87-019-039`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2018-08-09
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-019-039.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-019-039.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Проверка сопротивления

Схема датчика положения двигателя включает контакт 10 (провод питания +5-VDC), контакт 9 (сигнальный провод) и контакт 19 (возврат датчика).

Отсоедините электропроводку двигателя от ECM.

Отсоедините проводку двигателя от датчика положения двигателя.

Проверьте наличие поврежденных контактов.

![[19900781.png]]

**+5-VDC сопротивление проводов - проверка**

> [!warning] ОСТОРОЖНО
> Не используйте щупы или провода, отличные от Части № 3822758. Разъём будет повреждён. Лиды должны плотно помещаться в разъеме без расширения штифтов в разъеме.

Включить испытательный щуп в контакт 10 разъёма ремня электропроводки двигателя. Подключите аллигатор к многометровому щупу. Прикоснитесь к другому многометровому щупу, чтобы связаться с А разъемом датчика положения двигателя, проводкой спрятанной стороны.

![[19a00264.png]]

Измерьте сопротивление. Мультиметр **должен** показать замкнутую цепь (10 Ом и менее). Если измеряется более 10 Ом, то в проводе питания +5-VDC имеется открытая цепь. Ремонт провода питания +5-VDC или замена жгута проводов двигателя.

[[87-019-250 — Connector, 50-Pin|См. процедуру 019-250]],[[99-019-203 — AMP Connector Series|См. процедуру 019-203]]или[[87-019-043 — Engine Wiring Harness|См. процедуру 019-043]].

![[19a00264.png]]

**Сопротивление сигнальной проводов - Проверка**

Включить испытательный щуп в контакт 9 разъёма проводов двигателя. Подключите аллигатор к многометровому щупу. Прикоснитесь к другому щупу, чтобы связаться с C разъемом датчика положения двигателя, проводкой с жгута проводов.

![[19a00265.png]]

Измерьте сопротивление. Мультиметр **должен** показать замкнутую цепь (10 Ом и менее). Если измеряется более 10 Ом, в сигнальном проводе имеется открытая схема. Ремонт сигнального провода или замена жгута проводов двигателя.

[[87-019-250 — Connector, 50-Pin|См. процедуру 019-250]],[[99-019-203 — AMP Connector Series|См. процедуру 019-203]]или[[87-019-043 — Engine Wiring Harness|См. процедуру 019-043]].

![[19a00265.png]]

**Возвращение сопротивления провода - Проверка**

Включить испытательный щуп в контакт 19 разъёма ремней электропроводки двигателя. Подключите аллигатор к многометровому щупу. Прикоснитесь к другому щупу, чтобы связаться с B разъемом датчика положения двигателя, проводкой спрятанной стороны.

![[19a00266.png]]

Измерьте сопротивление. Мультиметр **должен** показать замкнутую цепь (10 Ом и менее). Если измеряется более 10 Ом, в обратном проводе имеется открытая цепь. Почините обратный провод или замените жгут проводов двигателя.

[[87-019-250 — Connector, 50-Pin|См. процедуру 019-250]],[[99-019-203 — AMP Connector Series|См. процедуру 019-203]]или[[87-019-043 — Engine Wiring Harness|См. процедуру 019-043]].

![[19a00266.png]]

### Проверка на замыкание на массу

**Возврат провода - Проверка**

> [!warning] ОСТОРОЖНО
> Не используйте щупы или испытательные щупы, кроме Части № 3822758. Разъём будет повреждён. Лиды должны плотно помещаться в разъеме без расширения штифтов в разъеме.

Отсоедините электропроводку двигателя от ECM.

Включить испытательный щуп в контакт 19 разъёма ремней электропроводки двигателя. Подключите аллигатор к многометровому щупу. Прикоснитесь к другому щупу блока двигателя.

![[19900529.png]]

Измерьте сопротивление. Мультиметр **должен** показать обрыв цепи (100 кОм и более). Если измеряется менее 100k Ом, в обратном проводе есть короткое замыкание на землю.

Почините обратный провод или замените жгут проводов двигателя.[[87-019-250 — Connector, 50-Pin|См. процедуру 019-250]],[[99-019-203 — AMP Connector Series|См. процедуру 019-203]]или[[87-019-043 — Engine Wiring Harness|См. процедуру 019-043]].

![[19900529.png]]

**Сигнальная проволока - Проверка**

Убедитесь, что датчик положения двигателя отключен от электропроводки двигателя.

Включить испытательный щуп в контакт 9 разъёма проводов двигателя. Подключите аллигатор к многометровому щупу. Прикоснитесь к другому щупу блока двигателя.

![[19a00707.png]]

Измерьте сопротивление. Мультиметр **должен** показать обрыв цепи (100 кОм и более). Если измеряется менее 100k Ом, в сигнальном проводе есть короткое замыкание на землю. Ремонт сигнального провода или замена жгута проводов двигателя.

[[87-019-250 — Connector, 50-Pin|См. процедуру 019-250]],[[99-019-203 — AMP Connector Series|См. процедуру 019-203]]или[[87-019-043 — Engine Wiring Harness|См. процедуру 019-043]].

![[19a00707.png]]

**+5-VDC Провода - Проверка**

Включить испытательный щуп в контакт 10 разъёма ремня электропроводки двигателя. Подключите аллигатор к многометровому щупу. Прикоснитесь к другому щупу блока двигателя.

> [!missing]- Иллюстрация `19a00708.png` не извлечена — смотрите PDF-оригинал документа

Измерьте сопротивление. Мультиметр **должен** показать обрыв цепи (100 кОм и более). Если измеряется менее 100k ом, в проводе питания +5-VDC есть короткое замыкание на землю.

Ремонт провода питания +5-VDC или замена жгута проводов двигателя.

[[87-019-250 — Connector, 50-Pin|См. процедуру 019-250]],[[99-019-203 — AMP Connector Series|См. процедуру 019-203]]или[[87-019-043 — Engine Wiring Harness|См. процедуру 019-043]].

> [!missing]- Иллюстрация `19a00708.png` не извлечена — смотрите PDF-оригинал документа

### Проверьте короткое замыкание от контакта к контакту

> [!warning] ОСТОРОЖНО
> Не используйте щупы или испытательные щупы, кроме Части № 3822758. Разъём будет повреждён. Лиды должны плотно помещаться в разъеме без расширения контактов разъема.

**Сигнальная проволока - Проверка**

Отсоедините OEM- и электропроводку двигателя от ECM.

Включить испытательный щуп в контакт 9 разъёма проводов двигателя. Подключите аллигаторы к многометровым зондам. Вставьте другой свинец во все другие штифты разъема жгута двигателя. Измерьте сопротивление.

> [!missing]- Иллюстрация `19900533.png` не извлечена — смотрите PDF-оригинал документа

Затем повторите проверку контакта с контактом от контакта 9 разъёма жгутов проводов двигателя ко всем штифтам в разъёме ремней OEM-интерфейса.

Измерьте сопротивление.

> [!missing]- Иллюстрация `19a00710.png` не извлечена — смотрите PDF-оригинал документа

Для всех проверок пин-кодов мультиметр **должен** показывать открытую схему (100k Ом или более). Если цепь **не** открыта, между штифтом сигнального провода и любым штифтом, который измерял замкнутую цепь, есть короткое замыкание.

Ремонт или замена ремня электропроводки двигателя.

[[87-019-250 — Connector, 50-Pin|См. процедуру 019-250]]или[[87-019-043 — Engine Wiring Harness|См. процедуру 019-043]].

> [!missing]- Иллюстрация `19a00710.png` не извлечена — смотрите PDF-оригинал документа

**Возврат провода - Проверка**

Включить испытательный щуп в контакт 19 разъёма ремней электропроводки двигателя. Подключите аллигаторы к многометровым зондам. Вставьте другой свинец во все другие штифты разъема жгута двигателя.

Измерьте сопротивление.

> [!missing]- Иллюстрация `19a00711.png` не извлечена — смотрите PDF-оригинал документа

Затем повторите проверку контакта с контактом от контакта 19 разъёма жгутов проводов двигателя ко всем штифтам в разъёме ремней OEM-интерфейса.

Измерьте сопротивление.

> [!missing]- Иллюстрация `19a00711.png` не извлечена — смотрите PDF-оригинал документа

Для всех проверок пин-кодов мультиметр **должен** показывать открытую схему (100k Ом или более). Если цепь **не** открыта, между штифтом обратной проволоки и любым штифтом, который измерял замкнутую цепь, есть короткое замыкание. Ремонт или замена ремня электропроводки двигателя.

[[87-019-250 — Connector, 50-Pin|См. процедуру 019-250]]или[[87-019-043 — Engine Wiring Harness|См. процедуру 019-043]].

> [!missing]- Иллюстрация `19a00711.png` не извлечена — смотрите PDF-оригинал документа


> [!quote]- Original (English) · английский оригинал
> ### Resistance Check
>
> The engine position sensor circuit includes pin 10 (+5-VDC supply wire), pin 9 (signal wire), and pin 19 (sensor return).
>
> Disconnect the engine harness from the ECM.
>
> Disconnect the engine harness from the engine position sensor.
>
> Check for damaged pins.
>
> **+5-VDC Supply Wire Resistance - Checking**
>
> **CAUTION · Осторожно**
> Do not use probes or leads other than Part Number 3822758. The connector will be damaged. The leads must fit tightly in the connector without expanding the pins in the connector.
>
> Insert the test lead into pin 10 of the engine harness connector. Connect the alligator clip to the multimeter probe. Touch the other multimeter probe to pin A of the engine position sensor connector, harness side.
>
> Measure the resistance. The multimeter **must** show a closed circuit (10 ohms or less). If more than 10 ohms are measured, there is an open circuit in the +5-VDC supply wire. Repair the +5-VDC supply wire or replace the engine harness.
>
> [[87-019-250 — Connector, 50-Pin|Refer to Procedure 019-250]], [[99-019-203 — AMP Connector Series|Refer to Procedure 019-203]], or [[87-019-043 — Engine Wiring Harness|Refer to Procedure 019-043]].
>
> **Signal Wire Resistance - Checking**
>
> Insert the test lead into pin 9 of the engine harness connector. Connect the alligator clip to the multimeter probe. Touch the other probe to pin C of the engine position sensor connector, harness side.
>
> Measure the resistance. The multimeter **must** show a closed circuit (10 ohms or less). If more than 10 ohms are measured, there is an open circuit in the signal wire. Repair the signal wire or replace the engine harness.
>
> [[87-019-250 — Connector, 50-Pin|Refer to Procedure 019-250]], [[99-019-203 — AMP Connector Series|Refer to Procedure 019-203]], or [[87-019-043 — Engine Wiring Harness|Refer to Procedure 019-043]].
>
> **Return Wire Resistance - Checking**
>
> Insert the test lead into pin 19 of the engine harness connector. Connect the alligator clip to the multimeter probe. Touch the other probe to pin B of the engine position sensor connector, harness side.
>
> Measure the resistance. The multimeter **must** show a closed circuit (10 ohms or less). If more than 10 ohms are measured, there is an open circuit in the return wire. Repair the return wire or replace the engine harness.
>
> [[87-019-250 — Connector, 50-Pin|Refer to Procedure 019-250]], [[99-019-203 — AMP Connector Series|Refer to Procedure 019-203]], or [[87-019-043 — Engine Wiring Harness|Refer to Procedure 019-043]].
>
> ### Check for Short Circuit to Ground
>
> **Return Wire - Checking**
>
> **CAUTION · Осторожно**
> Do not use probes or test leads other than Part Number 3822758. The connector will be damaged. The leads must fit tightly in the connector without expanding the pins in the connector.
>
> Disconnect the engine harness from the ECM.
>
> Insert the test lead into pin 19 of the engine harness connector. Connect the alligator clip to the multimeter probe. Touch the other probe to the engine block.
>
> Measure the resistance. The multimeter **must** show an open circuit (100k ohms or more). If less than 100k ohms are measured, there is a short circuit to ground in the return wire.
>
> Repair the return wire or replace the engine harness. [[87-019-250 — Connector, 50-Pin|Refer to Procedure 019-250]], [[99-019-203 — AMP Connector Series|Refer to Procedure 019-203]], or [[87-019-043 — Engine Wiring Harness|Refer to Procedure 019-043]].
>
> **Signal Wire - Checking**
>
> Make sure the engine position sensor is disconnected from the engine harness.
>
> Insert the test lead into pin 9 of the engine harness connector. Connect the alligator clip to the multimeter probe. Touch the other probe to the engine block.
>
> Measure the resistance. The multimeter **must** show an open circuit (100k ohms or more). If less than 100k ohms are measured, there is a short circuit to ground in the signal wire. Repair the signal wire or replace the engine harness.
>
> [[87-019-250 — Connector, 50-Pin|Refer to Procedure 019-250]], [[99-019-203 — AMP Connector Series|Refer to Procedure 019-203]], or [[87-019-043 — Engine Wiring Harness|Refer to Procedure 019-043]].
>
> **+5-VDC Supply Wire - Checking**
>
> Insert the test lead into pin 10 of the engine harness connector. Connect the alligator clip to the multimeter probe. Touch the other probe to the engine block.
>
> Measure the resistance. The multimeter **must** show an open circuit (100k ohms or more). If less than 100k ohms are measured, there is a short circuit to ground in the +5-VDC supply wire.
>
> Repair the +5-VDC supply wire or replace the engine harness.
>
> [[87-019-250 — Connector, 50-Pin|Refer to Procedure 019-250]], [[99-019-203 — AMP Connector Series|Refer to Procedure 019-203]], or [[87-019-043 — Engine Wiring Harness|Refer to Procedure 019-043]].
>
> ### Check for Short Circuit from Pin-to-Pin
>
> **CAUTION · Осторожно**
> Do not use probes or test leads other than Part Number 3822758. The connector will be damaged. The leads must fit tightly in the connector without expanding the connector pins.
>
> **Signal Wire - Checking**
>
> Disconnect the OEM and engine harnesses from the ECM.
>
> Insert a test lead into pin 9 of the engine harness connector. Connect the alligator clips to the multimeter probes. Insert the other lead into all other pins of the engine harness connector. Measure the resistance.
>
> Then, repeat the pin-to-pin check from pin 9 of the engine harness connector to all pins in the OEM interface harness connector.
>
> Measure the resistance.
>
> For all pin checks, the multimeter **must** show an open circuit (100k ohms or more). If the circuit is **not** open, there is a short circuit between the signal wire pin and any pin that measured a closed circuit.
>
> Repair or replace the engine harness.
>
> [[87-019-250 — Connector, 50-Pin|Refer to Procedure 019-250]] or [[87-019-043 — Engine Wiring Harness|Refer to Procedure 019-043]].
>
> **Return Wire - Checking**
>
> Insert a test lead into pin 19 of the engine harness connector. Connect the alligator clips to the multimeter probes. Insert the other lead into all other pins of the engine harness connector.
>
> Measure the resistance.
>
> Then, repeat the pin-to-pin check from pin 19 of the engine harness connector to all pins in the OEM interface harness connector.
>
> Measure the resistance.
>
> For all pin checks, the multimeter **must** show an open circuit (100k ohms or more). If the circuit is **not** open, there is a short circuit between the return wire pin and any pin that measured a closed circuit. Repair or replace the engine harness.
>
> [[87-019-250 — Connector, 50-Pin|Refer to Procedure 019-250]] or [[87-019-043 — Engine Wiring Harness|Refer to Procedure 019-043]].
