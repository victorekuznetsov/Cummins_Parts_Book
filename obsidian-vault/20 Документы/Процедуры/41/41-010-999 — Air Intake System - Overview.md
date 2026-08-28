---
aliases:
  - "Система впуска воздуха — обзор"
type: "Процедура"
doc: "41-010-999"
title_en: "Air Intake System - Overview"
title_ru: "Система впуска воздуха — обзор"
modified: "2003-08-26"
engines:
  - "93058669"
  - "93087701"
families:
  - "C8.3 · 6C8.3"
manuals:
  - "3666003"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/41/41-010-999.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/41-010-999.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "группа/41"
---

# Air Intake System - Overview
**Система впуска воздуха — обзор**

> [!abstract] Процедура · `41-010-999`
> **Двигатели:** [[93058669 — 6C8.3 CPL 3105|93058669]], [[93087701 — 6C8.3 CPL 3105|93087701]]
> **Семейство:** C8.3 · 6C8.3
> **Входит в руководства:** [[3666003 — C Troubleshooting and Repair Manual|3666003]]
> **Секции:** Section F - Familiarization
> **Даты:** изменён 2003-08-26
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/41/41-010-999.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/41-010-999.pdf)

### General Information

Air is pulled into the engine through an air filter. Clean air is very important to the life of the engine; dust and dirt can damage the cylinders very quickly.

Make sure that a high-quality air cleaner is used and that it is periodically replaced according to the manufacturer's recommendations.

Intake air for the naturally-aspirated engine flows through the air cleaner into the intake manifold. From the intake manifold, the air is pulled into the cylinders and used for combustion. After combustion, it is forced out of the cylinders and through the exhaust manifold.

On turbocharged engines, the intake air is drawn through the air cleaner into the compressor side of the turbocharger, through the crossover tube, and into the intake manifold. From the intake manifold, the air is forced into the cylinders and used for combustion.

On turbocharged engines, the energy from the exhaust is used to drive the turbine wheel of the turbocharger. The turbine wheel and shaft drive the compressor wheel, which forces more air into the cylinders for combustion. The additional air provided by the turbocharger allows more fuel to be injected to increase the power output of the engine.

On turbocharged, aftercooled engines, intake air from the turbocharger flows through the cooling fins of the aftercooler before entering the intake manifold. The cooled air becomes more dense and contains more oxygen; which allows more fuel to be injected, further increasing the power output from the engine.

The 1991 to 1994 automotive engines use a chassis-mounted charge-air cooler, rather than an engine-mounted aftercooler, to provide cooler intake air to the engine. This improves the engine performance and reduce emissions. The charger-air cooler system uses large piping to transfer the air from the turbocharger to the charge-air cooler; then to the engine intake manifold.

> [!note] Note · Примечание
> The long-term integrity of the charge-air cooling system is the responsibility of the vehicle and component manufacturers.

Some turbocharged engines use a wastegate turbocharger to limit the maximum boost pressure that the turbocharger can develop. Wastegate operation is controlled by an actuator that senses intake manifold pressure and balances it against a preset spring-load.

The wastegate valve is located in the turbine inlet passage. When open, it diverts a portion of the exhaust gas around the turbine wheel, thereby controlling the shaft speed and boost.

> [!warning] CAUTION · Осторожно
> The turbocharger is a performance part and must not be tampered with. The wastegate bracket is an integral part of the turbocharger. Tampering with the wastegate components can reduce durability by increasing cylinder pressure and thermal loading because of incorrect inlet and exhaust manifold pressure. Poor fuel economy and failure to meet regulatory emissions laws can result. Increasing the turbocharger boost will not increase engine power.

The turbine wheel, compressor wheel, and shaft are supported by two rotating bearings in the bearing housing. Passages within the bearing housing direct filtered, pressurized engine oil to the shaft bearings and thrust bearing. The oil is used to lubricate and cool the rotating components to provide for smooth operation. The oil then drains from the bearing housing to the engine sump through the oil drain line. A restricted or damaged oil drain line can cause the turbocharger bearing housing to be pressurized, causing oil to leak past the seals.

> [!note] Note · Примечание
> An adequate supply of good filtered oil is very important to the life of the turbocharger. Make sure that a high-quality oil is used and that the oil and oil filter are changed according to the maintenance recommendations.

> [!warning] CAUTION · Осторожно
> A catalyst is installed on all EPA- and CARB-approved automotive applications. Lubricating oil blending is not permitted. It will plug up and eventually damage the catalyst. High-sulfur fuels must not be used with the catalyst. No welding or modifications of the catalyst are permitted without permission of the catalyst manufacturer.

### Theory of Operation

White smoke indicates cold combustion/cold engine operation. The intake manifold heater control module monitors the intake air temperature, engine rpm and keyswitch voltage.

The intake manifold heater elements operate in the preheat, post heat, and post heat recycle modes.

- In preheat, the ignition switch is in the RUN position but the engine has **not** been started.
- In post heat and post heat recycle, the engine is operating.

The proper operation of the intake manifold heater system and starting procedures will prevent excessive engine starter motor use and minimize white exhaust smoke when the engine is first started.

> [!danger] WARNING · Опасно
> Ether starting systems or manually-induced starting fluids must not be used with electric air heater systems.

On C series marine applications, there are three phases of intake air heater operation: preheat (with keyswitch ON and engine **not** operating), post heat (after a successful engine start), and post heat recycle (after the termination of the post heat).

The preheat phase also controls the Optional WAIT TO START lamp to signify to the operator when it is appropriate to begin cranking the engine. In order to allow maximum current to be used by the starter, the heater elements are de-energized during cranking. The amount of time the heater stays in preheat, post heat, and post heat recycle is determined by the intake manifold temperature.

