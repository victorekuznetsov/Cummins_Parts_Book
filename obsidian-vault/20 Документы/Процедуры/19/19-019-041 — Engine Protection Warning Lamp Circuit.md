---
aliases:
  - "Цепь лампы предупреждения защиты двигателя"
type: "Процедура"
doc: "19-019-041"
title_en: "Engine Protection Warning Lamp Circuit"
title_ru: "Цепь лампы предупреждения защиты двигателя"
modified: "2002-08-20"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
  - "85017333"
families:
  - "QSK23"
  - "QSK60"
manuals:
  - "3666113"
figures: 4
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-019-041.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-019-041.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
  - "перевод/машинный"
---

# Engine Protection Warning Lamp Circuit
**Цепь лампы предупреждения защиты двигателя**

> [!abstract] Процедура · `19-019-041`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2002-08-20
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-019-041.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-019-041.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Проверка сопротивления

> [!warning] ОСТОРОЖНО
> Чтобы уменьшить вероятность повреждения разъема, не используйте щупы или провода, отличные от Части № 3822758, на разъеме 40-контактной OEM-проводов и Части № 3823993, на разъеме 31-контактной OEM-проводов. Лиды должны плотно помещаться в разъеме без расширения штифтов в разъеме.

Переключатель зажигания транспортного средства в положение выключения. Отключите проводку OEM-интерфейса от ECM. Отсоедините OEM-интерфейс от OEM-проводов на 31-контактном разъеме.

Измерить сопротивление от контакта 2 интерфейса OEM проводов жгута разъёма к контакту 1 31-контактного интерфейса OEM разъема, OEM интерфейса стороны. Мультиметр **должен** показать замкнутую цепь (10 Ом и менее).

Если схема **не** закрыта, отремонтируйте или замените проводку OEM-интерфейса. См. процедуру 019-231, 019-240 или[[19-019-072 — OEM Interface Harness|019-072]].

Проверьте сопротивление OEM-проводов. См. указания изготовителя.

![[19400233.png]]

### Проверка на замыкание на массу

Переключатель зажигания транспортного средства в положение выключения. Отключите проводку OEM-интерфейса от ECM. Отсоедините OEM-интерфейс от OEM-проводов на 31-контактном разъеме.

Измерить сопротивление от контакта 2 интерфейса OEM проводов ремня разъема ECM к блоку двигателя.

Мультиметр **должен** показать обрыв цепи (100 кОм и более). Если схема **не** открыта, отремонтируйте или замените проводку OEM-интерфейса. См. процедуру 019-240 или[[19-019-072 — OEM Interface Harness|019-072]].

Проверьте OEM проводку ремня для короткого замыкания на землю. См. указания изготовителя.

![[19400232.png]]

### Проверка напряжения

Отключите проводку OEM-интерфейса от ECM.

Вставьте один свинец в контакт 2 разъёма OEM-интерфейса.

![[19400230.png]]

Подключите аллигаторный клип к положительному (+) многометровому щупу. Подключите отрицательный (-) многометровый щуп к блоку двигателя. Переключатель зажигания транспортного средства в положение Включения. Установите мультиметр для измерения VDC. Мультиметр **должен** показывать напряжение батареи. Если напряжение батареи **не** присутствует, провод № 2 должен быть проверен на наличие открытого контура или короткого замыкания на землю.

![[19400231.png]]


> [!quote]- Original (English) · английский оригинал
> ### Resistance Check
>
> **CAUTION · Осторожно**
> To reduce the possibility of connector damage, do not use probes or leads other than Part Number 3822758, on the 40-pin OEM harness connector and Part Number 3823993, on the 31-pin OEM harness connector. The leads must fit tightly in the connector without expanding the pins in the connector.
>
> Turn the vehicle keyswitch to the OFF position. Disconnect the OEM interface harness from the ECM. Disconnect the OEM interface harness from the OEM harness at the 31-pin connector.
>
> Measure the resistance from pin 2 of the OEM interface harness connector to pin 1 of the 31-pin OEM interface connector, OEM interface side. The multimeter **must** show a closed circuit (10 ohms or less).
>
> If the circuit is **not** closed, repair or replace the OEM interface harness. Refer to Procedure 019-231, 019-240, or [[19-019-072 — OEM Interface Harness|019-072]].
>
> Check the OEM harness resistance. Refer to the manufacturer's instructions.
>
> ### Check for Short Circuit to Ground
>
> Turn the vehicle keyswitch to the OFF position. Disconnect the OEM interface harness from the ECM. Disconnect the OEM interface harness from the OEM harness at the 31-pin connector.
>
> Measure the resistance from pin 2 of the OEM interface harness ECM connector to the engine block.
>
> The multimeter **must** show an open circuit (100k ohms or more). If the circuit is **not** open, repair or replace the OEM interface harness. Refer to Procedure 019-240 or [[19-019-072 — OEM Interface Harness|019-072]].
>
> Check the OEM harness for a short circuit to ground. Refer to the manufacturer's instructions.
>
> ### Voltage Check
>
> Disconnect the OEM interface harness from the ECM.
>
> Insert one lead into pin 2 of the OEM interface harness connector.
>
> Connect the alligator clip to the positive (+) multimeter probe. Connect the negative (-) multimeter probe to the engine block. Turn the vehicle keyswitch to the ON position. Set the multimeter to measure VDC. The multimeter **must** show battery voltage. If battery voltage is **not** present, wire number 2 **must** be checked for an open circuit or a short circuit to ground.
