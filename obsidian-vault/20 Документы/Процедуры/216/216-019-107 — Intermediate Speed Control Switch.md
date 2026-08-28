---
aliases:
  - "Выключатель промежуточной частоты вращения"
type: "Процедура"
doc: "216-019-107"
title_en: "Intermediate Speed Control Switch"
title_ru: "Выключатель промежуточной частоты вращения"
modified: "2013-04-16"
engines:
  - "82099327"
families:
  - "QSB6.7"
manuals:
  - "4326168"
figures: 18
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/216/216-019-107.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/216-019-107.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSB6.7"
  - "группа/216"
---

# Intermediate Speed Control Switch
**Выключатель промежуточной частоты вращения**

> [!abstract] Процедура · `216-019-107`
> **Двигатели:** [[82099327 — QSB6.7 CM2150 B109 CPL 4375|82099327]]
> **Семейство:** QSB6.7
> **Входит в руководства:** [[4326168 — QSB6.7 CM2150 B109 Service Manual|4326168]]
> **Секции:** Section 19 - Electronic Controls - Group 19
> **Даты:** изменён 2013-04-16
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/216/216-019-107.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/216-019-107.pdf)

### General Information

The intermediate speed control (ISC) switch circuit signals the engine control module (ECM) that the operator is requesting the engine to run at a preset engine speed between low idle and high idle. Depending on the configuration, up to eight speeds are available. This procedure can **not** cover every possible configuration, but the functionality checks provided in this procedure will be similar for all of them.

![[19400281.png]]

The ISC circuit is shown for ISC 1 and ISC 2 features. The calibration can have **only** one ISC active feature. The ISC circuit is wired with a double pole, double throw (DPDT), three-position switch.

![[19d03212.png]]

The double pole, double throw (DPDT) three-position switch functions to selectively ground the three ISC input wires to the ECM. Refer to the wiring diagram for terminal locations. The logic of the switch is shown.

The lines that connect the switch terminals at the three lever positions are lines of continuity between the terminals.

In position 1, switch terminals No. 2, 3 and 5, 6 are connected, which shorts ISC 2 and ISC validation (pins 25 and 33) to ground.

In position 2, no pins are grounded.

In position 3, switch terminals No. 1, 2 and 4, 5 are connected, which shorts ISC 1 and ISC validation (pins 23 and 33) to ground.

![[19400283.png]]

### Resistance Check

Use the following steps for the intermedate speed control switch:

If INSITE™ electronic service tool is available, monitor the ISC switch for proper operation. If **not**, follow the troubleshooting procedures in this section.

Remove the four connectors from the switch. Label the wires with the switch location and the wire numbers before removing them from the switch.

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

If the multimeter does **not** show the correct values, the switch has malfunctioned. Verify the switch type and terminal location numbers. Refer to the OEM service manual for replacement and to verify the switch type and terminal location.

![[19400287.png]]

> [!warning] CAUTION · Осторожно
> The leads must fit tightly in the connector without expanding the pins in the connector otherwise the connector will be damaged.

Use the following steps for the variable intermediate speed control switch.

Disconnect the original equipment manufacturer (OEM) harness connector from the ECM. Disconnect the variable intermediate speed control switch from the OEM harness. Set the multimeter to measure resistance.

Insert a test lead into the variable intermediate speed control switch signal pin of the OEM harness connector. Connect the alligator clip to a multimeter probe. Insert the second test lead to the signal pin of the intermediate speed control switch and connect the clip to the other multimeter probe. Measure the resistance.

![[19c01269.png]]

The multimeter **must** show a measurement of 10 ohms or less (closed circuit).

If the measured value is more than 10 ohms, there is an open circuit in the signal wire.

Repair or replace the OEM harness. [[99-019-071 — OEM Wiring Harness|Refer to Procedure 019-071 in Section 19.]]

![[19c01235.png]]

Repeat the resistance check for the return wire. Measure the resistance from the variable intermediate speed control switch RETURN pin of the OEM harness connector to the variable intermediate speed control switch return pin of the switch.

The multimeter **must** show a measurement of 10 ohms or less (closed circuit).

If the measured value is more than 10 ohms, there is an open circuit in the RETURN wire.

Repair or replace the OEM harness. [[99-019-071 — OEM Wiring Harness|Refer to Procedure 019-071 in Section 19.]]

![[19c01235.png]]

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

![[19c01248.png]]

### Check for Short Circuit from Pin to Pin

Disconnect the OEM harness connector from the ECM. Disconnect the variable intermediate speed control switch from the OEM harness. Set the multimeter to measure resistance.

Measure the resistance from the variable intermediate speed control switch SIGNAL pin in the OEM harness connector to all other pins in the connector.

![[19c01194.png]]

The multimeter **must** show a measurement of 100k ohms or more (open circuit).

If the measured value is less than 100k ohms, there is a short circuit between the SIGNAL wire and any other pin that measured a closed circuit.

Repair or replace the OEM harness. [[99-019-071 — OEM Wiring Harness|Refer to Procedure 019-071 in Section 19.]]

![[19c01215.png]]

### Check for Short Circuit to External Voltage Source

Disconnect the OEM harness connector from the ECM. Disconnect the variable intermediate speed control switch from the OEM harness. Set the multimeter to measure VDC. Turn the vehicle keyswitch to the ON position.

Insert the test lead connected to the positive (+) multimeter probe into the variable intermediate speed control switch SIGNAL pin of the OEM harness connector. Touch the negative (-) multimeter probe to engine block ground and measure the voltage.

![[19c01158.png]]

If there is voltage present, there is a short circuit from the SIGNAL wire to an external voltage source.

Repair or replace the OEM harness. [[99-019-071 — OEM Wiring Harness|Refer to Procedure 019-071 in Section 19.]]

![[19c01158.png]]

Repeat the short to external voltage source check for the RETURN wire. Measure the voltage from the variable intermediate speed control switch RETURN pin of the OEM harness connector to engine block ground.

If there is voltage present, there is a short circuit from the RETURN wire to an external voltage source.

Repair or replace the OEM harness. [[99-019-071 — OEM Wiring Harness|Refer to Procedure 019-071 in Section 19.]]

![[19c01158.png]]
