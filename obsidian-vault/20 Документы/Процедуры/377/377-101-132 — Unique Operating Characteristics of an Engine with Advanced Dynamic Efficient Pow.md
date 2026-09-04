---
type: "Процедура"
doc: "377-101-132"
title_en: "Unique Operating Characteristics of an Engine with Advanced Dynamic Efficient Powertrain Technology (ADEPT™ Electronic Features)"
modified: "2020-02-10"
manuals:
  - "5411182"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/377/377-101-132.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/377-101-132.pdf"
tags:
  - "документ/процедура"
  - "группа/377"
---

# Unique Operating Characteristics of an Engine with Advanced Dynamic Efficient Powertrain Technology (ADEPT™ Electronic Features)

> [!abstract] Процедура · `377-101-132`
> **Входит в руководства:** [[5411182 — X15 CM2350 X114B - Efficiency Series Operation and Maintenance Manual|5411182]]
> **Секции:** Section 1 - Operating Instructions
> **Даты:** изменён 2020-02-10
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/377/377-101-132.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/377-101-132.pdf)

### General Information

The Advanced Dynamic Efficient Powertrain Technology (ADEPT™) suite of advanced electronic features provides vehicle controls to help drivers operate vehicles in a fuel-efficient manner while maintaining the desired level of productivity and performance. The ADEPT™ features will make minor adjustments to vehicle speed, engine power and driveline conditions to take advantage of vehicle momentum and knowledge of upcoming route attributes in order to achieve a more fuel efficient vehicle operation.

Features are divided into seven groups:

- Load Based Torque Control
- SmartCoast
- Predictive Shifting
- Predictive Engine Braking
- On-ramp Boost
- Predictive Cruise Control
- Predictive Road Speed Governor

Each of the individual ADEPT™ features can be disabled or adjusted to fit customer preferences using INSITE™ electronic service tool.

### Feature Description

Load Based Torque Control Feature

The Load Based Torque Control Feature is designed to provide the engine torque required to maintain the vehicle operating conditions to optimize fuel economy.

There are currently three types of Load Based Torque Control:

- Base
- SmartTorque
- SmartTorque2

The Base type is defined by the torque rating installed. A straight torque rating allows full torque for all vehicle operating conditions. The SmartTorque rating allows full torque in **only** the top two gears.

The default values provided in the calibration are recommended for the most fuel efficient operation and set at the factory. The Load Based Torque Control type parameter can be adjusted with the proper programming tools such as INSITE™ electronic service tool.

SmartTorque2 expands upon the current SmartTorque feature of limiting engine torque when operating in gears below the top two. The expanded functionality of SmartTorque2 utilizes an estimated vehicle weight and road grade to limit the available torque to what is needed to maintain the operating condition for that weight and road grade condition. This results in more efficient engine operation by limiting the use of excessive torque when it is **not** required.

SmartCoast™ Feature

The SmartCoast™ feature works in conjunction with an Eaton™ automated manual transmission to disengage the driveline when the vehicle operating conditions are such that the engine provided positive torque is **not** needed to maintain the target vehicle speed. By taking advantage of vehicle momentum, SmartCoast™ operation can significantly improve vehicle fuel economy, depending on the road grades traversed.

SmartCoast™ disengages the driveline when the vehicle is on a slight downhill grade and there is no other need for the driveline to be engaged. This can occur when cruise control is active, or when cruise control is inactive and either the road speed governor is used or when the operator has released the accelerator pedal.

When the Cruise Control Operating Mode is used and the vehicle speed exceeds the cruise control set speed plus the cruise control lower droop speed, the transmission will automatically reengage the driveline to allow the engine to maintain the cruise control set speed plus the lower droop speed. The driveline will also reengage with any action that causes the deactivation of Cruise Control.

When the Accelerator Control Operating Mode is used and the vehicle has exceeded the Road Speed Governor Maximum Vehicle Speed or the Maximum Vehicle Speed Control Start Maximum Engine Braking Speed, the driveline will automatically re-engage the driveline to allow the engine to maintain vehicle speed. The driveline will also re-engage with any action to engage the engine brakes or service brakes.

While SmartCoast™ is active the engine will either operate at its programmed low idle speed or operate at the SmartCoast™ specific idle speed if that feature is enabled. The default is for the engine to run at 500 rpm during SmartCoast™. The engine speed will smoothly return to the proper operating speed as the driveline is reengaged at the appropriate transmission gear.

> [!note] Note · Примечание
> This feature will work **only** on specific engine and transmission combinations. Contact a local Cummins® distributor for more details.

Predictive Gear Shifting Feature

Predictive Gear Shifting improves vehicle speed tracking performance during cruise control using knowledge of the upcoming road grade. The feature will select the optimum gear to allow the vehicle to maintain cruise control reference speed tracking on hills where the power available from the engine is limited as compared to power requirements, while minimizing fuel economy impact.

The feature is **only** available when used in conjunction with Cummins® Route Parameter Manager or an original equipment manufacturer (OEM) Predictive Cruise Control System and will utilize vehicle characteristics and road grade profile information to determine the proper transmission gear when the engine is power limited on hills.

Predictive Engine Braking Feature

Predictive Engine Braking aims to enhance the vehicle speed limiting capability of existing engine brake features based on the upcoming road grade. The features to which this predictive functionality can apply are Cruise Control and Engine Brake Interaction or Maximum Vehicle Speed Control.

