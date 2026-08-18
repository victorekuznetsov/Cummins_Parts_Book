---
aliases:
  - "Цепь датчика положения педали или рычага подачи"
type: "Процедура"
doc: "07-019-086"
title_en: "Accelerator Pedal or Lever Position Sensor Circuit"
title_ru: "Цепь датчика положения педали или рычага подачи"
modified: "2003-12-02"
engines:
  - "93058669"
families:
  - "C8.3 · 6C8.3"
manuals:
  - "4021442"
figures: 16
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-019-086.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/07-019-086.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "группа/07"
---

# Accelerator Pedal or Lever Position Sensor Circuit
**Цепь датчика положения педали или рычага подачи**

> [!abstract] Процедура · `07-019-086`
> **Двигатели:** [[93058669 — 6C8.3 CPL 3105|93058669]]
> **Семейство:** C8.3 · 6C8.3
> **Входит в руководства:** [[4021442 — C8.3 Marine Electronic Control System Troubleshooting and Repair Manual|4021442]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-12-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-019-086.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/07-019-086.pdf)

### Initial Check

> [!warning] CAUTION · Осторожно
> Do not use probes or test leads other than Part Number 3822758 or the connector will be damaged. The test leads must fit tightly in the connector without expanding the pins in the connector.

If the INSITE™ electronic service tool is available, monitor the accelerator position sensor circuit for proper operation.

If **not**, follow the troubleshooting procedures in this section.

![[19900524.png]]

### Resistance Check

> [!warning] CAUTION · Осторожно
> Do not use probes or test leads other than Part Number 3822758 or the connector will be damaged. The test leads must fit tightly in the connector without expanding the pins in the connector.

Disconnect the original equipment manufacturer (OEM) interface harness connector from the electronic control module (ECM).

Make sure the sensor is connected to the OEM harness.

Insert one of the test leads into the accelerator lever supply pin of the OEM interface harness connector.

Insert the other test lead into the accelerator lever return pin of the connector.

![[19901376.png]]

Connect the alligator clips to the multimeter test leads.

Measure the resistance.

The multimeter **must** show 2000 to 3000 ohms when the accelerator lever is at idle or full fuel position

If the resistance is **not** within the specification, there is a problem with the accelerator lever return wire or the accelerator lever supply wire in the OEM interface harness, provided the accelerator position sensor has been checked. Repair the OEM interface harness connector. Refer to Procedure [[99-019-204 — Deutsch DRC Connector Series|019-204]].

Repair the OEM harness according to the vehicle manufacturer's instructions.

![[19901377.png]]

Remove the test lead from the accelerator lever return pin of the OEM interface harness connector and insert it into the accelerator lever signal pin of the connector.

Make sure the accelerator lever is in the idle position.

Measure the resistance.

The multimeter **must** show 1500 to 3000 ohms.

![[19901378.png]]

Move the accelerator lever to the full fuel position and measure the resistance again.

The multimeter **must** show 200 to 1500 ohms.

This resistance value **must** be at least 1000 ohms lower than the resistance value at the low-idle position, measured in the above check.

If the resistance values are **not** within the specification, there is a problem with the accelerator lever supply wire or the accelerator lever signal wire in the OEM harness. Repair the OEM interface harness.

If the resistance values in the two previous checks are within the specification, the accelerator lever return, accelerator lever signal, and accelerator lever supply wires **must** still be checked for a short circuit to ground, a short circuit from pin to pin, and a short circuit to battery supply.

Examine the bulkhead connector and other connectors in the circuit for corrosion or damage to the accelerator position sensor wire terminals.

![[19901379.png]]

### Check for Short Circuit to Ground

> [!warning] CAUTION · Осторожно
> Do not use probes or test leads other than Part Number 3822758 or the connector will be damaged. The test leads must fit tightly in the connector without expanding the pins in the connector.

Disconnect the OEM interface harness connector from the ECM.

Disconnect the accelerator position sensor from the OEM harness at the accelerator lever assembly.

![[19901368.png]]

Insert the test lead into the accelerator lever supply pin of the OEM interface harness connector.

Connect the alligator clip to the multimeter positive (+) probe.

Touch the multimeter negative (-) probe to the engine block and measure the resistance.

The multimeter **must** show an open circuit (100k ohms or more).

Remove the test lead from the accelerator lever supply pin of the OEM interface harness connector and insert it into the accelerator return pin of the connector.

Touch the multimeter negative (-) probe to the engine block and measure the resistance.

The multimeter **must** show an open circuit (100k ohms or more).

Remove the test lead from the accelerator lever return pin of the OEM interface harness connector and insert it into the accelerator signal pin of the connector.

Touch the multimeter negative (-) probe to the engine block and measure the resistance.

The multimeter **must** show an open circuit (100k ohms or more).

If **any** of these three resistance measurements are **not** open, there is a short circuit to ground between the wire connected to the accelerator lever return, accelerator lever signal, or accelerator lever supply pin. Repair the OEM interface harness connector. Refer to Procedure [[99-019-204 — Deutsch DRC Connector Series|019-204]].

