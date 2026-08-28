---
aliases:
  - "Клапан отсечки топлива"
type: "Процедура"
doc: "40-005-043"
title_en: "Fuel Shutoff Valve"
title_ru: "Клапан отсечки топлива"
modified: "2005-01-14"
engines:
  - "93047320"
families:
  - "6B5.9"
manuals:
  - "4021538"
figures: 42
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/40/40-005-043.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/40-005-043.pdf"
tags:
  - "документ/процедура"
  - "двигатель/6B5.9"
  - "группа/40"
---

# Fuel Shutoff Valve
**Клапан отсечки топлива**

> [!abstract] Процедура · `40-005-043`
> **Двигатели:** [[93047320 — 6B5.9 CPL 3111|93047320]]
> **Семейство:** 6B5.9
> **Входит в руководства:** [[4021538 — B3.9 and B5.9 Recreational Marine Operation and Maintenance Manual|4021538]]
> **Секции:** Section A - Adjustment, Repair, and Replacement
> **Даты:** изменён 2005-01-14
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/40/40-005-043.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/40-005-043.pdf)

### General Information

Shutdown Solenoid Troubleshooting (In-Line-Type Injection Pump)

Engines using the in-line type of injection pumps are equipped with the Synchro-Start fuel shutoff solenoid to actuate the shutoff lever. Both 12-VDC and 24-VDC external fuel shutoff solenoids are available.

![[fv900ka.png]]

The Synchro-Start has a Weather-Pack connector with three wires in it.

| Color | Description | Weather-Pack Port |
|---|---|---|
| Black | Ground | C |
| White | Pull-in | B |
| Red | Hold-in | A |

![[fv900gk.png]]

Refer to the chart below to find the correct gauge size and length of continuous wire for the white (pull-in) wire which connects to the solenoid wiring.

This is the total wire length from the battery to the solenoid and back to the battery. Both white and black wire length **must** be added.

Fourteen-gauge wire is required for the red (hold-in) wire, which connects to the “Run” terminal on the ignition switch.

The black (ground) wire **must** be the same size as the white (pull-in) wire.

| Length of Wire - Maximum Length |  |  |
|---|---|---|
| Gauge | 12 VDC | 24 VDC |
| 14 | 1.5-m \[5-ft\] | 2.7-m \[9-ft\] |
| 12 | 2.7-m \[9-ft\] | 4.3-m \[14-ft\] |
| 10 | 4.3-m \[14-ft\] | 7.0-m \[23-ft\] |

![[05900603.png]]

### Preparatory Steps

Bosch® VE

Remove the electrical wire and complete the following steps.

Clean around the valve.

![[fv900mb.png]]

Bosch® A Pump with RSV Governor

This repair can be performed without removing the fuel pump from the engine.

Removal of the shutoff lever, filter, and supply line is **not** necessary if the solenoid can be accessed from the bottom of the fuel pump.

Remove the fuel filter and fuel supply line, if necessary. Refer to Procedures [[40-006-015-tr — Fuel Filter (Spin-On Type)|006-015]] and 006-024.

Disconnect the wire harness from the fuel shutoff solenoid.

![[fs9ftec.png]]

### Initial Check

In-line Fuel Injection Pumps

> [!danger] WARNING · Опасно
> Wear protective clothing to reduce the possibility of personal injury. Solenoid surface temperature can exceed 175°C \[347°F\], which can cause serious burns to the skin in the event of contact.

> [!note] Note · Примечание
> The following check is for all In-line fuel injector pumps.

Values are taken at 20°C \[68°F\] and rated voltage. Minimum values are for 25-mm \[1.00-in\] maximum plunger travel. As the temperature of the solenoid increases, the voltage and resistance requirements increase, while the amperage requirements decrease.

The solenoid resistance can be checked using a multimeter. Disconnect the wiring harness and check the solenoid resistance.

![[fv900sa.png]]

Synchro-Start solenoids with a 44.45-mm \[1.75-in\] diameter coil canister

