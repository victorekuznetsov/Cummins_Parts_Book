---
aliases:
  - "Жгут проводов Centinel™"
type: "Процедура"
doc: "96-019-131"
title_en: "Centinel™ Wiring Harness"
title_ru: "Жгут проводов Centinel™"
modified: "2004-05-10"
engines:
  - "37292556"
  - "37295879"
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
  - "QST30"
manuals:
  - "3666231"
figures: 124
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/96/96-019-131.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/96-019-131.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "двигатель/QST30"
  - "группа/96"
---

# Centinel™ Wiring Harness
**Жгут проводов Centinel™**

> [!abstract] Процедура · `96-019-131`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]], [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11, QST30
> **Входит в руководства:** [[3666231 — Centinel™ Master Repair Manual|3666231]]
> **Секции:** Section G - Installation Guidelines
> **Даты:** изменён 2004-05-10
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/96/96-019-131.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/96-019-131.pdf)

### Install

Burn-Only, L and M Series Engines

It will be necessary to choose a location for mounting the heavy-duty Centinel™ control module. Location of the Centinel™ control module should provide visibility of the diagnostic lamps to operators and maintenance personnel.

Recommended locations include:

- Inside the cab
- On the frame rail
- On the rear of the cab.

> [!note] Note · Примечание
> Do **not** mount the Heavy-Duty Centinel™ control module under the hood or in the engine compartment. The Centinel™ control module is **not** designed (or covered by warranty) for engine compartment temperatures.

![[nobox.png]]

> [!note] Note · Примечание
> Complete the installation of the wiring harness before using p-clamps or tie wraps to secure the wiring harness from rubbing.

Locate and remove the Centinel™ wiring harness from the package.

> [!note] Note · Примечание
> When connecting the harness to the Centinel™ control module, verify that the connector locks are engaged.

Install the 12-pin connector to the Centinel™ control module.

![[05100036.png]]

Locate the three oil monitoring plugs in the package. **Only** one of the plugs will be installed, depending on the type of oil to be used in the engine.

1. Standard oil monitoring plug - white wire
2. Advanced oil monitor plug - black wire
3. Service plug - red wire.

> [!note] Note · Примечание
> The service plug is used to place the installed Centinel™ system into service and to reset the system after an oil change.

![[05100038.png]]

Remove the cover from the oil monitoring plug on the Centinel™ wiring harness and install the appropriate calibration plug.

Install the appropriate calibration plug.

> [!note] Note · Примечание
> Refer to Procedure [[96-018-003 — Lubricating Oil Recommendations and Specifications|018-003]] for engine specific blend rates.

![[05100039.png]]

Route the Centinel™ wiring harness to the frame rail opposite the exhaust and forward to the oil control valve.

Secure the harness from rubbing using P-clamp and tie wraps.

![[17800019.png]]

Locate the connector labeled BURN SOLENOID and connect it to the connector on the top of the oil control valve leading to the burn solenoid.

![[05100041.png]]

Locate the connector labeled MAKE-UP SOLENOID and connect it to the connector on the top of the oil control valve leading to the make-up solenoid.

![[05100040.png]]

> [!note] Note · Примечание
> This step applies to engines equipped with the CELECT™ Plus system **only**. For non-CELECT™ Plus engines, continue to the next step.

Near the engine ECM, locate and remove the cover from the engine datalink connector.

Install the connector labeled DIAGNOSTIC LAMP ENGINE DATALINK CONNECTOR.

![[05100043.png]]

Drill a 1/4-inch hole in a location on the firewall of the engine compartment.

Install the grommet provided in the kit and route the wires through it and into the cab.

![[17800024.png]]

For engines that do **not** have a 6-pin datalink connector by the ECM, it is necessary to install two wires for the datalink inside the cab. These wires will be spliced into the J1587 datalink connector. These will be the same wires that are routed to the datalink, usually located under the dashboard. Locate the wires that lead to this connector and connect as specified in the following table:

| Signal | 8-Pin Connector | 6-Pin Connector | 2-Pin Connector |
|---|---|---|---|
| Datalink (+) | Pin 1 | Pin A | Pin A |
| Datalink (-) | Pin 2 | Pin B | Pin B |

![[05100044.png]]

Splice the wires using the above table as a reference (polarity).

Butt splices are designed to provide the best possible cold joint connection when properly crimped.

