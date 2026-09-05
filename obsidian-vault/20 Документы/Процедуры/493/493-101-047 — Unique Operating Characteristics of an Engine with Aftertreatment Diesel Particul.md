---
type: "Процедура"
doc: "493-101-047"
title_en: "Unique Operating Characteristics of an Engine with Aftertreatment Diesel Particulate Filter"
modified: "2025-04-28"
manuals:
  - "5411182"
  - "5411183"
figures: 3
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/493/493-101-047.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/493-101-047.pdf"
tags:
  - "документ/процедура"
  - "группа/493"
---

# Unique Operating Characteristics of an Engine with Aftertreatment Diesel Particulate Filter

> [!abstract] Процедура · `493-101-047`
> **Входит в руководства:** [[5411182 — X15 CM2350 X114B - Efficiency Series Operation and Maintenance Manual|5411182]], [[5411183 — X15 CM2350 X114B - Efficiency Series and X15 CM2350 X116B - Performance Series Owners|5411183]]
> **Секции:** Section 1 - Operating Instructions
> **Даты:** изменён 2025-04-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/493/493-101-047.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/493-101-047.pdf)

### General Information

The particulate filter system of the aftertreatment system is composed of two main sections. These sections are:

1. The aftertreatment diesel oxidation catalyst (DOC). The aftertreatment DOC is used to oxidize fuel in the exhaust in order to create heat for the regeneration process.
2. The aftertreatment diesel particulate filter (DPF). The aftertreatment DPF captures the soot and ash from the engine exhaust.

![[11l00159.png]]

Soot is composed of the partially burned particles of fuel that occur during normal engine operation (black smoke).

Ash is composed of the partially burned particles of engine oil that occur during normal engine operation.

Over time, both soot and ash accumulate in the aftertreatment DPF and **must** be removed. Soot is removed by a process called regeneration. Ash is removed by removing the aftertreatment DPF and cleaning it at specified intervals.

There are many factors that determine how ash accumulates in an aftertreatment DPF, such as duty cycle and engine health. How ash accumulates in an aftertreatment DPF influences the effectiveness of the different types of ash cleaning processes.

**Air-only cleaning:**

Air- **only** cleaning uses compressed air to remove excess ash from the DPF. This process pushes air in reverse of the exhaust flow to remove the excess ash and soot from the DPF. The entire process typically takes about 45 minutes.

Air- **only** cleaning can remove ash that is loosely packed in and **not** bonded to the DPF. Air- **only** cleaning is typically a lower cost DPF maintenance cleaning process, but it is less capable of removing densely packed ash or ash that is bonded to the DPF.

**Liquid cleaning** (most effective):

Liquid cleaning uses some type of liquid, such as water or chemicals, to help remove the bond between the ash and the DPF substrate. This is a longer cleaning process that can take up to several hours. There are different types of liquid that DPF cleaning suppliers can use.

- As opposed to air- **only**, liquid cleaning is more effective to loosen ash; however, ash can create a strong bond with the DPF substrate. In this case, water- **only**, or water combined with air, is **not** sufficient to clean all types of ash that can accumulate in the DPF. Two readily available suppliers in the market that provide liquid cleaning are:
- Liquid with organic chemicals is even more effective at breaking the bonds ash develops with the DPF substrate. An organic based chemical is safe to use and helps provide the best opportunity of breaking the ash bonds. When combined with air, it can effectively remove most ash that accumulates in DPFs. Some readily available suppliers in the market that provide this type of service are:

Each customer needs to evaluate the best option to maintain its DPFs and which cleaning process supports its business needs. DPF maintenance **must** be completed **only** by appropriately trained personnel.

**DPF maintenance and warranty guidelines:**

Maintaining Cummins® product is the customer's responsibility.

If there's a fault code other than 5383 related to a DPF for an out of warranty repair event, the customer should go to a Cummins® authorized service provider for diagnostics and repairs to identify the root cause of the issue. If 5383 is the **only** DPF-related code present, the customer can choose where to have the DPF cleaned.

