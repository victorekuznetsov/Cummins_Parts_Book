---
aliases:
  - "Проверка попадания пыли и грязи при диагностике повышенного прорыва газов"
type: "Сервисный бюллетень"
doc: "5613318"
title_en: "Checking For Dirt and Dust Ingestion While Troubleshooting High Blowby"
title_ru: "Проверка попадания пыли и грязи при диагностике повышенного прорыва газов"
released: "2020-01-17"
modified: "2026-07-23"
group: "10 - Intake Air Systems"
engines:
  - "33239746"
  - "33239899"
  - "37292556"
  - "37295879"
  - "41349633"
  - "93058669"
families:
  - "C8.3 · 6C8.3"
  - "K38/K50 · QSK38, QSK50, QSK60"
  - "QSK19"
  - "QST30"
figures: 16
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/bulletin/5613318.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/bulletin/5613318.pdf"
tags:
  - "документ/бюллетень"
  - "двигатель/C8.3"
  - "двигатель/K38/K50"
  - "двигатель/QSK19"
  - "двигатель/QST30"
  - "тема/intake-air-systems"
---

# Checking For Dirt and Dust Ingestion While Troubleshooting High Blowby
**Проверка попадания пыли и грязи при диагностике повышенного прорыва газов**

> [!abstract] Сервисный бюллетень · `5613318`
> **Раздел Cummins:** 10 - Intake Air Systems
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]], [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]], [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[93058669 — 6C8.3 CPL 3105|93058669]]
> **Семейство:** C8.3 · 6C8.3, K38/K50 · QSK38, QSK50, QSK60, QSK19, QST30
> **Даты:** выпущен 2020-01-17 · изменён 2026-07-23
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/bulletin/5613318.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/bulletin/5613318.pdf)

## Checking For Dirt and Dust Ingestion While Troubleshooting High Blowby

**Purpose**

- Do **not** disassemble any part of the air intake system before completing the intake leak checks covered in published troubleshooting.
- Troubleshooting high crankcase pressure faults can be caused by many factors, one being damage to the power cylinder from dirt/dust entering the engine air intake system. When this occurs, identifying the root cause can be very challenging as the defect itself may no longer be present. The air intake system leak checks **must** be performed before any disassembly occurs, which can include a smoke and/or pressure test. See corresponding service manual. Refer to Procedure 010-024 in Section 10.
- This document will provide the required repair instructions for engines that have experienced foreign object debris ingestion (dust out).
- Engines experiencing high blowby, high lubricating oil consumption, or possibly low power are to have their air intake systems inspected for signs of dirt or foreign object debris ingestion and possible leak paths.

#### X15

- The solution set associated with Fault Codes 555, 556, and 1974 and includes a new service tool diagnostic test which can identify low compression on up to two cylinders within the engine (Engine Compression and Air Handling System Test). If the engine has a broken ring, this test will help identify it. When the intake system does have a defect which allows unfiltered air into the engine, cylinder six takes the most of it and will often wear and malfunctionfirst.
- Knowing the state of the cylinders along with the results of the intake leak test and visual observations can be used to make a repair estimate prior to disassembling the engine with the goal to provide the most repair options to the customer while the engine is still in running condition.

**Verification**

Verify the unit exhibits the following complaints:

- Excessive lubricating oil dripping and/or noticeable combustion gases from the draft tube
- A sudden increased rate of lubricating oil consumption
- Engine low power
- High crankcase pressure faults

Possible Causes

- **Not** using an approved air filter. See OEM service requirements.
- Loose or damaged intake clamps between the air filter housing and the turbocharger inlet. For X15 engines built before 2022, see Technical Service Bulletin (TSB), New Turbocharger Adapter and O-ring, TSB210110.
- Worn, loose, or broken air housing latches/clamping hardware
- Loose or poor fitting connection at the turbocharger inlet
- Collapsed or buckled intake piping
- Incorrect air filter installation. Contact the OEM if there is a question about proper air filter installation
- Poor seal at the filter (incorrectly installed, damaged filter or housing, worn latches, and so forth)
- Cuts, tears, or other damage to the air filter media
- Overtightened clamps leading to hose bulging
- Lack of adherence to published maintenance schedules
- Poor owner maintenance practices (cleaning a dirty filter, contamination introduced during service, intake system left open for extended periods of time, and so forth)
- Hose/pipe rub-through
- Poor seal around plastic elbows or tees due to mold parting lines
- Air intake system components incorrectly assembled after a repair

