---
type: "Процедура"
doc: "98-019-065"
title_en: "Engine Oil Pressure Sensor Circuit"
modified: "2003-04-01"
engines:
  - "37269910"
  - "37280605"
families:
  - "K19"
manuals:
  - "3666070"
figures: 19
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-019-065.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-019-065.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K19"
  - "группа/98"
  - "перевод/машинный"
---

# Engine Oil Pressure Sensor Circuit

> [!abstract] Процедура · `98-019-065`
> **Двигатели:** [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]]
> **Семейство:** K19
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-04-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-019-065.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-019-065.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Часть цепи датчика в основной проводах двигателя состоит из провода питания +5-VDC (контакт 11), сигнального провода (контакт 15) и обратного провода (контакт 27).

Часть цепи датчика в проводной упряжке OEM состоит из провода питания +5-VDC (контакт C5-A), сигнального провода (контакт C5-B) и обратного провода (C5-J).

> [!note] Примечание
> Схема внутри датчика сложная. Не используйте мультиметр для проверки этого датчика. Отключите разъем датчика перед устранением неполадок в этой схеме.

![[19801834.png]]

### Проверка сопротивления

Отключите разъемы ECM и C5.

![[19801643.png]]

Выберите функцию сопротивления на мультиметре.

Прикосновение к одному из мультиметров приводит к контакту 11 главного разъёма проводов двигателя. Прикосновение к другому мультиметру приводит к контакту А основной стороны проводов двигателя с ремнем разъема С5.

![[19801644.png]]

Измерьте сопротивление.

Мультиметр **должен **показывать менее 10 Ом, что является замкнутой схемой. Если цепь **не **закрыта, в проводе питания +5-VDC есть открытая цепь.

Ремонт или замена основного двигателя проводов жгута. См. процедуру 019-228 или[[98-019-043 — Engine Wiring Harness|019-043]].

![[19801619.png]]

Повторите вышеупомянутую проверку сопротивления для сигнального провода.

Прикосновение к одному из мультиметров приводит к контакту 15 главного разъёма проводов двигателя. Прикосновение к другому мультиметру приводит к контакту B разъема C5.

Измерьте сопротивление. Мультиметр **должен **показывать менее 10 Ом.

![[19801646.png]]

Повторите вышеупомянутую проверку сопротивления для обратного провода.

Прикосновение к одному из мультиметров приводит к контакту 27 главного разъёма проводов двигателя. Прикосновение к другому мультиметру приводит к контакту J основной стороны проводов двигателя с ремнем разъема C5.

![[19801647.png]]

Измерьте сопротивление. Если мультиметр измеряет **не** менее 10 Ом, проверьте 5-амперный предохранитель в рельсовой проволоке для обратного давления для продувного предохранителя.

Если предохранитель в порядке, отремонтируйте или замените основную проводку двигателя. См. процедуру 019-228 или[[98-019-043 — Engine Wiring Harness|019-043]].

![[19801648.png]]

### Проверка на замыкание на массу

Убедитесь, что разъем C5 и датчик давления в рельсах отключены.

Прикосновение к одному из мультиметров приводит к контакту 11 главного разъёма проводов двигателя. Прикоснитесь к другому мультиметру, который приведет к заземлению блока двигателя.

![[19801649.png]]

Измерьте сопротивление.

Мультиметр **должен **показывать более 100k ом, что является открытой схемой. Если схема **не** открыта, то между проводом, подключенным к контакту 11, и землей шасси есть короткое замыкание.

Ремонт или замена основного двигателя проводов жгута. См. процедуру 019-228 или[[98-019-043 — Engine Wiring Harness|019-043]].

![[19801621.png]]

Повторите вышеупомянутое короткое замыкание, чтобы проверить наземный сигнал.

Прикосновение к одному из мультиметров приводит к контакту 15 главного разъёма проводов двигателя. Прикоснитесь к другому мультиметру, который приведет к заземлению блока двигателя.

Измерьте сопротивление. Мультиметр **должен **показывать более 100k ом.

![[19801651.png]]

### Проверка на замыкание между контактами

Убедитесь, что разъем C5 и датчик давления в рельсах отключены.

Проверьте короткое замыкание между контактом 11 главного разъёма проводов двигателя и **всеми **другими штифтами в разъеме главного разъёма проводов двигателя.

Прикосновение к одному из мультиметров приводит к контакту 11 разъема. Прикосновение к другому мультиметру приводит к **всем **другим штифтам в разъеме, по одному за раз.

