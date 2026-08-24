---
aliases:
  - "Цепь выключателя «холостой ход/номинал»"
type: "Процедура"
doc: "94-019-096"
title_en: "Idle Rated Switch Circuit"
title_ru: "Цепь выключателя «холостой ход/номинал»"
modified: "2003-03-24"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666184"
figures: 5
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/94/94-019-096.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/94-019-096.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/94"
  - "перевод/машинный"
---

# Idle Rated Switch Circuit
**Цепь выключателя «холостой ход/номинал»**

> [!abstract] Процедура · `94-019-096`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual|3666184]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-03-24
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/94/94-019-096.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/94-019-096.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Проверка сопротивления

> [!warning] ОСТОРОЖНО
> Не используйте ни пробы, ни зацепки, кроме Части Нет. 3822758. Разъём будет повреждён. Лиды должны плотно вписываться в разъем без расширения штифтов в разъеме.

Включить испытательный щуп в контакт 3 разъёма проводов OEM-приемника.

Измерьте сопротивление от контакта 3 до заземления блока двигателя.

![[19a00055.png]]

Переместить Idle/Rated в положение IDLE. Мультиметр **должен** показать замкнутую цепь (10 Ом и менее).

Если схема ** не ** закрыта, проверьте наличие открытой схемы в проводах переключателя Idle / Rated.

Переместите переключатель в положение «Рейтинг». Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Если схема ** не** открыта, отремонтируйте или замените проводку OEM-системы при условии, что выключатель был ранее проверен. См. OEM устранение неполадок и процедуры ремонта.

![[19a00056.png]]

### Проверка на замыкание на массу

Поместите Idle/Rated в положение RATED.

Удалите разъём OEM-проводов из ECM.

Используйте измерительный щуп, номер детали. 3822758, и измеряют сопротивление от контакта 3 проводов OEM-разъема с землей.

![[19a00057.png]]

Мультиметр **должен** показать обрыв цепи (100 кОм и более). Если схема **не** открыта, в схеме переключателя Idle/Rated имеется короткое замыкание при условии, что диагностический переключатель Idle/Rated ранее был проверен.

Ремонт или замена OEM проводов жгута, обратитесь к OEM устранение неполадок и процедур ремонта.

![[19a00058.png]]

### Проверка на замыкание между контактами

Удалите разъём жгута проводов двигателя из ECM.

Переместить Idle/Rated в положение RATED.

Используйте измерительный щуп, номер детали. 3822758, и измеряют сопротивление от контакта 3 разъёма OEM-проводов жгута проводов к любому другому штифту в разъёме. Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Если мультиметр не показывает открытую точку, между контактом 3 и любым штифтом, показанным менее 100k Ом, существует короткое замыкание. Ремонт или замена проводной упряжки OEM, обратитесь к процедурам устранения неполадок и ремонта OEM.

![[19a00059.png]]


> [!quote]- Original (English) · английский оригинал
> ### Resistance Check
>
> **CAUTION · Осторожно**
> Do not use probes or leads other than Part No. 3822758. The connector will be damaged. The leads must fit tight in the connector without expanding the pins in the connector.
>
> Insert the test lead into pin 3 of the OEM harness connector.
>
> Measure the resistance from pin 3 to engine block ground.
>
> Move the Idle/Rated switch to the IDLE position. The multimeter **must** show a closed circuit (10 ohms or less).
>
> If the circuit is **not** closed, check for an open circuit in the Idle/Rated switch wiring.
>
> Move the switch to the “Rated” position. The multimeter **must** show an open circuit (100k ohms or more).
>
> If the circuit is **not** open, repair or replace the OEM harness, provided the switch has previously been checked. Refer to OEM Troubleshooting and Repair Procedures.
>
> ### Check for Short Circuit to Ground
>
> Place the Idle/Rated switch in the RATED position.
>
> Remove the OEM harness connector from the ECM.
>
> Use test lead, Part No. 3822758, and measure the resistance from pin 3 of the OEM harness connector to ground.
>
> The multimeter **must** show an open circuit (100k ohms or more). If the circuit is **not** open, there is a short circuit in the Idle/Rated switch circuit, provided the diagnostic Idle/Rated switch has been previously checked.
>
> Repair or replace OEM harness, refer to OEM Troubleshooting and Repair Procedures.
>
> ### Check for Short Circuit from Pin to Pin
>
> Remove the engine harness connector from the ECM.
>
> Move the Idle/Rated switch to the RATED position.
>
> Use test lead, Part No. 3822758, and measure the resistance from pin 3 of the OEM harness connector to every other pin in the connector. The multimeter **must** show an open circuit (100k ohms or more).
>
> If the multimeter does not show an open, a short circuit exists between pin 3 and whichever pin showed less than 100k ohms. Repair or replace the OEM harness, refer to OEM Troubleshooting and Repair Procedures.