Predictive Engine Braking will select the appropriate transmission gear to allow the engine brakes to generate enough power for the upcoming road terrain. The feature can also activate the engine brakes up to 3 mph below the speed at which engine brakes would normally activate as needed for the upcoming terrain. The feature uses both the Start Minimum Engine Braking and Start Maximum Engine Braking vehicle speed values which are configured by Cruise Control and Engine Brake Interaction or Maximum Vehicle Speed Control. If both features are being used, Predictive Engine Braking will apply to the lower of the speed values. It also requires that these features can access full braking power. If the operator is overriding either of these features with the accelerator pedal or engine brake switch, Predictive Engine Braking will **not** activate. See the details of these individual features for more information.

> [!note] Note · Примечание
> Cummins® Route Parameter Manager or OEM Predictive Cruise Control hardware is required for proper operation of this feature.

> [!note] Note · Примечание
> This feature will work **only** on specific engine and transmission combinations. Contact a local Cummins® distributor for more details.

On-ramp Boost Feature

On-ramp Boost improves vehicle acceleration on an on-ramp leading to an interstate by increasing power output of the vehicle which increases the merging speeds and assists in an easier merging maneuver. It will temporarily disable torque limiting features of the engine and provide a performance shift schedule to boost the acceleration maneuver. By doing this, it allows the vehicle to operate in a fuel-efficient mode during regular operation and allows better performance during certain conditions like on-ramps.

> [!note] Note · Примечание
> Cummins® Route Parameter Manager or OEM Predictive Cruise Control hardware is required for proper operation of this feature.

> [!note] Note · Примечание
> This feature will work **only** on specific engine and transmission combinations. Contact a local Cummins® distributor for more details.

Predictive Cruise Control Feature

Predictive Cruise Control dynamically adjusts the vehicle speed profile while the vehicle is operating in cruise control. The vehicle speed profile is optimized for fuel economy based on the upcoming road grade.

Predictive Cruise Control uses Global Position System (GPS) signal data to determine the vehicle's position and the route being traveled. Combining the vehicle's route knowledge and a route map with road elevations allows the system to determine a more efficient speed profile to apply. For example, when the momentum of a vehicle can carry the vehicle over the hill crest with a slight speed increase the system will provide that slight increase prior to entering the hill and then allow the speed to decrease prior to cresting the hill. Adjusting the speed prior to entering the hill can be done more efficiently than waiting to provide more power while on the grade to maintain the minimum cruise control speed. The transmission gear may also need to change to a less efficient gear when waiting until being on the grade in order to maintain minimum cruise control speed.

The rules for operating cruise control are the same as they have been previously and are the same regardless of OEM or Cummins® Route Parameter Manager. Cruise control has the same enable and abort conditions and programmable functionality as it has had in the past. Predictive cruise control simply provides minor adjustments to the cruise control target speed to optimize the operation of the vehicle within the defined operating range.

Cummins® engines support two forms of Predictive Cruise Control:

- OEM-provided Predictive Cruise Control systems
- Cummins® Predictive Cruise Control

> [!note] Note · Примечание
> Cummins® Route Parameter Manager or OEM Predictive Cruise Control hardware is required for proper operation of this feature.

OEM Predictive Cruise Control

The OEM-provided Predictive Cruise Control system calculates and provides, via J1939 vehicle network to the engine control module (ECM), the speed delta between the Predictive Cruise Control desired speed and the current cruise control vehicle speed. The ECM in turn adjusts the cruise control target speed to attain that desired predictive cruise control speed. This speed adjustment **only** occurs when the engine is in cruise control mode and the predictive cruise control device has determined a more efficient speed profile for the upcoming route.

Cummins® Predictive Cruise Control

The Cummins® Predictive Cruise Control will run automatically when a Cummins® Route Parameter Manager device is installed on the vehicle. The ECM uses the information provided by the device to calculate the desired change to the cruise control target speed. This results in the same type of adjustment to the cruise control target speed as the OEM system.

Upon agreement between Cummins® and OEMs, the Cummins® ECM can recognize the OEM's Predictive Cruise Control Module as compatible for enabling Cummins® Predictive Cruise Control Algorithm. The module communicates the look ahead route data to the ECM via the J1939 powertrain network and the engine control module calculates the change to the cruise control target speed.

Cummins® Route Parameter Manager

The Cummins® system includes a small electronic module that is installed in a protected environment. The module communicates the look ahead route data to the ECM and the ECM calculates the necessary information to support the ADEPT electronic features. This occurs automatically when the module is properly installed on the J1939 vehicle network.

Cummins® Route Parameter Manager comes with two options: First Fit installed and Aftermarket Kit. First Fit option is installed by truck OEM and available as the factory option. Aftermarket Kit options can be purchased and installed at any time at Cummins® certified service locations.

> [!note] Note · Примечание
> For more information about this hardware and to confirm if it is installed in your vehicle, contact a local Cummins® distributor for more details.

Predictive Road Speed Governor Feature

Predictive Road Speed Governor dynamically adjusts the Road Speed Governor while the vehicle is operating in accelerator control. With constant application of the accelerator pedal, the vehicle speed profile is optimized for fuel economy based on the upcoming road grade.

Predictive Road Speed Governor uses Global Position System (GPS) signal data to determine the vehicle's position and the route being traveled. Combining the vehicle's route knowledge and a route map with road elevations allows the system to determine a more efficient speed profile to apply. For example, when the momentum of a vehicle can carry the vehicle over the hill crest with a slight speed increase the system will allow that slight increase prior to entering the hill and then reduce the speed prior to cresting the hill. Adjusting the speed prior to entering the hill can be done more efficiently than waiting to provide more power while on the grade. Additionally, the transmission gear may also need to change to a less efficient gear when waiting until being on the grade.

> [!note] Note · Примечание
> Cummins® Route Parameter Manager or OEM Predictive Cruise Control hardware is required for proper operation of this feature.
