---
aliases:
  - "Код 4615 — давление подачи топливного насоса выше нормы — наивысший уровень"
type: "Процедура"
doc: "122-t05-4615"
title_en: "FAULT CODE 4615 - Fuel Pump Delivery Pressure - Data Valid But Above Normal Operating Range - Most Severe Level"
title_ru: "Код 4615 — давление подачи топливного насоса выше нормы — наивысший уровень"
modified: "2015-03-04"
engines:
  - "33239746"
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
manuals:
  - "4022102"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-t05-4615.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/122-t05-4615.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/122"
  - "перевод/машинный"
---

# FAULT CODE 4615 - Fuel Pump Delivery Pressure - Data Valid But Above Normal Operating Range - Most Severe Level
**Код 4615 — давление подачи топливного насоса выше нормы — наивысший уровень**

> [!abstract] Процедура · `122-t05-4615`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Входит в руководства:** [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M|4022102]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2015-03-04
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-t05-4615.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/122-t05-4615.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

## Предупреждения и меры предосторожности

> [!warning] ОСТОРОЖНО
> Чтобы уменьшить вероятность повреждения нового модуля управления двигателем (ECM), все другие активные коды неисправностей должны быть исследованы перед заменой ECM.

> [!warning] ОСТОРОЖНО
> Чтобы не повредить контакты и жгут, при измерениях пользуйтесь следующими измерительными проводами: Номер детали 3822758 - пробный щуп типа пробки DeutschTM/AMPTM/Metri-PackTM и номер детали 3823993 - пробный щуп типа пробки DeutschTM.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте топливную систему низкого давления. |  |
|  | **СТЭП 1А** Проверьте датчик давления подачи топлива. | Инситем электронного обслуживания инструмент и показания датчика измерения давления в пределах 14 кПа \[2 psi \] друг от друга? |
|  | **СТЭП 1В** Проверить линии подачи топлива. | Повреждены, повреждены или ограничены топливные линии? |
|  | **STEP 1C** Проверьте ограничение топливного фильтра 2-й ступени. | 2-й этап ограничения топливного фильтра в установленных пределах. |
|  | **ШАГ 1С-1.** Проверьте головку установки топливного фильтра. | 2-й этап ограничения топливного фильтра в установленных пределах. |
|  | **STEP 1D.** Проверить давление подачи топлива на впускном коллекторе. | Давление на входе в топливо всегда меньше 34,5 кПаГ[5 psig]? |
| ШАГ 2. | Отключите и очистите код ошибки. |  |
|  | **STEP 2A.** Отключить код ошибки. | Код 4615 неактивен? |
|  | **STEP 2B.** Очистить коды неактивных ошибок. | Все коды неисправностей очищены? |

### ШАГ 1. Проверьте систему подачи топлива под давлением.

#### ШАГ 1A. Проверьте датчик давления подачи топлива.

| **Условия:** Подключите инструмент CompuchekTM. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте датчик давления подачи топлива. Запуск и эксплуатация двигателя на высоком холостом ходу. Запись показания датчика подачи топлива в электронном сервисном инструменте INSITETM. Запись показаний давления подачи топлива на датчике измерения давления, установленном на месте датчика давления подачи топлива. Используйте следующую процедуру для фильтров 2-й стадии в разделе Меры руководства по обслуживанию K38, K50, QSK38 и QSK50, Вестник [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]]. См. процедуру 006-024 в Таблице ассоциированных процедур. Используйте следующую процедуру для фильтров 2-й стадии в разделе Меры в руководстве по обслуживанию QSK45 и QSK60, Вестник [[4021530 — QSK45 and QSK60 Service Manual\|4021530]], См. процедуру 006-024 в Таблице ассоциированных процедур. | Электронная сервисная оснастка INSITETM и показания датчиков давления в пределах 14 кПа[2псия] друг от друга? *Да | 1В |
| Электронная сервисная оснастка INSITETM и показания датчиков давления в пределах 14 кПа[2псия] друг от друга? **NORepair:** Заменить датчик давления подачи топлива. См. процедуру 019-398 в Таблице ассоциированных процедур. | 2А |  |

#### ШАГ 1B. Проверьте линии подачи топлива.

| **Условия:** Выключите замок зажигания. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте линии подачи топлива на наличие повреждений, изломов или ограничений. См. процедуру 006-024 в Таблице ассоциированных процедур. | Повреждены, повреждены или ограничены топливные линии? **Ремонт:** Заменить поврежденную (и) топливную линию (линии) | 2А |
| Повреждены, повреждены или ограничены топливные линии? **НЕТ** | 1С |  |

