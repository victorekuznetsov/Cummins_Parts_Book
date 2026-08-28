---
aliases:
  - "Код 351 — питание форсунок — неисправное устройство"
type: "Процедура"
doc: "123-t05-351"
title_en: "FAULT CODE 351 - Injector Power Supply - Bad Intelligent Device or Component"
title_ru: "Код 351 — питание форсунок — неисправное устройство"
modified: "2021-11-03"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4022094"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/123/123-t05-351.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/123-t05-351.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/123"
  - "перевод/машинный"
---

# FAULT CODE 351 - Injector Power Supply - Bad Intelligent Device or Component
**Код 351 — питание форсунок — неисправное устройство**

> [!abstract] Процедура · `123-t05-351`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4022094 — QSK19 CM2150 and CM2670 Electronic Control System Troubleshooting and Repair Manual|4022094]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2021-11-03
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/123/123-t05-351.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/123-t05-351.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

## Предупреждения и меры предосторожности

> [!danger] ОПАСНО
> Аккумуляторные батареи выделяют взрывоопасные газы. Чтобы снизить риск травмы, перед обслуживанием аккумуляторных батарей обязательно проветрите помещение. Чтобы снизить риск искрения, минусовой (-) провод аккумуляторной батареи снимайте первым, а подсоединяйте последним.

> [!warning] ОСТОРОЖНО
> Чтобы уменьшить вероятность повреждения новой ECM, все другие активные коды неисправностей должны быть исследованы до замены ECM.

> [!warning] ОСТОРОЖНО
> Для уменьшения возможности повреждения штифта и проводов жгута проводов используйте при проведении измерений следующий испытательный щуп: Номер детали 3164133 - пробный щуп типа "Дойч".

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте коды неисправностей. |  |
|  | **СТЭП 1А.** Прочитайте коды неисправностей. | Коды 322, 323, 324, 325, 331 и 332, активные во время работы двигателя? |
| ШАГ 2. | Проверьте напряжение батареи 1. |  |
|  | **STEP 2A.** Проверить разъемы и предохранители напряжения батареи 1. | Ущерб был замечен? |
|  | **ШАГ 2В.** Проверить наличие открытой цепи. | Менее 0,5 Ом? |
|  | **STEP 2C.** Проверьте наличие открытой цепи в цепи напряжения батареи 1. | Менее 10 Ом? |
| ШАГ 3. | Проверить наличие этого кода неисправности. |  |
|  | **STEP 3A.** Управляйте двигателем и определяйте, существует ли условие кода неисправности. | Код 351 неисправности повторяется во время работы двигателя, в то время как коды 322, 323, 324, 325, 331 и 332 не встречаются? |
| ШАГ 4. | Сбросьте коды неисправностей. |  |
|  | **STEP 4A.** Отключить код ошибки. | Код 351 неактивен? |
|  | **STEP 4B.** Очистить коды неактивных ошибок. | Все коды неисправностей очищены? |

### ШАГ 1. Проверьте коды неисправностей.

#### ШАГ 1A. Считайте коды неисправностей.

| **Условия:** Подключить электронный сервисный инструмент INSITETM Включить переключатель зажигания. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Считайте коды неисправностей. Запустите двигатель и запускайте его на холостом ходу в течение 1 минуты. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Коды 322, 323, 324, 325, 331 и 332, активные во время работы двигателя? *Да | Соответствующий код неисправности дерево |
| Коды 322, 323, 324, 325, 331 и 332, активные во время работы двигателя? **НЕТ** | 2А |  |

### ШАГ 2. Проверьте напряжение батареи 1.

#### ШАГ 2A. Проверьте разъем и предохранители питания ECM 4-pin.

| **Условия:** Выключите замок зажигания. Отсоедините 4-контактный разъем питания от ECM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Осмотрите 4-контактный разъем питания ECM и предохранитель для следующего: Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема разъема разъема или на разъеме контакты Разъема оболочки разбитого Провода изоляционного повреждения Поврежденный разъем блокировки вкладки. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Ущерб был замечен? **Ремонт:** Очистить разъем и штифты. Ремонт или замена поврежденной проводов жгута, булавок, предохранителей или разъемов. | 4А |
| Ущерб был замечен? **НЕТ** | 2В |  |

#### ШАГ 2B. Проверьте цепь на обрыв.

