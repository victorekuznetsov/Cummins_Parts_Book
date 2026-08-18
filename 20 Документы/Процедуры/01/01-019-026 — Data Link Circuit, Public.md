---
aliases:
  - "Цепь общедоступной шины данных"
type: "Процедура"
doc: "01-019-026"
title_en: "Data Link Circuit, Public"
title_ru: "Цепь общедоступной шины данных"
modified: "2002-12-05"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 6
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-019-026.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-019-026.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Data Link Circuit, Public
**Цепь общедоступной шины данных**

> [!abstract] Процедура · `01-019-026`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2002-12-05
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-019-026.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-019-026.pdf)

### General Information

The RS232 public datalink circuit is used for INPOWER™ to communicate with the ECM. The RS485 public datalink can be used to communicate information electronically with other electronic devices, such as switch gears and external paralleling controllers.

![[19800902.png]]

The datalink is powered through and uses a 9-pin Deutsch connector. The wiring positions follow:

Position A - data set ready

Position B - receive

Position C - transmit

Position D - data terminal ready

Position E - ground

Position F - carrier detect

Position G - request to send

Position H - clear to send

Position J - ring indicator.

![[19802482.png]]

### Resistance Check

Remove the extension harness connector from the ECM 05 connector.

Use test lead, Part Number 3822758, on the ECM connector; and use test lead, Part Number 3824812, on the 9-pin Deutsch connector.

Turn the Run/Stop switch to the Stop position.

Measure the resistance from the data set ready wire by measuring the resistance from pin A of the 9-pin Deutsch connector to the corresponding pins on the ECM connector.

![[19802483.png]]

If the circuit is **not** closed, repair or replace the engine harness. Refer to Procedure [[01-019-043 — Engine Wiring Harness|019-043]].

Do the above for every pin in the 9-pin Deutsch.

![[19802483.png]]

### Check for Short Circuit to Ground

Remove the engine harness connector from the ECM 05 connector.

Use test lead, Part Number 3824811, for the 9-pin Deutsch connector.

Measure the resistance from the data set ready wire by measuring the resistance from pin A of the 9-pin Deutsch connector to the engine block. The multimeter **must** show an open circuit (100k ohms or more).

If the circuit is **not** open, repair or replace the engine harness. Refer to Procedure [[01-019-043 — Engine Wiring Harness|019-043]].

Do this for every pin in the 9-pin Deutsch, except ground.

![[19802484.png]]

### Check for Short Circuit from Pin to Pin

**Deutsch Connector**

Remove the extension harness connector from the ECM 05 connector.

Use test lead, Part Number 3824811, for the 9-pin Deutsch connector. Measure the resistance from the carrier detect pin to all other pins in the connector. The multimeter **must** show an open circuit (100k ohms or more).

If the circuit is **not** open, repair or replace the engine harness. Refer to Procedure [[01-019-043 — Engine Wiring Harness|019-043]].

Follow the above instructions for every pin in the 9-pin Deutsch connector.

![[19802485.png]]
