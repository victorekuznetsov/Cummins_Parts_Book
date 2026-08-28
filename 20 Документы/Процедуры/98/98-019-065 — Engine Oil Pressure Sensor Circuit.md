---
type: "Процедура"
doc: "98-019-065"
title_en: "Engine Oil Pressure Sensor Circuit"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-019-065.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-019-065.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K19"
  - "группа/98"
---

# Engine Oil Pressure Sensor Circuit

> [!abstract] Процедура · `98-019-065`
> **Двигатели:** [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]]
> **Семейство:** K19
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-04-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-019-065.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-019-065.pdf)

### General Information

The portion of the sensor circuit in the main engine harness consists of the +5-VDC supply wire (pin 11), the signal wire (pin 15), and the return wire (pin 27).

The portion of the sensor circuit in the OEM harness consists of the +5-VDC supply wire (pin C5-A), the signal wire (pin C5-B), and the return wire (C5-J).

> [!note] Note · Примечание
> The circuit inside the sensor is complex. Do **not** use a multimeter to check this sensor. Disconnect the sensor connector before troubleshooting this circuit.

![[19801834.png]]

### Resistance Check

Disconnect the ECM and the C5 connectors.

![[19801643.png]]

Select the resistance function on the multimeter.

Touch one of the multimeter leads to pin 11 of the main engine harness connector. Touch the other multimeter lead to pin A of the main engine harness side of the C5 connector.

![[19801644.png]]

Measure the resistance.

The multimeter **must** show less than 10 ohms, which is a closed circuit. If the circuit is **not** closed, there is an open circuit in the +5-VDC supply wire.

Repair or replace the main engine harness. Refer to Procedure 019-228 or [[98-019-043 — Engine Wiring Harness|019-043]].

![[19801619.png]]

Repeat the above resistance check for the signal wire.

Touch one of the multimeter leads to pin 15 of the main engine harness connector. Touch the other multimeter lead to pin B of the C5 connector.

Measure the resistance. The multimeter **must** show less than 10 ohms.

![[19801646.png]]

Repeat the above resistance check for the return wire.

Touch one of the multimeter leads to pin 27 of the main engine harness connector. Touch the other multimeter lead to pin J of the main engine harness side of the C5 connector.

![[19801647.png]]

Measure the resistance. If the multimeter does **not** measure less than 10 ohms, check the 5-amp fuse in the rail pressure return wire for a blown fuse.

If the fuse is okay, repair or replace the main engine harness. Refer to Procedure 019-228 or [[98-019-043 — Engine Wiring Harness|019-043]].

![[19801648.png]]

### Check for Short Circuit to Ground

Make sure the C5 connector and the rail pressure sensor are disconnected.

Touch one of the multimeter leads to pin 11 of the main engine harness connector. Touch the other multimeter lead to engine block ground.

![[19801649.png]]

Measure the resistance.

The multimeter **must** show more than 100k ohms, which is an open circuit. If the circuit is **not** open, then there is a short circuit between the wire connected to pin 11 and chassis ground.

Repair or replace the main engine harness. Refer to Procedure 019-228 or [[98-019-043 — Engine Wiring Harness|019-043]].

![[19801621.png]]

Repeat the above short circuit to ground check for the signal wire.

Touch one of the multimeter leads to pin 15 of the main engine harness connector. Touch the other multimeter lead to engine block ground.

Measure the resistance. The multimeter **must** show more than 100k ohms.

![[19801651.png]]

### Check for Short Circuit from Pin to Pin

Make sure the C5 connector and rail pressure sensor are disconnected.

Check for a short circuit between pin 11 of the main engine harness connector and **all** other pins in the main engine harness connector.

Touch one of the multimeter leads to pin 11 of the connector. Touch the other multimeter lead to **all** other pins in the connector, one at a time.

![[19801652.png]]

Measure the resistance.

The multimeter **must** show more than 100k ohms, which is an open circuit. If the circuit is **not** open, then there is a short between the wires connected to pin 11 of the main engine harness connector and **any** other pin that measured less than 100k ohms.

Repair or replace the main engine harness. Refer to Procedure 019-228 or [[98-019-043 — Engine Wiring Harness|019-043]].

![[19801621.png]]

Repeat the above short circuit from pin to pin check for the signal wire.

Touch one of the multimeter leads to pin 15 of the main engine harness connector. Touch the other multimeter lead to **all** other pins in the connector, one at time.

Measure the resistance.

The multimeter **must** show more than 100k ohms.

![[19801654.png]]

Repeat the above short circuit from pin to pin check for the return wire.

Touch one of the multimeter leads to pin 27 of the main engine harness connector. Touch the other multimeter lead to **all** other pins in the connector, one at a time.

Measure the resistance.

The multimeter **must** show more than 100k ohms.

![[19801655.png]]

### Voltage Check

Connect the C5 and C6 connectors.

Disconnect the rail pressure sensor.

Install breakout cable, Part No. 3824775, between the rail pressure sensor and the main engine harness.

Select the DC voltage function on the multimeter.

Turn keyswitch ON.

![[19802632.png]]

Measure the supply voltage by installing the breakout cable, Part No. 3824775, supply (pin A) and return (pin B) leads into the multimeter.

![[19802633.png]]

The multimeter **must** show between 4.75 and 5.25 VDC. If the voltage is **not** within this range and the +5-VDC supply wire and return wire have checked out okay, check the ECM power circuit and ground circuit for problems. Refer to Procedure 019-008.

If the power circuits check out, then the ECM has failed. Replace the ECM. Refer to Procedure [[98-019-031 — Engine Control Module|019-031]].

![[19801848.png]]

Measure the signal voltage by installing the breakout cable, Part No. 3824775, signal (pin C) and return (pin B) leads into the multimeter.

The multimeter will show a different voltage range at various pressure readings. Refer to the table below.

![[19802634.png]]

| Pressure | Acceptable Voltage Range |  |
|---|---|---|
| **(kPa)** | **(psi)** | **(VDC)** |
| 0 | 0 | 0.42 to 0.54 |
| 344.74 | 50 | 1.26 to 1.34 |
| 689.48 | 100 | 2.06 to 2.14 |
| 1034.22 | 150 | 2.85 to 2.95 |
| 1389.96 | 200 | 3.63 to 3.77 |
| 1723.70 | 250 | 4.39 to 4.62 |

![[nobox.png]]
