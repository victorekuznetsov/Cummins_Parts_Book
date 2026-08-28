---
type: "Процедура"
doc: "40-005-037-tr"
title_en: "Fuel Pump Timing"
modified: "2007-06-22"
engines:
  - "93047320"
families:
  - "6B5.9"
manuals:
  - "3666087"
figures: 30
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/40/40-005-037-tr.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/40-005-037-tr.pdf"
tags:
  - "документ/процедура"
  - "двигатель/6B5.9"
  - "группа/40"
---

# Fuel Pump Timing

> [!abstract] Процедура · `40-005-037-tr`
> **Двигатели:** [[93047320 — 6B5.9 CPL 3111|93047320]]
> **Семейство:** 6B5.9
> **Входит в руководства:** [[3666087 — B3.9, B4.5, B4.5 RGT, and B5.9 Service Manual|3666087]]
> **Секции:** Section 5 - Fuel System - Group 05
> **Даты:** изменён 2007-06-22
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/40/40-005-037-tr.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/40-005-037-tr.pdf)

### General Information

Pump-to-engine timing is extremely critical. Pump timing that is off by **only** a few crankshaft degrees will cause:

1. Poor performance - starting and power.
2. Excessive smoke.
3. Poor fuel economy.

![[oi901vm.png]]

### Time

Engine pump timing begins with the timing of the fuel injection pump drive gear to the camshaft gear.

The first step is the location of TDC of the compression stroke for cylinder Number 1.

Then, depending on the engine configuration, an alpha character on the injection pump drive gear will possibly need to be aligned with the mark on the camshaft gear.

![[it900wa.png]]

This table **must** be used to maintain proper fuel injection pump-to-engine timing. The Control Parts List (CPL) number from the engine dataplate and the Control Parts List Manual, Bulletin 3379133 or 4021327, **must** be used to determine whether the engine is certified, and if so, what year and regulating agency (EPA or CARB).

Given this information, use the following table to determine which letter on the fuel injection pump drive gear is aligned with the camshaft gear.

> [!note] Note · Примечание
> Timing mark alignment is **not** required for the Nippondenso EP-9 or Bosch® in-line drive gear.

> [!note] Note · Примечание
> The timing mark is **not** required for Bosch® VE and DP210 used on Tier II Industrial engines. For these engines, vary timing by using the Timing Check procedure.

| Letter on Pump Gear | Engine Model | Injection Pump | Certification |
|---|---|---|---|
| A | 4B3.9, 4BT3.9 | Stanadyne pump | Noncertified |
| A | 4B3.9, 4BT3.9, 4BTA3.9 | Lucas CAV DPA pump | All noncertified |
| B | 4B3.9, 4BTA3.9 | Bosch® VE | 1986, 1987 EPA, All pre-1986, All noncertified |
| C | 6BT5.9, 6BTA5.9 | Bosch® VE | 1986, 1987 EPA, All pre-1986, All noncertified, CPL 600 |
| D | 6B5.9, 6BT5.9 | Stanadyne | Noncertified |
| D | 6B5.9, 6BT5.9, 6BTA5.9 | Lucas CAV DPA | All noncertified |
| E | 6BT5.9, 6BTA5.9 | Bosch® VE | 1986, 1987, 1988, 1989, 1990, 1991, 1992 CARB |
| F | 4BT3.9, 4BTA3.9 | Bosch® VE | 1986, 1987, 1988, 1989, 1990, 1991, 1992 CARB, 1988, 1989, 1990, 1991, 1992 EPA |
| G | 6BTA5.9 | Lucas CAV DPA | All Fire Pumps |
| H | **Not** used at this time | N/A | N/A |

To verify that the fuel injection pump is timed correctly, first check the alignment marks on the pump flange and gear housing.

> [!note] Note · Примечание
> 1 mm of rotation past the timing mark will advance or retard (depending on direction of rotation) the pump timing by 1 degree.

![[it900wc.png]]

