---
aliases:
  - "Цепь датчика температуры охлаждающей жидкости"
type: "Процедура"
doc: "98-019-020"
title_en: "Coolant Temperature Sensor Circuit"
title_ru: "Цепь датчика температуры охлаждающей жидкости"
modified: "2003-04-01"
engines:
  - "37269910"
  - "37280605"
families:
  - "K19"
manuals:
  - "3666070"
figures: 10
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-019-020.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-019-020.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K19"
  - "группа/98"
  - "перевод/машинный"
---

# Coolant Temperature Sensor Circuit
**Цепь датчика температуры охлаждающей жидкости**

> [!abstract] Процедура · `98-019-020`
> **Двигатели:** [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]]
> **Семейство:** K19
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-04-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-019-020.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-019-020.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Часть цепи датчика в основной проводах двигателя состоит из сигнального провода (контакт 5) и обратного провода (контакт 25 или 26).

Часть цепи датчика в проводной упряжке OEM состоит из сигнального провода (C5-E) и обратного провода (C5-H).

![[19801656.png]]

### Проверка сопротивления

Отключите разъем ECM.

Отключите разъем C5.

![[19801656.png]]

Выберите функцию сопротивления на мультиметре.

Прикосновение к одному из мультиметров приводит к контакту 5 главного разъёма проводов двигателя. Прикосновение к другому мультиметру приводит к контакту E на основной стороне проводов двигателя жгута проводов разъема C5.

![[19802690.png]]

Измерьте сопротивление.

Мультиметр **должен **показывать менее 10 Ом, что является замкнутой схемой. Если цепь **не **закрыта, то в сигнальном проводе имеется открытая цепь.

Ремонт основной электропроводки двигателя упряжкой, или, при необходимости, ее замена. См. процедуру 019-228 или[[98-019-043 — Engine Wiring Harness|019-043]].

![[19801619.png]]

Повторите вышеупомянутую проверку сопротивления для обратного провода.

Прикосновение к одному из мультиметров приводит либо к контакту 25, либо к контакту 26 главного разъёма проводов двигателя. Прикосновение к другому мультиметру приводит к контакту Н основной стороны проводов двигателя с ремнем разъема С5.

Измерьте сопротивление. Мультиметр **должен **показывать менее 10 Ом.

> [!note] Примечание
> Система будет работать должным образом, если работает только один из проводов возврата батареи. Однако если цепь открыта на одном из проводов возврата батареи, то следует отремонтировать главный упряжь проводов двигателя.

![[19801659.png]]

### Проверка на замыкание на массу

Отключите разъем ECM.

Отключите разъем C5.

Прикосновение к одному из мультиметров приводит к контакту 5 главного разъёма проводов двигателя. Прикосновение к другому мультиметру приводит к хорошей, чистой поверхности на блоке двигателя.

![[19801660.png]]

Измерьте сопротивление.

Мультиметр **должен **показывать более 100k ом, что является открытой схемой. Если схема **не** открыта, то между проводом, подключенным к контакту 5, и землей шасси есть короткое замыкание.

Ремонт основной электропроводки двигателя упряжкой, или, при необходимости, ее замена. См. процедуру 019-228 или[[98-019-043 — Engine Wiring Harness|019-043]].

![[19801621.png]]

### Проверка на замыкание между контактами

Отключите разъем ECM.

Отключите разъем C5.

Проверьте короткое замыкание между контактом 5 основного разъёма проводов двигателя и **всеми **другими контактами в разъеме.

Прикосновение к одному из мультиметров приводит к контакту 5 главного разъёма проводов двигателя. Прикосновение к другому мультиметру приводит к **всем **другим штифтам в главном разъеме проводов двигателя, по одному за раз.

![[19801662.png]]

Измерьте сопротивление.

Мультиметр **должен **показывать более 100k ом, что является открытой схемой. Если схема **не** открыта, то между проводами, подключенными к контакту 5 главного разъёма проводов двигателя, и **любым** другим штифтом, который зарегистрировал замкнутую цепь, имеется короткое расстояние.

Ремонт основной электропроводки двигателя упряжкой, или, при необходимости, ее замена. См. процедуру 019-228 или[[98-019-043 — Engine Wiring Harness|019-043]].

![[19801621.png]]

Проверьте короткое замыкание между проводом возврата температуры охлаждающей жидкости и всеми другими штифтами.

Прикосновение к одному из мультиметров приводит к контакту 25 главного разъёма проводов двигателя. Прикосновение к другому мультиметру приводит к **всем **другим штифтам в разъеме**, за исключением **контакта 26.

Измерьте сопротивление.

Мультиметр **должен **показывать менее 100k ом.

![[19801693.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> The portion of the sensor circuit in the main engine harness consists of the signal wire (pin 5) and the return wire (pin 25 or 26).
>
> The portion of the sensor circuit in the OEM harness consists of the signal wire (C5-E) and the return wire (C5-H).
>
> ### Resistance Check
>
> Disconnect the ECM connector.
>
> Disconnect the C5 connector.
>
> Select the resistance function on the multimeter.
>
> Touch one of the multimeter leads to pin 5 of the main engine harness connector. Touch the other multimeter lead to pin E on the main engine harness side of the C5 connector.
>
> Measure the resistance.
>
> The multimeter **must** show less than 10 ohms, which is a closed circuit. If the circuit is **not** closed, then there is an open circuit in the signal wire.
>
> Repair the main engine harness, or, if necessary, replace it. Refer to Procedure 019-228 or [[98-019-043 — Engine Wiring Harness|019-043]].
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
> ### Check for Short Circuit to Ground
>
> Disconnect the ECM connector.
>
> Disconnect the C5 connector.
>
> Touch one of the multimeter leads to pin 5 of the main engine harness connector. Touch the other multimeter lead to a good, clean surface on the engine block.
>
> Measure the resistance.
>
> The multimeter **must** show more than 100k ohms, which is an open circuit. If the circuit is **not** open, then there is a short circuit between the wire connected to pin 5 and chassis ground.
>
> Repair the main engine harness, or, if necessary, replace it. Refer to Procedure 019-228 or [[98-019-043 — Engine Wiring Harness|019-043]].
>
> ### Check for Short Circuit from Pin to Pin
>
> Disconnect the ECM connector.
>
> Disconnect the C5 connector.
>
> Check for a short circuit between pin 5 of the main engine harness connector and **all** other pins in the connector.
>
> Touch one of the multimeter leads to pin 5 of the main engine harness connector. Touch the other multimeter lead to **all** other pins in the main engine harness connector, one at a time.
>
> Measure the resistance.
>
> The multimeter **must** show more than 100k ohms, which is an open circuit. If the circuit is **not** open, then there is a short between the wires connected to pin 5 of the main engine harness connector and **any** other pin that registered the closed circuit.
>
> Repair the main engine harness, or, if necessary, replace it. Refer to Procedure 019-228 or [[98-019-043 — Engine Wiring Harness|019-043]].
>
> Check for a short circuit between the coolant temperature return wire and all other pins.
>
> Touch one of the multimeter leads to pin 25 of the main engine harness connector. Touch the other multimeter lead to **all** other pins in the connector **except** pin 26.
>
> Measure the resistance.
>
> The multimeter **must** show less than 100k ohms.
