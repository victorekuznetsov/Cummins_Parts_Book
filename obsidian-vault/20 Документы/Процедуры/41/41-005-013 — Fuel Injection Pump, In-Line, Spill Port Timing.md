---
aliases:
  - "Рядный ТНВД: установка по моменту перекрытия отсечного окна"
type: "Процедура"
doc: "41-005-013"
title_en: "Fuel Injection Pump, In-Line, Spill Port Timing"
title_ru: "Рядный ТНВД: установка по моменту перекрытия отсечного окна"
modified: "2003-05-13"
engines:
  - "93058669"
  - "93087701"
families:
  - "C8.3 · 6C8.3"
manuals:
  - "3666003"
figures: 27
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/41/41-005-013.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/41-005-013.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "группа/41"
---

# Fuel Injection Pump, In-Line, Spill Port Timing
**Рядный ТНВД: установка по моменту перекрытия отсечного окна**

> [!abstract] Процедура · `41-005-013`
> **Двигатели:** [[93058669 — 6C8.3 CPL 3105|93058669]], [[93087701 — 6C8.3 CPL 3105|93087701]]
> **Семейство:** C8.3 · 6C8.3
> **Входит в руководства:** [[3666003 — C Troubleshooting and Repair Manual|3666003]]
> **Секции:** Section 5 - Fuel System - Group 05
> **Даты:** изменён 2003-05-13
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/41/41-005-013.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/41-005-013.pdf)

### Adjust

Use Cylinder No. 1 intake valve to make sure the engine is at top dead center on the compression stroke for Cylinder No. 1. Refer to Procedure [[41-001-049 — Timing Pin Housing|001-049]].

![[er900wl.png]]

Fabricate a timing mark pointer for the front of the engine.

> [!note] Note · Примечание
> This can be done by forming a piece of wire that can be tightened under one of the gear cover capscrews. Sharpen the wire at the vibration damper end so that it comes to a point for better accuracy.

![[er900wr.png]]

Attach a degree wheel or degree tape to the front of the vibration damper. Line the top dead center mark up with the pointer.

The degree wheel/tape **must** measure to an accuracy of at least ±1 degree.

![[er900wn.png]]

Install the fuel injection pump; refer to [[41-005-012 — Fuel Injection Pumps, In-Line|Procedure 005-012]].

If the fuel injection pump is already installed, continue the procedures.

![[fp900nb.png]]

Remove the No. 1 high-pressure fuel line from the fuel injection pump.

> [!note] Note · Примечание
> Lines 2 through 6 **must not** be removed or loosened.

![[ft900mg.png]]

> [!warning] CAUTION · Осторожно
> When attaching the fabricated tube, do not bend the No. 1 high-pressure fuel line. This can cause the inside of the fuel line to flake and cause injector failure.

A short length of high-pressure line that is compatible with the fuel lines used on the engine **must** be bent in a “U” shape and installed onto the delivery valve holder of the fuel injection pump.

> [!note] Note · Примечание
> The line is used to observe when the fuel is or is **not** flowing through the delivery valve holder assembly.

Place a container under the tube to catch the fuel or drain the fuel back into the spill port pump.

![[ft900wl.png]]

Remove the overflow valve from the fuel injection pump.

Install a 14-mm threaded plug and sealing washer into the fuel return port of the fuel injection pump.

> [!note] Note · Примечание
> The fuel return port is located on the inboard front side of the fuel injection pump for automotive in-line applications and on the outboard front side for most industrial applications.

![[ft900wm.png]]

Remove the fuel supply line between the fuel filter head and the fuel injection pump.

> [!note] Note · Примечание
> Attach the high-pressure outlet hose from the spill port to the fuel injection pump supply port.

![[ft900mf.png]]

Before continuing, make sure the fuel injection pump timing pin is **disengaged**.

![[fs9piha.png]]

Rotate the crankshaft **counterclockwise**, as viewed from the front of the engine, to approximately 40 degrees before top dead center.

![[er900wo.png]]

**Governor Lever Positioning**

> [!note] Note · Примечание
> The governor lever **must** be positioned before pressurizing the fuel injection pump.

The RQV governor throttle lever **must** be in the **low-idle** lever position.

Automotive engines with an RQV-K governor throttle lever **must** be in the **high-idle** throttle position.

Industrial engines with an RQV-K governor throttle lever **must** be in the low-idle throttle position.

