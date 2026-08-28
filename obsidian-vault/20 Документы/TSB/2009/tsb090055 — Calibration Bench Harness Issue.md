---
aliases:
  - "Проблема стендового калибровочного жгута"
type: "TSB"
doc: "tsb090055"
title_en: "Calibration Bench Harness Issue"
title_ru: "Проблема стендового калибровочного жгута"
released: "2009-08-04"
modified: "2009-08-04"
group: "22 - Service Tools"
engines:
  - "33224404"
  - "33239746"
  - "33239899"
  - "41340468"
  - "41349633"
  - "41353297"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
  - "QSK19"
  - "QSK50"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2009/tsb090055.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb090055.pdf"
tags:
  - "документ/tsb"
  - "двигатель/K38/K50"
  - "двигатель/QSK19"
  - "двигатель/QSK50"
  - "год/2009"
  - "перевод/машинный"
  - "тема/service-tools"
---

# Calibration Bench Harness Issue
**Проблема стендового калибровочного жгута**

> [!abstract] TSB · `tsb090055`
> **Раздел Cummins:** 22 - Service Tools
> **Двигатели:** [[33224404 — QSK50 CM2150 MCRS CPL 3391|33224404]], [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]], [[41340468 — QSK50 CM2150 MCRS CPL 3728|41340468]], [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60, QSK19, QSK50
> **Даты:** выпущен 2009-08-04 · изменён 2009-08-04
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2009/tsb090055.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb090055.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


## Проблема стендового калибровочного жгута

### Суть проблемы

В этом раннем уведомлении о полевых условиях описывается проблема с калибровочным стендом CM2150, номер детали 4918583. В настоящее время этот кабель использует Cummins® Engine Network (CEN) для соединений J1939 между электронным модулем управления CM2150 (ECM) и электронным сервисным оборудованием (например, движком). InsiteTM) вместо общедоступной сети J1939. Соединения с использованием CEN могут привести к тому, что адрес источника ECM будет отличаться от описанного в руководствах по эксплуатации, особенно для двигателей с многомодулевыми системами. Кроме того, попытки подключения, сделанные с использованием этого тест-стойки, могут быть успешными только в том случае, если попытка будет сделана в течение нескольких секунд после включения ключа.

### Подтверждение

- ISB CM2150
- ISC CM2150
- ISL CM2150
- B3.9/5.9/C8.3 CM2150
- ISDe CM2150C
- ISLE CM2150
- ISBe4 (4 и 6 цилиндров) CM2150E
- ISB4.5, 6.7 ISD4.5, 6.7 CM2150 SN (Евро 4.5)
- ISB4.5, 6.7 ISD4.5, 6.7 CM2150 SN (Евро 5)
- ISL8.9 CM2150 SN (Евро 4.5)
- ISL8.9 CM2150 SN (Евро 5)
- IsLe CM2150C
- QSB3.3 CM2150
- QSK19 CM2150 MCRS / Power Gen
- QSK38 CM2150 MCRS / Power Gen
- QSK50 CM2150 MCRS / Power Gen
- QSK60 CM2150 MCRS / Power Gen

Использование испытательного стенда калибровочной проводов, номер детали 4918583, с номером WO (перечислен в нижней части этикетки на кабеле), менее 190363, может привести к одному из следующих вопросов:

1. Откалиброванный ECM будет требовать другой адрес источника SAE J1939, как описано в руководствах по обслуживанию. Например, первичная ECM-система от многомодуля (переключается на «PRIM» на прикрепленной многомодулевой проводах) обычно требует адреса источника SAE J1939 00. В сети CEN с той же настройкой заявленный исходный адрес SAE J1939 равен 01 (что одинаково для вторичной ECM в общедоступной сети J1939).
2. ECM, который откалиброван и физически подключен к адаптеру шины данных INLINETM CAN, свет CAN/J1939 будет мигать только в течение нескольких секунд после включения ключа. Этот свет должен оставаться мигающим.

Один из симптомов, упомянутых в разделе «Симптомы и наблюдения» этого раннего уведомления о поле и кабеля, номер детали 4918583, с номером WO менее 190363.

Испытательный стенд калибровочной проводов, номер детали 4918583, использует сеть CEN для соединений J1939.

