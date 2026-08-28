---
aliases:
  - "Порядок установки"
type: "Процедура"
doc: "97-210-001"
title_en: "Installation Procedure"
title_ru: "Порядок установки"
modified: "2012-05-11"
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
figures: 73
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-210-001.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-210-001.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "двигатель/QSX15"
  - "группа/97"
---

# Installation Procedure
**Порядок установки**

> [!abstract] Процедура · `97-210-001`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSM11, QSX15
> **Входит в руководства:** [[3666415 — ICON Idle Control System Master Repair Manual|3666415]]
> **Секции:** Section G - Installation Guidelines
> **Даты:** изменён 2012-05-11
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-210-001.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-210-001.pdf)

### General Information

Aftermarket

This section has been designed to provide instructions for installing the Aftermarket version of the ICON™ system. Since Cummins Inc. provides engines for many different vehicle and equipment manufacturers, some of the steps will **not** necessarily be performed exactly as shown. A qualified technician should read the instruction, learn the intent of the step, and install the component in a fashion that will comply to the vehicle's configuration. Each deviation from the specific instructions provided in this procedure should be noted. If the ICON™ system fails to work properly, the first troubleshooting step will be to go back and check to see whether the improvised installation procedures were completed correctly.

Refer to the OEM service manual for proper alternator output voltage and amperage specifications.

It is recommended to have on hand the charge and start OEM wiring diagram that shows keyswitch connections before installing the ICON™ system. Variations in keyswitch wiring can increase installation time.

Use the following procedure for additional publications that can provide assistance with the installation of the ICON™ system. [[97-205-001 — Additional Service Literature|Refer to Procedure 205-001 in Section L.]]

> [!note] Note · Примечание
> Eaton Autoshift or Ultra Shift transmissions are currently supported but are incompatible with the keyless engine mode on aftermarked installations. However, **all** manual transmissions support the keyless mode feature.

Before installing the ICON™ system, verify that the transmission housing has a place for a neutral position switch. Neutral position switches are provided in the installation kit. If one of these switches does **not** work in the transmission provided, consult with the transmission supplier for a compatible switch.

Some electronic dashes, such as Pollack, can interfere with ICON™ system operation. This can be verified by performing the Charging System Test. An extra double-throw relay assembly **must** be installed when installing the ICON™ system in an installation with an electronic dash that causes incorrect ICON™ operation. When the ignition bus is powered down, the electronic dash loads down the J1587 public datalink and will **not** allow communication for a short period of time. The aforementioned relay disconnects the dash public datalink from the engine ECM and the ICON™ idle control module while the ignition bus is unpowered.

![[13800070.png]]

![[13800069.png]]

Prior to installing the ICON™ system on trucks older than 3 months or with 16,000 km \[10,000 mi\], the battery charging system **must** be checked. This check serves two purposes:

1. Identifies a charging system that is **not** capable of attaining the proper voltages to allow the ICON™ system to shut down the engine, or identifies a defective charging system.
2. To inform the customer that the charging system is **not** adequate and needs to be repaired or upgraded.

Verify charging system is operating properly. Refererence the following procedures:

- Use the following procedure in Troubleshooting and Repair Manual, N14 Base Engine, Bulletin 3666142. Refer to Procedure 013-001 in Section 13.
- Use the following procedure in Troubleshooting and Repair Manual, N14 Base Engine, Bulletin 3666142. Refer to Procedure 013-007 in Section 13.
- Use the following procedure in Troubleshooting and Repair Manual, M11 Series Engines, Bulletin 3666139. Refer to Procedure 013-001 in Section 13.
- Use the following procedure in Troubleshooting and Repair Manual, M11 Series Engines, Bulletin 3666139. Refer to Procedure 013-007 in Section 13.
- Use the following procedure in Troubleshooting and Repair Manual, ISM, ISM e Series Engines, Bulletin [[3666322 — ISM, ISMe, and QSM11 Service Manual\|3666322]]. Refer to Procedure 013-001 in Section 13.
- Use the following procedure in the QSM11 Series Engines, Bulletin [[3666322 — ISM, ISMe, and QSM11 Service Manual\|3666322]]. Refer to Procedure 013-007 in Section 13.
- Use the following procedures in Troubleshooting and Repair Manual, Signature, ISX, or QSX15 Series Engines, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. Refer to Procedure 013-001 in Section 13.
- Use the following procedure in Troubleshooting and Repair Manual, Signature, ISX, or QSX15 Series Engines, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. [[10-013-007 — Batteries|Refer to Procedure 013-007 in Section 13.]]
- Use the following procedure for the recommended battery charging system specifications. [[97-018-025 — ICON™ System|Refer to Procedure 018-025 in Section V.]]
- The preferred grounding is as follows
- If there is a grounding strap from the batteries to the frame, remove the strap. However, be sure that there is a grounding strap from the starter to the frame.
- Balancing the battery pack:
- Batteries can be discharged or charged unequally causing early failure of one or more batteries. Cummins Inc. recommends that in the main charger system all positive (+) and negative (-) terminal posts be equal distance from the starter.

