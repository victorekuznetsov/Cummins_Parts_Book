---
aliases:
  - "Цепь датчика частоты вращения двигателя"
type: "Процедура"
doc: "01-019-106"
title_en: "Engine Speed Sensor Circuit"
title_ru: "Цепь датчика частоты вращения двигателя"
modified: "2003-12-04"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 24
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-019-106.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-019-106.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Engine Speed Sensor Circuit
**Цепь датчика частоты вращения двигателя**

> [!abstract] Процедура · `01-019-106`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-12-04
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-019-106.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-019-106.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Проверка сопротивления

> [!warning] ОСТОРОЖНО
> Не используйте щупы или провода, кроме Части № 3822758 или 3822917. Лиды должны плотно помещаться в разъеме без расширения штифтов разъема.

Отсоедините проводку двигателя от встроенного разъема.

Убедитесь, что датчик скорости двигателя подключен к электропроводке.

![[19802556.png]]

Измерьте сопротивление между датчиком 1 скорости двигателя и обратным контактом на встраиваемом разъёме проводов двигателя. Значение сопротивления должно быть от 750 до 1100 Ом.

Измерьте сопротивление между датчиком 2 скорости двигателя и обратным контактом на встраиваемом разъёме жгута проводов двигателя. Значение сопротивления должно быть от 1100 до 1500 Ом.

Если любое из показаний не соответствует спецификациям, при условии, что датчик скорости двигателя был проверен, замените электропроводку двигателя. См. процедуру[[01-019-043 — Engine Wiring Harness|019-043]].

![[19802557.png]]

> [!warning] ОСТОРОЖНО
> Не используйте щупы или провода, отличные от Части № 3822758. Лиды должны плотно помещаться в разъеме без расширения штифтов разъема.

Подключите проводку двигателя ремня встраиваемого разъема.

Отсоедините удлинитель проводов от ECM.

Убедитесь, что датчик скорости двигателя подключен к электропроводке.

![[19802479.png]]

Измерьте сопротивление между сигналом датчика 1 оборота двигателя и обратным контактом на разъеме удлинительной проводов жгута проводов. Измерьте сопротивление между сигналом датчика 2 оборота двигателя и обратным контактом на разъеме удлинительной проводов жгута проводов. Значения сопротивления **должны** составлять от 1000 до 2000 Ом.

Если любой из показаний не соответствует спецификациям, при условии, что датчик скорости двигателя был проверен, замените удлинитель проводов. См. процедуру[[01-019-175 — Extension Wiring Harness|019-175]].

![[19802558.png]]

### Проверка на замыкание на массу

> [!warning] ОСТОРОЖНО
> Не используйте щупы или провода, кроме Части № 3822758 или 3822917. Лиды должны плотно помещаться в разъеме без расширения штифтов разъема.

Отсоедините проводку двигателя от встроенного разъема.

![[19802556.png]]

Включить испытательный щуп в датчик 1 скорости двигателя сигнального контакта на проводах двигателя ремня встраиваемого разъема. Прикоснитесь к другому многометровому щупу блока двигателя. Измерьте сопротивление. Мультиметр **должен** показывать открытую схему (более 10 м ом).

Включить испытательный щуп в датчик 1 оборота двигателя обратного контакта на проводах двигателя ремня встраиваемого разъема. Прикоснитесь к другому многометровому щупу блока двигателя. Измерьте сопротивление. Мультиметр **должен** показывать открытую схему (более 10 м ом).

![[19802559.png]]

Включить испытательный щуп в датчик 2 скорости двигателя сигнального контакта на проводах двигателя ремня встраиваемого разъема. Прикоснитесь к другому многометровому щупу блока двигателя. Измерьте сопротивление. Мультиметр **должен** показывать открытую схему (более 10 м ом).

Включить испытательный щуп в датчик 2 оборотов двигателя обратного контакта на проводах двигателя ремня встраиваемого разъема. Прикоснитесь к другому многометровому щупу блока двигателя. Измерьте сопротивление. Мультиметр **должен** показывать открытую схему (более 10 м ом).

![[19802559.png]]

Если значения сопротивления в любой из предыдущих проверок **не** в пределах спецификации, есть короткое замыкание на землю, при условии, что датчик скорости двигателя был ранее проверен. Замените жгут проводов двигателя. См. процедуру[[01-019-043 — Engine Wiring Harness|019-043]].

![[19802559.png]]

> [!warning] ОСТОРОЖНО
> Не используйте щупы или провода, отличные от Части № 3822758. Лиды должны плотно помещаться в разъеме без расширения штифтов разъема.

Подключите проводку двигателя ремня встраиваемого разъема.

Отсоедините удлинитель проводов от ECM.

![[19802479.png]]

