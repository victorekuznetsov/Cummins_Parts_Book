---
aliases:
  - "Код 1911 — давление в топливной рампе 1 выше нормы — наивысший уровень"
type: "Процедура"
doc: "123-t05-1911"
title_en: "FAULT CODE 1911 - Injector Metering Rail 1 Pressure - Data Valid But Above Normal Operating Range - Most Severe Level"
title_ru: "Код 1911 — давление в топливной рампе 1 выше нормы — наивысший уровень"
modified: "2018-11-01"
engines:
  - "41349633"
families:
  - "QSK19"
manuals:
  - "4022094"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/123/123-t05-1911.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/123-t05-1911.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/123"
  - "перевод/машинный"
---

# FAULT CODE 1911 - Injector Metering Rail 1 Pressure - Data Valid But Above Normal Operating Range - Most Severe Level
**Код 1911 — давление в топливной рампе 1 выше нормы — наивысший уровень**

> [!abstract] Процедура · `123-t05-1911`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4022094 — QSK19 CM2150 and CM2670 Electronic Control System Troubleshooting and Repair Manual|4022094]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2018-11-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/123/123-t05-1911.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/123-t05-1911.pdf)

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

> [!danger] ОПАСНО
> В зависимости от обстоятельств, дизельное топливо является легковоспламеняющимся. При осмотре или выполнении обслуживания или ремонта топливной системы, чтобы уменьшить вероятность пожара и в результате травмы, смерти или повреждения имущества, никогда не курите и не допускайте искр или пламени (например, пилотные огни, электрические выключатели или сварочное оборудование) в рабочей зоне.

> [!warning] ОСТОРОЖНО
> Чтобы не повредить новый блок управления двигателем (ЭБУ), перед его заменой разберитесь со всеми остальными активными кодами неисправностей.

> [!warning] ОСТОРОЖНО
> Чтобы не повредить контакты и жгут, при измерениях пользуйтесь следующими измерительными проводами: Номер детали 3822758 — пробный щуп типа штепсельной вилки DeutschTM/AMPTM/Metri-PackTM, номер детали 3823996 — пробный щуп гнездового Weather PackTM, а номер детали 3824774 — проводной ответвление жгута.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте коды неисправностей. |  |
|  | **СТЭП 1А.** Прочитайте коды неисправностей. | Код 271, 272, 2311, 2261, 451 или 452 активен или неактивен с более чем одним счетом за последние 25 часов работы двигателя? |
| ШАГ 2. | Очистить работу топливной системы низкого давления. |  |
|  | **ШАГ 2А.** Проверка наличия воздуха в топливе. | Воздух, присутствующий в линии расхода топлива? |
|  | **ШАГ 2В.** Проверьте давление на входе топливного фильтра первой ступени. | Давление топлива больше 0,35 бар \[5 psi\]? |
| ШАГ 3. | Проверьте работу топливного насоса, дающего давление. |  |
|  | **STEP 3A.** Проверьте привод топливного насоса. | Измеренное давление топливной рельсы снизилось более чем на 200 бар[2901 psi] по сравнению с командным давлением топливной рельсы? |
|  | **STEP 3B** Проверить уплотнительное кольцо топливного насоса. | О-кольцо разрезано или побрито? |
| ШАГ 4. | Сбросьте коды неисправностей. |  |
|  | **STEP 4A.** Отключить коды неисправностей. | Код 1911 неактивен? |

### ШАГ 1. Проверьте коды неисправностей.

#### ШАГ 1A. Считайте коды неисправностей.

| **Условия:** Включите переключатель зажигания на электронном сервисном оборудовании Connect INSITETM. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Считайте коды неисправностей. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Код 271, 272, 2311, 2261, 451 или 452 активен или неактивен с более чем одним счетом за последние 25 часов работы двигателя? *Да** | Правильное устранение неполадок дерево. |
| Код 271, 272, 2311, 2261, 451 или 452 активен или неактивен с более чем одним счетом за последние 25 часов работы двигателя? ** НЕТ** | 2А |  |