![[17800025.png]]

> [!warning] CAUTION · Осторожно
> Overheating of the butt splice can lead to wire damage.

Butt splices also provide protection against corrosion. After crimping the connection, heat the shrink tube with a heat gun until the shrink tube has sealed the joint.

![[17800026.png]]

> [!note] Note · Примечание
> It is very important that the Centinel™ system be properly grounded.

Locate the black lead (ground) on the Centinel™ wiring harness.

Connect the ground lead to ground on the starter (2).

Connect the red lead (positive) of the harness to the positive post (1) of the starter solenoid.

![[05100046.png]]

Connect the last remaining wire on the Centinel™ harness to the positive post on fuel shutoff solenoid.

> [!note] Note · Примечание
> Inspect all the wiring and plumbing lines to make certain your connections and clamps are tight, and all components are secured from rubbing.

![[05100053.png]]

On the Centinel™ wiring harness, locate the two wire connectors labeled LOW OIL LEVEL SENSOR. Cap the connector with the jumper harness found in the burn-only conversion kit.

> [!note] Note · Примечание
> The burn-only Centinel™ system uses the same harness as the standard Centinel™ system. As the standard system uses a make-up oil tank with a low oil level switch/sensor, in the burn-only system this sensor pickup in the harness **must** be jumped (to simulate a tank with adequate make-up oil) for the Centinel™ control module to operate the system properly.

![[07800058.png]]

> [!note] Note · Примечание
> The Centinel™ wiring harness is about 20 feet long. Depending on where the Centinel™ control module or lamp box is located, there can be a considerable length of excess harness. This excess **must** be rolled together and securely tie-wrapped out of the way.

![[07800059.png]]

Burn With Make-Up, L and M Series Engines

> [!note] Note · Примечание
> Complete the installation of the wiring harness before using p-clamps or tie wraps to secure the wiring harness from rubbing.

Locate and remove the Centinel™ wiring harness from the package.

> [!note] Note · Примечание
> When connecting the harness to the Centinel™ control module, verify that the connector locks are engaged.

Install the 12-pin connector to the Centinel™ control module.

![[05100036.png]]

Use p-clamps to secure the harness to the make-up oil tank.

![[17800020.png]]

Locate the connection on the wiring harness labeled MAKE-UP TANK sensor and connect it to the make-up tank sensor.

![[05100037.png]]

Locate the three oil calibration plugs in the package. **Only** one of the plugs will be installed, depending on the type of oil to be used in the engine.

1. Standard oil monitoring plug - white wire
2. Advanced oil monitor plug - black wire
3. Service plug - red wire.

> [!note] Note · Примечание
> The service plug is used to place the installed Centinel™ system into service and to reset the system after an oil change.

![[05100038.png]]

Remove the cover from the oil monitoring plug on the Centinel™ wiring harness and install the appropriate calibration plug.

> [!note] Note · Примечание
> Refer to Procedure [[96-018-003 — Lubricating Oil Recommendations and Specifications|018-003]] for engine specific blend rates.

![[05100039.png]]

Route the Centinel™ wiring harness to the frame rail opposite the exhaust and forward to the oil control valve.

Secure the harness from rubbing using P-clamp and tie wraps.

![[17800019.png]]

Locate the connector labeled BURN SOLENOID and connect it to the connector on the top of the oil control valve leading to the burn solenoid.

![[05100041.png]]

Locate the connector labeled MAKE-UP SOLENOID and connect it to the connector on the top of the oil control valve leading to the make-up solenoid.

![[05100040.png]]

> [!note] Note · Примечание
> This step applies to engines equipped with the CELECT™ Plus system **only**. For non-CELECT™ Plus engines, continue to the next step.

Near the engine ECM, locate and remove the cover from the engine datalink connector.

Install the connector labeled DIAGNOSTIC LAMP ENGINE DATALINK CONNECTOR.

![[05100043.png]]

Drill a 1/4-inch hole in a location on the firewall of the engine compartment.

Install the grommet provided in the kit and route the wires through it into the cab.

![[17800024.png]]

For engines that do **not** have a 6-pin datalink connector by the ECM, it is necessary to install two wires for the datalink inside the cab. These wires will be spliced into the J1587 datalink connector. These will be the same wires that are routed to the datalink, usually located under the dashboard. Locate the wires that lead to this connector and connect as specified in the following table:

