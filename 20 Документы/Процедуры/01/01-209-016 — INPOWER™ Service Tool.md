---
aliases:
  - "Сервисный инструмент INPOWER™"
type: "Процедура"
doc: "01-209-016"
title_en: "INPOWER™ Service Tool"
title_ru: "Сервисный инструмент INPOWER™"
modified: "2002-11-15"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 6
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-209-016.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-209-016.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# INPOWER™ Service Tool
**Сервисный инструмент INPOWER™**

> [!abstract] Процедура · `01-209-016`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section F - Familiarization
> **Даты:** изменён 2002-11-15
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-209-016.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-209-016.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Общие сведения

INPOWERTM - это инструмент для системы управления генераторным приводом. Используйте INPOWERTM для:

- Информация, указанная владельцем программы в ECM (параметры и функции)
- Помощь в устранении неисправностей двигателя
- Изменение мощности двигателя или калибровка номинальной скорости

См. руководство INPOWERTM для конкретных случаев.

![[19800902.png]]

### InpowerTM Режим настройки

Функция настройки позволяет вносить коррективы в параметры набора для отделки и настроек. Существует несколько параметров регулировки, и не все наборы будут иметь одинаковые настройки.

![[nobox.png]]

### Режим монитора Inpower

Режим монитора INPOWERTM является полезным средством устранения неполадок, которое отображает ключевые входы и выходы ECM. Эта функция может использоваться для определения постоянных или аномально колеблющихся значений.

Входные данные ECM показывают данные, которые подаются в ECM датчиками и переключателями системы. Аванпосты ECM представляют собой значения, которые ECM командует системой управления генераторным приводом. Режим мониторинга позволяет отслеживать и использовать взаимосвязь между входами и выходами ECM во время устранения неполадок.

![[nobox.png]]

### INPOWERTM Описание

INPOWERTM PRO позволяет пользователю передавать новые или обновленные калибровочные файлы для системы управления генераторным приводом ECM из центрального местоположения дистрибьюторам Cummins. Калибровочный файл — это электронные данные, которые дают двигателю его рейтинг производительности.

![[nobox.png]]

Калибровочный файл будет загружен в INPOWERTM, который затем используется для загрузки файла в ECM.

См. вашего представителя службы Cummins и руководство INPOWERTM для получения дополнительной информации.

![[19800902.png]]

### Режим тестирования INPOWERTM

Измерительная функция представляет собой диагностический инструмент, который используется для выполнения внутренних самопроверок на PowerCommand Control для проверки входов и выходов системы управления и функций защиты испытательного двигателя.

![[nobox.png]]


> [!quote]- Original (English) · английский оригинал
> ### General Information
>
> INPOWER™ is a service tool for the generator-drive control system. Use INPOWER™ to:
>
> - Program owner-specified information into the ECM (parameters and features)
> - Aid in troubleshooting the engine
> - Change the engine power or rated speed calibration
>
> Refer to INPOWER™ manual for specifics.
>
> ### INPOWER™ Adjust Mode
>
> The adjustment feature allows you to make adjustments to genset parameters for trims and settings. There are several adjustment parameters and not all gensets will have the same adjustments available.
>
> ### INPOWER™ Monitor Mode
>
> The INPOWER™ monitor mode is a useful troubleshooting aid that displays the key ECM inputs and outputs. This feature can be used to spot constant or abnormally fluctuating values.
>
> The ECM inputs show the data that is being fed into the ECM by the system's sensors and switches. The ECM outposts are values that the ECM commands to the generator-drive control system. Monitor mode allows the relationship between the ECM inputs and outputs to be monitored and used during troubleshooting.
>
> ### INPOWER™ PRO Description
>
> INPOWER™ PRO allows user to transfer new or updated calibration files for the generator-drive control system ECM from a central location to Cummins distributors. A calibration file is electronic data that give the engine its performance rating.
>
> The calibration file will be loaded into INPOWER™, which is then used to load the file into the ECM.
>
> Refer to your Cummins service representative and the INPOWER™ manual for more information.
>
> ### INPOWER™ Test Mode
>
> The test feature is a diagnostic tool that is used to perform internal self-checks on the PowerCommand Control to verify inputs and outputs of the control system and test engine protection functions.
