---
type: "TSB"
doc: "tsb110295"
title_en: "Updated High Pressure Injection (HPI) Fuel System Peak Cylinder Pressure Reduction Calibration"
modified: "2011-11-07"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
families:
  - "QSK60"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2011/tsb110295.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb110295.pdf"
tags:
  - "документ/tsb"
  - "двигатель/QSK60"
  - "перевод/машинный"
---

# Updated High Pressure Injection (HPI) Fuel System Peak Cylinder Pressure Reduction Calibration

> [!abstract] TSB · `tsb110295`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]]
> **Семейство:** QSK60
> **Даты:** изменён 2011-11-07
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2011/tsb110295.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb110295.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


## Обновленная система инъекций высокого давления (HPI) для калибровки пикового цилиндрического давления

### Положение о гарантии

Сведения в этом документе не изменяют действующие гарантийные обязательства и практику ремонта и не дают оснований для работ по программам TRP или Campaign.

### Содержание

В этом документе сообщается о выпуске новых калибровок HPI для строительных двигателей QSK45/60/78, чтобы помочь в контроле избыточного давления на пиковый цилиндр (PCP) при определенных обстоятельствах.

К калибровкам были применены следующие изменения:

1. Сроки инъекций имеют различный предел, когда температура впускного коллектора ниже 4,4 ° C (40° F)
2. Были сделаны улучшения для обнаружения несоответствия между командным и фактическим временным давлением топлива. Теперь будет запущен код ошибки, код ошибки 112.
3. Стол влагостойкости был изменен для улучшения белого дыма двигателя и стабильности при легкой нагрузке и низких температурах коллектора впуска (QSK78 только).

Долговечность компонентов силового цилиндра может быть уменьшена за счет высокого PCP. В этом документе сообщается о необходимости обновления затронутых ECM с помощью этих новых калибровок HPI.

Обновлены все калибровки конструкции двигателей QSK45/60/78.

#### ESN Firsts:

- QSK45: 33189032
- QSK60: 33189295
- QSK78: 66301938.

### История изменений документа


> [!quote]- Original (English) · английский оригинал
> ## Updated High Pressure Injection (HPI) Fuel System Peak Cylinder Pressure Reduction Calibration
>
> ### Warranty Statement
>
> The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.
>
> ### Contents
>
> This document announces the release of new HPI calibrations for QSK45/60/78 construction engines to aid in the control of excessive Peak Cylinder Pressure (PCP) under specific circumstances.
>
> The following changes have been applied to the calibrations:
>
> 1. Injection timing has a varying limit when the intake manifold temperature is below 4.4°C (40°F)
> 2. Improvements have been made to detect a mismatch between commanded and actual timing fuel pressure. A fault code will now trigger, Fault Code 112.
> 3. Wetstack table has been changed to improve engine white smoke and stability at light load and low intake manifold temperatures (QSK78 **only**).
>
> The durability of the power cylinder components may be reduced by high PCP. This document informs of the need to update the affected ECMs with these new HPI calibrations.
>
> All construction HPI calibrations for QSK45/60/78 engines have been updated.
>
> #### ESN Firsts:
>
> - QSK45: 33189032
> - QSK60: 33189295
> - QSK78: 66301938.
>
> ### Document History
