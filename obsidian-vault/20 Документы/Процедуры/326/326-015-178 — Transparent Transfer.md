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
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/326/326-015-178.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/326-015-178.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/326"
  - "перевод/машинный"
---

# Transparent Transfer

> [!abstract] Процедура · `326-015-178`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[4358378 — Cummins® Electronic Throttle and Shift (ETS) and Cummins® Inboard Joystick Marine Con|4358378]]
> **Секции:** Section 15 - Instruments and Controls
> **Даты:** изменён 2019-08-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/326/326-015-178.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/326-015-178.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Существует три типа джойстиков: Оставайтесь в одиночестве, ассоциированные и прозрачные трансферы.

Система Cummins® Inboard Joystick поддерживает передачу управления (1) от станции рычага управления к бортовому джойстику (2) движением джойстика, когда станция рычага управления находится в нейтральном и активном положении. Чтобы передать управление от бортового джойстика к станции рычага управления, переместите станцию рычага управления из нейтрального положения. Прозрачная функция передачи данных на одну станцию. Если станция рычага управления или бортовой джойстик на другой станции хотят получить управление, кнопка «Возьми/Включи» на панели кнопок должна быть нажата дважды.

Версия 4 и большая станция управления рычагом, а также версия 3 и более мощный бортовой джойстик могут быть соединены вместе и использовать прозрачную функцию передачи. Чтобы увидеть версию бортового джойстика или станции рычага управления, посмотрите на табличку с данными, расположенную на нижней стороне устройства, или подключитесь к инструменту конфигурации бортового джойстика Cummins®.

Для использования прозрачной передачи бортовой джойстик **должен** сначала быть «парным» со станцией управления рычагом. В процессе сопряжения будет подтверждено, что каждая станция управления рычагом или бортовой джойстик **должна быть соединена с одним соответствующим блоком (станцией управления рычагом или бортовым джойстиком). Если бортовой джойстик **не в паре с рычажной станцией управления, то функция передачи станции будет такой же, как и рычажная станция управления. Станция управления рычагом и бортовой джойстик при активации будут иметь токен Active Station, который является электронным ключом, позволяющим командовать системой управления. Станция управления рычагом будет удерживать токен Active Station, когда управление первоначально передается ему от другой станции управления, или если он находится в нейтральном положении. Бортовой джойстик может быть в состоянии взять под контроль всякий раз, когда станция управления рычагом находится в нейтральном положении, просто перемещая бортовой джойстик. Бортовой джойстик будет сохранять токен Active Station до тех пор, пока станция управления рычагом не будет выведена из нейтрального положения. Когда станция управления рычагом перемещается из нейтрального положения, то станция управления рычагом принимает токен Active Station обратно из бортового джойстика. Токен Active Station может быть принят любой другой станцией стандартным процессом передачи станции.

![[15o00002.png]]

Станция управления рычагом и процедура сопряжения джойстика

Процедура сопряжения рычажной станции управления и Joystick применяется только к следующей конфигурации программного обеспечения:

- Программное обеспечение для джойстиков в салоне больше 3
- Станция рычага управления, которая в сочетании с встроенным программным обеспечением джойстика, больше 4
- Станция управления рычагом/внутренний джойстик, который имеет устаревшие версии программного обеспечения (2/3), может использоваться в одной сети, где эти компоненты установлены на другой станции.

Перед выполнением следующей процедуры:

- Система управления должна быть работоспособной
- Двигатели **не должны **работать, а ключ находится в положении ON.
- Бортовой джойстик, который будет соединен с рычажной станцией управления, является активной станцией.

Следуйте этим шагам, чтобы соединить бортовой джойстик с станцией управления рычагом.

Действие: Переместить бортовой джойстик в полное обратное положение.

Результат: Не получилось.

![[15900097.png]]

Действие: Нажмите следующие кнопки в указанной последовательности. Эти три кнопки нажатия должны быть завершены в течение пяти секунд.

