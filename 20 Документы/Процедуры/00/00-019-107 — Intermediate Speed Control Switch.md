---
aliases:
  - "Выключатель промежуточной частоты вращения"
type: "Процедура"
doc: "00-019-107"
title_en: "Intermediate Speed Control Switch"
title_ru: "Выключатель промежуточной частоты вращения"
modified: "2021-08-05"
engines:
  - "37292556"
  - "37295879"
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
  - "QST30"
manuals:
  - "3666214"
  - "3666266"
figures: 14
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/00/00-019-107.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/00-019-107.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "двигатель/QST30"
  - "группа/00"
---

# Intermediate Speed Control Switch
**Выключатель промежуточной частоты вращения**

> [!abstract] Процедура · `00-019-107`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]], [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11, QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]], [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section 19 - Electronic Controls - Group 19
> **Даты:** изменён 2021-08-05
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/00/00-019-107.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/00-019-107.pdf)

### Select Service Tools

#### Recommended Cummins® Service Tools

- Cummins® electronic service tool, or equivalent

#### Additional Service Items

- Multimeter

### General Information

The intermediate speed control switch circuit signals the engine control module (ECM) that the operator is requesting the engine to run at a preset engine speed between low idle and high idle. Depending on the configuration, up to eight speeds are available. This procedure can **not** cover every possible configuration, but the functionality checks provided in this procedure will be similar for all of them.

![[19400281.png]]

The intermediate speed control circuit is shown for intermediate speed control 1 and intermediate speed control 2 features. The calibration can have **only** one intermediate speed control active feature. The intermediate speed control circuit is wired with a double pole, double throw, three-position switch.

![[19d03212.png]]

The double pole, double throw, three position switch, functions to selectively ground the three intermediate speed control input wires to the ECM. Reference the wiring diagram for terminal locations. The logic of the switch is shown.

The lines that connect the switch terminals at the three lever positions are lines of continuity between the terminals.

In position 1, switch terminals number 2, 3 and 5, 6 are connected, which shorts intermediate speed control 2 and intermediate speed control validation (pins 25 and 33) to ground.

In position 2, no pins are grounded.

In position 3, switch terminals number 1, 2 and 4, 5 are connected, which shorts intermediate speed control 1 and intermediate speed control validation (pins 23 and 33) to ground.

![[19400283.png]]

### Initial Check

Connect an electronic service tool to the vehicle data link.

Turn the keyswitch to the ON position.

Operate the intermediate speed control switch while monitoring with the recommended Cummins® electronic service tool or equivalent. The electronic service tool reading should change with the switch position.

![[19900524.png]]

### Resistance Check

Use the following steps for the intermediate speed control switch:

- If the electronic service tool is available, monitor the intermediate speed control switch for proper operation. If **not**, follow the troubleshooting procedures in this section.
- Remove the four connectors from the switch. Label the wires with the switch location and the wire numbers before removing them from the switch.

![[19d03213.png]]

With the switch in position 1, measure the resistance from switch terminal 2 to switch terminal 3. The resistance **must** be 10 ohms or less.

Measure the resistance from switch terminal 5 to switch terminal 6. The resistance **must** be 10 ohms or less.

Measure the resistance from switch terminal 1 to all switch terminals. The resistance **must** be 100K ohms or more.

Measure the resistance from switch terminal 4 to all other terminals. The resistance **must** be 100K ohms or more.

![[19400285.png]]

Move the switch lever to position 2.

Measure the resistance from switch terminal 1 to all other terminals. The resistance **must** be 100K ohms or more.

Measure the resistance from switch terminal 2 to all other terminals. The resistance **must** be 100K ohms or more.

![[19400286.png]]

Move the switch lever to position 3.

Measure the resistance from switch terminal 1 to terminal 2. The resistance **must** be 10 ohms or less.

Measure the resistance from switch terminal 4 to terminal 5. The resistance **must** be 10 ohms or less.

Measure the resistance from switch terminal 3 to all other terminals. The resistance **must** be 100K ohms or more.

Measure the resistance from switch terminal 6 to all other terminals. The resistance **must** be 100K ohms or more.

If the multimeter does **not** show the correct values, the switch has malfunctioned. Verify the switch type and terminal location numbers. Refer to the original equipment manufacturer (OEM) service manual for replacement and to verify the switch type and terminal location.

![[19400287.png]]

> [!warning] CAUTION · Осторожно
> The leads must fit tightly in the connector without expanding the pins in the connector, otherwise the connector will be damaged.

Use the following steps for the variable intermediate speed control switch.

Disconnect the OEM harness connector from the ECM. Disconnect the variable intermediate speed control switch from the OEM harness. Set the multimeter to measure resistance.

Insert a test lead into the variable intermediate speed control switch SIGNAL pin of the OEM harness connector. Connect the alligator clip to a multimeter probe. Insert the second test lead to the SIGNAL pin of the intermediate speed control switch and connect the clip to the other multimeter probe. Measure the resistance.

![[19c01269.png]]

The multimeter **must** show a measurement of 10 ohms or less (closed circuit).

If the measured value is more than 10 ohms, there is an open circuit in the SIGNAL wire.

