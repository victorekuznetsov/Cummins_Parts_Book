---
type: "Сервисный бюллетень"
doc: "3666094"
title_en: "Excessive Fuel Consumption Troubleshooting"
released: "2007-11-30"
modified: "2010-09-28"
engines:
  - "37269910"
  - "37280605"
  - "77804810"
  - "80141463"
  - "80248213"
  - "93948840"
families:
  - "15N"
  - "K19"
  - "QSX15"
  - "QSZ13"
figures: 5
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/bulletin/3666094.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/bulletin/3666094.pdf"
tags:
  - "документ/бюллетень"
  - "двигатель/15N"
  - "двигатель/K19"
  - "двигатель/QSX15"
  - "двигатель/QSZ13"
---

# Excessive Fuel Consumption Troubleshooting

> [!abstract] Сервисный бюллетень · `3666094`
> **Двигатели:** [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]], [[77804810 — 15N CM2380 M104B CPL 5977|77804810]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]], [[93948840 — QSZ13 CM2150 Z102 CPL 4858|93948840]]
> **Семейство:** 15N, K19, QSX15, QSZ13
> **Даты:** выпущен 2007-11-30 · изменён 2010-09-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/bulletin/3666094.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/bulletin/3666094.pdf)

## Excessive Fuel Consumption Troubleshooting

This Service Bulletin is a guide for finding the most effective diagnostic approach in response to a report of excessive fuel consumption. Because each engine/vehicle operation combination is unique, the steps or sequences can vary for different cases. Applied engine and installation knowledge are the best tools for such a diagnosis. However, a systematic, cost-effective method of checking for a possible engine problem can be valuable to both the troubleshooter and engine operator.

The first step in the effective diagnosis of any complaint about engine operation is a proper understanding of what is actually happening, or what is perceived to be happening. Rather than immediate engine work to locate a reported malfunction, reasonable time **must** be taken to review the complaint, understand the maintenance and operation of the particular vehicle, and to make an external examination of the vehicle and engine for related discrepancies. Such a review of external conditions which impact the reported complaint is a time and labor-saving method to be more certain that the relatively expensive engine tests and repairs are directed as accurately as possible.

Because numerous variables affect fuel consumption, the most accurate method of determining fuel consumption in the field, where there is varying terrain, speeds, idle time, etc., is to conduct a ride-along test. This test is discussed in the Ride-Along Test section. The ride-along test is **not always** possible or feasible. Therefore, applied engine and installation knowledge, along with additional items suggested in this bulletin, will assist in understanding fuel consumption.

It **must** also be noted that there are several tools (i.e., VE/VMS®, RoadRelay®, and Cadec®) listed in this document which can help determine fuel consumption. These are **only** tools, and the information from these devices **must** be used for reference **only**. They are **not** a substitute for actual ride-along testing.

The engine is **only** one part of the vehicle system. Therefore, Cummins Inc. can **not** and does **not** guarantee any specific fuel consumption level. As can be seen by the following information, numerous variables are involved, many being related to the vehicle design, owner operation, or operating environment.

| Fuel Consumption Diagnostic Worksheet |  |
|---|---|
| Customer Name |  |
| Date |  |
| Vehicle Specifications: |  |
| Engine Model |  |
| Tractor Year, Type, and Model |  |
| Transmission |  |
| Rear Axle Ratio |  |
| Number of Axles |  |
| Typical GVW |  |
| Trailer |  |
| Ribbed/Smooth |  |
| Height |  |
| Width |  |
| Trailer Gap |  |
| Fairing (Yes/No) |  |
| Length |  |
| Vehicle Aerodynamic % (See the Aerodynamics Section) |  |
| Tire Size (11R24.5, Low Profile, etc.) |  |
| Tire Type (Standard/Extra Tread) |  |
| Fan Type (Direct Drive/Viscous/Clutched) |  |
| Power Steering (Yes/No) |  |
| Refrigerant Compressor (Yes/No) |  |
| Other Parasitic Loads |  |

Answer the following questions:

- Has fuel economy gotten worse since the engine was new?
- What is the expected and actual fuel mileage?
- Is there a problem with acceleration or response? (Yes/No) \*

\*If yes, see the Response section.

