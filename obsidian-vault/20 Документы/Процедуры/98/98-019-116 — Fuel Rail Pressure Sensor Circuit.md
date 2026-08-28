---
type: "Процедура"
doc: "98-019-116"
title_en: "Fuel Rail Pressure Sensor Circuit"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-019-116.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-019-116.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K19"
  - "группа/98"
  - "перевод/машинный"
---

# Fuel Rail Pressure Sensor Circuit

> [!abstract] Процедура · `98-019-116`
> **Двигатели:** [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]]
> **Семейство:** K19
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-04-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-019-116.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-019-116.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Осмотр

Схема датчика состоит из проводов, подключенных к контакту 11 (провод питания +5-VDC), контакту 14 (сигнальный провод) и контакту 27 (обратный провод) главного разъёма проводов двигателя.

Отключите главный разъём жгута проводов двигателя. Промыть и очистить контакты разъема с помощью контактного очистителя, номер детали. 3824510. Проверьте разъем на наличие поврежденных контактов.

Убедитесь, что датчик отключен от основной проводов двигателя.

![[19801766.png]]

### Проверка сопротивления

> [!warning] ОСТОРОЖНО
> Не заставляйте многометровый щуп в разъемы разъема. Контакта с розеткой достаточно, чтобы получить чтение.

Отключите разъем ECM и разъем датчика.

Выберите функцию сопротивления на мультиметре.

Прикосновение к одному из мультиметров приводит к контакту 11 главного разъёма проводов двигателя. Прикосновение к другому мультиметру приводит к контакту А проводов с ремнями со стороны разъема датчика.

![[19801767.png]]

Измерьте сопротивление.

Мультиметр **должен **показывать менее 10 Ом, что является замкнутой схемой. Если цепь **не** закрыта, отремонтируйте или замените основную проводку двигателя. См. процедуру 019-228 или[[98-019-043 — Engine Wiring Harness|019-043]].

![[19801619.png]]

Прикосновение к одному из мультиметров приводит к контакту 14 главного разъёма проводов двигателя. Прикосновение к другому мультиметру приводит к контакту C основной стороны проводов двигателя с рельсовым датчиком давления разъема.

![[19801769.png]]

Измерьте сопротивление.

Мультиметр **должен **показывать менее 10 Ом, что является замкнутой схемой. Если цепь **не** закрыта, отремонтируйте или замените основную проводку двигателя. См. процедуру 019-228 или[[98-019-043 — Engine Wiring Harness|019-043]].

![[19801619.png]]

Прикосновение к одному из мультиметров приводит к контакту 27 главного разъёма проводов двигателя. Прикосновение к другому мультиметру приводит к контакту B основной стороны проводов двигателя с разъёмом датчика.

![[19801771.png]]

Измерьте сопротивление.

Мультиметр **должен **показывать менее 10 Ом, что является замкнутой схемой. Если цепь **не** закрыта, проверьте 5-амперный предохранитель в обратном проводе на продувной предохранитель. См. процедуру 019-198.

Если предохранитель в порядке, то отремонтируйте или замените основную проводку двигателя. См. процедуру 019-228 или[[98-019-043 — Engine Wiring Harness|019-043]].

![[19801619.png]]

### Проверка на замыкание на массу

Убедитесь, что разъем ECM и разъем датчика отключены.

Прикосновение к одному из мультиметров приводит к контакту 11 главного разъёма проводов двигателя. Прикосновение к другому мультиметру приводит к хорошей, чистой поверхности на блоке двигателя.

![[19801773.png]]

Измерьте сопротивление.

Мультиметр **должен **показывать более 100k ом, что является открытой схемой. Если схема **не** открыта, то между проводом, подключенным к контакту 11, и землей шасси есть короткое замыкание.

Ремонт или замена основного двигателя проводов жгута. См. процедуру 019-228 или[[98-019-043 — Engine Wiring Harness|019-043]].

![[19801621.png]]

Прикосновение к одному из мультиметров приводит к контакту 14 главного разъёма проводов двигателя. Прикосновение к другому мультиметру приводит к хорошей, чистой поверхности на блоке двигателя.

![[19801775.png]]

Измерьте сопротивление.

Мультиметр **должен **показывать более 100k ом, что является открытой схемой. Если схема **не** открыта, то между проводом, подключенным к контакту 14, и землей шасси есть короткое замыкание.

Ремонт или замена основного двигателя проводов жгута. См. процедуру 019-228 или[[98-019-043 — Engine Wiring Harness|019-043]].

![[19801621.png]]

### Проверка на замыкание между контактами

Убедитесь, что датчики, разъемы C6 и ECM отключены.

