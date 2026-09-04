---
aliases:
  - "Система выпуска — обзор"
type: "Процедура"
doc: "377-011-999"
title_en: "Exhaust System - Overview"
title_ru: "Система выпуска — обзор"
modified: "2022-04-25"
manuals:
  - "5411181"
figures: 16
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/377/377-011-999.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/377-011-999.pdf"
tags:
  - "документ/процедура"
  - "группа/377"
---

# Exhaust System - Overview
**Система выпуска — обзор**

> [!abstract] Процедура · `377-011-999`
> **Входит в руководства:** [[5411181 — X15 CM2350 X114B - Efficiency Series Service Manual|5411181]]
> **Секции:** Section F - Familiarization
> **Даты:** изменён 2022-04-25
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/377/377-011-999.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/377-011-999.pdf)

### General Information

On an engine with exhaust gas recirculation (EGR), the air intake system and exhaust system components work together to provide the correct amount of intake charge air flow into the engine. This overview covers the major components of the exhaust system.

1. Exhaust manifold and seal
2. EGR cooler
3. EGR valve
4. Exhaust pressure sensor and mounting (**not** shown).

> [!note] Note · Примечание
> Use the following procedure for information on the intake air system components. Refer to Procedure 010-999 in Section F.

This overview also covers the aftertreatment system components located off the engine in the exhaust system.

![[11t00027.png]]

The exhaust manifold is a two-piece design with a sealed slip-joint to allow for thermal expansion.

Depending on the application, the exhaust manifold used can vary to enable the turbocharger to be located in various positions.

The exhaust manifold has an additional port that connects to the EGR cooler inlet (1).

The exhaust manifold sections are sealed by a metallic exhaust seal (2), which is replaceable in the event the seal malfunctions and leaks exhaust gas.

The seal requires a special installation tool to be properly installed to the exhaust manifold.

![[11c00658.png]]

The EGR cooler (1) cools the exhaust gases flowing to the EGR valve. The EGR cooler is mounted below the exhaust manifold and is attached to the cylinder block and lubricating oil cooler housing.

Because the EGR valve is mounted after the EGR cooler, the EGR cooler is subject to the same exhaust temperatures and pressures as the exhaust manifold.

The EGR cooler has a coolant vent (2) near the exhaust inlet of the EGR cooler. This vent prevents air from being trapped in the cooler during coolant filling and engine operation by continuously flowing coolant to the top tank of the vehicle cooling system.

![[11o00063.png]]

Exhaust pressure in the exhaust manifold, which determines the position of the variable geometry turbocharger and the EGR valve, is measured by an exhaust pressure sensor.

To maximize the durability of the exhaust pressure sensor, the sensor does **not** mount directly into the exhaust manifold. The exhaust pressure sensor is connected by a tube to the exhaust manifold.

The exhaust pressure sensor is located on the EGR cooler coolant outlet connection (1) for additional cooling of the sensor.

![[11l00057.png]]

The diesel particulate filter (DPF) system is used to reduce particulate emissions and is composed of five main components:

1. Aftertreatment diesel oxidation catalyst (DOC)
2. Aftertreatment DPF
3. Aftertreatment exhaust gas temperature sensor
4. Aftertreatment DPF differential pressure sensor
5. Aftertreatment particulate matter sensor.

![[11l00058.png]]

Passive regeneration occurs when the exhaust temperatures are naturally high enough to oxidize the soot collected in the aftertreatment DPF (1) faster than the soot is collected.

Passive regeneration typically occurs when the temperature of the aftertreatment DPF is above 316°C \[601°F\]. This occurs during highway driving or driving with heavy loads.

Since passive regeneration occurs naturally, it is considered to be normal engine operation. No fuel is added to the exhaust stream during passive regeneration.

![[11l00059.png]]

Active regeneration occurs when the exhaust temperatures are **not** naturally high enough to oxidize the soot collected in the aftertreatment DPF faster than it is collected.

Active regeneration requires assistance from the engine in order to increase the exhaust temperature. This is typically done by injecting a small amount of diesel fuel into the exhaust stream (called aftertreatment injection) which is then oxidized by the aftertreatment DOC. The oxidation of this additional fuel creates the heat needed to regenerate the aftertreatment DPF.

For active regeneration to occur, the engine control module (ECM) **must** detect that the aftertreatment DPF restriction has reached a specified limit. Once this limit is reached, the engine will alter its operation in order to create exhaust temperatures high enough to actively regenerate the aftertreatment DPF.

![[11t00030.png]]

