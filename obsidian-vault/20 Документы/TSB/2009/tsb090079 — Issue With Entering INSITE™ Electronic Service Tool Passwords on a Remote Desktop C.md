---
aliases:
  - "Проблема ввода паролей INSITE™ через удалённый рабочий стол"
type: "TSB"
doc: "tsb090079"
title_en: "Issue With Entering INSITE™ Electronic Service Tool Passwords on a Remote Desktop Connection"
title_ru: "Проблема ввода паролей INSITE™ через удалённый рабочий стол"
released: "2009-09-24"
modified: "2009-09-24"
group: "22 - Service Tools"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
  - "35354607"
  - "35373113"
  - "37292556"
  - "37295879"
  - "71156161"
  - "80141463"
  - "80248213"
families:
  - "QSK60"
  - "QSM11"
  - "QST30"
  - "QSX15"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2009/tsb090079.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb090079.pdf"
tags:
  - "документ/tsb"
  - "двигатель/QSK60"
  - "двигатель/QSM11"
  - "двигатель/QST30"
  - "двигатель/QSX15"
  - "год/2009"
  - "перевод/машинный"
  - "тема/service-tools"
---

# Issue With Entering INSITE™ Electronic Service Tool Passwords on a Remote Desktop Connection
**Проблема ввода паролей INSITE™ через удалённый рабочий стол**

> [!abstract] TSB · `tsb090079`
> **Раздел Cummins:** 22 - Service Tools
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSK60, QSM11, QST30, QSX15
> **Даты:** выпущен 2009-09-24 · изменён 2009-09-24
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2009/tsb090079.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb090079.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


## Проблема ввода паролей INSITE™ через удалённый рабочий стол

### Суть проблемы

Это раннее уведомление о поле описывает проблему с вводом паролей электронного сервиса INSITETM на удаленном подключении к рабочему столу. Было обнаружено, что удаленное соединение с рабочим столом предотвратит доступ к инструментам и паролям электронных услуг INSITETM.

### Подтверждение

Все двигатели поддерживаются электронным сервисным оборудованием INSITETM.

При попытке открыть инструмент электронного сервиса INSITETM через удаленное соединение с рабочим столом программа предложит ввести пароль. При попытке ввести пароль, дается сообщение об ошибке, в котором говорится, что «введенный пароль недействителен», даже если пароль был проверен.

Не применяется

Не применяется

Не применяется

### Решение

Эта проблема была исправлена с помощью инструментария 7.3 для электронных услуг INSITETM и более поздних версий.

### Положение о гарантии

Сведения в этом документе не изменяют действующие гарантийные обязательства и практику ремонта и не дают оснований для работ по программам TRP или Campaign.


> [!quote]- Original (English) · английский оригинал
> ## Issue With Entering INSITE™ Electronic Service Tool Passwords on a Remote Desktop Connection
>
> ### Core Issue
>
> This Early Field Notification describes an issue with entering INSITE™ electronic service tool passwords on a remote desktop connection. It has been found that a remote desktop connection will prevent access to INSITE™ electronic service tool and passwords from being entered.
>
> ### Confirmation
>
> All engines supported by INSITE™ electronic service tool.
>
> When attempting to open INSITE™ electronic service tool through a remote desktop connection, the program will prompt for a password to be entered. When trying to enter a password, an error message is given stating that, “The password entered is invalid”, even though the password has been verified.
>
> N/A
>
> N/A
>
> N/A
>
> ### Resolution
>
> This issue was corrected with INSITE™ electronic service tool 7.3 and later versions.
>
> ### Warranty Statement
>
> The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.
