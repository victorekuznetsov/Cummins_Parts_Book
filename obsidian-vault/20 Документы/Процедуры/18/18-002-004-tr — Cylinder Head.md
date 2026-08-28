---
aliases:
  - "Головка блока цилиндров"
type: "Процедура"
doc: "18-002-004-tr"
title_en: "Cylinder Head"
title_ru: "Головка блока цилиндров"
modified: "2021-06-29"
engines:
  - "37269910"
  - "37280605"
families:
  - "K19"
manuals:
  - "4021499"
parts:
  - "3867687"
figures: 73
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/18/18-002-004-tr.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/18-002-004-tr.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K19"
  - "группа/18"
---

# Cylinder Head
**Головка блока цилиндров**

> [!abstract] Процедура · `18-002-004-tr`
> **Двигатели:** [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]]
> **Семейство:** K19
> **Входит в руководства:** [[4021499 — K19 Service Manual|4021499]]
> **Секции:** Section 2 - Cylinder Head - Group 02
> **Даты:** изменён 2021-06-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/18/18-002-004-tr.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/18-002-004-tr.pdf)

### General Information

ReCon® has implemented a new stamping code for all K and QSK cylinder heads.

The stamp is a diamond shape located between the short port exhaust valve and long port intake valve on the rocker lever side of the cylinder head. The marking, or lack of a marking inside the diamond shape indicates the size of the injector seal.

- An empty diamond shape indicates that the ReCon® cylinder head is equipped with a standard size injector seal.
- One mark inside the diamond shape indicates the cylinder head is equipped with a 0.010 oversize injector seal.
- Two marks inside the diamond shape indicate that the cylinder head is equipped with a 0.020 oversize injector seal.
- Three marks inside the diamond shape indicate that the cylinder head is equipped with a 0.030 oversize injector seal.

K and QSK cylinder heads use a different injector seal. Reference the tables below.

| K Cylinder Head Seal Part Numbers |  |
|---|---|
| Injector Seal Part Number | Injector Seal Size |
| 207244 | Standard |
| 3001658 | 0.010 oversize |
| 3001659 | 0.020 oversize |
| 3001660 | 0.030 oversize |

| QSK Cylinder Head Seal Part Numbers |  |
|---|---|
| Injector Seal Part Number | Injector Seal Size |
| [[3867687]] | Standard |
| 3347933 | 0.010 oversize |
| 3347934 | 0.020 oversize |
| 3347935 | 0.030 oversize |

![[02400187.png]]

Injector Seal Markings Location

Injector Seal Markings

1. Standard
2. 0.010 oversize
3. 0.020 oversize
4. 0.030 oversize.

### Preparatory Steps

> [!danger] WARNING · Опасно
> Batteries can emit explosive gasses. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and connect the negative (-) battery cable last.

> [!danger] WARNING · Опасно
> Do not remove the pressure cap from a hot engine. Wait until the coolant temperature is below 50°C \[120°F\] before removing the pressure cap. Heated coolant or spray or steam can cause personal injury.

> [!danger] WARNING · Опасно
> Coolant is toxic. Keep away from children and pets. If not reused, dispose of in accordance with local environmental regulations.

- Disconnect the batteries or air supply to the air starter to prevent accidental starting. Refer to the OEM service manual.
- Drain the cooling system. [[18-008-018-tr — Cooling System|Refer to Procedure 008-018 in Section 8.]]
- Remove the turbocharger. [[18-010-037-tr — Turbocharger, Water-Cooled|Refer to Procedure 010-037 in Section 10.]]
- Remove the exhaust manifold. Refer to Procedure 011-007 in Section 11.
- Remove the fuel supply lines. Refer to Procedure 006-024 in Section 6.
- Remove the aftercooler assembly. Refer to Procedure 010-002 in Section 10.
- Remove the fuel supply manifold. Refer to Procedure 006-022 in Section 6.
- Remove the STC oil manifold, if equipped. Refer to Procedure 006-038 in Section 6.
- Remove the rocker lever covers. Refer to Procedure 003-011 in Section 3.
- Remove the rocker levers. Refer to Procedure 003-009 in Section 3.
- Remove the push rods or tubes. [[18-004-014-tr — Push Rods or Tubes|Refer to Procedure 004-014 in Section 4.]]
- Remove the gear cover clamping plate. Refer to Procedure 001-031 in Section 1.
- Remove the rocker lever housing. [[18-003-013-tr — Rocker Lever Housing|Refer to Procedure 003-013 in Section 3.]]
- Remove the injector. Refer to Procedure 006-026 in Section 6.

![[ck800wa.png]]

### Remove

> [!danger] WARNING · Опасно
> This component or assembly weighs greater than 23 kg \[50 lb\]. To prevent serious personal injury, be sure to have assistance or use appropriate lifting equipment to lift this component or assembly.

Remove the six cylinder head capscrews.

Remove the cylinder head and the gasket.

Record the cylinder head gasket part number to determine if the gasket has standard or oversized thickness.

Discard the gasket.

