---
aliases:
  - "Подтверждение неисправностей ЭБУ не работает"
type: "Процедура"
doc: "115-t02-1013"
title_en: "ECM Fault Acknowledge Not Operational"
title_ru: "Подтверждение неисправностей ЭБУ не работает"
modified: "2006-06-12"
engines:
  - "41349633"
families:
  - "QSK19"
manuals:
  - "4021587"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/115/115-t02-1013.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/115-t02-1013.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/115"
  - "перевод/машинный"
---

# ECM Fault Acknowledge Not Operational
**Подтверждение неисправностей ЭБУ не работает**

> [!abstract] Процедура · `115-t02-1013`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021587 — C Command Panel System Marine Master Repair Manual|4021587]]
> **Секции:** Section TT — Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2006-06-12
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/115/115-t02-1013.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/115-t02-1013.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

- Функция будильника тишины работает, но ECM не получает сигнал распознавания неисправностей.

- ECM имеет активные сбои даже после исправления состояния сбоя и нажатия кнопки тишины тревоги.

### Как пользоваться этим деревом

Это дерево симптомов может быть использовано для устранения неполадок при признании симптомов ECM. Начните с шага 1 поиска неисправностей. На шаге 2 система задаст ряд вопросов и по симптому выдаст перечень действий по поиску неисправности.

### Практические замечания

После того, как сигнал тревоги получен и нажата кнопка тишины, зуммеры на панели машинного отделения и пульт дистанционного управления тишины. Логический блок клиентского интерфейса также посылает сигнал распознавания неисправностей в ECM.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверка проводки интерфейсной коробки заказчика |  |
|  | **ШАГ 1А.** Проверьте наличие сигнала с ошибкой | Сопротивление менее 10 Ом? |
| ШАГ 2. | Проверьте клиентский интерфейс Box на проводку двигателя с помощью кабеля |  |
|  | **ШАГ 2А.** Проверить наличие вины в сигнальной проволоке | Сопротивление менее 10 Ом? |

### ШАГ 1. Проверка проводки интерфейсной коробки заказчика

#### ШАГ 1A. Проверьте наличие сигнала Fault Acknowledge

| **Условия: ** Откройте окно интерфейса клиента Отключите окно интерфейса клиента к разъему кабеля C3. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте сигнальный провод, распознающий неисправность. Поместите один испытательный щуп на сигнальный провод с распознаванием неисправностей в разъём C3. Поместите другой измерительный щуп на терминал сигнала распознавания неисправностей на логический блок окна интерфейса клиента. | Сопротивление менее 10 Ом? *Да** | 2А |
| Сопротивление менее 10 Ом? **NORepair:** Заменить неисправный провод. См. процедуру[[115-015-023 — Customer Interface Box\|015-023]]. | Ремонт завершён. |  |

### ШАГ 2. Проверьте клиентский интерфейс Box на проводку двигателя с помощью кабеля

#### ШАГ 2A. Проверить неисправность Signal Wire

| **Условия:** Отсоединить кабельный разъем С3 от окна интерфейса клиента Отключить кабельный разъем С10 от электропроводки двигателя. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте сигнальный провод на неисправность. Поместите один испытательный щуп в неисправность, распознайте сигнал контакта разъема C3. Поместите другой испытательный щуп в сигнальное соединение разъема C10. | Сопротивление менее 10 Ом? **YESRepair:** Заменить логический блок клиентского интерфейса после проверки правильности работы электропроводки и модуля управления двигателем. См. процедуру[[115-015-023 — Customer Interface Box\|015-023]]. | Ремонт завершён. |
| Сопротивление менее 10 Ом? **Заменить кабель.** | Ремонт завершён. |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> - The alarm silence function works but the ECM does **not** receive a fault acknowledge signal.
>
> - The ECM has active faults even after fault condition has been corrected and alarm silence button has been pressed.
>
> ### How To Use This Tree
>
> This symptom tree can be used to troubleshoot ECM fault acknowledge symptoms. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.
>
> ### Shoptalk
>
> After an alarm is received and the silence button is pushed, the buzzers on the engine room panel and remote panel silence. The customer interface box logic unit also sends a fault acknowledge signal to the ECM.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check Customer Interface Box Wiring |  |
> |  | **STEP 1A.** Check the Fault Acknowledge Signal Wire | Less than 10 ohms resistance? |
> | STEP 2. | Check Customer Interface Box to Engine Harness Cable |  |
> |  | **STEP 2A.** Check Fault Acknowledge Signal Wire | Less than 10 ohms resistance? |
>
> ### STEP 1. Check Customer Interface Box Wiring
>
> #### STEP 1A. Check the Fault Acknowledge Signal Wire
>
> | **Conditions:** Open the customer interface box Disconnect the customer interface box to engine harness cable C3 connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the fault acknowledge signal wire. Place one test lead on the fault acknowledge signal wire in connector C3. Place the other test lead on the fault acknowledge signal terminal on the customer interface box logic unit. | Less than 10 ohms resistance? **YES** | 2A |
> | Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |  |
>
> ### STEP 2. Check Customer Interface Box to Engine Harness Cable
>
> #### STEP 2A. Check Fault Acknowledge Signal Wire
>
> | **Conditions:** Disconnect cable connector C3 from the customer interface box Disconnect cable connector C10 from the engine harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check fault acknowledge signal wire. Place one test lead in the fault acknowledge signal pin of the C3 connector. Place the other test lead in the fault acknowledge signal pin of the C10 connector. | Less than 10 ohms resistance? **YESRepair:** Replace the customer interface box logic unit after verifying on-engine harness and engine control module are operating properly. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |
> | Less than 10 ohms resistance? **NORepair:** Replace the cable. | Repair complete. |  |
