---
type: "Процедура"
doc: "377-002-014"
title_en: "Injector Sleeve, Cylinder Head"
modified: "2026-06-19"
manuals:
  - "5411181"
figures: 8
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/377/377-002-014.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/377-002-014.pdf"
tags:
  - "документ/процедура"
  - "группа/377"
---

# Injector Sleeve, Cylinder Head

> [!abstract] Процедура · `377-002-014`
> **Входит в руководства:** [[5411181 — X15 CM2350 X114B - Efficiency Series Service Manual|5411181]]
> **Секции:** Section 2 - Clinder Head · Section 2 - Cylinder Head · Section 2 - Cylinder Head - Group 02
> **Даты:** изменён 2026-06-19
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/377/377-002-014.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/377-002-014.pdf)

### General Information

The injector sleeve (1) is a component of the cylinder head group which separates the cooling water jacket from the injector bore/fuel system. The sleeve seals against the cylinder head at the top and bottom of the component. In cases where the injector sleeve leaks at the top, a retaining ring can be pressed into the sleeve to create a seal.

![[02o00016.png]]

### Preparatory Steps

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

- Disconnect the batteries. See equipment manufacturer service information.
- Remove the exhaust gas recirculation (EGR) crossover tube. Refer to Procedure 011-070 in Section 11.
- Remove the rocker lever cover. [[377-003-011-tr — Rocker Lever Cover|Refer to Procedure 003-011 in Section 3]].
- Disconnect the internal actuator harness. Refer to Procedure 019-063 in Section 19.
- Remove the high-pressure fuel line. Refer to Procedure 006-051 in Section 6.
- Remove the fuel connector retaining nut and fuel connector. Refer to Procedure 006-052 in Section 6.
- Drain the cooling system below the cylinder head level. Refer to Procedure 008-018 in Section 8.
- Remove the injectors. [[377-006-026 — Injector|Refer to Procedure 006-026 in Section 6]].

![[ck800wa.png]]

### Clean and Inspect for Reuse

Clean and inspect injector bores for wear, cracks, mis-drilled passages, or other damage.

The cylinder head must be replaced if cracks, mis-drilled passages, or other damage is detected in the injector bores.

![[02c00157.png]]

### Leak Test

> [!warning] CAUTION · Осторожно
> Do not apply more than 140 kPa \[20 psi\] air pressure to the cooling system. The water pump seal can be damaged.

Pressurize the cooling system. Refer to Procedure 008-018 in Section 8.

While the cooling system is under pressure, inspect the injector sleeves (1) for leaks. If needed, a light spray of a soapy water solution can be used to reveal the leaks if they exist. Visual confirmation of bubbles at the top or bottom of the sleeve indicate a leak.

If the top of the injector sleeve leaks, continue on to retaining ring installation instructions. Even if **only** one injector sleeve is found leaking at the top, the following installation procedure **must** be completed on all injector sleeves.

> [!note] Note · Примечание
> If the retaining ring is already installed and leaks are found at the top, pressure test the cylinder head to determine decay rate for reuse. [[377-002-004 — Cylinder Head|Refer to Procedure 002-004 in Section 2]].

![[02o00017.png]]

If the bottom of the injector sleeve leaks, pressure test the cylinder head to determine decay rate for reuse. [[377-002-004 — Cylinder Head|Refer to Procedure 002-004 in Section 2]].

![[02o00018.png]]

### Install

Even if **only** one injector sleeve is found leaking at the top, the following installation procedure **must** be completed on all injector sleeves.

Verify the injector bore is clean.

Gently drop a retaining ring into each injector bore.

Place service tool, Part Number 5394735, into the injector bore so the mandrel of the installer screw goes through the inner diameter of the retaining ring. Make sure the installer screw and Allen screw are backed out enough so that the tool is flush with the valve spring deck.

Tighten the tooling capscrew.

> [!tip] Момент затяжки · Torque Value
> 80 n•m [59 ft-lb]

Hand tighten the Allen screw so the pad makes contact with the cast surface of the cylinder head.

Tighten the installer screw on service part, Part Number 5394735, until the stop nut contacts the body of the installation tool.

Prior to attempting to loosen the capscrew of the installation tool, loosen the installer screw and Allen screw with the pad.

Confirm the depth of the top of the retaining ring to be 68.5 mm \[2.70 in\] or greater from the spring deck of the cylinder head. Use of a caliper is recommended for measurements.

If depth of retaining ring is less than 68.5 mm \[2.70 in\] from the spring deck of the cylinder head:

- Verify the stop nut made full contact with the body of the installation tool.
- Confirm installation tool depth is set to 69.8 ±0.25 mm \[2.75 ±0.01 in\].
- Measure 12.9 capscrew and replace **only** if stretched beyond 50 mm \[1.96 in\].
- If proper installation tool depth is still **not** achievable, use a dead blow hammer to apply a solid strike to the top of the installer screw of the installation tool to set the ring at the proper height.

![[02o00019.png]]

### Finishing Steps

Repeat the Leak Test. Confirm bubbles can no longer be detected.

- Install the injectors. [[377-006-026 — Injector|Refer to Procedure 006-026 in section 6]].
- Connect the internal actuator harness to the injector. Refer to Procedure 019-063 in Section 19.
- Orient the injector wires so they will **not** interfere with a rocker lever or engine brake housing. If the rocker lever is able to come into contact with the injector harness, it will rub through the wire insulation and cause injector circuit fault codes.
- Install the high-pressure fuel lines. Refer to Procedure 006-051 in Section 6.
- Install the rocker lever cover. [[377-003-011-tr — Rocker Lever Cover|Refer to Procedure 003-011 in Section 3]].
- Install the EGR crossover tube. Refer to Procedure 011-070 in Section 11.
- Connect the batteries. See equipment manufacturer service information

![[ck800wa.png]]

INSITE™ electronic service tool version 7.5.3 or newer is required to complete the injector reset.

Once a new injector is installed, an injector reset **must** be completed with INSITE™ electronic service tool.

#### Injector Reset Instructions

- Connect INSITE™ electronic service tool.
- Select "Advance engine Control Module Data."
- Select "Fuel Injector Reset."
- Select each injector that needs to be reset and click "Reset."

> [!note] Note · Примечание
> If multiple new injectors are installed, multiple injectors can be reset at the same time.

Fill the cooling system. Refer to Procedure 008-018 in Section 8.

Operate the engine until it reaches normal operating temperature. Check for leaks.

![[00c00030.png]]
