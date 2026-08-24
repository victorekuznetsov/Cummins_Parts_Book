---
aliases:
  - "Синхронизация агрегатов не включается по запросу"
type: "Процедура"
doc: "116-t02-1056"
title_en: "Multiple Unit Synchronization Not Active When Requested"
title_ru: "Синхронизация агрегатов не включается по запросу"
modified: "2009-07-15"
engines:
  - "41349633"
families:
  - "QSK19"
manuals:
  - "4021617"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1056.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/116-t02-1056.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/116"
  - "перевод/машинный"
---

# Multiple Unit Synchronization Not Active When Requested
**Синхронизация агрегатов не включается по запросу**

> [!abstract] Процедура · `116-t02-1056`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2009-07-15
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1056.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/116-t02-1056.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

- Многократная синхронизация активна, когда **не** Запрос.

- ECM ** не** взаимодействует с панелью клиентского интерфейса.

### Как пользоваться этим деревом

По этому дереву симптомов можно вести поиск неисправности. Начните с шага 1 поиска неисправностей. На шаге 2 система задаст ряд вопросов и по симптому выдаст перечень действий по поиску неисправности.

### Практические замечания

Многофункциональный коммутатор 2 и 1 синхронизации сигнальных цепей являются опцией для панели CIB.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте окно интерфейса клиента. |  |
|  | **STEP 1A.** Проверьте дисплей блока DCU410 на наличие неисправностей. |  |
|  | **STEP 1A-1.** Проверьте провод блока питания DCU410 на напряжение +24-VDC. |  |
|  | **STEP 1B.** Проверить несколько схем синхронизации блоков на наличие открытого. |  |
|  | **STEP 1C.** Проверьте несколько схем синхронизации блоков для короткого провода к проводу. |  |
|  | **STEP 1D.** Проверить несколько схем синхронизации блоков на короткое время до заземления. |  |
| ШАГ 2. | Проверьте жгут проводов изготовителя машины. |  |
|  | **STEP 2A.** Проверить несколько схем синхронизации блоков на наличие открытого. |  |
|  | **STEP 2B.** Проверьте несколько схем синхронизации для короткого провода. |  |
|  | **STEP 2C.** Проверить несколько схем синхронизации блоков на короткое время до заземления. |  |

### ШАГ 1. Проверьте окно интерфейса клиента.

#### ШАГ 1A. Проверьте дисплей блока DCU410 на наличие неисправностей.

| **Условия: ** Найдите дисплей блока DCU410. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте дисплей блока DCU410 для указания неисправностей. | DCU410 указывает на неисправность (неисправности)? *Да** | 1В |
| DCU410 указывает на неисправность (неисправности)? ** НЕТ** | 1А-1-1 |  |

#### ШАГ 1A-1. Проверьте провод блока питания DCU410 на напряжение +24-VDC.

| **Условия: ** Откройте окно интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте напряжение на батарее 1 напряжения (переключенной мощности) в блоке DCU410. Поместите один тест на провод напряжения батареи 1 (переключенной мощности) в блок DCU410. Поместите другой испытательный щуп на панельную площадку. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Меньше +24-VDC? *** Ремонт:** Проверить аккумуляторы. См. руководство по обслуживанию OEM. | Ремонт завершён |
| Меньше +24-VDC? ** НЕТ** | 1В |  |

#### ШАГ 1B. Проверьте несколько схем синхронизации блоков для открытого.

| **Условия: ** Откройте окно интерфейса клиента. Отсоедините многофункциональный коммутатор 2 синхронизации сигнального провода от разъемов X4 и C2. Отсоедините многофункциональный коммутатор синхронизации 1 сигнального провода от разъемов X4 и C2. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте несколько проводов сигнала синхронизации переключателя для открытого. Поместите один испытательный щуп на многофункциональный коммутатор синхронизации 1 сигнального провода на разъеме X4. Поместите другой испытательный щуп на многофункциональный коммутатор синхронизации 1 сигнального провода на разъеме C2. Поместите один испытательный щуп на многофункциональный коммутатор синхронизации 2 сигнального провода на разъеме X4. Поместите другой испытательный щуп на многофункциональный коммутатор 2 синхронизации сигнального провода на разъеме C2. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да** | 1С |
| Менее 10 Ом? **NORepair:** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |  |

