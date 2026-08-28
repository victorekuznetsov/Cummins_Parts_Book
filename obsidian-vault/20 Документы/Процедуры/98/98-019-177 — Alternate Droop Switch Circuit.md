---
aliases:
  - "Цепь выключателя альтернативного статизма"
type: "Процедура"
doc: "98-019-177"
title_en: "Alternate Droop Switch Circuit"
title_ru: "Цепь выключателя альтернативного статизма"
modified: "2003-04-01"
engines:
  - "37269910"
  - "37280605"
families:
  - "K19"
manuals:
  - "3666070"
figures: 15
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-019-177.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-019-177.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K19"
  - "группа/98"
---

# Alternate Droop Switch Circuit
**Цепь выключателя альтернативного статизма**

> [!abstract] Процедура · `98-019-177`
> **Двигатели:** [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]]
> **Семейство:** K19
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-04-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-019-177.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-019-177.pdf)

### General Information

The portion of the switch circuit in the main engine harness consists of the signal wire connected to pin 28 of the main engine harness connector and the intermediate speed/alternate droop validation wire connected to pin 2.

To check the OEM portion of the alternate droop switch circuit, refer to Procedure 019-071.

The switch is located on the driver interface panel.

![[19801738.png]]

> [!note] Note · Примечание
> **Not** all CENTRY™ applications use intermediate speed/alternate droop validation. Some applications will use a relay or remotely mounted switch instead of an interface panel switch. Refer to the OEM troubleshooting and repair manual to see how a particular system is wired.

![[nobox.png]]

### Resistance Check

If an electronic service tool is available, then the switch should be monitored for proper operation. If the switch is changing state correctly on the service tool, then the problem does **not** lie in the switch circuit. If an electronic service tool is **not** available, check the switch manually.

Locate the switch on the driver interface panel and remove it.

Refer to the OEM troubleshooting and repair manual for the procedure.

![[19801910.png]]

Disconnect the wires connected to the switch (wire Nos. C6-C, C6-D, C6-H).

> [!note] Note · Примечание
> The switch is a normally open switch.

Select the resistance function on the multimeter.

Touch the multimeter leads to the terminals on the switch.

Toggle the switch to the OFF (open) position.

![[19801912.png]]

Measure the resistance.

The multimeter **must** show more than 100k ohms, which is an open circuit. If the circuit is **not** open, then there is a short circuit within the switch.

Replace the switch. Refer to the OEM troubleshooting and repair manual for the procedure.

![[19801621.png]]

Toggle the switch to the ON position.

Measure the resistance. The multimeter **must** show less than 10 ohms, which is a closed circuit. If the circuit is **not** closed, then there is an open circuit within the switch.

Replace the switch. Refer to the OEM troubleshooting and repair manual for the procedure.

![[19801914.png]]

Check the main engine harness portion of the alternate droop switch circuit.

Disconnect ECM connector and the C5 connector.

Touch one of the multimeter leads to pin 28 of the main engine harness connector. Touch the other multimeter lead to pin D of the main engine harness side of the C5 connector.

![[19801739.png]]

Measure the resistance.

The multimeter **must** show less than 10 ohms, which is a closed circuit. If the circuit is **not** closed, then there is a open circuit in the signal wire.

Repair the main engine harness, or, if necessary, replace it. Refer to Procedure 019-228 or [[98-019-043 — Engine Wiring Harness|019-043]].

![[19801619.png]]

Repeat the above resistance check for the alternate droop validation wire.

Touch one of the multimeter leads to pin 2 of the main engine harness connector. Touch the other multimeter lead to pin C of the main engine harness side of the C5 connector.

Measure the resistance. The multimeter **must** show less than 10 ohms.

![[19801741.png]]

### Check for Short Circuit to Ground

Make sure the ECM connector and the C5 connector are disconnected.

Touch one of the multimeter leads to pin 28 of the main engine harness connector. Touch the other multimeter lead to a good, clean surface on the engine block.

![[19801742.png]]

Measure the resistance.

The multimeter **must** show more than 100k ohms, which is an open circuit. If the circuit is **not** open, then there is a short circuit between the wire connected to pin 28 and chassis ground.

Repair the main engine harness, or, if necessary, replace it. Refer to Procedure 019-228 or [[98-019-043 — Engine Wiring Harness|019-043]].

![[19801621.png]]

Repeat the above short to ground check for the alternate droop validation wire.

Touch one of the multimeter leads to pin 2 of the main engine harness connector. Touch the other multimeter lead to a good, clean surface on the engine block.

Measure the resistance. The multimeter **must** show more than 100k ohms.

![[19801744.png]]

### Check for Short Circuit from Pin to Pin

Make sure the ECM connector and the C5 connector are disconnected.

Check for a short circuit between pin 28 of the main engine harness connector and **all** other pins in the connector.

Touch one of the multimeter leads to pin 28 of the main engine harness connector. Touch the other multimeter lead to **all** other pins in the connector, one at a time.

![[19801745.png]]

Measure the resistance.

The multimeter **must** show more than 100k ohms, which is an open circuit. If the circuit is **not** open, then there is a short between the wires connected to pin 28 of the main engine harness and **any** other pin that measured less than 100k ohms.

Repair the main engine harness, or, if necessary, replace it. Refer to Procedure 019-228 or [[98-019-043 — Engine Wiring Harness|019-043]].

![[19801621.png]]

Repeat the above short pin to pin check for the alternate droop validation wire.

Touch one of the multimeter leads to pin 2 of the main engine harness connector. Touch the other multimeter lead to **all** other pins in the connector, one at a time.

Measure the resistance.

The multimeter **must** show more than 100k ohms.

![[19801747.png]]
