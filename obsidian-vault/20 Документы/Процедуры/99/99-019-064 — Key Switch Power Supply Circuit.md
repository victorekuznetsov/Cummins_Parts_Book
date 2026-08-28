---
aliases:
  - "Цепь питания от замка зажигания"
type: "Процедура"
doc: "99-019-064"
title_en: "Key Switch Power Supply Circuit"
title_ru: "Цепь питания от замка зажигания"
modified: "2015-11-06"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
  - "35354607"
  - "35373113"
  - "37269910"
  - "37280605"
  - "37292556"
  - "37295879"
  - "41343322"
  - "41370103"
  - "71156161"
  - "80141463"
  - "80248213"
  - "85017333"
  - "93058669"
  - "93087701"
families:
  - "C8.3 · 6C8.3"
  - "K19"
  - "NT/NTA855 · ISM/QSM11"
  - "QSK23"
  - "QSK60"
  - "QSM11"
  - "QST30"
  - "QSX15"
manuals:
  - "3666070"
  - "3666113"
  - "3666214"
  - "3666266"
  - "3666415"
  - "4021442"
  - "4021674"
figures: 6
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-064.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/99-019-064.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "двигатель/K19"
  - "двигатель/NT/NTA855"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "двигатель/QSM11"
  - "двигатель/QST30"
  - "двигатель/QSX15"
  - "группа/99"
---

# Key Switch Power Supply Circuit
**Цепь питания от замка зажигания**

> [!abstract] Процедура · `99-019-064`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]], [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]], [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]], [[85017333 — QSK23 CM500 CPL 2858|85017333]], [[93058669 — 6C8.3 CPL 3105|93058669]], [[93087701 — 6C8.3 CPL 3105|93087701]]
> **Семейство:** C8.3 · 6C8.3, K19, NT/NTA855 · ISM/QSM11, QSK23, QSK60, QSM11, QST30, QSX15
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]], [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]], [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]], [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]], [[3666415 — ICON Idle Control System Master Repair Manual|3666415]], [[4021442 — C8.3 Marine Electronic Control System Troubleshooting and Repair Manual|4021442]], [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section 19 - Electronic Engine Controls · Section 19 - Electronic Engine Controls - Group 19 · Section 19 — Electronic Engine Controls — Group 19
> **Даты:** изменён 2015-11-06
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-064.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/99-019-064.pdf)

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