| Signal | 8-Pin Connector | 6-Pin Connector | 2-Pin Connector |
|---|---|---|---|
| Datalink (+) | Pin 1 | Pin A | Pin A |
| Datalink (-) | Pin 2 | Pin B | Pin B |

![[05100044.png]]

Splice the wires using the above table as a reference (polarity).

Butt splices are designed to provide the best possible cold joint connection when properly crimped.

![[17800025.png]]

> [!warning] CAUTION · Осторожно
> Overheating of the butt splice can lead to wire damage.

Butt splices also provide protection against corrosion. After crimping the connection, heat the shrink tube with a heat gun until the shrink tube has sealed the joint.

![[17800026.png]]

> [!note] Note · Примечание
> It is very important that the Centinel™ system be properly grounded.

Locate the black lead (ground) on the Centinel™ wiring harness.

Connect the ground lead to ground on the starter (2).

Connect the red lead (positive) of the harness to the positive post (1) of the starter solenoid.

![[05100046.png]]

Connect the last remaining wire on the Centinel™ harness to the positive post on fuel shutoff solenoid.

> [!note] Note · Примечание
> Inspect all the wiring and plumbing lines to make certain your connections and clamps are tight, and all components are secured from rubbing.

![[05100053.png]]

Burn-Only, ISM Engines

Install the Centinel™ jumper harness between the engine harness (6-pin connector) and the control valve solenoid (2-pin connector).

Verify that the connector locks are engaged.

> [!note] Note · Примечание
> For burn-only, pins 24 and 25 of the 31-pin OEM connector **must** be jumped to simulate adequate oil is available in the make-up tank, even though there is **no** make-up tank.

Locate the jumper wiring harness in the burn-only valve and mounting or conversion kit.

Locate the 31-pin OEM interface connector on the side of the engine block.

![[07800085.png]]

Disconnect the 31-pin OEM connector. Locate pins 24 and 25 in the OEM interface connector, and remove the connector cavity plugs in the 24- and 25-pin locations.

Install the two female sockets of the jumper harness (supplied in the kit) into pins 24 and 25.

> [!note] Note · Примечание
> Make certain the sockets "snap" solidly into place.

Reconnect the OEM 31-pin connector, making absolutely certain the connector is solidly locked in place.

Use provided tie wraps to secure the remainder of the oil make-up level sensor leads to avoid chafing and to make sure **no** stress is applied to the pin sockets.

![[07800175.png]]

Properly reinstall any Cummins or customer hardware that was removed or relocated because of interference.

![[nobox.png]]

Burn With Make-Up, ISM Engines

Install the Centinel™ jumper harness between the engine harness (6-pin connector) and the control valve solenoid (2-pin connector).

Verify that the connector locks are engaged.

![[07800085.png]]

Insert the oil level sensor connector into the oil level sensor installed in the oil make-up tank.

Verify that the connector locks are engaged.

![[05100037.png]]

Butt-splice two number 16-gauge wires (**not** furnished with the kit) in the two oil level sensor connector butt splices.

Use a heat gun, or equivalent, to heat the butt splices to shrink and seal the connections.

![[17800026.png]]

Route the two wires along the make-up hose to the 31-pin OEM interface connector.

Use the provided tie wraps to secure the make-up hose and wires to the frame rail.

![[17800019.png]]

Cut the wires to size and butt-splice appropriate female socket connectors (Cummins Part Number 3822921 - **not** furnished with the kit) to the number 16-gauge wires.

> [!note] Note · Примечание
> Cummins Part Number 3822921 is a common repair item found in the Cummins harness repair kit(s).

![[07800086.png]]

Disconnect the 31-pin OEM connector. Locate pin locations 24 and 25 and remove their cavity plugs.

Install the two female sockets into pins 24 and 25.

> [!note] Note · Примечание
> Make sure the sockets "snap" securely into place.

![[07800087.png]]

Connect the 31-pin OEM connector, making sure the connector is securely locked in place.

Use the provided tie wraps to secure the remainder of the oil make-up level sensor leads to avoid chafing and to make sure no stress is applied to the pin sockets.

![[07800088.png]]

Properly reinstall any Cummins or customer hardware that was removed or relocated as interference.

![[nobox.png]]

N14 Engines

> [!note] Note · Примечание
> The following step is for N14 CELECT™ and CELECT™ Plus engines with **Burn-Only** applications.