### ШАГ 2. Очистить работу топливной системы низкого давления.

#### ШАГ 2A. Проверьте воздух в топливе.

| ** Условия:** Удалить линию кровотока воздуха из клапана с воздушным кровотоком на блоке коллектора слива топлива. Проведите линию воздушного кровотечения в подходящий контейнер для сбора топлива. Включите зажигание. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте расход топлива для воздуха. Используйте следующую процедуру в Руководстве по обслуживанию, QSK19, QSK19 CM850 MCRS и QSK19 CM2150 MCRS.[[20-006-003 — Air in Fuel\|См. процедуру 006-003 в разделе 6.]]. | Воздух, присутствующий в линии расхода топлива? *** Ремонт:** Ремонт или замена поврежденной линии или свободного соединения. Используйте следующую процедуру в руководстве по обслуживанию модульной общей железнодорожной системы QSK19, модульной общей железнодорожной системы QSK19 CM850 и модульной общей железнодорожной системы QSK19 CM2150, бюллетень [[4021592 — QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual\|4021592]].[[20-006-024-tr — Fuel Supply Lines\|См. процедуру 006-024 в разделе 6.]] | 4А |
| Воздух, присутствующий в линии расхода топлива? ** НЕТ** | 2В |  |

#### ШАГ 2B. Проверьте давление на входе топливного фильтра первой ступени.

| **Условия:** Выключите переключатель зажигания Установите датчик измерения давления в топливный фильтр, устанавливающий головку на входе. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Измерить давление на входе. Включите зажигание. Измерьте давление на входе в топливный фильтр первой ступени. См. информацию об услугах производителя оборудования. **Примечание**: Если двигатель не запускается, выполните это испытание, запуская двигатель. | Давление топлива больше 0,35 бар \[5 psi\]? ****** См. информацию об услугах изготовителя оборудования. | 4А |
| Давление топлива больше 0,35 бар \[5 psi\]? ** НЕТ** | 3А |  |

### ШАГ 3. Проверьте работу топливного насоса, дающего давление.

#### ШАГ 3A. Проверьте привод топливного насоса.

| **Условия:** Выключите замок зажигания. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте привод топливного насоса. Запускайте двигатель на холостом ходу в течение по крайней мере одной минуты, чтобы очистить воздух, вызванный предыдущими шагами. Используйте инструмент электронного обслуживания INSITETM для мониторинга давления в топливной рельсе и измерения давления в топливной рельсе при холостом ходу. | Измеренное давление топливной рельсы снизилось более чем на 200 бар[2901 psi] по сравнению с командным давлением топливной рельсы? **Ремонт:** Обнаружен неисправный привод топливного насоса. Заменить привод топливного насоса на сборку. См. процедуру 019-117 в разделе 19. | 4А |
| Измеренное давление топливной рельсы снизилось более чем на 200 бар[2901 psi] по сравнению с командным давлением топливной рельсы? ** НЕТ** | 3B |  |

#### ШАГ 3B. Осмотрите кольцо сборки для герметизации топливного насоса.

| **Условия:** Выключите замок зажигания. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте привод топливного насоса. Удалите привод топливного насоса. Используйте следующую процедуру в руководстве по обслуживанию модульной общей железнодорожной системы QSK19, модульной общей железнодорожной системы QSK19 CM850 и модульной общей железнодорожной системы QSK19 CM2150, бюллетень [[4021592 — QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual\|4021592]]. См. процедуру 005-016 в разделе 5. Осмотрите привод топливного насоса и кольцо. Если кольцо разрезано или выбрито, топливо может быть обойдено исполнительным механизмом топливного насоса и введено в насос высокого давления. | О-кольцо разрезано или побрито? *** Заменить поврежденное кольцо. Используйте следующую процедуру в руководстве по обслуживанию модульной общей железнодорожной системы QSK19, модульной общей железнодорожной системы QSK19 CM850 и модульной общей железнодорожной системы QSK19 CM2150, бюллетень [[4021592 — QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual\|4021592]].[[20-005-016-tr — Fuel Pump\|См. процедуру 005-016 в разделе 5.]]. | 4А |
| О-кольцо разрезано или побрито? ** НЕТ** | 4А |  |

