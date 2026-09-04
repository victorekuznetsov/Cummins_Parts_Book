---
type: "TSB"
doc: "tsb190003"
title_en: "Engine Control Module (ECM) Malfunctions Due to Incorrect Switch Input Wiring"
modified: "2023-10-10"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2019/tsb190003.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb190003.pdf"
tags:
  - "документ/tsb"
---

# Engine Control Module (ECM) Malfunctions Due to Incorrect Switch Input Wiring

> [!abstract] TSB · `tsb190003`
> **Даты:** изменён 2023-10-10
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2019/tsb190003.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb190003.pdf)

## Engine Control Module (ECM) Malfunctions Due to Incorrect Switch Input Wiring

### Warranty Statement

The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.

### Contents

**Product Affected**

- B6.7 CM2350 B121B
- B6.7 CM2350 B135B
- B6.7 CM2350 B148B
- B6.7 CM2350 B136C
- B6.7 CM2350 B157C
- B6.7 CM2350 B198C
- B6.7 CM2450 B155B
- ISB6.7 CM2350 B101
- ISL9 CM2350 L101
- ISX12 CM2350 X102
- ISX15 CM2350 X101
- L9 CM2350 L119B
- L9 CM2350 L123B
- L9 CM2450 L126B
- X12 CM2450 X137B
- X15 CM2350 X114B
- X15 CM2350 X116B
- X15 CM2450 X124B
- X15 CM2450 X134B
- X15 CM2350 X132C

**Issue**

Symptom:

- Engine control module (ECM) switch inputs, such as the power take-off (PTO)/Accelerator Interlock/Oil pressure switch, are inoperable.
- Fault Codes 175, 176, and 415 (B6.7 **Only**).
- Fault Codes 5879 and 5881 (B, L9, X12 and X15 engines).

Root Cause:

- ECM switch inputs are wired incorrectly
- Malfunctioning OEM wiring harness

**Confirmation**

Perform the following steps to check and verify that the ECM switch inputs are wired correctly.

1. Remove the original equipment manufacturer (OEM) wiring harness connector from the ECM.
2. Use a multimeter to measure for voltage between pins 11, 12, 19, 20, 43, 44, 47, 66 through 70, 86 through 94, and ECM switch RETURN pin 62 at the OEM wiring harness connector.
3. Toggle the switch to ground inputs and check for battery voltage with the keyswitch in both the ON and OFF positions.

Multimeter **must** show 0.0 volts. If any voltage is observed, the switch **must** be wired correctly before the ECM is installed.

Reference the circuit diagram or wiring diagram for connector pin identification.

Use the following procedure for general multimeter usage techniques.

The resistance measurement given in this document of 0.020 Ohms is different than the Service Manual specification.

Perform the following steps to check and verify that the ECM power return (ground) wires are grounded correctly.

1. Disconnect the batteries. See equipment manufacturer service information.
2. Use a multimeter to measure the resistance between the OEM connector ECM ground return pins and Battery (-) cable connection.
3. The multimeter ohm reading **must** be less than 0.020 Ohms. If reading is **not** less than 0.020 Ohms, the high resistance ground connection **must** be corrected.
4. Reconnect batteries. See equipment manufacturer service information.
5. With all components connected, use a multimeter to measure the voltage between the engine ECM block ground stud and battery negative connection with the following conditions met in order:
6. The multimeter **must** show less than 0.5VDC. If voltage is **not** less than 0.5VDC, the high resistance ground connection **must** be corrected.

Reference the circuit diagram or wiring diagram for connector pin identification.

Use the following procedure for general multimeter usage techniques. See the corresponding Service Manual. Reference Procedure 019-359 in Section 19.

**Resolution**

If any of the pins show a voltage with the multimeter when the switches are toggled, the switch **must** be wired correctly, so an open or ground is observed. If the ECM switch is wired correctly and there is still voltage in the pins, the OEM wiring harness **must** be visually inspected for any damage. If the ECM is installed before the switch is wired correctly, the ECM will be susceptible to repeat malfunctions.

Subsequent damage to the ECM, caused by incorrectly wiring wired switches prior to ECM installation, will not be warrantable.

ECM power return (ground) wiring **must** be connected to the engine cylinder block ground stud and then return from the engine cylinder block to the battery by a low resistance circuit of 0.020 Ohms or less between the ECM and battery.

Sustained voltage differential or peak-peak voltage differential levels between the engine ECM cylinder block ground stud and battery negative **not** to exceed 0.5VDC.

### Document History
