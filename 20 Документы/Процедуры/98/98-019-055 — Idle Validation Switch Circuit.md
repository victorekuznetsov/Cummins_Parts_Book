---
aliases:
  - "Цепь выключателя подтверждения холостого хода"
type: "Процедура"
doc: "98-019-055"
title_en: "Idle Validation Switch Circuit"
title_ru: "Цепь выключателя подтверждения холостого хода"
modified: "2003-04-01"
engines:
  - "37269910"
  - "37280605"
families:
  - "K19"
manuals:
  - "3666070"
figures: 29
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-019-055.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-019-055.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K19"
  - "группа/98"
---

# Idle Validation Switch Circuit
**Цепь выключателя подтверждения холостого хода**

> [!abstract] Процедура · `98-019-055`
> **Двигатели:** [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]]
> **Семейство:** K19
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-04-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-019-055.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-019-055.pdf)

### General Information

The portion of this circuit in the main engine harness consists of the off-idle signal wire (pin 9), the on-idle signal wire (pin 16), and the return wire (pins 25 and 26). The portion of this circuit in the OEM harness consists of the off-idle signal wire (pin C6-A), the on-idle signal wire (pin C6-C), and the return wire (pin C6-G).

![[19801684.png]]

### Resistance Check

Make sure the idle validation switch connector is connected. Disconnect the ECM and the C6 connectors.

Select the resistance function on the multimeter.

Touch one of the multimeter leads to pin C of the OEM harness side of the C6 connector. Touch the other multimeter lead to pin G of the OEM harness side of the C6 connector.

Leave the throttle pedal in the released (idle) position.

![[19801891.png]]

Measure the resistance.

The multimeter **must** show less than 10 ohms, which is a closed circuit. If the circuit is **not** closed, then there is an open circuit in either the return wire or the idle signal wire, provided the switch has already been checked and is okay.

![[19801619.png]]

Touch one of the multimeter leads to pin C of the OEM harness side of the C6 connector. Touch the other multimeter lead to pin G of the OEM harness side of the C6 connector.

Depress the throttle pedal.

![[19802629.png]]

Measure the resistance.

The multimeter **must** show more than 100k ohms, which is an open circuit. If the circuit is **not** open, repair or replace the OEM harness. Refer to the OEM troubleshooting and repair manual.

![[19801621.png]]

Touch one of the multimeter leads to pin A of the OEM harness side of the C6 connector. Touch the other multimeter lead to pin G of the OEM harness side of the C6 connector.

Depress the throttle pedal.

![[19801893.png]]

Measure the resistance.

The multimeter **must** show less than 10 ohms, which is a closed circuit. If it is more than 10 ohms, repair the OEM harness, or if necessary, replace it. Refer to the OEM troubleshooting and repair manual.

![[19801619.png]]

Touch one of the multimeter leads to pin A of the OEM harness side of the C6 connector. Touch the other multimeter lead to pin G of the OEM harness side of the C6 connector.

Release the throttle pedal.

![[19802630.png]]

Measure the resistance.

The multimeter **must** show more than 100k ohms, which is an open circuit. If the circuit is **not** open, repair the OEM harness, or if necessary, replace it. Refer to the OEM troubleshooting and repair manual.

![[19801621.png]]

Touch one of the multimeter leads to pin 9 of the main engine harness connector. Touch the other multimeter lead to pin A of the main engine harness side of the C6 connector.

![[19801686.png]]

Measure the resistance.

The multimeter **must** show less than 10 ohms, which is a closed circuit. If the circuit is **not** closed, then there is an open circuit in the off-idle signal wire.

Repair the main engine harness, or if necessary, replace it. Refer to Procedure 019-228 or [[98-019-043 — Engine Wiring Harness|019-043]].

![[19801619.png]]

Repeat the above resistance check for the idle validation signal wire.

Touch one of the multimeter leads to pin 16 of the main engine harness connector. Touch the other multimeter lead to pin C on the main engine harness side of the C6 connector.

Measure the resistance. The multimeter **must** show less than 10 ohms.

![[19801688.png]]

Repeat the above resistance check for the on-idle return wire.

Touch one of the multimeter leads to pin 25 or 26 of the main engine harness connector. Touch the other multimeter lead to pin G on the main engine harness side of the C6 connector.

Measure the resistance. The multimeter **must** show less than 10 ohms.

![[19802631.png]]

### Check for Short Circuit to Ground

Make sure the switch connector is connected.

Touch one of the multimeter leads to pin A on the OEM harness side of the C6 connector. Touch the other multimeter lead to a good, clean surface on the engine block.

![[19801895.png]]

Measure the resistance.