#### ШАГ 1C. Проверьте ограничение топливного фильтра 2-й стадии.

| **Условия:** Выключите замок зажигания. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерить ограничение фильтра 2 стадии. Используйте следующую процедуру в руководстве по обслуживанию K38, K50, QSK38 и QSK50, бюллетень [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]]. См. процедуру 006-020 в Таблице ассоциированных процедур. Используйте следующую процедуру в руководстве по обслуживанию QSK45 и QSK60, в бюллетене [[4021530 — QSK45 and QSK60 Service Manual\|4021530]]. См. процедуру 006-020 в Таблице ассоциированных процедур. | 2-й этап ограничения топливного фильтра в установленных пределах. *Да | 1D |
| 2-й этап ограничения топливного фильтра в установленных пределах. **NORepair:** Заменить топливные фильтры 2-го этапа. Используйте следующую процедуру в руководстве по обслуживанию K38, K50, QSK38 и QSK50, бюллетень [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]]. См. процедуру 006-076 в Таблице ассоциированных процедур. Используйте следующую процедуру в руководстве по обслуживанию QSK45 и QSK60, в бюллетене [[4021530 — QSK45 and QSK60 Service Manual\|4021530]]. См. процедуру 006-076 в Таблице ассоциированных процедур. | 1С-1-1 |  |

#### ШАГ 1C-1. Проверьте головку установки топливного фильтра.

| **Условия:** Выключите замок зажигания. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерить ограничение топливного фильтра 2-й стадии. Используйте следующую процедуру в руководстве по обслуживанию K38, K50, QSK38 и QSK50, в бюллетене [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]]. См. процедуру 006-020 в Таблице ассоциированных процедур. Используйте следующую процедуру в руководстве по обслуживанию QSK45 и QSK60, в бюллетене [[4021530 — QSK45 and QSK60 Service Manual\|4021530]]. См. процедуру 006-020 в Таблице ассоциированных процедур. | 2-й этап ограничения топливного фильтра в установленных пределах. *Да | 2А |
| 2-й этап ограничения топливного фильтра в установленных пределах. **NORepair:** Заменить установочную головку топливного фильтра 2-й ступени. Используйте следующую процедуру в руководстве по обслуживанию K38, K50, QSK38 и QSK50, бюллетень [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]]. См. процедуру 006-020 в Таблице ассоциированных процедур. Используйте следующую процедуру в руководстве по обслуживанию QSK45 и QSK60, в бюллетене [[4021530 — QSK45 and QSK60 Service Manual\|4021530]]. См. процедуру 006-020 в Таблице ассоциированных процедур. | 2А |  |

#### ШАГ 1D. Проверьте давление подачи топлива на впускном коллекторе топлива.

| **Условия:** Выключите замок зажигания. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте давление подачи топлива на топливном коллекторе. Закройте клапан подачи топлива. Удалите пробку M14 STOR из впускного коллектора топлива. Установите фитинг CompuchekTM, номер детали 3824844 или эквивалент, в впускном коллекторе топлива. Подключите вакуумный калибр и адаптер, номер 3164491 или эквивалент, и цифровой мультиметр, номер 3164488 или 3164489, или эквивалент, к фитингу CompuchekTM. Откройте клапан подачи топлива. Запуск и эксплуатация двигателя при низком и высоком холостом ходу. Запись показаний давления на входе топлива. | Давление на входе в топливо всегда меньше 34,5 кПаГ[5 psig]? Заменить топливный насос. Используйте следующие процедуры: K38, K50, QSK38 и QSK50 Service Manual, Bulletin [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]]. См. процедуру 005-016 в Таблице ассоциированных процедур. Используйте следующую процедуру в руководстве по обслуживанию QSK45 и QSK60, в бюллетене [[4021530 — QSK45 and QSK60 Service Manual\|4021530]]. См. процедуру 005-016 в Таблице ассоциированных процедур. | 2А |
| Давление на входе в топливо всегда меньше 34,5 кПаГ[5 psig]? **NORepair:** См. информацию об обслуживании изготовителя оборудования для снижения давления на входе топлива. | 2А |  |

### ШАГ 2. Отключите и очистите код ошибки.

#### ШАГ 2A. **Отключить код ошибки.**

