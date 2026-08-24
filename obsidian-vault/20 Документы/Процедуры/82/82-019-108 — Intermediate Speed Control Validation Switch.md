---
aliases:
  - "Выключатель подтверждения промежуточной частоты вращения"
type: "Процедура"
doc: "82-019-108"
title_en: "Intermediate Speed Control Validation Switch"
title_ru: "Выключатель подтверждения промежуточной частоты вращения"
modified: "2005-01-28"
engines:
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 7
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-108.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-019-108.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# Intermediate Speed Control Validation Switch
**Выключатель подтверждения промежуточной частоты вращения**

> [!abstract] Процедура · `82-019-108`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section 19 - Electronic Engine Controls
> **Даты:** изменён 2005-01-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-108.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-019-108.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Проверка сопротивления

Отсоедините разъём OEM-проводов от ECM.

Используйте пробный щуп, номер детали 3822758, на разъемах ECM.

Отсоедините переборочный разъем.

Измерьте сопротивление от контакта 23 разъёма проводов OEM-проводов к соответствующему штифту разъёма переборки (см. Руководство по устранению неполадок и ремонту OEM-производителя). Мультиметр **должен** показать замкнутую цепь (10 Ом и менее).

Если цепь ** не** закрыта, отремонтируйте или замените проводку. См. процедуру 019-043.

![[19c00908.png]]

Измерьте сопротивление от контакта 25 разъёма проводов OEM-упряжи к соответствующему штифту разъёма переборки (см. Руководство по устранению неполадок и ремонту OEM-установки). Мультиметр **должен** показать замкнутую цепь (10 Ом и менее).

Если цепь ** не** закрыта, отремонтируйте или замените проводку. См. процедуру 019-043.

![[19c00909.png]]

Измерьте сопротивление от контакта 33 разъёма проводов OEM-системы к соответствующему штифту разъёма переборки (см. Руководство по устранению неполадок и ремонту OEM-производителя). Мультиметр **должен** показать замкнутую цепь (10 Ом и менее).

Если цепь ** не** закрыта, отремонтируйте или замените проводку. См. процедуру 019-043.

Если проводная упряжка OEM на стороне двигателя переборки разъема проходит вышеупомянутые проверки сопротивления, проверьте сопротивление стороны транспортного средства переборки разъема. Смотрите инструкции производителя автомобиля.

![[19c00910.png]]

### Проверка на замыкание на массу

Отсоедините разъём OEM-проводов от ECM.

Используйте измерительный щуп, номер детали 3822758.

Переместить ISC переключатель в центральное (OFF) положение.

Измерьте сопротивление от контактов 23, 25 и 33 к блоку двигателя. Мультиметр ** должен ** показывать 100k Ом или более.

Если схема ** не открыта, проверьте короткое замыкание на землю в электропроводке OEM, при условии, что выключатель был проверен ранее.

![[19c00911.png]]

Отсоедините разъём переборки проводов.

Измерьте сопротивление контактов 23, 25 и 33 разъема ECM блоку двигателя. Мультиметр ** должен ** показывать 100k Ом или более.

Если схема ** не** открыта, проверьте короткое замыкание на землю в стороне транспортного средства от переборки разъема. Смотрите инструкции производителя автомобиля.

![[19c00911.png]]

### Проверка на замыкание между контактами

Отсоедините разъём OEM-проводов от ECM.

Используйте пробный щуп, номер детали 3822758 на разъеме ECM.

Измерьте сопротивление от контакта 23 разъёма OEM-проводов с другими штифтами в разъеме. Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Измерьте сопротивление от контакта 33 разъёма OEM-проводов с другими штифтами в разъеме. Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Измерьте сопротивление от контакта 25 разъёма OEM-проводов с другими штифтами в разъеме. Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Если схема ** не** открыта, проверьте короткое замыкание от штифта до штифта на стороне двигателя переборки разъема, при условии, что переключатель был проверен ранее.

![[19c00912.png]]

Отсоедините переборочный разъем.

