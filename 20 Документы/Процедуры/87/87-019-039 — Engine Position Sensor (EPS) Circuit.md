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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-019-039.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-019-039.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
---

# Engine Position Sensor (EPS) Circuit
**Цепь датчика положения коленвала (EPS)**

> [!abstract] Процедура · `87-019-039`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2018-08-09
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-019-039.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-019-039.pdf)

### Resistance Check

The engine position sensor circuit includes pin 10 (+5-VDC supply wire), pin 9 (signal wire), and pin 19 (sensor return).

Disconnect the engine harness from the ECM.

Disconnect the engine harness from the engine position sensor.

Check for damaged pins.

![[19900781.png]]

**+5-VDC Supply Wire Resistance - Checking**

> [!warning] CAUTION · Осторожно
> Do not use probes or leads other than Part Number 3822758. The connector will be damaged. The leads must fit tightly in the connector without expanding the pins in the connector.

Insert the test lead into pin 10 of the engine harness connector. Connect the alligator clip to the multimeter probe. Touch the other multimeter probe to pin A of the engine position sensor connector, harness side.

![[19a00264.png]]

Measure the resistance. The multimeter **must** show a closed circuit (10 ohms or less). If more than 10 ohms are measured, there is an open circuit in the +5-VDC supply wire. Repair the +5-VDC supply wire or replace the engine harness.

[[87-019-250 — Connector, 50-Pin|Refer to Procedure 019-250]], [[99-019-203 — AMP Connector Series|Refer to Procedure 019-203]], or [[87-019-043 — Engine Wiring Harness|Refer to Procedure 019-043]].

![[19a00264.png]]

**Signal Wire Resistance - Checking**

Insert the test lead into pin 9 of the engine harness connector. Connect the alligator clip to the multimeter probe. Touch the other probe to pin C of the engine position sensor connector, harness side.

![[19a00265.png]]

Measure the resistance. The multimeter **must** show a closed circuit (10 ohms or less). If more than 10 ohms are measured, there is an open circuit in the signal wire. Repair the signal wire or replace the engine harness.

[[87-019-250 — Connector, 50-Pin|Refer to Procedure 019-250]], [[99-019-203 — AMP Connector Series|Refer to Procedure 019-203]], or [[87-019-043 — Engine Wiring Harness|Refer to Procedure 019-043]].

![[19a00265.png]]

**Return Wire Resistance - Checking**

Insert the test lead into pin 19 of the engine harness connector. Connect the alligator clip to the multimeter probe. Touch the other probe to pin B of the engine position sensor connector, harness side.

![[19a00266.png]]

Measure the resistance. The multimeter **must** show a closed circuit (10 ohms or less). If more than 10 ohms are measured, there is an open circuit in the return wire. Repair the return wire or replace the engine harness.

[[87-019-250 — Connector, 50-Pin|Refer to Procedure 019-250]], [[99-019-203 — AMP Connector Series|Refer to Procedure 019-203]], or [[87-019-043 — Engine Wiring Harness|Refer to Procedure 019-043]].

![[19a00266.png]]

### Check for Short Circuit to Ground

**Return Wire - Checking**

> [!warning] CAUTION · Осторожно
> Do not use probes or test leads other than Part Number 3822758. The connector will be damaged. The leads must fit tightly in the connector without expanding the pins in the connector.

Disconnect the engine harness from the ECM.

Insert the test lead into pin 19 of the engine harness connector. Connect the alligator clip to the multimeter probe. Touch the other probe to the engine block.

![[19900529.png]]

Measure the resistance. The multimeter **must** show an open circuit (100k ohms or more). If less than 100k ohms are measured, there is a short circuit to ground in the return wire.

Repair the return wire or replace the engine harness. [[87-019-250 — Connector, 50-Pin|Refer to Procedure 019-250]], [[99-019-203 — AMP Connector Series|Refer to Procedure 019-203]], or [[87-019-043 — Engine Wiring Harness|Refer to Procedure 019-043]].

![[19900529.png]]

**Signal Wire - Checking**

