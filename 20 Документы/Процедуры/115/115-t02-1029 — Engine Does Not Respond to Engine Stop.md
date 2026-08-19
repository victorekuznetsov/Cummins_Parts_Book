---
aliases:
  - "Двигатель не реагирует на команду останова"
type: "Процедура"
doc: "115-t02-1029"
title_en: "Engine Does Not Respond to Engine Stop"
title_ru: "Двигатель не реагирует на команду останова"
modified: "2006-06-12"
engines:
  - "41349633"
families:
  - "QSK19"
manuals:
  - "4021587"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/115/115-t02-1029.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/115-t02-1029.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/115"
  - "перевод/машинный"
---

# Engine Does Not Respond to Engine Stop
**Двигатель не реагирует на команду останова**

> [!abstract] Процедура · `115-t02-1029`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021587 — C Command Panel System Marine Master Repair Manual|4021587]]
> **Секции:** Section TT — Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2006-06-12
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/115/115-t02-1029.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/115-t02-1029.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

- Двигатель **не** останавливается, когда кнопка остановки двигателя включена в поле интерфейса клиента.

### Как пользоваться этим деревом

Это дерево симптомов может быть использовано для устранения симптомов остановки двигателя. Начните с шага 1 поиска неисправностей. На шаге 2 система задаст ряд вопросов и по симптому выдаст перечень действий по поиску неисправности.

### Практические замечания

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте интерфейс клиента |  |
|  | **STEP 1A.** Check Engine Stop Switch (переключатель остановки двигателя) | Сопротивление менее 10 Ом? |

### ШАГ 1. Проверьте интерфейс клиента

#### ШАГ 1A. Проверьте переключатель Engine Stop

| **Условия: ** Открытый интерфейс клиента. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте выключатель остановки двигателя. Отсоедините четыре провода зажигания (остановка двигателя) от кнопки. Поместите измерительный щуп на каждую сторону одного контакта кнопки. Нажмите кнопку остановки двигателя. Повторите для другого контакта кнопки. | Сопротивление менее 10 Ом? *** Заменить кнопку остановки двигателя. См. процедуру[[115-015-023 — Customer Interface Box\|015-023]]. | Ремонт завершён. |
| Сопротивление менее 10 Ом? **NORepair: ** См. раздел TF в руководстве по устранению неполадок и ремонту, Электронная система управления, QSK19 CM850, Модульная общая железнодорожная система, Серийные двигатели, Бюллетень 4021493. | Ремонт завершён. |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> - The engine will **not** stop when the engine stop button is engaged at the customer interface box.
>
> ### How To Use This Tree
>
> This symptom tree can be used to troubleshoot engine stop symptoms. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.
>
> ### Shoptalk
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check Customer Interface Box |  |
> |  | **STEP 1A.** Check Engine Stop Switch | Less than 10 ohms resistance? |
>
> ### STEP 1. Check Customer Interface Box
>
> #### STEP 1A. Check Engine Stop Switch
>
> | **Conditions:** Open customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check engine stop switch. Disconnect the four ignition (engine stop) wires from the button. Place a test lead on each side of one contact of the button. Push the engine stop button. Repeat for the other contact of the button. | Less than 10 ohms resistance? **YESRepair:** Replace the engine stop button. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |
> | Less than 10 ohms resistance? **NORepair:** Refer to Section TF in the Troubleshooting and Repair Manual, Electronic Control System, QSK19 CM850, Modular Common Rail System, Series Engines, Bulletin 4021493. | Repair complete. |  |
