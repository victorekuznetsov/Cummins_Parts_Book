---
type: "Процедура"
doc: "1016-005-042"
title_en: "Fuel Regulator, NG"
modified: "2022-12-14"
engines:
  - "77804810"
families:
  - "15N"
manuals:
  - "5659763"
figures: 16
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/1016/1016-005-042.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/1016-005-042.pdf"
tags:
  - "документ/процедура"
  - "двигатель/15N"
---

# Fuel Regulator, NG

> [!abstract] Процедура · `1016-005-042`
> **Двигатели:** [[77804810 — 15N CM2380 M104B CPL 5977|77804810]]
> **Семейство:** 15N
> **Входит в руководства:** [[5659763 — 15N CM2380 M104B Service Manual|5659763]]
> **Секции:** Section 5 - Fuel System - Group 05
> **Даты:** изменён 2022-12-14
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/1016/1016-005-042.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/1016-005-042.pdf)

### Select Service Tools

#### Recommended Cummins® Service Tools

- Gas detector, Part Number 3165179
- Digital Multimeter Kit, Part Number 3400162
- Electrical Test Lead Kit, Part Number 5299367
- Pressure test adapter, Part Number 5394427

#### Additional Service Items

- 0 kPa \[ 0 psi \] to 2068 kPa \[ 300 psi \] pressure gauge.

### General Information

For Liquefied Natural Gas (LNG) engine, the fuel pressure regulator is integrated with a shutoff valve and a pressure relief valve, and the bottom line is covered by a filter for venting and to avoid dust, oil, and so forth, entering the spring chamber inside the pressure regulator.

![[05s00052.png]]

For Compressed Natural Gas (CNG) engine, there are two same fuel pressure regulators on this product, installed in parallel for fuel flow (1). Each one is integrated with a shutoff valve, a pressure relief valve, and two coolant ports (2). These two coolant ports need to be connected to the engine cooling circuit.

![[05s00073.png]]

### Initial Check

> [!danger] WARNING · Опасно
> Natural gas is explosive and flammable. Always be sure to maintain adequate ventilation in the work area. Keep all cigarettes, flames, pilot lights, arcing equipment, and switches out of the work area and areas with shared ventilation to reduce the possibility of severe personal injury or death when working on a natural gas system.

Turn the keyswitch to ON position.

Use a gas detector, Part Number 3165179, to check the regulator connector for gas leak.

Check the regulator, connectors, and gas pipes if gas leak is found from the regulator connector.

![[05s00074.png]]

### Preparatory Steps

> [!danger] WARNING · Опасно
> Natural gas is explosive and flammable. Always be sure to maintain adequate ventilation in the work area. Keep all cigarettes, flames, pilot lights, arcing equipment, and switches out of the work area and areas with shared ventilation to reduce the possibility of severe personal injury or death when working on a natural gas system.

> [!danger] WARNING · Опасно
> Natural gas is lighter than air. Check the ceiling of the area where work is to be done for any possible ignition source.

> [!danger] WARNING · Опасно
> Always have proper ventilation when working on a natural gas system.

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

> [!warning] CAUTION · Осторожно
> To reduce the possibility of shock loading of components downstream of the supply valve, opening and closing of the gas supply valve must be done slowly.

- Disconnect the batteries. See equipment manufacturer service information.
- Slowly close the manual gas supply valve. See equipment manufacturer service information for the location of the valve.
- Disconnect the wiring harness of the shutoff valve.

- Disconnect the piping connected to the fuel pressure regulator. See equipment manufacturer service information.

> [!note] Note · Примечание
> The fuel inlet and outlet connectors on fuel regulators **must** be held in place with a wrench when removing gas pipe from fuel regulators to prevent loosening the connectors during the removal process.

![[05s00075.png]]

### Remove

Remove the fuel pressure regulator valve assembly.

![[05s00056.png]]

### Clean and Inspect for Reuse

> [!danger] WARNING · Опасно
> When using solvents, acids, or alkaline materials for cleaning, follow the manufacturer's recommendations for use. Wear goggles and protective clothing to reduce the possibility of personal injury.

Clean the bracket and the regulator with solvent.

![[05s00057.png]]

Inspect the regulator and the bracket for damage or debris.

Replace the regulator if damage is found.

![[05s00058.png]]

### Test

Use Digital Multimeter Kit, Part Number 3400162, and Electrical Test Lead Kit, Part Number 5299367. Measure the resistance between the supply and return pins at the fuel shutoff valve connector.

