---
aliases:
  - "Обслуживание журналов неисправностей и трендов модуля CM530 CENSE™"
type: "TSB"
doc: "tsb110093"
title_en: "CM530 CENSE™ Module Fault and Trend Log Maintenance"
title_ru: "Обслуживание журналов неисправностей и трендов модуля CM530 CENSE™"
released: "2011-04-29"
modified: "2011-04-29"
group: "19 - Electronic Engine Controls"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
  - "37292556"
  - "37295879"
families:
  - "QSK60"
  - "QST30"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2011/tsb110093.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb110093.pdf"
tags:
  - "документ/tsb"
  - "двигатель/QSK60"
  - "двигатель/QST30"
  - "год/2011"
  - "тема/electronic-engine-controls"
---

# CM530 CENSE™ Module Fault and Trend Log Maintenance
**Обслуживание журналов неисправностей и трендов модуля CM530 CENSE™**

> [!abstract] TSB · `tsb110093`
> **Раздел Cummins:** 19 - Electronic Engine Controls
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QSK60, QST30
> **Даты:** выпущен 2011-04-29 · изменён 2011-04-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2011/tsb110093.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb110093.pdf)

## CM530 CENSE™ Module Fault and Trend Log Maintenance

### Warranty Statement

The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.

### Contents

#### Issue:

- A memory corruption issue has been identified when the CENSE™ module is allowed to become full for extended periods of time. A number of fault codes and symptoms with varying severity can be experienced as a result.
- CENSE™ modules often become filled when an intermittent type failure, which generates high fault code counts, is experienced. A snapshot is stored to the fault log buffer every time a fault code is activated. The rate at which the buffer is filled up is dependent on the number of parameters being logged and the frequency of the fault.
- It is also possible for RS-422 monitoring equipment to request data faster than it can be communicated across the RS-422 data link. In this situation, the CENSE™ module will buffer trend data which can **not** be immediately sent. When data is buffered for an extended period of time, the CENSE™ module can become full. The rate at which the buffer is filled up is dependent on the number of parameters being logged and the data request frequency of the remote monitoring system.
- Infrequent download of fault and trend data can also result in the fault and trend buffers becoming full.
- It has also been identified that QSV engines can suffer from the trend data memory becoming filled during normal operation of the engine.

> [!note] Note · Примечание
> Before attempting troubleshooting of the CENSE™ module, all active and inactive fault codes should be investigated.

#### Verification:

- Fault Code 111 – Internal Electronic Control Module (ECM) Error
- Fault Code 335 - Internal Electronic Control Module (ECM) Error
- Fault Code 747 - Trend Data Memory 90 percent Full
- Fault Code 748 - Trend Data Memory 100 percent Full
- Fault Code 749 – Fault Code Datalog Memory 90 percent Full
- Fault Code 754 – Fault Code Datalog Memory 100 percent Full

#### Symptoms:

- Fault lamp illumination
- Interruption of remote monitoring
- No propel
- No start
- Engine shuts down
- No communication possible with the CENSE™ module
- Data corruption - ESN, hours, fuel consumption etc. incorrect
- Gas engines can suffer misfires and inaccurate exhaust gas temperature sensor data.

Use the following procedures to resolve CENSE™ module corruption.

If communication can be established with the CENSE™ module use the following procedure when any number of the symptoms or fault codes above are experienced, and it is possible to establish a connection with the CENSE™ module when using INSITE CENSE, while the module is still installed on the unit.

#### Communication is Established

1. Download all data held in the CENSE™ module
2. Clear the fault/trend log memory
3. Check for evidence of memory corruption, such as ESN, hours, fuel consumption, etc. being incorrect. If corruption is detected, continue to step 4. Otherwise move to step 5
4. Calibrate the CENSE™ module with the latest calibration version
5. Allow the engine/equipment to operate normally for 1 hour. Download the CENSE™ module. Once the download is complete, inspect the CENSE™ module for evidence of memory corruption. If memory corruption is detected, replace the CENSE™ module. Reference [[tsb110024 — CM530 CENSE™ Module Re-Use\|TSB110024]] for further information.

If communication can **not** be established with the CENSE™ module use the following procedure when the symptoms or fault codes above are experienced, and it is **not** possible to establish a connection with the CENSE™ module when using INSITE CENSE, while the module is still installed on the unit.

#### Communication is not established

1. Data link checks (DB9 to 3-pin Deutsch™ connector)
2. Electronic tool checks
3. Hardware checks

#### If additional remote monitoring equipment is used:

- When remote monitoring equipment is used, it is essential to make sure the rate at which data is transmitted is within the bandwidth capabilities of the RS-422 data link. It is recommended that a logging frequency of no more than 0.1 Hz (1 log every 10 seconds) is used to make sure the CENSE™ module does **not** begin to buffer data.

> [!note] Note · Примечание
> Data link J1939 and RS-232 have higher bandwidth capabilities and may **not** require reduced sampling rates to be applied.

#### Recommended CENSE™ module download frequency:

- It is recommended that the CENSE™ module fault and trend buffer is downloaded and emptied during every service event. Refer to the following table for guidance on the number of hours before the CENSE™ module becomes 100 percent full.

| Sample Rate \[hrs/request\] | Table 1: Hours to 100 percent fill of CENSE™ Module |  |  |  |  |
|---|---|---|---|---|---|
| Number of Parameters Logged |  |  |  |  |  |
| 1 | 5 | 10 | 20 | 40 |  |
| 0.017 | 2133 | 427 | 213 | 107 | 53 |
| 0.25 | 32000 | 6400 | 3200 | 1600 | 800 |
| 0.5 | 64000 | 12800 | 6400 | 3200 | 1600 |
| 1 | 128000 | 25600 | 12800 | 6400 | 3200 |

### Document History