If the DPF is within a Cummins® warranty coverage (base, extended, emissions, new or ReCon Parts) period, and any DPF related fault codes are present, the customer **must** go to a Cummins® authorized service provider for diagnostics and repairs to identify the root cause of the issue. The authorized service provider will file the warranty claim to Cummins® if the root cause of failure is warrantable.

**Chemical and heavy metal waste disposal:**

> [!danger] WARNING · Опасно
> The material captured in a partial flow diesel particulate filter and/or a diesel particulate filter may contain elevated concentrations of metals. Primarily zinc, molybdenum, and possibly polynuclear aromatic hydrocarbons, that may be regulated. These materials must be characterized, handled, and disposed of according to applicable local regulations. In addition, due to the presence of the above-listed chemicals and other potentially toxic components such as oxides of calcium, zinc, phosphorous, silicon, sulfur, and iron, exhaust filter maintenance must be completed only by appropriately trained personnel.

**Disclaimer:**

Cummins® has provided this document for information purposes **only**; it is **not** intended as a substitute for professional advice and it does **not** constitute a solicitation, endorsement, or offer by Cummins® or any third-party cleaning company to buy or sell any product or services. Cummins® provides no warranty or representation and disclaims all warranties and conditions, whether express or implied, of merchantability, fitness for a particular purpose, or non-infringement, and all responsibility and liability for the services or products provided by third-party cleaning companies and/or for any reliance on the content of the information included herein. Under no circumstances will Cummins® be responsible or liable for any claims, damages, losses, expenses, costs or liabilities (including, without limitation, any direct or indirect damages for loss of profit, business interruption, or loss of information) resulting directly or indirectly from the use or inability to use the third-party cleaning companies and/or reliance on the content of the information included herein.

Equipment with an aftertreatment system has three additional indicator lamps on the dashboard. Two of the additional lamps, along with the CHECK ENGINE lamp, alert the operator of the status of the aftertreatment DPF. The third additional indicator lamp indicates the position of the Regeneration Permit switch.

Ultra low sulfur diesel fuel is required for an engine equipped with an aftertreatment DPF. If ultra low sulfur diesel fuel is **not** used, the aftertreatment system can be damaged.

> [!note] Note · Примечание
> The blending of fuel with new or used engine lubricating oil or other oils is **not** permitted on equipment using an aftertreatment DPF.

Some engines contain an engine control module (ECM) calibration feature, Aftertreatment Warm-Up, which activates automatically during periods of extended idle to remove water and hydrocarbon accumulations from the aftertreatment system.

The Aftertreatment Warm-Up feature is different from Active or Manual (Non-Mission) Regeneration, as it operates at a lower engine speed (RPM) and does **not** require aftertreatment fuel injection, because of lower aftertreatment system temperature requirements.

The ECM will automatically increase the engine speed to 760 RPM for approximately 15 to 20 minutes, if the ECM detects all of the conditions below have been met:

- More than 4 continuous idle hours with exhaust temperature \<110 °C \[230 °F\] or
- More than 8 continuous idle hours with exhaust temperature \<250 °C \[482 °F\]
- The clutch pedal is released
- The brake pedal is released
- The transmission is in neutral or park
- PTO or Remote PTO is turned OFF
- The vehicle speed is 0 mph
- The accelerator pedal is released.

The Aftertreatment Warm-Up feature can **not** be disabled by activating the active regeneration permit switch, if equipped, because the feature does **not** use aftertreatment fuel injection.

Increasing the temperature of the exhaust gas that enters the aftertreatment system to above 250°C \[482°F\] for approximately 15 to 20 minutes allows the Aftertreatment Warm-Up feature to deactivate. This can be done by allowing the engine to operate in this condition for approximately 15 to 20 minutes, or by driving the vehicle.

> [!note] Note · Примечание
> The engine speed will **not** be changed during power take-off (PTO) or remote PTO operation.

> [!note] Note · Примечание
> The Aftertreatment Warm-Up feature can **not** be disabled or adjusted with the recommended Cummins® electronic service tool or equivalent or other electronic tools.

### Regeneration

Overview

Regeneration is the process of converting the soot collected in the aftertreatment DPF into carbon dioxide.