> [!note] Note · Примечание
> This type of application is incompatible with keyless engine mode.

Scope - The Smart Steering Wheels usually use multiplexer control boxes that can be powered down when the ICON™ system powers down the vehicle. No fault codes will be displayed due to the ICON™ system interpreting this as the cruise switch being turned off.

Problem - It appears that the ICON™ system has been disabled.

Solution - The fix is to wire the keyswitch ignition post to the switched power input of the multiplexer. This will prevent the multiplexer from being powered down.

Keyswitches mounted in the column require different keyswitch wire connections. Wiring diagrams can be unclear on which wires are battery, ignition, start, and accessory connections.

The general installation recommendation in the installation guide is to move all wires from the accessory post and the ignition post of the keyswitch to the ignition bus 1 (wire to pin 30 of ignition bus relay). If necessary, split the wires up between ignition bus 1 and ignition bus 2 wires on the cab harness to balance the current load. Doing this will allow the ICON™ system to control the application of power to all circuits in the cab and to control engine starts. Some customers want the accessory position to control circuits the way it has been traditionally done. In trying to retain this configuration, difficulty can arise from the fact that different OEMs and models route power to these circuits in a way that prevents the ICON™ system from controlling circuit power (fan power for example) properly after an engine shutdown with the key on or off, depending on whether keyless engine mode is in use. Specifically, the difficulty arises because the accessory post is hot when the keyswitch is in the ignition position. This prevents the ICON™ system from turning the fan circuits off after a shutdown.

The accessory post wires **must** be traced out on an OEM diagram to determine which wires can be left connected to the accessory post. This allows the operator to control radios and other traditional circuits connected to the accessory post in the manner to which they have been accustomed. An alternative is to remove wires on a trial-and-error basis. Some installations require a trial-and-error process to determine if all wires can remain connected to the accessory post of the keyswitch. Newer keyswitches are mounted in the column or are the integrated (spade terminal) type. Care should be taken when wiring these installations.

A multimeter can be used to help identify which keyswitch pins have voltage on them when the keyswitch is in the OFF, ACCESSORIES, ON, and START positions.

### Install

Aftermarket

> [!note] Note · Примечание
> All harness connectors and wires are labeled to match the wiring diagram labels for ease of installation. Review the General Information at the front of this section (Section G) before proceeding.

> [!note] Note · Примечание
> Before starting the installation, but after verifying the battery and charging system, it is recommended to connect a battery charger to the batteries. Charging the batteries will help reduce the time it takes to perform the checkout test after the installation.

![[nobox.png]]

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To avoid personal injury, always ventilate the compartment before servicing the batteries. To avoid arcing, remove the negative (-) battery cable first and attach the negative (-) cable last.

Turn the keyswitch to the OFF position. Disconnect the vehicle batteries from the electrical system.

> [!note] Note · Примечание
> On some engine installations, disconnecting the vehicle battery connections can require that the engine ECM real-time clock be reset.

Remove the cab dash panel.

![[ea8coha.png]]

Find suitable places in the engine compartment to mount the ICON™ components. The ICON™ idle control module, engine start alarm, starter relay, and ICON™ engine harness pass-through connector **must** be positioned on the firewall, close to one another on the intake side of the engine. Make sure the ICON™ engine harness easily reaches all of the connectors. Check all harness lengths. Check for possible interference with other components, and check the fit of each component in its chosen location.

