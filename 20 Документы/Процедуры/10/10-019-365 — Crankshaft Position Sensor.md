---
aliases:
  - "Датчик положения коленчатого вала"
type: "Процедура"
doc: "10-019-365"
title_en: "Crankshaft Position Sensor"
title_ru: "Датчик положения коленчатого вала"
modified: "2023-08-18"
engines:
  - "80141463"
  - "80248213"
families:
  - "QSX15"
manuals:
  - "3666239"
figures: 11
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/10/10-019-365.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/10-019-365.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSX15"
  - "группа/10"
---

# Crankshaft Position Sensor
**Датчик положения коленчатого вала**

> [!abstract] Процедура · `10-019-365`
> **Двигатели:** [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSX15
> **Входит в руководства:** [[3666239 — Signature™, ISX, and QSX15 Service Manual|3666239]]
> **Секции:** Section 19 - Electronic Controls - Group 19
> **Даты:** изменён 2023-08-18
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/10/10-019-365.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/10-019-365.pdf)

### Remove

The crankshaft position sensor is located in the lower gear cover, behind the vibration damper.

Disconnect the crankshaft position sensor from the engine harness. Slide the locking tab sideways. Push down on the button toward the rear of the connector and disconnect it from crankshaft position sensor.

Remove the capscrew that secures the crankshaft position sensor to the lower gear cover.

Remove the crankshaft position sensor from the mounting location.

> [!note] Note · Примечание
> The lower gear cover may also be referred to as the gear HSG (housing) sensor adapter.

![[19o00110.png]]

### Inspect for Reuse

Inspect the crankshaft position sensor for debris, cracks, or other damage from contact with the crankshaft position sensor tone wheel.

If there is debris on the crankshaft position sensor, clean crankshaft position sensor.

If the crankshaft position sensor is chipped, cracked, extruded, or otherwise damaged, replace the crankshaft position sensor.

If the crankshaft position sensor retainer is bent or distorted and can **not** be returned to its original position, the crankshaft position sensor **must** be replaced.

![[19c01913.png]]

Inspect the crankshaft position sensor bore and mounting surface for corrosion or damage.

If corrosion is found, it should be removed. Use care to keep corrosion on the outside of the engine. Lightly scrape the crankshaft position sensor bore and mounting surface to remove any corrosion buildup. Do **not** use a file to remove the buildup material. The crankshaft position sensor bore may be damaged. Wipe the crankshaft position sensor bore and mounting surface clean with a cloth saturated with a spray cleaner.

If the mounting surface or the crankshaft position sensor bore is damaged and the crankshaft position sensor will **not** insert fully into the crankshaft position sensor bore, the component will need to be repaired or replaced.

![[19903763.png]]

> [!warning] CAUTION · Осторожно
> Minimal force is required to check the crankshaft position sensor tone wheel. If too much force is applied, damage to the engine may occur.

Use a small pry bar to carefully attempt to move the crankshaft position sensor tone wheel laterally. If the crankshaft position sensor tone wheel moves, it should be inspected. Refer to Procedure 001-069 in Section 1.

![[19903764.png]]

Locate the valve set marks on the outside of the vibration damper and the alignment mark on the gear cover.

One complete revolution of the crankshaft is required to inspect the crankshaft position sensor tone wheel.

![[03c00219.png]]

Use the following procedure for instructions on barring the engine. [[10-000-017 — Engine Barring|Refer to Procedure 000-017 in Section 0.]]

![[00900645.png]]

> [!danger] WARNING · Опасно
> Do not pull or pry on the fan to manually rotate the engine. To do so can damage the fan blades. Damaged fan blades can cause premature fan failures which can result in serious personal injury or property damage.

The crankshaft rotation is **clockwise**, as viewed from the front of the engine.

![[00900646.png]]

Use a light to observe the crankshaft position sensor tone wheel through the crankshaft position sensor bore while barring the engine one complete revolution.

Stop rotating the engine with a solid portion of the crankshaft position sensor tone wheel between two notches, centered in crankshaft position sensor bore.

If the crankshaft position sensor tone wheel is cracked, appears bent, or has any damage, it **must** be replaced. Refer to Procedure 001-069 in Section 1.

![[19o00111.png]]

### Measure

The crankshaft position sensor air gap is **not** adjustable.

Air gap can be measured using a depth micrometer or dial caliper.

First measure from the crankshaft position sensor mounting surface to the surface of the crankshaft position sensor tone wheel. Record the measurement.

Bar the crankshaft 90 degrees and repeat the measurement. Record the measurement. Repeat this process for one full crankshaft revolution. If the minimum and maximum values recorded vary by more than 0.051 mm \[ 0.002 in \] the crankshaft position sensor tone wheel is warped or loose, or the crankshaft is moving. For accurate results, these measurements **must** be made on the solid portion of crankshaft position sensor tone wheel, **not** in the notches of crankshaft position sensor tone wheel.

Second, measure the crankshaft position sensor from the mounting flange (2) to the end of the crankshaft position sensor (1).

Subtract the crankshaft position sensor length (second measurement) from the minimum measured crankshaft position sensor tone wheel depth (first measurement).

Air gap is the difference in these numbers.

| Air Gap |  |  |
|---|---|---|
| mm |  | in |
| 0.2 | MIN | 0.009 |
| 02.25 | MAX | 0.089 |

Maximum Target Runout: 0.5 mm \[ 0.02 in \].

> [!note] Note · Примечание
> It may be necessary to remove the vibration damper to perform this measurement.

If air gap is out of specifcations, this indicates an issue with either the crankshaft position sensor, crankshaft position sensor tone wheel, or the mounting component.

If air gap is in specification, but increasing or decreasing, the air gap corrects the issue, this indicates an issue with the crankshaft position sensor.

![[19602353.png]]

### Test

Connect the crankshaft position sensor to the engine harness.

Turn the keyswitch ON.

Connect INSITE™ electronic service tool.

Use INSITE™ electronic service tool monitor mode to read the crankshaft position sensor (engine speed) state.

Using the ratchet drive side of the socket tool that was used to remove the crankshaft position sensor from the engine, place it flush on the crankshaft position sensor so that the edge of the socket is on the edge of the crankshaft position sensor. Slowly slide the socket in a perpendicular direction to the marked line on the crankshaft position sensor or in a perpendicular direction to the mounting bracket of the crankshaft position sensor.

The crankshaft position sensor should transition from low to high, high to low, or the state will show triggered.

If the crankshaft position sensor state does **not** transition, check the supply and return circuits before replacing the crankshaft position sensor.

![[19d02998.png]]

### Install

Install a new o-ring onto the crankshaft position sensor.

Apply clean engine oil to the o-ring.

Install the crankshaft position sensor into the mounting hole.

Install and tighten the capscrew.

> [!tip] Момент затяжки · Torque Value
> 25 n•m [221 in-lb]

Connect the crankshaft position sensor to the engine harness.

Slide the lock tab sideways to lock the connector to the crankshaft position sensor.

![[19903765.png]]