Make sure the engine position sensor is disconnected from the engine harness.

Insert the test lead into pin 9 of the engine harness connector. Connect the alligator clip to the multimeter probe. Touch the other probe to the engine block.

![[19a00707.png]]

Measure the resistance. The multimeter **must** show an open circuit (100k ohms or more). If less than 100k ohms are measured, there is a short circuit to ground in the signal wire. Repair the signal wire or replace the engine harness.

[[87-019-250 — Connector, 50-Pin|Refer to Procedure 019-250]], [[99-019-203 — AMP Connector Series|Refer to Procedure 019-203]], or [[87-019-043 — Engine Wiring Harness|Refer to Procedure 019-043]].

![[19a00707.png]]

**+5-VDC Supply Wire - Checking**

Insert the test lead into pin 10 of the engine harness connector. Connect the alligator clip to the multimeter probe. Touch the other probe to the engine block.

> [!missing]- Иллюстрация `19a00708.png` не извлечена — смотрите PDF-оригинал документа

Measure the resistance. The multimeter **must** show an open circuit (100k ohms or more). If less than 100k ohms are measured, there is a short circuit to ground in the +5-VDC supply wire.

Repair the +5-VDC supply wire or replace the engine harness.

[[87-019-250 — Connector, 50-Pin|Refer to Procedure 019-250]], [[99-019-203 — AMP Connector Series|Refer to Procedure 019-203]], or [[87-019-043 — Engine Wiring Harness|Refer to Procedure 019-043]].

> [!missing]- Иллюстрация `19a00708.png` не извлечена — смотрите PDF-оригинал документа

### Check for Short Circuit from Pin-to-Pin

> [!warning] CAUTION · Осторожно
> Do not use probes or test leads other than Part Number 3822758. The connector will be damaged. The leads must fit tightly in the connector without expanding the connector pins.

**Signal Wire - Checking**

Disconnect the OEM and engine harnesses from the ECM.

Insert a test lead into pin 9 of the engine harness connector. Connect the alligator clips to the multimeter probes. Insert the other lead into all other pins of the engine harness connector. Measure the resistance.

> [!missing]- Иллюстрация `19900533.png` не извлечена — смотрите PDF-оригинал документа

Then, repeat the pin-to-pin check from pin 9 of the engine harness connector to all pins in the OEM interface harness connector.

Measure the resistance.

> [!missing]- Иллюстрация `19a00710.png` не извлечена — смотрите PDF-оригинал документа

For all pin checks, the multimeter **must** show an open circuit (100k ohms or more). If the circuit is **not** open, there is a short circuit between the signal wire pin and any pin that measured a closed circuit.

Repair or replace the engine harness.

[[87-019-250 — Connector, 50-Pin|Refer to Procedure 019-250]] or [[87-019-043 — Engine Wiring Harness|Refer to Procedure 019-043]].

> [!missing]- Иллюстрация `19a00710.png` не извлечена — смотрите PDF-оригинал документа

**Return Wire - Checking**

Insert a test lead into pin 19 of the engine harness connector. Connect the alligator clips to the multimeter probes. Insert the other lead into all other pins of the engine harness connector.

Measure the resistance.

> [!missing]- Иллюстрация `19a00711.png` не извлечена — смотрите PDF-оригинал документа

Then, repeat the pin-to-pin check from pin 19 of the engine harness connector to all pins in the OEM interface harness connector.

Measure the resistance.

> [!missing]- Иллюстрация `19a00711.png` не извлечена — смотрите PDF-оригинал документа

For all pin checks, the multimeter **must** show an open circuit (100k ohms or more). If the circuit is **not** open, there is a short circuit between the return wire pin and any pin that measured a closed circuit. Repair or replace the engine harness.

[[87-019-250 — Connector, 50-Pin|Refer to Procedure 019-250]] or [[87-019-043 — Engine Wiring Harness|Refer to Procedure 019-043]].

> [!missing]- Иллюстрация `19a00711.png` не извлечена — смотрите PDF-оригинал документа
