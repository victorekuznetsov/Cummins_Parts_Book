---
aliases:
  - "Диагностика сброса ЭБУ и проблем связи"
type: "TSB"
doc: "tsb230096"
title_en: "ECM Reset and Communication Issue Troubleshooting"
title_ru: "Диагностика сброса ЭБУ и проблем связи"
released: "2023-05-05"
modified: "2023-05-05"
group: "19 - Electronic Engine Controls"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2023/tsb230096.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/tsb/tsb230096.pdf"
tags:
  - "документ/tsb"
  - "двигатель/QST30"
  - "год/2023"
  - "тема/electronic-engine-controls"
---

# ECM Reset and Communication Issue Troubleshooting
**Диагностика сброса ЭБУ и проблем связи**

> [!abstract] TSB · `tsb230096`
> **Раздел Cummins:** 19 - Electronic Engine Controls
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Даты:** выпущен 2023-05-05 · изменён 2023-05-05
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2023/tsb230096.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/tsb/tsb230096.pdf)

## ECM Reset and Communication Issue Troubleshooting

### Warranty Statement

The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.

### Contents

**Product Affected**

- QST30 CM552

**Issue Summary**

Symptom:

- ECM **not** able to communicate upon engine key on

Root Cause:

- ECM issue

**Verification**

Use the following steps to diagnose ECM:

1. With Calterm® (preferred) or INSITE™ electronic service tool and a datalink adapter hooked up to a suspect ECM.
2. Set battery voltage at 26V to 28V.
3. Key on and verify if the ECM will communicate. Key off. Repeat a few times.
4. If the ECM will **not** communicate key off and reduce battery voltage to 12V to 14V.
5. Key on and see if the ECM will communicate.
6. If the ECM will **not** communicate at the higher voltage but does at the lower voltage, the ECM likely has the reset issue.
7. A malfunctioning ECM has been detected when keyed on at a higher voltage and **not** communicating will be continuously resetting.

> [!note] Note · Примечание
> If using Calterm® and can communicate, check the reset parameter NRESETSE and see how many resets have occurred. A normally functioning module should **not** have any or **only** a few resets. Improper shutdowns (removing battery voltage in less than 30 sec after keying off) will increment the reset count each occurrence. The longer the ECM is left on and **not** communicating the higher the reset count will be when the ECM does communicate at the lower voltage. The reset count can increment by hundreds in just a few minutes.

Fault codes that can be seen for suspect ECMs are listed below:

| Table 1, Fault Codes |  |
|---|---|
| Fault Code | Description |
| 285 | SAE J1939 Multiplexing PGN Timeout Error - Abnormal Update Rate |
| 346 | Engine Control Module Warning Software error - Bad intelligent device or component |
| 426 | SAE J1939 Datalink - Data Erratic, Intermittent, or Incorrect; J1939 Network \#1 - Data erratic, intermittent or incorrect |
| 434 | Power Lost With Ignition On - Data Erratic, Intermittent, or Incorrect |
| 1117 | Power Lost With Ignition On - Data Erratic, Intermittent, or Incorrect |
| 1135 | SAE J1939 Data Link 2 Engine Network - Abnormal Update Rate |
| 2727 | SAE J1939 Data Link 2 Engine Network - Abnormal Update Rate |

**Resolution**

Replace malfunctioning ECM. See QST30 Industrial Electronic Control System Troubleshooting and Repair Manual, Bulletin 3666214. [[87-019-031 — Engine Control Module|Refer to Procedure 019-031 in Section 19.]]

### Document History
