---
aliases:
  - "Привод перепускного клапана турбины"
type: "Процедура"
doc: "40-010-050"
title_en: "Turbocharger Wastegate Actuator"
title_ru: "Привод перепускного клапана турбины"
modified: "2006-03-31"
engines:
  - "93047320"
families:
  - "6B5.9"
manuals:
  - "3666087"
figures: 20
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/40/40-010-050.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/40-010-050.pdf"
tags:
  - "документ/процедура"
  - "двигатель/6B5.9"
  - "группа/40"
---

# Turbocharger Wastegate Actuator
**Привод перепускного клапана турбины**

> [!abstract] Процедура · `40-010-050`
> **Двигатели:** [[93047320 — 6B5.9 CPL 3111|93047320]]
> **Семейство:** 6B5.9
> **Входит в руководства:** [[3666087 — B3.9, B4.5, B4.5 RGT, and B5.9 Service Manual|3666087]]
> **Секции:** Section 10 - Air Intake System - Group 10
> **Даты:** изменён 2006-03-31
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/40/40-010-050.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/40-010-050.pdf)

### Initial Check

> [!note] Note · Примечание
> This procedure applies to actuators that are adjustable before pre-1998 B Series engines. B Series engines after January 1998 are **not** adjustable and the actuators are tamper proof.

Some versions of B Series engines are equipped with wastegated turbochargers to limit the peak boost level and increase engine response at low rpm.

The integral wastegate line takes boost from the turbocharger compressor outlet to the wastegate capsule.

![[10900089.png]]

Inspect the integral wastegate actuator hose for cracks or holes.

Replace the hose if damaged.

![[10900090.png]]

> [!warning] CAUTION · Осторожно
> A bent wastegate mounting bracket, actuator rod, or lever can cause improper operation.

Inspect the wastegate mounting bracket, actuator rod, and lever for damage.

If the wastegate mounting bracket, actuator rod, or lever is bent, it **must** be replaced.

![[10900091.png]]

### Preparatory Steps

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

- Disconnect the batteries.

![[13900050.png]]

### Remove

> [!note] Note · Примечание
> Prior to removal, note position length of the control rod from the boost capsule housing and orientation of the boost capsule hose connector in relation to the mounting bracket.

![[tb900wg.png]]

Turbocharger Wastegate Pressure Setting Kit, Part Number 3823799

Remove the retaining clip from the control lever.

![[tb9lvmb.png]]

> [!warning] CAUTION · Осторожно
> Be careful not to bend the control lever.

Disconnect the boost capsule actuator rod end from the turbocharger wastegate lever. This can be accomplished by applying regulated air pressure to the boost capsule in a sufficient amount to activate control rod movement.

Disconnect the control rod from the turbocharger wastegate lever pin.

> [!note] Note · Примечание
> If the boost capsule diaphragm material is ruptured and will **not** hold air pressure other than by hand, manually pull the control rod outward in order to overcome boost capsule spring tension for removal of the control rod from the turbocharger wastegate lever pin.

![[tb9lvma.png]]

Loosen the boost capsule mounting capscrews, disconnect the air supply hose, and remove assembly from the mounting bracket.

![[tb9homb.png]]

Note length of adjusting link prior to removal.

Loosen nut, and remove the adjusting link end from the boost capsule actuator.

![[tb900mc.png]]

### Inspect for Reuse

Inspect the wastegate actuator hose for cracks or holes. Replace the hose if damaged.

![[tb9hosb.png]]

Inspect the wastegate mounting bracket, actuator rod, and lever for damage. A bent wastegate mounting bracket, actuator rod, or lever can cause improper operation.

If the wastegate mounting bracket, actuator rod, or lever is bent, it **must** be replaced.

![[tb9lvsa.png]]

### Test

Functional Check

Attach a dial indicator as shown, so that its shaft is in line with the wastegate actuator rod. Set the indicator to zero, with no air pressure applied to the wastegate capsule.

Connect clean, regulated air pressure and a pressure gauge to the capsule. Apply air pressure to make sure the wastegate is functioning properly.

| Measurements |  |  |
|---|---|---|
|  | kpa | psi |
| Air Pressure: | 200 | 29 |

The rod should move **without** any sticking or air leakage.

| Measurements |  |  |
|---|---|---|
|  | mm | in |
| Rod: | 0.33 to 1.27 | 0.013 to 0.050 |

> [!note] Note · Примечание
> No air should be heard leaking through a functional wastegate capsule.

> [!note] Note · Примечание
> A small amount of travel when air pressure is first applied is normal; the tolerance is being removed from the system.

![[tb900nb.png]]

Replace the actuator if no movement of the actuator rod and lever is detected.

![[tb900kf.png]]

### Install

Install the adjusting link end onto the boost capsule actuator assembly. Adjust the rod to approximately the same length as when removed.

![[tb9lvha.png]]

Fit the new boost capsule actuator assembly to the actuator mounting bracket, and install the mounting capscrews.

> [!tip] Момент затяжки · Torque Value
> 4.5 n•m [40 in-lb]

![[tb9bkha.png]]

### Calibrate

> [!note] Note · Примечание
> The wastegate is set accurately from the factory. Adjustment is **not** necessary unless the capsule is removed.

Connect clean, regulated air pressure to the boost capsule.

| Engine Serial Number | Rating (HP) | Pressure (kPa) | Pressure (psi) |
|---|---|---|---|
| Before 45278518 | 195 | 83 | 12 |
| After and Including 45278518 | 195 | 83 | 12 |
| All | 150 | 48 | 7 |

![[tb900nb.png]]

> [!note] Note · Примечание
> Wastegate actuator adjustment is **not** a shortcut to diagnosing low boost. Use the appropriate symptom tree to diagnose the cause of the low boost before calibrating the wastegate actuator, if turbo boost is suspected.

This actuator travel specification applies to the 4B and 6B engine applications.

> [!note] Note · Примечание
> If the measured wastegate actuator travel is within specification, do **not** make any adjustment.

| mm |  | in |
|---|---|---|
| 0.033 | MIN | 0.013 |
| 1.27 | MAX | 0.050 |

> [!note] Note · Примечание
> Adjustment on wastegate actuators is **not** possible for engines that were built after January 1998 because tamper proof actuator links are used. The first engine serial number is 4536369. If the actuator needs to be replaced, the whole capsule has to be changed. You can **not** adjust the wastegate actuator.

![[tb900nb.png]]

> [!warning] CAUTION · Осторожно
> Do not pull, or push, or force alignment of the clevis pin. Failure to do so can cause component damage.

Adjust the wastegate, if necessary, to achieve specified travel.

- Pull the wastegate lever to the foremost closed position (lever toward boost capsule).
- Adjust the length of the clevis end of the control rod to where the clevis pin hole aligns to the wastegate lever.
- Install the adjusting link and retaining clip.
- After adjustment is completed, tighten actuator rod jam nuts.

![[tb9lvua.png]]

Disconnect regulated air pressure line from the boost capsule.

Connect the turbocharger boost line to the boost capsule, and secure the hose clamp.

If possible, a more accurate method of wastegate adjustment is to check the manifold pressure at rated rpm according to turbocharger boost pressure specifications.

![[tb900md.png]]

### Finishing Steps

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

- Connect the batteries
- Operate the engine and check for leaks.

![[13900050.png]]
