---
aliases:
  - "Код 559 — давление в топливной рампе 1 ниже нормы — умеренный уровень"
type: "Процедура"
doc: "122-t05-559"
title_en: "FAULT CODE 559 - Injector Metering Rail 1 Pressure - Data Valid But Below Normal Operating Range - Moderately Severe Level"
title_ru: "Код 559 — давление в топливной рампе 1 ниже нормы — умеренный уровень"
modified: "2015-04-07"
engines:
  - "33239746"
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
manuals:
  - "4022102"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-t05-559.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/122-t05-559.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/122"
  - "перевод/машинный"
---

# FAULT CODE 559 - Injector Metering Rail 1 Pressure - Data Valid But Below Normal Operating Range - Moderately Severe Level
**Код 559 — давление в топливной рампе 1 ниже нормы — умеренный уровень**

> [!abstract] Процедура · `122-t05-559`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Входит в руководства:** [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M|4022102]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2015-04-07
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-t05-559.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/122-t05-559.pdf)

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

> [!warning] ОСТОРОЖНО
> Чтобы не повредить контакты и жгут, при измерениях пользуйтесь следующими измерительными проводами: Номер детали 3822758 — пробный щуп типа штепсельной затворки DeutschTM/AMPTM/Metri-PackTM, номер детали 3823996 — гнездовой пробный щуп Weather-PackTM, а номер детали 3824774 — проводной ответвление жгута.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте коды неисправностей. |  |
|  | **СТЭП 1А.** Прочитайте коды неисправностей. | Код 451, 452, 2215, 2261 или 2262 активных или многих неактивных счетов Кода 451, 452, 2215, 2261 или 2262? |
| ШАГ 2. | Очистить работу топливной системы высокого давления. |  |
|  | **ШАГ 2А.** Проверить наличие внешней утечки. | Внешние утечки топлива? |
|  | **ШАГ 2В.** Проверка воздуха в топливе. | Воздух, присутствующий в линии расхода топлива? |
|  | **STEP 2C** Проверьте ограничение топливного фильтра 1-й ступени. | Ограничение топливных фильтров меньше, чем спецификации |
|  | **STEP 2D.** Проверьте ограничение топливного фильтра 2-й ступени. | Ограничение топливных фильтров меньше, чем спецификации |
|  | **ШАГ 2Е.** Проверить работу механического клапана сброса. | Протекает механический клапан? |
|  | **ШАГ 2Е.** Проверить работу топливного насоса нажимной сборки. | Код 559 ошибки активирован? |
| ШАГ 3. | Сбросьте коды неисправностей. |  |
|  | **STEP 3A.** Отключить коды неисправностей. | Код 559 неактивен? |
|  | **СТЭП 3А.** Очистить коды неисправностей. | Все коды неисправностей очищены? |

### ШАГ 1. Проверьте коды неисправностей.

#### ШАГ 1A. Считайте коды неисправностей.

| **Условия:** Включить переключатель зажигания. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Считайте коды неисправностей. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Код 451, 452, 2215, 2261 или 2262 активных или многих неактивных счетов Кода 451, 452, 2261 или 2262? *Да** | Правильное дерево для устранения неполадок |
| Код 451, 452, 2215, 2261 или 2262 активен или существует много неактивных счетов Кода 451, 452, 2261 или 2262? ** НЕТ** | 2А |  |

### ШАГ 2. Очистить работу топливной системы высокого давления.

#### ШАГ 2A. Проверьте внешнюю утечку.

| **Условия: ** Работа двигателя. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте внешние утечки топлива. Запустите двигатель и запускайте его на холостом ходу. Проверка внешних утечек топлива. | Внешние утечки топлива? *** Ремонт: ** Ремонт всех утечек топлива. Ссылка на QSK19, QSK19 CM850 MCRS и QSK19 CM2150 Modular Common Rail System Service Manual, Bulletin 4021592. | 3А |
| Внешние утечки топлива? ** НЕТ** | 2В |  |

#### ШАГ 2B. Проверьте воздух в топливе.

