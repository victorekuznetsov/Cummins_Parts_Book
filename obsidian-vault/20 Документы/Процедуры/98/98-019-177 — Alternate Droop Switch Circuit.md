---
aliases:
  - "Цепь выключателя альтернативного статизма"
type: "Процедура"
doc: "98-019-177"
title_en: "Alternate Droop Switch Circuit"
title_ru: "Цепь выключателя альтернативного статизма"
modified: "2003-04-01"
engines:
  - "37269910"
  - "37280605"
families:
  - "K19"
manuals:
  - "3666070"
figures: 15
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-019-177.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-019-177.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K19"
  - "группа/98"
  - "перевод/машинный"
---

# Alternate Droop Switch Circuit
**Цепь выключателя альтернативного статизма**

> [!abstract] Процедура · `98-019-177`
> **Двигатели:** [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]]
> **Семейство:** K19
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-04-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-019-177.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-019-177.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Часть схемы переключателя в основной проводах двигателя состоит из сигнального провода, подключенного к контакту 28 основного разъёма проводов двигателя и промежуточного провода проверки скорости / альтернативного сужения, подключенного к контакту 2.

Для проверки OEM-части схемы переключателя с дроп-ключом обратитесь к процедуре 019-071.

Переключатель расположен на панели интерфейса драйвера.

![[19801738.png]]

> [!note] Примечание
> Не все приложения CENTRYTM используют промежуточную проверку скорости/альтернативное снижение. Некоторые приложения будут использовать реле или удаленно установленный переключатель вместо переключателя панели интерфейса. Посмотрите руководство по устранению неполадок и ремонту OEM, чтобы увидеть, как подключена конкретная система.

![[nobox.png]]

### Проверка сопротивления

Если имеется электронный сервисный инструмент, то за переключателем следует следить для правильной работы. Если коммутатор правильно меняет состояние на инструменте обслуживания, то проблема не лежит в цепи коммутатора. Если электронный инструмент службы не доступен, проверьте переключатель вручную.

Найдите переключатель на панели интерфейса драйвера и удалите его.

См. руководство по устранению неполадок и ремонту OEM для процедуры.

![[19801910.png]]

Отсоедините провода, подключенные к коммутатору (провод Nos). C6-C, C6-D, C6-H.

> [!note] Примечание
> Коммутатор обычно является открытым коммутатором.

Выберите функцию сопротивления на мультиметре.

Прикосновение к мультиметру приводит к терминалам на коммутаторе.

Переключите переключение на положение OFF (open).

![[19801912.png]]

Измерьте сопротивление.

Мультиметр **должен **показывать более 100k ом, что является открытой схемой. Если схема **не **открыта, то внутри переключателя есть короткое замыкание.

Замените выключатель. См. руководство по устранению неполадок и ремонту OEM для процедуры.

![[19801621.png]]

Переключите переключатель на положение ON.

Измерьте сопротивление. Мультиметр **должен **показывать менее 10 Ом, что является замкнутой схемой. Если схема **не **закрыта, то в переключателе есть открытая схема.

Замените выключатель. См. руководство по устранению неполадок и ремонту OEM для процедуры.

![[19801914.png]]

Проверьте основную часть проводов двигателя ремня запасного выключателя.

Отключите разъем ECM и разъем C5.

Прикосновение к одному из мультиметров приводит к контакту 28 главного разъёма проводов двигателя. Прикосновение к другому мультиметру приводит к контакту D основной стороны проводов двигателя с ремнем разъема C5.

![[19801739.png]]

Измерьте сопротивление.

Мультиметр **должен **показывать менее 10 Ом, что является замкнутой схемой. Если цепь **не **закрыта, то в сигнальном проводе имеется открытая цепь.

Ремонт основной электропроводки двигателя упряжкой, или, при необходимости, ее замена. См. процедуру 019-228 или[[98-019-043 — Engine Wiring Harness|019-043]].

