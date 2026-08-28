---
aliases:
  - "Цепь датчика положения педали или рычага подачи"
type: "Процедура"
doc: "98-019-086"
title_en: "Accelerator Pedal or Lever Position Sensor Circuit"
title_ru: "Цепь датчика положения педали или рычага подачи"
modified: "2003-04-01"
engines:
  - "37269910"
  - "37280605"
families:
  - "K19"
manuals:
  - "3666070"
figures: 30
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-019-086.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-019-086.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K19"
  - "группа/98"
---

# Accelerator Pedal or Lever Position Sensor Circuit
**Цепь датчика положения педали или рычага подачи**

> [!abstract] Процедура · `98-019-086`
> **Двигатели:** [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]]
> **Семейство:** K19
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-04-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-019-086.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-019-086.pdf)

### General Information

The portion of the throttle position sensor circuit in the engine harness consists of the +5-VDC supply wire (pin 13), the signal wire (pin 19), and the return wire, which is connected to the rail pressure sensor return wire (pin 27).

The portion of the throttle position sensor in the OEM harness consists of the +5-VDC supply wire (C6-E), the signal wire (C6-D), and the return wire (C6-B). The sensor should be checked before checking the wiring. Refer to previous section if sensor has **not** been checked yet.

![[19801665.png]]

### Resistance Check

Disconnect the ECM and C6 connectors.

![[19801643.png]]

Select the resistance function on the multimeter.

Touch one of the multimeter leads to pin 13 of the main engine harness connector. Touch the other multimeter lead to pin E of the main engine harness side of the C6 connector.

![[19801666.png]]

Measure the resistance.

The multimeter **must** show less than 10 ohms, which is a closed circuit. If the circuit is **not** closed, there is an open circuit in the +5-VDC supply wire.

Repair or replace the main engine harness. Refer to Procedure 019-228 or [[98-019-043 — Engine Wiring Harness|019-043]].

![[19801619.png]]

Repeat the above resistance check on the signal wire.

Touch one of the multimeter leads to pin 19 of the main engine harness connector. Touch the other multimeter lead to pin D of the main engine harness side of the C6 connector.

Measure the resistance. The multimeter **must** show less than 10 ohms.

![[19801668.png]]

Repeat the above resistance check on the return wire. Touch one of the multimeter leads to pin 27 of the main engine harness connector. Touch the other multimeter lead to pin B of the main engine harness side of the C6 connector.

Measure the resistance. The multimeter **must** show less than 10 ohms. If the circuit is **not** closed, check the 5-amp fuse in the rail pressure sensor return wire.

If the fuse is okay, repair or replace the main engine harness. Refer to Procedure 019-228 or [[98-019-043 — Engine Wiring Harness|019-043]].

![[19801669.png]]

Touch one of the multimeter leads to pin E on the OEM harness side of the C6 connector.

Touch the other multimeter lead to pin B of the OEM harness side of the C6 connector.

![[19801871.png]]

Measure the resistance.

The multimeter **must** show between 2000 and 3000 ohms. If the resistance does **not** fall within this range and the sensor has already been checked, then there is either an open circuit or a short circuit in the +5-VDC supply wire or the return wire.

Repair the OEM harness, or, if necessary, replace it. Refer to Procedure 019-071.

![[19801872.png]]

Touch one of the multimeter leads to pin E on the OEM harness side of the C6 connector.

Touch the other multimeter lead to pin D of the OEM harness side of the C6 connector.

![[19801873.png]]

Measure the resistance.

The multimeter **must** show between 1500 and 3000 ohms. If the resistance does **not** fall within this range, then there is an open circuit in the signal wire.

Repair the OEM harness, or, if necessary, replace it. Refer to Procedure 019-071.

![[19801874.png]]

### Check for Short Circuit to Ground

Make sure the C6 and ECM connectors are disconnected.

Touch one of the multimeter leads to pin 13 of the main engine harness connector. Touch the other multimeter lead to a good, clean surface on the engine block.

![[19801670.png]]

Measure the resistance.

The multimeter **must** show more than 100k ohms, which is an open circuit. If the circuit is **not** open, there is a short circuit between the wire connected to pin 13 and chassis ground. Repair or replace the main engine harness.

Refer to Procedure 019-228 or [[98-019-043 — Engine Wiring Harness|019-043]].

![[19801621.png]]

Repeat the above short to ground check for the signal wire.

Touch one of the multimeter leads to pin 19 of the main engine harness connector. Touch the other multimeter lead to a good, clean surface on the engine block.

Measure the resistance. The multimeter **must** show more than 100k ohms.

![[19801672.png]]

Touch one of the multimeter leads to pin E of the OEM harness side of the C6 connector. Touch the other multimeter lead to a good, clean surface on the engine block.

![[19801875.png]]

Measure the resistance.

The multimeter **must** show more than 100k ohms, which is an open circuit. If the circuit is **not** open, then there is a short circuit to ground in the +5-VDC supply wire.

