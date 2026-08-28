---
aliases:
  - "Статическая установка угла опережения впрыска"
type: "Процедура"
doc: "18-006-025"
title_en: "Static Injection Timing"
title_ru: "Статическая установка угла опережения впрыска"
modified: "2012-06-27"
engines:
  - "37269910"
  - "37280605"
families:
  - "K19"
manuals:
  - "4021499"
figures: 21
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/18/18-006-025.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/18-006-025.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K19"
  - "группа/18"
---

# Static Injection Timing
**Статическая установка угла опережения впрыска**

> [!abstract] Процедура · `18-006-025`
> **Двигатели:** [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]]
> **Семейство:** K19
> **Входит в руководства:** [[4021499 — K19 Service Manual|4021499]]
> **Секции:** Section 6 - Injectors and Fuel Lines
> **Даты:** изменён 2012-06-27
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/18/18-006-025.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/18-006-025.pdf)

### General Information

The injection timing is the relative measurement of the distance remaining between the injector plunger and the injector cup when the piston is 5.16 mm \[0.2032 in\], or 19 degrees before top dead center on the compression stroke.

Injector timing is expressed by the amount of push rod travel remaining.

![[it800wa.png]]

The injector timing code appears on the engine dataplate. Codes are alphabetic letters that relate to a numerical specification.

Specifications can be found in the Control Part List (CPL) Manual, Bulletin 4021328.

![[it800wb.png]]

Below is a brief review of injection timing and how it can be adjusted.

Advanced timing means the fuel is injected earlier into the cylinder during the compression stroke.

Retarded timing means the fuel injection occurs closer to top dead center in the cylinder.

![[it400gb.png]]

The amount of push rod travel determines the time of fuel injection in relation to the piston position.

The higher the numerical value of the push rod travel remaining indicates a greater degree of retarded or slow timing.

The lower the numerical value of the push rod travel remaining indicates a greater degree of advanced or fast timing.

![[it400gc.png]]

Injection timing changes are accomplished by advancing or retarding the cam follower action in relation to the piston position.

This is accomplished by changing the orientation of the camshaft lobe to the cam follower using different camshaft gear keys.

Gear train timing (index mark alignment) always remain the same.

![[it400gd.png]]

The camshaft key provides a means of indexing the camshaft with the gear.

Offset keys allow the camshaft profile to be rotated slightly while the gear train timing remains the same.

The more the top of the offset is moved in the direction of the camshaft normal rotation, the more the injection timing will be retarded. The push rod travel numerical value will increase.

The direction of normal rotation on a K19 engine crankshaft is **clockwise** as viewed from the front.

![[04400023.png]]

Offset keys can be identified by measuring the offset and referring to the following chart.

Each 0.025 mm \[0.001 in\] of offset will cause a 0.0127 mm \[0.0005 in\] change in push rod travel from a straight key.

If checking or setting the injection timing, it is recommended to use a testing gear. A testing gear is a camshaft gear that has been modified to provide a slip-fit on the camshaft.

The camshaft key part number listed in the engine performance parts option is a starting point. Do **not** assume the listed key will provide the specified timing. **Always** measure the injection timing if the gear, camshaft, or key have been changed or if during disassembly the direction of any offset was **not** noted. Part of the reason for the existence of the offset key is to be able to adjust the static timing to all tolerances for the part used in the engine.

If a slip fit gear is used, the injection timing **must** be measured again after installation of the production gear.

| Timing Code | Recommended Code | Direction of Offset |
|---|---|---|
| AE | 216782 | Opposite camshaft rotation |
| AJ | 200706 | With camshaft rotation |
| AM | 216782 | With camshaft rotation |
| CI | 200711 | With camshaft rotation |
| CL | S-302 | None |
| CU | 3000492 | With camshaft rotation |

![[it4kega.png]]

### Measure

Use the injection timing tool, Part Number 3824942. The indicators (1) and (2) are identical.

- (1) Push rod travel indicator
- (2) Piston travel indicator
- (3) Piston plunger support assembly
- (4) Push rod plunger support
- (5) Hold-down adapter
- (6) Extension assembly (adapter wrench)
- (7) Indicator stem extension.

![[it8toga.png]]

The push rod plunger support assembly alignment is critical.

Install the push rod plunger support (4) in the outside slot in the piston support (3).

Align the push rod plunger support with the mark. Tighten the capscrew.

Install indicators (1) and (2) on the posts. Turn the indicators so they are **not** over the plungers.

Install the stem extension on the piston travel indicators.

![[it800sa.png]]

Install the injector push rod (8).

Install the timing tool in the injector bore. Install the hold-down adapter.

Align the push rod plunger and the rod to be sure they are straight.

Tighten the support lock (9).

![[it4toha.png]]

