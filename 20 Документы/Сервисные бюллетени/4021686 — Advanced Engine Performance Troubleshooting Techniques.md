---
aliases:
  - "Углублённые методы диагностики мощностных характеристик"
type: "Сервисный бюллетень"
doc: "4021686"
title_en: "Advanced Engine Performance Troubleshooting Techniques"
title_ru: "Углублённые методы диагностики мощностных характеристик"
released: "2010-10-11"
modified: "2022-04-21"
group: "14 - Engine Testing"
engines:
  - "33239746"
  - "33239899"
  - "37292556"
  - "37295879"
  - "41349633"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
  - "QSK19"
  - "QST30"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/bulletin/4021686.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/bulletin/4021686.pdf"
tags:
  - "документ/бюллетень"
  - "двигатель/K38/K50"
  - "двигатель/QSK19"
  - "двигатель/QST30"
  - "тема/engine-testing"
---

# Advanced Engine Performance Troubleshooting Techniques
**Углублённые методы диагностики мощностных характеристик**

> [!abstract] Сервисный бюллетень · `4021686`
> **Раздел Cummins:** 14 - Engine Testing
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]], [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]], [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60, QSK19, QST30
> **Даты:** выпущен 2010-10-11 · изменён 2022-04-21
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/bulletin/4021686.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/bulletin/4021686.pdf)

## Advanced Engine Performance Troubleshooting Techniques

## Introduction

This Service Bulletin provides advanced techniques for troubleshooting engine performance complaints such as low power, poor acceleration, and engine derates. A derate is defined as any condition where the electronic control module (ECM) intentionally reduces power output to protect the engine from damage. A simple example of a derate would be when the ECM detects high coolant temperature. The ECM will derate, or reduce, the torque output to protect the engine from damage. Sometimes these derates do **not** log fault codes, making performance complaints difficult to troubleshoot.

INSITE™ electronic service tool has provided a monitor parameter called “User Fueling State” for all engine applications released since 1995. This monitor parameter may also be called “Engine Operating State” on newer engine applications. This parameter indicates, in real-time, what governor, system, or derate is presently controlling the engine, and can be monitored using INSITE™ electronic service tool Data Monitor/Logger feature. Many of the parameters indicate normal operation, but others can help isolate causes of poor engine performance. Examples include:

- If the engine is idling, User Fueling State (Engine Operating State) indicates “Low Speed Governor”.
- If the engine is operating with an engine protection fault code, User Fueling State (Engine Operating State) indicates “Engine Protection”.
- If the engine is operating at high altitude, User Fueling State (Engine Operating State) indicates “Altitude Derate”.
- If the engine is operating at full power on the torque curve, User Fueling State (Engine Operating State) indicates “Maximum Throttle”.
- If a boost leak occurs and the engine can **not** get enough oxygen (boost pressure) for proper combustion, User Fueling State (Engine Operating State) indicates “Air Fuel Control Derate”.

This Service Bulletin lists all of the various states that can be displayed for the User Fueling State (Engine Operating State) parameter, a brief description of each state, and the ECM response when the state is active. Advanced techniques for troubleshooting engine performance complaints, using the User Fueling State (Engine Operating State) parameter, are also discussed in this Service Bulletin. The following advanced troubleshooting techniques will be discussed:

- Low Power Troubleshooting
- Poor Response or Slow Acceleration
- Typical User Fueling States During Acceleration
- No-Start Conditions
- Cruise Control or Power Take Off (PTO) Dropout
- Intermittent Derates or Loss of Power
- Automatic Transmission J1939 Messages.

## Troubleshooting Using the User Fueling State (Engine Operating State) Monitor Parameter

The parameter named 'User Fueling State' (Engine Operating State) in INSITE™ electronic service tool Monitor List is very powerful when troubleshooting performance related issues. This parameter displays what engine state is presently controlling the engine. There can be up to 50 different states that can potentially control the engine at any given time, but typically **only** 15 to 20 states will activate during normal operation.

Use INSITE™ electronic service tool to monitor the parameter 'User Fueling State' (Engine Operating State) at the same engine operating conditions where the engine performance symptom occurs.

## User Fueling States (Engine Operating States) that Indicate Normal Operation

The following User Fueling States (Engine Operating State) will occur during normal engine operation. These operating states, by themselves, do **not** indicate a problem with the engine, but can give clues to the cause of a performance complaint.

