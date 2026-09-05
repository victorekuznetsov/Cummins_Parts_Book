---
aliases:
  - "Дистанционный пульт не переключается в местный режим"
type: "Процедура"
doc: "115-t02-1033"
title_en: "Remote Panel Does Not Switch to Local"
title_ru: "Дистанционный пульт не переключается в местный режим"
modified: "2007-01-08"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4021587"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/115/115-t02-1033.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/115-t02-1033.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/115"
  - "перевод/машинный"
---

# Remote Panel Does Not Switch to Local
**Дистанционный пульт не переключается в местный режим**

> [!abstract] Процедура · `115-t02-1033`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021587 — C Command Panel System Marine Master Repair Manual|4021587]]
> **Секции:** Section TT — Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2007-01-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/115/115-t02-1033.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/115-t02-1033.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

- Двигатель будет сворачивать, когда кнопка запуска нажимается на удаленную панель.

### Как пользоваться этим деревом

Это дерево симптомов может быть использовано для устранения симптомов запуска двигателя. Начните с шага 1 поиска неисправностей. На шаге 2 система задаст ряд вопросов и по симптому выдаст перечень действий по поиску неисправности.

### Практические замечания

Для запуска коленчатого двигателя с панели машинного отделения должны быть соблюдены следующие параметры панели:

- Включается силовой выключатель машинного отделения и освещается лампа.

- Двигатель должен быть остановлен.

Для запуска коленчатого механизма двигателя с удаленной панели должны быть соблюдены следующие параметры панели:

- Удалённая панель питания лампы освещалась.

- Локальная стартовая лампа **только **не освещается.

- Двигатель должен быть остановлен.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте клиентский интерфейс Box Logic |  |
|  | **ШАГ 1А** Проверьте лампу в локальном режиме | Подсвечивается ли лампа местного режима? |
|  | **STEP 1B.** Проверьте локальный пуск только лампы на удаленной панели | Локальный старт **только** лампа подсвечивается? |
| ШАГ 2. | Проверьте панельную систему кабеля |  |
|  | **STEP 2A.** Проверить кабель дистанционной панели | Сопротивление менее 10 Ом? |
| ШАГ 3. | Проверка проводки интерфейсной коробки заказчика |  |
|  | **STEP 3A.** Проверьте провода локального режима питания удаленной панели | Сопротивление менее 10 Ом? |

### ШАГ 1. Проверьте клиентский интерфейс Box Logic

#### ШАГ 1A. Проверьте лампу локального режима

| **Условия: **Найдите панель машинного отделения Включите выключатель питания и светильник Открытый клиентский интерфейс. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте местный режим лампы. Нажмите кнопку локального запуска. Проверьте локальный режим лампы, освещенной на логическом блоке клиентского интерфейса. | Подсвечивается ли лампа местного режима? *Да | 1В |
| Подсвечивается ли лампа местного режима? **NORepair: **См. панель машинного отделения Не удается переключиться на локальное дерево симптомов. | Ремонт завершён. |  |

#### ШАГ 1B. Проверьте локальный запуск только лампы на удаленной панели

| **Условия:** Расположение удаленной панели Светильник Power освещен. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте только лампу локального запуска. | Подсвечивается ли лампа «только для старта»? *Да | Ремонт завершён. |
| Подсвечивается ли лампа «только для старта»? **НЕТ** | 2А |  |

### ШАГ 2. Проверьте панельную систему кабеля

#### ШАГ 2A. Проверьте удаленный панельный кабель

| **Условия: **Найти и открыть окно клиентского интерфейса Найти и открыть удаленную панель. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте кабель удаленной панели. Установите перемычку между терминалом питания удаленного режима локального режима и терминалом возврата удаленной панели на разъеме панели управления удаленной панелью. Поместите один измерительный щуп на удаленную панель локального режима терминала питания в клиентский интерфейс коробки X4 разъема. Поместите другой измерительный щуп на терминал возврата удаленной панели в разъеме интерфейса клиента X4. | Сопротивление менее 10 Ом? *Да | 3А |
| Сопротивление менее 10 Ом? **Заменить кабель.** См. сервисное руководство изготовителя машины. | Ремонт завершён. |  |

### ШАГ 3. Проверка проводки интерфейсной коробки заказчика