| Resistance |  |  |
|---|---|---|
|  | Ohms (for CNG engines) | Ohms (for LNG engines) |
| MIN | 21.6 | 46.8 |
| MAX | 26.4 | 57.2 |

If the resistance does **not** meet the specifications, replace the fuel shutoff valve.

![[05s00059.png]]

Measure the resistance between the supply pin and fuel shutoff valve body.

| Resistance |  |
|---|---|
|  | Ohms |
| MIN | 100k |

![[05s00060.png]]

### Install

Install the fuel pressure regulator valve assembly.

Tighten the mounting capscrews. See equipment manufacturer service information.

![[05s00056.png]]

The torque value for the nuts to regulator and the torque value for the Original Equipment Manufacturer (OEM) gas pipe to male adapter elbow are recommended by Cummins Inc. as below.

> [!tip] Момент затяжки · Torque Value
> Nuts to regulator inlet (1) 55 n•m [41 ft-lb]

> [!tip] Момент затяжки · Torque Value
> Nuts to regulator outlet (2) and each port on male adapter elbow (3) 80 n•m [59 ft-lb]

![[05s00076.png]]

### Finishing Steps

> [!danger] WARNING · Опасно
> Natural gas is explosive and flammable. Always be sure to maintain adequate ventilation in the work area. Keep all cigarettes, flames, pilot lights, arcing equipment, and switches out of the work area and areas with shared ventilation to reduce the possibility of severe personal injury or death when working on a natural gas system.

> [!danger] WARNING · Опасно
> Natural gas is lighter than air. Check the ceiling of the area where work is to be done for any possible ignition source.

> [!danger] WARNING · Опасно
> Always have proper ventilation when working on a natural gas system.

- Connect the piping connected to the fuel pressure regulator. See equipment manufacturer service information.

> [!note] Note · Примечание
> The fuel inlet and outlet connectors on fuel regulators **must** be held in place with a wrench when tightening the fitting connectors to prevent overtightening during the installation process.

![[05s00075.png]]

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

> [!warning] CAUTION · Осторожно
> To reduce the possibility of shock loading of components downstream of the supply valve, opening and closing of the gas supply valve must be done slowly.

- Connect the wiring harness of the shutoff valve.
- Slowly open the manual gas supply valve. See equipment manufacturer service information for the location of the valve.
- Connect the batteries. See equipment manufacturer service information.
- Operate the engine and check for leaks.

### Fuel Pressure Test

> [!warning] CAUTION · Осторожно
> Before removing any fuel system component, turn off the fuel supply at the vehicle's main gas shutoff valve.

Turn off the vehicle's main gas shutoff valve.

Operate the engine at low idle until the engine shuts down.

Remove the fuel supply line from the inlet to the fuel filter on the engine.

Install pressure test adapter, Part Number 5394427, at the inlet to the fuel filter on the engine. In engines that feature an air compressor, it may be necessary to adjust the angle of the fitting to allow installation of the service tool.

Connect the fuel lines.

![[05s00062.png]]

Connect a pressure gauge with a 0 kPa \[ 0 psi \] to 2068 kPa \[ 300 psi \] range to the Compuchek™ pressure fitting.

Turn on the vehicle's main gas shutoff valve.

Use a gas detector, Part Number 3165179, to check all fittings for fuel leaks.

![[05s00063.png]]

Confirm the specification of the OEM fuel tanks at the fuel pressure gauge.

Measure the gas pressure at the inlet side while operating the engine at full load and rated rpm conditions.

| Gas Pressure (Gauge) for LNG Engines |  |  |
|---|---|---|
| kpa |  | psi |
| 600 | MIN | 87 |
| 1600 | MAX | 232 |

| Gas Pressure (Gauge) for CNG Engines |  |  |
|---|---|---|
| kpa |  | psi |
| 2000 | MIN | 290 |
| 22,000 | MAX | 3191 |

If the pressure is below or above specifications, see equipment manufacturer service information.

![[05s00077.png]]

Measure the gas pressure at the outlet side while operating the engine at full load and rated rpm conditions.

| Gas Pressure (Gauge) |  |  |
|---|---|---|
| kpa |  | psi |
| 510 | MIN | 74 |
| 690 | MAX | 100 |

If the pressure is below or above specifications, replace the regulator.

![[05s00064.png]]