- Air Density Limit - The engine is presently being derated for high altitude conditions.
- Air Fuel Control Derate - The engine fueling is being limited due to lack of oxygen (boost pressure). This state will be active for a few seconds during hard accelerations to prevent excessive black smoke. This state can also be active for excessively high boost pressure.
- All Speed Governor - The engine is operating on the all speed governor. This is a normal state when the throttle position is greater than 0 percent, the engine is **not** operating on the torque curve, and the All Speed Governor feature is enabled.
- Automotive Governor - The engine is operating on the automotive governor. This is a normal state when the throttle position is greater than 0 percent, the engine is not operating on the torque curve, and the Automotive Governor feature is active.
- Crank - The engine is in the cranking state.
- Cruise Control - The vehicle speed is being controlled by the Cruise Control feature.
- Data Link Speed - The engine speed is being speed controlled by a J1939 device such as an automatic transmission. This will typically be active when an automatic or automated transmission is controlling the engine during a gear shift, in order to synchronize the engine speed with the transmission.
- Data Link Torque - The engine torque is being controlled by a J1939 device, such as an automatic transmission. This will typically be active when an automatic or automated transmission is controlling the engine during a gear shift.
- EGR Fueling Limit - The engine is operating at the maximum torque output. This state indicates the engine is operating on the torque curve and maximum fueling is being achieved.
- Engine Brake - The engine brakes are active and engaged.
- Engine Stop - The vehicle keyswitch is ON and the engine is **not** operating.
- Fuel System Derate - A fuel system related fault code is active.
- Fueling High Speed Governor - The engine is operating on the high speed governor. This indicates that the engine speed is at the maximum rpm for the given engine rating.
- Low Speed Governor - The engine is operating on the low speed governor. This state should always be active when the throttle is released and the engine is idling.
- Maximum Throttle - The engine is operating at the maximum torque output. This state indicates the engine is operating on the torque curve and maximum fueling is being achieved.
- Noise Control Derate - The engine timing is being adjusted to limit the engine noise during acceleration.
- PTO - Engine speed is being controlled by the PTO.
- Road Speed Governor - The vehicle's road speed is presently being limited by the Road Speed Governor setting.
- Shutdown - The vehicle keyswitch is turned OFF and the engine is in the process of stopping.
- Turbocharger Fuel Control - The engine torque output has been limited to reduce the engine exhaust temperature.
- Vehicle Speed Sensor Diagnostic - The engine speed is limited by the Maximum Engine Speed without VSS feature.

## User Fueling States (Engine Operating States) that May Cause Engine Derates

> [!note] Note · Примечание
> For every 305 m \[1000 ft\] increase in elevation, you can expect power to decrease by approximately 3.5 percent.

- Air Density Limit - The engine torque output is being limited for high altitude conditions.
- Air Fuel Control Derate - The engine fueling is being limited due to lack of oxygen (boost pressure). This state can also be active for excessive boost pressure.
- Altitude Derate - The engine torque output is being limited for high altitude conditions.
- Ambient Derate - The engine torque output is being limited due to high altitude operating conditions of the engine.
- Coolant Derate - The engine torque output is being limited to reduce the coolant temperature.
- Data Link Torque Derate - The engine torque output is being limited by a J1939 device.
- Engine Overspeed - The engine is operating in an overspeed condition.
- Engine Protection - The engine torque output is being limited for engine protection.
- Engine Protection Derate - The engine torque output is being limited for engine protection.
- Fuel System Derate - A fuel system related fault code is active.
- Noise Control Derate - The engine torque output is being limited to lower the noise output of the engine.
- Road Speed Governor - The vehicle is at the maximum programmable vehicle speed.
- Turbocharger Fuel Control - The engine torque output is being limited to reduce turbocharger turbine inlet temperature.

## Engine Torque Mode States

