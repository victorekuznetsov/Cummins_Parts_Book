---
type: "Процедура"
doc: "40-005-070"
title_en: "Cold Start Timing Advance System Pump Mounted"
modified: "2006-03-31"
engines:
  - "93047320"
families:
  - "6B5.9"
manuals:
  - "3666087"
figures: 28
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/40/40-005-070.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/40-005-070.pdf"
tags:
  - "документ/процедура"
  - "двигатель/6B5.9"
  - "группа/40"
---

# Cold Start Timing Advance System Pump Mounted

> [!abstract] Процедура · `40-005-070`
> **Двигатели:** [[93047320 — 6B5.9 CPL 3111|93047320]]
> **Семейство:** 6B5.9
> **Входит в руководства:** [[3666087 — B3.9, B4.5, B4.5 RGT, and B5.9 Service Manual|3666087]]
> **Секции:** Section 5 - Fuel System - Group 05
> **Даты:** изменён 2006-03-31
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/40/40-005-070.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/40-005-070.pdf)

### General Information

Wax-Motor Style

Need For KSB on 1988 VE Pumps

Emission requirements for 1988 prompted the need for a cold start timing advance system (KSB) to minimize white smoke.

After the engine starts, the wax motor-style KSB fully advances the ignition timing at low idle until the engine warms up. The KSB is **not** functional after the engine reaches 71°C \[160°F\] coolant temperature.

KSB Hardware Definition

There are currently two versions of pump-mounted wax motor-style KSBs released in the Cummins system and one remote-mounted version. The remote-mounted option is necessary in applications where the pump-mounted KSB causes interference with the air compressor.

![[nobox.png]]

Pump-Mounted KSB

The early pump-mounted KSB is a different design using two control lines. The two-line version was superseded in mid-1988 with a one-control-line version, which is the design used for both production and service at the moment.

There is no remote-mounted hardware available for the two-control-line KSB, so they can **not** be remote mounted.

![[nobox.png]]

The illustration shows a two-control-line KSB

![[cs900gw.png]]

The illustration shows a one-control-line KSB

![[cs900gx.png]]

Cold Start Timing Advance System (KSB)

Wax Motor-Style

The wax motor-style KSB is used on pre-1991 B Series automotive engine ratings using the Bosch® VE fuel pump.

> [!note] Note · Примечание
> The electrical solenoid-style KSB is used on 1991 model and newer B Series automotive engine ratings using the Bosch® VE fuel injection pump. Refer to [[40-005-046 — Cold Start Timing Advance System (KSB) Remote|Procedure 005-046]], Cold Start Timing Advance System (KSB) - Electrical Solenoid Style, for additional information.

![[nobox.png]]

Cold Start Timing Advance System (KSB)

Electrical Solenoid Style

The electrical solenoid-style KSB is used on 1991 model and newer B Series automotive engine ratings using the Bosch® VE fuel pump.

> [!note] Note · Примечание
> The wax motor-style KSB is used on pre-1991 B series automotive engine ratings using the Bosch® VE fuel pump.

![[nobox.png]]

Wax Motor-Style KSB

> [!note] Note · Примечание
> The temperature switch is located in the coolant jacket.

![[cs900gs.png]]

Electrical Solenoid-Style KSB

> [!note] Note · Примечание
> The temperature switch is located in the intake manifold.

![[cs900gt.png]]

Two types of electrical solenoid-style KSB valves are available.

The first type is the pump-mounted KSB, as shown.

![[cs900gz.png]]

The second type is a remote-mounted KSB, as shown.

The remote-mounted KSB is used on the B Series automotive engines that have an air compressor.

![[cs901ga.png]]

Both the four- and six-cylinder have the temperature switch mounted in the intake manifold as shown.

![[cs9swga.png]]

Pump-Mounted Wax Motor-Style KSB

1. KSB (one control line)
2. Wiring Harness, Cummins Part Number 3918364 (4B), Cummins Part Number 3918431 (6B)
3. 71°C \[160°F\] Temperature Switch, Cummins Part Number 3915945.

![[cs900gy.png]]

### Resistance Check

