---
type: "Процедура"
doc: "35-011-056"
title_en: "Exhaust System Diagnostics"
modified: "2023-03-02"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "3666322"
figures: 10
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/35/35-011-056.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/35-011-056.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/35"
---

# Exhaust System Diagnostics

> [!abstract] Процедура · `35-011-056`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[3666322 — ISM, ISMe, and QSM11 Service Manual|3666322]]
> **Секции:** Section 11 - Exhaust System - Group 11
> **Даты:** изменён 2023-03-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/35/35-011-056.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/35-011-056.pdf)

### General Information

The following procedure contains troubleshooting steps and information regarding the aftertreatment system.

![[nobox.png]]

Leaks in the exhaust system can cause exhaust odor or white smoke.

Inspect the exhaust piping for leaks, cracks, and loose connections. [[35-010-024-tr — Air Leaks, Air Intake and Exhaust Systems|Refer to Procedure 010-024 in Section 10.]]

Tighten the exhaust clamps, if necessary. Refer to the OEM specifications and the correct torque value.

It may be necessary to perform a stationary (parked) regeneration to locate exhaust leaks. [[101-014-013 — Aftertreatment Testing|Refer to Procedure 014-013 in Section 14.]]

![[10d00395.png]]

The ambient temperature affects the length of time it will take to perform a stationary (parked) regeneration because the engine **must** work harder to increase the exhaust temperatures to the appropriate levels in cold ambient temperatures.

In cold ambient temperatures (approximately -18°C \[0°F\] or colder), stationary (parked) regeneration may take longer to complete. In extremely cold ambient temperatures, stationary (parked) regeneration may **not** complete.

In these cases, it may be necessary to warm the engine to operating temperature before starting the stationary (parked) regeneration, or to move the vehicle to a location with higher ambient temperatures.

![[nobox.png]]

The vehicle manufacturer has the option of installing two switches that control aftertreatment function: the start switch and the permit switch.

The start switch (called the Diesel Particulate Filter Regeneration Start Switch in INSITE™ electronic service tool) is used to start a stationary (parked) regeneration. The vehicle manufacturer may also reference this switch as a "stationary regeneration switch," "start switch," or "parked regeneration switch".

The permit switch (called the Diesel Particulate Filter Permit Switch in INSITE™ electronic service tool) is used to allow the operator to disable active regeneration, if necessary. The vehicle manufacturer may also reference this switch as an "inhibit switch," "stop switch," or "disable switch".

The start switch can be hardwired to the ECM, or it can be multiplexed over J1939 multiplexing.

If the start switch is hardwired, it shares an ECM pin with the diagnostic switch. When the switch is turned ON and the engine is OFF, the ECM interprets this signal as the diagnostic switch. When the switch is turned ON and the engine is running, the ECM interprets this signal as the start switch.

If the start switch is J1939-multiplexed, the signal for this switch is broadcast over the J1939 data link.

A J1939-multiplexed start switch signal has priority over a hardwired start switch signal, therefore if the start switch is enabled over J1939, the hardwired signal is ignored by the engine ECM.

The default setting for the start switch is OFF. If the start switch is enabled to INSITE™ electronic service tool, but no switch is installed (either hardwired of J1939-multiplexed), the switch status will remain OFF.

The position of the start switch can be monitored with INSITE™ electronic service tool in the data monitor/logger screen.

The default setting for the permit switch is ENABLED.

If the permit switch is enabled with INSITE™ electronic service tool, but no switch is installed (either hardwired or J1939 multiplexed), the switch status will remain OFF.

If the vehicle is operated for an extended period of time with the permit switch OFF, fault codes for the above normal levels of aftertreatment diesel particulate filter soot load may result (Fault Codes 1921, 1922, and 2639).

If the aftertreatment diesel particulate filter soot load reaches the moderately severe level (Fault Code 2639), and the permit switch is OFF, the ECM will also log a Fault Code 2777.