- Low Idle Governor/No Request (Default mode) - This is the default mode. Active if accelerator pedal is zero.
- Accelerator Pedal - Active if accelerator pedal position is active (being followed). Mode is active for retarder if turned on by operator. May be disabled by accelerator pedal or clutch switches (operator selection).
- Cruise Control - Active if cruise control is active and greater than accelerator pedal request.
- PTO Governor - Active if PTO governor is active.
- Road Speed Governing - Indicates road speed governing is active and limiting torque.
- ASR (Anti-Slip Regulation) Control - Indicates ASR command is active (Speed, Torque, or Speed/Torque Limit Control).
- Transmission Control - Indicates transmission command is active (Speed, Torque, or Speed/Torque Limit Control).
- ABS Control - Indicates ABS is controlling torque.
- Torque Limiting - Active if demanded or commanded engine torque is limited by internal logic due to full load, smoke and/or emissions control, engine protection and/or other factors. A reduced torque limit may be necessary for engine protection if engine temperature is too high or a sensor malfunctions (speed, timing, or boost pressure), as examples.
- High Speed Governor - Active if engine is controlled by high speed governor due to normal operation.
- Brake System (Electronic) - Indicates brake pedal is controlling torque. Note that this may include enabling of retarder when brake pedal is depressed (touched).
- Remote Accelerator - Active if remote accelerator is controlling engine speed.
- Service procedure - Active if engine is operating in a specific service mode. For example, fuel injection may be disabled to allow a service procedure to crank engine without fuel injection occurring.
- Other - Torque control by a type of device which is different than those defined in Low Idle Governor/No request (default mode) and Transmission Control.

## Troubleshooting Techniques

The User Fueling State (Engine Operating State) parameter can be used to troubleshoot “hard to diagnose” performance complaints. The following examples show how to use this parameter to troubleshoot various engine symptoms.

## Low Power Troubleshooting

When operating a vehicle on a chassis dynamometer or operating under fully loaded conditions, the User Fueling State (Engine Operating State) parameter **must** indicate Maximum Throttle or EGR Fueling Limit State when operating under peak torque conditions. If these states are active during maximum torque conditions (100 percent throttle operation and the engine is fully loaded and operating on the torque curve), this indicates that the air handling system is providing the desired boost pressure and no derates are presently active. If a performance complaint still exists, follow the engine performance troubleshooting tree to isolate the potential cause of the low power complaint.

If the User Fueling State (Engine Operating State) reads Air Fuel Control Derate for an extended period of time (greater than 10 seconds) during a hard acceleration or during normal operation, troubleshoot the turbocharger and air handling system. Air Fuel Control Derate indicates that there is **not** enough oxygen (boost pressure) entering the engine for complete combustion. The electronic control system then limits the amount of fuel being injected, to prevent excessive black smoke. Air Fuel Control Derate will be active for a few seconds during hard accelerations. It should **not** be active under steady state operating conditions. Failure modes that can cause excessive time operating in the Air Fuel Control Derate state include charge-air cooler leaks, charge-air cooler plumbing leaks, VGT turbochargers **not** meeting commanded position, a malfunctioning in-range intake manifold pressure sensor, a malfunctioning in-range ambient air pressure sensor, air intake restrictions, excessive exhaust restriction, worn or malfunctioning turbocharger, malfunctioning fuel injectors, and fuel system restrictions. To isolate the potential cause of the low power complaint, see the engine performance troubleshooting tree.

> [!note] Note · Примечание
> For every 305 m \[1000 ft\] increase in elevation, you can expect power to decrease by approximately 3.5 percent.

## Poor Response or Slow Acceleration

Operate the vehicle in the same conditions where the poor response condition is active. When accelerating from a stop, the User Fueling State (Engine Operating State) will initially indicate Automotive Governor. Under hard accelerations, the User Fueling State (Engine Operating State) will indicate Air Fuel Control Derate, until the boost pressure is high enough to allow maximum fueling. The state should then transition to Maximum Throttle or EGR Fueling Limit State, when the engine is operating under full load conditions.

If the vehicle speed is being limited by the Road Speed Governor, the User Fueling State (Engine Operating State) will indicate Road Speed Governor State. This indicates that the vehicle speed has been limited by the Maximum Vehicle Speed feature. Check the adjustable parameter settings for tire size, rear axle ratio, transmission tailshaft gear teeth, and maximum vehicle speed.

> [!note] Note · Примечание
> For every 305 m \[1000 ft\] increase in elevation, you can expect power to decrease by approximately 3.5 percent.

## Intermittent Engine Shutdown

The User Fueling State (Engine Operating State) parameter can be used to troubleshoot intermittent keyswitch and engine dying problems. When the keyswitch is turned OFF, the User Fueling State (Engine Operating State) will indicate Shutdown. As soon as engine speed and turbocharger speed reaches 0, the state will change to Engine Stop. An intermittent keyswitch problem will cause the User Fueling State (Engine Operating State) to indicate Shutdown.

## No Start Conditions