Включить испытательный щуп в датчик 1 скорости двигателя сигнального контакта на разъеме удлинительной проводов жгута проводов. Прикоснитесь к другому многометровому щупу блока двигателя. Измерьте сопротивление. Мультиметр **должен** показывать открытую схему (более 10 м ом).

Включить испытательный щуп в датчик 1 оборота двигателя обратного контакта на разъеме удлинительной проводов жгута проводов. Прикоснитесь к другому многометровому щупу блока двигателя. Измерьте сопротивление. Мультиметр **должен** показывать открытую схему (более 10 м ом).

![[19802560.png]]

Включить испытательный щуп в датчик 2 скорости двигателя сигнального контакта на разъеме удлинительной проводов жгута проводов. Прикоснитесь к другому многометровому щупу блока двигателя. Измерьте сопротивление. Мультиметр **должен** показывать открытую схему (более 10 м ом).

Включить испытательный щуп в датчик 2 оборотов двигателя обратного контакта на разъеме удлинительной проводов жгута проводов. Прикоснитесь к другому многометровому щупу блока двигателя. Измерьте сопротивление. Мультиметр **должен** показывать открытую схему (более 10 м ом).

![[19802560.png]]

Если значения сопротивления в любой из предыдущих проверок на разъеме удлинительной проводов жгута проводов **не** в пределах спецификации, есть короткое замыкание на землю, при условии, что датчик скорости двигателя был ранее проверен. Замените удлинитель проводов. См. процедуру[[01-019-175 — Extension Wiring Harness|019-175]].

![[19802560.png]]

### Проверка на замыкание между контактами

> [!warning] ОСТОРОЖНО
> Не используйте щупы или провода, кроме Части № 3822758 или 3822917. Лиды должны плотно помещаться в разъеме без расширения штифтов разъема.

Отсоедините проводку двигателя от встроенного разъема.

Отсоедините датчик скорости двигателя от электропроводки двигателя.

![[19802556.png]]

Включить испытательный щуп в датчик 1 скорости двигателя сигнального контакта на проводах двигателя ремня встраиваемого разъема. Вставьте другой измерительный щуп во все другие штифты на встроенном разъёме проводов двигателя, по одному за раз. Измерьте сопротивление для каждого штифта. Мультиметр **должен** показывать открытую схему (более 10 м ом) для всех контактов в разъеме.

![[19802557.png]]

Включить испытательный щуп в датчик 1 оборота двигателя обратного контакта на проводах двигателя ремня встраиваемого разъема. Вставьте другой измерительный щуп во все другие штифты на встроенном разъёме проводов двигателя, по одному за раз. Измерьте сопротивление для каждого штифта. Мультиметр **должен** показывать открытую схему (более 10 м ом) для всех контактов в разъеме.

![[19802557.png]]

Включить испытательный щуп в датчик 2 скорости двигателя сигнального контакта на проводах двигателя ремня встраиваемого разъема. Вставьте другой измерительный щуп во все другие штифты на встроенном разъёме проводов двигателя, по одному за раз. Измерьте сопротивление для каждого штифта. Мультиметр **должен** показывать открытую схему (более 10 м ом) для всех контактов в разъеме.

![[19802557.png]]

Включить испытательный щуп в датчик 2 оборотов двигателя обратного контакта на проводах двигателя ремня встраиваемого разъема. Вставьте другой измерительный щуп во все другие штифты на встроенном разъёме проводов двигателя, по одному за раз. Измерьте сопротивление для каждого штифта. Мультиметр **должен** показывать открытую схему (более 10 м ом) для всех контактов в разъеме.

![[19802557.png]]

Если значения сопротивления в любой из предыдущих проверок **не*** в пределах спецификации, то происходит короткое замыкание от одного из проводов датчика скорости двигателя до любого штифта, который измеряет менее 10 м Ом. Ремонт или замена ремня электропроводки двигателя. См. процедуры[[01-019-043 — Engine Wiring Harness|019-043]]и[[99-019-208 — Deutsch HDP20 and HD30 Connector Series|019-208]].

![[19802557.png]]

> [!warning] ОСТОРОЖНО
> Не используйте щупы или провода, отличные от Части № 3822758. Лиды должны плотно помещаться в разъеме без расширения штифтов разъема.

Отсоедините удлинитель проводов от ECM.

![[19802555.png]]

Включить испытательный щуп в датчик 1 скорости двигателя сигнального контакта на разъеме удлинительной проводов жгута проводов. Вставьте другой измерительный щуп во все другие штифты на разъеме удлинительной проводов, по одному за раз. Измерьте сопротивление для каждого штифта. Мультиметр **должен** показывать открытую схему (более 10 м ом) для всех контактов в разъеме.

![[19802558.png]]

