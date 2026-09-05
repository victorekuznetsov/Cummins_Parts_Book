---
aliases:
  - "Цепь датчика положения педали или рычага подачи"
type: "Процедура"
doc: "98-019-086"
title_en: "Accelerator Pedal or Lever Position Sensor Circuit"
title_ru: "Цепь датчика положения педали или рычага подачи"
modified: "2003-04-01"
engines:
  - "37269910"
  - "37280605"
families:
  - "K19"
manuals:
  - "3666070"
figures: 30
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-019-086.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-019-086.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K19"
  - "группа/98"
  - "перевод/машинный"
---

# Accelerator Pedal or Lever Position Sensor Circuit
**Цепь датчика положения педали или рычага подачи**

> [!abstract] Процедура · `98-019-086`
> **Двигатели:** [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]]
> **Семейство:** K19
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-04-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-019-086.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-019-086.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Часть схемы датчика положения дроссельной заслонки в ремне электропроводки двигателя состоит из провода питания +5-VDC (контакт 13), сигнального провода (контакт 19) и обратного провода, который соединен с проводом обратного датчика давления рельса (контакт 27).

Часть датчика положения дроссельной заслонки в проводной ремне OEM состоит из провода питания +5-VDC (C6-E), сигнального провода (C6-D) и обратного провода (C6-B). Датчик должен быть проверен перед проверкой проводов. Смотрите предыдущий раздел, если датчик еще не был проверен.

![[19801665.png]]

### Проверка сопротивления

Отключите разъемы ECM и C6.

![[19801643.png]]

Выберите функцию сопротивления на мультиметре.

Прикосновение к одному из мультиметров приводит к контакту 13 главного разъёма проводов двигателя. Прикосновение к другому мультиметру приводит к контакту E основной стороны проводов двигателя с ремнем разъема C6.

![[19801666.png]]

Измерьте сопротивление.

Мультиметр **должен **показывать менее 10 Ом, что является замкнутой схемой. Если цепь **не **закрыта, в проводе питания +5-VDC есть открытая цепь.

Ремонт или замена основного двигателя проводов жгута. См. процедуру 019-228 или[[98-019-043 — Engine Wiring Harness|019-043]].

![[19801619.png]]

Повторите вышеупомянутую проверку сопротивления на сигнальном проводе.

Прикосновение к одному из мультиметров приводит к контакту 19 главного разъёма проводов двигателя. Прикосновение к другому мультиметру приводит к контакту D основной стороны проводов двигателя с ремнем разъема C6.

Измерьте сопротивление. Мультиметр **должен **показывать менее 10 Ом.

![[19801668.png]]

Повторите вышеупомянутую проверку сопротивления на обратном проводе. Прикосновение к одному из мультиметров приводит к контакту 27 главного разъёма проводов двигателя. Прикосновение к другому мультиметру приводит к контакту В основной стороны проводов двигателя с ремнем разъема C6.

Измерьте сопротивление. Мультиметр **должен **показывать менее 10 Ом. Если цепь **не** закрыта, проверьте 5-амперный предохранитель в проводе обратного датчика давления рельса.

Если предохранитель в порядке, отремонтируйте или замените основную проводку двигателя. См. процедуру 019-228 или[[98-019-043 — Engine Wiring Harness|019-043]].

![[19801669.png]]

Прикосновение к одному из мультиметров приводит к контакту E на стороне проводов OEM-подключателя разъема C6.

Прикосновение к другому мультиметру приводит к контакту B с OEM-проводкой стороны жгута проводов разъема C6.

![[19801871.png]]

Измерьте сопротивление.

Мультиметр **должен **показывать от 2000 до 3000 Ом. Если сопротивление **не** попадает в этот диапазон, и датчик уже проверен, то в подаче +5-VDC или обратном проводе имеется либо открытый контур, либо короткое замыкание.

Ремонт электропроводки OEM или, при необходимости, ее замена. См. процедуру 019-071.

![[19801872.png]]

Прикосновение к одному из мультиметров приводит к контакту E на стороне проводов OEM-подключателя разъема C6.

Прикосновение к другому мультиметру приводит к контакту D с OEM-проводкой стороны жгута проводов разъема C6.

![[19801873.png]]

Измерьте сопротивление.

