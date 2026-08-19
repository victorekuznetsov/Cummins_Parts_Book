---
aliases:
  - "Код 418 — индикатор воды в топливе выше нормы — низший уровень"
type: "Процедура"
doc: "123-t05-418"
title_en: "FAULT CODE 418 – Water In Fuel Indicator - Data Valid But Above Normal Operating Range - Least Severe Level"
title_ru: "Код 418 — индикатор воды в топливе выше нормы — низший уровень"
modified: "2015-11-17"
engines:
  - "41349633"
families:
  - "QSK19"
manuals:
  - "4022094"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/123/123-t05-418.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/123-t05-418.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/123"
  - "перевод/машинный"
---

# FAULT CODE 418 – Water In Fuel Indicator - Data Valid But Above Normal Operating Range - Least Severe Level
**Код 418 — индикатор воды в топливе выше нормы — низший уровень**

> [!abstract] Процедура · `123-t05-418`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4022094 — QSK19 CM2150 and CM2670 Electronic Control System Troubleshooting and Repair Manual|4022094]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2015-11-17
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/123/123-t05-418.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/123-t05-418.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте коды неисправностей |  |
|  | **ШАГ 1А.** Проверить код 418 ошибки. | Активный или неактивный код 418. |
| ШАГ 2. | Проверьте калибровку модуля управления двигателем (ECM) и четкие коды неисправностей. |  |
|  | **STEP 2A.** Проверьте наличие обновлений калибровки ECM. | Если доступно обновление калибровки для этого кода неисправности, содержит ли ECM эту правку или выше? |
|  | **STEP 2B.** Отключить код ошибки. | Код неактивен? |

### ШАГ 1. Проверьте коды неисправностей

#### ШАГ 1A. Проверить код 418.

| **Условия:** Включить переключатель зажигания. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте коды неисправностей. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Активный или неактивный код 418. *** Ремонт: ** Слить воду из топливного фильтра. | 2А |
| Активный или неактивный код 418. ** НЕТ** | Ремонт завершён |  |

### ШАГ 2. Проверьте калибровку ECM и четкие коды неисправностей.

#### ШАГ 2A. Проверьте, доступно ли обновление калибровки ECM.

| **Условия: ** Соединить все компоненты. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Сравните код ECM и номер пересмотра в ECM с калибровочными изменениями, перечисленными в истории калибровочных ревизий ECM, для применимых изменений, связанных с этим кодом неисправности. Используйте инструмент электронного сервиса INSITETM, чтобы найти в ECM код и номер версии. Код ECM и номер версии находятся в разделе Калибровочная информация идентификатора системы и таблички в характеристиках и параметрах. | Если доступно обновление калибровки для этого кода неисправности, содержит ли ECM эту правку или выше? *Да** | 2В |
| Если доступно обновление калибровки для этого кода неисправности, содержит ли ECM эту правку или выше? **NORepair:** При необходимости откалибровать ECM.[[105-019-032 — Engine Control Module Calibration Code\|См. процедуру 019-032 в разделе 19.]]. | 2В |  |

#### ШАГ 2B. Отключите код неисправности.

| **Условия: ** Соединить все компоненты. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Отключите и очистите код ошибки. Управляйте двигателем в рамках «Условий для устранения кода неисправности», найденных в разделе Обзор этой процедуры устранения неполадок. | Код неактивен? *Да** | Ремонт завершён |
| Код неактивен? **NORepair:** Возврат к шагам устранения неполадок или свяжитесь с авторизованным местом ремонта Cummins®, если все шаги были завершены и проверены снова. | 1А |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the fault codes |  |
> |  | **STEP 1A.** Check for Fault Code 418. | Active or inactive counts of Fault Code 418? |
> | STEP 2. | Check engine control module (ECM) calibration and clear fault codes. |  |
> |  | **STEP 2A.** Check if an ECM calibration update is available. | If a calibration update for this fault code is available, does the ECM contain that revision or higher? |
> |  | **STEP 2B.** Disable the fault code. | Fault code inactive? |
>
> ### STEP 1. Check the fault codes
>
> #### STEP 1A. Check for Fault Code 418.
>
> | **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for fault codes. Use INSITE™ electronic service tool to read the fault codes. | Active or inactive counts of Fault Code 418? **YESRepair:** Drain the water from the fuel filter. | 2A |
> | Active or inactive counts of Fault Code 418? **NO** | Repair complete |  |
>
> ### STEP 2. Check ECM calibration and clear fault codes.
>
> #### STEP 2A. Check if an ECM calibration update is available.
>
> | **Conditions:** Connect all components. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Compare the ECM code and revision number in the ECM to the calibration revisions listed in the ECM Calibration Revision History for applicable changes related to this fault code. Use INSITE™ electronic service tool to find the present ECM code and revision number in the ECM. The ECM code and revision number are found in the Calibration Information section of System ID and Dataplate in Features and Parameters | If a calibration update for this fault code is available, does the ECM contain that revision or higher? **YES** | 2B |
> | If a calibration update for this fault code is available, does the ECM contain that revision or higher? **NORepair:** If necessary, calibrate the ECM. [[105-019-032 — Engine Control Module Calibration Code\|Refer to Procedure 019-032 in Section 19]]. | 2B |  |
>
> #### STEP 2B. Disable the fault code.
>
> | **Conditions:** Connect all components. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Disable and clear the fault code. Operate the engine within the "Conditions for Clearing the Fault Code" found in the Overview section of this troubleshooting procedure. | Fault code inactive? **YES** | Repair Complete |
> | Fault code inactive? **NORepair:** Return to the troubleshooting steps or contact a Cummins® Authorized Repair Location, if all the steps have been completed and checked again. | 1A |  |
