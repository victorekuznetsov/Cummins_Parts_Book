---
type: "Процедура"
doc: "493-019-443"
title_en: "Aftertreatment Diesel Particulate Filter Differential/Outlet Pressure Sensor"
modified: "2024-04-09"
manuals:
  - "5411181"
figures: 9
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/493/493-019-443.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/493-019-443.pdf"
tags:
  - "документ/процедура"
  - "группа/493"
---

# Aftertreatment Diesel Particulate Filter Differential/Outlet Pressure Sensor

> [!abstract] Процедура · `493-019-443`
> **Входит в руководства:** [[5411181 — X15 CM2350 X114B - Efficiency Series Service Manual|5411181]]
> **Секции:** Section 19 - Electronic Controls - Group 19
> **Даты:** изменён 2024-04-09
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/493/493-019-443.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/493-019-443.pdf)

### Select Service Tools

#### Recommended Cummins® Service Tool

- Test Lead Kit, Part Number 5299367
- Framatome™ male test lead, Part Number 3164596
- Cummins® electronic service tool or equivalent

#### Additional Service Items

- No additional service items required.

### General Information

The aftertreatment diesel particulate filter differential pressure sensor (1) measures pressure across the aftertreatment diesel particulate filter (DPF) and outlet pressure.

The aftertreatment DPF differential/outlet pressure sensor (2) is mounted on the aftertreatment DPF differential pressure sensor mounting bracket.

![[19l00052.png]]

### Initial Check

In the recommended Cummins® electronic service tool or equivalent, add the following parameter to the Data Monitor/Logger screen:

1. Aftertreatment DPF differential pressure sensor signal voltage.

Verify the aftertreatment DPF differential pressure sensor signal voltage at keyswitch ON, engine OFF.

At ambient temperature 25°C \[77°F\] and below, the reading should be between 0.61 and 0.77 VDC.

At ambient temperature 26°C \[78°F\] and above, the reading should be between 0.642 and 0.738 VDC.

> [!note] Note · Примечание
> If the aftertreatment DPF differential pressure sensor signal voltage does **not** read within specification, inspect the aftertreatment DPF differential pressure sensor wiring for correct resistance and pin-to-pin routing.

> [!note] Note · Примечание
> If the aftertreatment DPF differential pressure sensor signal voltage does **not** read within specification, inspect the aftertreatment DPF differential pressure sensor tubes for blockage. [[493-011-047 — Aftertreatment Diesel Particulate Filter Differential Pressure Sensor Tubes|Refer to Procedure 011-047 in Section 11.]]

![[19803969.png]]

Disconnect the aftertreatment DPF differential pressure sensor wiring harness connector.

Use the electronic service tool to verify that Fault Codes 1881 and 3134 are active.

> [!note] Note · Примечание
> If Fault Codes 1881 and 3134 did **not** become active, inspect the aftertreatment DPF differential pressure sensor wiring for correct resistance and pin-to-pin routing.

![[11l00083.png]]

Use the Framatome™ male test lead, Part Number 3164596, or equivalent, to short the aftertreatment DPF differential pressure sensor SUPPLY pin to the aftertreatment DPF differential pressure sensor SIGNAL pin.

Use the electronic service tool to verify that Fault Codes 1879 and 3134 are active.

> [!note] Note · Примечание
> If Fault Codes 1879 and 3134 did **not** become active, the aftertreatment DPF differential pressure sensor signal and aftertreatment DPF outlet pressure sensor signal could be incorrectly routed from pin-to-pin. See equipment manufacturer service information.

> [!note] Note · Примечание
> If Fault Codes 1881 and 3134 did **not** become active, inspect the aftertreatment DPF differential pressure sensor wiring for correct resistance and pin-to-pin routing.

![[11y00001.png]]

Connect the aftertreatment DPF differential pressure sensor wiring harness connector.

In the electronic service tool, add the following parameter to the Data Monitor/Logger screen:

1. Aftertreatment DPF differential pressure sensor signal voltage.

Verify the aftertreatment DPF differential pressure sensor signal voltage at keyswitch ON, engine OFF.

At ambient temperature 25°C \[77°F\] and below, the reading should be between 0.61 and 0.77 VDC.

At ambient temperature 26°C \[78°F\] and above, the reading should be between 0.642 and 0.738 VDC.

If the aftertreatment DPF differential pressure sensor signal voltage does **not** meet specification, replace the aftertreatment DPF differential pressure sensor.

![[19803969.png]]

### Preparatory Steps

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

- Disconnect the batteries. See equipment manufacturer service information.
- Remove the aftertreatment DPF sensor table heat shield if equipped. Refer to Procedure 011-032 in Section 11.
- Disconnect the aftertreatment interface harness from the differential pressure sensor connector. Refer to Procedure 019-477 in Section 19.
- Disconnect the differential pressure sensor tubes from the differential pressure sensor by releasing the quick connect locking tab and pulling the tubes off the sensor. [[493-011-047 — Aftertreatment Diesel Particulate Filter Differential Pressure Sensor Tubes|Refer to Procedure 011-047 in Section 11.]]

### Remove

Remove the mounting capscrews that secure the aftertreatment DPF differential pressure sensor to the sensor mounting bracket.

> [!note] Note · Примечание
> For configurations that use an aftertreatment DPF sensor table heat shield, the aftertreatment DPF differential pressure sensor capscrews will be removed during the process of removing the DPF sensor table heat shield. Refer to Procedure 011-032 in Section 11.

> [!note] Note · Примечание
> For some configurations, the aftertreatment DPF differential pressure sensor can be remote mounted on the chassis.

![[19l00054.png]]

### Clean and Inspect for Reuse

Gently tap the sensor on a soft flat surface with the pressure ports facing downwards. This will remove any water that may have built up in the sensor.

Inspect the aftertreatment interface harness connector and sensor for the following:

- Cracked or broken connector
- Missing or damaged connector seals
- Dirt, debris, or moisture in or on the connector pins
- Corroded, bent, broken, pushed back, or expanded pins
- Chipped, cracked, extruded, or damaged sensor.

Replace the differential/outlet pressure sensor if damage is found.

![[19c01639.png]]

Inspect the differential/outlet pressure sensor vent for blockage or damage.

Replace the differential/outlet pressure sensor if blockage or damage is found.

![[19o00074.png]]

### Install

Install the aftertreatment DPF differential pressure sensor to the sensor mounting bracket.

Install and tighten the mounting capscrews that secure the aftertreatment DPF differential pressure sensor.

> [!tip] Момент затяжки · Torque Value
> 11 n•m [98 in-lb]

Install the DPF sensor table heat shield **if equipped**. Refer to Procedure 011-032 in Section 11.

> [!note] Note · Примечание
> For configurations that use a DPF sensor table heat shield, the DPF differential pressure sensor capscrews will be removed during the process of removing the DPF sensor table heat shield. Refer to Procedure 011-032 in Section 11.

> [!note] Note · Примечание
> For some configurations, the DPF differential pressure sensor can be remote mounted on the chassis.

![[19l00054.png]]

### Finishing Steps

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

- Verify the continuously downward slope of the aftertreatment DPF differential pressure sensor tubes from sensor connectors to sensor port fittings. Make adjustments, if required.
- Connect the batteries. See equipment manufacturer service information.
- Use the electronic service tool to check for fault codes.
- Check for fault codes and exhaust leaks.