| ** Условия:** Удалить линию кровотока воздуха из клапана с воздушным кровотоком на блоке коллектора слива топлива. Проведите линию воздушного кровотечения в подходящий контейнер для сбора топлива. Включите зажигание. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте расход топлива для воздуха. Используйте следующую процедуру в Руководстве по обслуживанию, K38, K50, QSK38 и QSK50, Вестник 4021528.[[28-006-003 — Air in Fuel\|См. процедуру 006-003 в разделе 6.]]Используйте следующую процедуру в Руководстве по обслуживанию, QSK45 и QSK60, Вестник 4021530. См. процедуру 006-003 в разделе 6. | Воздух, присутствующий в линии расхода топлива? *** Ремонт:** Ремонт или замена поврежденной линии или свободного соединения. См. процедуру 006-024 в Таблице ассоциированных процедур. | 3А |
| Воздух, присутствующий в линии расхода топлива? ** НЕТ** | 2C |  |

#### ШАГ 2C. Проверьте ограничение топливного фильтра 1-й стадии.

| **Условия:** Выключите замок зажигания. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Измерьте ограничение топлива. Управляйте двигателем в режиме холостого хода и измеряйте ограничение на топливных фильтрах первой ступени. См. процедуру 006-020 в разделе 6. | Ограничение топливных фильтров меньше, чем спецификации *Да** | 2D |
| Ограничение топливных фильтров меньше, чем спецификации **NORepair: ** Ограничение по фильтру первой ступени выше спецификации. Заменить топливный фильтр первой ступени. См. процедуру 006-075 в Таблице ассоциированных процедур. | 3А |  |

#### ШАГ 2D. Проверьте ограничение топливного фильтра 2-й стадии.

| **Условия:** Выключите замок зажигания. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Измерьте ограничение топлива. Управляйте двигателем на высоком холостом ходу и измеряйте ограничение по топливным фильтрам второй ступени. См. процедуру 006-020 в разделе 6. | Ограничение топливных фильтров меньше, чем спецификации *Да** | 2Е |
| Ограничение топливных фильтров меньше, чем спецификации **NORepair: ** Ограничение по фильтру второй ступени выше спецификации. Заменить топливный фильтр второй ступени. См. процедуру 006-076 в Таблице ассоциированных процедур. | 3А |  |

#### ШАГ 2E. Проверьте работу механического клапана сброса.

| **Условия:** Отсоединить шланг с механическим сливным клапаном от коллектора слива топлива. Поместите шланг для сброса рельефа в чистый контейнер. Управляйте двигателем. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Запускай двигатель. Используйте электронный сервис INSITETM для проведения испытания на высокое давление Common Rail Pressure Test для повышения давления в рельсе 1 для измерения давления в топливной форсунке. Измерить утечку топлива из механического клапана сброса. Установите и подключите M18 к коллектору слива топлива. Если двигатель не запускается, обратитесь к дереву по устранению неполадок в разделе TT. | Протекает механический клапан? **YESRepair:** Заменить механический клапан сброса и топливный насос на герметизирующий сборку. См. процедуру 006-061 в Таблице ассоциированных процедур. См. процедуру 005-016 в Таблице ассоциированных процедур. | 2F |
| Протекает механический клапан? **NORepair:** Заменить сборку для герметизации топливного насоса. См. процедуру 005-016 в Таблице ассоциированных процедур. | 2F |  |

#### ШАГ 2F. Проверьте работу топливного насоса, дающего давление.

| **Условия:** Включить переключатель зажигания. Управляйте двигателем. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Используйте инструмент электронного сервиса INSITETM для проверки кодов неисправностей. Запустите двигатель и запускайте его на холостом ходу в течение 1 минуты. Используйте электронный сервис INSITETM для проведения испытания на высокое давление Common Rail Pressure Test для повышения давления в рельсе 1 для измерения давления в топливной форсунке. | Код 559 ошибки активирован? *** Ремонт:** Заменить топливный насос высокого давления. См. процедуру 005-016 в Таблице ассоциированных процедур. | 3А |
| Код 559 ошибки активирован? ** НЕТ** | 3А |  |

### ШАГ 3. Сбросьте коды неисправностей.

#### ШАГ 3A. Отключите коды неисправностей.

| **Условия: ** Соединить все компоненты. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Отключите коды неисправностей. Запуск двигателя и холостость в течение 1 минуты. Используйте инструмент электронного сервиса INSITETM для проверки неактивных кодов неисправностей. | Код 559 неактивен? *Да** | 3B |
| Код 559 неактивен? ** НЕТ** | 1А |  |

#### ШАГ 3B. Сбросьте коды неисправностей.

| **Условия: ** Соединить все компоненты. Включите зажигание. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Сбросьте неактивные коды неисправностей. Используйте инструмент электронного сервиса INSITETM для очистки кодов неактивных ошибок. | Все коды неисправностей очищены? *Да** | Ремонт завершён |
| Все коды неисправностей очищены? ** НЕТ** | Соответствующие шаги по устранению неполадок |  |