The ICON™ engine harness **must** be positioned so that it can be connected to the cab harness pass-through connector under the dash. The cab harness connectors **must** be able to reach the parking brake switch, keyswitch, and in-cab datalink connectors. The exact location of components will vary by OEM.

![[15800030.png]]

When a suitable position for the ICON™ idle control module, engine start alarm, and pass-through connector is found, check the cab side of the firewall to make sure there will be no interference from anything mounted on or near where the pass-through connector will mount.

![[15800031.png]]

After confirming that the position selected is unobstructed, use a 1-1/2-inch hole saw to drill a hole in the firewall. A punch tool can speed the installation.

If necessary, file any loose material out of the hole.

![[15800032.png]]

Install the ICON™ cab harness pass-through connector into the previously drilled hole and install the mounting hardware.

Secure the connector with the provided flat washer and nut.

![[15800039.png]]

Connect the ICON™ engine harness to the cab harness pass-through connector. Connecting the two harnesses together before connecting the under-the-hood components to the ICON™ engine harness will aid in positioning those components properly on the vehicle's firewall.

![[15800040.png]]

Install the ICON™ idle control module on the firewall or other suitable location.

Do **not** install the ICON™ idle control module on the engine or any other location that will expose it to extreme heat.

![[15800033.png]]

Install the engine start alarm in a suitable location on or near the firewall. Orient the alarm so that it is pointing down. This orientation best directs the sound to warn personnel working under the vehicle that the ICON™ system is about to start the engine.

Do **not** install the engine start alarm on the engine or any other location that will expose it to extreme heat.

![[15800034.png]]

Install the starter relay on or near the firewall.

Do **not** install the starter relay on the engine or any other location that will expose it to extreme heat.

![[15800035.png]]

Remove the fuse from the fuse holder connected to the ICON™ engine harness.

![[15800036.png]]

> [!danger] WARNING · Опасно
> Some hood tilt switches contain Mercury, a chemical known to some state and federal agencies to cause birth defects or other reproductive harm. Do not dispose. Recycle in accordance with state regulations.

> [!note] Note · Примечание
> Some non-mercury hood tilt switches can be supplied without a bracket.

Install the hood tilt switch on the vehicle hood. Typically, this switch can be mounted on the back of the head lamp assembly on the left side of the vehicle. Position the switch so that the “wires” end of the switch points down when the hood is closed and points up when the hood is open. The mounting bracket should be perpendicular to the ground when the hood is closed.

It can be necessary to bend the bracket so that the mercury switch touches the side of the bracket that mounts to the head lamp assembly. This configuration will eliminate the possibility of intermittent switch contact.

![[15800037.png]]

Carefully close the vehicle's hood to make sure that none of the ICON™ components interfere with closing the hood.

![[15800038.png]]

Open the hood and attach the ICON™ engine harness to each of the components installed in the engine compartment:

- ICON™ idle control module A and B connectors
- Engine start alarm
- Starter relay
- Hood tilt switch.

Secure all the loose wiring to the vehicle frame with nylon wire ties.

![[15800048.png]]

Close and open the hood to make sure no wires catch on anything protruding from the vehicle.

![[15800038.png]]

> [!note] Note · Примечание
> Volvo Eaton transmissions can have a 5/8-inch or a M16 metric thread neutral position switch (**not** included in the ICON™ system installation kit).

Eaton and Meritor transmissions are equipped with a port for the installation of a neutral position switch. The Eaton transmission typically uses a 9/16-inch normally open switch, and the Meritor transmission typically uses a 3/4-inch normally closed switch.

> [!note] Note · Примечание
> If the vehicle is equipped with another type of transmission, contact the transmission supplier for instructions on the placement of a neutral position switch.

![[15800042.png]]

Remove the boot around the gear shift. Remove the neutral position switch plug from the transmission.

![[15800043.png]]

Install an o-ring on the neutral position switch. Install the neutral position switch into the threaded port.

> [!tip] Момент затяжки · Torque Value
> 20 n•m [15 ft-lb]

Connect the ICON™ engine harness connector to the switch.