If the permit switch is multiplexed, and therefore ENABLED, in the J1939 section of Features and Parameters in INSITE™ electronic service tool, it **must** also be enabled in the aftertreatment section of Features and Parameters in INSITE™ electronic service tool. If it is **not**, regeneration will be inhibited.

The permit switch can be hardwired to the ECM **only** in emergency vehicle calibrations. For all other non-emergency calibrations, the permit switch can **only** be J1939-multiplexed over the J1939 data link.

In emergency vehicle calibrations where the permit switch is hardwired, the permit switch replaces the governor type switch.

A J1939-multiplexed permit switch signal has priority over a hardwired start switch signal, so if the permit switch is enabled over J1939, the hardwired signal is ignored by the engine ECM.

The position of the permit switch can be monitored with INSITE™ electronic service tool in the data monitor/logger screen:

- When the permit switch is ON, active regeneration is allowed.
- When the permit switch is OFF, active regeneration is **not** allowed.

![[11d00294.png]]

If the aftertreatment exhaust gas temperature sensors are **not** connected properly, or if the wiring in the harness between the engine and aftertreatment is **not** correct, the engine may experience frequent Diesel Particulate Filter lamp illuminations, or stationary (parked) regenerations that do **not** complete.

Inspect the exhaust aftertreatment temperature sensor connectors to verify they are connected to the correct connector on the aftertreatment system wiring harness. Two of the temperature sensors have identical wiring harness connectors. Because the sensors are the same part number, it is possible to install the wiring harness connectors to the wrong sensor.

To verify the correct sensor locations, use INSITE™ electronic service tool to monitor the following parameters with the ignition key ON, but with the engine **not** running.

- Aftertreatment Diesel Oxidation Catalyst Inlet Temperature Sensor Signal Voltage (V)
- Aftertreatment Diesel Particulate Filter Inlet Temperature Sensor Signal Voltage (V)
- Aftertreatment Diesel Particulate Filter Outlet Temperature Sensor Signal Voltage (V).

Unplug each of the aftertreatment exhaust gas temperature sensors, one at a time.

If the voltage changes when the sensor is unplugged, the wiring harness connector is connected to the correct sensor.

If the voltage does **not** change when the sensor is unplugged, switch the connector location to the other temperature sensor, unplug it, and check for a voltage change.

An incorrectly assembled aftertreatment wiring harness can **not** be checked by unplugging each of the aftertreatment exhaust gas temperature sensors.

The **only** method to check for a misassembled aftertreatment wiring harness is to check the wiring harness connectors for correct pin installation. Refer to the engine wiring diagram for connector pin identification and location.

![[19c01217.png]]

When performing a stationary (parked) regeneration, monitor the exhaust temperatures in the aftertreatment to determine why a stationary (parked) regeneration will **not** complete.

Possible causes for stationary (parked) regenerations that will **not** complete include:

- Misassembled aftertreatment wiring harness
- High resistance in exhaust gas temperature sensor return circuit
- Aftertreatment exhaust gas temperature sensors installed in the wrong location
- A plugged aftertreatment diesel oxidation catalyst
- A malfunctioning turbocharger.

A normal stationary (parked) regeneration will follow the pattern shown.

- The dashed line is for the aftertreatment diesel oxidation catalyst inlet temperature sensor.
- The dotted line is for the aftertreatment diesel particulate filter inlet temperature sensor.
- The solid line is for the aftertreatment diesel particulate filter outlet temperature sensor.

When the stationary (parked) regeneration begins (1), all three temperatures should be approximately the same, and should increase at the same rate.

The wiring to the aftertreatment temperature sensors appears to be correct in this example because they all read approximately the same temperature at the beginning of the stationary (parked) regeneration and increase at the same rate.

Aftertreatment injection begins when all three temperatures reach approximately 288°C \[550°F\] (2).

Once aftertreatment injection begins, the aftertreatment diesel oxidation catalyst inlet temperature may vary slightly, but will typically remain between 260 and 399°C \[500 and 750°F\].

