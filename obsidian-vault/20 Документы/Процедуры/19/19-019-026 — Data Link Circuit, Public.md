---
aliases:
  - "Цепь общедоступной шины данных"
type: "Процедура"
doc: "19-019-026"
title_en: "Data Link Circuit, Public"
title_ru: "Цепь общедоступной шины данных"
modified: "2002-08-20"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
  - "85017333"
families:
  - "QSK23"
  - "QSK60"
manuals:
  - "3666113"
figures: 21
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-019-026.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-019-026.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
  - "перевод/машинный"
---

# Data Link Circuit, Public
**Цепь общедоступной шины данных**

> [!abstract] Процедура · `19-019-026`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2002-08-20
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-019-026.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-019-026.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Схема шины данных CAN используется для связи INSITETM, номер 3824801, с ECM. Публичная шина данных CAN также может использоваться для электронной передачи информации с другими бортовыми электронными устройствами, такими как электронные приборные панели и другое оборудование.

![[19400260.png]]

Шина данных CAN работает и использует 9-контактный разъем шины данных Deutsch CAN. Позиции проводов следующие:

Позиция А - блок-земля

Положение B - батарея (12/24 VDC)

Позиция C - J1939 (+)

Позиция D - J1939 (-)

Позиция E - щит J1939

Положение F - шина данных CAN (+)

Положение G - шина данных CAN (-)

Позиция H - Открытый

Позиция J - Открытый

![[19400743.png]]

### Проверка сопротивления

> [!warning] ОСТОРОЖНО
> Чтобы уменьшить вероятность повреждения разъема, не используйте щупы или провода, отличные от Части № 3822758, на разъеме 40-контактной проводов двигателя и Части № 3824812, на разъеме шины данных 9-контактной CAN. Лиды должны плотно помещаться в разъеме без расширения штифтов в разъеме.

Отсоедините электропроводку двигателя от ECM.

Переведите замок зажигания в положение OFF.

Измерьте сопротивление от контакта 14 разъёма ремня электропроводки двигателя к контакту F 9-контактного разъема шины данных CAN. Мультиметр **должен** показать замкнутую цепь (10 Ом и менее).

Если цепь **не** закрыта, отремонтируйте или замените электропроводку двигателя. См. процедуру 019-240, 019-206 или[[19-019-043 — Engine Wiring Harness|019-043]].

![[19400744.png]]

Измерьте сопротивление от контакта 15 разъёма ремня электропроводки двигателя к контакту G 9-контактного разъема шины данных CAN. Мультиметр **должен** показать замкнутую цепь (10 Ом и менее).

Если цепь **не** закрыта, отремонтируйте или замените электропроводку двигателя. См. процедуру 019-240, 019-206 или[[19-019-043 — Engine Wiring Harness|019-043]].

![[19400745.png]]

Измерьте сопротивление контактов 7 и 8 разъёма ремня электропроводки двигателя для контакта A с 9-контактным разъемом шины данных CAN. Мультиметр **должен** показать замкнутую цепь (10 Ом и менее).

Если цепь **не** закрыта, отремонтируйте или замените электропроводку двигателя. См. процедуру 019-240, 019-206 или[[19-019-043 — Engine Wiring Harness|019-043]].

![[19400746.png]]

Отключите питание от батареи +24-VDC.

Измерьте сопротивление от терминала питания батареи +24-VDC до контакта B 9-контактного разъема шины данных CAN. Мультиметр **должен** показывать замкнутую цепь (10 Ом или меньше)

Если цепь **не** закрыта, отремонтируйте или замените цепь питания OEM +24-VDC. См. указания изготовителя.

Если значения верны, схема **должна **все еще проверяться на наличие коротких замыканий на землю и коротких замыканий от пин-кодов до пин-кодов.

![[19400747.png]]

### Проверка на замыкание на массу

