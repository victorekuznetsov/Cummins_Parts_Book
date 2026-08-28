---
aliases:
  - "Форсунка"
type: "Процедура"
doc: "56-006-026-tr"
title_en: "Injector"
title_ru: "Форсунка"
modified: "2025-11-12"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
families:
  - "QSK60"
manuals:
  - "4021530"
parts:
  - "4918767"
figures: 60
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/56/56-006-026-tr.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/56-006-026-tr.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK60"
  - "группа/56"
---

# Injector
**Форсунка**

> [!abstract] Процедура · `56-006-026-tr`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]]
> **Семейство:** QSK60
> **Входит в руководства:** [[4021530 — QSK45 and QSK60 Service Manual|4021530]]
> **Секции:** Section 6 - Injectors and Fuel Lines - Group 06
> **Даты:** изменён 2025-11-12
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/56/56-006-026-tr.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/56-006-026-tr.pdf)

### General Information

with Electronically Actuated Injector

The injector consists of the following components:

1. O-ring and damper
2. Capscrew
3. Injector hold-down clamp
4. Seal
5. O-rings
6. Injector.

![[06400286.png]]

with Mechanically Actuated Injector

The injector consists of the following components:

1. Sealing ring
2. O-ring (brown)
3. O-ring (green)
4. O-ring (blue)
5. O-ring (black)
6. Capscrew
7. Injector hold-down clamp
8. Injector.

![[06800009.png]]

### Initial Check

with Mechanically Actuated Injector

Misfire Using Heat Indicator Marker

> [!danger] WARNING · Опасно
> Do not remove the pressure cap from a hot engine. Wait until the coolant temperature is below 50°C \[120°F\] before removing the pressure cap. Heated coolant spray or steam can cause personal injury.

> [!note] Note · Примечание
> This procedure is **not** effective when the symptoms occur **only** at low idle or when the engine is cold.

If the engine exhibits symptoms of an injector **not** firing, perform the following check:

- Operate the engine to normal operating coolant temperature of 80°C \[180°F\].
- Stop the engine and allow the exhaust manifold to cool for 10 minutes.
- Use a 204°C \[400°F\] temperature indicator marker, Part Number 3165163, or equivalent, to apply a mark (1) on the surface of all exhaust manifold ports. The mark **must** be as close to the cylinder head as possible, but **not** directly on the exhaust manifold mounting flange.
- Start the engine and operate under light load for a short time. Do **not** operate the engine under heavy load or for an extended period of time, as this can cause inaccurate results.

![[06400198.png]]

> [!note] Note · Примечание
> It is **not** recommended to use the temperature indicator markers to troubleshoot for cylinders that are operating too hot.

If the 204°C \[400°F\] mark melts (1) the color will disappear and leave **only** a transparent glazed appearance where the mark was. This indicates that the cylinder is operating at a temperature above 204°C \[400°F\].

If the 204°C \[400°F\] mark does **not** melt (2), the mark color remains present. This indicates that the cylinder is **not** operating at a temperature of 204°C \[400°F\], indicating a possible injector malfunction.

![[06400199.png]]

> [!warning] CAUTION · Осторожно
> This tool is not intended to be used above the engine idle speed. Do not use above 900 rpm engine speed. Doing so can damage the engine. Start and operate the engine until the coolant temperature reaches the normal range of 80°C \[180°F\]. Shut the engine OFF.

Misfire Using Injector Cutout Tool

Start and operate the engine until the coolant temperature reaches the normal range of 80°C \[180°F\].

Shut the engine OFF.

![[02400014.png]]

Use a 12-mm hex socket or Allen wrench to remove the existing plug from the top side of the cast iron valve cover.

![[02400015.png]]

Screw the single injector diagnostic cut-out tool **clockwise** into the threaded hole in the valve cover, until it bottoms out on the valve cover.

![[02400016.png]]

> [!warning] CAUTION · Осторожно
> This tool is not intended to be used above the engine idle speed. Do not use above 900 rpm engine speed. Doing so can damage the engine.

Install a 0 to 207 kPa \[0 to 30 psi\] pressure gauge on the Compuchek™ fitting located at the front of the block.

Start and operate engine at idle speed for approximately 1 minute.

1. Record the fuel rail pressure reading.

![[02400020.png]]