1. Кнопка Port/Bow
2. Кнопка правого/нижнего съёмника
3. Кнопка Port/Bow.

Результат: Диагностический (4) и веселый (5) свет будет мигать со скоростью 2 Гц (2 мига / секунда). У пользователя будет 10 секунд, чтобы завершить процедуру сопряжения с этого времени.

![[15o00004.png]]

Действие: Нажмите и отпустите кнопку ACTIVE/TAKE (1) на стойке управления рычагом.

Результат: Как станция управления рычагом, так и бортовой джойстик подтвердят сопряжение быстро мигающими (5 раз) светодиодами Joystick Activation / Station Select на бортовой джойстике и рычажной станции управления.

Для процедуры выхода из пары выключите систему выключения и верните станцию рычага управления в положение NEUTRAL.

![[15o00005.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> There are three types of joysticks: Stand Alone, Associated, and Transparent Transfer.
>
> The Cummins® Inboard Joystick system supports transferring control (1) from control lever station to inboard joystick (2) by a movement of the joystick when the control lever station is in the neutral and active position. To transfer control from inboard joystick to control lever station, move the control lever station out of the neutral position. The transparent transfer function is per station. If a control lever station or inboard joystick at another station wants control, the “Take/Active” button on the button pad is to be pushed twice.
>
> A version 4 and greater lever control station and a version 3 and greater inboard joystick can be paired together and use the transparent transfer feature. To see the version of inboard joystick or control lever station, look at the data plate located on the underside of the device or connect with the Cummins® Inboard Joystick Configuration Tool.
>
> To use transparent transfer, the inboard joystick **must** first be “paired” with the lever control station. During the pairing process it will be confirmed that each lever control station or inboard joystick is **only** to be paired with a single corresponding unit (lever control station or inboard joystick). If an inboard joystick is **not** paired with a lever control station, then station transfer function will be the same as a lever control station. The lever control station and inboard joystick when activated will possess an Active Station Token which is an electronic key that allows commands to the control system. The lever control station will hold the Active Station Token when control is initially transferred to it from another control station, or if is **not** in the neutral position. The inboard joystick may be able to take control whenever the lever control station is in the neutral position, by simply moving the inboard joystick. The inboard joystick will retain the Active Station Token until the lever control station is moved out of the neutral position. When the lever control station is moved out the neutral position, then the lever control station takes the Active Station Token back from the inboard joystick. The Active Station Token can be taken by any other station by the standard station transfer process.
>
> Lever Control Station and Joystick Pairing Procedure
>
> The Lever Control Station and Joystick Pairing Procedure applies **only** to the following software configuration:
>
> - Inboard joystick software is greater than 3
> - Control lever station which is paired with inboard joystick software is greater than 4
> - Control lever station/inboard joystick which has legacy versions of software (2/3) can be used in the same network, where those components are installed at a different station.
>
> Before accomplishing the following procedure:
>
> - The control system should be operational
> - The engines **must not** be running and key is in the ON position
> - The inboard joystick which will be paired with a lever control station is the active station.
>
> Follow these steps to pair an inboard joystick with a lever control station.
>
> Action: Move the inboard joystick to the full reverse position.
>
> Result: No result.
>
> Action: Press the following buttons in the sequence indicated. These three button presses **must** be completed within five seconds.
>
> 1. Port/Bow thruster button
> 2. Starboard/Bow thruster button
> 3. Port/Bow thruster button.
>
> Result: SYSTEM DIAGNOSTIC (4) and JOYSTICK ACTIVATION light (5) will be blinking at a 2 Hz rate (2 blinks/second). The user will have 10 seconds to complete the pairing procedure from this time.
>
> Action: Press and release the ACTIVE/TAKE button (1) on the lever control station.
>
> Result: Both the lever control station and inboard joystick will confirm the pairing by rapidly flashing (5 times) the Joystick Activation/Station Select LEDs on both the inboard joystick and lever control station.
>
> To exit pairing procedure, turn system OFF and return control lever station to NEUTRAL position.
