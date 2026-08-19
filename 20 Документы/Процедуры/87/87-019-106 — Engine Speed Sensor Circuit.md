---
aliases:
  - "Цепь датчика частоты вращения двигателя"
type: "Процедура"
doc: "87-019-106"
title_en: "Engine Speed Sensor Circuit"
title_ru: "Цепь датчика частоты вращения двигателя"
modified: "2003-02-10"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666214"
figures: 9
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-019-106.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-019-106.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
  - "перевод/машинный"
---

# Engine Speed Sensor Circuit
**Цепь датчика частоты вращения двигателя**

> [!abstract] Процедура · `87-019-106`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-02-10
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-019-106.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-019-106.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Проверка сопротивления

> [!warning] ОСТОРОЖНО
> Не используйте щупы или испытательные щупы, кроме Части № 3822758. Разъём будет повреждён. Лиды должны плотно помещаться в разъеме без расширения штифтов разъема.

Отсоедините разъем жгута проводов двигателя от ECM.

Вставьте штыревой штифт одного из выводов в контакт 17 разъема проводов двигателя. Вставьте штыревой штифт другого свинца в контакт 18 разъёма.

![[19a00169.png]]

Убедитесь, что датчик скорости двигателя подключен к электропроводке двигателя.

Подключите аллигаторы к многометровым зондам. Измерьте сопротивление. Значение сопротивления ** должно быть от 1000 до 2000 Ом.

Если сопротивление ** не** правильно, возникает проблема с проводкой двигателя, при условии, что датчик был предварительно проверен.

![[19a00170.png]]

### Проверка на замыкание на массу

> [!warning] ОСТОРОЖНО
> Не используйте щупы или испытательные щупы, кроме Части № 3822758. Разъём будет повреждён. Лиды должны плотно помещаться в разъеме без расширения штифтов разъема.

Отсоедините разъем жгута проводов двигателя от ECM. Вставьте испытательный щуп в контакт 17 разъема ремня электропроводки двигателя и соедините зажим аллигатора с многометровым щупом. Прикоснитесь к другому многометровому щупу блока двигателя. Измерьте сопротивление.

Мультиметр ** должен** показывать открытую схему (более 100k ом).

![[19900538.png]]

Удалите свинец из контакта 17 и вставьте его в контакт 8 разъёма ремня электропроводки двигателя. Прикоснитесь к другому многометровому щупу блока двигателя. Измерьте сопротивление.

Мультиметр ** должен** показывать открытую схему (более 100k ом).

![[19a00721.png]]

### Проверка на замыкание между контактами

> [!warning] ОСТОРОЖНО
> Не используйте щупы или испытательные щупы, кроме Части № 3822758. Разъём будет повреждён. Лиды должны плотно помещаться в разъеме без расширения штифтов разъема.

Отсоедините датчик скорости двигателя от датчика проводов ремня. Отсоедините разъем жгута проводов двигателя и разъем жгута OEM-интерфейса от ECM. Включить испытательный щуп в контакт 8 разъёма ремня электропроводки двигателя. Вставьте другой испытательный щуп в контакт 1 разъёма. Подключите аллигаторы к многометровым зондам. Измерьте сопротивление. Мультиметр **должен** показать обрыв цепи (100 кОм и более).

![[19a00722.png]]

Измерьте сопротивление от контакта 8 ко всем другим штифтам разъема жгута электропроводки двигателя. Мультиметр ** должен** показывать открытую схему (более 100k ом) на всех штифтах.

Затем повторите проверку контакта с контактом от контакта 8 разъёма жгутов проводов двигателя ко всем штифтам разъёма ремней OEM-интерфейса. Мультиметр ** должен** показывать открытую схему (100к Ом или более) на всех штифтах.

![[19a00723.png]]

Измерьте сопротивление от контакта 17 разъёма ремня электропроводки двигателя со всеми штифтами разъёма. Мультиметр ** должен** показывать открытую схему (более 100k ом) на всех штифтах.

Затем повторите проверку контакта с контактом от контакта 17 разъёма жгутов проводов двигателя ко всем штифтам разъёма ремней OEM-интерфейса. Мультиметр **должен** показать обрыв цепи (100 кОм и более).

![[19a00724.png]]

Удалите свинец из контакта 17 разъёма ремня электропроводки двигателя и вставьте его в контакт 18. Измерьте сопротивление от контакта 18 разъёма ремня электропроводки двигателя со всеми другими штифтами разъёма.

