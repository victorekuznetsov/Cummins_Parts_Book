---
aliases:
  - "Модуль CM530 CENSE™ — замена внутренней резервной батареи"
type: "TSB"
doc: "tsb120203"
title_en: "CM530 CENSE™ Module - Internal Back-Up Battery Replacement"
title_ru: "Модуль CM530 CENSE™ — замена внутренней резервной батареи"
released: "2012-06-22"
modified: "2012-06-22"
group: "19 - Electronic Engine Controls"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
figures: 12
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2012/tsb120203.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/tsb/tsb120203.pdf"
tags:
  - "документ/tsb"
  - "двигатель/QST30"
  - "год/2012"
  - "тема/electronic-engine-controls"
---

# CM530 CENSE™ Module - Internal Back-Up Battery Replacement
**Модуль CM530 CENSE™ — замена внутренней резервной батареи**

> [!abstract] TSB · `tsb120203`
> **Раздел Cummins:** 19 - Electronic Engine Controls
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Даты:** выпущен 2012-06-22 · изменён 2012-06-22
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2012/tsb120203.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/tsb/tsb120203.pdf)

## CM530 CENSE™ Module - Internal Back-Up Battery Replacement

### Core Issue

The document provides a guide for the replacement of the internal back-up battery installed in the CM530 CENSE™ module, Part Number 3098771.

### Confirmation

This document can be applied to all high horsepower (HHP) engine models and applications that use the CM530 CENSE™ module.

> [!note] Note · Примечание
> This procedure will **not** resolve all CM530 CENSE™ module issues, such as J1939 data link broadcast issues, etc.

#### Background

- The CM530 CENSE™ module is used on many HHP engine platforms, both diesel and natural gas.
- The module is equipped with an internal back-up battery, which is hard-soldered to the module's internal circuit board. It has been considered as "non-replaceable" in the field.
- Cummins Inc. has become aware that in some regions, customers are actively replacing the internal back-up battery. The purpose of this document is to give some guidance on how to replace the back-up battery so that the CM530 CENSE™ module service life can be extended.
- Typically, the expected service life of the back-up battery is approximately five years from the time the battery is installed in the CM530 CENSE™ module, which may be some months prior to the engine being put into service. Cummins Inc. advises the replacement of the back-up battery every five years or when the CM530 CENSE™ module has malfunctioned and the back-up battery condition is suspect.

> [!note] Note · Примечание
> For additional CM530 CENSE™ module related issues, troubleshooting and resolution information, contact a Cummins® Authorized Repair Location.

### Resolution

| Required Equipment |  |  |
|---|---|---|
| Description | Cummins® Part Number | Quantity |
| Torx™ T20 driver | N/A | 1 |
| Medium flat blade screwdriver | N/A | 1 |
| Safety blade | N/A | 1 |
| Soldering iron | N/A | 1 |
| Solder (lead free) | N/A | 1 |
| Heat gun | 3822860 | 1 |
| Deutsch™ DT06-2S connector plug | 3824012 | 1 |
| Deutsch™ Size 16 2-way wedgelock (orange) | 3824013 | 1 |
| Heat shrink insulator 9 mm \[0.354 in\] / 3 mm \[0.118 in\] | N/A | 1 |
| Deutsch™ size 16 terminal remover / installer | 3822760 | 1 |
| Deutsch™ size 16 contact pin\* | N/A | 2 |
| Deutsch™ size 16 contact pin repair wire\* | 3822920 | 2 |
| 3.6V lithium battery | 3681596 | 1 |
| Approximate 30 cm \[12 in\] length 20AWG cable (red) | N/A | 1 |
| Approximate 30 cm \[12 in\] length 20AWG cable (black) | N/A | 1 |
| Junior hacksaw | N/A | 1 |
| Round file | N/A | 1 |
| \*- both will **not** be required, select what is available locally. |  |  |

Battery Replacement Procedure:

1. Assemble the connection harness using the 14AWG wire (approximately 30 cm \[12 in\] in length), Deutsch™ DT06-2S connector plug, wedgelock, and Deutsch™ size 16 contact pins (or Deutsch™ size 16 contact pin repair wires).

![[19903488.png]]

2. Strip the wire insulation back approximately 6 mm \[0.25 in\] and pre-solder the exposed wire. Cover the harness with the heat shrink insulator. Use a heat gun to shrink the insulation to the wire.

> [!note] Note · Примечание
> Industrial applications may require additional strain relief and/or moisture and dirt ingress protection at the connector.

![[19903489.png]]

3. Remove the four Torx™ capscrews from the CM530 CENSE™ module base plate.

![[19903490.png]]

4. Use a medium flat bladed screwdriver to lever-off the base plate from the CM530 CENSE™ module.

> [!note] Note · Примечание
> There will be some resistance, since the base plate is bonded to the internal potting compound.

![[19903491.png]]

5. The internal back-up battery is located on the circuit board adjacent to the CM530 CENSE™ module connector-A socket.

![[19903492.png]]

6. Use a safety blade to cut-away the potting from the area above the back-up battery, until the back-up battery is exposed. A small flat-bladed screwdriver can also be used for removing the potting. Take care as you remove potting from the face of the circuit board, so **not** to damage the circuit board and components.

![[19903493.png]]

> [!note] Note · Примечание
> It is important that all traces of the potting compound are removed from the back-up battery connecting pins (circled above) to make sure of good solder adhesion.

7. Use suitable side cutters to cut the connector pins from the back-up battery.

> [!note] Note · Примечание
> Take care **not** to cut the pins too close to the battery, as this can cause the battery to leak.

Bend the pins away so that accidental contact with the pin stubs on the back-up battery is avoided. The existing battery can be left on the circuit board. If you chose to completely remove the existing back-up battery, it **must** be disposed of in accordance with local and national regulations.

![[19903494.png]]

8. Pre-solder the battery connector stubs protruding from the circuit board. Solder the pre-made harness to the connector stubs as follows:

- Red wire (+), to the connector stub nearest the capacitor
- Black wire (-), to the connector stub nearest the outer edge of the printed circuit board (PCB).

![[19903495.png]]

> [!note] Note · Примечание
> Some engines, such as industrial applications, may benefit from re-potting in the area of the soldered joints to provide additional strain-relief. **Only** potting compounds recommended for electrical components should be used.

9. Use a round file to create an exit point for the battery extension harness, so the harness can exit the module body without being crushed.

![[19903496.png]]

10. Use a junior hacksaw to remove the corner from the CM530 CENSE™ module base plate. This helps prevent the extension harness from being crushed when installing the base plate. De-burr the cut edge of the base plate.

![[19903497.png]]

11. Install the base plate and install the four Torx™ capscrews.

Tighten the Torx™ capscrews: 3 N.m \[27 in-lb\].

![[19903490.png]]

> [!note] Note · Примечание
> For applications in extreme environments (marine applications, engines operation in high humidity regions, or dusty sites, etc.), silicone sealant can also be applied in this region to provide additional cable strain relief and to prevent moisture and dust ingress.

12. Connect the new external back-up battery to the extension harness.

![[19903498.png]]

13. The CM530 CENSE™ module can now be programmed with the appropriate calibration and installed onto the engine. Make sure that the latest available version of the calibration is installed. The external back-up battery / extension harness can be secured to the existing engine harness using the cable tie provided with the back-up battery.

14. The new external back-up battery has a service life of three years and requires replacement at the end of that time period. When changing the external back-up battery, it is important that the external DC power supply is left switched ON. Changing the battery with the DC power supply switched OFF can result in CM530 CENSE™ module program corruption. Installation of the calibration will be required.

### Warranty Statement

The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.

### Document History
