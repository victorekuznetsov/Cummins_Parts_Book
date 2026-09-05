---
aliases:
  - "Цепь датчика частоты вращения двигателя"
type: "Процедура"
doc: "98-019-106"
title_en: "Engine Speed Sensor Circuit"
title_ru: "Цепь датчика частоты вращения двигателя"
modified: "2004-05-14"
engines:
  - "37269910"
  - "37280605"
families:
  - "K19"
manuals:
  - "3666070"
figures: 8
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-019-106.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-019-106.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K19"
  - "группа/98"
  - "перевод/машинный"
---

# Engine Speed Sensor Circuit
**Цепь датчика частоты вращения двигателя**

> [!abstract] Процедура · `98-019-106`
> **Двигатели:** [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]]
> **Семейство:** K19
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2004-05-14
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-019-106.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-019-106.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Проверка сопротивления

Отсоедините главный разъём электропроводки двигателя от ECM.

Убедитесь, что датчик скорости двигателя подключен к основной проводах двигателя.

![[19801636.png]]

Прикосновение к одному из мультиметров приводит к контакту 4 главного разъёма проводов двигателя. Прикосновение к другому мультиметру приводит к контакту 17 главного разъёма проводов двигателя.

![[19801637.png]]

Измерьте сопротивление.

Мультиметр должен измерять от 750 до 1500 Ом. Если измеренное сопротивление не попадает в этот диапазон, то возникает проблема с основной проводкой двигателя, при условии, что датчик скорости двигателя уже проверен и хорош. Ремонт или замена основного двигателя проводов жгута. См. процедуру 019-228 или[[98-019-043 — Engine Wiring Harness|019-043]].

Сгибайте проводку мягко при проверке схемы, чтобы проверить наличие прерывистых открытых цепей.

![[19801638.png]]

Повторите вышеупомянутую проверку сопротивления для измерения сопротивления между контактом 18 и контактом 24 главного разъёма ремня электропроводки двигателя.

Прикосновение к одному из мультиметров приводит к контакту 18 главного разъёма проводов двигателя. Прикосновение к другому мультиметру приводит к контакту 24 главного разъёма проводов двигателя.

Мультиметр должен измерять от 750 до 1500 Ом.

![[19801639.png]]

Разделите два разъема. Поднимите вкладку на разъемы и разберите их.

При измерении значений сопротивления катушек датчика скорости двигателя подключите спаривающийся разъем с короткими свинцовыми удлинителями. Это позволит мягко сгибать электрические провода датчика для проверки поврежденных или частично сломанных резьб провода под изоляцией.

![[19801627.png]]

### Проверка на замыкание между контактами

Проверьте короткое замыкание между контактом 4 главного разъёма проводов двигателя и **всеми **другими контактами в разъеме**, за исключением **контакта 17.

Прикосновение к одному из мультиметров приводит к контакту 4 разъема. Прикосновение к другому мультиметру приводит к **всем **другим штифтам в разъеме**, за исключением **контакта 17, по одному за раз.

![[19801640.png]]

Измерьте сопротивление.

Мультиметр **должен **показывать более 100k ом, что является открытой схемой. Если схема **не** открыта, то между проводами, подключенными к контакту 4 главного разъёма проводов двигателя, и любым другим штифтом, который измеряется менее 100k Ом.

Ремонт или замена основного двигателя проводов жгута. См. процедуру 019-228 и процедуру[[98-019-043 — Engine Wiring Harness|019-043]].

![[19801621.png]]

Повторите вышеупомянутую процедуру, чтобы проверить короткое замыкание между контактом 24 главного разъёма проводов двигателя и **всеми **другими контактами в разъеме**, за исключением **контакта 18.

Прикосновение к одному из мультиметров приводит к контакту 24 разъема. Прикосновение к другому мультиметру приводит к **всем **другим штифтам в разъеме**, за исключением **контакта 18, по одному за раз.

Измерьте сопротивление. Мультиметр **должен **показывать более 100k ом.

![[19801642.png]]


> [!quote]- Original (English) · английский оригинал
> ### Resistance Check
>
> Disconnect the main engine harness connector from the ECM.
>
> Make sure the engine speed sensor is connected to the main engine harness.
>
> Touch one of the multimeter leads to pin 4 of the main engine harness connector. Touch the other multimeter lead to pin 17 of the main engine harness connector.
>
> Measure the resistance.
>
> The multimeter **must** measure between 750 and 1500 ohms. If the measured resistance does **not** fall within this range, then there is a problem with the main engine harness, provided that the engine speed sensor has already been checked and is good. Repair or replace the main engine harness. Refer to Procedure 019-228 or [[98-019-043 — Engine Wiring Harness|019-043]].
>
> Flex the harness softly when checking the circuit to check for intermittent open circuits.
>
> Repeat the above resistance check to measure the resistance between pin 18 and pin 24 of the main engine harness connector.
>
> Touch one of the multimeter leads to pin 18 of the main engine harness connector. Touch the other multimeter lead to pin 24 of the main engine harness connector.
>
> The multimeter **must** measure between 750 and 1500 ohms.
>
> Separate the two connectors. Lift the tab on the connectors and pull them apart.
>
> When measuring the resistance values of the engine speed sensor coils, connect a mating connector with short lead extensions. This will allow the electrical leads of the sensor to be softly flexed to check for damaged or partially broken wire strands under the insulation.
>
> ### Check for Short Circuit from Pin to Pin
>
> Check for a short circuit between pin 4 of the main engine harness connector and **all** other pins in the connector **except** pin 17.
>
> Touch one of the multimeter leads to pin 4 of the connector. Touch the other multimeter lead to **all** other pins in the connector **except** pin 17, one at a time.
>
> Measure the resistance.
>
> The multimeter **must** show more than 100k ohms, which is an open circuit. If the circuit is **not** open, then there is a short between the wires connected to pin 4 of the main engine harness connector and any other pin that measured less than 100k ohms.
>
> Repair or replace the main engine harness. Refer to Procedure 019-228 and Procedure [[98-019-043 — Engine Wiring Harness|019-043]].
>
> Repeat the above procedure to check for a short circuit between pin 24 of the main engine harness connector and **all** other pins in the connector **except** pin 18.
>
> Touch one of the multimeter leads to pin 24 of the connector. Touch the other multimeter lead to **all** other pins in the connector **except** pin 18, one at a time.
>
> Measure the resistance. The multimeter **must** show more than 100k ohms.
