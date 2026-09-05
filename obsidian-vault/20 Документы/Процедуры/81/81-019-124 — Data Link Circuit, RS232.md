---
type: "Процедура"
doc: "81-019-124"
title_en: "Data Link Circuit, RS232"
modified: "2003-08-26"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
families:
  - "QSK60"
manuals:
  - "3666410"
figures: 21
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/81/81-019-124.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/81-019-124.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK60"
  - "группа/81"
  - "перевод/машинный"
---

# Data Link Circuit, RS232

> [!abstract] Процедура · `81-019-124`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]]
> **Семейство:** QSK60
> **Входит в руководства:** [[3666410 — QSK45 and QSK60 CENSE™ Electronic Control System Troubleshooting and Repair Manual|3666410]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-08-26
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/81/81-019-124.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/81-019-124.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Схема шины данных RS232 CAN используется INSITETM для связи с CENSETM ECM.

![[19a00042.png]]

Шина данных CAN использует 3-контактный разъем Deutsch. Позиции проводов следуют:

1. Пин А: - Земля
2. Пин С: - CAN Data Bus Transmit (Tx)
3. Пин Б: - CAN Data Bus Receive (Rx)
4. Ключ

Процедуры, которые следуют, охватывают разъем шины данных CAN, расположенный в кабине, и разъем шины данных CAN на стороне двигателя.

![[19801472.png]]

### Проверка сопротивления

**Двигатель расположен на CENSE**

Отсоедините проводку OEM от 23-контактного OEM-разъема CENSETM. Удалите провода CENSETM с расположением двигателя, разъёмы ECM A и B из ECM. См. процедуру 019-043.

Используйте измерительный щуп, номер детали. 3822758, на разъеме ECM и Части No. 3824811, на 23-контактном разъеме Deutsch. Выключите замок зажигания.

Измерить сопротивление от контакта 33 проводов CENSETM с помощью разъема ECM A для контакта L 23-контактного разъема Deutsch. Мультиметр **должен** показать замкнутую цепь (10 Ом и менее). Если цепь **не** закрыта, отремонтируйте или замените проводную упряжку CENSETM. См. процедуру 019-043.

![[19400570.png]]

Измерить сопротивление от контакта 22 проводов CENSETM с помощью разъема ECM A до контакта M 23-контактного разъема Deutsch. Мультиметр **должен** показать замкнутую цепь (10 Ом и менее).

Если цепь **не** закрыта, отремонтируйте или замените проводную упряжку CENSETM. См. процедуру 019-043.

![[19400571.png]]

Измерить сопротивление от контакта 13 проводов CENSETM с помощью разъема ECM B к контакту N 23-контактного разъема Deutsch. Мультиметр **должен** показать замкнутую цепь (10 Ом и менее).

Если цепь **не** закрыта, отремонтируйте или замените электропроводку двигателя. См. процедуру 019-043. Если все измерения соответствуют спецификациям, проводная упряжка OEM должна быть проверена. См. руководство по OEM.

![[19400572.png]]

Отсоедините проводку OEM от 23-контактного OEM-разъема CENSETM. Удалите провода CENSETM с расположением двигателя, разъёмы ECM A и B из ECM. См. процедуру 019-043.

Используйте измерительный щуп, номер детали. 3822758, на разъеме ECM и, номер детали. 3824811, на 3-контактном разъеме Deutsch. Выключите замок зажигания.

Измерьте сопротивление от контакта 33 проводов CENSETM с помощью разъема ECM A к контакту C 3-контактного разъема Deutsch. Мультиметр **должен** показать замкнутую цепь (10 Ом и менее).

Если цепь **не** закрыта, отремонтируйте или замените проводную упряжку CENSETM. См. процедуру 019-043.

![[19400629.png]]

Измерьте сопротивление от контакта 22 проводов CENSETM с помощью разъема ECM A к контакту B 3-контактного разъема Deutsch. Мультиметр **должен** показать замкнутую цепь (10 Ом и менее).

Если цепь **не** закрыта, отремонтируйте или замените проводную упряжку CENSETM. См. процедуру 019-043.

![[19400630.png]]

Измерьте сопротивление от контакта 13 проводов CENSETM с помощью разъема ECM B для контакта A с 3-контактным разъемом Deutsch. Мультиметр **должен** показать замкнутую цепь (10 Ом и менее).

Если цепь **не** закрыта, отремонтируйте или замените электропроводку двигателя. См. процедуру 019-043.

Если все измерения соответствуют спецификациям, проводная упряжка OEM должна быть проверена. См. руководство по OEM.

![[19400631.png]]

### Проверка на замыкание на массу

**Cab-Located CENSETM**

Используйте измерительный щуп, номер детали. 3824811, для кабины расположен 23-контактный разъем Deutsch. Отключите 23-контактный OEM-разъем Deutsch. Отключите разъемы ECM A и B.

Измерьте сопротивление от контакта L 23-контактного разъема Deutsch к заземлению блока двигателя. Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Если схема **не** открыта, отремонтируйте или замените проводную упряжку CENSETM. См. процедуру 019-043.

![[19400575.png]]

Измерьте сопротивление от контакта M 23-контактного разъема Deutsch к заземлению блока двигателя. Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Если схема **не** открыта, отремонтируйте или замените проводную упряжку CENSETM. См. процедуру 019-043.

![[19400576.png]]

Измерьте сопротивление от контакта N 23-контактного разъема Deutsch к заземлению блока двигателя. Мультиметр **должен** показывать открытую схему (10 Ом или меньше).

Если схема **не** открыта, отремонтируйте или замените проводную упряжку CENSETM. См. процедуру 019-043.

![[19400577.png]]

**Средства, используемые в CENSE**

Используйте измерительный щуп, номер детали. 3824811, для 3-контактного разъема Deutsch. Отключите разъемы ECM A и B.

Измерьте сопротивление от контакта А 3-контактного разъема Deutsch к заземлению блока двигателя. Мультиметр **должен** показывать открытую схему (10 Ом или меньше).

Если схема **не** открыта, отремонтируйте или замените проводную упряжку CENSETM. См. процедуру 019-043.

![[19400628.png]]

Измерьте сопротивление от контакта B 3-контактного разъема Deutsch к заземлению блока двигателя. Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Если схема **не** открыта, отремонтируйте или замените проводную упряжку CENSETM. См. процедуру 019-043.

![[19400626.png]]

Измерьте сопротивление от контакта C 3-контактного разъема Deutsch к заземлению блока двигателя. Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Если схема **не** открыта, отремонтируйте или замените проводную упряжку CENSETM. См. процедуру 019-043.

![[19400627.png]]

### Проверка на замыкание между контактами

**разъём электропроводки жгута проводов**

Отсоедините 40-контактные разъемы CENSE A и B Deutsch от ECM. Отсоедините 31-контактные и 23-контактные OEM-разъемы от OEM-проводов.

Используйте измерительный щуп, номер детали. 3822758, для 40-контактных разъемов Deutsch CENSETM ECM. Измерьте сопротивление контакта 33 разъёма ECM B ко всем другим штифтам в разъеме ECM B. Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Если схема **не** открыта, отремонтируйте или замените проводную упряжку CENSETM. См. процедуру 019-043.

![[19a00534.png]]

Теперь измеряют сопротивление от контакта 33 разъема ECM B ко всем штифтам **в разъеме ECM A**. Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Если схема **не** открыта, отремонтируйте или замените проводную упряжку CENSETM. См. процедуру 019-043.

![[19a00534.png]]

Измерьте сопротивление от контакта 22 разъема ECM A со всеми другими штифтами в разъеме ECM A. Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Если схема **не** открыта, отремонтируйте или замените проводную упряжку CENSETM. См. процедуру 019-043.

![[19a00535.png]]

### Проверка напряжения

Найдите разъем шины данных CAN на проводной ремне CENSETM.

Показано соединение шины данных CAN.

![[19400623.png]]

> [!warning] ОСТОРОЖНО
> Чтобы избежать повреждения штифта и проводов, используйте измерительный щуп, номер детали. 3824811.

Выберите функцию VDC на мультиметре.

Измерьте напряжение от контакта C 3-контактного разъема Deutsch до контакта A. Мультиметр **must** показывает -10,0 VDC (минимум -8,5 до максимума -11,0 VDC).

Если напряжение отсутствует, цепь шины данных CAN должна быть проверена на открытую цепь. Убедитесь, что напряжение батареи правильное.

![[19a00536.png]]

Измерьте напряжение от контакта B 3-контактного разъема Deutsch до контакта A.

Мультиметр **must** показывает 0 VDC. Если напряжение присутствует, шина данных CAN должна быть проверена на короткое замыкание от пин-кодов до пин-кодов.

![[19a00537.png]]

Измерьте напряжение от контакта А 3-контактного разъема Deutsch к блоку двигателя.

Мультиметр **must** показывает 0 VDC.

![[19a00538.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> The RS232 datalink circuit is used by INSITE™ for CENSE™ to communicate with the CENSE™ ECM.
>
> The datalink uses a 3-pin Deutsch connector. The wiring positions follow:
>
> 1. Pin A: - Ground
> 2. Pin C: - Datalink Transmit (Tx)
> 3. Pin B: - Datalink Receive (Rx)
> 4. Key
>
> The procedures that follow cover the cab-located datalink connector and the engine-side datalink connector.
>
> ### Resistance Check
>
> **Engine Located CENSE™**
>
> Disconnect the OEM harness from the CENSE™ 23-pin OEM connector. Remove the engine-located CENSE™ harness ECM A and B connectors from the ECM. Refer to Procedure 019-043.
>
> Use test leads, Part No. 3822758, on the ECM connector and Part No. 3824811, on the 23-pin Deutsch connector. Turn the keyswitch OFF.
>
> Measure the resistance from pin 33 of the CENSE™ harness ECM A connector to pin L of the 23-pin Deutsch connector. The multimeter **must** show a closed circuit (10 ohms or less). If the circuit is **not** closed, repair or replace the CENSE™ harness. Refer to Procedure 019-043.
>
> Measure the resistance from pin 22 of the CENSE™ harness ECM A connector to pin M of the 23-pin Deutsch connector. The multimeter **must** show a closed circuit (10 ohms or less).
>
> If the circuit is **not** closed, repair or replace the CENSE™ harness. Refer to Procedure 019-043.
>
> Measure the resistance from pin 13 of the CENSE™ harness ECM B connector to pin N of the 23-pin Deutsch connector. The multimeter **must** show a closed circuit (10 ohms or less).
>
> If the circuit is **not** closed, repair or replace the engine harness. Refer to Procedure 019-043. If all measurements are within specifications, the OEM harness **must** still be checked. Refer to the OEM manual.
>
> Disconnect the OEM harness from the CENSE™ 23-pin OEM connector. Remove the engine-located CENSE™ harness ECM A and B connectors from the ECM. Refer to Procedure 019-043.
>
> Use test leads, Part No. 3822758, on the ECM connector and, Part No. 3824811, on the 3-pin Deutsch connector. Turn the keyswitch OFF.
>
> Measure the resistance from pin 33 of the CENSE™ harness ECM A connector to pin C of the 3-pin Deutsch connector. The multimeter **must** show a closed circuit (10 ohms or less).
>
> If the circuit is **not** closed, repair or replace the CENSE™ harness. Refer to Procedure 019-043.
>
> Measure the resistance from pin 22 of the CENSE™ harness ECM A connector to pin B of the 3-pin Deutsch connector. The multimeter **must** show a closed circuit (10 ohms or less).
>
> If the circuit is **not** closed, repair or replace the CENSE™ harness. Refer to Procedure 019-043.
>
> Measure the resistance from pin 13 of the CENSE™ harness ECM B connector to pin A of the 3-pin Deutsch connector. The multimeter **must** show a closed circuit (10 ohms or less).
>
> If the circuit is **not** closed, repair or replace the engine harness. Refer to Procedure 019-043.
>
> If all measurements are within specifications, the OEM harness **must** still be checked. Refer to the OEM manual.
>
> ### Check for Short Circuit to Ground
>
> **Cab-Located CENSE™**
>
> Use test lead, Part No. 3824811, for the cab located 23-pin Deutsch connector. Disconnect the 23-pin Deutsch OEM connector. Disconnect the ECM A and B connectors.
>
> Measure the resistance from pin L of the 23-pin Deutsch connector to the engine block ground. The multimeter **must** show an open circuit (100k ohms or more).
>
> If the circuit is **not** open, repair or replace the CENSE™ harness. Refer to Procedure 019-043.
>
> Measure the resistance from pin M of the 23-pin Deutsch connector to the engine block ground. The multimeter **must** show an open circuit (100k ohms or more).
>
> If the circuit is **not** open, repair or replace the CENSE™ harness. Refer to Procedure 019-043.
>
> Measure the resistance from pin N of the 23-pin Deutsch connector to the engine block ground. The multimeter **must** show an open circuit (10 ohms or less).
>
> If the circuit is **not** open, repair or replace the CENSE™ harness. Refer to Procedure 019-043.
>
> **Engine-Located CENSE™**
>
> Use test lead, Part No. 3824811, for the engine-located 3-pin Deutsch connector. Disconnect the ECM A and B connectors.
>
> Measure the resistance from pin A of the 3-pin Deutsch connector to the engine block ground. The multimeter **must** show an open circuit (10 ohms or less).
>
> If the circuit is **not** open, repair or replace the CENSE™ harness. Refer to Procedure 019-043.
>
> Measure the resistance from pin B of the 3-pin Deutsch connector to the engine block ground. The multimeter **must** show an open circuit (100k ohms or more).
>
> If the circuit is **not** open, repair or replace the CENSE™ harness. Refer to Procedure 019-043.
>
> Measure the resistance from pin C of the 3-pin Deutsch connector to the engine block ground. The multimeter **must** show an open circuit (100k ohms or more).
>
> If the circuit is **not** open, repair or replace the CENSE™ harness. Refer to Procedure 019-043.
>
> ### Check for Short Circuit from Pin to Pin
>
> **Engine Harness Connector**
>
> Disconnect the CENSE™ 40-pin A and B Deutsch connectors from the ECM. Disconnect the 31-pin and 23-pin OEM connectors from the OEM harness.
>
> Use test lead, Part No. 3822758, for the CENSE™ ECM 40-pin Deutsch connectors. Measure the resistance from pin 33 of the ECM B connector to all other pins in the ECM B connector. The multimeter **must** show an open circuit (100k ohms or more).
>
> If the circuit is **not** open, repair or replace the CENSE™ harness. Refer to Procedure 019-043.
>
> Now measure the resistance from pin 33 of the ECM B connector to all pins **in the ECM A connector**. The multimeter **must** show an open circuit (100k ohms or more).
>
> If the circuit is **not** open, repair or replace the CENSE™ harness. Refer to Procedure 019-043.
>
> Measure the resistance from pin 22 of the ECM A connector to all other pins in the ECM A connector. The multimeter **must** show an open circuit (100k ohms or more).
>
> If the circuit is **not** open, repair or replace the CENSE™ harness. Refer to Procedure 019-043.
>
> ### Voltage Check
>
> Locate the datalink connector on the CENSE™ harness.
>
> The datalink connector is shown.
>
> **CAUTION · Осторожно**
> To avoid pin and harness damage, use test lead, Part No. 3824811.
>
> Select the VDC function on the multimeter.
>
> Measure the voltage from pin C of the 3-pin Deutsch connector to pin A. The multimeter **must** show -10.0 VDC (minimum -8.5 to maximum -11.0 VDC).
>
> If no voltage is present, the datalink circuit **must** be checked for an open circuit. Verify that the battery voltage is correct.
>
> Measure the voltage from pin B of the 3-pin Deutsch connector to pin A.
>
> The multimeter **must** show 0 VDC. If a voltage is present, the datalink **must** be checked for a short circuit from pin to pin.
>
> Measure the voltage from pin A of the 3-pin Deutsch connector to the engine block.
>
> The multimeter **must** show 0 VDC.