Включить испытательный щуп в датчик 1 оборота двигателя обратного контакта на разъеме удлинительной проводов жгута проводов. Вставьте другой измерительный щуп во все другие штифты на разъеме удлинительной проводов, по одному за раз. Измерьте сопротивление для каждого штифта. Мультиметр **должен** показывать открытую схему (более 10 м ом) для всех контактов в разъеме.

![[19802558.png]]

Включить испытательный щуп в датчик 2 скорости двигателя сигнального контакта на разъеме удлинительной проводов жгута проводов. Вставьте другой измерительный щуп во все другие штифты на разъеме удлинительной проводов, по одному за раз. Измерьте сопротивление для каждого штифта. Мультиметр **должен** показывать открытую схему (более 10 м ом) для всех контактов в разъеме.

![[19802558.png]]

Включить испытательный щуп в датчик 2 оборотов двигателя обратного контакта на разъеме удлинительной проводов жгута проводов. Вставьте другой измерительный щуп во все другие штифты на разъеме удлинительной проводов, по одному за раз. Измерьте сопротивление для каждого штифта. Мультиметр **должен** показывать открытую схему (более 10 м ом) для всех контактов в разъеме.

![[19802558.png]]

Если значения сопротивления в любой из предыдущих проверок на разъеме удлинительной проводов жгута проводов **не** в пределах спецификации, существует короткое замыкание от одного из проводов датчика скорости двигателя до любого штифта, который измеряет менее 10 м Ом. Ремонт или замена удлинителя проводов жгута. См. процедуры[[01-019-175 — Extension Wiring Harness|019-175]]и[[99-019-213 — D-Sub Miniature Connector Series|019-213]].

![[19802558.png]]


