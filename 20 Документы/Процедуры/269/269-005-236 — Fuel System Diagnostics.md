---
aliases:
  - "Диагностика топливной системы"
type: "Процедура"
doc: "269-005-236"
title_en: "Fuel System Diagnostics"
title_ru: "Диагностика топливной системы"
modified: "2020-07-01"
engines:
  - "93948840"
families:
  - "QSZ13"
manuals:
  - "4358369"
figures: 33
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/269/269-005-236.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/269-005-236.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSZ13"
  - "группа/269"
---

# Fuel System Diagnostics
**Диагностика топливной системы**

> [!abstract] Процедура · `269-005-236`
> **Двигатели:** [[93948840 — QSZ13 CM2150 Z102 CPL 4858|93948840]]
> **Семейство:** QSZ13
> **Входит в руководства:** [[4358369 — QSZ13 CM2150 Z102 Service Manual|4358369]]
> **Секции:** Section 5 - Fuel System - Group 05
> **Даты:** изменён 2020-07-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/269/269-005-236.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/269-005-236.pdf)

### General Information

> [!danger] WARNING · Опасно
> Wear appropriate eye and face protection when using compressed air. Flying debris and dirt can cause personal injury.

> [!danger] WARNING · Опасно
> When using a steam cleaner, wear safety glasses or a face shield, as well as protective clothing. Hot steam can cause serious personal injury.

> [!warning] CAUTION · Осторожно
> Clean all fittings before disassembly. Dirt or contaminants can damage the fuel system.

Before servicing **any** fuel system components, (such as fuel lines, fuel pump, injectors, etc.) which would expose the fuel system or internal engine components to potential contaminants prior to disassembly, clean the fittings, mounting hardware, and the area around the component to be removed. Dirt or contaminants can be introduced into the fuel system and engine if the surrounding areas are **not** cleaned, resulting in damage to the fuel system and engine. [[99-000-009 — Engine Cleaning|Refer to Procedure 000-009 in Section 0.]]

To prevent engine damage from debris or contamination, cover, cap, or plug any openings as soon as possible when servicing the fuel system. Caps and plugs can be found in Clean Care Kit, Part Number 4919073.

![[00c00206.png]]

The following procedures are used to diagnose fuel system issues. These checks and measurements are referenced throughout the applicable troubleshooting and fault code trees as needed.

This procedure is not intended to take the place of the troubleshooting tree repair direction.

Refer to the appropriate troubleshooting symptom tree for repair direction.

![[ck800wa.png]]

### High-Pressure System Leak Down Test

> [!note] Note · Примечание
> This test can **not** be performed if the engine will **not** start.

Connect INSITE ™ electronic service tool.

Operate the engine.

Monitor the fuel rail pressure.

Check the fuel pressure decay.

Shut off the engine and wait for it to completely stop. Turn the keyswitch ON quickly.

Monitor INSITE™ electronic service tool and record the fuel rail pressure for 1 minute.

A change in fuel pressure greater than 100 bar \[1450 psi\] in 1 minute is an indication of a high-pressure fuel system leak.

Refer to the appropriate troubleshooting symptom tree for repair direction.

![[19c01817.png]]

### Low-Pressure System Check

The low-pressure system check consists of a number of measurements and checks to make sure that the low pressure fuel system is functioning properly. These checks will vary, depending on whether or not the engine will start.

![[eg8gasj.png]]

Measurement - Engine Will Start

Check for air in the fuel. Refer to Procedure 006-003 in Section 6.

![[06d00542.png]]

Measure the fuel inlet restriction. Refer to Procedure 006-020 in Section 6.

![[05c00259.png]]

Measure the fuel gear pump output pressure. Use the instructions in the Fuel Pump Gear Pump Pressure Test section of this procedure.

![[05c00436.png]]

Measure the fuel filter restriction. Use the instructions in the Fuel Filter Restriction section of this procedure.

![[05c00438.png]]

Measure the fuel drain line restriction. Refer to Procedure 006-012 in Section 6.

![[05c00438.png]]

Measurement - Engine Will Not Start

Measure the fuel gear pump output pressure while cranking. Use the instructions in the Fuel Pump Gear Pump Pressure Test section of this procedure.

![[05c00436.png]]

Measure the fuel drain line restriction. Refer to Procedure 006-012 in Section 6.

![[06c00256.png]]

### Fuel Pump Gear Pump Pressure Test

Measurement - Engine Will Start

Install a 0 to 2068 kPa \[0 to 300 psi\] pressure gauge at the Compuchek™ fitting at the inlet to the fuel filter head.

Operate the engine at high idle and observe the fuel gear pump pressure.

| Gear Pump Pressure at High Idle |  |  |
|---|---|---|
| kpa |  | psi |
| 1000 | MIN | 145 |