Repair the OEM harness according to the vehicle manufacturer's instructions.

Connect the accelerator position sensor after completing the repair.

![[19901407.png]]

### Check for Short Circuit from Pin to Pin

> [!warning] CAUTION · Осторожно
> Do not use probes or test leads other than Part Number 3822758 or the connector will be damaged. The test leads must fit tightly in the connector without expanding the pins in the connector.

Disconnect the accelerator position sensor from the OEM harness at the accelerator lever assembly.

Disconnect the engine harness connector and OEM interface harness connector from the ECM.

![[19901368.png]]

Insert the test lead into the accelerator lever supply pin of the OEM interface harness connector.

Insert the other test lead into the stop lamp pin of the connector.

Connect the clips to the multimeter probes and measure the resistance.

The multimeter **must** show an open circuit (100k ohms or more).

![[19901408.png]]

Remove the test lead from the stop lamp pin and test all other pins of the connector.

Repeat the pin-to-pin check from the accelerator lever supply pin of the OEM interface harness connector to all pins of the engine harness connector.

The multimeter **must** show an open circuit (100k ohms or more) at all pins.

If the multimeter shows a closed circuit at any pin, there is a short circuit between the accelerator lever supply wire and any other wire that measured a closed circuit. Repair the OEM interface harness connector. Refer to Procedure [[99-019-204 — Deutsch DRC Connector Series|019-204]].

Repair the OEM harness according to the vehicle manufacturer's instructions.

![[19901415.png]]

Remove the test lead from the accelerator lever supply pin of the OEM interface harness connector and insert it into the accelerator lever return pin.

Insert the other test lead into the stop lamp pin and measure the resistance.

The multimeter **must** show an open circuit (100k ohms or more).

![[19901408.png]]

Remove the test lead from the stop lamp pin and test all other pins in the connector.

Repeat the pin-to-pin check from the accelerator lever return pin of the OEM interface harness connector to all pins of the engine harness connector.

The multimeter **must** show an open circuit (100k ohms or more) at all pins.

If the multimeter shows a closed circuit at any pin, there is a short circuit between the accelerator lever return wire and any other wire that measured a closed circuit. Repair the OEM interface harness connector. Refer to Procedure [[99-019-204 — Deutsch DRC Connector Series|019-204]].

Repair the OEM harness according to the vehicle manufacturer's instructions.

![[19901415.png]]

Remove the test lead from the accelerator lever return pin of the OEM interface harness connector and insert it into the accelerator lever signal pin.

Insert the other test lead into the stop lamp pin and measure the resistance.

The multimeter **must** show an open circuit (100k ohms or more).

![[19901408.png]]

Remove the test lead from the stop lamp pin and test all other pins of the connector.

Repeat the pin-to-pin check from the accelerator lever signal pin of the OEM interface harness connector to all pins of the engine harness connector.

The multimeter **must** show an open circuit (100k ohms or more) at all pins.

If the multimeter shows a closed circuit at any pin, there is a short circuit between the accelerator lever signal wire and any other wire that measured a closed circuit. Repair the OEM interface harness connector. Refer to Procedure [[99-019-204 — Deutsch DRC Connector Series|019-204]].

Repair the OEM harness according to the vehicle manufacturer's instructions.

![[19901415.png]]

### Check for Short Circuit to External Voltage Source

> [!warning] CAUTION · Осторожно
> Do not use probes or test leads other than Part Number 3822758 or the connector will be damaged. The test leads must fit tightly in the connector without expanding the pins in the connector.

Disconnect the OEM interface harness connector from the ECM.

Disconnect the accelerator position sensor from the OEM harness at the accelerator lever assembly.

![[19901368.png]]

Turn the vehicle keyswitch to the ON position.

Turn the multimeter dial to measure VDC.

Insert one of the test leads into the accelerator lever supply pin of the OEM interface harness connector.

Connect the clip to the multimeter positive (+) probe.

Touch the multimeter negative (-) probe to the engine block and measure the voltage.

The voltage **must** be 1.5 VDC or less.

Remove the test lead from the accelerator lever supply pin of the OEM interface harness connector and insert it into the accelerator lever return pin of the connector.

Touch the multimeter negative (-) probe to the engine block and measure the voltage.

The voltage **must** be 1.5 VDC or less.

Remove the test lead from the accelerator lever return pin of the OEM interface harness connector and insert it into the accelerator lever signal pin of the connector.

Touch the multimeter negative (-) probe to the engine block and measure the voltage.

The voltage **must** be 1.5 VDC or less.

If more than 1.5 VDC is measured at any pin, there is a short circuit from the accelerator lever return, signal, or supply wire to a wire carrying power. Repair the OEM interface harness connector. Refer to Procedure [[99-019-204 — Deutsch DRC Connector Series|019-204]].

Repair the OEM harness according to the vehicle manufacturer's instructions.

Connect the accelerator position sensor after completing the repair.

> [!missing]- Иллюстрация `19901416.png` не извлечена — смотрите PDF-оригинал документа
