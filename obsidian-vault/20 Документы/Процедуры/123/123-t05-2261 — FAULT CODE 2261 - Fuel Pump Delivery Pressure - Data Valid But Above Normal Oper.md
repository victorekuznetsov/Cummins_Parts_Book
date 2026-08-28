---
aliases:
  - "Код 2261 — давление подачи топливного насоса выше нормы — низший уровень"
type: "Процедура"
doc: "123-t05-2261"
title_en: "FAULT CODE 2261 - Fuel Pump Delivery Pressure - Data Valid But Above Normal Operating Range - Least Severe Level"
title_ru: "Код 2261 — давление подачи топливного насоса выше нормы — низший уровень"
modified: "2012-12-03"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4022094"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/123/123-t05-2261.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/123-t05-2261.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/123"
  - "перевод/машинный"
---

# FAULT CODE 2261 - Fuel Pump Delivery Pressure - Data Valid But Above Normal Operating Range - Least Severe Level
**Код 2261 — давление подачи топливного насоса выше нормы — низший уровень**

> [!abstract] Процедура · `123-t05-2261`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4022094 — QSK19 CM2150 and CM2670 Electronic Control System Troubleshooting and Repair Manual|4022094]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-12-03
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/123/123-t05-2261.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/123-t05-2261.pdf)

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
> Чтобы не повредить контакты и жгут, при измерениях пользуйтесь следующими измерительными проводами: Номер детали 3822758 — пробный щуп типа пробки DeutschTM/AMPTM/Metri-PackTM; номер детали 3823993 — пробный щуп типа пробки DeutschTM.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте топливную систему низкого давления. |  |
|  | **СТЭП 1А** Проверьте датчик давления подачи топлива. | Электронная сервисная оснастка INSITETM и показания датчиков давления в пределах 14 кПа[2 пс] друг от друга? |
|  | **СТЭП 1В** Проверить линии подачи топлива. | Повреждены, повреждены или ограничены топливные линии? |
|  | **ШАГ 1С** Проверьте ограничение топливного фильтра 2-й ступени. | 2-й этап ограничения топливного фильтра в установленных пределах. |
|  | **ШАГ 1С-1.** Проверьте головку установки топливного фильтра. | 2-й этап ограничения топливного фильтра в установленных пределах. |
|  | **STEP 1D.** Проверить давление подачи топлива на топливном коллекторе. | Давление на входе в топливо всегда меньше 34,5 кПаГ[5 psig]? |
| ШАГ 2. | Очистите код ошибки. |  |
|  | **STEP 2A.** Отключить код ошибки. | Код 2261 неактивен? |
|  | **STEP 2B.** Очистить коды неактивных ошибок. | Все коды неисправностей очищены? |

### ШАГ 1. Проверьте топливную систему низкого давления.

#### ШАГ 1A. Проверьте датчик давления подачи топлива.

| **Условия:** Подключите инструмент CompuchekTM. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте датчик давления подачи топлива. Запуск и эксплуатация двигателя на высоком холостом ходу. Запись показания датчика подачи топлива в электронном сервисном инструменте INSITETM. Запись показаний давления подачи топлива на датчике измерения давления, установленном на месте датчика давления подачи топлива. Используйте следующую процедуру в Руководстве по эксплуатации QSK19 и модульных двигателях общей железнодорожной системы QSK19 CM850, Бюллетень [[4021592 — QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual\|4021592]], для фильтров 2-й ступени в разделе Мера. См. процедуру 006-024 в разделе 6. | Электронная сервисная оснастка INSITETM и показания датчиков давления в пределах 14 кПа[2 пс] друг от друга? *Да | 1В |
| Электронная сервисная оснастка INSITETM и показания датчиков давления в пределах 14 кПа[2 пс] друг от друга? **NORepair:** Заменить датчик давления подачи топлива. См. процедуру 019-398 в разделе 19. | 2А |  |

#### ШАГ 1B. Проверьте линии подачи топлива.

| **Условия:** Выключите замок зажигания. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверяйте линии подачи топлива на наличие повреждений, изломов, ограничений. Используйте следующую процедуру: Руководство по эксплуатации QSK19 и модульные двигатели общей железнодорожной системы QSK19 CM850, Бюллетень [[4021592 — QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual\|4021592]]. См. процедуру 006-024 в разделе 6. | Повреждены, повреждены или ограничены топливные линии? **Ремонт:** Заменить линию (линии) подачи топлива. | 2А |
| Повреждены, повреждены или ограничены топливные линии? **НЕТ** | 1С |  |

#### ШАГ 1C. Проверьте ограничение топливного фильтра 2 стадии.

| **Условия:** Выключите замок зажигания. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерить ограничение фильтра 2 стадии. Используйте следующую процедуру: Руководство по эксплуатации QSK19 и модульные двигатели общей железнодорожной системы QSK19 CM850, Бюллетень [[4021592 — QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual\|4021592]]. См. процедуру 006-020 в разделе 6. | 2-й этап ограничения топливного фильтра в установленных пределах. *Да | 1D |
| 2-й этап ограничения топливного фильтра в установленных пределах. **NORepair:** Заменить топливные фильтры 2-й ступени. Используйте следующую процедуру: Руководство по эксплуатации QSK19 и модульные двигатели общей железнодорожной системы QSK19 CM850, Бюллетень [[4021592 — QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual\|4021592]]. См. процедуру 006-076 в разделе 6. | 1С-1-1 |  |