Prior to any part disassembly or removal:

- Connect the recommended Cummins® electronic service tool or equivalent, create an ECM image, perform a full data extraction, and save to file/send to cloud. This **must** be completed prior to recalibrating the ECM or information will be lost.
- If the complaint is Fault Code 555, 556, or 1974 verify the latest ECM calibration code is installed.
- For X15: X114, X116B, X124B, X134B, and X142B – Run diagnostic test “Engine Compression and Air Handling System Test".
- Follow published troubleshooting for the fault code(s) / symptom(s) present.

Check the air intake system for the following:

The air intake system leak checks **must** be performed before any disassembly occurs, which may include a smoke and/or pressure test. Follow the applicable troubleshooting tree according to the fault code(s) and/or symptom(s) present.

- Loose, missing, or misaligned air intake system clamps.
- Air intake system pipe joints that are buckled or collapsed. Hose buckling can result from over-tightened clamps; hose buckling can create leak paths.
- Recently replaced parts. Review warranty claims for both the engine and chassis for repair activities that would necessitate opening the air intake system (intake piping, air filter housing, engine components, and so forth).
- Excessive rubbing or interference.
- Signs of excessive movement, particularly at pipe joints.
- Air filter element fit and seal to the housing, as well as the filter element's overall condition. Also check the filter for any signs of dust passage (Note the brand and part number of the filter; original equipment or replacement filter).
- Inspect the customer's oil and air filter change records for compliance with the proper maintenance schedule or intervals.

Disassembly of the Air Intake System (after the applicable troubleshooting checks and tests are completed)

- Use the appropriate tools to disassemble the air intake piping. Note any overtightened or loose clamps.
- During the disassembly of the intake system, pay special attention to intake joints for possible leak paths.
- Document all suspected dust entry paths. Photographs **must** clearly document dust entry paths.

Parts Handling

- Carefully label and retain any and all parts that are worn or replaced as a result of dust ingestion, as they will be required for documentation and factory analysis.
- Retain all customer, OEM, and engine repair information for the documentation process.

Reference the photos below for visual indicators that dust ingestion has occurred.

![[01c00472.png]]

Figure 1, Dust present in intake piping.

![[01c00473.png]]

Figure 2, Dirt present in Charge-Air Cooler (CAC) hose.

![[00j00460.png]]

Figure 3, Often, the clean side of soft black rubber will age, causing a white “chalking”.

This is **not** dust nor does it rub off. Chalk is **not** a defect, but can hide dust evidence and make pictures hard to interpret.

![[00j00461.png]]

Figure 4, Chalk transfer from soft rubber to hard pipes can show witness of proper sealing.

The soft rubber hose (left) conformed to small irregularities on hard plastic mating pipe (right). This is a proper seal.

![[00j00468.png]]

Figure 5, Chalk can also help identify leak paths when clamp load is low, or a dust leak path is present.

Often dust is a different shade color than the white chalk, allowing a visual clue of the dust leak path.

![[00j00462.png]]

Figure 6, Misaligned filter shows improper sealing

![[00j00463.png]]

Figure 7, Air filters are a service item and not to be reused.

Left, a new filter rubber seal. Right, once torqued, the seal deforms permanently. This picture shows a leak path from low bolt torque allowing dust past the primary sealing surface.

![[00j00464.png]]

Figure 8, Bolt torque was low on this joint and primary seal showed a leak path.

The act of checking torque return to mark sealed this leak path. This joint was on the bottom side and very difficult to see.

![[00j00465.png]]

Figure 9, Dust present on the clean side of filter shows a defect in the media.

When tapped on the floor, dust fell from both the clean and dirty sides of the filter.

1. Dust from the dirty side – acceptable
2. Dust from the clean side – **not** acceptable, proof of filter defect

![[00j00466.png]]

Figure 10, SAE testing standards require the airbox to limit rainwater intake.

In winter, water mixed with road salt can pass through the air filter elements. Salt can then cause corrosion.

![[01c00468.png]]

Figure 11, Turbocharger compressor shaft.

1. Dirt can be found packed into the compressor end of the turbocharger shaft.
2. Leading edge of compressor wheel shows wear from dust ingestion.

Engine Teardown and Inspection

Cylinder Liner - Vertical scratching and loss of cross hatch pattern at low mileage indicates accelerated wear due to dust ingestion.

![[01c00471.png]]

Figure 12, Vertical Scratching on Cylinder Wall.

