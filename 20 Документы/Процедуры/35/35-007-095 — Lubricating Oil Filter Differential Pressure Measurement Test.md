---
type: "Процедура"
doc: "35-007-095"
title_en: "Lubricating Oil Filter Differential Pressure Measurement Test"
modified: "2020-11-17"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "3666322"
figures: 2
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/35/35-007-095.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/35-007-095.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/35"
---

# Lubricating Oil Filter Differential Pressure Measurement Test

> [!abstract] Процедура · `35-007-095`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[3666322 — ISM, ISMe, and QSM11 Service Manual|3666322]]
> **Секции:** Section 7 - Lubricating Oil System - Group 07
> **Даты:** изменён 2020-11-17
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/35/35-007-095.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/35-007-095.pdf)

### General Information

> [!danger] WARNING · Опасно
> To reduce the possibility of personal injury, avoid direct contact of hot oil with your skin.

Use this procedure for engines with plugged oil filters coming into the repair location with one of the following complaints:

1. Amber dash lamp caused by multiple counts of active or inactive Fault Code 143 (Engine Oil Rifle Pressure - Data Valid but Below Normal Operating Range - Moderately Severe Level).
2. Progressive drop of oil pressure on the dash gauge.

The appropriate troubleshooting trees for the existing symptoms **must** be followed.

A plugged oil filter can be detected by taking the proper oil pressure measurements. The oil pressure of an engine with a plugged filter will be high before the filter and low after the filter. A large pressure drop, greater than 172 kPa \[25 psid\] across the oil filter, will distinguish this issue from other issues that cause Fault Code 143, such as an oil sensor or lube pump malfunction.

If filter plugging is occurring at a high frequency, use Symptom Tree t103-56 (Lubricating Oil Filter Plugged), to determine the cause of filter plugging.

### Pressure Differential Test

Remove the oil plugs from the lubricating oil cooler housing at the filter inlet (2) and outlet (1) pressure ports and install manual gauges.

The following parts, or equivalent, are available for use:

| Part Number | Description |
|---|---|
| 3824844 | Compuchek™ fitting for port size M14x1.5 |
| 3376920 | Compuchek™ coupling (1/4-NPT pipe) |
| 3164491 | Electronic pressure adapter for multimeter (1/4-NPT pipe) |
| 3164488 or 3164489 | Electronic digital multimeter |

![[00r00882.png]]

Start and operate the engine until the oil temperature reaches or exceeds 70°C \[160°F\].

| Engine Information |  |
|---|---|
| Lubricating Oil Filter Type |  |
| Kilometers \[Miles} on Lubricating Oil Filter |  |
| Lubricating Oil Type |  |

Operate the engine at each rpm specified. Record the corresponding pressure values:

| Oil Temperature |  |
|---|---|
| Start of Test |  |
| End of Test |  |

![[00r00883.png]]

|  | Engine RPM | Lubricating Oil Pressure Filter Inlet | Lubricating Oil Pressure Filter Outlet | Inlet - Outlet = Differential Pressure | INSITE™ Electronic Service Tool |
|---|---|---|---|---|---|
| Low Idle |  |  |  |  |  |
| High Idle |  |  |  |  |  |

A pressure drop greater than 172 kPa \[25 psi\], at operating temperature, using 15W-40 oil, indicates the filter is plugged.

Identify the causes of a plugged filter. Verify that the Cummins Inc. maintenance guidelines are being met.

Use the following procedure to identify possible fluid contamination. [[35-007-083-tr — Lubricating Oil and Filter Analysis|Refer to Procedure 007-083 in Section 7.]]

Change both the lubricating oil and lubricating oil filter, if plugged.

For additional information about lubricating oil filter plugging, refer to Cummins® Engine Oil and Oil Analysis Recommendations, Bulletin [[3810340 — Cummins® Engine Oil and Oil Analysis Recommendations|3810340.]]