While cranking the engine during a no-start condition, the User Fueling State (Engine Operating State) should read Crank State. This indicates that the engine speed sensors are correctly receiving an engine speed signal and that the fuel system is correctly fueling the engine. If the User Fueling State (Engine Operating State) indicates Engine Stop during cranking, the engine speed signal is **not** being received by the ECM. Troubleshoot the engine speed signal.

## Cruise Control or PTO Dropout

When troubleshooting intermittent cruise control or PTO dropout problems, the User Fueling State (Engine Operating State) parameter can be used to indicate when the dropout is occurring. When the vehicle is operating in cruise control, the User Fueling State (Engine Operating State) will display 'Cruise Control'. When the cruise control is disabled or drops out during vehicle operation, the User Fueling State (Engine Operating State) will change from Cruise Control to Automotive Governor (or the present state that is controlling the engine). At the point where this transition occurs, other parameters, like brake switch and cruise control switch, can be investigated as causing the dropout problem.

## Intermittent Derates or Loss of Power

There are various power derates that can become active during extreme environmental operating conditions. Engines built in 2002 and later will log fault codes for these conditions, but it is possible for a derate to be active without a fault code. Confirm these User Fueling States (Engine Operating States) are **not** active under normal operating conditions:

- Air Density Limit - This state will be active if the vehicle is being operated in a high altitude condition. Confirm the altitude of the vehicle and verify correct ambient air pressure sensor operation. Engines built in 2002 and later will activate a fault code under these conditions.
- Turbocharger Fuel Control - Under extreme operating conditions, the engine will limit fueling to prevent turbocharger damage due to high turbine inlet temperatures. By reducing the torque output of the engine, exhaust temperatures are reduced. This state should **only** be active during hard accelerations. Confirm the altitude of the vehicle and verify correct ambient air pressure sensor operation. Engines built in 2002 and later will activate a fault code under these conditions.
- Vehicle Acceleration Management - Engine acceleration is being limited by the Acceleration Management feature.

## Automatic Transmission J1939 Messages

New automatic and automated manual transmissions will control engine speed and engine torque output during transmission shifting events. These J1939 commands are used to synchronize the engine and transmission for gear selection. Common User Fueling States (Engine Operating States) include Data Link Torque Derate, Data Link Torque, or Data Link Speed. The transmission will send a message via the J1939 data link to control the engine. These are normal events that might appear active during shifting and should **only** be active for very short periods of time.

## System Descriptions

The following list provides the system descriptions of each state that can be displayed in INSITE™ electronic service tool for the User Fueling State (Engine Operating States) parameter.