| Synchro-Start Solenoids 44.5-mm \[1.75-in\] Diameter Coil Canister |  |  |
|---|---|---|
| Solenoid Voltage | Acceptable Resistance Range in Ohms |  |
|  | Pull-in | Hold-in |
| 12 | 0.198 to 0.242 | 10.00 to 12.21 |
| 24 | 0738 to 0.902 | 37.17 to 45.43 |

Synchro-Start Solenoids with a 50.8-mm \[2.00-in\] Diameter Coil Canister.

| Synchro-Start Solenoids 50.8-mm \[2.00-in\] Diameter Coil Canister |  |  |
|---|---|---|
| Solenoid Voltage | Acceptable Resistance Range in Ohms |  |
|  | Pull-in | Hold-in |
| 12 | 0.175 to 0.213 | 12.75 to 15.56 |
| 24 | 0.554 to 0.678 | 46.76 to 57.15 |

![[fv900sa.png]]

Voltage Checking

> [!note] Note · Примечание
> The following check is for all In-line fuel injector pumps.

To perform the solenoid voltage check, disconnect the solenoid rod end from the shutdown lever on the fuel pump, connect the wiring harness, and apply voltage to the solenoid with the ignition key as follows:

1. With the key in the RUN position, check the hold-in voltage.
2. With the shutdown lever held in the shutdown position, move the key to the START position, and check the pull-in voltage.

Refer to the table for Synchro-Start voltage specification with solenoid at 20°C \[68°F\]. Voltage requirements will be higher as engine temperature rises; therefore, these values are **only** valid with the solenoid at normal ambient temperatures.

| Synchro-Start Solenoids 20° C \[68°F\] |  |  |
|---|---|---|
| Solenoid Voltage | Minimum Voltage |  |
|  | Pull-in | Hold-In |
| 12 | 8.5 | 5.2 |
| 24 | 17.0 | 9.4 |

![[fv900sb.png]]

Stanadyne DB4

> [!warning] CAUTION · Осторожно
> Do not check energize-to-run solenoid operation with governor cover removed from the fuel injection pump.

Test the shutdown solenoid on the Stanadyne DB4 fuel injection pump by applying an electrical current to the terminals and listening for a click. If a solid click is heard, the solenoid is operating freely.

Use the following values to check energize-to-run solenoids:

| Standadyne DB4 Solenoid |  |
|---|---|
| VDC | VDC to Energize (Minimum) |
| 12 | 8.8 |
| 24 | 17.6 |

![[ip900ka.png]]

Lucas CAV DPA or DPS

When the valve on the Lucas CAV DPA/DPS pump opens, a click can be heard.

Use the following values to check the solenoid:

| CAV Solenoid Values |  |  |
|---|---|---|
| VDC | Resistance Ohms | VDC to Energize (Minimum) |
| 12 | 9 at 22°C \[71.6°F\] | 9 |
| 24 | 36 at 22°C \[71.6°F\] | 18 |

![[fv900wc.png]]

Delivery Valves (Back Leakage Valves on Lucas CAV Pumps)

There is a valve for each discharge tube. The purpose of the valve is to control the residual pressure in the high-pressure line. A malfunctioning valve will cause an imbalance of the residual pressure resulting in rough engine operation or surging.

![[fv900gj.png]]

Bosch® VE

The Bosch® valve does **not** make a very loud sound when actuated, but it can be checked with an ohmmeter for the following values:

| Bosch Shutdown Values | Resistance Ohms | Peak Amperes |
|---|---|---|
| 12 VDC | 7.4 + 0.5 | 2 |
| 24 VDC | 29.5 + 2.5 | 1 |

![[fv900wd.png]]

> [!warning] CAUTION · Осторожно
> Do not connect the electrical wire to the solenoid when the plunger has been removed. Without the plunger, the valve can be damaged.

Malfunctioning valves and electrical wiring to the valve can be diagnosed by removing the plunger and spring, and then reinstalling the solenoid.

![[fs900ba.png]]

If the engine will start without the valve, the valve or the wiring to the valve is malfunctioning.

This method of removing the plunger to start the engine can be used, if necessary, to move the equipment to a service location.

