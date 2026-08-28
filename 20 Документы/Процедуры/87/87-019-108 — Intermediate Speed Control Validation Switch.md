---
aliases:
  - "Выключатель подтверждения промежуточной частоты вращения"
type: "Процедура"
doc: "87-019-108"
title_en: "Intermediate Speed Control Validation Switch"
title_ru: "Выключатель подтверждения промежуточной частоты вращения"
modified: "2018-08-09"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666214"
figures: 7
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-019-108.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-019-108.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
  - "перевод/машинный"
---

# Intermediate Speed Control Validation Switch
**Выключатель подтверждения промежуточной частоты вращения**

> [!abstract] Процедура · `87-019-108`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2018-08-09
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-019-108.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-019-108.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Проверка сопротивления

> [!warning] ОСТОРОЖНО
> Не используйте щупы или испытательные щупы, кроме Части № 3822758, на разъемах ECM и Испытательном щупе, Части № 3823993, на разъеме 31-контактной проводов OEM-интерфейса. Разъемы будут повреждены. Лиды должны плотно помещаться в разъеме без расширения штифтов разъема.

Отсоедините разъем OEM-интерфейса от ECM. Отключите 31-контактный OEM-интерфейс.

Измерьте сопротивление от контакта 46 50-контактного OEM-проводника ремня ремня подсоединения к контакту 23 31-контактного интерфейса проводов ремня подсоединения, стороны двигателя. Мультиметр **должен** показать замкнутую цепь (10 Ом и менее).

Если схема **не** закрыта, отремонтируйте или замените проводку OEM-интерфейса.[[99-019-071 — OEM Wiring Harness|См. процедуру 019-071]].

![[19a00343.png]]

Измерьте сопротивление от контакта 45 50-контактного OEM-проводника с ремнём жгута проводов к контакту 24 31-контактного интерфейса OEM-проводов с жгутом проводов разъема, со стороны двигателя. Мультиметр **должен** показать замкнутую цепь (10 Ом и менее).

Если цепь **не** закрыта, отремонтируйте или замените электропроводку OEM.[[99-019-071 — OEM Wiring Harness|См. процедуру 019-071]].

![[19a00344.png]]

Измерьте сопротивление от контакта 17 50-контактного OEM-коннектора с жгутом проводов к контакту 25 31-контактного интерфейса OEM-коннектора с жгутом проводов, со стороны двигателя. Мультиметр **должен** показать замкнутую цепь (10 Ом и менее).

Если цепь **не** закрыта, отремонтируйте или замените электропроводку OEM.[[99-019-071 — OEM Wiring Harness|См. процедуру 019-071]].

Если проводка OEM на стороне двигателя 31-контактного интерфейсного разъема OEM проходит вышеупомянутые проверки сопротивления, проверьте сопротивление стороны транспортного средства 31-контактного интерфейсного разъема OEM. Смотрите инструкции производителя автомобиля.

![[19a00345.png]]

### Проверка на замыкание на массу

> [!warning] ОСТОРОЖНО
> Не используйте щупы или испытательные щупы, кроме Части № 3822758. Разъём будет повреждён. Лиды должны плотно помещаться в разъеме без расширения штифтов разъема.

Отключите OEM-интерфейс от ECM.

Переместить ISC переключатель в центральное (OFF) положение.

Измерьте сопротивление контактов 46, 45 и 17 разъёма проводов OEM-системы к блоку двигателя. Мультиметр **должен** показывать 100k Ом или более.

Если схема не открыта, проверьте короткое замыкание на землю в электропроводке OEM, при условии, что выключатель был проверен ранее.

![[19a00346.png]]

Отключите 31-контактный OEM-интерфейс, проводящий разъём ремня.

Измерьте сопротивление контактов 46, 45 и 17 разъёма проводов OEM-системы к блоку двигателя. Мультиметр **должен** показывать 100k Ом или более.

Если схема **не** открыта, проверьте наличие коротких замыканий для заземления в стороне транспортного средства 31-контактного разъема OEM-интерфейса. Смотрите инструкции производителя автомобиля.

![[19a00346.png]]

### Проверьте короткое замыкание от контакта к контакту

> [!warning] ОСТОРОЖНО
> Не используйте щупы или испытательные щупы, кроме Части № 3822758. Разъём будет повреждён. Лиды должны плотно помещаться в разъеме без расширения штифтов разъема.

Отсоедините разъём OEM-интерфейса и разъём ремня электропроводки двигателя от ECM.

Измерьте сопротивление контактов 46, 45 и 17 разъёма OEM-проводов жгута проводов ко всем другим штифтам в разъеме. Мультиметр **должен** показывать открытую схему (100к Ом или более) на всех штифтах.

Измерьте сопротивление контактов 46, 45 и 17 разъёма OEM-проводов жгута проводов ко всем штифтам в разъеме ремня электропроводки двигателя. Мультиметр **должен** показывать открытую схему (100к Ом или более) на всех штифтах.

Если схема **не** открыта, проверьте короткое замыкание от пин-кодов до пин-кодов на стороне двигателя 31-контактного интерфейса проводов жгута разъема при условии, что переключатель ранее был проверен.

