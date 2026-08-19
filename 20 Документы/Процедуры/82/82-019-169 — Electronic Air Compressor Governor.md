---
aliases:
  - "Электронный регулятор воздушного компрессора"
type: "Процедура"
doc: "82-019-169"
title_en: "Electronic Air Compressor Governor"
title_ru: "Электронный регулятор воздушного компрессора"
modified: "2005-01-28"
engines:
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 4
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-169.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-019-169.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# Electronic Air Compressor Governor
**Электронный регулятор воздушного компрессора**

> [!abstract] Процедура · `82-019-169`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section 19 - Electronic Engine Controls
> **Даты:** изменён 2005-01-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-169.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-019-169.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Снятие

> [!danger] ОПАСНО
> Слить баллон воздушного компрессора и все линии перед снятием или установкой воздухоусилителя компрессора. Неспособность слить воздушный компрессор и линии давления может привести к личным травмам, механическим повреждениям или электрическим повреждениям или всему вышеперечисленному.

Поднимите на вкладку и отсоедините разъем от губернатора.

Удалите губернатора из воздушного компрессора.

Проверить губернатора на предмет повреждений.

![[19200315.png]]

### Установка

> [!danger] ОПАСНО
> Слить баллон воздушного компрессора и все линии перед снятием или установкой воздухоусилителя компрессора. Неспособность слить воздушный компрессор и линии давления может привести к личным травмам, механическим повреждениям или электрическим повреждениям или всему вышеперечисленному.

Убедитесь, что новый губернатор имеет кольцо вокруг поверхности, где оно уплотняется против воздушного компрессора.

Установите губернатора на воздушный компрессор.

> [!tip] Момент затяжки
> 14 Н·м [124 фунт-дюйм]

![[19200316.png]]

### Проверка сопротивления

> [!warning] ОСТОРОЖНО
> Не используйте испытуемый щуп, кроме Части № 3822758. Разъём будет повреждён. Лиды должны плотно вписываться в разъем без расширения контактов разъема.

Отсоедините разъем электропроводки привода от ECM. Отсоедините 6-контактный электронный регуляторный разъем от электропроводки двигателя. Вставьте испытательный щуп в контакт 14 разъёма проводов привода и соедините его с многометровым щупом. Вставьте другой испытательный щуп в контакт 5 из 6-контактного электронного регуляторного разъема, проводов двигателя с ремнями безопасности. Подключите свинец к другому многометровому щупу. Установите мультиметр на установку сопротивления и измерьте сопротивление.

Мультиметр **должен** показать замкнутую цепь (10 Ом и менее).

Если цепь ** не** закрыта, отремонтируйте или замените электропроводку двигателя. См. процедуру[[82-019-043-tr — Engine Wiring Harness|019-043]].

![[19c00422.png]]

Включить испытательный щуп в контакт 11 разъёма проводов привода. Вставьте другой испытательный щуп в контакт 6 из 6-контактного электронного регуляторного разъема, проводов двигателя с ремнями безопасности. Измерьте сопротивление.

Мультиметр **должен** показать замкнутую цепь (10 Ом и менее).

Если цепь ** не** закрыта, отремонтируйте или замените электропроводку двигателя. См. процедуру[[82-019-043-tr — Engine Wiring Harness|019-043]].

После ремонта подсоедините все компоненты.

![[19c00423.png]]


> [!quote]- Original (English) · английский оригинал
> ### Remove
>
> **WARNING · Опасно**
> Drain the air compressor tank and all lines before removing or installing the air compressor governor. Failure to drain the air compressor tank and lines of pressure could result in personal injury, mechanical damage, or electrical damage, or all of the above.
>
> Lift up on the tab and disconnect the connector from the governor.
>
> Remove the governor from the air compressor.
>
> Inspect the governor for damage.
>
> ### Install
>
> **WARNING · Опасно**
> Drain the air compressor tank and all lines before removing or installing the air compressor governor. Failure to drain the air compressor tank and lines of pressure could result in personal injury, mechanical damage, or electrical damage, or all of the above.
>
> Make sure the new governor has an o-ring around the surface where it seals against the air compressor.
>
> Install the governor onto the air compressor.
>
> **Момент затяжки · Torque Value**
> 14 n•m [124 in-lb]
>
> ### Resistance Check
>
> **CAUTION · Осторожно**
> Do not use test leads other than Part Number 3822758. The connector will be damaged. The leads must fit tightly into the connector without expanding the connector pins.
>
> Disconnect the actuator harness connector from the ECM. Disconnect the 6-pin electronic governor connector from the engine harness. Insert a test lead into pin 14 of the actuator harness connector, and connect it to the multimeter probe. Insert the other test lead into pin 5 of the 6-pin electronic governor connector, engine harness side. Connect the lead to the other multimeter probe. Set the multimeter to the resistance setting and measure the resistance.
>
> The multimeter **must** show a closed circuit (10 ohms or less).
>
> If the circuit is **not** closed, repair or replace the engine harness. Refer to Procedure [[82-019-043-tr — Engine Wiring Harness|019-043]].
>
> Insert the test lead into pin 11 of the actuator harness connector. Insert the other test lead into pin 6 of the 6-pin electronic governor connector, engine harness side. Measure the resistance.
>
> The multimeter **must** show a closed circuit (10 ohms or less).
>
> If the circuit is **not** closed, repair or replace the engine harness. Refer to Procedure [[82-019-043-tr — Engine Wiring Harness|019-043]].
>
> Connect all components after completing the repair.
