---
aliases:
  - "Выключатель подтверждения промежуточной частоты вращения"
type: "Процедура"
doc: "82-019-108"
title_en: "Intermediate Speed Control Validation Switch"
title_ru: "Выключатель подтверждения промежуточной частоты вращения"
modified: "2005-01-28"
engines:
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 7
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-108.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-019-108.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# Intermediate Speed Control Validation Switch
**Выключатель подтверждения промежуточной частоты вращения**

> [!abstract] Процедура · `82-019-108`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section 19 - Electronic Engine Controls
> **Даты:** изменён 2005-01-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-108.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-019-108.pdf)

### Resistance Check

Disconnect the OEM harness connector from the ECM.

Use test lead, Part Number 3822758, on the ECM connectors.

Disconnect the bulkhead connector.

Measure the resistance from pin 23 of the OEM harness connector to the corresponding pin of the bulkhead connector (refer to the OEM troubleshooting and repair manual). The multimeter **must** show a closed circuit (10 ohms or less).

If the circuit is **not** closed, repair or replace the wiring harness. Refer to Procedure 019-043.

![[19c00908.png]]

Measure the resistance from pin 25 of the OEM harness connector to the corresponding pin of the bulkhead connector (refer to the OEM troubleshooting and repair manual). The multimeter **must** show a closed circuit (10 ohms or less).

If the circuit is **not** closed, repair or replace the wiring harness. Refer to Procedure 019-043.

![[19c00909.png]]

Measure the resistance from pin 33 of the OEM harness connector to the corresponding pin of the bulkhead connector (refer to the OEM troubleshooting and repair manual). The multimeter **must** show a closed circuit (10 ohms or less).

If the circuit is **not** closed, repair or replace the wiring harness. Refer to Procedure 019-043.

If the OEM harness on the engine side of the bulkhead connector passes the above resistance checks, check the resistance of the vehicle side of the bulkhead connector. See the vehicle manufacturer's instructions.

![[19c00910.png]]

### Check for Short Circuit to Ground

Disconnect the OEM harness connector from the ECM.

Use test lead, Part Number 3822758.

Move the ISC switch to the center (OFF) position.

Measure the resistance from pins 23, 25, and 33 to the engine block. The multimeter **must** show 100k ohms or more.

If the circuit is **not** open, check for short circuit to ground in the OEM wiring harness, provided the switch has been checked previously.

![[19c00911.png]]

Disconnect the bulkhead harness connector.

Measure the resistance from the ECM connector pins 23, 25, and 33 to the engine block. The multimeter **must** show 100k ohms or more.

If the circuit is **not** open, check for short circuit to ground in the vehicle side of the bulkhead connector. See the vehicle manufacturer's instructions.

![[19c00911.png]]

### Check for Short Circuit from Pin to Pin

Disconnect the OEM harness connector from the ECM.

Use test lead, Part Number 3822758 on the ECM connector.

Measure the resistance from pin 23 of the OEM harness connector to all other pins in the connector. The multimeter **must** show an open circuit (100k ohms or more).

Measure the resistance from pin 33 of the OEM harness connector to all other pins in the connector. The multimeter **must** show an open circuit (100k ohms or more).

Measure the resistance from pin 25 of the OEM harness connector to all other pins in the connector. The multimeter **must** show an open circuit (100k ohms or more).

If the circuit is **not** open, check for a short circuit from pin to pin on the engine side of the bulkhead connector, provided the switch has been checked earlier.

![[19c00912.png]]

Disconnect the bulkhead connector.

Measure the resistance from pin 23 of the OEM harness connector to all other pins in the connector. The multimeter **must** show an open circuit (100k ohms or more).

Measure the resistance from pin 33 of the OEM harness connector to all other pins in the connector. The multimeter **must** show an open circuit (100k ohms or more).

Measure the resistance from pin 25 of the OEM harness connector to all other pins in the connector. The multimeter **must** show an open circuit (100k ohms or more).

If the circuit is **not** open, check for a short circuit from pin to pin on the vehicle side of the bulkhead connector. See the vehicle manufacturer's instructions.

Connect all components after completing the repair.

![[19c00912.png]]
