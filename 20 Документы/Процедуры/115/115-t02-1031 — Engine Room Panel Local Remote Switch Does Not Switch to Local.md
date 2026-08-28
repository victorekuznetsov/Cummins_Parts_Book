---
aliases:
  - "Переключатель пульта МО не переходит в местный режим"
type: "Процедура"
doc: "115-t02-1031"
title_en: "Engine Room Panel Local/Remote Switch Does Not Switch to Local"
title_ru: "Переключатель пульта МО не переходит в местный режим"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/115/115-t02-1031.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/115-t02-1031.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/115"
  - "перевод/машинный"
---

# Engine Room Panel Local/Remote Switch Does Not Switch to Local
**Переключатель пульта МО не переходит в местный режим**

> [!abstract] Процедура · `115-t02-1031`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021587 — C Command Panel System Marine Master Repair Manual|4021587]]
> **Секции:** Section TT — Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2007-01-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/115/115-t02-1031.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/115-t02-1031.pdf)

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

Для запуска коленчатого механизма двигателя с панели машинного отделения должны быть соблюдены следующие параметры панели:

- Включается панель питания машинного отделения и освещается лампа.

- Двигатель должен быть остановлен.

Для запуска коленчатого механизма двигателя с удаленной панели должны быть соблюдены следующие параметры панели:

- Удалённая панель питания лампы освещалась.

- Локальная стартовая лампа **только **не освещается.

- Двигатель должен быть остановлен.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте клиентский интерфейс Box Logic Unit |  |
|  | **ШАГ 1А** Проверьте лампу в локальном режиме | Подсвечивается ли лампа местного режима? |
| ШАГ 2. | Проверить панель машинного отделения |  |
|  | **ШАГ 2А** Проверьте кнопку «Начать только локально» | Сопротивление менее 10 Ом? |
| ШАГ 3. | Проверить Panel Wiring |  |
|  | **STEP 3A** Проверить проводку панели машинного отделения | Сопротивление менее 10 Ом? |
|  | **STEP 3A-1.** Проверьте питание коммутатора двигателя | Сопротивление менее 10 Ом? |
|  | **STEP 3A-2.** Проверьте локальный режим питания | Сопротивление менее 10 Ом? |
| ШАГ 4. | Проверьте панельную систему кабеля |  |
|  | **STEP 4A.** Проверить кабель панели машинного отделения | Сопротивление менее 10 Ом? |
| ШАГ 5. | Проверьте интерфейс клиента |  |
|  | **STEP 5A.** Проверьте локальный режим питания | Сопротивление менее 10 Ом? |

### ШАГ 1. Проверьте клиентский интерфейс Box Logic

#### ШАГ 1A. Проверьте лампу локального режима

| **Условия:** Найдите панель машинного отделения Включите выключатель питания и светильник Открытый клиентский интерфейс. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте местный режим лампы. Нажмите кнопку локального запуска. Проверьте локальный режим лампы, освещенной на логическом блоке клиентского интерфейса. | Подсвечивается ли лампа местного режима? *Да | Ремонт завершён. |
| Подсвечивается ли лампа местного режима? **НЕТ** | 2А |  |

### ШАГ 2. Проверить панель машинного отделения

#### ШАГ 2A. Локальная стартовая кнопка

| **Условия:** Расположение панели машинного отделения Отключить разъем панели управления. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте функцию локального запуска только с кнопок. Поместите один испытательный щуп на терминал питания переключателя питания машинного отделения разъема панели управления. Поместите другой испытательный щуп на локальный терминал подачи режима разъема панели управления. Нажмите кнопку локального запуска. | Сопротивление менее 10 Ом? *Да | 3А |
| Сопротивление менее 10 Ом? **NORepair:** Заменить панель управления. См. процедуру[[115-015-024 — Engine Room Panel\|015-024]]. | Ремонт завершён. |  |

### ШАГ 3. Проверить Panel Wiring

#### ШАГ 3A. Проверка проводов панели Engine Room