Измерьте сопротивление от контакта 23 разъёма OEM-проводов с другими штифтами в разъеме. Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Измерьте сопротивление от контакта 33 разъёма OEM-проводов с другими штифтами в разъеме. Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Измерьте сопротивление от контакта 25 разъёма OEM-проводов с другими штифтами в разъеме. Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Если схема **не** открыта, проверьте короткое замыкание от штифта до штифта на стороне транспортного средства переборки разъема. Смотрите инструкции производителя автомобиля.

После ремонта подсоедините все компоненты.

![[19c00912.png]]


> [!quote]- Original (English) · английский оригинал
> ### Resistance Check
>
> Disconnect the OEM harness connector from the ECM.
>
> Use test lead, Part Number 3822758, on the ECM connectors.
>
> Disconnect the bulkhead connector.
>
> Measure the resistance from pin 23 of the OEM harness connector to the corresponding pin of the bulkhead connector (refer to the OEM troubleshooting and repair manual). The multimeter **must** show a closed circuit (10 ohms or less).
>
> If the circuit is **not** closed, repair or replace the wiring harness. Refer to Procedure 019-043.
>
> Measure the resistance from pin 25 of the OEM harness connector to the corresponding pin of the bulkhead connector (refer to the OEM troubleshooting and repair manual). The multimeter **must** show a closed circuit (10 ohms or less).
>
> If the circuit is **not** closed, repair or replace the wiring harness. Refer to Procedure 019-043.
>
> Measure the resistance from pin 33 of the OEM harness connector to the corresponding pin of the bulkhead connector (refer to the OEM troubleshooting and repair manual). The multimeter **must** show a closed circuit (10 ohms or less).
>
> If the circuit is **not** closed, repair or replace the wiring harness. Refer to Procedure 019-043.
>
> If the OEM harness on the engine side of the bulkhead connector passes the above resistance checks, check the resistance of the vehicle side of the bulkhead connector. See the vehicle manufacturer's instructions.
>
> ### Check for Short Circuit to Ground
>
> Disconnect the OEM harness connector from the ECM.
>
> Use test lead, Part Number 3822758.
>
> Move the ISC switch to the center (OFF) position.
>
> Measure the resistance from pins 23, 25, and 33 to the engine block. The multimeter **must** show 100k ohms or more.
>
> If the circuit is **not** open, check for short circuit to ground in the OEM wiring harness, provided the switch has been checked previously.
>
> Disconnect the bulkhead harness connector.
>
> Measure the resistance from the ECM connector pins 23, 25, and 33 to the engine block. The multimeter **must** show 100k ohms or more.
>
> If the circuit is **not** open, check for short circuit to ground in the vehicle side of the bulkhead connector. See the vehicle manufacturer's instructions.
>
> ### Check for Short Circuit from Pin to Pin
>
> Disconnect the OEM harness connector from the ECM.
>
> Use test lead, Part Number 3822758 on the ECM connector.
>
> Measure the resistance from pin 23 of the OEM harness connector to all other pins in the connector. The multimeter **must** show an open circuit (100k ohms or more).
>
> Measure the resistance from pin 33 of the OEM harness connector to all other pins in the connector. The multimeter **must** show an open circuit (100k ohms or more).
>
> Measure the resistance from pin 25 of the OEM harness connector to all other pins in the connector. The multimeter **must** show an open circuit (100k ohms or more).
>
> If the circuit is **not** open, check for a short circuit from pin to pin on the engine side of the bulkhead connector, provided the switch has been checked earlier.
>
> Disconnect the bulkhead connector.
>
> Measure the resistance from pin 23 of the OEM harness connector to all other pins in the connector. The multimeter **must** show an open circuit (100k ohms or more).
>
> Measure the resistance from pin 33 of the OEM harness connector to all other pins in the connector. The multimeter **must** show an open circuit (100k ohms or more).
>
> Measure the resistance from pin 25 of the OEM harness connector to all other pins in the connector. The multimeter **must** show an open circuit (100k ohms or more).
>
> If the circuit is **not** open, check for a short circuit from pin to pin on the vehicle side of the bulkhead connector. See the vehicle manufacturer's instructions.
>
> Connect all components after completing the repair.
