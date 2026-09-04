---
type: "Процедура"
doc: "493-011-056"
title_en: "Exhaust System Diagnostics"
modified: "2021-04-27"
manuals:
  - "5411181"
figures: 14
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/493/493-011-056.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/493-011-056.pdf"
tags:
  - "документ/процедура"
  - "группа/493"
---

# Exhaust System Diagnostics

> [!abstract] Процедура · `493-011-056`
> **Входит в руководства:** [[5411181 — X15 CM2350 X114B - Efficiency Series Service Manual|5411181]]
> **Секции:** Section 11 - Exhaust System - Group 11
> **Даты:** изменён 2021-04-27
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/493/493-011-056.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/493-011-056.pdf)

### Select Service Tools

#### Recommended Cummins® Service Tool

- Diesel exhaust fluid (DEF) refractometer, Part Number 4919318, or equivalent
- DEF Contamination Test Kit, Part Number 5298935
- Cummins® electronic service tool or equivalent

#### Additional Service Items

- No additional service items required.

### General Information

The following procedure contains troubleshooting steps and information regarding the aftertreatment system.

Leaks in the exhaust system can cause exhaust odor or white smoke.

Inspect the exhaust piping for leaks, cracks, and loose connections.

Tighten the exhaust clamps, if necessary. See equipment manufacturer service information for the correct torque value.

It can be necessary to perform a stationary regeneration to locate exhaust leaks. [[493-014-016 — Aftertreatment Diesel Particulate Filter (DPF) Regeneration Test|Refer to Procedure 014-016 in Section 14.]]

![[10d00395.png]]

The ambient temperature affects the length of time it will take to perform a stationary (parked or non-mission) regeneration because the engine must work harder to increase the exhaust temperatures to the appropriate levels in cold ambient temperatures.

In cold ambient temperatures (approximately -18°C \[0°F\] or colder), stationary regeneration may take longer to complete. In extremely cold ambient temperatures, stationary regeneration may **not** complete.

In these cases, it may be necessary to warm the engine to operating temperature before starting the stationary regeneration, or to move the vehicle to a location with higher ambient temperatures.

![[14d00035.png]]

The vehicle manufacturer has the option of installing two switches that control aftertreatment function: the start switch and the permit switch.

The start switch (called the Diesel Particulate Filter (DPF) Regeneration Start Switch in the recommended Cummins® electronic service tool or equivalent) is used to start a stationary regeneration. The vehicle manufacturer may also reference this switch as a "stationary regeneration switch," "start switch," "non-mission regeneration," or "parked regeneration switch".

The permit switch (called the Diesel Particulate Filter Permit Switch in the electronic service tool) is used to allow the operator to disable active regeneration, if necessary. The vehicle manufacturer may also reference this switch as an "inhibit switch," "stop switch," or "disable switch".

The start switch can be hardwired to the engine control module (ECM), or it can be multiplexed over J1939 multiplexing.

If the start switch is hardwired, it shares an ECM pin with the diagnostic switch. When the switch is turned ON and the engine is OFF, the ECM interprets this signal as the diagnostic switch. When the switch is turned ON and the engine is operating, the ECM interprets this signal as the start switch.

If the start switch is J1939-multiplexed, the signal for this switch is broadcast over the J1939 data link.

A J1939-multiplexed start switch signal has priority over a hardwired start switch signal. Therefore, if the start switch is enabled over J1939, the hardwired signal is ignored by the engine ECM.

The default setting for the start switch is OFF. If the start switch is enabled with the electronic service tool, but no switch is installed (either hardwired or J1939-multiplexed), the switch status will remain OFF.

The position of the start switch can be monitored with the electronic service tool in the Data Monitor/Logger screen.

The default setting for the permit switch is enabled.

If the permit switch is enabled with the electronic service tool, but no switch is installed (either hardwired or J1939 multiplexed), the switch status will remain OFF.

If the vehicle is operated for an extended period of time with the permit switch OFF, fault codes for the above normal levels of aftertreatment DPF soot load can result (Fault Codes 1921, 1922, and 2639).

