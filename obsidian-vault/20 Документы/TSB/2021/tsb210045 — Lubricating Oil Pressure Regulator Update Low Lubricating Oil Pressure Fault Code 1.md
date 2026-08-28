---
type: "TSB"
doc: "tsb210045"
title_en: "Lubricating Oil Pressure Regulator Update: Low Lubricating Oil Pressure Fault Code 143"
modified: "2021-03-10"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
parts:
  - "3068979"
  - "3069728"
  - "5568108"
  - "5663305"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2021/tsb210045.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb210045.pdf"
tags:
  - "документ/tsb"
  - "двигатель/QSM11"
  - "перевод/машинный"
---

# Lubricating Oil Pressure Regulator Update: Low Lubricating Oil Pressure Fault Code 143

> [!abstract] TSB · `tsb210045`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Даты:** изменён 2021-03-10
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2021/tsb210045.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb210045.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


## Обновление регулятора давления моторного масла: Код разлома низкого давления моторного масла 143

### Положение о гарантии

Сведения в этом документе не изменяют действующие гарантийные обязательства и практику ремонта и не дают оснований для работ по программам TRP или Campaign.

### Содержание

**Затронутая продукция**

- QSM M570
- QSM11 CM876 M101
- QSM11 CM876 M102M

**Проблема**

Симптом:

- Код (коды) 143 по умолчанию низкого давления масла в сочетании с колебающимся давлением масла на номинальной скорости или вблизи нее. В некоторых случаях, апфит, описанный в настоящем документе, может быть целесообразным в случаях высокого давления моторного масла, даже если код неисправности отсутствует, в Cummins Inc. дискреционность.

Первопричина:

- Отверстие регулятора давления моторного масла (известное как датчик вязкости) является не достаточно строгим для поддержания стабильного давления моторного масла при высоких температурах моторного масла, которые обычно происходят на или вблизи номинальной скорости.

**Проверка**

- Проверить наличие колебаний давления моторного масла и исчерпание других мер по устранению неполадок

**Решение**

- Новая вилка для отверстия, которая была выпущена. Эта часть заменяет датчик вязкости и является более ограничительной, способствуя стабильности давления масла.
- Заменить датчик вязкости, номер детали[[3069728]]с помощью розетки, Part Number[[5568108]].
- Новый плунжер регулятора давления, который должен использоваться в сочетании с вышеупомянутой пробкой. Эта часть заменяет существующий регулятор давления плунжер и также является более ограничительной.

**Наличие сервисных деталей**

Сервисные детали доступны для заказа. Номера деталей приведены в таблице 1.

| Таблица 1, Части обслуживания |  |  |  |  |
|---|---|---|---|---|
| Часть описание | Существующий номер детали | устарелый | Заменённый | Новый номер детали |
| Датчик, вязкость | [[3069728]] | Да | Да | [[5663305]] |
| Plunger, PRS Регулятор | [[3068979]] | Да | Да | [[5663305]] |

### История изменений документа

## Детали, упомянутые в документе

| Артикул | Наименование | Русское название |
|---|---|---|
| [[3068979]] | PRESSURE REGULATOR PLUNGER | Плунжер регулятора давления |
| [[3069728]] | VISCOSITY SENSOR |  |
| [[5568108]] | Orifice Plug | Дроссельная пробка (жиклёр) |
| [[5663305]] | Regulator Kit |  |

> [!quote]- Original (English) · английский оригинал
> ## Lubricating Oil Pressure Regulator Update: Low Lubricating Oil Pressure Fault Code 143
>
> ### Warranty Statement
>
> The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.
>
> ### Contents
>
> **Product Affected**
>
> - QSM CM570
> - QSM11 CM876 M101
> - QSM11 CM876 M102M
>
> **Issue**
>
> Symptom:
>
> - Low oil pressure Fault Code(s) 143 coupled with fluctuating oil pressure at or near rated speed. In some cases, the upfit described herein may be appropriate in cases of high lubricating oil pressure fluctuation even if no fault code is present, at Cummins Inc. discretion.
>
> Root Cause:
>
> - Lubricating oil pressure regulator orifice (known as the viscosity sensor) is **not** restrictive enough to support stable lubricating oil pressures at high lubricating oil temperatures that typically occur at or near rated speed.
>
> **Verification**
>
> - Verify that lubricating oil pressure fluctuation is present and other troubleshooting measures have been exhausted
>
> **Resolution**
>
> - A new orifice plug that has been released. This part replaces the viscosity sensor and is more restrictive, promoting oil pressure stability.
> - Replace viscosity sensor, Part Number [[3069728]], with orifice plug, Part Number [[5568108]].
> - A new pressure regulator plunger that **must** be used in conjunction with the above-mentioned orifice plug. This part replaces the existing pressure regulator plunger and is also more restrictive.
>
> **Service Parts Availability**
>
> Service parts are available. See Table 1 for part numbers.
>
> | Table 1, Service Parts |  |  |  |  |
> |---|---|---|---|---|
> | Part Description | Existing Part Number | Obsolete | Superseded | New Part Number |
> | Sensor, Viscosity | [[3069728]] | Yes | Yes | [[5663305]] |
> | Plunger, PRS Regulator | [[3068979]] | Yes | Yes | [[5663305]] |
>
> ### Document History
