---
aliases:
  - "Цепь выключателя «Стоп/Работа»"
type: "Процедура"
doc: "94-019-015"
title_en: "Stop/Run Switch Circuit"
title_ru: "Цепь выключателя «Стоп/Работа»"
modified: "2003-03-24"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666184"
figures: 4
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/94/94-019-015.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/94-019-015.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/94"
  - "перевод/машинный"
---

# Stop/Run Switch Circuit
**Цепь выключателя «Стоп/Работа»**

> [!abstract] Процедура · `94-019-015`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual|3666184]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-03-24
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/94/94-019-015.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/94-019-015.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Проверка сопротивления

> [!warning] ОСТОРОЖНО
> Не используйте ни пробы, ни зацепки, кроме Части Нет. 3822758. Разъём будет повреждён. Лиды должны плотно вписываться в разъем без расширения штифтов в разъеме.

Отсоедините разъем от положительного клемма батареи.

Отсоедините OEM-разъем от ECM.

![[19a00055.png]]

Включить испытательный щуп в контакт 63 разъёма проводов OEM.

Измерьте сопротивление от контакта 63 до положительного разъема батареи.

Поместите выключатель Stop/Run в положение RUN. Мультиметр **должен** показать замкнутую цепь (10 Ом и менее).

Если схема ** не ** закрыта, проверьте наличие открытой цепи в проводах переключателя Stop/Run, учитывая, что переключатель уже проверен.

Ремонт или замена OEM проводов жгута. См. OEM устранение неполадок и процедуры ремонта.

![[19a00051.png]]

Переключите стоп/бег на стоп. Мультиметр **должен** показать обрыв цепи (100 кОм и более).

Если схема **не** открыта, в проводах переключателя Stop/Run существует короткое замыкание, при условии, что переключатель уже проверен.

Ремонт или замена OEM проводов жгута. См. OEM устранение неполадок и процедуры ремонта.

![[19a00051.png]]

### Проверка на замыкание между контактами

Отсоедините проводку OEM от ECM.

Отсоедините разъем от положительного свинца батареи.

Измерьте сопротивление от контакта 63 разъёма OEM-проводов с другими штифтами в разъеме. Мультиметр ** должен** показывать открытую схему (100к Ом или меньше).

Если какая-либо проверка показывает менее 100k Ом, отремонтируйте или замените электропроводку OEM. См. OEM устранение неполадок и процедуры ремонта.

> [!missing]- Иллюстрация `19a00052.png` не извлечена — смотрите PDF-оригинал документа


> [!quote]- Original (English) · английский оригинал
> ### Resistance Check
>
> **CAUTION · Осторожно**
> Do not use probes or leads other than Part No. 3822758. The connector will be damaged. The leads must fit tight in the connector without expanding the pins in the connector.
>
> Disconnect the connector from the positive battery terminal.
>
> Disconnect the OEM connector from the ECM.
>
> Insert a test lead into pin 63 of the OEM harness connector.
>
> Measure the resistance from pin 63 to the positive battery connector.
>
> Place the Stop/Run switch in the RUN position. The multimeter **must** show a closed circuit (10 ohms or less).
>
> If the circuit is **not** closed, check for an open circuit in the Stop/Run switch wiring, considering the switch has already been checked.
>
> Repair or replace the OEM harness. Refer to OEM Troubleshooting and Repair Procedures.
>
> Move the Stop/Run switch to STOP. The multimeter **must** show an open circuit (100k ohms or more).
>
> If the circuit is **not** open, a short circuit exists in the Stop/Run switch wiring, providing the switch has already been checked.
>
> Repair or replace the OEM harness. Refer to OEM Troubleshooting and Repair Procedures.
>
> ### Check for Short Circuit from Pin to Pin
>
> Disconnect the OEM harness from the ECM.
>
> Disconnect the connector from the positive battery lead.
>
> Measure the resistance from pin 63 of the OEM harness connector to all other pins in the connector. The multimeter **must** show an open circuit (100k ohms or less).
>
> If any check shows less than 100k ohms, repair or replace the OEM harness. Refer to OEM Troubleshooting and Repair Procedures.