It will be necessary to choose a location for mounting the heavy-duty Centinel™ control module. Location of the Centinel™ control module should provide visibility of the diagnostic lamps to operators and maintenance personnel.

Recommended locations include:

- Inside the cab
- On the frame rail
- On the rear of the cab.

> [!note] Note · Примечание
> Do **not** mount the heavy-duty Centinel™ control module under the hood or in the engine compartment. The Centinel™ control module is **not** designed (or covered by warranty) for engine compartment temperatures.

![[nobox.png]]

Use p-clamps to secure the harness to the make-up oil tank.

![[17800020.png]]

Locate and connect the connection on the wiring harness labeled LOW OIL LEVEL SENSOR.

![[05100037.png]]

> [!note] Note · Примечание
> The following steps are for N14 CELECT™ and CELECT™ Plus engines with **Burn-Only** or **Burn With Make-Up** applications.

> [!note] Note · Примечание
> Complete the installation of the wiring harness before using p-clamps or tie wraps to secure the wiring harness from rubbing.

Locate and remove the Centinel™ wiring harness from the package.

> [!note] Note · Примечание
> When connecting the harness to the Centinel™ control module, verify that the connector locks are engaged.

Install the 12-pin connector to the Centinel™ control module.

![[05100036.png]]

Locate the three oil monitoring plugs in the package. **Only** one of the plugs will be installed, depending on the type of oil to be used in the engine.

1. Standard oil monitoring plug - white wire
2. Advanced oil monitor plug - black wire
3. Service plug - red wire.

> [!note] Note · Примечание
> The service plug is used to place the installed Centinel™ system into service and to reset the system after an oil change.

![[05100038.png]]

Remove the cover from the oil monitoring plug on the Centinel™ wiring harness and install the appropriate calibration plug.

> [!note] Note · Примечание
> Refer to Procedure [[96-018-003 — Lubricating Oil Recommendations and Specifications|018-003]] for engine specific blend rates.

![[05100039.png]]

Route the Centinel™ wiring harness to the frame rail opposite the exhaust and forward to the oil control valve.

Secure the harness from rubbing using P-clamp and tie wraps.

![[17800019.png]]

Locate the connector labeled BURN SOLENOID and connect it to the connector on the top of the oil control valve leading to the burn solenoid.

![[05100041.png]]

Locate the connector labeled MAKE-UP SOLENOID and connect it to the connector on the top of the oil control valve leading to the make-up solenoid.

![[05100040.png]]

> [!note] Note · Примечание
> This step applies to engines equipped with the CELECT™ Plus system **only**. For non-CELECT™ Plus engines, continue to the next step.

Near the engine ECM, locate and remove the cover from the engine datalink connector.

Install the connector labeled DIAGNOSTIC LAMP ENGINE DATALINK CONNECTOR.

![[05100043.png]]

Drill a 1/4-inch hole in a location on the firewall of the engine compartment.

Install the grommet provided in the kit and route the wires through it into the cab.

![[17800024.png]]

For engines that do **not** have a 6-pin datalink connector by the ECM, it is necessary to install two wires for the datalink inside the cab. These wires will be spliced into the J1587 datalink connector. These will be the same wires that are routed to the datalink, usually located under the dashboard. Locate the wires that lead to this connector and connect as specified in the following table:

| Signal | 8-Pin Connector | 6-Pin Connector | 2-Pin Connector |
|---|---|---|---|
| Datalink (+) | Pin 1 | Pin A | Pin A |
| Datalink (-) | Pin 2 | Pin B | Pin B |

![[05100044.png]]

Splice the wires using the above table as a reference (polarity).

Butt-splices are designed to provide the best possible cold joint connection when properly crimped.

![[17800025.png]]

> [!warning] CAUTION · Осторожно
> Overheating of the butt splice can lead to wire damage.

Butt splices also provide protection against corrosion. After crimping the connection, heat the shrink tube with a heat gun until the shrink tube has sealed the joint.

![[17800026.png]]

> [!note] Note · Примечание
> It is very important that the Centinel™ system be properly grounded.

Locate the black lead (ground) on the Centinel™ wiring harness.

Connect the ground lead to ground on the starter (2).

Connect the red lead (positive) of the harness to the positive post (1) of the starter solenoid.

![[05100046.png]]

