---
aliases:
  - "Повышенный ток в цепи массы — условие возникло"
type: "Процедура"
doc: "01-fc1462"
title_en: "High Current on Ground Circuit - Condition Exists"
title_ru: "Повышенный ток в цепи массы — условие возникло"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1462.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1462.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# High Current on Ground Circuit - Condition Exists
**Повышенный ток в цепи массы — условие возникло**

> [!abstract] Процедура · `01-fc1462`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-05-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1462.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1462.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 1462

### Повышенный ток в цепи массы — условие возникло

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 1462 PID(P): СПН: ФМИ: Лампа: Предупреждение СТО: | Электрическая наземная цепь имеет высокий ток. | Калибровка зависит от действий, предпринятых ECM или отключение двигателя. |

![[17600025.png]]

Наземная схема генератора

### Описание цепи

Электроника с генераторным набором имеет общую схему. Модуль управления двигателем (ECM) контролирует цепь земли; когда происходит состояние высокого тока, ECM задает неисправность на активную. Высокий ток на общей почве может оказать неопределимое влияние на систему управления.

### Расположение компонента

Справочный раздел E для определения местоположения клетки карты ECM.

Справочный раздел E для чертежей общей схемы для электроники ECM.

### Практические замечания

Возможные режимы - грязный или неправильный грунт и провод питания напряжения, закороченный к наземному проводу.

См. Код устранения неполадок t05-1462.


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 1462
>
> ### High Current on Ground Circuit - Condition Exists
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 1462 PID(P): SPN: FMI: Lamp: Warning SRT: | Electric ground circuit has a high current. | Calibration-dependent no action taken by the ECM, or engine shutdown. |
>
> Generator Ground Circuit
>
> ### Circuit Description
>
> The generator-set electronics have a common ground circuit. The engine control module (ECM) monitors the ground circuit; when a high current condition occurs, the ECM will set the fault to active. High current on the common ground could have undefinable effects on the control system.
>
> ### Component Location
>
> Reference Section E for location of the ECM card cage.
>
> Reference Section E for drawings of the common ground circuit for the ECM electronics.
>
> ### Shoptalk
>
> The possible modes are a dirty or improper ground and a voltage supply wire shorted to a ground wire.
>
> Refer to Troubleshooting Fault Code t05-1462.
