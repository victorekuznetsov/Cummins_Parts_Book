---
aliases:
  - "Топливная система — обзор"
type: "Процедура"
doc: "56-005-999"
title_en: "Fuel System - Overview"
title_ru: "Топливная система — обзор"
modified: "2008-11-18"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
families:
  - "QSK60"
manuals:
  - "4021530"
figures: 9
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/56/56-005-999.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/56-005-999.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK60"
  - "группа/56"
---

# Fuel System - Overview
**Топливная система — обзор**

> [!abstract] Процедура · `56-005-999`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]]
> **Семейство:** QSK60
> **Входит в руководства:** [[4021530 — QSK45 and QSK60 Service Manual|4021530]]
> **Секции:** Section F - Familiarization
> **Даты:** изменён 2008-11-18
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/56/56-005-999.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/56-005-999.pdf)

### General Information

with Mechanically Actuated Injector

> [!danger] WARNING · Опасно
> Depending on the circumstance, diesel fuel is flammable. Keep all cigarettes, flames, pilot lights, arcing equipment, and switches out of the work area and areas sharing ventilation to avoid severe personal injury or death when working on the fuel system.

> [!warning] CAUTION · Осторожно
> Tampering with the fuel pump can void the engine warranty, lower engine performance, and be a violation of law.

The QSK fuel system is used on the QSK45 and QSK60 engines. Additional information about the QSK fuel system is available in the Troubleshooting and Repair Manual, Electronic Control Fuel System, QSK19, QSK23, QSK45, QSK60, and QSK78 Engines, Bulletin [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]].

![[05600069.png]]

The QSK fuel system uses an electronically controlled fuel pump to supply a regulated pressure to the electronic fuel control valve assembly.

The QSK45 and QSK60 fuel pump has an output pressure sensor and an actuator to control fuel flow.

There was a new fuel pump introduced in July, 2000, for the QSK45 industrial engine. A new fuel pump for the QSK45 generator drive and QSK60 industrial and generator drive engines was introduced in October, 2000.

The new fuel pump is designated D8 and has the following key design changes:

- The drive gear is a press fit on the drive shaft, eliminating the keyway.
- The pump has a redesigned bracket to improve rigidity and alignment.
- The production implementation date for this change occurred on July 1, 2000.

![[05600070.png]]

The electronic fuel control valve assembly is located on the fuel pump side of the engine.

The electronic fuel control valve assembly includes the:

1. Supply fitting
2. Timing rail actuators
3. Timing rail pressure sensor
4. Timing rail outlet
5. Fuel shutoff valve
6. Fueling rail actuator
7. Fueling rail pressure sensor
8. Fueling rail outlet
9. Fuel temperature sensor
10. Ambient air pressure sensor.

![[19600009.png]]

with Electronically Actuated Injector

![[05600277.png]]

The QSK60 engine is equipped with a modular common rail fuel system. The system provides full electronic control of the engine with high pressure fuel injection.

The fuel pump consists of two pumps:

- The primary pump is a five piston pump that provides a constant fuel supply to the injectors. The pump is lubricated by the engine oil system. The fuel pump pressurizing assembly (5) controls the fuel supply to be pumped, depending on the amount of power that is being required. In the event that the ECM loses control of the system pressure, the fuel rail pressure will rise rapidly. This will cause the mechanical dump valve (6) to trip, returning fuel to the tank and reducing fuel rail pressure. If this occurs, the mechanical dump valve is working properly, and the cause of uncontrolled system pressure **must** be investigated.
- A second pump (2) located on the back is a gerotor style pump that takes fuel from the stage one filter and sends it to the stage two filters. The cover plate (4) contains a priming bypass valve to allow fuel to pass through the gerotor without restriction when priming the system with the priming pump, and a 12 bar \[175 psi\] regulator that is designed to operate **only** when the fuel filters are plugged, to prevent fuel filter rupture or gerotor damage due to excessive pressure. An o-ring (3) provides a seal to prevent leaks.

The fuel pump delivers approximately 1600 bar \[23,000 psi\] to the injectors, which eliminates the need for mechanical injection. The rocker arm, push tube, and cam follower have been eliminated. Injection is controlled electronically through the ECM. The fuel filter head assembly contains a two stage filtration system. The first stage is mounted off the engine and includes the lift pump and three 7 micron fuel filters designed to capture particles that are 7 microns or larger. The first stage filter also has a water drain valve and water in fuel sensor. This sensor is connected to the ECM and will alert the operator with a check engine lamp if water is present. The second stage contains two 3 in 3 micron filters (two 3 micron filter layers in series) which are designed to capture particles that are 3 microns or larger. The second stage filters can be mounted on the engine or with a remote mount option. The electric lift pump operates **only** during cranking and at key on to aid in starting.

