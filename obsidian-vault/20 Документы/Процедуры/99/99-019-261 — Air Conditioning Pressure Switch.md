---
aliases:
  - "Датчик-реле давления кондиционера"
type: "Процедура"
doc: "99-019-261"
title_en: "Air Conditioning Pressure Switch"
title_ru: "Датчик-реле давления кондиционера"
modified: "2008-05-30"
engines:
  - "41343322"
  - "41370103"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 4
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-261.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/99-019-261.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/99"
  - "перевод/машинный"
---

# Air Conditioning Pressure Switch
**Датчик-реле давления кондиционера**

> [!abstract] Процедура · `99-019-261`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section 19 - Electronic Engine Controls
> **Даты:** изменён 2008-05-30
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-261.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/99-019-261.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Схема переключателя давления кондиционирования воздуха сигнализирует системе, что давление на головку кондиционера высокое, и вентилятор двигателя должен быть включен. Контур давления кондиционирования воздуха состоит из контакта сигнала переключателя давления кондиционирования и обратного контакта переключателя. Эта схема считается «безопасной», то есть, когда схема открыта, вентилятор двигателя будет задействован электронным модулем управления (ECM).

![[19c01234.png]]

### Проверка сопротивления

Найдите выключатель давления кондиционирования воздуха. Удалите электрическое соединение из выключателя. Настройте мультиметр для измерения сопротивления. Прикоснитесь одним многометровым щупом к одному из терминалов на выключателе. Прикоснитесь к другому многометровому щупу к другому терминалу переключателя.

Когда давление на головку системы высокое, мультиметр **должен **показать открытую схему (100к Ом или более). Если схема не открыта, выключатель не работает. См. руководство по устранению неполадок и ремонту оригинального оборудования (OEM) для процедур замены.

![[19c01350.png]]

Когда давление на головку системы низкое, мультиметр **должен **показать замкнутую цепь (10 Ом или меньше). Если цепь **не **закрыта, выключатель не работает. См. руководство по устранению неполадок и ремонту OEM для процедур замены. Если значение сопротивления правильное, переключатель должен быть проверен на короткое замыкание на землю.

![[eb8swkc.png]]

### Проверка на замыкание на массу

Когда давление на головку системы низкое, прикоснитесь к одному из многометровых датчиков к одному из переключателей. Прикоснитесь к другому щупу на земле шасси. Мультиметр **должен** показать обрыв цепи (100 кОм и более). Если схема **не открыта, выключатель не работает. См. руководство по устранению неполадок и ремонту OEM для процедур замены. Если переключатель проходит все предыдущие проверки, схема **должна быть проверена на открытую схему, короткое замыкание на землю, короткое замыкание от штифта до штифта и короткое замыкание к внешнему источнику напряжения.

![[eb8swke.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> The air conditioning pressure switch circuit signals the system that the air conditioner head pressure is high and the engine fan **must** be engaged. The air conditioning pressure circuit consists of the air conditioning pressure switch signal pin and switch return pin. This circuit is considered “fail safe”, meaning when the circuit is open, the engine fan will be engaged by the electronic control module (ECM).
>
> ### Resistance Check
>
> Locate the air conditioning pressure switch. Remove the electrical connection from the switch. Adjust the multimeter to measure resistance. Touch one multimeter probe to one of the terminals on the switch. Touch the other multimeter probe to the other terminal of the switch.
>
> When the system head pressure is high, the multimeter **must** show an open circuit (100k ohms or more). If the circuit is **not** open, the switch has failed. Refer to the original equipment manufacturer (OEM) troubleshooting and repair manual for replacement procedures.
>
> When the system head pressure is low, the multimeter **must** show a closed circuit (10 ohms or less). If the circuit is **not** closed, the switch has failed. Refer to the OEM troubleshooting and repair manual for replacement procedures. If the resistance value is correct, the switch **must** still be checked for a short circuit to ground.
>
> ### Check for Short Circuit to Ground
>
> When the system head pressure is low, touch one of the multimeter probes to one of the switch terminals. Touch the other probe to chassis ground. The multimeter **must** show an open circuit (100k ohms or more). If the circuit is **not** open, the switch has failed. Refer to the OEM troubleshooting and repair manual for replacement procedures. If the switch passes all of the previous checks, the circuit **must** be checked for an open circuit, a short circuit to ground, a short circuit from pin to pin, and a short circuit to an external voltage source.
