---
aliases:
  - "Регулятор напряжения"
type: "Процедура"
doc: "01-fc1329"
title_en: "Voltage Regulator"
title_ru: "Регулятор напряжения"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1329.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1329.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
  - "перевод/машинный"
---

# Voltage Regulator
**Регулятор напряжения**

> [!abstract] Процедура · `01-fc1329`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1329.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1329.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 1329

### Регулятор напряжения

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 1329 PID(P): СПН: ФМИ: Лампа: Предупреждение СТО: | Регулятор напряжения потерял свой источник питания постоянного тока. | Регулятор напряжения ** не** сможет регулировать выходное напряжение генераторной установки. Возможен низкий уровень напряжения переменного тока (код ошибки 1447). |

![[19802802.png]]

Схема регулятора напряжения

### Описание цепи

ECM использует этот код неисправности, чтобы сообщить оператору, что базовая плата может ** не** приводить мощность постоянного тока в регулятор напряжения.

### Расположение компонента

См. раздел E для определения местоположения регулятора напряжения.

### Практические замечания

Возможные режимы отказа - это открытый контур, короткое замыкание, короткое к земле, внутренние шорты к регулятору напряжения или базовой плате или плохой диод.

См. Код устранения неисправностей t05-1329


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 1329
>
> ### Voltage Regulator
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 1329 PID(P): SPN: FMI: Lamp: Warning SRT: | The voltage regulator has lost its DC power supply. | The voltage regulator will **not** be able to regulate generator set output voltage. Possible low AC voltage (Fault Code 1447) condition can occur. |
>
> Voltage Regulator Circuit
>
> ### Circuit Description
>
> The ECM uses this fault code to inform the operator that the base board can **not** drive DC power to the voltage regulator.
>
> ### Component Location
>
> Refer to Section E for location of the voltage regulator.
>
> ### Shoptalk
>
> The possible failure modes are open circuit, short circuit, short to ground, internal shorts to the voltage regulator or base board, or bad diode.
>
> Refer to Troubleshooting Fault Code t05-1329
