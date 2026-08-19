---
aliases:
  - "Высокий выходной ток генератора — предупреждение"
type: "Процедура"
doc: "01-fc1471"
title_en: "Generator AC Output Current High - Warning"
title_ru: "Высокий выходной ток генератора — предупреждение"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1471.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1471.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Generator AC Output Current High - Warning
**Высокий выходной ток генератора — предупреждение**

> [!abstract] Процедура · `01-fc1471`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-05-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1471.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1471.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 1471

### Высокий выходной ток генератора — предупреждение

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 1471 PID(P): СПН: ФМИ: Лампа: Предупреждение СТО: | Выходной ток переменного тока превысил порог предупреждения для высокого тока. | Никаких действий со стороны ЕКМ не предпринимается. |

![[19802906.png]]

AC Output Current Circuit (Текущая схема)

### Описание цепи

Генераторная установка вырабатывает электроэнергию. Эта мощность находится в форме трехфазного АС. Модуль управления двигателем (ECM) контролирует выходной ток переменного тока, чтобы убедиться, что он работает правильно, а производительность выходного тока генератора превысила 110 процентов от номинальной в течение не менее 60 секунд.

ECM использует этот код неисправности, чтобы сообщить оператору, когда выходной ток переменного тока проходит порог предупреждения для высокого тока.

### Расположение компонента

Справочный раздел E для определения местоположения регулятора напряжения и модуля PT/CT.

### Практические замечания

Смена генератора начинает перегружаться. Выходной ток переменного тока прошел откалиброванный порог уровня предупреждения.

Проверьте линии разделения нагрузки для правильного подключения.

См. Код устранения неполадок t05-1471.


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 1471
>
> ### Generator AC Output Current High - Warning
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 1471 PID(P): SPN: FMI: Lamp: Warning SRT: | AC output current has exceeded the warning threshold for high current. | No action is taken by the ECM. |
>
> AC Output Current Circuit
>
> ### Circuit Description
>
> The generator set produces electric power. This power is in the form of three-phase AC. The engine control module (ECM) monitors the AC output current to make certain it is operating correctly and performance of the generator output current has exceeded 110 percent of rated for at least 60 seconds.
>
> The ECM uses this fault code to tell the operator when the AC output current passes the warning threshold for high current.
>
> ### Component Location
>
> Reference Section E for location of the voltage regulator and PT/CT module.
>
> ### Shoptalk
>
> The alternator is beginning to become overloaded. The AC output current has passed the calibrated threshold for a warning level.
>
> Check load-sharing lines for proper connection.
>
> Refer to Troubleshooting Fault Code t05-1471.
