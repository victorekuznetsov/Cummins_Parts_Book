---
type: "Сервисный бюллетень"
doc: "2883397"
title_en: "Maintenance Monitor Feature Description and Manual Reset Procedure"
released: "2009-10-18"
modified: "2023-03-13"
engines:
  - "77804810"
  - "80141463"
  - "80248213"
families:
  - "15N"
  - "QSX15"
figures: 12
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/bulletin/2883397.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/bulletin/2883397.pdf"
tags:
  - "документ/бюллетень"
  - "двигатель/15N"
  - "двигатель/QSX15"
---

# Maintenance Monitor Feature Description and Manual Reset Procedure

> [!abstract] Сервисный бюллетень · `2883397`
> **Двигатели:** [[77804810 — 15N CM2380 M104B CPL 5977|77804810]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** 15N, QSX15
> **Даты:** выпущен 2009-10-18 · изменён 2023-03-13
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/bulletin/2883397.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/bulletin/2883397.pdf)

## Maintenance Monitor Feature Description and Manual Reset Procedure

**Feature Description**

This feature, when enabled will cause the electronic control module (ECM) to flash a lamp for 30 seconds when the keyswitch is turned ON, alerting the operator when it is time to service the engine. This feature can be adjusted, based on ECM measured distance or engine running time. Once the ECM determines the maintenance interval has expired, it will flash either the MAINTENANCE or the amber CHECK ENGINE lamp (refer to the OEM specifications for appropriate lamp that will be illuminated) for 30 seconds when the keyswitch is turned ON.

Furthermore, the feature can be customized (use Cummins® INSITE™ electronic service tool) to illuminate the lamp at sometime prior to the end of the maintenance interval (Example: The feature can be adjusted to illuminate the lamp at any point when 50 to 100 percent of the maintenance interval has expired. This is accomplished by selecting an appropriate value for Alert Percentage.)

Finally, some applications (specifically ISM and ISX) can have the ECM determine the maintenance interval using the Auto mode of the Maintenance Monitor. If these instances, the user **must** enter an Interval Factor (use Cummins® INSITE™ electronic service tool). The Interval Factor will be based on the vehicle's duty cycle and engine oil grade. The ECM will then calculate the end of the maintenance interval, based on engine operating conditions.

**Adjustable Parameters**

Name: Maintenance Monitor

Range: Enable/Disable

Description: Allows the user to enable the Maintenance Monitor feature.

Name: Mode

Range: Auto, Distance, Time (or Manual)

Description: Choosing Auto, Distance, Time (or Manual) mode will determine how the ECM enacts the Maintenance Monitor Feature.

Auto - If the Auto mode of Maintenance Monitor is available, it is necessary that an interval factor be entered (see Interval Factor in this Service Bulletin), and the maintenance interval will be based on an ECM determination of oil life.

Distance - If the Distance mode is chosen, it is necessary that a distance be entered, and the maintenance interval will be based on ECM measured distance traveled. It is necessary that the vehicle have a working vehicle speed sensor for this mode of Maintenance Monitor to work properly.

Time (or Manual) - If the Time mode is chosen, it is necessary that a time be entered, and the maintenance interval will be based on ECM measured engine run time.

In some industrial applications, the Time mode is labeled Manual mode on Cummins® INSITE™ electronic service tool.

Name: Distance

Range: Varies for different engines (KM/Mi)

Description: When operating in the Distance mode, the distance entered defines the maintenance interval. See the appropriate Operation and Maintenance Manual for a specific engine application for the correct oil drain interval.

Name: Time

Range: Varies for different engines (Hours)

Description: When operating in the Time mode (also called Manual mode in some industrial engines), the time entered defines the maintenance interval. See the appropriate Operation and Maintenance Manual for a specific engine application for the correct oil drain interval.

Name: Alert Percentage

Range: 50 percent to 100 percent

Description: This value **must** be entered. The ECM uses the Alert Percentage to determine when to illuminate the appropriate lamp. For example: If the Alert Percentage is entered as 90 percent, the ECM will illuminate the appropriate lamp at a time or distance corresponding to 90 percent of the total maintenance interval.

Name: Warn While Running

Range: Enable or Disable

Description: Some engines will have this component of the Maintenance Monitor feature available. When Warning While Running is enabled, the appropriate lamp will illuminate as soon as the mileage or time threshold is reached. Otherwise, the appropriate lamp will **only** illuminate at key ON. This component of the Maintenance Monitor feature is useful in some industrial applications where the engines are **not** turned off on a daily basis.

Name: Interval Factor

