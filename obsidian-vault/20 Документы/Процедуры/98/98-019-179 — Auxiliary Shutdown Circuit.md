---
type: "Процедура"
doc: "98-019-179"
title_en: "Auxiliary Shutdown Circuit"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-019-179.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-019-179.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K19"
  - "группа/98"
---

# Auxiliary Shutdown Circuit

> [!abstract] Процедура · `98-019-179`
> **Двигатели:** [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]]
> **Семейство:** K19
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-04-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-019-179.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-019-179.pdf)

### General Information

The portion of the auxiliary shutdown circuit in the main engine harness consists of the driver wire connected to pin 1 of the main engine harness connector.

To check the OEM portion of the auxiliary shutdown circuit, refer to Procedure 019-071.

> [!note] Note · Примечание
> If the driver wire is connected to the fuel shutoff solenoid, then use this section to troubleshoot fuel shutoff solenoid circuit problems.

> [!note] Note · Примечание
> Not all CENTRY™ applications will use the auxiliary shutdown circuit. Some applications will use it as torque output signal wire.

![[19801697.png]]

### Resistance Check

Disconnect the ECM connector and the C6 connector.

Select the resistance function on the multimeter.

Touch one of the multimeter leads to pin 1 of the main engine harness connector. Touch the other multimeter lead to pin F of the main engine harness side of the C6 connector.

![[19801698.png]]

Measure the resistance.

The multimeter **must** show less than 10 ohms, which is a closed circuit. If the circuit is **not** closed, then repair the main engine harness, or, if necessary, replace it. Refer to Procedure 019-228 or [[98-019-043 — Engine Wiring Harness|019-043]].

![[19801619.png]]

### Check for Short Circuit to Ground

Make sure the ECM connector and the C6 connector are disconnected.

Touch one of the multimeter leads to pin 1 of the main engine harness connector. Touch the other multimeter lead to a good, clean surface of the engine block.

![[19801700.png]]

Measure the resistance.

The multimeter **must** show more than 100k ohms, which is an open circuit. If the circuit is **not** closed, then there is a short circuit between the wire connected to pin 1 and chassis ground.

Repair the main engine harness, or, if necessary, replace it. Refer to Procedure 019-228 or [[98-019-043 — Engine Wiring Harness|019-043]].

![[19801621.png]]

### Check for Short Circuit from Pin to Pin

Make sure the C6 connector is disconnected.

Check for a short circuit between pin 1 of the main engine harness connector and **all** other pins in the connector.

Touch one of the multimeter leads to pin 1 of the main engine harness connector. Touch the other multimeter lead to **all** other pins in the connector, one at a time.

![[19801702.png]]

Measure the resistance.

The multimeter **must** show more than 100k ohms, which is an open circuit. If the circuit is **not** open, then there is a short circuit between the wires connected to pin 1 of the main engine harness and **any** other pin that measured less than 100k ohms.

Repair the main engine harness, or, if necessary, replace it. Refer to Procedure 019-228 or [[98-019-043 — Engine Wiring Harness|019-043]].

![[19801621.png]]

### Voltage Check

Make sure the C6 connector is disconnected.

Connect the ECM connector.

Turn keyswitch ON.

Select the DC voltage function on the multimeter.

Touch one of the multimeter leads to pin F of the main engine harness side of the C6 connector. Touch the other multimeter to a good, clean surface of the engine block.

![[19801704.png]]

Measure the voltage.

The multimeter **must** show the same as battery voltage (12 or 24 VDC). If the voltage is **not** correct, then inspect the wiring harness for damage. If the voltage is still low, check the battery connections for corrosion and clean them, if necessary.

![[19801705.png]]

### Check for Short Circuit to External Voltage Source

Disconnect the ECM connector.

Connect the C6 connector.

Touch one of the multimeter leads to pin 1 of the main engine harness connector. Touch the other multimeter lead to a good, clean surface on the engine block.

![[19802692.png]]

Measure the voltage.

The multimeter **must** show 1 VDC or less. If the voltage is **not** correct, then there is a short circuit between the driver wire and an external voltage source.

Remove the external voltage source.

![[19801707.png]]
