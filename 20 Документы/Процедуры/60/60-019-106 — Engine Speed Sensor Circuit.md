---
aliases:
  - "Цепь датчика частоты вращения двигателя"
type: "Процедура"
doc: "60-019-106"
title_en: "Engine Speed Sensor Circuit"
title_ru: "Цепь датчика частоты вращения двигателя"
modified: "2007-12-14"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021674"
figures: 10
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-019-106.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-019-106.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
  - "перевод/машинный"
---

# Engine Speed Sensor Circuit
**Цепь датчика частоты вращения двигателя**

> [!abstract] Процедура · `60-019-106`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section 19 — Electronic Engine Controls — Group 19
> **Даты:** изменён 2007-12-14
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-019-106.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-019-106.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Подготовительные операции

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Чтобы снизить риск искрения, минусовой (-) провод аккумуляторной батареи снимайте первым, а подсоединяйте последним.

- Отсоедините аккумуляторные батареи. См. процедуру 013-009 (Кабели и соединения аккумуляторов) в разделе 13 в руководстве по обслуживанию QST30, Бюллетень [[4021539 — QST30 Service Manual\|4021539]].

![[ck800wa.png]]

### Проверка сопротивления

> [!warning] ОСТОРОЖНО
> Не используйте щупы или провода, кроме Части № 3822758 или 3822917. Лиды должны плотно помещаться в разъеме без расширения штифтов разъема.

Отключите проводку двигателя от 50-контактных разъемов от ECM1, ECM2 и ECM3.

Убедитесь, что датчик скорости двигателя подключен к электропроводке.

![[19a00825.png]]

Измерить сопротивление между сигналом скорости коленчатого вала двигателя и обратного контакта скорости коленчатого вала двигателя на разъеме электропроводки двигателя ECM1. Значение сопротивления должно быть от 750 до 1100 Ом.

Измерьте сопротивление между сигналом датчика скорости коленчатого вала двигателя и обратным контактом скорости коленчатого вала двигателя на разъеме электропроводки двигателя ECM2. Значение сопротивления должно быть от 1100 до 1500 Ом.

Если любое из показаний не соответствует спецификациям, при условии, что датчик скорости двигателя был проверен, замените электропроводку двигателя.[[60-019-043 — Engine Wiring Harness|См. процедуру 019-043 (Применение электропроводки двигателя) в разделе 19.]]

![[19a00826.png]]

> [!warning] ОСТОРОЖНО
> Не используйте щупы или провода, отличные от Части № 3822758. Лиды должны плотно помещаться в разъеме без расширения штифтов разъема.

Подключите проводку двигателя с 50-контактным соединением к ECM1, ECM2 и ECM3.

Убедитесь, что датчик скорости двигателя подключен к электропроводке.

![[19a00825.png]]

Измерить сопротивление между сигналом скорости коленчатого вала двигателя и возвратом скорости коленчатого вала двигателя на 50-контактном разъеме ECM1. Измерьте сопротивление между сигналом коленчатого вала двигателя и возвратом скорости коленчатого вала двигателя на 50-контактном разъеме ECM2. Значения сопротивления должны быть от 1000 до 2000 Ом.

Если любое из показаний не соответствует спецификациям, при условии, что датчик скорости двигателя был проверен, замените удлинитель проводов.

![[19a00826.png]]

### Проверка на замыкание на массу

Отсоедините проводку двигателя от 50-контактного разъема от ECM1, ECM2 и ECM3.

![[19a00825.png]]

> [!warning] ОСТОРОЖНО
> Не используйте щупы или провода, кроме Части № 3822758 или 3822917. Лиды должны плотно помещаться в разъеме без расширения штифтов разъема.

Включить испытательный щуп в датчик скорости коленчатого вала двигателя, сигнальный контакт, и другой испытательный щуп в датчик скорости коленчатого вала двигателя, возвращаемый в 50-контактном разъеме ECM1. Повторите тест на сопротивление для ECM2 и ECM3. Измерьте сопротивление. Мультиметр **должен** показывать открытую схему (более 100 к Ом).

Если значения сопротивления в любой из предыдущих проверок **не** в пределах спецификации, есть короткое замыкание на землю, при условии, что датчик скорости коленчатого вала двигателя был ранее проверен. Замените жгут проводов двигателя.[[60-019-043 — Engine Wiring Harness|См. процедуру 019-043 (Применение электропроводки двигателя) в разделе 19.]]

![[19a00826.png]]

### Проверка на замыкание между контактами

> [!warning] ОСТОРОЖНО
> Не используйте щупы или провода, кроме Части № 3822758 или 3822917. Лиды должны плотно помещаться в разъеме без расширения штифтов разъема.

Отсоедините проводку двигателя от 50-контактного разъема от ECM1, ECM2 и ECM3.

Отсоедините датчик скорости двигателя от электропроводки двигателя.

![[19a00825.png]]

Включить испытательный щуп в датчик скорости коленчатого вала двигателя 1 сигнального контакта в электропроводке двигателя ECM1. Вставьте другой испытательный щуп во все другие штифты на электропроводке двигателя ECM1, по одному за раз. Измерьте сопротивление для каждого штифта. Мультиметр **должен** показывать открытую схему (более 100k Ом) для всех контактов в разъеме.

Повторите процедуру тестирования для ECM2 и ECM3.

Включить испытательный щуп в датчик 1 оборота двигателя обратного контакта на проводах двигателя ремня встраиваемого разъема. Вставьте другой измерительный щуп во все другие штифты на встроенном разъёме проводов двигателя, по одному за раз. Измерьте сопротивление для каждого штифта. Мультиметр **должен** показывать открытую схему (более 100k Ом) для всех контактов в разъеме.

