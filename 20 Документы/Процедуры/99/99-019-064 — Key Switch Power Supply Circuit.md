---
aliases:
  - "Цепь питания от замка зажигания"
type: "Процедура"
doc: "99-019-064"
title_en: "Key Switch Power Supply Circuit"
title_ru: "Цепь питания от замка зажигания"
modified: "2015-11-06"
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
  - "4021674"
figures: 6
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-064.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/99-019-064.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "двигатель/NT/NTA855"
  - "двигатель/QST30"
  - "группа/99"
---

# Key Switch Power Supply Circuit
**Цепь питания от замка зажигания**

> [!abstract] Процедура · `99-019-064`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]], [[41343322 — NH NT 855 CPL 3362|41343322]], [[93058669 — 6C8.3 CPL 3105|93058669]]
> **Семейство:** C8.3 · 6C8.3, NT/NTA855 · ISM/QSM11, QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]], [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]], [[4021442 — C8.3 Marine Electronic Control System Troubleshooting and Repair Manual|4021442]], [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section 19 - Electronic Engine Controls · Section 19 - Electronic Engine Controls - Group 19 · Section 19 — Electronic Engine Controls — Group 19
> **Даты:** изменён 2015-11-06
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-064.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/99-019-064.pdf)

### Voltage Check

The vehicle keyswitch supplies an input signal to the electronic control module (ECM) which turns the ECM on or off.

![[19803967.png]]

The Generator Set ECM Keyswitch supplies an input signal to all generator set electronic control modules (ECMs) which turns to ECM on or off.

For generator sets using the PowerCommand Supervisor 3100 mounted in the Generator Control Panel (GCP), the ECM keyswitch (1) is mounted on the Service Tool Connector Panel (2), located inside the main panel.

![[19803990.png]]

For generator sets using the PowerCommand Supervisor 3300 mounted in the Generator Interface Box, the ECM keyswitch (1) is mounted within the customer terminal box above the customer connection terminal connection strip (2).

![[19803991.png]]

Turn the keyswitch to the OFF position.

Disconnect the Actuator harness connector from the ECM.

Inspect the connector pins.

![[19400002.png]]

> [!warning] CAUTION · Осторожно
> Proper leads and/or a Cummins® approved circuit testing tool must be used when working with electrical connectors to prevent pin expansion and damage to the connector.

Adjust the multimeter to measure VDC.

Insert a test lead into the keyswitch input signal pin of the Actuator connector. Connect the lead to the multimeter probe. Touch the other probe to a clean, unpainted surface on the engine block ground.

Turn the keyswitch to the ON position.

The measured voltage **must** show battery voltage. If the measured voltage is more than 0.5 VDC below battery voltage, continue with the next step.

![[19c01158.png]]

Disconnect the bulkhead connector.

Inspect the connector pins. Refer to the OEM troubleshooting and repair manual for the proper procedure.

Measure the voltage. Refer to the OEM troubleshooting and repair manual for the proper procedure.

The measured voltage **must** show battery voltage. If the voltage is **not** correct, there is a problem with the keyswitch input signal wire, keyswitch, or battery connection.

Repair or replace the wiring harness, keyswitch, or check the battery connections. Refer to the OEM troubleshooting and repair manual for the proper procedures.

![[19c01251.png]]
