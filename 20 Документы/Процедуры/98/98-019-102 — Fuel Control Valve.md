---
type: "Процедура"
doc: "98-019-102"
title_en: "Fuel Control Valve"
modified: "2022-08-09"
engines:
  - "37269910"
  - "37280605"
families:
  - "K19"
manuals:
  - "3666070"
figures: 28
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-019-102.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-019-102.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K19"
  - "группа/98"
---

# Fuel Control Valve

> [!abstract] Процедура · `98-019-102`
> **Двигатели:** [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]]
> **Семейство:** K19
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]]
> **Секции:** Section 19 - Electronic Controls - Group 19 · Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2022-08-09
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-019-102.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-019-102.pdf)

### General Information

The EFC valve is contained within the EFC module, which is mounted directly on top of the fuel pump.

The circuit consists of the EFC valve and the EFC valve supply and return wires, which are connected to the main engine harness connector pins 21 and 10, respectively.

![[19801790.png]]

### Test

The electronic service tool INSITE™, Compulink™, or Echek™, can be used to perform an actuation test on the EFC valve, which produces an audible clicking sound from the EFC if it is moving freely. This test can be used to determine if the EFC valve is sticking.

Using INSITE™, from the Tests menu, select Fuel Control Actuator. Then, follow the instructions in the window.

![[19800109.png]]

The Compulink™ displays will be used in the following steps, but the Echek™ displays will be similar.

From the Main menu, press the “1” key to enter troubleshooting.

Select Compulink™ Main menu option:

1. Troubleshooting

2. Parameter & Adjustments

3. System Identification & Dataplate

4. Compulink™ File Manager

5. Calibration Transfers

6. Utilities

Active Keys: 1 to 6, BACK, HELP.

![[nobox.png]]

Next, press the “4” key to enter the special functions.

Select Troubleshooting menu option:

1. Fault Code Information

2. Monitor

3. Troubleshooting Tree

4. Special Functions

Active Keys: 1 to 4, BACK, HELP.

![[nobox.png]]

To enter the fuel control actuator test, press the “1” in the Special Functions menu.

Select Special Functions menu option:

1. Fuel Control Actuator Test

2. Read Audit Trail

Active Keys: 1 to 2, BACK, HELP, CNCL.

![[nobox.png]]

> [!note] Note · Примечание
> The engine **mustnot** be running when performing the fuel control actuator test.

To run the test, make sure the keyswitch is on with the engine **not** running. Press the “\*” button on the Compulink™. An audible clicking sound should be heard coming from the EFC valve.

Fuel Control Actuator Test

Press the "\*" key to cause the EFC valve to open and close with an audible click.

Valve Position --\> - -\[ \] - -

Active Keys: "\*," CNCL.

![[nobox.png]]

If an audible click is **not** heard from the EFC valve, then the valve is sticking. After checking the EFC circuit wiring for the valve and the valve supply and return ([[98-019-030 — EFC Module|Refer to Procedure 019-030]] in Section 19), the valve should be removed and inspected.

> [!note] Note · Примечание
> This test will **not** determine whether or **not** the EFC valve is **only** partially sticking. If it is suspected that its motion is restricted, then the valve should be removed and inspected.

![[19801969.png]]

### Leak Test

Check the EFC valve to make sure it is **not** stuck open or allowing excessive leakage.

Start the engine and warm the coolant temperature to at least 65°C \[ 150°F\]. With the engine idling, disconnect **one** of the EFC valve main engine harness connectors.

If the engine does **not** shut down, replace the EFC valve. If the engine does shut down, the valve can still be the cause of a raised low idle. Troubleshoot this symptom. Refer to Section TS for the appropriate troubleshooting symptom chart.

![[19801959.png]]

### Remove

If an electronic service tool is available, perform the EFC actuator test.

If the EFC valve is **not** clicking, then remove and inspect the EFC valve.

![[19800109.png]]

Disconnect the electrical leads from the valve.

![[19801959.png]]

> [!warning] CAUTION · Осторожно
> Do not force or pry the valve. If the valve is stuck in the module, remove the module to get a firmer grip on the valve. Refer to Procedure 019-030 .

Remove the three capscrews that hold the valve in the EFC module.

Carefully, pull the valve out of the EFC module.

![[19801960.png]]

### Inspect for Reuse

Inspect the actuator to make sure it is **not** sticking. Hold the mounting flange of the EFC and turn the inner core, which is attached to the spring. The core **must** turn freely and return to the original position by spring force. If it does **not** or if the sleeve has cracks in it, replace the EFC actuator.

> [!note] Note · Примечание
> Do **not** remove the return springs from the valve actuator. The EFC valve can be damaged.

![[19801969.png]]

