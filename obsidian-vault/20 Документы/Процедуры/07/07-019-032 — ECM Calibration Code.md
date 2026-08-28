---
aliases:
  - "Калибровочный код ЭБУ"
type: "Процедура"
doc: "07-019-032"
title_en: "ECM Calibration Code"
title_ru: "Калибровочный код ЭБУ"
modified: "2003-12-09"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-019-032.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/07-019-032.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "группа/07"
  - "перевод/машинный"
---

# ECM Calibration Code
**Калибровочный код ЭБУ**

> [!abstract] Процедура · `07-019-032`
> **Двигатели:** [[93058669 — 6C8.3 CPL 3105|93058669]], [[93087701 — 6C8.3 CPL 3105|93087701]]
> **Семейство:** C8.3 · 6C8.3
> **Входит в руководства:** [[4021442 — C8.3 Marine Electronic Control System Troubleshooting and Repair Manual|4021442]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-12-09
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-019-032.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/07-019-032.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

Калибровку ECM можно выполнить с помощью инструментария электронного сервиса INSITETM.

![[19c01217.png]]

Процесс калибровки ECM происходит с переключателем зажигания в положении ON.

Всегда следуйте инструкциям на экранах инструментов сервиса.

> [!note] Примечание
> Если инструмент будет **не*** взаимодействовать с выключателем зажигания в положении Включения, зациклите замок зажигания и попробуйте снова.

![[19800470.png]]

Подключите инструмент электронного сервиса к шине данных CAN, расположенной на панели диагностических инструментов.

См. раздел помощи с INSITETM для подробных процедур калибровки ECM.

![[19c01217.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> ECM calibrations can be performed by the INSITE™ electronic service tool.
>
> The ECM calibration process occurs with the keyswitch in the ON position.
>
> Always follow the instructions on the service tool screens.
>
> **Note · Примечание**
> If the tool will **not** communicate with the keyswitch in the ON position, cycle the keyswitch and try again.
>
> Connect the electronic service tool to the service tool datalink, located on the diagnostic tool panel.
>
> Refer to the help section with INSITE™ for detailed ECM calibration procedures.
