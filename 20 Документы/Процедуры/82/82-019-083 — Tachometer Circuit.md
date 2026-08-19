---
aliases:
  - "Цепь тахометра"
type: "Процедура"
doc: "82-019-083"
title_en: "Tachometer Circuit"
title_ru: "Цепь тахометра"
modified: "2002-06-27"
engines:
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 6
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-083.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-019-083.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# Tachometer Circuit
**Цепь тахометра**

> [!abstract] Процедура · `82-019-083`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section 19 - Electronic Engine Controls
> **Даты:** изменён 2002-06-27
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-083.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-019-083.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

ECM может подавать выходной сигнал для работы тахометра автомобиля. Схема - выходной сигнал, провод - нет. 11, и тахометром внутренней земли в электропроводке OEM.

![[19c00345.png]]

### Проверка сопротивления

Отсоедините разъём OEM-проводов от ECM. Отсоедините тахометр от электропроводки OEM.

> [!warning] ОСТОРОЖНО
> Не используйте ни пробы, ни зацепки, кроме Части Нет. 3822758. Разъём будет повреждён. Лиды должны плотно помещаться в разъеме без расширения контактов разъема.

Включить один испытательный щуп в контакт 11 разъёма проводной упряжки OEM и подключить испытательный щуп к многометровому щупу.

![[19c00346.png]]

Найдите разъем тахометра в электропроводке OEM.

Подключите другой испытательный щуп к другому многометровому щупу и прикоснитесь к нему соответствующим контактным тахометровым соединительным шлюзом. Проконсультируйтесь с руководством по устранению неполадок и ремонту OEM для схем проводов.

Установите мультиметр на установку сопротивления и измерьте сопротивление.

Мультиметр **должен** показать замкнутую цепь (10 Ом и менее). Если схема **не** закрыта, то имеется открытая схема или провода в разъеме тахометра перевернуты. Ремонт или замена провода, подключенного к контакту 11 в электропроводке OEM, в соответствии с процедурами производителя транспортного средства.

![[19c00347.png]]

### Проверка на замыкание на массу

Отсоедините тахометр от электропроводки OEM.

Вставьте измерительный щуп в контакт 11 разъёма проводов OEM-проводов и соедините его с многометровым щупом. Прикоснитесь к другому многометровому щупу к заземлению блока двигателя. Измерьте сопротивление.

Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Если схема ** не открыта в любом из предыдущих испытаний, отремонтируйте провода, которые имеют неправильные показания, в соответствии с процедурами производителя транспортного средства.

![[19c00342.png]]

### Проверка на замыкание между контактами

Отсоедините тахометр от электропроводки OEM.

Вставьте измерительный щуп в контакт 11 разъёма проводов OEM-проводов и соедините его с многометровым щупом. Вставьте другой испытательный щуп в контакт 10 разъёма проводов OEM-приемника и прикрепите его к другому щупу. Измерьте сопротивление.

Мультиметр **должен** показать обрыв цепи (100 кОм и более).

![[19200334.png]]

Удалите многометровый свинец из контакта 10 и проверьте все контакты в разъеме. Измерьте сопротивление. Мультиметр ** должен** показывать открытую схему (100к Ом или более) на всех штифтах. Если мультиметр регистрирует замкнутую цепь на любом штифте, между контактом 11 и этим штифтом существует короткое замыкание.

Ремонт проводной упряжки OEM. См. процедуру 019-250.

![[19c00344.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> The ECM can supply an output signal to operate the vehicle tachometer. The circuit is the output signal, wire No. 11, and a tachometer internal ground in the OEM harness.
>
> ### Resistance Check
>
> Disconnect the OEM harness connector from the ECM. Disconnect the tachometer from the OEM harness.
>
> **CAUTION · Осторожно**
> Do not use probes or leads other than Part No. 3822758. The connector will be damaged. The leads must fit tightly in the connector without expanding the connector pins.
>
> Insert one test lead into pin 11 of the OEM harness connector and connect the test lead to the multimeter probe.
>
> Locate the tachometer connector in the OEM harness.
>
> Connect the other test lead to the other multimeter probe and touch it to the appropriate tachometer connector pin. Consult the OEM troubleshooting and repair manual for wiring schematics.
>
> Set the multimeter to the resistance setting and measure the resistance.
>
> The multimeter **must** show a closed circuit (10 ohms or less). If the circuit is **not** closed, there is an open circuit or the wires in the tachometer connector are reversed. Repair or replace the wire connected to pin 11 in the OEM harness according to the vehicle manufacturer's procedures.
>
> ### Check for Short Circuit to Ground
>
> Disconnect the tachometer from the OEM harness.
>
> Insert the test lead into pin 11 of the OEM harness connector, and connect it to the multimeter probe. Touch the other multimeter probe to the engine block ground. Measure the resistance.
>
> The multimeter **must** show an open circuit (100k ohms or more).
>
> If the circuit is **not** open in either of the previous tests, repair the wires which have incorrect readings, according to the vehicle manufacturer's procedures.
>
> ### Check for Short Circuit from Pin to Pin
>
> Disconnect the tachometer from the OEM harness.
>
> Insert the test lead into pin 11 of the OEM harness connector, and connect it to the multimeter probe. Insert the other test lead into pin 10 of the OEM harness connector and attach it to the other probe. Measure the resistance.
>
> The multimeter **must** show an open circuit (100k ohms or more).
>
> Remove the multimeter lead from pin 10, and test all pins in the connector. Measure the resistance. The multimeter **must** show an open circuit (100k ohms or more) at all pins. If the multimeter registers a closed circuit at any pin, a short circuit exists between pin 11 and that pin.
>
> Repair the OEM harness. Refer to Procedure 019-250.
