---
aliases:
  - "Цепь клапана отсечки топлива"
type: "Процедура"
doc: "60-019-049"
title_en: "Fuel Shutoff Valve Circuit"
title_ru: "Цепь клапана отсечки топлива"
modified: "2007-12-19"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021674"
figures: 10
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-019-049.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-019-049.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
---

# Fuel Shutoff Valve Circuit
**Цепь клапана отсечки топлива**

> [!abstract] Процедура · `60-019-049`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section 19 — Electronic Engine Controls — Group 19
> **Даты:** изменён 2007-12-19
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-019-049.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-019-049.pdf)

### Initial Check

Inspect the fuel shutoff solenoid post for extra wires that are possibly connected to supply power to another device. Remove any extra wires that are found connected to the solenoid post.

![[19400454.png]]

Check that the terminal post is **not** in contact with any metallic object other than the harness terminal. Turning the Run/Stop switch to Run signals the ECM to open the fuel shutoff solenoid valve. The solenoid closes when the ECM senses the Run/Stop switch is set to Stop or when the ECM senses an engine protection condition.

![[19400742.png]]

### Preparatory Steps

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

- Disconnect the batteries. Refer to Procedure 013-009 (Battery Cables) in Section 13 in the Service Manual, QST30, Bulletin [[4021539 — QST30 Service Manual\|4021539]].

![[ck800wa.png]]

### Resistance Check

The fuel shutoff valve is a two-post solenoid. Therefore, it has both a signal wire and a ground wire through the harness to the ECM. Disconnect the fuel shutoff valve solenoid terminals from the terminal posts. Check for damaged terminals.

![[19802549.png]]

Disconnect the ECM1 50-pin and ECM2 50-pin connectors.

Inspect the pins in the ECM connectors for damage.

![[19a00841.png]]

> [!warning] CAUTION · Осторожно
> Do not use probes or leads other than Part Number 3822917. The connector will be damaged. The leads must fit tightly in the connector without expanding the pins of the connector.

Insert a test lead into the fuel shutoff valve signal pin at the engine harness. Insert a test lead into the battery 1 voltage return pin at the engine harness.

Touch the other multimeter lead to the fuel shutoff valve signal ring terminal. Measure the resistance. The multimeter **must** show a closed circuit (10 ohms or less). If the circuit is **not** closed, repeat this procedure at the engine harness connector. If it still does **not** show a closed circuit, repair or replace the engine harness.

- [[99-019-197 — Ring Terminal|Refer to Procedure 019-197 (Ring Terminal) in Section 19.]]
- [[99-019-199 — Connector, Butt Splice|Refer to Procedure 019-199 (Connector, Butt Splice) in Section 19.]]
- [[99-019-219 — Danfoss™ (Circular DIN Series) Connector|Refer to Procedure 019-219 (Danfoss (Circular DIN Series) Connection)) in Section 19.]]
- [[60-019-043 — Engine Wiring Harness|Refer to Procedure 019-043 (Engine Wiring Harness) in Section 19.]]

If the test at the engine harness shows a closed circuit, repair, or replace the engine harness.

- [[99-019-219 — Danfoss™ (Circular DIN Series) Connector|Refer to Procedure 019-219 (Danfoss (Circular DIN Series) Connector) in Section 19.]]
- [[99-019-213 — D-Sub Miniature Connector Series|Refer to Procedure 019-213 (D-Sub Miniature Connector Series) in Section 19.]]
- Contact an Authorized Cummins® Repair location for Extension Wiring Harness information.

If the circuit is closed, it **must** still be checked for a short to ground and a short from pin to pin.

Insert a test lead into the battery 1 voltage return pin at the engine harness.

Connect the alligator clip to the multimeter probe.

Touch the other multimeter lead to the fuel shutoff valve return ring terminal. Measure the resistance. The multimeter **must** show a closed circuit (10 ohms or less). If the circuit is **not** closed, repeat this procedure at the engine harness connector. If it still does **not** show a closed circuit, repair or replace the engine harness.

- [[99-019-197 — Ring Terminal|Refer to Procedure 019-197 (Ring Terminal) in Section 19.]]
- [[99-019-199 — Connector, Butt Splice|Refer to Procedure 019-199 (Connector, Butt Splice) in Section 19.]]
- [[99-019-219 — Danfoss™ (Circular DIN Series) Connector|Refer to Procedure 019-219 (Danfoss (Circular DIN Series Connector)) in Section 19.]]
- [[60-019-043 — Engine Wiring Harness|Refer to Procedure 019-043 (Engine Wiring Harness) in Section 19.]]

