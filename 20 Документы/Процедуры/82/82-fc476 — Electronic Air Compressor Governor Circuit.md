---
aliases:
  - "Цепь электронного регулятора воздушного компрессора"
type: "Процедура"
doc: "82-fc476"
title_en: "Electronic Air Compressor Governor Circuit"
title_ru: "Цепь электронного регулятора воздушного компрессора"
modified: "2010-09-02"
engines:
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc476.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc476.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# Electronic Air Compressor Governor Circuit
**Цепь электронного регулятора воздушного компрессора**

> [!abstract] Процедура · `82-fc476`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc476.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc476.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 476

### Цепь электронного регулятора воздушного компрессора

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 476 PID(P): S089 SPN: 1351 FMI: 3/3 лампы: Желтая СТО: | Высокое напряжение или открытая схема, обнаруженная в схеме привода электронного воздушного компрессора. | Воздушный компрессор работает непрерывно или вообще не работает. |

![[19c00329.png]]

Цепь электронного регулятора воздушного компрессора

### Описание цепи

Электронный компрессорный регулятор воздуха - это устройство, используемое электронным модулем управления (ECM) для управления выходом воздушного компрессора.

### Расположение компонента

Воздушный компрессор губернатора привод расположен поверх воздушного компрессора.

### Практические замечания

Высокое напряжение может быть вызвано коротким замыканием к батарее или коротким замыканием к другому проводу в проводной упряжке.

Напряжение требуется на компрессорном регуляторе электронного воздуха, чтобы выключить компрессор. Никакое напряжение не включает компрессор.

Устранение неполадок код t05-476


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 476
>
> ### Electronic Air Compressor Governor Circuit
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 476 PID(P): S089 SPN: 1351 FMI: 3/3 Lamp: Yellow SRT: | High voltage or an open circuit detected at the electronic air compressor governor actuator circuit. | Air compressor runs continuously or **not** at all. |
>
> Electronic Air Compressor Governor Circuit
>
> ### Circuit Description
>
> The electronic air compressor governor is a device used by the electronic control module (ECM) to control the output of the air compressor.
>
> ### Component Location
>
> The air compressor governor actuator is located on top of the air compressor.
>
> ### Shoptalk
>
> High voltage can be caused by a short circuit to battery or a short circuit to another wire in the harness.
>
> Voltage is required at the electronic air compressor governor to turn the compressor off. No voltage turns the compressor on.
>
> Refer to Troubleshooting Fault Code t05-476