Wax-Motor Style

The wiring harness used on the wax motor-style KSB can be inspected using a multimeter.

> [!note] Note · Примечание
> Pin C of the metro-pack connector is blank on the wax motor-style KSB wiring harness.

![[cs900wd.png]]

Use a multimeter to perform a continuity check between port A of the metro-pack connector and the female spade connector at the fuel pump shutdown solenoid connector.

Repair the wire if there is an open circuit.

Ohms Resistance - Less than 10.

![[cs900na.png]]

Use a multimeter to perform a continuity check between port B of the metro-pack connector and the female spade connector at the KSB wax motor connector.

Repair the wire if there is an open circuit.

Ohms Resistance - Less than 10.

![[cs900nb.png]]

Electrical Solenoid Style

Engines with CPL 1579 do **not** have a resistor in the harness.

![[ee900gl.png]]

Engines with CPL 1351 **must** be wired with the resistor in the harness.

![[ee900gm.png]]

The wiring harness used on the electric solenoid-style KSB can be inspected using a multimeter.

> [!note] Note · Примечание
> Pin B of the metro-pack connector is blank on the electric solenoid-style KSB wiring harness.

![[cs900we.png]]

The electric solenoid-style KSB wiring harness contains a 3-ohm resistor in the wire leading from port C of the metro-pack connector to the KSB electrical solenoid connector.

The 3-ohm resistor is mounted to a bracket that is used as a heat sink to absorb heat that is generated by the resistor.

![[cs900oa.png]]

Use a multimeter to perform a continuity check between port C of the metro-pack connector and the KSB electrical solenoid connector.

Repair the wire if there is an open circuit.

(Spec = Less than 10 ohms).

![[cs900ob.png]]

Use a multimeter to perform a continuity check between port A of the metro-pack connector and the fuel pump shutdown solenoid connector.

Repair the wire if there is an open circuit.

(Spec = Less than 10 ohms).

![[cs900oc.png]]

### Disassemble

Wax-Motor Style

Loosen and remove the KSB electrical element from the KSB housing if equipped with a wax motor-style KSB.

> [!note] Note · Примечание
> If equipped with a electrical solenoid-style KSB, proceed to the next step.

![[cs9swmb.png]]

Electrical Solenoid Style

Remove the KSB electrical solenoid from the KSB housing.

![[cs900ma.png]]

### Clean

Electrical Solenoid Style

> [!danger] WARNING · Опасно
> When using solvents, acids, or alkaline materials for cleaning, follow the manufacturer's recommendations for use. Wear goggles and protective clothing to avoid personal injury.

> [!danger] WARNING · Опасно
> Wear appropriate eye and face protection when using compressed air. Flying debris and dirt can cause bodily injury.

Thoroughly flush the pressure relief valve with cleaning solution.

Dry with compressed air.

![[cs9vaea.png]]

### Test

Wax-Motor Style

KSB Electric Element

Apply 12 VDC to the electrical terminal and a ground strap to the hexagonal portion of the element. Look for extensional movement of the plunger. If the plunger does **not** move after approximately 1 minute, check to make sure the element has been correctly connected to ground. If all connections are correct and the plunger does **not** move, the element is defective and **must** be replaced.

> [!note] Note · Примечание
> The amount of plunger movement will vary depending upon the ambient temperature.

![[cs9swvd.png]]

Electrical Solenoid Style

KSB Electric Solenoid

Apply 12 VDC to the electrical terminal, and ground the hexagonal portion of the element. The magnetic coil of the solenoid **must** push the plunger outward.

If the plunger does **not** push outward when voltage is applied, the solenoid is defective and **must** be replaced.

![[cs9swve.png]]

### Assemble

Wax-Motor Style

Install the original element or a replacement into the KSB housing.

> [!tip] Момент затяжки · Torque Value
> 22 n•m [16 ft-lb]

![[cs9swmb.png]]

Electrical Solenoid Style

Install the original solenoid or a replacement into the KSB housing.

> [!tip] Момент затяжки · Torque Value
> 22 n•m [16 ft-lb]

![[cs900ma.png]]