Мультиметр **должен **показывать от 1500 до 3000 Ом. Если сопротивление **не** попадает в этот диапазон, то в сигнальном проводе имеется открытая цепь.

Ремонт электропроводки OEM или, при необходимости, ее замена. См. процедуру 019-071.

![[19801874.png]]

### Проверка на замыкание на массу

Убедитесь, что разъемы C6 и ECM отключены.

Прикосновение к одному из мультиметров приводит к контакту 13 главного разъёма проводов двигателя. Прикосновение к другому мультиметру приводит к хорошей, чистой поверхности на блоке двигателя.

![[19801670.png]]

Измерьте сопротивление.

Мультиметр **должен **показывать более 100k ом, что является открытой схемой. Если схема **не** открыта, между проводом, подключенным к контакту 13, и землей шасси есть короткое замыкание. Ремонт или замена основного двигателя проводов жгута.

См. процедуру 019-228 или[[98-019-043 — Engine Wiring Harness|019-043]].

![[19801621.png]]

Повторите вышеупомянутую короткую проверку на землю для сигнального провода.

Прикосновение к одному из мультиметров приводит к контакту 19 главного разъёма проводов двигателя. Прикосновение к другому мультиметру приводит к хорошей, чистой поверхности на блоке двигателя.

Измерьте сопротивление. Мультиметр **должен **показывать более 100k ом.

![[19801672.png]]

Прикосновение к одному из мультиметров приводит к контакту Е проводов OEM-узла со стороны разъема C6. Прикосновение к другому мультиметру приводит к хорошей, чистой поверхности на блоке двигателя.

![[19801875.png]]

Измерьте сопротивление.

Мультиметр **должен **показывать более 100k ом, что является открытой схемой. Если схема **не **открыта, то есть короткое замыкание для заземления в проводе питания +5-VDC.

Ремонт электропроводки OEM или, при необходимости, ее замена. См. процедуру 019-071.

![[19801621.png]]

Повторите вышеупомянутое короткое замыкание, чтобы проверить наземный сигнал.

Прикосновение к одному из мультиметров приводит к контакту D с OEM-проводкой упряжкой стороны разъема C6. Прикосновение к другому мультиметру приводит к хорошей, чистой поверхности блока двигателя.

Измерьте сопротивление. Мультиметр **должен **показывать более 100k ом.

![[19801876.png]]

### Проверка на замыкание между контактами

Убедитесь, что разъем ECM и разъемы C6 и C5 отключены.

Для проверки OEM-части схемы убедитесь, что датчик положения дроссельной заслонки отключен.

Проверьте короткое замыкание между контактом 13 основного разъёма проводов двигателя и **всеми **другими контактами в разъеме.

Прикосновение к одному из мультиметров приводит к контакту 13 разъема. Прикосновение к другому мультиметру приводит к **всем **другим штифтам в разъеме, по одному за раз.

![[19801674.png]]

Измерьте сопротивление.

Мультиметр **должен **показывать более 100k ом, что является открытой схемой. Если схема **не** открыта, между проводами, подключенными к контакту 13 главного разъёма проводов двигателя, и **любым** другим штифтом, который измеряется менее 100k Ом.

Ремонт или замена основного двигателя проводов жгута. См. процедуру 019-228 или[[98-019-043 — Engine Wiring Harness|019-043]].

![[19801621.png]]

Повторите вышеупомянутое короткое замыкание от пин-кодов до пин-кодов для проверки сигнального провода.

Прикосновение к одному из мультиметров приводит к контакту 19 главного разъёма проводов двигателя. Прикосновение к другому мультиметру приводит к **всем **другим штифтам в разъеме ремней электропроводки двигателя, по одному за раз.

Измерьте сопротивление. Мультиметр **должен **показывать более 100k ом.

![[19801676.png]]

Повторите вышеупомянутое короткое замыкание от пин-кодов до пин-кодов для проверки обратного провода.

Прикосновение к одному из мультиметров приводит к контакту 27 главного разъёма проводов двигателя. Прикосновение к другому мультиметру приводит к **всем **другим штифтам в разъеме ремней электропроводки двигателя, по одному за раз.

Измерьте сопротивление. Мультиметр **должен **показывать более 100k ом.

![[19801781.png]]

