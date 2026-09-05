---
aliases:
  - "Переключатель режима диагностики"
type: "Процедура"
doc: "99-019-027"
title_en: "Diagnostic Test Mode Switch"
title_ru: "Переключатель режима диагностики"
modified: "2015-06-22"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
  - "37269910"
  - "37280605"
  - "37292556"
  - "37295879"
  - "85017333"
  - "93058669"
  - "93087701"
families:
  - "C8.3 · 6C8.3"
  - "K19"
  - "QSK23"
  - "QSK60"
  - "QST30"
manuals:
  - "3666070"
  - "3666113"
  - "3666214"
  - "4021419"
  - "4021442"
figures: 6
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-027.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/99-019-027.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "двигатель/K19"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "двигатель/QST30"
  - "группа/99"
  - "перевод/машинный"
---

# Diagnostic Test Mode Switch
**Переключатель режима диагностики**

> [!abstract] Процедура · `99-019-027`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]], [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]], [[85017333 — QSK23 CM500 CPL 2858|85017333]], [[93058669 — 6C8.3 CPL 3105|93058669]], [[93087701 — 6C8.3 CPL 3105|93087701]]
> **Семейство:** C8.3 · 6C8.3, K19, QSK23, QSK60, QST30
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]], [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]], [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]], [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]], [[4021442 — C8.3 Marine Electronic Control System Troubleshooting and Repair Manual|4021442]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2015-06-22
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-027.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/99-019-027.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Диагностическая схема переключателя ON/OFF сигнализирует системе, что оператор запрашивает считывание любого активного кода неисправности, записанного в ECM.

> [!note] Примечание
> Некоторые OEM используют шортинг, а не переключатель.

![[gp8swvs.png]]

Когда ECM получает сигнал от диагностического переключателя ON/OFF, желтый и красный предупредительные огни включаются и начинают мигать, если в ECM записан какой-либо активный код неисправности. Если оба предупреждающих огня остаются включенными и не мигают, то активных кодов неисправностей не существует.

> [!note] Примечание
> Оборудование должно быть стационарным. Если скорость движения будет обнаружена, то мигающая последовательность будет **не**.

![[19400239.png]]

### Проверка сопротивления

Если имеется электронный инструмент обслуживания, проверьте переключатель для правильной работы. Если **не**, следуйте процедурам устранения неполадок в этом разделе.

Найдите нужный переключатель ON/OFF. Удалите и пометьте два разъема из терминалов на коммутаторе.

Прикоснитесь к многометровым зондам к терминалам на выключателе.

![[19900590.png]]

Переместите переключатель в положение выключения и измерьте сопротивление. Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Если схема не открыта, выключатель не работает.

См. руководство по устранению неполадок и ремонту OEM для процедур замены.

![[19900591.png]]

Переместите переключатель в положение Включения и измерьте сопротивление. Мультиметр **должен** показать замкнутую цепь (10 Ом и менее). Если цепь **не **закрыта, выключатель не работает.

См. руководство по устранению неполадок и ремонту OEM для процедур замены.

Если значение сопротивления правильное, переключатель должен быть проверен на короткое замыкание на землю.

![[wr8swkd.png]]

### Проверка на замыкание на массу

Прикоснитесь к одному из многометровых щупов к одному из переключателей. Прикоснитесь к другому щупу на земле шасси. Переместите переключатель в положение Включения и измерьте сопротивление. Мультиметр **должен** показать обрыв цепи (100 кОм и более). Если схема **не открыта, выключатель не работает. См. руководство по устранению неполадок и ремонту OEM для процедур замены. Если переключатель проходит все предыдущие проверки, схема **должна быть проверена на открытую схему, короткое замыкание на землю, короткое замыкание от штифта до штифта и короткое замыкание к внешнему источнику напряжения.

![[19c01165.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> The diagnostic ON/OFF switch circuit signals the system that the operator is requesting to read any active fault code recorded in the ECM.
>
> **Note · Примечание**
> Some OEM's use a shorting plug rather than a switch.
>
> When the ECM receives the signal from the diagnostic ON/OFF switch, the yellow and red warning lights will come on and start flashing if any active fault code is recorded in the ECM. If both warning lights remain on and do **not** flash, there are no active fault codes present.
>
> **Note · Примечание**
> The equipment **must** be stationary. If road speed is detected, the flashing sequence will **not** occur.
>
> ### Resistance Check
>
> If an electronic service tool is available, monitor the switch for proper operation. If **not**, follow the troubleshooting procedures in this section.
>
> Locate the desired ON/OFF toggle switch. Remove and tag the two connectors from the terminals on the switch.
>
> Touch the multimeter probes to the terminals on the switch.
>
> Move the switch to the OFF position and measure the resistance. The multimeter **must** show an open circuit (100k ohms or more).
>
> If the circuit is **not** open, the switch has failed.
>
> Refer to the OEM troubleshooting and repair manual for the replacement procedures.
>
> Move the switch to the ON position and measure the resistance. The multimeter **must** show a closed circuit (10 ohms or less). If the circuit is **not** closed, the switch has failed.
>
> Refer to the OEM troubleshooting and repair manual for the replacement procedures.
>
> If the resistance value is correct, the switch **must** still be checked for a short circuit to ground.
>
> ### Check for Short Circuit to Ground
>
> Touch one of the multimeter probes to one of the switch terminals. Touch the other probe to chassis ground. Move the switch to the ON position and measure the resistance. The multimeter **must** show an open circuit (100k ohms or more). If the circuit is **not** open, the switch has failed. Refer to the OEM troubleshooting and repair manual for replacement procedures. If the switch passes all of the previous checks, the circuit **must** be checked for an open circuit, a short circuit to ground, a short circuit from pin to pin, and a short circuit to an external voltage source.