The regeneration process requires heat to occur, and can be classified into two different types: passive regeneration and active regeneration.

Passive Regeneration

Passive regeneration occurs when the exhaust temperatures are naturally high enough to oxidize the soot collected in the aftertreatment DPF faster than the soot is being collected.

Passive regeneration typically occurs when the vehicle is driven at high speeds (ie, highway speeds) and/or under heavy loads.

Active Regeneration

Active regeneration occurs when the exhaust temperatures are **not** naturally high enough to oxidize the soot collected in the aftertreatment DPF faster than it is being collected.

Active regeneration requires assistance from the engine in order to increase the exhaust temperature. This is typically accomplished by the engine injecting a small amount of diesel fuel into the exhaust stream, which is then oxidized by the aftertreatment DOC. This creates the heat needed to regenerate the aftertreatment DPF.

Active regeneration will occur more frequently in vehicles with low speed, low load, or stop-and-go duty cycles.

Active regeneration **only** occurs if the engine control module has detected that the aftertreatment DPF restriction has reached a specified limit, and may **only** occur if the vehicle is moving above a speed threshold. The engine control module will activate and de-activate active regeneration as needed.

The speed threshold for active regeneration to occur is dictated by the vehicle manufacturer, and can be set at vehicle speeds from 8 to 40 km/hr \[5 to 25 mph\].

Active regeneration can occur any time the vehicle speed is above the speed threshold.

Use the vehicle owner's manual for information about the speed threshold for active regeneration used for a specific vehicle.

Active regeneration is largely transparent to the vehicle operator. The vehicle operator may notice an increase in turbocharger noise during an active regeneration event, and may notice that the high exhaust temperature lamp is illuminated, if the exhaust temperature is greater than the high exhaust system temperature threshold set by the original equipment manufacturer (OEM).

During active regeneration, the exhaust temperature can be higher than when the engine is operating at full load. The exhaust temperature during a normal active regeneration event could reach 593°C \[1100°F\], and possibly 816°C \[1500°F\] under certain conditions.

> [!danger] WARNING · Опасно
> If the vehicle is not equipped with a High Exhaust System Temperature Lamp, follow these precautions for active regeneration whenever the vehicle is running and the vehicle slows or comes to a stop. Active regeneration can occur any time the vehicle is moving, and the exhaust temperature can remain hot after the vehicle has stopped moving. The exhaust temperature could reach 816°C \[1500°F\], which is hot enough to ignite or melt common materials, or to burn people.

Manual (Non-Mission) Regeneration

Under some operating conditions, such as low speed, low load, or stop and go duty cycles, the engine may **not** have enough opportunity to regenerate the aftertreatment DPF during normal vehicle operation. When this occurs, the engine will illuminate the aftertreatment DPF lamp to inform the vehicle operator that assistance is required, typically in the form of a manual (non-mission) regeneration.

Manual (non-mission) regeneration is a form of active regeneration that is initiated by the vehicle operator when the vehicle is **not** moving.

Manual (non-mission) regeneration requires an elevated engine speed of approximately 1000 to 1400 RPM. The length of a manual (non-mission) regeneration will vary, depending on how full the aftertreatment DPF is, but will typically take anywhere from 45 minutes to 1.5 hours to complete.

A manual (non-mission) regeneration can be initiated in one of two ways:

1. A vehicle mounted manual (non-mission) regeneration switch. Use the vehicle owners manual for the location and operation of this switch, if so equipped (this switch may also be called a "parked regeneration" switch or "start" switch). The vehicle mounted manual (non-mission) regeneration switch will only initiate a manual (non-mission) regeneration when the aftertreatment DPF lamp is illuminated.
2. The recommended Cummins® electronic service tool or equivalent can initiate a manual (non-mission) regeneration by starting the "Aftertreatment Diesel Particulate Filter Regeneration Test".

> [!danger] WARNING · Опасно
> During regeneration, exhaust gas temperature could reach 816°C \[1500°F\], and exhaust system surface temperature could exceed 740°C \[1300°F\], which is hot enough to ignite or melt common materials, and to burn people. Engine speed will increase and could possibly reach between 1000 to 1500 RPM. Follow these instructions to avoid the risk of fire, property damage, burns, or other serious personal injury.

