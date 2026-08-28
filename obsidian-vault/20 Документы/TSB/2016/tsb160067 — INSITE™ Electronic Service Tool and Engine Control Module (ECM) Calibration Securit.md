---
aliases:
  - "Изменения защиты калибровок ЭБУ и INSITE™"
type: "TSB"
doc: "tsb160067"
title_en: "INSITE™ Electronic Service Tool and Engine Control Module (ECM) Calibration Security Changes"
title_ru: "Изменения защиты калибровок ЭБУ и INSITE™"
released: "2016-07-06"
modified: "2018-10-04"
group: "22 - Service Tools"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
  - "33224404"
  - "33239746"
  - "33239899"
  - "35354607"
  - "35373113"
  - "37292556"
  - "37295879"
  - "41340468"
  - "41349633"
  - "41353297"
  - "71156161"
  - "80141463"
  - "80248213"
  - "82099327"
  - "85017333"
  - "93948840"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
  - "QSB6.7"
  - "QSK19"
  - "QSK23"
  - "QSK50"
  - "QSK60"
  - "QSM11"
  - "QST30"
  - "QSX15"
  - "QSZ13"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2016/tsb160067.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb160067.pdf"
tags:
  - "документ/tsb"
  - "двигатель/K38/K50"
  - "двигатель/QSB6.7"
  - "двигатель/QSK19"
  - "двигатель/QSK23"
  - "двигатель/QSK50"
  - "двигатель/QSK60"
  - "двигатель/QSM11"
  - "двигатель/QST30"
  - "двигатель/QSX15"
  - "двигатель/QSZ13"
  - "год/2016"
  - "перевод/машинный"
  - "тема/service-tools"
---

# INSITE™ Electronic Service Tool and Engine Control Module (ECM) Calibration Security Changes
**Изменения защиты калибровок ЭБУ и INSITE™**

