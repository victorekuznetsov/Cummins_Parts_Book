---
type: "TSB"
doc: "tsb170124"
title_en: "Fuel Pump Timing Correction to Reduce Engine Noise"
modified: "2020-03-19"
figures: 2
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2017/tsb170124.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb170124.pdf"
tags:
  - "документ/tsb"
---

# Fuel Pump Timing Correction to Reduce Engine Noise

> [!abstract] TSB · `tsb170124`
> **Даты:** изменён 2020-03-19
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2017/tsb170124.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb170124.pdf)

## Fuel Pump Timing Correction to Reduce Engine Noise

### Warranty Statement

The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.

### Contents

**Product Affected**

- ISX15 CM2250
- ISX15 CM2250 SN
- ISX15 CM2350 X101
- QSX CM2250 ECF
- QSX CM2250 X115
- QSX CM2350 X105
- QSX CM2350 X106
- QSX CM2350 X118
- X15 CM2350 X114B
- X15 CM2350 X116B
- X15 CM2350 X123B
- X15 CM2450 X124B
- X15 CM2350 X129B

**Issue**

Symptom:

- Gear train impact noise that is most noticeable at or around 1500 rpm and worsens as load increases.
- Gear train impact noise occurs at half-engine-order (once every 2 crankshaft revolutions), similar to a fuel knock and has been described as sounding like a “freight train” or “helicopter."

Root Cause:

- Incorrect fuel pump timing. This problem is **not** related to the timing of the fuel pump gear to the fuel pump. The fuel pump gear is keyed or indexed to the pump cam and is **always** in a fixed position with respect to the internal timing of the fuel pump. When the fuel pump is installed to the engine, it is possible to time the fuel pump incorrectly with respect to the crankshaft position and thereby worsen engine noise.
- Gear train impact noise caused by incorrect fuel pump timing will **not** lead to progressive engine damage or mechanical malfunction

**Verification**

- Confirm gear train impact noise that sounds like a “freight train” or “helicopter”. Reference audio clip below.
- Confirming that an engine noise complaint is caused by improper fuel pump timing and not due to another issue is **not** possible without removing the fuel pump and inspecting for its timing. No inspection or performance tests are available to confirm fuel pump timing is the cause of an engine noise complaint prior to fuel pump removal. See Resolution Section below.
- The following audio link is a representation of gear train impact noise producing a “freight train” or “helicopter” noise. **Note:** [http://tsb.cumminsvirtualcollege.com/TSB170124\_en.aspx](http://tsb.cumminsvirtualcollege.com/TSB170124_en.aspx)

**Resolution**

A new fuel pump timing gauge has been released for service. The following steps refer to the updated service documentation to follow so the fuel pump is timed correctly with the engine. Performing the steps below will help reduce engine noise.

For X15 CM2350 X114B engines, perform the following steps:

- Verify base engine timing. See corresponding Service Manual. [[377-001-088 — Engine Base Timing|Refer to Procedure 001-088]] in Section 1.
- Time the high-pressure fuel pump. See corresponding Service Manual. [[377-005-016 — Fuel Pump|Refer to Procedure 005-016]] in Section 5.

For all other engines perform the following steps:

- Verify base engine timing. See corresponding Service Manual. Refer to Procedure 001-088 in Section 1.
- Check the gear lash. See corresponding Service Manual. Refer to Procedure 001-088 in Section 1.
- Time the high-pressure fuel pump. See corresponding Service Manual. Refer to Procedure 005-016 in Section 5.

See Figures 1 and 2 for descriptions of tools installed on fuel pump(s).

![[17r00531.png]]

Figure 1. Service Tool Installation on ISX/QSX CM2250, CM2350, and X15 CM2350 114B.

![[17r00532.png]]

Figure 2. Service Tool Installation on X15 CM2350 116B.

If the noise is reduced by performing the previous steps, submit your claim under Fail Code BKGR.

**Production Status**

Implemented for production. See Table 1 for production information.

| Table 1, Production Information |  |  |
|---|---|---|
| ESN First | Build Date 1 | Plant |
| 80021663 | 3 November 2017 | Jamestown Engine Plant |
| 1 Engine build date can be found on engine dataplate. |  |  |

### Document History
