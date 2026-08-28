---
aliases:
  - "Блок останова не индицирует останов двигателя"
type: "Процедура"
doc: "116-t02-1082"
title_en: "Engine Shutdown Unit Does Not Indicate Engine Shut Down"
title_ru: "Блок останова не индицирует останов двигателя"
modified: "2008-04-04"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4021617"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1082.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1082.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/116"
  - "перевод/машинный"
---

# Engine Shutdown Unit Does Not Indicate Engine Shut Down
**Блок останова не индицирует останов двигателя**

> [!abstract] Процедура · `116-t02-1082`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2008-04-04
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1082.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1082.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

- Двигатель отключается без связи между цепью шин связи DCU410 и SDU410 ModiconTM.

### Как пользоваться этим деревом

По этому дереву симптомов можно вести поиск неисправности. Начните с шага 1 поиска неисправностей. На шаге 2 система задаст ряд вопросов и по симптому выдаст перечень действий по поиску неисправности.

### Практические замечания

Примечание: Проверьте руководство по устранению неполадок DCU410 перед выполнением любого из следующих шагов. Если связь есть, то отключение двигателя было вызвано SDU410. Если светодиод подсвечивается на блоке SDU410, то проблема заключается в блоке DCU410 или SDU410. Если светодиод не освещается, то SDU410 не является корнем причины.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверка проводки интерфейсной коробки заказчика |  |
|  | **ШАГ 1А.** Проверьте подачу и возврат проводов в коммуникационном автобусе ModiconTM на наличие открытого доступа. | Менее 10 Ом? |
|  | **STEP 1B.** Проверьте подачу и возврат проводов в коммуникационную шину ModiconTM для короткого провода к проводу. | Менее 10 Ом? |
|  | **STEP 1C** Проверить провода питания коммуникационной шины ModiconTM на короткое время до заземления. | Менее 10 Ом? |

### ШАГ 1. Проверка проводки интерфейсной коробки заказчика

#### ШАГ 1A. Проверьте подачу коммуникационного автобуса ModiconTM и обратные провода для открытого доступа.

| **Условия:** Откройте окно интерфейса клиента. Отключите подачу и возвратную проволоку коммуникационной шины ModiconTM на терминальных полосах SDU410 и DCU410. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте сигнал и верните провода для открытого. Поместите один испытательный щуп на блок отключения провода питания шины связи ModiconTM на блок SDU410. Поместите другой испытательный щуп на блок отключения провода питания шины связи ModiconTM в блок DCU410. Поместите один испытательный щуп на блок отключения провода обратной шины связи ModiconTM на блок SDU410. Поместите другой испытательный щуп на отключаемый модуль обратного провода шины связи ModiconTM в блок DCU410. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да | 1В |
| Менее 10 Ом? **NORepair:** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |  |

#### ШАГ 1B. Проверьте подачу и возврат проводов в коммуникационную шину ModiconTM для короткого провода к проводу.

| **Условия:** Откройте окно интерфейса клиента. Отключите провода питания и возврата коммуникационной шины ModiconTM на терминальных полосах SDU410 и DCU410. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте провода подачи и возврата для короткого провода к проводу. Поместите один испытательный щуп на блок отключения провода питания шины связи ModiconTM на блок SDU410. Поместите другой испытательный щуп на каждый из других проводов в блок SDU410. Поместите один испытательный щуп на блок отключения провода питания шины связи ModiconTM в блок DCU410. Поместите другой испытательный щуп на каждый из других проводов в блок DCU410. Поместите один испытательный щуп на блок отключения провода обратной шины связи ModiconTM на блок SDU410. Поместите другой испытательный щуп на каждый из других проводов в блок SDU410. Поместите один испытательный щуп на блок отключения провода обратной шины связи ModiconTM в блок DCU410. Поместите другой испытательный щуп на каждый из других проводов в блок DCU410. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? * Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |
| Менее 10 Ом? **НЕТ** | 1С |  |

#### ШАГ 1C. Проверьте провод связи ModiconTM для короткого приземления.

