---
aliases:
  - "Воздух в топливе"
type: "Процедура"
doc: "20-006-003"
title_en: "Air in Fuel"
title_ru: "Воздух в топливе"
modified: "2023-01-02"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4021592"
figures: 12
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/20/20-006-003.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/20-006-003.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/20"
---

# Air in Fuel
**Воздух в топливе**

> [!abstract] Процедура · `20-006-003`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021592 — QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual|4021592]]
> **Секции:** Section 6 - Injectors and Fuel Lines - Group 06
> **Даты:** изменён 2023-01-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/20/20-006-003.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/20-006-003.pdf)

### General Information

with Mechanically Actuated Injector

> [!danger] WARNING · Опасно
> Fuel is flammable. Do not allow cigarettes, flames, sparks, arcing switches or equipment, pilot lights or other ignition sources near the fuel system.

There are two good methods to check for air in the fuel on a fuel system with mechanically actuated injectors:

- Sight Glass Method
- Gear Pump Drain Method.

![[fp8tbka.png]]

with Electronically Actuated Injector

For engines with electronically actuated injectors, use the Prime section of the Fuel Filter (Stage 1) procedure to check for air in the fuel system and to remove all the air from the fuel system. [[20-006-075-tr — Fuel Filter (Stage 1)|Refer to Procedure 006-075 in Section 6.]]

![[06k00007.png]]

> [!danger] WARNING · Опасно
> Fuel is flammable. Do not allow cigarettes, flames, sparks, arcing switches or equipment, pilot lights or other ignition sources near the fuel system.

If air is still seen after completing the previous procedure, check the fuel supply lines for loose connections or damaged o-rings. [[20-006-024-tr — Fuel Supply Lines|Refer to Procedure 006-024 in Section 6.]]

![[06k00008.png]]

### Test

with Mechanically Actuated Injector

> [!danger] WARNING · Опасно
> Fuel is flammable. Do not allow cigarettes, flames, sparks, arcing switches or equipment, pilot lights or other ignition sources near the fuel system.

#### Sight Glass Method

- Remove the fuel inlet line
- Install a sight glass, Part Number 3163270, at the inlet of the fuel pump.
- Operate the engine at high idle with no load.

A small air leak will have a "milky" appearance.

A large air leak will look like bubbles in the fuel.

> [!note] Note · Примечание
> If the application incorporates a Day tank or a Positive Head Fuel System it is recommended to apply a sight glass before this accessory as these devices may mask the presence of air in fuel upstream.

![[06400061.png]]

If an air leak is found, perform the following.

- Systematically inspect the entire fuel supply routing for sources of air ingress starting at the fuel tank followed by all hose/tube interconnections, fuel filtration hardware and day tank/positive head fuel system, if provisioned. Tighten any loose connections as needed.
- Check the drop tube in the fuel tank for damage.
- Check the fuel return to tank and ensure the tube is both above fuel level and at a minimum distance of 305 mm \[ 12 in \] from the fuel supply connection.
- Check the o-rings for damage.

![[ft8hssa.png]]

Continue to test and look for the source of the air until **no** air bubbles are visible.

Remove the sight glass.

Install and tighten the fuel inlet hose.

> [!tip] Момент затяжки · Torque Value
> 88 n•m [65 ft-lb]

Retest the engine duplicating the operating conditions when performance complaint occurred to confirm air in fuel correction. This is especially important for standby Generator applications with infrequent starts and may require testing after an extended rest period.

![[06400033.png]]

Gear Pump Drain Method

To perform a pressure side air in fuel test, use the following items.

- Quick disconnect fitting, Part No. 3376859
- High pressure Hose
- Pressure valve (capable of 2758 kPa \[400 psi\])
- Clean tubing
- Clean container

![[06400034.png]]

Connect the equipment to the quick-connect fitting at the fuel pump outlet.

Place the end of the clear hose in the clean container.

![[06400035.png]]

Operate the engine at high idle with no load. **Slowly** open the valve until a steady stream of fuel is visible.

![[06400036.png]]

Place the end of the hose below the surface of the fuel.

If there is an air leak, bubbles will be visible.

> [!note] Note · Примечание
> If the application incorporates a Day tank or a Positive Head Fuel System it is recommended to use the Sight Glass Method placed before this accessory as these devices may mask the presence of air in fuel upstream.

![[06400062.png]]

If an air leak is found, perform the following.

- Systematically inspect the entire fuel supply routing for sources of air ingress starting at the fuel tank followed by all hose/tube interconnections, fuel filtration hardware and day tank/positive head fuel system, if provisioned. Tighten any loose connections as needed.
- Check the drop tube in the fuel tank for damage.
- Check the fuel return to tank and ensure the tube is both above fuel level and at a minimum distance of 305 mm \[ 12 in \] from the fuel supply connection.
- Check the o-rings for damage.

![[ft8hssa.png]]

Continue to test and look for air leaks until there are **no** bubbles visible.

Remove the test equipment.

Retest engine duplicating the operating conditions when performance complaint occurred to confirm air in fuel correction. This is especially important for standby Generator applications with infrequent starts and may require testing after an extended rest period.

Install and tighten the fuel inlet hose.

> [!tip] Момент затяжки · Torque Value
> 88 n•m [65 ft-lb]

![[06400035.png]]