Rotate the single-injector diagnostic cut-out tool **counter-clockwise** until it is approximately 13 mm \[½ inch\] clear of the valve cover.

1. Note the fuel rail pressure reading.

If the cylinder being tested is working properly, the fuel rail pressure can decrease on reading number 2.

If the cylinder being tested is weak or **not** firing, the fuel rail pressure will **not** change between reading number 1 and number 2.

![[02400017.png]]

Shut the engine OFF.

Repeat the above steps in different rocker lever covers until the non-functioning injector is found.

Replace the non-functioning injector(s).

![[02400018.png]]

After engine diagnostic testing, remove the single-injector diagnostic cut-out tool from the valve cover and install the plug.

Tighten the plug.

> [!tip] Момент затяжки · Torque Value
> 45 n•m [33 ft-lb]

![[02400019.png]]

Check the injectors when it is suspected they were run dry (without fuel).

Remove the rocker lever covers and check to be sure all of the injector links are intact. If they are intact, install the covers and follow the normal injector inspection procedure. If they are **not** intact, follow the injector inspection step in this procedure.

Warm up the engine by running at high idle to stabilize the exhaust temperature. If the exhaust temperatures are within 38°C or 68°F, then all injectors are firing and working correctly.

![[07400026.png]]

with Electronically Actuated Injector

Misfire Using Injector Tester Tool

> [!note] Note · Примечание
> This test **must** be performed with the engine shut down for at least 5 minutes.

> [!note] Note · Примечание
> If the engine is equipped with CM2150 engine control module (ECM) (1), cover the plug with a lint-free cloth. Slowly loosen the plug on the last injector of the high-pressure fuel lines 1/4 to 1/2 turn. The plug does **not** need to be removed to relieve the pressure. Connect INSITE™ electronic service tool and verify the fuel pressure has bled down by monitoring the fuel rail pressure.

![[06k00003.png]]

If the engine exhibits symptoms of an injector **not** firing, perform the following check using the injector iester (1)(2), Part Number 2892293:

1. Plug the tool harness into the injector tester tool via the 4 pin connector.
2. Plug the tool harness into the engine harness via the 9 pin connector.
3. Verify the injector tester tool's yellow READY light is illuminated. If **not**, verify the power supply to the 9 pin connector. If illuminated, proceed.
4. Turn the keyswitch ON.
5. Plug the tool harness into injector via the 2 pin connector.
6. Fully depress and release the injector tester tool's PRESS TO TEST button.

- If the green PASS light is illuminated, the injector is functioning.
- If the red FAIL light is illuminated, the injector is failed and must be replaced.

Repeat steps 5 and 6 until all injectors have been tested.

![[06k00004.png]]

Misfire Using Injector Cutout Tool

Use INSITE™ electronic service tool to perform the cylinder cutout test on engines with electronically actuated injectors. See INSITE™ electronic service tool manual for instructions.

![[14c00040.png]]

Check the injectors when it is suspected they were run dry (without fuel).

Remove the rocker lever covers and check to be sure all of the injector links are intact. If they are intact, install the covers and follow the normal injector inspection procedure. If they are **not** intact, follow the injector inspection step in this procedure.

Warm up the engine by running at high idle to stabilize the exhaust temperature. If the exhaust temperatures are within 38°C or 68°F, then all injectors are firing and working correctly.

![[07400026.png]]

### High-Pressure Injector Return Flow Test

with Electronically Actuated Injector

Remove the injector drain flow hose from the fuel drain manifold block located on the left bank of the engine. Remove the hose from the drain manifold block end (1) **only.** [[56-006-013-tr — Fuel Drain Lines|Refer to Procedure 006-013 in Section 6.]]

The union fitting in the fuel drain block **must** be capped to prevent fuel leakage during the test. It can be capped with Part Number 3164801, or equivalent.

![[06e00069.png]]

Run the injector drain flow hose into a graduated cylinder to collect drain fuel flow. The cylinder must be capable of holding at least 300 ml \[10 oz\].

![[22d00140.png]]

Disconnect each of the individual 2 pin injector electrical connectors (16 for QSK60). Use the following procedure in the QSK38, QSK50, and QSK60 (CM850 Modular Common Rail System) Troubleshooting and Repair Manual, Bulletin 4021533. Refer to Procedure 019-043 in Section 19.

![[06e00070.png]]

