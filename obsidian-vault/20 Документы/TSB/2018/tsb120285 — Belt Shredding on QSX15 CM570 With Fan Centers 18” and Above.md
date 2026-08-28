---
type: "TSB"
doc: "tsb120285"
title_en: "Belt Shredding on QSX15 CM570 With Fan Centers 18” and Above"
released: "2018-11-07"
modified: "2018-11-07"
engines:
  - "80141463"
  - "80248213"
families:
  - "QSX15"
parts:
  - "3009330"
  - "3026269"
  - "3093936"
  - "3093940"
  - "3104029"
  - "3681390"
  - "3681587"
  - "3902460"
  - "3903112"
  - "3914407"
  - "3935013"
figures: 6
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2012/tsb120285.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb120285.pdf"
tags:
  - "документ/tsb"
  - "двигатель/QSX15"
  - "год/2018"
---

# Belt Shredding on QSX15 CM570 With Fan Centers 18” and Above

> [!abstract] TSB · `tsb120285`
> **Двигатели:** [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSX15
> **Даты:** выпущен 2018-11-07 · изменён 2018-11-07
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2012/tsb120285.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb120285.pdf)

## Belt Shredding on QSX15 CM570 With Fan Centers 18” and Above

### Core Issue

There are QSX engines with fan centers 18” and above experiencing belt shredding due to long belt spans between the fan hub and the crankshaft, as well as the fan hub and the water pump. The span lengths are susceptible to vibration and quick deceleration events which cause the belt to jump grooves and start shredding on the edges of the pulleys. The customer will notice the coolant temperature rising, and find that the belt is missing ribs or is completely gone.

### Confirmation

To determine if the belt shredding on the unit is this issue, measure the fan center between the crankshaft and the fan hub. Compare the shredded belt to photographs 3, 4, and 5 located at the end of this document to determine if it is a match.

### Resolution

If the belt shredding and the fan center match the verification, a tight side idler needs to be installed on the unit to reduce the amount of vibration seen during deceleration events. Addition of a Goliath tensioner, on some FA options, increases the tension in the system, reducing belt vibration.

![[08000054.png]]

Photograph 1: Side View of Goliath Tensioner Configuration and Tight Side Idler

The following parts need to be ordered to install the Goliath belt tensioner configuration and the tight side idler:

| Table 1: Goliath Belt Tensioner Configuration Components |  |  |
|---|---|---|
| Part Number | Part Description | Quantity Required |
| See Table 2 for belt part number | Belt | 1 |
| [[3104029]] | Belt Tensioner | 1 |
| [[3093936]] | Capscrew, M10 x 90 mm | 3 |
| [[3902460]] | Capscrew, M10 x 25 mm | 1 |
| 3681715 | Pilot Adapter | 1 |
| 70760 | Dowel Pin | 1 |
| [[3026269]] | Washer | 1 |
| [[3681587]] | Idler Pulley | 1 |
| [[3914407]] | Capscrew, M10 x 100 mm | 1 |
| [[3935013]] | Dust Shield | 1 |
| 3681191 | Belt Tensioner Bracket | 1 |
| [[3681390]] | Capscrew, M10 x 150 mm | 1 |
| [[3009330]] | Washer | 1 |
| Tight Side Idler Components |  |  |
| [[3681587]] | Idler Pulley | 1 |
| 3035803 | Hex Nut | 2 |
| 3688979 | Idler Pulley Bracket | 1 |
| [[3093940]] | Capscrew, M12 x 45 mm | 2 |
| [[3935013]] | Dust Shield | 1 |
| [[3903112]] | Capscrew, M10 x 30 mm | 1 |
| [[3026269]] | Washer | 1 |

| Table 2: Belt Selection for FA options over 18 inches |  |  |
|---|---|---|
| Factory Installed FA Option | Factory Installed Fan Center Height | Goliath Configuration Belt Part Number |
| FA1545 | 19 inches | 3103838 |
| FA1533 | 19 inches | 3103835 |
| FA1539 | 20 inches | 3103837 |
| FA1541 | 20 inches | 3103838 |

| Table 3: Belt Selection with Tight Side Idler Only |  |  |
|---|---|---|
| Factory Installed FA Option | Factory Installed Fan Center Height | Orion Belt Part Number |
| FA1541 | 20 inches | 3100915 |
| FA1677 | 20 inches | 3100915 |
| FA1678 | 25 inches | 3100269 |

All service procedures referenced below are in Signature™, ISX, and QSX15 Service Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]].

#### Removal of fan drive components

- Remove the fan drive belt, belt tensioner, and belt tensioner support from the peg board.

#### Installation of the tight side idler:

- Remove the fan hub support.

- Install the idler pulley to the idler pulley bracket. Use capscrew, Part Number [[3903112]], and washer, Part Number [[3026269]].

- Install the dust shield. Refer to Procedure 008-030 in Section 8.
- Install the idler bracket to the fan hub support at the 2nd and 4th mounting holes on the right side of the board. Use hex nuts, Part Number 3035803, and capscrews, Part Number [[3093940]].

- Install the fan hub support.

#### Location of tight side idler bracket (no Goliath tensioner installed):

- Top hole of the tight side idler bracket, per Illustration 1, goes into the right side number eleven hole of the peg board for both options.

![[08y00023.png]]

Illustration 1 - Tight Side Idler Bracket

#### Installation of the Goliath belt tensioner configuration:

- Remove the 3 capscrews on the right side of the water pump, as identified in Illustration 2.

![[08000055.png]]

Illustration 2 - Capscrews to be Removed

- Install the belt tensioner bracket, Part Number 3681191, where the three capscrews were removed from the water pump. Per Illustration 2, capscrew 1 is Part Number [[3681390]], capscrews 2 and 3 are Part Number [[3093936]]. Capscrew 3 requires washer, Part Number [[3009330]].

- Install the pilot adapter, Part Number 3681715, and the idler pulley, Part Number [[3681587]].

- Install the Goliath belt tensioner (low mount-large tensioner).

- Install the fan drive belt.

![[08000056.png]]

Photograph 3 - Rib missing while belt is installed on the fan hub pulley.

![[08000057.png]]

Photograph 4 - The eleventh and twelfth ribs separating from the belt.

![[08000058.png]]

Photograph 5 - The ribs separating from the belt shown in the red box.

### Warranty Statement

The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.

### Document History

## Детали, упомянутые в документе

| Артикул | Наименование | Русское название |
|---|---|---|
| [[3009330]] | PLAIN WASHER | Плоская шайба |
| [[3026269]] | PLAIN WASHER | Плоская шайба |
| [[3093936]] | HEXAGON FLANGE HEAD CAP SCREW | Болт с шестигранной головкой и фланцем |
| [[3093940]] | HEXAGON FLANGE HEAD CAP SCREW | Болт с шестигранной головкой и фланцем |
| [[3104029]] | BELT TENSIONER | Натяжитель ремня |
| [[3681390]] | HEXAGON FLANGE HEAD CAP SCREW | Болт с шестигранной головкой и фланцем |
| [[3681587]] | IDLER PULLEY | Натяжной ролик |
| [[3902460]] | HEXAGON FLANGE HEAD CAP SCREW | Болт с шестигранной головкой и фланцем |
| [[3903112]] | HEXAGON FLANGE HEAD CAP SCREW | Болт с шестигранной головкой и фланцем |
| [[3914407]] | HEXAGON FLANGE HEAD CAP SCREW | Болт с шестигранной головкой и фланцем |
| [[3935013]] | DEBRIS SHIELD | Защитный экран от загрязнений |
