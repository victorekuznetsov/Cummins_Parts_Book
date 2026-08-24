---
aliases:
  - "Калибровочный код ЭБУ"
type: "Процедура"
doc: "01-019-032"
title_en: "ECM Calibration Code"
title_ru: "Калибровочный код ЭБУ"
modified: "2002-12-05"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 4
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-019-032.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-019-032.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# ECM Calibration Code
**Калибровочный код ЭБУ**

> [!abstract] Процедура · `01-019-032`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2002-12-05
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-019-032.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-019-032.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Калибровку ECM можно проводить с помощью электронной базы данных программного обеспечения и сети.

![[19800902.png]]

Процесс калибровки ECM для двигателя происходит с выключателем Run/Stop в положении Stop. ** Всегда следуйте инструкциям на экранах инструментов сервиса.

> [!note] Примечание
> Если инструмент будет **не** общаться, отсоедините упряжку служебной проводов и снова подключите ее, чтобы убедиться, что все соединения хороши.

![[19600070.png]]

Подключите инструмент электронного сервиса к шине данных CAN, которая расположена на двигателе.

![[19800902.png]]

См. руководство пользователя INPOWERTM для подробных процедур калибровки ECM.

![[19800902.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> ECM calibrations can be performed by the electronic software database and network.
>
> The ECM calibration process for the engine occurs with the Run/Stop switch in the Stop position. **Always** follow the instructions on the service tool screens.
>
> **Note · Примечание**
> If the tool will **not** communicate, disconnect the service harness, and reconnect it again to make sure all connections are good.
>
> Connect the electronic service tool to the service tool datalink, which is located on the engine.
>
> Refer to the INPOWER™ user's manual for detailed ECM calibration procedures.
