---
aliases:
  - "Код 1911 — давление в топливной рампе 1 выше нормы — наивысший уровень"
type: "Процедура"
doc: "122-t05-1911"
title_en: "FAULT CODE 1911 - Injector Metering Rail 1 Pressure - Data Valid But Above Normal Operating Range - Most Severe Level"
title_ru: "Код 1911 — давление в топливной рампе 1 выше нормы — наивысший уровень"
modified: "2015-04-10"
engines:
  - "33239746"
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
manuals:
  - "4022102"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-t05-1911.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/122-t05-1911.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/122"
  - "перевод/машинный"
---

# FAULT CODE 1911 - Injector Metering Rail 1 Pressure - Data Valid But Above Normal Operating Range - Most Severe Level
**Код 1911 — давление в топливной рампе 1 выше нормы — наивысший уровень**

> [!abstract] Процедура · `122-t05-1911`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Входит в руководства:** [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M|4022102]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2015-04-10
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-t05-1911.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/122-t05-1911.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

## Предупреждения и меры предосторожности

> [!danger] ОПАСНО
> Топливо огнеопасно. Держите все сигареты, пламя, пилотные огни, дуговое оборудование и выключатели из рабочей зоны и областей, разделяющих вентиляцию, чтобы уменьшить вероятность серьезных травм или смерти при работе на топливной системе.

> [!warning] ОСТОРОЖНО
> Чтобы не повредить новый блок управления двигателем (ЭБУ), перед его заменой разберитесь со всеми остальными активными кодами неисправностей.

> [!warning] ОСТОРОЖНО
> Чтобы не повредить контакты и жгут, при измерениях пользуйтесь следующими измерительными проводами: Номер детали 3822758 — пробный щуп типа штепсельной затворки DeutschTM/AMPTM/Metri-PackTM, номер детали 3823996 — пробный щуп Гнездовой метеозонд, а номер детали 3824774 — проводной ответвление жгута.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте коды неисправностей. |  |
|  | **СТЭП 1А.** Прочитайте коды неисправностей. | Код 271, 272, 2311, 2261, 451 или 452 активных или многих неактивных счетов Кода 271, 272, 2311, 2261, 451 или 452? |
| ШАГ 2. | Очистить работу топливной системы низкого давления. |  |
|  | **ШАГ 2А.** Проверка наличия воздуха в топливе. | Воздух, присутствующий в линии расхода топлива? |
|  | **ШАГ 2В.** Проверьте давление на входе топливного фильтра первой ступени. | Давление топлива больше 0,35 бар \[5 psi\]? |
|  | **STEP 2C** Проверьте давление на входе топливного фильтра первой ступени при работе двигателя. | Давление топлива больше 0,35 бар \[5 psi\]? |
| ШАГ 3. | Проверьте работу топливного насоса, дающего давление. |  |
|  | **STEP 3A.** Проверить узел герметизации топливного насоса. | О-кольцо разрезано или побрито? |
| ШАГ 4. | Сбросьте коды неисправностей. |  |
|  | **STEP 4A.** Отключить коды неисправностей. | Код 1911 неактивен? |
|  | **STEP 4B.** Очистить коды неактивных ошибок. | Все коды неисправностей очищены? |

### ШАГ 1. Проверьте коды неисправностей.

#### ШАГ 1A. Считайте коды неисправностей.

| **Условия:** Включить переключатель зажигания. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Считайте коды неисправностей. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Код 271, 272, 2311, 2261, 451 или 452 активных или многих неактивных счетов Кода 271, 272, 2311, 2261, 451 или 452? *Да | Правильное устранение неполадок дерево. |
| Код 271, 272, 2311, 2261, 451 или 452 активных или многих неактивных счетов Кода 271, 272, 2311, 2261, 451 или 452? **НЕТ** | 2А |  |

### ШАГ 2. Очистить работу топливной системы низкого давления.

#### ШАГ 2A. Проверьте воздух в топливе.