| **Условия:** Откройте окно интерфейса клиента. Отключите провод питания коммуникационной шины ModiconTM на блоках SDU410 и DCU410. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте проволоку для короткого приземления. Поместите один испытательный щуп на блок отключения провода питания шины связи ModiconTM на блок SDU410. Поместите другой испытательный щуп на панельную площадку. Поместите один испытательный щуп на блок отключения провода питания шины связи ModiconTM в блок DCU410. Поместите другой испытательный щуп на панельную площадку. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? * Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |
| Менее 10 Ом? **НЕТ** | Свяжитесь с авторизованной реакцией на ремонт Cummins® |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> - The engine shuts down with no communication between the DCU410 and SDU410 Modicon™ communication bus circuit.
>
> ### How To Use This Tree
>
> This symptom tree can be used to troubleshoot a malfunction. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.
>
> ### Shoptalk
>
> NOTE: Check the DCU410 troubleshooting manual before performing any of the following steps. If there is communication, then the engine shutdown was **not** caused by the SDU410. If the LED is illuminated on the SDU410 unit, then the problem is in the DCU410 or the SDU410 unit. If no LED is illuminated then the SDU410 is **not** the root of the cause.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check customer interface box wiring |  |
> |  | **STEP 1A.** Check the Modicon™ communication bus supply and return wires for an open. | Less than 10 ohms? |
> |  | **STEP 1B.** Check the Modicon™ communication bus supply and return wires for a wire-to-wire short. | Less than 10 ohms? |
> |  | **STEP 1C.** Check the Modicon™ communication bus supply wire for a short to ground. | Less than 10 ohms? |
>
> ### STEP 1. Check customer interface box wiring
>
> #### STEP 1A. Check the Modicon™ communication bus supply and return wires for an open.
>
> | **Conditions:** Open the customer interface box. Disconnect the Modicon™ communication bus supply and return wire at the SDU410 and DCU410 terminal strips. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the signal and return wires for an open. Place one test lead on the shutdown unit Modicon™ communication bus supply wire at the SDU410 unit. Place the other test lead on the shutdown unit Modicon™ communication bus supply wire at the DCU410 unit. Place one test lead on the shutdown unit Modicon™ communication bus return wire at the SDU410 unit. Place the other test lead on the shutdown unit Modicon™ communication bus return wire at the DCU410 unit. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1B |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |
>
> #### STEP 1B. Check the Modicon™ communication bus supply and return wires for a wire-to-wire short.
>
> | **Conditions:** Open the customer interface box. Disconnect the Modicon™ communication bus supply and return wires at the SDU410 and DCU410 terminal strips. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the supply and return wires for a wire-to-wire short. Place one test lead on the shutdown unit Modicon™ communication bus supply wire at the SDU410 unit. Place the other test lead on each of the other wires at the SDU410 unit. Place one test lead on the shutdown unit Modicon™ communication bus supply wire at the DCU410 unit. Place the other test lead on each of the other wires at the DCU410 unit. Place one test lead on the shutdown unit Modicon™ communication bus return wire at the SDU410 unit. Place the other test lead on each of the other wires at the SDU410 unit. Place one test lead on the shutdown unit Modicon™ communication bus return wire at the DCU410 unit. Place the other test lead on each of the other wires at the DCU410 unit. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
> | Less than 10 ohms? **NO** | 1C |  |
>
> #### STEP 1C. Check the Modicon™ communication bus supply wire for a short to ground.
>
> | **Conditions:** Open the customer interface box. Disconnect the Modicon™ communication bus supply wire at the SDU410 and DCU410 units. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the supply wire for short to ground. Place one test lead on the shutdown unit Modicon™ communication bus supply wire at the SDU410 unit. Place the other test lead on panel ground. Place one test lead on the shutdown unit Modicon™ communication bus supply wire at the DCU410 unit. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
> | Less than 10 ohms? **NO** | Contact a Cummins® Authorized Repair Loaction |  |
