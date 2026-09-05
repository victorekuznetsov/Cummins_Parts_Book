---
aliases:
  - "Судовая защита от перегрузки — условие возникло"
type: "Процедура"
doc: "123-fc5634prop"
title_en: "Marine Overload Protection - Condition Exists"
title_ru: "Судовая защита от перегрузки — условие возникло"
modified: "2015-09-03"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4022094"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/123/123-fc5634prop.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/123-fc5634prop.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/123"
  - "перевод/машинный"
---

# Marine Overload Protection - Condition Exists
**Судовая защита от перегрузки — условие возникло**

> [!abstract] Процедура · `123-fc5634prop`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4022094 — QSK19 CM2150 and CM2670 Electronic Control System Troubleshooting and Repair Manual|4022094]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2015-09-03
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/123/123-fc5634prop.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/123-fc5634prop.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 5634

### Судовая защита от перегрузки — условие возникло

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 5634 PID(P): СПН: 520892 FMI: 14 ламп: Янтарная СРТ: | Судовая защита от перегрузки — условие возникло. Состояние перегрузки было обнаружено модулем управления двигателем (ECM). | Ни одного на выступление. |

![[00700050.png]]

Типичный регион перегрузки для применения в тяге

### Описание цепи

X - Скорость двигателя

Y - крутящий момент

1 - Кривая крутящего момента Fuel Limited

2 - кривая Пропеллера

3 - Регион перегрузки.

Затененная область на графике выше соответствует калибруемой области перегрузки. Морская защита от перегрузки контролирует двигатель, работающий в состоянии перегрузки. Эта функция необходима для ограничения воздействия двигателя в таких условиях работы, предупреждая оператора.

### Расположение компонента

Не применяется

### Условия выполнения диагностики

- Эта диагностика выполняется, когда крутящий момент двигателя превышает порог перегрузки.

### Условия установки кодов неисправностей

- ECM обнаружил значения скорости и крутящего момента в области перегрузки в течение более чем калибровочного времени.

### Действия системы при активном коде неисправности

- ECM освещает лампу янтарного CHECK ENGINE сразу же, когда диагностика проходит и выходит из строя.

### Условия сброса кода неисправности

- ECM обнаружил значения скорости и крутящего момента в нормальной операционной области в течение более чем калибруемого времени.

- Состояние кода ошибки, отображаемого инструментами электронного сервиса INSITETM, изменится на INACTIVE после запуска и прохождения диагностики.

- ECM выключит лампу янтарного CHECK ENGINE сразу после диагностических прогонов и проходов.

### Практические замечания

- Это код ошибки только для информации, который становится активным, если крутящий момент двигателя превышает порог перегрузки в течение калибруемого времени.

- Высокий уровень неактивного кода 5634 может указывать на то, что двигатель часто работает за пределами ожидаемой области. Рабочий цикл судна или оборудование, возможно, потребуется исследовать, чтобы понять состояние неисправности.

- Ремонт не требуется.

- Ссылка на Бюллетень морских приложений - 0.19.00 - Электронные системы управления двигателем для получения дополнительной информации об этой диагностике.

См. Код 5634 устранения неполадок.


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 5634
>
> ### Marine Overload Protection - Condition Exists
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 5634 PID(P): SPN: 520892 FMI: 14 Lamp: Amber SRT: | Marine Overload Protection - Condition Exists. Overload condition has been detected by the engine control module (ECM). | None on performance. |
>
> Typical Overload Region for Propulsion Application
>
> ### Circuit Description
>
> X - Engine Speed
>
> Y - Torque
>
> 1 - Fuel Limited Torque Curve
>
> 2 - Propeller Curve
>
> 3 - Overload Region.
>
> The shaded region in the graph above corresponds to the calibratable overload region. Marine Overload Protection monitors the engine operating in an overload condition. This feature is needed to limit engine exposure in such working conditions by alerting the operator.
>
> ### Component Location
>
> N/A
>
> ### Conditions For Running The Diagnostics
>
> - This diagnostic runs when the engine torque exceeds the overload threshold.
>
> ### Conditions For Setting The Fault Codes
>
> - The ECM detected speed and torque values in the overload region for more than a calibratable time.
>
> ### Action Taken When The Fault Code Is Active
>
> - The ECM illuminates the amber CHECK ENGINE lamp immediately when the diagnostic runs and fails.
>
> ### Conditions For Clearing The Fault Code
>
> - The ECM detected speed and torque values in the normal operating region for more than a calibratable time.
>
> - The fault code status displayed by INSITE™ electronic service tool will change to INACTIVE after the diagnostic runs and passes.
>
> - The ECM will turn off the amber CHECK ENGINE lamp immediately after the diagnostic runs and passes.
>
> ### Shoptalk
>
> - This is an information-only fault code that becomes active if the engine torque exceeds the overload threshold for a calibratable time.
>
> - High counts of inactive Fault Code 5634 can indicate the engine is often operated beyond the normal expected region. Vessel operating duty cycle or equipment may need to be investigated to understand fault condition.
>
> - No repairs are necessary.
>
> - Reference the Marine Application Bulletin – 0.19.00 – Electronic Engine Controls for more information on this diagnostic.
>
> Refer to Troubleshooting Fault Code 5634.
