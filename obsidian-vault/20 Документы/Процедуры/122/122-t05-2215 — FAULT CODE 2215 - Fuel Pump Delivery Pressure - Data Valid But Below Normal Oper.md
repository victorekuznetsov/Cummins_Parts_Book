---
aliases:
  - "Код 2215 — давление подачи топливного насоса ниже нормы — умеренный уровень"
type: "Процедура"
doc: "122-t05-2215"
title_en: "FAULT CODE 2215 - Fuel Pump Delivery Pressure - Data Valid But Below Normal Operating Range - Moderately Severe Level"
title_ru: "Код 2215 — давление подачи топливного насоса ниже нормы — умеренный уровень"
modified: "2015-04-07"
engines:
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50"
manuals:
  - "4022102"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-t05-2215.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/122-t05-2215.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/122"
  - "перевод/машинный"
---

# FAULT CODE 2215 - Fuel Pump Delivery Pressure - Data Valid But Below Normal Operating Range - Moderately Severe Level
**Код 2215 — давление подачи топливного насоса ниже нормы — умеренный уровень**

> [!abstract] Процедура · `122-t05-2215`
> **Двигатели:** [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50
> **Входит в руководства:** [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M|4022102]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2015-04-07
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-t05-2215.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/122-t05-2215.pdf)

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
| ШАГ 1. | Проверьте, запустится ли двигатель или двигатель запустится и умрет. |  |
|  | **ШАГ 1А.** Попытайтесь запустить двигатель. | Двигатель запускается и продолжает работать? |
| ШАГ 2. | Проверьте низкое давление в топливной системе. |  |
|  | **ШАГ 2А.** Проверка внешних утечек топлива. | Топливо просачивается наружу? |
|  | **ШАГ 2В.** Проверка наличия воздуха в топливе. | Присутствует ли воздух в потоке топлива? |
|  | **STEP 2C** Проверьте датчик давления подачи топлива. | Электронная сервисная оснастка INSITETM и показания датчиков давления в пределах 14 кПа[2 пс] друг от друга? |
|  | **STEP 2D** Проверить оригинальное оборудование производителя (OEM) шланг подачи топлива и топливный бак. | Ограничение входа 1 стадии больше, чем спецификация? |
|  | **ШАГ 2Е.** Проверьте ограничение фильтра 1-й стадии. | Ограничение фильтра 1-й стадии меньше, чем спецификация? |
| ШАГ 3. | Отключите и очистите коды ошибок. |  |
|  | **STEP 3A.** Отключить код ошибки. | Код 2215 неактивен? |
|  | **STEP 3B.** Очистить коды неактивных ошибок. | Все коды неисправностей очищены? |

### ШАГ 1. Проверьте, запустится ли двигатель или двигатель запустится и умрет.

#### ШАГ 1A. Попытка запуска двигателя.

| **Условия: **Запуск двигателя. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Попробуйте запустить двигатель. Проверьте, если двигатель не запускается или если двигатель запускается и останавливается. | Двигатель запускается и продолжает работать? *Да | 2А |
| Двигатель запускается и продолжает работать? **НЕТ** | Ссылка на дерево симптомов устранения неисправностей двигателя |  |

### ШАГ 2. Проверьте низкое давление в топливной системе.

#### ШАГ 2A. Проверьте внешние утечки топлива.

| **Условия: **Работайте с двигателем в режиме холостого хода. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Запустите двигатель и проверьте наличие внешних утечек топлива. Проверьте внешние утечки топлива. | Топливо просачивается наружу? **Ремонт: **Ремонт всех утечек топлива. Используйте следующую процедуру из руководства по обслуживанию K38, K50, QSK38 и QSK50, Вестник [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]]. См. процедуру 006-024 в разделе 6. Используйте следующую процедуру из руководства по обслуживанию QSK45 и QSK60, Бюллетень [[4021530 — QSK45 and QSK60 Service Manual\|4021530]]. См. процедуру 006-024 в разделе 6. | 3А |
| Топливо просачивается наружу? **НЕТ** | 2В |  |

#### ШАГ 2B. Проверьте воздух в топливе.

