---
aliases:
  - "Код 5633 — судовая защита от малой нагрузки — условие возникло"
type: "Процедура"
doc: "00-t05-5633"
title_en: "FAULT CODE 5633 - Marine Low Load Protection - Condition Exists"
title_ru: "Код 5633 — судовая защита от малой нагрузки — условие возникло"
modified: "2016-11-02"
engines:
  - "33239746"
  - "33239899"
  - "41349633"
  - "41353297"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
  - "QSK19"
manuals:
  - "4022094"
  - "4022102"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/00/00-t05-5633.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/00-t05-5633.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "двигатель/QSK19"
  - "группа/00"
  - "перевод/машинный"
---

# FAULT CODE 5633 - Marine Low Load Protection - Condition Exists
**Код 5633 — судовая защита от малой нагрузки — условие возникло**

> [!abstract] Процедура · `00-t05-5633`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]], [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60, QSK19
> **Входит в руководства:** [[4022094 — QSK19 CM2150 and CM2670 Electronic Control System Troubleshooting and Repair Manual|4022094]], [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M|4022102]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2016-11-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/00/00-t05-5633.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/00-t05-5633.pdf)

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
| ШАГ 1. | Проверьте коды неисправностей. |  |
|  | **СТЭП 1А.** Прочитайте коды неисправностей. | Код ошибки 5633 активен? |
| ШАГ 2. | Проверьте калибровку модуля управления двигателем (ECM) и четкие коды неисправностей. |  |
|  | **STEP 2A.** Проверьте наличие обновлений калибровки ECM. | Если доступно обновление калибровки для этого кода неисправности, содержит ли ECM эту правку или выше? |
|  | **STEP 2B.** Отключить код ошибки. | Код неактивен? |

### ШАГ 1. Проверьте коды неисправностей.

#### ШАГ 1A. Считайте коды неисправностей.

| **Условия:** Включить переключатель зажигания. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверить код ошибки 5633. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. Проверьте другие активные коды неисправностей. | Код ошибки 5633 активен? **Ремонт: **Это код ошибки **только**, который будет активирован только , если крутящий момент двигателя превышает порог перегрузки в течение калибровочного времени. Устранение неполадок во всех других активных кодах неисправностей. Этот код неисправности становится неактивным, когда все другие коды неисправностей будут устранены. | 2А |
| Код ошибки 5633 активен? **НЕТ** | 2А |  |

### ШАГ 2. Проверьте калибровку ECM и четкие коды неисправностей.

#### ШАГ 2A. Проверьте, доступно ли обновление калибровки ECM.

| **Условия:** Соединить все компоненты. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Сравните код ECM и номер пересмотра в ECM с калибровочными изменениями, перечисленными в истории калибровочных ревизий ECM, для применимых изменений, связанных с этим кодом неисправности. Используйте инструмент электронного сервиса INSITETM, чтобы найти в ECM код и номер версии. Код и номер исправления ECM находятся в разделе «Информация о калибровке» идентификатора системы и таблички данных в функциях и параметрах. | Если доступно обновление калибровки для этого кода неисправности, содержит ли ECM эту правку или выше? *Да | 2В |
| Если доступно обновление калибровки для этого кода неисправности, содержит ли ECM эту правку или выше? **NORepair:** При необходимости откалибровать ECM.[[105-019-032 — Engine Control Module Calibration Code\|См. процедуру 019-032 в разделе 19.]] | 2В |  |

#### ШАГ 2B. Отключите код неисправности.

| **Условия:** Соединить все компоненты. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Отключите и очистите код ошибки. Управляйте двигателем в рамках «Условий для устранения кода неисправности», найденных в разделе Обзор этой процедуры устранения неполадок. | Код неактивен? *Да | Ремонт завершён |
| Код неактивен? **НЕТ** | Следите за процессом технической эскалации. |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the fault codes. |  |
> |  | **STEP 1A.** Read the fault codes. | Fault Code 5633 active? |
> | STEP 2. | Check engine control module (ECM) calibration and clear fault codes. |  |
> |  | **STEP 2A.** Check if an ECM calibration update is available. | If a calibration update for this fault code is available, does the ECM contain that revision or higher? |
> |  | **STEP 2B.** Disable the fault code. | Fault code inactive? |
>
> ### STEP 1. Check the fault codes.
>
> #### STEP 1A. Read the fault codes.
>
> | **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for Fault Code 5633. Use INSITE™ electronic service tool to read the fault codes. Check for other active fault codes. | Fault Code 5633 active? **YESRepair:** This is an information- **only** fault code that will **only** become active if the engine torque exceeds the overload threshold for a calibratable time. Troubleshoot all other active fault codes. This fault code will become inactive when all other active fault codes are resolved. | 2A |
> | Fault Code 5633 active? **NO** | 2A |  |
>
> ### STEP 2. Check ECM calibration and clear fault codes.
>
> #### STEP 2A. Check if an ECM calibration update is available.
>
> | **Conditions:** Connect all components. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Compare the ECM code and revision number in the ECM to the calibration revisions listed in the ECM Calibration Revision History for applicable changes related to this fault code. Use INSITE™ electronic service tool to find the present ECM code and revision number in the ECM. The ECM code and revision number are found in the Calibration Information section of System ID and Dataplate in Features and Parameters. | If a calibration update for this fault code is available, does the ECM contain that revision or higher? **YES** | 2B |
> | If a calibration update for this fault code is available, does the ECM contain that revision or higher? **NORepair:** If necessary, calibrate the ECM. [[105-019-032 — Engine Control Module Calibration Code\|Refer to Procedure 019-032 in Section 19.]] | 2B |  |
>
> #### STEP 2B. Disable the fault code.
>
> | **Conditions:** Connect all components. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Disable and clear the fault code. Operate the engine within the "Conditions for Clearing the Fault Code" found in the Overview section of this troubleshooting procedure. | Fault code inactive? **YES** | Repair complete |
> | Fault code inactive? **NO** | Follow the technical escalation process. |  |
