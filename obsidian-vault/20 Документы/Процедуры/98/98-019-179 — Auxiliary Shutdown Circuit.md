---
type: "Процедура"
doc: "98-019-179"
title_en: "Auxiliary Shutdown Circuit"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-019-179.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-019-179.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K19"
  - "группа/98"
  - "перевод/машинный"
---

# Auxiliary Shutdown Circuit

> [!abstract] Процедура · `98-019-179`
> **Двигатели:** [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]]
> **Семейство:** K19
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-04-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-019-179.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-019-179.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Часть вспомогательной цепи отключения в основной проводах двигателя состоит из провода водителя, соединенного с контактом 1 главного разъёма проводов двигателя.

Для проверки OEM-части вспомогательной цепи отключения обратитесь к процедуре 019-071.

> [!note] Примечание
> Если провод водителя подключен к соленоиду отключения топлива, используйте этот раздел для устранения проблем с отключением топлива.

> [!note] Примечание
> Не все приложения CENTRYTM будут использовать вспомогательную схему отключения. Некоторые приложения будут использовать его в качестве выходного сигнала крутящего момента.

![[19801697.png]]

### Проверка сопротивления

Отключите разъем ECM и разъем C6.

Выберите функцию сопротивления на мультиметре.

Прикосновение к одному из мультиметров приводит к контакту 1 главного разъёма проводов двигателя. Прикосновение к другому мультиметру приводит к контакту F основной стороны проводов двигателя с ремнем разъема C6.

![[19801698.png]]

Измерьте сопротивление.

Мультиметр **должен **показывать менее 10 Ом, что является замкнутой схемой. Если цепь **не** закрыта, то отремонтируйте основную проводку двигателя упряжкой, или, при необходимости, замените ее. См. процедуру 019-228 или[[98-019-043 — Engine Wiring Harness|019-043]].

![[19801619.png]]

### Проверка на замыкание на массу

Убедитесь, что разъем ECM и разъем C6 отключены.

Прикосновение к одному из мультиметров приводит к контакту 1 главного разъёма проводов двигателя. Прикосновение к другому мультиметру приводит к хорошей, чистой поверхности блока двигателя.

![[19801700.png]]

Измерьте сопротивление.

Мультиметр **должен **показывать более 100k ом, что является открытой схемой. Если цепь **не** закрыта, то между проводом, подключенным к контакту 1 и землей шасси, имеется короткое замыкание.

Ремонт основной электропроводки двигателя упряжкой, или, при необходимости, ее замена. См. процедуру 019-228 или[[98-019-043 — Engine Wiring Harness|019-043]].

![[19801621.png]]

### Проверка на замыкание между контактами

Убедитесь, что разъем C6 отключен.

Проверьте короткое замыкание между контактом 1 главного разъёма проводов двигателя и **всеми **другими штифтами в разъеме.

Прикосновение к одному из мультиметров приводит к контакту 1 главного разъёма проводов двигателя. Прикосновение к другому мультиметру приводит к **всем **другим штифтам в разъеме, по одному за раз.

![[19801702.png]]

Измерьте сопротивление.

Мультиметр **должен **показывать более 100k ом, что является открытой схемой. Если схема **не** открыта, то между проводами, подключенными к контакту 1 с основной проводкой двигателя, и **любым** другим штифтом, который измеряется менее 100k Ом.

Ремонт основной электропроводки двигателя упряжкой, или, при необходимости, ее замена. См. процедуру 019-228 или[[98-019-043 — Engine Wiring Harness|019-043]].

![[19801621.png]]

### Проверка напряжения

Убедитесь, что разъем C6 отключен.

Подключите разъем ECM.

Включите зажигание.

Выберите функцию постоянного напряжения на мультиметре.

Прикосновение к одному из мультиметров приводит к контакту F основной стороны проводов двигателя с ремнем разъема C6. Прикоснитесь к другой многометровой поверхности с хорошей, чистой поверхностью блока двигателя.

![[19801704.png]]

Измерьте напряжение.

Мультиметр **должен** показывать то же самое, что и напряжение батареи (12 или 24 ВДК). Если напряжение **не** правильно, то проверьте электропроводку на предмет повреждения. Если напряжение все еще низкое, проверьте соединения батареи на коррозию и очистите их, если это необходимо.

