---
type: "Сервисный бюллетень"
doc: "2883408"
title_en: "On-Board Diagnostics (OBD) for EPA/ARB Certified Engines"
released: "2013-01-21"
modified: "2013-01-29"
engines:
  - "77804793"
  - "77804810"
families:
  - "15N"
  - "A8.5"
figures: 8
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/bulletin/2883408.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/bulletin/2883408.pdf"
tags:
  - "документ/бюллетень"
  - "двигатель/15N"
  - "двигатель/A8.5"
---

# On-Board Diagnostics (OBD) for EPA/ARB Certified Engines

> [!abstract] Сервисный бюллетень · `2883408`
> **Двигатели:** [[77804793 — A8.5 CM2670 L153B CPL 6235|77804793]], [[77804810 — 15N CM2380 M104B CPL 5977|77804810]]
> **Семейство:** 15N, A8.5
> **Даты:** выпущен 2013-01-21 · изменён 2013-01-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/bulletin/2883408.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/bulletin/2883408.pdf)

## On-Board Diagnostics (OBD) for EPA/ARB Certified Engines

This service bulletin contains information regarding Heavy Duty On-Board Diagnostics (HD-OBD) for Cummins® engines. Heavy Duty On-Board Diagnostics (HD-OBD) is an Environmental Protection Agency / Air Resources Board (EPA/ARB) certification requirement for engines equipped in vehicles with gross vehicle weight rating (GVWR) \> 14,000 lb. The purpose of this bulletin is to define common OBD terms and explain the proper troubleshooting and fault code clearing strategies.This service bulletin is specific to HD-OBD certified Cummins® engines. This bulletin does **not** apply to OBDII or E-OBD certified vehicles/engines.

What is OBD?

OBD is a government-mandated standard that requires engines to actively monitor and test emissions-related components and systems to detect malfunctions that adversely affect emissions. An engine's OBD system monitors nearly every component that can affect the emission control system. If the OBD system detects a malfunction that could cause an increase in exhaust emission levels, the OBD system illuminates the malfunction indicator lamp (MIL) on the vehicle instrument panel to alert the operator that the engine is in need of repair. The level of OBD monitoring required can vary, depending on factors such as gross vehicle weight rating (GVWR), model year, certification level, and applicable government regulations.

OBD Terminology

To properly troubleshoot and diagnose HD-OBD equipped engine systems, it is important to understand the following terms:

- Fault Code (FC): A code reported and stored by the engine control module (ECM) which indicates that a particular malfunction or abnormal condition has been detected. Different failure modes cause different fault codes to be stored, which provides direction for the appropriate troubleshooting and repair. Fault codes can be read by connecting to the ECM with a scan tool, such as INSITE™ electronic service tool. Fault codes can be referred to within OBD terminology as a diagnostic trouble code (DTC).
- Malfunction Indicator Lamp (MIL): A dash lamp that illuminates and alerts the operator when an OBD fault code becomes ”Active”, indicating an engine malfunction that could impact emissions.
- OBD Diagnostic: A test or series of tests which are run by the engine ECM and are designed to determine the operational status of a specific emissions-related component or subsystem. OBD-equipped engines have multiple OBD diagnostics that run under certain operating conditions. These diagnostics test their respective systems and store or report the results accordingly. It is sometimes referred to within OBD terminology as a “monitor”.
- Continuous Diagnostic: A diagnostic that runs continuously during normal engine operation. It records a fault code and illuminates the MIL immediately after the diagnostic runs and does **not** pass.
- Non-Continuous Diagnostic: A diagnostic that runs **only** under certain enabling conditions. A non-continuous diagnostic may run every time certain operating or environmental conditions are met, or once per trip.
- Trip: Also known as a “drive cycle”. A specific series of steps or set of conditions that a vehicle **must** be operated under to enable a specific diagnostic to run. This can be part of the process required to clear certain OBD fault codes. Trip conditions are stated in the troubleshooting tree for the applicable fault code.
- OBD 1-Trip Fault: A fault code that is set to ”Active” and illuminates the MIL after the corresponding diagnostic for the fault code runs and does **not** pass once per trip.
- OBD Multi-Trip Fault: A fault code that is set to ”Active” and illuminates the MIL after the corresponding diagnostic for the fault code runs and does **not** pass during multiple consecutive trips. For example, an OBD 2-Trip fault will illuminate the MIL after the corresponding diagnostic runs and does **not** pass during two consecutive trips.
- Cold Soak: A portion of certain drive cycles in which a vehicle **must** sit for a minimum amount of time (8 to 10 hours) with the engine OFF. This allows all temperature sensors to equalize at ambient temperature.
- Derate: An action, caused by certain fault codes, that decreases available engine power. This is done to protect the engine from damage and/or help initiate a service event. Some derates occur immediately, while others occur after a certain amount of time since a fault became ”Active”. Once the repair is made and the fault goes ”Inactive”, the engine will no longer be derated.