| Troubleshooting |  |
|---|---|
| Cause | Correction |
| What are the expectations based on? (Original mileage, previous mileage, competitive engine, other units, VE/VMS®/other expectations, or demonstration truck) | Run a VE/VMS® report to determine if expectations are unreasonable. |
| Are the drive train specifications within Cummins Inc. recommendations? (Verify with a VE/VMS® run) | Correct for gearing or compensate by setting a lower road speed governor (RSG). Explain the trade-off of fuel economy versus performance with present gearing. |
| Evaluate fuel consumption over an extended period of time (3 to 6 months) | This is necessary to determine the effects of seasonal and/or operational changes. |
| Was the calculation of fuel consumption done correctly? | Evaluate the method for validity. Correct and reevaluate, if necessary. Also, be aware of fuel practices (use of reefers, lubricating oil blenders, additives, etc.). |
| Were there any changes in the vehicle's operating environment that contributed to the fuel consumption complaint? (Change of route, change of loads, cold ambient temperatures, windy conditions, snow/rain) | Explain the effects of the operating environment on the measured fuel consumption. A fuel consumption complaint may be based on adverse weather (up to one mile per gallon) or changes in routes and/or loads. |
| What grade or blend of fuel is being used when the complaint is generated? (Diesel number 1, diesel number 2, or winter fuel (P40, P50, etc.)) | Diesel number 1 and lighter winter fuels are lower in heat content and result in higher fuel consumption. Reevaluate using number 2 diesel fuel. |
| Does the engine coolant temperature reach normal operating temperature? | Repair as necessary. |
| Have the tractor or trailer brakes been recently serviced? | Check for dragging brakes and repair as necessary. |
| Is the trailer alignment correct? | Repair as necessary. |
| Has the complaint occurred after new tires were installed either on the tractor or the trailer? | Consider the effects of new tires and reevaluate fuel consumption. (There is an approximate 3 percent difference in the rolling radius between new and old tires.) |
| Are the hubometer and odometer calibrated correctly? | See the Tire Revolutions Per Mile section to determine the actual tire revolutions per mile, in calibration of hubometer and tire revolutions per mile parameter in the electronic control module (ECM). See the Hubometer Verification section for hubometer verification. Repair or calibrate as necessary and reevaluate fuel consumption. |
| Check the tread condition and the inflation pressure on both the tractor and the trailer tires. | Repair and inflate the tires as necessary and reevaluate fuel consumption. |
| Has the fuel consumption complaint occurred after an engine repair? | Investigate the repair to determine its effect on fuel consumption (incorrect injectors, incorrect turbocharger, incorrect SC code, etc.). |
| Can the fuel consumption complaint be correlated to a change in drivers? | If yes, evaluate the need for driver training. |
| Are there any signs of external or internal (crankcase) fuel leakage? | Repair as necessary and re-evaluate fuel consumption. |
| Are there signs of tampering with the CELECT™ system (inspect the vehicle speed sensor and the corresponding harness)? | Repair or correct as necessary and re-evaluate fuel consumption. |
| Are there indications of high exhaust temperatures (cracked exhaust manifolds, turbine casings, mounting hardware, etc.)? | This is an indication of an incorrect air-to-fuel ratio. This **must** be verified on a chassis dynamo-meter. |
| Is the oil level correct? | High oil levels can cause crank or rod dipping. Drain the engine oil and verify the dipstick calibration. Reevaluate fuel consumption with the correct oil level. |
| Check for active fault codes or high counts of inactive fault codes on CELECT™ engines. | Repair as necessary and reevaluate fuel consumption. |
| Are adjustable parameters and optional features (gear down protection) set to their correct/expected values, and are they consistent with vehicles being compared to in the fleet? | Set the parameters to the correct values and make sure that gear down protection is active and set correctly. Reevaluate fuel consumption. |
| Is the ECM calibration correct? | Calibrate again, as necessary, and reevaluate fuel consumption. |
| Are fuel rate, boost, intake and exhaust restrictions, etc., correct? | Verify these measurements using a chassis dynamometer. Repair as necessary and reevaluate fuel consumption. |
| Are there leaks in the intake air system between the turbocharger and the intake manifold? Does the charge air cooler have leaks? | Repair the intake system as necessary. Check the charge air cooler. Use the leak down procedure in the Troubleshooting and Repair Manual, N14 Engines, Bulletin 3810456. Repair as necessary and reevaluate fuel consumption. |

