---
type: "Процедура"
doc: "81-019-125"
title_en: "Data Link Circuit, RS422"
modified: "2003-08-26"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
families:
  - "QSK60"
manuals:
  - "3666410"
figures: 17
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/81/81-019-125.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/81-019-125.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK60"
  - "группа/81"
  - "перевод/машинный"
---

# Data Link Circuit, RS422

> [!abstract] Процедура · `81-019-125`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]]
> **Семейство:** QSK60
> **Входит в руководства:** [[3666410 — QSK45 and QSK60 CENSE™ Electronic Control System Troubleshooting and Repair Manual|3666410]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-08-26
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/81/81-019-125.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/81-019-125.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Схема шины данных RS422 CAN используется системами транспортных средств для связи с CENSETM ECM.

![[cent337.png]]

### Проверка сопротивления

Удалите проводку CENSETM с помощью разъема ECM A из ECM. См. процедуру 019-043. Отсоедините проводку OEM от 23-контактного OEM-разъема CENSETM.

Используйте измерительный щуп, номер детали. 3822758, на разъеме ECM и Части No. 3824811 на 23-контактном разъеме Deutsch. Выключите замок зажигания.

Измерьте сопротивление от контакта 23 разъёма ремня электропроводки двигателя к контакту C 23-контактного разъема Deutsch. Мультиметр **должен** показать замкнутую цепь (10 Ом и менее). Если цепь **не** закрыта, отремонтируйте или замените проводную упряжку CENSETM. См. процедуру 019-043.

![[19400593.png]]

Измерьте сопротивление от контакта 24 разъёма проводов CENSETM к контакту F 23-контактного разъёма Deutsch. Мультиметр **должен** показать замкнутую цепь (10 Ом и менее).

Если цепь **не** закрыта, отремонтируйте или замените проводную упряжку CENSETM. См. процедуру 019-043.

![[19400594.png]]

Измерьте сопротивление от контакта 28 разъёма проводов CENSETM к контакту D 23-контактного разъёма Deutsch. Мультиметр **должен** показать замкнутую цепь (10 Ом и менее).

Если цепь **не** закрыта, отремонтируйте или замените проводную упряжку CENSETM. См. процедуру 019-043.

![[19400595.png]]

Измерьте сопротивление от контакта 29 разъёма проводной ремни CENSETM к контакту E 23-контактного разъёма Deutsch. Мультиметр **должен** показать замкнутую цепь (10 Ом и менее).

Если цепь **не** закрыта, отремонтируйте или замените проводную упряжку CENSETM. См. процедуру 019-043.

Если все измерения соответствуют спецификациям, то необходимо проверить электропроводку OEM. См. руководство по OEM.

![[19400596.png]]

### Проверка на замыкание на массу

Выключите замок зажигания. Отключите 23-контактный OEM-разъем Deutsch. Отключите разъемы ECM A и B.

Используйте тест-щуп Номер детали. 3824811 для 23-контактного разъема Deutsch.

Измерьте сопротивление от контакта C 23-контактного разъема Deutsch к заземлению блока двигателя. Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Если схема **не** открыта, отремонтируйте или замените проводную упряжку CENSETM. См. процедуру 019-043.

![[19400597.png]]

Измерьте сопротивление от контакта D 23-контактного разъема Deutsch к заземлению блока двигателя. Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Если схема **не** открыта, отремонтируйте или замените проводную упряжку CENSETM. См. процедуру 019-043.

![[19400598.png]]

Измерьте сопротивление от контакта E 23-контактного разъема Deutsch к заземлению блока двигателя. Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Если схема **не** открыта, отремонтируйте или замените проводную упряжку CENSETM. См. процедуру 019-043.

![[19400599.png]]

Измерьте сопротивление от контакта F 23-контактного разъема Deutsch к заземлению блока двигателя. Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Если схема **не** открыта, отремонтируйте или замените проводную упряжку CENSETM. См. процедуру 019-043.

![[19400600.png]]

### Проверка на замыкание между контактами

**Deutsche Connector**

Выключите замок зажигания. Отсоедините 23-контактный разъем Deutsch от проводной ремни OEM.

Используйте измерительный щуп, номер детали. 3824811, для 23-контактного разъема Deutsch.

Измерьте сопротивление от контакта C ко всем другим штифтам в разъеме. Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Если схема **не** открыта, отремонтируйте или замените проводную упряжку CENSETM. См. процедуру 019-043.

![[19400601.png]]

Измерьте сопротивление от контакта D ко всем другим штифтам в разъеме. Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Если схема **не** открыта, отремонтируйте или замените проводную упряжку CENSETM. См. процедуру 019-043.

![[19400602.png]]

Измерьте сопротивление от контакта Е до всех других контактов в разъеме. Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Если схема **не** открыта, отремонтируйте или замените проводную упряжку CENSETM. См. процедуру 019-043.

![[19400603.png]]

Измерьте сопротивление от контакта F ко всем другим штифтам в разъеме. Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Если схема **не** открыта, отремонтируйте или замените проводную упряжку CENSETM. См. процедуру 019-043.

Если все измерения соответствуют спецификациям, проводку OEM-производителя необходимо проверить на короткое замыкание от пин-кодов до пин-кодов. См. руководство по OEM.

![[19400604.png]]

### Проверка напряжения

> [!warning] ОСТОРОЖНО
> Чтобы избежать повреждения штифта и проводов, используйте измерительный щуп, номер детали. 3824811.

Отсоедините 23-контактный разъем Deutsch от проводной ремни OEM.

Выберите функцию VDC на мультиметре. Включите замок зажигания.

Измерьте напряжение от контакта D 23-контактного разъема Deutsch к заземлению блока двигателя. Мультиметр **must** показывает от 0 до 3 VDC.

![[19400605.png]]

Измерьте напряжение от контакта F 23-контактного разъема Deutsch к заземлению блока двигателя.

Мультиметр **must** показывает от 0 до 3 VDC.

![[19400606.png]]

Измерьте напряжение от контакта C до контакта D на 23-контактном разъеме Deutsch.

Мультиметр **must** показывает от 0 до 3 VDC.

![[19400607.png]]

Измерьте напряжение от контакта Е до контакта F на 23-контактном разъеме Deutsch.

Мультиметр **must** показывает 2-8 VDC.

Если все измерения соответствуют спецификациям, то необходимо проверить электропроводку OEM. См. руководство по OEM.

![[19400608.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> The RS422 datalink circuit is used by vehicle systems to communicate with the CENSE™ ECM.
>
> ### Resistance Check
>
> Remove the CENSE™ harness ECM A connector from the ECM. Refer to Procedure 019-043. Disconnect the OEM harness from the CENSE™ 23-pin OEM connector.
>
> Use test leads, Part No. 3822758, on the ECM connector and Part No. 3824811 on the 23-pin Deutsch connector. Turn the keyswitch OFF.
>
> Measure the resistance from pin 23 of the engine harness connector to pin C of the 23-pin Deutsch connector. The multimeter **must** show a closed circuit (10 ohms or less). If the circuit is **not** closed, repair or replace the CENSE™ harness. Refer to Procedure 019-043.
>
> Measure the resistance from pin 24 of the CENSE™ harness connector to pin F of the 23-pin Deutsch connector. The multimeter **must** show a closed circuit (10 ohms or less).
>
> If the circuit is **not** closed, repair or replace the CENSE™ harness. Refer to Procedure 019-043.
>
> Measure the resistance from pin 28 of the CENSE™ harness connector to pin D of the 23-pin Deutsch connector. The multimeter **must** show a closed circuit (10 ohms or less).
>
> If the circuit is **not** closed, repair or replace the CENSE™ harness. Refer to Procedure 019-043.
>
> Measure the resistance from pin 29 of the CENSE™ harness connector to pin E of the 23-pin Deutsch connector. The multimeter **must** show a closed circuit (10 ohms or less).
>
> If the circuit is **not** closed, repair or replace the CENSE™ harness. Refer to Procedure 019-043.
>
> If all measurements are within specifications, the OEM harness **must** be checked. Refer to the OEM manual.
>
> ### Check for Short Circuit to Ground
>
> Turn the keyswitch OFF. Disconnect the 23-pin Deutsch OEM connector. Disconnect the ECM A and B connectors.
>
> Use test lead Part No. 3824811 for the 23-pin Deutsch connector.
>
> Measure the resistance from pin C of the 23-pin Deutsch connector to the engine block ground. The multimeter **must** show an open circuit (100k ohms or more).
>
> If the circuit is **not** open, repair or replace the CENSE™ harness. Refer to Procedure 019-043.
>
> Measure the resistance from pin D of the 23-pin Deutsch connector to the engine block ground. The multimeter **must** show an open circuit (100k ohms or more).
>
> If the circuit is **not** open, repair or replace the CENSE™ harness. Refer to Procedure 019-043.
>
> Measure the resistance from pin E of the 23-pin Deutsch connector to the engine block ground. The multimeter **must** show an open circuit (100k ohms or more).
>
> If the circuit is **not** open, repair or replace the CENSE™ harness. Refer to Procedure 019-043.
>
> Measure the resistance from pin F of the 23-pin Deutsch connector to the engine block ground. The multimeter **must** show an open circuit (100k ohms or more).
>
> If the circuit is **not** open, repair or replace the CENSE™ harness. Refer to Procedure 019-043.
>
> ### Check for Short Circuit from Pin to Pin
>
> **Deutsch Connector**
>
> Turn the keyswitch OFF. Disconnect the 23-pin Deutsch connector from the OEM harness.
>
> Use test lead, Part No. 3824811, for the 23-pin Deutsch connector.
>
> Measure the resistance from pin C to all other pins in the connector. The multimeter **must** show an open circuit (100k ohms or more).
>
> If the circuit is **not** open, repair or replace the CENSE™ harness. Refer to Procedure 019-043.
>
> Measure the resistance from pin D to all other pins in the connector. The multimeter **must** show an open circuit (100k ohms or more).
>
> If the circuit is **not** open, repair or replace the CENSE™ harness. Refer to Procedure 019-043.
>
> Measure the resistance from pin E to all other pins in the connector. The multimeter **must** show an open circuit (100k ohms or more).
>
> If the circuit is **not** open, repair or replace the CENSE™ harness. Refer to Procedure 019-043.
>
> Measure the resistance from pin F to all other pins in the connector. The multimeter **must** show an open circuit (100k ohms or more).
>
> If the circuit is **not** open, repair or replace the CENSE™ harness. Refer to Procedure 019-043.
>
> If all measurements are within specifications, the OEM harness **must** be checked for a short circuit from pin to pin. Refer to the OEM manual.
>
> ### Voltage Check
>
> **CAUTION · Осторожно**
> To avoid pin and harness damage, use test lead, Part No. 3824811.
>
> Disconnect the 23-pin Deutsch connector from the OEM harness.
>
> Select the VDC function on the multimeter. Turn the keyswitch ON.
>
> Measure the voltage from pin D of the 23-pin Deutsch connector to the engine block ground. The multimeter **must** show 0 to 3 VDC.
>
> Measure the voltage from pin F of the 23-pin Deutsch connector to the engine block ground.
>
> The multimeter **must** show 0 to 3 VDC.
>
> Measure the voltage from pin C to pin D on the 23-pin Deutsch connector.
>
> The multimeter **must** show 0 to 3 VDC.
>
> Measure the voltage from pin E to pin F on the 23-pin Deutsch connector.
>
> The multimeter **must** show 2 to 8 VDC.
>
> If all measurements are within specifications, the OEM harness **must** be checked. Refer to the OEM manual.