Use the mechanical shutdown lever to stop the engine.

![[fv900bb.png]]

### Remove

Bosch® VE

Remove the valve.

> [!note] Note · Примечание
> The Bosch® VE valve is shown. The valve for Lucas CAV is located at the bottom of the pump.

![[fv9vama.png]]

> [!warning] CAUTION · Осторожно
> When removing the valve, be careful not to drop the plunger and spring. Doing so can result in fuel pump damage.

![[fv9vaea.png]]

Stanadyne DB4

Tamper-Resistant Screw Removal Tool, Part Number 3399870

- Remove the electrical wiring.
- Remove the fuel drain line. Refer to Procedure 006-021.
- Remove the throttle and shutoff linkage. Refer to the OEM service manual.
- Remove tamper-resistant screws using service tool kit, Part Number. 3399870. Refer to Procedures [[40-005-012-tr — Fuel Injection Pumps, In-Line|005-012]] or [[40-005-014-tr — Fuel Injection Pump, Rotary|005-014]].
- Remove the fuel injection pump top cover. Refer to the Master Repair Manual, Injector Pumps and Injectors, Bulletin 3666037.
- Disassemble the fuel injection pump top cover. Refer to the Master Repair Manual, Injector Pumps and Injectors, Bulletin 3666037.

![[ip9cvmc.png]]

Bosch® A Pump with RSV Governor

Remove the rod end from the shutoff lever.

![[05900738.png]]

Remove the stop screw and bracket assembly.

![[05900552.png]]

Remove the shutoff lever (10) over the shutoff shaft on the inboard side of the fuel pump.

![[05900743.png]]

Remove the solenoid from the solenoid bracket assembly and solenoid bracket assembly from the fuel pump. If the old 1-3/4 inch solenoid and bracket assembly is being replaced with the new 2-inch solenoid, discard the solenoid mounting capscrews.

![[05900739.png]]

Bosch® P Pump with RQVK Governor

The solenoid does **not** have to be removed from engine to replace the control rod.

Loosen the locknut washer (1) from the solenoid (3).

Disconnect the control rod (2) at the lever if control rod is **not** broken.

Unscrew the control rod while holding the solenoid swivel.

![[05900834.png]]

Loosen the capscrew and nut that holds the rod end onto the shutoff lever.

Retain the spacer between the rod end and the shutoff lever.

![[05900835.png]]

Check the shufoff lever stop lever stop bracket.

The lever **must** make contact with the stop screw on the stop screw bracket. If the lever does **not** touch the stop screw, adjust the stop screw out 1-1/2 turns past the point of contact between the stop screw and the shutoff lever.

![[05900836.png]]

### Install

Bosch® VE

Package the solenoid, o-ring, spring, and plunger.

![[fv9pgha.png]]

Tighten the solenoid securely.

Connect the electric wire.

> [!tip] Момент затяжки · Torque Value
> 43 n•m [32 ft-lb]

![[fv900hb.png]]

Stanadyne DB4

Install new insulating tubes onto the terminals on the terminal studs of the new solenoid.

Install the valve into the cover.

> [!tip] Момент затяжки · Torque Value
> 14 n•m [124 in-lb]

![[ip9tbha.png]]

Install the cover and gasket onto the fuel injection pump.

With the tool installed as shown, place the cover in position on the pump housing. Twist the tool to release it, and slide it out from between the cover and the housing.

Extreme care **must** be taken in assembling the cover to a fuel injection pump to make sure the shutoff arm is in proper contact with the linkage hook tab.

![[ip9cvhb.png]]

In the event the service tool is **not** available, the governor cover **must** be installed as follows:

Move the shutoff lever to the stop position.

Install the cover to pump at a downward angle from the driveshaft end of the fuel injection pump, then slide the cover horizontally into position.

> [!tip] Момент затяжки · Torque Value
> 4.6 n•m [41 in-lb]

![[ip9cvha.png]]

Bosch® A Pump with RSV Governor

