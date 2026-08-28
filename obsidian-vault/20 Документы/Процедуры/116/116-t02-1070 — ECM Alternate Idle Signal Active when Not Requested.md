---
aliases:
  - "Сигнал альтернативного холостого хода активен без запроса"
type: "Процедура"
doc: "116-t02-1070"
title_en: "ECM Alternate Idle Signal Active when Not Requested"
title_ru: "Сигнал альтернативного холостого хода активен без запроса"
modified: "2008-05-22"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4021617"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1070.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1070.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/116"
  - "перевод/машинный"
---

# ECM Alternate Idle Signal Active when Not Requested
**Сигнал альтернативного холостого хода активен без запроса**

> [!abstract] Процедура · `116-t02-1070`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2008-05-22
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1070.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1070.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

Альтернативный сигнал бездействия ECM активен, когда **не** запрашивается.

### Как пользоваться этим деревом

По этому дереву симптомов можно вести поиск неисправности. Начните с шага 1 поиска неисправностей. На шаге 2 система задаст ряд вопросов и по симптому выдаст перечень действий по поиску неисправности.

### Практические замечания

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте окно интерфейса клиента. |  |
|  | **STEP 1A.** Проверьте дисплей блока DCU410 на наличие неисправностей. |  |
|  | **STEP 1A-1.** Проверьте провод блока питания DCU410 на напряжение +24-VDC. |  |
|  | **STEP 1B.** Проверьте наличие открытых альтернативных схем холостого/вспомогательного управления. |  |
|  | **STEP 1C.** Проверьте альтернативные схемы бездействия/вспомогательного управления для короткого провода к проводу. |  |
|  | **STEP 1D.** Проверьте альтернативные схемы бездействия/вспомогательного управления для короткого заземления. |  |
| ШАГ 2. | Проверьте жгут проводов изготовителя машины. |  |
|  | **STEP 2A.** Проверьте наличие открытых альтернативных схем холостого/вспомогательного управления. |  |
|  | **STEP 2B.** Проверьте альтернативные схемы бездействия/вспомогательного управления для короткого провода к проводу. |  |
|  | **STEP 2C.** Проверьте альтернативные схемы бездействия/вспомогательных управляющих для короткого заземления. |  |

### ШАГ 1. Проверьте окно интерфейса клиента.

#### ШАГ 1A. Проверьте дисплей блока DCU410 на наличие неисправностей.

| **Условия: **Найдите дисплей блока DCU410. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте дисплей блока DCU410 для указания неисправностей. | DCU410 указывает на неисправность (неисправности)? *Да | 1В |
| DCU410 указывает на неисправность (неисправности)? **НЕТ** | 1А-1-1 |  |

#### ШАГ 1A-1. Проверьте провод блока питания DCU410 на напряжение +24-VDC.

| **Условия: **Откройте окно интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте напряжение на батарее 1 напряжения (переключенной мощности) в блоке DCU410. Поместите один тест на провод напряжения батареи 1 (переключенной мощности) в блок DCU410. Поместите другой испытательный щуп на панельную площадку. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Меньше +24-VDC? **Ремонт:** Проверить аккумуляторы. См. руководство по обслуживанию OEM. | Ремонт завершён |
| Меньше +24-VDC? **НЕТ** | 1В |  |

#### ШАГ 1B. Проверьте альтернативные схемы бездействия / вспомогательных управляющих для открытого.

| **Условия: **Откройте окно интерфейса клиента. Отключите альтернативный простаивающий/вспомогательный регулятор выбора сигнального провода на разъемах X4 и C3. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте альтернативный простаивающий / вспомогательный управляющий выбрать сигнальный провод для открытого. Поместите один испытательный щуп на альтернативный простаивающий/вспомогательный регулятор, выберите сигнальный провод на разъеме X4. Поместите другой испытательный щуп на альтернативный простаивающий/вспомогательный регулятор, выберите сигнальный провод на разъеме C3. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да | 1С |
| Менее 10 Ом? **NORepair:** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |  |

#### ШАГ 1C. Проверьте альтернативные схемы бездействия / вспомогательного губернатора для короткой проводной проводов.

| **Условия: **Откройте окно интерфейса клиента. Отключите альтернативный простаивающий/вспомогательный регулятор выбора сигнального провода на разъеме X4. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте альтернативный простаивающий / вспомогательный регулятор выберите сигнальный провод для короткого провода к проводу. Поместите один испытательный щуп на альтернативный простаивающий/вспомогательный регулятор, выберите сигнальный провод на разъеме X4. Поместите другой испытательный щуп на все другие провода в разъем X4. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? Заменить терминальную полосу.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |
| Менее 10 Ом? **НЕТ** | 1D |  |

#### ШАГ 1D. Проверьте альтернативные холостые / вспомогательные губернаторские схемы для короткого приземления.