| **Условия: **Соединить все компоненты. Включите зажигание. Подключите инструмент электронного сервиса INSITETM. Управляйте двигателем. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Отключите код неисправности. Используйте инструмент электронного сервиса INSITETM для проверки неактивности кода ошибки. | Код 4615 неактивен? *Да | 2В |
| Код 4615 неактивен? **NORepair:** Возврат к шагам устранения неполадок или свяжитесь с авторизованным местом ремонта Cummins®, если все шаги были завершены и проверены снова. | 1А |  |

#### ШАГ 2B. Сбросьте неактивные коды неисправностей.

| **Условия: **Соединить все компоненты. Включите зажигание. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Сбросьте неактивные коды неисправностей. Используйте инструмент электронного сервиса INSITETM для очистки кодов неактивных ошибок. | Все коды неисправностей очищены? *Да | Ремонт завершён |
| Все коды неисправностей очищены? **NORepair:** Устранение неполадок с оставшимися кодами неисправностей. | Перейдите к соответствующим шагам устранения неполадок. |  |

## Связанные процедуры

| Связанные процедуры |  |  |  |
|---|---|---|---|
| Название процедуры | Процедурный номер | Модельный сервис | Номер бюллетеня |
| Топливный насос | [[28-005-016-tr — Fuel Pump\|См. процедуру 005-016]] | K38, K50, QSK38 и QSK50 | [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]] |
| Топливный насос | [[56-005-016-tr — Fuel Pump\|См. процедуру 005-016]] | QSK38 и QSK50 | [[4021530 — QSK45 and QSK60 Service Manual\|4021530]] |
| Головка топливного фильтра | [[28-006-017-tr — Fuel Filter Head\|См. процедуру 006-017]] | K38, K50, QSK38 и QSK50 | [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]] |
| Головка топливного фильтра | [[56-006-017-tr — Fuel Filter Head\|См. процедуру 006-017]] | QSK45 и QSK60 | [[4021530 — QSK45 and QSK60 Service Manual\|4021530]] |
| Сопротивление на входе топлива | [[28-006-020-tr — Fuel Inlet Restriction\|См. процедуру 006-020]] | K38, K50, QSK38 и QSK50 | [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]] |
| Сопротивление на входе топлива | [[56-006-020-tr — Fuel Inlet Restriction\|См. процедуру 006-020]] | QSK45 и QSK60 | [[4021530 — QSK45 and QSK60 Service Manual\|4021530]] |
| Магистрали подачи топлива | [[28-006-024-tr — Fuel Supply Lines\|См. процедуру 006-024]] | K38, K50, QSK38 и QSK50 | [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]] |
| Магистрали подачи топлива | [[56-006-024-tr — Fuel Supply Lines\|См. процедуру 006-024]] | QSK45 и QSK60 | [[4021530 — QSK45 and QSK60 Service Manual\|4021530]] |
| Топливный фильтр (ступень 2) | См. процедуру 006-076 | K38, K50, QSK38 и QSK50 | [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]] |
| Топливный фильтр (ступень 2) | См. процедуру 006-076 | QSK45 и QSK60 | [[4021530 — QSK45 and QSK60 Service Manual\|4021530]] |
| Датчик давления топливоподающего насоса | См. процедуру 019-398 | QSK19 | [[4022094 — QSK19 CM2150 and CM2670 Electronic Control System Troubleshooting and Repair Manual\|4022094]] |
| Датчик давления топливоподающего насоса | См. процедуру 019-398 | QSK38, QSK50 и QSK60 | [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M\|4022102]] |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ## Warnings and Cautions
>
> **CAUTION · Осторожно**
> To reduce the possibility of damaging a new engine control module (ECM), all other active fault codes must be investigated before replacing the ECM.
>
> **CAUTION · Осторожно**
> To reduce the possibility of pin and harness damage, use the following test leads when taking a measurement: Part Number 3822758 - male Deutsch™/AMP™/Metri-Pack™ test lead and Part Number 3823993 - male Deutsch™ test lead.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the low-pressure fuel system. |  |
> |  | **STEP 1A.** Check the fuel supply pressure sensor. | INSITE™ electronic service tool and pressure gauge readings within 14 kPa \[2 psi\] of each other? |
> |  | **STEP 1B.** Check the fuel supply lines. | Any fuel lines damaged, kinked, or restricted? |
> |  | **STEP 1C.** Check the Stage 2 fuel filter restriction. | Stage 2 fuel filter restriction within specification? |
> |  | **STEP 1C-1.** Check the fuel filter head. | Stage 2 fuel filter restriction within specification? |
> |  | **STEP 1D.** Check the fuel supply pressure at the fuel inlet manifold. | Fuel inlet pressure always less than 34.5 kPaG \[5 psig\]? |
> | STEP 2. | Disable and clear the fault code. |  |
> |  | **STEP 2A.** Disable the fault code. | Fault Code 4615 inactive? |
> |  | **STEP 2B.** Clear the inactive fault codes. | All fault codes cleared? |
>
> ### STEP 1. Check the fuel supply pressure fuel system.
>
> #### STEP 1A. Check the fuel supply pressure sensor.
>
> | **Conditions:** Connect the Compuchek™ tool. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the fuel supply pressure sensor. Start and operate the engine at high idle. Record the fuel supply sensor reading in INSITE™ electronic service tool. Record the fuel supply pressure reading on a pressure gauge installed in place of the fuel supply pressure sensor. Use the following procedure for Stage 2 filters in the Measure section of the K38, K50, QSK38 and QSK50 Service Manual, Bulletin [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]]. Refer to Procedure 006-024 in in the Associated Procedures Table. Use the following procedure for Stage 2 filters in the Measure section in the QSK45 and QSK60 Service Manual, Bulletin [[4021530 — QSK45 and QSK60 Service Manual\|4021530]],. Refer to Procedure 006-024 in the Associated Procedures Table. | INSITE™ electronic service tool and pressure gauge readings within 14 kPa \[2psia\] of each other? **YES** | 1B |
> | INSITE™ electronic service tool and pressure gauge readings within 14 kPa \[2psia\] of each other? **NORepair:** Replace the fuel supply pressure sensor. Refer to Procedure 019-398 in the Associated Procedures Table. | 2A |  |
>
> #### STEP 1B. Check the fuel supply lines.
>
> | **Conditions:** Turn keyswitch OFF. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Examine the fuel supply lines for damages, kinks, or restrictions. Refer to Procedure 006-024 in the Associated Procedures Table. | Any fuel lines damaged, kinked, or restricted? **YESRepair:** Replace the damaged fuel line(s). | 2A |
> | Any fuel lines damaged, kinked, or restricted? **NO** | 1C |  |
>
> #### STEP 1C. Check the Stage 2 fuel filter restriction.
>
> | **Conditions:** Turn keyswitch OFF. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the Stage 2 filter restriction. Use the following procedure in the K38, K50, QSK38 and QSK50 Service Manual, Bulletin [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]]. Refer to Procedure 006-020 in the Associated Procedures Table. Use the following procedure in the QSK45 and QSK60 Service Manual, Bulletin [[4021530 — QSK45 and QSK60 Service Manual\|4021530]]. Refer to Procedure 006-020 in in the Associated Procedures Table. | Stage 2 fuel filter restriction within specification? **YES** | 1D |
> | Stage 2 fuel filter restriction within specification? **NORepair:** Replace the Stage 2 fuel filters. Use the following procedure in the K38,K50, QSK38 and QSK50 Service Manual, Bulletin [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]]. Refer to Procedure 006-076 in the Associated Procedures Table. Use the following procedure in the QSK45 and QSK60 Service Manual, Bulletin [[4021530 — QSK45 and QSK60 Service Manual\|4021530]]. Refer to Procedure 006-076 in the Associated Procedures Table. | 1C-1 |  |
>
> #### STEP 1C-1. Check the fuel filter head.
>
> | **Conditions:** Turn keyswitch OFF. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the Stage 2 fuel filter restriction. Use the following procedure in the K38, K50,QSK38 and QSK50 Service Manual, Bulletin [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]]. Refer to Procedure 006-020 in the Associated Procedures Table. Use the following procedure in the QSK45 and QSK60 Service Manual, Bulletin [[4021530 — QSK45 and QSK60 Service Manual\|4021530]]. Refer to Procedure 006-020 in Associated Procedures Table. | Stage 2 fuel filter restriction within specification? **YES** | 2A |
> | Stage 2 fuel filter restriction within specification? **NORepair:** Replace the Stage 2 fuel filter head. Use the following procedure in the K38, K50, QSK38 and QSK50 Service Manual, Bulletin [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]]. Refer to Procedure 006-020 in the Associated Procedures Table. Use the following procedure in the QSK45 and QSK60 Service Manual, Bulletin [[4021530 — QSK45 and QSK60 Service Manual\|4021530]]. Refer to Procedure 006-020 in Associated Procedures Table. | 2A |  |
>
> #### STEP 1D. Check the fuel supply pressure at the fuel inlet manifold.
>
> | **Conditions:** Turn keyswitch OFF. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the fuel supply pressure at the fuel manifold. Close the fuel supply valve. Remove the M14 STOR plug from the fuel inlet manifold. Install a Compuchek™ fitting, Part Number 3824844, or equivalent, in the fuel inlet manifold. Connect the vacuum gauge and adapter, Part Number 3164491, or equivalent, and digital multimeter, Part Number 3164488 or 3164489,or equivalent, to the Compuchek™ fitting. Open the fuel supply valve. Start and operate the engine at low idle and high idle. Record the fuel inlet pressure readings. | Fuel inlet pressure always less than 34.5 kPaG \[5 psig\]? **YESRepair:** Replace the fuel pump. Use the following procedure the K38, K50, QSK38 and QSK50 Service Manual, Bulletin [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]]. Refer to Procedure 005-016 in the Associated Procedures Table. Use the following procedure in the QSK45 and QSK60 Service Manual, Bulletin [[4021530 — QSK45 and QSK60 Service Manual\|4021530]]. Refer to Procedure 005-016 in the Associated Procedures Table. | 2A |
> | Fuel inlet pressure always less than 34.5 kPaG \[5 psig\]? **NORepair:** Refer to the equipment manufacturer service information to reduce fuel inlet pressure. | 2A |  |
>
> ### STEP 2. Disable and clear the fault code.
>
> #### STEP 2A. **Disable the fault code.**
>
> | **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. Operate the engine. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Disable the fault code. Use INSITE™ electronic service tool to verify the fault code is inactive. | Fault Code 4615 inactive? **YES** | 2B |
> | Fault Code 4615 inactive? **NORepair:** Return to the troubleshooting steps or contact a Cummins® Authorized Repair Location if all steps have been completed and checked again. | 1A |  |
>
> #### STEP 2B. Clear the inactive fault codes.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Clear the inactive fault codes. Use INSITE™ electronic service tool to clear the inactive fault codes. | All fault codes cleared? **YES** | Repair complete |
> | All fault codes cleared? **NORepair:** Troubleshoot any remaining fault codes. | Go to the appropriate troubleshooting steps. |  |
>
> ## Associated Procedures
>
> | Associated Procedures |  |  |  |
> |---|---|---|---|
> | Procedure Title | Procedure Number | Service Model Name | Bulletin Number |
> | Fuel Pump | [[28-005-016-tr — Fuel Pump\|Refer to Procedure 005-016]] | K38, K50, QSK38 and QSK50 | [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]] |
> | Fuel Pump | [[56-005-016-tr — Fuel Pump\|Refer to Procedure 005-016]] | QSK38 and QSK50 | [[4021530 — QSK45 and QSK60 Service Manual\|4021530]] |
> | Fuel Filter Head | [[28-006-017-tr — Fuel Filter Head\|Refer to Procedure 006-017]] | K38, K50, QSK38 and QSK50 | [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]] |
> | Fuel Filter Head | [[56-006-017-tr — Fuel Filter Head\|Refer to Procedure 006-017]] | QSK45 and QSK60 | [[4021530 — QSK45 and QSK60 Service Manual\|4021530]] |
> | Fuel Inlet Restriction | [[28-006-020-tr — Fuel Inlet Restriction\|Refer to Procedure 006-020]] | K38, K50, QSK38 and QSK50 | [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]] |
> | Fuel Inlet Restriction | [[56-006-020-tr — Fuel Inlet Restriction\|Refer to Procedure 006-020]] | QSK45 and QSK60 | [[4021530 — QSK45 and QSK60 Service Manual\|4021530]] |
> | Fuel Supply Lines | [[28-006-024-tr — Fuel Supply Lines\|Refer to Procedure 006-024]] | K38, K50, QSK38, and QSK50 | [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]] |
> | Fuel Supply Lines | [[56-006-024-tr — Fuel Supply Lines\|Refer to Procedure 006-024]] | QSK45 and QSK60 | [[4021530 — QSK45 and QSK60 Service Manual\|4021530]] |
> | Fuel Filter (Stage 2) | Refer to Procedure 006-076 | K38, K50, QSK38, and QSK50 | [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]] |
> | Fuel Filter (Stage 2) | Refer to Procedure 006-076 | QSK45 and QSK60 | [[4021530 — QSK45 and QSK60 Service Manual\|4021530]] |
> | Fuel Supply Pump Pressure Sensor | Refer to Procedure 019-398 | QSK19 | [[4022094 — QSK19 CM2150 and CM2670 Electronic Control System Troubleshooting and Repair Manual\|4022094]] |
> | Fuel Supply Pump Pressure Sensor | Refer to Procedure 019-398 | QSK38, QSK50, and QSK60 | [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M\|4022102]] |
