---
type: "Процедура"
doc: "98-019-068"
title_en: "Engine Oil Temperature Sensor Circuit"
modified: "2003-04-01"
engines:
  - "37269910"
  - "37280605"
families:
  - "K19"
manuals:
  - "3666070"
figures: 11
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-019-068.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-019-068.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K19"
  - "группа/98"
  - "перевод/машинный"
---

# Engine Oil Temperature Sensor Circuit

> [!abstract] Процедура · `98-019-068`
> **Двигатели:** [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]]
> **Семейство:** K19
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-04-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-019-068.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-019-068.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Часть схемы датчика температуры масла в основной проводах двигателя состоит из сигнального провода (контакт 28) и обратного провода (контакт 25 или 26).

Часть цепи в проводной упряжке OEM состоит из сигнального провода (контакт C5-D) и обратного провода (C5-H).

![[19801801.png]]

### Проверка сопротивления

Отключите разъемы ECM и C5.

Выберите функцию сопротивления на мультиметре.

Прикосновение к одному из мультиметров приводит к контакту 28 главного разъёма проводов двигателя. Прикосновение к другому мультиметру приводит к контакту D на основной стороне проводов двигателя жгута проводов разъема C5.

![[19801802.png]]

Измерьте сопротивление.

Мультиметр **должен **показывать менее 10 Ом, что является замкнутой схемой. Если цепь **не **закрыта, в сигнальном проводе имеется открытая цепь.

Ремонт или замена основного двигателя проводов жгута. См. процедуру 019-228 или[[98-019-043 — Engine Wiring Harness|019-043]].

![[19801619.png]]

Повторите вышеупомянутую проверку сопротивления для обратного провода.

Прикосновение к одному из мультиметров приводит либо к контакту 25, либо к контакту 26 главного разъёма проводов двигателя. Прикосновение к другому мультиметру приводит к контакту Н основной стороны проводов двигателя с ремнем разъема С5.

Измерьте сопротивление. Мультиметр **должен **показывать менее 10 Ом.

> [!note] Примечание
> Система будет работать должным образом, если работает только один из проводов возврата батареи. Однако если цепь открыта на одном из проводов возврата батареи, то следует отремонтировать главный упряжь проводов двигателя.

![[19801804.png]]

Отключите разъем датчика. Убедитесь, что разъем C5 отключен.

Проверьте OEM-часть (контакты C5-E и C5-H) цепи для открытых и коротких замыканий. См. процедуру 019-071.

![[19801834.png]]

### Проверка на замыкание на массу

Убедитесь, что разъемы ECM и C5 отключены.

Прикосновение к одному из мультиметров приводит к контакту 28 главного разъёма проводов двигателя. Прикоснитесь к другому мультиметру, который приведет к заземлению блока двигателя.

![[19801805.png]]

Измерьте сопротивление.

Мультиметр **должен **показывать более 100k ом, что является открытой схемой. Если схема **не** открыта, между проводом, подключенным к контакту 28, и землей шасси есть короткое замыкание.

Ремонт или замена основного двигателя проводов жгута. См. процедуру 019-228 или[[98-019-043 — Engine Wiring Harness|019-043]].

![[19801621.png]]

### Проверка на замыкание между контактами

Убедитесь, что разъем ECM и разъемы C5 и C6 отключены.

Проверьте короткое замыкание между контактом 28 главного разъёма проводов двигателя и **всеми **другими контактами в разъеме.

Прикосновение к одному из мультиметров приводит к контакту 28 главного разъёма проводов двигателя. Прикосновение к другому мультиметру приводит к **всем **другим штифтам в разъеме, по одному за раз.

![[19801807.png]]

Измерьте сопротивление.

Мультиметр **должен **показывать более 100k ом, что является открытой схемой. Если схема **не** открыта, между проводами, подключенными к контакту 28 главного разъёма проводов двигателя, и **любым** другим штифтом, который измеряется менее 100k Ом.

Ремонт или замена основного двигателя проводов жгута. См. процедуру 019-228 или[[98-019-043 — Engine Wiring Harness|019-043]].

![[19801621.png]]

Повторите вышеупомянутое короткое замыкание от пин-кодов до пин-кодов на обратном проводе.

