---
type: "Процедура"
doc: "35-008-069-tr"
title_en: "Wiring Harness, Cummins Electric Fan Clutch"
modified: "2009-01-23"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "3666322"
figures: 33
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/35/35-008-069-tr.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/35-008-069-tr.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/35"
  - "перевод/машинный"
---

# Wiring Harness, Cummins Electric Fan Clutch

> [!abstract] Процедура · `35-008-069-tr`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[3666322 — ISM, ISMe, and QSM11 Service Manual|3666322]]
> **Секции:** Section 8 - Cooling System - Group 08
> **Даты:** изменён 2009-01-23
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/35/35-008-069-tr.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/35-008-069-tr.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Эта процедура применяется к двигателям с использованием электрического сцепления вентилятора, контролируемого ECM, и с использованием электропроводки сцепления вентилятора Cummins®. Если электропроводка упряжка **не **электропроводка сцепления Cummins®, обратитесь к руководству по обслуживанию OEM для правильной процедуры устранения неполадок.

![[08200050.png]]

### Первичная проверка

Для работы вентилятора реле электромагнитного сцепления вентилятора Cummins® **должно** принимать сигнал 12-VDC от ECM для включения и сигнал 0-VDC от ECM для отключения сцепления вентилятора. Убедитесь, что правильное электрическое соединение было сделано.

Проверьте провода и проводку, чтобы убедиться, что ни один из них не сломан или не закорочен. Замените провода или провода, которые сломаны.

![[wr2cnkb.png]]

Вентиляторное сцепление будет включаться, когда он получает 12-VDC от реле вентиляторного сцепления и отключается, когда он получает 0-VDC от реле вентиляторного сцепления.

![[08200055.png]]

12-VDC подается от электрической системы автомобиля к вентилятору одним из трех возможных элементов управления:

- Ручной вентилятор включения/выключения (1) в кабине
- Переключатель давления компрессора хладагента (2)
- Переключатель (3) температуры в корпусе термостата.

![[08200033.png]]

Чтобы убедиться, что нет открытых цепей, непрерывность должна быть проверена между следующими штифтами проводной ремни:

- Pin B разъема сцепления вентилятора (1) и наземного терминала (2)

![[08200035.png]]

- Pin A разъема сцепления вентилятора (1) и следующих разъемов проводов вентилятора:

- Pin A разъема переключателя температуры (2)
- Pin B разъёма компрессорного переключателя 3 давления хладагента
- Pin B ручного разъема переключателя кабины / выключения (4).

![[08200036.png]]

- Положительный (+) 12-VDC терминал (1) и следующие разъёмы ремней вентилятора:

- Pin B разъема переключателя температуры (2)
- Pin A разъёма компрессорного переключателя хладагента (3)
- Pin A ручного разъема переключателя кабины / выключения (4).

Мультиметр **должен** читать замкнутую цепь (10 Ом или меньше). Ремонт или замена проводной упряжки, если на любой из вышеперечисленных проверок обнаружено более 10 Ом.

![[08200038.png]]

Проверьте короткие замыкания в проводах. Сопротивление должно быть больше 100 К Ом для следующих целей:

- Pin A разъёма сцепления вентилятора (1) к наземному терминалу (2)

![[08200040.png]]

- Наземный терминал (1) и следующие разъёмы ремней вентилятора:

- Pin A разъема переключателя температуры (2)
- Pin B разъёма компрессорного переключателя 3 давления хладагента
- Pin B ручного разъема переключателя кабины / выключения (4).

![[08200041.png]]

- Положительный (+) 12-VDC терминал (1) к наземному терминалу (2)

![[08200042.png]]

- Положительный (+) 12-VDC источник питания (1) и следующие разъёмы ремней вентилятора:

- Pin A разъема переключателя температуры (2)
- Pin B разъёма компрессорного переключателя 3 давления хладагента
- Pin B ручного разъема переключателя кабины / выключения (4).

