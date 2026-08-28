---
aliases:
  - "Цепь датчика частоты вращения двигателя"
type: "Процедура"
doc: "94-019-106"
title_en: "Engine Speed Sensor Circuit"
title_ru: "Цепь датчика частоты вращения двигателя"
modified: "2003-03-24"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666184"
figures: 6
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/94/94-019-106.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/94-019-106.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/94"
  - "перевод/машинный"
---

# Engine Speed Sensor Circuit
**Цепь датчика частоты вращения двигателя**

> [!abstract] Процедура · `94-019-106`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual|3666184]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-03-24
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/94/94-019-106.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/94-019-106.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Проверка сопротивления

> [!warning] ОСТОРОЖНО
> Не используйте ни пробы, ни зацепки, кроме Части Нет. 3822758. Разъём будет повреждён. Лиды должны плотно вписываться в разъем без расширения штифтов разъема.

Вставьте один из выводов в контакт 21 провода двигателя с помощью адаптера ремня разъёма кабеля. Вставьте другой свинец в контакт 22.

![[19a00064.png]]

Убедитесь, что ESS подключен к проводах датчика.

Измерьте сопротивление. Значение сопротивления **должно быть менее 1500 Ом. Если сопротивление **не правильно, возникает проблема с проводкой двигателя, при условии, что датчик был предварительно проверен. См. Процедуры 019-202,[[94-019-240 — Connector, 40-Pin|019-240]]и[[94-019-043 — Engine Wiring Harness|019-043]].

![[19a00063.png]]

### Проверка на замыкание на массу

Отсоедините проводку двигателя от адаптера ремня от ECM.

Вставьте свинец в контакт 21. Прикоснитесь к другому многометровому щупу к блоку двигателя. Измерьте сопротивление. Мультиметр **должен** показывать открытую схему (более 100k ом).

![[19a00065.png]]

Удалите свинец из контакта 21 и поместите его в контакт 22. Прикоснитесь к другому многометровому щупу к блоку двигателя. Измерьте сопротивление. Мультиметр **должен** показывать открытую схему (более 100k ом).

Если значения сопротивления в любой из предыдущих проверок **не** в пределах спецификации, то есть короткое замыкание на землю, при условии, что датчик ESS был ранее проверен. Ремонт или замена ремня электропроводки двигателя. См. процедуру 019-199,[[94-019-240 — Connector, 40-Pin|019-240]]или[[94-019-043 — Engine Wiring Harness|019-043]].

![[19a00065.png]]

### Проверка на замыкание между контактами

Отсоедините проводку двигателя от адаптера ремня от ECM. Вставьте один из мультиметров, ведущих в контакт 21. Проверьте сопротивление всем штифтам в разъеме. Мультиметр **должен** показывать открытую схему (более 100k ом).

![[19a00029.png]]

Удалите свинец из контакта 21 и поместите его в контакт 22, и снова проверьте сопротивление всем штифтам в разъеме. Мультиметр **должен** показывать открытую схему (более 100k ом) на всех штифтах.

Если значения сопротивления в любой из предыдущих проверок находятся **не** в пределах спецификации, то существует короткое замыкание от контактов 21 или 22 до любого штифта, который измеряет менее 100k Ом. Ремонт или замена ремня электропроводки двигателя. См. Процедуры 019-199,[[94-019-240 — Connector, 40-Pin|019-240]]или[[94-019-043 — Engine Wiring Harness|019-043]].

![[19a00029.png]]


> [!quote]- Original (English) · английский оригинал
> ### Resistance Check
>
> **CAUTION · Осторожно**
> Do not use probes or leads other than Part No. 3822758. The connector will be damaged. The leads must fit tight in the connector without expanding the pins of the connector.
>
> Insert the one of the leads into pin 21 of the engine harness adaptor cable connector. Insert the other lead into pin 22.
>
> Make sure the ESS is connected to the sensor harness.
>
> Measure the resistance. The resistance value **must** be less than 1500 ohms. If the resistance is **not** correct, there is a problem with the engine harness, provided the sensor was previously checked. Refer to Procedures 019-202, [[94-019-240 — Connector, 40-Pin|019-240]], and [[94-019-043 — Engine Wiring Harness|019-043]].
>
> ### Check for Short Circuit to Ground
>
> Disconnect the engine harness adaptor cable from the ECM.
>
> Insert the lead into pin 21. Touch the other Multimeter probe to the engine block. Measure the resistance. The Multimeter **must** show an open circuit (more than 100k ohms).
>
> Remove the lead from pin 21 and place it into pin 22. Touch the other Multimeter probe to the engine block. Measure the resistance. The Multimeter **must** show an open circuit (more than 100k ohms).
>
> If the resistance values in any of the previous checks are **not** within the specification, there is a short circuit to ground, provided the ESS sensor has been previously checked. Repair or replace the engine harness. Refer to Procedure 019-199, [[94-019-240 — Connector, 40-Pin|019-240]] or [[94-019-043 — Engine Wiring Harness|019-043]].
>
> ### Check for Short Circuit from Pin to Pin
>
> Disconnect the engine harness adaptor cable from the ECM. Insert one of the multimeter leads into pin 21. Check the resistance to all pins in the connector. The multimeter **must** show an open circuit (more than 100k ohms).
>
> Remove the lead from pin 21 and place it into pin 22, and again check the resistance to all pins in the connector. The multimeter **must** show an open circuit (more than 100k ohms) at all pins.
>
> If the resistance values in any of the previous checks are **not** within specification, there is a short circuit from pins 21 or 22 to any pin that measures less than 100k ohms. Repair or replace the engine harness. Refer to Procedures 019-199, [[94-019-240 — Connector, 40-Pin|019-240]], or [[94-019-043 — Engine Wiring Harness|019-043]].