Repair or replace the OEM harness. [[99-019-071 — OEM Wiring Harness|Refer to Procedure 019-071 in Section 19.]]

![[19c01235.png]]

Repeat the resistance check for the RETURN wire. Measure the resistance from the variable intermediate speed control switch RETURN pin of the OEM harness connector to the variable intermediate speed control switch RETURN pin of the switch.

The multimeter **must** show a measurement of 10 ohms or less (closed circuit).

If the measured value is more than 10 ohms, there is an open circuit in the RETURN wire.

Repair or replace the OEM harness. [[99-019-071 — OEM Wiring Harness|Refer to Procedure 019-071 in Section 19.]]

Repeat the resistance check for the 5 volt SUPPLY wire. Measure the resistance from the variable intermediate speed control switch 5 volt SUPPLY pin of the OEM harness connector to the variable intermediate speed control switch 5 volt SUPPLY pin of the switch.

The multimeter **must** show a measurement of 10 ohms or less (closed circuit).

If the measured value is more than 10 ohms, there is an open circuit in the 5 volt SUPPLY wire.

Repair or replace the OEM harness. [[99-019-071 — OEM Wiring Harness|Refer to Procedure 019-071 in Section 19.]]

### Check for Short Circuit to Ground

Disconnect the OEM harness connector from the ECM. Disconnect the variable intermediate speed control switch from the OEM harness. Set the multimeter to measure resistance.

Insert the test lead into the variable intermediate speed control switch SIGNAL pin of the OEM harness connector. Touch the other multimeter probe to engine block ground. Measure the resistance.

![[19c01166.png]]

The multimeter **must** show a measurement of 100k ohms or more (open circuit).

If the measured value is less than 100k ohms, there is a short circuit to ground in the SIGNAL wire.

Repair or replace the OEM harness. [[99-019-071 — OEM Wiring Harness|Refer to Procedure 019-071 in Section 19.]]

![[19c01248.png]]

Repeat the short-to-ground check for the RETURN wire. Measure the resistance from the variable intermediate speed control switch RETURN pin of the OEM harness connector to engine block ground.

The multimeter **must** show a measurement of 100k ohms or more (open circuit).

If the measured value is less than 100k ohms, there is a short circuit to ground in the RETURN wire.

Repair or replace the OEM harness. [[99-019-071 — OEM Wiring Harness|Refer to Procedure 019-071 in Section 19.]]

Repeat the short-to-ground check for the 5 volt SUPPLY wire. Measure the resistance from the variable intermediate speed control switch 5 volt SUPPLY pin of the OEM harness connector to engine block ground.

The multimeter **must** show a measurement of 100k ohms or more (open circuit).

If the measured value is less than 100k ohms, there is a short circuit to ground in the 5 volt SUPPLY wire.

Repair or replace the OEM harness. [[99-019-071 — OEM Wiring Harness|Refer to Procedure 019-071 in Section 19.]]

### Check for Short Circuit from Pin-to-Pin

Disconnect the OEM harness connector from the ECM. Disconnect the variable intermediate speed control switch from the OEM harness. Set the multimeter to measure resistance.

Measure the resistance from the variable intermediate speed control switch SIGNAL pin in the OEM harness connector to all other pins in the connector.

![[19c01215.png]]

The multimeter **must** show a measurement of 100k ohms or more (open circuit).

If the measured value is less than 100k ohms, there is a short circuit between the SIGNAL wire and any other pin that measured a closed circuit.

Repair or replace the OEM harness. [[99-019-071 — OEM Wiring Harness|Refer to Procedure 019-071 in Section 19.]]

### Check for Short Circuit to External Voltage Source

Disconnect the OEM harness connector from the ECM. Disconnect the variable intermediate speed control switch from the OEM harness. Set the multimeter to measure volts of direct current (VDC). Turn the vehicle keyswitch to the ON position.

Insert the test lead connected to the positive (+) multimeter probe into the variable intermediate speed control switch SIGNAL pin of the OEM harness connector. Touch the negative (-) multimeter probe to engine block ground and measure the voltage.

![[19c01158.png]]

If there is voltage present, there is a short circuit from the SIGNAL wire to an external voltage source.

Repair or replace the OEM harness. [[99-019-071 — OEM Wiring Harness|Refer to Procedure 019-071 in Section 19.]]

Repeat the short to external voltage source check for the RETURN wire. Measure the voltage from the variable intermediate speed control switch RETURN pin of the OEM harness connector to engine block ground.

If there is voltage present, there is a short circuit from the RETURN wire to an external voltage source.

Repair or replace the OEM harness. [[99-019-071 — OEM Wiring Harness|Refer to Procedure 019-071 in Section 19.]]

Repeat the short to external voltage source check for the 5 volt SUPPLY wire. Measure the voltage from the variable intermediate speed control switch 5 volt SUPPLY pin of the OEM harness connector to engine block ground.

The multimeter **must** show a voltage of less than 5.5-VDC. If the voltage is greater than 5.5-VDC, there is a short circuit from the 5 volt SUPPLY wire to an external voltage source.

Repair or replace the OEM harness. [[99-019-071 — OEM Wiring Harness|Refer to Procedure 019-071 in Section 19.]]
