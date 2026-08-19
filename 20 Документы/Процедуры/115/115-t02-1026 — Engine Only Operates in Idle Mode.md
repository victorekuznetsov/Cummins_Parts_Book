---
aliases:
  - "Двигатель работает только на холостом ходу"
type: "Процедура"
doc: "115-t02-1026"
title_en: "Engine Only Operates in Idle Mode"
title_ru: "Двигатель работает только на холостом ходу"
modified: "2006-06-12"
engines:
  - "41349633"
families:
  - "QSK19"
manuals:
  - "4021587"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/115/115-t02-1026.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/115-t02-1026.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/115"
  - "перевод/машинный"
---

# Engine Only Operates in Idle Mode
**Двигатель работает только на холостом ходу**

> [!abstract] Процедура · `115-t02-1026`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021587 — C Command Panel System Marine Master Repair Manual|4021587]]
> **Секции:** Section TT — Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2006-06-12
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/115/115-t02-1026.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/115-t02-1026.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

- Двигатель будет работать только в режиме холостого хода.

### Как пользоваться этим деревом

Это дерево симптомов может быть использовано для устранения неполадок в симптомах холостого двигателя. Начните с шага 1 поиска неисправностей. На шаге 2 система задаст ряд вопросов и по симптому выдаст перечень действий по поиску неисправности.

### Практические замечания

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверка проводки интерфейсной коробки заказчика |  |
|  | **STEP 1A.** Проверьте Idle/Rated Switch Signal Wire для короткого замыкания | Сопротивление менее 10 Ом? |
| ШАГ 2. | Проверьте электропроводку двигателя на кабель клиентского интерфейса |  |
|  | **ШАГ 2А.** Проверьте Idle/Rated Switch Signal Wire | Сопротивление менее 10 Ом? |

### ШАГ 1. Проверка проводки интерфейсной коробки заказчика

#### ШАГ 1A. Проверить Idle / Rated Switch Signal Wire для короткого замыкания

| **Условия: ** Откройте окно клиентского интерфейса Отключить окно клиентского интерфейса к проводах двигателя, разъёму кабеля C3 от окна клиентского интерфейса. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверить провод сигнала холостого/рейтингового переключателя. Отсоедините провод сигнала холостого/рейтингового переключателя от разъема X4. Поместите один испытательный щуп на контакт с сигналом холостого/рейтингового переключателя в разъём C3. Поместите другой испытательный щуп на терминал возврата напряжения батареи 1 блока логики клиентского интерфейса. | Сопротивление менее 10 Ом? *** Ремонт: ** Заменить неисправный провод(ы). См. процедуру[[115-015-023 — Customer Interface Box\|015-023]]. | Ремонт завершён. |
| Сопротивление менее 10 Ом? ** НЕТ** | 2А |  |

### ШАГ 2. Проверьте электропроводку двигателя на кабель клиентского интерфейса

#### ШАГ 2A. Проверить Idle / Rated Switch Signal Wire

| **Условия:** Отсоедините окно интерфейса клиента к проводах двигателя, ремня кабельного разъема C3 от окна интерфейса клиента. Отсоедините окно интерфейса клиента к проводах двигателя кабельного разъема C10 от проводов двигателя. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверить провод сигнала холостого/рейтингового переключателя. Поместите один испытательный щуп в контакт сигнала холостого/рейтингового переключателя разъема C3. Поместите другой испытательный щуп на другой штифт в разъем C3. Повторите для всех других контактов в разъеме C3. | Сопротивление менее 10 Ом? *** Заменить кабель. | Ремонт завершён. |
| Сопротивление менее 10 Ом? **NORepair:** См. Руководство по обслуживанию OEM для инструкций по ремонту выключателей бездействия. | Ремонт завершён. |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> - The engine will **only** operate in idle mode.
>
> ### How To Use This Tree
>
> This symptom tree can be used to troubleshoot engine idle symptoms. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.
>
> ### Shoptalk
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check Customer Interface Box Wiring |  |
> |  | **STEP 1A.** Check Idle/Rated Switch Signal Wire for Short Circuit | Less than 10 ohms resistance? |
> | STEP 2. | Check Engine Harness to Customer Interface Box Cable |  |
> |  | **STEP 2A.** Check Idle/Rated Switch Signal Wire | Less than 10 ohms resistance? |
>
> ### STEP 1. Check Customer Interface Box Wiring
>
> #### STEP 1A. Check Idle/Rated Switch Signal Wire for Short Circuit
>
> | **Conditions:** Open the customer interface box Disconnect customer interface box to engine harness cable connector C3 from the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check idle/rated switch signal wire. Disconnect the idle/rated switch signal wire from the X4 connector. Place one test lead on the idle/rated switch signal pin in connector C3. Place the other test lead on the battery 1 voltage return terminal of the customer interface box logic unit. | Less than 10 ohms resistance? **YESRepair:** Replace the faulty wire(s). Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |
> | Less than 10 ohms resistance? **NO** | 2A |  |
>
> ### STEP 2. Check Engine Harness to Customer Interface Box Cable
>
> #### STEP 2A. Check Idle/Rated Switch Signal Wire
>
> | **Conditions:** Disconnect customer interface box to engine harness cable connector C3 from the customer interface box. Disconnect customer interface box to engine harness cable connector C10 from the engine harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check idle/rated switch signal wire. Place one test lead in the idle/rated switch signal pin of the C3 connector. Place the other test lead on another pin in the C3 connector. Repeat for all other pins in the C3 connector. | Less than 10 ohms resistance? **YESRepair:** Replace the cable. | Repair complete. |
> | Less than 10 ohms resistance? **NORepair:** Refer to OEM Service Manual for idle switch repair instructions. | Repair complete. |  |