![[08200043.png]]

- Pin A каждого из трех коммутационных разъемов (1) для контакта B каждого из трех коммутационных разъемов (1).

Упряжка проводов должна быть отремонтирована или заменена, если любое из вышеперечисленных сопротивлений меньше 100 Ом.

![[08200044.png]]

Для проверки переключателя (1) температуры для правильной работы проверьте непрерывность от контакта А до контакта В при комнатной температуре (должно быть более 100 Ом). Замените переключатель, если сопротивление меньше 100 К Ом.

![[08200045.png]]

Для проверки переключателя температуры на работу при температуре вентилятора Включите щуп (1) в емкость с водой вместе с термометром.

![[08200046.png]]

Поместите многометровые щупы в контакт А и контакт В.

![[08200047.png]]

Нагрейте воду.

Обратите внимание на температуру, при которой сопротивление изменяется от 100 или более ом до 10 ом или менее.

![[08200048.png]]

Если переключатель **не** закрывается при температуре, требуемой изготовителем переключателя, переключатель должен быть заменен.

![[08200049.png]]

Для проверки переключателя давления фреона и ручного вентилятора на / выключатель кабины обратитесь к рекомендациям производителя.

![[08200051.png]]

### Снятие

Отключите ручную проводку с ручным коммутатором, если она используется, от базовой проводов.

![[08200039.png]]

Удалите ремень переключения давления хладагента из базовой ремни.

![[08200037.png]]

Отсоедините серый разъём жгута проводов от переключателя температуры в корпусе термостата.

![[08200007.png]]

Отсоедините большой кольцевой терминал с черным проводом от земли шасси.

![[08200005.png]]

Отключите небольшой кольцевой терминал от источника питания.

![[08200053.png]]

Отсоедините разъем сцепления вентилятора на базовой проводах от сцепления вентилятора.

![[ea200hd.png]]

### Установка

Подключите разъем сцепления вентилятора на базовой проводах к сцеплению вентилятора.

![[ea200hd.png]]

Подключите небольшой кольцевой терминал с красным проводом к источнику питания, управляемому переключателем зажигания.

![[08200054.png]]

Подключите большой кольцевой терминал с черным проводом к земле шасси.

![[08200005.png]]

Установите переключатель температуры охлаждающей жидкости в корпус термостата, если он был удален.

![[08200004.png]]

Подключите серый разъём жгута проводов к переключателю температуры в корпусе термостата.

![[08200007.png]]

На транспортных средствах с кондиционером, если он был удален, установите соответствующий переключатель давления хладагента на стороне выпускного отверстия компрессора цепи хладагента.

![[08200006.png]]

Подключите проводку переключателя к базовой проводах и к переключателю давления хладагента.

![[08200014.png]]

Подключите управляемый оператором ручной коммутатор жгута к базовой проводах жгута.

![[08200015.png]]

Оставьте штепсель(ы) герметизации переключателя(ов) проводов в основании, если используется переключатель(ы) давления хладагента или ручной переключатель с управлением оператора **не**.

