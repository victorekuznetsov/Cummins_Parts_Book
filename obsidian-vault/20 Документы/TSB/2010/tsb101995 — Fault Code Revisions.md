---
type: "TSB"
doc: "tsb101995"
title_en: "Fault Code Revisions"
modified: "2010-05-11"
engines:
  - "80141463"
  - "80248213"
families:
  - "QSX15"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2010/tsb101995.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb101995.pdf"
tags:
  - "документ/tsb"
  - "двигатель/QSX15"
  - "перевод/машинный"
---

# Fault Code Revisions

> [!abstract] TSB · `tsb101995`
> **Двигатели:** [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSX15
> **Даты:** изменён 2010-05-11
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2010/tsb101995.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb101995.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


## Пересмотр кода ошибки

### Положение о гарантии

Сведения в этом документе не изменяют действующие гарантийные обязательства и практику ремонта и не дают оснований для работ по программам TRP или Campaign.

### Содержание

Эта тема / разделы пересматривает следующие коды ошибок.

- Код 153 по умолчанию, схема датчика температуры воздуха в коллекторе поглощения - напряжение выше нормального или короткое к высокому источнику.
- Код по умолчанию 195, (3-Wire Sensor) Схема датчика уровня охлаждающей жидкости 1 - напряжение выше нормального или короткое к высокому источнику.
- Код по умолчанию 196, (3-Wire Sensor) Сенсор уровня охлаждения 1 - напряжение ниже нормального или короткое до низкого источника.
- Код ошибки 687, турбокомпрессор No1 Скорость Низкий - Уровень предупреждения.
- Код 2551, Топливная система Заправки.

Для кода 153, кода 195 и кода 196 ошибки номера контактов были исправлены, чтобы отразить те же самые номера контактов на настоящих схемах проводов для ISX, SignatureTM и ISX CM870.

Для кода 687 по умолчанию в раздел «практическая записка» была добавлена информация о датчике скорости турбокомпрессора. В дополнение поясняется, что в некоторых случаях оригинальный датчик скорости турбокомпрессора может оставаться во время замены датчика. Затем новый датчик устанавливается с новым кольцом и создает чрезмерный зазор от датчика до вала турбокомпрессора. Это может привести к сбою кода 687.

Для кода 2551 ошибки направление на этапе 2А-1 процедуры устранения неисправностей кода 2551 является вводящим в заблуждение. Этот шаг был изменен, чтобы направить правильный курс действий.


> [!quote]- Original (English) · английский оригинал
> ## Fault Code Revisions
>
> ### Warranty Statement
>
> The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.
>
> ### Contents
>
> This Service/Parts Topic is revising the following Fault Codes.
>
> - Fault Code 153, Intake Manifold Air Temperature Sensor Circuit - Voltage Above Normal or Shorted to High Source.
> - Fault Code 195, (3-Wire Sensor) Coolant Level Sensor 1 Circuit - Voltage Above Normal or Shorted to High Source.
> - Fault Code 196, (3-Wire Sensor) Coolant Level Sensor 1 Circuit - Voltage Below Normal or Shorted to Low Source.
> - Fault Code 687, Turbocharger Number 1 Speed Low - Warning Level.
> - Fault Code 2551, Fuel System Overfueling.
>
> For Fault Code 153, Fault Code 195, and Fault Code 196, the pin numbers have been corrected to reflect the same pin numbers on the present wiring diagrams for ISX, Signature™, and ISX CM870.
>
> For the Fault Code 687, the turbocharger speed sensor o-ring information was added to the "Shop Talk" section. The addition explains that in some cases the turbocharger original speed sensor o-ring can remain during sensor replacement. The new sensor is then installed with a new o-ring and creates excessive clearance from the sensor to the turbocharger shaft. This can cause fault code 687.
>
> For Fault Code 2551, the direction in step 2A-1 of the troubleshooting procedure for fault code 2551 is misleading. The step has been changed to direct the correct course of action.
