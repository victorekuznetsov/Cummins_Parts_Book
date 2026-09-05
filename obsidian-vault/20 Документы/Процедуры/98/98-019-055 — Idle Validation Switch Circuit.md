---
aliases:
  - "Цепь выключателя подтверждения холостого хода"
type: "Процедура"
doc: "98-019-055"
title_en: "Idle Validation Switch Circuit"
title_ru: "Цепь выключателя подтверждения холостого хода"
modified: "2003-04-01"
engines:
  - "37269910"
  - "37280605"
families:
  - "K19"
manuals:
  - "3666070"
figures: 29
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-019-055.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-019-055.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K19"
  - "группа/98"
  - "перевод/машинный"
---

# Idle Validation Switch Circuit
**Цепь выключателя подтверждения холостого хода**

> [!abstract] Процедура · `98-019-055`
> **Двигатели:** [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]]
> **Семейство:** K19
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-04-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-019-055.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-019-055.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Часть этой схемы в основной проводах двигателя состоит из провода сигнала без сидения (контакт 9), провода сигнала без сидения (контакт 16) и обратного провода (контакты 25 и 26). Часть этой цепи в проводной упряжке OEM состоит из провода сигнала без сидения (pin C6-A), провода сигнала без сидения (pin C6-C) и обратного провода (pin C6-G).

![[19801684.png]]

### Проверка сопротивления

Убедитесь, что разъем переключателя проверки простаивания подключен. Отключите разъемы ECM и C6.

Выберите функцию сопротивления на мультиметре.

Прикосновение к одному из мультиметров приводит к контакту C с OEM-проводкой упряжкой стороны разъема C6. Прикосновение к другому мультиметру приводит к контакту G с OEM-проводкой стороны жгута проводов разъема C6.

Оставьте педаль дроссельной заслонки в освобожденном (пустом) положении.

![[19801891.png]]

Измерьте сопротивление.

Мультиметр **должен **показывать менее 10 Ом, что является замкнутой схемой. Если схема **не **закрыта, то в обратном проводе или проводе неработающего сигнала есть открытая схема, при условии, что выключатель уже проверен и в порядке.

![[19801619.png]]

Прикосновение к одному из мультиметров приводит к контакту C с OEM-проводкой упряжкой стороны разъема C6. Прикосновение к другому мультиметру приводит к контакту G с OEM-проводкой стороны жгута проводов разъема C6.

Ударь педалью дроссельной заслонки.

![[19802629.png]]

Измерьте сопротивление.

Мультиметр **должен **показывать более 100k ом, что является открытой схемой. Если схема **не** открыта, отремонтируйте или замените проводку OEM. См. руководство изготовителя машины по диагностике и ремонту.

![[19801621.png]]

Прикосновение к одному из мультиметров приводит к контакту А с OEM-проводкой упряжкой стороны разъема C6. Прикосновение к другому мультиметру приводит к контакту G с OEM-проводкой стороны жгута проводов разъема C6.

Ударь педалью дроссельной заслонки.

![[19801893.png]]

Измерьте сопротивление.

Мультиметр **должен **показывать менее 10 Ом, что является замкнутой схемой. Если он превышает 10 Ом, отремонтируйте электропроводку OEM или, если необходимо, замените ее. См. руководство изготовителя машины по диагностике и ремонту.

![[19801619.png]]

Прикосновение к одному из мультиметров приводит к контакту А с OEM-проводкой упряжкой стороны разъема C6. Прикосновение к другому мультиметру приводит к контакту G с OEM-проводкой стороны жгута проводов разъема C6.

Отпустите педаль дросселя.

![[19802630.png]]

Измерьте сопротивление.

Мультиметр **должен **показывать более 100k ом, что является открытой схемой. Если схема **не** открыта, отремонтируйте электропроводку OEM или, если необходимо, замените ее. См. руководство изготовителя машины по диагностике и ремонту.

![[19801621.png]]

Прикосновение к одному из мультиметров приводит к контакту 9 главного разъёма проводов двигателя. Прикосновение к другому мультиметру приводит к контакту А основной стороны проводов двигателя с ремнем разъема C6.

