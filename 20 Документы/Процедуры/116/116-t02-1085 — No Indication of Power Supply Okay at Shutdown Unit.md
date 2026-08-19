---
aliases:
  - "Нет индикации исправного питания на блоке останова"
type: "Процедура"
doc: "116-t02-1085"
title_en: "No Indication of Power Supply Okay at Shutdown Unit"
title_ru: "Нет индикации исправного питания на блоке останова"
modified: "2008-04-04"
engines:
  - "41349633"
families:
  - "QSK19"
manuals:
  - "4021617"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1085.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/116-t02-1085.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/116"
  - "перевод/машинный"
---

# No Indication of Power Supply Okay at Shutdown Unit
**Нет индикации исправного питания на блоке останова**

> [!abstract] Процедура · `116-t02-1085`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2008-04-04
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1085.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/116-t02-1085.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

- Блок SDU410 не освещает светодиод даже с подключенным источником питания.

### Как пользоваться этим деревом

По этому дереву симптомов можно вести поиск неисправности. Начните с шага 1 поиска неисправностей. На шаге 2 система задаст ряд вопросов и по симптому выдаст перечень действий по поиску неисправности.

### Практические замечания

Светодиод питания на блоке SDU410 должен быть освещен, если блок SDU410 принимает +24-VDC.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте SDU410. |  |
|  | **STEP 1A.** Проверьте SDU410 для подсвечиваемых светодиодов. | Светодиодная подсветка? |
| ШАГ 2. | Проверьте блок питания SDU410. |  |
|  | **STEP 2A.** Проверить блок питания SDU410 на +24-VDC. | Электроснабжение +24-VDC? |
| ШАГ 3. | Проверка проводки интерфейсной коробки заказчика. |  |
|  | **STEP 3A.** Проверить отключение блока питания и возврат проводов на наличие открытого. | Менее 10 Ом? |
|  | **STEP 3A-1.** Проверить блок отключения питания коммуникационной шины ModiconTM и обратные провода на наличие открытого. | Менее 10 Ом? |
|  | **STEP 3A-2.** Проверьте напряжение 1 питания батареи и провода возврата для открытого. | Менее 10 Ом? |
|  | **STEP 3B.** Проверьте цепи питания и возврата напряжения батареи 1 для напряжения питания +24-VDC. | Меньше +24-VDC? |
|  | **STEP 3C.** Проверьте блок отключения питания +24-VDC и возвратные провода для короткого провода к проводу. | Менее 10 Ом? |
|  | **STEP 3C-1.** Проверить блок отключения питания коммуникационной шины ModiconTM и возврат проводов на короткое время от провода к проводу. | Менее 10 Ом? |
|  | **STEP 3C-2.** Проверьте напряжение батареи 1 питания и возврата проводов для провода к проводу коротко. | Менее 10 Ом? |
|  | **STEP 3D.** Проверьте блок питания отключения +24-VDC провода на короткое время до земли. | Менее 10 Ом? |
|  | **STEP 3D-1.** Проверить блок отключения провода питания коммуникационной шины ModiconTM на короткое время до заземления. | Менее 10 Ом? |
|  | **STEP 3D-2.** Проверьте напряжение батареи 1 провода питания на короткое время до земли. | Менее 10 Ом? |

### ШАГ 1. Проверьте SDU410.

#### ШАГ 1A. Проверьте мощность светодиода для освещения.

| **Условия:** Проверьте дисплей SDU410. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте блок SDU410 для освещенных светодиодов. | Светодиодная подсветка? *** Ремонт:** Проверьте цепи подачи и возврата блока SDU410 на наличие прерывистой неисправности. Ссылка на соответствующее дерево устранения неполадок. | Ремонт завершён |
| Светодиодная подсветка? **NORepair:** Заменить модуль SDU410. Свяжитесь с авторизованным ремонтным центром Cummins® для замены блока SDU410. | 2А |  |

### ШАГ 2. Проверьте блок питания SDU410.

#### ШАГ 2A. Проверьте блок питания SDU410 на +24-VDC.

| **Условия: ** Откройте окно интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте блок питания SDU410 на +24-VDC. | Является ли электропитание +24-VDC? *** Ремонт:** Проверить аккумуляторы. См. сервисное руководство изготовителя машины. | Ремонт завершён |
| Является ли электропитание +24-VDC? **NORepair:** Заменить модуль SDU410. Свяжитесь с авторизованным ремонтным центром Cummins® для замены блока SDU410. | 3А |  |

