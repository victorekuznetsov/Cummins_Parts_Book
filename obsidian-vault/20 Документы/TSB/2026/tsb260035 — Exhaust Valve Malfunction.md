---
type: "TSB"
doc: "tsb260035"
title_en: "Exhaust Valve Malfunction"
modified: "2026-02-26"
engines:
  - "33239746"
families:
  - "QSK60 CM2150 MCRS"
parts:
  - "5542028"
figures: 10
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2026/tsb260035.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb260035.pdf"
tags:
  - "документ/tsb"
  - "двигатель/QSK60CM2150MCRS"
---

# Exhaust Valve Malfunction

> [!abstract] TSB · `tsb260035`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]]
> **Семейство:** QSK60 CM2150 MCRS
> **Даты:** изменён 2026-02-26
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2026/tsb260035.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb260035.pdf)

## Exhaust Valve Malfunction

### Warranty Statement

The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.

### Contents

**Product Affected**

- QSK60 CM2150 MCRS
- QSK60 CM850 MCRS
- QSK60 CM2350 K116
- QSK60 CM2350 K121
- QSK60 CM2350 K135
- QSK60 CM2350 K136

**Issue**

QSK60 exhaust valves can malfunction through fatigue fracture and seat material debond causing exhaust gas leakage.

**Symptoms:**

- Fault Code 621
- Fault Code 622
- Fault Code 623
- Fault Code 624
- Fault Code 625
- Fault Code 626
- Fault Code 627
- Fault Code 628
- Fault Code 631
- Fault Code 632
- Fault Code 633
- Fault Code 634
- Fault Code 635
- Fault Code 636
- Fault Code 637
- Fault Code 638
- Fault Code 641
- Fault Code 642
- Fault Code 643
- Fault Code 644
- Fault Code 645
- Fault Code 646
- Fault Code 647
- Fault Code 648
- Fault Code 652
- Fault Code 653
- Fault Code 654
- Fault Code 655
- Fault Code 656
- Fault Code 657
- Fault Code 658
- Exhaust Temperature High
- Runs Rough or Misfires
- White Smoke

**Root Cause:**

- For chordal fractures:
- For seat material de-bond:

**Verification/Confirmation**

To verify an exhaust valve malfunction following exhibiting one or more of the symptoms in this TSB, the cylinder head containing the valve malfunction **must** be isolated.

1. Verify the presence of Exhaust Gas Temperature (EGT) fault codes in the Engine Control Module (ECM) using the Cummins® Electronic Service Tool, or equivalent. EGT's faulting high or low with the most counts should be investigated further.
2. Remove the injector from problem cylinders. Refer to Procedure 006-026 in Section 6 in the Service Manual. Use a borescope to visually confirm signs of exhaust valve damage, including obvious fracture or parts of the valve head missing or damaged, see Figure 1 and Figure 2, and also torched or leaking valves, see Figure 3 and Figure 4.

In any case of exhaust valve malfunction, it is possible that a combination of root causes act together, in sequence, to cause the final exhaust valve malfunction. It is also possible that one root cause acts in isolation to cause exhaust valve malfunction. Final malfunction type depends wholly on the first malfunction, which determines the sequence of events which follows.

The latest exhaust valve hardware has been improved to combat all failure modes. The latest exhaust valve hardware should be used in replacement of all above verified cases.

![[17r02615.png]]

Figure 1, Borescope image showing chordal fracture on an exhaust valve

![[17r02616.png]]

Figure 2, Examples of Exhaust Valve Chordal Fracture

![[17r02617.png]]

Figure 3, Borescope image showing seat material de-bond on an exhaust valve.

![[17r02618.png]]

Figure 4, Exhaust Valve showing Seat Material De-Bond and subsequent torching.

**Resolution**

Exhaust valve head and seat material hardness has been increased to improve material robustness. Production facilities have implemented process improvements to reduce dings, dents, scratches, cracks and surface porosity to reduce the chance of crack initiation on valves during operation. In addition, production facilities have improved post-production inspection criteria and processes to increase detection of dings, dents, scratches, cracks and surface porosity.

Form, fit and function of the valve remains unchanged.

**Reason for Change**