#### ШАГ 1C. Проверьте несколько цепей синхронизации блоков для короткого провода к проводу.

| **Условия: ** Откройте окно интерфейса клиента. Отключите несколько проводов сигнала синхронизации блока в соединении X4. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте несколько проводов сигнала синхронизации переключателя для короткого провода к проводу. Поместите один испытательный щуп на многофункциональный коммутатор синхронизации 1 сигнального провода в соединение X4. Поместите другой испытательный щуп на все другие провода в соединение X4. Поместите один испытательный щуп на многофункциональный коммутатор синхронизации 2 сигнального провода в соединение X4. Поместите другой испытательный щуп на все другие провода в соединение X4. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да** | 1D |
| Менее 10 Ом? **NORepair:** Заменить соединение X4. Обратитесь в авторизованный сервисный центр Cummins®. | Ремонт завершён |  |

#### ШАГ 1D. Проверьте несколько схем синхронизации блоков для короткого наземного.

| **Условия: ** Откройте окно интерфейса клиента. Отключите разъем CLU. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте несколько проводов сигнала синхронизации переключателя для короткого наземного. Поместите один испытательный щуп на многофункциональный коммутатор синхронизации 1 сигнального провода в соединение X4. Поместите другой испытательный щуп на панельную площадку. Поместите один испытательный щуп на многофункциональный коммутатор синхронизации 2 сигнального провода в соединение X4. Поместите другой испытательный щуп на панельную площадку. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *** Заменить соединение X4. Обратитесь в авторизованный сервисный центр Cummins®. | Ремонт завершён |
| Менее 10 Ом? ** НЕТ** | 2А |  |

### ШАГ 2. Проверьте жгут проводов изготовителя машины.

#### ШАГ 2A. Проверьте несколько схем синхронизации блоков для открытого.

| **Условия: ** Расположение проводной упряжки OEM. Отсоедините многофункциональный коммутатор синхронизации 1 сигнального провода от разъема C2 и 50-контактного ECM. Отсоедините многофункциональный коммутатор синхронизации 2 сигнального провода от разъема C2 и 50-контактного ECM. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте несколько проводов сигнала синхронизации переключателя для открытого. Поместите один испытательный щуп на многофункциональный коммутатор синхронизации 1 сигнального провода на разъеме C2 на панели. Поместите другой испытательный щуп на многоцелевой коммутатор синхронизации 1 сигнального провода на 50-контактном разъеме ECM. Поместите один испытательный щуп на многофункциональный коммутатор синхронизации 2 сигнального провода на разъеме C2 на панели. Поместите другой испытательный щуп на многоцелевой коммутатор синхронизации 2 сигнального провода на 50-контактный разъем ECM. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да** | 2В |
| Менее 10 Ом? **NORepair:** Заменить провод. См. сервисное руководство изготовителя машины. | Ремонт завершён |  |

#### ШАГ 2B. Проверьте несколько цепей синхронизации блоков для короткого провода к проводу.

| **Условия: ** Откройте окно интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте несколько проводов сигнала синхронизации переключателя для короткого провода к проводу. Поместите один испытательный щуп на многофункциональный коммутатор синхронизации 1 сигнального провода на разъеме C2. Поместите другой испытательный щуп на все другие провода в разъем С2. Поместите один испытательный щуп на многофункциональный коммутатор синхронизации 2 сигнального провода на разъеме C2. Поместите другой испытательный щуп на все другие провода в разъем С2. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *** Заменить разъем.[[99-019-208 — Deutsch HDP20 and HD30 Connector Series\|См. процедуру 019-208 (Deutsch&Trade; HD20 и HD30 Connector Series) в разделе 19 в руководстве по устранению неполадок и ремонту, электронной системе управления, модульной общей железнодорожной системе QSK19 CM850, руководстве по устранению неполадок и ремонту, электронной системе управления, QSK38, QSK50 и QSK60 (модульной общей железнодорожной системе CM850), бюллетене 4021533.]] | Ремонт завершён |
| Менее 10 Ом? ** НЕТ** | 2C |  |

