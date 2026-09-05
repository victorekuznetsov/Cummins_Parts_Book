---
type: "Процедура"
doc: "377-010-150"
title_en: "Turbocharger Actuator Calibration Code"
modified: "2025-01-23"
manuals:
  - "5411181"
figures: 4
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/377/377-010-150.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/377-010-150.pdf"
tags:
  - "документ/процедура"
  - "группа/377"
---

# Turbocharger Actuator Calibration Code

> [!abstract] Процедура · `377-010-150`
> **Входит в руководства:** [[5411181 — X15 CM2350 X114B - Efficiency Series Service Manual|5411181]]
> **Секции:** Section 10 - Air Intake System
> **Даты:** изменён 2025-01-23
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/377/377-010-150.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/377-010-150.pdf)

### Select Service Tools

#### Recommended Cummins® Service Tools

- No Cummins® Service Tools required.

#### Additional Service Items

- No additional service items required.

### General Information

> [!note] Note · Примечание
> Downloading a calibration code into the turbocharger actuator is **only** required if directed by a Campaign, Temporary Repair Practice, or warrantable repair.

Fault Code 4956 will be active if the Turbocharger Actuator Calibration Code does **not** match the engine control module (ECM) calibration.

Turbocharger actuator calibration code downloads can be performed with the recommended Cummins® electronic service tool or equivalent.

The electronic service tool connects to the turbocharger actuator through the engine control module (ECM) by using the J1939 data link.

![[19r00163.png]]

The turbocharger actuator calibration code download can be performed with the actuator installed or removed from the turbocharger.

If the turbocharger actuator is removed from the engine during the calibration code download, the “Install” and “Calibrate Turbocharger Actuator to Turbocharger” steps **must** be performed. [[377-010-134 — Variable Geometry Turbocharger Actuator, Electric|Refer to Procedure 010-134 in Section 10.]]

If the turbocharger actuator is **not** removed during the calibration code download, no further steps are required.

![[10c00185.png]]

### Initial Check

The turbocharger actuator calibration code download process occurs with the keyswitch turned ON. **Always** follow the instructions on the service tool screens.

> [!note] Note · Примечание
> If the tool will **not** communicate with the keyswitch in the ON position, cycle the keyswitch and try again.

![[19800470.png]]

### Install

> [!note] Note · Примечание
> Although either the engine-mounted service tool connector or the vehicle-mounted service tool connector can be used for the software installation, Cummins Inc. recommends the engine-mounted service tool connector be used for the software installation process, whenever possible.

Connect the electronic service tool to the J1939 data link, located on the engine or in the vehicle cab.

Follow the steps in the electronic service tool screens to complete the turbocharger actuator calibration code download.

The turbocharger actuator calibration code download can be performed with the turbocharger actuator installed or removed from the turbocharger.

#### Update Contents of Calibration Workspace

- Connect the electronic service tool.
- Select Advanced ECM Data, select Turbocharger Actuator Compatibility; locate and record turbocharger actuator software part number and hardware part numbers. Locate and record the allowable Application Identifications Allowed.
- Disconnect the electronic service tool.
- Within Calibration Selection menu, use ECM/ PDD Code search, enter software part number without first 0000 (four digits if 0).
- Download turbocharger actuator calibration code to Calibration Workspace.

#### Download Calibration to Turbocharger Actuator

- Connect the electronic service tool.
- Select ECM/PDD calibration tab; select Calibration Workspace, select PDD folder, select turbocharger actuator controller, locate recorded Device Part Number for installed variable geometry turbocharger (VGT).
- Locate the newest software revision that matches the Application Identifications Allowed. If the software part number does **not** have a green check, return to the ECM/ PDD Code search to download the allowed calibration.
- Install turbocharger actuator calibration software part number.
- During install process the electronic service tool automatically disconnects from ECM.
- When complete, the electronic service tool will automatically reconnect.
- New turbocharger actuator calibration code is **not** stored until a key off event occurs.
- Turn keyswitch to OFF position to power down the ECM and wait 100 seconds before turning the keyswitch to the ON position.

If the turbocharger actuator is removed from the engine during the calibration code download, the “Install” and “Calibrate Turbocharger Actuator to Turbocharger” steps **must** be performed. [[377-010-134 — Variable Geometry Turbocharger Actuator, Electric|Refer to Procedure 010-134 in Section 10.]]

If the turbocharger actuator is **not** removed during the calibration code download, no further steps are required.

![[19803969.png]]

### Finishing Steps

> [!note] Note · Примечание
> If the connection is lost during the download process, it can result in Fault Code 2636 or 1894. If this occurs, the turbocharger actuator calibration process **must** be performed a second time to clear Fault Code 2636 or 1894.

- If necessary, complete the VGT actuator installation. [[377-010-134 — Variable Geometry Turbocharger Actuator, Electric|Refer to Procedure 010-134 in Section 10.]]
- Use the electronic service tool to clear all inactive fault codes.
