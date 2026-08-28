---
aliases:
  - "Цепь датчика частоты вращения двигателя"
type: "Процедура"
doc: "07-019-106"
title_en: "Engine Speed Sensor Circuit"
title_ru: "Цепь датчика частоты вращения двигателя"
modified: "2003-12-01"
engines:
  - "93058669"
  - "93087701"
families:
  - "C8.3 · 6C8.3"
manuals:
  - "4021442"
figures: 3
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-019-106.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/07-019-106.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "группа/07"
  - "перевод/машинный"
---

# Engine Speed Sensor Circuit
**Цепь датчика частоты вращения двигателя**

> [!abstract] Процедура · `07-019-106`
> **Двигатели:** [[93058669 — 6C8.3 CPL 3105|93058669]], [[93087701 — 6C8.3 CPL 3105|93087701]]
> **Семейство:** C8.3 · 6C8.3
> **Входит в руководства:** [[4021442 — C8.3 Marine Electronic Control System Troubleshooting and Repair Manual|4021442]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-12-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-019-106.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/07-019-106.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Проверка сопротивления

> [!warning] ОСТОРОЖНО
> Не используйте щупы или испытательные щупы, кроме Части 3822758, иначе разъем будет поврежден. Лиды должны плотно помещаться в разъеме без расширения штифтов разъема.

Отсоедините разъем жгута проводов двигателя от электронного модуля управления (ECM).

Вставьте штыревой штифт одного из выводов в сигнальный первичный штифт разъема жгута двигателя.

Вставьте штыревой штифт другого свинца в спинку двигателя с обратной скоростью основного штифта разъёма проводов двигателя.

Убедитесь, что датчик скорости двигателя подключен к электропроводке двигателя.

Подключите аллигаторы к многометровым зондам.

Измерьте сопротивление.

Значение сопротивления должно быть от 1000 до 2000 Ом.

Если сопротивление **не** правильно, возникает проблема с проводкой двигателя, при условии проверки датчика.

Вставьте штыревой штифт одного из выводов в сигнальный вторичный штифт разъема жгута двигателя.

Вставьте штыревой штифт другого свинца в двигатель, возвращающий основной штифт разъема.

Убедитесь, что датчик скорости двигателя подключен к электропроводке двигателя.

Подключите аллигаторы к многометровым зондам.

Измерьте сопротивление.

Значение сопротивления должно быть от 1000 до 2000 Ом.

Если сопротивление **не** правильно, возникает проблема с проводкой двигателя, при условии проверки датчика.

![[19901383.png]]

### Проверка на замыкание на массу

> [!warning] ОСТОРОЖНО
> Не используйте щупы или испытательные щупы, кроме Части 3822758, иначе разъем будет поврежден. Лиды должны плотно помещаться в разъеме без расширения штифтов разъема.

Отсоедините разъем жгута проводов двигателя от ECM.

Вставьте испытательный щуп в сигнал о движении двигателя первичный штифт разъема проводов двигателя и соедините зажим аллигатора с многометровым щупом.

Прикоснитесь к другому многометровому щупу блока двигателя.

Измерьте сопротивление.

Мультиметр **должен** показывать открытую схему (более 100k ом).

Удалите свинец из первичного штифта сигнала скорости двигателя и вставьте его во вторичный штифт сигнала скорости двигателя разъёма проводов двигателя.

Прикоснитесь к другому многометровому щупу блока двигателя.

Измерьте сопротивление.

Мультиметр **должен** показывать открытую схему (более 100k ом).

Удалите свинец из сигнала о скорости двигателя и вставьте его в основной штифт двигателя +5 VDC разъема проводов двигателя.

Прикоснитесь к другому многометровому щупу блока двигателя.

Измерьте сопротивление.

Мультиметр **должен** показывать открытую схему (более 100k ом).

![[19901407.png]]

### Проверка на замыкание между контактами

> [!warning] ОСТОРОЖНО
> Не используйте щупы или испытательные щупы, кроме Части 3822758, иначе разъем будет поврежден. Лиды должны плотно помещаться в разъеме без расширения штифтов разъема.

Отсоедините датчик скорости двигателя от датчика проводов ремня.

Отсоедините разъем жгута проводов двигателя от ECM.

Включить испытательный щуп в число оборотов двигателя +5 VDC первичного штифта разъема жгута проводов двигателя.

Вставьте другой испытательный щуп во все другие штифты разъема последовательно.

Подключите аллигаторы к многометровым зондам.

Измерьте сопротивление.

Мультиметр **должен** показывать открытую схему (100к Ом или более) в каждом случае.

Измерьте сопротивление от сигнала о скорости двигателя первичного штифта разъема жгута двигателя ко всем штифтам разъема.

Мультиметр **должен** показывать открытую схему (более 100k ом) на всех штифтах.

Удалите свинец из сигнала о движении двигателя первичного штифта разъёма проводов двигателя и вставьте его в обратный первичный штифт скорости двигателя.

Измерьте сопротивление от оборота двигателя возврата первичного штифта проводов двигателя жгута разъема ко всем другим штифтам разъема.

Мультиметр **должен** показывать открытую схему (более 100k ом) на всех штифтах.

Если значения сопротивления в любой из предыдущих проверок находятся **не** в заданных пределах, то происходит короткое замыкание от первичного штифта двигателя +5 VDC, первичного штифта сигнала скорости двигателя или возврата первичного штифта скорости двигателя к любому штифту, который измеряется менее 100k Ом.

Ремонт или замена ремня электропроводки двигателя.

См. процедуру[[07-019-043 — Engine Wiring Harness|019-043]]или[[99-019-204 — Deutsch DRC Connector Series|019-204]].

![[19901415.png]]


> [!quote]- Original (English) · английский оригинал
> ### Resistance Check
>
> **CAUTION · Осторожно**
> Do not use probes or test leads other than Part Number 3822758 or the connector will be damaged. The leads must fit tightly in the connector without expanding the pins of the connector.
>
> Disconnect the engine harness connector from the electronic control module (ECM).
>
> Insert the male pin of one of the leads into the engine speed signal primary pin of the engine harness connector.
>
> Insert the male pin of the other lead into the engine speed return primary pin of the engine harness connector.
>
> Make sure the engine speed sensor is connected to the engine harness.
>
> Connect the alligator clips to the multimeter probes.
>
> Measure the resistance.
>
> The resistance value **must** be 1000 to 2000 ohms.
>
> If the resistance is **not** correct, there is a problem with the engine harness, provided the sensor was checked.
>
> Insert the male pin of one of the leads into the engine speed signal secondary pin of the engine harness connector.
>
> Insert the male pin of the other lead into the engine speed return primary pin of the connector.
>
> Make sure the engine speed sensor is connected to the engine harness.
>
> Connect the alligator clips to the multimeter probes.
>
> Measure the resistance.
>
> The resistance value **must** be 1000 to 2000 ohms.
>
> If the resistance is **not** correct, there is a problem with the engine harness, provided the sensor was checked.
>
> ### Check for Short Circuit to Ground
>
> **CAUTION · Осторожно**
> Do not use probes or test leads other than Part Number 3822758 or the connector will be damaged. The leads must fit tightly in the connector without expanding the pins of the connector.
>
> Disconnect the engine harness connector from the ECM.
>
> Insert the test lead into the engine speed signal primary pin of the engine harness connector and connect the alligator clip to the multimeter probe.
>
> Touch the other multimeter probe to the engine block.
>
> Measure the resistance.
>
> The multimeter **must** show an open circuit (more than 100k ohms).
>
> Remove the lead from the engine speed signal primary pin and insert it into the engine speed signal secondary pin of the engine harness connector.
>
> Touch the other multimeter probe to the engine block.
>
> Measure the resistance.
>
> The multimeter **must** show an open circuit (more than 100k ohms).
>
> Remove the lead from the engine speed signal secondary pin and insert it into the engine speed +5 VDC primary pin of the engine harness connector.
>
> Touch the other multimeter probe to the engine block.
>
> Measure the resistance.
>
> The multimeter **must** show an open circuit (more than 100k ohms).
>
> ### Check for Short Circuit from Pin to Pin
>
> **CAUTION · Осторожно**
> Do not use probes or test leads other than Part Number 3822758 or the connector will be damaged. The leads must fit tightly in the connector without expanding the pins of the connector.
>
> Disconnect the engine speed sensor from the sensor harness.
>
> Disconnect the engine harness connector from the ECM.
>
> Insert a test lead into the engine speed +5 VDC primary pin of the engine harness connector.
>
> Insert the other test lead into all other pins of the connector in succession.
>
> Connect the alligator clips to the multimeter probes.
>
> Measure the resistance.
>
> The multimeter **must** show an open circuit (100k ohms or more) in each case.
>
> Measure the resistance from the engine speed signal primary pin of the engine harness connector to all pins of the connector.
>
> The multimeter **must** show an open circuit (more than 100k ohms) at all pins.
>
> Remove the lead from the engine speed signal primary pin of the engine harness connector and insert it into the engine speed return primary pin.
>
> Measure the resistance from the engine speed return primary pin of the engine harness connector to all other pins of the connector.
>
> The multimeter **must** show an open circuit (more than 100k ohms) at all pins.
>
> If the resistance values in any of the previous checks are **not** within specification, there is a short circuit from the engine speed +5 VDC primary pin, the engine speed signal primary pin, or the engine speed return primary pin to any pin that measured less than 100k ohms.
>
> Repair or replace the engine harness.
>
> Refer to Procedure [[07-019-043 — Engine Wiring Harness|019-043]] or [[99-019-204 — Deutsch DRC Connector Series|019-204]].
