---
aliases:
  - "Статическая установка угла опережения впрыска"
type: "Процедура"
doc: "10-006-025"
title_en: "Static Injection Timing"
title_ru: "Статическая установка угла опережения впрыска"
modified: "2011-11-02"
engines:
  - "80141463"
  - "80248213"
families:
  - "QSX15"
manuals:
  - "3666239"
figures: 34
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/10/10-006-025.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/10-006-025.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSX15"
  - "группа/10"
---

# Static Injection Timing
**Статическая установка угла опережения впрыска**

> [!abstract] Процедура · `10-006-025`
> **Двигатели:** [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSX15
> **Входит в руководства:** [[3666239 — Signature™, ISX, and QSX15 Service Manual|3666239]]
> **Секции:** Section 6 - Injectors and Fuel Lines - Group 06
> **Даты:** изменён 2011-11-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/10/10-006-025.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/10-006-025.pdf)

### General Information

The static timing measure is the amount of injection travel on the injector camshaft lobe remaining when the piston is 5.161 mm \[0.2032-in\], or 17.5 degrees before top dead center (TDC) on the compression stroke.

![[06a00126.png]]

The static timing code appears on the engine dataplate. Codes are listed in wedge degrees used to set the injector camshaft.

Specifications can be found in the Control Parts List (CPL) table. Use the following procedure for ISX, QSX Static Timing Values. Refer to Procedure 850-029 in Section V.

![[06a00127.png]]

Advanced timing (1) means the fuel is injected earlier into the cylinder during the compression stroke. Retarded timing (2) means the fuel injection occurs closer to TDC in the cylinder.

![[cg100wc.png]]

The amount of injector camshaft lobe travel determines the timing of fuel injection in relation to the piston position.

A **low** numerical value of the injector camshaft lobe travel remaining indicates a greater degree of advanced (1) or fast timing.

A **high** numerical value of the injector camshaft lobe travel remaining indicates a greater degree of retarded (2) or slow timing.

![[06a00128.png]]

> [!warning] CAUTION · Осторожно
> Advancing the injection timing beyond an engine's nominal timing value can cause engine and or aftertreatment damage.

Injection timing changes are accomplished by **advancing** or **retarding** the injector camshaft lobe action in relation to the piston position.

This is accomplished by changing the orientation of the camshaft lobe to the injector rocker lever using different wedges.

![[06a00129.png]]

### Setup

Injection timing is a measurement that determines the remaining injector camshaft lobe travel in relation to the piston travel. Injection timing tools, Part Number 3824942 and Part Number 2892426, are required.

![[06a00130.png]]

Remove the oil fill tube connector from the lower gear cover. Refer to Procedure 007-065 in Section 7.

Insert a 19 mm 3/4-inch drive ratchet and extension into the air compressor drive.

![[17c00091.png]]

Remove the rocker lever cover. Refer to Procedure 003-011 in Section 3.

![[03c00002.png]]

Remove the front injector and valve rocker lever assembly **only**. [[10-003-009-tr — Rocker Lever Assembly|Refer to Procedure 003-009 in Section 3.]]

![[03a00075.png]]

Remove the injector from cylinder number 3. [[10-006-026-tr — Injector|Refer to Procedure 006-026 in Section 6]]

> [!note] Note · Примечание
> If fuel or coolant have entered cylinder number 3, these fluids **must** be evacuated before proceeding.

![[06a00131.png]]

> [!note] Note · Примечание
> Injector timing tool, Part Number 3824982, can **not** be installed without removing the front valve and injector rocker levers. If **not** already completed, remove the front valve and injector rocker lever assembly. [[10-003-009-tr — Rocker Lever Assembly|Refer to Procedure 003-009 in Section 3.]]

Install the ISX injector bore adapter, Part Number 3163304, found within service tool kit, Part Number 2892426, into cylinder number 3 injector bore in the cylinder head.

![[06a00132.png]]

> [!note] Note · Примечание
> The portion of the service tool, Part Number 3824942, that measures push tube travel will **not** be used when measuring injection timing on an ISX or QSX engine.

Install **only** the piston travel portion of injector timing tool, Part Number 3824942, into cylinder number 3 with the capscrew provided in service tool, Part Number 2892426.

