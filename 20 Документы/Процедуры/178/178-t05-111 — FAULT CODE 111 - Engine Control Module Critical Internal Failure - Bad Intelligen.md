---
aliases:
  - "Код 111 — критический внутренний отказ ЭБУ"
type: "Процедура"
doc: "178-t05-111"
title_en: "FAULT CODE 111 - Engine Control Module Critical Internal Failure - Bad Intelligent Device or Component"
title_ru: "Код 111 — критический внутренний отказ ЭБУ"
modified: "2019-08-22"
engines:
  - "82099327"
families:
  - "QSB6.7"
manuals:
  - "4326169"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/178/178-t05-111.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/178-t05-111.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSB6.7"
  - "группа/178"
  - "перевод/машинный"
---

# FAULT CODE 111 - Engine Control Module Critical Internal Failure - Bad Intelligent Device or Component
**Код 111 — критический внутренний отказ ЭБУ**

> [!abstract] Процедура · `178-t05-111`
> **Двигатели:** [[82099327 — QSB6.7 CM2150 B109 CPL 4375|82099327]]
> **Семейство:** QSB6.7
> **Входит в руководства:** [[4326169 — QSB6.7 CM2150 B109 Fault Code Troubleshooting Manual|4326169]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2019-08-22
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/178/178-t05-111.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/178-t05-111.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

## Предупреждения и меры предосторожности

> [!warning] ОСТОРОЖНО
> Чтобы не повредить новый блок управления двигателем (ЭБУ), перед его заменой разберитесь со всеми остальными активными кодами неисправностей.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте ECM. |  |
|  | **СТЭП 1А.** Проверить ECM. | Код 111 неактивен? |
|  | **STEP 1B.** Проверить неактивные счета кода 111 ошибки. | Менее 3-х пунктов? |
| ШАГ 2. | Проверьте калибровку ECM и четкие коды неисправностей. |  |
|  | **STEP 2A.** Проверьте наличие обновлений калибровки ECM. | Если доступно обновление калибровки для этого кода неисправности, содержит ли ECM эту правку или выше? |
|  | **STEP 2B.** Отключить код ошибки. | Код неактивен? |

### ШАГ 1. Проверьте ECM.

#### ШАГ 1A. Проверьте ECM.

| **Условия: **Соединить все компоненты. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте ECM. Выключите замок зажигания и подождите 5 секунд. Запустите двигатель и запускайте его на холостом ходу в течение 1 минуты. | Код 111 неактивен? *Да | 1В |
| Код 111 неактивен? Заменить ЭКМ. См. процедуру 019-031 в Таблице ассоциированных процедур. | 2А |  |

#### ШАГ 1B. Проверьте неактивные счета кода 111.

| **Условия:** Включить переключатель зажигания. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте неактивные счета кода 111. Используйте инструмент электронного сервиса INSITETM для считывания неактивных чисел кода 111 ошибки. | Менее 3-х пунктов? *Да | 2 |
| Менее 3-х пунктов? Заменить ЭКМ. См. процедуру 019-031 в Таблице ассоциированных процедур. | Ремонт завершён. |  |

### ШАГ 2. Проверьте калибровку ECM и четкие коды неисправностей.

#### ШАГ 2A. Проверьте, доступно ли обновление калибровки ECM.

| **Условия: **Соединить все компоненты. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Сравните код ECM и номер пересмотра в ECM с калибровочными изменениями, перечисленными в истории калибровочных ревизий ECM, для применимых изменений, связанных с этим кодом неисправности. Используйте инструмент электронного сервиса INSITETM, чтобы найти в ECM код и номер версии. Код и номер исправления ECM находятся в разделе «Информация о калибровке» идентификатора системы и таблички в функциях и параметрах. | Если доступно обновление калибровки для этого кода неисправности, содержит ли ECM эту правку или выше? *Да | 2В |
| Если доступно обновление калибровки для этого кода неисправности, содержит ли ECM эту правку или выше? **NORepair:** При необходимости откалибровать ECM.[[105-019-032 — Engine Control Module Calibration Code\|См. процедуру 019-032 в разделе 19.]] | 2В |  |

#### ШАГ 2B. Отключите код неисправности.

| **Условия: **Соединить все компоненты. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Отключите и очистите код ошибки. Управляйте двигателем в рамках «Условий для устранения кода неисправности», найденных в разделе Обзор этой процедуры устранения неполадок. | Код неактивен? *Да | Ремонт завершён |
| Код неактивен? **NORepair:** Возврат к шагам устранения неполадок или свяжитесь с авторизованным местом ремонта Cummins®, если все шаги были завершены и проверены снова. | 1А |  |

## Связанные процедуры

| Связанные процедуры |  |  |  |
|---|---|---|---|
| Название процедуры | Процедурный номер | Модельный сервис | Номер бюллетеня |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISL8.9 CM2880 L112 | 4358493 |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISL9.5 CM2150 SN | 4310608 |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISB3.9 CM2220 B107 | 4310792 |
| Электронный блок управления двигателем | См. процедуру 019-031 | QSB4.5 CM2150 B108 | 4326163 |
| Электронный блок управления двигателем | См. процедуру 019-031 | QSB6.7 CM2150 B109 | [[4326168 — QSB6.7 CM2150 B109 Service Manual\|4326168]] |
| Электронный блок управления двигателем | См. процедуру 019-031 | QSB7 CM2880 B117 | 4358390 |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISG11 CM2880 G106 | 4332695 |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISG12 CM2880 G107 | 4332690 |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISG11 CM2880 G108 | 4332901 |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISG12 CM2880 G109 | 4332906 |
| Электронный блок управления двигателем | См. процедуру 019-031 | QSNT14 CM876 N102 | 4325993 |
| Электронный блок управления двигателем | См. процедуру 019-031 | QSF2.8 CM2880 F104 | 4332741 |
| Электронный блок управления двигателем | См. процедуру 019-031 | QSF2.8 CM2880 F108 | 4332746 |
| Электронный блок управления двигателем | См. процедуру 019-031 | QSF3.8 CM2880 F112 | 4383825 |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISB5.9 CM2880 B127 | 4383645 |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISF3.8 CM2220 F116 | 4383664 |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISB/ISD6.7 CM2880 B126 | 4383693 |
| Электронный блок управления двигателем | См. процедуру 019-031 | QSL9.3 CM2880 L113 | 4383811 |
| Электронный блок управления двигателем | См. процедуру 019-031 | QSC8.3 CM2880 C102 | 4388785 |
| Электронный блок управления двигателем | См. процедуру 019-031 | QSB5.9 CM2880 B139 | 4388870 |
| Электронный блок управления двигателем | См. процедуру 019-031 | QSB3.9 CM2880 B138 | 5411050 |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISD6.7 CM2880 D101 | 5411372 |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISF2.8 CM2220 F129 | 5411325 |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISF4.5 CM2220 F123 | 5411320 |
| Электронный блок управления двигателем | См. процедуру 019-031 | QSG12 CM2880 G112 | 4388731 |
| Электронный блок управления двигателем | См. процедуру 019-031 | ISF3.8 CM2220 F134B | 5504165 |
| Электронный блок управления двигателем | См. процедуру 019-031 | Z14 M2670 Z103B | 5504577 |
| Электронный блок управления двигателем | См. процедуру 019-031 | D6.7 CM2670 D102B | 5504515 |
| Электронный блок управления двигателем | См. процедуру 019-031 | B6.2 CM2670 B156B | 5579510 |
| Электронный блок управления двигателем | См. процедуру 019-031 | X12 CM2670 X121B | 5504455 |
| Электронный блок управления двигателем | См. процедуру 019-031 | L9 CM2670 L128B | 5504589 |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ## Warnings and Cautions
>
> **CAUTION · Осторожно**
> To reduce the possibility of damaging a new engine control module (ECM), all other active fault codes must be investigated prior to replacing the ECM.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the ECM. |  |
> |  | **STEP 1A.** Check the ECM. | Fault Code 111 inactive? |
> |  | **STEP 1B.** Check the inactive counts of Fault Code 111. | Less than 3 counts? |
> | STEP 2. | Check ECM calibration and clear fault codes. |  |
> |  | **STEP 2A.** Check if an ECM calibration update is available. | If a calibration update for this fault code is available, does the ECM contain that revision or higher? |
> |  | **STEP 2B.** Disable the fault code. | Fault code inactive? |
>
> ### STEP 1. Check the ECM.
>
> #### STEP 1A. Check the ECM.
>
> | **Conditions:** Connect all components. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the ECM. Turn the keyswitch OFF and wait 5 seconds. Start the engine and let it idle for 1 minute. | Fault Code 111 inactive? **YES** | 1B |
> | Fault Code 111 inactive? **NORepair:** Replace the ECM. Refer to Procedure 019-031 in the Associated Procedures Table. | 2A |  |
>
> #### STEP 1B. Check the inactive counts of Fault Code 111.
>
> | **Conditions:** Turn the keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the inactive counts of Fault Code 111. Use INSITE™ electronic service tool to read the inactive counts of Fault Code 111. | Less than 3 counts? **YES** | 2 |
> | Less than 3 counts? **NORepair:** Replace the ECM. Refer to Procedure 019-031 in the Associated Procedures Table. | Repair complete. |  |
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
> | Fault code inactive? **NORepair:** Return to the troubleshooting steps or contact a Cummins® Authorized Repair Location if all steps have been completed and checked again. | 1A |  |
>
> ## Associated Procedures
>
> | Associated Procedures |  |  |  |
> |---|---|---|---|
> | Procedure Title | Procedure Number | Service Model Name | Bulletin Number |
> | Engine Control Module | Refer to Procedure 019-031 | ISL8.9 CM2880 L112 | 4358493 |
> | Engine Control Module | Refer to Procedure 019-031 | ISL9.5 CM2150 SN | 4310608 |
> | Engine Control Module | Refer to Procedure 019-031 | ISB3.9 CM2220 B107 | 4310792 |
> | Engine Control Module | Refer to Procedure 019-031 | QSB4.5 CM2150 B108 | 4326163 |
> | Engine Control Module | Refer to Procedure 019-031 | QSB6.7 CM2150 B109 | [[4326168 — QSB6.7 CM2150 B109 Service Manual\|4326168]] |
> | Engine Control Module | Refer to Procedure 019-031 | QSB7 CM2880 B117 | 4358390 |
> | Engine Control Module | Refer to Procedure 019-031 | ISG11 CM2880 G106 | 4332695 |
> | Engine Control Module | Refer to Procedure 019-031 | ISG12 CM2880 G107 | 4332690 |
> | Engine Control Module | Refer to Procedure 019-031 | ISG11 CM2880 G108 | 4332901 |
> | Engine Control Module | Refer to Procedure 019-031 | ISG12 CM2880 G109 | 4332906 |
> | Engine Control Module | Refer to Procedure 019-031 | QSNT14 CM876 N102 | 4325993 |
> | Engine Control Module | Refer to Procedure 019-031 | QSF2.8 CM2880 F104 | 4332741 |
> | Engine Control Module | Refer to Procedure 019-031 | QSF2.8 CM2880 F108 | 4332746 |
> | Engine Control Module | Refer to Procedure 019-031 | QSF3.8 CM2880 F112 | 4383825 |
> | Engine Control Module | Refer to Procedure 019-031 | ISB5.9 CM2880 B127 | 4383645 |
> | Engine Control Module | Refer to Procedure 019-031 | ISF3.8 CM2220 F116 | 4383664 |
> | Engine Control Module | Refer to Procedure 019-031 | ISB/ISD6.7 CM2880 B126 | 4383693 |
> | Engine Control Module | Refer to Procedure 019-031 | QSL9.3 CM2880 L113 | 4383811 |
> | Engine Control Module | Refer to Procedure 019-031 | QSC8.3 CM2880 C102 | 4388785 |
> | Engine Control Module | Refer to Procedure 019-031 | QSB5.9 CM2880 B139 | 4388870 |
> | Engine Control Module | Refer to Procedure 019-031 | QSB3.9 CM2880 B138 | 5411050 |
> | Engine Control Module | Refer to Procedure 019-031 | ISD6.7 CM2880 D101 | 5411372 |
> | Engine Control Module | Refer to Procedure 019-031 | ISF2.8 CM2220 F129 | 5411325 |
> | Engine Control Module | Refer to Procedure 019-031 | ISF4.5 CM2220 F123 | 5411320 |
> | Engine Control Module | Refer to Procedure 019-031 | QSG12 CM2880 G112 | 4388731 |
> | Engine Control Module | Refer to Procedure 019-031 | ISF3.8 CM2220 F134B | 5504165 |
> | Engine Control Module | Refer to Procedure 019-031 | Z14 CM2670 Z103B | 5504577 |
> | Engine Control Module | Refer to Procedure 019-031 | D6.7 CM2670 D102B | 5504515 |
> | Engine Control Module | Refer to Procedure 019-031 | B6.2 CM2670 B156B | 5579510 |
> | Engine Control Module | Refer to Procedure 019-031 | X12 CM2670 X121B | 5504455 |
> | Engine Control Module | Refer to Procedure 019-031 | L9 CM2670 L128B | 5504589 |