Use **only** the crankshaft to rotate the engine. The use of gears will result in false measurement. Gear lash **must** be closed up in the direction of normal rotation (crankshaft **clockwise**).

Three guide bolts equally spaced in front of the crankshaft will aid in engine rotation.

With the engine in the compression stroke, turn the crankshaft in the direction of normal rotation and observe both timing tool plungers.

Both plungers will begin moving upward when the cylinder is on the compression stroke. The indicators will be rotating in a **clockwise** direction.

If both indicators do **not** rotate in a **clockwise** direction, the engine is on the exhaust stroke. Rotate the crankshaft one revolution to get to the compression stroke.

![[04400025.png]]

Slowly rotate the crankshaft in the direction of normal rotation while observing the piston plunger (10). The plunger will move upward, stop, then begin to move downward. The stop point of the plunger is top dead center.

Rotate the engine opposite the direction of normal rotation until the plunger begins to move downward. The cylinder is now slightly before top dead center.

Turn the indicator so the stem is touching the plunger.

Carefully lower the indicator until it bottoms out. Raise the indicator when the needle has turned a minimum of three revolutions 7.62 mm \[0.300 in\]. Lock the indicator in position.

Slowly turn the crankshaft in the direction of normal rotation until the indicator needle stops turning **clockwise** (top dead center). Adjust the indicator to zero.

**Always** zero at top dead center with the crankshaft having just been rotated in the direction of normal rotation.

Slowly and carefully rotate the crankshaft backward and forward until the needle stops at zero before reversing the direction to indicate the piston is after top dead center.

![[it800sc.png]]

Turn the push rod indicator so the stem touches the plunger.

Carefully lower the indicator until it bottoms out. Raise the indicator when the needle has turned a minimum of three revolutions 7.62 mm \[0.300 in\].

![[it800sd.png]]

Slowly turn the crankshaft in the direction of normal rotation until the push rod indicator stops (1), momentarily reverses direction (2), (this is the crush nose on the camshaft), and stops again (3). The cam follower is now on the outer base circle of the camshaft. The piston is now approximately 90 degrees after top dead center.

It is important to record the amount of travel remaining in the push rod travel indicator for later reference.

Carefully lower the push rod travel indicator until it bottoms out. Raise the indicator approximately ¼ revolution 6.35 mm \[0.025 in\]. Lock the indicator in position.

Set the indicator at zero.

![[it800se.png]]

Observe the piston travel indicator as the crankshaft is slowly rotated opposite the direction of normal rotation.

Stop rotating the crankshaft when the piston travel indicator indicates the piston is at top dead center (zero).

![[it800sf.png]]

The crankshaft **must** be turned slowly to accurately count the indicator revolutions.

Turn the crankshaft opposite the direction of normal rotation until the indicator needle moves 2½ revolutions, 6.35 mm \[0.250 in\].

The piston is now 6.35 mm \[0.250 in\] before top dead center.

![[it800sg.png]]

**Only** move the piston to 5.16 mm \[0.2032 in\] before top dead center by turning the crankshaft in the direction of normal rotation. If the crankshaft is turned too far, turn the crankshaft back opposite the direction of normal rotation more than 5.16 mm \[0.2032 in\] before top dead center. Then very slowly turn the crankshaft in the direction of normal rotation until the indicator indicates the piston is 5.16 mm \[0.2032 in\] before top dead center.

All K19 injection timing specifications are more than one indicator revolution 2.54 mm \[0.100 in\].

Read the push rod indicator **counterclockwise** from zero. This is the injection timing measurement. An example of 0.118 in is illustrated in the graphic.

If unsure of the number of push rod indicator revolutions, check by carefully lifting the indicator stem until the indicator has bottomed out. Lower the stem the amount of excess travel. Lower the stem to the plunger. Read the indicator.

If the injection timing is within specification and a slip fit gear is used, install the standard camshaft gear. Refer to Procedure 001-012 in Section 1. Repeat the injection timing procedure after the gear has cooled.

If the injection timing is still **not** within specification, repeat the measurement procedure to check the tool set up and zero settings.

If the timing is still **not** within specification, the camshaft key **must** be changed. Remove the camshaft gear. Refer to Procedure 001-012 in Section 1.

Record the orientation of the offset of the key. Use the following worksheet to determine the alternate key.

The timing measurement **must** be confirmed after changing the key.

![[it800sh.png]]

![[06400106.png]]

NEEDS TEXT FOR CORRECT STRUCTURE

![[06400105.png]]

NEEDS TEXT FOR CORRECT STRUCTURE

![[06400108.png]]

NEEDS TEXT FOR CORRECT STRUCTURE

![[06400107.png]]

NEEDS TEXT FOR CORRECT STRUCTURE
