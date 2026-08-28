---
aliases:
  - "Цепь датчика положения педали или рычага подачи"
type: "Процедура"
doc: "19-019-086"
title_en: "Accelerator Pedal or Lever Position Sensor Circuit"
title_ru: "Цепь датчика положения педали или рычага подачи"
modified: "2002-08-20"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
  - "85017333"
families:
  - "QSK23"
  - "QSK60"
manuals:
  - "3666113"
figures: 23
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-019-086.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-019-086.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
---

# Accelerator Pedal or Lever Position Sensor Circuit
**Цепь датчика положения педали или рычага подачи**

> [!abstract] Процедура · `19-019-086`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2002-08-20
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-019-086.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-019-086.pdf)

### Initial Check

> [!warning] CAUTION · Осторожно
> To reduce the possibility of connector damage, do not use probes or leads other than Part Number 3822758. The connector will be damaged. The leads must fit tightly in the connector without expanding the pins in the connector.

If INSITE™, Part Number 3824801, is available, monitor the accelerator position sensor circuit for proper operation. If **not**, follow the troubleshooting procedures in this section.

![[19400357.png]]

### Resistance Check

Disconnect the OEM interface harness from the ECM. Make sure the sensor is connected to the OEM harness.

Insert one of the leads into pin 26 (+5-VDC supply) of the OEM interface harness connector. Insert the other lead into pin 11 (return) of the connector.

![[19800922.png]]

Connect the alligator clips to the multimeter leads. Measure the resistance. The multimeter **must** show 2000 to 3000 ohms when the accelerator pedal is up or down. If the resistance is **not** within the specification, there is a problem with the wire connected to pin 11 or pin 26 in the OEM interface harness, provided the accelerator position sensor has been previously checked. Repair the OEM interface harness. Refer to Procedure 019-240. Repair the OEM harness according to the vehicle manufacturer's instructions.

![[19800926.png]]

Remove the pin of the lead from pin 11 (return) and insert it into pin 29 (signal) of the OEM interface harness connector.

Make sure the foot pedal is in the released (idle) position.

Measure the resistance from pin 26 to pin 29. The multimeter **must** show 1500 to 3000 ohms.

![[19800927.png]]

Depress the foot pedal (full-fuel) and measure the resistance again. The multimeter **must** show 200 to 1500 ohms. This resistance value **must** be at least 1000 ohms lower than the resistance value of 1500 to 3000 ohms measured in the above check. If the resistance values are **not** within the specification, there is a problem with the wire connected to pin 26 (+5-VDC supply) or pin 29 (signal) in the OEM harness. Repair the OEM interface harness. If the resistance values in the two previous checks are within the specification, pins 11, 26, and 29 **must** still be checked for a short circuit to ground, a short circuit from pin to pin, and a short circuit to battery supply.

> [!note] Note · Примечание
> When checking the OEM harness, examine the bulkhead connector and other connectors in the circuit for corrosion or damage to the accelerator position sensor wire terminals.

![[19800928.png]]

### Check for Short Circuit to Ground

Disconnect the accelerator position sensor from the OEM harness at the foot pedal assembly.

![[tl8swkb.png]]

Insert the test lead into pin 26 (+5-VDC supply). Connect the clip to the multimeter positive (+) probe. Touch the multimeter negative (-) probe to the engine block and measure the resistance.

The multimeter **must** show an open circuit (100k ohms or more).

![[19800929.png]]

Remove the lead from pin 26 and insert it into pin 11 (return). Touch the multimeter negative (-) lead to the engine block and measure the resistance.

The multimeter **must** show an open circuit (100k ohms or more).

![[19800930.png]]

Remove the lead from pin 11 and insert it into pin 29 (signal). Touch the multimeter negative (-) lead to the engine block and measure the resistance. The multimeter **must** show an open circuit (100k ohms or more).

If **any** of these three resistance measurements are **not** open, there is a short circuit to ground between the wires connected to pins 26, 29, or 11. Repair the OEM interface harness. Refer to Procedure 019-240. Repair the OEM harness according to the vehicle manufacturer's instructions.

![[19800931.png]]

### Check for Short Circuit from Pin to Pin

Disconnect the accelerator position sensor from the OEM harness at the foot pedal assembly.

![[tl8swkb.png]]

Insert one of the test leads to pin 26 (+5-VDC supply) of the OEM interface harness connector. Insert the other lead to pin 1 of the connector. Connect the clips to the multimeter probes and measure the resistance.

The multimeter **must** show an open circuit (100k ohms or more).

![[19800932.png]]

Remove the lead from pin 1 and insert it into pin 2, then pin 3, until all pins are tested.