Мультиметр ** должен** показывать открытую схему (более 100k ом) на всех штифтах.

Затем повторите проверку контакта с контактом от контакта 18 разъёма жгутов проводов двигателя ко всем штифтам разъёма жгутов проводов OEM-интерфейса. Мультиметр **должен** показать обрыв цепи (100 кОм и более).

![[19a00726.png]]

Если значения сопротивления в любой из предыдущих проверок находятся в пределах спецификации, то существует короткое замыкание от контакта 8, 17 или 18 до любого штифта, который измеряется менее 100k Ом. Ремонт или замена ремня электропроводки двигателя.

См. процедуру[[87-019-250 — Connector, 50-Pin|019-250]]или[[87-019-043 — Engine Wiring Harness|019-043]].

![[19a00726.png]]


> [!quote]- Original (English) · английский оригинал
> ### Resistance Check
>
> **CAUTION · Осторожно**
> Do not use probes or test leads other than Part Number 3822758. The connector will be damaged. The leads must fit tightly in the connector without expanding the pins of the connector.
>
> Disconnect the engine harness connector from the ECM.
>
> Insert the male pin of one of the leads into pin 17 of the engine harness connector. Insert the male pin of the other lead into pin 18 of the connector.
>
> Make sure the engine speed sensor is connected to the engine harness.
>
> Connect the alligator clips to the multimeter probes. Measure the resistance. The resistance value **must** be 1000 to 2000 ohms.
>
> If the resistance is **not** correct, there is a problem with the engine harness, provided the sensor was previously checked.
>
> ### Check for Short Circuit to Ground
>
> **CAUTION · Осторожно**
> Do not use probes or test leads other than Part Number 3822758. The connector will be damaged. The leads must fit tightly in the connector without expanding the pins of the connector.
>
> Disconnect the engine harness connector from the ECM. Insert the test lead into pin 17 of the engine harness connector, and connect the alligator clip to the multimeter probe. Touch the other multimeter probe to the engine block. Measure the resistance.
>
> The multimeter **must** show an open circuit (more than 100k ohms).
>
> Remove the lead from pin 17 and insert it into pin 8 of the engine harness connector. Touch the other multimeter probe to the engine block. Measure the resistance.
>
> The multimeter **must** show an open circuit (more than 100k ohms).
>
> ### Check for Short Circuit from Pin to Pin
>
> **CAUTION · Осторожно**
> Do not use probes or test leads other than Part Number 3822758. The connector will be damaged. The leads must fit tightly in the connector without expanding the pins of the connector.
>
> Disconnect the engine speed sensor from the sensor harness. Disconnect the engine harness connector and OEM interface harness connector from the ECM. Insert a test lead into pin 8 of the engine harness connector. Insert the other test lead into pin 1 of the connector. Connect the alligator clips to the multimeter probes. Measure the resistance. The multimeter **must** show an open circuit (100k ohms or more).
>
> Measure the resistance from pin 8 to all other pins of the engine harness connector. The multimeter **must** show an open circuit (more than 100k ohms) at all pins.
>
> Then, repeat the pin-to-pin check from pin 8 of the engine harness connector to all pins of the OEM interface harness connector. The multimeter **must** show an open circuit (100k ohms or more) at all pins.
>
> Measure the resistance from pin 17 of the engine harness connector to all pins of the connector. The multimeter **must** show an open circuit (more than 100k ohms) at all pins.
>
> Then, repeat the pin-to-pin check from pin 17 of the engine harness connector to all pins of the OEM interface harness connector. The multimeter **must** show an open circuit (100k ohms or more).
>
> Remove the lead from pin 17 of the engine harness connector and insert it into pin 18. Measure the resistance from pin 18 of the engine harness connector to all other pins of the connector.
>
> The multimeter **must** show an open circuit (more than 100k ohms) at all pins.
>
> Then, repeat the pin-to-pin check from pin 18 of the engine harness connector to all pins of the OEM interface harness connector. The multimeter **must** show an open circuit (100k ohms or more).
>
> If the resistance values in any of the previous checks are **not** within specification, there is a short circuit from pin 8, 17, or 18 to any pin that measured less than 100k ohms. Repair or replace the engine harness.
>
> Refer to Procedure [[87-019-250 — Connector, 50-Pin|019-250]] or [[87-019-043 — Engine Wiring Harness|019-043]].