![[19801705.png]]

### Проверьте короткое замыкание на источнике внешнего напряжения

Отключите разъем ECM.

Подключите разъем C6.

Прикосновение к одному из мультиметров приводит к контакту 1 главного разъёма проводов двигателя. Прикосновение к другому мультиметру приводит к хорошей, чистой поверхности на блоке двигателя.

![[19802692.png]]

Измерьте напряжение.

Мультиметр **must** показывает 1 VDC или меньше. Если напряжение **не** правильно, то между проводом водителя и внешним источником напряжения имеется короткое замыкание.

Удалите внешний источник напряжения.

![[19801707.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> The portion of the auxiliary shutdown circuit in the main engine harness consists of the driver wire connected to pin 1 of the main engine harness connector.
>
> To check the OEM portion of the auxiliary shutdown circuit, refer to Procedure 019-071.
>
> **Note · Примечание**
> If the driver wire is connected to the fuel shutoff solenoid, then use this section to troubleshoot fuel shutoff solenoid circuit problems.
>
> **Note · Примечание**
> Not all CENTRY™ applications will use the auxiliary shutdown circuit. Some applications will use it as torque output signal wire.
>
> ### Resistance Check
>
> Disconnect the ECM connector and the C6 connector.
>
> Select the resistance function on the multimeter.
>
> Touch one of the multimeter leads to pin 1 of the main engine harness connector. Touch the other multimeter lead to pin F of the main engine harness side of the C6 connector.
>
> Measure the resistance.
>
> The multimeter **must** show less than 10 ohms, which is a closed circuit. If the circuit is **not** closed, then repair the main engine harness, or, if necessary, replace it. Refer to Procedure 019-228 or [[98-019-043 — Engine Wiring Harness|019-043]].
>
> ### Check for Short Circuit to Ground
>
> Make sure the ECM connector and the C6 connector are disconnected.
>
> Touch one of the multimeter leads to pin 1 of the main engine harness connector. Touch the other multimeter lead to a good, clean surface of the engine block.
>
> Measure the resistance.
>
> The multimeter **must** show more than 100k ohms, which is an open circuit. If the circuit is **not** closed, then there is a short circuit between the wire connected to pin 1 and chassis ground.
>
> Repair the main engine harness, or, if necessary, replace it. Refer to Procedure 019-228 or [[98-019-043 — Engine Wiring Harness|019-043]].
>
> ### Check for Short Circuit from Pin to Pin
>
> Make sure the C6 connector is disconnected.
>
> Check for a short circuit between pin 1 of the main engine harness connector and **all** other pins in the connector.
>
> Touch one of the multimeter leads to pin 1 of the main engine harness connector. Touch the other multimeter lead to **all** other pins in the connector, one at a time.
>
> Measure the resistance.
>
> The multimeter **must** show more than 100k ohms, which is an open circuit. If the circuit is **not** open, then there is a short circuit between the wires connected to pin 1 of the main engine harness and **any** other pin that measured less than 100k ohms.
>
> Repair the main engine harness, or, if necessary, replace it. Refer to Procedure 019-228 or [[98-019-043 — Engine Wiring Harness|019-043]].
>
> ### Voltage Check
>
> Make sure the C6 connector is disconnected.
>
> Connect the ECM connector.
>
> Turn keyswitch ON.
>
> Select the DC voltage function on the multimeter.
>
> Touch one of the multimeter leads to pin F of the main engine harness side of the C6 connector. Touch the other multimeter to a good, clean surface of the engine block.
>
> Measure the voltage.
>
> The multimeter **must** show the same as battery voltage (12 or 24 VDC). If the voltage is **not** correct, then inspect the wiring harness for damage. If the voltage is still low, check the battery connections for corrosion and clean them, if necessary.
>
> ### Check for Short Circuit to External Voltage Source
>
> Disconnect the ECM connector.
>
> Connect the C6 connector.
>
> Touch one of the multimeter leads to pin 1 of the main engine harness connector. Touch the other multimeter lead to a good, clean surface on the engine block.
>
> Measure the voltage.
>
> The multimeter **must** show 1 VDC or less. If the voltage is **not** correct, then there is a short circuit between the driver wire and an external voltage source.
>
> Remove the external voltage source.
