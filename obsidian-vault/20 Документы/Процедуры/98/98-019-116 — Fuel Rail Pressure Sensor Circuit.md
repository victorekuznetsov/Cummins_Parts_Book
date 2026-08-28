---
type: "Процедура"
doc: "98-019-116"
title_en: "Fuel Rail Pressure Sensor Circuit"
modified: "2003-04-01"
engines:
  - "37269910"
  - "37280605"
families:
  - "K19"
manuals:
  - "3666070"
figures: 19
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-019-116.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-019-116.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K19"
  - "группа/98"
---

# Fuel Rail Pressure Sensor Circuit

> [!abstract] Процедура · `98-019-116`
> **Двигатели:** [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]]
> **Семейство:** K19
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-04-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-019-116.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-019-116.pdf)

### Inspect

The sensor circuit consists of the wires connected to pin 11 (+5-VDC supply wire), pin 14 (signal wire), and pin 27 (return wire) of the main engine harness connector.

Disconnect the main engine harness connector. Flush and clean the connector pins using contact cleaner, Part No. 3824510. Inspect the connector for damaged pins.

Make sure the sensor is disconnected from the main engine harness.

![[19801766.png]]

### Resistance Check

> [!warning] CAUTION · Осторожно
> Do not force the multimeter probe into the connector sockets. Contact with the socket is enough to get a reading.

Disconnect the ECM connector and the sensor connector.

Select the resistance function on the multimeter.

Touch one of the multimeter leads to pin 11 of the main engine harness connector. Touch the other multimeter lead to pin A of the harness side of the sensor connector.

![[19801767.png]]

Measure the resistance.

The multimeter **must** show less than 10 ohms, which is a closed circuit. If the circuit is **not** closed, repair or replace the main engine harness. Refer to Procedure 019-228 or [[98-019-043 — Engine Wiring Harness|019-043]].

![[19801619.png]]

Touch one of the multimeter leads to pin 14 of the main engine harness connector. Touch the other multimeter lead to pin C of the main engine harness side of the rail pressure sensor connector.

![[19801769.png]]

Measure the resistance.

The multimeter **must** show less than 10 ohms, which is a closed circuit. If the circuit is **not** closed, repair or replace the main engine harness. Refer to Procedure 019-228 or [[98-019-043 — Engine Wiring Harness|019-043]].

![[19801619.png]]

Touch one of the multimeter leads to pin 27 of the main engine harness connector. Touch the other multimeter lead to pin B of the main engine harness side of the sensor connector.

![[19801771.png]]

Measure the resistance.

The multimeter **must** show less than 10 ohms, which is a closed circuit. If the circuit is **not** closed, check the 5 amp fuse in the return wire for a blown fuse. Refer to Procedure 019-198.

If the fuse is okay, then repair or replace the main engine harness. Refer to Procedure 019-228 or [[98-019-043 — Engine Wiring Harness|019-043]].

![[19801619.png]]

### Check for Short Circuit to Ground

Make sure the ECM connector and sensor connector are disconnected.

Touch one of the multimeter leads to pin 11 of the main engine harness connector. Touch the other multimeter lead to a good, clean surface on the engine block.

![[19801773.png]]

Measure the resistance.

The multimeter **must** show more than 100k ohms, which is an open circuit. If the circuit is **not** open, then there is a short circuit between the wire connected to pin 11 and chassis ground.

Repair or replace the main engine harness. Refer to Procedure 019-228 or [[98-019-043 — Engine Wiring Harness|019-043]].

![[19801621.png]]

Touch one of the multimeter leads to pin 14 of the main engine harness connector. Touch the other multimeter lead to a good, clean surface on the engine block.

![[19801775.png]]

Measure the resistance.

The multimeter **must** show more than 100k ohms, which is an open circuit. If the circuit is **not** open, then there is a short circuit between the wire connected to pin 14 and chassis ground.

Repair or replace the main engine harness. Refer to Procedure 019-228 or [[98-019-043 — Engine Wiring Harness|019-043]].

![[19801621.png]]

### Check for Short Circuit from Pin to Pin

Make sure the sensor, C6, and ECM connectors are disconnected.

Check for a short circuit between pin 11 of the main engine harness connector and **all** other pins in the connector.

Touch one of the multimeter leads to pin 11 of the connector. Touch the other multimeter lead to **all** other pins in the connector, one at a time.

![[19801777.png]]

Measure the resistance.

The multimeter **must** show more than 100k ohms, which is an open circuit. If the circuit is **not** open, then there is a short between the wires connected to pin 11 of the main engine harness connector and **any** other pin that measured less than 100k ohms. Repair or replace the main engine harness. Refer to Procedure 019-228 or [[98-019-043 — Engine Wiring Harness|019-043]].

![[19801621.png]]

Check for a short circuit between pin 14 of the main engine harness connector and **all** other pins in the connector.

Touch one of the multimeter leads to pin 14 of the connector. Touch the other multimeter lead to **all** other pins in the connector, one at a time.

![[19801779.png]]

Measure the resistance.

The multimeter **must** show more than 100k ohms, which is an open circuit. If the circuit is **not** open, then there is a short between the wires connected to pin 14 of the main engine harness connector and **any** other pin that measured less than 100k ohms.

Repair or replace the main engine harness. Refer to Procedure 019-228 or [[98-019-043 — Engine Wiring Harness|019-043]].

![[19801621.png]]

Check for a short circuit between pin 27 of the main engine harness connector and **all** other pins in the connector.

Touch one of the multimeter leads to pin 27 of the connector. Touch the other multimeter lead to **all** other pins in the connector, one at a time.

![[19801781.png]]

Measure the resistance.

The multimeter **must** show more than 100k ohms, which is an open circuit. If the circuit is **not** open, then there is a short between the wires connected to pin 27 of the main engine harness connector and **any** other pin that measured less than 100k ohms.

Repair or replace the main engine harness. Refer to Procedure 019-228 or [[98-019-043 — Engine Wiring Harness|019-043]].

![[19801621.png]]

### Voltage Check

Connect the ECM and C5 connectors.

Install breakout cable, Part No. 3824774, between the rail pressure sensor and the main engine harness.

![[19801783.png]]

Select the DC voltage function on the multimeter. Touch the positive (+) multimeter lead to pin A of the breakout cable. Touch the other multimeter lead to pin C of the breakout cable.

Measure the resistance. The multimeter **must** show between 4.75 and 5.25 VDC. If the measured voltage does **not** fall within this range and the sensor circuit has been checked and is okay, then the ECM has failed. Replace the ECM. Refer to Procedure [[98-019-031 — Engine Control Module|019-031]].

> [!note] Note · Примечание
> To avoid damaging the new ECM, **all** other active fault codes **must** be investigated prior to replacing the ECM.

![[19802691.png]]
