---
type: "Процедура"
doc: "97-019-305"
title_en: "Cab Wiring Harness"
modified: "2007-02-06"
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
figures: 39
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-019-305.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-019-305.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "двигатель/QSX15"
  - "группа/97"
---

# Cab Wiring Harness

> [!abstract] Процедура · `97-019-305`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSM11, QSX15
> **Входит в руководства:** [[3666415 — ICON Idle Control System Master Repair Manual|3666415]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2007-02-06
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-019-305.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-019-305.pdf)

### Remove

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To avoid personal injury, always ventilate the compartment before servicing the batteries. To avoid arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

Turn the keyswitch to the OFF position. Disconnect the vehicle battery cables from the battery. Disconnect the ICON™ battery harness connectors from the battery.

> [!note] Note · Примечание
> Disconnecting the vehicle battery connections can require that the engine ECM real-time clock be reset, use INSITE™ electronic service tool.

![[ea8coha.png]]

Remove the fuse from the fuse holder on the cab harness.

![[15800036.png]]

Disconnect the ICON™ engine harness 14-pin pass-through connector from the mating cab harness connector at the vehicle's bulkhead.

![[15800040.png]]

Disconnect the cab thermostat jumper harness from the cab harness.

![[15800049.png]]

Remove the dash panel to gain access to the vehicle keyswitch, starter button (if vehicle is so equipped), parking brake switch connector, and ICON™ lamp connector.

![[15800051.png]]

> [!note] Note · Примечание
> Wires designated by a number are also shown in the wiring diagram for more detail.

Cut the cab harness datalink wires where they are spliced to the J1587 datalink wires, use wire crimping pliers, Part Number 3822930. These are wires Number 7 and Number 8.

![[15800055.png]]

Disconnect the parking brake switch from the cab harness.

![[19802872.png]]

Disconnect the ICON™ lamp from the cab harness.

![[19c00926.png]]

Remove the ignition bus relay(s) from the ignition bus relay holder.

Remove the screw securing the ignition bus relay holder in position under the dashboard.

![[15800056.png]]

Remove the keyswitch assembly from the dashboard.

Remove the starter button, if the vehicle is so equipped, from the dashboard.

![[15800057.png]]

If two ignition bus relays are installed, remove the cab harness ignition bus 2 power wire Number 24 (9) from the battery post in the keyswitch assembly. Remove the cab harness ignition bus 1 power wire Number 23 (10) from the battery post in the keyswitch assembly. Wiring for each different revision of module should be included.

![[15800069.png]]

Remove the cab harness starter power wire Number 19 (8) from the battery post in the keyswitch assembly.

![[15800068.png]]

Remove the cab harness keyswitch ignition pickup wire Number 6 (7) from the ignition post in the keyswitch assembly.

![[15800067.png]]

Cut the cab harness magnetic switch power wire that has been spliced to the vehicle magnetic switch wire Number 17, use wire crimping pliers, Part Number 3822930.

![[19802890.png]]

Remove the cab harness starter terminal wire Number 18 (5) from the starter post (or starter button) in the keyswitch assembly.

![[15800071.png]]

If the cab harness ignition bus relay wire Number 21 has been spliced to the single wire Number 22 that supplied power to vehicle components, cut the spliced cab harness wire, use wire crimping pliers, Part Number 3822930. If a terminal block has been used for connecting multiple wires, remove the electrical tape sealing the connections and disconnect all wires connected to the terminal block.

![[19802890.png]]

Remove the flat washer and nut securing the cab harness 14-pin pass-through connector to the vehicle's firewall.

Remove the cab harness.

![[15800039.png]]

### Install

Turn the keyswitch to the OFF position.

Make sure the fuse is removed from the fuse holder on the cab harness.

![[15800036.png]]

Install the cab harness 14-pin pass-through connector into the hole in the vehicle's firewall.

Use the flat washer and nut, secure the connector to the vehicle's firewall.

![[15800039.png]]

Coat the electrical connectors with lubricant DS-ES, Part Number 3822934, or equivalent, prior to connecting any of the electrical components. This lubricant prevents corrosion, enabling good electrical contact.

![[19800495.png]]

Connect the ICON™ engine harness 14-pin pass-through connector to the mating cab harness connector at the vehicle's firewall.

![[15800040.png]]

Connect the cab thermostat jumper harness to the cab harness.

![[15800049.png]]

Connect the parking brake switch to the cab harness.

![[19802872.png]]

Connect the ICON™ lamp to the cab harness.

![[19c00926.png]]

Splice the cab harness datalink wires to the mating J1587 datalink wires (cab harness positive (+) white wire to datalink positive (+) wire and cab harness negative (-) black wire to datalink negative (-) wire).

Heat-shrink the butt splices.

![[15800055.png]]

Mount the ignition bus relay holder(s) near the keyswitch by installing the screw securing the ignition bus relay holder in position under the dash.

Insert the ignition bus relay(s) into the holder.

![[15800056.png]]

If the cab harness ignition bus relay wire had been spliced to the single wire that supplied power to vehicle components, use the appropriate-size butt splice and splice these two wires together, use wire crimping pliers, Part Number 3822930.

Heat-shrink the butt splice.

![[19802891.png]]

If there are multiple wires supplying power to components through the ignition post, make all the connections, use a terminal block.

Seal off all the connections with electrical tape to prevent accidental contact with the electrical connections.

![[15800064.png]]

Connect the cab harness starter terminal wire Number 018 (5) to the starter post (or starter button) in the keyswitch assembly.

![[15800071.png]]

Splice the cab harness magnetic switch power wire Number 017 to the vehicle magnetic switch wire, use wire crimping pliers, Part Number 3822930.

Heat-shrink the butt splice.

![[19802891.png]]

Attach the cab harness keyswitch ignition pickup wire Number 020 (7) to the ignition post in the keyswitch assembly.

![[15800067.png]]

Attach the cab harness starter power wire Number 019 (8) to the battery post in the keyswitch assembly.

![[15800068.png]]

Attach the ICON™ cab harness ignition bus 1 power wire number 023 (10) to the ignition post on the keyswitch (switched battery).

If two ignition bus relays are installed, attach the cab harness ignition bus 2 power wire Number 024 (9) to the ignition post in the keyswitch switched battery.

![[15800069.png]]

Install the keyswitch and starter button (if applicable) in their original locations.

![[15800057.png]]

Install the dash panel that was removed to gain access to under dashboard components.

![[15800051.png]]

Install the fuse into the fuse holder on the cab harness.

![[15800036.png]]

### Convert

To determine if the ICON™ system needs to be converted from unswitched battery to keyswitch for the ignition bus relay circuit, perform the following test.

Turn the keyswitch OFF.

Turn the blower switch ON.

If the blowers are operating with the keyswitch OFF then the cab wiring harness **must** be converted as follows.

![[nobox.png]]

Remove the ignition bus power 1 (9) and ignition bus power 2 (10) from the unswitched battery post of the keyswitch assembly.

![[15800069.png]]

Install the ignition bus power 1 (7) and ignition bus power 2 (8) to the ignition post of the keyswitch assembly.

![[19803847.png]]
