---
aliases:
  - "Дистанционный пульт показывает неверное назначение"
type: "Процедура"
doc: "115-t02-1035"
title_en: "Remote Panel Indicates Incorrect Assignment"
title_ru: "Дистанционный пульт показывает неверное назначение"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/115/115-t02-1035.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/115-t02-1035.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/115"
  - "перевод/машинный"
---

# Remote Panel Indicates Incorrect Assignment
**Дистанционный пульт показывает неверное назначение**

> [!abstract] Процедура · `115-t02-1035`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021587 — C Command Panel System Marine Master Repair Manual|4021587]]
> **Секции:** Section TT — Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2006-06-12
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/115/115-t02-1035.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/115-t02-1035.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

- Удалённая панель указывает, что панель машинного отделения **не** в локальном режиме запуска **только**.

- Панель машинного отделения указывает на то, что активен режим локального запуска **только**.

### Как пользоваться этим деревом

Это дерево симптомов может быть использовано для устранения симптомов панели. Начните с шага 1 поиска неисправностей. На шаге 2 система задаст ряд вопросов и по симптому выдаст перечень действий по поиску неисправности.

### Практические замечания

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте локальный запуск только лампы |  |
|  | **STEP 1A.** Проверьте панель машинного отделения Локальная кнопка запуска и лампа | Светильник подсвечивается? |
| ШАГ 2. | Проверьте панель управления удаленной панелью |  |
|  | **STEP 2A.** Проверить на напряжённость панели управления | 24 ВДЦ? |
| ШАГ 3. | Проверьте панельную систему кабеля |  |
|  | **STEP 3A.** Проверить кабель дистанционной панели | Сопротивление менее 10 Ом? |
| ШАГ 4. | Проверка проводки интерфейсной коробки заказчика |  |
|  | **STEP 4A.** Проверить наличие провода в удаленном локальном режиме | Сопротивление менее 10 Ом? |
|  | **STEP 4B.** Проверьте удаленную панель | Сопротивление менее 10 Ом? |

### ШАГ 1. Проверьте локальный запуск только лампы

#### ШАГ 1A. Проверьте панель машинного отделения Локальный запуск только кнопки и лампы

| **Условия:** Убедитесь, что выключатель питания панели машинного отделения включен и лампа освещена. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Убедитесь, что лампа питания удаленной панели освещена. Нажмите локальный запуск только на кнопку на панели машинного отделения. Убедитесь, что на панели машинного отделения освещена только лампа локального запуска. | Светильник подсвечивается? *Да | 2А |
| Светильник подсвечивается? **NORepair:** См. панель машинного отделения указывает на неправильный признак наложения. | Ремонт завершён. |  |

### ШАГ 2. Проверьте панель управления удаленной панелью

#### ШАГ 2A. Проверьте напряжение на панели управления

| **Условия:** Проверить панель машинного отделения Локальный пуск только лампы освещается Откройте пульт дистанционного управления. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте напряжение на панели управления. Отключите провод питания удаленной панели локального режима от разъёма панели управления X4. Отключите провод возврата удаленной панели от разъема панели управления X4. Поместите положительный пробный щуп на удаленную панель локального режима питания провода. Поместите отрицательный пробный щуп на провод возврата удаленной панели. | 24 ВДЦ? **Ремонт:** Заменить пульт дистанционного управления. См. процедуру[[115-015-025 — Remote Panel\|015-025]]. | Ремонт завершён. |
| 24 ВДЦ? **НЕТ** | 3А |  |

### ШАГ 3. Проверьте панельную систему кабеля

#### ШАГ 3A. Проверьте удаленный панельный кабель

| **Условия:** Найти и открыть окно клиентского интерфейса Найти и открыть пульт дистанционного подключения Отключить кабель дистанционного управления от разъема X4 в окне клиентского интерфейса. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте кабель удаленной панели. Установите перемычку между терминалом питания локального режима удаленной панели и терминалом возврата удаленной панели на панели дистанционного управления X4 в панели дистанционного управления. Поместите один испытательный щуп на удаленную панель локального режима питания провода. Поместите другой испытательный щуп на провод возврата удаленной панели. | Сопротивление менее 10 Ом? *Да | 4А |
| Сопротивление менее 10 Ом? **Заменить кабель.** | Ремонт завершён. |  |

### ШАГ 4. Проверка проводки интерфейсной коробки заказчика

#### ШАГ 4A. Проверьте удаленную панель локального режима питания

| **Условия:** Откройте окно клиентского интерфейса Отключите разъем C7 от окна клиентского интерфейса. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте провод питания локального режима удаленной панели. Поместите один измерительный щуп на удаленную панель локального режима терминала питания в клиентский интерфейс коробки X4 разъема. Поместите другой испытательный щуп на контакт питания локального режима в разъем С7. | Сопротивление менее 10 Ом? *Да | 4B |
| Сопротивление менее 10 Ом? **NORepair:** Заменить неисправный провод. См. процедуру[[115-015-023 — Customer Interface Box\|015-023]]. | Ремонт завершён. |  |