![[08200012.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> This procedure applies to engines using an electric fan clutch controlled by the ECM and utilizing a Cummins® electric fan clutch wiring harness. If the wiring harness is **not** a Cummins® electric fan clutch wiring harness, refer to the OEM service manual for the correct troubleshooting procedure.
>
> ### Initial Check
>
> For the fan to operate, the Cummins® electromagnetic fan clutch relay **must** receive a 12-VDC signal from the ECM to engage and a 0-VDC signal from the ECM to disengage the fan clutch. Be sure the correct electrical connections have been made.
>
> Inspect the wires and harness to be sure none are broken or shorted. Replace the harness or wires that are broken.
>
> The fan clutch will engage when it receives 12-VDC from the fan clutch relay and disengage when it receives 0- VDC from the fan clutch relay.
>
> The 12-VDC is supplied from the vehicle's electrical system to the fan by one of three possible controls:
>
> - The manual fan on/off switch (1) in the cab
> - The refrigerant compressor pressure switch (2)
> - The temperature switch (3) in the thermostat housing.
>
> To check to be sure there are no open circuits, the continuity **must** be checked between the following pins of the wiring harness:
>
> - Pin B of the fan clutch connector (1) and the ground terminal (2)
>
> - Pin A of the fan clutch connector (1) and the following fan harness connectors:
>
> - Pin A of the temperature switch connector (2)
> - Pin B of the refrigerant compressor pressure switch connector (3)
> - Pin B of the manual on/off cab switch connector (4).
>
> - The positive (+) 12-VDC terminal (1) and the following fan harness connectors:
>
> - Pin B of the temperature switch connector (2)
> - Pin A of the refrigerant compressor pressure switch connector (3)
> - Pin A of the manual on/off cab switch connector (4).
>
> The multimeter **must** read a closed circuit (10 ohms or less). Repair or replace the harness if more than 10 ohms is detected on any of the above checks.
>
> Check for short circuits in the harness. The resistance **must** be greater than 100K ohms for the following:
>
> - Pin A of the fan clutch connector (1) to the ground terminal (2)
>
> - The ground terminal (1) and the following fan harness connectors:
>
> - Pin A of the temperature switch connector (2)
> - Pin B of the refrigerant compressor pressure switch connector (3)
> - Pin B of the manual on/off cab switch connector (4).
>
> - The positive (+) 12-VDC terminal (1) to the ground terminal (2)
>
> - The positive (+) 12-VDC supply (1) and the following fan harness connectors:
>
> - Pin A of the temperature switch connector (2)
> - Pin B of the refrigerant compressor pressure switch connector (3)
> - Pin B of the manual on/off cab switch connector (4).
>
> - Pin A of each of the three switch connectors (1) to pin B of each of the three switch connectors (1).
>
> The harness **must** be repaired or replaced if any of the above resistances are less than 100 ohms.
>
> To check the temperature switch (1) for proper operation, check the continuity from pin A to pin B at room temperature (**must** be greater than 100 ohms). Replace the switch if the resistance is less than 100K ohms.
>
> To check the temperature switch for operation at the fan ON temperature, place the probe (1) in a container of water, along with a thermometer.
>
> Place the multimeter probes in pin A and pin B.
>
> Heat the water.
>
> Note the temperature at which the resistance changes from 100 or greater ohms to 10 ohms or less.
>
> If the switch does **not** close at the temperature required according to the switch manufacturer, the switch **must** be replaced.
>
> To check the freon compressor pressure switch and the manual fan on/off cab switch, refer to the manufacturer's recommendations.
>
> ### Remove
>
> Disconnect the operator-controlled manual switch harness, if used, from the base harness.
>
> Remove the refrigerant pressure switch harness from the base harness.
>
> Disconnect the gray harness connector from the temperature switch in the thermostat housing.
>
> Disconnect the large ring terminal with the black wire from the chassis ground.
>
> Disconnect the small ring terminal from the power source.
>
> Disconnect the fan clutch connector on the base harness from the fan clutch.
>
> ### Install
>
> Connect the fan clutch connector on the base harness to the fan clutch.
>
> Connect the small ring terminal with the red wire to an ignition switch-controlled fused power source.
>
> Connect the large ring terminal with the black wire to the chassis ground.
>
> Install the coolant temperature switch in the thermostat housing, if it was removed.
>
> Connect the gray harness connector to the temperature switch in the thermostat housing.
>
> On air-conditioned vehicles, install the appropriate refrigerant pressure switch into the compressor outlet side of the refrigerant circuit, if it was removed.
>
> Connect the switch harness to the base harness and to the refrigerant pressure switch.
>
> Connect the operator-controlled manual switch harness to the base harness.
>
> Leave the base harness switch connector sealing cap(s) in place if a refrigerant pressure switch or an operator-controlled manual switch is **not** used.