Прикосновение к одному из мультиметров приводит к контакту 25 главного разъёма проводов двигателя. Прикосновение к другому мультиметру приводит к **всем **другим штифтам в разъеме, **за исключением **контакта 26, по одному за раз.

Измерьте сопротивление. Мультиметр **должен **показывать более 100k ом.

![[19801809.png]]

Повторите короткое замыкание от пин-кодов до пин-контроля для второго возвратного провода.

Прикосновение к одному из мультиметров приводит к контакту 26 главного разъёма проводов двигателя. Прикосновение к другому мультиметру приводит к **всем **другим штифтам в разъеме, **за исключением **контакта 25, по одному за раз.

Измерьте сопротивление. Мультиметр **должен **показывать более 100k ом.

![[19802465.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> The portion of the oil temperature sensor circuit in the main engine harness consists of the signal wire (pin 28) and the return wire (pin 25 or 26).
>
> The portion of the circuit in the OEM harness consists of the signal wire (pin C5-D) and the return wire (C5-H).
>
> ### Resistance Check
>
> Disconnect the ECM and the C5 connectors.
>
> Select the resistance function on the multimeter.
>
> Touch one of the multimeter leads to pin 28 of the main engine harness connector. Touch the other multimeter lead to pin D on the main engine harness side of the C5 connector.
>
> Measure the resistance.
>
> The multimeter **must** show less than 10 ohms, which is a closed circuit. If the circuit is **not** closed, there is an open circuit in the signal wire.
>
> Repair or replace the main engine harness. Refer to Procedure 019-228 or [[98-019-043 — Engine Wiring Harness|019-043]].
>
> Repeat the above resistance check for the return wire.
>
> Touch one of the multimeter leads to either pin 25 or pin 26 of the main engine harness connector. Touch the other multimeter lead to pin H of the main engine harness side of the C5 connector.
>
> Measure the resistance. The multimeter **must** show less than 10 ohms.
>
> **Note · Примечание**
> The system will operate properly if **only** one of the battery return wires is working. However, if the circuit is open on one of the battery return wires, then the main engine harness should be repaired.
>
> Disconnect the sensor connector. Make sure the C5 connector is disconnected.
>
> Check the OEM portion (pins C5-E and C5-H) of the circuit for open circuits and short circuits. Refer to Procedure 019-071.
>
> ### Check for Short Circuit to Ground
>
> Make sure the ECM and C5 connectors are disconnected.
>
> Touch one of the multimeter leads to pin 28 of the main engine harness connector. Touch the other multimeter lead to engine block ground.
>
> Measure the resistance.
>
> The multimeter **must** show more than 100k ohms, which is an open circuit. If the circuit is **not** open, there is a short circuit between the wire connected to pin 28 and chassis ground.
>
> Repair or replace the main engine harness. Refer to Procedure 019-228 or [[98-019-043 — Engine Wiring Harness|019-043]].
>
> ### Check for Short Circuit from Pin to Pin
>
> Make sure the ECM connector and the C5 and C6 connectors are disconnected.
>
> Check for a short circuit between pin 28 of the main engine harness connector and **all** other pins in the connector.
>
> Touch one of the multimeter leads to pin 28 of the main engine harness connector. Touch the other multimeter lead to **all** other pins in the connector, one at a time.
>
> Measure the resistance.
>
> The multimeter **must** show more than 100k ohms, which is an open circuit. If the circuit is **not** open, there is a short between the wires connected to pin 28 of the main engine harness connector and **any** other pin that measured less than 100k ohms.
>
> Repair or replace the main engine harness. Refer to Procedure 019-228 or [[98-019-043 — Engine Wiring Harness|019-043]].
>
> Repeat the above short circuit from pin to pin check on the return wire.
>
> Touch one of the multimeter leads to pin 25 of the main engine harness connector. Touch the other multimeter lead to **all** other pins in the connector, **except** pin 26, one at a time.
>
> Measure the resistance. The multimeter **must** show more than 100k ohms.
>
> Repeat the short circuit from pin to pin check for the second return wire.
>
> Touch one of the multimeter leads to pin 26 of the main engine harness connector. Touch the other multimeter lead to **all** other pins in the connector, **except** pin 25, one at a time.
>
> Measure the resistance. The multimeter **must** show more than 100k ohms.
