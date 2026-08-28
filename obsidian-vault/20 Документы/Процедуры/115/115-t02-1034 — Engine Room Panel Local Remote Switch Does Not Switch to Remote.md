---
aliases:
  - "Переключатель «местный/дистанционный» пульта МО не переходит в дистанционный режим"
type: "Процедура"
doc: "115-t02-1034"
title_en: "Engine Room Panel Local/Remote Switch Does Not Switch to Remote"
title_ru: "Переключатель «местный/дистанционный» пульта МО не переходит в дистанционный режим"
modified: "2006-08-14"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4021587"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/115/115-t02-1034.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/115-t02-1034.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/115"
  - "перевод/машинный"
---

# Engine Room Panel Local/Remote Switch Does Not Switch to Remote
**Переключатель «местный/дистанционный» пульта МО не переходит в дистанционный режим**

> [!abstract] Процедура · `115-t02-1034`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021587 — C Command Panel System Marine Master Repair Manual|4021587]]
> **Секции:** Section TT — Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2006-08-14
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/115/115-t02-1034.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/115-t02-1034.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

- Двигатель **не** будет сворачиваться, когда кнопка запуска нажимается на удаленную панель.

- Двигатель будет **только **кранить, когда кнопка запуска нажимается на панель машинного отделения.

### Как пользоваться этим деревом

Это дерево симптомов может быть использовано для устранения симптомов запуска двигателя. Начните с шага 1 поиска неисправностей. На шаге 2 система задаст ряд вопросов и по симптому выдаст перечень действий по поиску неисправности.

### Практические замечания

Для запуска коленчатого двигателя с панели машинного отделения должны быть соблюдены следующие параметры панели:

- Выключатель питания панели машинного отделения на освещенной лампе.

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
|  | **ШАГ 1В** Выключите лампу локального режима | Подсвечивается ли лампа местного режима? |
| ШАГ 2. | Проверьте удаленную панель |  |
|  | **STEP 2A.** Проверьте локальный запуск панели удаленного управления только лампой | Подсвечивается ли местная лампа **только**? |
| ШАГ 3. | Проверка проводки интерфейсной коробки заказчика |  |
|  | **STEP 3A.** Проверьте провода локального режима питания удаленной панели | 24 ВДЦ? |
| ШАГ 4. | Проверьте панельную систему кабеля |  |
|  | **STEP 4A.** Проверьте кабель удаленной панели | Сопротивление больше 100k Ом? |

### ШАГ 1. Проверьте клиентский интерфейс Box Logic

#### ШАГ 1A. Проверьте лампу локального режима

| **Условия: **Найдите панель машинного отделения Включите выключатель питания и светильник Открытый клиентский интерфейс. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте местный режим лампы. Нажмите кнопку локального запуска. Проверьте локальный режим лампы, освещенной на логическом блоке клиентского интерфейса. | Подсвечивается ли лампа местного режима? *Да | 1В |
| Подсвечивается ли лампа местного режима? **NORepair:** См. Панель машинного отделения Локальный/Удаленный коммутатор Не удается переключить на Локальное дерево симптомов. | Ремонт завершён. |  |

#### ШАГ 1B. Выключите лампу локального режима

| **Условия: **Найдите панель машинного отделения Включите выключатель питания и светильник Открытый клиентский интерфейс. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте местный режим лампы. Нажмите кнопку локального запуска. Проверить локальный режим лампы не подсвечивается на логическом блоке клиентского интерфейса. | Подсвечивается ли лампа местного режима? **Ремонт: **См. панель машинного отделения Локальный/Удаленный коммутатор Не удается переключить на Удаленный симптом дерева. | Ремонт завершён. |
| Подсвечивается ли лампа местного режима? **НЕТ** | 2А |  |

### ШАГ 2. Проверьте удаленную панель

#### ШАГ 2A. Проверьте локальный запуск удаленной панели только лампой

| **Условия:** Расположение удаленной панели Светильник Power освещен. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Подсвечивается ли лампа локального запуска? | Подсвечивается ли местная лампа **только**? *Да | 3А |
| Подсвечивается ли лампа «только для старта»? **НЕТ** | Ремонт завершён. |  |

### ШАГ 3. Проверка проводки интерфейсной коробки заказчика

#### ШАГ 3A. Проверьте локальный режим питания Remote Panel

| **Условия: **Откройте окно интерфейса клиента Отключите кабель машинного отделения на разъеме C7 от окна интерфейса клиента Отключите кабель удаленной панели на разъеме интерфейса клиента X4. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте провод питания локального режима удаленной панели. Поместите положительный измерительный щуп на удаленную панель локального режима питания контакта на блок логики клиентского интерфейса. Поместите отрицательный измерительный щуп на терминал возврата удаленной панели на логический блок окна интерфейса клиента. | 24 ВДЦ? Заменить логический блок клиентского интерфейса. См. процедуру[[115-015-023 — Customer Interface Box\|015-023]]. | Ремонт завершён. |
| 24 ВДЦ? **НЕТ** | 4А |  |

