---
aliases:
  - "Работа с мультиметром"
type: "Процедура"
doc: "99-019-359"
title_en: "Multimeter Usage"
title_ru: "Работа с мультиметром"
modified: "2023-02-03"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
  - "35354607"
  - "35373113"
  - "37269910"
  - "37280605"
  - "37292556"
  - "37295879"
  - "41343322"
  - "41349633"
  - "41353297"
  - "41370103"
  - "71156161"
  - "80141463"
  - "80248213"
  - "85017333"
  - "93058669"
  - "93087701"
families:
  - "C8.3 · 6C8.3"
  - "K19"
  - "NT/NTA855 · ISM/QSM11"
  - "QSK19"
  - "QSK23"
  - "QSK60"
  - "QSM11"
  - "QST30"
  - "QSX15"
manuals:
  - "3666070"
  - "3666113"
  - "3666184"
  - "3666214"
  - "3666266"
  - "3666410"
  - "3666415"
  - "4021419"
  - "4021442"
  - "4021587"
  - "4021617"
  - "4021674"
figures: 27
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-359.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/99-019-359.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "двигатель/K19"
  - "двигатель/NT/NTA855"
  - "двигатель/QSK19"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "двигатель/QSM11"
  - "двигатель/QST30"
  - "двигатель/QSX15"
  - "группа/99"
---

# Multimeter Usage
**Работа с мультиметром**

> [!abstract] Процедура · `99-019-359`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]], [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]], [[41343322 — NH NT 855 CPL 3362|41343322]], [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]], [[41370103 — NH NT 855 CPL 3362|41370103]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]], [[85017333 — QSK23 CM500 CPL 2858|85017333]], [[93058669 — 6C8.3 CPL 3105|93058669]], [[93087701 — 6C8.3 CPL 3105|93087701]]
> **Семейство:** C8.3 · 6C8.3, K19, NT/NTA855 · ISM/QSM11, QSK19, QSK23, QSK60, QSM11, QST30, QSX15
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]], [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]], [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual|3666184]], [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]], [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]], [[3666410 — QSK45 and QSK60 CENSE™ Electronic Control System Troubleshooting and Repair Manual|3666410]], [[3666415 — ICON Idle Control System Master Repair Manual|3666415]], [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]], [[4021442 — C8.3 Marine Electronic Control System Troubleshooting and Repair Manual|4021442]], [[4021587 — C Command Panel System Marine Master Repair Manual|4021587]], [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]], [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section 19 - Electronic Engine Controls · Section 19 - Electronic Engine Controls - Group 19 · Section 19 — Electronic Engine Controls · Section 19 — Electronic Engine Controls — Group 19
> **Даты:** изменён 2023-02-03
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-359.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/99-019-359.pdf)

### General Information

How to Use a Multimeter

On most meters, the negative (-), (black) meter probe **must** be plugged into the COM position and the positive (+), (red) meter probe **must** be plugged into one of the positions marked for amperage, resistance, or voltage. Refer to the manufacturer's procedures for more detail.

> [!note] Note · Примечание
> When measuring to a block or chassis ground, use a clean, unpainted metal surface to make sure a good measurement exists.

![[19400203.png]]

Use of Special Test Leads

> [!warning] CAUTION · Осторожно
> To reduce the possibility of pin and harness damage, use the appropriate test lead for the connector. Refer to the Service Tools listing or the appropriate wiring repair kit for this control system.

Refer to the appropriate wiring repair kit for specific test leads used on this application.

![[nobox.png]]

How to Measure Amperage

Make an open circuit at the place where the current is to be measured.

Select the AC current (A ˜) or DC current (A-) function on the meter.

Turn on the power in the circuit being measured.

Put the probes of the meter across the open circuit to measure the amperage.

Read the displayed measurement.

![[19400206.png]]

How to Measure Voltage

Select the AC voltage (V ˜) or DC voltage (V-) function on the meter.

Turn on the power in the circuit being measured.

Touch the positive (+) probe of the multimeter to the terminal or pin that is being measured for voltage. Touch the other probe to a clean, unpainted metal surface that is connected to battery ground or to the negative (-) post of the battery.

Read the displayed measurement.

![[19a00020.png]]

How to Measure Resistance

Select the resistance function on the meter.

Verify that there is no power to the components being tested.

Disconnect both ends of the circuit or component to be measured. Touch one probe to one end of the circuit or component terminal. Touch the other probe to the other end of the circuit or the other component terminal.

Read the displayed measurement.

![[19400207.png]]

How to Find the Internal Resistance of the Meter

It is important to know the internal resistance of the meter when measuring small resistances. To measure small resistances accurately, the internal resistance of the meter **must** be subtracted from the measured resistance.

Turn the meter ON.

Set the meter to the lowest ohm scale.

Measure the resistance of the meter by touching the test probes together and reading the resistance value (including special test leads, if they are being used).

ZERO the meter or subtract this value when taking measurements.

![[19400208.png]]

How to Test for Continuity

Select the continuity function on the meter (usually marked with a diode symbol).

Make sure there is no power to the component being measured.