![[19a00842.png]]

### Check for Short Circuit to Ground

Insert the electrical lead into the fuel shutoff valve signal at the engine harness connector pin. Touch the other multimeter probe to engine block. The ring terminal at the solenoid **must** be disconnected and can **not** touch anything that is grounded. Measure the resistance. The multimeter **must** show an open circuit (more than 100K ohms). If the circuit is **not** open, there is a short to ground in the fuel shutoff valve signal wire. Repair or replace the engine harness.

- [[99-019-197 — Ring Terminal|Refer to Procedure 019-197 (Ring Terminal) in Section 19.]]
- [[99-019-199 — Connector, Butt Splice|Refer to Procedure 019-199 (Connector, Butt Splice) in Section 19.]]
- [[99-019-219 — Danfoss™ (Circular DIN Series) Connector|Refer to Procedure 019-219 (Danfoss (Circular DIN Series) Connector) in Section 19.]]
- [[60-019-043 — Engine Wiring Harness|Refer to Procedure 019-043 (Engine Wiring Harness) in Section 19.]]

![[19a00844.png]]

### Check for Short Circuit from Pin to Pin

Check for a short circuit from the fuel shutoff valve signal pin to all other pins in the engine harness connector. Connect a test lead from the fuel shutoff valve signal pin in the engine harness connector. Connect the alligator clip of a second test lead to the other multimeter probe. Insert the pin of the lead into all of the other pins in the actuator.

The ring terminals at the solenoid **must** be disconnected and can **not** touch anything that is grounded. The battery voltage supply **must** be disconnected.

Measure the resistance. The multimeter **must** show an open circuit (more than 100k ohms). If the circuit is **not** open, there is a short between the fuel shutoff value signal pin and **any** pin that measured a closed circuit. Repair or replace the engine harness.

- [[99-019-197 — Ring Terminal|Refer to Procedure 019-197 (Ring Terminal) in Section 19.]]
- [[99-019-199 — Connector, Butt Splice|Refer to Procedure 019-199 (Connector, Butt Splice) in Section 19.]]
- [[99-019-219 — Danfoss™ (Circular DIN Series) Connector|Refer to Procedure 019-219 (Danfoss (Circular DIN Series) Connector) in Section 19.]]
- [[60-019-043 — Engine Wiring Harness|Refer to Procedure 019-043 (Engine Wiring Harness) in Section 19.]]

Repeat the above steps at the ECM3 engine harness connector harness. If the circuit is **not** open, there is a short between the fuel shutoff value signal pin and **any** pin that measured a closed circuit. Repair or replace the extension harness. [[99-019-219 — Danfoss™ (Circular DIN Series) Connector|Refer to Procedure 019-219 (Danfoss (Circular DIN Series) Connector) in Section 19.]] [[99-019-213 — D-Sub Miniature Connector Series|Refer to Procedure 019-213 (D-Sub Miniature Connector Series) in Section 19.]] Contact an Authorized Cummins® Repair location for Extension Wiring Harness information.

![[19a00836.png]]

### Check for Short Circuit to External Voltage Source

Check for a short circuit from the fuel shutoff valve circuit to a +24-VDC source. Disconnect the extension harness connector from the ECM. Connect the battery voltage supply if it has been disconnected. Set the Run/Stop switch to the Run position. Adjust the multimeter to measure VDC. Insert a test lead into the fuel shutoff valve signal pin; connect it to the multimeter. Touch the other multimeter probe to the engine block ground.

> [!note] Note · Примечание
> An external voltage source is any wire in the OEM wiring that carries voltage.

Measure the voltage. The voltage **must** be 1.5-VDC or less. If the voltage is **not** correct, there is a short circuit between the fuel shutoff valve circuit and an external voltage source. Remove the external voltage source.

Connect all components after the repair is complete.

![[19a00844.png]]

### Finishing Steps

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

- Connect the batteries. Refer to Procedure 013-009 (Battery Cables) in Section 13 in the Service Manual, QST30, Bulletin [[4021539 — QST30 Service Manual\|4021539]].

![[ck800wa.png]]