### ШАГ 4. Проверьте панельную систему кабеля

#### ШАГ 4A. Проверьте кабель удаленной панели

| **Условия:** Отсоедините кабель удаленной панели в разъеме X4 интерфейса клиента и разъем удаленной панели. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте провод питания локального режима удаленной панели. Поместите один испытательный щуп на удаленную панель локального режима питания терминала на кабель. Поместите другой испытательный щуп на другой проводной терминал на кабель. Повторите для всех других проводных терминалов на кабеле. | Сопротивление больше 100k Ом? Заменить панель управления. См. процедуру[[115-015-025 — Remote Panel\|015-025]]. | Ремонт завершён. |
| Сопротивление больше 100k Ом? **Заменить кабель.** | Ремонт завершён. |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> - Engine will **not** crank when the start button is pushed at the remote panel.
>
> - Engine will **only** crank when the start button is pushed at the engine room panel.
>
> ### How To Use This Tree
>
> This symptom tree can be used to troubleshoot engine start symptoms. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.
>
> ### Shoptalk
>
> To initiate engine crank from the engine room panel the following panel parameters **must** be met:
>
> - The engine room panel power switch on the lamp illuminated.
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
> |  | **STEP 1B.** Shut Off Local Mode Lamp | Is the local mode lamp illuminated? |
> | STEP 2. | Check Remote Panel |  |
> |  | **STEP 2A.** Check Remote Panel Local Start Only Lamp | Is the local start **only** lamp illuminated? |
> | STEP 3. | Check Customer Interface Box Wiring |  |
> |  | **STEP 3A.** Check the Remote Panel Local Mode Supply Wire | 24 VDC? |
> | STEP 4. | Check Panel System Cable |  |
> |  | **STEP 4A.** Check the Remote Panel Cable | Greater than 100k ohms resistance? |
>
> ### STEP 1. Check Customer Interface Box Logic Unit
>
> #### STEP 1A. Check Local Mode Lamp
>
> | **Conditions:** Locate engine room panel Power switch on and lamp illuminated Open customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check local mode lamp. Push the local start only button. Verify local mode lamp illuminated on the customer interface box logic unit. | Is the local mode lamp illuminated? **YES** | 1B |
> | Is the local mode lamp illuminated? **NORepair:** Refer to Engine Room Panel Local/Remote Switch Fails to Switch to Local symptom tree. | Repair complete. |  |
>
> #### STEP 1B. Shut Off Local Mode Lamp
>
> | **Conditions:** Locate engine room panel Power switch on and lamp illuminated Open customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check local mode lamp. Push the local start only button. Verify local mode lamp is not illuminated on the customer interface box logic unit. | Is the local mode lamp illuminated? **YESRepair:** Refer to Engine Room Panel Local/Remote Switch Fails to Switch to Remote symptom tree. | Repair complete. |
> | Is the local mode lamp illuminated? **NO** | 2A |  |
>
> ### STEP 2. Check Remote Panel
>
> #### STEP 2A. Check Remote Panel Local Start Only Lamp
>
> | **Conditions:** Locate remote panel Power lamp illuminated. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Is the local start lamp illuminated? | Is the local start **only** lamp illuminated? **YES** | 3A |
> | Is local start **only** lamp illuminated? **NO** | Repair complete. |  |
>
> ### STEP 3. Check Customer Interface Box Wiring
>
> #### STEP 3A. Check the Remote Panel Local Mode Supply Wire
>
> | **Conditions:** Open the customer interface box Disconnect engine room cable at connector C7 from the customer interface box Disconnect remote panel cable at customer interface box X4 connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the remote panel local mode supply wire. Place the positive test lead on the remote panel local mode supply pin on the customer interface box logic unit. Place the negative test lead on the remote panel return terminal on the customer interface box logic unit. | 24 VDC? **YESRepair:** Replace the customer interface box logic unit. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |
> | 24 VDC? **NO** | 4A |  |
>
> ### STEP 4. Check Panel System Cable
>
> #### STEP 4A. Check the Remote Panel Cable
>
> | **Conditions:** Disconnect remote panel cable at customer interface box X4 connector and remote panel connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the remote panel local mode supply wire. Place one test lead on the remote panel local mode supply terminal on the cable. Place the other test lead on another wire terminal on the cable. Repeat for all other wire terminals on the cable. | Greater than 100k ohms resistance? **YESRepair:** Replace the control panel. Refer to Procedure [[115-015-025 — Remote Panel\|015-025]]. | Repair complete. |
> | Greater than 100k ohms resistance? **NORepair:** Replace the cable. | Repair complete. |  |
