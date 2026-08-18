---
aliases:
  - "Цепь датчика положения педали или рычага подачи"
type: "Процедура"
doc: "87-019-086"
title_en: "Accelerator Pedal or Lever Position Sensor Circuit"
title_ru: "Цепь датчика положения педали или рычага подачи"
modified: "2018-08-09"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666214"
figures: 20
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-019-086.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-019-086.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
---

# Accelerator Pedal or Lever Position Sensor Circuit
**Цепь датчика положения педали или рычага подачи**

> [!abstract] Процедура · `87-019-086`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2018-08-09
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-019-086.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-019-086.pdf)

### Initial Check

> [!warning] CAUTION · Осторожно
> Do not use probes or test leads other than Part Number 3822758. The connector will be damaged. The leads must fit tightly in the connector without expanding the pins in the connector.

If INSITE™ is available, monitor the accelerator position sensor circuit for proper operation. If **not**, follow the troubleshooting procedures in this section.

![[19900524.png]]

### Resistance Check

> [!warning] CAUTION · Осторожно
> Do not use probes or test leads other than Part Number 3822758. The connector will be damaged. The leads must fit tightly in the connector without expanding the pins in the connector.

Disconnect the OEM interface harness connector from the ECM. Make sure the sensor is connected to the OEM harness.

Insert one of the leads into pin 29 (+5-VDC supply) of the OEM interface harness connector. Insert the other test lead into pin 19 (return) of the connector.

![[19900638.png]]

Connect the alligator clips to the multimeter leads. Measure the resistance. The multimeter **must** show 2000 to 3000 ohms when the accelerator pedal is up or down. If the resistance is **not** within the specification, there is a problem with wire 19 or wire 29 in the OEM interface harness, provided the accelerator position sensor has been previously checked. Repair the OEM interface harness. [[99-019-199 — Connector, Butt Splice|Refer to Procedure 019-199]]. Repair the OEM harness according to the vehicle manufacturer's instructions.

![[19900639.png]]

Remove the lead from pin 19 (return) of the OEM interface harness connector and insert it into pin 30 (signal) of the connector.

Make sure the foot pedal is in the released (idle) position.

Measure the resistance. The multimeter **must** show 1500 to 3000 ohms.

![[19a00717.png]]

Depress the foot pedal (full fuel) and measure the resistance again. The multimeter **must** show 200 to 1500 ohms. This resistance value **must** be at least 1000 ohms lower than the resistance value of the throttle-released (low-idle) position, measured in the above check. If the resistance values are **not** within the specification, there is a problem with wire 29 (+5-VDC supply) or wire 30 (signal) in the OEM harness. Repair the OEM interface harness. If the resistance values in the two previous checks are within the specification, wires 19, 29, and 30 **must** still be checked for a short circuit to ground, a short circuit from pin to pin, and a short circuit to battery supply.

> [!note] Note · Примечание
> When checking the OEM harness, examine the bulkhead connector and other connectors in the circuit for corrosion or damage to the accelerator position sensor wire terminals.

![[19900641.png]]

### Check for Short Circuit to Ground

> [!warning] CAUTION · Осторожно
> Do not use probes or test leads other than Part Number 3822758. The connector will be damaged. The leads must fit tightly in the connector without expanding the pins of the connector.

Disconnect the OEM interface harness connector from the ECM. Disconnect the accelerator position sensor from the OEM harness at the foot pedal assembly.

![[tl8swkb.png]]

Insert the test lead into pin 29 (+5-VDC supply) of the OEM interface harness connector. Connect the alligator clip to the multimeter positive (+) probe. Touch the multimeter negative (-) probe to the engine block and measure the resistance.

The multimeter **must** show an open circuit (100k ohms or more).

![[19900642.png]]

Remove the lead from pin 29 of the OEM interface harness connector and insert it into pin 19 (return) of the connector. Touch the multimeter negative (-) probe to the engine block and measure the resistance.

The multimeter **must** show an open circuit (100k ohms or more).

![[19900643.png]]

Remove the lead from pin 19 of the OEM interface harness connector and insert it into pin 30 (signal) of the connector. Touch the multimeter negative (-) probe to the engine block and measure the resistance. The multimeter **must** show an open circuit (100k ohms or more).

If **any** of these three resistance measurements are **not** open, there is a short circuit to ground between the wire connected to pin 29, 19, or 30. Repair the OEM interface harness. [[87-019-250 — Connector, 50-Pin|Refer to Procedure 019-250]]. Repair the OEM harness according to the vehicle manufacturer's instructions.

Connect the accelerator position sensor after completing the repair.

![[19900644.png]]

### Check for Short Circuit from Pin-to-Pin