#### ШАГ 2C. Проверьте несколько схем синхронизации блоков для короткого наземного.

| **Условия: ** Откройте окно интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте несколько проводов сигнала синхронизации переключателя для короткого наземного. Поместите один испытательный щуп на многофункциональный коммутатор синхронизации 1 сигнального провода на разъеме C2. Поместите другой испытательный щуп на панельную площадку. Поместите один испытательный щуп на многофункциональный коммутатор синхронизации 2 сигнального провода на разъеме C2. Поместите другой испытательный щуп на панельную площадку. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *** Заменить разъем.[[99-019-208 — Deutsch HDP20 and HD30 Connector Series\|См. процедуру 019-208 (Deutsch&Trade; HD20 и HD30 Connector Series) в разделе 19 в руководстве по устранению неполадок и ремонту, электронной системе управления, модульной общей железнодорожной системе QSK19 CM850, руководстве по устранению неполадок и ремонту, электронной системе управления, QSK38, QSK50 и QSK60 (модульной общей железнодорожной системе CM850), бюллетене 4021533.]] | Ремонт завершён |
| Менее 10 Ом? ** НЕТ** | Обратитесь в авторизованный сервисный центр Cummins®. |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> - Multiple Unit Synchronization Active when **not** Requested.
>
> - ECM is **not** communicating with customer interface box panel.
>
> ### How To Use This Tree
>
> This symptom tree can be used to troubleshoot a malfunction. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.
>
> ### Shoptalk
>
> The multiple unit synchronization switch 2 and 1 signal circuits are an option for the CIB panel.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the customer interface box. |  |
> |  | **STEP 1A.** Check the DCU410 unit display for faults. |  |
> |  | **STEP 1A-1.** Check the DCU410 unit power supply wire for voltage +24-VDC. |  |
> |  | **STEP 1B.** Check the multiple unit synchronization circuits for an open. |  |
> |  | **STEP 1C.** Check the multiple unit synchronization circuits for a wire-to-wire short. |  |
> |  | **STEP 1D.** Check the multiple unit synchronization circuits for a short to ground. |  |
> | STEP 2. | Check the OEM wiring harness. |  |
> |  | **STEP 2A.** Check the multiple unit synchronization circuits for an open. |  |
> |  | **STEP 2B.** Check the multiple unit synchronization circuits for a wire-to-wire short. |  |
> |  | **STEP 2C.** Check the multiple unit synchronization circuits for a short to ground. |  |
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
> #### STEP 1B. Check the multiple unit synchronization circuits for an open.
>
> | **Conditions:** Open the customer interface box. Disconnect the multiple unit synchronization switch 2 signal wire from the X4 and C2 connectors. Disconnect the multiple unit synchronization switch 1 signal wire from the X4 and C2 connectors. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the multiple unit synchronization switch signal wires for an open. Place one test lead on the multiple unit synchronization switch 1 signal wire at the X4 connector. Place the other test lead on the multiple unit synchronization switch 1 signal wire at the C2 connector. Place one test lead on the multiple unit synchronization switch 2 signal wire at the X4 connector. Place the other test lead on the multiple unit synchronization switch 2 signal wire at the C2 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1C |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |
>
> #### STEP 1C. Check the multiple unit synchronization circuits for a wire-to-wire short.
>
> | **Conditions:** Open the customer interface box. Disconnect the multiple unit synchronization signal wires at the X4 connection. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the multiple unit synchronization switch signal wires for a wire-to-wire short. Place one test lead on the multiple unit synchronization switch 1 signal wire at the X4 connection. Place the other test lead on all other wires at the X4 connection. Place one test lead on the multiple unit synchronization switch 2 signal wire at the X4 connection. Place the other test lead on all other wires at the X4 connection. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1D |
> | Less than 10 ohms? **NORepair:** Replace the X4 connection. Contact a Cummins® Authorized Repair Location. | Repair complete |  |
>
> #### STEP 1D. Check the multiple unit synchronization circuits for a short to ground.
>
> | **Conditions:** Open the customer interface box. Disconnect the CLU connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the multiple unit synchronization switch signal wires for a short to ground. Place one test lead on the multiple unit synchronization switch 1 signal wire at the X4 connection. Place the other test lead on panel ground. Place one test lead on the multiple unit synchronization switch 2 signal wire at the X4 connection. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the X4 connection. Contact a Cummins® Authorized Repair Location. | Repair complete |
> | Less than 10 ohms? **NO** | 2A |  |
>
> ### STEP 2. Check the OEM wiring harness.
>
> #### STEP 2A. Check the multiple unit synchronization circuits for an open.
>
> | **Conditions:** Locate the OEM wiring harness. Disconnect the multiple unit synchronization switch 1 signal wire from the C2 and 50-pin ECM connector. Disconnect the multiple unit synchronization switch 2 signal wire from the C2 and 50-pin ECM connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the multiple unit synchronization switch signal wires for an open. Place one test lead on the multiple unit synchronization switch 1 signal wire at the C2 connector on panel. Place the other test lead on the multiple unit synchronization switch 1 signal wire at the 50-pin ECM connector. Place one test lead on the multiple unit synchronization switch 2 signal wire at the C2 connector on panel. Place the other test lead on the multiple unit synchronization switch 2 signal wire at the 50-pin ECM connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 2B |
> | Less than 10 ohms? **NORepair:** Replace the wire. Refer to the OEM service manual. | Repair complete |  |
>
> #### STEP 2B. Check the multiple unit synchronization circuits for a wire-to-wire short.
>
> | **Conditions:** Open the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the multiple unit synchronization switch signal wires for a wire-to-wire short. Place one test lead on the multiple unit synchronization switch 1 signal wire at the C2 connector. Place the other test lead on all other wires at the C2 connector. Place one test lead on the multiple unit synchronization switch 2 signal wire at the C2 connector. Place the other test lead on all other wires at the C2 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace connector. [[99-019-208 — Deutsch HDP20 and HD30 Connector Series\|Refer to Procedure 019-208 (Deutsch&trade; HD20 and HD30 Connector Series) in Section 19 in the Troubleshooting and Repair Manual, Electronic Control System, QSK19 CM850 Modular Common Rail System, Bulletin 4021493 or the Troubleshooting and Repair Manual, Electronic Control System, QSK38, QSK50, and QSK60 (CM850 Modular Common Rail System), Bulletin 4021533.]] | Repair complete |
> | Less than 10 ohms? **NO** | 2C |  |
>
> #### STEP 2C. Check the multiple unit synchronization circuits for a short to ground.
>
> | **Conditions:** Open the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the multiple unit synchronization switch signal wires for a short to ground. Place one test lead on the multiple unit synchronization switch 1 signal wire at the C2 connector. Place the other test lead on panel ground. Place one test lead on the multiple unit synchronization switch 2 signal wire at the C2 connector. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace connector. [[99-019-208 — Deutsch HDP20 and HD30 Connector Series\|Refer to Procedure 019-208 (Deutsch&trade; HD20 and HD30 Connector Series) in Section 19 in the Troubleshooting and Repair Manual, Electronic Control System, QSK19 CM850 Modular Common Rail System, Bulletin 4021493 or the Troubleshooting and Repair Manual, Electronic Control System, QSK38, QSK50, and QSK60 (CM850 Modular Common Rail System), Bulletin 4021533.]] | Repair complete |
> | Less than 10 ohms? **NO** | Contact a Cummins® Authorized Repair Location. |  |