## AERODYNAMICS

The vehicle configuration plays a vital role in fuel consumption. One of the most effective tools that can be used in understanding gearing, routes, weights, and aerodynamics is VMS®. VMS® is a computer program that simulates the vehicle operation. However, as with any computer program, the results are **only** as accurate as the data used. Therefore, the following guidelines have been established in VMS® to reflect the effects of aerodynamics.

Rules for aerodynamic values (additive):

| Percentage | Configuration |
|---|---|
| 0% | Standard vehicle |
| 2% | For aerodynamic bumper |
| 2% | For sloped hood, aerodynamic headlights, and under-hood air cleaner |
| 1% | For full side skirts |
| 5 to 10% | For roof deflector, 5% for simple deflectors or 10% for full width deflectors with extenders |
| 0 to 7% | Depending on gaps beyond cab, 0% for more than 50-inch gap or 1% for 45 to 49-inch gap or 2% for 40 to 44-inch gap or 3% for 35 to 39-inch gap or 4% for 30 to 34-inch gap or 5% for 25 to 29-inch gap or 6% for 20 to 24-inch gap or 7% for less than 20-inch gap |

- Most trucks are 12 to 20 percent aerodynamic.
- The most aerodynamic trucks are 22 percent aerodynamic.
- Some trucks are 0 percent aerodynamic.
- Negative aerodynamic aids (-10 percent) can occur with irregularly shaped loads on lowboy trailers.
- Negative aerodynamic aids (-X percent) can also occur when the tractor has an air deflector and is pulling a flatbed or something other than a van trailer.
- Tanker trucks are -5 percent aerodynamic.
- Rib trailers are -10 percent aerodynamic.
- Flat beds are -10 to -30 percent aerodynamic.
- Car haulers are -30 percent aerodynamic.

## RESPONSE

Response testing procedure for heavy duty CELECT™ engines:

For this test, a boost pressure gauge, associated plumbing lines, and a stop watch are needed.

1. Attach the tractor to a loaded trailer (GCW **must** be 65,000 to 80,000 pounds).
2. Make sure the engine is warmed up.
3. Determine the full load boost pressure at torque peak engine speed while applying full throttle. (Trailer brakes may also be applied for additional loading, if required.) Note the boost pressure at torque peak engine speed.
4. Perform the coast down test. Select a secondary road that is level and has minimal traffic. Accelerate the vehicle up through the gears to direct gear (1 to 1) and to an engine speed of at least 300 rpm above the torque peak engine speed. Allow the vehicle to coast down to torque peak engine speed then snap the throttle. Measure the time required to develop 50 percent of torque peak boost (determined in Step 3 above).
5. Repeat Step 4 two more times for a total of three data points.
6. Calculate the average time to 50 percent boost: Average time to 50 percent boost = (time 1 + time 2 + time 3)/3.

This average time **must** be 3 seconds or less for acceptable performance.

## RIDE-ALONG TEST

After completing the steps outlined previously in this bulletin, there are occasional instances where it is beneficial to conduct a ride-along fuel consumption test on the vehicle. If done correctly, this test provides fuel economy results which are representative of those predicted by the VE/VMS® computer simulation. This demonstrates realistic fuel mileage under known conditions, and helps a customer understand the factors which influence tank mileage on the vehicle. By monitoring vehicle speed, fuel fill, loads, driver technique, and terrain, an accurate fuel mileage figure can be determined.

Other types of road tests, such as SAE Type II and Type III provide increased tank mileage accuracy under simulated conditions (defined course, speeds, idle time, etc.) at the expense of added cost and complexity. These tests are excellent ways to compare different vehicles but are beyond the scope of this bulletin.

Use the following information to obtain accurate ride-along test results:

Prior to the test:

- Choose a route that is representative of what the customer normally drives.
- If possible, plan the trip so that the start and finish are at the same point.
- If the start and finish are at two different locations, be aware that differences in elevation (feet above sea level) and the orientation of vehicle at final fill can impact fuel economy.
- Use a trailer and load that is representative of the operator's normal use.
- Plan to operate the vehicle for a minimum of 966 km \[600 mi\], if possible. (Higher mileage accumulations provide more accurate test results.)
- Check the tire inflation pressures. Observe all tires for signs of misalignment.
- Top off the fuel tank(s) at the same fuel station, using the same bay (pump), facing the same direction, at the start and at the conclusion of the test.
- Use a fuel gauge device similar to the dangle meter shown in the Dangle Meter section to determine consistent fill point(s) in the fuel tank(s).
- When the fuel tanks are full, weigh the vehicle using certified scales.
- Record the odometer reading. If the truck has a hubometer, note that as well.

During the test:

- If the vehicle has cruise control, encourage the driver to use this device as much as possible. This reduces throttle variation and helps maintain a consistent vehicle speed.
- If testing a COMMAND concept L10 or N14 engine, optimum fuel economy is obtained with low rpm (1400 to 1600 rpm at cruise) operation. Encourage the driver to lug the engine to 1100 to 1200 rpm on hills. Minimize engine operation above 1700 rpm in downshift situations.
- Verify odometer operation using mile markers along the highway. Speedometer accuracy can also be verified in this manner.
- If the vehicle speed varies significantly through the test, divide the distance traveled (miles) by the number of hours to determine the average speed.
- Note the terrain and attempt to determine which of the three VE/VMS® simulations best represents the trip:

- Near level 1 and 2 percent grades
- Short hills up to 5 percent grades
- Long mountain grades.

- Minimize idle time, if possible. If the operator insists on idling the engine for extended periods of time (greater than 5-minute segments), record the total minutes and divide this number by the total engine operation minutes to determine the percentage of idle time for the trip.

At the end of the test:

- Assuming the end point of the test is at the same location as the start point, fill the tank(s), using the same pump, in the same bay, with the vehicle parked in the same direction as the initial fill.
- Use the fuel gauge dangle meter to accurately top off the fuel tank(s).

> [!note] Note · Примечание
> Make sure the dangle meter is consistently positioned on the filler neck. Inconsistent positioning can cause discrepancies in your final results.

- Divide the distance (miles) by the number of gallons used to determine miles per gallon.
- If an odometer error was noted earlier in the trip, calculate the corrected miles. Divide the corrected miles by the number of gallons used on the trip to get the corrected miles per gallon.
- If a final VE/VMS® computer simulation is an option, run the simulation, using actual (or estimated) vehicle speed, gross vehicle weight, terrain, etc., to verify earlier predictions on fuel mileage.
- Share the test results with the driver and record the driver's comments.

## TIRE REVOLUTIONS PER MILE

![[05800092.png]]

(1) Measure distance (1 revolution)

1. Inflate the tires to 621/689 kpa \[90/100 psi\], or to the recommended pressure, and record the values.
2. Back the vehicle under a loaded trailer.
3. Locate the tractor and trailer on a flat surface.
4. Put a vertical mark at the top and bottom of the tire and a corresponding mark on the flat surface.
5. Roll the vehicle forward exactly one (1) tire revolution; and put a second mark on the surface, aligning with the vertical mark previously placed at the bottom of the tire. Use a level to align the marks at the top and bottom of the tire with the mark being placed on the surface.
6. Measure the distance between the marks and divide the value (in feet) into 5280 (ft/mi) to accurately determine the tire revolutions per mile.

Tire circumference:

Tire revolutions/mile:

Inflation pressure:

Comments:

![[05800093.png]]

## HUBOMETER VERIFICATION

- Put the hubometer on a Cummins® fuel pump test stand by using a front cover from a PT fuel pump with a thread adapter (see above illustration).
- Set the fuel pump stand operating rpm to the specified hubometer revolution per mile.

![[05800094.png]]

10 minutes = 10 miles

- Conduct a verification test for 10 minutes at the specified rpm to determine the accuracy of the hubometer (see above illustration).

![[05800090.png]]

## DANGLE METER

A dangle meter gauge is used to consistently measure the fuel level in the tank during volumeteric-type fuel consumption testing.

![[05800091.png]]

> [!note] Note · Примечание
> Make sure the dangle meter is consistently positioned on the filler neck. Inconsistent positioning can cause discrepancies in the final results.

### Document History