The multimeter **must** show an open circuit (100k ohms or more) at all pins.

If the multimeter shows a closed circuit at any pin, there is a short circuit between pin 26 and any other pin that measured a closed circuit. Repair the OEM interface harness. Refer to Procedure 019-240. Repair the OEM harness according to the vehicle manufacturer's instructions.

![[19800933.png]]

Remove the lead from pin 26 and insert it into pin 29 (return) of the OEM interface harness connector. Insert the other lead into pin 1 and measure the resistance.

The multimeter **must** show an open circuit (100k ohms or more).

![[19800934.png]]

Remove the lead from pin 1 and insert it into pin 2, then pin 3, until all pins are tested.

The multimeter **must** show an open circuit (100k ohms or more) at all pins.

If the multimeter shows a closed circuit at any pin, there is a short circuit between pin 29 and any other pin that measured a closed circuit. Repair the OEM interface harness. Refer to Procedure 019-240. Repair the OEM harness according to the vehicle manufacturer's instructions.

![[19800935.png]]

Remove the lead from pin 29 and insert it into pin 11 (return) of the OEM interface harness connector. Insert the other lead into pin 1 and measure the resistance.

The multimeter **must** show an open circuit (100k ohms or more).

![[19400485.png]]

Remove the lead from pin 1 and insert it into pin 2, then pin 3, until all pins are tested.

The multimeter **must** show an open circuit (100k ohms or more) at all pins.

If the multimeter shows a closed circuit at any pin, there is a short circuit between pin 11 and any other pin that measured a closed circuit. Repair the OEM interface harness. Refer to Procedure 019-240. Repair the OEM harness according to the vehicle manufacturer's instructions.

![[19400486.png]]

### Check for Short Circuit to External Voltage Source

Disconnect the accelerator position sensor from the OEM harness at the foot pedal assembly.

![[tl8swkb.png]]

Turn the vehicle keyswitch to the ON position. Set the multimeter to measure VDC. Insert one of the leads into pin 26 (+5-VDC supply) of the OEM interface harness connector. Connect the clip to the multimeter positive (+) probe. Connect the multimeter negative (-) probe to the engine block and measure the voltage.

The voltage **must** be 1.5 VDC or less.

![[19800923.png]]

Remove the lead from pin 26 and insert it into pin 11 (return) of the OEM interface harness connector. Touch the multimeter negative (-) probe to the engine block and measure the voltage.

The voltage **must** be 1.5 VDC or less.

![[19800924.png]]

Remove the lead from pin 11 and insert it into pin 29 (signal) of the OEM interface harness connector. Touch the multimeter negative (+) probe to the engine block and measure the voltage.

The voltage **must** be 1.5 VDC or less.

If more than 1.5 VDC is measured at **any** pin, there is a short circuit from pin 26, 11, or 29 to a wire carrying power. Repair the OEM interface harness. Refer to Procedure 019-240. Repair the OEM harness according to the vehicle manufacturer's instructions.

> [!note] Note · Примечание
> The external voltage source is **any** wire in the harness that carries voltage.

![[19800925.png]]

Connect the alligator clips to the multimeter leads. Measure the resistance. The multimeter **must** show 2000 to 3000 ohms when the accelerator pedal is up or down. If the resistance is **not** within the specification, there is a problem with pin 11 or 26 in the OEM interface harness, provided the accelerator position sensor has been previously checked. Repair the OEM interface harness. Refer to Procedure 019-240. Repair the OEM harness according to the vehicle manufacturer's instructions.

![[19800926.png]]

Remove the lead from pin 11 (return) and insert it into pin 29 (signal) of the OEM harness connector.

Make sure the foot pedal is in the released (idle) position.

Measure the resistance from pin 26 to pin 29 of the OEM interface harness connector. The multimeter **must** show 1500 to 3000 ohms.

![[19800927.png]]

Depress the foot pedal (full-fuel) and measure the resistance again. The multimeter **must** show 200 to 1500 ohms. This resistance value **must** be at least 1000 ohms lower than the resistance value of 1500 to 3000 ohms measured in the above check. If the resistance values are **not** within the specification, there is a problem with pin 26 (+5-VDC supply) or pin 29 (signal) in the OEM harness. Repair the OEM interface harness. If the resistance values in the two previous checks are within the specification, pins 11, 26, and 29 **must** still be checked for a short circuit to ground, a short circuit from pin to pin, and a short circuit to battery supply.

> [!note] Note · Примечание
> When checking the OEM harness, examine the bulkhead connector and other connectors in the circuit for corrosion or damage to the accelerator position sensor wire terminals.

![[19800928.png]]
