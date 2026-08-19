---
aliases:
  - "Печатная плата ЭБУ"
type: "Процедура"
doc: "01-019-322"
title_en: "ECM Circuit Board"
title_ru: "Печатная плата ЭБУ"
modified: "2003-06-30"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 7
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-019-322.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-019-322.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# ECM Circuit Board
**Печатная плата ЭБУ**

> [!abstract] Процедура · `01-019-322`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-06-30
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-019-322.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-019-322.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Схемные платы ECM расположены в карточной клетке внутри коробки управления. Генераторная установка будет иметь по крайней мере три платы, топливный щит, базовый щит и джинсовый щит. Как параллельная доска, так и доска LonWorks® являются необязательными.

![[19802869.png]]

### Снятие

Базовый совет (другие аналогичные советы).

Отсоедините 50-контактный D-подключатель от платы.

Отсоедините 25-контактный D-подключатель от платы (базовая плата **только **).

![[19802661.png]]

Отвинтить крепежный винт на каждом конце блока терминала. Вытащите блок терминала из платы. Квартира с конечным блоком ** не должна быть отключена. (Набор топлива не имеет терминального блока.)

![[19802835.png]]

Устраните винт на каждом конце доски.

Вытяните печатную плату прямо, пока она не освободится от клетки карты. Удалите печатную плату.

![[19803034.png]]

### Установка

Базовый совет (другие аналогичные советы).

Держа доску непосредственно над слотом, выровняйте задний край доски с выравнивающим канавкой в задней части карточной клетки.

Медленно опустите доску так, чтобы задний край доски помещался внутри выравнивающей канавки на задней части карточной клетки. Скользите по доске вниз и в разъем задней плоскости в нижней части карточной клетки.

Убедитесь, что плата установлена с верхней поверхностью карточной клетки и с другими печатными платами. Закручивайте винт на каждом конце печатной платы.

![[19803034.png]]

Найдите терминальный блок в положении на печатной плате. Затягивайте крепежный винт на каждом конце блока терминала. (Набор топлива не имеет терминальных блоков.)

![[19802835.png]]

Подключите 25-контактный D-подключатель к плате. (Только базовая доска.)

Подключите 50-контактный D-подключатель к плате.

Подключите инструмент электронного сервиса и проверьте наличие активных кодов неисправностей.

![[19802661.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> The ECM circuit boards are located in the card cage inside the controls box. The generator set will have at least three boards, the fuel board, base board, and genset board. Both the paralleling board and LonWorks® board are optional.
>
> ### Remove
>
> Base board (other boards similar).
>
> Disconnect the 50-pin D-sub connector from the board.
>
> Disconnect the 25-pin D-sub connector from the board (base board **only**).
>
> Unscrew the mounting screw at each end of the terminal block. Pull the terminal block off the circuit board. The terminal block wiring does **not** need to be disconnected. (Fuel board does **not** have terminal block.)
>
> Loosen the screw at each end of the board.
>
> Pull the circuit board straight up until it is free from the card cage. Remove the circuit board.
>
> ### Install
>
> Base board (other boards similar).
>
> Holding the board directly above the slot, align the back edge of the board with the alignment groove in the back of the card cage.
>
> Slowly drop the board down so that the back edge of the board fits inside the alignment groove on the back of the card cage. Slide the board down and into the backplane connector at the bottom of the card cage.
>
> Make sure the board is mounted flush with the top surface of the card cage, and with the other circuit boards. Tighten down the screw on each end of the circuit board.
>
> Locate the terminal block in position onto the circuit board. Tighten down the mounting screw at each end of the terminal block. (Fuel board does **not** have terminal blocks.)
>
> Connect the 25-pin D-sub connector to the board. (Base board only.)
>
> Connect the 50-pin D-sub connector to the board.
>
> Connect the electronic service tool and check for any active fault codes.
