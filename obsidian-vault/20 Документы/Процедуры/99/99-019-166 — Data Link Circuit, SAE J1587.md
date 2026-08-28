---
aliases:
  - "Цепь шины данных SAE J1587"
type: "Процедура"
doc: "99-019-166"
title_en: "Data Link Circuit, SAE J1587"
title_ru: "Цепь шины данных SAE J1587"
modified: "2008-05-30"
engines:
  - "35354607"
  - "35373113"
  - "41343322"
  - "41370103"
  - "71156161"
  - "80141463"
  - "80248213"
  - "93058669"
  - "93087701"
families:
  - "C8.3 · 6C8.3"
  - "NT/NTA855 · ISM/QSM11"
  - "QSM11"
  - "QSX15"
manuals:
  - "3666266"
  - "3666415"
  - "4021442"
figures: 9
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-166.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/99-019-166.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "двигатель/NT/NTA855"
  - "двигатель/QSM11"
  - "двигатель/QSX15"
  - "группа/99"
---

# Data Link Circuit, SAE J1587
**Цепь шины данных SAE J1587**

> [!abstract] Процедура · `99-019-166`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]], [[93058669 — 6C8.3 CPL 3105|93058669]], [[93087701 — 6C8.3 CPL 3105|93087701]]
> **Семейство:** C8.3 · 6C8.3, NT/NTA855 · ISM/QSM11, QSM11, QSX15
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]], [[3666415 — ICON Idle Control System Master Repair Manual|3666415]], [[4021442 — C8.3 Marine Electronic Control System Troubleshooting and Repair Manual|4021442]]
> **Секции:** Section 19 - Electronic Engine Controls · Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2008-05-30
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-166.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/99-019-166.pdf)

### General Information

The OEM J1587 datalink circuit is located in the OEM wiring harness.

The purpose of this datalink is to allow the ECM to communicate to the vehicle control operated systems such as the transmission controllers, traction control system, etc. The J1587 datalink includes the Society of Automotive Engineers (SAE J1587) datalink positive (+) and the SAE J1587 datalink negative (-) wires in the OEM wiring harness.

> [!note] Note · Примечание
> Typical SAE J1587 connectors will either be 2 or 6-pin connectors.

![[nobox.png]]

| 6-Pin Connector |  |
|---|---|
| Position A | Datalink positive (+) |
| Position B | Datalink negative (-) |
| Position C | Battery (12/24 VDC) |
| Position D | Open |
| Position E | Engine block ground |
| Position F | **Not** used |

![[19400740.png]]

### Resistance Check

> [!warning] CAUTION · Осторожно
> The leads must fit tightly in the connector without expanding the pins in the connector otherwise the connector will be damaged.

Turn the keyswitch to the OFF position. Disconnect the OEM harness connector from the ECM.

Insert a test lead into the SAE J1587 datalink positive (+) pin of the OEM harness connector and connect to a multimeter probe. Insert the other test lead into the SAE J1587 datalink positive (+) pin of the 6-pin connector and connect it to the other multimeter probe. Measure the resistance. The multimeter **must** show a closed circuit (10 ohms or less).

If the circuit is **not** closed, repair or replace the OEM harness. Refer to the OEM troubleshooting and repair manual.

Remove the test lead from the SAE J1587 datalink positive (+) pin and insert it into the SAE J1587 datalink negative (-) pin. Remove the other test lead from the SAE J1587 datalink positive (+) pin and insert it into the SAE J1587 datalink negative (-) pin of the 6-pin connector. Measure the resistance. The multimeter **must** show a closed circuit (10 ohms or less).

If the circuit is **not** closed, repair or replace the OEM harness. Refer to the OEM troubleshooting and repair manual.

![[19c01188.png]]

Remove the test lead from the SAE J1587 datalink negative (-) pin and insert it into the battery negative (-) pin of the 6-pin Deutsch connector. Remove the test lead from the SAE J1587 datalink negative (-) pin and disconnect it from the multimeter probe. Touch the multimeter probe to the engine block ground. Measure the resistance. The multimeter **must** show a closed circuit (10 ohms or less).

If the circuit is **not** closed, repair or replace the OEM harness. Refer to the OEM troubleshooting and repair manual.

![[19c01190.png]]

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

> [!warning] CAUTION · Осторожно
> The leads must fit tightly in the connector without expanding the pins in the connector otherwise the connector will be damaged.

Disconnect the batteries.

Measure the resistance from the positive (+) battery terminal to battery positive (+) of the 6-pin Deutsch connector. The multimeter **must** show a closed circuit (10 ohms or less).