Orient the service tool so that the tool is in line with the crankshaft axis, and the portion of the tool that holds the push tube travel gage is extended over cylinder number 4.

> [!note] Note · Примечание
> Improper tightening of this capscrew will cause a measurement error. Use a 13 mm swivel to tighten the capscrew. After tighting the capscrew, check to make sure the piston plunger rod has free movement up and down. If the piston plunger rod does **not** move freely, the tool **must** be adjusted to obtain free travel.

Tighten the capscrew.

> [!tip] Момент затяжки · Torque Value
> 47 n•m [35 ft-lb]

![[06a00133.png]]

### Measure

Rotate the engine **clockwise**, as viewed from the front of the engine, until the B mark on the engine damper aligns with the mark on the lower gear housing cover, and the intake and exhaust valves are closed on cylinder number 4.

The rocker levers on cylinder number 4 **must** be loose. If they are **not**, rotate the engine 360 degrees and check the rocker levers again to make sure the intake and exhaust valves are closed on cylinder number 4. Both sets of valves are closed when the rocker levers are loose.

![[06a00134.png]]

Install the piston travel dial indicator (1) and adapter (2) onto the service tool installed in cylinder number 3.

The adapter **must** touch the tool with the indicator facing the operator. Tighten the thumb screw.

The dial indicator **must** also be fully seated into the adapter. Tighten the thumb screw.

![[06a00135.png]]

Use the following procedure to locate engine TDC on cylinder number 3.

Rotate the engine **clockwise** until the piston plunger rod reaches its full upper travel position.

Rotate the engine **counterclockwise** and **clockwise** while observing the dial indicator needle movement.

Rotate the engine **clockwise** until needle movement stops.

Zero the dial indicator by adjusting the outer ring and locking it into place. Repeat this step several times to be sure of TDC accuracy.

> [!note] Note · Примечание
> Always set the dial indicator to "0" (zero) at TDC, with the crankshaft having just been rotated in the direction of normal rotation **(clockwise)** to reduce any timing errors due to gear backlash.

![[06a00136.png]]

Rotate engine **counterclockwise** to 6.35 mm \[0.250 in\] before top dead center (BTDC). The large needle on the dial indicator will make 2-1/2 revolutions and will move in a **counterclockwise** motion.

![[06a00137.png]]

> [!note] Note · Примечание
> The piston **must** be positioned at 5.161 mm \[0.2032 in\] BTDC to avoid a timing measurement error.

Rotate engine **clockwise** until the dial indicator reads 5.161 mm \[0.2032 in\] BTDC. The indicator needle will move in a **clockwise** motion.

![[06a00138.png]]

> [!note] Note · Примечание
> This step **must** be performed to prevent an error in measurement.

Loosen cylinder number 4 injector adjusting screw locknut and retract the adjusting screw completely, so there is no load on the injector link. The injector lever **must** rock back and forth freely.

Tighten the injector adjusting screw until just to the point the injector lever will **not** rock any longer.

Tighten the adjusting screw one additional turn (360 degrees). Hand-tighten the locknut while making sure the adjusting screw does **not** turn.

Tighten the adjusting screw locknut.

> [!tip] Момент затяжки · Torque Value
> 47 n•m [35 ft-lb]

![[06a00139.png]]

Install injection travel indicator bracket, Part Number 2892427, onto the service tool installed in cylinder number 3. The bracket **must** extend over cylinder number 4.

Hand-tighten the bracket retainer.

![[06a00140.png]]

Assemble the indicator probe onto the injection travel dial indicator.

![[06a00141.png]]

Install the injection travel indicator and adapter onto the bracket, Part Number 2892427. The adapter **must** rest 9.5 mm \[0.375 in\] above the bracket.

Tighten the thumb screw.

The dial indicator **must** be facing toward the operator.

![[06a00142.png]]

> [!note] Note · Примечание
> Some injector upper spring retainers have a step where the measurement probe sits, so pay close attention that the probe does **not** slip during the injection measurement step. If the probe slips, timing errors will occur.

The measurement probe **must** be oriented so that it contacts the injector upper spring retainer as close to the crankshaft center line as possible. Take special care to make sure the probe does **not** contact the injector lever or crosshead. The probe **must** be positioned at the crankshaft centerline to avoid measurement errors.

