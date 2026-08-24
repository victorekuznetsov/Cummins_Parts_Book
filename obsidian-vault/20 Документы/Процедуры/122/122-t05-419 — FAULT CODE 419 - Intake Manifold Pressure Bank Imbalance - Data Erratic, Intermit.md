---
aliases:
  - "Код 419 — разбаланс давления коллекторов рядов — данные нестабильны или неверны"
type: "Процедура"
doc: "122-t05-419"
title_en: "FAULT CODE 419 - Intake Manifold Pressure Bank Imbalance - Data Erratic, Intermittent, or Incorrect"
title_ru: "Код 419 — разбаланс давления коллекторов рядов — данные нестабильны или неверны"
modified: "2015-06-25"
engines:
  - "33239746"
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
manuals:
  - "4022102"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-t05-419.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/122-t05-419.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/122"
  - "перевод/машинный"
---

# FAULT CODE 419 - Intake Manifold Pressure Bank Imbalance - Data Erratic, Intermittent, or Incorrect
**Код 419 — разбаланс давления коллекторов рядов — данные нестабильны или неверны**

> [!abstract] Процедура · `122-t05-419`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Входит в руководства:** [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M|4022102]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2015-06-25
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-t05-419.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/122-t05-419.pdf)

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
| ШАГ 1. | Проверьте клапан отключения воздуха. |  |
|  | **ШАГ 1А.** Проверить положение клапана отключения воздуха. | Запорный клапан с включенным/закрытым воздухом? |
| ШАГ 2. | Проверьте турбированный импеллер. |  |
|  | **ШАГ 2А.** Проверить турбированный привод на предмет повреждения. | Поврежденные лопасти импеллера? |
| ШАГ 3. | Проверить датчик давления. |  |
|  | **STEP 3A.** Валидировать показания датчиков давления. | Считывание инструментария электронного сервиса INSITETM находится в пределах 102 мм рт.ст. \[4 in-Hg\] механического калибра? |
| ШАГ 4. | Проверьте форсунка |  |
|  | **STEP 4A.** Проверка неисправности форсунки. | Низкие показатели температуры выхлопных газов на нескольких цилиндрах на одном берегу? |
| ШАГ 5. | Проверьте калибровку модуля управления двигателем (ECM) и четкие коды неисправностей. |  |
|  | **STEP 5A.** Проверьте наличие обновлений калибровки ECM. | Если доступно обновление калибровки для этого кода неисправности, содержит ли ECM эту правку или выше? |
|  | **STEP 5B.** Отключить код ошибки. | Код неактивен? |

### ШАГ 1. Проверьте клапан отключения воздуха.

#### ШАГ 1A. Проверьте положение клапана отключения воздуха.

| **Условия:** Выключите замок зажигания. Переключитесь на режим «Стоп/Стоп/Авто» |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте положение клапана отключения воздуха. Есть ли закрытый клапан для отключения воздуха? | Закрытый/приводимый в действие клапан. *** Ремонт: ** Запорный клапан открытого воздуха. См. сервисную документацию изготовителя оборудования. | 2А |
| Закрытый/приводимый в действие клапан. ** НЕТ** | 2А |  |

### ШАГ 2. Проверьте турбированный импеллер.

#### ШАГ 2A. Проверить турбированный импеллер на предмет повреждения.

| **Условия:** Замок зажигания выключен/изолирован. Удалите впускную трубку с обоих турбокомпрессоров. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверить турбированный импеллер. Проверить лопасти турбокомпрессора на наличие признаков повреждения. | Поврежденные лопасти импеллера? *** Заменить турбокомпрессор. Используйте следующую процедуру в руководстве по обслуживанию K38, K50, QSK38 и QSK50, в бюллетене [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]].[[28-010-033-tr — Turbocharger\|См. процедуру 010-033 в разделе 10.]] | 3А |
| Поврежденные лопасти импеллера? ** НЕТ** | 3А |  |

### ШАГ 3. Проверить показания датчиков давления.

#### ШАГ 3A. Проверить показания датчиков давления.