### ШАГ 3. Проверьте клиентский интерфейс коробки проводов.

#### ШАГ 3A. Проверьте блок отключения питания и возврат проводов для открытого.

| **Условия: ** Откройте окно интерфейса клиента. Отключите провода подачи и возврата на блоке SDU410. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте провода подачи и возврата для открытого. Поместите один испытательный щуп на блок питания отключения +24-VDC провода на блоке SDU410. Поместите другой измерительный щуп на блок отключения питания +24-VDC провода в блок логики интерфейса клиента. Поместите один испытательный щуп на блок питания отключения +24-VDC провода на блоке SDU410. Поместите другой испытательный щуп на блок питания отключения +24-VDC на разъем X4. Поместите один испытательный щуп на провод возврата блока отключения в блок SDU410. Поместите другой измерительный щуп на провод возврата блока отключения в логический блок окна интерфейса клиента. Поместите один испытательный щуп на провод возврата блока отключения в блок SDU410. Поместите другой испытательный щуп на обратный контакт блока отключения на разъем X4. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да** | Ремонт завершён |
| Менее 10 Ом? **NORepair:** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | 3А-1-1 |  |

#### ШАГ 3A-1. Проверьте блок отключения питания коммуникационной шины ModiconTM и возвратные провода для открытого доступа.

| **Условия: ** Откройте окно интерфейса клиента. Отключите блок отключения питания и возврата шины связи ModiconTM от блока SDU410 и блока DCU410. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте блок отключения питания коммуникационной шины ModiconTM и возвратные провода для открытого доступа. Поместите один испытательный щуп на блок отключения провода питания шины связи ModiconTM на блок SDU410. Поместите другой испытательный щуп на блок отключения провода питания шины связи ModiconTM в блок DCU410. Поместите один испытательный щуп на блок отключения провода обратной шины связи ModiconTM на блок SDU410. Поместите другой испытательный щуп на отключаемый модуль обратного провода шины связи ModiconTM в блок DCU410. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да** | Ремонт завершён |
| Менее 10 Ом? **NORepair:** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | 3А-2 |  |

#### ШАГ 3A-2. Проверьте напряжение батареи 1 питания и возврат проводов для открытого.

| **Условия: ** Откройте окно интерфейса клиента. Отключите напряжение батареи 1 податочных и возвратных проводов на логическом блоке окна интерфейса клиента и разъеме X4. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте напряжение батареи 1 питания и возврат проводов для открытого. Поместите один испытательный щуп на провод питания напряжения батареи 1 в логический блок окна интерфейса клиента. Поместите другой испытательный щуп на контакт питания 1 напряжения батареи на разъеме X4. Поместите один испытательный щуп на провод возврата напряжения батареи в логический блок окна интерфейса клиента. Поместите другой испытательный щуп на обратный контакт напряжения батареи на разъеме X4. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да** | Ремонт завершён |
| Менее 10 Ом? **NORepair:** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | 3B |  |

#### ШАГ 3B. Проверьте напряжение батареи 1 цепи питания и возврата для напряжения питания +24-VDC.

| **Условия: ** Откройте окно интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте напряжение батареи 1 цепи питания и возврата для напряжения питания +24-VDC. Поместите один испытательный щуп на контакт питания 1 напряжения батареи на разъеме X4. Поместите другой испытательный щуп на обратный контакт напряжения батареи на разъеме X4. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Меньше +24-VDC? *** Заменить батареи. См. сервисное руководство изготовителя машины. | 3C |
| Меньше +24-VDC? ** НЕТ** | Ремонт завершён |  |

#### ШАГ 3C. Проверьте блок отключения питания +24-VDC и возвратные провода для короткого провода к проводу.

| **Условия: ** Откройте окно интерфейса клиента. Отключите блок отключения питания +24-VDC и возвратные провода от блока SDU410. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте блок отключения питания +24-VDC и возвратные провода для короткого провода к проводу. Поместите один испытательный щуп на блок питания отключения +24-VDC провода на блоке SDU410. Поместите другой испытательный щуп на все другие провода в блок SDU410. Поместите один испытательный щуп на провод возврата блока отключения в блок SDU410. Поместите другой испытательный щуп на все другие провода в блок SDU410. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |
| Менее 10 Ом? ** НЕТ** | 3С-1-1 |  |

#### ШАГ 3C-1. Проверьте блок отключения питания коммуникационной шины ModiconTM и возвратные провода для короткого провода к проводу.