There is no preheat cycle above 35°C \[95°F\], no post heat cycle above 24°C \[75°F\] and no post heat recycle above the maximum duration for preheat and post heat (20 seconds) and post heat recycle (20 minutes). When the air intake temperature is below 35°C \[95°F\], the heating elements are energized in the preheat and post heat cycles, the voltage system current draw is approximately 200 amperes for a 12-VDC system and 100 amperes for a 24-VDC system.

During the post heat recycle mode the heater elements are energized in five-second intervals for a maximum duration of 20 minutes. There are three optional conditions that will interrupt the post heat recycle mode: Out of voltage range, exceeding operational rpm, and air intake temperature above 35°C \[95°F\]. Once the grid heater post heat recycle mode terminates because of timing out or over/under keyswitch voltage, the grid heater will **not** come back on unless the keyswitch has been cycled from OFF to ON.

If the engine rpm is advanced above the maximum set point (950 rpm for B series and 1200 rpm for C series engines), the post heat recycle will be terminated. Once the engine rpm is adjusted below maximum set point and air intake temperature is below 35°C \[95°F\], the post heat recycle will reset back to the beginning of the 20-minute cycle.

| Heater Cycle Chart |  |  |  |
|---|---|---|---|
| Battery voltage above 10.5 to 17 for 12-VDC |  |  |  |
| Rpm: (B) 450 to 950, (C) 350 to 1200 |  |  |  |
| Engine Intake Manifold Temperature | Preheat Cycle Time Ignition Keyswitch ON before Crank Cycle | Postheat Cycle Occurs Ignition Keyswitch ON after Crank Cycle | Recycle Mode (After Post Heat) |
| Above 35°C \[95°F\] | None | None | None |
| 24 to 35°C \[75 to 95°F\] | 10 seconds | None | 25/75% (1) |
| 15.6 to 23°C \[60 to 75°F\] | 10 seconds | 20 seconds | 50/50% (2) |
| 1 to 15.5°C \[32 to 60°F\] | 15 seconds | 20 seconds | 50/50% (2) |
| Below 0°C \[32°F\] | 20 seconds | 20 seconds | 50/50% (2) |

| Heater Operating Modes (Parameter) |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|
| Recycle Mode 12-VDC | Element (Heater) | 5-Second Time Intervals |  |  |  |  |  |  |
| (1) 25/75% | 1 | On | Off | Off | Off | On | Off | Off |
| 2 | Off | Off | On | Off | Off | Off | On |  |
| (2) 50/50% | 1 | On | Off | On | Off | On | Off | On |
| 2 | Off | On | Off | On | Off | On | Off |  |

| Recycle Mode 24-VDC | Element (Heater) | 5-Second Time Intervals |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|
| (1) 25/75% | 1 | On | Off | Off | Off | On | Off | On |
| (2) 50/50% | 1 | On | Off | On | Off | On | Off | On |

The intake manifold heater option is installed between the aftercooler and intake manifold. The heater is totally electrically operated. The intake manifold heater aids in reducing white smoke at startup and the engine's startability at colder temperatures. Components required to operate the intake heater are:

- Ignition keyswitch
- Heater control module
- Temperature sensor
- Solenoids
- Intake heater grids
- Engine speed sensor
- Wiring.

The intake heater system operates in three modes as follows:

Preheat Cycle

The heater control module receives and monitors supply voltage from the keyswitch.

The heater control module receives electrical signals from sensors mounted on the engine.

The temperature sensor senses intake air manifold temperature and provides input to the heater control module circuit. Temperatures below 35°C \[95°F\] activate the heater control module heater circuit. This is known as the preheat cycle.

The heater control module provides signal voltage to active the air heater solenoids. A cable connected to the battery side of the starter solenoid provides supply current/voltage to the air heater solenoid.

Intake air temperatures sensed by the temperature sensor dictate different preheat cycle times, up to a maximum of 20 seconds.

Both elements heat during this cycle.

After the preheat cycle, the starter can be engaged to start the engine.

If the starter is engaged before the cycle time is complete, the heater control module will automatically shut off the elements during cranking.

Post Heat Cycle

The engine speed sensor on the flywheel housing senses engine speed and activates the post heat cycle within a specified rpm range.

The engine **must** be operating in a given range.

Battery voltage is monitored by the heater control module system.

The temperature sensor continues to monitor intake air temperature.

This cycle can continue for up to 20 seconds maximum and does **not** have a rpm cutout.

Both elements heat during this cycle.

Post Heat Recycle

The post heat recycle mode occurs for a maximum of 20 minutes; as long as the heater control module senses specified range of the air temperature, voltage, and rpm.

The post heat recycle activates the heater elements in two sequence modes:

- 25/75: Both elements alternately cycle on and off with a five-second delay between element activation. Each activation lasts for five seconds. **Only** one element is activated at a time on a 12-VDC system.
- 50/50: Both elements cycle on and off for five seconds. **Only** one element is activated at a time.

Post heat recycle operates for a maximum of 20 minutes. This operating cycle can be interrupted at any time, if any one of the following conditions occur:

1. Engine exceeds specified rpm, intake air temperature, or voltage range
2. Intake manifold temperature exceeds 35°C \[95°F\]
3. Heater control module battery sensing voltage below 10.5 VDC or above 17 VDC.

If the post heat recycle is interrupted during its 20-minute cycle, the cycle will restart, and reset for another 20 minutes if all of the following conditions occur:

1. Engine below 1000 rpm
2. Intake manifold temperature below 30°C \[85°F\]
3. Heater control module battery sensing voltage between 10.5 and 17 VDC.

Once the 20 minutes of post heat recycle has ended, the ignition key **must** be turned to the OFF position and back to the RUN position to restart the air heater cycles again.