The multimeter **must** show more than 100k ohms, which is an open circuit. If the circuit is **not** open, then there is a short circuit between the off-idle signal wire and chassis ground.

Repair the OEM harness, or, if necessary, replace it. Refer to the OEM troubleshooting and repair manual for the procedure.

![[19801621.png]]

Touch one of the multimeter leads to pin G on the main engine harness side of the C6 connector. Touch the other multimeter lead to a good, clean surface on the engine block.

Measure the resistance. The multimeter **must** show less than 10 ohms.

![[19801689.png]]

Repeat the above short circuit to ground check for the idle signal wire.

Touch one of the multimeter leads to pin C of the OEM harness side of the C6 connector. Touch the other multimeter lead to a good, clean surface on the engine block.

Measure the resistance. The multimeter **must** show more than 100k ohms.

![[19801897.png]]

### Check for Short Circuit from Pin to Pin

Make sure the C5 and C6 connectors and the idle validation switch are disconnected. Make sure the throttle pedal is in the released (idle) position.

Touch one of the multimeter leads to pin A of the OEM harness side of the C6 connector. Touch the other multimeter lead to **all** other pins on the OEM harness side of both the C5 and C6 connectors, one at a time.

![[19801899.png]]

Measure the resistance.

The multimeter **must** show more than 100k ohms, which is an open circuit. If the circuit is **not** open, then there is a short circuit between the wires connected to pin A and **any** other pins that measured less than 100k ohms.

Repair the OEM harness, or, if necessary, replace it. Refer to the OEM troubleshooting and repair manual for the procedure.

![[19801621.png]]

Repeat the above short circuit from pin to pin check for the on-idle signal wire.

Touch one of the multimeter leads to pin C of the OEM harness side of the C6 connector. Touch the other multimeter lead to **all** other pins on the OEM harness side of both the C5 and C6 connectors, one at a time.

Measure the resistance. The multimeter **must** show more than 100k ohms.

![[19801901.png]]

Repeat the above short circuit from pin to pin check for the return wire.

Touch one of the multimeter leads to pin G of the OEM harness side of the C6 connector. Touch the other multimeter lead to **all** other pins on the OEM harness side of both the C5 and C6 connectors, one at a time.

Measure the resistance. The multimeter **must** show more than 100k ohms.

![[19801902.png]]

Check for a short circuit between pin 9 of the main engine harness connector and **all** other pins in the connector.

Touch one of the multimeter leads to pin 9 of the connector. Touch the other multimeter lead to **all** other pins in the connector, one at a time.

![[19801690.png]]

Measure the resistance.

The multimeter **must** show more than 100k ohms, which is an open circuit. If the circuit is **not** open, then there is a short between the wires connected to pin 9 of the main engine harness connector and **any** other pin that measured less than 100k ohms.

Repair or replace the main engine harness. Refer to Procedure 019-228 or [[98-019-043 — Engine Wiring Harness|019-043]].

![[19801621.png]]

Repeat the above short circuit from pin to pin for the on-idle signal wire.

Touch one of the multimeter leads to pin 16 of the main engine harness connector. Touch the other multimeter lead to **all** other pins in the connector, one at a time.

Measure the resistance. The multimeter **must** show more than 100k ohms.

![[19801692.png]]

Repeat the above short circuit from pin to pin for the idle validation return wire.

Touch one of the multimeter leads to pin 25 of the main engine harness connector. Touch the other multimeter lead to **all** other pins in the connector, one at a time, **except** pin 26.

Measure the resistance. The multimeter **must** show more than 100k ohms.

![[19801693.png]]

### Check for Short Circuit to External Voltage Source

Connect the ECM connector. Make sure the C6 connector is disconnected.

Turn keyswitch ON.

Select the DC voltage function on the multimeter.

Touch one of the multimeter leads to pin A of the OEM harness side of the C6 connector. Touch the other multimeter lead to the engine block ground.

![[19801903.png]]

Measure the voltage.

The multimeter **must** show less than 1 VDC. If the voltage is **not** less than 1 VDC, there is a short to an external voltage source in the off-idle signal wire.

Repair or replace the OEM harness. Refer to the OEM troubleshooting and repair manual for the procedure.

![[19801904.png]]

Repeat the above short circuit to external voltage source check for the idle signal wire.

Touch one of the multimeter leads to pin C of the OEM harness side of the C6 connector. Touch the other multimeter lead to engine block ground.

Measure the resistance The multimeter **must** show less than 1 VDC.

![[19801905.png]]

Repeat the above short circuit to external voltage source check for the return wire.

Touch one of the multimeter leads to pin G of the OEM harness side of the C6 connector. Touch the other multimeter lead to engine block ground.

Measure the resistance. The multimeter **must** show less than 1 VDC.

![[19801906.png]]
