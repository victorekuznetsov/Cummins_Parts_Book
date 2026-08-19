---
aliases:
  - "Низкий уровень охлаждающей жидкости — критично"
type: "Процедура"
doc: "01-fc235"
title_en: "Engine Coolant Level Low - Critical"
title_ru: "Низкий уровень охлаждающей жидкости — критично"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc235.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc235.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Engine Coolant Level Low - Critical
**Низкий уровень охлаждающей жидкости — критично**

> [!abstract] Процедура · `01-fc235`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc235.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc235.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 235

### Низкий уровень охлаждающей жидкости — критично

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 235 PID(P): СПН: ФМИ: Лампа: Отключение SRT: | Уровень охлаждающей жидкости двигателя упал ниже порога отключения для низкого уровня охлаждающей жидкости. | Двигатель отключится. |

![[19803601.png]]

Цепь датчика уровня охлаждающей жидкости

### Описание цепи

Датчик уровня охлаждающей жидкости контролирует уровень охлаждающей жидкости в системе охлаждающей жидкости и передает информацию в ECM.

### Расположение компонента

[[01-100-002-tr — Engine Diagrams|См. процедуру 100-002 (Диаграммы двигателя) в разделе Е настоящего руководства для определения местоположения компонента.]]

### Практические замечания

- Когда уровень охлаждающей жидкости падает ниже определенного уровня, будет активирован выпадение мощности, что снизит выходную мощность на 50 процентов в течение 30-секундного периода.

- Если в цепи уровня охлаждающей жидкости используется штепсель, убедитесь, что он правильно подключен. Выключатель уровня охлаждающей жидкости с высоким сигналом ** должен быть сокращен до источника питания переключателя уровня охлаждающей жидкости, а переключатель уровня охлаждающей жидкости с низким сигналом ** должен быть сокращен до возврата переключателя уровня охлаждающей жидкости.

- Осмотрите проводную упряжку между четырехсторонним разъемом и датчиком уровня охлаждающей жидкости на предмет повреждения.

См. Код устранения неполадок t05-235


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 235
>
> ### Engine Coolant Level Low - Critical
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 235 PID(P): SPN: FMI: Lamp: Shutdown SRT: | Engine coolant level has dropped below the shutdown threshold for low coolant level. | Engine will shut down. |
>
> Coolant Level Sensor Circuit
>
> ### Circuit Description
>
> The coolant level sensor monitors the coolant level within the coolant system and passes information to the ECM.
>
> ### Component Location
>
> [[01-100-002-tr — Engine Diagrams|Refer to Procedure 100-002 (Engine Diagrams) in Section E of this manual for the component location.]]
>
> ### Shoptalk
>
> - When the coolant level drops below a certain level, a power derate will be activated, which will decrease the power output by 50 percent over a 30-second period.
>
> - If a shorting plug is used in the coolant level circuit, verify that it is wired correctly. The coolant level switch high signal **must** be shorted to the coolant level switch supply and the coolant level switch low signal **must** be shorted to the coolant level switch return.
>
> - Inspect the wiring harness between the four-way connector and the coolant level sensor for damage.
>
> Refer to Troubleshooting Fault Code t05-235
