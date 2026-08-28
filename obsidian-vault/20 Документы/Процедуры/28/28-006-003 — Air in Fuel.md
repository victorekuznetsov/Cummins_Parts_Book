---
aliases:
  - "Воздух в топливе"
type: "Процедура"
doc: "28-006-003"
title_en: "Air in Fuel"
title_ru: "Воздух в топливе"
modified: "2023-01-02"
engines:
  - "33239746"
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
manuals:
  - "4021528"
figures: 15
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/28/28-006-003.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/28-006-003.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/28"
---

# Air in Fuel
**Воздух в топливе**

> [!abstract] Процедура · `28-006-003`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Входит в руководства:** [[4021528 — K38, K50, QSK38, and QSK50 Service Manual|4021528]]
> **Секции:** Section 6 - Injectors and Fuel Lines - Group 06
> **Даты:** изменён 2023-01-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/28/28-006-003.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/28-006-003.pdf)

### General Information

There are two good methods to check for air in the fuel.

1. Sight glass method
2. Gear pump drain method.

![[fp8tbka.png]]

### Test

with Mechanically Actuated Injector

> [!danger] WARNING · Опасно
> Depending on the circumstance fuel is flammable. Keep all cigarettes, flames, pilot lights, arcing equipment, and switches out of the work area and areas sharing ventilation to reduce the possibility of severe personal injury or death when working on the fuel system.

> [!danger] WARNING · Опасно
> Do not vent the fuel system on a hot engine; this can cause fuel to spill onto a hot exhaust manifold, which can cause a fire.

Sight Glass Method

Remove the fuel inlet line.

Install a sight glass, Part Number 3163270, at the inlet of the fuel pump.

Operate the engine at high idle with no load.

A small air leak will have a "milky" appearance.

A large air leak will look like bubbles in the fuel.

> [!note] Note · Примечание
> If the application incorporates a Day tank or a Positive Head Fuel System it is recommended to apply a sight glass before this accessory as these devices may mask the presence of air in fuel upstream.

![[06400061.png]]

If an air leak is found, perform the following:

- Systematically inspect the entire fuel supply routing for sources of air ingress starting at the fuel tank followed by all hose/tube interconnections, fuel filtration hardware and day tank/positive head fuel system, if provisioned. Tighten any loose connections as needed.
- Check the drop tube in the fuel tank for damage.
- Check the fuel return to tank and ensure the tube is both above fuel level and at a minimum distance of 305 mm \[ 12 in \] from the fuel supply connection.
- Check the o-rings for damage.

![[ft8hssa.png]]

Continue to test and look for the source of air until no air bubbles are visible.

Remove the sight glass.

Install and tighten the fuel inlet hose.

> [!tip] Момент затяжки · Torque Value
> 120 n•m [89 ft-lb]

Retest engine duplicating the operating conditions when performance complaint occurred to confirm air in fuel correction. This is especially important for standby Generator applications with infrequent starts and may require testing after an extended rest period.

![[06400033.png]]

Gear Pump Drain Method

> [!danger] WARNING · Опасно
> Fuel is flammable. Keep all cigarettes, flames, pilot lights, arcing equipment, and switches out of the work area and areas sharing ventilation to avoid severe personal injury or death when working on the fuel system.

To perform a pressure-side air in fuel test, use the following items:

- Quick-disconnect female fitting
- High pressure hose
- Pressure valve (capable of 2758 kPa \[400 psi\])
- Clear tubing
- Clean container.

![[06400034.png]]

Connect the equipment to the quick connect fitting at the fuel pump outlet.

Put the end of the clear tubing into the clean container.

![[06400035.png]]

> [!danger] WARNING · Опасно
> Depending on the circumstance fuel is flammable. Keep all cigarettes, flames, pilot lights, arcing equipment, and switches out of the work area and areas sharing ventilation to reduce the possibility of severe personal injury or death when working on the fuel system.

> [!danger] WARNING · Опасно
> Do not vent the fuel system on a hot engine; this can cause fuel to spill onto a hot exhaust manifold, which can cause a fire.

Operate the engine at high idle with no load. Slowly open the valve until a steady stream of fuel is visible.

![[06400036.png]]

Put the end of the tube below the surface of the fuel.

If there is an air leak, bubbles will be visible.

> [!note] Note · Примечание
> If the application incorporates a Day tank or a Positive Head Fuel System it is recommended to use the Sight Glass Method placed before this accessory as these devices may mask the presence of air in fuel upstream.

![[06400062.png]]

If an air leak is found, perform the following:

- Systematically inspect the entire fuel supply routing for sources of air ingress starting at the fuel tank followed by all hose/tube interconnections, fuel filtration hardware and day tank/positive head fuel system, if provisioned. Tighten any loose connections as needed.
- Check the drop tube in the fuel tank for damage.
- Check the fuel return to tank and ensure the tube is both above fuel level and at a minimum distance of 305 mm \[ 12 in \] from the fuel supply connection.
- Check the o-rings for damage.

Remove the test equipment from the quick connect fitting at the fuel pump outlet.

Retest engine duplicating the operating conditions when performance complaint occurred to confirm air in fuel correction. This is especially important for standby Generator applications with infrequent starts and may require testing after an extended rest period.

![[ft8hssa.png]]

with Electronically Actuated Injector

> [!danger] WARNING · Опасно
> Depending on the circumstance fuel is flammable. Keep all cigarettes, flames, pilot lights, arcing equipment, and switches out of the work area and areas sharing ventilation to reduce the possibility of severe personal injury or death when working on the fuel system.

> [!danger] WARNING · Опасно
> Do not vent the fuel system on a hot engine; this can cause fuel to spill onto a hot exhaust manifold, which can cause a fire.

Disconnect the air bleed line from the air bleed valve.

Remove the air bleed valve from the fuel drain manifold.

![[06300050.png]]

> [!note] Note · Примечание
> A significant amount of fuel will flow from the air bleed line. Be sure the minimum bucket capacity is 19 liters \[5 gallons\].

Install the air bleed valve onto the air bleed line.

Route the air bleed line and valve into the 19 liter \[5 gallon\] bucket.

![[06700146.png]]

Plug the fuel drain manifold. Use a M16 x 1.5 straight thread standard plug or fuel system tester, Part Number 4918612.

![[22k00011.png]]

Start the engine. Allow it to idle.

Watch the fuel flow from the air bleed valve.

If the flow is constant and the stream is steady, there is no air entering the fuel system. If the flow intermittently drops out or is erratic, air is entering the fuel system.

![[06700146.png]]

If air is entering the fuel system, check the fuel supply lines for loose connections or damaged o-rings. Use the following procedure or equipment manufacturer service information. [[28-006-024-tr — Fuel Supply Lines|Refer to Procedure 006-024 in Section 6.]]

![[06300051.png]]

Remove the plug or fuel system tester. Install the air bleed valve and the air bleed line.

![[06300050.png]]
