---
type: "Процедура"
doc: "35-008-069-tr"
title_en: "Wiring Harness, Cummins Electric Fan Clutch"
modified: "2009-01-23"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "3666322"
figures: 33
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/35/35-008-069-tr.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/35-008-069-tr.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/35"
---

# Wiring Harness, Cummins Electric Fan Clutch

> [!abstract] Процедура · `35-008-069-tr`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[3666322 — ISM, ISMe, and QSM11 Service Manual|3666322]]
> **Секции:** Section 8 - Cooling System - Group 08
> **Даты:** изменён 2009-01-23
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/35/35-008-069-tr.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/35-008-069-tr.pdf)

### General Information

This procedure applies to engines using an electric fan clutch controlled by the ECM and utilizing a Cummins® electric fan clutch wiring harness. If the wiring harness is **not** a Cummins® electric fan clutch wiring harness, refer to the OEM service manual for the correct troubleshooting procedure.

![[08200050.png]]

### Initial Check

For the fan to operate, the Cummins® electromagnetic fan clutch relay **must** receive a 12-VDC signal from the ECM to engage and a 0-VDC signal from the ECM to disengage the fan clutch. Be sure the correct electrical connections have been made.

Inspect the wires and harness to be sure none are broken or shorted. Replace the harness or wires that are broken.

![[wr2cnkb.png]]

The fan clutch will engage when it receives 12-VDC from the fan clutch relay and disengage when it receives 0- VDC from the fan clutch relay.

![[08200055.png]]

The 12-VDC is supplied from the vehicle's electrical system to the fan by one of three possible controls:

- The manual fan on/off switch (1) in the cab
- The refrigerant compressor pressure switch (2)
- The temperature switch (3) in the thermostat housing.

![[08200033.png]]

To check to be sure there are no open circuits, the continuity **must** be checked between the following pins of the wiring harness:

- Pin B of the fan clutch connector (1) and the ground terminal (2)

![[08200035.png]]

- Pin A of the fan clutch connector (1) and the following fan harness connectors:

- Pin A of the temperature switch connector (2)
- Pin B of the refrigerant compressor pressure switch connector (3)
- Pin B of the manual on/off cab switch connector (4).

![[08200036.png]]

- The positive (+) 12-VDC terminal (1) and the following fan harness connectors:

- Pin B of the temperature switch connector (2)
- Pin A of the refrigerant compressor pressure switch connector (3)
- Pin A of the manual on/off cab switch connector (4).

The multimeter **must** read a closed circuit (10 ohms or less). Repair or replace the harness if more than 10 ohms is detected on any of the above checks.

![[08200038.png]]

Check for short circuits in the harness. The resistance **must** be greater than 100K ohms for the following:

- Pin A of the fan clutch connector (1) to the ground terminal (2)

![[08200040.png]]

- The ground terminal (1) and the following fan harness connectors:

- Pin A of the temperature switch connector (2)
- Pin B of the refrigerant compressor pressure switch connector (3)
- Pin B of the manual on/off cab switch connector (4).

![[08200041.png]]

- The positive (+) 12-VDC terminal (1) to the ground terminal (2)

![[08200042.png]]

- The positive (+) 12-VDC supply (1) and the following fan harness connectors:

- Pin A of the temperature switch connector (2)
- Pin B of the refrigerant compressor pressure switch connector (3)
- Pin B of the manual on/off cab switch connector (4).

![[08200043.png]]

- Pin A of each of the three switch connectors (1) to pin B of each of the three switch connectors (1).

The harness **must** be repaired or replaced if any of the above resistances are less than 100 ohms.

![[08200044.png]]

To check the temperature switch (1) for proper operation, check the continuity from pin A to pin B at room temperature (**must** be greater than 100 ohms). Replace the switch if the resistance is less than 100K ohms.

![[08200045.png]]

To check the temperature switch for operation at the fan ON temperature, place the probe (1) in a container of water, along with a thermometer.

![[08200046.png]]

Place the multimeter probes in pin A and pin B.

![[08200047.png]]

Heat the water.

Note the temperature at which the resistance changes from 100 or greater ohms to 10 ohms or less.

![[08200048.png]]

If the switch does **not** close at the temperature required according to the switch manufacturer, the switch **must** be replaced.

![[08200049.png]]

To check the freon compressor pressure switch and the manual fan on/off cab switch, refer to the manufacturer's recommendations.

![[08200051.png]]

### Remove

Disconnect the operator-controlled manual switch harness, if used, from the base harness.

![[08200039.png]]

Remove the refrigerant pressure switch harness from the base harness.

![[08200037.png]]

Disconnect the gray harness connector from the temperature switch in the thermostat housing.

![[08200007.png]]

Disconnect the large ring terminal with the black wire from the chassis ground.

![[08200005.png]]

Disconnect the small ring terminal from the power source.

![[08200053.png]]

Disconnect the fan clutch connector on the base harness from the fan clutch.

![[ea200hd.png]]

### Install

Connect the fan clutch connector on the base harness to the fan clutch.

![[ea200hd.png]]

Connect the small ring terminal with the red wire to an ignition switch-controlled fused power source.

![[08200054.png]]

Connect the large ring terminal with the black wire to the chassis ground.

![[08200005.png]]

Install the coolant temperature switch in the thermostat housing, if it was removed.

![[08200004.png]]

Connect the gray harness connector to the temperature switch in the thermostat housing.

![[08200007.png]]

On air-conditioned vehicles, install the appropriate refrigerant pressure switch into the compressor outlet side of the refrigerant circuit, if it was removed.

![[08200006.png]]

Connect the switch harness to the base harness and to the refrigerant pressure switch.

![[08200014.png]]

Connect the operator-controlled manual switch harness to the base harness.

![[08200015.png]]

Leave the base harness switch connector sealing cap(s) in place if a refrigerant pressure switch or an operator-controlled manual switch is **not** used.

![[08200012.png]]