| **Условия:** Выключите замок зажигания. Отсоедините 4-контактный разъем питания от ECM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте цепь на обрыв. Измерьте сопротивление между штифтами напряжения батареи 1 на 4-контактном разъеме питания SUPPLY и штифтами положительной (+) батареи на положительном (+) соединении батареи. Используйте схему проводов для идентификации контакта с разъемом и следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Менее 0,5 Ом? *Да | 2C |
| Менее 0,5 Ом? **NORepair:** Ремонтировать или заменить электропроводку ECM, предохранители или держатели предохранителей, или очистить соединения терминала батареи. См. процедуру 019-206 в разделе 19. См. процедуру 019-198 в разделе 19. | 4А |  |

#### ШАГ 2C. Проверьте наличие открытой цепи в цепи напряжения батареи 1.

| **Условия:** Выключите замок зажигания. Отсоедините электропроводку электропроводки ECM с 4-контактным разъемом питания от ECM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте наличие открытой цепи в цепи электропитания ECM. Измерьте сопротивление между отрицательными (-) штифтами батареи на 4-контактном разъеме питания ECM к заземлению блока двигателя. Используйте схему проводов для идентификации контакта с разъемом и следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Менее 10 Ом? *Да | 3А |
| Менее 10 Ом? **NORepair:** Ремонтировать или заменить электропроводку ECM, предохранители или держатели предохранителей, или очистить соединения терминала батареи. См. процедуру 019-206 в разделе 19. См. процедуру 019-198 в разделе 19. | 4А |  |

### ШАГ 3. Проверить наличие этого кода неисправности.

#### ШАГ 3A. Управляйте двигателем и определяйте, существует ли условие кода неисправности.

| **Условия:** Соединить все компоненты. Подключите инструмент электронного сервиса INSITETM. Включите зажигание. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Управляйте двигателем и определяйте, существует ли еще условие кода неисправности. Работайте с двигателем на высоком холостом ходу, без нагрузки. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. Примечание: Электронное сервисное оборудование INSITETM также может использоваться для мониторинга напряжения питания ECM и напряжения питания топливных форсунок. | Код 351 неисправности повторяется во время работы двигателя, в то время как коды 322, 323, 324, 325, 331 и 332 неисправности форсунки не происходят.  Заменить ЭКМ. См. процедуру 019-031 в разделе 19. | 4А |
| Код 351 неисправности повторяется во время работы двигателя, в то время как коды 322, 323, 324, 325, 331 и 332 неисправности форсунки не происходят. **NORepair:** Возможна предельная нагрузка на аккумулятор. Убедитесь, что батареи полностью заряжены. | 4А |  |

### ШАГ 4. Сбросьте коды неисправностей.

#### ШАГ 4A. Отключите код неисправности.

| **Условия:** Соединить все компоненты. Включите зажигание. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Отключите код неисправности. Запустите двигатель и запускайте его на холостом ходу в течение 1 минуты. Используйте инструмент электронного сервиса INSITETM для проверки неактивности кода ошибки. | Код 351 неактивен? *Да | 4B |
| Код 351 неактивен? **NORepair:** Возврат к шагам устранения неполадок или свяжитесь с местным авторизованным местом ремонта Cummins®, если все шаги были завершены и проверены снова. | 1А |  |

#### ШАГ 4B. Сбросьте неактивные коды неисправностей.

