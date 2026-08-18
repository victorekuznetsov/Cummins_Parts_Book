---
aliases:
  - "Датчик частоты вращения двигателя (ESS)"
type: "Процедура"
doc: "01-019-042"
title_en: "Engine Speed Sensor (ESS)"
title_ru: "Датчик частоты вращения двигателя (ESS)"
modified: "2002-12-05"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 11
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-019-042.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-019-042.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Engine Speed Sensor (ESS)
**Датчик частоты вращения двигателя (ESS)**

> [!abstract] Процедура · `01-019-042`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2002-12-05
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-019-042.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-019-042.pdf)

### Remove

Disconnect the engine speed sensor connectors from the engine harness.

![[19a00245.png]]

Loosen the locknut.

Remove the engine speed sensor from the flywheel housing.

![[19a00246.png]]

### Inspect for Reuse

Inspect the engine speed sensor for debris, cracked, or chipped potting, extruded potting, and damage from contact with the flywheel.

If there is debris on the engine speed sensor, clean the sensor.

If the sensor is chipped, cracked, extruded, or damaged, replace the sensor with a new one.

![[19800369.png]]

### Install

Make sure a gear tooth is aligned with the hole in the flywheel housing.

Install the engine speed sensor into the hole until it touches the gear tooth.

> [!note] Note · Примечание
> If the engine speed sensor does **not** turn in with finger pressure, check the flywheel housing hold threads and sensor threads for damage.

Turn the ESS out 1/2 to 3/4 of a turn **counterclockwise**.

![[19a00246.png]]

Tighten the locknut against the flywheel housing.

> [!tip] Момент затяжки · Torque Value
> 34 to 47 n•m [25 to 35 ft-lb]

> [!note] Note · Примечание
> Overtightening the locknut can damage the sensor.

![[19a00246.png]]

Connect the sensor to the sensor harness. Push the connectors together until they lock.

![[19a00245.png]]

### Resistance Check

Separate the four-way connector. Lift the tab and pull the connector apart. Install a mating connector with short test leads on the sensor connector.

> [!note] Note · Примечание
> The purpose of installing a mating connector is to allow the electrical leads of the sensor to be softly flexed to check for damaged or partially broken wire strands under the insulation.

![[19a00245.png]]

Measure the resistance from pin A to pin B for each coil. The multimeter **must** measure between 700 and 2000 ohms. If both resistance values are within the specifications, the sensor **must** still be checked for short circuit to ground.

If any of the preceding checks fail, replace the engine speed sensor.

![[19a00269.png]]

### Check for Short Circuit to Ground

Measure the resistance from pin A to the engine block. The multimeter **must** show an open circuit (10M ohms or more).

> [!note] Note · Примечание
> The open circuit specification (10M ohms) for the engine speed sensor is higher than the open circuit specification used throughout the manual due to the sensitivity of the engine position sensor.

![[19a00270.png]]

Measure the resistance from pin B to the engine block. The multimeter **must** show an open circuit (10M ohms or more).

If either of the preceding tests fail, replace the engine speed sensor.

![[19a00271.png]]

### Check for Short Circuit from Pin to Pin

Measure the resistance from engine speed sensor 1 signal (pin A) to engine speed sensor 2 signal (pin A) and engine speed sensor 2 signal (pin B).

The resistance must show an open circuit (10M ohms or more).

Measure from engine speed sensor 1 return (pin B) to engine speed sensor 2 signal (pin A) and engine speed sensor 2 signal (pin B).

If any of the previous resistance checks are not within specifications, the sensor has failed. Replace the sensor.

> [!missing]- Иллюстрация `19a00272.png` не извлечена — смотрите PDF-оригинал документа
