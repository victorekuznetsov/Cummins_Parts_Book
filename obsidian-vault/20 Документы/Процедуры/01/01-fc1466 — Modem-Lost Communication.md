---
aliases:
  - "Модем — потеря связи"
type: "Процедура"
doc: "01-fc1466"
title_en: "Modem-Lost Communication"
title_ru: "Модем — потеря связи"
modified: "2010-07-29"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1466.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1466.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Modem-Lost Communication
**Модем — потеря связи**

> [!abstract] Процедура · `01-fc1466`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1466.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1466.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 1466

### Модем — потеря связи

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 1466 PID(P): СПН: ФМИ: Лампа: Предупреждение СТО: | ECM может ** не** общаться с модемом. | Никаких действий со стороны ЕКМ не предпринималось. |

![[19802919.png]]

Модемная схема

### Описание цепи

ECM проверяет модем, чтобы убедиться, что он работает правильно. ECM использует модем для информирования удаленного оператора о работе генераторной установки, производительности, настройке и диагностике. ECM контролирует модем (без связи с модемом будет срабатывать код 1466 ошибки) и может быть вызван шортами или открытиями.

### Расположение компонента

См. раздел E для определения местоположения модема.

### Практические замечания

Возможные режимы отказа - это открытая цепь, короткая к земле и потеря напряжения питания внутри ECM.

Проверьте наличие открытого, короткого замыкания на землю и свободных соединений на проводах, поставляемой клиентом, на модем.

См. Код устранения неисправностей t05-1466


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 1466
>
> ### Modem-Lost Communication
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 1466 PID(P): SPN: FMI: Lamp: Warning SRT: | ECM can **not** communicate with the modem. | No action taken by the ECM. |
>
> Modem Circuit
>
> ### Circuit Description
>
> The ECM checks the modem to make certain it is operating correctly. The ECM uses the modem to inform a remote operator about generator set operation, performance, setup, and diagnostics. The ECM monitors the modem (no communication with the modem will trip Fault Code 1466) and can be caused by shorts or opens.
>
> ### Component Location
>
> Refer to Section E for location of the modem.
>
> ### Shoptalk
>
> The possible failure modes are open circuit, short to ground, and loss of supply voltage inside the ECM.
>
> Check for open, short circuit to ground, and loose connections on customer-supplied wiring to the modem.
>
> Refer to Troubleshooting Fault Code t05-1466