A fuel temperature sensor and pressure sensor are located in the fuel filter head so the ECM can monitor the condition of the fuel.

The high pressure fuel pump supplies fuel to the high pressure fuel lines, which supply the injectors. The high pressure fuel lines are double-walled lines. The inner-wall line carries the high pressure fuel to each of the injectors in the system. The inner-wall lines connect at each injector with a cone style seat. This seat is sensitive to foreign debris and dirt, and **must** be kept clean at all times if fuel lines are removed from the system.

The outer-wall lines are designed to capture any high pressure leak from the inner-wall lines. The outer-wall lines are also plumbed in series, allowing any leaks of the high pressure system to drain back towards the fuel pump. At the fuel pump, the outer-wall lines connect to drain tubes at the connection between the injector supply lines and the fuel pump. The drain lines are plumbed to atmosphere, allowing for leak detection of the high pressure lines by fuel drainage at the outlet of the tubes.

The optional Alarm and Safety system, which allows for compliance with the Marine Certification agencies, features a leak detection system that is connected to these outer-wall lines. The leak detector consists of a floating level switch, which can close a circuit to enable an alarm based on the presence of fuel in the leak detector.

![[06600279.png]]

### Installation Recommendations

For customers in the U.S./Canada, publications are available to provide fuel system installation recommendations approved by Cummins Inc. at:

Gannett

10003 Bunsen Way

P. O. Box 99085

Louisville, KY 40299

For customers outside of the U.S./Canada, refer to Procedure [[99-205-002 — Service Literature Ordering Location|205-002]] (Service Literature Ordering Location) in Section L for publication ordering information.

Contact a Cummins® Authorized Repair Location for engine fuel system specifications and requirements provided on the Engine Data Sheet for the specific engine and application.

![[oi800kv.png]]

> [!danger] WARNING · Опасно
> If a fuel line shutoff valve is not installed, the overhead tank can drain when the fuel filter is changed, causing an extreme fire hazard.

Cummins Inc., recommends a ball type valve, **not** a gate type valve.

Install a fuel shutoff valve between the fuel filters and the fuel tank.

![[ft8vaca.png]]

Install a check valve in the fuel drain line when the maximum fuel level in the fuel tank is even or above the fuel drain that is in the cylinder head.

Install the valve with the fuel flow arrow toward the fuel tank.

![[06400063.png]]

The QSK45 and QSK60 fuel pump contains an integral check valve in the fuel pump outlet to prevent drain back. An additional check valve is **not** required when the maximum fuel level is above the injector drain, or when the fuel filters are lower than the fuel tank.

![[05600135.png]]

Cummins® diesel engines have been developed to take advantage of the high energy content and generally lower cost of Number 2 diesel fuels. A Cummins® diesel engine will also operate satisfactorily on Number 1 fuels or other fuels within the following specifications. [[3379001 — Fuels for Cummins® Engines|For more detailed fuel recommendations, refer to Fuel for Cummins® Engines, Bulletin 3379001.]]

| Viscosity (ASTM D-445) | 1.3 to 5.8 CentiStoke (1.3 to 5.8 mm² \[0.002 to 0.009 in²\] per second) at 40°C \[104°F\]. |
|---|---|
| Cetane number (ASTM D-613) | 40 minimum above 0°C \[32°F\], 45 minimum below 0°C \[32°F\]. |
| Sulfur content (ASTM D-129 or 1552) | **Not** to exceed 0.5 mass percent. |
| Water and sediment (ASTM D-1796) | **Not** to exceed 0.05 volume percent. |
| Carbon residue (ransbottom ASTM D-524 or D-189) | **Not** to exceed 0.35 mass percent on 10 volume percent residuum. |
| Flash point (ASTM D-93) | 52°C \[125°F\] minimum. Certain marine registries require higher flash points. |
| Density (ASTM D-287) | -1 to 6°C \[30 to 42°F\] A.P.I. gravity at 16°C \[60°F\] (0.816 to 0.876 g/cc at 15°C). |
| Cloud point (ASTM D-97) | 6°C \[10°F\] below lowest temperature expected to operate. |
| Active sulfur-copper strip-corrosion (ASTM D-130) | **Not** to exceed Number 2 rating after 3 hours at 50°C \[122°F\]. |
| Ash (ASTM D-482) | **Not** to exceed 0.02 mass percent (0.05 mass percent with lubricating oil blending). |
| Distillation (ASTM D-86) | At least 90 percent of the fuel **must** evaporate at less than 360°C \[680°F\]. All of the fuel **must** evaporate at less than 385°C \[725°F\]. |
| Acid number | **Not** to exceed 0.1 mg \[3.5 oz\] KOH per 100 ml \[3.4 fl oz\]. |
| Lubricity | [[3379001 — Fuels for Cummins® Engines\|Refer to Fuel for Cummins® Engines, Bulletin 3379001]]. |