Disconnect both ends of the circuit or component to be measured. Touch one probe to one end of the circuit or component terminal. Touch the other probe to the other end of the circuit or the other component terminal.

Read the displayed measurement.

The meter will beep if the resistance is less than about 150 ohms. If there is an open circuit, the meter does **not** beep.

![[19800311.png]]

Short Circuit to Ground - Check

Short circuit to ground is a condition where a connection from a circuit to ground exists when it is **not** intended.

The procedure for checking for a short circuit to ground is as follows:

- Turn keyswitch OFF.
- Disconnect the connectors that are to be tested.

![[19200195.png]]

When testing a sensor, **only** the sensor connection is required to be disconnected.

When testing a harness, the harness connector at the electronic control unit and the connector at the sensor or multiple sensors should be disconnected.

Identify the pins that need to be tested.

Inspect the connector pins. 019-361.

Adjust the multimeter to measure resistance.

![[19800313.png]]

> [!warning] CAUTION · Осторожно
> To reduce the possibility of pin and harness damage, use the appropriate test lead for the connector. Refer to the Service Tools listing or the appropriate wiring repair kit for this control system.

Touch one of the multimeter probes to the correct pin to be tested.

Touch the other probe of the multimeter to a clean, unpainted surface on the engine block or chassis ground.

Read the value on the multimeter display.

![[19800314.png]]

The multimeter **must** read greater than 100k ohms, which is an open circuit.

If the circuit is **not** open, the wire being checked has a short circuit to ground, engine block or chassis ground.

Repair or replace the component or wire.

![[19a00016.png]]

Short Circuit from Pin to Pin - Check

Short circuit from pin to pin is a condition in which an electrical path exists between two pins where it is **not** intended to exist.

The procedure for checking short circuit from pin to pin is as follows:

1. Turn keyswitch OFF.
2. Disconnect the connector that is to be tested.
3. Identify the pins that are to be tested.
4. Adjust the multimeter to measure resistance.

![[19400213.png]]

> [!warning] CAUTION · Осторожно
> To reduce the possibility of pin and harness damage, use the appropriate test lead for the connector. Refer to the Service Tools listing or the appropriate wiring repair kit for this control system.

1. Touch one of the multimeter probes to the correct pin to be tested on the harness side of the connector.
2. Touch the other probe of the multimeter to all other pins on the harness side of the connector.

![[19800315.png]]

1. Read the value on the multimeter display.
2. The multimeter **must** read greater than 100k ohms, which is an open circuit.
3. If the circuit is **not** open, the pins being checked are electrically connected.

> [!note] Note · Примечание
> Refer to the wiring diagram to verify that the wires in question are **not** supposed to be connected.

1. Inspect the harness connectors for moisture that can be the cause of an inappropriate electrical connection.
2. Repair or replace the harness.

![[19a00016.png]]

Voltage Checking

Voltage check is a procedure to measure the difference in voltage potential between two points.

The procedure for checking voltage is as follows:

1. Disconnect the connectors that are to be tested.
2. Turn keyswitch ON.
3. Identify the pins that are to be tested.
4. Adjust the multimeter to AC voltage (V ˜) or DC voltage (V-).

![[19c00177.png]]

> [!warning] CAUTION · Осторожно
> To reduce the possibility of pin and harness damage, use the appropriate test lead for the connector. Refer to the Service Tools listing or the appropriate wiring repair kit for this control system.

1. Touch one of the multimeter test probes to the correct lead to be tested.
2. Touch the other multimeter probe to a clean, unpainted surface on the engine block, chassis ground or to the appropriate return pin.

![[19900495.png]]

1. Read the value on the multimeter display. Compare the measured value to the range of voltage given in the specifications.
2. If the measured value falls outside of the specified range, check the repair procedure for the electrical system that is being checked for the appropriate action.

![[19400217.png]]

Circuit Load Test

> [!warning] CAUTION · Осторожно
> To reduce the possibility of pin and wiring harness damage, always use the appropriate test lead for the connector. Reference Service Tools listing or the appropriate wiring harness repair kit.

> [!warning] CAUTION · Осторожно
> Never insert test leads into ECM connector terminals. Connector terminals can spread and cause intermittent electrical connections.

Circuit load testing is a procedure to measure the amount of voltage loss that occurs in a circuit caused by high circuit resistance. Perform this test with Cummins® service tool, Part Number 5394709, Electronic Specialties 180 LOADpro® Dynamic Test Leads, circuit load test leads, or equivalent, or with a 12 VDC H6024 or H6054 headlight or equivalent.

Use electrical circuit tester, to help identify terminal number locations. See corresponding wiring diagram for circuit terminal locations.

![[19800315.png]]

**Circuit load test with Cummins® service tool, Part Number 5394709, Electronic Specialties 180 LOADpro® Dynamic Test Leads, circuit load test leads, or equivalent**

Initial Set-up

Remove multimeter test leads and install Cummins® service tool, Part Number 5394709, Electronic Specialties 180 LOADpro® Dynamic Test Leads, circuit load test leads, or equivalent. Connect connector test leads to connector pins and connect alligator clips to multimeter probe.

