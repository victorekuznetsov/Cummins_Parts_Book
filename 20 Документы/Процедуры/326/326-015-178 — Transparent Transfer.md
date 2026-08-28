---
type: "Процедура"
doc: "326-015-178"
title_en: "Transparent Transfer"
modified: "2019-08-02"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "4358378"
figures: 4
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/326/326-015-178.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/326-015-178.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/326"
---

# Transparent Transfer

> [!abstract] Процедура · `326-015-178`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[4358378 — Cummins® Electronic Throttle and Shift (ETS) and Cummins® Inboard Joystick Marine Con|4358378]]
> **Секции:** Section 15 - Instruments and Controls
> **Даты:** изменён 2019-08-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/326/326-015-178.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/326-015-178.pdf)

### General Information

There are three types of joysticks: Stand Alone, Associated, and Transparent Transfer.

The Cummins® Inboard Joystick system supports transferring control (1) from control lever station to inboard joystick (2) by a movement of the joystick when the control lever station is in the neutral and active position. To transfer control from inboard joystick to control lever station, move the control lever station out of the neutral position. The transparent transfer function is per station. If a control lever station or inboard joystick at another station wants control, the “Take/Active” button on the button pad is to be pushed twice.

A version 4 and greater lever control station and a version 3 and greater inboard joystick can be paired together and use the transparent transfer feature. To see the version of inboard joystick or control lever station, look at the data plate located on the underside of the device or connect with the Cummins® Inboard Joystick Configuration Tool.

To use transparent transfer, the inboard joystick **must** first be “paired” with the lever control station. During the pairing process it will be confirmed that each lever control station or inboard joystick is **only** to be paired with a single corresponding unit (lever control station or inboard joystick). If an inboard joystick is **not** paired with a lever control station, then station transfer function will be the same as a lever control station. The lever control station and inboard joystick when activated will possess an Active Station Token which is an electronic key that allows commands to the control system. The lever control station will hold the Active Station Token when control is initially transferred to it from another control station, or if is **not** in the neutral position. The inboard joystick may be able to take control whenever the lever control station is in the neutral position, by simply moving the inboard joystick. The inboard joystick will retain the Active Station Token until the lever control station is moved out of the neutral position. When the lever control station is moved out the neutral position, then the lever control station takes the Active Station Token back from the inboard joystick. The Active Station Token can be taken by any other station by the standard station transfer process.

![[15o00002.png]]

Lever Control Station and Joystick Pairing Procedure

The Lever Control Station and Joystick Pairing Procedure applies **only** to the following software configuration:

- Inboard joystick software is greater than 3
- Control lever station which is paired with inboard joystick software is greater than 4
- Control lever station/inboard joystick which has legacy versions of software (2/3) can be used in the same network, where those components are installed at a different station.

Before accomplishing the following procedure:

- The control system should be operational
- The engines **must not** be running and key is in the ON position
- The inboard joystick which will be paired with a lever control station is the active station.

Follow these steps to pair an inboard joystick with a lever control station.

Action: Move the inboard joystick to the full reverse position.

Result: No result.

![[15900097.png]]

Action: Press the following buttons in the sequence indicated. These three button presses **must** be completed within five seconds.

1. Port/Bow thruster button
2. Starboard/Bow thruster button
3. Port/Bow thruster button.

Result: SYSTEM DIAGNOSTIC (4) and JOYSTICK ACTIVATION light (5) will be blinking at a 2 Hz rate (2 blinks/second). The user will have 10 seconds to complete the pairing procedure from this time.

![[15o00004.png]]

Action: Press and release the ACTIVE/TAKE button (1) on the lever control station.

Result: Both the lever control station and inboard joystick will confirm the pairing by rapidly flashing (5 times) the Joystick Activation/Station Select LEDs on both the inboard joystick and lever control station.

To exit pairing procedure, turn system OFF and return control lever station to NEUTRAL position.

![[15o00005.png]]
