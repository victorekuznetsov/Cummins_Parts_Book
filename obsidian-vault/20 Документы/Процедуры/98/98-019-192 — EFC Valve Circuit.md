---
type: "Процедура"
doc: "98-019-192"
title_en: "EFC Valve Circuit"
modified: "2003-04-01"
engines:
  - "37269910"
  - "37280605"
families:
  - "K19"
manuals:
  - "3666070"
figures: 7
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-019-192.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-019-192.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K19"
  - "группа/98"
---

# EFC Valve Circuit

> [!abstract] Процедура · `98-019-192`
> **Двигатели:** [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]]
> **Семейство:** K19
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-04-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-019-192.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-019-192.pdf)

### Resistance Check

Disconnect the ECM connector.

Make sure that the EFC valve terminal connectors are connected.

Touch one of the multimeter leads to pin 21 of the main engine harness connector. Touch the other multimeter lead to pin 10 of the main engine harness connector.

![[19801794.png]]

Measure the resistance. The measured resistance **must** fall within the ranges shown in the table below. If the measured resistance is **not** within range, repair or replace the main engine harness. Refer to Procedure 019-228 or [[98-019-043 — Engine Wiring Harness|019-043]].

|  | 12VDC Valve | 24VDC Valve |
|---|---|---|
| Resistance at 22.2°C \[72°F\] | 2.0 to 2.2 ohms | 7.1 to 7.3 ohms |
| Resistance at -93.2°C \[-40°F\] | 1.5 to 1.7 ohms | 5.3 to 5.5 ohms |
| Resistance at 121.1°C \[250°F\] | 2.8 to 3.0 ohms | 9.9 to 10.1 ohms |

![[19801795.png]]

### Check for Short Circuit to Ground

Disconnect the ECM connector.

Disconnect the terminal connectors from the EFC valve.

Touch one of the multimeter leads to one of the EFC connectors on the wiring harness. Touch the other multimeter lead to the engine block ground.

![[19801796.png]]

Measure the resistance.

The multimeter **must** show more than 100k ohms, which is an open circuit. If the circuit is **not** open, then there is a short to ground in the main engine harness. Repair or replace the main engine harness. Refer to Procedure 019-228 or [[98-019-043 — Engine Wiring Harness|019-043]].

Repeat the above short circuit to ground check for the other EFC connector on the wiring harness.

![[19801621.png]]

### Check for Short Circuit from Pin to Pin

Disconnect the ECM connector. Disconnect the EFC connectors.

Check for a short circuit between pin 21 of the main engine harness connector and **all** other pins in the connector.

Touch one of the multimeter leads to pin 21 of the main engine harness connector. Touch the other multimeter lead to **all** other pins in the connector, one at a time.

![[19801798.png]]

Measure the resistance.

The multimeter **must** show more than 100k ohms, which is an open circuit. If the circuit is **not** open, then there is a short between the wire connected to pin 21 of the main engine harness connector and **any** other pin that measured less than 100k ohms.

Repair or replace the main engine harness. Refer to Procedure 019-228 or [[98-019-043 — Engine Wiring Harness|019-043]].

![[19801621.png]]

Repeat the above short from pin to pin check for pin 10 of the main engine harness connector.

Touch one of the multimeter leads to pin 10 of the main engine harness connector. Touch the other multimeter lead to **all** other pins in the connector, one at a time.

Measure the resistance. The multimeter **must** show more than 100k ohms.

![[19801800.png]]
