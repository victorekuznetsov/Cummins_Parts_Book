---
aliases:
  - "Код 449 — давление в топливной рампе 1 выше нормы — наивысший уровень"
type: "Процедура"
doc: "123-t05-449"
title_en: "FAULT CODE 449 - Injector Metering Rail 1 Pressure - Data Valid But Above Normal Operating Range - Most Severe Level"
title_ru: "Код 449 — давление в топливной рампе 1 выше нормы — наивысший уровень"
modified: "2015-04-07"
engines:
  - "41349633"
families:
  - "QSK19"
manuals:
  - "4022094"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/123/123-t05-449.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/123-t05-449.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/123"
  - "перевод/машинный"
---

# FAULT CODE 449 - Injector Metering Rail 1 Pressure - Data Valid But Above Normal Operating Range - Most Severe Level
**Код 449 — давление в топливной рампе 1 выше нормы — наивысший уровень**

> [!abstract] Процедура · `123-t05-449`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4022094 — QSK19 CM2150 and CM2670 Electronic Control System Troubleshooting and Repair Manual|4022094]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2015-04-07
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/123/123-t05-449.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/123-t05-449.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

## Предупреждения и меры предосторожности

> [!danger] ОПАСНО
> В зависимости от условий топливо огнеопасно. При выполнении любых или всех из следующих процедур для удаления линий подачи топлива и связанных с ними компонентов, держите все сигареты, пламя, пилотные огни, дуговое оборудование и выключатели из рабочей зоны и областей, разделяющих вентиляцию, чтобы уменьшить вероятность серьезных травм или смерти при работе на топливной системе.

> [!warning] ОСТОРОЖНО
> Чтобы не повредить новый блок управления двигателем (ЭБУ), перед его заменой разберитесь со всеми остальными активными кодами неисправностей.

> [!warning] ОСТОРОЖНО
> Чтобы не повредить контакты и жгут, при измерениях пользуйтесь следующими измерительными проводами: Номер детали 3822758 — пробный щуп типа штепсельной затворки DeutschTM/AMPTM/Metri-PackTM, номер детали 3823996 — гнездовой пробный щуп Weather-PackTM, а номер детали 3824774 — проводной ответвление жгута.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте коды неисправностей. |  |
|  | **СТЭП 1А.** Прочитайте коды неисправностей. | Код 271, 272, 2311, 2261, 451 или 452 активных или многих неактивных счетов кода 271, 272, 2311, 2261, 451 или 452 неисправностей? |
| ШАГ 2. | Заменить механический клапан. |  |
|  | **ШАГ 2А.** Проверка наличия воздуха в топливе. | Воздух, присутствующий в линии расхода топлива? |
|  | **ШАГ 2В.** Проверьте давление на входе топливного фильтра первой ступени. | Давление топлива больше 0,35 бар \[5 psi\]? |
| ШАГ 3. | Проверьте работу топливного насоса, дающего давление сборки 1. |  |
|  | **СТЭП 3А** Проверить узл 1 кольцевой герметизации топливного насоса. | О-кольцо разрезано или побрито? |
| ШАГ 4. | Сбросьте коды неисправностей. |  |
|  | **STEP 4A.** Отключить код ошибки. | Код 449 неактивен? |
|  | **STEP 4B.** Очистить коды неактивных ошибок. | Все коды неисправностей очищены? |

### ШАГ 1. Проверьте коды неисправностей.

#### ШАГ 1A. Считайте коды неисправностей.

| **Условия:** Включить переключатель зажигания. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Считайте коды неисправностей. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Код 271, 272, 2311, 2261, 451 или 452 активного или много неактивного кода 271, 272, 2311, 2261, 451 или 452 неисправности? *Да** | Правильное устранение неполадок дерево. |
| Код 271, 272, 2311, 2261, 451 или 452 активных или многих неактивных счетов кода 271, 272, 2311, 2261, 451 или 452 неисправностей? ** НЕТ** | 2А |  |

### ШАГ 2. Очистить работу топливной системы низкого давления.

#### ШАГ 2A. Проверьте воздух в топливе.

> [!danger] ОПАСНО
> Топливо огнеопасно. Держите все сигареты, пламя, пилотные огни, дуговое оборудование и выключатели из рабочей зоны и областей, разделяющих вентиляцию, чтобы уменьшить вероятность серьезных травм или смерти при работе на топливной системе. Не истечет кровь топливной системы горячего двигателя; это может привести к разливу топлива на горячий выхлопной коллектор, что может вызвать пожар.