The aftertreatment diesel particulate filter inlet and outlet temperatures will increase to approximately 482 to 649°C \[900 to 1200°F\]. The temperatures may vary during the stationary (parked) regeneration as the amount of fuel injected during aftertreatment injection is changed to maintain a constant temperature.

The aftertreatment diesel particulate filter inlet and outlet temperatures will remain at this temperature for the duration of the stationary (parked) regeneration.

![[11d00299.png]]

This graph illustrates a stationary (parked) regeneration where the inlet of the aftertreatment diesel oxidation catalyst is blocked.

- The dashed line is for the aftertreatment diesel oxidation catalyst inlet temperature sensor.
- The dotted line is for the aftertreatment diesel particulate filter inlet temperature sensor.
- The solid line is for the aftertreatment diesel particulate filter outlet temperature sensor.

In this condition, the engine speed will increase to the stationary (parked) regeneration speed of 1000 to 1400 rpm.

Raising the aftertreatment temperature to the aftertreatment injection temperature may take longer to complete than normal if the inlet to the aftertreatment diesel oxidation catalyst is plugged, restricting some of the exhaust flow.

Once aftertreatment injection begins (2), the aftertreatment diesel particulate filter inlet and outlet temperatures will differ greatly due to the plugged aftertreatment diesel oxidation catalyst being unable to oxidize the injected fuel. The aftertreatment diesel particulate filter has some capability to oxidize the injected fuel, but can **not** maintain this condition without damaging the filter material over time. It is possible that white smoke would be present from the vehicle tailpipe during this condition.

The wiring to the aftertreatment temperature sensors appears to be correct in this example because they all read approximately the same temperature at the beginning of the stationary (parked) regeneration and they increase at the same rate.

The possible cause of this condition is a plugged aftertreatment diesel oxidation catalyst. Use the following procedure to inspect the aftertreatment diesel oxidation catalyst. [[101-011-049-tr — Aftertreatment Diesel Oxidation Catalyst|Refer to Procedure 011-049 in Section 11.]]

![[11d00300.png]]

This graph illustrates a stationary (parked) regeneration where the engine can **not** build enough heat to start aftertreatment injection.

- The dashed line is for the aftertreatment diesel oxidation catalyst inlet temperature sensor.
- The dotted line is for the aftertreatment diesel particulate filter inlet temperature sensor.
- The solid line is for the aftertreatment diesel particulate filter outlet temperature sensor.

The engine speed will likely increase to the stationary (parked) regeneration speed of 1000 to 1400 rpm, but because the aftertreatment temperatures do **not** increase enough to start aftertreatment injection, the stationary (parked) regeneration will **not** complete.

Possible causes of this issue include:

- High resistance in the exhaust gas temperature sensor return circuit. Use the following procedure in the ISX CM871 and ISM CM876 Electronic Control System Troubleshooting and Repair Manual, Bulletin 4021560. Refer to Procedure 019-360 in Section 19.
- A malfunctioning turbocharger. Use the following procedure to verify the turbocharger sector gear has full travel. [[35-010-134 — Variable Geometry Turbocharger Actuator, Electric|Refer to Procedure 010-134 in Section 10.]]
- Low ambient temperatures. Move the vehicle to a location with higher ambient temperatures.

![[11d00301.png]]

This graph illustrates a stationary (parked) regeneration where the wiring to the aftertreatment temperature sensors is incorrect.

- The dashed line is for the aftertreatment diesel oxidation catalyst inlet temperature sensor.
- The dotted line is for the aftertreatment diesel particulate filter inlet temperature sensor.
- The solid line is for the aftertreatment diesel particulate filter outlet temperature sensor.

In this condition, the engine speed will increase to the stationary (parked) regeneration speed of 1000 to 1400 rpm.

Aftertreatment injection will **not** occur in this condition because the aftertreatment diesel oxidation catalyst inlet temperature does **not** reach the required temperature. Because aftertreatment injection is **not** occurring, the aftertreatment temperatures should **not** read differently.

