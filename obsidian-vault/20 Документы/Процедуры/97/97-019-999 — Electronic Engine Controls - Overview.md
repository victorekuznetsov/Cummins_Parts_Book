---
type: "Процедура"
doc: "97-019-999"
title_en: "Electronic Engine Controls - Overview"
modified: "2003-06-13"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
  - "80141463"
  - "80248213"
families:
  - "QSM11"
  - "QSX15"
manuals:
  - "3666415"
figures: 30
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-019-999.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-019-999.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "двигатель/QSX15"
  - "группа/97"
---

# Electronic Engine Controls - Overview

> [!abstract] Процедура · `97-019-999`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSM11, QSX15
> **Входит в руководства:** [[3666415 — ICON Idle Control System Master Repair Manual|3666415]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-06-13
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-019-999.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-019-999.pdf)

### General Information

How to Use a Multimeter

On most meters, the negative (black) multimeter lead **must** be plugged in the COM position and the positive (red) multimeter lead **must** be plugged into one of the positions marked for amperage, resistance, or voltage. Refer to the manufacturer's instructions for more detail.

> [!note] Note · Примечание
> When measuring to a block ground, use a clean, unpainted metal surface to make sure of a good measurement.

![[19400203.png]]

Use of Special Test Leads

> [!warning] CAUTION · Осторожно
> To avoid pin and harness damage, use the following test leads when taking a measurement:

(C) Male Deutsch/AMP/Metri-Pack test lead, Part Number 3822758

(F) Female Deutsch/AMP/Metri-Pack test lead, Part Number 3822917.

![[19800729.png]]

How to Measure Amperage

Make an open circuit at the place where the current needs to be measured.

1. Select the AC current (A∼) or DC current (A-) function on the multimeter.
2. Turn on the power in the circuit being measured.
3. Put the leads of the multimeter across the open circuit to measure the amperage.
4. Read the displayed measurement.

![[19400205.png]]

How to Measure Voltage

1. Select the AC voltage (V∼) or DC voltage (V−) function on the multimeter.
2. Turn on the power in the circuit being measured.
3. Touch the positive (+) lead of the multimeter to the terminal or pin that is being measured for voltage. Touch the other lead to a clean, unpainted metal surface that is connected to battery ground or to the negative post of the battery.
4. Read the displayed measurement.

![[19a00020.png]]

How to Measure Resistance

1. Select the resistance function on the multimeter.
2. Verify that there is no power to the components being tested.
3. Disconnect both ends of the circuit or component to be measured. Touch one lead to one end of the circuit or component terminal. Touch the other lead to the other end of the circuit or the other component terminal.
4. Read the displayed measurement.

![[19400207.png]]

How to Find the Internal Resistance of the Meter

It is important to know the internal resistance of the multimeter when measuring small resistances. To measure small resistances accurately, the internal resistance of the multimeter **must** be subtracted from the measured resistance.

1. Turn the multimeter on.
2. Set the multimeter to the lowest ohm scale.
3. Measure the resistance of the multimeter by touching the test leads together and reading the resistance value (including special test leads, if they are being used).
4. “ZERO” the multimeter or subtract this value when taking measurements.

![[19400208.png]]

How to Test for Continuity

1. Select the continuity function on the multimeter (usually marked with a diode symbol).
2. Make sure there is no power to the component being measured.
3. Disconnect both ends of the circuit or component to be measured. Touch one lead to one end of the circuit or component terminal. Touch the other lead to the other end of the circuit or the other component terminal.
4. Read the displayed measurement. The multimeter will beep if the resistance is less than about 150 ohms. If there is an open circuit, the multimeter will **not** beep.

![[19800311.png]]

Connector Pins - Checking

When disconnecting connectors during troubleshooting, the pins **must** always be inspected to make sure they are **not** the cause of a bad connection. First, flush and clean the connector pins using electrical contact cleaner, Part Number 3824510. Then, inspect for bent, expanded, corroded, and pushed back pins.

Moisture in a connector can also cause system performance issues. Many times it is difficult to see moisture in a connector. If moisture is suspected, the connector **must** be dried. Apply contact cleaner, Part Number 3824510, to the connector, or use a heat gun on a low heat setting so that it will **not** damage the connector or wires.

> [!note] Note · Примечание
> Do **not** blow compressed air in the engine ECM or idle control module ports or connectors. Compressed air can contain moisture due to condensation.

![[19900492.png]]

Bent Pins

Inspect the male terminals of the connector. If any of the terminals are bent or expanded so that they will **not** easily mate with the other side of the connector, then the pin **must** be replaced. Refer to the repair section for the specific connector in question.

![[19900492.png]]

Corroded Pins

Inspect both the male and female terminals for corrosion which can cause a poor electrical connection within the connector. If any corrosion is evident on the pins, then the corroded pins **must** be replaced. Refer to the repair section for the specific connector in question.

![[19900492.png]]

Pushed Back Pins

Inspect both the male and female terminals for pins that can **not** be making contact because they are pushed back in the connector. To repair, push the pin into the connector body from the back of the connector. Make sure the terminal locks into place. If the terminal will **not** lock into place, then replace it. Refer to the repair section for the specific connector in question.

![[19900492.png]]

Short Circuit to Ground - Check

The procedure for checking for a short circuit to ground is as follows:

1. Turn the keyswitch to the OFF position.
2. Disconnect the connectors that need to be tested.

![[19900493.png]]

When testing a sensor, it is **only** necessary to disconnect the sensor connection.

When testing a harness, disconnect the harness connector at the idle control module, and the connector at the sensor, or multiple sensors.

1. Identify the pins that need to be tested.
2. Flush and clean the connector pins.
3. Inspect the connector pins for damage.
4. Select the resistance function on the multimeter.

