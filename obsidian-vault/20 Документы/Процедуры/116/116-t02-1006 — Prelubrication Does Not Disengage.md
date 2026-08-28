---
aliases:
  - "Предпусковая прокачка не отключается"
type: "Процедура"
doc: "116-t02-1006"
title_en: "Prelubrication Does Not Disengage"
title_ru: "Предпусковая прокачка не отключается"
modified: "2008-05-29"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4021617"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1006.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1006.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/116"
  - "перевод/машинный"
---

# Prelubrication Does Not Disengage
**Предпусковая прокачка не отключается**

> [!abstract] Процедура · `116-t02-1006`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2008-05-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1006.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1006.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

- Прелюбрикация двигателя будет **не **отключаться.

### Как пользоваться этим деревом

По этому дереву симптомов можно вести поиск неисправности. Начните с шага 1 поиска неисправностей. На шаге 2 система задаст ряд вопросов и по симптому выдаст перечень действий по поиску неисправности.

### Практические замечания

Примечание: Провод прыгуна должен быть удален на разъеме прелюбрики, если необходимо использовать прелюбрику.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте окно интерфейса клиента. |  |
|  | **STEP 1A.** Проверьте логическую блокировку светодиодного освещения в интерфейсе клиента. |  |
|  | **STEP 1B.** Проверьте провод питания DCU410 на напряжение +24-VDC. |  |
|  | **STEP 1C.** Проверить провод активации прелюбрикации на наличие открытого источника питания. |  |
|  | **STEP 1D.** Проверить наличие провода сигнала на открытом воздухе. |  |
|  | **STEP 1E.** Проверьте активацию прелюбрикации и полные провода сигнала на наличие открытого сигнала. |  |
|  | **STEP 1F.** Проверить активацию прелюбрикации и полные провода сигнала на короткое время до заземления. |  |
| ШАГ 2. | Проверьте жгут проводов изготовителя машины. |  |
|  | **ШАГ 2А.** Проверить наличие проводов подачи и возврата для открытого источника. |  |
|  | **STEP 2B.** Проверьте наличие проводов подачи и возврата для короткого провода к проводу. |  |
|  | **STEP 2C.** Проверить проволоку подачи смазки на короткое время до заземления. |  |

### ШАГ 1. Проверьте окно интерфейса клиента.

#### ШАГ 1A. Проверьте логическое устройство клиентского интерфейса LED подсветка.

| **Условия: **Откройте окно интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте лампу с коленчатым приводом на блоке DCU 410 или удаленной панели для освещения. | Светильник с кривошипом? *Да | 1В |
| Светильник с кривошипом? **НЕТ** | Свяжитесь с авторизованным местом ремонта Cummins® |  |

#### ШАГ 1B. Проверьте провод питания DCU410 на напряжение +24-VDC.

| **Условия: **Откройте окно интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте напряжение на батарее 1 напряжения (переключенной мощности) в блоке DCU410. Поместите один испытательный щуп на провод питания напряжения батареи 1 (переключенной мощности) в блоке DCU410. Поместите другой испытательный щуп на панельную площадку. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Меньше +24-VDC? **Ремонт:** Проверить аккумуляторы. См. сервисное руководство изготовителя машины. | Ремонт завершён |
| Меньше +24-VDC? **НЕТ** | 1С |  |

#### ШАГ 1C. Проверьте провод сигнала прелюбрикационной активации на наличие открытого.

| **Условия: **Откройте окно интерфейса клиента. Отсоедините провод сигнала прелюбрикационной активации от блока DCU410. Отключите разъем C1. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте провод сигнала прелюбрикационной активации на блоке DCU410 и разъеме C1 для открытого соединения. Поместите один испытательный щуп на провод сигнала прелюбрикационной активации в блок DCU410. Поместите другой провод сигнала прелюбрикационной активации пробы на разъем С1. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да | 1D |
| Менее 10 Ом? **NORepair:** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |  |

#### ШАГ 1D. Проверьте прелюбрикационный полный сигнальный провод на наличие открытого.

| **Условия: **Откройте окно интерфейса клиента. Отсоедините провод с прелюбрикацией полного сигнала на блоке DCU410, блоке CLU и разъеме C1. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте полный сигнальный провод прелюбрики на блоке DCU410, блоке CLU и разъеме C1 для открытого. Поместите один испытательный щуп на предсмазочный полный сигнальный провод в блок DCU410. Поместите другой испытательный щуп на предсмазочный полный сигнальный провод в блоке CLU. Поместите один испытательный щуп на предсмазочный полный сигнальный провод в блок DCU410. Поместите другой испытательный щуп на провод с прелюбрикацией полного сигнала на разъеме C1. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да | 1Е |
| Менее 10 Ом? **NORepair:** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |  |

#### ШАГ 1E. Проверьте активацию прелюбрикации и полные провода сигнала для короткого провода к проводу.

