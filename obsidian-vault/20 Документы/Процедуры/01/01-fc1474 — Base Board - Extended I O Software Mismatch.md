---
aliases:
  - "Базовая плата — несоответствие ПО расширенного ввода-вывода"
type: "Процедура"
doc: "01-fc1474"
title_en: "Base Board - Extended I/O Software Mismatch"
title_ru: "Базовая плата — несоответствие ПО расширенного ввода-вывода"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1474.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1474.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Base Board - Extended I/O Software Mismatch
**Базовая плата — несоответствие ПО расширенного ввода-вывода**

> [!abstract] Процедура · `01-fc1474`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1474.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1474.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 1474

### Базовая плата — несоответствие ПО расширенного ввода-вывода

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 1474 PID(P): СПН: ФМИ: Лампа: Отключение SRT: | Несоответствие версий программного обеспечения между базовой платой и расширенной платой ввода/вывода. | Генератор будет отключен. |

![[19802649.png]]

Генератор установил ECM-картонную клетку

### Описание цепи

Этот код неисправности используется ECM для того, чтобы сообщить оператору, что версия программного обеспечения для базовой платы не соответствует версии программного обеспечения, загруженного в расширенную плату ввода-вывода.

### Расположение компонента

См. раздел E для определения местоположения клетки карты ECM, базовой платы и расширенной платы ввода/вывода.

### Практические замечания

Возможные режимы отказа - неправильная установка базовой платы или расширенной платы ввода/вывода и загрузка неправильной калибровки программного обеспечения в ECM.

См. Код устранения неисправностей t05-1474


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 1474
>
> ### Base Board - Extended I/O Software Mismatch
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 1474 PID(P): SPN: FMI: Lamp: Shutdown SRT: | Software version mismatch between the base board and the extended I/O board. | Generator set will shut down. |
>
> Generator Set ECM Card Cage
>
> ### Circuit Description
>
> This fault code is used by the ECM to tell the operator that the base board software version does not correspond to the version of software loaded into the extended I/O board.
>
> ### Component Location
>
> Refer to section E for location of the ECM card cage, the base board, and the extended I/O board.
>
> ### Shoptalk
>
> The possible failure modes are incorrect installation of the base board or extended I/O board, and loading an incorrect software calibration into the ECM.
>
> Refer to Troubleshooting Fault Code t05-1474
