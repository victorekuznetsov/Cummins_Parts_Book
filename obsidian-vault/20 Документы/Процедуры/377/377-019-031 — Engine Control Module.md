---
aliases:
  - "Электронный блок управления двигателем"
type: "Процедура"
doc: "377-019-031"
title_en: "Engine Control Module"
title_ru: "Электронный блок управления двигателем"
modified: "2019-10-21"
manuals:
  - "5411181"
figures: 9
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/377/377-019-031.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/377-019-031.pdf"
tags:
  - "документ/процедура"
  - "группа/377"
---

# Engine Control Module
**Электронный блок управления двигателем**

> [!abstract] Процедура · `377-019-031`
> **Входит в руководства:** [[5411181 — X15 CM2350 X114B - Efficiency Series Service Manual|5411181]]
> **Секции:** Section 19 - Electronic Controls - Group 19
> **Даты:** изменён 2019-10-21
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/377/377-019-031.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/377-019-031.pdf)

### Select Service Tools

#### Recommended Cummins® Service Tools

- Electrical Contact Cleaner, Part Number 3824510, or equivalent

#### Additional Service Items

- No additional service items required.

### Initial Check

Turn the keyswitch to the ON position while monitoring the fault lamps. The fault lamps **must** illuminate for 2 to 3 seconds.

If the lamps do **not** illuminate, check for burned-out bulbs.

![[gp8swkb.png]]

Turn the keyswitch to the OFF position.

Connect INSITE™ electronic service tool to the vehicle data link.

Turn the keyswitch to the ON position.

Select the Monitor Mode on INSITE™ electronic service tool. INSITE™ electronic service tool **must** be able to communicate with the engine control module (ECM). If the ECM will **not** communicate with INSITE™ electronic service tool, use the ECM - No Communication Troubleshooting Tree in Section TF before requesting authorization to replace the ECM.

Record the following values found in the Trip Information section of Features and Parameters, prior to replacing or calibrating the ECM.

- ECM Distance Offset
- ECM Time Offset
- Engine Distance Offset
- Engine Time Offset

![[19t00005.png]]

### Preparatory Steps

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

- Record all programmable parameters, features, and calibration information from the old ECM before disconnecting the harness connectors. This information will be needed to program the new ECM.
- Disconnect the batteries. See equipment manufacturer service information.

### Remove

> [!note] Note · Примечание
> Do **not** remove the ECM harness clamps from the wiring harnesses.

> [!note] Note · Примечание
> Do **not** close the lever after the connector has been removed from the ECM. Attempting to do so may cause damage to the connector.

> [!note] Note · Примечание
> Do **not** remove the wire tie from the ECM connector backshell.

Loosen the ECM harness clamp capscrews on the engine wiring harness connector and the original equipment manufacturer (OEM) wiring harness connector.

![[19500050.png]]

> [!warning] CAUTION · Осторожно
> To prevent damage to the ECM connector backshell depress the locking tab prior to lifting the lever. Failure to do so will result in damage to the ECM connector backshell.

Disconnect the OEM harness connector and engine harness connector from the ECM by pressing down on the locking tab (1) and pulling up on the lever (2).

![[19500051.png]]

Remove the capscrews that secure the ECM to the ECM mounting plate.

![[19t00007.png]]

### Install

> [!warning] CAUTION · Осторожно
> Do not paint the backside of the ECM. Make sure there is no grease or dirt between the ECM and the engine block.

Install the new ECM to the mounting plate.

Tighten the capscrews.

> [!tip] Момент затяжки · Torque Value
> 25 n•m [221 in-lb]

![[19t00007.png]]

> [!warning] CAUTION · Осторожно
> Do not blow compressed air into the ECM ports or connectors. Compressed air can contain moisture due to condensation.

Use electrical contact cleaner, Part Number 3824510, to remove all dirt and moisture from the ECM connector ports and the harness connectors.

![[19t00008.png]]

Connect the OEM harness connector (1) and engine harness connector (2) to the ECM by placing the connector into the ECM receptacle. Pull back on the locking lever until the connector is fully seated and the lever locking tab is engaged.

If the wire tie securing the wiring harness to the ECM connector backshell was removed, install a new wire tie.

If the ECM harness clamp was removed, use the following procedure for installation instructions. Refer to Procedure 019-043 in Section 19.

> [!note] Note · Примечание
> Do **not** overtighten the ECM harness clamp capscrews.

Tighten the ECM harness clamp capscrews.

> [!tip] Момент затяжки · Torque Value
> 8 to 10 n•m [71 to 89 in-lb]

![[19t00010.png]]

Push on the connector to attach the harness to the bottom of the ECM (1).

> [!note] Note · Примечание
> When an ECM is replaced, the new ECM **must** be calibrated. [[105-019-032 — Engine Control Module Calibration Code|Refer to Procedure 019-032 in Section 19.]]

Use INSITE™ electronic service tool to adjust the following values in the Trip Information section of Features and Parameters after calibrating the ECM.

- ECM Distance Offset
- ECM Time Offset
- Engine Distance Offset
- Engine Time Offset

![[19t00071.png]]

### Finishing Steps

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

- Connect the batteries. See equipment manufacturer service information.
- Operate the engine and check for proper operation.
- Verify vehicle odometer is equal to the value recorded before ECM removal. Contact OEM service location if values are incorrect.