Измерьте сопротивление от контакта F 9-контактного разъема шины данных CAN к блоку двигателя. Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Если схема **не** открыта, отремонтируйте или замените электропроводку двигателя. См. процедуру 019-206 или[[19-019-043 — Engine Wiring Harness|019-043]].

![[19400748.png]]

Измерьте сопротивление от контакта G 9-контактного разъема шины данных CAN к блоку двигателя. Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Если схема **не** открыта, отремонтируйте или замените электропроводку двигателя. См. процедуру 019-206 или[[19-019-043 — Engine Wiring Harness|019-043]].

![[19400749.png]]

Отключите питание от батареи +24-VDC.

Отключите проводку OEM-интерфейса от ECM.

Измерьте сопротивление от контакта B 9-контактного разъема шины данных CAN к блоку двигателя. Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Если схема **не** открыта, отремонтируйте или замените электропроводку двигателя. См. процедуру 019-206 или[[19-019-043 — Engine Wiring Harness|019-043]].

![[19400750.png]]

### Проверка на замыкание между контактами

Измерьте сопротивление от контакта F 9-контактного разъема шины данных CAN ко всем другим разъемам в разъеме. Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Если схема **не** открыта, отремонтируйте или замените электропроводку двигателя. См. процедуру 019-206 или[[19-019-043 — Engine Wiring Harness|019-043]].

![[19400751.png]]

Измерьте сопротивление от контакта G ко всем другим штифтам в разъеме. Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Если схема **не** открыта, отремонтируйте или замените электропроводку двигателя. См. процедуру 019-206 или[[19-019-043 — Engine Wiring Harness|019-043]].

![[19400752.png]]

Измерьте сопротивление от контакта B ко всем другим штифтам в разъеме. Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Если схема **не** открыта, отремонтируйте или замените электропроводку двигателя. См. процедуру 019-206 или[[19-019-043 — Engine Wiring Harness|019-043]].

![[19400753.png]]

Измерьте сопротивление от контакта А до всех других контактов в разъеме. Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Если схема **не** открыта, отремонтируйте или замените электропроводку двигателя. См. процедуру 019-206 или[[19-019-043 — Engine Wiring Harness|019-043]].

![[19400754.png]]

Отсоедините электропроводку двигателя от ECM.

Измерьте сопротивление от контакта 14 разъёма ремня электропроводки двигателя со всеми другими штифтами в разъеме. Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Если схема **не** открыта, отремонтируйте или замените электропроводку двигателя. См. процедуру 019-240 или[[19-019-043 — Engine Wiring Harness|019-043]].

![[19400279.png]]

Измерьте сопротивление от контакта 15 ко всем другим штифтам в разъеме. Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Если схема **не** открыта, отремонтируйте или замените электропроводку двигателя. См. процедуру 019-240 или[[19-019-043 — Engine Wiring Harness|019-043]].

![[19400280.png]]

### Проверка напряжения

Найдите разъем шины данных CAN на ремне проводов OEM. Месторасположение будет зависеть от процедур установки OEM.

Показано устройство CAN Data Bus. Доступна шина данных CAN с публичной и двигательной стороны.

![[19400475.png]]

Переведите замок зажигания в положение ON.

Установите мультиметр для измерения VDC.

Измерьте напряжение от контакта F 9-контактного разъема шины данных CAN к блоку двигателя.

Мультиметр **must** показывает от 4,0 до 5,0 VDC.

![[19400758.png]]

Измерьте напряжение от контакта G 9-контактного разъема шины данных CAN с блоком двигателя.

Мультиметр **must** показывает от 0 до 1,0 VDC.

![[19400759.png]]

Измерьте напряжение от контакта B 9-контактного разъема шины данных CAN к блоку двигателя.

Мультиметр **must** показывает от 18.0 до 27.0 VDC.

![[19400755.png]]

Измерьте напряжение от контакта А 9-контактного разъема шины данных CAN к блоку двигателя.

Мультиметр **must** показывает 0 VDC.

![[19400756.png]]