#### ШАГ 4B. Проверить удаленную панель Return Wire

| **Условия:** Откройте окно клиентского интерфейса Отключите разъем C7 от окна клиентского интерфейса. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте провод возврата удаленной панели. Поместите один измерительный щуп на терминал возврата удаленной панели на разъеме интерфейса клиента X4. Поместите другой испытательный щуп на панель машинного отделения обратного контакта в разъем С7. | Сопротивление менее 10 Ом? **Ремонт:** Заменить пульт дистанционного управления. См. процедуру[[115-015-025 — Remote Panel\|015-025]]. | Ремонт завершён. |
| Сопротивление менее 10 Ом? **NORepair:** Заменить провод. См. процедуру[[115-015-025 — Remote Panel\|015-025]]. | Ремонт завершён. |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> - The remote panel indicates the engine room panel is **not** in the local start **only** mode.
>
> - The engine room panel indicates that local start **only** mode is active.
>
> ### How To Use This Tree
>
> This symptom tree can be used to troubleshoot panel symptoms. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.
>
> ### Shoptalk
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check Local Start Only Lamp Operation |  |
> |  | **STEP 1A.** Check Engine Room Panel Local Start Only Button and Lamp | Lamp illuminated? |
> | STEP 2. | Check Remote Panel Control Panel |  |
> |  | **STEP 2A.** Check for Voltage to Control Panel | 24 VDC? |
> | STEP 3. | Check Panel System Cable |  |
> |  | **STEP 3A.** Check Remote Panel Cable | Less than 10 ohms resistance? |
> | STEP 4. | Check Customer Interface Box Wiring |  |
> |  | **STEP 4A.** Check Remote Local Mode Supply Wire | Less than 10 ohms resistance? |
> |  | **STEP 4B.** Check Remote Panel Return Wire | Less than 10 ohms resistance? |
>
> ### STEP 1. Check Local Start Only Lamp Operation
>
> #### STEP 1A. Check Engine Room Panel Local Start Only Button and Lamp
>
> | **Conditions:** Verify that engine room panel power switch is on and lamp illuminated. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Verify that remote panel power lamp is illuminated. Press the local start only on button on the engine room panel. Verify that the local start only lamp is illuminated on the engine room panel. | Lamp illuminated? **YES** | 2A |
> | Lamp illuminated? **NORepair:** Refer to Engine Room Panel Indicates Incorrect Assignment symptom tree. | Repair complete. |  |
>
> ### STEP 2. Check Remote Panel Control Panel
>
> #### STEP 2A. Check for Voltage to Control Panel
>
> | **Conditions:** Verify engine room panel local start only lamp is illuminated Open the remote panel. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check voltage to control panel. Disconnect remote panel local mode supply wire from control panel X4 connector. Disconnect remote panel return wire from control panel X4 connector. Place the positive test lead on the remote panel local mode supply wire. Place the negative test lead on the remote panel return wire. | 24 VDC? **YESRepair:** Replace the remote panel control panel. Refer to Procedure [[115-015-025 — Remote Panel\|015-025]]. | Repair complete. |
> | 24 VDC? **NO** | 3A |  |
>
> ### STEP 3. Check Panel System Cable
>
> #### STEP 3A. Check Remote Panel Cable
>
> | **Conditions:** Locate and open customer interface box Locate and open remote panel Disconnect remote panel cable from the X4 connector in the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the remote panel cable. Install a jumper between remote panel local mode supply terminal and the remote panel return terminal on remote control panel X4 in the remote control panel. Place one test lead on the remote panel local mode supply wire. Place the other test lead on the remote panel return wire. | Less than 10 ohms resistance? **YES** | 4A |
> | Less than 10 ohms resistance? **NORepair:** Replace the cable. | Repair complete. |  |
>
> ### STEP 4. Check Customer Interface Box Wiring
>
> #### STEP 4A. Check Remote Panel Local Mode Supply Wire
>
> | **Conditions:** Open the customer interface box Disconnect connector C7 from customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the remote panel local mode supply wire. Place one test lead on the remote panel local mode supply terminal in customer interface box X4 connector. Place the other test lead on the local mode supply pin in connector C7. | Less than 10 ohms resistance? **YES** | 4B |
> | Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |  |
>
> #### STEP 4B. Check Remote Panel Return Wire
>
> | **Conditions:** Open the customer interface box Disconnect connector C7 from customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the remote panel return wire. Place one test lead on the remote panel return terminal on the customer interface box X4 connector. Place the other test lead on the engine room panel return pin in connector C7. | Less than 10 ohms resistance? **YESRepair:** Replace the remote panel control panel. Refer to Procedure [[115-015-025 — Remote Panel\|015-025]]. | Repair complete. |
> | Less than 10 ohms resistance? **NORepair:** Replace the wire. Refer to Procedure [[115-015-025 — Remote Panel\|015-025]]. | Repair complete. |  |
