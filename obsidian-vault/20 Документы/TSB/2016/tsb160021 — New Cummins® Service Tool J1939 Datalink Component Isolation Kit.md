---
type: "TSB"
doc: "tsb160021"
title_en: "New Cummins® Service Tool: J1939 Datalink Component Isolation Kit"
modified: "2024-10-04"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2016/tsb160021.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb160021.pdf"
tags:
  - "документ/tsb"
---

# New Cummins® Service Tool: J1939 Datalink Component Isolation Kit

> [!abstract] TSB · `tsb160021`
> **Даты:** изменён 2024-10-04
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2016/tsb160021.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb160021.pdf)

## New Cummins® Service Tool: J1939 Datalink Component Isolation Kit

### Warranty Statement

The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.

### Contents

**Product Affected**

- All CM2350 engines equipped with J1939 components

**Description of Change**

This document introduces a new Cummins® service tool to help troubleshoot J1939 components that will **not** communicate with the engine control module (ECM). The J1939 Datalink Component Isolation Kit allows the technician to isolate/bypass the J1939 datalink harness by using a base tool harness with appropriate adapters.

**Service Instructions**

> [!warning] CAUTION · Осторожно
> Some components tested with this kit operate on 12 volts of direct current (VDC) and some operate on 24 VDC. Applying incorrect voltage may cause damage.

> [!warning] CAUTION · Осторожно
> Several adapter harness in the kit use the same non-key connector with different wiring. Using an adapter harness with incorrect wiring for the component being tested may cause component damage.

1. Locate the component on the vehicle for troubleshooting. Make note of operating voltage of the component. Reference the Software Calibration (SC) option on QuickServe® Online (QSOL) to determine system voltage.
2. Unplug the component from the engine harness or the original equipment manufacturer (OEM) harness.
3. Reference the engine or OEM wiring diagram. Select the appropriate adapter harness for the component being diagnosed.
4. Plug the adapter harness into the master bypass harness, Part Number 5299466.
5. Plug the three pin female connector from the master harness into the engine J1939 datalink connector on the engine harness.
6. Use the accessory power outlet plug to provide voltage to the component. Verify the accessory power voltage matches the component being tested using a multimeter. The center post is positive. The outer spring clip are negative. The accessory power outlet plug has a replaceable tubular fuse under the center post.
7. The male three pin connector has a cap with a built in 120 ohm terminating resistor. Remove or install as necessary for proper J1939 datalink communication.
8. The miniature banana jacks on the master bypass may be used to perform multimeter measurement. The test leads included in the kit will fit snugly into the jacks. The jacks are wired in parallel to the main harness circuit and are color coded to match the master bypass harness wiring.

**Service Parts Availability**

| Table 1, Service Parts |  |
|---|---|
| Part Description | New Part Number |
| Datalink Component Isolation Kit | 5299465 |

### Document History