#### ШАГ 3A. Проверьте локальную сеть удаленной панели

| **Условия: **Откройте окно интерфейса клиента Отключите кабель удаленной панели на разъеме X4 окна интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте провод питания локального режима удаленной панели. Поместите один измерительный щуп на удаленную панель локального режима питания контакта в разъем X4 клиентского интерфейса коробки. Поместите другой измерительный щуп на локальный терминал поставки в интерфейсе клиента на логический блок. | Сопротивление менее 10 Ом? **Ремонт:** Заменить пульт дистанционного управления. См. процедуру[[115-015-025 — Remote Panel\|015-025]]. | Ремонт завершён. |
| Сопротивление менее 10 Ом? **NORepair:** Заменить неисправный провод. См. процедуру[[115-015-023 — Customer Interface Box\|015-023]]. | Ремонт завершён. |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> - Engine will crank when the start button is pushed at the remote panel.
>
> ### How To Use This Tree
>
> This symptom tree can be used to troubleshoot engine start symptoms. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.
>
> ### Shoptalk
>
> To initiate engine crank from the engine room panel the following panel parameters **must** be met:
>
> - The engine room power switch on and lamp illuminated.
>
> - The engine **must** be stopped.
>
> To initiate engine crank from the remote panel the following panel parameters **must** be met:
>
> - The remote panel power lamp illuminated.
>
> - The local start **only** lamp is **not** illuminated.
>
> - The engine **must** be stopped.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check Customer Interface Box Logic Unit |  |
> |  | **STEP 1A.** Check Local Mode Lamp | Is the local mode lamp illuminated? |
> |  | **STEP 1B.** Check Local Start Only Lamp at Remote Panel | Local start **only** lamp illuminated? |
> | STEP 2. | Check Panel System Cable |  |
> |  | **STEP 2A.** Check Remote Panel Cable | Less than 10 ohms resistance? |
> | STEP 3. | Check Customer Interface Box Wiring |  |
> |  | **STEP 3A.** Check the Remote Panel Local Mode Supply Wire | Less than 10 ohms resistance? |
>
> ### STEP 1. Check Customer Interface Box Logic Unit
>
> #### STEP 1A. Check Local Mode Lamp
>
> | **Conditions:** Locate engine room panel Power switch on and lamp illuminated Open customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check local mode lamp. Push the local start only button. Verify local mode lamp illuminated on the customer interface box logic unit. | Is the local mode lamp illuminated? **YES** | 1B |
> | Is the local mode lamp illuminated? **NORepair:** Refer to Engine Room Panel Fails to Switch to Local symptom tree. | Repair complete. |  |
>
> #### STEP 1B. Check Local Start Only Lamp at Remote Panel
>
> | **Conditions:** Locate remote panel Power lamp illuminated. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check local start only lamp. | Is local start **only** lamp illuminated? **YES** | Repair complete. |
> | Is local start **only** lamp illuminated? **NO** | 2A |  |
>
> ### STEP 2. Check Panel System Cable
>
> #### STEP 2A. Check Remote Panel Cable
>
> | **Conditions:** Locate and open customer interface box Locate and open remote panel. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the remote panel cable. Install a jumper between remote panel local mode supply terminal and the remote panel return terminal on remote panel control panel connector. Place one test lead on the remote panel local mode supply terminal in customer interface box X4 connector. Place the other test lead on the remote panel return terminal in the customer interface box X4 connector. | Less than 10 ohms resistance? **YES** | 3A |
> | Less than 10 ohms resistance? **NORepair:** Replace the cable. Refer to the OEM service manual. | Repair complete. |  |
>
> ### STEP 3. Check Customer Interface Box Wiring
>
> #### STEP 3A. Check the Remote Panel Local Supply Wire
>
> | **Conditions:** Open the customer interface box Disconnect remote panel cable at X4 connector of the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the remote panel local mode supply wire. Place one test lead on the remote panel local mode supply pin in connector X4 of the customer interface box. Place the other test lead on the local mode supply terminal on the customer interface box logic unit. | Less than 10 ohms resistance? **YESRepair:** Replace the remote panel control panel. Refer to Procedure [[115-015-025 — Remote Panel\|015-025]]. | Repair complete. |
> | Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |  |
