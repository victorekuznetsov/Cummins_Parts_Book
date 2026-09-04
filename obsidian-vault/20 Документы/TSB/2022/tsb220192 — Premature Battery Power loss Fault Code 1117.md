---
type: "TSB"
doc: "tsb220192"
title_en: "Premature Battery Power loss: Fault Code 1117"
modified: "2022-09-29"
figures: 6
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2022/tsb220192.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb220192.pdf"
tags:
  - "документ/tsb"
---

# Premature Battery Power loss: Fault Code 1117

> [!abstract] TSB · `tsb220192`
> **Даты:** изменён 2022-09-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2022/tsb220192.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb220192.pdf)

## Premature Battery Power loss: Fault Code 1117

### Warranty Statement

The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.

### Contents

**Product Affected**

- B6.7 CM2350 B121B
- B6.7 CM2450 B155B
- ISX12 CM2350 X102
- L9 CM2350 L116B, L9 CM2350 L123B
- L9 CM2450 L126B
- L9N CM2380 L142B
- X12 CM2350 X119B
- X12 CM2450 X137B
- X15 CM2350 X114B
- X15 CM2350 X116B
- X15 CM2450 X124B
- X15 CM2450 X134B

**Issue Summary**

Symptom:

- Fault Code 1117

Root Cause:

- ECM power supply loss
- ECM power ground Loss
- Key Switch voltage drop

**Verification**

- ECM Power Ground Loss: Cummins Inc. prefers the ECM power ground is 4 or 5 wires that will be one the OEM J2 ground for the ECM to be grounded to the cylinder block. The cylinder block ground stud should be an M10 threaded stud on the cylinder block usually below or near the ECM and then from the cylinder block directly to the battery negative post.

> [!note] Note · Примечание
> Some applications may have an ECM case ground strap. This grounds **only** the housing of the ECM and does **not** ground internal connections. This is **not** a connection that would lead to Fault Code 1117.

![[19r99882.png]]

Figure 1, Grounding Strap.

1. ECM Power Supply Loss: The ECM power supply (See Figure 5) is the 4 or 5 wires that will be on the OEM J2 power for the engine control module (ECM).

![[19r99883.png]]

Figure 2, Example Power Distribution Module.

- Loose ECM ground connections will cause intermittent ECM power ground loss. The ECM ground connection is located on the cylinder block as a threaded stud below or near the ECM.

![[19r99884.png]]

Figure 3, Example Grounding Wire Location.

Figure 3 Items:

1. Fuel pump rear bracket.
2. OEM installed bracket.
3. Ground cable, stud, and nut.
4. Power steering pump.
5. Lubricating oil pan.

- Ground noise issues can cause ECM power ground loss if Cummins Inc. grounding best practices are **not** followed.

2. ECM Power Supply Loss: The ECM power supply (See Figure 5) is the 4 or 5 wires that will be on the OEM J2 power for the engine control module (ECM).

- a.Using an OEM Disconnect switch, sometimes referred to as a kill switch, E-Stop, etc., and/or **not** letting the ECM power down appropriately can cause a Fault Code 1117 indicating a premature power supply loss

![[19r99885.png]]

Figure 4, Example Kill Switch.

- Using a Power Distribution Module (PDM) can cause a premature power supply loss. Depending on application this may or may **not** be present. If present, A PDM is a module that can be used to control power on and off to a subset of the equipment or the whole engine.
- If the ECM Power wiring is connected through the starter to the battery a power supply loss could be detected by the ECM.

> [!note] Note · Примечание
> CMI requires ECM power connected straight to battery from the ECM positive terminals on J2.

![[19r99886.png]]

Figure 5, Example OEM wiring Schematic.

3. Key Switch Voltage Drop

- Old or weak batteries weak batteries can cause a voltage drop at engine cranking events.
- Loss of key switch signal or connection could cause voltage drops. Verify key switch hardware and or wiring is not loose. For the purpose of troubleshooting Fault Code 1117, the key switch of concern is the input signal from the OEM's physical key switch to the ECM J2 connector.
- Key switch signal should be uninterrupted without relays. Interruptions of the input signal could induce Fault Code 1117.

![[19r99887.png]]

Figure 6, Key Switch Signal Example.

**Resolution**

- If any connections are found to be incorrectly routed or in need of repair, contact OEM.
- For any malfunctions that are **not** covered under Cummins Inc. warranty, repair locations are to contact OEM for further repair direction.

### Document History