The Lucas CAV DPA, DPS, Delphi DP210, Stanadyne DB4, and the Bosch® VE fuel injection pumps all have a provision for locking the pump shaft at a position corresponding to top dead center for cylinder Number 1. New and reconditioned fuel injection pumps **must** be received with the shafts located in this position.

![[fp9shwb.png]]

At the point of injection, the keyway of the shaft will align with the delivery valve receiving the injection and the illustrated hash mark on the seal housing.

> [!note] Note · Примечание
> The illustrated mark is for reference **only** and **must not** be used for setting the fuel injection pump timing.

![[fp9shwc.png]]

The Number 1 cylinder delivery valve is marked as illustrated.

Four cylinder = A

Six cylinder = D

| Firing Order |  |
|---|---|
| Four Cylinder | Six Cylinder |
| A =1 | D = 1 |
| B = 3 | E = 5 |
| C = 4 | F = 3 |
| D = 2 | A = 6 |
|  | B = 2 |
|  | C = 4 |

![[fp9pgga.png]]

The engine is equipped with an engine timing pin to locate top dead center (TDC) for cylinder Number 1.

![[cg9gega.png]]

> [!warning] CAUTION · Осторожно
> If the timing pin is incorrectly located on the gear housing, the pump will not be timed correctly.

After precisely locating TDC for cylinder Number 1, the factory positions the timing pin assembly to the gear housing, using the timing pin and the hole in the camshaft gear. If the gear housing or timing pin assembly are removed, the same precision is required to relocate it.

If the timing pin assembly is incorrectly located, reposition the timing pin.

![[cg9gewa.png]]

The flange of a replacement pump **must** be marked to align with the mark on the gear housing after installation.

During production, after the locked pump is fitted to the engine with cylinder Number 1 at top dead center (TDC), a mark is stamped on the gear housing and the pump flange. Thereafter, when these marks are aligned, the pump is correctly timed to the engine.

> [!note] Note · Примечание
> The marks on the gear housing and the pump flange are unique to each engine.

![[fp900wl.png]]

See Service Tool Instruction, Bulletin 3400196 and Service Tool Catalog, Bulletin 3377710 to determine the appropriate Bosch® timing tool and adapter kit part numbers.

A special indicator can be used to measure the position of the Bosch® VE fuel injection pump plunger to check pump timing.

![[fs900wn.png]]

Stanadyne DB4 Fuel Injection Pump Timing

Clean all debris from around the fuel injection pump timing window cover.

![[ip900ea.png]]

Remove the fuel injection pump timing cover.

![[ip9cvmb.png]]

Rotate the fuel injection pump driveshaft in the direction of pump rotation to align the timing line on the weight retainer hub with the line on the cam ring.

![[ip900wb.png]]

Position the fuel injection driveshaft locking key plate in the locked position. Turn the locking screw in until contact is made with the driveshaft.

> [!tip] Момент затяжки · Torque Value
> 11.9 n•m [105 in-lb]

![[ip9waha.png]]

Verify the timing marks are aligned after timing is locked.

![[ip900wb.png]]

Install the fuel injection pump timing cover.

![[ip9cvmb.png]]

CAV DPA/DPS Fuel Injection Pump Timing

Correct timing of the Lucas CAV DPA/DPS fuel injection pump can be verified by removing the inspection plate.

> [!note] Note · Примечание
> Special equipment in an authorized shop is required to time the Lucas CAV DPA fuel injection pump precisely. However, for troubleshooting and in an emergency, visual alignment of the timing mark is close enough for the engine to run.

Both of these checks are described in the fuel injection pump replacement. [[40-005-012-tr — Fuel Injection Pumps, In-Line|Refer to Procedure 005-012 (Fuel Injection Pumps, In-Line) in Section 5.]]

[[40-005-014-tr — Fuel Injection Pump, Rotary|Refer to Procedure 005-014 (Fuel Injection Pump, Rotary) in Section 5.]]

[[40-005-013 — Fuel Injection Pump, In-Line, Spill Port Timing|Refer to Procedure 005-013 (Fuel Injection Pump, In-Line, Spill Port Timing) in Section 5 for installation of the timing pin.]]

![[ap9plwa.png]]

