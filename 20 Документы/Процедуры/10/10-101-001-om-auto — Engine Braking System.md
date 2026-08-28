---
type: "Процедура"
doc: "10-101-001-om-auto"
title_en: "Engine Braking System"
modified: "2006-05-10"
engines:
  - "80141463"
  - "80248213"
families:
  - "QSX15"
manuals:
  - "3666251"
  - "4960314"
figures: 39
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/10/10-101-001-om-auto.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/10-101-001-om-auto.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSX15"
  - "группа/10"
---

# Engine Braking System

> [!abstract] Процедура · `10-101-001-om-auto`
> **Двигатели:** [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSX15
> **Входит в руководства:** [[3666251 — Signature and ISX Operation and Maintenance Manual|3666251]], [[4960314 — ISX Owners Manual|4960314]]
> **Секции:** Section 1 - Operating Instructions
> **Даты:** изменён 2006-05-10
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/10/10-101-001-om-auto.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/10-101-001-om-auto.pdf)

### General Information

> [!warning] CAUTION · Осторожно
> Do not exceed governed engine speed when operating engine brakes. Engine damage can occur. The engine brakes are designed to assist the vehicle's service brakes to slow down the vehicle.

![[nobox.png]]

Signature and ISX engines are equipped with the Intebrake™ system (engine brakes).

Engine brakes use the energy of engine compression to provide vehicle retardation by converting the engine to an energy-absorbing device to reduce vehicle speed. This is accomplished by a hydraulic circuit that opens the exhaust valves near the end of the compression stroke.

The ISX CM870 product and newer use the added benefit of the variable geometry turbocharger to assist in engine braking.

![[17c00015.png]]

The amount of braking power available on this engine is up to 600 hp. Braking power is managed by the Intebrake™ system (engine brakes).

![[17c00010.png]]

> [!warning] CAUTION · Осторожно
> Do not operate the engine if the engine brakes will not deactivate. To do so will cause severe engine damage.

If the engine brakes will **not** shut off, shut off the engine immediately, and contact a Cummins Authorized Repair Facility.

![[17c00172.png]]

Engine brake controls consist of the following:

- A six-position or three-position selector switch
- An on/off switch
- A clutch switch
- A throttle sensor
- A service brake pressure switch.

![[17c00012.png]]

Other switches for cruise control that affect engine brake operations are:

- Cruise control on/off and set/resume switches (if the engine brakes in cruise control feature is turned off)
- Service brake air pressure switch.

Engine brakes can operate while cruise control is turned on. The electronic feature, fan control engine braking, can be enabled to turn the fan on during engine braking. This increases the parasitic load on the engine during braking. Refer to Programmable Features in this section.

![[es8bdga.png]]

> [!note] Note · Примечание
> Some OEMs choose to use a three-position switch.

The six-position selector switch is located next to the on/off switch in the cab, and allows you to select the retarding power from one to six brakes.

![[17c00014.png]]

The engine brake level specifications:

Position No. 1 = 17-percent engine braking power.

Position No. 2 = 33-percent engine braking power.

Position No. 3 = 50-percent engine braking power.

Position No. 4 = 67-percent engine braking power.

Position No. 5 = 83-percent engine braking power.

Position No. 6 = 100-percent engine braking power.

> [!note] Note · Примечание
> For OEMs that use a three-position switch, the brake level specifications are: Position No. 1 = 33-percent engine braking power. Position No. 2 = 67-percent engine braking power. Position No. 3 = 100-percent engine braking power.

For ISX CM870 and newer products, the engine brake select switch does **not** always directly correlate to the number of engine brake solenoids that are activated. This is due to the added use of the variable geometry turbocharger to assist in engine braking and the use of **only** two engine brake solenoids.

![[17c00033.png]]

> [!note] Note · Примечание
> Any one of these switches can deactivate the engine brakes. If the engine brakes in cruise control feature is turned on, the cruise control switch, PTO switches, or both will **not** deactivate the engine brakes.

With the engine, signals from the on/off switch, the clutch switch, the throttle sensor, and the cruise control switch, PTO switches, or both are fed into the electronic control module.

![[17c00013.png]]

> [!note] Note · Примечание
> Engine brakes can **not** be enabled:

The ECM then electronically enables or disables the engine brakes.

1. When cruise control is active, if the engine brakes in cruise control feature is turned off
2. When engine speed goes below 850 rpm or 30 mph
3. When an electronic fault code is active
4. When the clutch pedal is depressed
5. When the throttle pedal is depressed
6. When the PTO or remote PTO is active.

![[17c00015.png]]

The throttle position sensor is part of the accelerator pedal assembly located in the cab and will deactivate the engine brakes when depressed.

![[ea8swva.png]]

The clutch switch uses the motion of the clutch linkage to deactivate the engine brakes when the clutch pedal is depressed. Depressing the clutch while in cruise control will disengage the cruise control.

![[cl8swva.png]]

The service brake pressure switch is attached to the service brake air supply line.

Applying the service brakes while in cruise control will disengage the cruise control and enable the engine brakes.

If the pedal-activated engine brake feature is enabled, the service brake pedal **must** be tapped before the engine brakes will be activated.

![[eb8swvo.png]]

Idle the engine 3 to 5 minutes at approximately 1000 rpm to warm the engine before activating the engine brakes. Do **not** operate the engine brakes until the engine oil temperature is above 30°C \[86°F\].

![[eb800va.png]]

> [!note] Note · Примечание
> See the “Tips for Operation” steps in this section for specific information about engine brake operation under certain road conditions.

To activate the engine brakes, switch the on/off switch to the ON position. Once activated, the operation of the engine brakes is fully automatic.