| **Условия: **Откройте окно интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте активацию прелюбрикации и полный сигнальный провод в блоке DCU410 для короткого провода к проводу. Поместите один испытательный щуп на провод сигнала прелюбрикационной активации в блок DCU410. Поместите другой испытательный щуп на все другие провода в блок DCU410. Поместите один испытательный щуп на предсмазочный полный сигнальный провод в блок DCU410. Поместите другой испытательный щуп на все другие провода в блок DCU410. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? Заменить DCU410. Обратитесь в авторизованный сервисный центр Cummins®. | Ремонт завершён |
| Менее 10 Ом? **НЕТ** | 1F |  |

#### ШАГ 1F. Проверьте активацию прелюбрикации и полные провода сигнала для короткого приземления.

| **Условия: **Откройте окно интерфейса клиента. Отключите прелюбрикационную активацию и полные сигнальные провода на блоке DCU410. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте активацию прелюбрикации и полные провода сигнала на блоке DCU410 для короткого заземления. Поместите один испытательный щуп на провод сигнала прелюбрикационной активации в блок DCU410. Поместите другой испытательный щуп на панельную площадку. Поместите один испытательный щуп на предсмазочный полный сигнальный провод в блок DCU410. Поместите другой испытательный щуп на панельную площадку. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? Заменить DCU410. Обратитесь в авторизованный сервисный центр Cummins®. | Ремонт завершён |
| Менее 10 Ом? **НЕТ** | 2А |  |

### ШАГ 2. Проверьте жгут проводов изготовителя машины.

#### ШАГ 2A. Проверьте прелюбрикационные подводящие и возвращающие провода для открытого.

| **Условия: **Откройте окно интерфейса клиента. Отсоедините провода подачи и возврата прелюбрикации на разъёме C1 и датчике прелюбрикации. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте подачу и возврат проводов прелюбрики на разъеме C1 и датчике прелюбрики для открытого. Поместите один испытательный щуп на провод подачи прелюбрикации на разъеме C1. Поместите другой испытательный щуп на провод подачи прелюбрикации на датчик прелюбрики. Поместите один испытательный щуп на провод с прелюбрикацией на разъеме C1. Поместите другой испытательный щуп на провод для прелюбрикации на провод для прелюбрики для возврата на датчик для прелюбрики. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да | 2В |
| Менее 10 Ом? **NORepair:** Заменить провод. См. сервисное руководство изготовителя машины. | Ремонт завершён |  |

#### ШАГ 2B. Проверьте прелюбрикационные подводящие и возвращающие провода для короткого провода к проводу.

| **Условия: **Откройте окно интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте подачу смазки и обратные провода на разъеме C1 для короткого провода к проводу. Поместите один испытательный щуп на провод подачи прелюбрикации на разъеме C1. Поместите другой испытательный щуп на все другие провода в разъем С1. Поместите один испытательный щуп на провод с прелюбрикацией на разъеме C1. Поместите другой испытательный щуп на все другие провода в разъем С1. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? Заменить провод. См. сервисное руководство изготовителя машины. | Ремонт завершён |
| Менее 10 Ом? **НЕТ** | 2C |  |

#### ШАГ 2C. Проверьте провод подачи прелюбрикации на короткий срок до земли.

