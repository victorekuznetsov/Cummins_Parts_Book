---
type: "TSB"
doc: "tsb150166"
title_en: "New Piston, Low Temperature Aftercooled (LTA) Thermostat, and Engine Control Module (ECM) Calibrations for Haul Trucks Operating at High Altitude."
modified: "2015-12-14"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
families:
  - "QSK60"
parts:
  - "3645958"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2015/tsb150166.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb150166.pdf"
tags:
  - "документ/tsb"
  - "двигатель/QSK60"
---

# New Piston, Low Temperature Aftercooled (LTA) Thermostat, and Engine Control Module (ECM) Calibrations for Haul Trucks Operating at High Altitude.

> [!abstract] TSB · `tsb150166`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]]
> **Семейство:** QSK60
> **Даты:** изменён 2015-12-14
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2015/tsb150166.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb150166.pdf)

## New Piston, Low Temperature Aftercooled (LTA) Thermostat, and Engine Control Module (ECM) Calibrations for Haul Trucks Operating at High Altitude.

### Warranty Statement

The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.

### Contents

**Product Affected**

- QSK60 CM500 (**Only** 2-Stage Haul Trucks Operating at Approximately 2590 Meters \[ 8500 Feet \] or Above)

**Description of Change**

This document announces the release of:

- High compression ratio piston
- New low temperature aftercooled (LTA) circuit thermostat
- New engine control module (ECM) calibrations with high altitude timing algorithm (HATA)

High compression ratio piston:

- Is an existing part that is now being structured into builds for engines operating above 2590 meters \[ 8500 feet \]
- The compression ratio changes from 14.5:1 on the standard piston to 16.0:1 on the high compression ratio piston
- Helps to control combustion at altitude and reduce abnormal firing events and high cylinder pressure spikes

New low temperature aftercooler (LTA) circuit thermostat:

- Has a new higher fully open temperature as compared to the existing part
- Fully open temperature has increased from 57°C \[ 134°F \] to 68°C \[ 154°F \]

New engine control module (ECM) calibrations with high altitude timing algorithm (HATA):

- Adjusts the fueling timing depending on the altitude
- Keeps cylinder pressure at a consistent level and also has small fuel efficiency benefits
- Changes other fueling tables to reduce abnormal combustion

**Reason for Change**

These changes have been made to reduce abnormal combustion events for 2-stage haul trucks operating at approximately 2590 meters \[ 8500 feet \] or above.

**Service Instructions**

For 2-stage haul trucks operating at approximately 2590 meters \[ 8500 feet \] or above, Cummins Inc. recommends the installation of the following:

- New high compression pistons, Part Number 3640513

- New LTA thermostats, Part Number 4381506

- Corresponding ECM calibration with high altitude timing algorithm (HATA) feature
- Once an engine has the new high compression pistons and high altitude timing algorithm (HATA) calibration installed, the engine will be operating with a different control parts list (CPL) and FR rating from that specified on the engine dataplate. This means that a new dataplate **must** be ordered and installed on the engine.

For a detailed component installation recommendation guide, see Table 1 below.

| Table 1, Component Installation Recommendation Guide |  |  |  |  |  |
|---|---|---|---|---|---|
| Installation Scenario | High Compression Piston | LTA Thermostat | ECM Calibration | Altitude | Installation Notes |
| 1 | x | x | x | Above 2590 meters \[ 8500 feet \] | **Always** recommended |
| 2 | x |  | x | Above 2590 meters \[ 8500 feet \] | **Not** recommended but allowed |
| 3 |  |  | x | Above 2590 meters \[ 8500 feet \] | **Not** allowed |
| 4 | x |  | x | Below 2590 meters \[ 8500 feet \] | **Not** allowed |
| 5 |  |  | x | Below 2590 meters \[ 8500 feet \] | **Not** allowed |
| 6 |  | x |  | Any | **Not** recommended but allowed |
| 7 | x |  |  | Below 2590 meters \[ 8500 feet \] | **Not** allowed |
| 8 | x | x |  | Above 2590 meters \[ 8500 feet \] | **Not** recommended but allowed |
| 9 | x | x |  | Below 2590 meters \[ 8500 feet \] | **Not** allowed |
| 10 | x |  |  | Above 2590 meters \[ 8500 feet \] | **Not** recommended but allowed |

Installation Scenario Notes:

1. **Always** recommended: Cummins Inc. recommends that all three components are installed together to effectively reduce abnormal combustion events.

2. **Not** recommended but allowed: The new LTA circuit thermostat will be particularly effective in cold climates, and will stop the decay of intake manifold temperatures. Low intake

manifold temperatures can cause abnormal combustion.

3. **Not** allowed: The ECM calibration with the high altitude timing algorithm (HATA) feature can be used with engines running standard pistons at altitudes over 2590 meters \[ 8500 feet \]. However, these engines will not be able to control combustion as well, and may still inducing ringing in the piston rings.

> [!warning] CAUTION · Осторожно
> The new ECM calibration with the high altitude timing algorithm (HATA) should only be used in tandem with the new high compression ratio piston or engine damage can result.