![[19801619.png]]

Повторите вышеупомянутую проверку сопротивления для альтернативного проволоки проверки сбрасывания.

Прикосновение к одному из мультиметров приводит к контакту 2 главного разъёма проводов двигателя. Прикосновение к другому мультиметру приводит к контакту C основной стороны проводов двигателя с ремнем разъема C5.

Измерьте сопротивление. Мультиметр **должен **показывать менее 10 Ом.

![[19801741.png]]

### Проверка на замыкание на массу

Убедитесь, что разъем ECM и разъем C5 отключены.

Прикосновение к одному из мультиметров приводит к контакту 28 главного разъёма проводов двигателя. Прикосновение к другому мультиметру приводит к хорошей, чистой поверхности на блоке двигателя.

![[19801742.png]]

Измерьте сопротивление.

Мультиметр **должен **показывать более 100k ом, что является открытой схемой. Если схема **не** открыта, то между проводом, подключенным к контакту 28, и землей шасси есть короткое замыкание.

Ремонт основной электропроводки двигателя упряжкой, или, при необходимости, ее замена. См. процедуру 019-228 или[[98-019-043 — Engine Wiring Harness|019-043]].

![[19801621.png]]

Повторите вышеупомянутую короткую проверку на землю для альтернативного проволоки проверки сбрасывания.

Прикосновение к одному из мультиметров приводит к контакту 2 главного разъёма проводов двигателя. Прикосновение к другому мультиметру приводит к хорошей, чистой поверхности на блоке двигателя.

Измерьте сопротивление. Мультиметр **должен **показывать более 100k ом.

![[19801744.png]]

### Проверка на замыкание между контактами

Убедитесь, что разъем ECM и разъем C5 отключены.

Проверьте короткое замыкание между контактом 28 главного разъёма проводов двигателя и **всеми **другими контактами в разъеме.

Прикосновение к одному из мультиметров приводит к контакту 28 главного разъёма проводов двигателя. Прикосновение к другому мультиметру приводит к **всем **другим штифтам в разъеме, по одному за раз.

![[19801745.png]]

Измерьте сопротивление.

Мультиметр **должен **показывать более 100k ом, что является открытой схемой. Если схема **не** открыта, то между проводами, подключенными к контакту 28 основного жгута проводов двигателя, и **любым** другим штифтом, который измеряется менее 100k Ом.

Ремонт основной электропроводки двигателя упряжкой, или, при необходимости, ее замена. См. процедуру 019-228 или[[98-019-043 — Engine Wiring Harness|019-043]].

![[19801621.png]]

Повторите вышеупомянутый короткий штифт, чтобы проверить штифт для альтернативного проволоки проверки сбрасывания.

Прикосновение к одному из мультиметров приводит к контакту 2 главного разъёма проводов двигателя. Прикосновение к другому мультиметру приводит к **всем **другим штифтам в разъеме, по одному за раз.

Измерьте сопротивление.

Мультиметр **должен **показывать более 100k ом.

