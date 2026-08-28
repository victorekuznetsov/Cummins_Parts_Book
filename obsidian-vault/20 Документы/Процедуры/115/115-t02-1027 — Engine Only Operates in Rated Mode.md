---
aliases:
  - "Двигатель работает только в номинальном режиме"
type: "Процедура"
doc: "115-t02-1027"
title_en: "Engine Only Operates in Rated Mode"
title_ru: "Двигатель работает только в номинальном режиме"
modified: "2006-06-12"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4021587"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/115/115-t02-1027.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/115-t02-1027.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/115"
  - "перевод/машинный"
---

# Engine Only Operates in Rated Mode
**Двигатель работает только в номинальном режиме**

> [!abstract] Процедура · `115-t02-1027`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021587 — C Command Panel System Marine Master Repair Manual|4021587]]
> **Секции:** Section TT — Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2006-06-12
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/115/115-t02-1027.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/115-t02-1027.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

- Двигатель будет работать только в номинальном режиме.

### Как пользоваться этим деревом

Это дерево симптомов может быть использовано для устранения симптомов двигателя. Начните с шага 1 поиска неисправностей. На шаге 2 система задаст ряд вопросов и по симптому выдаст перечень действий по поиску неисправности.

### Практические замечания

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверка проводки интерфейсной коробки заказчика |  |
|  | **STEP 1A.** Проверьте Idle/Rated Switch Signal Wire с помощью жгута с проводкой двигателя | Сопротивление менее 10 Ом? |
|  | **STEP 1B.** Проверьте Idle/Rated Switch Signal Wire с помощью жгута для проводов двигателя | Сопротивление менее 10 Ом? |
| ШАГ 2. | Проверьте электропроводку двигателя на кабель клиентского интерфейса |  |
|  | **ШАГ 2А.** Проверьте Idle/Rated Switch Signal Wire | Сопротивление менее 10 Ом? |

### ШАГ 1. Проверка проводки интерфейсной коробки заказчика

#### ШАГ 1A. Проверьте Idle / Rated Switch Signal Wire с помощью электропроводки двигателя

| **Условия:** Откройте окно клиентского интерфейса Отключить окно клиентского интерфейса к проводах двигателя, разъёму кабеля C3 от окна клиентского интерфейса. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверить провод сигнала холостого/рейтингового переключателя. Отсоедините провод сигнала холостого/рейтингового переключателя от разъема X4. Поместите один испытательный щуп на контакт с сигналом холостого/рейтингового переключателя в разъём C3. Поместите другой испытательный щуп на контакт с сигналом переключателя с номинальным значением холостого хода на разъем X4. | Сопротивление менее 10 Ом? *Да | 1В |
| Сопротивление менее 10 Ом? **NORepair:** Заменить неисправный провод. См. процедуру[[115-015-023 — Customer Interface Box\|015-023]]. | Ремонт завершён. |  |

#### ШАГ 1B. Проверьте Idle / Rated Switch Signal Wire с помощью электропроводки двигателя

| **Условия:** Откройте окно интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверить провод возврата выключателя / номинальный выключатель. Отсоедините провод возврата холостого/рейтингового переключателя от разъема X4. Поместите один измерительный щуп на терминал возврата выключателя с неработающим/рейтинговым номером на логический блок окна интерфейса клиента. Поместите другой испытательный щуп на неработающий обратный контакт переключателя на разъеме X4. | Сопротивление менее 10 Ом? *Да | 2А |
| Сопротивление менее 10 Ом? **NORepair:** Заменить неисправный провод. См. процедуру[[115-015-023 — Customer Interface Box\|015-023]]. | Ремонт завершён. |  |

### ШАГ 2. Проверьте электропроводку двигателя на кабель клиентского интерфейса

#### ШАГ 2A. Проверить Idle / Rated Switch Signal Wire

| **Условия:** Отсоедините окно интерфейса клиента к проводах двигателя, ремня кабельного разъема C3 от окна интерфейса клиента. Отсоедините окно интерфейса клиента к проводах двигателя кабельного разъема C10 от проводов двигателя. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверить провод сигнала холостого/рейтингового переключателя. Поместите один испытательный щуп в контакт сигнала холостого/рейтингового переключателя разъема C3. Поместите другой испытательный щуп в контакт сигнала холостого/рейтингового переключателя разъема C10. | Сопротивление менее 10 Ом? **Ремонт:** Заменить инструкции по ремонту выключателей или выключателей. | Ремонт завершён. |
| Сопротивление менее 10 Ом? **Заменить кабель.** | Ремонт завершён. |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> - The engine will **only** operate in rated mode.
>
> ### How To Use This Tree
>
> This symptom tree can be used to troubleshoot engine symptoms. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.
>
> ### Shoptalk
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check Customer Interface Box Wiring |  |
> |  | **STEP 1A.** Check Idle/Rated Switch Signal Wire with Engine Harness Disconnected | Less than 10 ohms resistance? |
> |  | **STEP 1B.** Check Idle/Rated Switch Signal Wire with Engine Harness Disconnected | Less than 10 ohms resistance? |
> | STEP 2. | Check Engine Harness to Customer Interface Box Cable |  |
> |  | **STEP 2A.** Check Idle/Rated Switch Signal Wire | Less than 10 ohms resistance? |
>
> ### STEP 1. Check Customer Interface Box Wiring
>
> #### STEP 1A. Check Idle/Rated Switch Signal Wire with Engine Harness Disconnected
>
> | **Conditions:** Open the customer interface box Disconnect customer interface box to engine harness cable connector C3 from the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check idle/rated switch signal wire. Disconnect the idle/rated switch signal wire from the X4 connector. Place one test lead on the idle/rated switch signal pin in connector C3. Place the other test lead on idle rated switch signal pin on the X4 connector. | Less than 10 ohms resistance? **YES** | 1B |
> | Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |  |
>
> #### STEP 1B. Check Idle/Rated Switch Signal Wire with Engine Harness Disconnected
>
> | **Conditions:** Open the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check idle/rated switch return wire. Disconnect the idle/rated switch return wire from the X4 connector. Place one test lead on the idle/rated switch return terminal on the customer interface box logic unit. Place the other test lead on the idle rated switch return pin on the X4 connector. | Less than 10 ohms resistance? **YES** | 2A |
> | Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |  |
>
> ### STEP 2. Check Engine Harness to Customer Interface Box Cable
>
> #### STEP 2A. Check Idle/Rated Switch Signal Wire
>
> | **Conditions:** Disconnect customer interface box to engine harness cable connector C3 from the customer interface box. Disconnect customer interface box to engine harness cable connector C10 from the engine harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check idle/rated switch signal wire. Place one test lead in the idle/rated switch signal pin of the C3 connector. Place the other test lead in the idle/rated switch signal pin of the C10 connector. | Less than 10 ohms resistance? **YESRepair:** Replace to the OEM service manual or idle switch repair instructions. | Repair complete. |
> | Less than 10 ohms resistance? **NORepair:** Replace the cable. | Repair complete. |  |
