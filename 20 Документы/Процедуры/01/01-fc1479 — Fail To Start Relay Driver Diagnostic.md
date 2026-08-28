---
aliases:
  - "Диагностика драйвера реле «отказ пуска»"
type: "Процедура"
doc: "01-fc1479"
title_en: "Fail To Start Relay Driver Diagnostic"
title_ru: "Диагностика драйвера реле «отказ пуска»"
modified: "2012-05-08"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1479.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1479.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Fail To Start Relay Driver Diagnostic
**Диагностика драйвера реле «отказ пуска»**

> [!abstract] Процедура · `01-fc1479`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-05-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1479.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1479.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 1479

### Диагностика драйвера реле «отказ пуска»

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 1479 PID(P): СПН: ФМИ: Лампа: Предупреждение СТО: | Неспособность начать диагностику драйвера реле выявила ошибку. | Неспособность запустить реле будет работать **не** правильно. Никаких действий со стороны ЕКМ не предпринимается. Никаких потерь в производительности. |

![[19802449.png]]

Не удалось запустить ретранслятор Driver Circuit

### Описание цепи

Модуль управления энжионом (ECM) проверяет неисправный драйвер реле для поддержания правильной работы. ECM использует реле отказа запуска для информирования оператора о некритической неисправности. ECM контролирует напряжение, падение напряжения не будет сбивать код 1479 по умолчанию и может быть вызвано шортами, открытиями, плохими реле или неудачным отказом запуска драйвера реле в ECM.

### Расположение компонента

Ссылка на руководство по обслуживанию OEM для определения местоположения ECM. Ссылка на руководство по обслуживанию OEM для определения местоположения панели пользовательского интерфейса и не запуска ретрансляции.

### Практические замечания

Возможные режимы отказа - это открытая цепь, короткая к земле, выгоревшая реле и потеря напряжения питания внутри ECM.

См. Код устранения неполадок t05-1479.


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 1479
>
> ### Fail To Start Relay Driver Diagnostic
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 1479 PID(P): SPN: FMI: Lamp: Warning SRT: | Fail to start relay driver diagnostic has detected an error. | The fail to start relay will **not** function correctly. No action is taken by the ECM. No loss of performance. |
>
> Fail To Start Relay Driver Circuit
>
> ### Circuit Description
>
> The engione control module (ECM) checks the fail-to-start relay driver to sustain correct operation. The ECM uses the fail-to-start relay to inform the operator of a noncritical fault. The ECM monitors the voltage, no voltage drop will trip Fault Code 1479, and can be caused by shorts, opens, bad relays, or a failed fail to start relay driver in the ECM.
>
> ### Component Location
>
> Reference the OEM service manual for location of the ECM. Reference the OEM service manual for location of the user interface panel and the fail to start relay.
>
> ### Shoptalk
>
> The possible failure modes are open circuit, short to ground, burned-out relay, and loss of supply voltage inside the ECM.
>
> Refer to Troubleshooting Fault Code t05-1479.