Aftertreatment injection requires temperatures in the aftertreatment system to reach approximately 288°C \[550°F\]. At this temperature and above, the small quantities of fuel injected into the exhaust will properly oxidize across the aftertreatment DOC, creating the additional heat required to actively regenerate the aftertreatment DPF.

During active regeneration, the ECM monitors the exhaust temperatures before and after the aftertreatment DPF, and maintains the temperatures in a range of approximately 482 to 649°C \[900 to 1200°F\]. The quantity of fuel used for aftertreatment injection will vary as the temperature is controlled within these limits.

The temperatures achieved during active regeneration are typically higher than those achieved during passive regeneration. The conversion of soot to carbon dioxide occurs much faster as temperatures increase.

A typical active regeneration event will take approximately 20 to 40 minutes to complete while the vehicle is operating. The vehicle operator may notice additional turbocharger noise during this time, along with an illuminated HIGH EXHAUST TEMPERATURE lamp, if equipped.

The frequency at which an engine will require an active regeneration varies greatly from application to application. In general, vehicles with a low vehicle speed, such as urban vehicles, or a low-load duty cycle, will require more active regeneration events than a heavily loaded vehicle or a vehicle with a highway speed duty cycle.

The ECM also contains a time-based feature for active regenerations that is used to verify correct aftertreatment operation when the vehicle duty cycle is typically high enough that active regeneration events are **not** necessary.

If the engine has **not** completed an active regeneration within the last 100 hours of operation, the ECM will call for a time-based active regeneration event.

The 100-hour timer resets each time the ECM detects that an active regeneration event has completed.

Under some operating conditions, such as low speed, low load, or stop-and-go duty cycles, the engine may **not** have enough opportunity to regenerate the aftertreatment DPF during normal vehicle operation. When this occurs, the engine illuminates the aftertreatment DPF lamp to inform the vehicle operator that assistance is required, typically in the form of a stationary (parked or non-mission) regeneration.

Stationary (parked or non-mission) regeneration is a form of active regeneration that is initiated by the vehicle operator when the vehicle is **not** moving. [[493-014-016 — Aftertreatment Diesel Particulate Filter (DPF) Regeneration Test|Refer to Procedure 014-016 in Section 14.]]

![[11d00294.png]]

The vehicle manufacturer has the option of installing two switches (the start switch and the permit switch) that control aftertreatment functions.

- The start switch (known as the Diesel Particulate Filter Regeneration Start Switch in INSITE™ electronic service tool) is used to start a stationary (parked or non-mission) regeneration. The vehicle manufacturer can also reference this switch as a stationary regeneration switch, start switch, or parked (non-mission) regeneration switch.
- The permit switch (known as the Diesel Particulate Filter Permit Switch in INSITE™ electronic service tool) is used to allow the vehicle operator to disable active regeneration, if necessary. The vehicle manufacturer can also reference this switch as an inhibit switch, stop switch, or disable switch.

[[493-011-056 — Exhaust System Diagnostics|Refer to Procedure 011-056 in Section 11.]]

The Minimum Vehicle Speed for Automotive Mobile Regeneration parameter in INSITE™ electronic service tool allows the vehicle manufacturer to program a minimum vehicle speed at which active regeneration is allowed.

This parameter is controlled by the vehicle manufacturer and can be protected by an original equipment manufacturer (OEM) password. Do **not** change the value of this parameter without written consent of the vehicle manufacturer. This parameter can be set between 0 to 40 km/h \[0 and 25 mph\].

When this parameter is set to 0 km/h \[0 mph\], the engine is allowed to activate an active regeneration event at any vehicle speed.

If the engine needs to initiate an active regeneration event, but the vehicle speed is 0 km/h \[0 mph\] and the engine is at low idle speed, the engine will **not** immediately enter an active regeneration event. The ECM will wait until the engine speed increases to begin the active regeneration event. Once the active regeneration begins, and the exhaust temperatures have increased, the engine will maintain the active regeneration event, even if the vehicle speed returns to 0 km/h \[0 mph\] and the engine speed returns to idle.

When the vehicle speed is greater than 0 km/h \[0 mph\] and the engine speed is above idle speed, an active regeneration event can occur at any time.

When this parameter is set to any speed other than 0 km/h \[0 mph\], the triggers for active regeneration change.

In order for an active regeneration event to start, the vehicle speed **must** exceed 64 km/h \[40 mph\], regardless of minimum vehicle speed parameter setting. Once the vehicle speed exceeds 64 km/h \[40 mph\], an active regeneration event can begin.