![[06a00143.png]]

Hand-tighten the probe locknut with a 6.35 mm \[1/4 in\] wrench.

Zero the injection travel indicator by adjusting the outer ring and locking it into place. Make sure all thumb screws are tight and the indicator remains at zero (0).

Check that the piston travel indicator still reads 5.161 mm \[0.2032 in\] BTDC.

![[06a00144.png]]

> [!note] Note · Примечание
> Do **not** watch the piston travel dial indicator. At this point in the procedure, that indicator movement is no longer needed.

Rotate the engine **clockwise** while watching the large needle on the injection travel indicator on cylinder number 4, until the needle stops moving. Note the needle will move **counterclockwise**.

When the needle stops moving, record the reading of the injection travel indicator. Pay close attention to the number of revolutions the indicator travels. Each full revolution is 2.54 mm \[0.100 in\].

![[06a00145.png]]

> [!note] Note · Примечание
> The injection travel indicator is read in a **counterclockwise** direction from "0" (zero). The total amount of travel represents the injection timing value.

Compare the reading of the injection travel indicator to the specification listed for the engine's CPL found in the Critical Parts List (CPL) table. Use the following procedure for ISX, QSX static timing wedge values. Refer to Procedure 850-029 in Section V.

This table can also be found by typing in the engine serial number (ESN) into QuickService™ Online then selecting the Warranty Tab. Under the Warranty Tab select Engine Dataplate. On the engine dataplate screen click on the engine CPL number and it will take you to a Critical Parts List Screen. Select the link titled ISX QSX Static Timing Wedge. Find the engine CPL for the engine you are working on in the table. Record the nominal injection timing value for the correct CPL. Compare the nominal CPL value to the injection timing value you just measured on the engine. Proceed to the next step.

The engine CPL can be found on the engine dataplate located on the rocker lever cover.

![[cg1uaje.png]]

If the injection timing is **not** within the specified limits, check the following:

- Is the timing tool correctly installed?
- Are the dial indicators correctly adjusted?
- Has the crankshaft been rotated in the correct direction and timing sequence?

If these steps have been verified to be correct and the engine is out of time, proceed with the next step to determine whether the injection timing is retarded or advanced.

![[06a00146.png]]

If the indicator reading is higher than the nominal specification, the timing is retarded.

If the indicator reading is lower than the nominal specification, the timing is advanced.

![[nobox.png]]

> [!note] Note · Примечание
> The injection timing can be changed by using different wedges supplied in service tool, Part Number 2892426. Each 1/4-degree wedge will change timing by approximately 0.1016 mm \[0.004 in\].

- 4.25 Degree Wedge – Advance Timing by 0.1016 mm \[0.004 in\]
- 4.50 Degree Wedge – Advance Timing by 0.2032 mm \[0.008 in\]
- 4.75 Degree Wedge – Advance Timing by 0.3048 mm \[0.012 in\]

![[nobox.png]]

Select the appropriate wedge and perform the base engine timing procedure. [[10-001-088-tr — Engine Base Timing|Refer to Procedure 001-088 in Section 1.]] Use the crankshaft pin and selected wedge to change the injection timing to bring it into specification. Once the base engine timing has been completed, repeat this procedure and measure the injection timing again to make sure the injection timing is now within specification.

Update the engine dataplate to reflect the degree wedge used to obtain nominal engine timing.

![[nobox.png]]

Remove the injection timing tool and injector bore adapter.

![[06a00147.png]]

Use new o-rings and install cylinder number 3 injector. [[10-006-026-tr — Injector|Refer to Procedure 006-026 in Section 6.]]

![[06a00131.png]]

Install the valve crossheads.

Install the rocker lever assemblies. [[10-003-009-tr — Rocker Lever Assembly|Refer to Procedure 003-009 in Section 3.]]

![[03c00129.png]]

Adjust the valves and injectors. [[10-003-004-tr — Overhead Set|Refer to Procedure 003-004 in Section 3.]]

![[03c00088.png]]

Install the rocker lever cover. Refer to Procedure 003-011 in Section 3.

Remove the barring device and install the oil fill tube. Refer to Procedure 007-065 in Section 7.

![[03c00002.png]]