#### ШАГ 1C-1. Проверьте головку установки топливного фильтра.

| **Условия:** Выключите замок зажигания. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерить ограничение топливного фильтра 2 стадии. Используйте следующую процедуру: Руководство по эксплуатации QSK19 и модульные двигатели общей железнодорожной системы QSK19 CM850, Бюллетень [[4021592 — QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual\|4021592]]. См. процедуру 006-020 в разделе 6. | 2-й этап ограничения топливного фильтра в установленных пределах. *Да | 2А |
| 2-й этап ограничения топливного фильтра в установленных пределах. **NORepair:** Заменить установочную головку топливного фильтра 2-й ступени. Используйте следующую процедуру: Руководство по эксплуатации QSK19 и модульные двигатели общей железнодорожной системы QSK19 CM850, Бюллетень [[4021592 — QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual\|4021592]]. См. процедуру 006-017 в разделе 6. | 2А |  |

#### ШАГ 1D. Проверьте давление подачи топлива на топливном коллекторе.

| **Условия:** Выключите замок зажигания. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте давление подачи топлива на топливном коллекторе. Закройте клапан подачи топлива. Удалите пробку M14 STOR из впускного коллектора топлива. Установите фитинг CompuchekTM, номер детали 3824844 или эквивалент, в впускном коллекторе топлива. Подключите вакуумный калибр и адаптер, номер 3164491 или эквивалент, и цифровой мультиметр, номер 3164488 или 3164489, или эквивалент, к фитингу CompuchekTM. Откройте клапан подачи топлива. Запуск и эксплуатация двигателя при низком и высоком холостом ходу. Запись показаний давления на входе топлива. | Давление на входе в топливо всегда меньше 34,5 кПаГ[5 psig]?  Заменить топливный насос. Используйте следующую процедуру: Руководство по эксплуатации QSK19 и модульные двигатели общей железнодорожной системы QSK19 CM850, Бюллетень [[4021592 — QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual\|4021592]]. См. процедуру 005-016 в разделе 5. | 2А |
| Давление на входе в топливо всегда меньше 34,5 кПаГ[5 psig]? **NORepair:** См. руководство по эксплуатации изготовителя оригинального оборудования (OEM) для снижения давления на входе топлива. | 2А |  |

### ШАГ 2. Очистите код ошибки.

#### ШАГ 2A. Отключите код неисправности.

| **Условия:** Соединить все компоненты. Включите зажигание. Подключите инструмент электронного сервиса INSITETM. Управляйте двигателем. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Отключите код неисправности. Используйте инструмент электронного сервиса INSITETM для проверки неактивности кода ошибки. | Код 2261 неактивен? *Да | 2В |
| Код 2261 неактивен? **NORepair:** Возврат к шагам устранения неполадок или свяжитесь с авторизованным местом ремонта Cummins®, если все шаги были завершены и проверены снова. | 1А |  |

#### ШАГ 2B. Сбросьте неактивные коды неисправностей.