![[02400005.png]]

### Clean

> [!danger] WARNING · Опасно
> When using solvents, acids, or alkaline materials for cleaning, follow the manufacturer's recommendations for use. Wear goggles and protective clothing to reduce the possibility of personal injury.

Clean the cylinder heads with solvent, Part Number 3824421, or equivalent.

Check for broken springs or other damage.

![[02400011.png]]

### Inspect for Reuse

Check for cracks on the combustion surface.

| Cylinder Head Allowable Crack Length |  |  |
|---|---|---|
| mm |  | in |
| 6 | MAX | 0.25 |

If a crack around the injector bore exceeds the maximum length, the cylinder head **must** be replaced.

Both ends of a crack between the valve **must** be visible. If one end of a crack extends into the valve seat bore (behind the valve seat), the condition of the cylinder head is questionable. To be sure the cylinder head is reusable, remove the valve and valve seat.

![[kn6bdsa.png]]

Measure the valve head depth in the cylinder head with a depth gauge, Part Number 3164438, or equivalent.

| Allowable Valve Depth in Combustion Face |  |  |
|---|---|---|
| mm |  | in |
| 0.00 | MIN | 0.000 |
| 0.51 | MAX | 0.020 |

If the valve head depth is **not** within specifications, the cylinder head **must** be reconditioned.

![[kn6vaja.png]]

Check the flatness of the cylinder head with a straight edge and feeler gauge.

The cylinder head **must** be resurfaced if a feeler gauge larger than 0.08 mm \[0.003 in\] will fit between the straight edge and the cylinder head.

The cylinder head can be resurfaced as long as the thickness measurement is within specifications.

| Used Cylinder Head Minimum Thickness (1) |  |  |
|---|---|---|
| mm |  | in |
| 119.76 | MIN | 4.715 |

| New Cylinder Head Thickness (1) |  |  |
|---|---|---|
| mm |  | in |
| 120.52 | MIN | 4.745 |
| 120.78 | MAX | 4.755 |

If the cylinder head is resurfaced, make sure the injector protrusion and valve depth are adjusted properly.

![[02400077.png]]

### Disassemble

> [!danger] WARNING · Опасно
> The valve springs are under compression. Use caution when using the valve spring compressor. Personal injury can result if the tool slips out of the hands.

Use one of the valve spring compressors listed below to remove the valve springs:

- Valve spring compressor, Part Number 3163606
- Valve spring compressor stand, Part Number ST-1022
- Valve spring compressor plate, Part Number 3163177, can be used with valve spring compressor, Part Number 3163066, and valve spring compressor stand, Part Number ST-1022, to remove four springs at once
- Air operated valve spring compressor, Part Number 3375960.

The intake and exhaust valves are different.

Mark the valves for location prior to removal, to aid in assembly.

Remove the listed parts:

1. Valve collet
2. Valve spring retainer
3. Valve spring
4. Valve spring rotator/or guide
5. Valve.

![[kn6hdfa.png]]

If a valve guide is replaced, the valve seat insert for the valve guide **must** be measured for runout. It is likely the seat **must** also be machined or replaced.

> [!note] Note · Примечание
> **Only** replace the valve guide if it is **not** within specifications.

Remove the worn valve guide (2) with a mandrel (1) and an arbor press.

![[02400147.png]]

> [!note] Note · Примечание
> **Only** replace the valve seat if it is **not** within specifications.

If necessary, a groove (2) can be machined in the valve seat insert to allow the valve seat extractor (1) to be used.

Machine a groove into the valve seat insert, as close to the bottom of the bore as possible, with valve seat grooving kit, Part Number 3376405, or equivalent.

![[02400150.png]]

Remove the valve seat with the appropriate valve seat extractor listed below and slide hammer, Part Number 3376799.

- Exhaust seat extractor, Part Number ST-1323-1
- Intake seat extractor, Part Number 3376799.

> [!note] Note · Примечание
> In some older cylinder head assemblies, the intake ports contain anti-swirl plates.

Remove and discard the anti-swirl plate, if used.

![[02400151.png]]

> [!note] Note · Примечание
> **Only** remove the crosshead guide if it is bent or is **not** within specifications.

Crosshead guides that are straight and are installed to the correct height do **not** have to be removed to install stemless crossheads.

![[02400156.png]]

To remove the cup plugs, a drill, sheet metal screw, and a slide hammer from the light duty puller kit, Part Number 3375784, is used.

![[02400038.png]]

Cup plugs **must** be removed from the cylinder head casting for cleaning purposes.

Remove and discard the ten cup plugs.

![[kn6epga.png]]

### Pressure Test

One method to pressure test the cylinder head is to use the hydrostatic tester, Part Number ST-1012, with the water test adapter plate, Part Number 3375070.

The steps below outline this method.

![[kn8toga.png]]

Remove one of the two plugs from the pressure regulator.

Install a pressure gauge into the regulator.

Turn the adjusting knob on the regulator **counterclockwise** as far as it will turn.

![[kn8toaa.png]]

