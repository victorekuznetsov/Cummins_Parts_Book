---
aliases:
  - "Диагностика топливной системы"
type: "Процедура"
doc: "28-005-236"
title_en: "Fuel System Diagnostics"
title_ru: "Диагностика топливной системы"
modified: "2026-03-02"
engines:
  - "33239746"
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
manuals:
  - "4021528"
figures: 27
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/28/28-005-236.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/28-005-236.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/28"
---

# Fuel System Diagnostics
**Диагностика топливной системы**

> [!abstract] Процедура · `28-005-236`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Входит в руководства:** [[4021528 — K38, K50, QSK38, and QSK50 Service Manual|4021528]]
> **Секции:** Section 5 - Fuel System - Group 05
> **Даты:** изменён 2026-03-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/28/28-005-236.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/28-005-236.pdf)

### Select Service Tools

#### Recommended Cummins® Service Tools

- Single Cylinder Diagnostic Kit, Part Number 3824212

### General Information

This procedure contains multiple steps that can be used to diagnose fuel system issues. This procedure is **not** intended to replace troubleshooting trees. See the appropriate troubleshooting symptom tree in Section TS for repair direction.

Cylinder Cutout Test

- Used to detect a malfunctioning injector by isolating the failed injector while monitoring rail pressure.

### Clean

> [!danger] WARNING · Опасно
> Wear safety glasses or a face shield, as well as protective clothing, to prevent personal injury when using a steam cleaner or high-pressure water.

> [!warning] CAUTION · Осторожно
> Fuel system is extremely sensitive to dirt and debris. All connections and ports must be cleaned and covered. Even a very small amount of debris can result in fuel system malfunction.

Before servicing fuel system components, clean fittings, mounting hardware, and area around component being removed. Use high-pressure water or steam.

To prevent engine damage from debris or contamination, cover all openings immediately after removing component.

### Cylinder Cutout Test

Remove the plugs from both ends of the fuel block on the left bank.

Install the brass needle valves, Part Number 3824521, in the fuel blocks on the left bank.

After bottoming out the brass needle valve, loosen the needle valve four turns.

Remove the plug from the face of the fuel block on the left bank.

Install the Compuchek™ fitting.

Remove the plugs from both ends of the fuel blocks on the right bank.

Install the brass needle valves, Part Number 3824521, in the fuel blocks on the right bank.

After bottoming out the brass needle valve, loosen the needle valve four turns.

Remove the plug from the face of the fuel block on the left bank.

Install the Compuchek™ fitting.

![[fs6howf.png]]

Start the engine.

Let the engine get up to normal operating temperature.

Check for fuel leaks.

Reduce the engine RPM to low idle.

Connect the pressure gauge to the fuel valve assembly Compuchek™ fitting.

![[oi6vagc.png]]

With the engine operating at low idle, close off both right bank needle valves.

Allow the engine RPM to stabilize.

![[oi6vavy.png]]

After the RPM has stabilized, close the close the needle valve to the left bank front quadrant of the engine.

![[oi6vav01.png]]

With the engine operating **only** on the left bank rear quadrant, use the pressure gauge to measure the rail pressure.

Record the measurement.

![[oi6gajk.png]]

Open the needle valve to the left bank front quadrant of the engine.

Allow the engine to stabilize.

Close the needle valve to the left bank rear quadrant of the engine.

![[oi6vav02.png]]

With the engine operating **only** on the left bank front quadrant, measure the rail pressure.

Record the measurement.

![[oi6gajk.png]]

Open the needle valve to the left bank rear quadrant of the engine.

Allow the engine RPM to stabilize.

![[oi6gawc.png]]

Open both needle valves to the right bank of the engine. Close both needle valves to the left bank of the engine. Allow the engine RPM to stabilize.

![[oi6vawf.png]]

Close the needle valve to the right bank front quadrant of the engine.

![[oi6vav03.png]]

With the engine operating **only** on the right bank rear quadrant, measure the rail pressure.

Record the measurement.

![[oi6gajh.png]]

Open the needle valve to the right bank front quadrant of the engine. Allow the engine RPM to stabilize.

![[fv6gajd.png]]

After the engine RPM has stabilized, close the needle valve to the right bank rear quadrant of the engine.

![[oi6vav04.png]]

With the engine operating **only** on the right bank front quadrant, measure the rail pressure.

