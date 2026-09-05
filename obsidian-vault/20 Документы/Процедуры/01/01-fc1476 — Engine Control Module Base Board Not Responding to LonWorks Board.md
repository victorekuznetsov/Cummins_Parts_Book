---
aliases:
  - "Базовая плата ЭБУ не отвечает плате LonWorks"
type: "Процедура"
doc: "01-fc1476"
title_en: "Engine Control Module Base Board Not Responding to LonWorks Board"
title_ru: "Базовая плата ЭБУ не отвечает плате LonWorks"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1476.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1476.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Engine Control Module Base Board Not Responding to LonWorks Board
**Базовая плата ЭБУ не отвечает плате LonWorks**

> [!abstract] Процедура · `01-fc1476`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-05-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1476.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1476.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 1476

### Базовая плата ЭБУ не отвечает плате LonWorks

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 1476 PID(P): СПН: ФМИ: Лампа: Предупреждение СТО: | Базовая плата ECM не отвечает на доску LonWorks. | Никаких действий со стороны ЕКМ не предпринимается. |

![[19802649.png]]

Генератор установил ECM-картонную клетку

### Описание цепи

Этот код неисправности используется модулем управления двигателем (ECM) для того, чтобы сообщить оператору, что базовая плата **не** отвечает на команды, отправленные через плату LonWorks.

### Расположение компонента

Справочный раздел E для определения местоположения клетки карты ECM, базовой платы и платы сети LonWorks.

### Практические замечания

Возможные режимы отказа — неправильная установка базовой платы, платы LonWorks и загрузка неправильной калибровки программного обеспечения в ECM.

См. Код устранения неполадок t05-1476.


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 1476
>
> ### Engine Control Module Base Board Not Responding to LonWorks Board
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 1476 PID(P): SPN: FMI: Lamp: Warning SRT: | ECM base board is **not** responding to the LonWorks board. | No action is taken by the ECM. |
>
> Generator Set ECM Card Cage
>
> ### Circuit Description
>
> This fault code is used by the engine control module (ECM) to tell the operator that the base board is **not** responding to commands sent via the LonWorks board.
>
> ### Component Location
>
> Reference Section E for location of the ECM card cage, the base board, and the LonWorks Network board.
>
> ### Shoptalk
>
> The possible failure modes are incorrect installation of the base board, LonWorks board, and loading an incorrect software calibration into the ECM.
>
> Refer to Troubleshooting Fault Code t05-1476.