> [!abstract] TSB · `tsb160067`
> **Раздел Cummins:** 22 - Service Tools
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[33224404 — QSK50 CM2150 MCRS CPL 3391|33224404]], [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]], [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]], [[41340468 — QSK50 CM2150 MCRS CPL 3728|41340468]], [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]], [[82099327 — QSB6.7 CM2150 B109 CPL 4375|82099327]], [[85017333 — QSK23 CM500 CPL 2858|85017333]], [[93948840 — QSZ13 CM2150 Z102 CPL 4858|93948840]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60, QSB6.7, QSK19, QSK23, QSK50, QSK60, QSM11, QST30, QSX15, QSZ13
> **Даты:** выпущен 2016-07-06 · изменён 2018-10-04
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2016/tsb160067.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb160067.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


## Изменения защиты калибровок ЭБУ и INSITE™

### Положение о гарантии

Сведения в этом документе не изменяют действующие гарантийные обязательства и практику ремонта и не дают оснований для работ по программам TRP или Campaign.

### Содержание

**Затронутая продукция**

- Все продукты, поддерживаемые инструментами электронного сервиса INSITETM

**Описание изменения**

В электронной сервисной оснастке INSITETM версии 8.1.4 повышен уровень безопасности калибровок модуля управления двигателем (ECM). Эти изменения безопасности в INSITETM согласуются с изменениями безопасности во всех предстоящих калибровках Cummins® ECM. Эти изменения безопасности **** влияют на возможность загрузки калибровки ECM в версии 8.1.4 INSITETM Pro и Road Speed Governor Restricted (RSGR)/Industrial ProTM.

**Причина изменения**

Эта улучшенная безопасность предназначена для того, чтобы обеспечить загрузку определенных **только** аутентичных калибровок Cummins® ECM в электронные модули управления и программируемые устройства шины данных CAN.

**Клиентская коммуникация**

Начиная с 26 июля 2016 года, INSITETM Pro версии 8.1.4 будет необходим для всех калибровок ECM, выпущенных 26 июля 2016 года и после этого. Это бесплатное обновление будет доступно всем пользователям INSITETM Pro. Старые версии INSITETM Pro будут **не** распознавать калибровки ECM, выпущенные после этой даты. Cummins Inc. Рекомендует обновить существующую версию INSITETM Pro (8.1.3), поэтому обновления, начиная с 26 июля 2016 года, не требуют много времени. Это обновление позволит отложить установку до трех раз, прежде чем начать автоматическое обновление.

Пользователи INSITETM будут уведомлены через автоматическое всплывающее окно, когда INSITETM 8.1.4 будет доступен для установки. Для бесшовной поддержки клиентов, Cummins Inc. Рекомендуем обновить INSITETM до новой версии по запросу.

**Указания по обслуживанию**

Если INSITETM**не обновляется, предыдущие версии INSITETM** будут загружать калибровки ECM только на старые DVD INCALTM, срок действия которых истек. После истечения срока действия DVD-дисков INCALTM INSITETM больше не сможет загружать калибровку ECM до обновления до версии 8.1.4 INSITETM.

> [!note] Примечание
> Если возникают проблемы с процессом калибровки INSITETM или ECM, позвоните по телефону (800) 433-9341 и выберите вариант 2. Горячая линия будет работать 24 часа в сутки в течение этого периода обновления с 26 июля 2016 года по 15 августа 2016 года.

Начиная с 26 июля, **только *** эти новые калибровки ECM с улучшенной встроенной безопасностью будут доступны в QuickServe® Online (QSOL) и в функции поиска и сохранения кода ECM в INSITETM. С 26 июля 2016 года по 15 августа 2016 года более старые версии INSITETM по-прежнему смогут загружать более старые калибровки ECM с DVD-дисков INCALTM и http://care.cummins.com. Срок действия DVD-дисков INCAL истекает через семь месяцев после публикации. Следующий выпуск DVD INCALTM 26 июля 2016 года будет содержать **только **новые калибровки ECM с улучшенной встроенной безопасностью и может быть загружен только * с помощью INSITETM версии 8.1.4.

**Совместимость частей**

| Таблица 1, Инсайт TM Электронная версия службы и диаграмма совместимости калибровки ECM: Перед внедрением безопасности |  |  |  |
|---|---|---|---|
| Источник калибровки ECM | QuickServe® Online и поиск кода ECM | http://care.cummins.com | DVD INCALTM |
| Дата | До 26 июля 2016 года | С 26 июля 2016 года по 15 августа 2016 года | До 26 июля 2016 года |
| Insite 8.1.4 и более новая версия | - | - | Не совместимы |
| Insite 8.1.3 и более старая версия | совместимый | совместимый | совместимый |

| Таблица 2, Инсайт TM Электронная версия для инструментов и диаграмма совместимости калибровки ECM: После встраивания безопасности |  |  |  |
|---|---|---|---|
| Источник калибровки ECM | QuickServe® Online и поиск кода ECM | http://care.cummins.com | DVD INCALTM |
| Дата | После 26 июля 2016 года | После 15 августа 2016 года | После 26 июля 2016 года |
| Insite 8.1.4 и более новая версия | совместимый | - | совместимый |
| Insite 8.1.3 и более старая версия | **Не совместимы | - |**Не совместимы |

### История изменений документа


> [!quote]- Original (English) · английский оригинал
> ## INSITE™ Electronic Service Tool and Engine Control Module (ECM) Calibration Security Changes
>
> ### Warranty Statement
>
> The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.
>
> ### Contents
>
> **Product Affected**
>
> - All products supported by INSITE™ electronic service tool
>
> **Description of Change**
>
> INSITE™ electronic service tool version 8.1.4 has an improved level of security for engine control module (ECM) calibrations. These security changes in INSITE™ are aligned with security changes in all upcoming Cummins® ECM calibrations. These security changes **only** affect the ECM calibration download capability of INSITE™ Pro and Road Speed Governor Restricted (RSGR)/Industrial Pro™ version 8.1.4.
>
> **Reason for Change**
>
> This improved security is intended to make certain **only** authentic Cummins® ECM calibrations are downloaded into electronic control modules and programmable datalink devices.
>
> **Customer Communication**
>
> Beginning 26 July 2016, INSITE™ Pro version 8.1.4 will be needed for all ECM calibrations released on 26 July 2016 and thereafter. This free update will be pushed to all licensed users of INSITE™ Pro. Older versions of INSITE™ Pro will **not** recognize ECM calibrations released after this date. Cummins Inc. recommends updating to the existing version of INSITE™ Pro (8.1.3) now so updates beginning on 26 July 2016 are **not** as time consuming. This update will provide the option to delay the install up to three times before commencing with an automatic update.
>
> INSITE™ users will be notified through an automated pop-up window when INSITE™ 8.1.4 is available for installation. For seamless customer support, Cummins Inc. recommends INSITE™ be updated to the new version when prompted.
>
> **Service Instructions**
>
> If INSITE™ is **not** updated, previous versions of INSITE™ will **only** download ECM calibrations on old INCAL™ DVDs that have **not** expired. Once INCAL™ DVDs have expired, INSITE™ will no longer be able to download any ECM calibration until updated to INSITE™ version 8.1.4.
>
> **Note · Примечание**
> If issues are encountered with the INSITE™ update or ECM calibration process, call (800) 433-9341 and select option 2. The hotline will be operating 24 hours a day during this update period between 26 July 2016 and 15 August 2016.
>
> Beginning July 26 th, **only** these new ECM calibrations with improved embedded security will be available from QuickServe® Online (QSOL) and from the ECM Code Search and Save feature within INSITE™. Between 26 July 2016 and 15 August 2016, older versions of INSITE™ will still be able to download older ECM calibrations from the INCAL™ DVDs and http://care.cummins.com. However, INCAL™ DVDs will expire seven months after publication. The next release of INCAL™ DVD on 26 July 2016 will contain **only** the new ECM calibrations with improved embedded security and can **only** be downloaded with INSITE™ version 8.1.4.
>
> **Part Compatibility**
>
> | Table 1, INSITE™ Electronic Service Tool Version and ECM Calibration Compatibility Chart: Before Embedded Security |  |  |  |
> |---|---|---|---|
> | ECM Calibration Source | QuickServe® Online and ECM Code Search | http://care.cummins.com | INCAL™ DVD |
> | Date | Before 26 July 2016 | Between 26 July 2016 and 15 August 2016 | Before 26 July 2016 |
> | INSITE™ Version 8.1.4 and newer | - | - | **Not** Compatible |
> | INSITE™ Version 8.1.3 and older | Compatible | Compatible | Compatible |
>
> | Table 2, INSITE™ Electronic Service Tool Version and ECM Calibration Compatibility Chart: After Embedded Security |  |  |  |
> |---|---|---|---|
> | ECM Calibration Source | QuickServe® Online and ECM Code Search | http://care.cummins.com | INCAL™ DVD |
> | Date | After 26 July 2016 | After 15 August 2016 | After 26 July 2016 |
> | INSITE™ Version 8.1.4 and newer | Compatible | - | Compatible |
> | INSITE™ Version 8.1.3 and older | **Not** Compatible | - | **Not** Compatible |
>
> ### Document History
