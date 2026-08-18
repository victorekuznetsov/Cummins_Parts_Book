---
aliases:
  - "Выключатель регулировки холостого хода"
type: "Процедура"
doc: "99-019-052"
title_en: "Idle Adjust Switch"
title_ru: "Выключатель регулировки холостого хода"
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
figures: 12
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-052.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/99-019-052.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "двигатель/NT/NTA855"
  - "двигатель/QST30"
  - "группа/99"
---

# Idle Adjust Switch
**Выключатель регулировки холостого хода**

> [!abstract] Процедура · `99-019-052`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]], [[41343322 — NH NT 855 CPL 3362|41343322]], [[93058669 — 6C8.3 CPL 3105|93058669]]
> **Семейство:** C8.3 · 6C8.3, NT/NTA855 · ISM/QSM11, QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]], [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]], [[4021442 — C8.3 Marine Electronic Control System Troubleshooting and Repair Manual|4021442]]
> **Секции:** Section 19 - Electronic Engine Controls · Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2015-06-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-052.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/99-019-052.pdf)

### General Information

The idle adjustment feature is a part of the cruise control set/resume multi-functionality switch. Moving the switch to the set position increases the low idle speed and moving the switch to the resume position decreases the low idle speed.

![[19c00894.png]]

Depending on how the switch is configured, moving the switch in one direction will increase the low idle speed.

![[19c00895.png]]

Push the diagnostic switch to the ON position or install the shorting plug. After the first active fault code has flashed out, push the idle adjust switch positive (+) up to advance to the next active fault code. Push the switch again until all of the active fault codes have been recorded.

![[19c00896.png]]

The idle adjust switch circuit consists of the idle/diagnostics increment signal, the idle/diagnostics decrement signal, the return wire, and the two-position switch located in the vehicle.

![[19c01180.png]]

### Resistance Check

If an electronic service tool is available, monitor the idle adjust switch for proper operation. If **not,** follow the troubleshooting procedures in this section.

Remove the three electrical connectors from the switch. Label the wires with the switch location and the circuit name.

![[19c00898.png]]

Touch one probe of the multimeter to the center terminal of the switch.

Touch the other probe to the cruise control/PTO resume/accelerate switch signal terminal of the switch.

![[ee8swkn.png]]

Hold the idle adjust switch in the positive (+) increment position. The multimeter **must** show an open circuit (100k ohms or more) when the switch is held in the positive (+) increment position and after it is released. If the circuit is **not** open, the switch has failed.

Refer to the OEM troubleshooting and repair manual for the replacement procedures.

![[ee8swkz.png]]

Hold the switch in the negative (-) decrement position. The multimeter **must** show a closed circuit (10 ohms or less) when the switch is held in the negative (-) decrement position.

When the switch is released, it **must** show an open circuit (100k ohms or more). If the multimeter does **not** show the correct values, the switch has failed.

Refer to the OEM troubleshooting and repair manual for the replacement procedures.

![[ee8swk01.png]]

Move the electrical lead from the cruise control/PTO resume/accelerate switch signal terminal to the cruise control/PTO set/coast switch signal terminal.

Hold the idle adjust switch in the positive (+) increment position. The multimeter **must** show a closed circuit (10 ohms or less) while the switch is held in the positive (+) increment position.

When the switch is released, the multimeter **must** show an open circuit (100k ohms or more). If the multimeter does **not** show the correct values, the switch has failed.

Refer to the OEM troubleshooting and repair manual for the replacement procedures.

![[ee8swk03.png]]

Move the idle adjust switch to the negative (-) decrement position. The multimeter **must** show an open circuit (100k ohms or more) when the switch is held in the negative (-) decrement position and when it is released. If the circuit is **not** open, the switch has failed.

Refer to the OEM troubleshooting and repair manual for the replacement procedures.

If the resistance value is correct, the switch **must** still be checked for a short circuit to ground.

![[ee8swk04.png]]

### Check for Short Circuit to Ground

Touch one multimeter probe to the cruise control PTO set/coast switch signal terminal of the switch and touch the other multimeter probe to chassis ground. Move the idle adjust switch to the negative (-) decrement position then to the positive (+) increment position. Measure the resistance. The multimeter **must** show an open circuit (100k ohms or more) when the switch is in all positions. If the circuit is **not** open, the switch has failed. Refer to the OEM troubleshooting and repair manual for the replacement procedures.

![[ee8swk05.png]]

Check for a short circuit to ground. Remove the multimeter probe from the cruise control/PTO set/coast switch signal terminal and touch it to the cruise control/PTO resume/accelerate switch signal terminal of the switch. Keep the other multimeter touching chassis ground. Move the switch to the positive (+) increment position then to the negative (-) decrement position. Measure the resistance. The multimeter **must** show an open circuit (100k ohms or more) when the switch is in all positions. If the circuit is **not** open, the switch has failed. Refer to the OEM troubleshooting and repair manual for the replacement procedures. If the switch passes all of the previous checks, the switch circuit **must** be checked.

![[ee8swk02.png]]