| **Условия:** Удалить линию кровотока воздуха из клапана с воздушным кровотоком на блоке коллектора слива топлива. Проведите линию воздушного кровотечения в подходящий контейнер для сбора топлива. Включите зажигание. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте расход топлива для воздуха. Используйте следующую процедуру в Руководстве по обслуживанию, K38, K50, QSK38 и QSK50, Вестник [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]].[[28-006-003 — Air in Fuel\|См. процедуру 006-003 в разделе 6.]]Используйте следующую процедуру в Руководстве по обслуживанию, QSK45 и QSK60, Вестник [[4021530 — QSK45 and QSK60 Service Manual\|4021530]]. См. процедуру 006-003 в разделе 6. | Воздух, присутствующий в линии расхода топлива? *** Ремонт:** Ремонт или замена поврежденной линии или свободного соединения. Используйте следующую процедуру в Руководстве по обслуживанию, K38, K50 и QSK50, Вестник [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]]. См. процедуру 006-024 в разделе 6. Используйте следующую процедуру в Руководстве по обслуживанию, QSK45 и QSK60, Вестник [[4021530 — QSK45 and QSK60 Service Manual\|4021530]]. См. процедуру 006-024 в разделе 6. | 4А |
| Воздух, присутствующий в линии расхода топлива? **НЕТ** | 2В |  |

#### ШАГ 2B. Проверьте давление на входе топливного фильтра первой ступени с остановленным двигателем.

| **Условия:** Выключите замок зажигания. Установите датчик измерения давления в топливный фильтр, устанавливающий головку на входе. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерить давление на входе. Измерьте давление на входе в топливный фильтр первой ступени. | Давление топлива больше 0,35 бар \[5 psi\]? См. информацию об услугах изготовителя оборудования. | 4А |
| Давление топлива больше 0,35 бар \[5 psi\]? **НЕТ** | 2C |  |

#### ШАГ 2C. Проверьте давление на входе топливного фильтра первой ступени при работе двигателя.

| **Условия:** Выключите замок зажигания. Установите датчик измерения давления в топливный фильтр, устанавливающий головку на входе. Включите зажигание. Операционный двигатель. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерить давление на входе. Измерьте давление на входе в топливный фильтр первой ступени. Если двигатель не запускается, выполните это испытание, запуская двигатель. | Давление топлива больше 0,35 бар \[5 psi\]? См. информацию об услугах изготовителя оборудования. | 4А |
| Давление топлива больше 0,35 бар \[5 psi\]? **НЕТ** | 3А |  |

### ШАГ 3. Проверьте работу топливного насоса, дающего давление.

#### ШАГ 3A. Осмотрите кольцо сборки для герметизации топливного насоса.

| **Условия:** Выключите замок зажигания. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте сборку для герметизации топливного насоса. Удалите топливный насос, дающий давление. Используйте следующую процедуру в Руководстве по обслуживанию, K38, K50 и QSK50, Вестник [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]]. См. процедуру 005-232 в разделе 5. Используйте следующую процедуру в Руководстве по обслуживанию, QSK45 и QSK60, Вестник [[4021530 — QSK45 and QSK60 Service Manual\|4021530]]. См. процедуру 005-232 в разделе 5. Осмотрите кольцо сборки для герметизации топливного насоса. Если кольцо разрезано или выбрито; топливо может быть обойдено топливным насосом, прессующим сборку и поступающим в насос высокого давления. | О-кольцо разрезано или побрито? * Заменить поврежденное кольцо. Используйте следующую процедуру в Руководстве по обслуживанию, K38, K50 и QSK50, Вестник [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]]. См. процедуру 005-232 в разделе 5. Используйте следующую процедуру в Руководстве по обслуживанию, QSK45 и QSK60, Вестник [[4021530 — QSK45 and QSK60 Service Manual\|4021530]]. См. процедуру 005-232 в разделе 5. | 4А |
| О-кольцо разрезано или побрито? **NORepair:** Заменить топливный насос на герметизирующий сборочный и механический клапан сброса. Используйте следующую процедуру в Руководстве по обслуживанию, K38, K50 и QSK50, Вестник [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]]. См. процедуру 005-232 в разделе 5 и процедуру 006-061 в разделе 6. Используйте следующую процедуру в Руководстве по обслуживанию, QSK45 и QSK60, Вестник [[4021530 — QSK45 and QSK60 Service Manual\|4021530]]. См. процедуру 005-232 в разделе 5 и процедуру 006-061 в разделе 6. | 4А |  |

### ШАГ 4. Очистить коды неисправностей

#### ШАГ 4A. Отключите коды неисправностей.