Нет.

### Решение

Испытательный стенд калибровочной электропроводки, номер детали 4918583, был перестроен для использования в общедоступной сети J1939. Эти новые кабели будут иметь номер WO 190363 или больше. Кабель с номером WO менее 190363 может быть модифицирован для использования в общедоступной сети J1939.

Для коррекции этих кабелей переместить терминал 51 в место 01 терминала и терминал 31 в терминал 21 на разъеме OEM, используя инструмент удаления терминала, номер детали 3824815 или эквивалент. Процедуру удаления терминала для разъемов DeutschTM DRC можно найти в следующем руководстве по устранению неполадок и ремонту.[[99-019-204 — Deutsch DRC Connector Series|См. процедуру 019-204 в разделе 19.]]

### Положение о гарантии

Сведения в этом документе не изменяют действующие гарантийные обязательства и практику ремонта и не дают оснований для работ по программам TRP или Campaign.


> [!quote]- Original (English) · английский оригинал
> ## Calibration Bench Harness Issue
>
> ### Core Issue
>
> This Early Field Notification describes an issue with the CM2150 calibration bench harness, Part Number 4918583. This cable presently uses the Cummins® Engine Network (CEN) for J1939 connections between a CM2150 electronic control module (ECM) and an electronic service tool (e.g. INSITE™) instead of the public J1939 network. Connections using CEN could possibly cause the ECM source address to be different than described in service manuals, specifically for engines with multi-module systems. Also, connection attempts made using this bench harness could possibly **only** succeed, if the attempt is made within a few seconds of key ON.
>
> ### Confirmation
>
> - ISB CM2150
> - ISC CM2150
> - ISL CM2150
> - B3.9/5.9/C8.3 CM2150
> - ISDe CM2150C
> - ISLe CM2150
> - ISBe4 (4 and 6 cylinder) CM2150E
> - ISB4.5, 6.7 ISD4.5, 6.7 CM2150 SN (Euro 4.5)
> - ISB4.5, 6.7 ISD4.5, 6.7 CM2150 SN (Euro 5)
> - ISL8.9 CM2150 SN (Euro 4.5)
> - ISL8.9 CM2150 SN (Euro 5)
> - ISLe CM2150C
> - QSB3.3 CM2150
> - QSK19 CM2150 MCRS / Power Gen
> - QSK38 CM2150 MCRS / Power Gen
> - QSK50 CM2150 MCRS / Power Gen
> - QSK60 CM2150 MCRS / Power Gen
>
> The use of bench calibration harness, Part Number 4918583, with a WO number (listed at the bottom of the label on the cable), less than 190363, could possibly exhibit one of the following issues:
>
> 1. An ECM that is calibrated will claim a different SAE J1939 source address as decribed in the service manuals. For example, a primary ECM from a multi-module system (switched to "PRIM" on the attached multiple module harness) normally claims SAE J1939 source address 00. On the CEN network with the same setup, the claimed SAE J1939 source address is 01 (which is the same for the secondary ECM on the public J1939 network).
> 2. An ECM that is calibrated and physically connected to an INLINE™ data link adapter, the CAN/J1939 light will **only** flash for a few seconds after a key ON. This light should remain flashing.
>
> One of the symptoms mentioned in the "Symptoms and Observations" section of this Early Field Notification and cable, Part Number 4918583, with a WO number less than 190363.
>
> Bench calibration harness, Part Number 4918583, uses the CEN network for the J1939 connections.
>
> None.
>
> ### Resolution
>
> Bench calibration harness, Part Number 4918583, has been rewired to use the public J1939 network. These new cables will have a WO number of 190363 or greater. Cables with WO number less than 190363 can be modified to use the public J1939 network.
>
> To correct these cables, move terminal 51 to terminal location 01 and terminal 31 to terminal 21 on the OEM connector, using terminal removal tool, Part Number 3824815, or equivalent. The terminal removal procedure for Deutsch™ DRC connectors can be found in the following procedure in the appropriate Troubleshooting and Repair Manual. [[99-019-204 — Deutsch DRC Connector Series|Refer to Procedure 019-204 in Section 19.]]
>
> ### Warranty Statement
>
> The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.