![[eb8swvc.png]]

> [!danger] WARNING · Опасно
> Do not use the engine brakes while bobtailing or pulling an empty trailer. With the engine brakes in operation, wheel lockup can occur more quickly when the service brakes are applied, especially on vehicles with single-drive axles.

Make sure the engine brakes are switched to the OFF position when bobtailing or pulling an empty trailer.

![[eb8swqa.png]]

> [!warning] CAUTION · Осторожно
> The engine brakes are designed to assist the vehicle's service brakes in slowing the vehicle to a stop.

Remember, service brakes will be required to bring the vehicle to a stop.

![[eb800be.png]]

> [!warning] CAUTION · Осторожно
> Do not use the engine brakes to aid clutchless gear shifting. This can cause the engine to stall or lead to engine damage.

![[eb800bf.png]]

The ECM will disable the engine brakes when engine rpm is below 850 rpm, when an electronic fault code is active, or if the vehicle speed is less than the engine brake minimum vehicle speed parameter.

![[00800004.png]]

> [!warning] CAUTION · Осторожно
> Do not operate the engine if the engine brakes will not deactivate. To do so will cause severe engine damage.

If the engine brakes will **not** shut off, shut off the engine immediately, and contact a Cummins Authorized Repair Facility.

![[eb100ba.png]]

Tips for Operating on Level and Dry Pavement

For operating on dry and relatively flat surfaces when greater retarding power is **not** required, you can select a lower position.

![[17c00016.png]]

To reduce vehicle speed, put the engine brake on or off switch in the ON position. Remove your foot from the throttle and clutch pedal. The engine brakes will immediately begin to operate, slowing the vehicle.

![[eb8swvn.png]]

For operation on dry pavement when maximum retarding power is required, select the No. 6 position.

![[17c00017.png]]

> [!danger] WARNING · Опасно
> The safe control speed of a vehicle will vary with the size of the load, the type of load, the grade, and the road conditions.

> [!note] Note · Примечание
> **Always** be prepared to use the vehicle service brakes for emergency stopping.

Tips for Operation on Grades with Dry Pavement

Vehicles equipped with properly operated engine brakes are capable of traveling downhill at slightly higher control speeds than vehicles **not** equipped with engine brakes.

![[eb800ba.png]]

> [!warning] CAUTION · Осторожно
> Never exceed governed engine speed as engine damage can occur.

> [!note] Note · Примечание
> The optimum braking power of engine brakes is reached at rated engine speed, therefore, correct gear selection is critical.

Once you have determined the safe speed for your vehicle, operate the engine brakes with the transmission in the lowest gear which will **not** cause the engine speed to exceed the rated engine speed.

![[eb800vf.png]]

> [!note] Note · Примечание
> Some OEMs choose to use a three-position switch.

The six-position selector switch can be used to vary braking power as road conditions change.

![[17c00018.png]]

Vehicle service brakes **must** be used when additional braking power is required.

![[eb800vg.png]]

> [!danger] WARNING · Опасно
> Frequent use of the service brakes will cause them to heat up, which reduces the ability to slow or stop the vehicle.

![[eb800bb.png]]

> [!note] Note · Примечание
> The longer or steeper the hill, the more important it is to use your engine brakes. Make maximum use of your engine brakes by gearing down and letting the engine brakes do the work.

If frequent use of the vehicle service brakes is required, it is recommended that a slower control speed be used by selecting a lower transmission gear.

![[eb800vi.png]]

### Tips for Operation on Slick Roads

> [!warning] CAUTION · Осторожно
> The operation of any vehicle is difficult to predict on slick roads. The first 10 to 15 minutes of rainfall are the most dangerous, as road dirt and oil mixed with rain create a very slippery surface.

**Always** allow for extra distance between your vehicle and other objects when using the service brakes or engine brakes on slick roads.

![[eb800bc.png]]

> [!danger] WARNING · Опасно
> Using the engine brakes on wet or slippery roads can cause overbraking of the wheels, especially vehicles with light loads or single-drive axles. Stopping distance can actually increase, or the vehicle can skid or jackknife.

Reduce the retarding power, or turn off the engine brakes on slick roads.

![[17c00019.png]]

When driving on slick roads, start with the on/off switch in the OFF position and the six-position selector switch in the No. 1 or No. 2 position.

If your tractor is equipped with a twin-screw rear axle, use the power divider in the UNLOCKED position.

![[17c00020.png]]

Remove your foot from the throttle to make sure that the vehicle will maintain traction with the retarding power of the engine alone.

If the vehicle drive wheels begin to skid or there is a fishtailing motion, do **not** activate the engine brakes.

![[eb800vh.png]]

If traction is maintained and more braking power is required, you can select the next higher position on the six-position selector switch. Activate the engine brakes by switching the on - off switch to the ON position.

![[17c00021.png]]

If the vehicle's drive wheels begin to skid or there is a fishtailing motion, switch the on/off switch to the OFF position.

![[17c00022.png]]

If traction is maintained when the engine brakes are activated and more braking power is required, move the six-position selector switch to the No. 3 or 4 position.

![[17c00023.png]]

Again, if the vehicle has lost traction or there is a fishtailing motion, switch the on/off switch to the OFF position. Do **not** attempt to use the engine brakes in the No. 3 or 4 position.

![[17c00025.png]]

Repeat the above procedures to select the No. 5 or 6 position on the selector switch.

![[17c00024.png]]

Again, if the vehicle has lost traction or there is a fishtailing motion, switch the on/off switch to the OFF position. Do **not** attempt to use the engine brakes in the No. 5 or 6 position.

![[17c00025.png]]