Connect the last remaining wire on the Centinel™ harness to the positive post on fuel shutoff solenoid.

> [!note] Note · Примечание
> Inspect all the wiring and plumbing lines to make certain your connections and clamps are tight, and all components are secured from rubbing.

![[05100053.png]]

On the Centinel™ wiring harness, locate the two wire connectors labeled LOW OIL LEVEL SENSOR. Cap the connector with the jumper harness found in the burn-only conversion kit.

> [!note] Note · Примечание
> The burn-only Centinel™ system uses the same harness as the standard Centinel™ system. As the standard system uses a make-up oil tank with a low oil level switch/sensor, in the burn-only system this sensor pickup in the harness **must** be jumped (to simulate a tank with adequate make-up oil) for the Centinel™ control module to operate the system properly.

![[07800058.png]]

> [!note] Note · Примечание
> The Centinel™ wiring harness is about 20 feet long. Depending on where the Centinel™ control module or lamp box is located, there can be a considerable length of excess harness. This excess should be rolled together and securely tie-wrapped out of the way.

![[07800059.png]]

> [!note] Note · Примечание
> The following steps apply to N14 PT® and STC engines.

> [!note] Note · Примечание
> Complete the installation of the wiring harness before using P-clamps or tie wraps to secure it from rubbing.

Install the 28-pin connector to the Centinel™ control module.

![[07100075.png]]

Identify the tower-to-shroud connector converter. Securely connect this part to the 2-pin oil control valve solenoid lead.

![[07800085.png]]

Locate the connector labeled RAIL PRESSURE SENSOR, and connect it to the rail sensor located on top of the fuel connecting block.

![[07100093.png]]

> [!note] Note · Примечание
> It is very important that the Centinel™ system be properly grounded.

> [!note] Note · Примечание
> For applications where the engine block is electrically isolated from the negative (-) battery terminal, the block ground lead on the Centinel™ harness **must** be connected to the negative (-) battery return line instead of the mounting bracket bolted on the engine.

Locate the black harness ground lead and fasten it to the oil control valve bracket.

![[07100083.png]]

Route the Centinel™ wiring harness to the oil make-up tank.

Secure the harness from rubbing using P-clamps and tie wraps.

![[17800019.png]]

Locate the connection on the wiring harness labeled LOW OIL LEVEL SENSOR and connect it to the make-up tank sensor.

![[05100037.png]]

Locate the connection marked DIAGNOSTIC LAMPS and connect it to the diagnostic lamp assembly.

Use a P-clamp to attach the wiring to the oil tank.

![[13800034.png]]

Inspect all of the wiring and plumbing lines to make certain that the connections are tight, the clamps are tight, and everything is secured from rubbing.

Locate the connections marked FUEL SHUTOFF SOLENOID.

Route and connect the harness to the fuel shutoff solenoid.

![[05100053.png]]

ISX Engines

Insert the oil level sensor connector into the oil level sensor installed in the oil make-up tank.

Verify that the connector locks are engaged.

![[05100037.png]]

Butt-splice two 16-gauge wires in the two oil level sensor connector butt splices.

Use a heat gun, or equivalent, to heat the butt splices to shrink and seal the connections.

![[17800026.png]]

Route the two wires along the make-up hose to the 31-pin OEM interface connector.

Use the provided tie wraps to secure the make-up hose and wires to the frame rail.

![[17800019.png]]

Cut the wires to size and butt-splice appropriate female socket connectors to the 16-gauge wires.

> [!note] Note · Примечание
> Cummins, Part Number 3822921, is a common repair item found in the Cummins harness repair kit(s).

![[07800086.png]]

Disconnect the 31-pin OEM connector. Locate pin locations 24 and 25, and remove their cavity plugs.

Install two female sockets into pins 24 and 25.

> [!note] Note · Примечание
> Make sure the sockets “snap” securely into place.

![[07800087.png]]

Connect the 31-pin OEM connector, making sure the connector is securely locked in place.

Use provided tie wraps to secure the remainder of the oil make-up level sensor leads to avoid chafing and to make sure no stress is applied to the pin sockets.

![[07800088.png]]

Burn-Only, K19 Engines

> [!note] Note · Примечание
> Complete the installation of the wiring harness before using p-clamps or tie wraps to secure it from rubbing.

Locate and remove the Centinel™ wiring harness from the package.

Install the 28-pin connector to the Centinel™ control module.