> [!warning] CAUTION · Осторожно
> Failure to observe proper cranking and fuel system priming procedures can cause solenoid failures.

Install the shutoff solenoid on the fuel pump using two new M16 x 1.5-16 capscrews. Apply Loctite™ to the capscrew threads. Tighten the capscrews just enough to hold the solenoid in place.

> [!note] Note · Примечание
> New solenoid mounting capscrews have threadlocker pre-applied. Loctite™ application is **not** necessary when new capscrews are installed.

> [!warning] CAUTION · Осторожно
> New solenoid mounting capscrews must be used if replacing an old 1-3/4-inch solenoid with a 2-inch solenoid. Insufficient thread engagement can cause damage to the pump and the solenoid.

![[05900740.png]]

Install the shutoff lever (10) over the shutoff shaft on the fuel pump.

Use the capscrew (7) previously removed to hold the shutoff lever in place.

> [!tip] Момент затяжки · Torque Value
> 9 n•m [84 in-lb]

![[05900743.png]]

Connect the rod end of the solenoid to the shutoff lever.

Tighten the shutoff lever nut.

> [!tip] Момент затяжки · Torque Value
> 9 n•m [84 in-lb]

![[05900744.png]]

> [!warning] CAUTION · Осторожно
> The solenoid mounting capscrews must not be overtightened. Distortion to the fuel pump body can result causing the rack to stick in the fuel pump.

Tighten the solenoid mounting capscrews.

> [!tip] Момент затяжки · Torque Value
> 24 n•m [212 in-lb]

![[05900741.png]]

> [!note] Note · Примечание
> If the stop screw is **not** moved, readjustment may **not** be necessary.

Assemble the stop screw to the stop screw bracket. Adjust the stop screw (3) so the contact surface of the screw protrudes 10 mm beyond the surface of the stop bracket (4).

Tighten the nut (2) against the stop bracket to lock the stop screw in place.

![[05900551.png]]

Install the stop bracket assembly using two M6 x 1-16 capscrews (5).

Tighten the capscrews.

> [!tip] Момент затяжки · Torque Value
> 7 n•m [60 in-lb]

![[05900552.png]]

> [!warning] CAUTION · Осторожно
> The solenoid rod length is pre-set. Adjustment of the solenoid rod can cause damage to the solenoid or lead to a low power complaint.

Verify the shutoff lever is contacting the stop screw and is in the full stop position. If the shutoff lever does **not** contact the stop screw, verify the shutoff solenoid and stop screw bracket are assembled correctly. Loosen the solenoid mounting capscrews and readjust the solenoid, if necessary.

![[05900742.png]]

Bosch® P Pump with RQVK Governor

The rod end to control rod orientation is important. If the rod end is installed incorrectly, improper operation of the shutoff solenoid assembly can occur.

Install the locknut (1) onto the new control rod at the rod end until there is \[13 mm\] 7/16 inch between the start of the threads (2) and nut (1).

![[05900837.png]]

Install the lock washer.

Screw the rod end onto the control rod, hand tightening and making certain **not** to move the locknut. Lay the control rod and rod end on a flat surface. Rotate the rod end so both the control rod and the rod end lay flat.

Tighten the locknut onto the rod end.

![[05900838.png]]

Install the locknut (2) on the control rod at the solenoid end until there is \[6 mm\] 1/4 inch between start of the threads (1) and locknut (2).

Install the lock washer and screw the control rod into the solenoid.

![[05900839.png]]

Install the control rod end capscrew onto the fuel pump shutoff lever to align the control rod.

Tighten the locknut (1) while holding the solenoid swivel (3).

![[05900840.png]]

The solenoid is designed to allow rotation of the control rod.

Make certain to install the spacer between the rod end and the shutoff lever.

Tighten the capscrew and nut that holds the rod end onto the shutoff lever.

> [!tip] Момент затяжки · Torque Value
> 9 n•m [80 in-lb]

![[05900835.png]]

### Finishing Steps

Install all components removed, including the fuel filter and fuel supply line.

Connect the wire harness to the fuel shutoff solenoid.

![[ck800wa.png]]