> [!warning] CAUTION · Осторожно
> Do not use probes or test leads other than Part Number 3822758. The connector will be damaged. The leads must fit tightly in the connector without expanding the pins of the connector.

Disconnect the accelerator position sensor from the OEM harness at the foot pedal assembly. Disconnect the engine harness connector and OEM interface harness connector from the ECM.

![[tl8swkb.png]]

Insert the test lead into pin 29 (+5-VDC supply) of the OEM interface harness connector. Insert the other lead into pin 1 of the connector. Connect the clips to the multimeter probes and measure the resistance.

The multimeter **must** show an open circuit (100k ohms or more).

![[19900645.png]]

Remove the lead from pin 1 and test all other pins of the connector.

Then, repeat the pin-to-pin check from pin 29 of the OEM interface harness connector to all pins of the engine harness connector.

The multimeter **must** show an open circuit (100k ohms or more) at all pins.

If the multimeter shows a closed circuit at any pin, there is a short circuit between wire 29 and any other wire that measured a closed circuit. Repair the OEM interface harness. [[87-019-250 — Connector, 50-Pin|Refer to Procedure 019-250]]. Repair the OEM harness according to the vehicle manufacturer's instructions.

![[19a00718.png]]

Remove the lead from pin 29 of the OEM interface harness connector and insert it into pin 19 (return). Insert the other lead into pin 1 and measure the resistance.

The multimeter **must** show an open circuit (100k ohms or more).

![[19900647.png]]

Remove the lead from pin 1 and test all other pins of the connector.

Then, repeat the pin-to-pin check from pin 19 of the OEM interface harness connector to all pins of the engine harness connector.

The multimeter **must** show an open circuit (100k ohms or more) at all pins.

If the multimeter shows a closed circuit at any pin, there is a short circuit between wire 19 and any other wire that measured a closed circuit. Repair the OEM interface harness. [[87-019-250 — Connector, 50-Pin|Refer to Procedure 019-250]]. Repair the OEM harness according to the vehicle manufacturer's instructions.

![[19a00719.png]]

Remove the lead from pin 19 of the OEM interface harness connector and insert it into pin 30 (signal). Insert the other lead into pin 1 and measure the resistance.

The multimeter **must** show an open circuit (100k ohms or more).

![[19900649.png]]

Remove the lead from pin 1 and test all other pins of the connector.

Then, repeat the pin-to-pin check from pin 30 of the OEM interface harness connector to all pins of the engine harness connector.

The multimeter **must** show an open circuit (100k ohms or more) at all pins.

If the multimeter shows a closed circuit at any pin, there is a short circuit between wire 30 and any other wire that measured a closed circuit. Repair the OEM interface harness. [[87-019-250 — Connector, 50-Pin|Refer to Procedure 019-250]]. Repair the OEM harness according to the vehicle manufacturer's instructions.

Connect the accelerator position sensor after completing the repair.

![[19a00720.png]]

### Check for Short Circuit to External Voltage Source

> [!warning] CAUTION · Осторожно
> Do not use probes or test leads other than Part Number 3822758. The connector will be damaged. The leads must fit tightly in the connector without expanding the pins of the connector.

> [!note] Note · Примечание
> An external voltage source is **any** wire in the harness that carries voltage.

Disconnect the OEM interface harness connector from the ECM. Disconnect the accelerator position sensor from the OEM harness at the foot pedal assembly.

![[tl8swkb.png]]

Turn the vehicle keyswitch to the ON position. Turn the multimeter dial to measure VDC. Insert one of the leads into pin 29 (+5-VDC supply) of the OEM interface harness connector. Connect the clip to the multimeter positive (+) probe. Touch the multimeter negative (-) probe to the engine block and measure the voltage.

The voltage **must** be 1.5 VDC or less.

![[19900651.png]]

Remove the lead from pin 29 of the OEM interface harness connector and insert it into pin 19 (return) of the connector. Touch the multimeter negative (-) probe to the engine block and measure the voltage.

The voltage **must** be 1.5 VDC or less.

![[19900652.png]]

Remove the lead from pin 19 of the OEM interface harness connector and insert it into pin 30 (signal) of the connector. Touch the multimeter negative (-) probe to the engine block and measure the voltage.

The voltage **must** be 1.5 VDC or less.

If more than 1.5 VDC is measured at any pin, there is a short circuit from wire 19, 29, or 30 to a wire carrying power. Repair the OEM interface harness. [[87-019-250 — Connector, 50-Pin|Refer to Procedure 019-250]]. Repair the OEM harness according to the vehicle manufacturer's instructions. Connect the accelerator position sensor after completing the repair.

![[19900653.png]]