Once the vehicle speed has exceeded 64 km/h \[40 mph\] and the active regeneration event has started, the active regeneration event will continue until the vehicle speed drops below the minimum speed parameter. Once the vehicle speed drops below the minimum speed parameter, the active regeneration stops.

The vehicle **must** exceed 64 km/h \[40 mph\] to begin the active regeneration event again.

If a vehicle has a non-0 km/h \[0 mph\] minimum vehicle speed for mobile (mission) active regeneration, and has a low vehicle speed, or stop-and-go duty cycle (such as a transit bus, delivery vehicle, or school bus), the engine may **not** have enough opportunity to perform or complete an active regeneration event. An engine in this situation can illuminate the DPF lamp on a frequent basis, signaling the need for a stationary regeneration.

The Aftertreatment Warm-up feature activates during periods of extended idle time.

The purpose of this feature is to increase the temperature of the aftertreatment system to remove any water condensation that has built up during the idle time.

After the ECM detects that the exhaust temperature entering the aftertreatment system has been below 150°C \[302°F\] for 4 hours, the ECM automatically increases the engine speed to between 760 rpm for approximately 15 to 20 minutes.

For the Aftertreatment Warm-up feature to activate, the following conditions **must** be met:

- More than 4 continuous idle hours with exhaust temperature less than 110°C \[230°F\], or
- More than 8 continuous idle hours with exhaust temperature less than 250°C \[482°F\]
- The clutch pedal is released
- The brake pedal is released
- The transmission is in neutral or park
- Power Take-Off (PTO) or Remote PTO is OFF
- The vehicle speed is 0 mph
- The accelerator pedal is released.

The Aftertreatment Warm-up feature is different from stationary regeneration as the Aftertreatment Warm-up feature operates at a lower rpm and does **not** require aftertreatment HC injection since it requires lower temperatures than a stationary (parked) regeneration.

The Aftertreatment Warm-up feature can **not** be disabled by activating the permit switch, if equipped, because it does **not** use aftertreatment injection.

Increasing the exhaust temperature entering the aftertreatment system to above 250°C \[482°F\] for approximately 15 to 20 minutes allows the Aftertreatment Warm-up to deactivate. This can be done by allowing the engine to operate in this condition for approximately 15 to 20 minutes or by driving the vehicle.

The aftertreatment selective catalytic reduction (SCR) is designed to reduce nitrogen oxides (NOx) emissions from the engine using the following components:

1. Aftertreatment decomposition tube
2. Aftertreatment SCR
3. Aftertreatment outlet NOx sensor and probe
4. SCR outlet temperature sensor probe

![[11l00060.png]]

The diesel exhaust fluid (DEF) converts nitrogen oxides from the exhaust stream into nitrogen and water.

During an initial cold start, the engine will go into SCR warm-up condition. This condition will sound and act like an active regeneration. The SCR catalyst will need to have a temperature of over 150°C \[302°F\] in order to properly convert NOx in the exhaust stream.

The aftertreatment outlet NOx sensor at the outlet of the SCR (1) will monitor the NOx output in the exhaust system and relay the information back to the ECM.

![[11l00061.png]]

The DEF dosing system is composed of five main components to aid the SCR catalyst in the NOx conversion process.

1. Aftertreatment DEF dosing unit
2. Aftertreatment decomposition tube
3. Aftertreatment DEF dosing valve
4. Aftertreatment DEF tank
5. Aftertreatment DEF lines.

![[11l00062.png]]

The aftertreatment DEF dosing valve is controlled by the ECM. The ECM commands the correct amount of DEF to be sprayed into the exhaust stream. Because the dosing control valve is mounted directly to the exhaust system, it will encounter high temperatures. DEF is circulated through the DEF dosing valve to keep the valve cool and operable.

1. Electrical connection to the ECM
2. DEF inlet port
3. DEF outlet port

Use the following procedure for additional information. [[377-011-059 — Aftertreatment Diesel Exhaust Fluid Dosing Valve|Refer to Procedure 011-059 in Section 11.]]

![[11l00063.png]]

The DEF control valve is mounted to the aftertreatment decomposition tube. The aftertreatment decomposition tube contains a mixer to help the DEF mist distribute evenly in the exhaust stream.

1. Aftertreatment decomposition tube
2. Aftertreatment decomposition tube inlet
3. Aftertreatment DEF dosing valve
4. Aftertreatment decomposition tube outlet.

![[11l00064.png]]

When the aftertreatment DEF dosing unit is activated, it pulls DEF from the DEF tank, filters the DEF, and pressurizes the DEF to the DEF dosing valve. Any DEF that is **not** used is returned to the DEF tank.

