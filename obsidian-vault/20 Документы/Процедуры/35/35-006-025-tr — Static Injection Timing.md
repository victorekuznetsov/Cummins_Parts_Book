---
aliases:
  - "Статическая установка угла опережения впрыска"
type: "Процедура"
doc: "35-006-025-tr"
title_en: "Static Injection Timing"
title_ru: "Статическая установка угла опережения впрыска"
modified: "2020-02-04"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "3666322"
figures: 22
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/35/35-006-025-tr.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/35-006-025-tr.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/35"
---

# Static Injection Timing
**Статическая установка угла опережения впрыска**

> [!abstract] Процедура · `35-006-025-tr`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[3666322 — ISM, ISMe, and QSM11 Service Manual|3666322]]
> **Секции:** Section 6 - Injectors and Fuel Lines - Group 06 · Section 6- Injectors and Fuel Lines - Group 06
> **Даты:** изменён 2020-02-04
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/35/35-006-025-tr.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/35-006-025-tr.pdf)

### Setup

- Remove the rocker lever cover. [[35-003-011-tr — Rocker Lever Cover|Refer to Procedure 003-011 in Section 3.]]
- Remove the injector from cylinder number one. Refer to Procedure 006-026 in Section 6.

> [!note] Note · Примечание
> It is **not** necessary to remove all injectors; however, engine rotation will be easier with all injectors removed.

![[fi200md.png]]

The timing tool, Part Number 3824942, can be installed without removing the rocker housing.

Install the piston plunger rod (1) in the injector bore of number one cylinder.

![[it200jr.png]]

Align the swivel bracket (2) with the injector hold-down capscrew hole.

Install capscrew, Part Number 3823600, through the swivel bracket. The capscrew is included with the timing tool kit.

![[it200js.png]]

> [!warning] CAUTION · Осторожно
> Do not tighten the capscrew too tightly. The capscrew can be damaged.

Tighten the capscrew (3) enough to hold the timing fixture rigidly.

![[it200jt.png]]

Position the timing tool push tube plunger bracket (4) on the backside of the center bracket (5).

![[it200ju.png]]

Use the alignment tool (6), Part Number 3824947, to align the push rod plunger rod (7).

Be sure to tighten the clamp handle (8) after the plunger rod is aligned, and remove the alignment tool.

![[it200jv.png]]

Install the injector push rod (9) between the injector camshaft follower and the plunger rod.

The push rod (9) **must** be vertically aligned with the plunger rod. If it is **not**, incorrect timing values will result. Be careful **not** to drop the push rod into the engine.

![[it200jw.png]]

### Measure

> [!warning] CAUTION · Осторожно
> Use the accessory driveshaft to rotate the crankshaft. If another method is used, the injection timing will not be correct, or the engine can be damaged.

Determine the piston top dead center (TDC) on the compression stroke by rotating the accessory driveshaft **clockwise**.

The piston is on the compression stroke when both plungers move in an upward direction at the same time. TDC is indicated by the maximum **clockwise** indicator position of the piston travel indicator pointer.

![[it200jx.png]]

> [!warning] CAUTION · Осторожно
> Both indicators must have a travel range of at least 6.35-mm \[0.250-in\], or the indicators will be damaged.

Position the gauge contact tip in the center of the plunger rod, and lower the gauge to within 0.63-mm \[0.025-in\] of the fully compressed position.

![[it200jy.png]]

Set the dial indicator over the piston plunger rod to zero "0" when the piston plunger rod has reached maximum upward movement at TDC.

![[it200jz.png]]

Rotate the accessory driveshaft back and forth, before and after the zero "0" indicator reading, for approximately 3 degrees, to be sure the piston is at TDC.

![[it200jd.png]]

Rotate the accessory driveshaft **clockwise** to 90-degrees after TDC.

The piston plunger will be at the "L10 90 degree" mark on the timing fixture.

![[it200je.png]]

Position the push rod dial indicator contact tip in the center of the plunger rod, and lower the gauge to within 0.63 mm \[0.025 in\] of the fully compressed position.

Set the push rod dial indicator to zero "0."

Rotate the accessory driveshaft **counterclockwise** to TDC.

![[it200jf.png]]

Continue to rotate the accessory driveshaft **counterclockwise** until the crankshaft is at 45-degrees before TDC. This step is necessary to remove gear backlash in the engine.

![[it200jg.png]]

Rotate the accessory driveshaft **clockwise**, slowly, until the piston travel gauge is at 5.160-mm \[0.2032-in\] before TDC.

If the crankshaft is rotated beyond the 5.160-mm \[0.2032- in\] before TDC position, the crankshaft **must** be rotated **counterclockwise**, back to the 45-degrees before TDC mark.

![[it200jh.png]]

Read the push rod travel gauge **counterclockwise** from zero "0." This travel represents the injection timing value. In the example shown, the value is 1.98-mm \[0.078-in\].

![[it200ji.png]]

To verify the correct injection timing for a particular engine, check the injector timing code on the engine dataplate. [[35-100-001-tr — Engine Identification|Refer to Procedure 100-001 in Section E for the engine dataplate location]]. Timing codes are listed as two alphabetical characters that relate to a numberical specification.

Specifications can be found in the Static Timing Codes chart in the Control Part List (CPL) Manual, Bulletin 4021327 or 4021328.

![[06a00163.png]]

If the indicator reading is lower than the specification, the timing is advanced.

If the indicator reading is higher than the specification, the timing is retarded.

The push rod **must** be vertically aligned with the plunger, or incorrect timing values will result. Repeat the procedure if in doubt.

![[it200jj.png]]

Injection timing can be changed by removing the camshaft gear and installing an offset key. [[35-001-012-tr — Camshaft Gear (Camshaft Installed)|Refer to Procedure 001-012 in Section 1.]]

![[it200jk.png]]

The accompanying table lists offset keys by part number and degree of offset.

**Never** advance injection timing beyond the specification limits. The engine's durability will be diminished.

![[lt200nb.png]]

If the arrow on the key is pointing toward the engine, the timing is retarded.

If the arrow is pointing away from the engine, the timing is advanced.

After installing a new timing key, **always** recheck the timing to be sure it is within the specifications.

![[cg2kegc.png]]

- Install the injector(s). [[35-006-026-tr — Injector|Refer to Procedure 006-026 in Section 6.]]
- Install the rocker lever cover. [[35-003-011-tr — Rocker Lever Cover|Refer to Procedure 003-011 in Section 3.]]

![[fi2bdhg.png]]