With the return flow hose routed to the graduated cylinder, crank the engine at a minimum of 150 rpm for 30 seconds in 10 second intervals.

> [!warning] CAUTION · Осторожно
> Do not overheat the starters. Damage to the starters can result.

The volume of fuel collected during the 30 second crank cycle **must** be less than the volume indicated in the table below.

| Measured Return Flow |  |
|---|---|
| Engine | Volume |
| QSK60 | 200 ml \[6.75 oz\] |

![[06e00071.png]]

Remove the cap from the male union and install the fuel drain hose (1) at the fuel drain block.

> [!tip] Момент затяжки · Torque Value
> 45 n•m [33 ft-lb]

![[06e00069.png]]

### High-Pressure Injector Return Flow Isolation Test

with Electronically Actuated Injector

Drain the low temperature aftercooler (LTA) cooling system. [[56-008-018-tr — Cooling System|Refer to Procedure 008-018 in Section 8.]]

Remove the intake manifolds. [[56-010-002-tr — Aftercooler Assembly|Refer to Procedure 010-002 in Section 10.]]

Install the fuel drain hose on cylinder number 1 LB in place of the banjo bolt through the fuel drain line that routes to the fuel drain block. The fuel drain hose for QSK60 is Part Number 4918679.

Place the end of the fuel injector drain line fuel return flow hose in a small graduated cylinder to collect return flow.

![[22d00140.png]]

Disconnect each of the individual 2-pin injector electrical connectors (16 for QSK60). Use the following procedure in the QSK38, QSK50, and QSK60 (CM850 Modular Common Rail System) Troubleshooting and Repair Manual, Bulletin 4021533. Refer to Procedure 019-043 in Section 19.

![[06e00070.png]]

With the return flow hose routed to the graduated cylinder, crank the engine at a minimum of 150 rpm for 30 seconds in 10 second intervals.

> [!warning] CAUTION · Осторожно
> Do not overheat the starters. Damage to the starters can result.

Record the amount of fuel collected.

![[06e00071.png]]

Swap the fuel drain hose and banjo bolt between cylinders 1 LB and 2 LB.

Place the end of the fuel injector drain line fuel return flow hose in a small graduated cylinder to collect return flow.

Crank the engine at least 150 rpm for 30 seconds in 10 second intervals.

> [!warning] CAUTION · Осторожно
> Do not overheat the starters. Damage to the starters can result.

Record the amount of fuel collected.

![[22d00140.png]]

Repeat the previous step until drain flow has been recorded for all cylinders on both banks.

| Measurements |  |  |
|---|---|---|
|  | ml | fl-oz |
| Isolated Injector Return Flow with Engine Cranking at 150 rpm for 30 Seconds | 15 | 0.5 |

> [!warning] CAUTION · Осторожно
> Do not overheat the starters. Damage to the starters can result.

![[06e00071.png]]

Replace injectors on any cylinder that has more leakage than specified above.

If any injectors were replaced, repeat the test on each of the cylinders until all cylinders have less flow than specified.

![[22d00140.png]]

Remove the fuel drain hose and assemble the fuel drain lines. [[56-006-013-tr — Fuel Drain Lines|Refer to Procedure 006-013 in Section 6]].

Install the intake manifolds. [[56-010-002-tr — Aftercooler Assembly|Refer to Procedure 010-002 in Section 10.]]

Fill the cooling system. [[56-008-018-tr — Cooling System|Refer to Procedure 008-018 in Section 8.]]

### Preparatory Steps

with Mechanically Actuated Injector

> [!danger] WARNING · Опасно
> Depending on the circumstance, fuel is flammable. When inspecting or performing service or repairs on the fuel system, to reduce the possibility of fire and resulting severe personal injury, death or property damage, never smoke or allow sparks or flames (such as pilot lights, electrical switches, or welding equipment) in the work area.

> [!warning] CAUTION · Осторожно
> Do not spill or drain fuel into the bilge area when disconnecting or removing fuel lines, replacing filters, and priming the fuel system. Do not drop or throw filter elements into the bilge area. The fuel and fuel filters must be disposed of in accordance with local environmental regulations.

- Remove the rocker lever cover. [[56-003-011-tr — Rocker Lever Cover|Refer to Procedure 003-011 in Section 3.]]
- Remove the rocker lever assembly. [[56-003-009-tr — Rocker Lever Assembly|Refer to Procedure 003-009 in Section 3.]]