> [!quote]- Original (English) · английский оригинал
> ### Resistance Check
>
> **CAUTION · Осторожно**
> Do not use probes or leads other than Part Number 3822758 or 3822917. The leads must fit tightly in the connector without expanding the pins of the connector.
>
> Disconnect the engine harness inline connector.
>
> Make sure the engine speed sensor is connected to the harness.
>
> Measure the resistance between the engine speed sensor 1 signal and return pin at the engine harness inline connector. The resistance value **must** be 750 to 1100 ohms.
>
> Measure the resistance between the engine speed sensor 2 signal and return pin at the engine harness inline connector. The resistance value **must** be 1100 to 1500 ohms.
>
> If either of the readings are outside the specifications, provided the engine speed sensor has been checked, replace the engine harness. Refer to Procedure [[01-019-043 — Engine Wiring Harness|019-043]].
>
> **CAUTION · Осторожно**
> Do not use probes or leads other than Part Number 3822758. The leads must fit tightly in the connector without expanding the pins of the connector.
>
> Connect the engine harness inline connector.
>
> Disconnect the extension harness from the ECM.
>
> Make sure the engine speed sensor is connected to the harness.
>
> Measure the resistance between the engine speed sensor 1 signal and return pin at the extension harness connector. Measure the resistance between the engine speed sensor 2 signal and return pin at the extension harness connector. The resistance values **must** be 1000 to 2000 ohms.
>
> If either of the readings are outside the specifications, provided the engine speed sensor has been checked, replace the extension harness. Refer to Procedure [[01-019-175 — Extension Wiring Harness|019-175]].
>
> ### Check for Short Circuit to Ground
>
> **CAUTION · Осторожно**
> Do not use probes or leads other than Part Number 3822758 or 3822917. The leads must fit tightly in the connector without expanding the pins of the connector.
>
> Disconnect the engine harness inline connector.
>
> Insert the test lead into the engine speed sensor 1 signal pin at the engine harness inline connector. Touch the other multimeter probe to the engine block. Measure the resistance. The multimeter **must** show an open circuit (more than 10M ohms).
>
> Insert the test lead into the engine speed sensor 1 return pin at the engine harness inline connector. Touch the other multimeter probe to the engine block. Measure the resistance. The multimeter **must** show an open circuit (more than 10M ohms).
>
> Insert the test lead into the engine speed sensor 2 signal pin at the engine harness inline connector. Touch the other multimeter probe to the engine block. Measure the resistance. The multimeter **must** show an open circuit (more than 10M ohms).
>
> Insert the test lead into the engine speed sensor 2 return pin at the engine harness inline connector. Touch the other multimeter probe to the engine block. Measure the resistance. The multimeter **must** show an open circuit (more than 10M ohms).
>
> If the resistance values in any of the previous checks are **not** within the specification, there is a short circuit to ground, provided the engine speed sensor has been previously checked. Replace the engine harness. Refer to Procedure [[01-019-043 — Engine Wiring Harness|019-043]].
>
> **CAUTION · Осторожно**
> Do not use probes or leads other than Part Number 3822758. The leads must fit tightly in the connector without expanding the pins of the connector.
>
> Connect the engine harness inline connector.
>
> Disconnect the extension harness from the ECM.
>
> Insert the test lead into the engine speed sensor 1 signal pin at the extension harness connector. Touch the other multimeter probe to the engine block. Measure the resistance. The multimeter **must** show an open circuit (more than 10M ohms).
>
> Insert the test lead into the engine speed sensor 1 return pin at the extension harness connector. Touch the other multimeter probe to the engine block. Measure the resistance. The multimeter **must** show an open circuit (more than 10M ohms).
>
> Insert the test lead into the engine speed sensor 2 signal pin at the extension harness connector. Touch the other multimeter probe to the engine block. Measure the resistance. The multimeter **must** show an open circuit (more than 10M ohms).
>
> Insert the test lead into the engine speed sensor 2 return pin at the extension harness connector. Touch the other multimeter probe to the engine block. Measure the resistance. The multimeter **must** show an open circuit (more than 10M ohms).
>
> If the resistance values in any of the previous checks at the extension harness connector are **not** within the specification, there is a short circuit to ground, provided the engine speed sensor has been previously checked. Replace the extension harness. Refer to Procedure [[01-019-175 — Extension Wiring Harness|019-175]].
>
> ### Check for Short Circuit from Pin to Pin
>
> **CAUTION · Осторожно**
> Do not use probes or leads other than Part Number 3822758 or 3822917. The leads must fit tightly in the connector without expanding the pins of the connector.
>
> Disconnect the engine harness inline connector.
>
> Disconnect the engine speed sensor from the engine harness.
>
> Insert the test lead into the engine speed sensor 1 signal pin at the engine harness inline connector. Insert the other test lead into all of the other pins on the engine harness inline connector, one at a time. Measure the resistance for each pin. The multimeter **must** show an open circuit (more than 10M ohms) for all pins in the connector.
>
> Insert the test lead into the engine speed sensor 1 return pin at the engine harness inline connector. Insert the other test lead into all of the other pins on the engine harness inline connector, one at a time. Measure the resistance for each pin. The multimeter **must** show an open circuit (more than 10M ohms) for all pins in the connector.
>
> Insert the test lead into the engine speed sensor 2 signal pin at the engine harness inline connector. Insert the other test lead into all of the other pins on the engine harness inline connector, one at a time. Measure the resistance for each pin. The multimeter **must** show an open circuit (more than 10M ohms) for all pins in the connector.
>
> Insert the test lead into the engine speed sensor 2 return pin at the engine harness inline connector. Insert the other test lead into all of the other pins on the engine harness inline connector, one at a time. Measure the resistance for each pin. The multimeter **must** show an open circuit (more than 10M ohms) for all pins in the connector.
>
> If the resistance values in any of the previous checks are **not** within specification, there is a short circuit from one of the engine speed sensor wires to any pin that measures less than 10M ohms. Repair or replace the engine harness. Refer to Procedures [[01-019-043 — Engine Wiring Harness|019-043]] and [[99-019-208 — Deutsch HDP20 and HD30 Connector Series|019-208]].
>
> **CAUTION · Осторожно**
> Do not use probes or leads other than Part Number 3822758. The leads must fit tightly in the connector without expanding the pins of the connector.
>
> Disconnect the extension harness from the ECM.
>
> Insert the test lead into the engine speed sensor 1 signal pin at the extension harness connector. Insert the other test lead into all of the other pins on the extension harness connector, one at a time. Measure the resistance for each pin. The multimeter **must** show an open circuit (more than 10M ohms) for all pins in the connector.
>
> Insert the test lead into the engine speed sensor 1 return pin at the extension harness connector. Insert the other test lead into all of the other pins on the extension harness connector, one at a time. Measure the resistance for each pin. The multimeter **must** show an open circuit (more than 10M ohms) for all pins in the connector.
>
> Insert the test lead into the engine speed sensor 2 signal pin at the extension harness connector. Insert the other test lead into all of the other pins on the extension harness connector, one at a time. Measure the resistance for each pin. The multimeter **must** show an open circuit (more than 10M ohms) for all pins in the connector.
>
> Insert the test lead into the engine speed sensor 2 return pin at the extension harness connector. Insert the other test lead into all of the other pins on the extension harness connector, one at a time. Measure the resistance for each pin. The multimeter **must** show an open circuit (more than 10M ohms) for all pins in the connector.
>
> If the resistance values in any of the previous checks at the extension harness connector are **not** within specification, there is a short circuit from one of the engine speed sensor wires to any pin that measures less than 10M ohms. Repair or replace the extension harness. Refer to Procedures [[01-019-175 — Extension Wiring Harness|019-175]] and [[99-019-213 — D-Sub Miniature Connector Series|019-213]].
