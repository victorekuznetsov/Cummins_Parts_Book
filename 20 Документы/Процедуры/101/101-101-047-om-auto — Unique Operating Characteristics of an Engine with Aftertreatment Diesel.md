---
type: "Процедура"
doc: "101-101-047-om-auto"
title_en: "Unique Operating Characteristics of an Engine with Aftertreatment Diesel Particulate Filter"
modified: "2025-04-28"
engines:
  - "80141463"
  - "80248213"
families:
  - "QSX15"
manuals:
  - "3666251"
  - "4960314"
figures: 6
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/101/101-101-047-om-auto.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/101-101-047-om-auto.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSX15"
  - "группа/101"
---

# Unique Operating Characteristics of an Engine with Aftertreatment Diesel Particulate Filter

> [!abstract] Процедура · `101-101-047-om-auto`
> **Двигатели:** [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSX15
> **Входит в руководства:** [[3666251 — Signature and ISX Operation and Maintenance Manual|3666251]], [[4960314 — ISX Owners Manual|4960314]]
> **Секции:** Section 1 - Operating Instructions
> **Даты:** изменён 2025-04-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/101/101-101-047-om-auto.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/101-101-047-om-auto.pdf)

### General Information

The aftertreatment system is used to reduce particulate emissions and is composed of six main components:

1. Aftertreatment inlet
2. Aftertreatment diesel particulate filter (DPF) differential pressure sensor
3. Aftertreatment diesel oxidation catalyst (DOC)
4. Aftertreatment DPF
5. Aftertreatment outlet
6. Aftertreatment exhaust gas temperature sensors.

![[11c00256.png]]

The components of the aftertreatment system perform the following functions:

The aftertreatment inlet and outlet adapt the vehicle exhaust piping to the aftertreatment system and also provide a mounting location for the aftertreatment gas temperature sensors.

The aftertreatment DPF differential/outlet pressure sensor measures:

1. The restriction across the aftertreatment DPF.
2. The pressure on the outlet of the aftertreatment DPF.

The aftertreatment DPF captures the soot and ash from the engine exhaust.

The aftertreatment DOC is used to oxidize fuel in the exhaust in order to create heat for the regeneration process.

The aftertreatment exhaust gas temperature sensors are used to measure the exhaust gas temperatures at various points in the aftertreatment system.

Soot is composed of the partially burned particles of fuel that occur during normal engine operation (black smoke).

Ash is composed of the partially burned particles of engine oil that occur during normal engine operation.

Over time, both soot and ash accumulate in the aftertreatment DPF and **must** be removed. Soot is removed by a process called regeneration. Ash is removed by removing the aftertreatment DPF and cleaning it at specified intervals.

Equipment with an aftertreatment system has three additional indicator lamps on the dashboard. Two of the additional lamps, along with the CHECK ENGINE lamp, alert the operator of the status of the aftertreatment DPF. The third additional indicator lamp indicates the position of the Regeneration Permit switch.

> [!note] Note · Примечание
> Use the following procedure for additional information about the engine indicator lamps. Refer to Procedure 101-048 in Section 1.

Ultra low sulfur diesel fuel is required for an engine equipped with an aftertreatment DPF. If ultra low sulfur diesel is **not** used, the aftertreatment DPF or aftertreatment DOC can be damaged.

> [!note] Note · Примечание
> The blending of fuel with new or used engine lubricating oil or other oils is **not** permitted on equipment using an aftertreatment DPF.

> [!note] Note · Примечание
> Use the following procedure for additional information about the fuel recommendations and specifications required for use in the engine being serviced. Refer to Procedure 018-002 in Section V.

To maximize the maintenance intervals of the aftertreatment DPF, Cummins® requires the use of a lubricating engine oil meeting Cummins® Engineering Standard 20081. The use of oil meeting CES 20081 also requires the use of ultra low sulfur diesel fuel to maintain the specified oil drain interval without risk of engine damage.

> [!note] Note · Примечание
> Use the following procedure for additional information about the lubricating oil recommendations and specifications recommended for use in the engine being serviced. [[101-018-003-om-auto — Lubricating Oil Recommendations and Specifications|Refer to Procedure 018-003 in Section V.]]

