---
aliases:
  - "Проблемы подключения INLINE™ 6 с Windows® 10 версий 1809 и 1903"
type: "TSB"
doc: "tsb190044"
title_en: "Connectivity Issues with INLINE™ 6 Datalink Adapter and Windows® 10 Version 1809 or Windows® 10 Version 1903"
title_ru: "Проблемы подключения INLINE™ 6 с Windows® 10 версий 1809 и 1903"
released: "2019-08-14"
modified: "2019-08-14"
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
  - "K38/K50 · QSK38, QSK50"
  - "QSB6.7"
  - "QSK19"
  - "QSK23"
  - "QSK50"
  - "QSK60"
  - "QSK60 CM2150 MCRS"
  - "QSM11"
  - "QSX15"
  - "QSZ13"
figures: 2
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2019/tsb190044.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb190044.pdf"
tags:
  - "документ/tsb"
  - "двигатель/K38/K50"
  - "двигатель/QSB6.7"
  - "двигатель/QSK19"
  - "двигатель/QSK23"
  - "двигатель/QSK50"
  - "двигатель/QSK60"
  - "двигатель/QSK60CM2150MCRS"
  - "двигатель/QSM11"
  - "двигатель/QSX15"
  - "двигатель/QSZ13"
  - "год/2019"
  - "перевод/машинный"
  - "тема/service-tools"
---

# Connectivity Issues with INLINE™ 6 Datalink Adapter and Windows® 10 Version 1809 or Windows® 10 Version 1903
**Проблемы подключения INLINE™ 6 с Windows® 10 версий 1809 и 1903**

> [!abstract] TSB · `tsb190044`
> **Раздел Cummins:** 22 - Service Tools
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[33224404 — QSK50 CM2150 MCRS CPL 3391|33224404]], [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]], [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[41340468 — QSK50 CM2150 MCRS CPL 3728|41340468]], [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]], [[82099327 — QSB6.7 CM2150 B109 CPL 4375|82099327]], [[85017333 — QSK23 CM500 CPL 2858|85017333]], [[93948840 — QSZ13 CM2150 Z102 CPL 4858|93948840]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSB6.7, QSK19, QSK23, QSK50, QSK60, QSK60 CM2150 MCRS, QSM11, QSX15, QSZ13
> **Даты:** выпущен 2019-08-14 · изменён 2019-08-14
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2019/tsb190044.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb190044.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


## Проблемы подключения INLINE™ 6 с Windows® 10 версий 1809 и 1903

### Положение о гарантии

Сведения в этом документе не изменяют действующие гарантийные обязательства и практику ремонта и не дают оснований для работ по программам TRP или Campaign.

### Содержание

**Пострадавшие продукты**

- Все продукты двигателя с электронным управлением

**Проблема**

Используя операционную систему Windows® 10 версии 1809 или Windows 10 версии 1903 (иногда называемую 19H1), при попытке подключения инструментария электронной службы INSITETM с использованием адаптера шины данных INLINETM 6 CAN можно наблюдать прерывистые проблемы подключения.

**Проверка**

Для поиска сборки операционной системы Windows 10:

1. Нажмите клавиши Windows® Key и R одновременно, чтобы открыть диалог Run, затем введите winver и выберите OK. См. рисунок 1 ниже.

![[22r00302.png]]

Рисунок 1 - Диалог бега.

2. Появится диалоговое окно Windows®, будет представлена версия Windows® и будут построены детали. См. рисунок 2 ниже.

![[22r00303.png]]

Рисунок 2, Windows® Version.

**Решение**

- Разработаны новые драйверы INLINETM 6, которые позволят решить эту проблему.
- Поскольку драйверы INLINETM 6 все еще находятся в полевых испытаниях, отправьте электронное письмо на адрес CumminsFieldTest@cummins.com с контактной информацией (имя, номер телефона, адрес электронной почты) и «Водители INLINE 6» в строке «Предмет», если вы заинтересованы в тестировании драйверов INLINE 6.
- Дополнительный обходной путь: Используйте инструмент для электронных услуг INSITETM с подключением INLINETM 6 через 9-контактный последовательный порт или используйте другой адаптер шины данных CAN, такой как INLINETM 7.
- Во избежание сбоев или сбоев в загрузке рекомендуется использовать компьютер с другой операционной системой и/или другим номером версии и/или другим адаптером шины данных CAN для любых загрузок кода калибровки ECM.

### История изменений документа


> [!quote]- Original (English) · английский оригинал
> ## Connectivity Issues with INLINE™ 6 Datalink Adapter and Windows® 10 Version 1809 or Windows® 10 Version 1903
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
> Using a Windows® 10 Version 1809 or Windows 10 Version 1903 (sometimes called 19H1) operating system, when trying to connect INSITE™ electronic service tool using an INLINE™ 6 datalink adapter, intermittent connectivity issues can be observed.
>
> **Verification**
>
> To locate Windows® 10 Operating System build:
>
> 1. Press the Windows® Key and R key simultaneously to open Run dialog, then type winver and select OK. See Figure 1 below.
>
> Figure 1, Run Dialog.
>
> 2. About Windows® dialog box will appear and provide the Windows® version and build details. See Figure 2 below.
>
> Figure 2, Windows® Version.
>
> **Resolution**
>
> - New INLINE™ 6 drivers have been developed which will resolve this issue.
> - Since the INLINE™ 6 drivers are still in field test, send an email to CumminsFieldTest@cummins.com with contact information (name, phone number, email address) and “INLINE 6 Drivers” in the Subject line, if interested in testing the INLINE 6 drivers.
> - Additional Workaround: Use INSITE™ electronic service tool with INLINE™ 6 connecting through 9-pin serial port, or use another datalink adapter, such as an INLINE™ 7.
> - To avoid any disruptions or download failures, using a computer with a different operating system and/or different version number and/or different datalink adapter for any ECM calibration code downloads is recommended.
>
> ### Document History