Install the pressure regulator between the air supply and the quick disconnect fitting.

The arrow on the top of the pressure regulator **must** point in the direction of the air flow (toward the disconnect fitting).

![[kn8toab.png]]

With the head positioned as illustrated in the graphic, assemble the adapter plates.

The guide pins on the lower plate, Part Number 3375070, (5) **must** fit into the water passages.

The o-ring on the upper plate (4) creates a seal on the upper water passage.

The other end of the plate fits into the injector bore.

![[kn6toha.png]]

Place the clamping assembly (1) over the head and adapters.

The guide pins on the clamp **must** fit into the holes in the adapter plate.

Tighten the clamp on the cylinder head.

Connect the wire hose to the upper adapter fitting.

![[kn6tohb.png]]

Attach the lifting arm (2) to the clamp assembly with the lock pins.

One mounting location on each piece is colored red.

![[kn6tohc.png]]

> [!danger] WARNING · Опасно
> This component or assembly weighs greater than 23 kg \[50 lb\]. To prevent serious personal injury, be sure to have assistance or use appropriate lifting equipment to lift this component or assembly.

Adjust the air pressure to 552 kPa \[80 psi\].

Lower the cylinder head into a tank of water.

Bubbles will indicate a leak.

If the cylinder head leaks, it **must** be repaired or replaced.

![[kn6hdda.png]]

An alternate method to using the hydrostatic tester, Part Number ST-1012, pressure testing the cylinder head is to use the cylinder head leak test kit, Part Number 3164341, with the pressure regulator valve kit, Part Number 3164231.

Assemble the wing nut (8) to the clamp and plug (13).

![[22a00130.png]]

> [!note] Note · Примечание
> The K19 engine uses **only** the four longer assemblies shown.

Install the clamp and plug assembly into the cylinder head to block the coolant passages.

Insert the appropriate capscrew through the valve guide side of the cylinder head and thread it into the clamp.

Tighten the capscrew.

> [!tip] Момент затяжки · Torque Value
> 20 n•m [177 in-lb]

![[22a00131.png]]

Install the o-ring (4) into the o-ring groove of the test adapter (5).

Thread the adapter elbow (6) into the adapter (5).

![[22a00133.png]]

Place the test adapter assembly into the cylinder head.

Install the clamp (7) over the test adapter assembly and secure it with the appropriate capscrew and washer.

Tighten the capscrew.

> [!tip] Момент затяжки · Torque Value
> 54 n•m [40 ft-lb]

![[22a00134.png]]

Connect the pressure regulator valve kit to the pipe nipple.

Connect the pressure regulator valve kit to compressed air and adjust the air pressure to 345 kPa \[50 psi\].

![[22a00135.png]]

> [!danger] WARNING · Опасно
> This component or assembly weighs greater than 23 kg \[50 lb\]. To prevent serious personal injury, be sure to have assistance or use appropriate lifting equipment to lift this component or assembly.

Attach an eye bolt to the cylinder head.

Use a suitable lifting device to lift the cylinder head.

Immerse the cylinder head into a tank of water.

Check for bubbles. Bubbles indicate an air leak.

If the cylinder head leaks, it **must** be repaired or replaced.

![[22a00136.png]]

### Clean and Inspect for Reuse

Check the valve guide for chips and cracks.

Measure the inside diameter of the valve guide with a ball gauge or a dial bore indicator.

| Valve Guide Inside Diameter (Installed) |  |  |
|---|---|---|
| mm |  | in |
| 12.598 | MIN | 0.496 |
| 12.674 | MAX | 0.499 |

The valve guide can be reusable if the inside diameter of the first 13 mm \[0.50 in\] from the top or bottom of the valve guide is over specification. However, if an area 13 mm \[0.50 in\] or greater from the top or bottom is out of tolerance, the valve guide **must** be replaced.

![[02400137.png]]

> [!danger] WARNING · Опасно
> When using solvents, acids, or alkaline materials for cleaning, follow the manufacturer's recommendations for use. Wear goggles and protective clothing to reduce the possibility of personal injury.

Clean the part with solvent, Part Number 3824421, or equivalent.

Measure the valve guide bore inside diameter.

| Valve Guide Bore Inside Diameter |  |  |
|---|---|---|
| mm |  | in |
| 21.438 | MIN | 0.844 |
| 21.463 | MAX | 0.845 |

If the valve guide bore is **not** within specifications, ream the bore for an oversize valve guide.

The oversize valve guides are oversized on the outside diameter **only**. The bore in the valve guide is **not** oversized.

Valve guides are available in two oversize guides: 0.25 mm \[0.010 in\] and 0.38 mm \[0.015 in\].

Ream the valve guide bore to maintain a press fit within 0.25 to 0.062 mm \[0.001 to 0.003 in\] between the valve guide and the valve guide bore.

![[02400148.png]]

Clean the valve seat insert bore.

Check the length of any cracks extending into the valve insert bore.

The cylinder head **must** be replaced if a crack extends into the bottom of the bore.