| ** Условия:** Удалить линию кровотока воздуха из клапана с воздушным кровотоком на блоке коллектора слива топлива. Проведите линию воздушного кровотечения в подходящий контейнер для сбора топлива. Включите зажигание. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте расход топлива для воздуха. Используйте следующую процедуру в Руководстве по обслуживанию, QSK19, QSK19 CM850 Модульная общая железнодорожная система, QSK19 CM2150 Модульная общая железнодорожная система, Вестник [[4021592 — QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual\|4021592]].[[20-006-003 — Air in Fuel\|См. процедуру 006-003 в разделе 6.]]. | Воздух, присутствующий в линии расхода топлива? *** Ремонт:** Ремонт или замена поврежденной линии или свободного соединения. Заменить механический клапан высокого давления. Используйте следующую процедуру в Руководстве по обслуживанию, QSK19, QSK19 CM850 Модульная общая железнодорожная система, QSK19 CM2150 Модульная общая железнодорожная система, Вестник [[4021592 — QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual\|4021592]].[[20-006-024-tr — Fuel Supply Lines\|См. процедуру 006-024 в разделе 6.]] | 4А |
| Воздух, присутствующий в линии расхода топлива? ** НЕТ** | 2В |  |

#### ШАГ 2B. Проверьте давление на входе топливного фильтра первой ступени.

| **Условия:** Выключите замок зажигания. Установите датчик измерения давления в топливный фильтр, устанавливающий головку на входе. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Измерить давление на входе. Измерьте давление на входе в топливный фильтр первой ступени. Если двигатель не запускается, выполните это испытание, запуская двигатель. | Давление топлива больше 0,35 бар \[5 psi\]? ****** См. информацию об услугах изготовителя оборудования. | 4А |
| Давление топлива больше 0,35 бар \[5 psi\]? ** НЕТ** | 3А |  |

### ШАГ 3. Проверьте работу топливного насоса, дающего давление сборки 1.

#### ШАГ 3A. Осмотрите герметизирующий агрегат топливного насоса 1 уплотнительное кольцо.

| **Условия:** Выключите замок зажигания. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверить сборку 1 для герметизации топливного насоса. Удалите топливный насос, дающий давление сборка 1. Используйте следующую процедуру в Руководстве по обслуживанию, QSK19, QSK19 CM850 Модульная общая железнодорожная система, QSK19 CM2150 MCRS, Вестник [[4021592 — QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual\|4021592]]. См. процедуру 005-016 в разделе 5. Осмотрите герметизирующий агрегат топливного насоса 1 уплотнительное кольцо. Если кольцо обрезано или выбрито, топливо может быть обойдено топливным насосом, дающим давление в сборе 1 и поступающим в насос высокого давления. | О-кольцо разрезано или побрито? *** Заменить поврежденное кольцо. Используйте следующую процедуру в Руководстве по обслуживанию, QSK19, QSK19 CM850 Модульная общая железнодорожная система, QSK19 CM2150 Модульная общая железнодорожная система, Вестник [[4021592 — QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual\|4021592]]. См. процедуру 005-016 в разделе 5. | 4А |
| О-кольцо разрезано или побрито? ** НЕТ** | 4А |  |

### ШАГ 4. Сбросьте коды неисправностей.

#### ШАГ 4A. Отключите код неисправности.

| **Условия: ** Соединить все компоненты. Включите зажигание. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Отключите код неисправности. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Код 449 неактивен? *Да** | 4B |
| Код 449 неактивен? **NORepair:** Возврат к шагам устранения неполадок или свяжитесь с авторизованным ремонтным центром Cummins®, если все шаги были завершены и проверены во второй раз. | 1А |  |

#### ШАГ 4B. Сбросьте неактивные коды неисправностей.

