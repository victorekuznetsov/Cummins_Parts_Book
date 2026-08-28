---
type: "Процедура"
doc: "98-fc414"
title_en: "SAE J1587/J1922 Datalink - Abnormal Update Rate"
modified: "2021-09-10"
engines:
  - "37269910"
  - "37280605"
families:
  - "K19"
manuals:
  - "3666070"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-fc414.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-fc414.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K19"
  - "группа/98"
---

# SAE J1587/J1922 Datalink - Abnormal Update Rate

> [!abstract] Процедура · `98-fc414`
> **Двигатели:** [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]]
> **Семейство:** K19
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2021-09-10
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-fc414.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-fc414.pdf)

### Fault Code: 414

### SAE J1587/J1922 Datalink - Abnormal Update Rate

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 414 PID(P): S250 SPN: FMI: 9 Lamp: On SRT: 00-632 | An abnormal update rate has been detected on the J1587/1922 data link. | None |

![[19802306.png]]

Datalink Circuit

### Circuit Description

The J1587/1922 data link is a public data link that broadcasts engine operating data as well as fault codes.

### Component Location

The J1587/1922 datalink is located in the engine wiring harness between the ECM and the datalink connectors.

### Conditions For Running The Diagnostics

This diagnostic runs continuously when the keyswitch is in the ON position.

### Conditions For Setting The Fault Codes

The Engine Control Module (ECM) has detected the J1587/1992 datalink communications is transmitting abnormally.

### Action Taken When The Fault Code Is Active

- The ECM logs the fault code immediately when the diagnostic runs and fails.

For Power Generation Applications:

- The generator set controller displays the fault immediately when the diagnostics runs and fails.

### Conditions For Clearing The Fault Code

- Turn the keyswitch OFF. Allow the ECM to completely power down and turn the keyswitch ON.

- The fault code status displayed by the recommended Cummins® electronic service tool or equivalent will change to INACTIVE immediately after the diagnostic runs and passes.

- The “Reset All Faults” command in the recommended Cummins® electronic service tool or equivalent can be used to clear active and inactive faults.

For Power Generation Applications:

- To validate the repair, start the engine and let it run for 1 minute at no load.

- The generator set controller will turn off the fault code immediately after the user presses reset.

- The “Reset All Faults” command in the recommended Cummins® electronic service tool or equivalent can be used to clear active faults.

### Shoptalk

Possible causes of this fault code include:

- Malfunctioning or damaged engine wiring harness.

- Malfunctioning or damaged OEM wiring harness.

- Damaged or loose connections.

Refer to Troubleshooting Fault Code t05-414