| **Условия: ** Откройте окно интерфейса клиента. Отключите блок отключения питания и возврата шины связи ModiconTM от блока SDU410 и блока DCU410. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте блок отключения питания коммуникационной шины ModiconTM и возвратные провода для короткого провода к проводу. Поместите один испытательный щуп на блок отключения провода питания шины связи ModiconTM на блок SDU410. Поместите другой испытательный щуп на все другие провода в блок SDU410. Поместите один испытательный щуп на блок отключения провода обратной шины связи ModiconTM на блок SDU410. Проведите другой тест на всех других проводах в блоке SDU410. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |
| Менее 10 Ом? ** НЕТ** | 3С-2 |  |

#### ШАГ 3C-2. Проверьте блок отключения питания коммуникационной шины ModiconTM и возвратные провода для короткого провода к проводу.

| **Условия: ** Откройте окно интерфейса клиента. Отключите напряжение 1 питания и возврата от блока SDU410 и блока DCU410. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте блок отключения питания коммуникационной шины ModiconTM и возвратные провода для короткого провода к проводу. Поместите один испытательный щуп на провод питания напряжения батареи 1 в блоке SDU410. Поместите другой испытательный щуп на все другие провода в блок SDU410. Поместите один испытательный щуп на провод возврата напряжения батареи в блок SDU410. Поместите другой испытательный щуп на все другие провода в блок SDU410. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |
| Менее 10 Ом? ** НЕТ** | 3D |  |

#### ШАГ 3D. Проверьте блок отключения питания +24-VDC провода для короткого наземного.

| **Условия: ** Откройте окно интерфейса клиента. Отключите блок питания отключения +24-VDC от блока SDU410. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте блок отключения питания +24-VDC провода для короткого наземного. Поместите один испытательный щуп на блок питания отключения +24-VDC на блок SDU410. Поместите другой испытательный щуп на панельную площадку. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |
| Менее 10 Ом? ** НЕТ** | 3D-1 |  |

#### ШАГ 3D-1. Проверьте блок отключения провода питания коммуникационной шины ModiconTM для короткого заземления.

| **Условия: ** Откройте окно интерфейса клиента. Отключите отключающий блок провода питания шины связи ModiconTM от блока SDU410 и блока DCU410. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте блок отключения провода питания коммуникационной шины ModiconTM для короткого заземления. Поместите один испытательный щуп на блок отключения провода питания шины связи ModiconTM на блок SDU410. Поместите другой испытательный щуп на панельную площадку. Поместите один испытательный щуп на блок отключения провода питания шины связи ModiconTM в блок DCU410. Поместите другой испытательный щуп на панельную площадку. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |
| Менее 10 Ом? ** НЕТ** | 3D-2 |  |

#### ШАГ 3D-2. Проверьте напряжение батареи 1 провода питания для короткого наземного.