![[15800044.png]]

Locate the keyswitch input circuit for the engine ECM. ISM and ISX/Signature engines use pin 38 in the OEM connector. CELECT™ Plus engines use pin 26 in the actuator harness connector. ISX CM870, ISX CM871, ISM CM870, ISM 876, and ISM CM875 use pin 39 in the ECM OEM harness connector.

Refer to the appropriate wiring diagram for the specific pin number that relates to the engine onto which ICON™ system is being installed.

![[15800046.png]]

Disconnect the OEM connector that contains the engine ECM keyswitch input circuit. Cut the wire that leads to the engine ECM keyswitch input circuit pin near the connector. Use the appropriate butt splice, splice the engine ECM keyswitch input circuit wire coming from the connector to the ICON™ idle control module keyswitch input wire in the ICON™ engine harness. Heat-shrink the splice. It may be necessary to trim excess harness length. Connect the connector. Electrically isolate the loose engine ECM keyswitch input wire. Use the appropriate butt splice, crimp one end to the wire and heat-shrink the splice.

Secure the loose keyswitch input wire to the vehicle's engine harness with nylon wire ties.

![[15800047.png]]

Use nylon wire ties to secure all of the loose ICON™ engine harness wires. Make sure the wires do **not** rub against sharp or jagged edges. Make sure the wires do **not** rest against any hot surface that can damage the wire insulation.

![[15800048.png]]

Remove the fuse from the fuse holder connected to the cab harness.

![[15800036.png]]

Connect the cab thermostat jumper harness to the ICON™ cab harness. Route the cab thermostat jumper harness from the cab harness to the bunk area so that it can be connected to the bunk thermostat. Performing this procedure first aids in determining the mounting position for the bunk thermostat. Depending on the OEM, route the harness under the kick panel, or under the interior lining above the driver window, and then under the interior panels to the location in the cab where the hole will be drilled to mount the thermostat. If necessary, remove cab panels, flooring, or other items, to route the harness.

![[15800049.png]]

Find a suitable location to install the cab thermostat. This position **must** be readily accessible to the vehicle operator. The thermostat is typically installed approximately 2 feet over the bunk sleeping surface, or midway between the bunk and the ceiling. It should also be placed out of the direct flow of air from the vehicle heating or air conditioning. Be certain to position the thermostat so that it can **not** be easily damaged and will **not** be accidentally covered by clothing or pillows.

It is recommended that a knife be used to trim the interior enough to allow the drilling of a hole ample enough for the thermostat connectors to be pushed through it, in order to connect the ambient air temperature and cab thermostat jumper harnesses.

![[15800050.png]]

Install the cab thermostat.

Connect the cab thermostat jumper harness to the thermostat.

![[15800050.png]]

Drill a 3/4-inch hole in the floor of the bunk area, preferably under the sleeper bunk pedestal. Route the temperature sensor harness into the cab. Install a grommet to seal the hole around the wire and prevent abrasion. Seal with silicone to prevent exhaust gas from seeping into the cab.

Connect the temperature sensor harness to the cab thermostat.

![[15800059.png]]

Install the ambient air temperature sensor in an area shaded from the sun, but **not** in an area without airflow. Make sure the sensor is protected and is located outside the engine compartment away from engine heat or the exhaust system. A position under the vehicle's fifth wheel is recommended. Fuel tank temperatures can affect ambient temperature sensed by the sensor. Do **not** mount over fuel tanks.

Connect the temperature sensor harness to the ambient air temperature sensor.

> [!note] Note · Примечание
> Do **not** bolt the sensor to secure it.

Use nylon wire ties to secure the sensor and the wiring harness. The sensor should be secured to an air line or wire conduit.

![[15800060.png]]

Remove the dash panel to gain access to the vehicle keyswitch, parking brake air line, optional trailer parking brake air line, and starter button if the vehicle is so equipped.

Route the ICON™ cab harness throughout the dash area so that each connector reaches the appropriate location.

![[15800051.png]]

If the vehicle is equipped with a Pollack electronic dash, it may be necessary to install the optional dash relay (**not** provided in the ICON™ installation kit). For applications other than Pollack, please skip the following steps for installing the dash relay and go to “connecting the ICON™ engine harness battery connectors to the vehicle batteries” step.