| **Условия: **Откройте окно интерфейса клиента. Отключите альтернативный простаивающий/вспомогательный регулятор выбора сигнального провода на разъеме X4. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте альтернативный простаивающий / вспомогательный регулятор, выберите сигнальный провод для короткого приземления. Поместите один испытательный щуп на альтернативный простаивающий/вспомогательный регулятор, выберите сигнальный провод на разъеме X4. Поместите другой испытательный щуп на панельную площадку. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? Заменить терминальную полосу.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |
| Менее 10 Ом? **НЕТ** | 2А |  |

### ШАГ 2. Проверьте жгут проводов изготовителя машины.

#### ШАГ 2A. Проверьте альтернативные схемы бездействия / вспомогательных управляющих для открытого.

| **Условия: **Откройте окно интерфейса клиента. Отключите альтернативный провод для отключения/вспомогательный управляющий выбор сигнала на разъеме C3 и 50-контактном разъеме ECM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте альтернативный простаивающий / вспомогательный управляющий выбрать сигнальный провод для открытого. Поместите один испытательный щуп на альтернативный простаивающий/вспомогательный регулятор, выберите сигнальный провод на разъеме C3. Поместите другой испытательный щуп на альтернативный простаивающий/вспомогательный регулятор, выберите сигнальный провод на 50-контактном разъеме ECM. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да | 2В |
| Менее 10 Ом? **NORepair:** Заменить провод. См. сервисное руководство изготовителя машины. | Ремонт завершён |  |

#### ШАГ 2B. Проверьте альтернативные схемы бездействия / вспомогательного губернатора для короткой проводной проводов.

| **Условия: **Откройте окно интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте альтернативный простаивающий / вспомогательный регулятор выберите сигнальный провод для короткого провода к проводу. Поместите один испытательный щуп на альтернативный простаивающий/вспомогательный регулятор, выберите сигнальный провод на разъеме C3. Поместите другой испытательный щуп на все другие провода на разъеме C3. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? Заменить разъем.[[99-019-208 — Deutsch HDP20 and HD30 Connector Series\|См. процедуру 019-208 (Deutsch&Trade; HD20 и HD30 Connector Series) в разделе 19 в руководстве по устранению неполадок и ремонту, электронной системе управления, модульной общей железнодорожной системе QSK19 CM850, руководстве по устранению неполадок и ремонту, электронной системе управления, QSK38, QSK50 и QSK60 (модульной общей железнодорожной системе CM850), бюллетене 4021533.]] | Ремонт завершён |
| Менее 10 Ом? **НЕТ** | 2C |  |

#### ШАГ 2C. Проверьте альтернативные холостые / вспомогательные губернаторские схемы для короткого приземления.