Sometimes it is possible to remove the crack by machining the cylinder head to use an oversize valve seat insert.

Use valve insert counterbore cutter kit, Part Number ST-257, or equivalent, with the appropriate counterbore cutter listed below:

- ST-1310-1 (0.010 oversize)
- ST-1310-2 (0.020 oversize)
- ST-1310-3 (0.030 oversize)
- ST-1310-4 (0.040 oversize).

![[02400161.png]]

Measure the inside diameter and the depth of the valve seat insert bore.

| Valve Seat Insert Bore Inside Diameter (6) |  |  |  |
|---|---|---|---|
|  | mm |  | in |
| Intake with Anti-Swirl Plates | 60.38 | MIN | 2.377 |
|  | 60.40 | MAX | 2.378 |
| Exhaust and Intake without Anti-Swirl Plates | 60.38 | MIN | 2.377 |
|  | 60.40 | MAX | 2.378 |

| Valve Seat Insert Bore Depth (7) and (8) |  |  |  |
|---|---|---|---|
|  | mm |  | in |
| Intake with Anti-Swirl Plates | 13.00 | MIN | 0.512 |
|  | 13.13 | MAX | 0.517 |
| Exhaust and Intake without Anti-Swirl Plates | 12.50 | MIN | 0.492 |
|  | 12.62 | MAX | 0.497 |

If the valve guide seat insert inside diameter is **not** within specifications, use an oversize valve seat.

Oversize valve seat inserts are available in the sizes listed in the table below. Machine the valve seat insert bore in the cylinder head to maintain a press fit within 0.064 to 0.114 mm \[0.002 to 0.005 in\] between the valve seat insert and the valve seat insert bore.

| Outside Diameter Oversize | Depth (Thickness) of Oversize |
|---|---|
| 0.25 mm \[0.010 in\] | Standard |
| 0.51 mm \[0.020 in\] | 0.13 mm \[0.005 in\] |
| 0.76 mm \[0.030 in\] | 0.25 mm \[0.010 in\] |
| 1.02 mm \[0.040 in\] | 0.38 mm \[0.015 in\] |

![[02400152.png]]

> [!note] Note · Примечание
> K19 engines with an engine serial number greater than 37158462, built 13 July 1995, do **not** have crosshead guides. These engines use stemless crossheads.

The crosshead guide **must** be straight. Measure the crosshead guide outside diameter.

| Crosshead Guide Outside Diameter |  |  |
|---|---|---|
| mm |  | in |
| 10.973 | MIN | 0.432 |
| 11.002 | MAX | 0.434 |

If the crosshead guide is **not** within specifications it **must** be replaced, or the stemless crosshead guides **must** be used on the engine assembly. It is authorized, but **not** recommended, to have a stemmed and stemless crosshead on the same cylinder. Installation of stemless crossheads is recommended.

![[02400138.png]]

> [!note] Note · Примечание
> Cummins Inc. recommends installing stemless crossheads instead of machining the cylinder head for oversize crosshead guides.

Measure the crosshead guide bore inside diameter.

| Crosshead Guide Bore Inside Diameter |  |  |
|---|---|---|
| mm |  | in |
| 10.947 | MIN | 0.431 |
| 11.000 | MAX | 0.433 |

Ream the bore to accept an oversize crosshead guide if it is **not** within specifications. Size the bore to maintain a 0.013 to 0.053 mm \[0.002 to 0.005 in\] press fit.

![[02400157.png]]

The intake and exhaust valve face and seating surfaces **must** be cleaned and free of carbon deposits before the inspection is performed.

Use Scotch-Brite™ 7448 abrasive hand pad, Part Number 3823258, or equivalent, to clean the valve.

The valve head thickness gauge, Part Number 3164983, is used to check intake and exhaust valve head thickness. The lower gauging surface marked “INTAKE” is for the intake valve. The upper gauging surface marked “EXHAUST” is for the exhaust valve.

Place the valve into the valve head thickness gauge.

Measure the valve height.

If the valve is flush or above the gauging surface, the valve can be reused.

If the valve is below the gauging surface, the valve can **not** be reused.

![[22600216.png]]

> [!warning] CAUTION · Осторожно
> This type of a check is not as accurate as the checking tool. It can result in valves that are too thin to be reused. Valves that are too thin can fail, causing severe progressive damage to the power cylinder.

If a valve checking tool is **not** available, place the valve on a flat surface and check the height of the outside diameter.

| Minimum Valve Head Thickness (at the Outside Diameter) |  |  |  |
|---|---|---|---|
|  | mm |  | in |
| Exhaust | 3.00 | MIN | 0.120 |
| Intake | 2.16 | MIN | 0.085 |

If the valve is **not** within specifications, it **must** be replaced.

![[02400136.png]]

It is **not** necessary to remove any black or brown stain on the valve closest to the port unless the buildup affects the movement in the guide. Use nothing more coarse than crocus cloth (1000 grit) to remove the stain.

The valve stems are plated with chrome. If there are scuffs or marks that can be felt with the fingernail, the valve **must** be replaced.

Check the collet groove area for wear. If the groove area is worn, the valve **must** be replaced.

Measure the valve stem outside diameter.

| Valve Stem Outside Diameter |  |  |
|---|---|---|
| mm |  | in |
| 12.548 | MIN | 0.494 |
| 12.573 | MAX | 0.495 |

![[kn2vata.png]]

Valve springs of three different lengths are used on the engine. The springs used with a valve rotator are called “short springs”. Springs that are used when a rotator is **not** used are called “long springs”.

There are two different lengths of "short springs". These are identified as red stripe (old) and white stripe (new) short springs.

Cummins Inc. recommends using new white stripe valve springs when the cylinder head is reconditioned.

A bent or broken spring **must not** be used again.

A spring with a notch worn in the first coil **mustnot** be used again. The ends of the springs will wear into the first coil, creating a worn notch in the material.

If a worn notch can be seen or felt, the valve spring **must not** be used again.

Often a spring that has these notches will make a clicking sound. Hand compress the spring until the end of the first coil is completely collapsed to check for a click sound. A large notch will cause a clicking sound.

Check both ends of the spring for the clicking sound.

Check the spring free length.

| Approximate Free Length |  |  |
|---|---|---|
| Long Spring (without rotator) | Red Stripe Spring (with rotator) | White Stripe Spring (with rotator) |
| 85 mm \[3.35 in\] | 65 mm \[2.57 in\] | 69 mm \[2.72 in\] |

Check the spring force at the indicated test height.

| Test Height |  |  |
|---|---|---|
| Long Spring (without rotator) | Red Stripe Spring (with rotator) | White Stripe Spring (with rotator) |
| 50 mm \[2.0 in\] | 39 mm \[1.53 in\] | 38 mm \[1.51 in\] |

| Valve Spring Force |  |  |  |
|---|---|---|---|
|  | n |  | lbf |
| Long Spring (without rotator) | 1053 | MIN | 237 |
|  | 1237 | MAX | 278 |
| Red Stripe Spring (with rotator) | 1183 | MIN | 266 |
|  | 1308 | MAX | 294 |
| White Stripe Spring (with rotator) | 1241 | MIN | 279 |
|  | 1383 | MAX | 311 |

If the valve spring is **not** within specification, the valve spring **must** be replaced.

![[07400086.png]]

### Magnetic Crack Inspect

> [!warning] CAUTION · Осторожно
> To reduce the possibility of engine damage, always demagnetize and clean the parts thoroughly after a magnetic particle inspection.

Use the magnetic particle residual method to check the valves for cracks.

Check the exhaust valves with the coil shot method.

Use a 305 mm \[12 in\] minimum diameter coil.

| Coil Shot Amperage (Ampere Turns) |  |
|---|---|
| Minimum | Maximum |
| 400 VDC or rectified VAC | 800 VDC or rectified VAC |

An ampere turn is an electrical current of one ampere flowing through the coil multiplied by the number of turns in the coil.

Test the valve.

A broad fuzzy pattern will appear at the welded joint on the exhaust valves. This is normal. If there is a distinct line in the broad fuzzy pattern, the valve **must** be replaced.

![[kn2vakb.png]]

Use the head shot method to test the intake valve.

| Head Shot Amperage (Ampere) |  |
|---|---|
| Minimum | Maximum |
| 500 VDC or rectified VAC | 700 VDC or rectified VAC |

![[kn2vakd.png]]

The acceptable criteria for intake and exhaust data is listed below:

1. Indications less than 38.1 mm \[1.50 in\] in length are acceptable
2. No indications
3. **Only** longitudinal indications are acceptable
4. **Only** longitudinal indications are acceptable
5. No indications.

More than five indications, spaced closer than 3.175 mm \[0.125 in\] are **not** acceptable.

![[kn2vake.png]]

### Grind

Valve

Intake and exhaust valves **must** be ground to the same angle.

Use valve facing machine, Part Number 3376256, to grind the valve to a 30 degree angle, as illustrated in the graphic.

Do **not** to remove too much material too quickly. **Only** remove the minimum amount of material, making sure the seating area of the valve is free from grooves.

![[kn8vaxa.png]]

### Machine

Valve Seat

Cummins Inc. recommends using machines that will cut the valve seat insert. Grinding the valve seat with stones that are too coarse can cause an unacceptable surface finish that can lead to early valve and/or seat wear. If the valve protrusion is too great and a machine to cut the valve seat is **not** available, Cummins Inc. recommends to remove the seat then machine the bore in the cylinder head to a greater depth, if possible.

Use a valve guide arbor set, Part Number 3375946, or equivalent, with valve seat grinding machining ST-685-A (110 VAC) or ST-685-C (220 VAC).

Machine the valve seat insert to the angle illustrated in the graphic.

Measure the valve seat insert width.

| Valve Seat Insert Width |  |  |  |
|---|---|---|---|
|  | mm |  | in |
| Intake | 3.05 | MIN | 0.120 |
|  | 3.56 | MAX | 0.140 |
| Exhaust | 1.52 | MIN | 0.060 |
|  | 2.54 | MAX | 0.100 |

