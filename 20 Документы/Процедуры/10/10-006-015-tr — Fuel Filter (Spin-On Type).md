---
aliases:
  - "Топливный фильтр (навинчиваемый)"
type: "Процедура"
doc: "10-006-015-tr"
title_en: "Fuel Filter (Spin-On Type)"
title_ru: "Топливный фильтр (навинчиваемый)"
modified: "2010-09-16"
engines:
  - "80141463"
  - "80248213"
families:
  - "QSX15"
manuals:
  - "3666239"
figures: 21
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/10/10-006-015-tr.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/10-006-015-tr.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSX15"
  - "группа/10"
---

# Fuel Filter (Spin-On Type)
**Топливный фильтр (навинчиваемый)**

> [!abstract] Процедура · `10-006-015-tr`
> **Двигатели:** [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSX15
> **Входит в руководства:** [[3666239 — Signature™, ISX, and QSX15 Service Manual|3666239]]
> **Секции:** Section 6 - Injector and Fuel Lines - Group 06
> **Даты:** изменён 2010-09-16
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/10/10-006-015-tr.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/10-006-015-tr.pdf)

### Initial Check

With Pressurized Fuel Filtering

Install a pressure gauge, Part Number 3824877 (2758 kPa \[400 psi\]), on the fuel pump Compuchek™ fitting, to measure the fuel pressure before the fuel filter.

![[06c00088.png]]

Start the engine and operate at high idle and no load.

Measure and record the fuel pressure.

Shut the engine off.

Remove the pressure gauge from the fuel pump.

![[06c00089.png]]

Install a pressure gauge, Part Number 3824877 (275 kPa \[400 psi\]), on the rail fuel pressure Compuchek™ fitting located on the IFSM to measure the fuel pressure after the filter.

![[06c00090.png]]

Start the engine and operate at high idle and no load.

Measure and record the fuel pressure.

Shut the engine off.

Remove the pressure gauge from the rail fuel pressure Compuchek™ fitting.

The pressure difference between the rail fuel pressure and fuel pump pressure is the differential pressure.

| Fuel Filter Restriction |  |  |
|---|---|---|
| kpa |  | psi |
| 517 | MAX | 75 |

If the fuel filter restriction is above specifications, replace the filter.

![[06c00091.png]]

With Vacuum Fuel Filtering

Connect a vacuum gauge to either suction-side Compuchek™ fitting.

> [!note] Note · Примечание
> Some engines equipped with priming pumps do **not** have a lower Compuchek™ fitting and have an air bleed line plumbed into the upper location. Reference the Install Section for measuring inlet restriction.

![[05c00113.png]]

Disconnect the air bleed line from the upper location on the IFSM. Insert a Compuchek™ fitting in this location and run a line to a catch container.

![[06c00092.png]]

Start the engine.

After the fuel lift pump stops running and with the engine operating at idle, disconnect the hose to the catch container.

Connect the vacuum gauge to the Compuchek™ fitting and measure the fuel inlet restriction.

![[06c00093.png]]

Operate the engine at high idle and no load.

| Fuel Inlet Restriction |  |  |  |  |
|---|---|---|---|---|
|  | mm-hg |  | in-hg |  |
| Upper Location |  | 356 | MAX | 14 |
| Lower Location |  | 305 | MAX | 12 |

An inlet restriction greater than specification indicates either a dirty fuel filter or a restriction in the OEM fuel supply plumbing. Inlet restriction at the fuel supply connection **must** be checked to identify the correct source of the restriction.

![[06c00094.png]]

### Remove

With Pressurized Fuel Filtering

> [!danger] WARNING · Опасно
> Fuel is flammable. Keep all cigarettes, flames, pilot lights, arcing equipment, and switches out of the work area and areas sharing ventilation to reduce the possibility of severe personal injury or death when working on the fuel system.

Clean the area around the fuel filter head and filter.

Remove the fuel filter with filter wrench, Part Number 3400157.

![[06c00102.png]]

With Vacuum Fuel Filtering

> [!danger] WARNING · Опасно
> Fuel is flammable. Keep all cigarettes, flames, pilot lights, arcing equipment, and switches out of the work area and areas sharing ventilation to reduce the possibility of severe personal injury or death when working on the fuel system.

Clean the area around the fuel filter head and filter.

Disconnect the wiring harness from the water-in-fuel sensor, if equipped.

Remove the fuel filter with filter wrench, Part Number 3400158.

![[00c00013.png]]

### Clean

All Applications

Use a clean, lint-free cloth to clean the filter head gasket surface.

![[00c00014.png]]

### Install

With Pressurized Fuel Filtering

Use the correct filter(s) for your engine. It **must** remove a minimum of 95 percent of free and emulsified water. It **must** also have a minimum of 98.7 percent 15-micron particle-removal efficiency.

