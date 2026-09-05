---
type: "Процедура"
doc: "493-011-165"
title_en: "Aftertreatment Diesel Exhaust Fluid Dosing Unit Circuit Load Test"
modified: "2023-05-08"
manuals:
  - "5411181"
figures: 2
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/493/493-011-165.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/493-011-165.pdf"
tags:
  - "документ/процедура"
  - "группа/493"
---

# Aftertreatment Diesel Exhaust Fluid Dosing Unit Circuit Load Test

> [!abstract] Процедура · `493-011-165`
> **Входит в руководства:** [[5411181 — X15 CM2350 X114B - Efficiency Series Service Manual|5411181]]
> **Секции:** Section 11 - Exhaust System - Group 11
> **Даты:** изменён 2023-05-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/493/493-011-165.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/493-011-165.pdf)

### Select Service Tools

#### Recommended Cummins® Service Tools

- Multimeter Kit, Part Number 3400162, or equivalent
- Circuit load tester, Part Number 5394709, or Electronic Specialties 180 LOADpro® Dynamic Test Leads, or equivalent
- Test Lead Kit, Part Number 5299367, or equivalent.

#### Additional Service Items

- No additional service items required.

### General Information

![[22r00151.png]]

The purpose of this test is to check the resistance between the aftertreatment diesel exhaust fluid (DEF) dosing unit and the original equipment manufacturer (OEM) wiring harness. Use circuit load tester, Part Number 5394709, or Electronic Specialties 180 LOADpro® Dynamic Test Leads, to check the resistance between the DEF dosing unit and OEM wiring harness.

### Test

> [!warning] CAUTION · Осторожно
> Any probe that supplies battery voltage or a ground is not to be utilized during this test procedure.

- Verify the vehicle batteries are charged to normal levels.
- Turn the keyswitch OFF to allow the engine control module (ECM) to power down.
- Disconnect the DEF dosing unit from the harness.
- Disconnect the DEF dosing unit relay.
- Place a jumper between the DEF dosing unit relay power and DEF dosing unit Supply on the DEF dosing unit relay connector.
- Connect Circuit load tester, Part Number 5394709, or Electronic Specialties 180 LOADpro® Dynamic Test Leads, or equivalent to multimeter.
- Connect the positive circuit load tester probe to the DEF dosing unit SUPPLY in the DEF pump harness connector and the negative circuit load tester probe to the DEF dosing unit RETURN in the DEF pump harness connector.
- This value is open load voltage. Record the open load voltage.

![[19l00301.png]]

1. Harness pins to install jumper wire
2. Harness pins to measure voltage drop.

- Press the button on the circuit load tester and record the voltage.
- Subtract the voltage with the button pressed from the open load voltage. This value is the voltage drop on the circuit.
- Voltage drop on the circuit should be less than 0.5 VDC.
- When complete, remove the jumper and reconnect the relay and DEF pump.

### Finishing Steps

- Connect the DEF dosing unit relay.
- Connect the DEF dosing unit to the harness.