The possible cause of this condition is an incorrectly assembled aftertreatment wiring harness. See the aftertreatment exhaust gas temperature sensor wiring section of this procedure.

![[11d00302.png]]

This graph illustrates a stationary (parked) regeneration where the connectors to the aftertreatment diesel oxidation catalyst inlet temperature sensor and the aftertreatment diesel particulate filter outlet temperature sensor are reversed.

- The dashed line is for the aftertreatment diesel oxidation catalyst inlet temperature sensor.
- The dotted line is for the aftertreatment diesel particulate filter inlet temperature sensor.
- The solid line is for the aftertreatment diesel particulate filter outlet temperature sensor.

In this condition, the engine speed will increase to the stationary regeneration speed of 1000 to 1400 rpm.

Aftertreatment injection may occur in this condition (2). However, the aftertreatment diesel oxidation catalyst inlet temperature increases after aftertreatment injection begins, while the aftertreatment diesel particulate filter outlet temperature remains constant.

The possible cause of this condition is that the connectors to the aftertreatment diesel oxidation catalyst inlet temperature sensor and the aftertreatment diesel particulate filter outlet temperature sensor are reversed. See the aftertreatment exhaust gas temperature sensor wiring section of this procedure.

![[11d00303.png]]

A regeneration that will **not** complete can be caused by malfunctions in the EGR, variable geometry turbocharger systems, or fueling. These malfunctions do **not** allow the aftertreatment to reach the necessary temperatures for aftertreatment fuel injection.

When performing a stationary (parked) regeneration, monitor the following parameters to determine why a stationary (parked) regeneration will **not** complete:

- EGR Differential Pressure
- EGR Valve Position Measured (Percent Open)
- Exhaust Gas Pressure
- Intake Manifold Pressure
- Percent Load under Turbocharger Actuator Position Measured (Percent Closed)
- Turbocharger Speed

During a stationary (parked) regeneration, these are the typical values for a healthy system.

- EGR Differential Pressure - Less than 12.7 mm-Hg \[0.5 in-Hg\]
- EGR Valve Position Measured (Percent Open) - less than one percent
- Exhaust Gas Pressure – 103 to 161 in-Hg \[350 to 507 kPa\]
- Intake Manifold Pressure – 7 to 11 in-Hg \[25 to 37 kPa\]
- Percent Load - Less than 12 percent
- Turbocharger Actuator Position Measured (Percent Closed) – 89-100 percent
- Turbocharger Speed – 45,000 to 78,000 rpm

During a stationary (parked) regeneration, the EGR valve should be closed to help increase the load on the engine.

A leaking EGR valve can be detected by monitoring the EGR Differential Pressure while the EGR valve is closed.

If the EGR Differential Pressure exceeds 12.7 mm-Hg \[0.5 in-Hg\] while the EGR Valve Position Measure (Percent Open) is one percent during the stationary (parked) regeneration, a leaking EGR valve has been detected.

Clean and inspect the EGR valve for reuse. [[35-011-022-tr — EGR Valve|Refer to Procedure 011-022]] in Section 11.

During a stationary (parked) regeneration, the turbocharger also closes to help increase the load on the engine.

If the Turbocharger Actuator Position Measured (Percent Closed) is **not** within 89 to 100 percent, or, the exhaust gas pressure is **not** within 103 in-Hg to 161 in-Hg \[ 350 kPa to 507 kPa \] a malfunction of the variable geometry turbocharger is the likely cause of the stationary (parked) regeneration that will **not** complete.

Check the variable geometry turbocharger shroud plate and nozzle ring for damage or wear. [[35-010-033-tr — Turbocharger|Refer to Procedure 010-033]] in Section 10.

During a stationary (parked) regeneration, the percent load on the engine will fluctuate until the engine and aftertreatment reach a steady condition. Once the engine stabilizes, the percent load should **not** exceed 12 percent during the stationary (parked) regeneration.

> [!note] Note · Примечание
> The percent load may fluctuate when the engine fan cycles ON and OFF.