**Never** use circuit load test lead positive red (+) probe in RETURN pin of circuit as this can energize a component switched in ground.

Measurement

The procedure for performing circuit load testing is as follows:

1. Disconnect load component (sensor or actuator) from wiring harness connector.
2. Disconnect ECM power harness connector from ECM.
3. Using appropriate test leads, connect external 12/24 VDC battery positive to one end of the wire to be tested.
4. Connect battery negative to a clean, unpainted surface on engine cylinder block or chassis ground.
5. Connect circuit load tester positive red (+) probe at other end of wire to be tested.
6. Connect negative circuit load tester lead to a clean, unpainted surface on engine cylinder block or chassis ground.
7. Adjust multimeter to DC voltage (V-).
8. If voltage is within + 1 volt of battery voltage, proceed to step 10.
9. If voltage is **not** within + 1 volt of battery, perform open circuit checks.
10. Depress circuit load tester probe button for maximum of 5 to 8 seconds. Record voltage drop.
11. Repeat steps 3, 4, 5, 6, 7, 8 and 9 for all pins at sensor, or actuator connector.
12. If voltage drops, there is high resistance in wiring circuit.

Specification

| Maximum allowable voltage drop | Less than 0.8 VDC per wire |
|---|---|

If high resistance is found in circuit. See corresponding Service Manual. Reference 019-360 in Section 19.

**Circuit load test with a 12 VDC H6024 or H6054 or equivalent headlight**

Initial Set-up

The procedure for performing circuit load testing is as follows:

1. Disconnect load component (sensor or actuator) from engine harness connector.
2. Disconnect ECM power harness connector from ECM.
3. Using appropriate test leads, connect external 12 VDC battery positive to one end of the wire to be tested.
4. Connect battery negative to a clean, unpainted surface on the engine block or chassis ground.
5. Connect headlight at the opposite end of the wire being tested, with the appropriate pin/socket connector test lead.
6. Connect RETURN pins of the headlight to a clean, unpainted surface on the engine block or chassis ground. Reference specification.
7. Repeat steps 3, 4, 5 and 6 for all pins at sensor, or actuator connector.
8. Connect multimeter test leads across the headlight terminals and measure voltage drop.

Specification

| Voltage drop across headlight terminal | Within + 1 VDC of battery voltage |
|---|---|

If the headlight light does **not** light when tested, then a malfunctioning wiring harness has been detected.

![[22r00151.png]]

Polarity Check

A battery will be used as an example to check polarity of a circuit.

The terminals of a battery are marked for polarity. The multimeter displays the voltage difference of the positive (+) probe (red) to the negative (-) probe (black).

![[19a00021.png]]

The polarity is correct when the positive (red) probe of the multimeter is on the positive (+) terminal of the battery and the negative (black) probe of the multimeter is on the negative (-) terminal of the battery.

The multimeter will display positive voltage if the polarity is correct.

If the multimeter probes are reversed, the multimeter displays a negative voltage.

![[19800323.png]]

Continuity Check

> [!warning] CAUTION · Осторожно
> To reduce the possibility of pin and harness damage, use the appropriate test lead for the connector. Refer to the Service Tools listing or the appropriate wiring repair kit for this control system.

Continuity is an electrical connection between two pins that is less than a certain resistance value. For harness wires, the specification is less than 10 ohms.

![[19900496.png]]

The procedure for checking continuity is as follows:

1. Turn keyswitch OFF.
2. Disconnect the harness connectors that are to be tested.
3. Adjust the multimeter to measure resistance.

![[19c00186.png]]

> [!warning] CAUTION · Осторожно
> To reduce the possibility of pin and harness damage, use the appropriate test lead for the connector. Refer to the Service Tools listing or the appropriate wiring repair kit for this control system.

1. Insert test lead to the pin of the wire being tested and connect the alligator clip to the multimeter probe.
2. Insert the other test lead to the pin at the other end of the wire being tested and connect the alligator clip to the other multimeter probe.
3. Read the value on the multimeter display.

![[19900496.png]]

The multimeter **must** display less than 10 ohms for wire continuity.

If the multimeter displays greater than 10 ohms, the wire **must** be repaired or the harness replaced.

![[19400225.png]]

Resistance Check - Coil

Turn keyswitch OFF.

Disconnect the harness from the coil.

Adjust the multimeter to measure resistance.

![[19400226.png]]

> [!warning] CAUTION · Осторожно
> To reduce the possibility of pin and harness damage, use the appropriate test lead for the connector. Refer to the Service Tools listing or the appropriate wiring repair kit for this control system.

Insert test lead to the coil connector pin, and connect the alligator clip to the multimeter probe.

Insert the other test lead to the other coil connector pin, and connect the alligator clip to the other multimeter probe.

> [!note] Note · Примечание
> For internally grounded coils, touch one multimeter lead to the coil terminal and the other multimeter lead to a clean, unpainted surface on the engine block.

Read the measured resistance on the multimeter display.

Check the measured resistance against the resistance specification for the coil.

> [!note] Note · Примечание
> The internal resistance of the multimeter is significant in some coil resistance checks.

![[19400227.png]]