| **Условия: **Откройте окно интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте провод подачи прелюбрикации на разъеме C1 для короткого отключения. Поместите один испытательный щуп на провод подачи прелюбрикации на разъеме C1. Поместите другой испытательный щуп на землю двигателя. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? Заменить провод. См. сервисное руководство изготовителя машины. | Ремонт завершён |
| Менее 10 Ом? **NORepair:** Заменить прелюбрикационный датчик. См. руководство по обслуживанию OEM или свяжитесь с авторизованным местом ремонта Cummins®. | Ремонт завершён |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> - Engine prelubrication will **not** disengage.
>
> ### How To Use This Tree
>
> This symptom tree can be used to troubleshoot a malfunction. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.
>
> ### Shoptalk
>
> NOTE: A jumper wire **must** be removed at the prelubrication connector, if prelubrication is to be used.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the customer interface box. |  |
> |  | **STEP 1A.** Check the customer interface box logic unit LED illumination. |  |
> |  | **STEP 1B.** Check the DCU410 power supply wire for voltage +24-VDC. |  |
> |  | **STEP 1C.** Check the prelubrication activation supply wire for an open. |  |
> |  | **STEP 1D.** Check the prelubrication complete signal wire for an open. |  |
> |  | **STEP 1E.** Check the prelubrication activation and complete signal wires for an open. |  |
> |  | **STEP 1F.** Check the prelubrication activation and complete signal wires for a short to ground. |  |
> | STEP 2. | Check the OEM wiring harness. |  |
> |  | **STEP 2A.** Check the prelubrication supply and return wires for an open. |  |
> |  | **STEP 2B.** Check the prelubrication supply and return wires for a wire-to-wire short. |  |
> |  | **STEP 2C.** Check the prelubrication supply wire for a short to ground. |  |
>
> ### STEP 1. Check the customer interface box.
>
> #### STEP 1A. Check the customer interface box logic unit LED illumination.
>
> | **Conditions:** Open the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the crank lamp LED on the DCU 410 unit or remote panel for illumination. | Crank lamp illuminated? **YES** | 1B |
> | Crank lamp illuminated? **NO** | Contact a Cummins® Authorized Repair Location |  |
>
> #### STEP 1B. Check the DCU410 power supply wire for voltage +24-VDC.
>
> | **Conditions:** Open the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the voltage at the battery 1 voltage (switched power) at the DCU410 unit. Place one test lead on the battery 1 voltage (switched power) supply wire at the DCU410 unit. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than +24-VDC? **YESRepair:** Check the batteries. Refer to the OEM service manual. | Repair complete |
> | Less than +24-VDC? **NO** | 1C |  |
>
> #### STEP 1C. Check the prelubrication activation signal wire for an open.
>
> | **Conditions:** Open the customer interface box. Disconnect the prelubrication activation signal wire from the DCU410 unit. Disconnect the C1 connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the prelubrication activation signal wire at the DCU410 unit and C1 connector for an open. Place one test lead on the prelubrication activation signal wire at the DCU410 unit. Place the other test lead prelubrication activation signal wire at the C1 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1D |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |
>
> #### STEP 1D. Check the prelubrication complete signal wire for an open.
>
> | **Conditions:** Open the customer interface box. Disconnect the prelubrication complete signal wire at the DCU410 unit, CLU unit, and C1 connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the prelubrication complete signal wire at the DCU410 unit, CLU unit, and C1 connector for an open. Place one test lead on the prelubrication complete signal wire at the DCU410 unit. Place the other test lead on the prelubrication complete signal wire at the CLU unit. Place one test lead on the prelubrication complete signal wire at the DCU410 unit. Place the other test lead on the prelubrication complete signal wire at the C1 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1E |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |
>
> #### STEP 1E. Check the prelubrication activation and complete signal wires for a wire-to-wire short.
>
> | **Conditions:** Open the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the prelubrication activation and complete signal wire at the DCU410 unit for a wire-to-wire short. Place one test lead on the prelubrication activation signal wire at the DCU410 unit. Place the other test lead on all other wires at the DCU410 unit. Place one test lead on the prelubrication complete signal wire at the DCU410 unit. Place the other test lead on all other wires at the DCU410 unit. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the DCU410 unit. Contact a Cummins® Authorized Repair Location. | Repair complete |
> | Less than 10 ohms? **NO** | 1F |  |
>
> #### STEP 1F. Check the prelubrication activation and complete signal wires for a short to ground.
>
> | **Conditions:** Open the customer interface box. Disconnect the prelubrication activation and complete signal wires at the DCU410 unit. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the prelubrication activation and complete signal wires at the DCU410 unit for a short to ground. Place one test lead on the prelubrication activation signal wire at the DCU410 unit. Place the other test lead on panel ground. Place one test lead on the prelubrication complete signal wire at the DCU410 unit. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the DCU410 unit. Contact a Cummins® Authorized Repair Location. | Repair complete |
> | Less than 10 ohms? **NO** | 2A |  |
>
> ### STEP 2. Check the OEM wiring harness.
>
> #### STEP 2A. Check the prelubrication supply and return wires for an open.
>
> | **Conditions:** Open the customer interface box. Disconnect the prelubrication supply and return wires at the C1 connector and prelubrication sensor. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the prelubrication supply and return wires at the C1 connector and prelubrication sensor for an open. Place one test lead on the prelubrication supply wire at the C1 connector. Place the other test lead on the prelubrication supply wire at the prelubrication sensor. Place one test lead on the prelubrication return wire at the C1 connector. Place the other test lead on the prelubrication return wire at the prelubrication return wire at prelubrication sensor. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 2B |
> | Less than 10 ohms? **NORepair:** Replace the wire. Refer to the OEM service manual. | Repair complete |  |
>
> #### STEP 2B. Check the prelubrication supply and return wires for a wire-to-wire short.
>
> | **Conditions:** Open the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the prelubrication supply and return wires at the C1 connector for a wire-to-wire short. Place one test lead on the prelubrication supply wire at the C1 connector. Place the other test lead on all other wires at the C1 connector. Place one test lead on the prelubrication return wire at the C1 connector. Place the other test lead on all other wires at the C1 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. Refer to the OEM service manual. | Repair complete |
> | Less than 10 ohms? **NO** | 2C |  |
>
> #### STEP 2C. Check the prelubrication supply wire for a short to ground.
>
> | **Conditions:** Open the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the prelubrication supply wire at the C1 connector for a short to ground. Place one test lead on the prelubrication supply wire at the C1 connector. Place the other test lead on engine ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. Refer to the OEM service manual. | Repair complete |
> | Less than 10 ohms? **NORepair:** Replace the prelubrication sensor. Refer to the OEM service manual or contact a Cummins® Authorized Repair Location. | Repair complete |  |