## Связанные процедуры

| Связанные процедуры |  |  |  |
|---|---|---|---|
| Название процедуры | Процедурный номер | Модельный сервис | Номер бюллетеня |
| Топливный насос | См. процедуру 005-016 | QSK45 и QSK60 | 4021530 |
| Сопротивление на входе топлива | См. процедуру 006-020 | QSK45 и QSK60 | 4021530 |
| Магистрали подачи топлива | См. процедуру 006-024 | QSK45 и QSK60 | 4021530 |
| Предохранительный клапан давления топлива | [[102-006-061 — Fuel Pressure Relief Valve\|См. процедуру 006-061]] | QSK45 и QSK60 | 4021530 |
| Топливный фильтр (ступень 1) | См. процедуру 006-075 | QSK45 и QSK60 | 4021530 |
| Топливный фильтр (ступень 2) | См. процедуру 006-076 | QSK45 и QSK60 | 4021530 |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ## Warnings and Cautions
>
> **CAUTION · Осторожно**
> To reduce the possibility of damaging a new engine control module (ECM), all other active fault codes must be investigated prior to replacing the ECM.
>
> **CAUTION · Осторожно**
> To reduce the possibility of pin and harness damage, use the following test leads when taking a measurement: Part Number 3822758 - male Deutsch™/AMP™/Metri-Pack™ test lead, Part Number 3823996 - female Weather-Pack™ test lead, and Part Number 3824774 - breakout cable.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the fault codes. |  |
> |  | **STEP 1A.** Read the fault codes. | Fault Code 451, 452, 2215, 2261, or 2262 active or many inactive counts of Fault Code 451, 452, 2215, 2261, or 2262? |
> | STEP 2. | Clear the operation of the high pressure fuel system. |  |
> |  | **STEP 2A.** Check for external leak. | External fuel leaks? |
> |  | **STEP 2B.** Check for air in fuel. | Air present in the fuel flow line? |
> |  | **STEP 2C.** Check the Stage 1 fuel filter restriction. | Fuel filter restriction less than specifications? |
> |  | **STEP 2D.** Check the Stage 2 fuel filter restriction. | Fuel filter restriction less than specifications? |
> |  | **STEP 2E.** Check the operation of the mechanical dump valve. | Mechanical dump valve leaking? |
> |  | **STEP 2E.** Check the operation of the fuel pump pressurizing assembly. | Fault Code 559 become active? |
> | STEP 3. | Clear the fault codes. |  |
> |  | **STEP 3A.** Disable the fault codes. | Fault Code 559 inactive? |
> |  | **STEP 3A.** Clear the fault codes. | All fault codes cleared? |
>
> ### STEP 1. Check the fault codes.
>
> #### STEP 1A. Read the fault codes.
>
> | **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Read the fault codes. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 451, 452, 2215, 2261, or 2262 active or many inactive counts of Fault Code 451, 452, 2261, or 2262? **YES** | Appropriate troubleshooting tree |
> | Fault Code 451, 452, 2215, 2261, or 2262 active or are there many inactive counts of Fault Code 451, 452, 2261, or 2262? **NO** | 2A |  |
>
> ### STEP 2. Clear the operation of the high pressure fuel system.
>
> #### STEP 2A. Check for external leak.
>
> | **Conditions:** Operate engine. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for external fuel leaks. Start the engine and let it idle. Inspect for external fuel leaks. | External fuel leaks? **YESRepair:** Repair all fuel leaks. Reference the QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 Modular Common Rail System Service Manual, Bulletin 4021592. | 3A |
> | External fuel leaks? **NO** | 2B |  |
>
> #### STEP 2B. Check for air in fuel.
>
> | **Conditions:** Remove air bleed line from air bleed valve on the fuel drain manifold block. Route the air bleed line into a suitable container to collect fuel. Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the fuel flow for air. Use the following procedure in Service Manual, K38, K50, QSK38 and QSK50, Bulletin 4021528. [[28-006-003 — Air in Fuel\|Refer to Procedure 006-003 in Section 6]] Use the following procedure in Service Manual, QSK45 and QSK60, Bulletin 4021530. Refer to Procedure 006-003 in Section 6. | Air present in the fuel flow line? **YESRepair:** Repair or replace the damaged line or loose connection. Refer to Procedure 006-024 in the Associated Procedures Table. | 3A |
> | Air present in the fuel flow line? **NO** | 2C |  |
>
> #### STEP 2C. Check the Stage 1 fuel filter restriction.
>
> | **Conditions:** Turn keyswitch OFF. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the fuel restriction. Operate the engine at idle and measure the restriction across the first stage fuel filters. Refer to Procedure 006-020 in Section 6. | Fuel filter restriction less than specifications? **YES** | 2D |
> | Fuel filter restriction less than specifications? **NORepair:** The restriction across the first stage filter is above specification. Replace the first stage fuel filter. Refer to Procedure 006-075 in the Associated Procedures Table. | 3A |  |
>
> #### STEP 2D. Check the Stage 2 fuel filter restriction.
>
> | **Conditions:** Turn keyswitch OFF. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the fuel restriction. Operate the engine at high idle and measure the restriction across the second stage fuel filters. Refer to Procedure 006-020 in Section 6. | Fuel filter restriction less than specifications? **YES** | 2E |
> | Fuel filter restriction less than specifications? **NORepair:** The restriction across the second stage filter is above specification. Replace the second stage fuel filter. Refer to Procedure 006-076 in the Associated Procedures Table. | 3A |  |
>
> #### STEP 2E. Check the operation of the mechanical dump valve.
>
> | **Conditions:** Disconnect the mechanical dump valve drain hose from the fuel drain manifold. Place the relief drain hose into a clean container. Operate the engine. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Start the engine. Use INSITE™ electronic service tool High Pressure Common Rail Pressure Test to raise the injector metering rail 1 pressure. Measure the fuel leakage from the mechanical dump valve. Install and M18 plug into the fuel drain manifold. If the engine will **not** start, reference the Engine Performance Troubleshooting Tree in Section TT. | Mechanical dump valve leaking? **YESRepair:** Replace the mechanical dump valve and fuel pump pressurizing assembly. Refer to Procedure 006-061 in the Associated Procedures Table. Refer to Procedure 005-016 in the Associated Procedures Table. | 2F |
> | Mechanical dump valve leaking? **NORepair:** Replace the fuel pump pressurizing assembly. Refer to Procedure 005-016 in the Associated Procedures Table. | 2F |  |
>
> #### STEP 2F. Check the operation of the fuel pump pressurizing assembly.
>
> | **Conditions:** Turn keyswitch ON. Operate the engine. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Use INSITE™ electronic service tool to verify the fault codes. Start the engine and let it idle for 1 minute. Use INSITE™ electronic service tool High Pressure Common Rail Pressure Test to raise the injector metering rail 1 pressure. | Fault Code 559 become active? **YESRepair:** Replace the high pressure fuel pump assembly. Refer to Procedure 005-016 in the Associated Procedures Table. | 3A |
> | Fault Code 559 become active? **NO** | 3A |  |
>
> ### STEP 3. Clear the fault codes.
>
> #### STEP 3A. Disable the fault codes.
>
> | **Conditions:** Connect all components. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Disable the fault codes. Start the engine and idle for 1 minute. Use INSITE™ electronic service tool to verify the inactive fault codes. | Fault Code 559 inactive? **YES** | 3B |
> | Fault Code 559 inactive? **NO** | 1A |  |
>
> #### STEP 3B. Clear the fault codes.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Clear the inactive fault codes. Use INSITE™ electronic service tool to clear the inactive fault codes. | All fault codes cleared? **YES** | Repair complete |
> | All fault codes cleared? **NO** | Appropriate troubleshooting steps |  |
>
> ## Associated Procedures
>
> | Associated Procedures |  |  |  |
> |---|---|---|---|
> | Procedure Title | Procedure Number | Service Model Name | Bulletin Number |
> | Fuel Pump | Refer to Procedure 005-016 | QSK45 and QSK60 | 4021530 |
> | Fuel Inlet Restriction | Refer to Procedure 006-020 | QSK45 and QSK60 | 4021530 |
> | Fuel Supply Lines | Refer to Procedure 006-024 | QSK45 and QSK60 | 4021530 |
> | Fuel Pressure Relief Valve | [[102-006-061 — Fuel Pressure Relief Valve\|Refer to Procedure 006-061]] | QSK45 and QSK60 | 4021530 |
> | Fuel Filter (Stage 1) | Refer to Procedure 006-075 | QSK45 and QSK60 | 4021530 |
> | Fuel Filter (Stage 2) | Refer to Procedure 006-076 | QSK45 and QSK60 | 4021530 |
