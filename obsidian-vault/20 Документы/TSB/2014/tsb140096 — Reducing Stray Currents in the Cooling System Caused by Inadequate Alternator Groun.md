---
type: "TSB"
doc: "tsb140096"
title_en: "Reducing Stray Currents in the Cooling System Caused by Inadequate Alternator Grounding"
released: "2014-08-11"
modified: "2014-08-11"
engines:
  - "80141463"
  - "80248213"
families:
  - "QSX15"
figures: 9
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2014/tsb140096.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb140096.pdf"
tags:
  - "документ/tsb"
  - "двигатель/QSX15"
  - "год/2014"
---

# Reducing Stray Currents in the Cooling System Caused by Inadequate Alternator Grounding

> [!abstract] TSB · `tsb140096`
> **Двигатели:** [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSX15
> **Даты:** выпущен 2014-08-11 · изменён 2014-08-11
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2014/tsb140096.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb140096.pdf)

## Reducing Stray Currents in the Cooling System Caused by Inadequate Alternator Grounding

### Core Issue

This document reviews the issue of excessive stray currents in the cooling system caused by inadequate alternator grounding and examines specifically their effects on the lubricating oil cooler assembly.

Improper alternator grounding will increase current flow passing through the cooling system and across the cylinder block, causing damage to the lubricating oil cooler components. This has been identified in both automotive and industrial applications. This document applies specific visual inspection criteria and the corrective resolution for improper alternator grounding.

There are two types of alternator designs that utilize different grounding methods. The grounding cable location point is crucial to preventing stray currents from entering the engine block and doing damage to the lubricating oil cooler assembly. The two grounding strategies are:

- Non-Case Isolated: Splits the current between a ground cable and the alternator mounting location
- Case Isolated: The current is directed **only** through a dedicated ground cable to the starter negative terminal or directly to the negative battery terminal.

### Confirmation

Once it has been determined the lubricating oil cooler element is damaged, the root cause of the malfunction **must** be identified. Oil cooler elements can fail due to a number of causes. Therefore, it is important to determine the correct root cause of the malfunction.

Inspect the oil cooler elements for signs of electrical damage as follows:

- Determine the location of the leak (areas of electrical damage can be random).
- Inspect the lubricating oil cooler element end plate for signs of electrical arcing. This can appear as white stains on the element end plate. (See Figure 1)
- Inspect the lubricating oil cooler element fins for signs of electrical arcing. This can appear as black discoloration due to the electrical arcing. (See Figure 2)
- Inspect the coolant thermostat cover for signs of electrical damage. This will be exhibited as a small pocketed area, often with jagged edges and a distinctive burn mark. (See Figure 3 & 4)
- Inspect the lubricating oil cooler element for erosion. (See Figure 5).

![[08p00066.png]]

Figure 1

![[08p00067.png]]

Figure 2

![[08p00068.png]]

Figure 3

![[08p00069.png]]

Figure 4

![[08p00070.png]]

Figure 5

If damage is found during the inspection of the lubricating oil cooler components, the damaged components **must** be replaced according to the appropriate service procedure. In addition, the cooling system **must** be inspected for stray currents when the repairs have been completed.

Perform a walk-around inspection. Visually check the electrical system installation. Look for alternator type, rating, and whether it is an isolated or non-isolated system. Identify the alternator grounding path (could be multiple paths). Inspect the condition of the ground cable, straps, and post. In some instances, it was found some original equipment manufacturers (OEMs) were grounding the alternator to the lubricating oil cooler housing. This is **not** an approved grounding location according to Cummins Inc., standards and will cause damage to the lubricating oil cooler components. Cummins Inc., requirements state that the alternator **must** be grounded to the battery or to the point at which the negative battery cable attaches to the starter or engine block. Some OEMs use the cylinder block ground stud as a connection point for the cab and accessory ground. This is typically due to space limitations on the starter motor negative connection. Although this installation is **not** optimum, it typically should **not** lead to stray electrical currents passing into the engine cooling system, since the electrical current is **only** using the ground stud as a connection point. If OEMs are using the cylinder block as a connection point, cab currents need to be taken into consideration (subtracted from the calculations).

> [!note] Note · Примечание
> Some OEM's have installed additional ground leads from the alternator body and mounting locations to the vehicle chassis and from the vehicle chassis to the vehicle electrical power source in an attempt to reduce the electrical current passing through the engine block and cooling system. This had limited success and excessive electrical current was still passing through the engine block.

Testing current flow at ground cables.

- Start and operate the engine at approximately 1500 rpm constant speed to gain optimum alternator output.
- Make sure equipment full electrical load is applied during the test. (Lighting, in-cab appliances, etc…..)
- Using an inductive ampmeter, Cummins® Part Number 3823574, measure the current from the cylinder block ground stud to the starter negative connection
- Record the amperage flow. If the current flow is higher than specifications, further investigation is required to determine the source of excessive current.
- Specification (approximately 8 amperes. Limit: fuel priming pump ground path uses approximately 6 amperes).
- By routing the alternator negative directly to the starter negative/battery negative will eliminate high current flow via cylinder block.

### Resolution

When it has been verified that the engine cooling system is carrying stray current, the alternator **must** be adequately grounded. Follow these instructions for the correct alternator grounding. Although allowed, cylinder block grounding is **not** the optimal location for alternator grounding. Re-routing the ground cable to the starter negative post or negative battery post will greatly reduce the possibility of stray current across the cylinder block. Reference Figure 6 for a diagram of the preferred alternator grounding. The correct way to attach alternator/chassis/cab grounds are down to starter negative with a ground to engine block and back to battery negative post. It has been found that cab grounds connected to the engine block put a significant amount of stray current through the block, so it is recommended to also connect this to the starter negative if the space is available.

The alternator ground cable **must** also meet an effectiveness specification. The effectiveness specification defines the percentage of alternator current that **must** return to the battery by the way of the cable, as opposed to other paths such as the engine block. For case isolated alternators, this is **not** an issue as the alternator current will travel through the ground cable. For alternators that are **not** case isolated, the current typically splits between the ground cable and the alternator mounting location or engine block.

![[08p00071.png]]

Figure 6

![[08p00072.png]]

Preferred Alternator Grounding - Figure 7

![[08p00073.png]]

Isolated Ground Connector Point - Figure 8

![[08p00074.png]]

Figure 9

Figure 9 illustrates two pole starters are available for more grounds to be connected. The yellow arrow is the block ground. The blue arrow is the chassis ground. The black arrows are starter leads. The purple arrow is the alternator lead. The red arrow is the cab ground.

### Warranty Statement

The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.

### Document History
