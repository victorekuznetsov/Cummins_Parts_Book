---
aliases:
  - "Изменения защиты калибровок ЭБУ: требуется INSITE™ версии 8.7.0 или новее"
type: "TSB"
doc: "tsb200247"
title_en: "Changes to Engine Control Module (ECM) Calibration Code Security Requiring INSITE™ Electronic Service Tool Version 8.7.0 or Newer"
title_ru: "Изменения защиты калибровок ЭБУ: требуется INSITE™ версии 8.7.0 или новее"
released: "2020-12-17"
modified: "2024-10-04"
group: "22 - Service Tools"
engines:
  - "33239746"
  - "33239899"
  - "37292556"
  - "37295879"
  - "41349633"
  - "93058669"
families:
  - "C8.3 · 6C8.3"
  - "K38/K50 · QSK38, QSK50, QSK60"
  - "QSK19"
  - "QST30"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2020/tsb200247.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/tsb/tsb200247.pdf"
tags:
  - "документ/tsb"
  - "двигатель/C8.3"
  - "двигатель/K38/K50"
  - "двигатель/QSK19"
  - "двигатель/QST30"
  - "год/2020"
  - "перевод/машинный"
  - "тема/service-tools"
---

# Changes to Engine Control Module (ECM) Calibration Code Security Requiring INSITE™ Electronic Service Tool Version 8.7.0 or Newer
**Изменения защиты калибровок ЭБУ: требуется INSITE™ версии 8.7.0 или новее**

> [!abstract] TSB · `tsb200247`
> **Раздел Cummins:** 22 - Service Tools
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]], [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]], [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[93058669 — 6C8.3 CPL 3105|93058669]]
> **Семейство:** C8.3 · 6C8.3, K38/K50 · QSK38, QSK50, QSK60, QSK19, QST30
> **Даты:** выпущен 2020-12-17 · изменён 2024-10-04
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2020/tsb200247.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/tsb/tsb200247.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


## Изменения защиты калибровок ЭБУ: требуется INSITE™ версии 8.7.0 или новее

### Положение о гарантии

Сведения в этом документе не изменяют действующие гарантийные обязательства и практику ремонта и не дают оснований для работ по программам TRP или Campaign.

### Содержание

** Пострадавшие продукты**

- Все продукты двигателя с электронным управлением

**Проблема**

10 декабря 2020 года будут выпущены новые калибровочные коды модуля управления двигателем (ECM) с использованием стандартного шифрования для всех продуктов двигателя с электронным управлением. Эти коды калибровки ECM поддерживаются только в электронной версии инструментария INSITETM 8.7.0 и более новой. Если пользователи обновят систему **not**, пользователи не смогут использовать калибровки ECM, загруженные через QuickServe® Online (QSOL) или Cal через Интернет после 10 декабря 2020 года.

**Решение**

10 декабря 2020 года будут выпущены новые калибровки ECM с использованием нового стандарта шифрования. Для этого потребуется использование INSITE 8.7.0 или более при использовании этих калибровок, загруженных из Quickserve Online (QSOL), или использование функции поиска кода ECM в INSITETM. Cummins Inc. Рекомендуем пользователям обновиться до INSITE 8.7.0 как можно скорее. Калибровки, выпущенные после декабря 2019 года или на DVD INCAL с августа 2020 года или позже, все еще могут использоваться с INSITE 8.7.0.

1. Во время установки INSITE 8.7.0.exe пользователь может видеть несколько диалоговых окон антивируса, обнаруживающих подозрительные файлы во время всей установки. Пользователь ** не обязан их признавать.

![[19r99693.png]]

Рисунок 1 Пример антивирусной диалоговой коробки.

2. Если пользователь хочет использовать другой пакет INSITE 8.7.0, извлеченный другой пакет может быть использован только один раз. Если пользователь хочет использовать второй раз, пользователю необходимо удалить извлеченный пакет и повторно извлечь файл OtherPackage.zip.

### История изменений документа


> [!quote]- Original (English) · английский оригинал
> ## Changes to Engine Control Module (ECM) Calibration Code Security Requiring INSITE™ Electronic Service Tool Version 8.7.0 or Newer
>
> ### Warranty Statement
>
> The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.
>
> ### Contents
>
> **Products Affected**
>
> - All electronically controlled engine products
>
> **Issue**
>
> On 10 December 2020, new engine control module (ECM) calibration codes will be released using industry standard encryption for all electronically controlled engine products. These ECM calibration codes are **only** supported in INSITE™ electronic service tool version 8.7.0 and newer. If users do **not** upgrade, users will **not** be able to use any ECM calibrations downloaded through QuickServe® Online (QSOL) or Cal over web after 10 December 2020.
>
> **Resolution**
>
> On 10 December 2020, new ECM calibrations will be released using new industry standard encryption. This will require use of INSITE 8.7.0 or greater when using these calibrations downloaded from Quickserve Online (QSOL) or using the ECM Code Search feature within INSITE™. Cummins Inc. recommends users upgrade to INSITE 8.7.0 as soon as possible. Calibrations released after December 2019 or on an INCAL™ DVD from August 2020 or later can still be used with INSITE 8.7.0.
>
> 1. During the installation of the INSITE 8.7.0.exe, the user might see multiple dialog boxes of antivirus detecting suspicious files during the whole installation. The user does **not** need to acknowledge them.
>
> Figure 1, Example of Antivirus Dialog Box.
>
> 2. If a user wants to use the INSITE 8.7.0 Other Package, the extracted other package can **only** be used once. If user wants to use is a second time, the user needs to delete the extracted package and re-extract the OtherPackage.zip file.
>
> ### Document History
