---
aliases:
  - "Двигатель не останавливается ни от блока управления, ни с дистанционного пульта"
type: "Процедура"
doc: "116-t02-1048"
title_en: "Engine Will Not Stop from Diesel Control Unit or Remote Panel"
title_ru: "Двигатель не останавливается ни от блока управления, ни с дистанционного пульта"
modified: "2008-05-22"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4021617"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1048.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1048.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/116"
---

# Engine Will Not Stop from Diesel Control Unit or Remote Panel
**Двигатель не останавливается ни от блока управления, ни с дистанционного пульта**

> [!abstract] Процедура · `116-t02-1048`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2008-05-22
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1048.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1048.pdf)

Printable Version

### Symptoms

- Engine does **not** respond to engine stop.

- Engine executes un-requested engine stop.

### How To Use This Tree

This symptom tree can be used to troubleshoot a malfunction. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.

### Shoptalk

The engine can be stopped by pushing the stop button on the DCU410 unit or remote panel.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the customer interface box. |  |
|  | **STEP 1A.** Check the DCU410 unit display for faults. |  |
|  | **STEP 1A-1.** Check the DCU410 unit power supply wire for voltage +24-VDC. |  |
| STEP 2. | Check the customer interface box wiring. |  |
|  | **STEP 2A.** Check the switched inputs power supply 2 wire for an open. |  |
|  | **STEP 2B.** Check the remote stop supply wire for an open. |  |
|  | **STEP 2C.** Check the engine stop indication supply wire for an open. |  |
|  | **STEP 2D.** Check the energize to stop relay return wire for an open at the DCU410 unit and CLU unit. |  |
| STEP 3. | Check the engine stop button. |  |
|  | **STEP 3A.** Check the power on signal wire at the SDU410 unit and engine stop switch. |  |
|  | **STEP 3B.** Check the ignition (engine stop) supply wire at the C1 connector and engine stop switch. |  |

### STEP 1. Check the customer interface box.

#### STEP 1A. Check the DCU410 unit display for faults.

| **Conditions:** Locate the DCU410 unit display. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the DCU410 unit display for indication of faults. | DCU410 unit indicates fault(s)? **YES** | 2A |
| DCU410 unit indicates fault(s)? **NO** | 1A-1 |  |

#### STEP 1A-1. Check the DCU410 unit power supply wire for voltage +24-VDC.

| **Conditions:** Open the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the voltage at the battery 1 voltage (switched power) at the DCU410 unit. Place one test on the battery 1 voltage supply wire at the DCU410 unit. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than +24-VDC? **YESRepair:** Check the batteries. Refer to OEM service manual. | Repair complete |
| Less than +24-VDC? **NO** | 2A |  |

### STEP 2. Check the customer interface box wiring.

#### STEP 2A. Check the switched inputs power supply 2 wire for an open.

| **Conditions:** Open the customer interface box. Disconnect the switched inputs power supply 2 wire from the DCU410 unit and the X4 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the switched inputs power supply 2 wire for an open. Place one test lead on the switched inputs power supply 2 wire at the DCU410 unit. Place the other test lead on the switched inputs power supply 2 wire at the X4 connection. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 2B |
| Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |

#### STEP 2B. Check the remote stop supply wire for an open.

| **Conditions:** Open the customer interface box. Disconnect the switched inputs power supply 2 wire from the DCU410 unit and the X4 connection. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the remote stop supply wire for an open. Place one test lead on the remote stop supply wire at the DCU410 unit. Place the other test lead on the remote stop supply wire at the X4 connection. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 2C |
| Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |

#### STEP 2C. Check the engine stop indication supply wire for an open.

| **Conditions:** Open the customer interface box. Disconnect the engine stop indication supply wire at the DCU410 unit and the CLU unit. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the engine stop indication supply wire for an open. Place one test lead on the engine stop indication supply wire at the DCU410 unit. Place the other test lead on the engine stop indication supply wire at the CLU unit. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 2D |
| Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |

#### STEP 2D. Check the energize to stop relay return wire for an open at the DCU410 unit and CLU unit.

| **Conditions:** Open the customer interface box. Disconnect the energize to stop relay return wire at the DCU410 unit and CLU unit. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the energize to stop relay return wire for an open at the DCU410 unit and CLU unit. Place one test lead on the energize to stop relay return wire at the DCU410 unit. Place the other test lead on the energize to stop relay return wire at the CLU unit. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 3A |
| Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |

### STEP 3. Check the engine stop button.

#### STEP 3A. Check the power on signal wire at the SDU410 unit and engine stop switch.

| **Conditions:** Open the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the power on signal wire at the SDU410 unit and engine stop switch. Place one test lead on the power on signal wire at the SDU410 unit. Place the other test lead on the engine stop switch. Operate the engine stop switch. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 3B |
| Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] Replace the engine stop switch. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |

#### STEP 3B. Check the ignition (engine stop) supply wire at the C1 connector and engine stop switch.

| **Conditions:** Open the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the ignition (engine stop) supply wire at the C1 connector and engine stop switch. Place one test lead on the ignition (engine stop) supply wire at the C1 connector. Place the other test lead on the engine stop switch. Operate the engine stop switch. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | Contact a Cummins® Authorized Repair Location. |
| Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] Replace the engine stop switch. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |
