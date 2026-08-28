---
type: "Процедура"
doc: "326-015-177"
title_en: "Dual Relay Module"
modified: "2019-08-20"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "4358378"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/326/326-015-177.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/326-015-177.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/326"
  - "перевод/машинный"
---

# Dual Relay Module

> [!abstract] Процедура · `326-015-177`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[4358378 — Cummins® Electronic Throttle and Shift (ETS) and Cummins® Inboard Joystick Marine Con|4358378]]
> **Секции:** Section 15 - Instruments and Controls
> **Даты:** изменён 2019-08-20
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/326/326-015-177.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/326-015-177.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Сигнал активации Джойстика открывает и закрывает двойное реле Функции 5 и 6 в ремне электропроводки интерфейса двигателя (в случае использования коммутатора или аналоговых модулей интерфейса двигателя) или может управлять внутренними реле, существующими в шлюзе CAN. Cummins Inc. **не несет ответственности за любые оригинальные компоненты, поставляемые производителем оборудования (OEM), подключенные к функции 5 и 6 двойного реле. Модуль двойного реле **доступен только с коммутаторными и аналоговыми интерфейсными модулями. Справочная схема проводов, Бюллетень 4358381, при необходимости. См. процедуру 015-179 CAN Gateway для получения дополнительной информации об использовании Joystick Activation Signal и CAN Gateway.

Процедура применяется к следующей конфигурации программного обеспечения:

- Встроенный Joystick версии 2.17 и выше
- Модуль Thruster Interface версии 2.10 и выше.

**Сигнал активации смайлика**

Сигнал активации Joystick доступен с шлюзом CAN через 4-контактный разъем. OEM отвечает за изготовление собственной электропроводки. Сигнал активации Joystick управляет внутренними реле в шлюзе CAN вместо использования модуля двойного реле. Функции 5 и 6 остаются прежними. См. диаграмму проводов, Бюллетень 4358381, для получения дополнительной информации.

Во время сигнала Функции 5 сигнал активации джойстика активирует Функцию 5. Функция 5 активируется, когда джойстик смещается с нейтральной точки. Функция 5 будет активирована, если кнопки двигателя нажаты во время работы головки управления. После перехода в режим джойстика Функция 5 будет оставаться активированной до тех пор, пока ручки станции рычага управления не будут выведены из нейтрального состояния, затем Функция 5 будет деактивирована.

Во время сигнала Функции 6 сигнал активации джойстика использует как Функцию 5, так и 6. При джойстике ручка перемещается из нейтрального положения, Функция 5 и 6 активируются (ретранслируют контакты открытые/закрытые) в течение предписанного количества времени (в секундах). Когда управление возвращается на станцию управления рычагом (ручки станции управления рычагом перемещаются из нейтральной зоны), тогда Функция 5 и 6 снова активируются в течение предписанного количества времени.

![[15o00001.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> The Joystick Activation Signal opens and closes the Function 5 and 6 dual relay within the thruster interface data harness (in case of using the switch or analog based thruster interface modules) or it could drive internal relays existing in the CAN gateway. Cummins Inc. is **not** responsible for any original equipment manufacturer (OEM) supplied components connected to the dual relay Function 5 and 6. The dual relay module is **only** available with the switch-based and analog-based thruster interface modules. Reference wiring Diagram, Bulletin 4358381, if necessary. Refer to Procedure 015-179 CAN Gateway for more information about using Joystick Activation Signal and CAN Gateway.
>
> The procedure applies to the following software configuration:
>
> - Inboard Joystick version 2.17 and greater
> - Thruster Interface Module version 2.10 and greater.
>
> **Joystick Activation Signal**
>
> Joystick activation signal is available with the CAN gateway via a 4 pin connector. The OEM is responsible for fabricating their own harness. Joystick activation signal drives internal relays within the CAN Gateway instead of using the Dual Relay Module. Function 5 and 6 remains the same. Refer to wiring diagram, Bulletin 4358381, for more information.
>
> During Function 5 signal, the joystick activation signal activates Function 5. Function 5 will be activated when the joystick is moved off neutral. Function 5 will **not** be activated if the thruster buttons are pressed while the control head is active. Once in joystick mode, Function 5 will remain activated until the control lever station handles are moved out of neutral, then Function 5 is deactivated.
>
> During Function 6 signal, the joystick activation signal uses both Function 5 and 6. When the joystick knob is moved from the neutral position, Function 5 and 6 will activate (relay contacts open/close) for the prescribed amount of time (in seconds). When control is returned to the lever control station (lever control station handles are moved out of neutral), then Function 5 and 6 will activate again for the prescribed amount of time.
