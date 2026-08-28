---
type: "Процедура"
doc: "98-019-182"
title_en: "Intermediate Speed Switch Circuit"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-019-182.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-019-182.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K19"
  - "группа/98"
  - "перевод/машинный"
---

# Intermediate Speed Switch Circuit

> [!abstract] Процедура · `98-019-182`
> **Двигатели:** [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]]
> **Семейство:** K19
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-04-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-019-182.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-019-182.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Часть схемы переключателя промежуточной скорости в основной проводах двигателя состоит из сигнального провода, подключенного к контакту 5 разъёма главного разъёма проводов двигателя, и провода промежуточной проверки скорости, подключенного к контакту 2.

Для проверки OEM-части схемы переключателя средней скорости обратитесь к процедуре 019-071.

> [!note] Примечание
> Не все приложения CENTRYTM используют промежуточную/альтернативную валидацию сбрасывания.

![[19801748.png]]

### Проверка сопротивления

Отключите разъем ECM и разъем C5.

Выберите функцию сопротивления на мультиметре.

Прикосновение к одному из мультиметров приводит к контакту 5 главного разъёма проводов двигателя. Прикосновение к другому мультиметру приводит к контакту E основной стороны проводов двигателя с ремнем разъема C5.

![[19801749.png]]

Измерьте сопротивление.

Мультиметр **должен **показывать менее 10 Ом, что является замкнутой схемой. Если цепь **не **закрыта, то в сигнальном проводе имеется открытая цепь.

Ремонт основной электропроводки двигателя упряжкой, или, при необходимости, ее замена. См. процедуру 019-228 или[[98-019-043 — Engine Wiring Harness|019-043]].

![[19801619.png]]

Повторите вышеупомянутую проверку сопротивления для проволоки проверки средней скорости.

Прикосновение к одному из мультиметров приводит к контакту 2 главного разъёма проводов двигателя. Прикосновение к другому мультиметру приводит к контакту C основной стороны проводов двигателя с ремнем разъема C5.

Измерьте сопротивление. Мультиметр **должен **показывать менее 10 Ом.

![[19801751.png]]

### Проверка на замыкание на массу

Убедитесь, что разъем ECM и разъем C5 отключены.

Прикосновение к одному из мультиметров приводит к контакту 5 главного разъёма проводов двигателя. Прикосновение к другому мультиметру приводит к хорошей, чистой поверхности на блоке двигателя.

![[19801752.png]]

Измерьте сопротивление.

Мультиметр **должен **показывать более 100k ом, что является открытой схемой. Если схема **не** открыта, то между проводом, подключенным к контакту 5, и землей шасси есть короткое замыкание.

Ремонт основной электропроводки двигателя упряжкой, или, при необходимости, ее замена. См. процедуру 019-228 или[[98-019-043 — Engine Wiring Harness|019-043]].

![[19801621.png]]

Повторите вышеупомянутое короткое замыкание для проверки на промежуточной скорости проволоки.

Прикосновение к одному из мультиметров приводит к контакту 2 главного разъёма проводов двигателя. Прикосновение к другому мультиметру приводит к хорошей, чистой поверхности на блоке двигателя.

Измерьте сопротивление. Мультиметр **должен **показывать более 100k ом.

![[19801754.png]]

### Проверка на замыкание между контактами

Убедитесь, что разъем ECM и разъем C5 отключены.

Проверьте короткое замыкание между контактом 5 основного разъёма проводов двигателя и **всеми **другими контактами в разъеме.

Прикосновение к одному из мультиметров приводит к контакту 5 главного разъёма проводов двигателя. Прикосновение к другому мультиметру приводит к **всем **другим штифтам в разъеме, по одному за раз.

![[19801755.png]]

Измерьте сопротивление.

Мультиметр **должен **показывать более 100k ом, что является открытой схемой. Если схема **не** открыта, то между проводами, подключенными к контакту 5 соединительной проводов, и **любым** другим штифтом, который измеряется менее 100k Ом.

