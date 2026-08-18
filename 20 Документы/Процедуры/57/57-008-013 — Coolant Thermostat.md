---
aliases:
  - "Термостат системы охлаждения"
type: "Процедура"
doc: "57-008-013"
title_en: "Coolant Thermostat"
title_ru: "Термостат системы охлаждения"
modified: "2002-07-08"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666134"
figures: 22
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/57/57-008-013.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/57-008-013.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/57"
---

# Coolant Thermostat
**Термостат системы охлаждения**

> [!abstract] Процедура · `57-008-013`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666134 — QST30 Operation and Maintenance Manual|3666134]]
> **Секции:** Section 6 - Maintenance Procedures at 6000 Hours or 2 Years
> **Даты:** изменён 2002-07-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/57/57-008-013.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/57-008-013.pdf)

### Leak Test

The engine thermostat and thermostat seal **must** operate properly for the engine to operate in the most efficient heat range. Overheating or overcooling will shorten engine life.

> [!note] Note · Примечание
> The QST30 Series engine intake air temperature is monitored by the electronic control module (ECM), which will generate a fault code when the intake air temperature exceeds specifications.

![[ec800kb.png]]

**Engine Coolant Temperature below Normal**

> [!danger] WARNING · Опасно
> Do not remove the pressure cap from a hot engine. Wait until the coolant temperature is below 50°C \[120°F\] before removing the pressure cap. Heated coolant spray or steam can cause personal injury.

> [!note] Note · Примечание
> Do **not** remove the aftercooler water inlet and outlet lines from the aftercooler or thermostat housing.

Remove the upper engine radiator hoses from the thermostat housing.

![[08a00008.png]]

Install on each thermostat housing outlets a hose that is the same size and long enough to reach a dry, remote container.

Install and tighten hose clamps on the housing outlets.

Put the hose ends in separate, dry containers.

![[08a00008.png]]

Operate the engine at rated rpm for 1 minute.

Shut the engine off, and measure the amount of coolant collected in each container.

The amount of coolant collected **must not** be more than 100 cc \[3.3 fl oz\].

![[eg8gaka.png]]

> [!note] Note · Примечание
> If more than 100 cc \[3.3 fl oz\] of coolant is collected, the thermostat or the thermostat seal is leaking.

Remove the thermostat, and test for proper operation.

If the thermostat operates properly and more than 100 cc \[3.3 fl oz\] is collected during the in-chassis test, replace the thermostat seal.

![[08a00060.png]]

**Engine Coolant Temperature above Normal**

Restrict the radiator airflow. Operate the engine until the coolant temperature rises to 90 to 93°C \[194 to 199°F\].

![[ra800kb.png]]

Record the temperature of the coolant outlet hoses. An increase in temperature indicates the thermostats have started to open.

Use a contact pyrometer, or install a temperature gauge in the desired locations prior to operating the engine.

![[08a00008.png]]

Record the temperature of the radiator bottom tank or coolant-out tube.

![[ra800wh.png]]

If the difference in temperature is more than 8°C \[15°F\], either the thermostats are **not** fully open or the radiator core is plugged.

![[ec4etsa.png]]

### Remove

> [!danger] WARNING · Опасно
> Coolant is toxic. Keep away from children and pets. If not reused, dispose of in accordance with local environmental regulations.

> [!danger] WARNING · Опасно
> Do not remove the pressure cap from a hot engine. Wait until the coolant temperature is below 50°C \[120°F\] before removing the pressure cap. Heated coolant spray or steam can cause personal injury.

Open the draincock in the radiator bottom tank. Remove the lower radiator hose, if necessary.

Drain the cooling system. Refer to Procedure [[57-008-018 — Cooling System|008-018]].

![[ra8homa.png]]

Remove the thermostat housing.

![[08a00013.png]]

Inspect the housing support for damage.

> [!missing]- Иллюстрация `08a00014.png` не извлечена — смотрите PDF-оригинал документа

Remove the thermostats and seals.

Clean all gasket surfaces and bores.

![[08a00012.png]]

### Inspect for Reuse

Check the thermostat for wear or damage. If the barrel of the thermostat is worn or fretted, it **must** be discarded.

![[ec800sc.png]]

### Test

Check the temperature to see when the thermostat is designed to open.

The design temperature of this thermostat is 77°C \[171°F\]. The rated opening temperature is marked on the side of the thermostat.

![[08a00135.png]]

Suspend the thermostat and thermometer in a container of water. Do **not** let the thermostat or the thermometer touch the side of the container. Heat the water to check the temperature at which the thermostat begins to open.

| celsius |  | fahrenheit |
|---|---|---|
| 74.4°C | MIN | 166°F |
| 78.3°C | MAX | 173°F |

![[ec8bdsa.png]]

Continue to apply heat to check the temperature when the thermostat is open completely.

| mm |  | in |
|---|---|---|
| 10.0 | MIN | 0.40 |

| celsius |  | fahrenheit |
|---|---|---|
| 90°C | MIN | 194°F |

![[ec8bdsb.png]]

Remove the container from the heat.

Check to see if the thermostat returns to the CLOSED position.

![[ec8bdsc.png]]

With the thermostat open, check the thermostat for wear or damage. If the seat of the thermostat is worn or fretted, it **must** be replaced.

![[ec800sc.png]]

### Install

Use a mallet and a mandrel, or a socket with a diameter the same as the diameter of the seal case. Install the seals. The seals **must** seat in the bottom of the counterbore.

![[th6seha.png]]

Install the thermostat by pushing on the outer rim.

![[ec4bdha.png]]

Fill the cooling system. Refer to Procedure [[57-008-018 — Cooling System|008-018]].

Operate the engine to 70°C \[158°F\] coolant temperature and inspect for leaks.

![[oi803vn.png]]