| **Условия:** Соединить все компоненты. Включите зажигание. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Сбросьте неактивные коды неисправностей. Используйте инструмент электронного сервиса INSITETM для удаления неактивных кодов неисправностей. | Все коды неисправностей очищены? *Да | Ремонт завершён |
| Все коды неисправностей очищены? **НЕТ** | Соответствующие шаги по устранению неполадок |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ## Warnings and Cautions
>
> **WARNING · Опасно**
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.
>
> **CAUTION · Осторожно**
> To reduce the possibility of damaging a new ECM, all other active fault codes must be investigated prior to replacing the ECM.
>
> **CAUTION · Осторожно**
> To reduce the possibility of pin and harness damage, use the following test lead when taking a measurement: Part Number 3164133 - male Deutsch test lead.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the fault codes. |  |
> |  | **STEP 1A.** Read the fault codes. | Fault Codes 322, 323, 324, 325, 331, and 332 active during engine operation? |
> | STEP 2. | Check the battery 1 voltage. |  |
> |  | **STEP 2A.** Inspect the battery 1 voltage connectors and fuses. | Damage observed? |
> |  | **STEP 2B.** Check for an open circuit. | Less than 0.5 ohms? |
> |  | **STEP 2C.** Check for an open circuit in the battery 1 voltage circuit. | Less than 10 ohms? |
> | STEP 3. | Validate the occurrence of this fault code. |  |
> |  | **STEP 3A.** Operate the engine and determine if fault code condition exists. | Fault Code 351 reoccurs during engine operation, while injector Fault Codes 322, 323, 324, 325, 331, and 332 do not occur? |
> | STEP 4. | Clear the fault codes. |  |
> |  | **STEP 4A.** Disable the fault code. | Fault Code 351 inactive? |
> |  | **STEP 4B.** Clear the inactive fault codes. | All fault codes cleared? |
>
> ### STEP 1. Check the fault codes.
>
> #### STEP 1A. Read the fault codes.
>
> | **Conditions:** Connect the INSITE™ electronic service tool Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Read the fault codes. Start the engine and let it idle for 1 minute. Use INSITE™ electronic service tool to read the fault codes. | Fault Codes 322, 323, 324, 325, 331, and 332 active during engine operation? **YES** | Appropriate fault code troubleshooting tree |
> | Fault Codes 322, 323, 324, 325, 331, and 332 active during engine operation? **NO** | 2A |  |
>
> ### STEP 2. Check the battery 1 voltage.
>
> #### STEP 2A. Inspect the ECM 4-pin power connector and fuses.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the ECM 4-pin power connector from the ECM. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the ECM 4-pin power connector and fusess for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Damage observed? **YESRepair:** Clean the connector and pins. Repair or replace the damaged harness, pins, fuses, or connectors. | 4A |
> | Damage observed? **NO** | 2B |  |
>
> #### STEP 2B. Check for an open circuit.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the ECM 4-pin power connector from the ECM. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for an open circuit. Measure the resistance between the battery 1 voltage pins at the ECM 4-pin power connector SUPPLY harness and the battery positive (+) pins at the battery positive (+) connection. Use a wiring diagram for connector pin identification and the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Less than 0.5 ohms? **YES** | 2C |
> | Less than 0.5 ohms? **NORepair:** Repair or replace the ECM power supply harness, fuses, or fuse holders, or clean the battery terminal connections. Refer to Procedure 019-206 in Section 19. Refer to Procedure 019-198 in Section 19. | 4A |  |
>
> #### STEP 2C. Check for an open circuit in the battery 1 voltage circuit.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the ECM 4-pin power connector harness from the ECM. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for an open circuit in the ECM power supply circuit. Measure the resistance between the battery negative (-) pins at the ECM 4-pin power connector to engine block ground. Use a wiring diagram for connector pin identification and the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Less than 10 ohms? **YES** | 3A |
> | Less than 10 ohms? **NORepair:** Repair or replace the ECM power supply harness, fuses, or fuse holders, or clean the battery terminal connections. Refer to Procedure 019-206 in Section 19. Refer to Procedure 019-198 in Section 19. | 4A |  |
>
> ### STEP 3. Validate the occurrence of this fault code.
>
> #### STEP 3A. Operate the engine and determine if fault code condition exists.
>
> | **Conditions:** Connect all components. Connect INSITE™ electronic service tool. Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Operate the engine and determine whether the fault code condition still exists. Operate the engine at high idle, no load. Use INSITE™ electronic service tool to read the fault codes. Note: INSITE™ electronic service tool can also be used to monitor ECM power supply and injector power supply voltages. | Fault Code 351 reoccurs during engine operation, while injector Fault Codes 322, 323, 324, 325, 331, and 332 do **not** occur? **YESRepair:** Replace the ECM. Refer to Procedure 019-031 in Section 19. | 4A |
> | Fault Code 351 reoccurs during engine operation, while injector Fault Codes 322, 323, 324, 325, 331, and 332 do **not** occur? **NORepair:** A marginal battery voltage condition is possible. Make sure that the batteries are fully charged. | 4A |  |
>
> ### STEP 4. Clear the fault codes.
>
> #### STEP 4A. Disable the fault code.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Disable the fault code. Start the engine and let it idle for 1 minute. Use INSITE™ electronic service tool to verify that the fault code is inactive. | Fault Code 351 inactive? **YES** | 4B |
> | Fault Code 351 inactive? **NORepair:** Return to the troubleshooting steps or contact a local Cummins® Authorized Repair Location if all steps have been completed and checked again. | 1A |  |
>
> #### STEP 4B. Clear the inactive fault codes.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Clear the inactive fault codes. Use INSITE™ electronic service tool to erase the inactive fault codes. | All fault codes cleared? **YES** | Repair complete |
> | All fault codes cleared? **NO** | Appropriate troubleshooting steps |  |