![[19801652.png]]

Измерьте сопротивление.

Мультиметр **должен **показывать более 100k ом, что является открытой схемой. Если схема **не** открыта, то между проводами, подключенными к контакту 11 главного разъёма проводов двигателя, и **любым** другим штифтом, который измеряется менее 100k Ом.

Ремонт или замена основного двигателя проводов жгута. См. процедуру 019-228 или[[98-019-043 — Engine Wiring Harness|019-043]].

![[19801621.png]]

Повторите вышеупомянутое короткое замыкание от пин-кодов до пин-кодов для проверки сигнального провода.

Прикосновение к одному из мультиметров приводит к контакту 15 главного разъёма проводов двигателя. Прикосновение к другому мультиметру приводит к **всем **другим штифтам в разъеме, по одному за раз.

Измерьте сопротивление.

Мультиметр **должен **показывать более 100k ом.

![[19801654.png]]

Повторите вышеупомянутое короткое замыкание от пин-кодов до пин-кодов для проверки обратного провода.

Прикосновение к одному из мультиметров приводит к контакту 27 главного разъёма проводов двигателя. Прикосновение к другому мультиметру приводит к **всем **другим штифтам в разъеме, по одному за раз.

Измерьте сопротивление.

Мультиметр **должен **показывать более 100k ом.

![[19801655.png]]

### Проверка напряжения

Подключите разъемы C5 и C6.

Отключите датчик давления в рельсах.

Установите проводку с помощью ветвленного кабеля, номер детали. 3824775, между датчиком давления рельса и главным жгутом проводов двигателя.

Выберите функцию постоянного напряжения на мультиметре.

Включите зажигание.

![[19802632.png]]

Измерить напряжение питания путем установки проводов жгута ветвь кабеля, номер детали. 3824775, подача (контакт А) и возврат (контакт В) ведут в мультиметр.

![[19802633.png]]

Мультиметр **must** показывает от 4,75 до 5,25 VDC. Если напряжение **не** в пределах этого диапазона, а провод питания +5-VDC и обратный провод проверили нормально, проверьте цепь питания ECM и наземную цепь на наличие проблем. См. процедуру 019-008.

Если электрические цепи проверить, то ECM не удалось. Заменить ECM. См. процедуру[[98-019-031 — Engine Control Module|019-031]].

![[19801848.png]]

Измерить напряжение сигнала, установив проводной ремень ветвь кабеля, номер детали. 3824775, сигнал (контакт С) и возврат (контакт В) ведут в мультиметр.

Мультиметр покажет различный диапазон напряжения при различных показаниях давления. Смотрите таблицу ниже.

![[19802634.png]]

| Давление | Допустимая дальность напряжённости |  |
|---|---|---|
| **(кПа)** | **(пси)** | **(VDC)** |
| 0 | 0 | 0,42 - 0,54 |
| 344.74 | 50 | 1.26-1.344 |
| 689.48 | 100 | 2,06-2,14 |
| 1034.22 | 150 | 2.85 - 2.95 |
| 1389.96 | 200 | 3.63 - 3.77 |
| 1723.70 | 250 | 4.39 - 4.62 |