Process improvements have been made to increase the robustness of new exhaust valve hardware. Improved exhaust valve head material hardness and improved supplier inspection post manufacturing are the two methods implemented to improve part quality. These improvements are required to reduce the likelihood of exhaust valve failure modes described in this TSB.

**Customer Communication**

Improvements to exhaust valve hardware have been implemented over time. Changes at production facilities to the valve material and post-production inspection and handling criteria, were implemented at different stages in iterations.

Exhaust valve material hardness improvements were implemented first and affected the QSK60 Tier 2 and QSK60 Tier 4 valves separately, see Table 1. These changes **only** affected valve material and **not** the handling or inspection improvements, which came later. Valve date codes can be cross referenced to year and month, see Table 2.

| Table 1, Valve material improvement implementation |  |  |  |
|---|---|---|---|
| Engine Service Model | Exhaust Valve Part Number | Date Code | Valve Material Clean Date |
| QSK60 CM2150 MCRS QSK60 CM850 MCRS | [[5542028]] | M-W onwards | December 2024 onwards |
| QSK60 CM2350 K116 QSK60 CM2350 K121 QSK60 CM2350 K135 QSK60 CM2350 K136 | 5541752 | A-X onwards | January 2025 onwards |

| Table 2, Exhaust valve date code matrix |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|
|  | **2020** | **2021** | **2022** | **2023** | **2024** | **2025** | **2026** |
| **JAN** | **A-S** | **A-T** | **A-U** | **A-V** | **A-W** | **A-X** | **A-Y** |
| **FEB** | **B-S** | **B-T** | **B-U** | **B-V** | **B-W** | **B-X** | **B-Y** |
| **MAR** | **C-S** | **C-T** | **C-U** | **C-V** | **C-W** | **C-X** | **C-Y** |
| **APR** | **D-S** | **D-T** | **D-U** | **D-V** | **D-W** | **D-X** | **D-Y** |
| **MAY** | **E-S** | **E-T** | **E-U** | **E-V** | **E-W** | **E-X** | **E-Y** |
| **JUN** | **F-S** | **F-T** | **F-U** | **F-V** | **F-W** | **F-X** | **F-Y** |
| **JUL** | **G-S** | **G-T** | **G-U** | **G-V** | **G-W** | **G-X** | **G-Y** |
| **AUG** | **H-S** | **H-T** | **H-U** | **H-V** | **H-W** | **H-X** | **H-Y** |
| **SEP** | **J-S** | **J-T** | **J-U** | **J-V** | **J-W** | **J-X** | **J-Y** |
| **OCT** | **K-S** | **K-T** | **K-U** | **K-V** | **K-W** | **K-X** | **K-Y** |
| **NOV** | **L-S** | **L-T** | **L-U** | **L-V** | **L-W** | **L-X** | **L-Y** |
| **DEC** | **M-S** | **M-T** | **M-U** | **M-V** | **M-W** | **M-X** | **M-Y** |

Exhaust valve production facility handling and inspection improvements were the final step in implementing changes to improve valve quality. Loose exhaust valves, exhaust valve kits and cylinder head assemblies for aftermarket sale were handled on a separate timeline to engine build plant production cylinder head assemblies. Production engine ESN firsts are available in Table 5.

First clean serial numbers are recorded for cylinder head assemblies, see Table 3. All cylinder head assemblies following were fitted with the latest clean exhaust valve hardware.

| Table 3, Serial number firsts for clean cylinder head assemblies |  |  |  |  |  |
|---|---|---|---|---|---|
| Engine Service Model | New / Recon | Part Name | Part Number | Serial Number | Clean Date/ Implementation Date |
| QSK60 CM2150 MCRS | New | HEAD, CYLINDER | 5538438 | S25254141 | 11 Sep 25 |
| QSK60 CM850 MCRS | Recon | HEAD, CYLINDER | 5538438-RX | 5K0294 | 18 Sep 25 |
| QSK60 CM2350 K116 QSK60 CM2350 K121 QSK60 CM2350 K135 QSK60 CM2350 K136 | New | HEAD, CYLINDER | 5540562 | S25258254 | 15 Sep 25 |
| Recon | HEAD, CYLINDER | 5540562-RX | 5K0294 | 18 Sep 25 |  |

Aftermarket loose exhaust valves, exhaust valve kits and cylinder head rebuilt kits take valves from loose exhaust valve stock. Implementation dates are available, see Table 1. Part Numbers of cylinder head assemblies and exhaust valve kits are available, see Table 4.