![[19801686.png]]

Измерьте сопротивление.

Мультиметр **должен **показывать менее 10 Ом, что является замкнутой схемой. Если цепь **не **закрыта, то в проводе сигнала без сидения есть открытая цепь.

Ремонт основной электропроводки двигателя упряжкой, или при необходимости ее замена. См. процедуру 019-228 или[[98-019-043 — Engine Wiring Harness|019-043]].

![[19801619.png]]

Повторите вышеупомянутую проверку сопротивления для провода сигнала проверки бездействия.

Прикосновение к одному из мультиметров приводит к контакту 16 главного разъёма проводов двигателя. Прикосновение к другому мультиметру приводит к контакту C на основной стороне проводов двигателя разъема C6.

Измерьте сопротивление. Мультиметр **должен **показывать менее 10 Ом.

![[19801688.png]]

Повторите вышеупомянутую проверку сопротивления для провода возврата на холостом ходу.

Прикосновение к одному из мультиметров приводит к контакту 25 или 26 главного разъёма проводов двигателя. Прикосновение к другому мультиметру приводит к контакту G на основной стороне проводов двигателя жгута проводов разъема C6.

Измерьте сопротивление. Мультиметр **должен **показывать менее 10 Ом.

![[19802631.png]]

### Проверка на замыкание на массу

Убедитесь, что разъём переключателя подключен.

Прикосновение к одному из мультиметров приводит к контакту А на стороне проводов OEM-подключателя разъема C6. Прикосновение к другому мультиметру приводит к хорошей, чистой поверхности на блоке двигателя.

![[19801895.png]]

Измерьте сопротивление.

Мультиметр **должен **показывать более 100k ом, что является открытой схемой. Если схема **не **открыта, то между проводом сигнала без сидения и землей шасси есть короткое замыкание.

Ремонт электропроводки OEM или, при необходимости, ее замена. См. руководство по устранению неполадок и ремонту OEM для процедуры.

![[19801621.png]]

Прикосновение к одному из мультиметров приводит к контакту G на основной стороне проводов двигателя жгута проводов разъема C6. Прикосновение к другому мультиметру приводит к хорошей, чистой поверхности на блоке двигателя.

Измерьте сопротивление. Мультиметр **должен **показывать менее 10 Ом.

![[19801689.png]]

Повторите вышеупомянутое короткое замыкание для проверки на землю для провода неработающего сигнала.

Прикосновение к одному из мультиметров приводит к контакту C с OEM-проводкой упряжкой стороны разъема C6. Прикосновение к другому мультиметру приводит к хорошей, чистой поверхности на блоке двигателя.

Измерьте сопротивление. Мультиметр **должен **показывать более 100k ом.

![[19801897.png]]

### Проверка на замыкание между контактами

Убедитесь, что разъемы C5 и C6 и переключатель проверки неработающих устройств отключены. Убедитесь, что педаль дросселя находится в освобожденном (пустом) положении.

Прикосновение к одному из мультиметров приводит к контакту А с OEM-проводкой упряжкой стороны разъема C6. Прикосновение к другому мультиметру приводит к **всем **другим штифтам на стороне OEM-проводов как разъемов C5, так и C6, по одному за раз.

![[19801899.png]]

Измерьте сопротивление.

Мультиметр **должен **показывать более 100k ом, что является открытой схемой. Если схема **не** открыта, то между проводами, подключенными к контакту А, и **любыми** другими штифтами, измеренными менее 100k ом.

Ремонт электропроводки OEM или, при необходимости, ее замена. См. руководство по устранению неполадок и ремонту OEM для процедуры.

![[19801621.png]]

Повторите вышеупомянутое короткое замыкание от пин-кодов до пин-контроля для провода сигнала на холостом ходу.

Прикосновение к одному из мультиметров приводит к контакту C с OEM-проводкой упряжкой стороны разъема C6. Прикосновение к другому мультиметру приводит к **всем **другим штифтам на стороне OEM-проводов как разъемов C5, так и C6, по одному за раз.