![[fp900wo.png]]

Both the RQV and RQV-K governor **must** have the shutdown lever in the **full-run** position.

![[fp900wp.png]]

The RSV governor throttle lever **must** be in the low-idle position and the shutdown lever needs to be wired or locked in the ½-travel position.

![[fp900wq.png]]

Turn on the spill timing cart pump.

Check the fuel pressure.

| kpa |  | psi |
|---|---|---|
| 2068 | MIN | 300 |
| 2551 | MAX | 370 |

> [!note] Note · Примечание
> The shutdown lever **must** be held in the required position before turning the spill cart pump on.

![[ip900ob.png]]

Fuel **must** be flowing out of the tube attached to the fuel injection pump. If the fuel is **not** flowing, recheck the procedures carefully.

![[ip900wh.png]]

Slowly rotate the crankshaft **clockwise**, as viewed from the front of the engine, until fuel flow from cylinder No. 1 begins.

The plunger No. 1 element is now approaching port closure. Continue to rotate the crankshaft slowly until the flow is reduced to a drip. At the point that the steady stream of flow changes from a solid flow to a drip, **stop**. This is the static timing position of the fuel injection pump.

![[ip900wf.png]]

If the flow does **not** slow down to a drip:

1. Check the position of the governor levers.
2. Make sure cylinder No. 1 is before top dead center on the compression stroke.
3. Turn off the spill port pump.

![[fp900wq.png]]

Check the degree wheel on the vibration damper to see what engine degree the timing pointer is indicating. This is spill port static timing. Compare this number to the timing specification for your particular application.

![[er900wp.png]]

If the fuel injection pump static timing, as measured by the above method, is **not** within specification, remove the large nut that fastens the fuel injection pump camshaft to the fuel pump drive gear.

If the crankshaft has rotated, turn on the spill port pump and rotate the crankshaft to find port closure.

Turn off the spill port pump.

![[ip900wj.png]]

Using the fuel pump gear puller, Part No. 3824469, pull the fuel injection pump drive gear from the fuel injection pump camshaft taper.

![[fs9gemc.png]]

Slowly rotate the crankshaft **counterclockwise** about 40 degrees past the desired static timing specification.

Slowly rotate the crankshaft **clockwise** until the timing pointer indicates the desired static timing.

![[er900wq.png]]

Install and tighten the retaining nut and washer.

> [!tip] Момент затяжки · Torque Value
> 12 n•m [106 in-lb]

> [!note] Note · Примечание
> To prevent damage to the timing pins, do **not** exceed the torque value given. This is **not** the final torque value for the retaining nut.

![[fp9nuhc.png]]

> [!danger] WARNING · Опасно
> Wear appropriate eye and face protection when using compressed air. Flying debris and dirt can cause bodily injury.

Tighten the fuel injection pump drive nut.

Make sure the static timing has **not** changed after the fuel injection drive nut is tightened to the required specification.

> [!note] Note · Примечание
> Before installing the fuel pump drive gear, clean the injection pump shaft and gear tapers with residue-free cleaner, Part No. 3824510, by spraying into the gap between the shaft and the gear. Dry the surface with compressed air.

![[ip9nuhd.png]]

> [!warning] CAUTION · Осторожно
> Failure to clean and dry the shaft and gear tapers thoroughly can result in timing shift to the retarded side after the engine is started and running under a load. This will result in low power, smoke, rough running, and engine damage.

Tighten the fuel injection pump drive gear nut.

| Nippondenso | 123 n.m | \[92 ft-lb\] |
|---|---|---|

| Bosch A pump | 85 n.m | \[63 ft-lb\] |
|---|---|---|

| Bosch MW pump | 105 n.m | \[77 ft-lb\] |
|---|---|---|

| Bosch P3000/P7100 | 195 n.m | \[144 ft-lb\] |
|---|---|---|

![[nobox.png]]

Repeat this procedure as needed until the timing matches the specification.

![[ip900wf.png]]

The fuel injection pump timing pin **must** fit over the injecting pump pointer when the engine is at top dead center or on the compression stroke for the cylinder No. 1. If it does **not**, the fuel injection pump **must** be adjusted by an authorized fuel injection pump shop or the fuel injection pump was installed incorrectly.

![[ip9gewb.png]]

Remove the degree wheel and timing mark pointer.

![[er900wr.png]]