Прикосновение к одному из мультиметров приводит к контакту E на стороне разъёма OEM-проводов жгута проводов разъема C6. Прикосновение к другому мультиметру приводит к **всем **другим штифтам на стороне OEM-проводов как разъемов C5, так и C6, по одному за раз.

![[19801878.png]]

Измерьте сопротивление.

Мультиметр **должен **показывать более 100k ом, что является открытой схемой. Если схема **не **открыта, то в проводной упряжке есть короткое замыкание между проводом питания +5-VDC и любым проводом, подключенным к штифту, который измеряется менее 100k Ом.

Ремонт электропроводки OEM или, при необходимости, ее замена. См. процедуру 019-071.

![[19801621.png]]

Повторите вышеупомянутое короткое замыкание от пин-кодов до пин-кодов для проверки сигнального провода.

Прикосновение к одному из мультиметров приводит к контакту D с OEM-проводкой упряжкой стороны разъема C6. Прикоснитесь к другому мультиметру, чтобы **все **другие контакты на стороне OEM-проводов разъёмов C5 и C6, по одному за раз.

Измерьте сопротивление. Мультиметр **должен **показывать более 100k ом.

![[19801880.png]]

Повторите вышеупомянутое короткое замыкание от пин-кодов до пин-кодов для проверки обратного провода. Прикосновение к одному из мультиметров приводит к контакту В с OEM-проводкой упряжкой стороны разъема C6. Прикоснитесь к другому мультиметру, чтобы **все **другие контакты на стороне OEM-проводов жгутов проводов как разъемов C5, так и C6.

Измерьте сопротивление. Мультиметр **должен **показывать более 100k ом.

![[19801881.png]]

### Проверка напряжения

Убедитесь, что разъем ECM и разъем C5 подключены.

Отключите разъем C6.

Выберите функцию постоянного напряжения на мультиметре.

Включите зажигание.

Прикосновение к одному из мультиметров приводит к контакту Е основной стороны проводов двигателя с ремнем разъема С6. Прикосновение к другому мультиметру приводит к хорошей, чистой поверхности на блоке двигателя.

![[19801682.png]]

Измерьте напряжение.

Мультиметр **must** показывает от 4,75 до 5,25 VDC. Если измеренное напряжение не попадает в этот диапазон, замените ECM. См. процедуру[[98-019-031 — Engine Control Module|019-031]].

![[19801683.png]]

### Проверьте короткое замыкание на источнике внешнего напряжения

Убедитесь, что разъем ECM отключен.

Подключите разъемы C5 и C6.

Выберите функцию постоянного напряжения на мультиметре.

Включите зажигание.

Прикосновение к одному из мультиметров приводит к контакту 13 главного разъёма проводов двигателя. Прикосновение к другому мультиметру приводит к хорошей, чистой поверхности на блоке двигателя.

![[19801678.png]]

Измерьте напряжение.

Мультиметр **must** показывает 1.0 VDC или меньше. Если напряжение **не** менее 1,0 ВДК, то найдите внешний источник напряжения и удалите его из положения дроссельной заслонки +5-ВДК питающего провода.

![[19801679.png]]

Повторите вышеприведенное короткое на внешнее напряжение проверку источника для сигнала положения дроссельной заслонки.

Прикосновение к одному из мультиметров приводит к контакту 19 главного разъёма проводов двигателя. Прикосновение к другому мультиметру приводит к хорошей, чистой поверхности на блоке двигателя.

Измерьте сопротивление. Мультиметр **must** показывает 1.0 VDC или меньше.

![[19801680.png]]

Повторите вышеприведенную короткую проверку источника внешнего напряжения для обратного провода положения дроссельной заслонки.

Прикосновение к одному из мультиметров приводит к контакту 27 главного разъёма проводов двигателя. Прикосновение к другому мультиметру приводит к хорошей, чистой поверхности на блоке двигателя.

Измерьте сопротивление. Мультиметр **must** показывает 1.0 VDC или меньше.

