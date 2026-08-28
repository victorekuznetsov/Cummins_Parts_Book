---
aliases:
  - "Топливная система — обзор"
type: "Процедура"
doc: "20-005-999-tr"
title_en: "Fuel System - Overview"
title_ru: "Топливная система — обзор"
modified: "2006-06-30"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4021592"
figures: 12
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/20/20-005-999-tr.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/20-005-999-tr.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/20"
---

# Fuel System - Overview
**Топливная система — обзор**

> [!abstract] Процедура · `20-005-999-tr`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021592 — QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual|4021592]]
> **Секции:** Section F - Familiarization
> **Даты:** изменён 2006-06-30
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/20/20-005-999-tr.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/20-005-999-tr.pdf)

### General Information

with Mechanically Actuated Injector

> [!danger] WARNING · Опасно
> Depending on the circumstance, fuel is flammable. Keep all cigarettes, flames, pilot lights, arcing equipment, and switches out of the work area and areas sharing ventilation to avoid severe personal injury or death when working on the fuel system.

> [!warning] CAUTION · Осторожно
> Tampering with the fuel pump can void the engine warranty, lower engine performance, and be a violation of law.

The QSK fuel system is used on the QSK19 engine. Additional information about the QSK fuel system is available in the Troubleshooting and Repair Manual, Electronic Control Fuel System, QSK19, QSK23, QSK45, QSK60, and QSK78 Engines, Bulletin [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]].

> [!note] Note · Примечание
> Warranty repairs are **not** to be made to the fuel pump unless the work is performed in a shop meeting all requirements established by Cummins Inc. to accurately calibrate, test and repair the fuel systems on Cummins® engines.

![[06400099.png]]

The performance of the engine is defined by the control parts list (CPL) and the fuel pump code. The fuel pump calibration **must** be within published specifications. Fuel pump calibration is certified by several emissions agencies.

The QSK fuel system with mechanically actuated injectors uses a PT type fuel pump to supply a linear gear pump pressure from 414 kPa \[60 psi\] at 600 rpm to 1931 kPa \[280 psi\] at 2100 rpm to the electronic fuel control valve assembly.

![[05400009.png]]

The QSK fuel pump throttle shaft is locked in the full closed position.

There is **no** mechanical throttle on the QSK fuel pump.

![[05400010.png]]

The QSK fuel pump does **not** contain an air fuel control valve (AFC) valve. The pump **only** has an air fuel control (AFC) cover plate.

![[05400011.png]]

The electronic fuel control valve assembly is located on the fuel pump side of the engine.

The electronic fuel control valve assembly includes:

- Timing and rail pressure sensors
- Timing and rail actuators
- Fuel shutoff valve
- Ambient air pressure sensor
- Fuel inlet and outlet connections.

The electronic fuel control valve contains the following components:

1. Timing actuator
2. Fuel shutoff valve
3. Rail actuator
4. Ambient air pressure sensor
5. Rail pressure sensor
6. Timing pressure sensor
7. Fuel rail supply line connector
8. Fuel timing supply line connector
9. Fuel control supply line connector.

![[05400012.png]]

The lubricating oil scavenge pump (A) **must** be removed prior to removing the fuel pump (B) to allow access to the fuel pump mounting capscrews.

The fuel pump (B) **must** be installed prior to installing the lubricating oil scavenge pump (A).

![[17400021.png]]

with Electronically Actuated Injector

The fuel system for the QSK19 engine is equipped with a modular common rail fuel system. The system provides full electronic control of the engine with high-pressure fuel injection.

![[05400240.png]]

The fuel pump consists of two pumps:

- The primary pump (1) is a two piston pump that provides a constant fuel supply to the injectors. The pump is lubricated by the engine oil system. An inlet metering valve controls the fuel supply to the pump depending on the amount of power that is being required. For excess fuel, a mechanical dump valve (6) relieves excess fuel from the pump and returns it to the fuel tank. A pressure sensor (7) provides a signal to the ECM to monitor the pressure from the pump.
- A second pump (2) located on the back is a gerotor style pump that takes fuel from the stage one filter and sends it through the ECM cooling plate and stage two filter. The cover plate (4) also contains the pressure regulator for the gerotor pump. An o-ring (3) provides a seal to prevent leaks.

The fuel pump delivers approximately 1600 bar \[23,000 psi\] to the injectors, which eliminates the need for mechanical injection. The rocker arm, push tube, cam follower, and cam lobe have been eliminated. Injection is controlled electronically through the ECM. The fuel filter head assembly contains a two-stage filtration system. The first stage contains a 7 micron fuel filter. The first stage filter also has a water drain valve and water in filter sensor. The sensor is connected to the ECM and will alert the operator with a check engine lamp if water is present. The second stage contains a 3 micron fuel filter. The electric lift pump operates **only** during cranking to aid in starting.

A fuel temperature sensor and pressure sensor are located in the fuel filter head so the ECM can monitor the condition of the fuel.

![[05400240.png]]

### Installation Recommendations

Installation publications are available to provide fuel system installation recommendations approved by Cummins Inc. Refer to Procedure [[20-205-001-tr — Additional Service Literature|205-001]] for publication ordering information.

Contact the nearest Cummins Authorized Repair Location for engine fuel system specifications and requirements provided on the Engine Data Sheet for your specific engine and application.

![[oi800kv.png]]

> [!danger] WARNING · Опасно
> Depending on the circumstance, fuel is flammable. When performing any or all of the following procedures to remove fuel supply lines and related components, keep all cigarettes, flames, pilot lights, arcing equipment, and switches out of the work area and areas sharing ventilation to reduce the possibility of severe personal injury or death when working on the fuel system.

> [!danger] WARNING · Опасно
> If a fuel line shutoff valve is not installed, the overhead tank can drain when the fuel filter is changed, causing an extreme fire hazard.

Cummins Inc., recommends a ball-type valve and **not** a gate-type valve for the overhead tank installation.

Install a fuel shutoff valve between the filter and the fuel tank.

![[ft8vaca.png]]

Install a check valve in the fuel drain line when the maximum fuel level in the fuel tank is even or above the fuel drain that is in the cylinder head. Install the valve with the fuel flow arrow toward the fuel tank.

![[06400063.png]]

The QSK fuel pump for mechanically actuated injectors contains an integral check valve in the fuel pump outlet. An additional check valve is **not** required when the maximum fuel level is above the injector drain, or when the fuel filters are lower than the fuel tank.

![[05400026.png]]

Cummins diesel engines have been developed to take advantage of the high energy content and generally lower cost of number 2 diesel fuels. A Cummins diesel engine will also operate satisfactorily on number 1 fuels or other fuels within the following specifications. For more detailed fuel recommendations, refer to Fuel for Cummins Engines, Bulletin [[3379001 — Fuels for Cummins® Engines|3379001]].
