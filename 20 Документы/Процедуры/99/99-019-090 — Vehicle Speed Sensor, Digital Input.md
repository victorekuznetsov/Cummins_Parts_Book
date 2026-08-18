---
aliases:
  - "Датчик скорости машины, цифровой вход"
type: "Процедура"
doc: "99-019-090"
title_en: "Vehicle Speed Sensor, Digital Input"
title_ru: "Датчик скорости машины, цифровой вход"
modified: "2015-06-29"
engines:
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 7
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-090.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/99-019-090.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/99"
---

# Vehicle Speed Sensor, Digital Input
**Датчик скорости машины, цифровой вход**

> [!abstract] Процедура · `99-019-090`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section 19 - Electronic Engine Controls
> **Даты:** изменён 2015-06-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-090.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/99-019-090.pdf)

### General Information

The digital input signal device is an OEM optional part. It changes the signal pulses from AC to DC. This part is near the transmission or in the vehicle cab. The DC voltage pulses are then sent to the ECM and computed into miles per hour.

![[ee8mpgd.png]]

The digital vehicle speed sensor circuit consists of the speed sensor, the digital vehicle speed sensor +5 volt supply wire, the digital vehicle speed sensor signal wire, and the digital vehicle speed sensor return wire.

![[nobox.png]]

> [!warning] CAUTION · Осторожно
> When the OEM-supplied signal conditioner is internally grounded, do not connect the vehicle speed sensor signal negative (-) wire to the ECM. This will create a ground loop in the system that will inject unwanted electrical noise into the system. Only the digital vehicle speed sensor +5 volt supply wire is required in this case.

![[nobox.png]]

### Resistance Check

> [!warning] CAUTION · Осторожно
> Proper leads and/or a Cummins® approved circuit testing tool must be used when working with electrical connectors to prevent pin expansion and damage to the connector.

Disconnect the original equipment manufacturer (OEM) harness engine interface connector. To determine the location of the connector, see the corresponding engine wiring diagram.

Disconnect the digital vehicle speed sensor from the OEM harness.

Insert a test lead into the digital vehicle speed sensor +5 volt supply pin in the OEM harness connector, and connect it to the multimeter probe.

![[19c01387.png]]

Insert the other test lead to the digital vehicle speed sensor +5 volt supply in the vehicle speed sensor connector and connect the alligator clip to the other multimeter probe. Adjust the multimeter to the resistance setting and measure the resistance.

The multimeter **must** show a closed circuit (10 ohms or less).

If the circuit is **not** closed, there is an open circuit. Repair or replace the wire connected to the digital vehicle speed sensor +5 volt supply pin in the OEM harness according to the vehicle manufacturer's procedures.

Remove the lead from the digital vehicle speed sensor +5 volt supply pin and insert it into the digital vehicle speed sensor signal pin of the OEM harness connector. Remove the multimeter lead from the digital vehicle speed sensor +5 volt supply at the speed sensor connector and connect it to the digital vehicle speed sensor signal pin in the vehicle speed sensor connector. Measure the resistance.

The multimeter **must** show a closed circuit (10 ohms or less).

If the circuit is **not** closed, there is an open circuit. Repair or replace the wire connected to the vehicle speed sensor signal pin in the OEM harness according to the vehicle manufacturer's procedures.

Remove the lead from the digital vehicle speed sensor signal pin and insert it into the digital vehicle speed sensor return pin of the OEM harness connector. Remove the multimeter lead from the digital vehicle speed sensor signal pin at the speed sensor connector and connect it to the digital vehicle speed sensor return pin in the vehicle speed sensor connector. Measure the resistance.

The multimeter **must** show a closed circuit (10 ohms or less).

If the circuit is **not** closed, there is an open circuit. Repair or replace the wire connected to the vehicle speed sensor return pin in the OEM harness according to the vehicle manufacturer's procedures.

If the values are correct, the circuit **must** still be checked for a short circuit to ground and a short circuit from pin-to-pin.

> [!missing]- Иллюстрация `19c01385.png` не извлечена — смотрите PDF-оригинал документа

### Check for Short Circuit to Ground

Disconnect the vehicle speed sensor from the OEM harness. Disconnect the original equipment manufacturer (OEM) harness engine interface connector. To determine the location of the connector, see the corresponding engine wiring diagram.

Insert a test lead into the digital vehicle speed sensor signal return pin of the OEM harness connector, and connect it to the multimeter probe. Touch the other multimeter probe to the engine block ground. Measure the resistance.

The multimeter **must** show an open circuit (100k ohms or more).

Remove the test lead from the digital vehicle speed sensor signal return pin and insert it into the digital vehicle speed sensor +5 volt supply pin of the OEM harness connector. Touch the other multimeter probe to the engine block ground. Measure the resistance.

The multimeter **must** show an open circuit (100k ohms or more).

Remove the test lead from the digital vehicle speed sensor signal +5 volt supply pin and insert it into the digital vehicle speed sensor signal pin of the OEM harness connector. Touch the other multimeter probe to the engine block ground. Measure the resistance.

The multimeter **must** show an open circuit (100k ohms or more).

If the circuit is **not** open in either of these checks, there is a short circuit to ground in the digital vehicle speed sensor circuit in the OEM harness.

Repair the wires which have a short circuit according to the vehicle manufacturer's procedures.

![[19c01154.png]]

### Check for Short Circuit from Pin to Pin

Disconnect the vehicle speed sensor from the OEM harness.

Disconnect the original equipment manufacturer (OEM) harness engine interface connector. To determine the location of the connector, see the corresponding engine wiring diagram.

Insert one test lead into the digital vehicle speed sensor +5 volt supply pin of the OEM harness connector, and connect it to the multimeter probe. Connect the other test lead to the other multimeter probe and check all pins in the OEM harness connector.Measure the resistance.

The multimeter **must** show an open circuit at all pins (100k ohms or more).

Remove the test lead from the digital vehicle speed sensor +5 volt supply pin, and insert it into the digital vehicle speed sensor signal return pin.

Use the other test lead to check all pins in the connector. Measure the resistance.

The multimeter **must** show an open circuit (100k ohms or more).

Remove the test lead from the digital vehicle speed sensor return pin, and insert it into the digital vehicle speed sensor signal signal pin.

Use the other test lead to check all pins in the connector. Measure the resistance.

The multimeter **must** show an open circuit (100k ohms or more).

If the circuit is **not** open in any of the checks, repair the wires that have the short circuit according to the vehicle manufacturer's procedures.

> [!note] Note · Примечание
> If the values are correct for all of the circuit checks in Procedure 019-090, the vehicle speed sensor circuit is good.

The problem is in the vehicle speed sensor. Repair or replace the vehicle speed sensor according to the vehicle manufacturer's procedures.

![[19c01236.png]]
