---
aliases:
  - "QSK19/38/50/60 MCRS: не отвечает управление подачей по шине данных"
type: "TSB"
doc: "tsb120296"
title_en: "QSK19/38/50/60 Modular Common Rail System (MCRS) Engine Data Link Throttle Unresponsive"
title_ru: "QSK19/38/50/60 MCRS: не отвечает управление подачей по шине данных"
released: "2012-12-11"
modified: "2012-12-11"
group: "19 - Electronic Engine Controls"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2012/tsb120296.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb120296.pdf"
tags:
  - "документ/tsb"
  - "двигатель/K38/K50"
  - "двигатель/QSK19"
  - "двигатель/QSK50"
  - "год/2012"
  - "перевод/машинный"
  - "тема/electronic-engine-controls"
---

# QSK19/38/50/60 Modular Common Rail System (MCRS) Engine Data Link Throttle Unresponsive
**QSK19/38/50/60 MCRS: не отвечает управление подачей по шине данных**

> [!abstract] TSB · `tsb120296`
> **Раздел Cummins:** 19 - Electronic Engine Controls
> **Двигатели:** [[33224404 — QSK50 CM2150 MCRS CPL 3391|33224404]], [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]], [[41340468 — QSK50 CM2150 MCRS CPL 3728|41340468]], [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60, QSK19, QSK50
> **Даты:** выпущен 2012-12-11 · изменён 2012-12-11
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2012/tsb120296.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb120296.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


## QSK19/38/50/60 MCRS: не отвечает управление подачей по шине данных

### Суть проблемы

После замены двигателя или модернизации с CM850 до CM2150 двигатель может работать нормально в режиме холостого хода, но не реагировать на сообщение TSC1 шины данных CAN. Это связано с тем, что исходное сообщение производителя оборудования (OEM) дроссельной заслонки **не** соответствует стандарту Общества автомобильных инженеров (SAE) J1939-71.

### Подтверждение

Модуль CM2150 будет принимать только сообщения с дроссельной заслонки (TSC1), которые соответствуют стандарту SAE J1939-71. Модуль CM850 будет принимать сообщения, которые были очень близки, но не идентичны стандарту SAE J1939-71.

| Формат сообщения TSC1 Примеры |  |
|---|---|
| Пример правильного формата сообщения TSC1 | Неправильный пример формата сообщения TSC1 |
| xx0000xx AA BB BB CC 00 00 **DD EE** | xx0000xx AA BB BB CC 00 00 0000 |

AA = режим управления (т.е. Скоростной лимит / Speed Limit

BB = Командовое значение скорости / ограничение

CC = момент затяжки/ограничение

DD = счетчик сообщений (**Должен быть 0xF, если не используется**)

EE = контрольная сумма (**Должна быть 0xF, если не используется**)

### Решение

Ссылка на бюллетени по устранению неполадок или технической помощи производителя оригинального оборудования (OEM) для получения информации о том, как обновить свое программное обеспечение в соответствии со стандартами SAE J1939-71.

### Положение о гарантии

Сведения в этом документе не изменяют действующие гарантийные обязательства и практику ремонта и не дают оснований для работ по программам TRP или Campaign.

### История изменений документа


> [!quote]- Original (English) · английский оригинал
> ## QSK19/38/50/60 Modular Common Rail System (MCRS) Engine Data Link Throttle Unresponsive
>
> ### Core Issue
>
> After an engine replacement or upgrade from a CM850 to a CM2150, the engine may run normally at idle, but be unresponsive to the data link throttle's TSC1 message. This is due to the original equipment manufacturer (OEM) throttle message **not** meeting the Society of Automotive Engineers (SAE) J1939-71 standard.
>
> ### Confirmation
>
> The CM2150 module will **only** accept throttle messages (TSC1) that meet SAE J1939-71 standard. The CM850 module would accept messages that were very close, but **not** identical, to the SAE J1939-71 standard.
>
> | TSC1 Message Format Examples |  |
> |---|---|
> | Correct TSC1 Message Format Example | Incorrect TSC1 Message Format Example |
> | xx0000xx AA BB BB CC 00 00 **DD EE** | xx0000xx AA BB BB CC 00 00 **0000** |
>
> AA = Control Mode (i.e. Speed Command/Speed Limit)
>
> BB = Speed Command Value/Limit
>
> CC = Torque Value/Limit
>
> DD = Message Counter (**Must be 0xF if not used**)
>
> EE = Checksum (**Must be 0xF if not used**)
>
> ### Resolution
>
> Reference the original equipment manufacturer (OEM) troubleshooting or technical service bulletins for information on how to update their software to meet SAE J1939-71 standards.
>
> ### Warranty Statement
>
> The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.
>
> ### Document History
