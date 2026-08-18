---
aliases:
  - "QSK50 и QSK60 CM850/CM2150: замыкание датчиков температуры ОГ"
type: "TSB"
doc: "tsb140112"
title_en: "QSK50 and QSK60 CM850 and CM2150 Exhaust Gas Temperature Sensors Shorted Low or High"
title_ru: "QSK50 и QSK60 CM850/CM2150: замыкание датчиков температуры ОГ"
released: "2014-08-26"
modified: "2014-08-26"
group: "19 - Electronic Engine Controls"
engines:
  - "33239746"
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2014/tsb140112.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/tsb/tsb140112.pdf"
tags:
  - "документ/tsb"
  - "двигатель/K38/K50"
  - "год/2014"
  - "тема/electronic-engine-controls"
---

# QSK50 and QSK60 CM850 and CM2150 Exhaust Gas Temperature Sensors Shorted Low or High
**QSK50 и QSK60 CM850/CM2150: замыкание датчиков температуры ОГ**

> [!abstract] TSB · `tsb140112`
> **Раздел Cummins:** 19 - Electronic Engine Controls
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Даты:** выпущен 2014-08-26 · изменён 2014-08-26
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2014/tsb140112.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/tsb/tsb140112.pdf)

## QSK50 and QSK60 CM850 and CM2150 Exhaust Gas Temperature Sensors Shorted Low or High

### Core Issue

This document highlights a countermeasure that has been developed to reduce customer downtime. Two serious quality problem (SQP) projects have been launched on the QSK50 and QSK60 CM850 and CM2150 exhaust gas temperature (EGT) sensors to identify the root cause of the malfunctions. There are two distinct malfunctions, although they are reporting similar fault codes. The fault codes are either "Voltage Below Normal or Shorted to Low Source" or "Voltage Above Normal or Shorted to High Source". There are two distinct root causes, as listed below.

Typically, QSK50 malfunctions have visible damage at the rear of the sensor body, leading to a loss of insulation and bare wires, chafing, or touching one another.

QSK60 malfunctions, however, are often caused by internal sensor damage that is not visually detectable. This damage can **only** be confirmed by X-rays. It is typically located at the tip of the EGT sensor (in the sensing region).

### Confirmation

Confirm and troubleshoot the appropriate fault codes with an electronic service tool or wiring diagram.

### Resolution

Replace the EGT sensor using Section 019-013 in the QSK38, QSK50, and QSK60 (CM850 Modular Common Rail System) Troubleshooting and Repair Manual, Bulletin 4021533, if required by the customer.

Update the engine's engine control module (ECM) calibrations to the new software, as shown in the list below.

The calibrations have been released to deactivate fault code diagnostics associated with EGT sensors found to be out of range (shorted). This diagnostic is deactivated when:

- More than 50% (8) exhaust gas temperature sensors are not functioning or
- The user electively disconnects 50% (8) exhaust gas temperature sensors.

When the above conditions have been met, diagnostic fault lamps relating to the EGT sensors will **not** be displayed. Additionally, temperature readings will **not** be available from any remaining EGT sensors, even if they are connected and functioning.

If the sensors are disconnected from the harness, a cap should be used to prevent dirt and water ingress while disconnected. One part is required for each disconnected EGT sensor. Contact your local Cummins® distributor for information to source these parts.

The calibration will reactivate EGT sensor functionality when nine or more EGT sensors are connected and functioning correctly. If diagnostics are needed, the EGT sensors will need to be connected and functioning. A keyswitch cycle will be needed to activate or deactivate this function.

These calibrations have no effect on engine performance.

When updating calibrations on a multiple module engine it is important to confirm that the software revisions between the primary, secondary 1, and secondary 2 modules are the same.

To identify an appropriate secondary ECM code(s), first select the correct primary ECM code from the Calibration Selection tab in INSITE™ electronic service tool. Right click on the desired primary calibration code and select "View Compatible ECM/FCM Calibrations" from the selection list. Select the proper ECM part number. The appropriate secondary ECM codes will be displayed.

Refer to the following list for the software ECM codes that have the new feature.

#### Affected Calibrations

- AR60193.05
- AR60194.05
- AR60195.04
- AR60196.04
- AR60199.05
- AR60200.05
- AR60201.07
- AR60202.07
- AR60210.04
- AR60211.04
- AR60212.03
- AR60213.03
- AR60219.07
- AR60220.06
- AR60221.02
- AR60222.02
- AR60253.02
- AR60254.02
- AR60255.03
- AR60256.03
- AR60257.03
- AR60258.03
- AR60259.03
- AR60260.03
- AR60265.03
- AR60266.03
- AR60267.03
- AR60268.03
- AR60269.03
- AR60270.03
- AR60271.02
- AR60272.02
- AR60275.04
- AR60276.04
- AR60277.04
- AR60278.04
- AR60279.04
- AR60280.04
- AR60283.02
- AR60284.02
- AR60285.04
- AR60286.04
- AR60287.02
- AR60288.02
- AR60293.04
- AR60294.04
- AR60295.04
- AR60296.04
- AR60297.02
- AR60298.02
- AR60299.04
- AR60300.04
- AR60301.02
- AR60302.02
- AR60303.04
- AR60304.04
- AR60307.04
- AR60308.04
- AR60309.04
- AR60310.04
- AR60311.04
- AR60312.04
- AR60313.02
- AR60314.02
- AR60315.02
- AR60316.02
- AR60317.02
- AR60318.02
- AR60321.04
- AR60322.03
- AR60323.04
- AR60324.03
- AR60325.04
- AR60326.03
- AR60328.05
- AR60329.05
- AR60330.02
- AR60331.02
- AR60337.02
- AR60338.02
- AR60339.02
- AR60340.02
- AR60343.02
- AR60344.02
- AR60347.02
- AR60348.02
- AR60349.02
- AR60350.02
- AR60354.02
- AR60355.02
- AR60358.02
- AR60359.02
- AR60360.02
- AR60361.02
- AR60362.02
- AR60363.02
- AR60405.01
- AR60406.01.

### Warranty Statement

The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.

### Document History