Если напряжение при контакте F измеряет от 0 до 1,0 VDC, а напряжение при контакте G измеряет от 4,0 до 5,0 VDC, то штифты в 9-контактном разъеме шины данных CAN неправильно установлены и должны быть отменены.

Если напряжение и полярность верны, цепь шины данных CAN должна быть проверена на короткое замыкание на землю и короткое замыкание от пин-кодов до пин-кодов.

Если напряжение отсутствует, цепь шины данных CAN должна быть проверена на открытую цепь. Проверьте, правильно ли работает аккумулятор.

Если напряжение при контакте А составляет 18,0-27,0 ВДК, а напряжение при контакте В - 0 ВДК, то штифты в 9-контактном разъеме шины данных CAN установлены неправильно и должны быть обращены вспять.

![[19400757.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> The public datalink circuit is used for INSITE™, Part Number 3824801, to communicate with the ECM. The public datalink can also be used to electronically communicate information with other on-board electronic devices such as electronic dashboards and other equipment.
>
> The datalink is powered and uses a 9-pin Deutsch datalink connector. The wiring positions are as follows:
>
> Position A - Block Ground
>
> Position B - Battery (12/24 VDC)
>
> Position C - J1939 (+)
>
> Position D - J1939 (-)
>
> Position E - J1939 shield
>
> Position F - Datalink (+)
>
> Position G - Datalink (-)
>
> Position H - Open
>
> Position J - Open
>
> ### Resistance Check
>
> **CAUTION · Осторожно**
> To reduce the possibility of connector damage, do not use probes or leads other than Part Number 3822758, on the 40-pin engine harness connector and Part Number 3824812, on the 9-pin datalink connector. The leads must fit tightly in the connector without expanding the pins in the connector.
>
> Disconnect the engine harness from the ECM.
>
> Turn the keyswitch to the OFF position.
>
> Measure the resistance from pin 14 of the engine harness connector to pin F of the 9-pin datalink connector. The multimeter **must** show a closed circuit (10 ohms or less).
>
> If the circuit is **not** closed, repair or replace the engine harness. Refer to Procedure 019-240, 019-206, or [[19-019-043 — Engine Wiring Harness|019-043]].
>
> Measure the resistance from pin 15 of the engine harness connector to pin G of the 9-pin datalink connector. The multimeter **must** show a closed circuit (10 ohms or less).
>
> If the circuit is **not** closed, repair or replace the engine harness. Refer to Procedure 019-240, 019-206, or [[19-019-043 — Engine Wiring Harness|019-043]].
>
> Measure the resistance from pins 7 and 8 of the engine harness connector to pin A of the 9-pin datalink connector. The multimeter **must** show a closed circuit (10 ohms or less).
>
> If the circuit is **not** closed, repair or replace the engine harness. Refer to Procedure 019-240, 019-206, or [[19-019-043 — Engine Wiring Harness|019-043]].
>
> Disconnect the +24-VDC battery supply from the battery.
>
> Measure the resistance from the +24-VDC battery supply terminal to pin B of the 9-pin datalink connector. The multimeter **must** show a closed circuit (10 ohms or less)
>
> If the circuit is **not** closed, repair or replace the OEM +24-VDC supply circuit. Refer to the manufacturer's instructions.
>
> If the values are correct, the circuit **must** still be checked for short circuits to ground and short circuits from pin to pin.
>
> ### Check for Short Circuit to Ground
>
> Measure the resistance from pin F of the 9-pin datalink connector to the engine block. The multimeter **must** show an open circuit (100k ohms or more).
>
> If the circuit is **not** open, repair or replace the engine harness. Refer to Procedure 019-206 or [[19-019-043 — Engine Wiring Harness|019-043]].
>
> Measure the resistance from pin G of the 9-pin datalink connector to the engine block. The multimeter **must** show an open circuit (100k ohms or more).
>
> If the circuit is **not** open, repair or replace the engine harness. Refer to Procedure 019-206 or [[19-019-043 — Engine Wiring Harness|019-043]].
>
> Disconnect the +24-VDC battery supply from the battery.
>
> Disconnect the OEM interface harness from the ECM.
>
> Measure the resistance from pin B of the 9-pin datalink connector to the engine block. The multimeter **must** show an open circuit (100k ohms or more).
>
> If the circuit is **not** open, repair or replace the engine harness. Refer to Procedure 019-206 or [[19-019-043 — Engine Wiring Harness|019-043]].
>
> ### Check for Short Circuit from Pin to Pin
>
> Measure the resistance from pin F of the 9-pin datalink connector to all other pins in the connector. The multimeter **must** show an open circuit (100k ohms or more).
>
> If the circuit is **not** open, repair or replace the engine harness. Refer to Procedure 019-206 or [[19-019-043 — Engine Wiring Harness|019-043]].
>
> Measure the resistance from pin G to all other pins in the connector. The multimeter **must** show an open circuit (100k ohms or more).
>
> If the circuit is **not** open, repair or replace the engine harness. Refer to Procedure 019-206 or [[19-019-043 — Engine Wiring Harness|019-043]].
>
> Measure the resistance from pin B to all other pins in the connector. The multimeter **must** show an open circuit (100k ohms or more).
>
> If the circuit is **not** open, repair or replace the engine harness. Refer to Procedure 019-206 or [[19-019-043 — Engine Wiring Harness|019-043]].
>
> Measure the resistance from pin A to all other pins in the connector. The multimeter **must** show an open circuit (100k ohms or more).
>
> If the circuit is **not** open, repair or replace the engine harness. Refer to Procedure 019-206 or [[19-019-043 — Engine Wiring Harness|019-043]].
>
> Disconnect the engine harness from the ECM.
>
> Measure the resistance from pin 14 of the engine harness connector to all other pins in the connector. The multimeter **must** show an open circuit (100k ohms or more).
>
> If the circuit is **not** open, repair or replace the engine harness. Refer to Procedure 019-240 or [[19-019-043 — Engine Wiring Harness|019-043]].
>
> Measure the resistance from pin 15 to all other pins in the connector. The multimeter **must** show an open circuit (100k ohms or more).
>
> If the circuit is **not** open, repair or replace the engine harness. Refer to Procedure 019-240 or [[19-019-043 — Engine Wiring Harness|019-043]].
>
> ### Voltage Check
>
> Locate the datalink connector on the OEM harness. The location will depend on the OEM installation procedures.
>
> The datalink circuit is shown. A public and engine side datalink are available.
>
> Turn the keyswitch to the ON position.
>
> Set the multimeter to measure VDC.
>
> Measure the voltage from pin F of the 9-pin datalink connector to the engine block.
>
> The multimeter **must** show 4.0 to 5.0 VDC.
>
> Measure the voltage from pin G of the 9-pin datalink connector to the engine block.
>
> The multimeter **must** show 0 to 1.0 VDC.
>
> Measure the voltage from pin B of the 9-pin datalink connector to the engine block.
>
> The multimeter **must** show 18.0 to 27.0 VDC.
>
> Measure the voltage from pin A of the 9-pin datalink connector to the engine block.
>
> The multimeter **must** show 0 VDC.
>
> If the voltage at pin F measures 0 to 1.0 VDC and the voltage at pin G measures 4.0 to 5.0 VDC, then the pins in the 9-pin datalink connector are improperly installed and **must** be reversed.
>
> If the voltage and polarity are correct, the datalink circuit **must** be checked for a short circuit to ground and a short circuit from pin to pin.
>
> If no voltage is present, the datalink circuit **must** be checked for an open circuit. Verify the battery voltage is correct.
>
> If the voltage at pin A is 18.0 to 27.0 VDC and the voltage at pin B is 0 VDC, then the pins in the 9-pin datalink connector are improperly installed and **must** be reversed.