![[nobox.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> The portion of the sensor circuit in the main engine harness consists of the +5-VDC supply wire (pin 11), the signal wire (pin 15), and the return wire (pin 27).
>
> The portion of the sensor circuit in the OEM harness consists of the +5-VDC supply wire (pin C5-A), the signal wire (pin C5-B), and the return wire (C5-J).
>
> **Note · Примечание**
> The circuit inside the sensor is complex. Do **not** use a multimeter to check this sensor. Disconnect the sensor connector before troubleshooting this circuit.
>
> ### Resistance Check
>
> Disconnect the ECM and the C5 connectors.
>
> Select the resistance function on the multimeter.
>
> Touch one of the multimeter leads to pin 11 of the main engine harness connector. Touch the other multimeter lead to pin A of the main engine harness side of the C5 connector.
>
> Measure the resistance.
>
> The multimeter **must** show less than 10 ohms, which is a closed circuit. If the circuit is **not** closed, there is an open circuit in the +5-VDC supply wire.
>
> Repair or replace the main engine harness. Refer to Procedure 019-228 or [[98-019-043 — Engine Wiring Harness|019-043]].
>
> Repeat the above resistance check for the signal wire.
>
> Touch one of the multimeter leads to pin 15 of the main engine harness connector. Touch the other multimeter lead to pin B of the C5 connector.
>
> Measure the resistance. The multimeter **must** show less than 10 ohms.
>
> Repeat the above resistance check for the return wire.
>
> Touch one of the multimeter leads to pin 27 of the main engine harness connector. Touch the other multimeter lead to pin J of the main engine harness side of the C5 connector.
>
> Measure the resistance. If the multimeter does **not** measure less than 10 ohms, check the 5-amp fuse in the rail pressure return wire for a blown fuse.
>
> If the fuse is okay, repair or replace the main engine harness. Refer to Procedure 019-228 or [[98-019-043 — Engine Wiring Harness|019-043]].
>
> ### Check for Short Circuit to Ground
>
> Make sure the C5 connector and the rail pressure sensor are disconnected.
>
> Touch one of the multimeter leads to pin 11 of the main engine harness connector. Touch the other multimeter lead to engine block ground.
>
> Measure the resistance.
>
> The multimeter **must** show more than 100k ohms, which is an open circuit. If the circuit is **not** open, then there is a short circuit between the wire connected to pin 11 and chassis ground.
>
> Repair or replace the main engine harness. Refer to Procedure 019-228 or [[98-019-043 — Engine Wiring Harness|019-043]].
>
> Repeat the above short circuit to ground check for the signal wire.
>
> Touch one of the multimeter leads to pin 15 of the main engine harness connector. Touch the other multimeter lead to engine block ground.
>
> Measure the resistance. The multimeter **must** show more than 100k ohms.
>
> ### Check for Short Circuit from Pin to Pin
>
> Make sure the C5 connector and rail pressure sensor are disconnected.
>
> Check for a short circuit between pin 11 of the main engine harness connector and **all** other pins in the main engine harness connector.
>
> Touch one of the multimeter leads to pin 11 of the connector. Touch the other multimeter lead to **all** other pins in the connector, one at a time.
>
> Measure the resistance.
>
> The multimeter **must** show more than 100k ohms, which is an open circuit. If the circuit is **not** open, then there is a short between the wires connected to pin 11 of the main engine harness connector and **any** other pin that measured less than 100k ohms.
>
> Repair or replace the main engine harness. Refer to Procedure 019-228 or [[98-019-043 — Engine Wiring Harness|019-043]].
>
> Repeat the above short circuit from pin to pin check for the signal wire.
>
> Touch one of the multimeter leads to pin 15 of the main engine harness connector. Touch the other multimeter lead to **all** other pins in the connector, one at time.
>
> Measure the resistance.
>
> The multimeter **must** show more than 100k ohms.
>
> Repeat the above short circuit from pin to pin check for the return wire.
>
> Touch one of the multimeter leads to pin 27 of the main engine harness connector. Touch the other multimeter lead to **all** other pins in the connector, one at a time.
>
> Measure the resistance.
>
> The multimeter **must** show more than 100k ohms.
>
> ### Voltage Check
>
> Connect the C5 and C6 connectors.
>
> Disconnect the rail pressure sensor.
>
> Install breakout cable, Part No. 3824775, between the rail pressure sensor and the main engine harness.
>
> Select the DC voltage function on the multimeter.
>
> Turn keyswitch ON.
>
> Measure the supply voltage by installing the breakout cable, Part No. 3824775, supply (pin A) and return (pin B) leads into the multimeter.
>
> The multimeter **must** show between 4.75 and 5.25 VDC. If the voltage is **not** within this range and the +5-VDC supply wire and return wire have checked out okay, check the ECM power circuit and ground circuit for problems. Refer to Procedure 019-008.
>
> If the power circuits check out, then the ECM has failed. Replace the ECM. Refer to Procedure [[98-019-031 — Engine Control Module|019-031]].
>
> Measure the signal voltage by installing the breakout cable, Part No. 3824775, signal (pin C) and return (pin B) leads into the multimeter.
>
> The multimeter will show a different voltage range at various pressure readings. Refer to the table below.
>
> | Pressure | Acceptable Voltage Range |  |
> |---|---|---|
> | **(kPa)** | **(psi)** | **(VDC)** |
> | 0 | 0 | 0.42 to 0.54 |
> | 344.74 | 50 | 1.26 to 1.34 |
> | 689.48 | 100 | 2.06 to 2.14 |
> | 1034.22 | 150 | 2.85 to 2.95 |
> | 1389.96 | 200 | 3.63 to 3.77 |
> | 1723.70 | 250 | 4.39 to 4.62 |