with Electronically Actuated Injector

> [!danger] WARNING · Опасно
> Depending on the circumstance, fuel is flammable. When inspecting or performing service or repairs on the fuel system, to reduce the possibility of fire and resulting severe personal injury, death, or property damage, never smoke or allow sparks or flames (such as pilot lights, electrical switches, or welding equipment) in the work area.

> [!warning] CAUTION · Осторожно
> Do not spill or drain fuel into the bilge area when disconnecting or removing fuel lines, replacing filters, and priming the fuel system. Do not drop or throw filter elements into the bilge area. The fuel and fuel filters must be disposed of in accordance with local environmental regulations.

- Remove the injector supply lines. [[20-006-051-tr — Injector Supply Lines (High Pressure)|Refer to Procedure 006-051 in Section 6.]]
- Install the injector protective plugs, Part Number [[4918767]].
- Remove the two-piece valve cover. [[56-003-011-tr — Rocker Lever Cover|Refer to Procedure 003-011 in Section 3.]]

### Remove

with Mechanically Actuated Injector

> [!note] Note · Примечание
> The hold-down clamp can **not** be removed until the injector is removed.

Remove the injector hold-down capscrew and washer, and discard. Remove the injector and injector hold-down clamp.

Use injector puller, Part Number 3823579, or equivalent, to remove the injectors. Insert the pin of the tool in the hole provided in the body of the injector. The hole faces the front of the engine.

> [!note] Note · Примечание
> If the injector puller is **not** available, carefully use a pry bar. Pry upward on the injector against the cylinder head.

Cover the injection bore to prevent foreign objects from entering the cylinder.

![[06400020.png]]

with Electronically Actuated Injector

> [!note] Note · Примечание
> Do **not** reuse protective plugs. The protective plugs **must** be used immediately upon removal from the plastic wrapping. If they are **not** used immediately, the protective plugs **must** be discarded. If the protective plugs are fouled in any manner before use, the protective plugs **must** be discarded and a new set used.

If **not** already completed, plug the ports in each side of the injector tee-piece with the injector protective plugs before removing the injector. Make sure that the plugs are wedged firmly into place. This will prevent debris from entering and causing damage to the injector.

![[06600454.png]]

> [!warning] CAUTION · Осторожно
> DO NOT reuse the injector hold down capscrew or injector combustion seal. The reuse of those components can result in engine damage.

> [!note] Note · Примечание
> On applications with high drain line head pressure, such as a fuel tank mounted higher than the engine, shut off the fuel drain line valve and evacuate the fuel drain line of fuel before removing the injector.

Remove and discard the injector hold-down capscrew.

Use a heel bar to remove the injector. Place the heel between the injector body and the exhaust rocker lever and gently pry the injector from the injector bore.

> [!note] Note · Примечание
> On applications with high drain line head pressure, such as a fuel tank mounted higher than the engine, it is possible for fuel to leak from the drain line into the cylinder when the injector is removed. After removing the injector, check for fuel dripping into the cylinder and evacuate the fuel before continuing in the removal procedure.

Cover the injector bore in the cylinder head to prevent foreign objects from entering and causing damage to the bore and combustion chamber.

![[06400388.png]]

Remove and discard the seal on the end of the injector.

![[06400379.png]]

Remove and discard the two o-rings on the injector.

![[06400289.png]]

Do **not** remove the o-ring/damper at this time.

![[06600267.png]]

### Clean and Inspect for Reuse

with Mechanically Actuated Injector

Use a lint-free cloth to clean the exterior of the injector.

![[06400117.png]]

Sealing rings are available in different thicknesses to adjust the injector protrusion.

Remove the sealing ring and note the cylinder location.

Inspect the injector o-rings.

Inspect the injector body and cup retainer for cracks or other damage.

Inspect the injector links for damage, excessive wear, and pitting or scoring on the ball ends.

> [!note] Note · Примечание
> If the link is damaged, or if pitting or scoring can be seen or felt, the link **must** be replaced.

![[06400386.png]]

> [!danger] WARNING · Опасно
> When using solvents, acids, or alkaline materials for cleaning, follow the manufacturer's recommendations for use. Wear goggles and protective clothing to reduce the possibility of personal injury.