| **Условия:** Удалить линию кровотока воздуха из клапана с воздушным кровотоком на блоке коллектора слива топлива. Проведите линию воздушного кровотечения в подходящий контейнер для сбора топлива. Включите зажигание. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Направьте поток топлива из линии воздушного кровотечения в контейнер. Проверить расход топлива для воздуха. Используйте следующую процедуру в Руководстве по обслуживанию, K38, K50, QSK38 и QSK50, Вестник [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]].[[28-006-003 — Air in Fuel\|См. процедуру 006-003 в разделе 6.]]. Используйте следующую процедуру в Руководстве по обслуживанию, QSK45 и QSK60, Вестник [[4021530 — QSK45 and QSK60 Service Manual\|4021530]].[[56-006-003 — Air in Fuel\|См. процедуру 006-003 в разделе 6.]] | Присутствует ли воздух в потоке топлива? **Ремонт:** Ремонт или замена поврежденной линии или свободного соединения. Используйте следующую процедуру из руководства по обслуживанию K38, K50, QSK38 и QSK50, Вестник [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]]. См. процедуру 006-024 в разделе 6. Используйте следующую процедуру из руководства по обслуживанию QSK45 и QSK60, Бюллетень [[4021530 — QSK45 and QSK60 Service Manual\|4021530]]. См. процедуру 006-024 в разделе 6. | 3А |
| Присутствует ли воздух в потоке топлива? **НЕТ** | 2C |  |

#### ШАГ 2C. Проверьте датчик давления подачи топлива.

| **Условия:** Подключить электронный сервисный инструмент INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте точность датчика давления подачи топлива. Запуск и эксплуатация двигателя на высоком холостом ходу. Запись показания датчика подачи топлива в электронном сервисном инструменте INSITETM. Выключите двигатель и удалите датчик давления подачи топлива. См. процедуру 019-398 в разделе 19. Установите датчик измерения давления. Запуск и эксплуатация двигателя на высоком холостом ходу. Запись показаний давления подачи топлива на датчике измерения давления, установленном на месте датчика давления подачи топлива. | Электронная сервисная оснастка INSITETM и показания датчиков давления в пределах 14 кПа[2 пс] друг от друга? **Ремонт:** Установите датчик давления подачи топлива, который был удален. См. процедуру 019-398 в разделе 19. | 2D |
| Электронная сервисная оснастка INSITETM и показания датчиков давления в пределах 14 кПа[2 пс] друг от друга? **NORepair:** Заменить датчик давления подачи топлива. См. процедуру 019-398 в разделе 19. | 3А |  |

#### ШАГ 2D. Осмотрите шланг подачи топлива OEM и топливный бак.

| **Условия:** Выключите замок зажигания. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерить ограничение входного отверстия на входе топливного фильтра 1-й стадии. Для двигателей серий K38, K50 и QSK50 в бюллетене [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]] используется следующая процедура. См. процедуру 006-020 в разделе 6. Для двигателей серии QSK45 и QSK60 используйте следующую процедуру в бюллетене [[4021530 — QSK45 and QSK60 Service Manual\|4021530]]. См. процедуру 006-020 в разделе 6. | Ограничение входа 1 стадии больше, чем спецификация? См. информацию об услугах изготовителя оборудования для инструкций по ремонту. | 3А |
| Ограничение входа 1 стадии больше, чем спецификация? **НЕТ** | 2Е |  |

#### ШАГ 2E. Проверьте ограничение фильтра 1-й стадии.

| **Условия:** Выключите замок зажигания. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерить ограничение топливного фильтра 1-й стадии. Для двигателей серий K38, K50 и QSK50 в бюллетене [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]] используется следующая процедура. См. процедуру 006-020 в разделе 6. Для двигателей серии QSK45 и QSK60 используйте следующую процедуру в бюллетене [[4021530 — QSK45 and QSK60 Service Manual\|4021530]]. См. процедуру 006-020 в разделе 6. | Ограничение фильтра 1-й стадии меньше, чем спецификация? **Ремонт: **Заменить насосную установку высокого давления. Для двигателей серий K38, K50 и QSK50 в бюллетене [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]] используется следующая процедура. См. процедуру 005-016 в разделе 5. Для двигателей серии QSK45 и QSK60 используйте следующую процедуру в бюллетене [[4021530 — QSK45 and QSK60 Service Manual\|4021530]]. См. процедуру 005-016 в разделе 5. | 3А |
| Ограничение фильтра 1-й стадии меньше, чем спецификация? **NORepair:** Заменить топливный фильтр 1-й ступени. Для двигателей серий K38, K50 и QSK50 в бюллетене [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]] используется следующая процедура. См. процедуру 006-075 в разделе 6. Для двигателей серии QSK45 и QSK60 используйте следующую процедуру в бюллетене [[4021530 — QSK45 and QSK60 Service Manual\|4021530]]. См. процедуру 006-075 в разделе 6. | 3А |  |

