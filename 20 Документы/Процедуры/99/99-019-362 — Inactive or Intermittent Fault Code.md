---
aliases:
  - "Неактивный или перемежающийся код неисправности"
type: "Процедура"
doc: "99-019-362"
title_en: "Inactive or Intermittent Fault Code"
title_ru: "Неактивный или перемежающийся код неисправности"
modified: "2022-02-23"
engines:
  - "37292556"
  - "37295879"
  - "41343322"
  - "93058669"
families:
  - "C8.3 · 6C8.3"
  - "NT/NTA855 · ISM/QSM11"
  - "QST30"
manuals:
  - "3666184"
  - "3666214"
  - "3666266"
  - "4021419"
  - "4021442"
  - "4021674"
figures: 12
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-362.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/99-019-362.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "двигатель/NT/NTA855"
  - "двигатель/QST30"
  - "группа/99"
---

# Inactive or Intermittent Fault Code
**Неактивный или перемежающийся код неисправности**

> [!abstract] Процедура · `99-019-362`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]], [[41343322 — NH NT 855 CPL 3362|41343322]], [[93058669 — 6C8.3 CPL 3105|93058669]]
> **Семейство:** C8.3 · 6C8.3, NT/NTA855 · ISM/QSM11, QST30
> **Входит в руководства:** [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual|3666184]], [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]], [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]], [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]], [[4021442 — C8.3 Marine Electronic Control System Troubleshooting and Repair Manual|4021442]], [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section 19 - Electronic Engine Controls · Section 19 - Electronic Engine Controls - Group 19 · Section 19 — Electronic Engine Controls — Group 19
> **Даты:** изменён 2022-02-23
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-362.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/99-019-362.pdf)

### General Information

This procedure is designed to troubleshoot electrical circuit faults that are intermittent and are currently inactive. This procedure can also be used to troubleshoot high inactive counts of circuit related fault codes.

If multiple fault codes are present, use a wiring diagram to check for common sensor supplies and ground circuits that may be shared between sensors, actuators, and switches. Pressure sensors may share a common 5 volt supply and ground circuit. Temperature sensors and actuators may share a common ground circuit. If either a sensor supply or a ground circuit has an intermittent connection, fault codes related to all the sensors may be active or have high counts of inactive fault codes.

If the conditions for a fault code to trigger exist and then the conditions are no longer present, an inactive fault code is created. When conditions are intermittent, there may be multiple inactive counts for a given fault code. If there are more than 10 inactive counts, the fault code should be troubleshot as an active fault code. Troubleshooting priority should be given to fault codes that are associated engine performance.

### Initial Check

Interview the operator and determine the engine operating conditions when the fault occurs and what symptoms occur when the fault is active.

Determine if there have been any recent service repairs or maintenance performed that may be related to the intermittent condition.

Review the “Shop Talk” section of the fault code troubleshooting tree. Shop Talk will give additional troubleshooting information and will list possible causes for the fault code.

Verify the electronic control module (ECM) calibration is correct. Check the calibration revision history found on QuickServe® Online for applicable fixes for the ECM calibration. If necessary, recalibrate the ECM. See procedure 019-032 Engine Control Module Calibration Code.

![[19800902.png]]

Disconnect the sensor or actuator related to the intermittent condition.

Inspect the wiring harness and connector for the following:

- Loose connector (gently pull the wires at the back of the connectors)
- Corroded pins
- Bent or broken pins
- Pushed back or expanded pins
- Moisture in or on the connectors
- Dirt or debris in, or on, the connector pins
- Missing or damaged connector seals
- Wire insulation damage
- Connector shell broken
- Damaged locking tab connector
- Pin wear (close visual inspection)
- Rusty, painted, corroded, or loose grounds.

Thoroughly inspect the wiring harness between the suspected component and ECM connection. Check for the proper strain relief on the wiring harness.

A dark powder found inside the connector may be a sign of pin fretting. Clean the pin contacts and reconnect the connector.

![[19400450.png]]

Disconnect the wiring harness connector from the ECM. Inspect the ECM connector for the following:

- Loose connector (gently pull the wires at the back of the connectors)
- Corroded pins
- Bent or broken pins
- Pushed back or expanded pins
- Moisture in or on the connectors
- Dirt or debris in, or on, the connector pins
- Missing or damaged connector seals
- Wire insulation damage
- Connector shell broken
- Damaged locking tab connector
- Pin wear (close visual inspection)
- Rusty, painted, corroded, or loose grounds.

![[19400450.png]]

Clean connector(s) of any components related to the fault code. Use Cummins® service tool, Part Number 3823290, QD® contact cleaner or equivalent.

Clear all fault codes.

