---
type: "Процедура"
doc: "98-019-180"
title_en: "Step Timing Control Circuit"
modified: "2003-04-01"
engines:
  - "37269910"
  - "37280605"
families:
  - "K19"
manuals:
  - "3666070"
figures: 8
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-019-180.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-019-180.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K19"
  - "группа/98"
  - "перевод/машинный"
---

# Step Timing Control Circuit

> [!abstract] Процедура · `98-019-180`
> **Двигатели:** [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]]
> **Семейство:** K19
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-04-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-019-180.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-019-180.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Схема управления временем шага (STC) состоит из провода водителя, подключенного к контакту 20 основного разъёма проводов двигателя и клапана управления маслом, который управляется соленоидом. Провод водителя STC подключен к этому соленоиду. Клапан управления маслом обычно закрыт. Когда клапан управления маслом закрыт, двигатель находится в нормальном времени.

![[19801616.png]]

### Проверка сопротивления

Отключите разъем ECM.

Отсоедините проводной терминал STC от соленоида STC.

![[19801617.png]]

Выберите функцию сопротивления на мультиметре.

Прикосновение к одному из мультиметров приводит к контакту 20 главного разъёма проводов двигателя. Прикосновение к другому мультиметру приводит к кольцевому терминалу на конце провода драйвера STC.

![[19801618.png]]

Измерьте сопротивление.

Мультиметр **должен **показывать менее 10 Ом, что является замкнутой схемой. Если схема **не **закрыта, то в проводе драйвера STC есть открытая схема.

Ремонт основной электропроводки двигателя упряжкой, или, при необходимости, ее замена. См. процедуру 019-228 или[[98-019-043 — Engine Wiring Harness|019-043]].

![[19801619.png]]

### Проверка на замыкание на массу

Убедитесь, что провод драйвера STC отключен от соленоида.

Прикосновение к одному из мультиметров приводит к контакту 20 главного разъёма проводов двигателя. Прикосновение к другому мультиметру приводит к хорошей, чистой поверхности на блоке двигателя.

![[19801620.png]]

Измерьте сопротивление.

Мультиметр **должен **показывать более 100k ом, что является открытой схемой. Если схема **не** открыта, то между проводом, подключенным к контакту 20, и землей шасси есть короткое замыкание.

Ремонт основной электропроводки двигателя упряжкой, или, при необходимости, ее замена. См. процедуру 019-228 или[[98-019-043 — Engine Wiring Harness|019-043]].

![[19801621.png]]

### Проверка на замыкание между контактами

Отключите разъем ECM и разъемы C5 и C6.

Проверьте короткое замыкание между контактом 20 главного разъёма проводов двигателя и **всеми **другими контактами в разъеме**, за исключением **контактов 25 и 26.

Прикосновение к одному из мультиметров приводит к контакту 20 главного разъёма проводов двигателя. Прикосновение к другому мультиметру приводит к **всем **другим контактам в разъеме**, за исключением **контактов 25 и 26, по одному за раз.

![[19802467.png]]

Измерьте сопротивление.

Мультиметр **должен **показывать более 100k ом, что является открытой схемой. Если схема **не** открыта, то между проводами, подключенными к контакту 20 главного разъёма проводов двигателя, и **любым** другим штифтом, который измеряется менее 100k Ом.

Ремонт основной электропроводки двигателя упряжкой, или, при необходимости, ее замена. См. процедуру 019-228 или[[98-019-043 — Engine Wiring Harness|019-043]].

![[19801621.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> The step timing control (STC) circuit consists of the driver wire connected to pin 20 of the main engine harness connector and an oil control valve that is controlled by a solenoid. The STC driver wire is connected to this solenoid. The oil control valve is normally closed. When the oil control valve is closed, the engine is in normal timing.
>
> ### Resistance Check
>
> Disconnect the ECM connector.
>
> Disconnect the STC driver wire terminal from the STC solenoid.
>
> Select the resistance function on the multimeter.
>
> Touch one of the multimeter leads to pin 20 of the main engine harness connector. Touch the other multimeter lead to the ring terminal on the end of the STC driver wire.
>
> Measure the resistance.
>
> The multimeter **must** show less than 10 ohms, which is a closed circuit. If the circuit is **not** closed, then there is an open circuit in the STC driver wire.
>
> Repair the main engine harness, or, if necessary, replace it. Refer to Procedure 019-228 or [[98-019-043 — Engine Wiring Harness|019-043]].
>
> ### Check for Short Circuit to Ground
>
> Make sure the STC driver wire is disconnected from the solenoid.
>
> Touch one of the multimeter leads to pin 20 of the main engine harness connector. Touch the other multimeter lead to a good, clean surface on the engine block.
>
> Measure the resistance.
>
> The multimeter **must** show more than 100k ohms, which is an open circuit. If the circuit is **not** open, then there is a short circuit between the wire connected to pin 20 and chassis ground.
>
> Repair the main engine harness, or, if necessary, replace it. Refer to Procedure 019-228 or [[98-019-043 — Engine Wiring Harness|019-043]].
>
> ### Check for Short Circuit from Pin to Pin
>
> Disconnect the ECM connector and the C5 and C6 connectors.
>
> Check for a short circuit between pin 20 of the main engine harness connector and **all** other pins in the connector **except** pins 25 and 26.
>
> Touch one of the multimeter leads to pin 20 of the main engine harness connector. Touch the other multimeter lead to **all** other pins in the connector **except** pins 25 and 26, one at a time.
>
> Measure the resistance.
>
> The multimeter **must** show more than 100k ohms, which is an open circuit. If the circuit is **not** open, then there is a short between the wires connected to pin 20 of the main engine harness connector and **any** other pin that measured less than 100k ohms.
>
> Repair the main engine harness, or, if necessary, replace it. Refer to Procedure 019-228 or [[98-019-043 — Engine Wiring Harness|019-043]].