![[05c00436.png]]

Measurement - Engine Will Not Start

Install a 0 to 207 kPa \[0 to 30 psi\] pressure gauge at the Compuchek™ fitting at the inlet to the fuel filter head.

Crank the engine and observe the fuel gear pump pressure.

| Gear Pump Pressure at Cranking |  |  |
|---|---|---|
| kpa |  | psi |
| 69 | MIN | 10 |

![[05c00444.png]]

### Fuel Filter Restriction

Initial Setup

Install a 1/8-inch NPT Compuchek™ into banjo fitting adapter, Part Number 4919057, and install the assembled fitting into the outlet of the pressure side fuel filter.

Connect orificed diagnostic fuel line, Part Number 3164621, to the banjo fitting adapter and route to the engine fuel tank or other suitable container.

The orificed diagnostic fuel line is used in procedures to create rated flow through the low pressure fuel system without the need to operate the engine under load.

![[05c00437.png]]

Measurement

Install a 0 to 2068 kPa \[0 to 300 psi\] pressure gauge at the Compuchek™ fitting at the inlet to the fuel filter head.

Operate the engine at high idle and observe the filter inlet pressure.

Install a 0 to 2068 kPa \[0 to 300 psi\] pressure gauge at the Compuchek™ fitting at the outlet to the fuel filter head.

Operate the engine at high idle and observe the filter outlet pressure.

| Fuel Filter Restriction |  |  |
|---|---|---|
| kpa |  | psi |
| 138 | MAX | 20 |

If the difference between the filter inlet pressure and filter outlet pressure is greater than the specification, replace the fuel filter.

![[05c00438.png]]

### High-Pressure Fuel Pump Return Flow Test

> [!danger] WARNING · Опасно
> Depending on the circumstances, diesel fuel is flammable. When inspecting or performing service or repairs on the fuel system, to reduce the possibility of fire and resulting severe personal injury, death or property damage, never smoke or allow sparks or flames (such as pilot lights, electrical switches, or welding equipment) in the work area.

> [!warning] CAUTION · Осторожно
> Installation of the banjo flow adapter at any place other than the recommended locations can cause damage to high-pressure fuel system components.

This test uses a flow adapter fitting. The purpose of the flow adapter fitting is to route the drain flow of the fuel pump head **only** into a collection device so that leakage may be measured.

This procedure requires the use of a fuel system leak tester, Part Number 3164618.

![[05d00790.png]]

Initial Setup

> [!warning] CAUTION · Осторожно
> Make sure to hold the banjo fittings while tightening the banjo bolt to prevent fitting rotation. Allowing the banjo fitting to rotate may damage the fuel line.

Remove the M12 banjo bolt connecting the fuel drain connection to the fuel pump head.

Install a banjo flow adapter fitting, Part Number 3164618, at the fuel drain connection and route a hose from this adapter to a bucket or the vehicle's fuel tank. This will isolate the injector and high pressure relief valve drain from the fuel pump drain.

Disconnect the OEM fuel return and clamp a hose over the fuel drain to be routed for measurement.

![[05c00439.png]]

> [!warning] CAUTION · Осторожно
> The High-Pressure Leakage Test in INSITE™ electronic service tool will cause the engine to operate at elevated pressures while the engine idles. The engine noise will change when this test is being performed due to the higher fuel injection pressures. Safety glasses should be worn while working near the running engine. Fuel lines should not be adjusted while performing this test.

Close the engine cover(s) while performing these tests.

![[05d00818.png]]

Measurement - Engine Will Start

If the engine will start, perform INSITE™ electronic service tool High-Pressure Leakage Test.

Connect INSITE™ electronic service tool.

Start the engine and allow the engine to idle with fuel flowing into a collection device.

Begin the High-Pressure Leakage Test.

Measure the time necessary to collect 450 ml (cc) of fuel pump head drain flow while performing the High-Pressure Leakage Test.

Use a graduated cylinder for this measurement.

This measurement should be taken three times, but **only** the third reading is used.

![[19c01817.png]]

| Maximum Volume of Fuel During High-Pressure Leakage Test |  |
|---|---|
| ml (cc) | Seconds |
| 450 | 30 |

If 450 ml (cc) pump head drain flow is collected in less than 30 seconds, the fuel pump head has malfunctioned and **must** be replaced.

This specification is valid for engines operating on diesel fuels. Low fuel viscosity will increase the leakage rate; for example, kerosene or aviation fuels will result in excessive leakage. Verify the fuel type before replacing a fuel pump head for excessive leakage.

![[05d00821.png]]

Measurement - Engine Will Not Start

Begin cranking the engine until fuel exits the drain line.

