---
type: "Процедура"
doc: "377-019-647"
title_en: "Route Parameter Manager Module Calibration Code"
modified: "2018-10-04"
manuals:
  - "5411181"
figures: 8
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/377/377-019-647.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/377-019-647.pdf"
tags:
  - "документ/процедура"
  - "группа/377"
---

# Route Parameter Manager Module Calibration Code

> [!abstract] Процедура · `377-019-647`
> **Входит в руководства:** [[5411181 — X15 CM2350 X114B - Efficiency Series Service Manual|5411181]]
> **Секции:** Section 19 - Electronic Controls - Group 19
> **Даты:** изменён 2018-10-04
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/377/377-019-647.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/377-019-647.pdf)

### Select Service Tools

#### Recommended Cummins® Service Tools

- INLINE™ 7 Data Link Adapter Kit, Part Number 5299899
- Data link adapter for split network, Part Number 5394863
- Cummins Guidanz™ electronic service tool

#### Additional Service Items

- Mobile device
- Wireless or cellular network

### General Information

> [!note] Note · Примечание
> See the following to download the latest version of the Cummins Guidanz™ electronic service tool. [https://www.cummins.com/support/electronic-service-tools-support/guidanz-support](https://www.cummins.com/support/electronic-service-tools-support/guidanz-support)

> [!note] Note · Примечание
> Due to the number of various smart handheld devices, this procedure has been written to be generic. **Not** all illustrations within this procedure will represent the application being worked on.

The route parameter manager calibration update can be performed by Cummins Guidanz™ electronic service tool.

### Preparatory Steps

- Turn the keyswitch to the OFF position.
- Connect the INLINE™ 7 data link adapter to the vehicle service tool connector.
- Turn the keyswitch to the ON position.
- Launch the Cummins Guidanz™ electronic service tool on a mobile device. Connect it to the INLINE™ 7 data link adapter via a bluetooth connection.

> [!note] Note · Примечание
> Cummins Guidanz™ electronic service tool can not perform the map update procedure.

> [!note] Note · Примечание
> It can take up to one hour to complete the route parameter manager calibration update. It is recommended there be a constant power supply to the mobile device for the duration of the procedure.

> [!note] Note · Примечание
> It is recommended to have a constant power supply to the vehicle batteries during the update procedure.

![[19800470.png]]

### Calibrate

From the main screw of the Cummins Guidanz™ electronic service tool, select Route Parameter Manager Module.

![[19l00159.png]]

From the options available, select Calibrate RPM.

> [!note] Note · Примечание
> An active connection to a wireless or cellular network is required to check for code update availability. When using a cellular network, additional data charges can apply.

![[19l00160.png]]

Cummins Guidanz™ electronic service tool will perform a check between the current software in the route parameter manager module and any software available in the Cummins® database.

If new software is available, select Download RPM Engine Control Module (ECM) Code.

> [!note] Note · Примечание
> An active connection to a wireless or cellular network is required to check for code update availability. When using a cellular network, additional data charges can apply.

> [!note] Note · Примечание
> Access to mobile device storage is required.

![[19l00161.png]]

Cummins Guidanz™ electronic service tool will download the calibration to mobile device storage.

> [!note] Note · Примечание
> Access to mobile device storage is required.

![[19l00162.png]]

Select Install RPM ECM Code to initiate the calibration download to the route parameter manager module.

![[19l00163.png]]

Once the calibration process is complete, Cummins Guidanz™ electronic service tool will perform a check between the calibration available in the database and the calibration installed in the route parameter manager module.

> [!note] Note · Примечание
> An active connection to a wireless or cellular network is required to check for code update availability. When using a cellular network, additional data charges can apply.

![[19l00164.png]]

### Finishing Steps

- Turn the keyswitch to the OFF position.
- Disconnect the INLINE™ 7 data link adapter from the vehicle service tool connector.
- Turn the keyswitch to the ON position.

![[19800470.png]]
