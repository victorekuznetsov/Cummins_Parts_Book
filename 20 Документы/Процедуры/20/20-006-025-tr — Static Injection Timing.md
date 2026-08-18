---
aliases:
  - "Статическая установка угла опережения впрыска"
type: "Процедура"
doc: "20-006-025-tr"
title_en: "Static Injection Timing"
title_ru: "Статическая установка угла опережения впрыска"
modified: "2018-11-13"
engines:
  - "41349633"
families:
  - "QSK19"
manuals:
  - "4021592"
figures: 25
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/20/20-006-025-tr.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/20-006-025-tr.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/20"
---

# Static Injection Timing
**Статическая установка угла опережения впрыска**

> [!abstract] Процедура · `20-006-025-tr`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021592 — QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual|4021592]]
> **Секции:** Section 6 - Injectors and Fuel Lines · Section 6 - Injectors and Fuel Lines - Group 06
> **Даты:** изменён 2018-11-13
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/20/20-006-025-tr.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/20-006-025-tr.pdf)

### General Information

with Mechanically Actuated Injector

The injection timing is the relative measurement of the distance remaining between the injector plunger and the injector cup when the piston is 5.16 mm \[0.2032 inch\], or 19 degrees before TDC on the compression stroke.

Injector timing is expressed by the amount of push tube travel remaining.

![[cg100wa.png]]

The injection timing code appears on the engine dataplate. Codes are alphabetic letters that relate to a numerical specification.

Specifications can be found in the Control Part List (CPL) Manual, Bulletin 4021328.

![[cg100wh.png]]

The next six frames are a brief review of injection timing and how it can be adjusted.

Advanced timing (1) means the fuel is injected earlier into the cylinder during the compression stroke.

Retarded timing (2) means the fuel injection occurs closer to top dead center (TDC) in the cylinder.

![[cg100wc.png]]

The amount of push rod travel determines the time of fuel injection in relation to the piston position.

A low numerical value of the push rod travel remaining indicates a greater degree of advanced (1) or fast timing.

A high numerical value of push rod travel remaining indicates a greater degree of retarded (2) or slow timing.

![[it400gc.png]]

Injection timing changes are accomplished by advancing or retarding the cam follower action in relation to the piston position.

This is accomplished by changing the orientation of the camshaft lobe to the cam follower using different camshaft gear keys.

> [!note] Note · Примечание
> Gear train timing (index mark alignment) always remains the same.

![[cg100we.png]]

The camshaft key provides a means of indexing the camshaft with the gear.

Offset keys allow the camshaft profile to be rotated slightly while the gear train timing remains the same.

The more the top of the offset is moved in the direction of the camshaft normal rotation, the more the injection timing will be retarded. The push rod travel numerical value will increase.

> [!note] Note · Примечание
> The direction of normal rotation on a QSK19 engine crankshaft is **clockwise** as viewed from the front.

![[00400010.png]]

Offset keys can be identified by measuring the offset and referring to the chart at the end of this section.

> [!note] Note · Примечание
> Each 0.025 mm \[0.001 inch\] of offset will cause a 0.0127 mm \[0.0005 inch\] change in the push rod travel from a straight key.

![[it4kega.png]]

If checking or setting the injection timing, it is recommended to use a testing gear. A testing gear is a camshaft gear that has been modified to provide a slip-fit on the camshaft.

![[01400035.png]]

### Preparatory Steps

Prepare the engine to adjust the static timing.

- Remove the rocker lever cover. [[20-003-011-tr — Rocker Lever Cover|Refer to Procedure 003-011 in Section 3.]]
- Remove the rocker lever assembly from cylinder Number 3. [[20-003-009-tr — Rocker Lever Assembly|Refer to Procedure 003-009 in Section 3.]]
- Remove the injector from cylinder Number 3. [[20-006-026-tr — Injector|Refer to Procedure 006-026 in Section 6.]]

NOTE: It is **not** necessary to remove all injectors; however, engine rotation will be easier with all injectors removed.

![[ck800wa.png]]

### Setup

Use the injection timing tool, Part Number 3824942. The indicators (1) and (2) are identical.

1. Push tube travel indicator
2. Piston travel indicator
3. Piston plunger support assembly
4. Push rod plunger support assembly
5. Hold-down adapter
6. Extension assembly (adapter wrench)
7. Indicator stem extension

![[it8toga.png]]

The push rod plunger support assembly alignment is critical.

Install the push rod plunger support (4) in the outside slot in the piston plunger support (3).

Align the push rod plunger support with the mark. Tighten the capscrew.

Install the indicators (1) and (2) on the posts. Turn the indicators so they are **not** over the plungers.

Install the stem extension on the piston travel indicator.

![[it800sa.png]]

Install the injector push rod (8) for cylinder Number 3.

Install the timing tool in the injector bore Number 3. Install the hold-down adapters.

Align the push rod plunger and the rod to be sure they are straight.

Tighten the support lock (9).

![[it4toha.png]]

### Measure

Use **only** the crankshaft to rotate the engine. The use of the gears will result in false measurement. Gear lash **must** be closed up in the direction of normal rotation.