> [!tip] Момент затяжки · Torque Value
> 1 n•m [9 in-lb]

![[05400055.png]]

Locate the connector labeled BURN SOLENOID and connect it to the connector on the top of the oil control valve to the burn solenoid.

![[05100041.png]]

Locate the connector labeled MAKE-UP SOLENOID and connect it to the connector on the top of the oil control valve leading to the make-up solenoid.

![[05100040.png]]

Locate the connector labeled RAIL PRESSURE SENSOR and connect it to the rail sensor located on the top of the fuel connecting block.

![[05400056.png]]

Use the p-clamp provided in the upfit kit to attach the harness to the bottom left bracket control valve bolt.

![[05600052.png]]

> [!note] Note · Примечание
> It is very important that the Centinel™ system is properly grounded.

> [!note] Note · Примечание
> For applications where the engine block is electrically isolated from the negative battery terminal, the block ground lead on the Centinel™ harness **must** be connected to the negative battery return line instead of to the mounting bracket bolted on the engine.

Locate the black lead on the Centinel™ wiring harness.

Use a 1/4-20 bolt to ground the lead to the unpainted 1/4-inch threaded hole on the mounting bracket.

> [!tip] Момент затяжки · Torque Value
> 9 n•m [80 in-lb]

![[05600055.png]]

On the Centinel™ wiring harness, locate the two wire connectors labeled LOW OIL LEVEL SENSOR. Cap the connector with the jumper harness found in the burn-only conversion kit.

> [!note] Note · Примечание
> The burn-only Centinel™ system uses the same harness as the standard Centinel™ system. As the standard system uses a make-up oil tank with a low oil level switch/sensor, in the burn-only system this sensor pickup in the harness **must** be jumped (to simulate a tank with adequate make-up oil) for the Centinel™ control module to operate the system properly.

![[07800058.png]]

It will be necessary to choose a location for mounting the high-horsepower diagnostic lamp box (which is normally tank mounted). Location of the Centinel™ lamp box should provide visibility of the diagnostic lamps to operators and maintenance personnel.

Recommended locations include:

- Inside the cab
- On the frame rail
- On the rear of the cab.

> [!note] Note · Примечание
> Do **not** mount the high-horsepower diagnostic lamp box under the hood or in the engine compartment. The Centinel™ lamp box is **not** designed (or covered by warranty) for engine compartment temperatures.

![[nobox.png]]

> [!note] Note · Примечание
> The Centinel™ wiring harness is about 20 feet long. Depending on where the Centinel™ control module or lamp box is located, there can be a considerable length of excess harness. This excess should be rolled together and securely tie-wrapped out of the way.

![[07800059.png]]

Burn With Make-Up, K19 Engines

> [!note] Note · Примечание
> Complete the installation of the wiring harness before using p-clamps or tie wraps to secure it from rubbing.

Locate and remove the Centinel™ wiring harness from the package.

Install the 28-pin connector to the Centinel™ control module.

> [!tip] Момент затяжки · Torque Value
> 1 n•m [9 in-lb]

![[05400055.png]]

Locate the connector labeled BURN SOLENOID and connect it to the connector on the top of the oil control valve to the burn solenoid.

![[05100041.png]]

Locate the connector labeled MAKE-UP SOLENOID and connect it to the connector on the top of the oil control valve leading to the make-up solenoid.

![[05100040.png]]

Locate the connector labeled RAIL PRESSURE SENSOR and connect it to the rail sensor located on the top of the fuel connecting block.

![[05400056.png]]

Use the p-clamp provided in the upfit kit to attach the harness to the bottom left bracket to control valve bolt.

![[05600052.png]]

> [!note] Note · Примечание
> It is very important that the Centinel™ system be properly grounded.

> [!note] Note · Примечание
> For applications where the engine block is electrically isolated from the negative battery terminal, the block ground lead on the Centinel™ harness **must** be connected to the negative battery return line instead of to the mounting bracket bolted on the engine.

Locate the black lead on the Centinel™ wiring harness.

Use a 1/4-20 bolt to ground the lead to the unpainted 1/4-inch threaded hole on the mounting bracket.

> [!tip] Момент затяжки · Torque Value
> 9 n•m [80 in-lb]

![[05600055.png]]

Route the Centinel™ wiring harness to the oil make-up tank. Secure the harness from rubbing using p-clamps and tie-wraps.

