---
type: "TSB"
doc: "tsb120232"
title_en: "ISX/QSX and ISM/QSM CM570 Horsepower and Torque Ratings Can Display Incorrectly in INSITE™ Electronic Service Tool"
released: "2012-10-02"
modified: "2012-10-02"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
  - "80141463"
  - "80248213"
families:
  - "QSM11"
  - "QSX15"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2012/tsb120232.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb120232.pdf"
tags:
  - "документ/tsb"
  - "двигатель/QSM11"
  - "двигатель/QSX15"
  - "год/2012"
  - "перевод/машинный"
---

# ISX/QSX and ISM/QSM CM570 Horsepower and Torque Ratings Can Display Incorrectly in INSITE™ Electronic Service Tool

> [!abstract] TSB · `tsb120232`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSM11, QSX15
> **Даты:** выпущен 2012-10-02 · изменён 2012-10-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2012/tsb120232.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb120232.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


## ISX/QSX и ISM/QSM CM570 Horsepower and Torque Ratings могут отображаться некорректно в инструменте электронного обслуживания INSITETM

### Суть проблемы

При подключении к модулю управления двигателем (ECM) блока с электронным сервисным оборудованием INSITETM могут отображаться показатели мощности и крутящего момента **не**.

### Подтверждение

При подключении к ECM блока с электронным сервисным оборудованием INSITETM функции и параметры будут отображать мощность двигателя и крутящий момент. Рейтинги перечислены в Системной информации в разделе «Идентификатор системы и таблички с функциями и параметрами».

Если калибровка, которая в настоящее время находится в ECM, будет затронута, значения будут показаны как нули.

### Решение

Нет решения, легко доступного для правильного отображения значений мощности и крутящего момента в электронном сервисном оборудовании INSITETM. Если необходимы значения мощности и крутящего момента, значения отображаются на вкладке Калибровочный выбор для каждого конкретного кода ECM. DVD INCALTM или калибровка, загруженная с QuickServeTM Online, после загрузки в инструмент электронного сервиса INSITETM, отображает необходимые значения.

### Положение о гарантии

Сведения в этом документе не изменяют действующие гарантийные обязательства и практику ремонта и не дают оснований для работ по программам TRP или Campaign.

### История изменений документа


> [!quote]- Original (English) · английский оригинал
> ## ISX/QSX and ISM/QSM CM570 Horsepower and Torque Ratings Can Display Incorrectly in INSITE™ Electronic Service Tool
>
> ### Core Issue
>
> When connected to a unit's engine control module (ECM) with INSITE™ electronic service tool, the horsepower and torque ratings may **not** be displayed.
>
> ### Confirmation
>
> When connected to a unit's ECM with INSITE™ electronic service tool, Features and Parameters will display the engine's horsepower and torque ratings. The ratings are listed in System Information under the System ID and Dataplate Section of Features and Parameters.
>
> If the calibration that is presently in the ECM is affected, the values will be shown as zeros.
>
> ### Resolution
>
> There is no solution readily available to make the horsepower and torque values display correctly in INSITE™ electronic service tool. If the horsepower and torque values are needed, the values are displayed in the Calibration Selection tab for each particular ECM Code. An INCAL™ DVD or the calibration downloaded from QuickServe™ Online, once loaded into INSITE™ electronic service tool, will display the needed values.
>
> ### Warranty Statement
>
> The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.
>
> ### Document History