| **Условия:** Найдите панель машинного отделения Открытая дверь панели машинного отделения. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте проводку панели машинного отделения. Отсоедините кабельный разъём C14 от панели машинного отделения. Подключите один испытательный щуп к контакту питания переключателя питания в машинном отделении на разъеме C14 на панели. Поместите другой испытательный щуп на контакт питания локального режима на разъеме C14 на панели. Нажмите кнопку локального запуска. | Сопротивление менее 10 Ом? *Да | 4А |
| Сопротивление менее 10 Ом? **НЕТ** | 3А-1-1 |  |

#### ШАГ 3A-1. Проверьте двигатель комнаты питание коммутатор провод

| **Условия:** Найдите панель машинного отделения Открытая дверь панели машинного отделения. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверяйте провода между разъёмом жгута проводов и разъёмом панели управления. Отсоедините кабельный разъём C14 от панели машинного отделения. Поместите один испытательный щуп на контакт питания переключателя двигателя в панельный разъем C14. Поместите другой испытательный щуп на контакт питания переключателя в машинном отделении на разъем панели управления. | Сопротивление менее 10 Ом? *Да | 3А-2 |
| Сопротивление менее 10 Ом? **NORepair:** Заменить неисправный провод. См. процедуру[[115-015-024 — Engine Room Panel\|015-024]]. | Ремонт завершён. |  |

#### ШАГ 3A-2. Проверьте локальный режим поставки

| **Условия:** Найдите панель машинного отделения Открытая дверь панели машинного отделения. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверяйте провода между разъёмом жгута проводов и разъёмом панели управления. Отсоедините кабельный разъём C14 от панели машинного отделения. Поместите один испытательный щуп на контакт питания локального режима на разъем С14. Поместите другой испытательный щуп на контакт питания локального режима на разъем панели управления. | Сопротивление менее 10 Ом? *Да | 4А |
| Сопротивление менее 10 Ом? **NORepair:** Заменить неисправный провод. См. процедуру[[115-015-024 — Engine Room Panel\|015-024]]. | Ремонт завершён. |  |

### ШАГ 4. Проверьте панельную систему кабеля

#### ШАГ 4A. Проверить панель кабеля машинного отделения

| **Условия:** Отсоединить кабельный разъём С14 от панели машинного отделения Отключить кабельный разъём С7 от окна интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте кабель панели машинного отделения. Установите перемычку между контактом питания переключателя двигателя и контактом питания локального режима в разъеме C14. Поместите один испытательный щуп в контакт питания переключателя в разъеме C7. Поместите другой испытательный щуп в локальный режим подачи контакта в разъем С7. | Сопротивление менее 10 Ом? *Да | 5а |
| Сопротивление менее 10 Ом? **Заменить кабель.** | Ремонт завершён. |  |

### ШАГ 5. Проверка проводки интерфейсной коробки заказчика

#### ШАГ 5A. Проверьте локальный режим поставки