If the aftertreatment DPF soot load reaches an above normal level (Fault Code 1921, 1922, and 2639), and the permit switch is OFF, the ECM will log Fault Code 2777. The ECM will also log Fault Code 2777 if the ECM is requesting active regeneration of the aftertreatment and the permit switch is OFF.

If the permit switch is multiplexed, and therefore enabled, in the J1939 section of Features and Parameters in the electronic service tool, it **must** also be enabled in the aftertreatment section of Features and Parameters in the electronic service tool. If it is **not**, regeneration will be inhibited.

A J1939-multiplexed permit switch signal has priority over a hardwired permit switch signal, so if the permit switch is enabled over J1939, the hardwired signal is ignored by the engine ECM.

The position of the permit switch can be monitored with the electronic service tool in the Data Monitor/Logger screen:

- When the permit switch is ON, active regeneration is allowed.
- When the permit switch is OFF, active regeneration is **not** allowed.

> [!note] Note · Примечание
> If there is no permit switch installed and the permit switch is disabled in the J1939 section and the aftertreatment section of Features and Parameters in the electronic service tool, the permit switch status in the Data Monitor/Logger screen will show the permit switch is OFF, but active regeneration will be allowed.

![[11d00294.png]]

> [!note] Note · Примечание
> This step describes possible incorrect aftertreatment exhaust gas temperature sensor wiring conditions.

The aftertreatment sensors link to the ECM over J1939. See the appropriate fault code troubleshooting manual to diagnose and troubleshoot fault codes.

To verify the original equipment manufacturer (OEM) wiring harness and the temperature sensors, use the electronic service tool to monitor the following parameters with the engine operating. Verify they increase from room temperature.

- Aftertreatment diesel oxidation catalyst (DOC) intake temperature
- Aftertreatment DPF intake temperature
- Aftertreatment DPF outlet temperature
- Aftertreatment selective catalytic reduction (SCR) outlet temperature.

If any of the parameters do **not** show a temperature as expected, check the aftertreatment wiring and connections to the sensor(s).

When performing a stationary regeneration, monitor the exhaust temperatures in the aftertreatment to determine why a stationary regeneration will **not** complete.

Possible causes for stationary regenerations that will **not** complete include:

- Misassembled OEM wiring harness
- A plugged aftertreatment DOC
- A malfunctioning turbocharger.

A normal stationary regeneration will follow the pattern shown.

- The dashed line is for the aftertreatment DOC inlet temperature sensor
- The dotted line is for the aftertreatment DPF inlet temperature sensor
- The solid line is for the aftertreatment DPF outlet temperature sensor.

When the stationary regeneration begins (1), all three temperatures should be approximately the same, and should increase at the same rate.

The wiring to the aftertreatment temperature sensors appears to be correct in this example because they all read approximately the same temperature at the beginning of the stationary regeneration and increase at the same rate.

Aftertreatment injection begins when all three temperatures reach approximately 288°C \[550°F\] (2).

Once aftertreatment injection begins, the aftertreatment DOC inlet temperature can vary slightly, but will typically remain between 260 and 399°C \[500 and 750°F\].

The aftertreatment DPF inlet and outlet temperatures will increase to approximately 482 to 649°C \[900 to 1200°F\]. The temperatures may vary during the stationary regeneration as the amount of fuel injected during aftertreatment injection is changed to maintain a constant temperature.

The aftertreatment DPF inlet and outlet temperatures will remain at this temperature for the duration of the stationary regeneration.

![[11d00299.png]]

This graph illustrates a stationary regeneration where the inlet of the aftertreatment DOC is blocked (1).

- The dashed line is for the aftertreatment DOC inlet temperature sensor.
- The dotted line is for the aftertreatment DPF inlet temperature sensor.
- The solid line is for the aftertreatment DPF outlet temperature sensor.

In this condition, the engine speed will increase to the stationary regeneration speed of 1000 revolutions per minute (rpm).