Timing Check - (Bosch® VE Pump)

Rotate the crankshaft to top dead center (TDC).

![[cg9piwa.png]]

Remove the plug from the end of the pump.

![[fp9pxma.png]]

> [!warning] CAUTION · Осторожно
> Do not bend the fuel lines. Doing so can result in fuel system failure.

See Service Tool Instruction, Bulletin 3400196 and Service Tool Catalog, Bulletin 3377710 to determine the appropriate Bosch® timing tool and adapter kit part numbers.

Install the timing indicator. Be sure to allow adequate travel for the indicator.

In order to install the timing indicator, it is often necessary to disconnect one or more of the fuel lines from the fuel pump.

> [!note] Note · Примечание
> The indicator is marked in increments of 0.01 mm. 1 revolution of the indicator needle is equal to 0.50 mm.

![[fp9towa.png]]

Bar the crankshaft in the direction opposite engine rotation until the indicator needle stops moving. Adjust the indicator face to read 0.

Rotate the crankshaft back to top dead center (TDC), and count the number of revolutions of the indicator needle. The reading shown when the engine timing pin engages is the amount of plunger lift the pump has at that point.

![[er900wg.png]]

Bosch® VE Pumps with Slotted Mounting Holes

Rotate the pump on the mounting studs until the indicator reads the correct value for plunger lift. This illustration gives an example of the indicator readings for the various plunger lift values.

Tighten the flange mounting nuts.

> [!tip] Момент затяжки · Torque Value
> 24 n•m [18 ft-lb]

![[fp900wm.png]]

Bosch® VE Pumps with Round Mounting Holes

Rotate the engine until the plunger travel is at the desired location.

Lock the fuel pump. [[40-005-014-tr — Fuel Injection Pump, Rotary|Refer to Procedure 005-014 (Fuel Injection Pump, Rotary) in Section 5.]]

![[05900806.png]]

Separate the fuel pump drive gear from the pump shaft. [[40-005-014-tr — Fuel Injection Pump, Rotary|Refer to Procedure 005-014 (Fuel Injection Pump, Rotary) in Section 5]]

With the pump locked, rotate the engine back to TDC.

![[05900807.png]]

Torque the fuel pump drive nut. [[40-005-014-tr — Fuel Injection Pump, Rotary|Refer to Procedure 005-014 (Fuel Injection Pump, Rotary) in Section 5.]]

Unlock the fuel pump.

Verify the correct timing has been achieved by measuring the static timing.

![[fp9nuhd.png]]

Remove the timing indicator. Install the plug.

> [!tip] Момент затяжки · Torque Value
> 10 n•m [89 in-lb]

![[fp9toma.png]]

Pump Timing - Lucas CAV DPA, Stanadyne DB4, Delphi DP210, Nippondenso EP-9, and Bosch® P7100

Rotate the engine to top dead center (TDC).

![[cg9piwa.png]]

Correct timing of the Lucas CAV DPA and Stanadyne DB4 fuel injection pump can be verified by removing the timing window cover plate.

The Nippondenso EP-9 and Bosch® P-7100 fuel injection pumps are checked by removing the timing pin access plug and verifying the slot in the pin will fit over the timing tooth in the fuel injection pump.

> [!note] Note · Примечание
> Special equipment in an authorized shop is required to time the Lucas CAV DPA fuel injection pump precisely. However, for troubleshooting and in an emergency, visual alignment of the timing mark is close enough for the engine to run.

To correct the timing on the Bosch® P-7100 and Nippondenso EP-9, see the replacement procedure for the respective pump.

![[fp900wn.png]]

Two injection pump timing marks are used on the Stanadyne DB4 for timing injection of fuel into the Number 1 cylinder. One mark is located on the governor weight retainer hub. The other is located on the internal cam ring. These two marks **must** be aligned at Number 1 cylinder top dead center (TDC).

![[ip900wb.png]]

On the Lucas CAV DPA, the correct timing letter can be located on the engine dataplate as shown.

The letter G indicated refers to the correct timing letter alignment as shown in the previous frame.

![[ap9plwb.png]]
