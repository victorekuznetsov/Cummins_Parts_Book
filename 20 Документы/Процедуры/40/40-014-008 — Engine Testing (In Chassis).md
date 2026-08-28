---
aliases:
  - "Испытание двигателя на машине"
type: "Процедура"
doc: "40-014-008"
title_en: "Engine Testing (In Chassis)"
title_ru: "Испытание двигателя на машине"
modified: "2006-04-24"
engines:
  - "93047320"
families:
  - "6B5.9"
manuals:
  - "3666087"
figures: 17
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/40/40-014-008.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/40-014-008.pdf"
tags:
  - "документ/процедура"
  - "двигатель/6B5.9"
  - "группа/40"
---

# Engine Testing (In Chassis)
**Испытание двигателя на машине**

> [!abstract] Процедура · `40-014-008`
> **Двигатели:** [[93047320 — 6B5.9 CPL 3111|93047320]]
> **Семейство:** 6B5.9
> **Входит в руководства:** [[3666087 — B3.9, B4.5, B4.5 RGT, and B5.9 Service Manual|3666087]]
> **Секции:** Section 14 - Engine Testing - Group 14
> **Даты:** изменён 2006-04-24
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/40/40-014-008.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/40-014-008.pdf)

### Initial Check

B3.9, B5.9, and B4.5 Engines

It is very time consuming and expensive to remove internal engine components to diagnose failures. A compression gauge and adapter can be used as an aid in checking for failures.

![[oi900vp.png]]

Use the compression gauge and adapter to check for following component failures:

1. Piston ring sealing
2. Intake and exhaust valve sealing
3. Cylinder head gasket sealing
4. Cylinder head cracked.

See the appropriate procedures for the replacement of failed components.

![[kn9bdka.png]]

> [!note] Note · Примечание
> Due to variables such as starter and battery conditions that affect engine cranking speed, it is difficult to establish an absolute value for compression pressure; however, the following values can be used as guidelines:

- New engine (cranking speed @ 250 rpm) 2413 kPa \[350 psi\]
- Used engine (cranking speed @ 250 rpm) 2068 kPa \[300 psi\].

It is recommended that the compression pressure be checked on all cylinders and then compared to specification. All cylinders **must** be within 690 kPa \[100 psi\] of each other.

![[oi900kn.png]]

Piston Ring Sealing

If the compression is low but can be increased significantly by squirting oil into the cylinder, the cause is inadequate sealing between the rings and the cylinder walls.

Refer to [[40-001-054-tr — Piston and Connecting Rod Assembly|Procedure 001-054]] for piston ring replacement.

![[oi900ka.png]]

Intake and Exhaust Valve Sealing

If the compression is low on one or more nonadjacent cylinders, and the pressure can **not** be increased by oiling the rings, poor valve sealing is suspected.

Refer to [[40-002-004-tr — Cylinder Head|Procedure 002-004]] for cylinder head replacement.

![[oi900kb.png]]

Valve leakage is often an audible sound from the intake and exhaust manifolds.

![[oi900kc.png]]

Cylinder Head Gasket Sealing

If the compression is low on adjacent cylinders, and the pressure can **not** be increased by oiling the rings, the cylinder head gasket is probably leaking between the cylinders.

Refer to [[40-002-021-tr — Cylinder Head Gasket|Procedure 002-021]] for cylinder gasket replacement.

![[oi900kd.png]]

> [!note] Note · Примечание
> Low compression on a single cylinder can be caused by an external leak or a leak to a coolant passage. A leak to a coolant passage of this magnitude will also result in coolant in the cylinder.

![[oi900ke.png]]

A compression leak to the coolant will normally be detected by a loss of coolant as the coolant is blown from the cooling system.

Service Tip: Remove the drive belt from the water pump. Refer to [[40-008-002-tr — Drive Belt, Cooling Fan|Procedure 008-002]] for removal and installation of drive belt.

Run the engine for one to two minutes, and check for coolant being blown from the radiator by compression gases.

![[oi900kf.png]]

B4.5 RGT Engines

For B4.5 RGT engines, no compression service tools are available. To inspect for loss of compression, a blow-by check should be performed. Refer to [[100-014-010 — Crankcase Blowby, Measure|Procedure 014-010]].

![[nobox.png]]

### Test

> [!note] Note · Примечание
> The compressed air load in the accompanying illustration **must** be attached to the air compressor outlet (2).

Make sure the air compressor will be unloaded during the performance check.

Apply regulated air pressure of 655 kPa \[95 psi\] to the air compressor unloader (1).

![[cp900va.png]]

> [!warning] CAUTION · Осторожно
> Do not crank the engine for more than 30 seconds. Excessive heat will damage the starting motor.

Crank the engine and observe the oil pressure when the engine starts. If the engine fails to start within 30 seconds, allow the starting motor to cool for two minutes before cranking the engine again.

![[st8bdba.png]]

> [!warning] CAUTION · Осторожно
> If the lubricating oil pressure is not within specifications, shut off the engine immediately. Low lubricating oil pressure will cause engine damage. Correct the problem if lubricating oil pressure is not within specifications.

Engine lubricating oil pressure **must** be at least 69 kPa \[10 psi\] at approximately 700 rpm.

![[oi902vv.png]]

> [!note] Note · Примечание
> The horsepower readings will **not** be accurate if the lubricating oil temperature and fuel temperature are **not** within specifications.

Make sure the engine is at operating temperature.

Move the throttle lever to the FULL-OPEN position. Adjust the dynamometer load until the engine maintains the rated rpm.

Allow the readings to stabilize. Read the horsepower.

Check all gauges, and record the readings.

| Measurements |  |  |
|---|---|---|
|  | celsius | fahrenheit |
| Lubricating Oil Temperature | 90 | 194 |

| Measurements |  |  |
|---|---|---|
|  | celsius | fahrenheit |
| Fuel Temperature | 32 | 90 |

![[oi901vt.png]]

> [!warning] CAUTION · Осторожно
> Do not shut off the engine immediately after it has been loaded. It must be allowed to cool sufficiently. Failure to do so will result in engine damage.

> [!note] Note · Примечание
> Idle periods longer than five minutes are to be avoided.

Remove the dynamometer load completely, and operate the engine at idle speed for three to five minutes. This will allow the turbocharger and other components to cool.

![[oi804vm.png]]

Shut off the engine after the cool-down period.

![[oi802vx.png]]

> [!note] Note · Примечание
> If the engine is to be stored temporarily and does **not** have permanent-type antifreeze, it is necessary to drain all coolant.

Remove all test instrumentation.

Remove the engine from the dynamometer.

![[bp9gama.png]]
