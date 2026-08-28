---
aliases:
  - "Цепь лампы предупреждения защиты двигателя"
type: "Процедура"
doc: "87-019-041"
title_en: "Engine Protection Warning Lamp Circuit"
title_ru: "Цепь лампы предупреждения защиты двигателя"
modified: "2003-02-10"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666214"
figures: 6
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-019-041.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-019-041.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
  - "перевод/машинный"
---

# Engine Protection Warning Lamp Circuit
**Цепь лампы предупреждения защиты двигателя**

> [!abstract] Процедура · `87-019-041`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-02-10
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-019-041.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-019-041.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Проверка сопротивления

> [!warning] ОСТОРОЖНО
> Для уменьшения возможности повреждения штифта и проводов жгута проводов используйте измерительный щуп, Номер детали 3823993, на 31-контактном разъеме, и испытательный щуп, Номер детали 3822758, на 50-контактном разъеме, при проведении измерения.

Переключатель зажигания транспортного средства в положение выключения. Отсоедините проводку OEM-интерфейса и электропроводку двигателя от ECM. Отсоедините OEM-проводку от OEM-интерфейса проводов на 31-контактном разъеме.

![[19a00331.png]]

Измерить сопротивление от контакта 4 50-контактного интерфейса проводов упряжки разъёма к контакту 14 31-контактного интерфейса проводов упряжки разъема, интерфейса проводов упряжки стороны. Мультиметр **должен** показать замкнутую цепь (10 Ом и менее).

Если цепь **не** закрыта, отремонтируйте или замените электропроводку двигателя.

См. процедуру 019-231 или[[87-019-250 — Connector, 50-Pin|019-250]]Для ремонта проводов. См. процедуру[[87-019-043 — Engine Wiring Harness|019-043]]Заменить проводку на шнур.

![[19a00331.png]]

### Проверка на замыкание на массу

> [!warning] ОСТОРОЖНО
> Не используйте щупы или испытательные щупы, кроме Части № 3822758. Разъём будет повреждён. Лиды должны плотно помещаться в разъеме без расширения штифтов в разъеме.

Переключатель зажигания транспортного средства в положение выключения. Отсоедините OEM- и электропроводку двигателя от ECM. Отсоедините OEM-проводку от OEM-интерфейса проводов на 31-контактном разъеме.

![[19a00712.png]]

Вставьте измерительный щуп в контакт 4 50-контактного интерфейса проводов жгута разъема, и прикрепите его к многометровому щупу. Прикоснитесь к другому многометровому щупу блока двигателя.

Мультиметр **должен** показать обрыв цепи (100 кОм и более). Если схема **не** открыта, отремонтируйте или замените электропроводку двигателя.

См. процедуру[[87-019-250 — Connector, 50-Pin|019-250]]или[[87-019-043 — Engine Wiring Harness|019-043]].

![[19a00712.png]]

### Проверка напряжения

> [!warning] ОСТОРОЖНО
> Не используйте щупы или провода, отличные от Части № 3822758. Разъём будет повреждён. Лиды должны плотно помещаться в разъеме без расширения штифтов в разъеме.

Отсоедините OEM- и электропроводку двигателя от ECM. Переключатель зажигания транспортного средства в положение Включения. Установите мультиметр для измерения VDC.

Включить испытательный щуп в контакт 4 разъёма проводов OEM-приемника.

![[19a00332.png]]

Подключите аллигаторный клип к положительному (+) многометровому щупу. Прикоснитесь к отрицательному (-) многометровому щупу блока двигателя. Измерьте напряжение. Мультиметр **должен** показывать напряжение батареи.

Если напряжение батареи **не** присутствует, провод 4 должен быть проверен на наличие открытого контура или короткого замыкания на землю.

![[19a00332.png]]


> [!quote]- Original (English) · английский оригинал
> ### Resistance Check
>
> **CAUTION · Осторожно**
> To reduce the possibility of pin and harness damage, use test lead, Part Number 3823993, on the 31-pin connector, and test lead, Part Number 3822758, on the 50-pin connector, when taking a measurement.
>
> Turn the vehicle keyswitch to the OFF position. Disconnect the OEM interface harness and the engine harness from the ECM. Disconnect the OEM harness from the OEM interface harness at the 31-pin connector.
>
> Measure the resistance from pin 4 of the 50-pin OEM interface harness connector to pin 14 of the 31-pin OEM interface harness connector, interface harness side. The multimeter **must** show a closed circuit (10 ohms or less).
>
> If the circuit is **not** closed, repair or replace the engine harness.
>
> Refer to Procedure 019-231 or [[87-019-250 — Connector, 50-Pin|019-250]] to repair the harness. Refer to Procedure [[87-019-043 — Engine Wiring Harness|019-043]] to replace the harness.
>
> ### Check for Short Circuit to Ground
>
> **CAUTION · Осторожно**
> Do not use probes or test leads other than Part Number 3822758. The connector will be damaged. The leads must fit tightly in the connector without expanding the pins in the connector.
>
> Turn the vehicle keyswitch to the OFF position. Disconnect the OEM and engine harnesses from the ECM. Disconnect the OEM harness from the OEM interface harness at the 31-pin connector.
>
> Insert the test lead into pin 4 of the 50-pin OEM interface harness connector, and attach it to the multimeter probe. Touch the other multimeter probe to the engine block.
>
> The multimeter **must** show an open circuit (100k ohms or more). If the circuit is **not** open, repair or replace the engine harness.
>
> Refer to Procedure [[87-019-250 — Connector, 50-Pin|019-250]] or [[87-019-043 — Engine Wiring Harness|019-043]].
>
> ### Voltage Check
>
> **CAUTION · Осторожно**
> Do not use probes or leads other than Part Number 3822758. The connector will be damaged. The leads must fit tightly in the connector without expanding the pins in the connector.
>
> Disconnect the OEM and engine harnesses from the ECM. Turn the vehicle keyswitch to the ON position. Set the multimeter to measure VDC.
>
> Insert a test lead into pin 4 of the OEM harness connector.
>
> Connect the alligator clip to the positive (+) multimeter probe. Touch the negative (-) multimeter probe to the engine block. Measure the voltage. The multimeter **must** show battery voltage.
>
> If battery voltage is **not** present, wire 4 **must** be checked for an open circuit or a short circuit to ground.