Измерьте сопротивление. Мультиметр **должен **показывать более 100k ом.

![[19801901.png]]

Повторите вышеупомянутое короткое замыкание от пин-кодов до пин-кодов для проверки обратного провода.

Прикосновение к одному из мультиметров приводит к контакту G с OEM-проводкой упряжкой стороны разъема C6. Прикосновение к другому мультиметру приводит к **всем **другим штифтам на стороне OEM-проводов как разъемов C5, так и C6, по одному за раз.

Измерьте сопротивление. Мультиметр **должен **показывать более 100k ом.

![[19801902.png]]

Проверьте короткое замыкание между контактом 9 основного разъёма проводов двигателя и **всеми **другими штифтами в разъеме.

Прикосновение к одному из мультиметров приводит к контакту 9 разъема. Прикосновение к другому мультиметру приводит к **всем **другим штифтам в разъеме, по одному за раз.

![[19801690.png]]

Измерьте сопротивление.

Мультиметр **должен **показывать более 100k ом, что является открытой схемой. Если схема **не** открыта, то между проводами, подключенными к контакту 9 главного разъёма проводов двигателя, и **любым** другим штифтом, который измеряется менее 100k Ом.

Ремонт или замена основного двигателя проводов жгута. См. процедуру 019-228 или[[98-019-043 — Engine Wiring Harness|019-043]].

![[19801621.png]]

Повторите вышеупомянутое короткое замыкание от пин-кодов до пин-кодов для провода сигнала на холостом ходу.

Прикосновение к одному из мультиметров приводит к контакту 16 главного разъёма проводов двигателя. Прикосновение к другому мультиметру приводит к **всем **другим штифтам в разъеме, по одному за раз.

Измерьте сопротивление. Мультиметр **должен **показывать более 100k ом.

![[19801692.png]]

Повторите вышеупомянутое короткое замыкание от пин-кодов до пин-кодов для провода возврата для неработающего подтверждения.

Прикосновение к одному из мультиметров приводит к контакту 25 главного разъёма проводов двигателя. Прикосновение к другому мультиметру приводит к **всем **другим штифтам в разъеме, по одному за раз, **за исключением **контакта 26.

Измерьте сопротивление. Мультиметр **должен **показывать более 100k ом.

![[19801693.png]]

### Проверьте короткое замыкание на источнике внешнего напряжения

Подключите разъем ECM. Убедитесь, что разъем C6 отключен.

Включите зажигание.

Выберите функцию постоянного напряжения на мультиметре.

Прикосновение к одному из мультиметров приводит к контакту А с OEM-проводкой упряжкой стороны разъема C6. Прикосновение к другому мультиметру приводит к заземлению блока двигателя.

![[19801903.png]]

Измерьте напряжение.

Мультиметр **must** показывает менее 1 VDC. Если напряжение **не **менее 1 VDC, то в проводе сигнала без сидения имеется короткий к внешнему источнику напряжения.

Ремонт или замена OEM проводов жгута. См. руководство по устранению неполадок и ремонту OEM для процедуры.

![[19801904.png]]

Повторите вышеупомянутое короткое замыкание на внешний источник напряжения для проверки провода неработающего сигнала.

Прикосновение к одному из мультиметров приводит к контакту C с OEM-проводкой упряжкой стороны разъема C6. Прикоснитесь к другому мультиметру, который приведет к заземлению блока двигателя.

Измерить сопротивление мультиметр **must** показывает менее 1 VDC.

![[19801905.png]]

Повторите вышеупомянутое короткое замыкание на внешний источник напряжения для проверки обратного провода.

Прикосновение к одному из мультиметров приводит к контакту G с OEM-проводкой упряжкой стороны разъема C6. Прикоснитесь к другому мультиметру, который приведет к заземлению блока двигателя.

Измерьте сопротивление. Мультиметр **must** показывает менее 1 VDC.

