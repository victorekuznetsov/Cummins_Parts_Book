---
aliases:
  - "Привод перепускного клапана турбины"
type: "Процедура"
doc: "35-010-050-tr"
title_en: "Turbocharger Wastegate Actuator"
title_ru: "Привод перепускного клапана турбины"
modified: "2021-03-29"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "3666322"
figures: 18
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/35/35-010-050-tr.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/35-010-050-tr.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/35"
---

# Turbocharger Wastegate Actuator
**Привод перепускного клапана турбины**

> [!abstract] Процедура · `35-010-050-tr`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[3666322 — ISM, ISMe, and QSM11 Service Manual|3666322]]
> **Секции:** Section 10 - Air Intake System - Group 10
> **Даты:** изменён 2021-03-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/35/35-010-050-tr.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/35-010-050-tr.pdf)

### Initial Check

Some M Series engines are equipped with wastegate turbochargers to limit the peak boost level and increase engine response at low rpm.

The wastegate actuator hose transfers boost pressure from the intake manifold via the control valve to the wastegate capsule.

![[10200041.png]]

Inspect the wastegate actuator hose for cracks and holes.

Replace the hose if damaged.

![[10200042.png]]

> [!warning] CAUTION · Осторожно
> A bent wastegate mounting bracket, actuator rod, or lever can cause improper operation.

Inspect the wastegate mounting bracket, actuator rod, and lever for damage.

If the wastegate mounting bracket, actuator rod, or lever is bent, it **must** be replaced.

![[10900091.png]]

### Remove

In most applications, the turbocharger **must** be removed in order to remove the wastegate actuator. [[35-010-033-tr — Turbocharger|Refer to Procedure 010-033 in Section 10.]]

![[10200043.png]]

Remove the retaining clip from the control lever.

![[10900029.png]]

> [!danger] WARNING · Опасно
> Wear appropriate eye and face protection when using compressed air. Flying debris and dirt can cause personal injury.

> [!warning] CAUTION · Осторожно
> Be careful not to bend the control lever. A bent wastegate mounting bracket, actuator rod, or control lever can cause improper operation.

Disconnect the boost capsule actuator rod end from the turbocharger wastegate lever. This can be accomplished by slowly applying regulated air pressure to the boost capsule until the control rod is activated. A maximum of 310 kPa \[45 psi\] can be used.

![[10200044.png]]

> [!note] Note · Примечание
> If the boost capsule diaphragm material is ruptured and will **not** hold air pressure, it can be required to manually pull the control rod outward, in order to overcome boost capsule spring-tension for removal of the control rod from the turbocharger wastegate lever pin, while applying air pressure.

Disconnect the control rod from the turbocharger wastegate lever pin.

![[10200045.png]]

Loosen the boost capsule mounting capscrews, disconnect the wastegate actuator hose, and remove the assembly from the mounting bracket.

![[10900031.png]]

### Test

In most applications, the turbocharger **must** be removed in order to test the wastegate actuator. See the OFF engine test.

In some cases it may be possible to test the capsule while the turbocharger is installed on the engine. See the ON engine test.

![[10200044.png]]

Procedure for ON engine test:

A new hose clamp, Part Number 3914419, will be required to reinstall the signal line.

Disconnect the actuator hose form the wastegate actuator by cutting the crimped hose clamp.

![[10200042.png]]

No air will be heard (i.e., leaking noise) through a functional wastegate capsule.

Connect clean regulated air pressure and a pressure gauge to the actuator.

Apply a regulated air pressure to the wastegate actuator to measure travel.

ISM: 117 kPa \[17 psi\]

QSM (400HP and Above): 230 kPa \[33.4 psi\]

QSM (Below 400HP): 165 kPa \[24 psi\]

The actuator rod will extend 0.66 mm \[0.026 in\] to 0.91 mm \[0.036 in\] when the air pressure is applied.

If less than 0.66 mm \[0.026 in\], or no movement of the actuator rod and lever is detected, remove the turbocharger from the engine and perform the OFF engine test.

[[35-010-033-tr — Turbocharger|Refer to Procedure 010-033 in Section 10]] for turbocharger removal.

Procedure for OFF engine test.

Connect clean, regulated air pressure and a pressure gauge to the actuator.

Apply a regulated air pressure to the wastegate actuator to measure travel.

ISM: 117 kPa \[17 psi\]

QSM (400HP and Above): 230 kPa \[33.4 psi\]

QSM (Below 400HP): 165 kPa \[24 psi\]

The actuator rod will extend 0.66 mm \[0.026 in\] to 0.91 mm \[0.036 in\] when the air pressure is applied.

If less than 0.66 mm \[0.026 in\], or no movement of the actuator rod and lever is detected, remove the actuator rod from the pin.

Actuate the wastegate lever by hand.

If the lever moves, replace the actuator, if the lever does **not** move, replace the turbocharger.

![[10200044.png]]

### Install

If a new actuator is being installed, install the adjusting end-link onto the shaft of the pre-calibrated wastegate actuator assembly.

![[10200049.png]]

Fit the end-link over the turbocharger wastegate lever pin. With the spine of the spacer visible and the turbocharger wastegate lever pushed toward the rod, lay the actuator alongside the mounting bracket.

Do **not** install the two studs into the mounting holes at this time.

![[10200050.png]]

Adjust the length of the actuator assembly by rotating the end-link and re-fitting it until the underside of the actuator will just fit over the mounting bracket.

![[10200060.png]]

The setting is correct when the underside of the actuator will just fit over the mounting bracket, with less than a 0.5-mm \[0.20-in\] gap.

![[10200051.png]]

Install the actuator mounting studs into the holes in the bracket and install both actuator mounting capscrews.

Install the end-link onto the wastegate lever pin. Install the control rod retaining clip.

> [!tip] Момент затяжки · Torque Value
> 8.5 n•m [75 in-lb]

![[10200052.png]]

Snug the control rod jam nut against the end-link. Cut the tie wrap and remove and discard the tie wrap and spacer piece. Continue turning the jam nut in the same direction and tighten it against the end-link.

> [!tip] Момент затяжки · Torque Value
> 8.5 n•m [75 in-lb]

![[10200053.png]]

> [!note] Note · Примечание
> New hose clamps are **not** included in new actuator kits.

The hose clamp will need to be crimped for proper installation.

Fit the wastegate actuator hose to the actuator; use a new hose clamp, Part Number 3914419.

![[10200054.png]]