> [!note] Note · Примечание
> Do **not** crank the engine for 30 seconds continously. Crank the engine in 15 second intervals with a 15 second pause between intervals. This reduces the possibility of overheating the starting motor.

When fuel begins to exit the drain line, route the drain flow to a graduated cylinder and continue cranking for 30 seconds.

This measurement should be taken three times, but **only** the third reading is used.

| Maximum Volume of Fuel During Cranking |  |
|---|---|
| ml (cc) | Seconds |
| 320 | 30 |

If 320 ml (cc) pump head drain flow is collected in less than 30 seconds of cranking, the pump head has malfunctioned and **must** be replaced.

![[05d00819.png]]

### High-Pressure Injector Return Flow Test

Initial Setup

> [!warning] CAUTION · Осторожно
> Installation of the banjo flow adapter at any place other than the recommended locations can cause damage to high-pressure fuel system components.

> [!note] Note · Примечание
> Make sure the engine is at operating temperature before beginning this test.

Return fuel is transmitted from the injectors and fuel rail high-pressure relief valve through a common return line. The common return line connects to a fuel drain connection that also receives fuel drain from the fuel pump head.

Measurement of fuel injector leakage requires use of a fuel return hose and a special fuel fitting, Part Numbers 4919058 and 3164618.

The tools are used in combination to isolate the leakage from the injectors, so it can be measured into a graduated cylinder.

![[05d00255.png]]

> [!danger] WARNING · Опасно
> Depending on the circumstance, diesel fuel is flammable. When inspecting or performing service or repairs on the fuel system, to reduce the possibility of fire and resulting severe personal injury, death, or property damage, never smoke or allow sparks or flames (such as pilot lights, electrical switches, or welding equipment) in the work area.

Remove the banjo bolt that connects the common drain line to the high-pressure relief valve.

Install a 1/8-inch NPT Compuchek™ into banjo fitting adapter, Part Number 4919058, and install the assembled fitting at the fuel pressure relief valve drain connection. Use a quick-connect to route the fuel into a collection device or back to the vehicle fuel tank.

Remove the banjo bolt that connects the common drain line to the fuel drain connection at the fuel pump.Install the fuel return hose, Part Number 3164618, at the fuel drain connection at the fuel pump.

Route the return fuel into a collection device that is marked in cubic centimeters.

> [!note] Note · Примечание
> Graduated cylinder, Part Number 4919139, or a similar measuring device may be used.

![[05c00440.png]]

Measurement - Engine Will Start

If the engine will start, perform INSITE™ electronic service tool High-Pressure Leak Test.

Connect INSITE™ electronic service tool.

Start the engine and allow the engine to idle with fuel flowing into a collection device.

Begin the High-Pressure Leakage Test.

| Leagage Specification with Engine Running |  |
|---|---|
| Maximum Leakage in 1 Minute | 70 ml (cc) |

> [!note] Note · Примечание
> Fuel temperature and fuel type will influence this measurement. For example; as the engine is warmed up and the injectors become hot, the leakage rate will increase. Also, low viscosity fuels, such as kerosene will cause the leakage rate to increase. The above specification is correct for on-highway diesel fuels where fuel inlet temperature is less than 49°C \[120°F\].

After recording the fuel leakage quantity, stop INSITE™ electronic service tool High-Pressure Leak Test and turn the keyswitch to OFF.

> [!note] Note · Примечание
> Make sure a steady flow of fuel is present at the drain line before beginning the measurement. Air in the line and movement of the hose during measurement can result in inaccurate measurements.

![[19c01817.png]]

If injector drain flow is excessive, it will be necessary to isolate the damaged or worn injector(s) or fuel connector(s).

A loose fuel connector retaining nut results in a poor seal at the interface between the fuel connector and the injector. The loose condition will result in a leak of high-pressure fuel to the injector drain.

Verify first that the fuel connectors are properly tightened. Refer to Procedure 006-052 in Section 6.

If loose retaining nut(s) are found, test for leakage after tightening the retaining nut(s).

![[05c00442.png]]

Measurement - Engine Will Not Start

Crank the engine until fuel exits the drain line.

> [!note] Note · Примечание
> Do **not** crank the engine for 30 seconds continously. Crank the engine in 15 second intervals with a 15 second pause between intervals. This reduces the possibility of overheating the starting motor.

When fuel begins to exit the drain line, route the drain flow to a graduated cylinder and continue cranking for 30 seconds.

The leakage should **only** be a few drops. Any more than a few drops indicates either an injector or a high-pressure connector failure.

> [!note] Note · Примечание
> Vent the pressure from the fuel system as directed after each cranking event.

![[05c00441.png]]

### High-Pressure Injector Return Flow Isolation Test

