---
aliases:
  - "Топливоподкачивающий насос"
type: "Процедура"
doc: "269-005-045"
title_en: "Fuel Lift Pump"
title_ru: "Топливоподкачивающий насос"
modified: "2023-02-22"
engines:
  - "93948840"
families:
  - "QSZ13"
manuals:
  - "4358369"
figures: 9
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/269/269-005-045.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/269-005-045.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSZ13"
  - "группа/269"
---

# Fuel Lift Pump
**Топливоподкачивающий насос**

> [!abstract] Процедура · `269-005-045`
> **Двигатели:** [[93948840 — QSZ13 CM2150 Z102 CPL 4858|93948840]]
> **Семейство:** QSZ13
> **Входит в руководства:** [[4358369 — QSZ13 CM2150 Z102 Service Manual|4358369]]
> **Секции:** Section 5 - Fuel System - Group 05
> **Даты:** изменён 2023-02-22
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/269/269-005-045.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/269-005-045.pdf)

### Select Service Tools

#### Recommended Cummins® Service Tools

- Removal tool, Part Number 4918878
- Diagnostic fuel line, Part Number 4918895
- Orificed diagnostic fuel line, Part Number 3164621

#### Additional Service Items

- Screwdriver
- Container suitable for fuel.

### Initial Check

A malfunctioning electric fuel lift pump can cause slow engine starts or can result in an engine failing to start. The fuel lift pump can be cleaned and repaired to a limited extent.

The fuel lift pump will operate for 30 to 60 seconds when the key is switched ON. The fuel lift pump will also operate while the engine is cranking.

![[05900327.png]]

A fuel lift pump is mounted to the back of the Engine Control Module (ECM) cooling plate.

A bypass check valve in the ECM cooling plate makes sure the system is primed by the fuel lift pump. This check valve opens under vacuum created by the gear pump once the engine is started. High vacuum measured between the electric fuel lift pump and the gear pump can indicate this check valve has become plugged.

The ECM cooling plate check valve is integral with the lower (outlet) fitting of the ECM cooling plate.

![[05d00792.png]]

#### Fuel Lift Pump Flow Test Setup

- Remove the clasp from the fuel line brace. This will allow the fuel lines to move so that test equipment can be installed properly.

![[06d00248.png]]

- Disconnect the quick-disconnect style fuel line from the gear pump inlet by pressing in the locking tangs on both sides of the quick-disconnect fitting.
- To aid in the removal of quick-disconnect style fuel lines, slide removal tool, Part Number 4918878, over the locking tangs. Verify the tool is removed from the fuel line as soon as possible after the line has been disconnected.
- Inadvertently leaving the tool in place can result in fuel leaks.

![[06d00489.png]]

- To aid in removal, a screwdriver may be inserted between the fuel line end and quick-disconnect male union. After pressing the opposing locking tangs, twisting the flat blade of the screwdriver helps to remove the fuel line.

![[06d00249.png]]

- Install diagnostic fuel line, Part Number 4918895, between the gear pump fuel supply line and the gear pump inlet.
- Connect orificed diagnostic fuel line, Part Number 3164621, to the Compuchek™ fitting on the diagnostic fuel line, Part Number 4918895, and run hose into a collection device.

![[05d01044.png]]

> [!note] Note · Примечание
> At initial key-ON, the fuel lift pump will run for 30 seconds and then stop.

Turn keyswitch to the ON position and allow fuel to flow into a collection device for 10 seconds (or until fuel stream is continuous).

> [!note] Note · Примечание
> It may take longer than 10 seconds for fuel stream to flow continuously during the first key-ON cycle because of air in the diagnostic fuel lines.

Once fuel flow is continuous, transfer the orificed diagnostic fuel line to a clear graduated cylinder and allow fuel to flow into the graduated cylinder for 10 seconds.

Remove the orificed diagnostic fuel line from graduated cylinder after 10 seconds and turn keyswitch to the OFF position.

Record the volume of fuel collected over 10 seconds.

Repeat this test three times and take an average of the flow rates.

| Measurements |  |  |
|---|---|---|
|  | ml | fl-oz |
| Minimum volume of fuel during 10 second fuel lift pump flow test | 100 | 3.4 |

> [!note] Note · Примечание
> If the fuel lift pump flow is low while the fuel lift pump runs, verify the ECM cooling plate check valve is **not** blocked open. Also, verify the original equipment manufacturer (OEM) connection inlet restriction is within specification.

> [!note] Note · Примечание
> If the fuel lift pump flow is low while the fuel lift pump runs, verify fuel is primed. For example, following fuel filter replacement, cycle the fuel lift pump three or four times before the air is purged.

![[05d01045.png]]

### Preparatory Steps

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

> [!danger] WARNING · Опасно
> When using a steam cleaner, wear safety glasses or a face shield, as well as protective clothing. Hot steam can cause serious personal injury.

> [!danger] WARNING · Опасно
> The fuel pump, high-pressure fuel lines, and fuel rail contain very high-pressure fuel. Do not loosen any fittings while the engine is running. Wait at least 10 minutes after shutting down the engine before loosening any fittings in the high-pressure fuel system to allow pressure to decrease to a lower level.

Before servicing any fuel system components (such as fuel lines, fuel pump, injectors, and so forth), which can expose the fuel system or internal engine component to potential contaminants prior to disassembly, clean the fittings, mounting hardware, and the area around the component to be removed. Dirt or contaminants can be introduced into the fuel system and engine if the surrounding areas are **not** cleaned, resulting in damage to the fuel system and engine.

- Disconnect the batteries. See equipment manufacturer service information.
- Steam clean the fuel system components (such as fuel lines, fuel pump, injectors, and so forth). [[99-000-009 — Engine Cleaning|Refer to Procedure 000-009 in Section 0.]]
- Disconnect the electric fuel priming pump from the engine wiring harness.
- Remove the fuel supply lines. Refer to Procedure 006-024 in Section 6.
- Remove the ECM cooling plate. Refer to Procedure 006-006 in Section 6.

### Remove

Remove the electric fuel lift pump from the ECM cooling plate.

![[05d00797.png]]

### Install

Install the electric fuel lift pump to the ECM cooling plate.

Tighten the mounting capscrews.

> [!tip] Момент затяжки · Torque Value
> 10 n•m [89 in-lb]

The ECM cooling plate check valve **must** be free of debris and installed into the lower ECM cooling plate port (outlet port).

Hold the fuel lines, as illustrated, so they do **not** come into contact with each other or the cylinder block.

![[05d00797.png]]

### Finishing Steps

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

- Install the ECM cooling plate to the cylinder block. Refer to Procedure 006-006 in Section 6.
- Install all fuel supply lines. Refer to Procedure 006-024 in Section 6.
- Connect the batteries. See equipment manufacturer service information.
- Operate the engine and check for leaks.