Проверьте короткое замыкание между контактом 11 главного разъёма проводов двигателя и **всеми **другими контактами в разъеме.

Прикосновение к одному из мультиметров приводит к контакту 11 разъема. Прикосновение к другому мультиметру приводит к **всем **другим штифтам в разъеме, по одному за раз.

![[19801777.png]]

Измерьте сопротивление.

Мультиметр **должен **показывать более 100k ом, что является открытой схемой. Если схема **не** открыта, то между проводами, подключенными к контакту 11 главного разъёма проводов двигателя, и **любым** другим штифтом, который измеряется менее 100k Ом. Ремонт или замена основного двигателя проводов жгута. См. процедуру 019-228 или[[98-019-043 — Engine Wiring Harness|019-043]].

![[19801621.png]]

Проверьте короткое замыкание между контактом 14 главного разъёма проводов двигателя и **всеми **другими штифтами в разъеме.

Прикосновение к одному из мультиметров приводит к контакту 14 разъема. Прикосновение к другому мультиметру приводит к **всем **другим штифтам в разъеме, по одному за раз.

![[19801779.png]]

Измерьте сопротивление.

Мультиметр **должен **показывать более 100k ом, что является открытой схемой. Если схема **не** открыта, то между проводами, подключенными к контакту 14 главного разъёма проводов двигателя, и **любым** другим штифтом, который измеряется менее 100k Ом.

Ремонт или замена основного двигателя проводов жгута. См. процедуру 019-228 или[[98-019-043 — Engine Wiring Harness|019-043]].

![[19801621.png]]

Проверьте короткое замыкание между контактом 27 основного разъёма проводов двигателя и **всеми **другими контактами в разъеме.

Прикосновение к одному из мультиметров приводит к контакту 27 разъема. Прикосновение к другому мультиметру приводит к **всем **другим штифтам в разъеме, по одному за раз.

![[19801781.png]]

Измерьте сопротивление.

Мультиметр **должен **показывать более 100k ом, что является открытой схемой. Если схема **не** открыта, то между проводами, подключенными к контакту 27 главного разъёма проводов двигателя, и **любым** другим штифтом, который измеряется менее 100k Ом.

Ремонт или замена основного двигателя проводов жгута. См. процедуру 019-228 или[[98-019-043 — Engine Wiring Harness|019-043]].

![[19801621.png]]

### Проверка напряжения

Подключите разъемы ECM и C5.

Установите проводку с помощью ветвленного кабеля, номер детали. 3824774, между датчиком давления рельса и главным упряжь для проводов двигателя.

![[19801783.png]]

Выберите функцию постоянного напряжения на мультиметре. Прикосновение положительного (+) мультиметра приводит к контакту А проводов ремня ветки кабеля. Прикосновение к другому мультиметру приводит к контакту С проводов жгута с ветвью кабеля.

Измерьте сопротивление. Мультиметр **must** показывает от 4,75 до 5,25 VDC. Если измеренное напряжение не попадает в этот диапазон, и схема датчика была проверена и в порядке, то ECM не работает. Заменить ECM. См. процедуру[[98-019-031 — Engine Control Module|019-031]].

> [!note] Примечание
> Чтобы избежать повреждения новой ECM, **все **другие активные коды ошибок должны быть исследованы до замены ECM.

![[19802691.png]]