> [!note] Note · Примечание
> Use the following procedure for information on the Maintenance Schedule, which provides the aftertreatment DPF cleaning intervals for the engine being serviced. [[10-102-002-om-auto — Maintenance Schedule|Refer to Procedure 102-002 in Section 2.]]

### Regeneration

Regeneration is the process of converting the soot collected in the aftertreatment DPF into carbon dioxide.

The regeneration process requires heat to occur, and can be classified into two different types: passive regeneration and active regeneration.

Passive Regeneration

Passive regeneration occurs when the exhaust temperatures are naturally high enough to oxidize the soot collected in the aftertreatment DPF faster than the soot is collected.

Passive regeneration typically occurs when the vehicle is driven at high speeds (ie, highway speeds) and/or under heavy loads.

Active Regeneration

Active regeneration occurs when the exhaust temperatures are **not** naturally high enough to oxidize the soot collected in the aftertreatment DPF faster than it is collected.

Active regeneration requires assistance from the engine in order to increase the exhaust temperature. This is typically accomplished by the engine injecting a small amount of diesel fuel into the exhaust stream, which is then oxidized by the aftertreatment DOC, which creates the heat needed to regenerate the aftertreatment DPF.

Active regeneration will occur more frequently in vehicles with low speed, low load, or stop and go duty cycles.

Active regeneration **only** occurs if the ECM has detected that the aftertreatment DPF restriction has reached a specified limit, and may **only** occur if the vehicle is moving above a speed threshold. The ECM will activate and de-activate active regeneration as needed.

The speed threshold for active regeneration to occur is dictated by the vehicle manufacturer and can be set at vehicle speeds from 5 mph to 25 mph.

For all ISX engines and ISM non-transit bus applications, active regeneration can occur at any time the vehicle speed is above the speed threshold.

For ISM transit bus applications, the vehicle speed must reach 40 mph for active regeneration to begin, regardless of the set speed. The active regeneration event will then continue until the vehicle speed drops below the speed threshold.

Use the vehicle owner's manual for information for the speed threshold for active regeneration used for a specific vehicle.

Active regeneration is largely transparent to the vehicle operator. The vehicle operator may notice an increase in turbocharger noise during an active regeneration event and may notice that the high exhaust temperature lamp is illuminated, if the exhaust temperature is greater than the high exhaust system temperature threshold set by the equipment OEM.

During active regeneration, the exhaust temperature can be higher than when the engine is operating at full load. The exhaust temperature during a normal active regeneration event could reach 593°C \[1100°F\], and possibly 816°C \[1500°F\] under certain conditions.

> [!note] Note · Примечание
> Use the following procedure for additional information on the engine indicator lamps for the engine being serviced. Refer to Procedure 101-048 in Section 1.

> [!danger] WARNING · Опасно
> If the vehicle is not equipped with a High Exhaust System Temperature Lamp, follow these precautions for active regeneration whenever the vehicle is running and the vehicle slows or comes to a stop. Active regeneration can occur any time the vehicle is moving, and the exhaust temperature can remain hot after the vehicle has stopped moving. The exhaust temperature could reach 816°C \[1500°F\], which is hot enough to ignite or melt common materials, or to burn people.

Manual (Non-Mission) Regeneration

Under some operating conditions, such as low speed, low load, or stop and go duty cycles, the engine may **not** have enough opportunity to regenerate the aftertreatment DPF during normal vehicle operation. When this occurs, the engine will illuminate the aftertreatment DPF lamp to inform the vehicle operator that assistance is required, typically in the form of a manual (non-mission) regeneration.

Manual (non-mission) regeneration is a form of active regeneration that is initiated by the vehicle operator when the vehicle is **not** moving.

Manual (non-mission) regeneration requires an elevated engine speed of approximately 1000 to 1400 rpm. The length of a manual (non-mission) regeneration will vary depending on how full the aftertreatment DPF is, but will typically take anywhere from 45 minutes to 1.5 hours to complete.

A manual (non-mission) regeneration can be initiated one of two ways:

- A vehicle mounted manual (non-mission) regeneration switch. Use the vehicle owners manual for the location and operation of this switch, if so equipped (this switch may also be called a "parked regeneration" switch or "start" switch). The vehicle mounted manual (non-mission) regeneration switch will **only** initiate a manual (non-mission) regeneration when the aftertreatment DPF lamp is illuminated.
- The INSITE™ electronic service tool can initiate a manual (non-mission) regeneration by starting the Aftertreatment Diesel Particulate Filter Regeneration Test.

> [!danger] WARNING · Опасно
> During regeneration, exhaust gas temperature could reach 816°C \[1500°F\], and exhaust system surface temperature could exceed 740°C \[1300°F\], which is hot enough to ignite or melt common materials, and to burn people. Engine speed will increase and could possibly reach between 1000 to 1500 rpm. Follow these instructions to avoid the risk of fire, property damage, burns, or other serious personal injury.

To perform a manual (non-mission) regeneration, follow the steps listed:

- Select an appropriate location to park the vehicle.
- Park the vehicle away from anything that can burn, melt, or explode.
- Park the vehicle securely. Place the transmission in park, if provided, otherwise in neutral. Set wheel chocks at the front and rear of at least one tire.
- Set up a safe exhaust area. If bystanders might enter the area, set up barriers to keep people at least 5 ft from the exhaust outlet during the manual (non-mission) regeneration. When indoors, attach an exhaust discharge pipe rated for at least 816°C \[1500°F\].
- Keep a fire extinguisher nearby.
- Check the exhaust system surfaces. Confirm that nothing is on or near the exhaust system surfaces (such as tools, rags, grease, or debris).
- Verify the following conditions are met in the vehicle:
- Initiate the manual (non-mission) regeneration by toggling the vehicle mounted manual (non-mission) regeneration switch or by using INSITE™ electronic service tool.
- Monitor the vehicle and surrounding area during the manual (non-mission) regeneration. If any unsafe condition occurs, shut OFF the engine immediately.

Once the manual (non-mission) regeneration is complete, exhaust gas and surface temperatures will remain elevated for 3 to 5 minutes.

### Aftertreatment Switches

The vehicle manufacturer may choose to equip the vehicle with up to two switches that interact with the aftertreatment system:

- A manual (non-mission) regeneration switch (can also be called a START switch or PARKED REGENERATION switch).
- An active regeneration permit switch (can also be called an INHIBIT switch, DISABLE switch, or STOP switch)

Both of these switches are optional. Please reference the vehicle owners manual for the location and presence of these switches.

![[nobox.png]]

The manual (non-mission) regeneration switch is used to initiate a manual (non-mission) regeneration. Reference the Manual (Non-Mission) Regeneration section of this procedure for further instructions.

The active regeneration permit switch is used to disable active regeneration of the aftertreatment.

The permit switch **must only** be used for special circumstances where it is desirable to **not** allow an active regeneration event. Prolonged engine operation with this switch engaged may result in illumination of the aftertreatment diesel particulate lamp, as the aftertreatment DPF will continue to accumulate soot as the engine operates.

![[nobox.png]]

The aftertreatment switches are typically used in two configurations:

- A two-position switch that is used to activate manual (non-mission) regeneration.
- A three-position switch that is used to activate manual (non-mission) regeneration and also disable active regeneration.

The examples below are generic and show two typical switch configurations. Use the vehicle owner's manual for the location and presence of these switches.

![[nobox.png]]

A two-position switch (ON and OFF positions) will, when in the ON position (1), activate a manual (non-mission) regeneration.

The switch should be left in the OFF position (2) when the switch is **not** being used.

![[11d00293.png]]

A three-position switch (ON, NEUTRAL, and OFF positions) will typically have both START and PERMIT functions.

In the ON position (1), the START switch is depressed, which will activate a manual (non-mission) regeneration.

In NEUTRAL position (2), neither the START switch or PERMIT switch is depressed as the switch is in the NEUTRAL position. This position is recommended for normal engine operation.

In OFF position (3), the PERMIT switch is depressed. When the switch is in this position, active regeneration of the aftertreatment system will **not** be allowed.

![[11d00294.png]]