4. **Not** allowed: If the ECM calibration with the high altitude timing algorithm (HATA) feature is used on engines operating below 2590 meters \[ 8500 feet \] the engine will enter a derate state.

5. **Not** allowed: If the ECM calibration with the high altitude timing algorithm (HATA) feature is used on engines operating below 2590 meters \[ 8500 feet \] the engine will enter a derate state.

6. **Not** recommended but allowed: The new LTA circuit thermostat will be particularly effective in cold climates, and will stop the decay of intake manifold temperatures. Low intake

manifold temperatures can cause abnormal combustion.

7. **Not** allowed: If operating at an altitude lower than 3658 meters \[12,000 feet \], an engine with the high compression ratio pistons and non high altitude timing algorithm (HATA) calibration could exceed cylinder pressure limits and engine damage can result.

8. **Not** recommended but allowed: Cummins Inc. strongly recommends that the ECM calibration with the high altitude timing algorithm (HATA) feature is **not** used unless the engine has the high compression ratio pistons installed. There is also less control over cylinder pressure at all operating heights.

9. **Not** allowed:

> [!warning] CAUTION · Осторожно
> The new high compression ratio pistons are not to be used on engines operating below 2590 meters \[8500 feet\] as this will mean the engines will exceed the cylinder pressure limits, and could cause damage to the engine.

10. **Not** recommended but allowed: Cummins Inc. strongly recommends that the ECM calibration with the high altitude timing algorithm (HATA) feature is **not** used unless the engine has the high compression ratio pistons installed. There is also less control over cylinder pressure at all operating heights. The new LTA circuit thermostat can be used on engines operating at all altitudes. The new LTA circuit thermostat will be particularly effective in cold climates, and will stop the decay of intake manifold temperatures. Low intake

manifold temperatures can cause abnormal combustion

**Service Parts Availability**

Service parts are available. See Table 2 below.

| **Table 2, Service Parts** |  |  |  |
|---|---|---|---|
| **Part Description** | **Previous Part Number** | **New Part Number** | **Quantity** |
| Piston | [[3645958]] or 3640474 | 3640513 (Sold in Service Kit 4955783) | 16 per engine |
| LTA Thermostat | 4065566 | 4381506 | 2 per engine |

Nine new ECM calibrations have been released with the high altitude timing algorithm (HATA) feature and timing table changes. See Table 3 below.

- Seven of the ECM calibrations are certified for the Tier1 emissions level.
- The additional two ECM calibrations are non-certified fuel optimized calibrations. These new calibrations necessitated the release new DO, SC, and FC options for these engines.
- The correct ECM calibration, that meets the emissions level of the country the unit is operating in, **must** be installed.

| **Table 3, Engine Control Module (ECM) Calibrations and Options** |  |  |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **Existing Calibrations and Options** | **New Calibrations and Options** |  |  |  |  |  |  |  |  |  |  |
| **Previous ECM Code** | **Existing SC Option** | **Existing DO Option** | **Existing FC Option** | **FR Option** | **Certification** | **New ECM Code** | **New SC Option** | **New DO Option** | **New FC Option** | **FR Option** | **Certification** |
| D60559.02 | SC61622 | DO60786 | FCWD86 | FR60259 | Tier 1 | D60693.00 | SC61738 | DO60904 | FCWH05 | FR60259 | Tier 1 |
| D60684.01 | SC61668 | DO60831 | FCWF68 | FR60259 | D60694.00 | SC61739 | DO60905 | FCWH06 | FR60259 |  |  |
| D60685.01 | SC61689 | DO60853 | FCWF77 | FR60259 | D60695.00 | SC61740 | DO60906 | FCWH07 | FR60259 |  |  |
| D60560.02 | SC61623 | DO60787 | FCWD87 | FR60260 | D60696.00 | SC61741 | DO60907 | FCWH08 | FR60260 |  |  |
| D60676.01 | SC61660 | DO60823 | FCWF63 | FR60260 | D60697.00 | SC61742 | DO60908 | FCWH09 | FR60260 |  |  |
| D60683.01 | SC61667 | DO60830 | FCWF67 | FR60260 | D60698.00 | SC61743 | DO60909 | FCWH10 | FR60260 |  |  |
| D60686.01 | SC61690 | DO60854 | FCWF78 | FR60260 | D60699.00 | SC61744 | DO60910 | FCWH11 | FR60260 |  |  |
| D60561.02 | SC61624 | DO60789 | FCWD88 | FR60267 | Non Certified Fuel Optimised | D60700.00 | SC61745 | DO60911 | FCWH12 | FR60267 | Non Certified Fuel Optimised |
| D60562.02 | SC61625 | DO60790 | FCWD89 | FR60268 | Non Certified Fuel Optimised | D60701.00 | SC61746 | DO60912 | FCWH13 | FR60268 | Non Certified Fuel Optimised |

**Part Compatibility**

The new high compression piston and LTA thermostat are backwards compatible.

**Part Identification**

The high compression ratio piston has a shallower piston bowl when compared to the standard piston.

### Document History

## Детали, упомянутые в документе

| Артикул | Наименование | Русское название |
|---|---|---|
| [[3645958]] | Engine Piston | Поршень двигателя |
