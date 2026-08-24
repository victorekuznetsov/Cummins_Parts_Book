---
aliases:
  - "Выключатель круиз-контроля или отбора мощности"
type: "Процедура"
doc: "82-019-021"
title_en: "Cruise Control or PTO ON/OFF Switch"
title_ru: "Выключатель круиз-контроля или отбора мощности"
modified: "2005-01-28"
engines:
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 5
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-021.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-019-021.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# Cruise Control or PTO ON/OFF Switch
**Выключатель круиз-контроля или отбора мощности**

> [!abstract] Процедура · `82-019-021`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section 19 - Electronic Engine Controls
> **Даты:** изменён 2005-01-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-021.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-019-021.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Переключатель переключения включения/выключения используется для активации или отключения операции круиз-контроля и операции PTO. Схема круиз-контроля ON и OFF состоит из контакта 23 (сигнал включения / выключения), общей площадки переключателя и переключателя переключения, установленного на кабине OEM.

![[19c00184.png]]

### Проверка сопротивления

Если InsiteTM доступен, проверьте переключатель на правильное функционирование. Если **не**, следуйте процедурам устранения неполадок в этом разделе.

Найдите нужный переключатель включения / выключения. Удалите и пометьте два разъема из терминалов на коммутаторе. Прикоснитесь к многометровым зондам к терминалам на выключателе.

![[19900590.png]]

Переместите переключатель в положение выключения и измерьте сопротивление. Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Если схема ** не открыта, выключатель не работает. См. руководство по устранению неполадок и ремонту OEM для процедур замены.

![[19900591.png]]

Переместите переключатель в положение Включения и измерьте сопротивление. Мультиметр **должен** показать замкнутую цепь (10 Ом и менее).

Если цепь ** не ** закрыта, выключатель не работает. См. руководство по устранению неполадок и ремонту OEM для процедур замены.

Если значение сопротивления правильное, переключатель ** должен быть проверен на короткое замыкание на землю.

![[wr8swkd.png]]

### Проверка на замыкание на массу

Прикоснитесь к одному из многометровых щупов к одному из переключателей. Прикоснитесь к другому щупу на земле шасси. Переместите переключатель в положение Включения и измерьте сопротивление. Мультиметр **должен** показать обрыв цепи (100 кОм и более). Если схема ** не открыта, выключатель не работает. См. руководство по устранению неполадок и ремонту OEM для процедур замены. Если переключатель проходит все предыдущие проверки, схема ** должна быть проверена на открытую схему, короткое замыкание на землю, короткое замыкание от штифта до штифта и короткое замыкание к внешнему источнику напряжения.

![[19900592.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> The on/off toggle switch is used to activate or disable the cruise control operation and PTO operation. The cruise control ON and OFF circuit consists of pin 23 (on/off signal), switch common ground, and the OEM cab-mounted toggle switch.
>
> ### Resistance Check
>
> If INSITE™ is available, monitor the switch for proper operation. If **not**, follow the troubleshooting procedures in this section.
>
> Locate the desired on/off toggle switch. Remove and tag the two connectors from the terminals on the switch. Touch the multimeter probes to the terminals on the switch.
>
> Move the switch to the OFF position and measure the resistance. The multimeter **must** show an open circuit (100k ohms or more).
>
> If the circuit is **not** open, the switch has failed. Refer to the OEM troubleshooting and repair manual for the replacement procedures.
>
> Move the switch to the ON position and measure the resistance. The multimeter **must** show a closed circuit (10 ohms or less).
>
> If the circuit is **not** closed, the switch has failed. Refer to the OEM troubleshooting and repair manual for the replacement procedures.
>
> If the resistance value is correct, the switch **must** still be checked for a short circuit to ground.
>
> ### Check for Short Circuit to Ground
>
> Touch one of the multimeter probes to one of the switch terminals. Touch the other probe to chassis ground. Move the switch to the ON position and measure the resistance. The multimeter **must** show an open circuit (100k ohms or more). If the circuit is **not** open, the switch has failed. Refer to the OEM troubleshooting and repair manual for replacement procedures. If the switch passes all of the previous checks, the circuit **must** be checked for an open circuit, a short circuit to ground, a short circuit from pin to pin, and a short circuit to an external voltage source.