Если значения сопротивления в любой из предыдущих проверок **не** в пределах спецификации, то происходит короткое замыкание от одного из проводов датчика скорости двигателя до любого штифта, который измеряет менее 10 м Ом. Ремонт или замена ремня электропроводки двигателя.[[60-019-043 — Engine Wiring Harness|См. процедуру 019-043 (Применение электропроводки двигателя) в разделе 19.]] [[99-019-208 — Deutsch HDP20 and HD30 Connector Series|См. процедуру 019-208 (DeutschTM HDP20 и HD30 Connector Series) в разделе 19.]]

![[19a00826.png]]

### Завершающие операции

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Чтобы снизить риск искрения, минусовой (-) провод аккумуляторной батареи снимайте первым, а подсоединяйте последним.

- Подсоедините аккумуляторные батареи. См. процедуру 013-009 (Кабели и соединения аккумуляторов) в разделе 13 в руководстве по обслуживанию QST30, Бюллетень [[4021539 — QST30 Service Manual\|4021539]].

![[ck800wa.png]]


> [!quote]- Original (English) · английский оригинал
> ### Preparatory Steps
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> - Disconnect the batteries. Refer to Procedure 013-009 (Battery Cables and Connections) in Section 13 in the QST30 Service Manual, Bulletin [[4021539 — QST30 Service Manual\|4021539]].
>
> ### Resistance Check
>
> **CAUTION · Осторожно**
> Do not use probes or leads other than Part Number 3822758 or 3822917. The leads must fit tightly in the connector without expanding the pins of the connector.
>
> Disconnect the engine harness 50-pin connectors from ECM1, ECM2, and ECM3.
>
> Make sure the engine speed sensor is connected to the harness.
>
> Measure the resistance between the engine crankshaft speed signal and engine crankshaft speed return pin at the engine harness ECM1 connector. The resistance value **must** be 750 to 1100 ohms.
>
> Measure the resistance between the engine crankshaft speed sensor signal and engine crankshaft speed return pin at the engine harness ECM2 connector. The resistance value **must** be 1100 to 1500 ohms.
>
> If either of the readings are outside of the specifications, provided the engine speed sensor has been checked, replace the engine harness. [[60-019-043 — Engine Wiring Harness|Refer to Procedure 019-043 (Engine Wiring Harness) in Section 19.]]
>
> **CAUTION · Осторожно**
> Do not use probes or leads other than Part Number 3822758. The leads must fit tightly in the connector without expanding the pins of the connector.
>
> Connect the engine harness 50-pin connection to ECM1, ECM2, and ECM3.
>
> Make sure the engine speed sensor is connected to the harness.
>
> Measure the resistance between the engine crankshaft speed signal and the engine crankshaft speed return at ECM1 50-pin connector. Measure the resistance between the engine crankshaft signal and the engine crankshaft speed return at the ECM2 50-pin connector. The resistance values **must** be between 1000 to 2000 ohms.
>
> If either of the readings are outside of the specifications, provided the engine speed sensor has been checked, replace the extension harness.
>
> ### Check for Short Circuit to Ground
>
> Disconnect the engine harness 50-pin connector from ECM1, ECM2, and ECM3.
>
> **CAUTION · Осторожно**
> Do not use probes or leads other than Part Number 3822758 or 3822917. The leads must fit tightly in the connector without expanding the pins of the connector.
>
> Insert the test lead into the engine crankshaft speed sensor signal pin and the other test lead into the engine crankshaft speed sensor return in the ECM1 50-pin connector. Repeat the resistance test for ECM2 AND ECM3. Measure the resistance. The multimeter **must** show an open circuit (more than 100 k ohms).
>
> If the resistance values in any of the previous checks are **not** within the specification, there is a short circuit to ground, provided the engine crankshaft speed sensor has been previously checked. Replace the engine harness. [[60-019-043 — Engine Wiring Harness|Refer to Procedure 019-043 (Engine Wiring Harness) in Section 19.]]
>
> ### Check for Short Circuit from Pin to Pin
>
> **CAUTION · Осторожно**
> Do not use probes or leads other than Part Number 3822758 or 3822917. The leads must fit tightly in the connector without expanding the pins of the connector.
>
> Disconnect the engine harness 50-pin connector from ECM1, ECM2, and ECM3.
>
> Disconnect the engine speed sensor from the engine harness.
>
> Insert the test lead into the engine crankshaft speed sensor 1 signal pin at the ECM1 engine harness. Insert the other test lead into all of the other pins on the ECM1 engine harness, one at a time. Measure the resistance for each pin. The multimeter **must** show an open circuit (more than 100k ohms) for all pins in the connector.
>
> Repeat the test procedure for ECM2 and ECM3.
>
> Insert the test lead into the engine speed sensor 1 return pin at the engine harness inline connector. Insert the other test lead into all of the other pins on the engine harness inline connector, one at a time. Measure the resistance for each pin. The multimeter **must** show an open circuit (more than 100k ohms) for all pins in the connector.
>
> If the resistance values in any of the previous checks are **not** within specification, there is a short circuit from one of the engine speed sensor wires to any pin that measures less than 10M ohms. Repair or replace the engine harness. [[60-019-043 — Engine Wiring Harness|Refer to Procedure 019-043 (Engine Wiring Harness) in Section 19.]] [[99-019-208 — Deutsch HDP20 and HD30 Connector Series|Refer to Procedure 019-208 (Deutsch™ HDP20 and HD30 Connector Series) in Section 19.]]
>
> ### Finishing Steps
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> - Connect the batteries. Refer to Procedure 013-009 (Battery Cables and Connections) in Section 13 in the QST30 Service Manual, Bulletin [[4021539 — QST30 Service Manual\|4021539]].