![[19801906.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> The portion of this circuit in the main engine harness consists of the off-idle signal wire (pin 9), the on-idle signal wire (pin 16), and the return wire (pins 25 and 26). The portion of this circuit in the OEM harness consists of the off-idle signal wire (pin C6-A), the on-idle signal wire (pin C6-C), and the return wire (pin C6-G).
>
> ### Resistance Check
>
> Make sure the idle validation switch connector is connected. Disconnect the ECM and the C6 connectors.
>
> Select the resistance function on the multimeter.
>
> Touch one of the multimeter leads to pin C of the OEM harness side of the C6 connector. Touch the other multimeter lead to pin G of the OEM harness side of the C6 connector.
>
> Leave the throttle pedal in the released (idle) position.
>
> Measure the resistance.
>
> The multimeter **must** show less than 10 ohms, which is a closed circuit. If the circuit is **not** closed, then there is an open circuit in either the return wire or the idle signal wire, provided the switch has already been checked and is okay.
>
> Touch one of the multimeter leads to pin C of the OEM harness side of the C6 connector. Touch the other multimeter lead to pin G of the OEM harness side of the C6 connector.
>
> Depress the throttle pedal.
>
> Measure the resistance.
>
> The multimeter **must** show more than 100k ohms, which is an open circuit. If the circuit is **not** open, repair or replace the OEM harness. Refer to the OEM troubleshooting and repair manual.
>
> Touch one of the multimeter leads to pin A of the OEM harness side of the C6 connector. Touch the other multimeter lead to pin G of the OEM harness side of the C6 connector.
>
> Depress the throttle pedal.
>
> Measure the resistance.
>
> The multimeter **must** show less than 10 ohms, which is a closed circuit. If it is more than 10 ohms, repair the OEM harness, or if necessary, replace it. Refer to the OEM troubleshooting and repair manual.
>
> Touch one of the multimeter leads to pin A of the OEM harness side of the C6 connector. Touch the other multimeter lead to pin G of the OEM harness side of the C6 connector.
>
> Release the throttle pedal.
>
> Measure the resistance.
>
> The multimeter **must** show more than 100k ohms, which is an open circuit. If the circuit is **not** open, repair the OEM harness, or if necessary, replace it. Refer to the OEM troubleshooting and repair manual.
>
> Touch one of the multimeter leads to pin 9 of the main engine harness connector. Touch the other multimeter lead to pin A of the main engine harness side of the C6 connector.
>
> Measure the resistance.
>
> The multimeter **must** show less than 10 ohms, which is a closed circuit. If the circuit is **not** closed, then there is an open circuit in the off-idle signal wire.
>
> Repair the main engine harness, or if necessary, replace it. Refer to Procedure 019-228 or [[98-019-043 — Engine Wiring Harness|019-043]].
>
> Repeat the above resistance check for the idle validation signal wire.
>
> Touch one of the multimeter leads to pin 16 of the main engine harness connector. Touch the other multimeter lead to pin C on the main engine harness side of the C6 connector.
>
> Measure the resistance. The multimeter **must** show less than 10 ohms.
>
> Repeat the above resistance check for the on-idle return wire.
>
> Touch one of the multimeter leads to pin 25 or 26 of the main engine harness connector. Touch the other multimeter lead to pin G on the main engine harness side of the C6 connector.
>
> Measure the resistance. The multimeter **must** show less than 10 ohms.
>
> ### Check for Short Circuit to Ground
>
> Make sure the switch connector is connected.
>
> Touch one of the multimeter leads to pin A on the OEM harness side of the C6 connector. Touch the other multimeter lead to a good, clean surface on the engine block.
>
> Measure the resistance.
>
> The multimeter **must** show more than 100k ohms, which is an open circuit. If the circuit is **not** open, then there is a short circuit between the off-idle signal wire and chassis ground.
>
> Repair the OEM harness, or, if necessary, replace it. Refer to the OEM troubleshooting and repair manual for the procedure.
>
> Touch one of the multimeter leads to pin G on the main engine harness side of the C6 connector. Touch the other multimeter lead to a good, clean surface on the engine block.
>
> Measure the resistance. The multimeter **must** show less than 10 ohms.
>
> Repeat the above short circuit to ground check for the idle signal wire.
>
> Touch one of the multimeter leads to pin C of the OEM harness side of the C6 connector. Touch the other multimeter lead to a good, clean surface on the engine block.
>
> Measure the resistance. The multimeter **must** show more than 100k ohms.
>
> ### Check for Short Circuit from Pin to Pin
>
> Make sure the C5 and C6 connectors and the idle validation switch are disconnected. Make sure the throttle pedal is in the released (idle) position.
>
> Touch one of the multimeter leads to pin A of the OEM harness side of the C6 connector. Touch the other multimeter lead to **all** other pins on the OEM harness side of both the C5 and C6 connectors, one at a time.
>
> Measure the resistance.
>
> The multimeter **must** show more than 100k ohms, which is an open circuit. If the circuit is **not** open, then there is a short circuit between the wires connected to pin A and **any** other pins that measured less than 100k ohms.
>
> Repair the OEM harness, or, if necessary, replace it. Refer to the OEM troubleshooting and repair manual for the procedure.
>
> Repeat the above short circuit from pin to pin check for the on-idle signal wire.
>
> Touch one of the multimeter leads to pin C of the OEM harness side of the C6 connector. Touch the other multimeter lead to **all** other pins on the OEM harness side of both the C5 and C6 connectors, one at a time.
>
> Measure the resistance. The multimeter **must** show more than 100k ohms.
>
> Repeat the above short circuit from pin to pin check for the return wire.
>
> Touch one of the multimeter leads to pin G of the OEM harness side of the C6 connector. Touch the other multimeter lead to **all** other pins on the OEM harness side of both the C5 and C6 connectors, one at a time.
>
> Measure the resistance. The multimeter **must** show more than 100k ohms.
>
> Check for a short circuit between pin 9 of the main engine harness connector and **all** other pins in the connector.
>
> Touch one of the multimeter leads to pin 9 of the connector. Touch the other multimeter lead to **all** other pins in the connector, one at a time.
>
> Measure the resistance.
>
> The multimeter **must** show more than 100k ohms, which is an open circuit. If the circuit is **not** open, then there is a short between the wires connected to pin 9 of the main engine harness connector and **any** other pin that measured less than 100k ohms.
>
> Repair or replace the main engine harness. Refer to Procedure 019-228 or [[98-019-043 — Engine Wiring Harness|019-043]].
>
> Repeat the above short circuit from pin to pin for the on-idle signal wire.
>
> Touch one of the multimeter leads to pin 16 of the main engine harness connector. Touch the other multimeter lead to **all** other pins in the connector, one at a time.
>
> Measure the resistance. The multimeter **must** show more than 100k ohms.
>
> Repeat the above short circuit from pin to pin for the idle validation return wire.
>
> Touch one of the multimeter leads to pin 25 of the main engine harness connector. Touch the other multimeter lead to **all** other pins in the connector, one at a time, **except** pin 26.
>
> Measure the resistance. The multimeter **must** show more than 100k ohms.
>
> ### Check for Short Circuit to External Voltage Source
>
> Connect the ECM connector. Make sure the C6 connector is disconnected.
>
> Turn keyswitch ON.
>
> Select the DC voltage function on the multimeter.
>
> Touch one of the multimeter leads to pin A of the OEM harness side of the C6 connector. Touch the other multimeter lead to the engine block ground.
>
> Measure the voltage.
>
> The multimeter **must** show less than 1 VDC. If the voltage is **not** less than 1 VDC, there is a short to an external voltage source in the off-idle signal wire.
>
> Repair or replace the OEM harness. Refer to the OEM troubleshooting and repair manual for the procedure.
>
> Repeat the above short circuit to external voltage source check for the idle signal wire.
>
> Touch one of the multimeter leads to pin C of the OEM harness side of the C6 connector. Touch the other multimeter lead to engine block ground.
>
> Measure the resistance The multimeter **must** show less than 1 VDC.
>
> Repeat the above short circuit to external voltage source check for the return wire.
>
> Touch one of the multimeter leads to pin G of the OEM harness side of the C6 connector. Touch the other multimeter lead to engine block ground.
>
> Measure the resistance. The multimeter **must** show less than 1 VDC.