![[17800019.png]]

Locate the connection on the wiring harness labeled LOW OIL LEVEL SENSOR and connect it to the make-up tank sensor.

![[05100037.png]]

Locate the connection marked DIAGNOSTIC LAMPS and connect it to the diagnostic lamp assembly.

Use a p-clamp from the upfit kit to attach the wiring to the oil tank.

![[13800034.png]]

> [!note] Note · Примечание
> Inspect all the wiring and plumbing lines to make sure your connections are tight, clamps are tight, and everything is secured from rubbing.

Locate the connections marked FUEL SHUTOFF SOLENOID. Route and connect the harness to the fuel shutoff solenoid.

![[05100053.png]]

Burn-Only, K38 and K50 Engines

> [!note] Note · Примечание
> Complete the installation of the wiring harness before using p-clamps or tie wraps to secure it from rubbing.

Locate and remove the Centinel™ wiring harness from the package.

Install the 28-pin connector to the Centinel™ control module.

> [!tip] Момент затяжки · Torque Value
> 1 n•m [9 in-lb]

![[05400055.png]]

Locate the connector labeled BURN SOLENOID and connect it to the connector on the top of the oil control valve to the burn solenoid.

![[05100041.png]]

Locate the connector labeled MAKE-UP SOLENOID and connect it to the connector on the top of the oil control valve to the make-up solenoid.

![[05100040.png]]

Locate the connector labeled RAIL PRESSURE SENSOR and connect it to the rail sensor located on the top of the fuel connecting block.

![[05400056.png]]

Use the p-clamp provided in the upfit kit to attach the harness to the bottom left bracket to control valve bolt.

![[05600052.png]]

> [!note] Note · Примечание
> It is very important that the Centinel™ system be properly grounded.

Locate the black lead on the Centinel™ wiring harness.

Use a 1/4-20 bolt to ground the lead to the unpainted 1/4-inch threaded hole on the mounting bracket.

> [!tip] Момент затяжки · Torque Value
> 9 n•m [80 in-lb]

![[05600055.png]]

On the Centinel™ wiring harness, locate the two wire connectors labeled LOW OIL LEVEL SENSOR. Cap the connector with the jumper harness found in the burn-only conversion kit.

> [!note] Note · Примечание
> The burn-only Centinel™ system uses the same harness as the standard Centinel™ system. As the standard system uses a make-up oil tank with a low oil level switch/sensor, in the burn-only system this sensor pickup in the harness **must** be jumped (to simulate a tank with adequate make-up oil) for the Centinel™ control module to operate the system properly.

![[07800058.png]]

It will be necessary to choose a location for mounting the high-horsepower diagnostic lamp box (which is normally tank mounted). Location of the Centinel™ lamp box should provide visibility of the diagnostic lamps to operators and maintenance personnel.

Recommended locations include:

- Inside the cab
- On the frame rail
- On the rear of the cab.

> [!note] Note · Примечание
> Do **not** mount the high-horsepower diagnostic lamp box under the hood or in the engine compartment. The Centinel™ lamp box is **not** designed (or covered by warranty) for engine compartment temperatures.

![[nobox.png]]

> [!note] Note · Примечание
> The Centinel™ wiring harness is about 20 feet long. Depending on where the Centinel™ control module or lamp box is located, there can be a considerable length of excess harness. This excess should be rolled together and securely tie-wrapped out of the way.

![[07800059.png]]

Burn With Make-Up, K38 and K50 Engines

> [!note] Note · Примечание
> Complete the installation of the wiring harness before using p-clamps or tie wraps to secure it from rubbing.

Locate and remove the Centinel™ wiring harness from the package.

Install the 28-pin connector to the Centinel™ control module.

> [!tip] Момент затяжки · Torque Value
> 1 n•m [9 in-lb]

![[05400055.png]]

Locate the connector labeled BURN SOLENOID and connect it to the connector on the top of the oil control valve leading to the burn solenoid.

![[05100041.png]]

Locate the connector labeled MAKE-UP SOLENOID and connect it to the connector on the top of the oil control valve to the make-up solenoid.

![[05100040.png]]

Locate the connector labeled RAIL PRESSURE SENSOR and connect it to the rail sensor located on the top of the fuel connecting block.

![[05400056.png]]

