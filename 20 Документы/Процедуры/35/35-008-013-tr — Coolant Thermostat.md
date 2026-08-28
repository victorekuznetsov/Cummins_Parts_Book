---
aliases:
  - "Термостат системы охлаждения"
type: "Процедура"
doc: "35-008-013-tr"
title_en: "Coolant Thermostat"
title_ru: "Термостат системы охлаждения"
modified: "2011-12-19"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "3666322"
figures: 21
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/35/35-008-013-tr.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/35-008-013-tr.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/35"
---

# Coolant Thermostat
**Термостат системы охлаждения**

> [!abstract] Процедура · `35-008-013-tr`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[3666322 — ISM, ISMe, and QSM11 Service Manual|3666322]]
> **Секции:** Section 8 - Cooling System - Group 08
> **Даты:** изменён 2011-12-19
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/35/35-008-013-tr.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/35-008-013-tr.pdf)

### Leak Test

The engine thermostat and thermostat seal **must** operate properly in order for the engine to operate in the most efficient heat range. Overheating or overcooling will shorten engine life.

[[35-008-016-tr — Coolant Thermostat Seal|Refer to Procedure 008-016 in Section 8]] to inspect the thermostat seal.

![[ec800kb.png]]

> [!danger] WARNING · Опасно
> Complete this test with the engine coolant temperature below 50°C \[120°F\]. Hot steam can cause serious personal injury.

Remove the radiator hose from the thermostat housing.

![[wo2hoha.png]]

Install a thermocouple or temperature gauge, which is known to be accurate, in the water header plate or engine side of the thermostat housing.

![[oi200kf.png]]

Install a hose of the same size on the thermostat housing outlet. It **must** be long enough to reach a remote, dry container used to collect coolant.

Install and tighten a hose clamp on the housing outlet.

Place the other end of the hose in a dry container.

![[ec200kd.png]]

Operate the engine at rated rpm for 1 minute.

Shut off the engine, and measure the amount of coolant collected in the container.

The amount of coolant collected **must not** be more than 100 cc \[3.3 fl oz\].

![[ec800kc.png]]

If more than 100 cc \[3.3 fl oz\] of coolant is collected, the thermostat seal is leaking and **must** be replaced.

[[35-008-016-tr — Coolant Thermostat Seal|Refer to Procedure 008-016 in Section 8]] to replace the seal.

![[ec200kc.png]]

Complete the following test in-chassis to test the thermostat opening temperature.

Start the engine and monitor the water temperature gauge and the container.

| Thermostat Initial Opening Temperature |  |  |
|---|---|---|
| celsius |  | fahrenheit |
| 81 | MIN | 178 |
| 83 | MAX | 181 |

Shut off the engine when the coolant starts to flow.

If coolant does **not** start flowing into the container during the initial opening temperature range, the thermostat **must** be replaced.

![[oi200kg.png]]

### Remove

> [!danger] WARNING · Опасно
> Do not remove the pressure cap from a hot engine. Wait until the coolant temperature is below 50°C \[120°F\] before removing the coolant system pressure cap. Heated coolant spray or steam can cause personal injury.

Remove the pressure cap when the engine is cool.

![[ra800qa.png]]

> [!danger] WARNING · Опасно
> Coolant is toxic. Keep away from children and pets. If not reused, dispose of in accordance with local environmental regulations.

Drain the cooling system as follows:

- Open the radiator draincock.
- Remove the lower radiator hose.

![[ra8homa.png]]

Remove the upper coolant hose from the thermostat housing.

Loosen the coolant bypass hose clamps.

> [!note] Note · Примечание
> Some models could have a converter cooler disc located in the bypass hose. [[35-008-065-tr — Torque Converter Cooler|Refer to Procedure 008-065 in Section 8.]]

![[th2homa.png]]

Remove the four thermostat housing mounting capscrews and the thermostat housing.

![[th2hsha.png]]

Remove the thermostat from the housing.

![[ec200hb.png]]

### Inspect for Reuse

Inspect the thermostat seal for cracks, corrosion, or other damage.

If the seal is damaged, it **must** be replaced. [[35-008-016-tr — Coolant Thermostat Seal|Refer to Procedure 008-016 in Section 8.]]

![[th200sa.png]]

Inspect the thermostat for damage.

![[ec2bdsa.png]]

Suspend the thermostat and a 100°C \[212°F\] thermometer in a container of water.

Do **not** allow the thermostat or thermometer to touch the container.

Heat the water and check the thermostat as follows:

![[ec200na.png]]

The nominal operating temperature is stamped on the thermostat.

- Thermostat **must** begin to open within 1°C \[2°F\] of the nominal temperature.
- Thermostat **must** be fully open within 12°C \[22°F\] of the nominal temperature.

The fully open distance between the thermostat flange and housing is 11 mm \[0.435 in\].

If the thermostat operates properly and more than 100 cc \[3.3 fl oz\] leakage is detected during in-chassis test, replace the thermostat. [[35-008-016-tr — Coolant Thermostat Seal|Refer to Procedure 008-016 in Section 8.]]

![[ec2bdga.png]]

### Install

Install the thermostat in the housing.

Install a new o-ring seal in the groove on the thermostat housing mounting surface.

![[ec200hb.png]]

Install the hose on the thermostat housing bypass outlet.

Install the thermostat housing and four mounting capscrews.

Tighten the mounting capscrews.

> [!tip] Момент затяжки · Torque Value
> 54 n•m [40 ft-lb]

![[th2hsha.png]]

Install the upper coolant hose to the thermostat housing outlet.

Tighten the coolant bypass hose clamps.

> [!tip] Момент затяжки · Torque Value
> 5 n•m [44 in-lb]

![[th2hohb.png]]

Close the cooling system draincock, and install the lower coolant hose.

Tighten the hose clamp.

Refer to the OEM's specifications for the correct torque value.

![[ra8hsha.png]]

The correct concentration of coolant additives **must** be used in the cooling system. Refer to Procedure 018-004 in Section V of the Operation and Maintenance Manual, ISM and ISMe, Bulletin 3666319.

Fill the cooling system. [[35-008-018-tr — Cooling System|Refer to Procedure 008-018 in Section 8.]]

Fill the cooling system. [[35-008-018-om-ind — Cooling System|Refer to Procedure 008-018 in Section 6.]]

Operate the engine until it reaches 80°C \[180°F\], and check for coolant leaks.

![[oi803vn.png]]
