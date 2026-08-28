---
aliases:
  - "Лампа напоминания об обслуживании"
type: "Процедура"
doc: "82-019-167"
title_en: "Maintenance Lamp"
title_ru: "Лампа напоминания об обслуживании"
modified: "2002-06-03"
engines:
  - "41343322"
  - "41370103"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 5
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-167.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-019-167.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# Maintenance Lamp
**Лампа напоминания об обслуживании**

> [!abstract] Процедура · `82-019-167`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section 19 - Electronic Engine Controls
> **Даты:** изменён 2002-06-03
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-167.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-019-167.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Система защиты двигателя использует лампу или гудильщик для оповещения водителя об одном из следующих условий:

1. Низкий уровень охлаждающей жидкости
2. Высокая температура охлаждающей жидкости
3. Низкое давление масла
4. Высокое давление масла
5. Высокая температура коллектора впуска
6. Очень низкое давление масла.

![[19200217.png]]

Схема лампы технического обслуживания представляет собой положительную (+) 12-VDC (24 VDC в Великобритании или Европе) поставку от переключателя зажигания транспортного средства, лампы или зуммера и провода No. 5.

ECM обеспечивает дорожку для заземления цепи для освещения лампы.

![[19200217.png]]

### Проверка напряжения

Переключатель зажигания транспортного средства в положение Включения.

Прикоснитесь к положительному (+) многометровому щупу к зуммеру или к оконечному устройству лампы. Прикоснитесь к отрицательному (-) многометровому щупу к земле шасси.

Измерьте напряжение. Мультиметр **должен** показывать напряжение батареи. Если надлежащее напряжение **не присутствует**, возникает проблема с проводом переключателя зажигания или лампа (или зуммер) вышла из строя. См. руководство по устранению неполадок и ремонту OEM для процедур ремонта.

![[ee8cos29.png]]

Повторите эту проверку для другого терминала гудка или лампы неисправности. Мультиметр **должен** показывать напряжение батареи.

Если напряжение батареи **не присутствует**, возникает проблема с линией переключателя зажигания или лампа вышла из строя. См. руководство по устранению неполадок и ремонту OEM для процедур.

> [!note] Примечание
> Напряжение батареи будет варьироваться между автомобилями, в зависимости от возраста и состояния батарей. должно быть достаточно напряжения, чтобы освещать лампу.

> [!missing]- Иллюстрация `19900543.png` не извлечена — смотрите PDF-оригинал документа

Прикоснитесь к положительному (+) многометровому датчику к другому оконечному устройству неисправной лампы.

Прикоснитесь к отрицательному (-) многометровому щупу на земле шасси.

Измерьте напряжение. Мультиметр **должен** показывать напряжение батареи. Если надлежащее напряжение **не присутствует**, возникает проблема с проводом переключателя зажигания или лампа (или зуммер) вышла из строя. См. руководство по устранению неполадок и ремонту OEM для процедур ремонта.

Повторите эту проверку для другого терминала неисправной лампы. Мультиметр **должен** показывать напряжение батареи. Если напряжение батареи **не присутствует**, возникает проблема с линией переключателя зажигания или лампа вышла из строя. См. руководство по устранению неполадок и ремонту OEM для процедур.

Повторите это испытание для другого терминала гудка или лампы неисправности.

Подключите все компоненты после завершения ремонта.

> [!missing]- Иллюстрация `19900543.png` не извлечена — смотрите PDF-оригинал документа


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> The engine protection system uses a lamp or a buzzer to alert the driver of one of the following conditions:
>
> 1. Low coolant level
> 2. High coolant temperature
> 3. Low oil pressure
> 4. High oil pressure
> 5. High intake manifold temperature
> 6. Very low oil pressure.
>
> The maintenance lamp circuit is a positive (+) 12-VDC (24 VDC in the United Kingdom or Europe) supply from the vehicle keyswitch, a lamp or buzzer, and wire No. 5.
>
> The ECM provides a ground path for the circuit to illuminate the lamp.
>
> ### Voltage Check
>
> Turn the vehicle keyswitch to the ON position.
>
> Touch the positive (+) multimeter probe to the buzzer or lamp terminal. Touch the negative (-) multimeter probe to the chassis ground.
>
> Measure the voltage. The multimeter **must** show battery voltage. If the proper voltage is **not** present, there is a problem with the keyswitch wire or the lamp (or buzzer) has failed. Refer to the OEM troubleshooting and repair manual for repair procedures.
>
> Repeat this check for the other terminal of the buzzer or fault lamp. The multimeter **must** show the battery voltage.
>
> If battery voltage is **not** present, there is a problem with the keyswitch line or the lamp has failed. Refer to the OEM troubleshooting and repair manual for procedures.
>
> **Note · Примечание**
> The battery voltage will vary between vehicles, depending on the age and the condition of the batteries. There **must** be enough voltage available to illuminate the lamp.
>
> Touch the positive (+) multimeter probe to the other fault lamp terminal.
>
> Touch the negative (-) multimeter probe to chassis ground.
>
> Measure the voltage. The multimeter **must** show battery voltage. If the proper voltage is **not** present, there is a problem with the keyswitch wire or the lamp (or buzzer) has failed. Refer to the OEM troubleshooting and repair manual for repair procedures.
>
> Repeat this check for the other terminal of the fault lamp. The multimeter **must** show battery voltage. If battery voltage is **not** present, there is a problem with the keyswitch line or the lamp has failed. Refer to the OEM troubleshooting and repair manual for procedures.
>
> Repeat this test for the other terminal of the buzzer or fault lamp.
>
> Connect all components after the repair is complete.
