---
type: "Процедура"
doc: "19-019-187"
title_en: "Actuator Diagnostic for Idle Surge"
modified: "2002-08-20"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
  - "85017333"
families:
  - "QSK23"
  - "QSK60"
manuals:
  - "3666113"
figures: 6
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-019-187.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-019-187.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
---

# Actuator Diagnostic for Idle Surge

> [!abstract] Процедура · `19-019-187`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2002-08-20
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-019-187.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-019-187.pdf)

### Test

With the engine running at low idle (and surging), disconnect the fuel rail pressure sensor.

![[19400306.png]]

If the surging does **not** stop, replace the fueling actuator. Refer to Procedure 019-110 in the Troubleshooting and Repair Manual, QSK19 Service Engines, Bulletin 3666098, Troubleshooting and Repair Manual, QSK45 and QSK60 Service Engines, Bulletin [[3666260 — QSK45 and QSK60 Operation and Maintenance Manual\|3666260]], or the Troubleshooting and Repair Manual, QSK78 Series Engines, Bulletin 3666727.

![[19400368.png]]

If the surging does stop, check that the engine is running at the correct low idle rpm.

![[19800979.png]]

If the engine is **not** running at the correct low idle rpm, replace the rail actuator. Refer to Procedure [[19-019-337 — Rail Actuator|019-337]].

![[19400368.png]]

Disconnect the timing pressure sensor from the harness.

If the low idle returns to the correct speed, troubleshoot the common power supply line (pin 5 on connector A) between the two sensors using the troubleshooting trees for Fault Codes 116, 117, 451, and 452.

![[19400306.png]]

If the engine is running at the correct low idle rpm, run the engine to high idle for 10 seconds (with a load on the engine if possible), then back to low idle. Repeat the test from the beginning.

After the test has been repeated, if the engine is still surging and running at the correct low idle rpm, reconnect the pressure sensor. Check the rail pressure sensor and ambient air pressure sensor for in-range failure. Refer to Procedure [[19-019-186 — In-Range Pressure Sensor|019-186]].

![[nobox.png]]