![[02400139.png]]

If the width of the valve seat is **not** within specifications, remove the surface material on the inside diameter and outside diameter to decrease the width of the valve seat.

If the valve seat specifications are **not** obtained by machining, the valve seat **must** be replaced.

![[02400140.png]]

It is important that the eccentrimeter is **not** positioned too far down the arbor. The meter needle **must not** complete more than between one and one and a half revolutions before touching the valve seat insert. If the meter will **not** touch the insert at a minimum revolution, change the arbor to a smaller diameter. The meter will have to be adjusted for each seat and arbor combination.

Use an eccentrimeter, Part Number ST-685-4, or equivalent, and the arbor included in the valve seat grinding machine kit, Part Number ST-685-A or ST-685-C.

Measure the valve seat to the valve guide concentricity.

The seat and guide **must** be concentric within 0.05 mm \[0.002 in\].

If the concentricity is **not** within specification, machine the valve seat.

![[02400141.png]]

### Assemble

Identify the valve guide style and location.

Locomotive and some hydraulic excavator engines **must** use the flat-top style (5). This valve guide is grooved to allow the use of a valve stem seal.

When the flat-top style with a seal is used, it is to be installed in all four locations in the cylinder head.

All other engines use the taper-top valve guide (3).

Use the appropriate valve guide driver (6) and an arbor press to install the valve guide (7) to the specified height.

- Taper-Top valve guide (3), use valve guide driver, Part Number 3376779.
- Flat-Top valve guide (5), use valve guide driver, Part Number 3376149.

| Valve Guide Height (Installed) |  |  |  |
|---|---|---|---|
|  | mm |  | in |
| Taper-Top (3) | 33.655 | MIN | 1.325 |
|  | 34.163 | MAX | 1.345 |
| Flat-Top (5) | 29.210 | MIN | 1.150 |
|  | 29.718 | MAX | 1.170 |

![[02400149.png]]

> [!warning] CAUTION · Осторожно
> To reduce the possibility of crosshead guide damage, do not use a hammer to install the crosshead guide.

Install the crosshead guide to the specified height into the cylinder head with a crosshead spacer (10), Part Number ST-1264, or equivalent, and a press.

| Crosshead Guide Height (Installed) |  |  |
|---|---|---|
| mm |  | in |
| 59.69 | MIN | 2.350 |
| 60.20 | MAX | 2.370 |

The new crosshead guide **must** be straight.

![[02400158.png]]

Identify the correct valve seat insert.

- The top of the graphic is the intake port valve seat insert.
- The bottom of the graphic is the exhaust port valve seat insert.

Both the intake and exhaust port valve seat inserts **must** be installed with the 30 degree angle positioned as illustrated in the graphic.

Exhaust valve seat inserts are color coded blue to identify the 30 degree angle side of the seat insert.

![[02400153.png]]

> [!note] Note · Примечание
> Some engines do **not** require an anti-swirl plate. Engines that do **not** require an anti-swirl plate **must** have an insert spacer plate.

Install a new anti-swirl plate in each intake port.

![[02400154.png]]

> [!warning] CAUTION · Осторожно
> Do not use a hammer or mallet to install the valve seat inserts. The inserts can be cracked leading to a seat failure.

Install the valve seat insert (4) with a mandrel (9) and an arbor press.

![[02400155.png]]

Check the injector bore for cracks or other damage.

If cracks or other damage is found, the cylinder head **must** be repaired or replaced.

![[02400142.png]]

> [!warning] CAUTION · Осторожно
> Support the cylinder head to prevent damage to the injector tip that protrudes from the combustion face.

Install the injector protrusion gauge, Part Number 4919196, into the cylinder head. Refer to Procedure 006-026 in Section 6.

![[02400189.png]]

Turn the cylinder head over.

Measure the injector protrusion with a depth gauge, Part Number 3164438.

| Injector Protrusion |  |  |
|---|---|---|
| mm |  | in |
| 2.29 | MIN | 0.090 |
| 2.79 | MAX | 0.110 |

If the protrusion is **not** within specifications, use an oversize sealing ring.

The sealing ring sizes and the amount of injector protrusion associated with the use of each ring is listed in the table below.

| Injector Sealing Rings |  |
|---|---|
| Wall Thickness | Injector Protrusion Change |
| 0.356 to 0.432 mm \[0.014 to 0.017 in\]\* | 0.00 mm \[0.000 in\] |
| 0.483 to 0.559 mm \[0.019 to 0.022 in\] | 0.25 mm \[0.010 in\] |
| 0.610 to 0.686 mm \[0.024 to 0.027 in\] | 0.51 mm \[0.020 in\] |
| 0.737 to 0.813 mm \[0.029 to 0.032 in\] | 0.76 mm \[0.030 in\] |
| \* The injector sealing ring with a wall thickness of 0.356 to 0.432 mm \[0.014 to 0.017 in\] is the standard sealing ring. |  |

