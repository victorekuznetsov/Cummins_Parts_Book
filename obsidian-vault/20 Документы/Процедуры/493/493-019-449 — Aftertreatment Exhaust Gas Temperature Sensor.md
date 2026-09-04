---
type: "Процедура"
doc: "493-019-449"
title_en: "Aftertreatment Exhaust Gas Temperature Sensor"
modified: "2020-11-25"
manuals:
  - "5411181"
figures: 17
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/493/493-019-449.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/493-019-449.pdf"
tags:
  - "документ/процедура"
  - "группа/493"
---

# Aftertreatment Exhaust Gas Temperature Sensor

> [!abstract] Процедура · `493-019-449`
> **Входит в руководства:** [[5411181 — X15 CM2350 X114B - Efficiency Series Service Manual|5411181]]
> **Секции:** Section 19 - Electronic Controls - Group 19
> **Даты:** изменён 2020-11-25
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/493/493-019-449.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/493-019-449.pdf)

### Select Service Tools

#### Recommended Cummins® Service Tool

- Anti-seize compound, Part Number 3824879, or equivalent
- J1939 Component Isolation Kit, Part Number 5299465
- Battery adapter cable, Part Number 5299000.
- Cummins® electronic service tool or equivalent.

#### Additional Service Items

- No additional service items required.

### General Information

Due to the number of various aftertreatment configurations, this procedure has been written to be generic. **Not** all illustrations within this procedure will represent the application being serviced.

The exhaust gas temperature sensor is a one-piece unit made up of four sensor probes. The temperature sensor module and temperature sensor probes are not serviceable separately and must be replaced as an assembly.

![[19l00056.png]]

Aftertreatment exhaust gas temperature sensor is used to measure the temperature of exhaust gas.

1. T1 is located on the intake of the diesel oxidation catalyst (DOC)
2. T2 is located on the intake of the diesel particulate filter (DPF) (DOC outlet)
3. T3 is located on the outlet of the DPF
4. T4 is located on the outlet of the selective catalytic reduction (SCR).

![[19l00057.png]]

![[19401918.png]]

### Initial Check

Use recommended Cummins® electronic service tool or equivalent to monitor the value of the aftertreatment exhaust gas temperature sensors with the key ON and engine off.

The engine **must** be turned off long enough for the coolant temperature to match the local ambient air temperature.

The aftertreatment exhaust gas temperature sensors should read within 10°C or 18°F of the local ambient air temperature on a cold engine.

Replace any aftertreatment exhaust gas temperature sensor assemblies with values out of specification.

![[19r00163.png]]

### Test

Disconnect the aftertreatment interface harness (1) from the temperature sensor (2). Refer to Procedure 019-477 procedure in Section 19.

![[19l00058.png]]

Connect the Cummins® service tool, Part Number 5299466 and 5299467, from kit 5299465, to the temperature sensor module.

![[19l00059.png]]

Connect the service tool data link, 3-pin Deutsch™, to the engine Society of Automotive Engineers (SAE) J1939 data link connection, located on the driver's side of the engine.

![[19803641.png]]

Use the vehicle VDC to supply power to the service tool.

> [!note] Note · Примечание
> Cummins® battery adapter cable, Part Number 5299000, can be used to provide power from the vehicle battery supply.

For Fault Code 4151 - the following conditions **must** be met before checking the status of the active fault code.

This diagnostic runs continuously when the keyswitch is in the ON position.

> [!note] Note · Примечание
> If service tool is being used on 24 volt sensor, battery adapter cable, Part Number 5299000, will need to be used to provide power from the vehicle battery supply.

Check for inactive fault codes. After the above conditions have been met for the active fault code:

- Check to see if the active fault code 4151 now displays as inactive.
- If the active fault codes now displays as inactive, the sensor is operating normally and should **not** be replaced. The source of the fault code is located within the wiring that was isolated by the service tool.

![[19o00057.png]]

### Preparatory Steps

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

- Disconnect the batteries. See equipment manufacturer service information.

### Remove

> [!note] Note · Примечание
> Label each of the temperature sensors prior to removal.

Disconnect the aftertreatment wiring harness from the temperature sensor module. Refer to Procedure 019-477 procedure in Section 19.

Remove the two remaining cap screws.

![[19l00058.png]]

Remove the wire ties (1) securing the exhaust gas temperature sensor probe wires to the sensor support bracket.

![[19l00060.png]]

> [!warning] CAUTION · Осторожно
> Do not bend the temperature sensor probes when removing them from the aftertreatment system. After the retaining nut is loosened pull the sensor probe straight out until it is removed from the aftertreatment system.

Loosen the retaining nuts and remove the temperature sensor probes from the aftertreatment system.

Record or mark the locations of where each probe was installed to make sure they are installed in the same locations.

![[19l00061.png]]

Remove the capscrews securing the exhaust gas temperature sensor assembly to the sensor support bracket.

![[19l00062.png]]

### Inspect for Reuse

Inspect the aftertreatment gas temperature sensor assembly for damaged or exposed wires, bent or broken pins, damaged connectors, or damaged threads.

Inspect the tip of the sensors for cracks, dents, and kinks.

Replace the entire assembly if damage is found.

![[19l00063.png]]

### Install

Install the temperature sensor module onto the aftertreatment system.

Tighten the mounting capscrews.

> [!tip] Момент затяжки · Torque Value
> 11 n•m [98 in-lb]

![[19l00062.png]]

Connect the temperature sensor module (2) to the aftertreatment wiring harness (1).

![[19l00064.png]]

> [!warning] CAUTION · Осторожно
> If the temperature sensor wire connectors are not installed in the proper locations, aftertreatment system damage can result.

Apply a light coating of anti-seize compound, Part Number 3824879, to the threads of the temperature sensor probes.

Install the aftertreatment gas temperature sensors.

Tighten the nut that secures the sensors to the aftertreatment system.

> [!tip] Момент затяжки · Torque Value
> 38 n•m [28 ft-lb]

Connect the temperature sensor module to the aftertreatment wiring harness.

![[19l00065.png]]

Install new wire ties (1) to secure the exhaust gas temperature sensor probe wires to the sensor table.

Confirm that the exhaust gas temperature sensor probe wires are properly secured so that they do **not** come into contact with hot components and areas of wear that can result in damage.

![[19l00066.png]]

### Finishing Steps

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

- Connect the batteries. See the equipment manufacturer service information.
- Operate the engine and check for proper operation.