Ремонт основной электропроводки двигателя упряжкой, или, при необходимости, ее замена. См. процедуру 019-228 или[[98-019-043 — Engine Wiring Harness|019-043]].

![[19801621.png]]

Повторите вышеупомянутое короткое замыкание от пин-кодов до пин-контроля.

Прикосновение к одному из мультиметров приводит к контакту 2 главного разъёма проводов двигателя. Прикосновение к другому мультиметру приводит к **всем **другим штифтам в разъеме, по одному за раз.

Измерьте сопротивление. Мультиметр **должен **показывать более 100k ом.

![[19801757.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> The portion of the intermediate-speed switch circuit in the main engine harness consists of the signal wire connected to pin 5 of the main engine harness connector and the intermediate-speed validation wire connected to pin 2.
>
> To check the OEM portion of the intermediate-speed switch circuit, refer to Procedure 019-071.
>
> **Note · Примечание**
> **Not** all CENTRY™ applications use intermediate-speed/alternate droop validation.
>
> ### Resistance Check
>
> Disconnect the ECM connector and the C5 connector.
>
> Select the resistance function on the multimeter.
>
> Touch one of the multimeter leads to pin 5 of the main engine harness connector. Touch the other multimeter lead to pin E of the main engine harness side of the C5 connector.
>
> Measure the resistance.
>
> The multimeter **must** show less than 10 ohms, which is a closed circuit. If the circuit is **not** closed, then there is an open circuit in the signal wire.
>
> Repair the main engine harness, or, if necessary, replace it. Refer to Procedure 019-228 or [[98-019-043 — Engine Wiring Harness|019-043]].
>
> Repeat the above resistance check for the intermediate-speed validation wire.
>
> Touch one of the multimeter leads to pin 2 of the main engine harness connector. Touch the other multimeter lead to pin C of the main engine harness side of the C5 connector.
>
> Measure the resistance. The multimeter **must** show less than 10 ohms.
>
> ### Check for Short Circuit to Ground
>
> Make sure the ECM connector and the C5 connector are disconnected.
>
> Touch one of the multimeter leads to pin 5 of the main engine harness connector. Touch the other multimeter lead to a good, clean surface on the engine block.
>
> Measure the resistance.
>
> The multimeter **must** show more than 100k ohms, which is an open circuit. If the circuit is **not** open, then there is a short circuit between the wire connected to pin 5 and chassis ground.
>
> Repair the main engine harness, or, if necessary, replace it. Refer to Procedure 019-228 or [[98-019-043 — Engine Wiring Harness|019-043]].
>
> Repeat the above short circuit to ground check for the intermediate-speed validation wire.
>
> Touch one of the multimeter leads to pin 2 of the main engine harness connector. Touch the other multimeter lead to a good, clean surface on the engine block.
>
> Measure the resistance. The multimeter **must** show more than 100k ohms.
>
> ### Check for Short Circuit from Pin to Pin
>
> Make sure the ECM connector and the C5 connector are disconnected.
>
> Check for a short circuit between pin 5 of the main engine harness connector and **all** other pins in the connector.
>
> Touch one of the multimeter leads to pin 5 of the main engine harness connector. Touch the other multimeter lead to **all** other pins in the connector, one at a time.
>
> Measure the resistance.
>
> The multimeter **must** show more than 100k ohms, which is an open circuit. If the circuit is **not** open, then there is a short between the wires connected to pin 5 of the connector harness and **any** other pin that measured less than 100k ohms.
>
> Repair the main engine harness, or, if necessary, replace it. Refer to Procedure 019-228 or [[98-019-043 — Engine Wiring Harness|019-043]].
>
> Repeat the above short circuit from pin to pin check.
>
> Touch one of the multimeter leads to pin 2 of the main engine harness connector. Touch the other multimeter lead to **all** other pins in the connector, one at a time.
>
> Measure the resistance. The multimeter **must** show more than 100k ohms.