Lamps

Not all fault codes have the potential to impact emissions. Therefore, HD-OBD equipped engines can have both OBD and non-OBD fault codes. Typically, non-OBD fault codes illuminate either the amber warning lamp (AWL) or red stop lamp (RSL), which are the traditional Cummins Inc. dash lamps. OBD faults always illuminate the MIL, and in some cases the AWL or RSL are illuminated as well. Refer to the original equipment manufacturer (OEM) service manual for specific details about each dash lamp.

Malfunction Indicator Lamp

The malfunction indicator lamp is amber (yellow) in color and is the image of an engine.

![[11c00253.png]]

Amber Warning Lamp

The AWL is amber (yellow) in color and can either be the image of an engine featuring a wrench or can be the text: “Check” or “Check Engine”. The AWL is used to indicate a non-OBD fault code is active or a maintenance condition exists.

![[19c01777.png]]

![[19c01778.png]]

Red Stop Lamp

The RSL is red in color and can either be the image of an engine featuring an exclamation point, the outline of a STOP sign featuring the engine, or the text “Stop” or “Stop Engine”. The RSL is used to indicate an engine protection fault code or engine protection condition exists.

![[11c00254.png]]

![[19c01780.png]]

Troubleshooting OBD Fault Codes

The preferred strategy for troubleshooting OBD fault codes is the same as for traditional Cummins® fault codes: troubleshooting based on the Cummins® fault status, as displayed in the ”Fault Codes” INSITE™ electronic service tool screen. The ”OBD Fault Codes” and ”OBD Monitors” INSITE™ electronic service tool screens are **not** used on EPA 2010 or EPA 2013 OBD certified engines.

During the troubleshooting process, the appropriate fault code troubleshooting tree for each fault code **must** be referred to in order to complete the repair. The troubleshooting trees can be found in the applicable Fault Code Troubleshooting Manual. **Not all** fault codes require the replacement of parts to complete the repair. Follow the troubleshooting tree carefully and **only** replace damaged parts when instructed. Once a repair is made, the troubleshooting tree provides instructions on how to get the diagnostic to complete a drive cycle or trip in order to validate the repair. If the repair was successful, the Cummins® fault code status (which can be monitored in the INSITE™ electronic service tool “Fault Codes” screen) will become ”Inactive” once the diagnostic runs and passes. The troubleshooting process should be done for each fault code present in the ECM.

Extinguishing the MIL

OBD fault codes require three drive cycles or trips to extinguish the MIL. The fault codes go “Inactive” after the diagnostic runs and passes once, but the MIL stays on until two additional drive cycles or trips are completed in which the diagnostic runs and passes. When one drive cycle has been completed and the fault code is “Inactive”, the repair has been validated, and the “Inactive” fault code can be cleared with INSITE™ electronic service tool “Reset All Faults” option. This extinguishes the appropriate dash lamps. If the “Inactive” fault code is **not** cleared with INSITE™ electronic service tool “Reset All Faults” option, the MIL will stay on until the diagnostic has run and passed on two additional drive cycles (three drive cycles total).

The troubleshooting trees provide important information, such as how the fault code is set, what **must** be done to get the diagnostic to run, and how many drive cycles are required to turn the MIL off. For many fault codes, a drive cycle can be completed by starting the engine, letting it idle for 1 minute, and shutting it down. However, some fault codes may require that the vehicle be driven, operated on a chassis dynamometer, or forced to perform a stationary regeneration in order to get the diagnostic to run and make the fault code go “Inactive”. Reference the “Conditions for Clearing the Fault Code“ section of the fault code troubleshooting in order to determine the appropriate operating conditions to verify the repair.

OBD Fault Code Functionality

![[19c01781.png]]

The illustration shows the different ways that OBD fault codes are set to ”Active” and the MIL is turned on:

![[19c01782.png]]

The illustration shows the different ways that OBD fault codes are set to ”Active” and the MIL is turned on:

![[19c01784.png]]

The illustration shows the different ways that OBD fault codes are cleared and how the MIL is turned off:

### Document History