| **Условия:** Включить переключатель зажигания. Подключите инструмент электронного сервиса INSITETM. Установите механическую измерительную манометрию давления на впускной коллектор. Управляйте двигателем. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте показания датчика давления наддува.. Используйте инструмент электронного обслуживания INSITETM для мониторинга датчиков давления впускного коллектора 1 и 2. Сравните показания давления впускного коллектора электронного оборудования INSITETM с механическим измерительным манометрическим давлением. Работайте с двигателем под нагрузкой. | Считывание инструментария электронного сервиса INSITETM находится в пределах 102 мм рт.ст. \[4 in-Hg\] механического измерительного манометрического давления? *Да** | 4А |
| Считывание инструментария электронного сервиса INSITETM находится в пределах 102 мм рт.ст. \[4 in-Hg\] механического измерительного манометрического давления? **NORepair:** Заменить датчик давления коллектора впуска. См. процедуру 019-061 в разделе 19. | 4А |  |

### ШАГ 4. Проверьте форсунка.

#### ШАГ 4A. Проверьте неисправность форсунки.

| **Условия: ** Соединить все компоненты. Подключите инструмент электронного сервиса INSITETM. Переключитесь на положение RUN / Stop / Auto. Включите зажигание. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте неисправность форсунки. Используйте электронный сервисный инструмент INSITETM для мониторинга всех показаний датчиков температуры выхлопных газов. Ищите несколько показаний низкой температуры выхлопных газов на одном и том же банке. | Несколько показаний низкой температуры выхлопных газов на одном и том же банке? *** Подтвердите, что форсунка работает правильно. | Перейдите к соответствующей процедуре устранения неисправностей кода неисправности в разделе TT. |
| Несколько показаний низкой температуры выхлопных газов на одном и том же банке? ** НЕТ** | 5а |  |

### ШАГ 5. Проверьте калибровку модуля управления двигателем (ECM) и четкие коды неисправностей.

#### ШАГ 5A. Проверьте, доступно ли обновление калибровки ECM.

| **Условия: ** Соединить все компоненты. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Сравните код ECM и номер пересмотра в ECM с калибровочными изменениями, перечисленными в истории калибровочных ревизий ECM, для применимых изменений, связанных с этим кодом неисправности. Используйте инструмент электронного сервиса INSITETM, чтобы найти в ECM код и номер версии. Код и номер исправления ECM находятся в разделе «Информация о калибровке» идентификатора системы и таблички данных в функциях и параметрах. | Если доступно обновление калибровки для этого кода неисправности, содержит ли ECM эту правку или выше? *Да** | 5В |
| Если доступно обновление калибровки для этого кода неисправности, содержит ли ECM эту правку или выше? **NORepair:** При необходимости откалибровать ECM.[[105-019-032 — Engine Control Module Calibration Code\|См. процедуру 019-032 в разделе 19.]] | 5В |  |