Raising the aftertreatment temperature to the aftertreatment injection temperature may take longer to complete than normal if the inlet to the aftertreatment DOC is plugged, restricting some of the exhaust flow.

Once aftertreatment injection begins (2), the aftertreatment DPF inlet and outlet temperatures will differ greatly due to the plugged aftertreatment DOC being unable to oxidize the injected fuel. The aftertreatment DPF has some capability to oxidize the injected fuel, but can **not** maintain this condition without damaging the filter material over time. It is possible white smoke would be present from the vehicle tailpipe during this condition.

The wiring to the aftertreatment temperature sensors appears to be correct in this example because they all read approximately the same temperature at the beginning of the stationary regeneration and they increase at the same rate.

The possible cause of this condition is a plugged aftertreatment DOC. Use the following procedure to inspect the aftertreatment DOC. [[493-011-049 — Aftertreatment Diesel Oxidation Catalyst|Refer to Procedure 011-049 in Section 11.]]

![[11d00300.png]]

This graph illustrates a stationary regeneration where the engine can **not** build enough heat to start aftertreatment injection (1).

- The dashed line is for the aftertreatment DOC inlet temperature sensor.
- The dotted line is for the aftertreatment DPF inlet temperature sensor.
- The solid line is for the aftertreatment DPF outlet temperature sensor.

The engine speed will likely increase to the stationary regeneration speed of 1000 rpm, but because the aftertreatment temperatures do **not** increase enough to start aftertreatment injection, the stationary regeneration will **not** complete.

The wiring to the aftertreatment temperature sensor appears to be correct in this example because they all read approximately the same temperature for the same conditions.

Possible causes of this issue include:

- A malfunctioning turbocharger
- Exhaust piping leaks, cracks, or loose connections
- Low ambient temperatures: Move the vehicle to a location with higher ambient temperatures.

Inspect the exhaust piping for leaks, cracks, and loose connections.

![[11d00301.png]]

This graph illustrates a stationary regeneration where the wiring to the aftertreatment temperature sensors is incorrect (1).

- The dashed line is for the aftertreatment DOC inlet temperature sensor.
- The dotted line is for the aftertreatment DPF inlet temperature sensor.
- The solid line is for the aftertreatment DPF outlet temperature sensor.

In this condition, the engine speed will increase to the stationary regeneration speed of 1000 rpm.

Aftertreatment injection will **not** occur in this condition because the aftertreatment DOC inlet temperature does **not** reach the required temperature. Because aftertreatment injection is **not** occurring, the aftertreatment temperatures should **not** read differently.

The possible cause of this condition is an incorrectly assembled aftertreatment wiring harness. See the Aftertreatment Exhaust Gas Temperature Sensor Wiring part of this procedure.

![[11d00302.png]]

This graph illustrates a stationary regeneration (1) where the OEM wiring to the aftertreatment DOC inlet temperature sensor and the aftertreatment DPF outlet temperature sensor is reversed.

- The dashed line is for the aftertreatment DOC inlet temperature sensor.
- The dotted line is for the aftertreatment DPF inlet temperature sensor.
- The solid line is for the aftertreatment DPF outlet temperature sensor.

In this condition, the engine speed will increase to the stationary regeneration speed of 1000 rpm.

Aftertreatment injection may occur in this condition (2). However, the aftertreatment DOC inlet temperature increases after aftertreatment injection begins, while the aftertreatment DPF outlet temperature remains constant.

The possible cause of this condition is that the OEM wiring to the aftertreatment DOC inlet temperature sensor and the aftertreatment DPF outlet temperature sensor is reversed. See the Aftertreatment Exhaust Gas Temperature Sensor Wiring part of this procedure.

![[11d00303.png]]

A regeneration that will **not** complete can be caused by malfunctions in the exhaust gas recirculation (EGR), variable geometry turbocharger (VGT) systems, or fueling. These malfunctions do **not** allow the aftertreatment to reach the necessary temperatures for aftertreatment fuel injection.