Record the measurement.

![[oi6gajg.png]]

Open the needle valves on both banks of the engine.

Allow the engine RPM to stabilize.

![[oi6vav05.png]]

Turn off the engine.

Compare the rail pressure measurements between each quadrant.

The graphics of rail pressure measurements are examples **only** of an engine with a single defective injector. Do **not** use as specifications.

The engine low idle rail pressure on the right bank will be approximately 2 psi lower than the left bank due to restriction in the fuel line.

The quadrant that produces higher rail pressure than the other three quadrants is suspected to have a defective injector(s).

| Quadrant | Rail Pressure |
|---|---|
| Left Bank Rear | 12 |
| Left Bank Front | 7 |
| Right Bank Rear | 5 |
| Right Bank Front | 5 |

After the suspected quadrant has been identified, remove the rocker lever covers from that quadrant. [[28-003-011-tr — Rocker Lever Cover|Refer to Procedure 003-011 in Section 3.]]

Install the diagnostic rocker lever covers from the Single Cylinder Diagnostic Kit, Part Number 3824212.

Install a new rocker lever cover gasket.

> [!tip] Момент затяжки · Torque Value
> 45 n•m [35 ft-lb]

![[kn6cvka.png]]

Verify both needle valves are open on each bank of the engine.

![[oi6vav05.png]]

Start the engine and let the engine reach normal operating temperatures. Check for lubricating oil leaks at the diagnostic rocker lever covers.

![[kn6cvkb.png]]

With the engine at low idle, close the needle valves to the three quadrants with standard rocker lever covers.

Allow the engine RPM to stabilize.

![[oi6vawg.png]]

Use the hand knob to depress and release the actuator piston. Tighten the knob to depress the piston. This will hold the injector rocker lever down preventing fuel injection on that cylinder. Loosen the knob to release the piston.

![[rh6ackx.png]]

> [!note] Note · Примечание
> It can be necessary to operate the engine on both quadrants on the same bank if more than one injector is defective to prevent the engine from stalling when checking that quadrant for a defective injector.

Use the needle valve to throttle enough fuel to the good quadrant to prevent the engine from stalling.

![[oi6gakd.png]]

Start with the first cylinder at either end of the isolated quadrant.

Tighten the knob to depress the actuator piston. Repeat two or three times while listening to the engine sound. A distinct change will become audible in the sound of the engine when the actuator piston is depressed and released if the injector is partially or fully functional.

In the event there is no audible change in the sound of the engine, the injector is defective and **must** be replaced. [[28-006-026-tr — Injector|Refer to Procedure 006-026 in Section 6.]]

![[rh6acke.png]]

If an audible change is noted in the sound of the engine, tighten the hand knob and hold the piston against the stop while recording the rail pressure.

Use the pressure gauge to measure the rail pressure.

![[oi6gaji.png]]

After recording the measurement, loosen the hand knob to release the actuator piston.

![[rh6ackf.png]]

Repeat the procedure to check all cylinders in the isolated quadrant. Record the rail pressure for each cylinder with the actuator piston held against the stop.

![[oi600ka.png]]

Turn off the engine. Compare the rail pressure measurements between each cylinder in the quadrant.

The graphics of rail pressure measurements are examples **only**. Do **not** use as specifications.

| Cylinder Number | Rail Pressure |
|---|---|
| Right Bank Number 5 | 38 |
| Right Bank Number 6 | 38 |
| Right Bank Number 7 | 12 |
| Right Bank Number 8 | 38 |

An increase in rail pressure with the actuator piston held against the stop indicates the injector is **not** defective.

If the rail pressure does **not** increase with the piston held against the stop indicates the injector is defective.

Replace the defective injector. [[28-006-026-tr — Injector|Refer to Procedure 006-026 in Section 6.]]

After the replacement injector is installed, repeat the test on the quadrant with the defective injector to confirm the problem is corrected before removing the test equipment.

![[oi6gakc.png]]

Remove the Single Cylinder Diagnostic Kit, Part Number 3824212.

Remove the diagnostic rocker lever covers. Install rocker lever covers. [[28-003-011-tr — Rocker Lever Cover|Refer to Procedure 003-011 in Section 3.]]

Remove the needle valves. Install the plugs into the fuel rail manifold. Refer to Procedure 006-010 in Section 6.

![[fs6howh.png]]
