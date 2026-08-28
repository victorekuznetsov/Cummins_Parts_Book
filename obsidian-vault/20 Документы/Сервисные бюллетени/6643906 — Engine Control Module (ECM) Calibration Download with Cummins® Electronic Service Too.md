---
type: "Сервисный бюллетень"
doc: "6643906"
title_en: "Engine Control Module (ECM) Calibration Download with Cummins® Electronic Service Tools"
released: "2025-07-22"
modified: "2025-08-08"
engines:
  - "77804793"
  - "77804810"
families:
  - "15N"
  - "A8.5"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/bulletin/6643906.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/bulletin/6643906.pdf"
tags:
  - "документ/бюллетень"
  - "двигатель/15N"
  - "двигатель/A8.5"
---

# Engine Control Module (ECM) Calibration Download with Cummins® Electronic Service Tools

> [!abstract] Сервисный бюллетень · `6643906`
> **Двигатели:** [[77804793 — A8.5 CM2670 L153B CPL 6235|77804793]], [[77804810 — 15N CM2380 M104B CPL 5977|77804810]]
> **Семейство:** 15N, A8.5
> **Даты:** выпущен 2025-07-22 · изменён 2025-08-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/bulletin/6643906.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/bulletin/6643906.pdf)

## Engine Control Module (ECM) Calibration Download with Cummins ® Electronic Service Tools

**Product Affected**

- Engines with managed calibration transfers will be identified by the service tool

**Introduction**

This document introduces changes to engine control module (ECM) calibration transfers with Cummins® electronic service tools for products that calibration transfers are managed by the service calibration management (SCM) process.

**Overview**

Beginning with Guidanz Diagnostic Tool Kit (DTK) mobile version 7.3/Windows version 3.3 and INSITE™ electronic service tool version 9.2 which is scheduled for release in August 2025, the service calibration management (SCM) will begin to manage calibration installs to the ECM. The SCM is a process the Cummins® electronic service tool uses to determine the correct calibration and provides the authorization for the calibration install to the ECM. The SCM uses various sources of data to determine the correct ECM calibration for a particular engine serial number (ESN) see Figure 1.

![[00r01911.png]]

Figure 1, SCM Flow Schematic.

1. Dataplate Uprate

2. Field Test

3. SCM

4. Manufacturing Plant

5. Field Action

The Cummins® electronic service tool will require internet connection as well as the ESN to allow SCM to provide authorization for the ECM calibration install. If internet connection is **not** available at the job site, an offline process is available, however the SCM **must** provide authorization while connected to the internet before arriving at the job site to install the ECM calibration to the ECM. A revision update to the ECM base code will **always** be authorized regardless of internet connection. The Cummins® electronic service tool collects data for every ECM calibration transfer to the ECM.

Most ECM calibration transfers to the ECM are ECM base code revision updates. For the repairs that require an ECM base code change the reason for the change **must** be entered. Causes for ECM base code changes are:

- Campaign
- Temporary Repair Practices (TRP)
- Account Team Coverage (ATC)
- Uprate
- Technical Service Bulletins (TSBs)
- New/SEEDED Module

When obtaining SCM authorization for Campaign, TRP, ATC or TSB the letter will be prepopulated only the number **must** be entered.

If an uprate is being performed product modification procedure 111-513-007 Product Modification **must** be followed including request for a new engine dataplate. SCM will only authorize the ECM calibration transfer after these steps are completed.

Fleetcount or CalAssists are no longer required when changing the ECM base code.

The following items have been created or updated to provide additional training and information on SCM and ECM calibration installs:

- Training course 1629 – Cummins Service Calibration Management has been created to provide further detail on SCM.
- News article Cummins Electronic Service Tools – Calibration Download Changes

> [!note] Note · Примечание
> [https://quickserve.cummins.com/qs3/qsol/news/back\_office\_changes.html](https://quickserve.cummins.com/qs3/qsol/news/back_office_changes.html)

### Document History
