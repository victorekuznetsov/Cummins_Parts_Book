---
aliases:
  - "Цепь общедоступной шины данных"
type: "Процедура"
doc: "96-019-026"
title_en: "Data Link Circuit, Public"
title_ru: "Цепь общедоступной шины данных"
modified: "2004-04-28"
engines:
  - "37292556"
  - "37295879"
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
  - "QST30"
manuals:
  - "3666231"
figures: 11
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/96/96-019-026.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/96-019-026.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "двигатель/QST30"
  - "группа/96"
---

# Data Link Circuit, Public
**Цепь общедоступной шины данных**

> [!abstract] Процедура · `96-019-026`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]], [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11, QST30
> **Входит в руководства:** [[3666231 — Centinel™ Master Repair Manual|3666231]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2004-04-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/96/96-019-026.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/96-019-026.pdf)

### General Information

Heavy-Duty Only

To communicate with the Centinel™ control module, the public datalink circuit is used for an electronic service tool.

> [!note] Note · Примечание
> No service tool is provided for Heavy-Duty applications. The Centinel™ control module will use the public datalink.

![[19800337.png]]

For Celect™ Plus engines, the datalink is powered and uses a 6-pin Deutsch connector. (For Celect™ engines, the public datalink is accessed by the control harness through splices in the cab.) The wiring positions follow:

Position A - Datalink (+)

Position B - Datalink (-)

Position C - Battery (12 or 24 VDC)

Position D - Open

Position E - Block ground

Position F -

Not

used.

![[19801499.png]]

### Resistance Check

> [!warning] CAUTION · Осторожно
> Use test lead, Part Number 3822758, on the Centinel™ control module connector and use test lead, Part Number 3823993, on the 6-pin Deutsch connector to avoid damage to the connector pins.

Disconnect the harness connector from the Centinel™ control module and the Deutsch 6-pin connector.

Turn the keyswitch to the “OFF” position.

Measure the resistance from pin 8 (Heavy-Duty) or pin 6 (High-Horsepower) of the Centinel™ control module harness connector to pin A of the 6-pin Deutsch connector (or the proper wire splice for the Celect installation).

The multimeter **must** show a closed circuit (10 ohms or less).

If the circuit is **not** closed, repair or replace the Centinel™ harness. Refer to Procedure [[96-019-131-tr — Centinel™ Wiring Harness|019-131]].

![[19801500.png]]

Measure the resistance from pin 9 (Heavy-Duty) or pin 8 (High-Horsepower) of the Centinel™ control module harness connector to pin B of the 6-pin Deutsch connector (or the proper wire splice for the Celect™ installation).

The multimeter **must** show a closed circuit (10 ohms or less).

If the circuit is **not** closed, repair or replace the Centinel™ harness. Refer to Procedure [[96-019-131-tr — Centinel™ Wiring Harness|019-131]].

![[19801501.png]]

### Check for Short Circuit to Ground

> [!warning] CAUTION · Осторожно
> Use test lead, Part Number 3823993, for the 6-pin Deutsch connector to avoid damage to the connector pins.

Disconnect the harness connector from the Centinel™ control module.

Measure the resistance from pin A of the Deutsch connector or pin 8 of the Centinel™ control module harness connector to the engine block.

The multimeter **must** show an open circuit (1M ohms or more).

If the circuit is **not** open, repair or replace the Centinel™ harness. Refer to Procedure [[96-019-131-tr — Centinel™ Wiring Harness|019-131]].

![[19801502.png]]

Measure the resistance from pin B of the 6-pin Deutsch connector or pin 9 of the Centinel™ control module harness connector to the engine block. The multimeter **must** show an open circuit (1M ohms or more).

If the circuit is **not** open, repair or replace the Centinel™ harness. Refer to Procedure [[96-019-131-tr — Centinel™ Wiring Harness|019-131]].

![[19801503.png]]

### Check for Short Circuit from Pin to Pin

Deutsch

Measure the resistance from pin B to all other pins in the connector. The multimeter **must** show an open circuit (1M ohms or more).

If the circuit is **not** open, repair or replace the Centinel™ harness. Refer to the appropriate base engine troubleshooting and repair manual.

![[19801505.png]]

Measure the resistance from pin C to all other pins in the connector. The multimeter **must** show an open circuit (1M ohms or more).

If the circuit is **not** open, repair or replace the Centinel™ harness. Refer to the appropriate base engine troubleshooting and repair manual.

![[19801506.png]]

### Voltage Check

Locate the datalink connector on the Centinel™ harness. The location will depend on the installation procedures.

![[19801507.png]]

> [!warning] CAUTION · Осторожно
> Use test lead, Part Number 3823993, for the 6-pin Deutsch connector to avoid damage to the connector pins.

Turn the keyswitch ON.

Turn the dial on the multimeter to measure DC voltage.

Measure the voltage from pin 8 of the Centinel™ control module harness connector to the engine block. The multimeter **must** show 2.5 to 5 VDC.

![[19801508.png]]

Measure the voltage from pin 9 of the Centinel™ control module harness connector to the engine block. The multimeter **must** show 0 to 2.5 VDC.

![[19801509.png]]