Use solvent when cleaning the filters. The screens **must** be thoroughly dry prior to installation.

Check the rail (6) and timing (7) filter screens for debris, tears, or punctures. If the screens are damaged, the injector **must** be replaced.

![[06400009.png]]

with Electronically Actuated Injector

> [!danger] WARNING · Опасно
> When using solvents, acids, or alkaline materials for cleaning, follow the manufacturer's recommendations for use. Wear goggles and protective clothing to reduce the possibility of personal injury.

Clean the injector assembly with electrical contact cleaner, Part Number 3824510, or equivalent. Allow to air dry completely.

Do **not** use compressed air to clean or dry the injector.

![[06400291.png]]

Inspect the nozzle tip for damage.

Replace injectors with damaged nozzles that prevent fuel delivery into the combustion chamber.

![[06400292.png]]

Inspect the injector body for signs of corrosion, cracks, or other damage.

Inspect the o-ring grooves for damage that will **not** allow the o-rings to seal properly.

![[06400293.png]]

Inspect the t-fitting on top of the injector where the injector supply lines attach.

Inspect for corrosion, cracks, or other damage that will **not** allow proper sealing of the injector supply lines.

Replace damaged injectors.

![[06400294.png]]

Inspect the o-ring/damper for wear, cracks, or other damage. Replace, if damaged.

If the valve cover shows signs of oil leakage around the injector, replace the o-ring/damper.

Inspect the injector wiring for damaged wires, shrink tubing, elbow, and connector.

![[06400296.png]]

### Calibrate

with Mechanically Actuated Injector

This procedure requires special equipment and **must** be done at a Cummins® Authorized Repair Location.

![[fi801ua.png]]

with Electronically Actuated Injector

Calibration is **not** required for electronically actuated injectors.

![[06400389.png]]

### Install

with Mechanically Actuated Injector

Do **not** lubricate the o-rings until the injector is ready for installation in the cylinder head.

Install four new o-rings on the injector. Do **not** twist the o-rings.

O-ring (1) is brown and is smaller in diameter than the other three.

O-ring (2) is green.

O-ring (3) is blue and is larger in diameter than (2), but has a smaller cross section than o-ring (4).

O-ring (4) is black and is the largest in diameter and cross section.

![[06400387.png]]

Install the proper size sealing ring.

[[56-002-004-tr — Cylinder Head|Refer to Procedure 002-004]] in Section 2 for instructions on how to measure injector protrusion and select the correct seal.

> [!note] Note · Примечание
> Incorrect injector protrusion can lead to premature injector tip wear.

![[06400386.png]]

Use clean engine lubricating oil (15W-40) to lubricate the o-rings.

![[06400014.png]]

Install the hold-down clamp on the side of the injector.

Install the injector and hold-down clamp in the cylinder head.

> [!note] Note · Примечание
> If the injector installation tool, Part Number 3824830, is **not** available, use a 40 mm \[1 9/16 inch\] socket with an extension and a rubber mallet to install the injector.

Use injector installation tool, Part Number 3824830, to set the injector in the bore.

The slide hammer will make a dull sound when the injector is seated properly.

![[06400016.png]]

Use clean engine oil to lubricate the injector hold-down capscrew.

Install the new washer and injector hold-down capscrew.

> [!tip] Момент затяжки · Torque Value
> 75 n•m [55 ft-lb]

![[06400365.png]]

with Electronically Actuated Injector

Install the new o-ring/damper on the injector.

![[06600270.png]]

Install the new o-rings on the injector body.

![[06400289.png]]

> [!warning] CAUTION · Осторожно
> DO NOT reuse the injector hold-down capscrew or injector combustion seal. The reuse of those components can result in engine damage.

Install the new seal on the end of the injector.

![[06400379.png]]

> [!danger] WARNING · Опасно
> Some solvents are flammable and toxic. Read the manufacturer's instructions before using.

> [!danger] WARNING · Опасно
> When using solvents, acids, or alkaline materials for cleaning, follow the manufacturer's recommendations for use. Wear goggles and protective clothing to reduce the possibility of personal injury.

> [!danger] WARNING · Опасно
> Wear appropriate eye and face protection when using compressed air. Flying debris and dirt can cause personal injury.

