---
aliases:
  - "Цепь датчика положения педали или рычага подачи"
type: "Процедура"
doc: "82-019-086"
title_en: "Accelerator Pedal or Lever Position Sensor Circuit"
title_ru: "Цепь датчика положения педали или рычага подачи"
modified: "2002-06-03"
engines:
  - "41343322"
  - "41370103"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 21
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-086.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-019-086.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# Accelerator Pedal or Lever Position Sensor Circuit
**Цепь датчика положения педали или рычага подачи**

> [!abstract] Процедура · `82-019-086`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section 19 - Electronic Engine Controls
> **Даты:** изменён 2002-06-03
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-086.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-019-086.pdf)

### Initial Check

> [!warning] CAUTION · Осторожно
> Do not use probes or leads other than Part No. 3822758. The OEM connector will be damaged. The leads must fit tightly in the connector without expanding the connector pins.

If INSITE™ is available, monitor the accelerator position sensor circuit for proper operation. If **not**, follow the troubleshooting procedures in this section. Disconnect the OEM harness connector from the ECM. Make sure the accelerator position sensor is connected to the OEM harness.

![[19c00691.png]]

### Resistance Check

Insert a test lead into pin 48 (accelerator position (+) 5-VDC supply) of the OEM harness connector. Insert the other lead into pin 49 (return) of the connector.

Connect the test leads to the multimeter probes. With the accelerator pedal depressed, measure the resistance. The multimeter **must** show 2000 to 3000 ohms when the accelerator pedal is down (or up). If the resistance is **not** within the specification, there is a problem with wire 48 or wire 49 in the OEM harness, provided the accelerator position sensor has been previously checked. Repair the OEM harness according to the manufacturer's procedures.

![[19200229.png]]

Repeat the check with the accelerator pedal in the released position. Measure the resistance. The multimeter **must** show 2000 to 3000 ohms when the accelerator pedal is up (or down). If the resistance is **not** within the specification, there is a problem with wire 48 or wire 49 in the OEM harness, provided the accelerator position sensor has been previously checked.

Repair the OEM harness according to the manufacturer's procedures.

![[19200230.png]]

Remove the test lead from pin 49 (accelerator position return) and insert it into pin 47 (accelerator position signal).

Make sure the foot pedal is in the released (idle) position.

Measure the resistance. The multimeter **must** show 1500 to 3000 ohms.

![[19c00889.png]]

Depress the foot pedal (full-fuel) and measure the resistance again.

The multimeter **must** show 200 to 1500 ohms. This resistance value **must** be at least 1000 ohms lower than the resistance value of 1500 to 3000 ohms measured in the above check. If the resistance values are **not** within the specification, there is a problem with wire 48 (accelerator position (+) 5-VDC supply) or wire 47 (accelerator position signal) in the OEM harness.

![[19200232.png]]

Repair the OEM harness according to the manufacturer's procedures. If the resistance values in the two previous checks are within the specification, wire 48, 49, and 47 **must** still be checked for a short circuit to ground, a short circuit from pin to pin, and a short circuit to battery supply.

> [!note] Note · Примечание
> When checking the OEM harness, inspect the bulkhead connector and other connectors in the circuit for corrosion or damage to the accelerator position sensor wire terminals.

![[19200232.png]]

### Check for Short Circuit to Ground

Disconnect the accelerator position sensor from the OEM harness at the foot pedal assembly.

![[tl8swkb.png]]

Insert a test lead into pin 48 (+5-VDC supply) of the OEM harness connector, and connect it to the multimeter (+) positive probe. Touch the multimeter (-) negative probe to the engine block and measure the resistance.

The multimeter **must** show an open circuit (100k ohms or more).

![[19200233.png]]

Remove the lead from pin 48 and insert it into pin 49 (return ground). Touch the multimeter (-) negative probe to the engine block ground and measure the resistance.

The multimeter **must** show an open circuit (100k ohms or more).

![[19200234.png]]

Remove the lead from pin 49 and insert it into pin 47 (signal return). Touch the multimeter (-) negative probe to the engine block ground and measure the resistance. The multimeter **must** show an open circuit (100k ohms or more).

If **any** of these three resistance measurements are **not** open, there is a short circuit to ground between the wires connected to pins 48, 49, and/or 47. Repair the OEM harness according to the vehicle manufacturer's procedures.

![[19200235.png]]

### Check for Short Circuit from Pin to Pin

Disconnect the accelerator position sensor from the OEM harness at the foot pedal assembly.

![[tl8swkb.png]]

Insert a test lead into pin 48 (+5-VDC supply) of the OEM harness connector. Insert the other lead into pin 6 of the connector. Connect the leads to the multimeter probes and measure the resistance.

The multimeter **must** show an open circuit (100k ohms or more).

![[19200236.png]]

Test all pins. Remove the lead from pin 6, and measure the resistance from pin 48 to all other pins in the connector, one at a time.

The multimeter **must** show an open circuit (100k ohms or more) at all pins.

If the multimeter shows a closed circuit at any pin, there is a short circuit between wire No. 48 and any other wire that measured a closed circuit.

Repair the OEM harness according to the vehicle manufacturer's procedures.

![[19200237.png]]

Remove the lead from pin 48 and insert it into pin 49 (return ground). Insert the other lead into pin 6 and measure the resistance.

The multimeter **must** show an open circuit (100k ohms or more).

![[19200238.png]]

Remove the lead from pin 6 and test all pins. Measure the resistance from pin 49 to all other pins in the connector, one at a time.

The multimeter **must** show an open circuit (100k ohms or more) at all pins.

![[19200239.png]]

Remove the lead from pin 49 and insert it into pin 47 (signal return). Insert the other lead into pin 1 and measure the resistance.

The multimeter **must** show an open circuit (100k ohms or more).

![[19200240.png]]

Remove the lead from pin 1 and test all pins.

The multimeter **must** show an open circuit (100k ohms or more) in all pins.

If the multimeter showed a closed circuit at any pin, there is a short circuit between wire No. 47 and any other wire that measured a closed circuit. Repair the OEM harness according to the vehicle manufacturer's procedures.

![[19200241.png]]

### Check for Short Circuit to External Voltage Source

Disconnect the accelerator position sensor from the OEM harness at the foot pedal assembly.

![[tl8swkb.png]]

Turn the vehicle keyswitch to the ON position. Set the multimeter to measure VDC. Insert a test lead into pin 48 (+5-VDC supply). Connect it to the multimeter (+) positive probe. Touch the multimeter (−) negative probe to the engine block ground and measure the voltage.

The voltage **must** be 1.5 VDC or less.

![[19200242.png]]

Remove the lead from pin 48 and insert it into pin 49 (return ground). Touch the multimeter (−) negative probe to the engine block ground and measure the voltage.

The voltage **must** be 1.5 VDC or less.

![[19200243.png]]

Remove the lead from pin 49 and insert it into pin 47 (signal return). Touch the multimeter (−) negative probe to the engine block ground and measure the voltage.

The voltage **must** be 1.5 VDC or less.

If more than 1.5 VDC is measured at any pin, there is a short circuit from wire No. 48, 49, or 47 to an external voltage source. Repair the OEM harness according to the vehicle manufacturer's procedures.

> [!note] Note · Примечание
> An external voltage source is any wire in the OEM harness that carries voltage.

Connect all components after completing the repair.

![[19200244.png]]