If the circuit is **not** closed, repair or replace the OEM battery supply circuit. Refer to the OEM troubleshooting and repair manual for the procedures.

If the values are correct, the circuit **must** still be checked for a short circuit to ground and a short circuit from pin to pin.

![[19c01191.png]]

### Check for Short Circuit to Ground

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

> [!warning] CAUTION · Осторожно
> The leads must fit tightly in the connector without expanding the pins in the connector otherwise the connector will be damaged.

Disconnect the batteries.

Disconnect the OEM harness connector from the ECM.

Insert a test lead into the SAE J1587 datalink positive (+) pin of the 6-pin connector and connect it to a multimeter probe. Touch the other multimeter probe to the engine block ground. Measure the resistance. The multimeter **must** show an open circuit (100k ohms or more).

If the circuit is **not** open, repair or replace the OEM harness. Refer to the OEM troubleshooting and repair manual.

Remove the test lead from the SAE J1587 datalink positive (+) pin and insert it into the SAE J1587 datalink negative (-) pin of the 6-pin connector. Touch the other multimeter probe to the engine block ground. Measure the resistance from the SAE J1587 datalink negative (-) pin of the 6-pin connector to the engine block ground. The multimeter **must** show an open circuit (100k ohms or more).

If the circuit is **not** open, repair or replace the OEM harness. Refer to the OEM troubleshooting and repair manual.

![[19c01192.png]]

### Check for Short Circuit from Pin to Pin

> [!warning] CAUTION · Осторожно
> The leads must fit tightly in the connector without expanding the pins in the connector otherwise the connector will be damaged.

Disconnect the OEM harness connector from the ECM.

Insert a test lead into the SAE J1587 datalink positive (+) pin of the OEM harness connector and connect it to the multimeter probe. Insert the other test lead into another pin in the OEM harness and connect it to the other multimeter probe. Measure the resistance. The multimeter **must** show an open circuit (100k ohms or more).

If the circuit is **not** open, repair or replace the OEM harness. Refer to the OEM troubleshooting and repair manual.

Measure the resistance from the SAE J1587 datalink positive (+) pin of the OEM harness connector to all other pins in the connector, one at a time. The multimeter **must** show an open circuit (100k ohms or more).

If the circuit is **not** open, repair or replace the OEM harness. Refer to the OEM troubleshooting and repair manual.

Remove the test lead from the SAE J1587 datalink positive (+) pin of the OEM harness connector and insert it into the SAE J1587 datalink negative (-) pin. Measure the resistance from the SAE J1587 datalink negative (-) pin to all other pins in the connector. The multimeter **must** show an open circuit (100k ohms or more) at all pins.

If the circuit is **not** open, repair or replace the OEM harness. Refer to the OEM troubleshooting and repair manual.

Connect all components after repairs are completed.

![[19c01194.png]]

### Voltage Check

Locate the datalink connector on the OEM harness. The location will depend on the OEM.

![[nobox.png]]

> [!warning] CAUTION · Осторожно
> The leads must fit tightly in the connector without expanding the pins in the connector otherwise the connector will be damaged.

Turn the keyswitch to the ON position. Adjust the multimeter to measure VDC.

Insert a test lead into the SAE J1587 datalink positive (+) pin of the 6-pin connector and connect it to a multimeter probe. Touch the other multimeter probe to the engine block ground. Measure the voltage.

The multimeter **must** read 3.5 to 5 VDC for the voltage check from the SAE J1587 datalink positive (+) pin of the datalink connector to ground.

Remove the test lead from the SAE J1587 datalink positive (+) pin and insert it into the SAE J1587 datalink negative (-) pin of the 6-pin Deutsch connector. Touch the other multimeter probe to the engine block ground. Measure the voltage.

The multimeter **must** read 0 to 2.5 VDC for the voltage check from the SAE J1587 datalink negative (-) pin of the datalink connector to ground.

Remove the test lead from the SAE J1587 datalink negative (-) pin and insert it into battery positive (+) pin of the 6-pin connector. Touch the other multimeter probe to the engine block ground. Measure the voltage.

The multimeter **must** read battery voltage for the voltage check from pin C of the datalink connector to ground.

Remove the test lead from the battery positive (+) pin and insert it into the battery negative (-) pin of the 6-pin connector. Touch the other multimeter probe to the engine block ground. Measure the voltage.

The multimeter **must** read 0 voltage for the voltage check from the battery negative (-) pin of the datalink connector to ground.

![[19c01195.png]]