Range: Varies for different engines (a unit-less number that is used by the ECM to calculate the vehicle's duty cycle and oil grade).

Description: This value is used when operating in the Auto mode. Some engines have calibrations that will base the maintenance interval on duty-cycle and engine operating conditions. In this mode, the engine will allow the maximum oil life if the engine is lightly loaded, and at the same time alert the operator to change the oil sooner if a more severe duty cycle is detected.

Name: Reset

Range: Reset

Description: Resets the Maintenance Monitor interval data. See the following tables in this Service Bulletin to properly select an Interval Factor for various engine types. If the engine type is **not** specifically listed below, it is recommended that Maintenance Monitor be run in either the Distance or Time mode **only**.

**ISX and Signature™ Engines**

First, use Table 1 to select a duty cycle. Evaluate the vehicle's duty cycle based on all three Operational Criteria. The correct duty cycle for the vehicle is the worst case duty cycle based on the three Operational Criteria (Example: A dump truck that averages 6.5 MPG and GVW is 30844 kg \[68,000 lbs\] will be considered as a Severe Duty cycle if the vehicle is operated in dusty environments).

| Table 1 |  |  |  |
|---|---|---|---|
| Operational Criteria | Severe Duty | Normal Duty | Light Duty |
| Average Fuel Consumption | Less than 5.5 MPG | 5.5 to 6.5 MPG | Above 6.5 MPG |
| Gross Vehicle Weight (GVW) | Above 36,287 kg \[80,000 lbs\] | 31,752 to 36,287 kg \[70,000 to 80,000 lbs\] | Below 31,752 kg \[70,000 lbs\] |
| Does the Vehicle Operate in Dusty Environments? | YES | NO | NO |

Pick the correct interval factor based on Table 2.

The correct interval factor on both the duty cycle and the grade of oil used by the customer, if the grade of oil used by the customer changes, the interval factor **must** be evaluated again.

| Table 2 |  |  |  |
|---|---|---|---|
| Oil Grade | Severe Duty | Normal Duty | Light Duty |
| Standard CG-4 | Interval Factor 1.0 | Interval Factor 1.5 | Interval Factor 2.0 |
| CES 20071 (CH-4) | Interval Factor 1.25 | Interval Factor 2.71 | Interval Factor 3.43 |
| CES 20076 | Interval Factor 1.5 | Interval Factor 3.07 | Interval Factor 3.79 |

**ISM Engines**

First, use Table 3 to select a duty cycle. Evaluate the vehicle's duty cycle based on all three Operational Criteria. The correct duty cycle for the vehicle is the worse case duty cycle based on the three Operational Criteria (Example: A dump truck that averages 7.0 MPG and GVW is 30844 kg \[68,000 lbs\] will be considered as a Severe Duty cycle if the vehicle is operated in dusty environments).

| Table 3 |  |  |  |
|---|---|---|---|
| Operational Criteria | Severe Duty | Normal Duty | Light Duty |
| Average Fuel Consumption | Less than 6.0 MPG | 6.0 to 7.0 MPG | Above 7.0 MPG |
| Gross Vehicle Weight (GVW) | Above 36,287 kg \[80,000 lbs\] | 31,752 to 36,287 kg \[70,000 to 80,000 lbs\] | Below 31,752 kg \[70,000 lbs\] |
| Does the Vehicle Operate in Dusty Environments? | YES | NO | NO |

Pick the correct interval factor based on Table 4.

The correct interval factor on both the duty cycle and the grade of oil used by the customer, if the grade of oil used by the customer changes, the interval factor **must** be evaluated again.

Vehicle accumulates 13,000 km \[8000 mi\] (or more) per month and engine has a wastegate turbocharger.

| Table 4 |  |  |  |
|---|---|---|---|
| Oil Grade | Severe Duty | Normal Duty | Light Duty |
| Standard CG-4 | Interval Factor 0.67 | Interval Factor 1.33 | Interval Factor 1.67 |
| CES 20071 (CH-4) | Interval Factor 1.00 | Interval Factor 2.00 | Interval Factor 2.67 |
| CES 20076 | Interval Factor 1.33 | Interval Factor 2.33 | Interval Factor 3.00 |

Vehicle accumulates 13,000 km \[8000 mi\] (or more) per month and engine has a wastegate turbocharger.

| Table 5 |  |  |  |
|---|---|---|---|
| Oil Grade | Severe Duty | Normal Duty | Light Duty |
| Standard CG-4 | Interval Factor 0.33 | Interval Factor 0.53 | Interval Factor 0.80 |
| CES 20071 (CH-4) | Interval Factor 0.67 | Interval Factor 1.00 | Interval Factor 1.67 |
| CES 20076 | Interval Factor 0.83 | Interval Factor 1.33 | Interval Factor 2.00 |

Vehicle accumulates less than 13,000 km \[8000 mi\] per month.

| Table 6 |  |  |  |
|---|---|---|---|
| Oil Grade | Wastegate Turbocharger | Non-Wastegate Turbocharger | N/A |
| Standard CG-4 | Interval Factor 0.17 | Interval Factor 0.30 | N/A |
| CES 20071 (CH-4) | Interval Factor 0.30 | Interval Factor 0.47 | N/A |
| CES 20076 | Interval Factor 0.40 | Interval Factor 0.60 | N/A |

Vehicle is a recreational vehicle or fire truck.

| Table 7 |  |  |
|---|---|---|
| Oil Grade | 450 Horsepower | 500 Horsepower |
| Standard CG-4 | Interval Factor 0.40 | Interval Factor 0.20 |
| CES 20071 (CH-4) | Interval Factor 0.60 | Interval Factor 0.30 |
| CES 20076 | Interval Factor 0.80 | Interval Factor 0.40 |

**Driver Activation/Deactivation**

Use INSITE™ electronic service tool to enable this feature.

The **only** driver or user interaction is to reset the appropriate lamp manually. Otherwise, Cummins® INSITE™ electronic service tool can be used to reset the appropriate lamp.

The Maintenance Monitor reset, on engines without aftertreatment, can be accomplished by clicking the reset button on the Maintenance Monitor screen, using INSITE™ electronic service tool, or by using one of the following procedures.

> [!danger] WARNING · Опасно
> Set the service brake using the trailer brake hand valve. Make sure there is enough air pressure to activate the brake pressure switch. Securely chock the wheels. Truck movement during troubleshooting can cause severe equipment damage, personal injury, or death.

> [!note] Note · Примечание
> Turn the keyswitch to the ON position (but do **NOT** start the engine).

1. Turn the keyswitch to the ON position.

![[19c01704.png]]

2. Release the service brake pedal.

![[19c01705.png]]

3. Depress the throttle pedal and hold at 100 percent throttle.

![[19c01706.png]]

4. Press and release the service brake pedal 3 times.

![[19c01707.png]]

5. Release the throttle pedal.

![[19c01708.png]]

6. Press and release the service brake pedal 1 time.

![[19c01709.png]]

7. Depress and hold the throttle pedal at 100 percent throttle again.

![[19c01706.png]]

8. Press and release the service brake pedal 3 more times.

![[19c01707.png]]

9. Release the throttle pedal.

![[19c01708.png]]

10. Press and release the service brake pedal 1 time.

![[19c01709.png]]

11. The appropriate lamp will flash 3 times.

![[19c01773.png]]

12. Turn the keyswitch to the OFF position.

![[19c01711.png]]

**Procedure for Applications without a Throttle Pedal**

1. Turn the keyswitch to the ON position (but do **NOT** start the engine).
2. Turn the diagnostic switch to the ON position for at least 3 seconds and then turn it to the OFF position.
3. Turn the diagnostic switch to the ON position (for less than 3 seconds) and then to the OFF position, twice, with less than 3 seconds between each switching.
4. Turn the diagnostic switch to the ON position for at least 3 seconds and then turn it to the OFF position.

The procedure **must** be completed within 20 seconds or data will **not** reset.

The appropriate lamp will flash 3 times to indicate that the reset has been completed.

**Interaction with other Features and Parameters**

Not all engines (Example: CELECT™) are equipped with a separate MAINTENANCE lamp. In these cases, the engine can utilize another method (Example: CELECT™ engines alert the operator by flashing the ENGINE PROTECTION lamp through 5, 3-flash cycles approximately 12 seconds after key ON). See the appropriate Operation and Maintenance Manual to see how the operator is alerted when this feature is enabled.

Maintenance Monitor will **not** be enabled if Centinel™ is installed on the vehicle.

**Special Instructions**

Do **not** enable the Auto mode of Maintenance Monitor without referring first to a specific engine application Operation and Maintenance Manual and correctly evaluating the vehicle's duty cycle. It is necessary that the correct Interval Factor be chosen if using the Auto Mode.

**Disadvantages**

Applications that do **not** utilize a separate MAINTENANCE lamp can illuminate engine WARNING lamps, which can result in false service complaints if drivers are **not** trained to use the Maintenance Monitor feature.

**Visual Aids**

None.

### Document History