![[19800313.png]]

> [!warning] CAUTION · Осторожно
> Use the appropriate test leads from the wiring harness repair kit, Part Number 3163652 or 3824904, to avoid damage to the connector pins.

1. Touch one of the multimeter leads to the correct pin to be tested.
2. Touch the other multimeter lead to the engine block.
3. Read the value on the multimeter display.

![[19800314.png]]

The multimeter **must** show greater than 100k ohms, which is an open circuit.

If the circuit is **not** open, the wire being checked has a short to ground or the engine block.

1. Repair or replace the component or wire.

![[19a00016.png]]

Short Circuit from Pin to Pin - Check

Short circuit from pin to pin is a condition where an electrical path exists between two pins where it is **not** intended to exist.

The procedure for checking short circuit from pin to pin is as follows:

1. Turn the keyswitch to the OFF position.
2. Disconnect the connector that needs to be tested.
3. Identify the pins that need to be tested.
4. Select the resistance function on the multimeter.

![[19400213.png]]

> [!warning] CAUTION · Осторожно
> Use the appropriate test leads from the wiring harness repair kit, Part Number 3163652 or 3824904, to avoid damage to the connector pins.

1. Touch one of the multimeter leads to the correct pin to be tested on the harness side of the connector.
2. Touch the other multimeter lead to **all** other pins on the harness side of this connector, one at a time.

![[19800315.png]]

1. Read the value on the multimeter display.
2. The multimeter **must** show greater than 100k ohms, which is an open circuit.
3. If the circuit is **not** open, the pins being checked are electrically connected.

> [!note] Note · Примечание
> Refer to the wiring diagram to verify that the wires in question are **not** supposed to be connected.

1. Inspect the harness connectors for moisture, which can cause an electrical connection.
2. Repair or replace the harness.

![[19a00016.png]]

Voltage Checking

Voltage check is a procedure to measure the difference in voltage potential between two points.

The procedure for checking voltage is as follows:

1. Disconnect the connectors that need to be tested.
2. Turn the keyswitch to the ON position.
3. Identify the pins that need to be tested.
4. Select the AC voltage (V∼) or DC voltage (V-) function on the multimeter.

![[19900494.png]]

> [!warning] CAUTION · Осторожно
> Use the appropriate test leads from the wiring harness repair kit, Part Number 3163652 or 3824904, to avoid damage to the connector pins.

1. Touch one of the multimeter test leads to the correct lead to be tested.
2. Touch the other multimeter lead to a clean, unpainted surface on the engine block, or to the appropriate return pin.

![[19900495.png]]

1. Read the value on the multimeter display. Compare the measured value to the range of voltage given in the specifications.
2. If the measured value falls outside of the specified range, check the repair procedure of the electrical system that is being checked for the appropriate action.

![[19400217.png]]

Polarity Check

A battery will be used as an example to check polarity of a circuit.

The terminals of a battery are marked for polarity. The multimeter displays the voltage difference of the positive (+) lead (red) to the negative (-) lead (black).

![[19400221.png]]

The polarity is correct when the positive (+) lead (red) of the multimeter is on the positive terminal of the battery and the negative (-) lead (black) of the multimeter is on the negative terminal of the battery.

The multimeter will display positive voltage if the polarity is correct.

If the multimeter leads are reversed, the multimeter will display negative voltage.

![[19a00021.png]]

Continuity Check

> [!warning] CAUTION · Осторожно
> Use the appropriate test leads from wiring harness repair kit, Part Number 3163652 or 3824904, to avoid damage to the connector pins.

Continuity is an electrical connection between two pins that is less than a certain resistance value. For harness wires, the specification is less than 10 ohms.

![[19900496.png]]

The procedure for checking continuity is as follows:

1. Turn the keyswitch to the OFF position.
2. Disconnect the harness connectors to be tested.
3. Select the resistance function on the multimeter.

![[19900497.png]]

> [!warning] CAUTION · Осторожно
> Use the appropriate test leads from the wiring harness repair kit, Part Number 3163652 or 3824904, to avoid damage to the connector pins.

1. Touch one of the multimeter test leads to the pin of the wire being tested.
2. Touch the other multimeter lead to the pin at the other end of the wire being tested.
3. Read the value on the multimeter display.

![[19900496.png]]

The multimeter **must** display less than 10 ohms for wire continuity.

If the multimeter displays greater than 10 ohms, the wire **must** be repaired or the harness replaced.

![[19400225.png]]

Resistance Check - Coil

1. Turn the keyswitch to the OFF position.
2. Disconnect the harness from the coil.
3. Select the resistance function on the multimeter.

![[19900883.png]]

> [!warning] CAUTION · Осторожно
> Use the appropriate test leads from the wiring harness repair kit, Part Number 3163652 or 3824904, to avoid damage to the connector pins.

1. Touch one of the multimeter leads to the coil connector pin.
2. Touch the other multimeter lead to the other coil connector pin.

> [!note] Note · Примечание
> For internally grounded coils, touch one multimeter lead to the coil terminal and the other multimeter lead to the engine block.

1. Read the measured resistance on the multimeter display.

![[19900884.png]]

Check the measured resistance against the resistance specification for the coil.

> [!note] Note · Примечание
> The internal resistance of the multimeter is significant in some coil resistance checks. Before taking the measurement, “ZERO” the meter, or subtract the meter's internal resistance from the measured value.

![[19900884.png]]

> [!note] Note · Примечание
> It is recommended that a job image from the engine ECM be taken, using the electronic service tool, INSITE™, to aid in troubleshooting.

> [!note] Note · Примечание
> Disconnecting the vehicle battery connections can require that the engine ECM real-time clock be reset using INSITE™
