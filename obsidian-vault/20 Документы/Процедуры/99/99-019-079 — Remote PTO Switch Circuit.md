---
aliases:
  - "Цепь дистанционного выключателя отбора мощности"
type: "Процедура"
doc: "99-019-079"
title_en: "Remote PTO Switch Circuit"
title_ru: "Цепь дистанционного выключателя отбора мощности"
modified: "2015-06-29"
engines:
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 5
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-079.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/99-019-079.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/99"
  - "перевод/машинный"
---

# Remote PTO Switch Circuit
**Цепь дистанционного выключателя отбора мощности**

> [!abstract] Процедура · `99-019-079`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section 19 - Electronic Engine Controls
> **Даты:** изменён 2015-06-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-079.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/99-019-079.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Проверка сопротивления

> [!warning] ОСТОРОЖНО
> Правильные провода и/или одобренный Cummins® инструмент для тестирования цепи должны использоваться при работе с электрическими разъемами для предотвращения расширения штифта и повреждения разъема.

Отключите разъем интерфейса оригинального производителя оборудования (OEM) проводов жгута проводов двигателя. Чтобы определить местоположение разъема, см. соответствующую схему проводов двигателя.

Вставьте измерительный щуп в пульт дистанционного отбора мощности (PTO) переключателя обратного контакта разъема проводов OEM-проводов и подключите его к многометровому щупу. Вставьте другой испытательный щуп в удаленный PTO-переключатель сигнального контакта разъема и соедините его с другим щупом.

Убедитесь, что выключатель подключен к цепи. Переместите удаленный PTO-переключатель в положение ON. Измерьте сопротивление с помощью мультиметра. Мультиметр **должен** показать замкнутую цепь (10 Ом и менее). Если цепь ** не** закрыта, проверьте обратный провод переключателя и сигнальный провод удаленного переключателя PTO для открытой цепи. Ремонт или замена OEM-проводов при условии, что выключатель был ранее проверен. См. руководство по устранению неполадок и ремонту OEM для процедур.

![[19c01256.png]]

Если сопротивление правильное, провод возврата пульта переключателя PTO и провод сигнала пульта переключателя PTO ** должны быть проверены на короткое замыкание на землю, короткое замыкание от штифта до штифта и короткое замыкание на внешний источник напряжения.

Подключите все компоненты после завершения ремонта.

![[19c01257.png]]

### Проверка на замыкание на массу

> [!warning] ОСТОРОЖНО
> Правильные провода и/или одобренный Cummins® инструмент для тестирования цепи должны использоваться при работе с электрическими разъемами для предотвращения расширения штифта и повреждения разъема.

Отключите разъем интерфейса оригинального производителя оборудования (OEM) проводов жгута проводов двигателя. Чтобы определить местоположение разъема, см. соответствующую схему проводов двигателя.

Вставьте измерительный щуп в удаленный контакт сигнала PTO-переключателя в разъеме OEM-проводов и подключите его к многометровому щупу. Прикоснитесь к другому щупу, чтобы заземлить двигатель.

С помощью пульта дистанционного PTO переключателя в положении OFF, считайте сопротивление.

Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Если значения сопротивления ** не** верны, убедитесь, что на коммутаторе правильно установлена дистанционная сигнальная проводка PTO-коммутатора и наземная проводка. Если оба провода правильно установлены, проверьте провода на короткое заземление, при условии, что удаленный PTO-переключатель был ранее проверен.

![[19c01258.png]]

### Проверка на замыкание между контактами

Проверьте короткое замыкание от пин-кодов до пин-кодов. Установите удаленный PTO-переключатель в положение OFF. Вставьте измерительный щуп в удаленный PTO-коммутатор обратного контакта разъема проводов OEM-производителя и подключите его к многометровому щупу. С помощью измерительного щупа, подключенного к другому многометровому щупу, проверьте все остальные штифты в разъеме. Измерьте сопротивление. Мультиметр **должен** показать обрыв цепи (100 кОм и более).

![[19c01168.png]]

Удалите свинец из удаленного PTO-ключа обратного контакта и вставьте его в удаленный PTO-ключ сигнального контакта разъёма проводов. С другим измерительным щупом проверьте все другие штифты в разъеме. Измерьте сопротивление. Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Если схема ** не** открыта, между схемой переключателя и любым штифтом, который не измерял открытую схему, существует короткое замыкание при условии, что переключатель ранее был проверен. Ремонт или замена проводов в электропроводке OEM в соответствии с процедурами производителя транспортного средства.

После ремонта подсоедините все компоненты.

![[19c01236.png]]


> [!quote]- Original (English) · английский оригинал
> ### Resistance Check
>
> **CAUTION · Осторожно**
> Proper leads and/or a Cummins® approved circuit testing tool must be used when working with electrical connectors to prevent pin expansion and damage to the connector.
>
> Disconnect the original equipment manufacturer (OEM) harness engine interface connector. To determine the location of the connector, see the corresponding engine wiring diagram.
>
> Insert a test lead into the remote power take-off (PTO) switch return pin of the OEM harness connector and connect it to the multimeter probe. Insert the other test lead into the remote PTO switch signal pin of the connector and connect it to the other probe.
>
> Make sure the switch is connected to the circuit. Move the remote PTO switch to the ON position. Measure the resistance with the multimeter. The multimeter **must** show a closed circuit (10 ohms or less). If the circuit is **not** closed, inspect the switch return wire and the remote PTO switch signal wire for an open circuit. Repair or replace the OEM harness, provided the switch has been previously checked. Refer to the OEM troubleshooting and repair manual for the procedures.
>
> If the resistance is correct, the remote PTO switch return wire and the remote PTO switch signal wire **must** be checked for a short circuit to ground, a short circuit from pin to pin, and a short circuit to an external voltage source.
>
> Connect all components after the repair is complete.
>
> ### Check for Short Circuit to Ground
>
> **CAUTION · Осторожно**
> Proper leads and/or a Cummins® approved circuit testing tool must be used when working with electrical connectors to prevent pin expansion and damage to the connector.
>
> Disconnect the original equipment manufacturer (OEM) harness engine interface connector. To determine the location of the connector, see the corresponding engine wiring diagram.
>
> Insert the test lead into the remote PTO switch signal pin in the OEM harness connector and connect it to the multimeter probe. Touch the other probe to engine block ground.
>
> With the remote PTO switch in the OFF position, read the resistance.
>
> The multimeter **must** show an open circuit (100k ohms or more).
>
> If the resistance values are **not** correct, make sure the remote PTO switch signal wire and the ground wire are properly installed on the switch. If both wires are correctly installed, inspect the wires for a short to ground circuit, provided the remote PTO switch has been previously checked.
>
> ### Check for Short Circuit from Pin to Pin
>
> Check for a short circuit from pin to pin. Set the remote PTO switch to the OFF position. Insert the test lead into the remote PTO switch return pin of the OEM harness connector and connect it to the multimeter probe. With a test lead connected to the other multimeter probe, check all the other pins in the connector. Measure the resistance. The multimeter **must** show an open circuit (100k ohms or more).
>
> Remove the lead from the remote PTO switch return pin and insert it into the remote PTO switch signal pin of the harness connector. With the other test lead, check all other pins in the connector. Measure the resistance. The multimeter **must** show an open circuit (100k ohms or more).
>
> If the circuit is **not** open, there is a short circuit between the switch circuit and any pin that did **not** measure an open circuit, provided the switch has previously been checked. Repair or replace the wires in the OEM harness according to the vehicle manufacturer's procedures.
>
> Connect all components after completing the repair.