> [!note] Note · Примечание
> Three guide bolts equally spaced in front of the crankshaft will help rotate the engine.

Turn the crankshaft in the direction of normal rotation while observing both of the timing tool plungers. Both plungers will begin moving upward when the cylinder is on the compression stroke.

Assuming all the gear index marks were aligned when the injection timing process was started, the crankshaft will have to be rotated approximately three-quarters of a revolution to get to the compression stroke for the Number 3 cylinder.

If both plungers are **not** moving upward (one upward and one downward), the engine is on the exhaust stroke. Rotate the crankshaft one revolution to get to the compression stroke.

![[00400009.png]]

Establish TDC by slowly rotating the crankshaft in the direction of normal rotation while observing the piston plunger (10). The plunger will move upward, STOP, then begin to move downward. The STOP point of the plunger is TDC. Rotate the engine opposite the direction of normal rotation until the plunger begins to move downward. The cylinder is now before TDC slightly.

![[it800sc.png]]

Turn the indicator so the stem is touching the plunger. Carefully move the indicator downward until the needle has turned a minimum of five revolutions \[0.500 inch\]. LOCK the indicator in position.

Slowly turn the crankshaft in the direction of normal rotation until the indicator needle STOPS turning **clockwise** (TDC). Move the indicator downward until there is **only** one revolution \[0.100 inch\] of travel remaining until the indicator bottoms out.

Adjust the indicator to ZERO.

![[it800sc.png]]

Turn the push rod indicator so that the stem touches the plunger.

Carefully lower the indicator until it bottoms out. Raise the indicator when the needle has turned a minimum of three revolutions \[0.300 inch\].

![[it800sd.png]]

Slowly turn the crankshaft in the direction of normal rotation until the push rod indicator STOPS (1), momentarily reverses direction (2) (this is the crush nose on the camshaft), and STOPS again (3). The cam follower is now on the outer base circle of the camshaft. The piston is now approximately 45 degrees after TDC.

It is important to record the amount of travel remaining in the push rod travel indicator for later reference.

Carefully lower the push rod travel indicator until it bottoms out. Raise the indicator approximately one-half of a revolution \[0.050 inch\]. LOCK the indicator in position.

Set the indicator at ZERO.

![[it800se.png]]

Set the piston at \[0.2032 inch\] before TDC

Observe the piston travel indicator as you slowly rotate the crankshaft opposite the direction of normal rotation.

Stop rotating the crankshaft when the piston travel indicator indicates the piston is at TDC (ZERO).

![[it800sf.png]]

The crankshaft **must** be turned slowly to accurately count the indicator revolutions.

Turn the crankshaft opposite the direction of normal rotation until the indicator needle moves two and one-half revolutions \[0.250 inch\].

The piston is now \[0.250 inch\] before TDC.

![[it800sg.png]]

**Only** move the piston to \[0.2032 inch\] before TDC by turning the crankshaft in the direction of normal rotation. If you accidently turn the crankshaft too far, you **must** turn the crankshaft opposite the direction of normal rotation more than \[0.2032 inch\] before TDC. Then very slowly turn the crankshaft in the direction of normal rotation until the indicator indicates that the piston is \[0.2032 inch\] before TDC.

> [!note] Note · Примечание
> Remember that all QSK19 injection timing specifications are more than one indicator revolution \[0.100 inch\].

Read the push rod travel indicator **counterclockwise** from zero. This is the injection timing measurement to compare to the specification. An example of \[0.118 inch\] is shown.

![[it800sh.png]]

If **not** sure of the number of push rod indicator revolutions, check by:

- Carefully lifting the indicator stem until the indicator has bottomed out
- Lower the stem the amount of excess travel you set in the third preceding step
- Lower the stem to the plunger.
- Read the indicator.

If the injection timing is within specification and you are using a slipper-fit gear, install the standard gear. [[20-001-012-tr — Camshaft Gear (Camshaft Installed)|Refer to Procedure 001-012 in Section]]. Repeat the injection timing procedure after the camshaft gear has cooled.

![[dp8gewa.png]]

If the injection timing is **not** within specification, repeat the measurement procedure to check the tool setup and the ZERO settings.

If the timing is still **not** within specification, the camshaft key **must** be changed. [[20-001-012-tr — Camshaft Gear (Camshaft Installed)|Refer to Procedure 001-012 in Section]] for instructions to remove the camshaft gear.

Record the orientation of any offset of the key. Use the following worksheet to determine an alternate key.

You **must** confirm the timing measurement after changing the key.

![[06400081.png]]

![[06400106.png]]

![[06400105.png]]

### Finishing Steps

with Mechanically Actuated Injector

- Install the injector from cylinder Number 3. [[20-006-026-tr — Injector|Refer to Procedure 006-026 in Section 6.]]
- Install the rocker lever assembly from cylinder Number 3. [[20-003-009-tr — Rocker Lever Assembly|Refer to Procedure 003-009 in Section 3.]]
- Install the rocker lever cover. [[20-003-011-tr — Rocker Lever Cover|Refer to Procedure 003-011 in Section 3.]]
- Operate the engine and check for leaks.

![[ck800wa.png]]
