---
aliases:
  - "Самопроизвольный останов двигателя"
type: "Процедура"
doc: "115-t02-1008"
title_en: "Un-requested Engine Stop"
title_ru: "Самопроизвольный останов двигателя"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/115/115-t02-1008.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/115-t02-1008.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/115"
  - "перевод/машинный"
---

# Un-requested Engine Stop
**Самопроизвольный останов двигателя**

> [!abstract] Процедура · `115-t02-1008`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021587 — C Command Panel System Marine Master Repair Manual|4021587]]
> **Секции:** Section TT — Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2006-06-12
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/115/115-t02-1008.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/115-t02-1008.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

- Двигатель останавливается без нажатия оператором кнопки остановки на панели машинного отделения или удаленной панели.

### Как пользоваться этим деревом

Это дерево симптомов может быть использовано для устранения симптомов остановки двигателя. Начните с шага 1 поиска неисправностей. Шаг 2 задаст ряд вопросов и предоставит список шагов по устранению неполадок, которые необходимо выполнить в зависимости от симптома.

### Практические замечания

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте интерфейс клиента |  |
|  | **STEP 1A** Проверьте логику интерфейса клиента | Освещена ли стоп-сигнал? |
| ШАГ 2. | Проверить панель машинного отделения |  |
|  | **STEP 2A** Проверить панель управления машинным отделением | Сопротивление менее 10 Ом? |
| ШАГ 3. | Проверьте удаленную панель |  |
|  | **STEP 3A.** Проверить панель управления удаленной панелью | Сопротивление менее 10 Ом? |

### ШАГ 1. Проверьте интерфейс клиента

#### ШАГ 1A. Проверьте клиентский интерфейс Box Logic

| **Условия:** Найти окно клиентского интерфейса Открытый ящик клиентского интерфейса. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте, что стоп-сигнал освещен. | Освещена ли стоп-сигнал? *Да | 2А |
| Освещена ли стоп-сигнал? NORepair: см. Двигатель Исполняет Незапрошенный Двигатель Прекратить Устранение Неисправностей Дерево | Ремонт завершён. |  |

### ШАГ 2. Проверить панель машинного отделения

#### ШАГ 2A. Проверить панель управления панелью Engine Room Panel

| **Условия:** Расположение панели машинного отделения Открытая дверь панели машинного отделения Отключить разъём панели управления X4. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте панель управления машинного отделения. Поместите один испытательный щуп в панель машинного отделения стоп-контакт питания на разъёме панели управления X4. Поместите другой испытательный щуп в контакт питания переключателя в машинном отделении на разъёме панели управления X4. | Сопротивление менее 10 Ом? **Ремонт:** Заменить панель управления машинного отделения. См. процедуру[[115-015-024 — Engine Room Panel\|015-024]]. | Ремонт завершён. |
| Сопротивление менее 10 Ом? **НЕТ** | 3А |  |

### ШАГ 3. Проверьте удаленную панель

#### ШАГ 3A. Проверьте панель управления удаленной панелью

| **Условия:** Расположение удаленной панели Открытая удаленная панель Отключить дистанционный панель управления панелью разъема X4. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте панель управления удаленной панелью. Поместите один испытательный щуп в контакт питания пульта дистанционного управления на разъёме панели управления X4. Поместите другой испытательный щуп на удаленную панель, остановите контакт питания панели управления разъемом X4. | Сопротивление менее 10 Ом? **Ремонт:** Заменить панель управления пультом дистанционного управления. См. процедуру[[115-015-025 — Remote Panel\|015-025]]. | Ремонт завершён. |
| Сопротивление менее 10 Ом? **NORepair:** Заменить логический блок клиентского интерфейса. См. процедуру[[115-015-023 — Customer Interface Box\|015-023]]. | Ремонт завершён. |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> - The engine stops without the operator pushing the stop button on the engine room panel or remote panel.
>
> ### How To Use This Tree
>
> This symptom tree can be used to troubleshoot engine stop symptoms. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform depending on the symptom.
>
> ### Shoptalk
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check Customer Interface Box |  |
> |  | **STEP 1A.** Check Customer Interface Box Logic Unit | Is stop lamp illuminated? |
> | STEP 2. | Check Engine Room Panel |  |
> |  | **STEP 2A.** Check Engine Room Panel Control Panel | Less than 10 ohms resistance? |
> | STEP 3. | Check Remote Panel |  |
> |  | **STEP 3A.** Check Remote Panel Control Panel | Less than 10 ohms resistance? |
>
> ### STEP 1. Check Customer Interface Box
>
> #### STEP 1A. Check Customer Interface Box Logic Unit
>
> | **Conditions:** Locate customer interface box Open customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Verify stop lamp is illuminated. | Is stop lamp illuminated? **YES** | 2A |
> | Is stop lamp illuminated? **NORepair:** Refer to the Engine Executes Un-requested Engine Stop Troubleshooting Tree | Repair complete. |  |
>
> ### STEP 2. Check Engine Room Panel
>
> #### STEP 2A. Check Engine Room Panel Control Panel
>
> | **Conditions:** Locate engine room panel Open engine room panel door Disconnect control panel connector X4. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the engine room panel control panel. Place one test lead in the engine room panel stop supply pin on the control panel X4 connector. Place the other test lead in the engine room power switch supply pin on the control panel X4 connector. | Less than 10 ohms resistance? **YESRepair:** Replace the engine room panel control panel. Refer to Procedure [[115-015-024 — Engine Room Panel\|015-024]]. | Repair complete. |
> | Less than 10 ohms resistance? **NO** | 3A |  |
>
> ### STEP 3. Check Remote Panel
>
> #### STEP 3A. Check Remote Panel Control Panel
>
> | **Conditions:** Locate remote panel Open remote panel Disconnect remote panel control panel connector X4. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the remote panel control panel. Place one test lead in the remote panel power switch supply pin on the control panel X4 connector. Place the other test lead on the remote panel stop supply pin of the control panel X4 connector. | Less than 10 ohms resistance? **YESRepair:** Replace the remote control panel control panel. Refer to Procedure [[115-015-025 — Remote Panel\|015-025]]. | Repair complete. |
> | Less than 10 ohms resistance? **NORepair:** Replace customer interface box logic unit. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |  |