When performing a stationary (parked) regeneration, monitor the following parameters to determine why a stationary (parked) regeneration will **not** complete:

- EGR Differential Pressure
- EGR Valve Position Measured (Percent Open)
- Exhaust Gas Pressure
- Intake Manifold Pressure
- Percent Load
- Turbocharger Actuator Position Measured (Percent Closed)
- Turbocharger Speed.

During a stationary (parked) regeneration, these are the typical values for a healthy system.

- EGR Differential Pressure - Less than 12.7 mm-Hg \[0.5 in-Hg\]
- EGR Valve Position Measured (Percent Open) - Zero percent
- Exhaust Gas Pressure - 3048 to 4064 mm-Hg \[120 to 160 in-Hg\]
- Intake Manifold Pressure - 247 to 915 mm-Hg \[10 to 36 in-Hg\]
- Percent Load - Less than 12 percent
- Turbocharger Actuator Position Measured (Percent Closed) - - 80 to 90 percent
- Turbocharger Speed - 40k to 78k rpm

During a stationary (parked) regeneration, the EGR valve should be closed to help increase the load on the engine.

A leaking EGR valve can be detected by monitoring the EGR Differential Pressure while the EGR valve is closed.

If the EGR Differential Pressure exceeds 12.7 mm-Hg \[0.5 in-Hg\] while the EGR Valve Position Measure (Percent Open) is zero percent during the stationary (parked) regeneration, a leaking EGR valve has been detected.

Clean and inspect the EGR valve for reuse. Reference Procedure 011-022 in Section 11.

During a stationary (parked) regeneration, the turbocharger also closes down to help increase the load on the engine.

If the Turbocharger Actuator Position Measured (Percent Closed) is **not** 80 to 90 percent, or, the exhaust gas pressure is **not** within 3048 to 3556 mm-Hg \[120 to 160 in-Hg\], a malfunction of the VGT is the likely cause of the stationary (parked) regeneration that will **not** complete.

Check the variable geometry turbocharger sector gear travel. Refer to Procedure 010-134 in Section 10.

Check the variable geometry turbocharger shroud plate and nozzle ring for damage or wear. Refer to Procedure 010-033 in Section 10.

During a stationary (parked) regeneration, the percent load on the engine will fluctuate until the engine and aftertreatment reach a steady condition. Once the engine stabilizes, the percent load should remain less than 12 percent. The percent load should **not** consistently exceed 12 percent during the stationary (parked) regeneration.

> [!note] Note · Примечание
> The percent load may fluctuate when the engine fan cycles ON and OFF.

### Test

> [!danger] WARNING · Опасно
> The DEF contains urea. Do not get the substance in your eyes. In case of contact, immediately flush eyes with large amounts of water for a minimum of 15 minutes. Do not swallow. In the event the DEF is ingested, contact a physician immediately. Reference the Materials Safety Data Sheet (MSDS) for additional information.

> [!warning] CAUTION · Осторожно
> It is unlawful to tamper with or remove any component of the aftertreatment system. It is also unlawful to use a DEF that does not meet the specifications provided or to operate the vehicle/equipment without DEF.

> [!warning] CAUTION · Осторожно
> Never add water or any other fluid besides what is specified to the DEF tank. The aftertreatment system may be damaged.

This section of the procedure provides information for testing the DEF concentration.

The correct concentration of DEF is critical to the engine and aftertreatment system for correct performance.

Cummins Inc. is **not** responsible for malfunctions or damage resulting from what Cummins Inc. determines to be abuse or neglect. This includes, but is **not** limited to: operation without correctly specified DEF, lack of maintenance of the aftertreatment system, improper storage or shutdown practices, or unauthorized modifications of the engine and aftertreatment system. Cummins Inc. is also **not** responsible for malfunctions caused by incorrect DEF, water, dirt, or other contaminants in the DEF. Use DEF refractometer, Part Number 4919318, to test the concentration of the DEF. Follow the instructions provided with the service tool.

> [!note] Note · Примечание
> The concentration of the DEF **must** be 32.5 ± 0.7 percent.

