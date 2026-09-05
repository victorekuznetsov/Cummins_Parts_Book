---
aliases:
  - "Выключатель «холостой ход/номинал»"
type: "Процедура"
doc: "94-019-095"
title_en: "Idle Rated Switch"
title_ru: "Выключатель «холостой ход/номинал»"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/94/94-019-095.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/94-019-095.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/94"
  - "перевод/машинный"
---

# Idle Rated Switch
**Выключатель «холостой ход/номинал»**

> [!abstract] Процедура · `94-019-095`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual|3666184]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-03-24
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/94/94-019-095.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/94-019-095.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Переключатель Idle/Rated используется для переключения между скоростью Idle и скоростью Rated.

![[19a00061.png]]

### Проверка сопротивления

Использование INSITETM, номер детали. 3825145, в режиме монитора, переключатель Idle/Rated между IDLE и RATED для правильной работы.

Если переключатель работает **не** или INSITETM недоступен, следуйте процедурам устранения неполадок в этом разделе.

Удалите и пометьте разъемы из терминалов на коммутаторе. Поместите мультиметр на каждый терминал.

![[19800348.png]]

Поместите Idle/Rated выключатель в положение RATED и измерьте сопротивление. Мультиметр **должен** показать обрыв цепи (100 кОм и более). Если схема **не открыта, выключатель вышел из строя и **должен быть заменен. См. OEM устранение неполадок и процедуры ремонта.

![[19a00053.png]]

Переместите переключатель в положение IDLE и измерьте сопротивление. Мультиметр **должен** показать замкнутую цепь (10 Ом и менее). Если схема **не** закрыта, выключатель вышел из строя и должен быть заменен. См. OEM устранение неполадок и процедуры ремонта.

![[19a00054.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> The Idle/Rated switch is used to switch between Idle speed and Rated speed.
>
> ### Resistance Check
>
> Using INSITE™, Part No. 3825145, in the monitor mode, toggle the Idle/Rated switch between IDLE and RATED checking for proper operation.
>
> If the switch does **not** operate properly or INSITE™ is **not** available, follow the troubleshooting procedures in this section.
>
> Remove and tag the connectors from the terminals on the switch. Place the multimeter leads on each terminal.
>
> Place the Idle/Rated switch in the RATED position and measure the resistance. The multimeter **must** show an open circuit (100k ohms or more). If the circuit is **not** open, the switch has failed and **must** be replaced. Refer to OEM Troubleshooting and Repair Procedures.
>
> Move the switch to the IDLE position and measure the resistance. The multimeter **must** show a closed circuit (10 ohms or less). If the circuit is **not** closed, the switch has failed and **must** be replaced. Refer to OEM Troubleshooting and Repair Procedures.