![[kn2slkd.png]]

Remove the injector protrusion gauge, Part Number 4919196, or equivalent, from the cylinder head.

![[02400189.png]]

Apply Loctite™ sealant, Part Number 3375068, to the cup plugs.

![[ck8epwa.png]]

Cup plug driver handle, Part Number 3164085, is used with expansion plug drivers, Part Numbers 3376813 and 3376814.

Use the appropriate expansion plug driver and handle combination to drive in the cup plug until the shoulder of the driver contacts the cylinder head.

![[kn6epga.png]]

Install the valve into the valve guide.

Measure the depth of the valve with a depth gauge, Part Number 3164438, or equivalent.

The valve head **must** be even with or **not** more than 0.51 mm \[0.020 in\] below the surface of the cylinder head.

If the valve depth is **not** within specifications, the valve or the valve seat **must** be replaced.

![[02400146.png]]

Apply a thin even coating of fine lapping compound, Part Number 3375805, or equivalent, onto the valve face.

Provide pressure in the center of the valve with a power or hand suction lapping tool.

Turn the valve backward and forward.

Continue lapping until the compound shows a continuous contact pattern on both the valve seat insert and the valve.

![[02400159.png]]

> [!warning] CAUTION · Осторожно
> Lapping compound is an abrasive material. Failure will result if the cylinder head, the valves, and the valve seats are not cleaned thoroughly.

Remove the valve.

Clean the lapping compound from the valve, valve seat insert, and cylinder head.

![[02400160.png]]

When turning the rotator by hand, it can turn roughly, be difficult to turn, or **not** turn at all. This is normal until the rotator is installed; after installation it will rotate freely.

The rotator **must** be soaked in clean engine oil for at least 15 minutes prior to installation.

The rotator **must** be installed over the valve guide with the spring pilot flange facing upwards, as illustrated in the graphic.

![[kn6spka.png]]

> [!danger] WARNING · Опасно
> The valve springs are under compression. Be cautious when using the valve spring compressor. Personal injury can result if the tool slips out of the hands.

Use one of the valve spring compressors listed below, to install the valve springs:

- Valve spring compressor, Part Number 3163606
- Valve spring compressor stand, Part Number ST-1022
- Valve spring compressor plate, Part Number 3163177, can be used with valve spring compressor, Part Number 3163066, and valve spring compressor stand, Part Number ST-1022, to remove four springs at a time
- Air operated valve spring compressor, Part Number 3375960.

Thoroughly lubricate the valve guide inside diameter with 140 weight gear oil.

Install the parts:

1. Valve
2. Valve rotator/or guide
3. Valve spring
4. Valve spring retainer
5. Valve collet.

![[kn6hdaa.png]]

### Vacuum Test

Use valve vacuum tester, Part Number 3824277 (115-VAC, 50/60 hz) or 3824278 (220-VAC, 50/60 hz).

Before using the tester, test the leakage shutoff valve to prevent false leakage measurements.

Check the valve:

- Open the shutoff valve.
- Turn on the vacuum pump.
- Place the cup against a smooth surface.
- Close the shutoff valve.
- Turn off the vacuum pump.
- Wait approximately 10 seconds.
- If the gauge drops more than 7 kPa \[2 in Hg\], replace the valve vacuum tester.

![[02j00107.png]]

Install vacuum cup, Part Number 3823852, on the vacuum tester hose.

Inspect vacuum cup seal, Part Number 3823853, prior to installation on the vacuum cup.

Replace the seal if:

- Cracked
- Abraded
- Brittle
- Otherwise damaged.

![[02400026.png]]

The valve and the valve seats **must** be clean and dry.

Cover the valve with the cup and the seal. The seal **must** have a tight contact on the cylinder head around the valve.

To check the exhaust valves, the seal **must** completely fill the milled area between the exhaust valves.

![[02400027.png]]

Move the toggle switch (3) to the ON position.

Turn the vacuum control valve (4) to the OPEN position.

![[02400028.png]]

When gauge indicates 85 percent of barometric pressure, turn vacuum control valve (4) to CLOSED or OFF position. [[99-018-028 — Barometric Pressure at Altitude|Refer to Procedure 018-028 in Section V.]]

> [!note] Note · Примечание
> At sea level, 85 percent of barometric pressure corresponds to 85 kPa \[25 in-hg\].

Turn toggle switch (3) to OFF position.

If unable to achieve specified vacuum, perform following:

- Use soft mallet to hit valve stem to be certain valve is seated.
- Repeat test.
- If still unable to achieve specified vacuum, replace valve, valve guide, and valve seat insert. See Disassemble and Assemble sections in this procedure.

![[02j00033.png]]

> [!warning] CAUTION · Осторожно
> The cylinder head must be disassembled and cleaned after any grinding or cutting procedures to reduce the possibility of engine damage.

Use stopwatch to measure time it takes for needle on vacuum gauge to drop from 85 to 58 percent of barometric pressure.