When a driver turns the key OFF, the dosing system may run a recirculation cycle during shutdown to prevent the DEF dosing valve from overheating. An audible click and pumping sound will be heard from the DEF dosing unit when it is in the recirculation cycle. This unused DEF is returned to the DEF tank.

The main components of the aftertreatment DEF dosing unit:

1. Aftertreatment DEF dosing unit filter cap
2. Electrical connector to the ECM
3. DEF inlet port
4. Coolant ports
5. DEF outlet port.

Use the following procedure for a more detailed description of the aftertreatment DEF dosing unit. [[377-011-058 — Aftertreatment Diesel Exhaust Fluid Dosing Unit|Refer to Procedure 011-058 in Section 11.]]

Use the following procedure for a more detailed description of the aftertreatment DEF dosing unit filter. Refer to Procedure 011-060 in Section 11.

![[11l00065.png]]

The aftertreatment DEF tank is designed to store DEF for the SCR aftertreatment. A sensor detects DEF tank level, temperature, and quality, and sends a signal to the ECM.

If the DEF tank level becomes too low, the ECM will register a fault and derate engine power.

If the DEF tank temperature drops below -5°C \[23°F\], the DEF tank coolant valve will be commanded open by the ECM. Hot engine coolant will flow though the tank to defrost the frozen DEF. The DEF dosing system will **not** prime until the DEF tank is defrosted.

If the DEF tank is filled with the incorrect fluid (anything other than DEF) the aftertreatment system will **not** operate correctly.

Refer to service bulletin, Diesel Exhaust Fluid Specifications for Cummins® Selective Catalytic Reduction Systems, Bulletin [[4021566 — Diesel Exhaust Fluid (DEF) Specifications for Cummins® Selective Catalytic Reduction|4021566]].

DEF tanks will vary in size and shape. See equipment manufacturer service information for additional information.

![[11c00655.png]]

The aftertreatment DEF lines carry the DEF to and from the aftertreatment DEF tank as well as to the DEF dosing valve.

The DEF will remain in the lines.

DEF line connectors, length, and design will vary upon vehicle manufacturer. See equipment manufacturer service information.

![[19d02324.png]]

The SCR system is comprised of many components, but requires a minimal amount of servicing or driver intervention. The SCR system is comprised of three main states: priming, dosing, and heating.

#### Priming State

- Once the SCR reaches a temperature of 150°C \[302°F\] the ECM will command the aftertreatment DEF dosing unit to start its priming process. The aftertreatment DEF dosing unit will draw DEF from the DEF tank, pressurize the DEF, and then filter the DEF to the aftertreatment DEF dosing valve. The aftertreatment DEF dosing valve will open and close to rid any air from the system. Once the system is able to build up pressure and has removed most of the air bubbles from the DEF lines, the aftertreatment DEF dosing system is capable of dosing.

#### Dosing State

- The aftertreatment DEF dosing valve will open and spray DEF in the exhaust stream when commanded by the ECM. The DEF will then be chemically altered by the aftertreatment SCR catalyst to clean the exhaust gases. As long as the dosing system is in the dosing state, the aftertreatment DEF dosing unit will continue to run regardless if the aftertreatment DEF dosing valve is or is **not** spraying DEF. DEF dosing rates are dependent on vehicle duty cycle. The dosing rates are **not** necessarily constant under most duty cycles. The aftertreatment DEF dosing valve will pulse the demanded amount of DEF into the exhaust stream. Any DEF that is **not** used by the aftertreatment DEF dosing valve is returned to the DEF.

#### Heating State

- Diesel exhaust fluid freezes at -11°C \[12°F\]. If a driver starts the engine in a cold climate, the dosing heating state will be activated. If the ambient air temperature sensor reads ambient conditions are below -4°C \[25°F\], the ECM will command the dosing system to go into the defrost state. The aftertreatment dosing unit will turn on its internal heater to defrost any remaining DEF that still may be inside. The heated DEF lines will also be commanded on. If the DEF tank temperature drops below -5°C \[23°F\] the DEF tank coolant valve will be commanded open by the ECM. Engine coolant will flow through the tank to defrost the frozen DEF. It will also flow through the DEF dosing unit to heat up the pump and defrost the DEF. The DEF dosing system will **not** prime until every component is completely defrosted. If ambient conditions continue to be cold after the system has primed, the ECM will command a maintenance heating feature to prevent the DEF dosing system from refreezing. This feature will cycle the heating on and off to the DEF lines, DEF tank, and aftertreatment DEF dosing unit.