> [!quote]- Original (English) · английский оригинал
> ### Inspect
>
> The sensor circuit consists of the wires connected to pin 11 (+5-VDC supply wire), pin 14 (signal wire), and pin 27 (return wire) of the main engine harness connector.
>
> Disconnect the main engine harness connector. Flush and clean the connector pins using contact cleaner, Part No. 3824510. Inspect the connector for damaged pins.
>
> Make sure the sensor is disconnected from the main engine harness.
>
> ### Resistance Check
>
> **CAUTION · Осторожно**
> Do not force the multimeter probe into the connector sockets. Contact with the socket is enough to get a reading.
>
> Disconnect the ECM connector and the sensor connector.
>
> Select the resistance function on the multimeter.
>
> Touch one of the multimeter leads to pin 11 of the main engine harness connector. Touch the other multimeter lead to pin A of the harness side of the sensor connector.
>
> Measure the resistance.
>
> The multimeter **must** show less than 10 ohms, which is a closed circuit. If the circuit is **not** closed, repair or replace the main engine harness. Refer to Procedure 019-228 or [[98-019-043 — Engine Wiring Harness|019-043]].
>
> Touch one of the multimeter leads to pin 14 of the main engine harness connector. Touch the other multimeter lead to pin C of the main engine harness side of the rail pressure sensor connector.
>
> Measure the resistance.
>
> The multimeter **must** show less than 10 ohms, which is a closed circuit. If the circuit is **not** closed, repair or replace the main engine harness. Refer to Procedure 019-228 or [[98-019-043 — Engine Wiring Harness|019-043]].
>
> Touch one of the multimeter leads to pin 27 of the main engine harness connector. Touch the other multimeter lead to pin B of the main engine harness side of the sensor connector.
>
> Measure the resistance.
>
> The multimeter **must** show less than 10 ohms, which is a closed circuit. If the circuit is **not** closed, check the 5 amp fuse in the return wire for a blown fuse. Refer to Procedure 019-198.
>
> If the fuse is okay, then repair or replace the main engine harness. Refer to Procedure 019-228 or [[98-019-043 — Engine Wiring Harness|019-043]].
>
> ### Check for Short Circuit to Ground
>
> Make sure the ECM connector and sensor connector are disconnected.
>
> Touch one of the multimeter leads to pin 11 of the main engine harness connector. Touch the other multimeter lead to a good, clean surface on the engine block.
>
> Measure the resistance.
>
> The multimeter **must** show more than 100k ohms, which is an open circuit. If the circuit is **not** open, then there is a short circuit between the wire connected to pin 11 and chassis ground.
>
> Repair or replace the main engine harness. Refer to Procedure 019-228 or [[98-019-043 — Engine Wiring Harness|019-043]].
>
> Touch one of the multimeter leads to pin 14 of the main engine harness connector. Touch the other multimeter lead to a good, clean surface on the engine block.
>
> Measure the resistance.
>
> The multimeter **must** show more than 100k ohms, which is an open circuit. If the circuit is **not** open, then there is a short circuit between the wire connected to pin 14 and chassis ground.
>
> Repair or replace the main engine harness. Refer to Procedure 019-228 or [[98-019-043 — Engine Wiring Harness|019-043]].
>
> ### Check for Short Circuit from Pin to Pin
>
> Make sure the sensor, C6, and ECM connectors are disconnected.
>
> Check for a short circuit between pin 11 of the main engine harness connector and **all** other pins in the connector.
>
> Touch one of the multimeter leads to pin 11 of the connector. Touch the other multimeter lead to **all** other pins in the connector, one at a time.
>
> Measure the resistance.
>
> The multimeter **must** show more than 100k ohms, which is an open circuit. If the circuit is **not** open, then there is a short between the wires connected to pin 11 of the main engine harness connector and **any** other pin that measured less than 100k ohms. Repair or replace the main engine harness. Refer to Procedure 019-228 or [[98-019-043 — Engine Wiring Harness|019-043]].
>
> Check for a short circuit between pin 14 of the main engine harness connector and **all** other pins in the connector.
>
> Touch one of the multimeter leads to pin 14 of the connector. Touch the other multimeter lead to **all** other pins in the connector, one at a time.
>
> Measure the resistance.
>
> The multimeter **must** show more than 100k ohms, which is an open circuit. If the circuit is **not** open, then there is a short between the wires connected to pin 14 of the main engine harness connector and **any** other pin that measured less than 100k ohms.
>
> Repair or replace the main engine harness. Refer to Procedure 019-228 or [[98-019-043 — Engine Wiring Harness|019-043]].
>
> Check for a short circuit between pin 27 of the main engine harness connector and **all** other pins in the connector.
>
> Touch one of the multimeter leads to pin 27 of the connector. Touch the other multimeter lead to **all** other pins in the connector, one at a time.
>
> Measure the resistance.
>
> The multimeter **must** show more than 100k ohms, which is an open circuit. If the circuit is **not** open, then there is a short between the wires connected to pin 27 of the main engine harness connector and **any** other pin that measured less than 100k ohms.
>
> Repair or replace the main engine harness. Refer to Procedure 019-228 or [[98-019-043 — Engine Wiring Harness|019-043]].
>
> ### Voltage Check
>
> Connect the ECM and C5 connectors.
>
> Install breakout cable, Part No. 3824774, between the rail pressure sensor and the main engine harness.
>
> Select the DC voltage function on the multimeter. Touch the positive (+) multimeter lead to pin A of the breakout cable. Touch the other multimeter lead to pin C of the breakout cable.
>
> Measure the resistance. The multimeter **must** show between 4.75 and 5.25 VDC. If the measured voltage does **not** fall within this range and the sensor circuit has been checked and is okay, then the ECM has failed. Replace the ECM. Refer to Procedure [[98-019-031 — Engine Control Module|019-031]].
>
> **Note · Примечание**
> To avoid damaging the new ECM, **all** other active fault codes **must** be investigated prior to replacing the ECM.