To perform a manual (non-mission) regeneration, follow the steps listed:

- Select an appropriate location to park the vehicle.
- Park the vehicle away from anything that can burn, melt, or explode.
- Park the vehicle securely. Place the transmission in park, if provided, otherwise in neutral. Set wheel chocks at the front and rear of at least one tire.
- Set up a safe exhaust area. If bystanders might enter the area, set up barriers to keep people at least 152 cm \[5 ft\] from the exhaust outlet during the manual (non-mission) regeneration. When indoors, attach an exhaust discharge pipe rated for at least 816°C \[1500°F\].
- Keep a fire extinguisher nearby.
- Check the exhaust system surfaces. Confirm that nothing is on or near the exhaust system surfaces (such as tools, rags, grease, or debris).
- Verify the following conditions are met in the vehicle:
- Initiate the manual (non-mission) regeneration by toggling the vehicle mounted manual (non-mission) regeneration switch or by using the recommended Cummins® electronic service tool or equivalent.
- Monitor the vehicle and surrounding area during the manual (non-mission) regeneration. If any unsafe condition occurs, shut off the engine immediately.

Once the manual (non-mission) regeneration is complete, exhaust gas and surface temperatures will remain elevated for 3 to 5 minutes.

Some engines contain an ECM calibration feature, Aftertreatment Idle-Up, that activates automatically and is used to control the aftertreatment system temperature. This feature will maintain an elevated low idle speed, approximately 760 rpm, when an aftertreatment regeneration, active or manual, completes or is cancelled by:

1. Depressing the accelerator, clutch, or service brake pedal
2. Activating the aftertreatment regeneration inhibit switch or
3. Activating another engine feature that may interact with the regeneration, such as remote throttle or PTO.

> [!note] Note · Примечание
> The Aftertreatment Idle-Up feature can **not** be disabled or adjusted with the recommended Cummins® electronic service tool or equivalent or other electronic tools.

### Aftertreatment Switches

The vehicle manufacturer may choose to equip the vehicle with up to two switches that interact with the aftertreatment system:

- A manual (non-mission) regeneration switch (can also be called a "START" switch or "PARKED REGENERATION" switch).
- An active regeneration permit switch (can also be called an "INHIBIT" switch, "DISABLE" switch, or "STOP" switch)

Both of these switches are optional. Please reference the vehicle owners manual for the location and presence of these switches.

The manual (non-mission) regeneration switch is used to initiate a manual (non-mission) regeneration. Please reference the "Stationary (Parked) Regeneration" section of this procedure for further instructions.

The active regeneration permit switch is used to disable active regeneration of the aftertreatment.

The permit switch **must only** be used for special circumstances where it is desirable to **not** allow an active regeneration event. Prolonged engine operation with this switch engaged may result in illumination of the aftertreatment diesel particulate lamp, as the aftertreatment DPF will continue to accumulate soot as the engine operates.

The aftertreatment switches are typically used in two configurations:

1. A two-position switch that is used to activate manual (non-mission) regeneration.
2. A three-position switch that is used to activate manual (non-mission) regeneration and also disable active regeneration.

The examples below are generic and show two typical switch configurations. Use the vehicle owner's manual for the location and presence of these switches.

A two-position switch (ON and OFF positions) will, when in the "ON" position (1), activate a manual (non-mission) regeneration.

The switch should be left in the "OFF" position (2) when the switch is **not** being used.

![[11d00293.png]]

A three-position switch (ON, NEUTRAL, and OFF positions) will typically have both "START" and "PERMIT" functions.

In the "ON" position (1), the "START" switch is depressed, which will activate a manual (non-mission) regeneration.

In "NEUTRAL" position (2), neither the "START" switch or "PERMIT" switch is depressed as the switch is in the NEUTRAL position. This position is recommended for normal engine operation.

In "OFF" position (3), the "PERMIT" switch is depressed. When the switch is in this position, active regeneration of the aftertreatment system will **not** be allowed.

![[11d00294.png]]