Use the p-clamp provided in the upfit kit to attach the harness to the bottom left bracket to control valve bolt.

![[05600052.png]]

> [!note] Note · Примечание
> It is very important that the Centinel™ system be properly grounded.

Locate the black lead on the Centinel™ wiring harness.

Use a 1/4-20 bolt to ground the lead to the unpainted 1/4-inch threaded hole on the mounting bracket.

> [!tip] Момент затяжки · Torque Value
> 9 n•m [80 in-lb]

![[05600055.png]]

Route the Centinel™ wiring harness to the oil make-up tank. Secure the harness from rubbing using p-clamps and tie wraps.

![[17800019.png]]

Locate the connection on the wiring harness labeled MAKE-UP TANK SENSOR and connect it to the make-up tank sensor.

![[05100037.png]]

Locate the connection marked DIAGNOSTIC LAMPS and connect it to the diagnostic lamp assembly.

Use a p-clamp from the upfit kit to attach the wiring to the oil tank.

![[13800034.png]]

> [!note] Note · Примечание
> Inspect all the wiring and plumbing lines to make sure your connections are tight, clamps are tight, and everything is secured from rubbing.

Locate the connections marked FUEL SHUTOFF SOLENOID. Route and connect the harness to the fuel shutoff solenoid.

![[05100053.png]]

Burn-Only, QSK45 and QSK60 Engines

Install the Centinel™ jumper harness between the engine harness (6-pin connector) and the control valve solenoid (2-pin connector).

Verify that the connector locks are engaged.

> [!note] Note · Примечание
> For burn-only, pins 23 and 30 of the 31-pin OEM connector **must** be jumped to simulate adequate oil is available in the make-up tank, even though there is **no** make-up tank.

![[07800085.png]]

> [!note] Note · Примечание
> Make a jumper wire by splicing the appropriate female socket connectors, Part Number 3822921, to a number 16 gauge wire. Cummins Part Number 3822921 is a common repair item found in the Cummins harness repair kit(s).

Disconnect the 31-pin OEM connector. Locate pin locations 23 and 30 and remove their cavity plugs.

Install the two female sockets of the jumper wire into pins 23 and 30.

> [!note] Note · Примечание
> Make certain the sockets "snap" securely into place.

![[07800089.png]]

Connect the 31-pin OEM connector making certain the connector is securely locked in place.

Use provided tie wraps to secure the remainder of the oil make-up level sensor leads to avoid chafing and making certain there is no stress applied to the pin sockets.

![[07800175.png]]

Properly reinstall any Cummins or customer hardware that was removed or relocated.

![[nobox.png]]

Burn With Make-Up, QSK45 and QSK60 Engines

Install the Centinel™ jumper harness between the engine harness (6-pin connector) and the control valve solenoid (2-pin connector).

Verify that the connector locks are engaged.

![[07800085.png]]

Insert the oil level sensor connector into the oil level sensor installed in the oil make-up tank.

Verify that the connector locks are engaged.

![[05100037.png]]

Butt-splice two number 16-gauge wires (**not** furnished) in the two oil level sensor connector butt splices.

Use a heat gun, or equivalent, to heat the butt splices to shrink and seal the connections.

Use the provided tie wraps to secure the two wires to the make-up hose, making certain there is **no** stress applied to the butt-splices and sensor connector.

![[17800026.png]]

Route the two wires along the make-up hose to the 31-pin OEM interface connector.

Use provided tie wraps to secure the make-up hose and wires to the frame rail.

![[17800019.png]]

Cut the wires to size and butt-splice appropriate female socket connectors, Part Number 3822921 (**not** furnished), to the number 16-gauge wires.

> [!note] Note · Примечание
> Cummins Part Number 3822921 is a common repair item found in the Cummins harness repair kit(s).

![[07800086.png]]

Disconnect the 31-pin OEM connector. Locate pin locations 23 and 30 and remove their cavity plugs.

Install the two female sockets into pins 23 and 30.

> [!note] Note · Примечание
> Make certain the sockets "snap" securely into place.

![[07800087.png]]

Connect the OEM 31-pin connector making certain the connector is securely locked in place.

Use provided tie wraps to secure the remainder of the oil make-up level sensor leads to avoid chafing and making certain there is no stress applied to the pin sockets.

![[07800088.png]]

Properly reinstall any Cummins or customer hardware that was removed or relocated.

![[nobox.png]]