| **Условия: ** Откройте окно интерфейса клиента. Отсоедините провод питания напряжения батареи 1 от блока логики окна клиентского интерфейса и разъема X4. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте напряжение батареи 1 провода питания для короткого наземного. Поместите один испытательный щуп на провод питания напряжения батареи 1 в логический блок окна интерфейса клиента. Поместите другой испытательный щуп на панельную площадку. Поместите один испытательный щуп на контакт питания 1 напряжения батареи на разъеме X4. Поместите другой испытательный щуп на панельную площадку. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |
| Менее 10 Ом? ** НЕТ** | Свяжитесь с авторизованным местом ремонта Cummins® |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> - The SDU410 unit does **not** illuminate the power LED even with power supply connected.
>
> ### How To Use This Tree
>
> This symptom tree can be used to troubleshoot a malfunction. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.
>
> ### Shoptalk
>
> A power LED on the SDU410 unit should be illuminated if the SDU410 unit is receiving +24-VDC.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check SDU410 unit. |  |
> |  | **STEP 1A.** Check SDU410 unit for illuminated LEDs. | Is power LED illuminated? |
> | STEP 2. | Check SDU410 unit power supply. |  |
> |  | **STEP 2A.** Check SDU410 unit power supply for +24-VDC. | Is power supply +24-VDC? |
> | STEP 3. | Check customer interface box wiring. |  |
> |  | **STEP 3A.** Check shutdown unit supply and return wires for an open. | Less than 10 ohms? |
> |  | **STEP 3A-1.** Check shutdown unit Modicon™ communication bus supply and return wires for an open. | Less than 10 ohms? |
> |  | **STEP 3A-2.** Check the battery voltage 1 supply and return wires for an open. | Less than 10 ohms? |
> |  | **STEP 3B.** Check the battery voltage 1 supply and return circuits for supply voltage +24-VDC. | Less than +24-VDC? |
> |  | **STEP 3C.** Check the shutdown unit supply +24-VDC and return wires for a wire-to-wire short. | Less than 10 ohms? |
> |  | **STEP 3C-1.** Check shutdown unit Modicon™ communication bus supply and return wires for a wire-to-wire short. | Less than 10 ohms? |
> |  | **STEP 3C-2.** Check the battery voltage 1 supply and return wires for a wire-to-wire short. | Less than 10 ohms? |
> |  | **STEP 3D.** Check the shutdown unit supply +24-VDC wire for a short to ground. | Less than 10 ohms? |
> |  | **STEP 3D-1.** Check shutdown unit Modicon™ communication bus supply wire for a short to ground. | Less than 10 ohms? |
> |  | **STEP 3D-2.** Check the battery voltage 1 supply wire for a short to ground. | Less than 10 ohms? |
>
> ### STEP 1. Check the SDU410 unit.
>
> #### STEP 1A. Check the power LED for illumination.
>
> | **Conditions:** Check the SDU410 unit display. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the SDU410 unit for illuminated LEDs. | Is the power LED illuminated? **YESRepair:** Check the SDU410 unit supply and return circuits for intermittent fault. Reference the appropriate troubleshooting tree. | Repair complete |
> | Is the power LED illuminated? **NORepair:** Replace the SDU410 unit. Contact a Cummins® Authorized Repair Location for replacement of the SDU410 unit. | 2A |  |
>
> ### STEP 2. Check the SDU410 unit power supply.
>
> #### STEP 2A. Check the SDU410 unit power supply for +24-VDC.
>
> | **Conditions:** Open the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the SDU410 unit power supply for +24-VDC. | Is the power supply +24-VDC? **YESRepair:** Check the batteries. Refer to the OEM service manual. | Repair complete |
> | Is the power supply +24-VDC? **NORepair:** Replace the SDU410 unit. Contact a Cummins® Authorized Repair Location for replacement of the SDU410 unit. | 3A |  |
>
> ### STEP 3. Check the customer interface box wiring.
>
> #### STEP 3A. Check the shutdown unit supply and return wires for an open.
>
> | **Conditions:** Open the customer interface box. Disconnect the supply and return wires at the SDU410 unit. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the supply and return wires for an open. Place one test lead on the shutdown unit supply +24-VDC wire at the SDU410 unit. Place the other test lead on the shutdown unit supply +24-VDC wire at the customer interface box logic unit. Place one test lead on the shutdown unit supply +24-VDC wire at the SDU410 unit. Place the other test lead on the shutdown unit supply +24-VDC pin at the X4 connector. Place one test lead on the shutdown unit return wire at the SDU410 unit. Place the other test lead on the shutdown unit return wire at the customer interface box logic unit. Place one test lead on the shutdown unit return wire at the SDU410 unit. Place the other test lead on the shutdown unit return pin at the X4 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | Repair complete |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | 3A-1 |  |
>
> #### STEP 3A-1. Check the shutdown unit Modicon™ communication bus supply and return wires for an open.
>
> | **Conditions:** Open the customer interface box. Disconnect the shutdown unit Modicon™ communication bus supply and return wires from the SDU410 unit and DCU410 unit. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the shutdown unit Modicon™ communication bus supply and return wires for an open. Place one test lead on the shutdown unit Modicon™ communication bus supply wire at the SDU410 unit. Place the other test lead on the shutdown unit Modicon™ communication bus supply wire at the DCU410 unit. Place one test lead on the shutdown unit Modicon™ communication bus return wire at the SDU410 unit. Place the other test lead on the shutdown unit Modicon™ communication bus return wire at the DCU410 unit. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | Repair complete |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | 3A-2 |  |
>
> #### STEP 3A-2. Check the battery voltage 1 supply and return wires for an open.
>
> | **Conditions:** Open the customer interface box. Disconnect the battery voltage 1 supply and return wires at the customer interface box logic unit and the X4 connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the battery voltage 1 supply and return wires for an open. Place one test lead at the battery voltage 1 supply wire at the customer interface box logic unit. Place the other test lead on the battery voltage 1 supply pin at the X4 connector. Place one test lead at the battery voltage return wire at the customer interface box logic unit. Place the other test lead on the battery voltage return pin at the X4 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | Repair complete |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | 3B |  |
>
> #### STEP 3B. Check the battery voltage 1 supply and return circuits for supply voltage +24-VDC.
>
> | **Conditions:** Open the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the battery voltage 1 supply and return circuits for supply voltage +24-VDC. Place one test lead on the battery voltage 1 supply pin at the X4 connector. Place the other test lead on the battery voltage return pin at the X4 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than +24-VDC? **YESRepair:** Replace the batteries. Refer to the OEM service manual. | 3C |
> | Less than +24-VDC? **NO** | Repair complete |  |
>
> #### STEP 3C. Check the shutdown unit supply +24-VDC and return wires for a wire-to-wire short.
>
> | **Conditions:** Open the customer interface box. Disconnect the shutdown unit supply +24-VDC and return wires from the SDU410 unit. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the shutdown unit supply +24-VDC and return wires for a wire-to-wire short. Place one test lead on the shutdown unit supply +24-VDC wire at the SDU410 unit. Place the other test lead on all other wires at the SDU410 unit. Place one test lead on the shutdown unit return wire at the SDU410 unit. Place the other test lead on all other wires at the SDU410 unit. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
> | Less than 10 ohms? **NO** | 3C-1 |  |
>
> #### STEP 3C-1. Check the shutdown unit Modicon™ communication bus supply and return wires for a wire-to-wire short.
>
> | **Conditions:** Open the customer interface box. Disconnect the shutdown unit Modicon™ communication bus supply and return wires from the SDU410 unit and DCU410 unit. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the shutdown unit Modicon™ communication bus supply and return wires for a wire-to-wire short. Place one test lead on the shutdown unit Modicon™ communication bus supply wire at the SDU410 unit. Place the other test lead on all other wires at the SDU410 unit. Place one test lead on the shutdown unit Modicon™ communication bus return wire at the SDU410 unit. Place the other test on all other wires at the SDU410 unit. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
> | Less than 10 ohms? **NO** | 3C-2 |  |
>
> #### STEP 3C-2. Check the shutdown unit Modicon™ communication bus supply and return wires for a wire-to-wire short.
>
> | **Conditions:** Open the customer interface box. Disconnect the battery voltage 1 supply and return wires from the SDU410 unit and DCU410 unit. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the shutdown unit Modicon™ communication bus supply and return wires for a wire-to-wire short. Place one test lead on the battery voltage 1 supply wire at the SDU410 unit. Place the other test lead on all other wires at the SDU410 unit. Place one test lead on the battery voltage return wire at the SDU410 unit. Place the other test lead on all other wires at the SDU410 unit. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
> | Less than 10 ohms? **NO** | 3D |  |
>
> #### STEP 3D. Check the shutdown unit supply +24-VDC wire for a short to ground.
>
> | **Conditions:** Open the customer interface box. Disconnect the shutdown unit supply +24-VDC wire from the SDU410 unit. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the shutdown unit supply +24-VDC wire for a short to ground. Place one test lead on the shutdown unit supply +24-VDC at the SDU410 unit. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
> | Less than 10 ohms? **NO** | 3D-1 |  |
>
> #### STEP 3D-1. Check the shutdown unit Modicon™ communication bus supply wire for a short to ground.
>
> | **Conditions:** Open the customer interface box. Disconnect the shutdown unit Modicon™ communication bus supply wire from the SDU410 unit and DCU410 unit. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the shutdown unit Modicon™ communication bus supply wire for a short to ground. Place one test lead on the shutdown unit Modicon™ communication bus supply wire at the SDU410 unit. Place the other test lead on panel ground. Place one test lead on the shutdown unit Modicon™ communication bus supply wire at the DCU410 unit. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
> | Less than 10 ohms? **NO** | 3D-2 |  |
>
> #### STEP 3D-2. Check the battery voltage 1 supply wire for a short to ground.
>
> | **Conditions:** Open the customer interface box. Disconnect the battery voltage 1 supply wire from the customer interface box logic unit and X4 connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the battery voltage 1 supply wire for a short to ground. Place one test lead on the battery voltage 1 supply wire at the customer interface box logic unit. Place the other test lead on panel ground. Place one test lead on the battery voltage 1 supply pin at the X4 connector. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
> | Less than 10 ohms? **NO** | Contact a Cummins® Authorized Repair Location |  |
