---
aliases:
  - "Плата сети LonWorks — неверная установка"
type: "Процедура"
doc: "01-fc1346"
title_en: "LonWorks Network Board - Incorrect Installation"
title_ru: "Плата сети LonWorks — неверная установка"
modified: "2010-07-29"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1346.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1346.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# LonWorks Network Board - Incorrect Installation
**Плата сети LonWorks — неверная установка**

> [!abstract] Процедура · `01-fc1346`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1346.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1346.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 1346

### Плата сети LonWorks — неверная установка

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 1346 PID(P): СПН: ФМИ: Лампа: Отключение SRT: | Сетевая плата LonWorks (слот 4) отсутствует или была установлена неправильно. | Двигатель не запускается **. |

![[19802792.png]]

Генератор ECM LonWorks Board

### Описание цепи

После того, как программное обеспечение было загружено в ECM, программное обеспечение проведет аппаратную проверку, чтобы убедиться, что все необходимые карты установлены для приложения.

Этот код используется ECM для того, чтобы сообщить оператору, что доска LonWorks Network (слот 4) отсутствует или установлена неправильно.

### Расположение компонента

См. раздел E для определения местоположения клетки карты ECM и платы сети LonWorks (слот 4).

### Практические замечания

Возможные режимы отказа — неправильная установка платы сети LonWorks и загрузка неправильной калибровки программного обеспечения в ECM.

См. Код устранения неполадок t05-1346


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 1346
>
> ### LonWorks Network Board - Incorrect Installation
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 1346 PID(P): SPN: FMI: Lamp: Shutdown SRT: | The LonWorks Network board (slot 4) is missing or has **not** been installed correctly. | Engine will **not** start. |
>
> Generator Set ECM LonWorks Board
>
> ### Circuit Description
>
> Once the software has been loaded into the ECM, the software will do a hardware check to make sure that all necessary cards are installed for the application.
>
> This fault code is used by the ECM to tell the operator that the LonWorks Network board (slot 4) is missing or has been installed incorrectly.
>
> ### Component Location
>
> Refer to Section E for location of the ECM card cage and the LonWorks Network board (slot 4).
>
> ### Shoptalk
>
> The possible failure modes are incorrect installation of the LonWorks Network board and loading an incorrect software calibration into the ECM.
>
> Refer to Troubleshooting Fault Code t05-1346