![[19801316.png]]

Harness Shake Test

Connect a recommended Cummins® electronic service tool or equivalent and open the Data Monitor/Logger feature.

Monitor the sensor signal voltage for the appropriate sensor or component.

Monitor the actual value of the sensor or component.

![[19800902.png]]

Beginning at the component in question and working back through the harness to the ECM, gently twist, bend and pull at each connection and in between connections in the harness.

While performing the Harness Shake Test, the sensor signal voltage that the electronic service tool displays should remain steady. A typical reading should be between 0.5 and 5.12 volts.

> [!note] Note · Примечание
> This procedure can also be used to check for loose or damaged wires for switches. Switch status can be monitored with an electronic service tool. Look for switch changes when performing the Harness Shake Test.

![[19803637.png]]

If the fault code goes active, inactive counts increase, the sensor signal voltage fluctuates, or the switch status changes, there is a loose connection or damaged wire at that specific location. Inspect the pins at the corresponding connectors. [[99-019-361 — Component Connector and Pin Inspection|Refer to Procedure 019-361]].

> [!note] Note · Примечание
> The ECM will **not** change the status of switches and faults instantaneously. Approximately 10 to 15 seconds should be used to gently twist the harness and see a reading change from the ECM. Monitoring too many parameters at one time with an electronic service tool will slow down the update rate on the screen. Keep the number of parameters monitored with the electronic service tool to minimum to increase the update rate.

![[19800902.png]]

Start the engine.

Monitor the sensor signal voltage for the appropriate sensor. Also monitor the actual value of the sensor or component.

While performing the Harness Shake Test, the sensor signal voltage that the electronic service tool displays should remain steady. A typical reading should be between 0.5 and 5.12 volts.

Now gently bend, twist, and pull the connections and in between connections in the harness while monitoring the sensor signal voltage.

If the sensor signal voltage fluctuates during the test, then there is a loose connection or damaged wire at that specific location. Inspect the pins at the connectors in question. Repair or replace as necessary. [[99-019-361 — Component Connector and Pin Inspection|Refer to Procedure 019-361]].

![[nobox.png]]

Ground Circuit Check

Check for poor battery and chassis grounds. Firmly pull on ground wires or cables checking for loose connections. Check the following grounds making sure they are secure, clean, and on a non-painted surface:

- Engine block grounds.
- Chassis grounds
- ECM grounds.
- Alternator negative (-) post.
- Starter negative (-) post.

While performing this step, check to see if the fault code goes active, or if inactive counts increase. If this happens, there is a loose connection or damaged wire at that location. Disconnect, clean grounding cables and grounding surfaces, then reconnect. Repair or replace grounding cables or wires if necessary.

![[19803636.png]]

Use a multimeter to measure resistance. [[99-019-359 — Multimeter Usage|Refer to Procedure 019-359]].

Measure resistance from the battery negative (-) post to:

- ECM casing (clean, non-painted surface).
- Engine block (clean, non-painted surface).
- Starter negative (-) post.
- Alternator negative (-) post.
- Chassis grounds.

All resistance values should measure less than 1 ohm. If resistance values exceed 1 ohm, clean grounding cables and grounding surfaces, then reconnect. Repair or replace grounding cables or wires if necessary.

![[19803635.png]]

### Voltage Check

This test **must** be performed with the sensor or actuator connected to the wiring harness.

With the sensor or actuator disconnected from the wiring harness, measure the voltage at the engine harness connector of the component.

Connect the sensor or actuator to the wiring harness and measure the voltage with all the components connected. Use a breakout cable or back-probe the connector with the multimeter leads when performing this check.

The voltage to the component should be within 0.5 volts of the original voltage measured. If the voltage drops more than 0.5 volts, check for intermittent connections, cut wires, or corroded relay connections between the actuator and the ECM.

> [!missing]- Иллюстрация `19c00095.png` не извлечена — смотрите PDF-оригинал документа

### Sensor Accuracy Check

When a sensor circuit is shorted high or shorted low, the sensor value will be locked to a default value when the fault code is active. The default value will usually be set to a value that is within the standard operating range of the sensor. When monitoring the sensor values with a service tool it will appear as if the sensor is reading a correct value even when the fault code is active.

Be aware when troubleshooting intermittent circuit fault codes that the value displayed with a service tool could be a default sensor reading. Always use the sensor signal voltage measurement when troubleshooting intermittent circuit fault codes.

If further investigation is necessary, use the Data Monitor/Logger feature in an electronic service tool to monitor the inputs and outputs of a running engine and to capture data to a log file. The data logger feature in an electronic service tool will allow for information to be captured during the intermittent event and can reviewed at a later time.

![[19800902.png]]
