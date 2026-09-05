---
aliases:
  - "Цепь лампы напоминания об обслуживании"
type: "Процедура"
doc: "82-019-168"
title_en: "Maintenance Lamp Circuit"
title_ru: "Цепь лампы напоминания об обслуживании"
modified: "2005-01-28"
engines:
  - "41343322"
  - "41370103"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 4
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-168.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-019-168.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# Maintenance Lamp Circuit
**Цепь лампы напоминания об обслуживании**

> [!abstract] Процедура · `82-019-168`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section 19 - Electronic Engine Controls
> **Даты:** изменён 2005-01-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-168.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-019-168.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Проверка сопротивления

> [!warning] ОСТОРОЖНО
> Чтобы уменьшить вероятность повреждения штифта и проводов, используйте измерительный щуп Номер детали 3822758.

Переключатель зажигания транспортного средства в положение выключения. Отсоедините разъём OEM-проводов от ECM. Отсоедините проводку OEM на главном разъеме приборной панели (панели интерфейса водителя) за разъемом переборки, в кабине автомобиля.

> [!note] Примечание
> В зависимости от OEM и транспортного средства, проводка может быть запущена на отдельные переключатели вместо основного многоконтактного разъема. Проверьте руководство по устранению неполадок и ремонту OEM для процедур.

![[19200217.png]]

Измерить сопротивление от контакта 5 проводов OEM-разъема с задней частью лампы.

Мультиметр **должен** показать замкнутую цепь (10 Ом и менее).

Если цепь **не** закрыта, отремонтируйте или замените электропроводку OEM. См. процедуру 019-071.

![[19200217.png]]

### Проверка на замыкание на массу

> [!warning] ОСТОРОЖНО
> Чтобы уменьшить вероятность повреждения штифта и проводов, используйте измерительный щуп Номер детали 3822758.

Переключатель зажигания транспортного средства в положение выключения. Отсоедините разъём OEM-проводов от ECM. Отсоедините проводку OEM на главном разъеме приборной панели (панель интерфейса водителя), за разъемом переборки, в кабине автомобиля.

> [!note] Примечание
> В зависимости от OEM и транспортного средства, проводка может быть запущена на отдельные переключатели, а не на основной многоконтактный разъем. Проверьте руководство по устранению неполадок и ремонту OEM для процедур.

Измерьте сопротивление от контакта 5 разъёма проводов OEM-проводов к заземлению блока двигателя.

Мультиметр **должен** показать обрыв цепи (100 кОм и более). Если схема **не** открыта, отремонтируйте или замените проводку OEM. См. процедуру 019-071.

![[19c00891.png]]

### Проверка напряжения

Переключатель зажигания транспортного средства в положение Включения.

Настройте мультиметр для измерения напряжения. Прикоснитесь к положительному (+) многометровому щупу к зуммеру или клемме лампы, а отрицательному (-) многометровому щупу к земле шасси.

Измерьте напряжение. Мультиметр **должен** показывать напряжение батареи. Если надлежащее напряжение **не присутствует**, возникает проблема с проводом переключателя зажигания или лампа (или зуммер) вышла из строя. См. руководство по устранению неполадок и ремонту OEM для процедур ремонта.

Повторите эту проверку для другого терминала гудка или лампы неисправности.

![[19200217.png]]


> [!quote]- Original (English) · английский оригинал
> ### Resistance Check
>
> **CAUTION · Осторожно**
> To reduce the possibility of pin and harness damage, use test lead Part Number 3822758.
>
> Turn the vehicle keyswitch to the OFF position. Disconnect the OEM harness connector from the ECM. Disconnect the OEM harness at the main dashboard connector (driver interface panel) beyond the bulkhead connector, in the vehicle cab.
>
> **Note · Примечание**
> Depending on the OEM and the vehicle, the wiring could be run to individual switches instead of a main multi-pin connector. Check the OEM troubleshooting and repair manual for procedures.
>
> Measure the resistance from pin 5 of the OEM harness connector to the back of the lamp.
>
> The multimeter **must** show a closed circuit (10 ohms or less).
>
> If the circuit is **not** closed, repair or replace the OEM harness. Refer to Procedure 019-071.
>
> ### Check for Short Circuit to Ground
>
> **CAUTION · Осторожно**
> To reduce the possibility of pin and harness damage, use test lead Part Number 3822758.
>
> Turn the vehicle keyswitch to the OFF position. Disconnect the OEM harness connector from the ECM. Disconnect the OEM harness at the main dashboard connector (driver interface panel), beyond the bulkhead connector, in the vehicle cab.
>
> **Note · Примечание**
> Depending on the OEM and the vehicle, the wiring could be run to individual switches, instead of a main multi-pin connector. Check the OEM troubleshooting and repair manual for procedures.
>
> Measure the resistance from pin 5 of the OEM harness connector to the engine block ground.
>
> The multimeter **must** show an open circuit (100k ohms or more). If the circuit is **not** open, repair or replace the OEM harness. Refer to Procedure 019-071.
>
> ### Voltage Check
>
> Turn the vehicle keyswitch to the ON position.
>
> Adjust the multimeter to measure voltage. Touch the positive (+) multimeter probe to the buzzer or lamp terminal and the negative (-) multimeter probe to chassis ground.
>
> Measure the voltage. The multimeter **must** show battery voltage. If the proper voltage is **not** present, there is a problem with the keyswitch wire or the lamp (or buzzer) has failed. Refer to the OEM troubleshooting and repair manual for repair procedures.
>
> Repeat this check for the other terminal of the buzzer or fault lamp.