![[19801681.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> The portion of the throttle position sensor circuit in the engine harness consists of the +5-VDC supply wire (pin 13), the signal wire (pin 19), and the return wire, which is connected to the rail pressure sensor return wire (pin 27).
>
> The portion of the throttle position sensor in the OEM harness consists of the +5-VDC supply wire (C6-E), the signal wire (C6-D), and the return wire (C6-B). The sensor should be checked before checking the wiring. Refer to previous section if sensor has **not** been checked yet.
>
> ### Resistance Check
>
> Disconnect the ECM and C6 connectors.
>
> Select the resistance function on the multimeter.
>
> Touch one of the multimeter leads to pin 13 of the main engine harness connector. Touch the other multimeter lead to pin E of the main engine harness side of the C6 connector.
>
> Measure the resistance.
>
> The multimeter **must** show less than 10 ohms, which is a closed circuit. If the circuit is **not** closed, there is an open circuit in the +5-VDC supply wire.
>
> Repair or replace the main engine harness. Refer to Procedure 019-228 or [[98-019-043 — Engine Wiring Harness|019-043]].
>
> Repeat the above resistance check on the signal wire.
>
> Touch one of the multimeter leads to pin 19 of the main engine harness connector. Touch the other multimeter lead to pin D of the main engine harness side of the C6 connector.
>
> Measure the resistance. The multimeter **must** show less than 10 ohms.
>
> Repeat the above resistance check on the return wire. Touch one of the multimeter leads to pin 27 of the main engine harness connector. Touch the other multimeter lead to pin B of the main engine harness side of the C6 connector.
>
> Measure the resistance. The multimeter **must** show less than 10 ohms. If the circuit is **not** closed, check the 5-amp fuse in the rail pressure sensor return wire.
>
> If the fuse is okay, repair or replace the main engine harness. Refer to Procedure 019-228 or [[98-019-043 — Engine Wiring Harness|019-043]].
>
> Touch one of the multimeter leads to pin E on the OEM harness side of the C6 connector.
>
> Touch the other multimeter lead to pin B of the OEM harness side of the C6 connector.
>
> Measure the resistance.
>
> The multimeter **must** show between 2000 and 3000 ohms. If the resistance does **not** fall within this range and the sensor has already been checked, then there is either an open circuit or a short circuit in the +5-VDC supply wire or the return wire.
>
> Repair the OEM harness, or, if necessary, replace it. Refer to Procedure 019-071.
>
> Touch one of the multimeter leads to pin E on the OEM harness side of the C6 connector.
>
> Touch the other multimeter lead to pin D of the OEM harness side of the C6 connector.
>
> Measure the resistance.
>
> The multimeter **must** show between 1500 and 3000 ohms. If the resistance does **not** fall within this range, then there is an open circuit in the signal wire.
>
> Repair the OEM harness, or, if necessary, replace it. Refer to Procedure 019-071.
>
> ### Check for Short Circuit to Ground
>
> Make sure the C6 and ECM connectors are disconnected.
>
> Touch one of the multimeter leads to pin 13 of the main engine harness connector. Touch the other multimeter lead to a good, clean surface on the engine block.
>
> Measure the resistance.
>
> The multimeter **must** show more than 100k ohms, which is an open circuit. If the circuit is **not** open, there is a short circuit between the wire connected to pin 13 and chassis ground. Repair or replace the main engine harness.
>
> Refer to Procedure 019-228 or [[98-019-043 — Engine Wiring Harness|019-043]].
>
> Repeat the above short to ground check for the signal wire.
>
> Touch one of the multimeter leads to pin 19 of the main engine harness connector. Touch the other multimeter lead to a good, clean surface on the engine block.
>
> Measure the resistance. The multimeter **must** show more than 100k ohms.
>
> Touch one of the multimeter leads to pin E of the OEM harness side of the C6 connector. Touch the other multimeter lead to a good, clean surface on the engine block.
>
> Measure the resistance.
>
> The multimeter **must** show more than 100k ohms, which is an open circuit. If the circuit is **not** open, then there is a short circuit to ground in the +5-VDC supply wire.
>
> Repair the OEM harness, or, if necessary, replace it. Refer to Procedure 019-071.
>
> Repeat the above short circuit to ground check for the signal wire.
>
> Touch one of the multimeter leads to pin D of the OEM harness side of the C6 connector. Touch the other multimeter lead to a good, clean surface of the engine block.
>
> Measure the resistance. The multimeter **must** show more than 100k ohms.
>
> ### Check for Short Circuit from Pin to Pin
>
> Make sure the ECM connector and the C6 and C5 connectors are disconnected.
>
> For the check on the OEM portion of the circuit, make sure the throttle position sensor is disconnected.
>
> Check for a short circuit between pin 13 of the main engine harness connector and **all** other pins in the connector.
>
> Touch one of the multimeter leads to pin 13 of the connector. Touch the other multimeter lead to **all** other pins in the connector, one at a time.
>
> Measure the resistance.
>
> The multimeter **must** show more than 100k ohms, which is an open circuit. If the circuit is **not** open, there is a short between the wires connected to pin 13 of the main engine harness connector and **any** other pin that measured less than 100k ohms.
>
> Repair or replace the main engine harness. Refer to Procedure 019-228 or [[98-019-043 — Engine Wiring Harness|019-043]].
>
> Repeat the above short circuit from pin to pin check for the signal wire.
>
> Touch one of the multimeter leads to pin 19 of the main engine harness connector. Touch the other multimeter lead to **all** other pins in the engine harness connector, one at a time.
>
> Measure the resistance. The multimeter **must** show more than 100k ohms.
>
> Repeat the above short circuit from pin to pin check for the return wire.
>
> Touch one of the multimeter leads to pin 27 of the main engine harness connector. Touch the other multimeter lead to **all** other pins in the engine harness connector, one at a time.
>
> Measure the resistance. The multimeter **must** show more than 100k ohms.
>
> Touch one of the multimeter leads to pin E on the OEM harness connector side of the C6 connector. Touch the other multimeter lead to **all** other pins on the OEM harness side of both the C5 and C6 connectors, one at a time.
>
> Measure the resistance.
>
> The multimeter **must** show more than 100k ohms, which is an open circuit. If the circuit is **not** open, then there is a short circuit in the wiring harness between the +5-VDC supply wire and **any** wire connected to the pin that measured less than 100k ohms.
>
> Repair the OEM harness, or, if necessary, replace it. Refer to Procedure 019-071.
>
> Repeat the above short circuit from pin to pin check for the signal wire.
>
> Touch one of the multimeter leads to pin D of the OEM harness side of the C6 connector. Touch the other multimeter to **all** other pins on the OEM harness side of both the C5 and C6 connectors, one at a time.
>
> Measure the resistance. The multimeter **must** show more than 100k ohms.
>
> Repeat the above short circuit from pin to pin check for the return wire. Touch one of the multimeter leads to pin B of the OEM harness side of the C6 connector. Touch the other multimeter to **all** other pins on the OEM harness side of both the C5 and C6 connectors.
>
> Measure the resistance. The multimeter **must** show more than 100k ohms.
>
> ### Voltage Check
>
> Make sure the ECM connector and the C5 connector are connected.
>
> Disconnect the C6 connector.
>
> Select the DC voltage function on the multimeter.
>
> Turn keyswitch ON.
>
> Touch one of the multimeter leads to pin E of the main engine harness side of the C6 connector. Touch the other multimeter lead to a good, clean surface on the engine block.
>
> Measure the voltage.
>
> The multimeter **must** show between 4.75 and 5.25 VDC. If the measured voltage does **not** fall within this range, replace the ECM. Refer to Procedure [[98-019-031 — Engine Control Module|019-031]].
>
> ### Check for Short Circuit to External Voltage Source
>
> Make sure the ECM connector is disconnected.
>
> Connect the C5 and C6 connectors.
>
> Select the DC voltage function on the multimeter.
>
> Turn keyswitch ON.
>
> Touch one of the multimeter leads to pin 13 of the main engine harness connector. Touch the other multimeter lead to a good, clean surface on the engine block.
>
> Measure the voltage.
>
> The multimeter **must** show 1.0 VDC or less. If the voltage is **not** less than 1.0 VDC, then locate the external voltage source, and remove it from the throttle position +5-VDC supply wire.
>
> Repeat the above short to external voltage source check for the throttle position signal wire.
>
> Touch one of the multimeter leads to pin 19 of the main engine harness connector. Touch the other multimeter lead to a good, clean surface on the engine block.
>
> Measure the resistance. The multimeter **must** show 1.0 VDC or less.
>
> Repeat the above short to external voltage source check for the throttle position return wire.
>
> Touch one of the multimeter leads to pin 27 of the main engine harness connector. Touch the other multimeter lead to a good, clean surface on the engine block.
>
> Measure the resistance. The multimeter **must** show 1.0 VDC or less.
