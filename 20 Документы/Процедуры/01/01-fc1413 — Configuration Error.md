---
aliases:
  - "Ошибка конфигурации"
type: "Процедура"
doc: "01-fc1413"
title_en: "Configuration Error"
title_ru: "Ошибка конфигурации"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1413.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1413.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Configuration Error
**Ошибка конфигурации**

> [!abstract] Процедура · `01-fc1413`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1413.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1413.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 1413

### Ошибка конфигурации

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 1413 PID(P): СПН: ФМИ: Лампа: Отключение SRT: | Была обнаружена ошибка конфигурации. | Двигатель не запускается **. |

![[19802494.png]]

СХУ ECM

### Описание цепи

ECM проверяет, какие другие компоненты установлены при включении питания, и если список установленных компонентов не соответствует калибровке, то ECM будет использовать код ошибки 1413, ошибку конфигурации.

### Расположение компонента

См. руководство по OEM для определения местоположения ECM.

### Практические замечания

Убедитесь, что правильная калибровка загружена в ECM. Если он продолжит заменять ЕЦМ.

См. Код устранения неисправностей t05-1413


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 1413
>
> ### Configuration Error
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 1413 PID(P): SPN: FMI: Lamp: Shutdown SRT: | Configuration error has been detected. | Engine will **not** start. |
>
> GCS ECM
>
> ### Circuit Description
>
> The ECM checks to see what other components are installed at power-up, and if the list of installed components does **not** match the calibration, then the ECM will trip Fault Code 1413, Configuration Error.
>
> ### Component Location
>
> Refer to the OEM manual for location of the ECM.
>
> ### Shoptalk
>
> Verify that the correct calibration is loaded in the ECM. If it continues replace the ECM.
>
> Refer to Troubleshooting Fault Code t05-1413