Repair the OEM harness, or, if necessary, replace it. Refer to Procedure 019-071.

![[19801621.png]]

Repeat the above short circuit to ground check for the signal wire.

Touch one of the multimeter leads to pin D of the OEM harness side of the C6 connector. Touch the other multimeter lead to a good, clean surface of the engine block.

Measure the resistance. The multimeter **must** show more than 100k ohms.

![[19801876.png]]

### Check for Short Circuit from Pin to Pin

Make sure the ECM connector and the C6 and C5 connectors are disconnected.

For the check on the OEM portion of the circuit, make sure the throttle position sensor is disconnected.

Check for a short circuit between pin 13 of the main engine harness connector and **all** other pins in the connector.

Touch one of the multimeter leads to pin 13 of the connector. Touch the other multimeter lead to **all** other pins in the connector, one at a time.

![[19801674.png]]

Measure the resistance.

The multimeter **must** show more than 100k ohms, which is an open circuit. If the circuit is **not** open, there is a short between the wires connected to pin 13 of the main engine harness connector and **any** other pin that measured less than 100k ohms.

Repair or replace the main engine harness. Refer to Procedure 019-228 or [[98-019-043 — Engine Wiring Harness|019-043]].

![[19801621.png]]

Repeat the above short circuit from pin to pin check for the signal wire.

Touch one of the multimeter leads to pin 19 of the main engine harness connector. Touch the other multimeter lead to **all** other pins in the engine harness connector, one at a time.

Measure the resistance. The multimeter **must** show more than 100k ohms.

![[19801676.png]]

Repeat the above short circuit from pin to pin check for the return wire.

Touch one of the multimeter leads to pin 27 of the main engine harness connector. Touch the other multimeter lead to **all** other pins in the engine harness connector, one at a time.

Measure the resistance. The multimeter **must** show more than 100k ohms.

![[19801781.png]]

Touch one of the multimeter leads to pin E on the OEM harness connector side of the C6 connector. Touch the other multimeter lead to **all** other pins on the OEM harness side of both the C5 and C6 connectors, one at a time.

![[19801878.png]]

Measure the resistance.

The multimeter **must** show more than 100k ohms, which is an open circuit. If the circuit is **not** open, then there is a short circuit in the wiring harness between the +5-VDC supply wire and **any** wire connected to the pin that measured less than 100k ohms.

Repair the OEM harness, or, if necessary, replace it. Refer to Procedure 019-071.

![[19801621.png]]

Repeat the above short circuit from pin to pin check for the signal wire.

Touch one of the multimeter leads to pin D of the OEM harness side of the C6 connector. Touch the other multimeter to **all** other pins on the OEM harness side of both the C5 and C6 connectors, one at a time.

Measure the resistance. The multimeter **must** show more than 100k ohms.

![[19801880.png]]

Repeat the above short circuit from pin to pin check for the return wire. Touch one of the multimeter leads to pin B of the OEM harness side of the C6 connector. Touch the other multimeter to **all** other pins on the OEM harness side of both the C5 and C6 connectors.

Measure the resistance. The multimeter **must** show more than 100k ohms.

![[19801881.png]]

### Voltage Check

Make sure the ECM connector and the C5 connector are connected.

Disconnect the C6 connector.

Select the DC voltage function on the multimeter.

Turn keyswitch ON.

Touch one of the multimeter leads to pin E of the main engine harness side of the C6 connector. Touch the other multimeter lead to a good, clean surface on the engine block.

![[19801682.png]]

Measure the voltage.

The multimeter **must** show between 4.75 and 5.25 VDC. If the measured voltage does **not** fall within this range, replace the ECM. Refer to Procedure [[98-019-031 — Engine Control Module|019-031]].

![[19801683.png]]

### Check for Short Circuit to External Voltage Source

Make sure the ECM connector is disconnected.

Connect the C5 and C6 connectors.

Select the DC voltage function on the multimeter.

Turn keyswitch ON.

Touch one of the multimeter leads to pin 13 of the main engine harness connector. Touch the other multimeter lead to a good, clean surface on the engine block.

![[19801678.png]]

Measure the voltage.

The multimeter **must** show 1.0 VDC or less. If the voltage is **not** less than 1.0 VDC, then locate the external voltage source, and remove it from the throttle position +5-VDC supply wire.

![[19801679.png]]

Repeat the above short to external voltage source check for the throttle position signal wire.

Touch one of the multimeter leads to pin 19 of the main engine harness connector. Touch the other multimeter lead to a good, clean surface on the engine block.

Measure the resistance. The multimeter **must** show 1.0 VDC or less.

![[19801680.png]]

Repeat the above short to external voltage source check for the throttle position return wire.

Touch one of the multimeter leads to pin 27 of the main engine harness connector. Touch the other multimeter lead to a good, clean surface on the engine block.

Measure the resistance. The multimeter **must** show 1.0 VDC or less.

![[19801681.png]]