[[10-018-024-om-auto — Filter Specifications|Refer to Procedure 018-024 in Section V]].

Apply a thin coating of clean engine oil to the filter gasket surface.

![[00c00015.png]]

> [!warning] CAUTION · Осторожно
> Mechanical overtightening of the filter can distort the threads or damage the filter element seal.

> [!note] Note · Примечание
> Do not prefill the fuel filter. Damage to the fuel system may result.

Install the filter onto the filter head. Turn the filter until the gasket contacts the filter head surface.

Tighten the filter an additional ¾ of a turn after the gasket contacts the filter head surface, or as specified by the filter manufacturer.

![[ff8bdaa.png]]

To perform the priming procedure, use the following items to fabricate a fuel bypass hose:

- 2- Quick-disconnect fittings, Part Number 3376859
- Clear tubing (capable of 2758 kPa \[400 psi\])

Install the fuel bypass hose fabricated above between the suction-side Compuchek™ fitting at the top of the IFSM and the fuel pump Compuchek™ fitting located on the head of the fuel pump.

Connect the clear hose and the shutoff valve normally used to check for air-in-fuel to the rail Compuchek™ fitting. Refer to Procedure 006-003 in Section 6. Place the open end of the tube in a suitable container and fully open the shutoff valve in the hose.

![[19c01879.png]]

Fill the fuel filter by turning the ignition switch to the ON position, but do not start the engine. The fuel lift pump should begin to operate. Monitor the open end of the bleed line from the rail Compuchek™. When fuel is seen coming out of this line, turn the ignition OFF. Remove the bleed line and the air-in-fuel test line.

![[05c00155.png]]

With Vacuum Fuel Filtering and Priming Pump

Use the correct filter(s) for your engine. It **must** remove a minimum of 95 percent of free and emulsified water. It **must** also have a minimum of 98.7 percent at 25-micron particle-removal efficiency.

[[10-018-024-om-auto — Filter Specifications|Refer to Procedure 018-024 in Section V]].

Apply a thin coating of clean engine oil to the filter gasket surface and the center seal.

![[00c00015.png]]

> [!warning] CAUTION · Осторожно
> Mechanical overtightening of the filter can distort the threads or damage the filter element seal.

> [!note] Note · Примечание
> Do not prefill the fuel filter. Damage to the fuel system may result.

Install the filter onto the filter head. Turn the filter until the gasket contacts the filter head surface.

Tighten the filter an additional 3/4 of a turn after the gasket contacts the filter head surface, or as specified by the filter manufacturer.

If the filter is equipped with a water-in-fuel sensor, rotate the sensor to the desired location and connect the wiring harness.

![[ff8bdaa.png]]

> [!note] Note · Примечание
> The engine will, perhaps, run rough for several minutes until the air is out of the system.

Fill the fuel filter by turning the ignition keyswitch to the ON position. The priming pump will operate for 2 minutes, which will adequately fill the fuel filter. The engine can then be started.

Some engines utilize a manual, remote mount priming pump. Flip the priming pump mounted toggle switch to the ON position. Operate the pump for 2 minutes and shut it off. The engine can then be started.

![[05c00155.png]]

With Vacuum Fuel Filtering and Without Priming Pump

Use the correct filter(s) for your engine. It **must** remove a minimum of 95 percent of free and emulsified water. It **must** also have a minimum of 98.7 percent at 25-micron particle-removal efficiency.

[[10-018-024-om-auto — Filter Specifications|Refer to Procedure 018-024 in Section V]].

Apply a thin coating of clean engine oil to the filter gasket surface and the center seal.

![[00c00015.png]]

> [!warning] CAUTION · Осторожно
> Mechanical overtightening of the filter can distort the threads or damage the filter element seal.

> [!note] Note · Примечание
> If the filter is equipped with a water-in-fuel sensor, rotate the sensor on the filter to the desired location and connect the wiring harness. Fill the filter with clean fuel prior to installation.

Install the filter onto the filter head. Turn the filter until the gasket contacts the filter head surface.

Tighten the filter an additional 3/4 of a turn after the gasket contacts the filter head surface, or as specified by the filter manufacturer.

![[ff8bdaa.png]]

> [!note] Note · Примечание
> The engine will, perhaps, run rough for several minutes until the air is out of the system.

Remove the external hex plug on the top ofthe integrated fuel system module. Crank the engine until a solid stream of fuel comes out of the port.

Install the hex plug.

Crank the engine for 20 seconds. If the engine does **not** start within 20 seconds, wait two minutes. It will probably be necessary to remove the filter, fill the filter with clean fuel, and install the filter.

Repeat these steps until the engine starts.

![[05c00155.png]]