Install a 2 Form C relay (double pole/double throw relay) between the electronic dash and the public datalink as follows:

![[15800013.png]]

Find the connector on the dash that connects the J1587 public datalink from the vehicle harness to the dash.

Locate the J1587 public datalink positive (+) wire and negative (-) wire on the dash harness connector and label them.

Cut these wires.

If necessary, splice longer wires to each of the cut wires to allow connection to the relay base.

![[19802944.png]]

| Relay Connections on Dash Harness |  |
|---|---|
| Connector side | Truck side |
| Relay pin 3 to (+) J1587 public datalink | Relay pin 5 to (+) J1587 public datalink |
| Relay pin 4 to (-) J1587 public datalink | Relay pin 6 to (-) J1587 public datalink |

![[19802818.png]]

Use a separate wire, connect pin A (relay coil (+) to pin 30 of the ignition bus 1 relay. Splice into the wire labeled ignition bus 1 - wire 21 (L4) that goes to the OEM cab circuits. This wire is the same wire that was connected to all of the ignition and accessory post wires (the wires removed from the keyswitch).

> [!note] Note · Примечание
> Care **must** be taken to distinguish between the “relay pins” and the “relay base pins.” All instructions above are for “relay pins.”

![[19802818.png]]

Install a separate wire from pin B to a cab ground, use a ring terminal or other appropriate connector.

![[19802818.png]]

Locate the parking brake line connecting the vehicle parking brake push/pull valve to the brake.

To verify that this is the correct line, loosen a fitting on the line and deactivate the vehicle parking brake. Air should continuously bleed off from the loosened fitting.

After verifying that the correct line has been selected, tighten the fitting.

![[15800052.png]]

Activate the brake to remove air pressure from the line. Cut the vehicle parking brake line, and use the fittings supplied to install a tee in the line. Orient the open port on the tee above horizontal. This helps prevent any moisture from becoming trapped in the switch contact area once it is installed. Install the vehicle parking brake switch in the tee to allow the switch to sense the air pressure in the parking brake line.

Connect the ICON™ cab harness to the vehicle parking brake switch.

![[15800053.png]]

Locate the J1587 datalink connector in the vehicle cab.

This connector is typically located on the driver's side of the vehicle under the dash.

![[15800054.png]]

With the 6-pin Deutsch connector, pin A is typically the positive (+) datalink wire, and pin B is typically the negative (-) datalink wire.

With the 9-pin Deutsch connector, pin F is typically the positive (+) datalink wire, and pin G is typically the negative (-) datalink wire.

![[19803464.png]]

Cut the positive (+) and negative (-) datalink wires near the connector. Strip the ends of the wires. Place both ends of the positive (+) datalink wires into the appropriate butt splice. Attach the ICON™ cab harness positive (+) white wire to the positive (+) datalink wires. In the same manner, attach the ICON™ cab harness negative (-) black wire to the negative (-) datalink wires. Heat-shrink the butt splices.

These splices connect the ICON™ datalink wires to the in-cab datalink. This connection is made in such a way that the cab datalink is still connected to the idle control module.

![[15800055.png]]

Mount the ICON™ cab harness ignition bus relay holder(s) near the keyswitch. Make sure the ignition bus 1 and 2 wires will reach wires removed from the keyswitch. Orient the leads pointing down to prevent any moisture from getting into the relays.

Insert the ignition bus 1 relay (40 amperes) into the ignition bus 1 relay holder. This relay allows the ICON™ system to control the application of cab power. This relay is a normally closed relay.

![[15800056.png]]

> [!note] Note · Примечание
> The following procedure shows the four-post style of keyswitch. Your vehicle's configuration can be different. See the charging and starting diagram for the application onto which the ICON™ system is being installed (if different from the procedure shown here).

> [!note] Note · Примечание
> This procedure is necessary to be certain that the ICON™ system can start and stop the engine, as well as turn the in-cab power on and off, at the appropriate time. Some of the cab circuits can initially be connected to the accessory terminal post of the keyswitch (this is **not** recommended). If accessories are connected in this way, the cab power can **not** be removed when the vehicle is being powered down by the ICON™ system, the reason being that the accessory terminal post is hot when the keyswitch is in the ignition and accessory positions. If the operator desires to have manual control of some devices in the cab while the vehicle is powered down by ICON™ system, it will be necessary to hardwire those devices to the keyswitch unswitched battery terminal post instead of the accessory post.

![[15800057.png]]

> [!note] Note · Примечание
> A newer style of keyswitch uses solderless quick-disconnect (blade) connections on the keyswitch. For vehicles with this type of keyswitch, see the charging and starting diagrams for that application to confirm the function of each keyswitch wire.

Remove the keyswitch from the dash.

If equipped, remove the starter button from the dash.

![[15800057.png]]

Tag and then disconnect all of the existing wires (1) from the keyswitch ignition post.

![[15800062.png]]

If the vehicle is equipped with a starter button, connect a wire (2) to supply power to the button directly from the ignition post on the keyswitch, if such a wire is **not** already present.

![[15800063.png]]

If there is only one wire (the wire originally connected to the ignition post of the keyswitch) supplying power to components through the ignition post and accessory post, use the appropriate-size butt splice and attach that wire (1) to the ICON™ cab harness ignition bus 1 wire Number 021 (L4). Heat-shrink the butt splice.

Make sure to use ignition bus 1 wire, wire Number 021, **not** the ignition bus 1 power wire.

![[15800070.png]]

If more than one wire was supplying power to components through the ignition post and the accessory post, a terminal block or other device that allows multiple connections should be used. After making the necessary connections, be sure to seal off and secure the terminal block with electrical tape to prevent accidental contact with the electrical connections. (A terminal block is **not** provided in the ICON™ installation kit.)

![[15800064.png]]

Some installations require a second ignition bus relay (**not** provided in the ICON™ installation kit) to allow the ICON™ system to control additional circuits. (If needed, this relay is installed the same as the first ignition bus relay, and connected to the cab harness ignition bus 2 holder position.)

Make sure to use ignition bus 2 wire, wire Number 022 (L5), **not** the ignition bus 2 power wire.

As a rule, if there are multiple wires connected to the ignition post and the accessory post, the wire loads should be evenly distributed between ignition bus 1 and 2 relay circuits. Ignition bus 2 (wire Number 022 (L5)) will be connected to half of the cab circuit load wires removed from the ignition post and the accessory post. Ignition bus 1 (wire Number 021 (L4)) will be connected to the other half. These relays are normally closed relays.

![[15800002.png]]

Remove the wire (4) connecting the starter post on the keyswitch to the starter magnetic switch.

If the vehicle is equipped with a starter button, remove the wire (4) connecting the starter button to the starter magnetic switch.

![[15800065.png]]

Connect the ICON™ cab harness starter terminal wire Number 018 (T3) to the starter post or to the starter button (if equipped).

![[15800071.png]]

Use the appropriate-size butt splice, attach the wire (4) from the magnetic switch that was removed from the starter post or the starter button to the ICON™ cab harness magnetic switch power wire Number 017 (L3). This splice connects the magnetic switch to pin 30 on the starter relay. Heat-shrink the butt splice.

> [!note] Note · Примечание
> The starter relay is a normally open relay.

![[15800066.png]]

Attach the ICON™ cab harness keyswitch ignition pickup wire Number 020 (T5) to the ignition post on the keyswitch.

![[15800067.png]]

Attach the ICON™ cab harness starter power wire Number 019 (T4) to the battery post (unswitched battery) on the keyswitch.

![[15800068.png]]

Attach the ICON™ cab harness ignition bus 1 power wire Number 023 (T6) to the ignition post on the keyswitch (switched battery). If a second relay is installed, attach the cab harness ignition bus 2 power wire Number 024 (T7) to the ignition post on the keyswitch (switched battery). These wires provide power to the ignition bus relays.

Install the keyswitch and starter button in their original OEM location.

![[15800069.png]]

Find a visible location on the vehicle dash for the ICON™ lamp. Make sure that the chosen location is one that is **not** subject to be easily kicked or hit. Drill a 11/16-inch hole in the dash.

Remove the lamp cover and nut from the housing.

With the star washer still on the housing, insert it through the hole in the dash.

Install and tighten the nut to hold the housing in position. Install the lamp cover.

Attach the ICON™ cab harness to the lamp.

Tape any exposed wires and secure all wiring to the vehicle, use nylon wire ties. Make sure that none of the wiring is binding and that there is no tension on the lamp wires that lead to the lamp connector.

![[15800058.png]]

Connect the ICON™ engine harness battery connectors to the batteries. Connect the positive (+) ring terminal (red wire) wire Number 013 (T1) to the positive (+) battery connector first. Then connect the negative (-) ring terminal (black wire) wire Number 003 (T2) to the negative (-) battery connector.

> [!note] Note · Примечание
> For the ICON™ system to work properly, these connectors **must** be directly attached to the batteries. Do **not** attach them to the engine block ground or the positive (+) starter motor post.

![[15800045.png]]

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To avoid personal injury, always ventilate the compartment before servicing the batteries. To avoid arcing, remove the negative (-) battery cable first and attach the negative (-) cable last.

Connect the vehicle battery terminals to the vehicle batteries.

![[ea8coha.png]]

Install the fuse into the fuse holder on the ICON™ cab harness.

Reassemble all of the panels, flooring, or other components that were removed for this installation.

Install the fuse into the fuse holder on the ICON™ engine harness.

![[15800036.png]]

Install the provided warning labels to the vehicle. The labels **must** be installed in a prominent location to alert the operator and maintenance personnel around the vehicle of the potential hazards of the ICON™ system. These labels are typically installed on the charge air piping.

The operating instructions label should be placed in the vehicle cab on the dash where it can be easily seen by the operator.

![[15800061.png]]

Use INSITE™ electronic service tool to disable the following engine features:

- Idle shutdown
- Idle shutdown override enable
- Idle shutdown in PTO enable
- Ambient air temperature idle shutdown override
- Any automatic antitheft devices.

The ICON™ system is incompatible with the features listed above. All of these features **must** be disabled before activating the ICON™ system.

![[19400357.png]]

Perform the charging system test before performing the checkout test in the following steps. See the General Information step at the beginning of this procedure.

![[nobox.png]]

Once the ICON™ system has been installed, perform the following steps to confirm that the system is working properly. Refer to the ICON™ Operation and Maintenance Manual, Bulletin [[3666422 — ICON™ Idle Control System\|3666422]], Fault Code Notification, for the fault code flashout procedure.

- Turn the keyswitch on, engine **not** running. ICON™ lamp should turn on for 3 seconds, pulsing once per second. If **not**, troubleshoot symptoms. Refer to Procedure 019-087 in Section 19.
- For unswitched battery circuit and ICON™ lamp circuit. Refer to Procedure 019-047 in Section 19.

![[19803448.png]]

- Turn the keyswitch on, engine **not** running. Ignition bus power should come on. If **not**, check for correct wiring of the ignition bus relay or troubleshoot active fault code, if present. See Section TS, Troubleshooting Symptom Tree T095-155.

![[19803449.png]]

- Turn the keyswitch off, engine **not** running. Ignition bus power should stay off. If **not**, check for correct wiring of the ignition bus relay. See Section TS, Troubleshooting Symptom Tree T095-125.

![[19803450.png]]

- Turn keyswitch on. Start vehicle. Vehicle should start and run normally. If vehicle does **not** crank, check for correct wiring of the starter relay circuit or see Section TS, Troubleshooting Symptom Tree T078. If vehicle does crank but does **not** start, check for correct wiring of the keyswitch input circuit into the ICON™ idle control module, or the keyswitch input circuit into the engine ECM, or see Section TS, Troubleshooting Symptom Tree T078. Troubleshoot active fault code, if present.

![[19803451.png]]

- Check the mandatory shutdown mode shutdown time. Refer to the ICON™ Operation and Maintenance Manual, Bulletin [[3666422 — ICON™ Idle Control System\|3666422]]. Start the engine normally. Do **not** activate ICON™. Time the engine shutdown. The shutdown time is as follows:
- Revision level 11, 13, and 14: default is 5 or 15 minutes, adjustable up to two hours.
- Revision level 15: default is 10 minutes, adjustable up to two hours.
- Revision level 16: default is 5 minutes, adjustable up to two hours.
- Revision level 18: default is 5 minutes with zero vehicle speed and parking brake engaged, 15 minutes with zero vehicle speed and parking brake **not** engaged.
- Revision level 19: default is 3 minutes with zero vehicle speed and parking brake engaged, 15 minutes with zero vehicle speed and park brake **not** engaged.

If needed, check the cab thermostat trim settings to make sure the short idle enable trim is **not** selected unless a 5-minute idle shutdown time is desired. [[97-018-025 — ICON™ System|Refer to Procedure 018-025 in Section V]]. This helps make sure the batteries are fully charged before performing the rest of the procedure.

![[19803452.png]]

- Turn keyswitch on.
- Activate the ICON™ system. Refer to the ICON™ Operation and Maintenance Manual, Bulletin [[3666422 — ICON™ Idle Control System\|3666422]]. Keep thermostat off. Keep keyswitch on. Engine oil temperature should be above the maximum specification and the battery post voltage above the maximum OEM specification, when the engine is running. If the ICON™ system does **not** activate, see Section TS, Troubleshooting Symptom Tree T095.

![[19803453.png]]

Once activated in engine mode (reference the ICON™ Operation and Maintenance Manual, Bulletin [[3666422 — ICON™ Idle Control System\|3666422]]), perform the following:

Interlock Check - Before first auto-shutdown, opening an interlock should deactivate the ICON™ system and shut down the engine.

- Open hood - ICON™ system deactivates, engine shuts down.

![[19803454.png]]

- Release parking brake - ICON™ system deactivates, engine shuts down.

![[19803455.png]]

- Place transmission in gear - ICON™ system deactivates, engine shuts down.

![[19803456.png]]

Time the auto-shutdown of the engine. The time period from the moment the ICON™ system is activated until the engine shuts off for the first time should be 1 minute. If it is longer than 5 minutes, make sure the engine oil temperature is above the maximum specification and battery post voltage is above the maximum OEM specification. The ICON™ lamp should remain on pulsing at a rate of once per second. At this point if the ICON™ lamp turns off, check for active fault codes and troubleshoot accordingly. If the battery voltage is **not** above these levels, the ICON™ system will run the engine for at least 1 hour, or until the battery voltage reaches these levels.

![[19803457.png]]

Wait 10 minutes after the shutdown. This waiting period prevents generating an E3 fault. With the engine shut down from step 2 and the ICON™ system active, turn on the cab thermostat and activate cab comfort mode. No faults should display. If Fault Code E1, E2, or E3 is displayed, troubleshoot Fault Code 469, if present, or see Section TS, Troubleshooting Symptom Tree T015. Refer to the ICON™ Operation and Maintenance Manual, Bulletin [[3666422 — ICON™ Idle Control System\|3666422]], Cab Comfort Mode Activation and Function. Enable the heat or cool mode. Adjust the set points and heat or cool mode appropriately to force an engine start. For example, this will be above cool set point and range set, or below heat set point and range set. Check that the alarm sounds before the ICON™ system starts the engine. The heat or cool indicator should start to flash and the engine should perform an engine start. Once the engine is started and the set point is reached, the engine speed should ramp down and the engine should shut off. If **not**, check the thermostat signal circuit. [[97-019-309 — Thermostat Signal Circuit|Refer to Procedure 019-309 in Section 19]]. Also, see Section TS, Troubleshooting Symptom Tree T015-1.

![[19803458.png]]

Turn keyswitch off. For applications that will use engine mode keyless operation, activate the ICON™ system in keyless engine mode. Refer to the ICON™ Operation and Maintenance Manual, Bulletin [[3666422 — ICON™ Idle Control System\|3666422]]. Keep the thermostat off. Turn the keyswitch off prior to the first auto-shutdown. Keep the fan blowers on the maximum setting. Engine oil temperature should be above the maximum specification and battery voltage above the OEM specification, when the engine is running. The ignition bus electrical circuits should **not** turn off when the keyswitch is turned off. If this happens, check for correct wiring of the ignition bus relay at the keyswitch.

![[19803447.png]]
