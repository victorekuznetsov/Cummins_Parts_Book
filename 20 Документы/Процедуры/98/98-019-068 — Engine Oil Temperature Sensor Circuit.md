---
type: "Процедура"
doc: "98-019-068"
title_en: "Engine Oil Temperature Sensor Circuit"
modified: "2003-04-01"
engines:
  - "37269910"
  - "37280605"
families:
  - "K19"
manuals:
  - "3666070"
figures: 11
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-019-068.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-019-068.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K19"
  - "группа/98"
---

# Engine Oil Temperature Sensor Circuit

> [!abstract] Процедура · `98-019-068`
> **Двигатели:** [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]]
> **Семейство:** K19
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-04-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-019-068.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-019-068.pdf)

### General Information

The portion of the oil temperature sensor circuit in the main engine harness consists of the signal wire (pin 28) and the return wire (pin 25 or 26).

The portion of the circuit in the OEM harness consists of the signal wire (pin C5-D) and the return wire (C5-H).

![[19801801.png]]

### Resistance Check

Disconnect the ECM and the C5 connectors.

Select the resistance function on the multimeter.

Touch one of the multimeter leads to pin 28 of the main engine harness connector. Touch the other multimeter lead to pin D on the main engine harness side of the C5 connector.

![[19801802.png]]

Measure the resistance.

The multimeter **must** show less than 10 ohms, which is a closed circuit. If the circuit is **not** closed, there is an open circuit in the signal wire.

Repair or replace the main engine harness. Refer to Procedure 019-228 or [[98-019-043 — Engine Wiring Harness|019-043]].

![[19801619.png]]

Repeat the above resistance check for the return wire.

Touch one of the multimeter leads to either pin 25 or pin 26 of the main engine harness connector. Touch the other multimeter lead to pin H of the main engine harness side of the C5 connector.

Measure the resistance. The multimeter **must** show less than 10 ohms.

> [!note] Note · Примечание
> The system will operate properly if **only** one of the battery return wires is working. However, if the circuit is open on one of the battery return wires, then the main engine harness should be repaired.

![[19801804.png]]

Disconnect the sensor connector. Make sure the C5 connector is disconnected.

Check the OEM portion (pins C5-E and C5-H) of the circuit for open circuits and short circuits. Refer to Procedure 019-071.

![[19801834.png]]

### Check for Short Circuit to Ground

Make sure the ECM and C5 connectors are disconnected.

Touch one of the multimeter leads to pin 28 of the main engine harness connector. Touch the other multimeter lead to engine block ground.

![[19801805.png]]

Measure the resistance.

The multimeter **must** show more than 100k ohms, which is an open circuit. If the circuit is **not** open, there is a short circuit between the wire connected to pin 28 and chassis ground.

Repair or replace the main engine harness. Refer to Procedure 019-228 or [[98-019-043 — Engine Wiring Harness|019-043]].

![[19801621.png]]

### Check for Short Circuit from Pin to Pin

Make sure the ECM connector and the C5 and C6 connectors are disconnected.

Check for a short circuit between pin 28 of the main engine harness connector and **all** other pins in the connector.

Touch one of the multimeter leads to pin 28 of the main engine harness connector. Touch the other multimeter lead to **all** other pins in the connector, one at a time.

![[19801807.png]]

Measure the resistance.

The multimeter **must** show more than 100k ohms, which is an open circuit. If the circuit is **not** open, there is a short between the wires connected to pin 28 of the main engine harness connector and **any** other pin that measured less than 100k ohms.

Repair or replace the main engine harness. Refer to Procedure 019-228 or [[98-019-043 — Engine Wiring Harness|019-043]].

![[19801621.png]]

Repeat the above short circuit from pin to pin check on the return wire.

Touch one of the multimeter leads to pin 25 of the main engine harness connector. Touch the other multimeter lead to **all** other pins in the connector, **except** pin 26, one at a time.

Measure the resistance. The multimeter **must** show more than 100k ohms.

![[19801809.png]]

Repeat the short circuit from pin to pin check for the second return wire.

Touch one of the multimeter leads to pin 26 of the main engine harness connector. Touch the other multimeter lead to **all** other pins in the connector, **except** pin 25, one at a time.

Measure the resistance. The multimeter **must** show more than 100k ohms.

![[19802465.png]]