| **Условия:** Откройте окно интерфейса клиента Отключите кабель машинного отделения на разъеме C7 от окна интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте локальный режим питания провода. Поместите один испытательный щуп на контакт питания локального режима в разъем С7. Поместите другой измерительный щуп на локальный терминал поставки в интерфейсе клиента на логический блок. | Сопротивление менее 10 Ом?  Заменить логический блок клиентского интерфейса. См. процедуру[[115-015-023 — Customer Interface Box\|015-023]]. | Ремонт завершён. |
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
> To initiate engine crank from the engine room panel, the following panel parameters **must** be met:
>
> - The engine room panel power switch on and lamp illuminated.
>
> - The engine **must** be stopped.
>
> To initiate engine crank from the remote panel, the following panel parameters **must** be met:
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
> | STEP 1. | Check the Customer Interface Box Logic Unit |  |
> |  | **STEP 1A.** Check Local Mode Lamp | Is local mode lamp illuminated? |
> | STEP 2. | Check Engine Room Panel |  |
> |  | **STEP 2A.** Check Local Start Only Button | Less than 10 ohms resistance? |
> | STEP 3. | Check Panel Wiring |  |
> |  | **STEP 3A.** Check Engine Room Panel Wiring | Less than 10 ohms resistance? |
> |  | **STEP 3A-1.** Check Engine Room Power Switch Supply Wire | Less than 10 ohms resistance? |
> |  | **STEP 3A-2.** Check the Local Mode Supply Wire | Less than 10 ohms resistance? |
> | STEP 4. | Check Panel System Cable |  |
> |  | **STEP 4A.** Check Engine Room Panel Cable | Less than 10 ohms resistance? |
> | STEP 5. | Check Customer Interface Box |  |
> |  | **STEP 5A.** Check the Local Mode Supply Wire | Less than 10 ohms resistance? |
>
> ### STEP 1. Check Customer Interface Box Logic Unit
>
> #### STEP 1A. Check Local Mode Lamp
>
> | **Conditions:** Locate engine room panel Power switch on and lamp illuminated Open customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check local mode lamp. Push the local start only button. Verify local mode lamp illuminated on the customer interface box logic unit. | Is the local mode lamp illuminated? **YES** | Repair complete. |
> | Is the local mode lamp illuminated? **NO** | 2A |  |
>
> ### STEP 2. Check Engine Room Panel
>
> #### STEP 2A. Check Local Start Only Button
>
> | **Conditions:** Locate engine room panel Disconnect control panel connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Verify local start only button function. Place one test lead on the engine room power switch supply terminal of the control panel connector. Place the other test lead on the local mode supply terminal of the control panel connector. Press the local start only button. | Less than 10 ohms resistance? **YES** | 3A |
> | Less than 10 ohms resistance? **NORepair:** Replace the control panel. Refer to Procedure [[115-015-024 — Engine Room Panel\|015-024]]. | Repair complete. |  |
>
> ### STEP 3. Check Panel Wiring
>
> #### STEP 3A. Check Engine Room Panel Wiring
>
> | **Conditions:** Locate engine room panel Open engine room panel door. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check engine room panel wiring. Disconnect cable connector C14 from the engine room panel. Connect one test lead to the engine room power switch supply pin at the C14 connector on the panel. Place the other test lead on the local mode supply pin at the C14 connector on the panel. Press the local start only button. | Less than 10 ohms resistance? **YES** | 4A |
> | Less than 10 ohms resistance? **NO** | 3A-1 |  |
>
> #### STEP 3A-1. Check Engine Room Power Switch Supply Wire
>
> | **Conditions:** Locate engine room panel Open engine room panel door. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check wires between harness connector and control panel connector. Disconnect cable connector C14 from the engine room panel. Place one test lead on the engine room power switch supply pin on panel connector C14. Place the other test lead on the engine room power switch supply pin on the control panel connector. | Less than 10 ohms resistance? **YES** | 3A-2 |
> | Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-024 — Engine Room Panel\|015-024]]. | Repair complete. |  |
>
> #### STEP 3A-2. Check the Local Mode Supply Wire
>
> | **Conditions:** Locate engine room panel Open engine room panel door. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check wires between harness connector and control panel connector. Disconnect cable connector C14 from the engine room panel. Place one test lead on the local mode supply pin on connector C14. Place the other test lead on the local mode supply pin on the control panel connector. | Less than 10 ohms resistance? **YES** | 4A |
> | Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-024 — Engine Room Panel\|015-024]]. | Repair complete. |  |
>
> ### STEP 4. Check Panel System Cable
>
> #### STEP 4A. Check Engine Room Panel Cable
>
> | **Conditions:** Disconnect cable connector C14 from the engine room panel Disconnect cable connector C7 from the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the engine room panel cable. Install a jumper between the engine room power switch supply pin and the local mode supply pin in connector C14. Place one test lead in the engine room power switch supply pin in connector C7. Place the other test lead in the local mode supply pin in connector C7. | Less than 10 ohms resistance? **YES** | 5A |
> | Less than 10 ohms resistance? **NORepair:** Replace the cable. | Repair complete. |  |
>
> ### STEP 5. Check Customer Interface Box Wiring
>
> #### STEP 5A. Check the Local Mode Supply Wire
>
> | **Conditions:** Open the customer interface box Disconnect engine room cable at connector C7 from the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the local mode supply wire. Place one test lead on the local mode supply pin in connector C7. Place the other test lead on the local mode supply terminal on the customer interface box logic unit. | Less than 10 ohms resistance? **YESRepair:** Replace the customer interface box logic unit. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |
> | Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |  |