| **Условия:** Соединить все компоненты. Включите зажигание. Подключите инструмент электронного сервиса INSITETM. Операционный двигатель. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Отключите коды неисправностей. Используйте инструмент Insite для проверки неактивности кода ошибки. | Код 1911 неактивен? *Да | 4B |
| Код 1911 неактивен? **NORepair:** Возврат к шагам устранения неполадок или свяжитесь с авторизованным местом ремонта Cummins®, если все шаги были завершены и проверены снова. | 1А |  |

#### ШАГ 4B. Сбросьте неактивные коды неисправностей.

| **Условия:** Соединить все компоненты. Включите зажигание. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Сбросьте неактивные коды неисправностей. Используйте инструмент Insite для очистки любых неактивных кодов неисправностей. | Все коды неисправностей очищены? *Да | Ремонт завершён |
| Все коды неисправностей очищены? **NORepair:** Устранение неполадок с оставшимися кодами неисправностей. | Соответствующие шаги по устранению неполадок |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ## Warnings and Cautions
>
> **WARNING · Опасно**
> Fuel is flammable. Keep all cigarettes, flames, pilot lights, arcing equipment, and switches out of the work area and areas sharing ventilation to reduce the possibility of severe personal injury or death when working on the fuel system.
>
> **CAUTION · Осторожно**
> To reduce the possibility of damaging a new engine control module (ECM), all other active fault codes must be investigated prior to replacing the ECM.
>
> **CAUTION · Осторожно**
> To reduce the possibility of pin and harness damage, use the following test leads when taking a measurement: Part Number 3822758 - male Deutsch™/AMP™/Metri-Pack™ test lead, Part Number 3823996 - Female Weather-Pack™ test lead, and Part Number 3824774 - breakout cable.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the fault codes. |  |
> |  | **STEP 1A.** Read the fault codes. | Fault Code 271, 272, 2311, 2261, 451, or 452 active or many inactive counts of Fault Code 271, 272, 2311, 2261, 451, or 452? |
> | STEP 2. | Clear the operation of the low-pressure fuel system. |  |
> |  | **STEP 2A.** Check for air in fuel. | Air present in the fuel flow line? |
> |  | **STEP 2B.** Check the first stage fuel filter inlet pressure. | Fuel pressure greater than 0.35 bar \[5 psi\]? |
> |  | **STEP 2C.** Check the first stage fuel filter inlet pressure with the engine running. | Fuel pressure greater than 0.35 bar \[5 psi\]? |
> | STEP 3. | Check the operation of the fuel pump pressurizing assembly. |  |
> |  | **STEP 3A.** Inspect the fuel pump pressurizing assembly o-ring. | O-ring cut or shaved? |
> | STEP 4. | Clear the fault codes. |  |
> |  | **STEP 4A.** Disable the fault codes. | Fault Code 1911 inactive? |
> |  | **STEP 4B.** Clear the inactive fault codes. | All fault codes cleared? |
>
> ### STEP 1. Check the fault codes.
>
> #### STEP 1A. Read the fault codes.
>
> | **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Read the fault codes. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 271, 272, 2311, 2261, 451, or 452 active or many inactive counts of Fault Code 271, 272, 2311, 2261, 451, or 452? **YES** | Appropriate troubleshooting tree. |
> | Fault Code 271, 272, 2311, 2261, 451, or 452 active or many inactive counts of Fault Code 271, 272, 2311, 2261, 451, or 452? **NO** | 2A |  |
>
> ### STEP 2. Clear the operation of the low-pressure fuel system.
>
> #### STEP 2A. Check for air in fuel.
>
> | **Conditions:** Remove air bleed line from air bleed valve on the fuel drain manifold block. Route the air bleed line into a suitable container to collect fuel. Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the fuel flow for air. Use the following procedure in Service Manual, K38, K50, QSK38 and QSK50, Bulletin [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]]. [[28-006-003 — Air in Fuel\|Refer to Procedure 006-003 in Section 6.]] Use the following procedure in Service Manual, QSK45 and QSK60, Bulletin [[4021530 — QSK45 and QSK60 Service Manual\|4021530]]. [[56-006-003 — Air in Fuel\|Refer to Procedure 006-003 in Section 6]]. | Air present in the fuel flow line? **YESRepair:** Repair or replace the damaged line or loose connection. Use the following procedure in Service Manual, K38, K50, and QSK50, Bulletin [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]]. Refer to Procedure 006-024 in Section 6. Use the following procedure in Service Manual, QSK45 and QSK60, Bulletin [[4021530 — QSK45 and QSK60 Service Manual\|4021530]]. Refer to Procedure 006-024 in Section 6. | 4A |
> | Air present in the fuel flow line? **NO** | 2B |  |
>
> #### STEP 2B. Check the first stage fuel filter inlet pressure with the engine stopped.
>
> | **Conditions:** Turn keyswitch OFF. Install the pressure gauge into the fuel filter head port at the inlet. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure inlet pressure. Measure the inlet pressure to the first stage fuel filter. | Fuel pressure greater than 0.35 bar \[5 psi\]? **YESRepair:** Refer to the equipment manufacturer service information. | 4A |
> | Fuel pressure greater than 0.35 bar \[5 psi\]? **NO** | 2C |  |
>
> #### STEP 2C. Check the first stage fuel filter inlet pressure with the engine running.
>
> | **Conditions:** Turn keyswitch OFF. Install the pressure gauge into fuel filter head port at inlet. Turn keyswitch ON. Operate engine. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure inlet pressure. Measure the inlet pressure to the first stage fuel filter. If the engine will **not** start, perform this test while cranking the engine. | Fuel pressure greater than 0.35 bar \[5 psi\]? **YESRepair:** Refer to the equipment manufacturer service information. | 4A |
> | Fuel pressure greater than 0.35 bar \[5 psi\]? **NO** | 3A |  |
>
> ### STEP 3. Check the operation of the fuel pump pressurizing assembly.
>
> #### STEP 3A. Inspect the fuel pump pressurizing assembly o-ring.
>
> | **Conditions:** Turn keyswitch OFF. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the fuel pump pressurizing assembly. Remove the fuel pump pressurizing assembly. Use the following procedure in Service Manual, K38, K50, and QSK50, Bulletin [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]]. Refer to Procedure 005-232 in Section 5. Use the following procedure in Service Manual, QSK45 and QSK60, Bulletin [[4021530 — QSK45 and QSK60 Service Manual\|4021530]]. Refer to Procedure 005-232 in Section 5. Inspect the fuel pump pressurizing assembly o-ring. If the o-ring is cut or shaved; fuel can be bypassing the fuel pump pressuring assembly and entering the high-pressure pump. | O-ring cut or shaved? **YESRepair:** Replace the damaged o-ring. Use the following procedure in Service Manual, K38, K50, and QSK50, Bulletin [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]]. Refer to Procedure 005-232 in Section 5. Use the following procedure in Service Manual, QSK45 and QSK60, Bulletin [[4021530 — QSK45 and QSK60 Service Manual\|4021530]]. Refer to Procedure 005-232 in Section 5. | 4A |
> | O-ring cut or shaved? **NORepair:** Replace the fuel pump pressurizing assembly and mechanical dump valve. Use the following procedure in Service Manual, K38, K50, and QSK50, Bulletin [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]]. Refer to Procedure 005-232 in Section 5 and Refer to Procedure 006-061 in Section 6. Use the following procedure in Service Manual, QSK45 and QSK60, Bulletin [[4021530 — QSK45 and QSK60 Service Manual\|4021530]]. Refer to Procedure 005-232 in Section 5 and Refer to Procedure 006-061 in Section 6. | 4A |  |
>
> ### STEP 4. Clear the fault codes
>
> #### STEP 4A. Disable the fault codes.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. Operate engine. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Disable the fault codes. Use INSITE electronic service tool to verify the fault code is inactive. | Fault Code 1911 inactive? **YES** | 4B |
> | Fault Code 1911 inactive? **NORepair:** Return to the troubleshooting steps or contact a Cummins® Authorized Repair Location if all steps have been completed and checked again. | 1A |  |
>
> #### STEP 4B. Clear the inactive fault codes.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Clear the inactive fault codes. Use INSITE electronic service tool to clear any inactive fault codes. | All fault codes cleared? **YES** | Repair complete |
> | All fault codes cleared? **NORepair:** Troubleshoot any remaining fault codes. | Appropriate troubleshooting steps |  |
