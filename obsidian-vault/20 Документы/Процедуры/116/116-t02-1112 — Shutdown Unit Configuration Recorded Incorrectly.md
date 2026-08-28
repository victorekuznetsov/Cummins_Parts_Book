---
aliases:
  - "Конфигурация блока останова записана неверно"
type: "Процедура"
doc: "116-t02-1112"
title_en: "Shutdown Unit Configuration Recorded Incorrectly"
title_ru: "Конфигурация блока останова записана неверно"
modified: "2008-04-15"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4021617"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1112.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1112.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/116"
  - "перевод/машинный"
---

# Shutdown Unit Configuration Recorded Incorrectly
**Конфигурация блока останова записана неверно**

> [!abstract] Процедура · `116-t02-1112`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2008-04-15
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1112.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1112.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

- Выключение двигателя без указания схемы коммуникационной шины SDU410 ModiconTM.

### Как пользоваться этим деревом

По этому дереву симптомов можно вести поиск неисправности. Начните с шага 1 поиска неисправностей. На шаге 2 система задаст ряд вопросов и по симптому выдаст перечень действий по поиску неисправности.

### Практические замечания

Входные сигналы блока SDU410 являются переключателями. Эти переключатели обычно открыты и закрыты при активации.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверка проводки интерфейсной коробки заказчика. |  |
|  | **STEP 1A.** Проверить блок отключения питания коммуникационной шины ModiconTM и обратные провода на наличие открытого. | Менее 10 Ом? |
|  | **STEP 1B.** Проверить блок отключения питания коммуникационной шины ModiconTM и возврат проводов на короткое время от провода к проводу. | Менее 10 Ом? |
|  | **STEP 1C.** Проверить блок отключения провода питания коммуникационной шины ModiconTM на короткое время до заземления. | Менее 10 Ом? |

### ШАГ 1. Проверьте клиентский интерфейс коробки проводов.

#### ШАГ 1A. Проверьте блок отключения питания коммуникационной шины ModiconTM и возвратные провода для открытого доступа.

| **Условия:** Откройте окно интерфейса клиента. Отключите блок отключения питания и возврата шины связи ModiconTM от блока SDU410 и блока DCU410. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте блок отключения питания коммуникационной шины ModiconTM и возвратные провода для открытого доступа. Поместите один испытательный щуп на блок отключения провода питания шины связи ModiconTM на блок SDU410. Поместите другой испытательный щуп на блок отключения провода питания шины связи ModiconTM в блок DCU410. Поместите один испытательный щуп на блок отключения провода обратной шины связи ModiconTM на блок SDU410. Поместите другой испытательный щуп на отключаемый модуль обратного провода шины связи ModiconTM в блок DCU410. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да | 1В |
| Менее 10 Ом? **NORepair:** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |  |

#### ШАГ 1B. Проверьте блок отключения питания коммуникационной шины ModiconTM и возвратные провода для короткого провода к проводу.

| **Условия:** Откройте окно интерфейса клиента. Отключите блок отключения питания и возврата шины связи ModiconTM от блока SDU410 и блока DCU410. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте блок отключения питания коммуникационной шины ModiconTM и возвратные провода для короткого провода к проводу. Поместите один испытательный щуп на блок отключения провода питания шины связи ModiconTM на блок SDU410. Поместите другой испытательный щуп на все другие провода в блок SDU410. Поместите один испытательный щуп на блок отключения провода обратной шины связи ModiconTM на блок SDU410. Проведите другой тест на всех других проводах в блоке SDU410. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом?  Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |
| Менее 10 Ом? **НЕТ** | 1С |  |

#### ШАГ 1C. Проверьте блок отключения провода питания коммуникационной шины ModiconTM для короткого заземления.

| **Условия:** Откройте окно интерфейса клиента. Отключите отключающий блок провода питания шины связи ModiconTM от блока SDU410 и блока DCU410. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте блок отключения провода питания коммуникационной шины ModiconTM для короткого заземления. Поместите один испытательный щуп на блок отключения провода питания шины связи ModiconTM на блок SDU410. Поместите другой испытательный щуп на панельную площадку. Поместите один испытательный щуп на блок отключения провода питания шины связи ModiconTM в блок DCU410. Поместите другой испытательный щуп на панельную площадку. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом?  Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |
| Менее 10 Ом? **НЕТ** | Процедуры устранения неполадок должны быть проверены повторно. Режим неисправности должен был быть обнаружен. |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> - The engine shutdowns with no indication from the SDU410 Modicon™ communication bus circuit.
>
> ### How To Use This Tree
>
> This symptom tree can be used to troubleshoot a malfunction. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.
>
> ### Shoptalk
>
> The SDU410 unit input signals are switches. These switches are normally open and closed when activated.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check customer interface box wiring. |  |
> |  | **STEP 1A.** Check shutdown unit Modicon™ communication bus supply and return wires for an open. | Less than 10 ohms? |
> |  | **STEP 1B.** Check shutdown unit Modicon™ communication bus supply and return wires for a wire-to-wire short. | Less than 10 ohms? |
> |  | **STEP 1C.** Check shutdown unit Modicon™ communication bus supply wire for a short to ground. | Less than 10 ohms? |
>
> ### STEP 1. Check the customer interface box wiring.
>
> #### STEP 1A. Check the shutdown unit Modicon™ communication bus supply and return wires for an open.
>
> | **Conditions:** Open the customer interface box. Disconnect the shutdown unit Modicon™ communication bus supply and return wires from the SDU410 unit and DCU410 unit. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the shutdown unit Modicon™ communication bus supply and return wires for an open. Place one test lead on the shutdown unit Modicon™ communication bus supply wire at the SDU410 unit. Place the other test lead on the shutdown unit Modicon™ communication bus supply wire at the DCU410 unit. Place one test lead on the shutdown unit Modicon™ communication bus return wire at the SDU410 unit. Place the other test lead on the shutdown unit Modicon™ communication bus return wire at the DCU410 unit. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1B |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |
>
> #### STEP 1B. Check the shutdown unit Modicon™ communication bus supply and return wires for a wire-to-wire short.
>
> | **Conditions:** Open the customer interface box. Disconnect the shutdown unit Modicon™ communication bus supply and return wires from the SDU410 unit and DCU410 unit. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the shutdown unit Modicon™ communication bus supply and return wires for a wire-to-wire short. Place one test lead on the shutdown unit Modicon™ communication bus supply wire at the SDU410 unit. Place the other test lead on all other wires at the SDU410 unit. Place one test lead on the shutdown unit Modicon™ communication bus return wire at the SDU410 unit. Place the other test on all other wires at the SDU410 unit. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
> | Less than 10 ohms? **NO** | 1C |  |
>
> #### STEP 1C. Check the shutdown unit Modicon™ communication bus supply wire for a short to ground.
>
> | **Conditions:** Open the customer interface box. Disconnect the shutdown unit Modicon™ communication bus supply wire from the SDU410 unit and DCU410 unit. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the shutdown unit Modicon™ communication bus supply wire for a short to ground. Place one test lead on the shutdown unit Modicon™ communication bus supply wire at the SDU410 unit. Place the other test lead on panel ground. Place one test lead on the shutdown unit Modicon™ communication bus supply wire at the DCU410 unit. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
> | Less than 10 ohms? **NO** | Troubleshooting procedures **must** be checked again. A fault mode should have been detected. |  |