| **Условия: ** Соединить все компоненты. Включите зажигание. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Сбросьте неактивные коды неисправностей. Используйте инструмент электронного сервиса INSITETM для очистки кодов неактивных ошибок. | Все коды неисправностей очищены? *Да** | Ремонт завершён |
| Все коды неисправностей очищены? **NORepair: ** Устранение неполадок с оставшимися активными кодами неисправностей. | Соответствующие шаги по устранению неполадок |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ## Warnings and Cautions
>
> **WARNING · Опасно**
> Depending on the circumstance, fuel is flammable. When performing any or all of the following procedures to remove fuel supply lines and related components, keep all cigarettes, flames, pilot lights, arcing equipment, and switches out of the work area and areas sharing ventilation to reduce the possibility of severe personal injury or death when working on the fuel system.
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
> |  | **STEP 1A.** Read the fault codes. | Fault Code 271, 272, 2311, 2261, 451, or 452 active or many inactive counts of fault code 271, 272, 2311, 2261, 451, or 452? |
> | STEP 2. | Replace the mechanical dump valve. |  |
> |  | **STEP 2A.** Check for air in fuel. | Air present in the fuel flow line? |
> |  | **STEP 2B.** Check the first stage fuel filter inlet pressure. | Fuel pressure greater than 0.35 bar \[5 psi\]? |
> | STEP 3. | Check the operation of the fuel pump pressurizing assembly 1. |  |
> |  | **STEP 3A.** Inspect the fuel pump pressurizing assembly 1 o-ring. | O-ring cut or shaved? |
> | STEP 4. | Clear the fault codes. |  |
> |  | **STEP 4A.** Disable the fault code. | Fault Code 449 inactive? |
> |  | **STEP 4B.** Clear the inactive fault codes. | All fault codes cleared? |
>
> ### STEP 1. Check the fault codes.
>
> #### STEP 1A. Read the fault codes.
>
> | **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Read the fault codes. Use INSITE™ electronic service tool to read the fault codes. | Fault code 271, 272, 2311, 2261, 451, or 452 active or many inactive counts of fault code 271, 272, 2311, 2261, 451, or 452? **YES** | Appropriate troubleshooting tree. |
> | Fault Code 271, 272, 2311, 2261, 451, or 452 active or many inactive counts of fault code 271, 272, 2311, 2261, 451, or 452? **NO** | 2A |  |
>
> ### STEP 2. Clear the operation of the low pressure fuel system.
>
> #### STEP 2A. Check for air in fuel.
>
> **WARNING · Опасно**
> Fuel is flammable. Keep all cigarettes, flames, pilot lights, arcing equipment, and switches out of the work area and areas sharing ventilation to reduce the possibility of severe personal injury or death when working on the fuel system. Do not bleed the fuel system of a hot engine; this can result in fuel spilling onto a hot exhaust manifold, which can cause a fire.
>
> | **Conditions:** Remove air bleed line from air bleed valve on the fuel drain manifold block. Route the air bleed line into a suitable container to collect fuel. Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the fuel flow for air. Use the following procedure in Service Manual, QSK19, QSK19 CM850 Modular Common Rail System, QSK19 CM2150 Modular Common Rail System, Bulletin [[4021592 — QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual\|4021592]]. [[20-006-003 — Air in Fuel\|Refer to Procedure 006-003 in Section 6]]. | Air present in the fuel flow line? **YESRepair:** Repair or replace the damaged line or loose connection. Replace the mechanical high pressure relief valve. Use the following procedure in Service Manual, QSK19, QSK19 CM850 Modular Common Rail System, QSK19 CM2150 Modular Common Rail System, Bulletin [[4021592 — QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual\|4021592]]. [[20-006-024-tr — Fuel Supply Lines\|Refer to Procedure 006-024 in Section 6.]] | 4A |
> | Air present in the fuel flow line? **NO** | 2B |  |
>
> #### STEP 2B. Check the first stage fuel filter inlet pressure.
>
> | **Conditions:** Turn keyswitch OFF. Install the pressure gauge into fuel filter head port at inlet. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure inlet pressure. Measure the inlet pressure to the first stage fuel filter. If the engine will **not** start, perform this test while cranking the engine. | Fuel pressure greater than 0.35 bar \[5 psi\]? **YESRepair:** Refer to the equipment manufacturer service information. | 4A |
> | Fuel pressure greater than 0.35 bar \[5 psi\]? **NO** | 3A |  |
>
> ### STEP 3. Check the operation of the fuel pump pressurizing assembly 1.
>
> #### STEP 3A. Inspect the fuel pump pressurizing assembly 1 o-ring.
>
> | **Conditions:** Turn keyswitch OFF. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the fuel pump pressurizing assembly 1. Remove the fuel pump pressurizing assembly 1. Use the following procedure in Service Manual, QSK19, QSK19 CM850 Modular Common Rail System, QSK19 CM2150 MCRS, Bulletin [[4021592 — QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual\|4021592]]. Refer to Procedure 005-016 in Section 5. Inspect the fuel pump pressurizing assembly 1 o-ring. If the o-ring is cut or shaved, fuel can be bypassing the fuel pump pressurizing assembly 1 and entering the high pressure pump. | O-ring cut or shaved? **YESRepair:** Replace the damaged o-ring. Use the following procedure in Service Manual, QSK19, QSK19 CM850 Modular Common Rail System, QSK19 CM2150 Modular Common Rail System, Bulletin [[4021592 — QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual\|4021592]]. Refer to Procedure 005-016 in Section 5. | 4A |
> | O-ring cut or shaved? **NO** | 4A |  |
>
> ### STEP 4. Clear the fault codes.
>
> #### STEP 4A. Disable the fault code.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Disable the fault code. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 449 inactive? **YES** | 4B |
> | Fault Code 449 inactive? **NORepair:** Return to the troubleshooting steps or contact a Cummins® Authorized Repair location if all steps have been completed and checked a second time. | 1A |  |
>
> #### STEP 4B. Clear the inactive fault codes.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Clear the inactive fault codes. Use INSITE™ electronic service tool to clear the inactive fault codes. | All fault codes cleared? **YES** | Repair complete |
> | All fault codes cleared? **NORepair:** Troubleshoot any remaining active fault codes. | Appropriate troubleshooting steps |  |