### ШАГ 3. Сбросьте коды неисправностей.

#### ШАГ 3A. Отключите код неисправности.

| **Условия: **Соединить все компоненты. Включите зажигание. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Отключите код неисправности. Используйте инструмент электронного сервиса INSITETM для проверки неактивности кода ошибки. | Код 2215 неактивен? *Да | 3B |
| Код 2215 неактивен? **NORepair:** Возврат к шагам устранения неполадок или свяжитесь с авторизованным местом ремонта Cummins®, если все шаги были завершены и проверены снова. | 1А |  |

#### ШАГ 3B. Сбросьте неактивные коды неисправностей.

| **Условия: **Соединить все компоненты. Включите зажигание. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Сбросьте неактивные коды неисправностей. Используйте инструмент электронного сервиса INSITETM для очистки кодов неактивных ошибок. | Все коды неисправностей очищены? *Да | Ремонт завершён. |
| Все коды неисправностей очищены? **NORepair:** Устранение неполадок с оставшимися кодами неисправностей. | Перейдите к соответствующим шагам устранения неполадок. |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check if engine will start or engine starts and dies. |  |
> |  | **STEP 1A.** Attempt to start the engine. | Engine starts and continues operating? |
> | STEP 2. | Check the low pressure side of the fuel system. |  |
> |  | **STEP 2A.** Check for external fuel leaks. | Fuel leaking externally? |
> |  | **STEP 2B.** Check for air in the fuel. | Air present in fuel flow? |
> |  | **STEP 2C.** Check the fuel supply pressure sensor. | INSITE™ electronic service tool and pressure gauge readings within 14 kPa \[2 psia\] of each other? |
> |  | **STEP 2D.** Inspect the original equipment manufacturer (OEM) fuel supply hose and fuel tank. | Stage 1 inlet restriction greater than specification? |
> |  | **STEP 2E.** Check the Stage 1 filter restriction. | Stage 1 filter restriction less than specification? |
> | STEP 3. | Disable and clear the fault codes. |  |
> |  | **STEP 3A.** Disable the fault code. | Fault Code 2215 inactive? |
> |  | **STEP 3B.** Clear the inactive fault codes. | All fault codes cleared? |
>
> ### STEP 1. Check if engine will start or engine starts and dies.
>
> #### STEP 1A. Attempt to start engine.
>
> | **Conditions:** Start engine. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Attempt to start the engine. Check if the engine will **not** start or if the engine starts and stalls. | Engine starts and continues operating? **YES** | 2A |
> | Engine starts and continues operating? **NO** | Reference the Engine Performance troubleshooting symptom tree |  |
>
> ### STEP 2. Check the low pressure side of the fuel system.
>
> #### STEP 2A. Check for external fuel leaks.
>
> | **Conditions:** Operate the engine at idle. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Start the engine and check for external fuel leaks. Check for external fuel leaks. | Fuel leaking externally? **YESRepair:** Repair all fuel leaks. Use the following procedure from the K38, K50, QSK38 and QSK50 Service Manual, Bulletin [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]]. Refer to Procedure 006-024 in Section 6. Use the following procedure from the QSK45 and QSK60 Service Manual, Bulletin [[4021530 — QSK45 and QSK60 Service Manual\|4021530]]. Refer to Procedure 006-024 in Section 6. | 3A |
> | Fuel leaking externally? **NO** | 2B |  |
>
> #### STEP 2B. Check for air in fuel.
>
> | **Conditions:** Remove air bleed line from air bleed valve on the fuel drain manifold block. Route the air bleed line into a suitable container to collect fuel. Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Direct the fuel flow from the air bleed line into a container. Inspect fuel flow for air. Use the following procedure in Service Manual, K38, K50, QSK38 and QSK50, Bulletin [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]]. [[28-006-003 — Air in Fuel\|Refer to Procedure 006-003 in Section 6]]. Use the following procedure in Service Manual, QSK45 and QSK60, Bulletin [[4021530 — QSK45 and QSK60 Service Manual\|4021530]]. [[56-006-003 — Air in Fuel\|Refer to Procedure 006-003 in Section 6.]] | Air present in the fuel flow? **YESRepair:** Repair or replace the damaged line or loose connection. Use the following procedure from the K38, K50, QSK38 and QSK50 Service Manual, Bulletin [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]]. Refer to Procedure 006-024 in Section 6. Use the following procedure from the QSK45 and QSK60 Service Manual, Bulletin [[4021530 — QSK45 and QSK60 Service Manual\|4021530]]. Refer to Procedure 006-024 in Section 6. | 3A |
> | Air present in the fuel flow? **NO** | 2C |  |
>
> #### STEP 2C. Check the fuel supply pressure sensor.
>
> | **Conditions:** Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the fuel supply pressure sensor accuracy. Start and operate the engine at high idle. Record the fuel supply sensor reading in INSITE™ electronic service tool. Shut the engine down and remove the fuel supply pressure sensor. Refer to Procedure 019-398 in Section 19. Install a pressure gauge. Start and operate the engine at high idle. Record the fuel supply pressure reading on a pressure gauge installed in place of the fuel supply pressure sensor. | INSITE™ electronic service tool and pressure gauge readings within 14 kPa \[2 psia\] of each other? **YESRepair:** Install the fuel supply pressure sensor that was removed. Refer to Procedure 019-398 in Section 19. | 2D |
> | INSITE™ electronic service tool and pressure gauge readings within 14 kPa \[2 psia\] of each other? **NORepair:** Replace the fuel supply pressure sensor. Refer to Procedure 019-398 in Section 19. | 3A |  |
>
> #### STEP 2D. Inspect the OEM fuel supply hose and fuel tank.
>
> | **Conditions:** Turn keyswitch OFF. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure fuel inlet restriction at the Stage 1 fuel filter inlet. For K38, K50, and QSK50 Series Engines, use the following procedure in Bulletin [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]]. Refer to Procedure 006-020 in Section 6. For QSK45 and QSK60 Series Engines, use the following procedure in Bulletin [[4021530 — QSK45 and QSK60 Service Manual\|4021530]]. Refer to Procedure 006-020 in Section 6. | Stage 1 inlet restriction greater than specification? **YESRepair:** Refer to the equipment manufacturer service information for repair instructions. | 3A |
> | Stage 1 inlet restriction greater than specification? **NO** | 2E |  |
>
> #### STEP 2E. Check the Stage 1 filter restriction.
>
> | **Conditions:** Turn keyswitch OFF. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the Stage 1 fuel filter restriction. For K38, K50, and QSK50 Series Engines, use the following procedure in Bulletin [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]]. Refer to Procedure 006-020 in Section 6. For QSK45 and QSK60 Series Engines, use the following procedure in Bulletin [[4021530 — QSK45 and QSK60 Service Manual\|4021530]]. Refer to Procedure 006-020 in Section 6. | Stage 1 filter restriction less than specification? **YESRepair:** Replace the high pressure pump assembly. For K38, K50, and QSK50 Series Engines, use the following procedure in Bulletin [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]]. Refer to Procedure 005-016 in Section 5. For QSK45 and QSK60 Series Engines, use the following procedure in Bulletin [[4021530 — QSK45 and QSK60 Service Manual\|4021530]]. Refer to Procedure 005-016 in Section 5. | 3A |
> | Stage 1 filter restriction less than specification? **NORepair:** Replace the Stage 1 fuel filter. For K38, K50, and QSK50 Series Engines, use the following procedure in Bulletin [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]]. Refer to Procedure 006-075 in Section 6. For QSK45 and QSK60 Series Engines, use the following procedure in Bulletin [[4021530 — QSK45 and QSK60 Service Manual\|4021530]]. Refer to Procedure 006-075 in Section 6. | 3A |  |
>
> ### STEP 3. Clear the fault codes.
>
> #### STEP 3A. Disable the fault code.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Disable the fault code. Use INSITE™ electronic service tool to verify that the fault code is inactive. | Fault Code 2215 inactive? **YES** | 3B |
> | Fault Code 2215 inactive? **NORepair:** Return to the troubleshooting steps or contact a Cummins® Authorized Repair Location if all steps have been completed and checked again. | 1A |  |
>
> #### STEP 3B. Clear the inactive fault codes.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Clear the inactive fault codes. Use INSITE™ electronic service tool to clear the inactive fault codes. | All fault codes cleared? **YES** | Repair complete. |
> | All fault codes cleared? **NORepair:** Troubleshoot any remaining fault codes. | Go to the appropriate troubleshooting steps. |  |