**Service Instructions**

Clean exhaust valves that have been through final inspection will be marked with a blue dot, see Figure 5. The outside of the exhaust valve box will also have a blue marking on the part number label, in the white section or the red section near the Cummins logo.

![[17r02619.png]]

Figure 5, Blue dot marking on clean valve stock

If an exhaust valve is not marked with a blue dot but was manufactured on or later than the material clean date (see Table 1), then part inspection can be carried out to verify cleanliness. Inspections should be carried out with reference to Figure 6 and using the guided steps below.

![[17r02620.png]]

Figure 6, Exhaust valve inspection areas

1. Use a magnifying glass (5x) or equivalent to check the outer diameter (1), exhaust valve seat (2) and exhaust valve seat edge (3) for porosity or obvious holes in the material surface around the full circumference of the valve, see Figure 7.

![[17r02621.png]]

Figure 7, Example porosity

2. Check for dings, dents or scratches on the exhaust valve seat surface (2). See Figures 8 and 9

![[17r02622.png]]

Figure 8, Example scratches

![[17r02623.png]]

Figure 9, Example dings/dents

If non-conforming parts are found, please return them to the local parts distribution center or branch from which the parts were received. Parts stocking locations can process this non-conforming stock via the parts alert process. See alert 2025-174 for loose valves and valve kits. See alert 2025-175 for cylinder head assemblies.

**Service Parts Availability**

Service parts are available. See Table 4 for part numbers.

| Engine Service Model | Part Description | Existing Part Number | Obsolete | Superseded |
|---|---|---|---|---|
| QSK60 CM2350 K116 QSK60 CM2350 K121 QSK60 CM2350 K135 QSK60 CM2350 K136 | HEAD, CYLINDER | 553843900 | No | No |
| HEAD, CYLINDER | 554056200 | No | No |  |
| HEAD, CYLINDER | 561343600 | No | No |  |
| HEAD, CYLINDER | 553843900RX | No | No |  |
| HEAD, CYLINDER | 554056200RX | No | No |  |
| HEAD, CYLINDER | 561343600RX | No | No |  |
| VALVE, EXHAUST | 554175200 | No | No |  |
| KIT, EXHAUST VALVE | 540591200 | No | No |  |
| KIT, CYLINDER HEAD REBUILD | 557911200 | No | No |  |
| QSK60 CM2150 MCRS QSK60 CM850 MCRS | HEAD, CYLINDER | 553843800 | No | No |
| HEAD, CYLINDER | 553844100 | No | No |  |
| HEAD, CYLINDER | 563534300 | No | No |  |
| HEAD, CYLINDER | 569455000 | No | No |  |
| HEAD, CYLINDER | 553843800RX | No | No |  |
| HEAD, CYLINDER | 553844100RX | No | No |  |
| HEAD, CYLINDER | 563534300RX | No | No |  |
| HEAD, CYLINDER | 569455000RX | No | No |  |
| VALVE, EXHAUST | 554202800 | No | No |  |
| KIT, EXHAUST VALVE | 288181100 | No | No |  |
| KIT, CYLINDER HEAD REBUILD | 547340100 | No | No |  |
| KIT, CYLINDER HEAD REBUILD | 547340200 | No | No |  |

**Part Identification**

Exhaust valves are identifiable by the marking on the tip of the valve stem. The valve part number, date code and manufacturing facility will be visible, see Figure 10.

![[17r02624.png]]

Figure 10, Example valve tip information

Clean exhaust valves which have been through final inspection will be marked with a blue dot. See Figure 5 in the service instructions section of this document.

**Part Inventory Action**

In stock parts are affected. See Parts Alert 2025-174 and 2025-175

**Production Status**

Implemented for production. See Table 5.

| Table 5, Production Information |  |  |
|---|---|---|
| ESN First | Build Date 1 | Plant |
| 33240842 | 29 th October 2025 | Daventry Engine Plant |
| 1 Engine build date can be found on engine dataplate. |  |  |

### Document History

## Детали, упомянутые в документе

| Артикул | Наименование | Русское название |
|---|---|---|
| [[5542028]] | Exhaust Valve | Выпускной клапан |