> [!missing]- Иллюстрация `19a00727.png` не извлечена — смотрите PDF-оригинал документа

Отключите 31-контактный OEM-интерфейс, проводящий разъём ремня.

Измерьте сопротивление контактов 46, 45 и 17 разъёма OEM-проводов жгута проводов ко всем другим штифтам в разъеме. Мультиметр **должен** показывать открытую схему (100к Ом или более) на всех штифтах.

Измерьте сопротивление контактов 46, 45 и 17 разъёма OEM-проводов жгута проводов ко всем штифтам в разъеме ремня электропроводки двигателя. Мультиметр **должен** показывать открытую схему (100к Ом или более) на всех штифтах.

Если схема **не** открыта, проверьте короткое замыкание от пин-кодов до пин-кодов на стороне транспортного средства 31-контактного разъема OEM-интерфейса. Смотрите инструкции производителя автомобиля.

> [!missing]- Иллюстрация `19a00727.png` не извлечена — смотрите PDF-оригинал документа


> [!quote]- Original (English) · английский оригинал
> ### Resistance Check
>
> **CAUTION · Осторожно**
> Do not use probes or test leads other than Part Number 3822758 on the ECM connectors and test lead, Part Number 3823993, on the 31-pin OEM interface harness connector. The connectors will be damaged. The leads must fit tightly in the connector without expanding the pins of the connector.
>
> Disconnect the OEM interface harness connector from the ECM. Disconnect the 31-pin OEM interface connector.
>
> Measure the resistance from pin 46 of the 50-pin OEM harness connector to pin 23 of the 31-pin OEM interface harness connector, engine side. The multimeter **must** show a closed circuit (10 ohms or less).
>
> If the circuit is **not** closed, repair or replace the OEM interface wiring harness. [[99-019-071 — OEM Wiring Harness|Refer to Procedure 019-071]].
>
> Measure the resistance from pin 45 of the 50-pin OEM harness connector to pin 24 of the 31-pin OEM interface harness connector, engine side. The multimeter **must** show a closed circuit (10 ohms or less).
>
> If the circuit is **not** closed, repair or replace the OEM wiring harness. [[99-019-071 — OEM Wiring Harness|Refer to Procedure 019-071]].
>
> Measure the resistance from pin 17 of the 50-pin OEM harness connector to pin 25 of the 31-pin OEM interface harness connector, engine side. The multimeter **must** show a closed circuit (10 ohms or less).
>
> If the circuit is **not** closed, repair or replace the OEM wiring harness. [[99-019-071 — OEM Wiring Harness|Refer to Procedure 019-071]].
>
> If the OEM harness on the engine side of the 31-pin OEM interface connector passes the above resistance checks, check the resistance of the vehicle side of the 31-pin OEM interface connector. Refer to the vehicle manufacturer's instructions.
>
> ### Check for Short Circuit to Ground
>
> **CAUTION · Осторожно**
> Do not use probes or test leads other than Part Number 3822758. The connector will be damaged. The leads must fit tightly in the connector without expanding the pins of the connector.
>
> Disconnect the OEM interface connector from the ECM.
>
> Move the ISC switch to the center (OFF) position.
>
> Measure the resistance from pins 46, 45, and 17 of the OEM harness connector to the engine block. The multimeter **must** show 100k ohms or more.
>
> If the circuit is **not** open, check for short circuit to ground in the OEM wiring harness, provided the switch has been checked previously.
>
> Disconnect the 31-pin OEM interface harness connector.
>
> Measure the resistance from pins 46, 45, and 17 of the OEM harness connector to the engine block. The multimeter **must** show 100k ohms or more.
>
> If the circuit is **not** open, check for short circuits to ground in the vehicle side of the 31-pin OEM interface harness connector. Refer to the vehicle manufacturer's instructions.
>
> ### Check for Short Circuit from Pin-to-Pin
>
> **CAUTION · Осторожно**
> Do not use probes or test leads other than Part Number 3822758. The connector will be damaged. The leads must fit tightly in the connector without expanding the pins of the connector.
>
> Disconnect the OEM interface harness connector and engine harness connector from the ECM.
>
> Measure the resistance from pins 46, 45, and 17 of the OEM harness connector to all other pins in the connector. The multimeter **must** show an open circuit (100k ohms or more) at all pins.
>
> Measure the resistance from pins 46, 45, and 17 of the OEM harness connector to all pins in the engine harness connector. The multimeter **must** show an open circuit (100k ohms or more) at all pins.
>
> If the circuit is **not** open, check for a short circuit from pin to pin on the engine side of the 31-pin OEM interface harness connector, provided the switch has previously been checked.
>
> Disconnect the 31-pin OEM interface harness connector.
>
> Measure the resistance from pins 46, 45, and 17 of the OEM harness connector to all other pins in the connector. The multimeter **must** show an open circuit (100k ohms or more) at all pins.
>
> Measure the resistance from pins 46, 45, and 17 of the OEM harness connector to all pins in the engine harness connector. The multimeter **must** show an open circuit (100k ohms or more) at all pins.
>
> If the circuit is **not** open, check for a short circuit from pin to pin on the vehicle side of the 31-pin OEM interface harness connector. Refer to the vehicle manufacturer's instructions.