Piston Ring Wear - Full face wear on the top compression ring, combined with full face wear on the intermediate ring, indicates the presence of dust ingestion, which accelerates ring wear. Notice the presence of a lip on the bottom side of the compression and intermediate rings.

![[00j00467.png]]

Figure 13

Mechanics of top ring wear due to dirt or dust ingestion:

If material that is harder than the piston and ring enter the engine, it can become embedded between the bottom side of the top ring and the piston ring land. Once the debris is embedded, it stays in place creating “sandpaper”.

Repetitive motion of the ring against the piston sands away the bottom of the ring. The lip created is the part of the ring that never enters the piston.

![[01c00467.png]]

Figure 14, Compression Piston Ring Example Side View.

Compression Ring Analysis

1. Lip created by excessive wear due to abrasive particles or extended oil drain intervals.
2. Bottom surface of compression ring.
3. Note full face compression ring wear.

![[01c00470.png]]

Figure 15

Intermediate Ring Analysis Number 1:

1. Top surface of intermediate ring.
2. Full face intermediate ring wear is a clear sign that dust ingestion has occurred.
3. Small lip present on bottom side of intermediate ring indicates that abrasive dust particles have been embedded in the piston ring land.

![[01c00469.png]]

Figure 16, Intermediate Piston Ring Example Front View.

Intermediate Ring Analysis Number 2:

1. Bottom surface of intermediate ring.
2. Note the large area that has **not** been in contact with the cylinder liner.
3. Twenty percent face contact present between intermediate ring and cylinder liner.

> [!note] Note · Примечание
> Ring wear due to extended oil drain intervals and not dust ingestion can be clarified by closely examining the intermediate ring. Excessive top compression ring wear combined with normal wear of the intermediate ring (less than 20 percent face wear) indicates that extended oil drain intervals are the root cause for the excessive top compression ring wear.

**Resolution**

If dust ingestion can be confirmed, an in-frame overhaul **must** be completed.

Parts that **must** be replaced during an in-frame overhaul:

- Cylinder kits (pistons, rings and liners)
- Air compressor
- All associated gaskets and seals including all O-rings removed for testing or during repair.
- For X15, if engine was **not** built with an O-ring on the turbocharger adapter, apply a bead of silicone sealant, Part Number 3164067, in the adapter to turbocharger joint. Refer to TSB210110.

Parts that **must** be cleaned and inspected prior to reuse on all engines:

- Cylinder head – Clean combustion face and inspect for pitting or cracking. Replace cylinder head if pitting or a crack is found. Perform the valve seat vacuum test. If tool is **not** available, conduct the leak test. Replace head if vacuum test or leak test fails.
- Turbocharger - Inspect the leading edge of the compressor wheel for wear (replace if wear is present or if visibly contaminated with foreign object debris)
- Charge-air cooler - Replace if contaminated with dust.
- Main and rod bearings - Light, smooth scratches are acceptable for reuse. Bearings exhibiting deep scratches and/or raised or ragged edges **must** be replaced
- Lubricating oil pump - Reference the appropriate service procedure for instructions on cleaning and inspecting for reuse
- Camshafts, cam followers, tappets, rocker shafts, and rocker levers - Reference the appropriate service procedure for instructions on cleaning and inspecting for reuse.

Parts that **must** be cleaned and inspected prior to reuse on engines with exhaust gas recirculation (EGR):

- EGR cooler - Reference the appropriate service procedure for instructions on cleaning and inspecting for reuse.
- EGR valve - Reference the appropriate service procedure for instructions on cleaning and inspecting for reuse.
- EGR delta pressure tubes or passages - Reference the appropriate service procedure for instructions on cleaning and inspecting for reuse.
- Exhaust manifold - Reference the appropriate service procedure for instructions on cleaning and inspecting for reuse.

Prepare repair estimate.

Requested Failure Information

- Contact Cummins Care 1-800-CUMMINS if all possible causes have been investigation and the issue has **not** been resolved.
- Contact an OEM Dealer if it is suspected that there is an OEM warranty defect. If so, submit the repair estimate.

Corrective Action and Follow-Up

- Work with the customer/fleet to inspect other vehicles in their fleet for similar concerns. Visit the customer as needed. Report any additional findings.
- Work with the customer to set up an inspection process for the air intake system. Use the OEM-specified guidelines to inspect the intake system at the OEM-specified intervals or at normal oil change intervals for loose, missing, or damaged intake system components. For vocational applications operating in dusty environments, more frequent checks **must** be completed.

### Document History