> [!warning] CAUTION · Осторожно
> Keep the injector bore and combustion chamber protected when using compressed air to prevent contamination. Failure to do so can cause engine damage.

> [!warning] CAUTION · Осторожно
> DO NOT reuse the injector hold down capscrew or injector combustion seal. The reuse of those components can result in engine damage.

> [!note] Note · Примечание
> On applications with high drain line head pressure, such as a fuel tank mounted higher than the engine, it is possible for fuel to leak from the drain line into the cylinder when the injector is removed. Prior to installing the injector, check for fuel dripping into the cylinder and evacuate the fuel before installing the injector.

Clean the injector bore in the cylinder head with electrical contact cleaner, Part Number 3824510, or equivalent, to make sure the o-rings will seal properly.Verify the injector bore is free of debris to allow proper sealing of the new o-rings.

Clean the threaded hole in the cylinder head where the injector hold-down capscrew will be installed with electrical contact cleaner, Part Number 3824510, or equivalent, and compressed air.

![[06400364.png]]

Lubricate the threads and underside of the new injector hold-down capscrew with clean engine lubricating oil.

![[06400365.png]]

Lubricate all the o-rings with a light coating of clean engine lubricating oil.

![[06400366.png]]

> [!warning] CAUTION · Осторожно
> Do not reuse the injector hold-down capscrew or injector combustion seal. The reuse of those components can result in engine damage.

Assemble the injector hold-down clamp and capscrew into the injector.

![[06s00062.png]]

> [!warning] CAUTION · Осторожно
> Only use a soft face mallet. Otherwise damage to the injector can occur.

The injector installer can be used on single or multiple injector installations.

Install the assembly into the cylinder head by tapping gently on the injector with a soft face mallet.

Verify the injector is fully seated in the cylinder head before proceeding.

> [!note] Note · Примечание
> If the injector is **not** fully seated prior to torquing it can lead to engine damage during operation.

![[06400368.png]]

Assemble the injector installer kit, Part Number 4918620. Finger-tighten the three shoulder capscrews.

![[06400369.png]]

Place the injector installer on the injector such that the ball spring plunger is on the tapered side of the injector (1). If necessary, adjust the ball spring plunger so that it presses against the injector. Make sure the flat side of the injector (2) sits flush with the injector installer.

![[06400370.png]]

Align the injector installer with two injectors.

![[06400371.png]]

Verify the injector hold-down clamp is properly located.

Hand tighten the injector hold-down clamp capscrew two to three turns to start, verifying the hold-down clamp capscrew engages properly to prevent cross threading.

Torque the injector hold-down capscrews.

The 60 degree torque angle can be achieved at the capscrew by marking the location of one corner of the capscrew to a location on the injector hold-down clamp.

Tighten to:

> [!tip] Момент затяжки · Torque Value
> 68 n•m [50 ft-lb]

Back off completely.

Tighten to:

> [!tip] Момент затяжки · Torque Value
> 30 n•m [22 ft-lb]

Rotate the capscrew 60 degrees.

Remove the injector installer.

![[06400297.png]]

### Finishing Steps

with Mechanically Actuated Injector

- Install the rocker lever assembly. [[56-003-009-tr — Rocker Lever Assembly|Refer to Procedure 003-009 in Section 3.]]
- Adjust the valves and injectors. [[56-003-006-tr — Overhead Set (OBC)|Refer to Procedure 003-006 in Section 3.]]
- Install the rocker lever cover. [[56-003-011-tr — Rocker Lever Cover|Refer to Procedure 003-011 in Section 3.]]
- Operate the engine and check for leaks.

with Electronically Actuated Injector

- Adjust the valves. [[56-003-006-tr — Overhead Set (OBC)|Refer to Procedure 003-006 in Section 3.]]
- Install the rocker lever cover. [[56-003-011-tr — Rocker Lever Cover|Refer to Procedure 003-011 in Section 3.]]
- Remove the protective plugs from the injectors.
- Install the injector supply lines. [[56-006-051-tr — Injector Supply Lines (High Pressure)|Refer to Procedure 006-051 in Section 6.]]
- Paint the exposed portion of the injector to prevent the formation of rust and corrosion.
- Operate the engine and check for leaks.

## Детали, упомянутые в документе

| Артикул | Наименование | Русское название |
|---|---|---|
| [[4918767]] | Protective Plug | Защитная пробка |