### ШАГ 4. Сбросьте коды неисправностей.

#### ШАГ 4A. Отключите коды неисправностей.

| **Условия:** Подключить все компоненты Подключить электронный сервисный инструмент INSITETM. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Отключите коды неисправностей. Управляйте двигателем в рамках «Условий для устранения кода неисправности», найденных в разделе Обзор этой процедуры устранения неполадок. Используйте инструмент электронного сервиса INSITETM для проверки неактивных кодов неисправностей. | Код 1911 неактивен? *Да** | Ремонт завершён |
| Код 1911 неактивен? **Секретарь:**Проверить, что все шаги были выполнены. Если все шаги выполнены, то следуйте процессу технической эскалации. | Эскалация или призыв к помощи |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ## Warnings and Cautions
>
> **WARNING · Опасно**
> Fuel is flammable. Keep all cigarettes, flames, pilot lights, arcing equipment, and switches out of the work area and areas sharing ventilation to reduce the possibility of severe personal injury or death when working on the fuel system.
>
> **WARNING · Опасно**
> Depending on the circumstance, diesel fuel is flammable. When inspecting or performing service or repairs on the fuel system, to reduce the possibility of fire and resulting personal injury, death or property damage, never smoke or allow sparks or flames (such as pilot lights, electrical switches, or welding equipment) in the work area.
>
> **CAUTION · Осторожно**
> To reduce the possibility of damaging a new engine control module (ECM), all other active fault codes must be investigated prior to replacing the ECM.
>
> **CAUTION · Осторожно**
> To reduce the possibility of pin and harness damage, use the following test leads when taking a measurement: Part Number 3822758 - male Deutsch™/AMP™/Metri-Pack™ test lead, Part Number 3823996 - female Weather Pack™ test lead, and Part Number 3824774 - breakout cable.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the fault codes. |  |
> |  | **STEP 1A.** Read the fault codes. | Fault Code 271, 272, 2311, 2261, 451, or 452 active or inactive with more than one count in the last 25 engine hours? |
> | STEP 2. | Clear the operation of the low pressure fuel system. |  |
> |  | **STEP 2A.** Check for air in fuel. | Air present in the fuel flow line? |
> |  | **STEP 2B.** Check the first stage fuel filter inlet pressure. | Fuel pressure greater than 0.35 bar \[5 psi\]? |
> | STEP 3. | Check the operation of the fuel pump pressurizing assembly. |  |
> |  | **STEP 3A.** Check fuel pump actuator. | Measured fuel rail pressure devated more than 200 bar \[2901 psi\] compared to the commanded fuel rail pressure? |
> |  | **STEP 3B.** Inspect the fuel pump pressuring assembly o-ring. | O-ring cut or shaved? |
> | STEP 4. | Clear the fault codes. |  |
> |  | **STEP 4A.** Disable the fault codes. | Fault Code 1911 inactive? |
>
> ### STEP 1. Check the fault codes.
>
> #### STEP 1A. Read the fault codes.
>
> | **Conditions:** Turn keyswitch ON Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Read the fault codes. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 271, 272, 2311, 2261, 451, or 452 active or inactive with more than one count in the last 25 engine hours? **YES** | Appropriate troubleshooting tree. |
> | Fault Code 271, 272, 2311, 2261, 451, or 452 active or inactive with more than one count in the last 25 engine hours? **NO** | 2A |  |
>
> ### STEP 2. Clear the operation of the low-pressure fuel system.
>
> #### STEP 2A. Check for air in fuel.
>
> | **Conditions:** Remove air bleed line from air bleed valve on the fuel drain manifold block. Route the air bleed line into a suitable container to collect fuel. Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the fuel flow for air. Use the following procedure in Service Manual, QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS. [[20-006-003 — Air in Fuel\|Refer to Procedure 006-003 in Section 6]]. | Air present in the fuel flow line? **YESRepair:** Repair or replace the damaged line or loose connection. Use the following procedure in the QSK19, QSK19 CM850 Modular Common Rail System, and QSK19 CM2150 Modular Common Rail System Service Manual, Bulletin [[4021592 — QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual\|4021592]]. [[20-006-024-tr — Fuel Supply Lines\|Refer to Procedure 006-024 in Section 6.]] | 4A |
> | Air present in the fuel flow line? **NO** | 2B |  |
>
> #### STEP 2B. Check the first stage fuel filter inlet pressure.
>
> | **Conditions:** Turn keyswitch OFF Install the pressure gauge into fuel filter head port at inlet. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure inlet pressure. Turn keyswitch ON. Measure the inlet pressure to the first stage fuel filter. Refer to the equipment manufacturer service information. **Note**: If the engine will **not** start, perform this test while cranking the engine. | Fuel pressure greater than 0.35 bar \[5 psi\]? **YESRepair:** Refer to the equipment manufacturer service information. | 4A |
> | Fuel pressure greater than 0.35 bar \[5 psi\]? **NO** | 3A |  |
>
> ### STEP 3. Check the operation of the fuel pump pressurizing assembly.
>
> #### STEP 3A. Check the fuel pump actuator.
>
> | **Conditions:** Turn keyswitch OFF. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the fuel pump actuator. Run the engine at idle for at least one minute to purge air induced from previous steps. Use INSITE™ electronic service tool to monitor commanded fuel rail pressure and measured fuel rail pressure at idle. | Measured fuel rail pressure devated more than 200 bar \[2901 psi\] compared to the commanded fuel rail pressure? **YESRepair:** A malfunctioning fuel pump actuator has been detected. Replace the fuel pump actuator assembly. Refer to Procedure 019-117 in Section 19. | 4A |
> | Measured fuel rail pressure devated more than 200 bar \[2901 psi\] compared to the commanded fuel rail pressure? **NO** | 3B |  |
>
> #### STEP 3B. Inspect the fuel pump pressurizing assembly o-ring.
>
> | **Conditions:** Turn keyswitch OFF. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the fuel pump actuator. Remove the fuel pump actuator. Use the following procedure in the QSK19, QSK19 CM850 Modular Common Rail System, and QSK19 CM2150 Modular Common Rail System Service Manual, Bulletin [[4021592 — QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual\|4021592]]. Refer to Procedure 005-016 in Section 5. Inspect the fuel pump actuator and o-ring. If the o-ring is cut or shaved, fuel can be bypassing the fuel pump actuator and entering the high-pressure pump. | O-ring cut or shaved? **YESRepair:** Replace the damaged o-ring. Use the following procedure in the QSK19, QSK19 CM850 Modular Common Rail System, and QSK19 CM2150 Modular Common Rail System Service Manual, Bulletin [[4021592 — QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual\|4021592]]. [[20-005-016-tr — Fuel Pump\|Refer to Procedure 005-016 in Section 5]]. | 4A |
> | O-ring cut or shaved? **NO** | 4A |  |
>
> ### STEP 4. Clear the fault codes.
>
> #### STEP 4A. Disable the fault codes.
>
> | **Conditions:** Connect all components Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Disable the fault codes. Operate the engine within the “Conditions for Clearing the Fault Code” found in the Overview section of this troubleshooting procedure. Use INSITE™ electronic service tool to verify the inactive fault codes. | Fault Code 1911 inactive? **YES** | Repair complete |
> | Fault Code 1911 inactive? **NORepair:** Verify that all steps have been completed. If all steps have been completed, then follow the technical escalation process. | Escalate or call for assistance |  |
