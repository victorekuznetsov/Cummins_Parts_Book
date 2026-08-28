---
aliases:
  - "Жгут переменного тока"
type: "Процедура"
doc: "01-019-315"
title_en: "AC Harness"
title_ru: "Жгут переменного тока"
modified: "2003-06-30"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 11
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-019-315.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-019-315.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# AC Harness
**Жгут переменного тока**

> [!abstract] Процедура · `01-019-315`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-06-30
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-019-315.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-019-315.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Упряжка электропроводки переменного тока переносит сигналы напряжения и тока в плату PT / CT, переносит напряжение возбуждения PMG к регулятору напряжения, а затем переносит возбуждение поля от регулятора напряжения обратно к генератору переменного тока.

Упряжка AC-проводов расположена в блоке управления и простирается над генератором переменного тока.

![[nobox.png]]

### Снятие

Отсоедините провода P2, P3 и P4 от проводов разъема PMG.

Отсоедините провода F1 и F2 от полевого провода к генератору переменного тока.

![[19802831.png]]

Отключите проводку к каждому трансформатору тока. Уберите гайки и заприте шайбу. Каждый трансформатор тока будет иметь КТ и КТ COM (общий) провод, который должен быть удален.

![[19802832.png]]

Отключите проводку GEN L1, L2, L3 и NEUTRAL с выходных проводов.

![[19802839.png]]

Отсоедините 12-контактный AMP-разъем 09 от платы PT/CT.

![[19802840.png]]

Отсоедините 6-контактный AMP-разъем 10 от регулятора напряжения.

Удалите все проводов, поддерживающие ремни.

Медленно вытащите электропроводку переменного тока из коробки управления, убедившись, что нет связывания или запутывания.

![[19802833.png]]

### Установка

> [!note] Примечание
> На некоторых генераторных установках установка может варьироваться.

Маршрутируйте электропроводку переменного тока через заднюю часть блока управления, чтобы генератор переменного тока и соединения PMG были близки к выходным выводам.

Кормите другой конец проводов с соединениями 09 и 10 в блок управления и вниз и позади блоков терминала.

Подключите 6-контактный AMP-разъем 10 к регулятору напряжения.

![[19802833.png]]

Подключите 12-контактный AMP-разъем 09 к плате PT/CT.

![[19802840.png]]

Подключите проводку GEN, L1, L2, L3 и NEUTRAL для определения напряжения к выходным проводам.

![[19802839.png]]

Подключите проводку к каждому трансформатору тока. Установите гайку и шайбу. Каждый трансформатор тока будет иметь КТ и КТ COM (общий) провод, который должен быть установлен.

![[19802832.png]]

Соедините провода P2, P3 и P4 с проводами разъема PMG.

Подключите провода F1 и F2 к разъемам электропроводки генератора.

![[19802831.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> The AC harness carries the voltage and current sensing signals into the PT/CT board, carries the PMG excitation voltage to the voltage regulator, and then carries the field excitation from the voltage regulator back to the alternator.
>
> The AC harness is located in the controls box and extends out over the alternator.
>
> ### Remove
>
> Disconnect wires P2, P3, and P4 from the PMG connector wires.
>
> Disconnect wires F1 and F2 from field wiring to alternator.
>
> Disconnect wiring to each current transformer. Remove nuts and lock washer. Each current transformer will have a CT and a CT COM (common) wire that **must** be removed.
>
> Disconnect voltage sensing wiring GEN L1, L2, L3, and NEUTRAL from output leads.
>
> Disconnect 12-pin AMP connector 09 from the PT/CT board.
>
> Disconnect 6-pin AMP connector 10 from the voltage regulator.
>
> Remove any harness supports.
>
> Slowly pull the AC harness out of the controls box, making sure there is no binding or tangling.
>
> ### Install
>
> **Note · Примечание**
> On some generator sets, installation can vary.
>
> Route the AC harness through the back of the controls box so that the alternator and PMG connections are close to the output leads.
>
> Feed the other end of the harness with connections 09 and 10 into the controls box and down and behind the terminal blocks.
>
> Connect 6-pin AMP connector 10 to the voltage regulator.
>
> Connect 12-pin AMP connector 09 to the PT/CT board.
>
> Connect voltage sensing wiring GEN, L1, L2, L3, and NEUTRAL to output leads.
>
> Connect wiring to each current transformer. Install nut and lock washer. Each current transformer will have a CT and a CT COM (common) wire that **must** be installed.
>
> Connect wires P2, P3, and P4 to the PMG connector wires.
>
> Connect wires F1 and F2 to the alternator field wiring connectors.