> [!note] Note · Примечание
> At sea level, 58 percent of barometric pressure corresponds to 58 kPa \[17 in-hg\].

If elapsed time is less than 3 seconds, perform following:

- Repeat the test to be certain the equipment is functioning properly.
- Use a mallet to lightly hit the valve stem to be certain the valve is sealed. Repeat the test.
- Apply a thin coating of grease on the outside diameter of the insert and the valve head. Repeat the vacuum test. The grease pattern will show the point of leakage.
- If the leakage is between the valve insert and the head, the insert **must** be replaced.

If the leakage is between the valve and the valve insert seat, one of the following procedures **must** be performed:

- Lap valve to insert seat
- Grind the valves
- Grind the valve insert seat.

![[02j00034.png]]

### Install

Clean the top of the cylinder block and the cylinder liners.

![[cy8cywa.png]]

Measure the cylinder liner protrusion. Refer to Procedure 001-064 in Section 1.

![[ck1cytj.png]]

The word TOP, stamped on the top of the cylinder head gasket, **must** be visible after the gasket is installed.

Install the cylinder head gasket.

![[02400002.png]]

> [!danger] WARNING · Опасно
> This component or assembly weighs greater than 23 kg \[50 lb\]. To prevent serious personal injury, be sure to have assistance or use appropriate lifting equipment to lift this component or assembly.

Install the cylinder head. It **must** slide easily over the groove pins.

Lubricate the cylinder head capscrew flange with SAE EP 140 weight oil.

Lubricate the cylinder head capscrew threads with clean engine oil.

Allow the excess oil to drip off the capscrews before installing them into the block.

Install the capscrews.

![[02400004.png]]

> [!warning] CAUTION · Осторожно
> The torque specification for the cadmium plated 170 mm \[6¾ in\] capscrews is lower than the torque specification for the lubrite coated (black) capscrews of the same length. Over-tightening of the cadmium plated capscrews causes overload of the cylinder blocks, which can result in counterbore cracking or damaged threads. Do not mix cadmium plated capscrews with lubrite coated (black) capscrews on the same engine.

The original K19 cylinder head capscrews are 170 mm \[6¾ in\]. The capscrews can either be cadmium plated, producing a shiny chrome like finish, lubrite coated which appears black, or have a zinc phosphate coating, which is gray in color but can appear shiny after cleaning with a wire wheel. Make sure the correct torque is used when installing the capscrews.

All K19 engines with a serial number greater than 31103629 and all service blocks shipped since mid-1977 have used 203 mm \[8 in\] capscrews for the cylinder heads. The 203 mm \[8 in\] capscrews can be black or gray in color. Those that are gray in color have a zinc phosphate coating. The gray capscrews can appear shiny after cleaning with a wire wheel. There is **only** one torque specification for all capscrews that are 203 mm \[8 in\] in length.

![[kn8csga.png]]

Tighten the capscrews in the sequence illustrated in the graphic.

Torque Value:

Shiny Chrome 170 mm \[6¾ in\]

Torque Value:

Black 170 mm \[6¾ in\]

Torque Value:

Zinc Phosphate Gray 203 mm \[8 in\]

Torque Value:

Zinc Phosphate Gray 203 mm \[8 in\] (Alternate Method)

![[kn400hb.png]]

### Finishing Steps

> [!danger] WARNING · Опасно
> Batteries can emit explosive gasses. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and connect the negative (-) battery cable last.

- Install the injector. Refer to Procedure 006-026 in Section 6.
- Install the rocker lever housing. [[18-003-013-tr — Rocker Lever Housing|Refer to Procedure 003-013 in Section 3.]]
- Install the gear cover clamping plate. Refer to Procedure 001-031 in Section 1.
- Install the push rods or tubes. [[18-004-014-tr — Push Rods or Tubes|Refer to Procedure 004-014 in Section 4.]]
- Install the rocker levers. Refer to Procedure 003-009 in Section 3.
- Install the rocker lever covers. Refer to Procedure 003-011 in Section 3.
- Install the STC oil manifold, if equipped. Refer to Procedure 006-038 in Section 6.
- Install the fuel supply manifold. Refer to Procedure 006-022 in Section 6.
- Install the aftercooler assembly. Refer to Procedure 010-002 in Section 10.
- Install the fuel supply lines. Refer to Procedure 006-024) in Section 6.
- Install the exhaust manifold. Refer to Procedure 011-007 in Section 11.
- Install the turbocharger. [[18-010-037-tr — Turbocharger, Water-Cooled|Refer to Procedure 010-037 in Section 10.]]
- Fill the cooling system. [[18-008-018-tr — Cooling System|Refer to Procedure 008-018 in Section 8.]]
- Connect the batteries or air supply to the air starter. Refer to the OEM service manual.
- Operate the engine to 70°C \[160°F\] minimum coolant temperature and check for leaks.

![[ck800wa.png]]

## Детали, упомянутые в документе

| Артикул | Наименование | Русское название |
|---|---|---|
| [[3867687]] | Injector Seal | Уплотнение форсунки |