Inspect the EFC actuator terminal posts for cracks, corrosion, and damage from arcing. If terminal damage exists, replace the EFC valve.

![[19801969.png]]

Inspect the mounting bore of the EFC in the CENTRY™ module for damage, which can cause leakage. Inspect for debris in the mounting bore. If damage or debris exists, clean or replace the EFC module.

![[19801971.png]]

Install a new o-ring on the 2-inch diameter of the EFC valve. Install two new o-rings on the EFC valve barrel.

> [!note] Note · Примечание
> The o-rings on the EFC valve barrel are different sizes.

![[19801972.png]]

Use clean engine oil to lubricate the o-rings.

#### Lever Arm Posts:

- Each EFC actuator is slightly different in its performance as built. The lever arm post is bent to tune the EFC actuator within its calibration requirements by the manufacturer. The lever arm post can be bent in multiple directions to calibrate the EFC's performance.
- If the lever arm post is bent towards the center of the EFC valve this change decreases the amount of force that the lever arm spring can exert on the rotor.
- If the post is bent out-board this change adds spring tension and increases the amount of force that the lever arm spring can exert on the rotor.
- Some posts can be straight as well depending the individual EFC actuator performance.

#### Broken Lever Arms Springs:

- If the Lever Arm Spring is broken do **not** replace the spring as the EFC valve will be out of calibration. The EFC Valve must be replaced.

#### Play in the Governor Shaft:

- If there is concern that there is excessive play between the rotating valve shaft and the rotating valve shaft housing (gold section). The EFC valve should be replaced. Currently there are no specifications for establishing excessive play other than there should be little difference between the suspect EFC valve and a new EFC valve.

#### Cracks & Fractures:

- Inspect the rotating valve shaft housing (gold section) for hairline fractures that suggest the housing is failing and allowing fuel to leak through. If fractures are found the EFC valve should be replaced.

Install the EFC valve into the EFC module. The valve flange will be about 9.5 mm \[3/8 in\] from the body.

![[19801973.png]]

> [!warning] CAUTION · Осторожно
> Do not force the valve into the module; excessive force can damage the valve or o-rings.

Using the palm of the hand, push and rotate the EFC valve 30 degrees. Rotate the valve until the mounting holes are aligned.

![[19801974.png]]

Install the three hex head capscrews. These capscrews have captive spring washers and do **not** require lock washers.

Tighten the capscrews until they are finger-tight.

![[19801975.png]]

The EFC valve capscrews **must** be tightened in the following sequence:

1. Tighten the capscrews 1/8 of a turn in the sequence shown in the figure until they are seated.

![[19801976.png]]

1. Tighten the capscrews in sequence shown.

> [!tip] Момент затяжки · Torque Value
> 2.8 n•m [25 in-lb]

![[19801977.png]]

1. Tighten the capscrews in sequence shown.

> [!tip] Момент затяжки · Torque Value
> 5.6 n•m [50 in-lb]

![[19801978.png]]

1. Loosen all three capscrews completely.

![[19801979.png]]

1. Tighten the capscrews again in the sequence shown.

> [!tip] Момент затяжки · Torque Value
> 2.8 n•m [25 in-lb]

![[19801977.png]]

1. Tighten the capscrews again.

> [!tip] Момент затяжки · Torque Value
> 5.6 n•m [50 in-lb]

This procedure will make sure that the actuator is properly installed.

![[19801978.png]]

Install the module onto the fuel pump, if necessary. [[98-019-030 — EFC Module|Refer to Procedure 019-030]].

![[19801967.png]]

### Resistance Check

Ensure that a digital multimeter is used to measure all the EFC valves electronic parameters.

Disconnect the valve terminal connectors.

Measure the resistance of the EFC valve. Select the resistance function on the multimeter. Touch one of the multimeter leads to one of the valve terminals. Touch the other multimeter lead to the other valve terminal.

![[19801791.png]]

Measure the resistance. The measured resistance should fall in the ranges shown below. If the measured resistance is **not** in these ranges, then replace the EFC valve.

|  | 12-VDC Valve | 24-VDC Valve |
|---|---|---|
| Resistance at 22.2°C \[72°F\] | 2.0 to 2.2 ohms | 7.1 to 7.3 ohms |
| Resistance at -93.2°C \[-40°F\] | 1.5 to 1.7 ohms | 5.3 to 5.5 ohms |
| Resistance at 121.1°C \[250°F\] | 2.8 to 3.0 ohms | 9.9 to 10.1 ohms |

![[19801792.png]]

### Check for Short Circuit to Ground

Touch one of the multimeter leads to either valve terminal. Touch the other multimeter lead to the body of the valve.

Measure the resistance.

The multimeter **must** show more than 100k ohms, which is an open circuit. If the circuit is **not** open, then the valve **must** be replaced.

![[19801793.png]]