> [!danger] WARNING · Опасно
> Normal engine operation creates highly pressurized fuel in the fuel line which will remain in the fuel line after engine shutdown. Never open the fuel system when the engine is operating. Before servicing the fuel system, always loosen the pump-to-rail fuel line at the rail to vent the pressure. Keep hands clear of the line when loosening. High-pressure fuel spray can penetrate the skin, resulting in serious personal injury or death.

Before servicing the high-pressure fuel system, loosen the pump-to-rail line at the rail to vent the pressure.

Keep hands clear of the line when loosening.

Tighten the fuel rail nut.

Torque Value:

> [!note] Note · Примечание
> A machined slot in this fitting directs the fuel spray towards the engine.

![[00c00206.png]]

> [!warning] CAUTION · Осторожно
> Do not install the isolation tool at the high-pressure pump outlet fitting. Severe engine damage will result. This tool must only be installed at the fuel rail for the purpose of isolating the high-pressure fuel supply from individual injectors.

> [!warning] CAUTION · Осторожно
> Make certain the keyswitch is in the OFF position (engine not running) when loosening or tightening high-pressure fuel lines.

Use leak test isolation tool, Part Number 4918563, to isolate excessive fuel drain from injectors or fuel connectors.

Follow the pressure relief step (shown in the previous step) prior to every installation of the isolation tool.

![[05c00399.png]]

Isolate the injector and fuel connector for each cylinder by installing the isolation tool at the fuel rail in place of the high-pressure fuel line that supplies the fuel connector.

Torque Value:

![[05c00440.png]]

Record the amount of fuel flow from the injector drain line in 1 minute while the engine is running. Use INSITE™ electronic service tool High Pressure Leak Test. Do this up to six (6) times, once while each line is isolated.

If isolating a single injector and high-pressure fuel connector causes the leakage to decrease significantly compared to the rest of the set, that injector and fuel connector **must** be inspected.

> [!note] Note · Примечание
> Make sure a steady flow of fuel is present at the drain line before beginning the measurement. Air in the line and movement of the hose during measurement can result in inaccurate measurements.

Inspect the suspect fuel connector. Refer to Procedure 006-052 in Section 6. If the fuel connector is **not** damaged, replace both the injector and the fuel connector.

![[06d00483.png]]

### Fuel Pressure Relief Valve Return Flow Test

Initial Setup

> [!warning] CAUTION · Осторожно
> Installation of the banjo flow adapter at any place other than the recommended locations can cause damage to high-pressure fuel system components.

Measurement of fuel pressure relief valve leakage requires use of a fuel leak test fitting, Part Number 4919058, and a fuel return hose. The tool is used to isolate the leakage from just the fuel pressure relief valve so that it can be measured in a graduated cylinder.

> [!note] Note · Примечание
> If Fault Code 449 or 2311 is active, do **not** replace the fuel pressure relief valve without first determining the cause of the fault condition. See the appropriate troubleshooting tree(s).

Remove the M16 banjo bolt that connects the fuel pressure relief valve to the fuel drain line.

Install a 1/8-inch NPT Compuchek™ into banjo fitting adapter, Part Number 4919058, and install the assembled fitting at the fuel pressure relief valve drain connection.

> [!tip] Момент затяжки · Torque Value
> 16.8 n•m [148 in-lb]

Use a quick-connect to route the fuel into a graduated cylinder.

![[05c00443.png]]

Measurement - Engine Will Start

Start the engine and allow the engine to idle with fuel flowing into a collection device.

Begin the High-Pressure Leakage Test.

When fuel begins to exit the drain line, route the drain flow into a graduated cylinder.

The leakage **must** be less than 10 drops per minute.

Refer to the appropriate troubleshooting symptom tree for repair directions.

> [!note] Note · Примечание
> If Fault Code 449 or 2311 is active, do **not** replace the fuel pressure relief valve without first determining the cause of the fault condition. Use the appropriate fault code troubleshooting tree in Section TF of the QSZ13 CM2150 Z101 Fault Code Troubleshooting Manual, Bulletin 4358367.

![[19c01817.png]]

Measurement - Engine Will Not Start

Begin cranking the engine until fuel exits the drain line.

When fuel begins to exit the drain line, route the drain flow to a graduated cylinder and continue cranking for 30 seconds.

> [!note] Note · Примечание
> Do **not** crank the engine for 30 seconds continously. Crank the engine in 15 second intervals with a 15 second pause between intervals. This reduces the possibility of overheating the starting motor.

The leakage should be **less than** 10 drops per minute.

> [!note] Note · Примечание
> If Fault Code 449 or 2311 is active, do **not** replace the fuel pressure relief valve without first determining the cause of the fault condition. Use the appropriate fault code troubleshooting tree in Section TF of the QSZ13 CM2150 Z101 Fault Code Troubleshooting Manual, Bulletin 4358367.

![[11800286.png]]