- Aftertreatment Regeneration Active - The engine is performing a regeneration of the diesel particulate filter.
- Air Density Limit - The engine is presently being derated for high altitude conditions.
- Air Fuel Control Derate - The engine fueling is being limited due to lack of oxygen (boost pressure). This state will normally be active for a few seconds during a hard acceleration. Excessive time operating in this state indicates the lack of oxygen (boost pressure) entering the engine.
- All Speed Accelerator - The All Speed Governor is controlling the engine speed. This is a normal state when the throttle pedal is depressed and the all speed governor is enabled.
- All Speed Governor Application - The industrial All Speed Governor is controlling engine speed. This is a normal state when the all speed governor is enabled.
- Alternate Torque - The industrial alternate torque feature is presently active.
- Alternator Failure Warning - The Alternator Failure Warning feature is active.
- Altitude Derate - The engine torque output is being limited due to high altitude conditions.
- Ambient Derate State - The engine torque output is being limited due to high altitude conditions.
- Anti-Theft Derate - An anti-theft device is presently derating the engine.
- Automotive Governor - The Automotive Throttle is controlling the engine speed. This is a normal state when the throttle pedal is depressed and the automotive governor is enabled.
- Charge Manager State - The ECM is limiting the amount of charge pressure to protect the air handling system.
- Coolant Derate State - The engine torque output is being limited due to high coolant temperature.
- Crank State - The engine is cranking and is in the process of starting.
- Cruise Control - The vehicle is presently operating with the cruise control feature active.
- Data Link Powertrain Protection State - The engine's torque output is presently limited by the Powertrain Protection feature.
- Data Link Speed - The engine speed is being controlled by a J1939 device, such as an automatic transmission.
- Data Link Torque - The engine torque output is being controlled by a J1939 device, such as an automatic transmission.
- Data Link Torque Derate - The engine torque output is being controlled by a J1939 device.
- EGR Fueling Limit State - The engine is presently operating on the torque curve and maximum fueling.
- Engine Brake - The engine brakes are presently activated.
- Engine Overspeed - The engine speed has exceeded the overspeed limit set in the calibration.
- Engine Protection - The engine torque output is presently limited by an engine protection state.
- Engine Protection Derate - The engine is presently being derated by an engine protection state.
- Engine Startup Oil Limit - The engine startup protection feature is limiting throttle control until oil pressure is reached. This is normal operation at startup until operating oil pressure is reached.
- Engine Stop - The keyswitch is turned ON and the engine is **not** operating.
- Engine Warm-up Protection - The engine torque and speed is limited by the engine warm-up protection feature. This state should **only** be active until sufficient oil pressure is available to the engine.
- Fast Idle Warm-up - The Fast Idle Warm-up feature is active.
- Fast Idle Warm-up Ramp - The Fast Idle Warm-up feature is active and ramping engine speed.
- Firetruck Governor - The firetruck governor is controlling engine.
- Fuel System Derate - A fuel system fault code is active and is presently limiting the engine torque and/or speed output.
- Fueling High Speed Governor State - The engine is operating at the maximum engine speed.
- Fueling Override State - For engineering use **only**.
- High Fuel Temperature Engine Protection - The engine torque output is being limited due to high fuel temperature.
- Industrial Auxiliary Governor - The Industrial Auxiliary Governor is controlling engine speed.
- Industrial Engine Speed Cruise Control - The industrial engine speed cruise control feature is active.
- Limp Home - A throttle pedal fault code is presently active.
- Load Based Speed Control - The Load Based Speed Control feature is active. The load based speed control feature is active. This will limit the maximum operating speed of the engine under low load conditions while allowing the engine full engine speed range under high load and out of gear conditions.
- Low Gear - For engineering use **only**.
- Low Speed Governor State - The engine is presently idling on the low speed governor. The throttle pedal is released, the vehicle is stationary, and the engine is idling.
- Maximum Throttle - The engine is presently operating on the torque curve and maximum fueling.
- Momentary Engine Override - The engine speed is being momentarily overridden by a device such as an automatic transmission.
- No Torque Derate - For engineering use **only**.
- Noise Control Derate - The injection timing is being adjusted to reduce engine noise.
- None - For engineering use **only**.
- OBD Fueling Derate - An On-Board Diagnostics system fault is active and is currently limiting the engine torque and/or speed output.
- Out Of Gear - The ECM has detected the transmission is in neutral or the clutch has been disengaged.
- Override - For engineering use **only**.
- Partial Throttle Limit State - The industrial hybrid governor is controlling engine.
- Powertrain Protection Derate - The engine's torque output is presently limited by the Powertrain Protection feature.
- Primary/Secondary - The Multi-Unit Synchronization feature is active. This is an industrial feature.
- Progressive Shift Speed - For engineering use **only**.
- PTO - The engine is presently operating in PTO mode.
- PTO Derate - The engine torque output is limited in PTO mode.
- Road Speed Governor - The vehicle's maximum speed is presently being limited by the Road Speed Governor setting.
- Setup for Dynamometer - The electronic control system has been configured so that engine performance testing can be done on a dynamometer without restrictions on Engine Speed, Power and Torque.
- Shutdown - The engine is in the process of being shut down. The keyswitch has been turned off, but engine speed has **not** yet reached 0 rpm.
- Top2 Derate - The engine torque is limited by the Eaton® Top 2 transmission.
- Top2 Speed - The engine speed is limited by the Eaton® Top 2 transmission.
- Top2 Torque - The engine torque is limited by the Eaton® Top 2 transmission.
- Torque Control - For engineering use **only**.
- Torque Derate Override- For engineering use **only**.
- Torque Rate Limit - A fuel system fault is active and is currently limiting the engine torque and/or speed output.
- Turbocharger Fuel Control State - The engine torque output has been limited to reduce the engine exhaust temperature.
- Turbocharger Speed Derate - The engine torque output has been limited to reduce the turbocharger speed.
- Turbocharger Surge Limit - The turbocharger surge limit has been exceeded. This may cause a turbocharger speed derate.
- User Command - For engineering use **only**.
- Vehicle Acceleration Management State - The vehicle acceleration rate is being limited by the Acceleration Management feature.
- Vehicle Speed Sensor Diagnostic - The engine speed is limited by the Maximum Engine Speed without Vehicle Speed Sensor feature.

### Document History
