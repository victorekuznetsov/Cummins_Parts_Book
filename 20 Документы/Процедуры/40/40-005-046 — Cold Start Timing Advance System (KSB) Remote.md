---
type: "Процедура"
doc: "40-005-046"
title_en: "Cold Start Timing Advance System (KSB) Remote"
modified: "2006-03-31"
engines:
  - "93047320"
families:
  - "6B5.9"
manuals:
  - "3666087"
figures: 32
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/40/40-005-046.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/40-005-046.pdf"
tags:
  - "документ/процедура"
  - "двигатель/6B5.9"
  - "группа/40"
---

# Cold Start Timing Advance System (KSB) Remote

> [!abstract] Процедура · `40-005-046`
> **Двигатели:** [[93047320 — 6B5.9 CPL 3111|93047320]]
> **Семейство:** 6B5.9
> **Входит в руководства:** [[3666087 — B3.9, B4.5, B4.5 RGT, and B5.9 Service Manual|3666087]]
> **Секции:** Section 5 - Fuel System - Group 05
> **Даты:** изменён 2006-03-31
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/40/40-005-046.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/40-005-046.pdf)

### General Information

Wax-Motor Style

Cold Start Timing Advance System (KSB) - Wax Motor Style

The wax motor-style KSB is used on pre-1991 B Series automotive engine ratings using the Bosch® VE fuel pump.

> [!note] Note · Примечание
> The electrical solenoid-style KSB is used on 1991 model and newer B Series automotive engine ratings using the Bosch® VE fuel injection pump. See [[40-005-070 — Cold Start Timing Advance System Pump Mounted|Procedure 005-070]], Cold Start Timing Advance System (KSB) - Pump Mounted, for additional information.

![[cs900gs.png]]

Wax Motor Style KSB

> [!note] Note · Примечание
> Temperature switch is located in the coolant jacket.

![[cs900gs.png]]

Electrical Solenoid-Style KSB

> [!note] Note · Примечание
> Temperature switch is located in the intake manifold.

![[cs900gt.png]]

KSB Hardware Definition

There are currently two versions of pump-mounted wax motor-style KSBs released in the Cummins system and one remote-mounted version. The remote mounted option is necessary in applications where the pump-mounted KSB causes interference (i.e., with the air compressor).

![[nobox.png]]

Remote Mounted KSB

The remote-mounted KSB is used on B Series automotive engines that have an air compressor.

![[cs900gu.png]]

> [!warning] CAUTION · Осторожно
> Most pumps will have a shim between the KSB and the timing piston. This shim must be reassembled between the cover plate and the timing piston. If this shim sticks to the KSB and is installed with the remote-mounting hardware, it will block the regulating valve drain path and damage the pump. This damage is usually evidenced by a fuel leak.

![[cs900wb.png]]

The four-cylinder engine using remote mounting requires the temperature switch to be installed in the cylinder head as illustrated.

![[cs900wc.png]]

Electrical Solenoid Style

Cold Start Timing Advance System (KSB) - Electrical Solenoid Style

The electrical solenoid-style KSB is used on 1991 model and newer B Series automotive engine ratings using the Bosch® VE fuel pump.

> [!note] Note · Примечание
> The wax motor-style KSB is used on pre-1991 B Series automotive engine ratings using the Bosch® VE fuel pump.

![[nobox.png]]

Wax Motor-Style KSB

> [!note] Note · Примечание
> The temperature switch is located in the coolant jacket.

![[cs900gs.png]]

Electrical Solenoid-Style KSB

> [!note] Note · Примечание
> Temperature switch is located in intake manifold.

![[cs900gt.png]]

Two types of electrical solenoid-style KSB valves are available.

The first type is the pump-mounted KSB, as shown.

![[cs900gz.png]]

The second type is the remote-mounted KSB, as shown.

The remote-mounted KSB is used on B Series automotive engines that have an air compressor.

![[cs901ga.png]]

> [!warning] CAUTION · Осторожно
> Most pumps will have a shim between the KSB and the timing piston. This shim must be reassembled between the cover plate and the timing piston. If this shim sticks to the KSB and is installed with the remote-mounting hardware, it will block the regulating valve drain path and damage the pump. This damage is usually evidenced by a fuel leak.

![[cs900wb.png]]

Both the four-and-six cylinder have the temperature switch mounted in the intake manifold, as shown.

![[cs9swga.png]]

### Disassemble

Wax-Motor Style

Loosen and remove the KSB electrical element from the KSB housing.

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

Use a very small screwdriver to be sure the check ball is **not** sticking.

> [!note] Note · Примечание
> A sticking or malfunctioning pressure relief valve will result in either white smoke or a ruptured fuel pump housing.

Replace the pressure relief valve assembly, if necessary.

![[cs9cbsa.png]]

Install the original pressure relief valve or a replacement into the KSB housing.

> [!tip] Момент затяжки · Torque Value
> 13 n•m [115 in-lb]

![[cs9vama.png]]

### Test

Wax-Motor Style

Apply 12 VDC to the electrical terminal and a ground strap to the hexagonal portion of the element. Check for extensional movement of the plunger. If the plunger does **not** move after approximately 1 minute, check to make sure the element has been correctly connected to ground. If all connections are correct and the plunger does **not** move, the element is defective and **must** be replaced.

> [!note] Note · Примечание
> The amount of plunger movement will vary depending upon the ambient temperature.

![[cs9swvd.png]]

Electrical Solenoid Style

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

### Resistance Check

Wax-Motor Style

The wiring harness used on the wax motor-style KSB can be inspected using a multimeter.

> [!note] Note · Примечание
> Pin C of the metro-pack connector is blank on the wax motor style KSB wiring harness.

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
> Pin B of the metro-pack connector is blank on the electric solenoid style KSB wiring harness.

![[cs900we.png]]

The electric solenoid-style KSB wiring harness contains a 3-ohm resistor in the wire leading from port C of the metro-pack connector to the KSB electrical solenoid connector.

The 3-ohm resistor is mounted to a bracket that is utilized as a heat sink to absorb heat that is generated by the resistor.

![[cs900oa.png]]

Use a multimeter to perform a continuity check between port C of the metro-pack connector and the KSB electrical solenoid connector.

Repair the wire if there is an open circuit.

(Spec = Less than 10 ohms).

![[cs900ob.png]]

Use a multimeter to perform a continuity check between port A of the metro-pack connector and the fuel pump shutdown solenoid connector.

Repair the wire if there is an open circuit.

(Spec = Less than 10 ohms).

![[cs900oc.png]]