![[19801747.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> The portion of the switch circuit in the main engine harness consists of the signal wire connected to pin 28 of the main engine harness connector and the intermediate speed/alternate droop validation wire connected to pin 2.
>
> To check the OEM portion of the alternate droop switch circuit, refer to Procedure 019-071.
>
> The switch is located on the driver interface panel.
>
> **Note · Примечание**
> **Not** all CENTRY™ applications use intermediate speed/alternate droop validation. Some applications will use a relay or remotely mounted switch instead of an interface panel switch. Refer to the OEM troubleshooting and repair manual to see how a particular system is wired.
>
> ### Resistance Check
>
> If an electronic service tool is available, then the switch should be monitored for proper operation. If the switch is changing state correctly on the service tool, then the problem does **not** lie in the switch circuit. If an electronic service tool is **not** available, check the switch manually.
>
> Locate the switch on the driver interface panel and remove it.
>
> Refer to the OEM troubleshooting and repair manual for the procedure.
>
> Disconnect the wires connected to the switch (wire Nos. C6-C, C6-D, C6-H).
>
> **Note · Примечание**
> The switch is a normally open switch.
>
> Select the resistance function on the multimeter.
>
> Touch the multimeter leads to the terminals on the switch.
>
> Toggle the switch to the OFF (open) position.
>
> Measure the resistance.
>
> The multimeter **must** show more than 100k ohms, which is an open circuit. If the circuit is **not** open, then there is a short circuit within the switch.
>
> Replace the switch. Refer to the OEM troubleshooting and repair manual for the procedure.
>
> Toggle the switch to the ON position.
>
> Measure the resistance. The multimeter **must** show less than 10 ohms, which is a closed circuit. If the circuit is **not** closed, then there is an open circuit within the switch.
>
> Replace the switch. Refer to the OEM troubleshooting and repair manual for the procedure.
>
> Check the main engine harness portion of the alternate droop switch circuit.
>
> Disconnect ECM connector and the C5 connector.
>
> Touch one of the multimeter leads to pin 28 of the main engine harness connector. Touch the other multimeter lead to pin D of the main engine harness side of the C5 connector.
>
> Measure the resistance.
>
> The multimeter **must** show less than 10 ohms, which is a closed circuit. If the circuit is **not** closed, then there is a open circuit in the signal wire.
>
> Repair the main engine harness, or, if necessary, replace it. Refer to Procedure 019-228 or [[98-019-043 — Engine Wiring Harness|019-043]].
>
> Repeat the above resistance check for the alternate droop validation wire.
>
> Touch one of the multimeter leads to pin 2 of the main engine harness connector. Touch the other multimeter lead to pin C of the main engine harness side of the C5 connector.
>
> Measure the resistance. The multimeter **must** show less than 10 ohms.
>
> ### Check for Short Circuit to Ground
>
> Make sure the ECM connector and the C5 connector are disconnected.
>
> Touch one of the multimeter leads to pin 28 of the main engine harness connector. Touch the other multimeter lead to a good, clean surface on the engine block.
>
> Measure the resistance.
>
> The multimeter **must** show more than 100k ohms, which is an open circuit. If the circuit is **not** open, then there is a short circuit between the wire connected to pin 28 and chassis ground.
>
> Repair the main engine harness, or, if necessary, replace it. Refer to Procedure 019-228 or [[98-019-043 — Engine Wiring Harness|019-043]].
>
> Repeat the above short to ground check for the alternate droop validation wire.
>
> Touch one of the multimeter leads to pin 2 of the main engine harness connector. Touch the other multimeter lead to a good, clean surface on the engine block.
>
> Measure the resistance. The multimeter **must** show more than 100k ohms.
>
> ### Check for Short Circuit from Pin to Pin
>
> Make sure the ECM connector and the C5 connector are disconnected.
>
> Check for a short circuit between pin 28 of the main engine harness connector and **all** other pins in the connector.
>
> Touch one of the multimeter leads to pin 28 of the main engine harness connector. Touch the other multimeter lead to **all** other pins in the connector, one at a time.
>
> Measure the resistance.
>
> The multimeter **must** show more than 100k ohms, which is an open circuit. If the circuit is **not** open, then there is a short between the wires connected to pin 28 of the main engine harness and **any** other pin that measured less than 100k ohms.
>
> Repair the main engine harness, or, if necessary, replace it. Refer to Procedure 019-228 or [[98-019-043 — Engine Wiring Harness|019-043]].
>
> Repeat the above short pin to pin check for the alternate droop validation wire.
>
> Touch one of the multimeter leads to pin 2 of the main engine harness connector. Touch the other multimeter lead to **all** other pins in the connector, one at a time.
>
> Measure the resistance.
>
> The multimeter **must** show more than 100k ohms.
