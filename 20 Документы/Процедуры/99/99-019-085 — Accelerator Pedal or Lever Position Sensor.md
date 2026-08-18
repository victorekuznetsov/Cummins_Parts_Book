---
aliases:
  - "Датчик положения педали или рычага подачи"
type: "Процедура"
doc: "99-019-085"
title_en: "Accelerator Pedal or Lever Position Sensor"
title_ru: "Датчик положения педали или рычага подачи"
modified: "2015-06-29"
engines:
  - "37292556"
  - "37295879"
  - "41343322"
  - "93058669"
families:
  - "C8.3 · 6C8.3"
  - "NT/NTA855 · ISM/QSM11"
  - "QST30"
manuals:
  - "3666214"
  - "3666266"
  - "4021442"
figures: 8
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-085.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/99-019-085.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "двигатель/NT/NTA855"
  - "двигатель/QST30"
  - "группа/99"
---

# Accelerator Pedal or Lever Position Sensor
**Датчик положения педали или рычага подачи**

> [!abstract] Процедура · `99-019-085`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]], [[41343322 — NH NT 855 CPL 3362|41343322]], [[93058669 — 6C8.3 CPL 3105|93058669]]
> **Семейство:** C8.3 · 6C8.3, NT/NTA855 · ISM/QSM11, QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]], [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]], [[4021442 — C8.3 Marine Electronic Control System Troubleshooting and Repair Manual|4021442]]
> **Секции:** Section 19 - Electronic Engine Controls · Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2015-06-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-085.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/99-019-085.pdf)

### General Information

The accelerator pedal or lever position sensor will vary with OEM. Refer to the vehicle manufacturer's manual for the specific troubleshooting and repair procedures. This section contains troubleshooting and repair procedures for one typical accelerator pedal or lever position sensor.

The accelerator pedal or lever position sensor sends a signal to the ECM when the operator pushes on the accelerator pedal or lever. The accelerator position circuit consists of the accelerator pedal or lever position sensor, the ECM, accelerator pedal/lever position +5 volt, accelerator pedal/lever position signal, and accelerator pedal/lever position return wires.

![[19c01341.png]]

### Resistance Check

If an electronic service tool is available, monitor the accelerator position sensor for proper operation. If **not**, follow the troubleshooting procedures in this section.

Disconnect the 3-pin connector from the accelerator position sensor.

Connect the test connector.

![[tl8swkk.png]]

Connect the multimeter positive (+) test lead to the accelerator pedal/lever position +5 volt supply test connector wire. Connect the negative (-) multimeter test probe to the accelerator pedal/lever position return test connector wire.

Measure the resistance. The multimeter **must** show between 2000 and 3000 ohms when the accelerator pedal is released (idle position) or depressed (full-fuel position).

If the resistance is **not** within the specification, the accelerator position sensor has failed. Replace the accelerator position sensor. Refer to the OEM troubleshooting and repair manual for the procedures.

![[tl8swkl.png]]

Remove the multimeter probe from the accelerator pedal/lever position +5 volt supply test connector wire and connect it to the accelerator pedal/lever position signal test connector wire.

When the accelerator pedal is in the released (idle) position, measure the resistance. The multimeter **must** show between 1500 and 3000 ohms.

![[19900633.png]]

Depress the accelerator pedal assembly (full-fuel position) and measure the resistance. The multimeter **must** show between 250 and 1500 ohms. This resistance value **must** be at least 1000 ohms lower than the resistance value of 1500 to 3000 ohms measured in the above check. If the resistance values in the two previous steps are **not** within the specification, the accelerator position sensor has failed. Replace the accelerator position sensor according to the vehicle manufacturer's procedures. If the resistance values are within the specifications, the accelerator position sensor **must** still be checked for a short circuit to ground.

![[19900634.png]]

### Check for Short Circuit to Ground

Connect the multimeter positive (+) probe to the accelerator pedal/lever position return test connector wire. Touch the negative (-) multimeter probe to the chassis ground and measure the resistance.

The multimeter **must** show an open circuit (100k ohms or more).

![[19900635.png]]

Remove the multimeter positive (+) probe from accelerator pedal/lever position return test connector wire and connect it to the accelerator pedal/lever position signal test connector wire. Measure the resistance.

The multimeter **must** show an open circuit (100k ohms or more).

![[19900636.png]]

Remove the multimeter positive (+) probe from the accelerator pedal/lever position signal test connector wire and connect it to the accelerator pedal/lever position +5 volt supply test connector wire. Measure the resistance. The multimeter **must** show an open circuit (100k ohms or more).

If the resistance values are **not** within the specifications in the previous check, the accelerator position sensor has failed. Replace the accelerator position sensor according to the vehicle manufacturer's procedures.

If the accelerator position sensor has passed all the previous checks, connect the sensor to the wiring harness. The accelerator position sensor circuit **must** still be checked.

![[19900637.png]]
