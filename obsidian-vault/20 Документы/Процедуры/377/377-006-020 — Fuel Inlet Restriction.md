---
aliases:
  - "Сопротивление на входе топлива"
type: "Процедура"
doc: "377-006-020"
title_en: "Fuel Inlet Restriction"
title_ru: "Сопротивление на входе топлива"
modified: "2019-06-19"
manuals:
  - "5411181"
figures: 4
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/377/377-006-020.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/377-006-020.pdf"
tags:
  - "документ/процедура"
  - "группа/377"
---

# Fuel Inlet Restriction
**Сопротивление на входе топлива**

> [!abstract] Процедура · `377-006-020`
> **Входит в руководства:** [[5411181 — X15 CM2350 X114B - Efficiency Series Service Manual|5411181]]
> **Секции:** Section 6 - Injectors and Fuel Lines - Group 06
> **Даты:** изменён 2019-06-19
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/377/377-006-020.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/377-006-020.pdf)

### Select Service Tools

#### Recommended Cummins® Service Tools

- Orificed diagnostic fuel line, Part Number 3164621
- 1/8” NPT Compuchek™ fitting, Part Number 3042618
- Inlet restriction tool, Part Number 4918895.

#### Additional Service Items

- 0 to 762 mm-Hg \[0 to 30 in-Hg\] vacuum gauge.

### Setup

Install orificed diagnostic fuel line, Part Number 3164621, onto the Compuchek™ fitting at the inlet to the pressure side fuel filter.

The orificed diagnostic fuel line is used in procedures to create rated flow through the low pressure fuel system without the need to operate the engine under load.

Obtain a container suitable for collection of fuel that exits the diagnostic fuel line. A 19 liter \[5 gal\] bucket is recommended.

![[06400526.png]]

Obtain inlet restriction tool, Part Number 4918895.

Disconnect the fuel line from the gear pump inlet and install the inlet restriction tool, Part Number 4918895, inline between the gear pump inlet and the inlet fuel line.

Attach a 0 to 762 mm-Hg \[0 to 30 in-Hg\] vacuum gauge to the inlet restriction tool at the gear pump inlet.

![[06l00054.png]]

### Measure

Engine Will Start

> [!note] Note · Примечание
> Disconnect the fuel lift pump, or wait until the lift pump has completed its cycle, before beginning the fuel inlet restriction measurements.

Operate the engine at high idle and measure the inlet vacuum.

| Fuel Inlet Restriction |  |  |
|---|---|---|
| mm-hg |  | in-hg |
| -254 | MAX | -10 |

![[06l00055.png]]

Engine Will Not Start

> [!note] Note · Примечание
> Disconnect the fuel lift pump, or wait until the lift pump has completed its cycle, before beginning the fuel inlet restriction measurements.

Operate the engine at cranking (minimum of 150 rpm for 10 seconds) and measure the inlet vacuum.

| Fuel Inlet Restriction |  |  |
|---|---|---|
| mm-hg |  | in-hg |
| -127 | MAX | -5 |

If the inlet restriction is excessive, look for the root cause:

- Suction-side fuel filter(s) plugged
- Fuel heater valves are restricted
- Lift pump or check valve restriction
- Original equipment manufacturer (OEM) fuel lines pinched or restricted
- Fuel tank stand pipes restricted.

![[06t00006.png]]

### Finishing Steps

- Disconnect all diagnostic test fittings and install all components removed during testing. [[377-006-024 — Fuel Supply Lines|Refer to Procedure 006-024 in Section 6.]]
- Connect the fuel lines. Verify the connection gives an audible click. Lightly pull on the fuel line to verify the connector is fully seated and locked.
- Connect the fuel lift pump to the engine harness. Refer to Procedure 005-045 in Section 5.
- Bleed air from the fuel system. Refer to Procedure 005-234 in Section 5.
- If applicable, connect the fuel lift pump to the engine harness.