| **Условия:** Соединить все компоненты. Включите зажигание. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Сбросьте неактивные коды неисправностей. Используйте инструмент электронного сервиса INSITETM для очистки кодов неактивных ошибок. | Все коды неисправностей очищены? *Да | Ремонт завершён |
| Все коды неисправностей очищены? **НЕТ** | Соответствующие шаги по устранению неполадок |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ## Warnings and Cautions
>
> **CAUTION · Осторожно**
> To reduce the possibility of damaging a new engine control module (ECM), all other active fault codes must be investigated before replacing the ECM.
>
> **CAUTION · Осторожно**
> To reduce the possibility of pin and harness damage, use the following test leads when taking a measurement: Part Number 3822758 - male Deutsch™/AMP™/Metri-Pack™ test lead; Part Number 3823993 - male Deutsch™ test lead.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the low-pressure fuel system. |  |
> |  | **STEP 1A.** Check the fuel supply pressure sensor. | INSITE™ electronic service tool and pressure gauge readings within 14 kPa \[2 psia\] of each other? |
> |  | **STEP 1B.** Check the fuel supply lines. | Any fuel lines damaged, kinked, or restricted? |
> |  | **STEP 1C.** Check the stage 2 fuel filter restriction. | Stage 2 fuel filter restriction within specification? |
> |  | **STEP 1C-1.** Check the fuel filter head. | Stage 2 fuel filter restriction within specification? |
> |  | **STEP 1D.** Check the fuel supply pressure at the fuel manifold. | Fuel inlet pressure always less than 34.5 kPaG \[5 psig\]? |
> | STEP 2. | Clear the fault code. |  |
> |  | **STEP 2A.** Disable the fault code. | Fault Code 2261 inactive? |
> |  | **STEP 2B.** Clear the inactive fault codes. | All fault codes cleared? |
>
> ### STEP 1. Check the low- pressure fuel system.
>
> #### STEP 1A. Check the fuel supply pressure sensor.
>
> | **Conditions:** Connect the Compuchek™ tool. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the fuel supply pressure sensor. Start and operate the engine at high idle. Record the fuel supply sensor reading in INSITE™ electronic service tool. Record the fuel supply pressure reading on a pressure gauge installed in place of the fuel supply pressure sensor. Use the following procedure the Service Manual QSK19 and QSK19 CM850 Modular Common Rail System Engines, Bulletin [[4021592 — QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual\|4021592]], for the stage 2 filters in the Measure section. Refer to Procedure 006-024 in Section 6. | INSITE™ electronic service tool and pressure gauge readings within 14 kPa \[2 psia\] of each other? **YES** | 1B |
> | INSITE™ electronic service tool and pressure gauge readings within 14 kPa \[2 psia\] of each other? **NORepair:** Replace the fuel supply pressure sensor. Refer to Procedure 019-398 in Section 19. | 2A |  |
>
> #### STEP 1B. Check the fuel supply lines.
>
> | **Conditions:** Turn keyswitch OFF. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Examine the fuel supply lines for damages, kinks, restrictions. Use the following procedure the Service Manual QSK19 and QSK19 CM850 Modular Common Rail System Engines, Bulletin [[4021592 — QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual\|4021592]]. Refer to Procedure 006-024 in Section 6. | Any fuel lines damaged, kinked, or restricted? **YESRepair:** Replace the fuel line(s). | 2A |
> | Any fuel lines damaged, kinked, or restricted? **NO** | 1C |  |
>
> #### STEP 1C. Check the stage 2 fuel filter restriction.
>
> | **Conditions:** Turn keyswitch OFF. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the stage 2 filter restriction. Use the following procedure the Service Manual QSK19 and QSK19 CM850 Modular Common Rail System Engines, Bulletin [[4021592 — QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual\|4021592]]. Refer to Procedure 006-020 in Section 6. | Stage 2 fuel filter restriction within specification? **YES** | 1D |
> | Stage 2 fuel filter restriction within specification? **NORepair:** Replace the stage 2 fuel filters. Use the following procedure the Service Manual QSK19 and QSK19 CM850 Modular Common Rail System Engines, Bulletin [[4021592 — QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual\|4021592]]. Refer to Procedure 006-076 in Section 6. | 1C-1 |  |
>
> #### STEP 1C-1. Check the fuel filter head.
>
> | **Conditions:** Turn keyswitch OFF. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the stage 2 fuel filter restriction. Use the following procedure the Service Manual QSK19 and QSK19 CM850 Modular Common Rail System Engines, Bulletin [[4021592 — QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual\|4021592]]. Refer to Procedure 006-020 in Section 6. | Stage 2 fuel filter restriction within specification? **YES** | 2A |
> | Stage 2 fuel filter restriction within specification? **NORepair:** Replace the stage 2 fuel filter head. Use the following procedure the Service Manual QSK19 and QSK19 CM850 Modular Common Rail System Engines, Bulletin [[4021592 — QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual\|4021592]]. Refer to Procedure 006-017 in Section 6. | 2A |  |
>
> #### STEP 1D. Check the fuel supply pressure at the fuel manifold.
>
> | **Conditions:** Turn keyswitch OFF. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the fuel supply pressure at the fuel manifold. Close the fuel supply valve. Remove the M14 STOR plug from the fuel inlet manifold. Install a Compuchek™ fitting, Part Number 3824844, or equivalent, in the fuel inlet manifold. Connect the vacuum gauge and adapter, Part Number 3164491, or equivalent, and digital multimeter, Part Number 3164488 or 3164489, or equivalent, to the Compuchek™ fitting. Open the fuel supply valve. Start and operate the engine at low idle and high idle. Record the fuel inlet pressure readings. | Fuel inlet pressure always less than 34.5 kPaG \[5 psig\]? **YESRepair:** Replace the fuel pump. Use the following procedure the Service Manual QSK19 and QSK19 CM850 Modular Common Rail System Engines, Bulletin [[4021592 — QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual\|4021592]]. Refer to Procedure 005-016 in Section 5. | 2A |
> | Fuel inlet pressure always less than 34.5 kPaG \[5 psig\]? **NORepair:** Refer to the original equipment manufacturer (OEM) service manual to reduce fuel inlet pressure. | 2A |  |
>
> ### STEP 2. Clear the fault code.
>
> #### STEP 2A. Disable the fault code.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. Operate the engine. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Disable the fault code. Use INSITE™ electronic service tool to verify the fault code is inactive. | Fault Code 2261 inactive? **YES** | 2B |
> | Fault Code 2261 inactive? **NORepair:** Return to the troubleshooting steps or contact a Cummins® Authorized Repair Location if all steps have been completed and checked again. | 1A |  |
>
> #### STEP 2B. Clear the inactive fault codes.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Clear the inactive fault codes. Use INSITE™ electronic service tool to clear the inactive fault codes. | All fault codes cleared? **YES** | Repair complete |
> | All fault codes cleared? **NO** | Appropriate troubleshooting steps |  |