#### ШАГ 5B. Отключите код неисправности.

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
> | STEP 1. | Check air shutoff valve. |  |
> |  | **STEP 1A.** Check air shutoff valve position. | Air shutoff valve actuated/closed? |
> | STEP 2. | Inspect the turbocharged impeller. |  |
> |  | **STEP 2A.** Inspect turbocharged impeller for damage. | Damaged impeller blades? |
> | STEP 3. | Validate the boost pressure sensor. |  |
> |  | **STEP 3A.** Validate boost pressure sensor readings. | INSITE™ electronic service tool reading is within 102 mm-Hg \[4 in-Hg\] of the mechanical gauge? |
> | STEP 4. | Check the injectors |  |
> |  | **STEP 4A.** Check for malfunctioning injectors. | Low exhaust gas temperature readings on multiple cylinders on same bank? |
> | STEP 5. | Check engine control module (ECM) calibration and clear fault codes. |  |
> |  | **STEP 5A.** Check if an ECM calibration update is available. | If a calibration update for this fault code is available, does the ECM contain that revision or higher? |
> |  | **STEP 5B.** Disable the fault code. | Fault code inactive? |
>
> ### STEP 1. Check air shut off valve.
>
> #### STEP 1A. Check air shutoff valve position.
>
> | **Conditions:** Turn keyswitch OFF. Turn run/stop/auto switch to STOP position. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the air shut off valve position. Is there a closed air shut off valve? | Air shut off valve actuated/closed? **YESRepair:** Open air shutoff valve. See equipment manufacturer service information. | 2A |
> | Air shut off valve actuated/closed? **NO** | 2A |  |
>
> ### STEP 2. Inspect the turbocharged impeller.
>
> #### STEP 2A. Inspect turbocharged impeller for damage.
>
> | **Conditions:** Turn keyswitch OFF/isolated. Remove intake tubing from both turbochargers. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect turbocharged impeller. Inspect turbocharger impeller blades for signs of damage. | Damaged impeller blades? **YESRepair:** Replace the turbocharger. Use the following procedure in the K38, K50, QSK38, and QSK50 Service Manual, Bulletin [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]]. [[28-010-033-tr — Turbocharger\|Refer to Procedure 010-033 in Section 10.]] | 3A |
> | Damaged impeller blades? **NO** | 3A |  |
>
> ### STEP 3. Validate boost pressure sensor readings.
>
> #### STEP 3A. Validate boost pressure sensor readings.
>
> | **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. Install a mechanical pressure gauge to the intake manifold. Operate the engine. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Verify the boost pressure sensor readings.. Use INSITE™ electronic service tool to monitor the intake manifold 1 and 2 pressure sensors. Compare INSITE™ electronic service tool intake manifold pressure readings with the mechanical gauge pressure. Operate the engine under load. | INSITE™ electronic service tool reading is within 102 mm-Hg \[4 in-Hg\] of the mechanical gauge pressure? **YES** | 4A |
> | INSITE™ electronic service tool reading is within 102 mm-Hg \[4 in-Hg\] of the mechanical gauge pressure? **NORepair:** Replace the intake manifold pressure sensor. Refer to Procedure 019-061 in Section 19. | 4A |  |
>
> ### STEP 4. Check for injectors.
>
> #### STEP 4A. Check for malfunctioning injectors.
>
> | **Conditions:** Connect all components. Connect INSITE™ electronic service tool. Turn run/stop/auto switch to RUN position. Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for malfunctioning injectors. Use INSITE™ electronic service tool to monitor all exhaust gas temperature sensor readings. Look for multiple low exhaust gas temperature readings on the same bank. | Multiple low exhaust gas temperature readings on same bank? **YESRepair:** Confirm the injectors are functioning correctly. | Go to the appropriate fault code troubleshooting procedure within Section TT. |
> | Multiple low exhaust gas temperature readings on same bank? **NO** | 5A |  |
>
> ### STEP 5. Check engine control module (ECM) calibration and clear fault codes.
>
> #### STEP 5A. Check if an ECM calibration update is available.
>
> | **Conditions:** Connect all components. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Compare the ECM code and revision number in the ECM to the calibration revisions listed in the ECM Calibration Revision History for applicable changes related to this fault code. Use INSITE™ electronic service tool to find the present ECM code and revision number in the ECM. The ECM code and revision number are found in the Calibration Information section of System ID and Dataplate in Features and Parameters. | If a calibration update for this fault code is available, does the ECM contain that revision or higher? **YES** | 5B |
> | If a calibration update for this fault code is available, does the ECM contain that revision or higher? **NORepair:** If necessary, calibrate the ECM. [[105-019-032 — Engine Control Module Calibration Code\|Refer to Procedure 019-032 in Section 19.]] | 5B |  |
>
> #### STEP 5B. Disable the fault code.
>
> | **Conditions:** Connect all components. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Disable and clear the fault code. Operate the engine within the "Conditions for Clearing the Fault Code" found in the Overview section of this troubleshooting procedure. | Fault code inactive? **YES** | Repair Complete |
> | Fault code inactive? **NORepair:** Return to the troubleshooting steps or contact a Cummins® Authorized Repair Location if all steps have been completed and checked again. | 1A |  |