If the DEF concentration does **not** meet this specification, drain the DEF tank. Flush the tank with distilled water. Fill the tank with new and/or known good DEF. Check the DEF concentration.

Concentration of the DEF **must** be checked when:

- The vehicle has been stored for an extended period of time.
- It is suspected water has been added to the DEF tank.

![[ra8toda.png]]

### Contamination/Incorrect Fluid

DEF can become contaminated by the following situations:

- If equipped, the aftertreatment DEF tank coolant heating system malfunctions, allowing coolant to mix with the DEF.
- The aftertreatment DEF tank cap is missing or damaged, or the tank vent malfunctions.
- The aftertreatment DEF tank is filled with the incorrect fluid.

In the event that the DEF becomes contaminated, inspect the DEF to determine the most likely source.

Obtain a sample from the DEF tank and pour the sample into an appropriate container. Make sure to get a sample from the highest fluid level.

![[11800272.png]]

Petroleum based liquids, such as, but **not** limited to:

- Diesel fuel
- Hydraulic fluid
- Brake fluid.

Because DEF is largely composed of water, petroleum based liquids will separate from the DEF and rise to the top. Look for separation of the fluids, as well as characteristic smells.

Use DEF Contamination Test Kit, Part Number 5298935, to detect petroleum based contaminants in the DEF.

![[11c00592.png]]

Non-petroleum based liquids, such as, but **not** limited to:

- Water
- Coolant
- Windshield washer fluid.

If water has been added, the DEF will remain clear. As a result, the DEF will become diluted, reducing the concentration level.

> [!note] Note · Примечание
> If **only** water has been added to the DEF tank, drain the DEF tank. Flush with distilled water. Fill the tank with new and/or known good DEF. Check the DEF concentration after completing the refill. Follow the instructions in the Test section of this procedure.

For other non-petroleum based liquids that may have been added to the DEF, typically those fluids have coloring and will mix with DEF. If the DEF has a color tint to it, look for other fluids used on the vehicle that may match, such as coolant or windshield washer fluid.

If the DEF is contaminated, follow the steps detailed later in this procedure

![[11c00593.png]]

> [!note] Note · Примечание
> Use the electronic service tool to view and troubleshoot any fault codes that occur during the following steps. See the applicable Fault Code Troubleshooting Manual.

If the DEF has been contaminated, remove the aftertreatment DEF dosing unit filter. [[493-011-060 — Aftertreatment Diesel Exhaust Fluid Dosing Unit Filter|Refer to Procedure 011-060 in Section 11]]. Inspect the filter for signs the contaminated fluid went through the dosing system.

If the contaminated fluid did **not** go through the dosing system, drain the DEF tank. Flush with distilled water. Replace the DEF in the tank filter. See equipment manufacturer service information for details on servicing the DEF tank.

After the DEF tank has been cleaned, fill the tank with new and/or known good DEF. Check the DEF concentration after completing the refill. Follow the instructions in the Test section of this procedure.

![[11l00115.png]]

> [!note] Note · Примечание
> Any discarded contaminated fluids and/or parts **must** be disposed of according to local area ordinances.

If the contaminated fluid did go through the dosing system:

1. Drain the DEF tank. Thoroughly flush with distilled water.
2. Clean and flush the DEF tank header and filter. Replace the DEF tank filter, as necessary.
3. Remove all of the aftertreatment DEF lines. Flush with distilled water. See equipment manufacturer service information on the handling of contaminants in the aftertreatment DEF lines.
4. Install the aftertreatment DEF lines.
5. Remove the DEF dosing unit inlet screen filter and main filter. Replace both filters. [[493-011-058 — Aftertreatment Diesel Exhaust Fluid Dosing Unit|Refer to Procedure 011-058 in Section 11]].
6. Fill the DEF tank with clean, certified DEF.

> [!note] Note · Примечание
> If the DEF dosing system is contaminated with diesel fuel, replace the DEF dosing valve.

![[11800273.png]]