| **Условия: **Откройте окно интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте альтернативный простаивающий / вспомогательный регулятор, выберите сигнальный провод для короткого приземления. Поместите один испытательный щуп на альтернативный простаивающий/вспомогательный регулятор, выберите сигнальный провод на разъеме C3. Поместите другой испытательный щуп на панельную площадку. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? Заменить разъем.[[99-019-208 — Deutsch HDP20 and HD30 Connector Series\|См. процедуру 019-208 (Deutsch&Trade; HD20 и HD30 Connector Series) в разделе 19 в руководстве по устранению неполадок и ремонту, электронной системе управления, модульной общей железнодорожной системе QSK19 CM850, руководстве по устранению неполадок и ремонту, электронной системе управления, QSK38, QSK50 и QSK60 (модульной общей железнодорожной системе CM850), бюллетене 4021533.]] | Ремонт завершён |
| Менее 10 Ом? **НЕТ** | Обратитесь в авторизованный сервисный центр Cummins®. |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> The ECM alternate idle signal is active when **not** requested.
>
> ### How To Use This Tree
>
> This symptom tree can be used to troubleshoot a malfunction. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.
>
> ### Shoptalk
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the customer interface box. |  |
> |  | **STEP 1A.** Check the DCU410 unit display for faults. |  |
> |  | **STEP 1A-1.** Check the DCU410 unit power supply wire for voltage +24-VDC. |  |
> |  | **STEP 1B.** Check the alternate idle/auxiliary governor circuits for an open. |  |
> |  | **STEP 1C.** Check the alternate idle/auxiliary governor circuits for a wire-to-wire short. |  |
> |  | **STEP 1D.** Check the alternate idle/auxiliary governor circuits for a short to ground. |  |
> | STEP 2. | Check the OEM wiring harness. |  |
> |  | **STEP 2A.** Check the alternate idle/auxiliary governor circuits for an open. |  |
> |  | **STEP 2B.** Check the alternate idle/auxiliary governor circuits for a wire-to-wire short. |  |
> |  | **STEP 2C.** Check the alternate idle/auxiliary governor circuits for a short to ground. |  |
>
> ### STEP 1. Check the customer interface box.
>
> #### STEP 1A. Check the DCU410 unit display for faults.
>
> | **Conditions:** Locate the DCU410 unit display. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the DCU410 unit display for indication of faults. | DCU410 unit indicates fault(s)? **YES** | 1B |
> | DCU410 unit indicates fault(s)? **NO** | 1A-1 |  |
>
> #### STEP 1A-1. Check the DCU410 unit power supply wire for voltage +24-VDC.
>
> | **Conditions:** Open the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the voltage at the battery 1 voltage (switched power) at the DCU410 unit. Place one test on the battery 1 voltage (switched power) wire at the DCU410 unit. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than +24-VDC? **YESRepair:** Check the batteries. Refer to OEM service manual. | Repair complete |
> | Less than +24-VDC? **NO** | 1B |  |
>
> #### STEP 1B. Check the alternate idle/auxiliary governor circuits for an open.
>
> | **Conditions:** Open the customer interface box. Disconnect the alternate idle/auxiliary governor select signal wire at the X4 and C3 connectors. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the alternate idle/auxiliary governor select signal wire for an open. Place one test lead on the alternate idle/auxiliary governor select signal wire at the X4 connector. Place the other test lead on the alternate idle/auxiliary governor select signal wire at C3 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1C |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |
>
> #### STEP 1C. Check the alternate idle/auxiliary governor circuits for a wire-to-wire short.
>
> | **Conditions:** Open the customer interface box. Disconnect the alternate idle/auxiliary governor select signal wire at the X4 connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the alternate idle/auxiliary governor select signal wire for a wire-to-wire short. Place one test lead on the alternate idle/auxiliary governor select signal wire at the X4 connector. Place the other test lead on all other wires at the X4 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the terminal strip. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
> | Less than 10 ohms? **NO** | 1D |  |
>
> #### STEP 1D. Check the alternate idle/auxiliary governor circuits for a short to ground.
>
> | **Conditions:** Open the customer interface box. Disconnect the alternate idle/auxiliary governor select signal wire at the X4 connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the alternate idle/auxiliary governor select signal wire for a short to ground. Place one test lead on the alternate idle/auxiliary governor select signal wire at the X4 connector. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the terminal strip. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
> | Less than 10 ohms? **NO** | 2A |  |
>
> ### STEP 2. Check the OEM wiring harness.
>
> #### STEP 2A. Check the alternate idle/auxiliary governor circuits for an open.
>
> | **Conditions:** Open the customer interface box. Disconnect the alternate idle/auxiliary governor select signal wire at the C3 connector and 50-pin ECM connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the alternate idle/auxiliary governor select signal wire for an open. Place one test lead on the alternate idle/auxiliary governor select signal wire at the C3 connector. Place the other test lead on the alternate idle/auxiliary governor select signal wire at 50-pin ECM connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 2B |
> | Less than 10 ohms? **NORepair:** Replace the wire. Refer to the OEM service manual. | Repair complete |  |
>
> #### STEP 2B. Check the alternate idle/auxiliary governor circuits for a wire-to-wire short.
>
> | **Conditions:** Open the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the alternate idle/auxiliary governor select signal wire for a wire-to-wire short. Place one test lead on the alternate idle/auxiliary governor select signal wire at the C3 connector. Place the other test lead on all other wires at the C3 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace connector. [[99-019-208 — Deutsch HDP20 and HD30 Connector Series\|Refer to Procedure 019-208 (Deutsch&trade; HD20 and HD30 Connector Series) in Section 19 in the Troubleshooting and Repair Manual, Electronic Control System, QSK19 CM850 Modular Common Rail System, Bulletin 4021493 or the Troubleshooting and Repair Manual, Electronic Control System, QSK38, QSK50, and QSK60 (CM850 Modular Common Rail System), Bulletin 4021533.]] | Repair complete |
> | Less than 10 ohms? **NO** | 2C |  |
>
> #### STEP 2C. Check the alternate idle/auxiliary governor circuits for a short to ground.
>
> | **Conditions:** Open the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the alternate idle/auxiliary governor select signal wire for a short to ground. Place one test lead on the alternate idle/auxiliary governor select signal wire at the C3 connector. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace connector. [[99-019-208 — Deutsch HDP20 and HD30 Connector Series\|Refer to Procedure 019-208 (Deutsch&trade; HD20 and HD30 Connector Series) in Section 19 in the Troubleshooting and Repair Manual, Electronic Control System, QSK19 CM850 Modular Common Rail System, Bulletin 4021493 or the Troubleshooting and Repair Manual, Electronic Control System, QSK38, QSK50, and QSK60 (CM850 Modular Common Rail System), Bulletin 4021533.]] | Repair complete |
> | Less than 10 ohms? **NO** | Contact a Cummins® Authorized Repair Location. |  |
