---
aliases:
  - "Цепь общедоступной шины данных"
type: "Процедура"
doc: "98-019-026"
title_en: "Data Link Circuit, Public"
title_ru: "Цепь общедоступной шины данных"
modified: "2012-11-14"
engines:
  - "37269910"
  - "37280605"
families:
  - "K19"
manuals:
  - "3666070"
figures: 14
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-019-026.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-019-026.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K19"
  - "группа/98"
---

# Data Link Circuit, Public
**Цепь общедоступной шины данных**

> [!abstract] Процедура · `98-019-026`
> **Двигатели:** [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]]
> **Семейство:** K19
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2012-11-14
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-019-026.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-019-026.pdf)

### General Information

This circuit is used for the Compulink™, Echek™, or INSITE™ electronic service tool to communicate with the engine control module (ECM). The circuit consists of the wires connected to pin 6 and pin 8 of the main engine harness connector. There are two datalink connectors. One is located in the vicinity of the dash (usually under it) and the other is located on the main engine harness near the ECM connector.

> [!note] Note · Примечание
> Check the original equipment manufacturer (OEM) portion of this circuit. [[99-019-071 — OEM Wiring Harness|Refer to Procedure 019-071 in Section 19.]]

![[19801719.png]]

### Inspect

Disconnect the ECM connector.

Flush and clean the connector pins using contact cleaner, Part Number 3824510.

Inspect the pins in the main engine harness connector for damaged pins.

If any of the pins are damaged, repair or replace the main engine harness.

- Refer to Procedure 019-228 in Section 19.
- [[98-019-043 — Engine Wiring Harness|Refer to Procedure 019-043 in Section 19.]]

![[19801724.png]]

### Resistance Check

Disconnect the ECM connector.

Disconnect the C6 connector.

Select the resistance function on the multimeter.

Touch one of the multimeter leads to pin 6 of the main engine harness connector. Touch the other multimeter lead to pin J of the C6 connector.

![[19801725.png]]

Measure the resistance.

The multimeter **must** show less than 10 ohms, which is a closed circuit. If the circuit is **not** closed, then repair or replace the main engine harness.

- Refer to Procedure 019-228 in Section 19.
- [[98-019-043 — Engine Wiring Harness|Refer to Procedure 019-043 in Section 19.]]

![[19801619.png]]

Touch one of the multimeter leads to pin 8 of the main engine harness connector. Touch the other multimeter lead to pin H of the C6 connector.

Measure the resistance.

The multimeter **must** show less than 10 ohms. If the circuit is **not** less than 10 ohms, repair or replace the main engine harness.

- Refer to Procedure 019-228 in Section 19.
- [[98-019-043 — Engine Wiring Harness|Refer to Procedure 019-043 in Section 19.]]

![[19801727.png]]

### Check for Short Circuit to Ground

Disconnect the ECM connector.

Disconnect the C5 and C6 connectors.

Flush and clean the connector pins using contact cleaner, Part Number 3824510. Inspect the connectors for damaged pins.

Touch one of the multimeter leads to pin 6 of the main engine harness connector. Touch the other multimeter lead to a good clean surface on the engine block.

![[19801728.png]]

Measure the resistance.

The multimeter **must** show more than 100k ohms, which is an open circuit. If the circuit is **not** open, then there is a short circuit between the wire connected to pin 6 and engine block ground.

Repair or replace the main engine harness.

- Refer to Procedure 019-228 in Section 19.
- [[98-019-043 — Engine Wiring Harness|Refer to Procedure 019-043 in Section 19.]]

![[19801621.png]]

Touch one of the multimeter leads to pin 8 of the main engine harness connector. Touch the other multimeter lead to pin H of the C6 connector.

Measure the resistance.

The multimeter **must** show more than 100k ohms. If the circuit is **not** more than 100k ohms, repair or replace the main engine harness.

- Refer to Procedure 019-228 in Section 19.
- [[98-019-043 — Engine Wiring Harness|Refer to Procedure 019-043 in Section 19.]]

![[19801730.png]]

### Check for Short Circuit from Pin to Pin

Disconnect the ECM, C5, and C6 connectors.

Flush and clean the connector pins.

Inspect the connectors for damaged pins.

Check for a short circuit between pin 6 of the main engine harness connector and all other pins in the connector, except pin 8.

Touch one of the multimeter leads to pin 6 of the connector. Touch the other multimeter lead to all other pins in the connector except for pin 8, one at a time.

![[19801731.png]]

Measure the resistance.

The multimeter **must** show more than 100k ohms, which is an open circuit. If the circuit is **not** open, then there is a short between the wire connected to pin 6 of the main engine harness connector and any other pin that measured less than 100k ohms.

Repair or replace the main engine harness.

- Refer to Procedure 019-228 in Section 19.
- [[98-019-043 — Engine Wiring Harness|Refer to Procedure 019-043 in Section 19.]]

![[19801621.png]]

Touch one of the multimeter leads to pin 8 of the main engine harness connector. Touch the other multimeter lead to all other pins in the connector, except pin 6, one at a time.

Measure the resistance.

The multimeter should measure more than 100k ohms. If the measured resistances are **not** greater than 100k ohms, then repair or replace the main engine harness.

- Refer to Procedure 019-228 in Section 19.
- [[98-019-043 — Engine Wiring Harness|Refer to Procedure 019-043 in Section 19.]]

![[19802406.png]]

### Polarity Check

Locate the datalink connector of the main engine harness. The data link wires nunber 6 and number 8 are in the 2-pin Weather-Pack™ connector.

![[19801720.png]]

Touch the multimeter positive (+) lead to pin B of the datalink connector. Touch the negative (-) multimeter lead to the engine block ground. Measure the voltage.The multimeter **must** show 0 to 1 VDC.

![[19801772.png]]

If the voltage at pin B measures 4 to 5 VDC, the pins in the 2-pin Weather-Pack™ connector are improperly installed and **must** be reversed.

If the voltage and polarity are correct, the circuit **must** be checked for short circuit to ground and short circuits from pin-to-pin.

![[19801723.png]]
