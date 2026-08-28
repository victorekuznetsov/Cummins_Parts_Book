---
aliases:
  - "Двигатель не останавливается ни из МО, ни с дистанционного пульта"
type: "Процедура"
doc: "115-t02-1009"
title_en: "Engine Will Not Stop From the Engine Room or Remote Panel"
title_ru: "Двигатель не останавливается ни из МО, ни с дистанционного пульта"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/115/115-t02-1009.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/115-t02-1009.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/115"
  - "перевод/машинный"
---

# Engine Will Not Stop From the Engine Room or Remote Panel
**Двигатель не останавливается ни из МО, ни с дистанционного пульта**

> [!abstract] Процедура · `115-t02-1009`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021587 — C Command Panel System Marine Master Repair Manual|4021587]]
> **Секции:** Section TT — Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2007-01-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/115/115-t02-1009.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/115-t02-1009.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

- Двигатель **не** останавливается, когда кнопка остановки нажимается на панель машинного отделения.

- Двигатель **не** остановится, когда кнопка остановки нажата на удаленную панель.

### Как пользоваться этим деревом

Это дерево симптомов может быть использовано для устранения симптомов остановки двигателя. Начните с шага 1 поиска неисправностей. На шаге 2 система задаст ряд вопросов и по симптому выдаст перечень действий по поиску неисправности.

### Практические замечания

Двигатель можно остановить, нажав кнопку остановки с панели машинного отделения или удаленной панели. Панель не должна иметь контроль запуска, чтобы остановить двигатель.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверить панель машинного отделения Stop Button |  |
|  | **STEP 1A.** Проверить вход кнопки Stop Button в блок логики интерфейса клиента | Остановить лампу? |
|  | **STEP 1B** Check Stop Button Operation | Сопротивление менее 10 Ом? |
| ШАГ 2. | Проверить кнопку Stop Panel |  |
|  | **STEP 2A.** Проверьте кнопку Stop Button на блоке логики интерфейса клиента | Остановить лампу? |
|  | **STEP 2B** Check Stop Button Operation | Сопротивление менее 10 Ом? |
| ШАГ 3. | Проверить Panel Wiring |  |
|  | **STEP 3A** Проверить проводку панели машинного отделения | Сопротивление менее 10 Ом? |
|  | **STEP 3A-1.** Проверьте питание коммутатора двигателя | Сопротивление менее 10 Ом? |
|  | **STEP 3A-2.** Проверить двигательную панель, остановить подачу проволоки | Сопротивление менее 10 Ом? |
| ШАГ 4. | Проверьте кабели Панельной системы |  |
|  | **STEP 4A.** Проверить кабель панели машинного отделения | Сопротивление менее 10 Ом? |
|  | **STEP 4B.** Проверить кабель дистанционной панели | Сопротивление менее 10 Ом? |
| ШАГ 5. | Проверка проводки интерфейсной коробки заказчика |  |
|  | **STEP 5A.** Проверить двигательную панель, остановить подачу провода | Сопротивление менее 10 Ом? |
|  | **STEP 5B.** Проверьте, не работает ли провод дистанционного питания | Сопротивление менее 10 Ом? |

### ШАГ 1. Проверить панель машинного отделения Stop Button

#### ШАГ 1A. Проверьте вход кнопки Stop Button в блок логики интерфейса клиента

| **Условия:** Расположение панели машинного отделения Панельная лампа Двигателя подсвечивается Открытым клиентским интерфейсом коробки. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте ввод кнопки остановки двигателя в логический блок клиентского интерфейса. Нажмите кнопку остановки. Проверить стоп-сигнал подсвечивается на логическом блоке клиентского интерфейса. | Остановить лампу? *Да | 2А |
| Остановить лампу? **НЕТ** | 1В |  |

#### ШАГ 1B. Операция Stop Button

| **Условия:** Открытая панель машинного отделения Отключить кабельный коннектор панели машинного отделения от панели управления. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте работу кнопки остановки. Поместите один испытательный щуп на терминал питания переключателя питания в машинном отделении разъема панели управления. Поместите другой испытательный щуп на панель машинного отделения остановки терминала питания разъема панели управления. Нажмите кнопку остановки. | Сопротивление менее 10 Ом? *Да | 3А |
| Сопротивление менее 10 Ом? **NORepair:** Заменить панель управления. См. процедуру[[115-015-024 — Engine Room Panel\|015-024]]. | Ремонт завершён. |  |

### ШАГ 2. Проверить кнопку Stop Panel

#### ШАГ 2A. Проверьте кнопку Stop Button на блоке логики интерфейса клиента

| **Условия:** Расположение пульта дистанционного управления Светодиодная панель питания подсветила Open клиентский интерфейс коробки. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте ввод кнопки остановки двигателя в логический блок клиентского интерфейса. Нажмите кнопку остановки. Проверьте стоп-сигнал, освещенный на логическом блоке клиентского интерфейса. | Остановить лампу? **** Заменить логический блок клиентского интерфейса. См. процедуру[[115-015-023 — Customer Interface Box\|015-023]]. | Ремонт завершён. |
| Остановить лампу? **НЕТ** | 2В |  |

#### ШАГ 2B. Операция Stop Button

| **Условия:** Открытая удаленная панель Отключить от панели управления кабельный разъем машинного отделения. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте работу кнопки остановки. Поместите один испытательный щуп на терминал подачи дистанционной панели разъема панели управления. Поместите другой испытательный щуп на терминал питания пульта дистанционного питания разъёма панели управления. Нажмите кнопку остановки. | Сопротивление менее 10 Ом? *Да | 4B |
| Сопротивление менее 10 Ом? **NORepair:** Заменить панель управления. См. процедуру[[115-015-025 — Remote Panel\|015-025]]. | Ремонт завершён. |  |

### ШАГ 3. Проверить Panel Wiring

#### ШАГ 3A. Проверка проводов панели Engine Room

| **Условия:** Найдите панель машинного отделения Открытая дверь панели машинного отделения. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте проводку панели машинного отделения. Отсоедините кабель C14 от панели машинного отделения. Подключите один испытательный щуп к контакту питания переключателя двигателя в разъеме C14. Поместите другой испытательный щуп на панель машинного отделения, чтобы остановить контакт питания на разъеме C14. Нажмите кнопку остановки. | Сопротивление менее 10 Ом? *Да | 4А |
| Сопротивление менее 10 Ом? **НЕТ** | 3А-1-1 |  |

#### ШАГ 3A-1. Проверьте двигатель комнаты питание коммутатор провод

| **Условия:** Найдите панель машинного отделения Открытая дверь панели машинного отделения. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверяйте провода между разъёмом жгута проводов и разъёмом панели управления. Отсоедините кабель C14 от панели машинного отделения. Поместите один испытательный щуп на контакт питания переключателя двигателя в разъеме C14. Поместите другой испытательный щуп на контакт питания переключателя в машинном отделении на разъем панели управления. | Сопротивление менее 10 Ом? *Да | 3А-2 |
| Сопротивление менее 10 Ом? **NORepair:** Заменить неисправный провод. См. процедуру[[115-015-024 — Engine Room Panel\|015-024]]. | Ремонт завершён. |  |

#### ШАГ 3A-2. Проверить панель машинного отделения Stop Supply Wire

| **Условия:** Найдите панель машинного отделения Открытая дверь панели машинного отделения. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверяйте провода между разъёмом жгута проводов и разъёмом панели управления. Отсоедините кабель C14 от панели машинного отделения. Поместите один испытательный щуп на панель машинного отделения, остановите контакт питания на разъеме C14. Поместите другой испытательный щуп на панель машинного отделения, остановите контакт питания на разъеме панели управления. | Сопротивление менее 10 Ом? *Да | 4А |
| Сопротивление менее 10 Ом? **NORepair:** Заменить неисправный провод. См. процедуру[[115-015-024 — Engine Room Panel\|015-024]]. | Ремонт завершён. |  |

### ШАГ 4. Проверьте кабели Панельной системы

#### ШАГ 4A. Проверить панель кабеля машинного отделения

| **Условия:** Отсоединить кабельный разъём С14 от панели машинного отделения Отключить кабельный разъём С7 от окна интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте кабель панели машинного отделения. Установите перемычку между контактом питания переключателя двигателя и контактом питания панели машинного отделения в разъеме C14. Поместите один испытательный щуп в контакт питания переключателя в разъеме C7. Поместите другой испытательный щуп в панель машинного отделения, чтобы остановить контакт питания в разъеме C7. | Сопротивление менее 10 Ом? *Да | 5а |
| Сопротивление менее 10 Ом? **Заменить кабель.** | Ремонт завершён. |  |

#### ШАГ 4B. Проверьте удаленный панельный кабель

| **Условия:** Найти и открыть окно клиентского интерфейса Найти и открыть пульт дистанционного подключения Отключить кабель удаленной панели от окна клиентского интерфейса X4 разъема. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте кабель удаленной панели. Установите перемычку между терминалом питания переключателя удаленной панели и терминалом питания дистанционной панели остановки на панели дистанционного управления X4 в панели дистанционного управления. Поместите один испытательный щуп на провод питания пульта дистанционного управления. Поместите другой испытательный щуп на удаленную панель, остановите подачу провода. | Сопротивление менее 10 Ом? *Да | 5В |
| Сопротивление менее 10 Ом? **Заменить кабель.** | Ремонт завершён. |  |

### ШАГ 5. Проверка проводки интерфейсной коробки заказчика

#### ШАГ 5A. Проверить панель машинного отделения Stop Supply Wire

| **Условия:** Откройте окно интерфейса клиента Отключите кабель машинного отделения на разъеме C7 от окна интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте, чтобы панель машинного отделения не подавала провод. Поместите один испытательный щуп на панель машинного отделения, остановите контакт питания в разъеме C7. Поместите другой испытательный щуп на панель остановки питания машинного отделения на логический блок клиентского интерфейса. | Сопротивление менее 10 Ом? *Да | 2А |
| Сопротивление менее 10 Ом? **NORepair:** Заменить неисправный провод. См. процедуру[[115-015-023 — Customer Interface Box\|015-023]]. | Ремонт завершён. |  |

#### ШАГ 5B. Проверьте удаленную панель Stop Supply Wire

| **Условия:** Откройте окно интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте провод питания дистанционной панели. Поместите один испытательный щуп на удаленную панель остановки проводного терминала в клиентском интерфейсе разъема X4. Поместите другой измерительный щуп на удаленный панель остановки провода на логическом блоке клиентского интерфейса. | Сопротивление менее 10 Ом? **** Заменить логический блок клиентского интерфейса. См. процедуру[[115-015-023 — Customer Interface Box\|015-023]]. | Ремонт завершён. |
| Сопротивление менее 10 Ом? **NORepair:** Заменить провод. См. процедуру[[115-015-023 — Customer Interface Box\|015-023]]. | Ремонт завершён. |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> - Engine will **not** stop when the stop button is pushed at the engine room panel.
>
> - Engine will **not** stop when the stop button is pushed at the remote panel.
>
> ### How To Use This Tree
>
> This symptom tree can be used to troubleshoot engine stop symptoms. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.
>
> ### Shoptalk
>
> The engine can be stopped by pushing the stop button from the engine room panel or remote panel. The panel does **not** need to have start control to stop the engine.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check Engine Room Panel Stop Button |  |
> |  | **STEP 1A.** Check Stop Button Input to Customer Interface Box Logic Unit | Stop lamp illuminated? |
> |  | **STEP 1B.** Check Stop Button Operation | Less than 10 ohms resistance? |
> | STEP 2. | Check Remote Panel Stop Button |  |
> |  | **STEP 2A.** Check Stop Button to Customer Interface Box Logic Unit | Stop lamp illuminated? |
> |  | **STEP 2B.** Check Stop Button Operation | Less than 10 ohms resistance? |
> | STEP 3. | Check Panel Wiring |  |
> |  | **STEP 3A.** Check Engine Room Panel Wiring | Less than 10 ohms resistance? |
> |  | **STEP 3A-1.** Check Engine Room Power Switch Supply Wire | Less than 10 ohms resistance? |
> |  | **STEP 3A-2.** Check Engine Room Panel Stop Supply Wire | Less than 10 ohms resistance? |
> | STEP 4. | Check Panel System Cables |  |
> |  | **STEP 4A.** Check Engine Room Panel Cable | Less than 10 ohms resistance? |
> |  | **STEP 4B.** Check Remote Panel Cable | Less than 10 ohms resistance? |
> | STEP 5. | Check Customer Interface Box Wiring |  |
> |  | **STEP 5A.** Check Engine Room Panel Stop Supply Wire | Less than 10 ohms resistance? |
> |  | **STEP 5B.** Check the Remote Panel Stop Supply Wire | Less than 10 ohms resistance? |
>
> ### STEP 1. Check Engine Room Panel Stop Button
>
> #### STEP 1A. Check Stop Button Input to Customer Interface Box Logic Unit
>
> | **Conditions:** Locate engine room panel Engine room panel power lamp illuminated Open customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check engine stop button input to customer interface box logic unit. Push the stop button. Verify stop lamp is illuminated on the customer interface box logic unit. | Stop lamp illuminated? **YES** | 2A |
> | Stop lamp illuminated? **NO** | 1B |  |
>
> #### STEP 1B. Check Stop Button Operation
>
> | **Conditions:** Open engine room panel Disconnect engine room panel cable connetor from control panel. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the stop button operation. Place one test lead on the engine room panel power switch supply terminal of the control panel connector. Place the other test lead on the engine room panel stop supply terminal of the control panel connector. Press the stop button. | Less than 10 ohms resistance? **YES** | 3A |
> | Less than 10 ohms resistance? **NORepair:** Replace the control panel. Refer to Procedure [[115-015-024 — Engine Room Panel\|015-024]]. | Repair complete. |  |
>
> ### STEP 2. Check Remote Panel Stop Button
>
> #### STEP 2A. Check Stop Button to Customer Interface Box Logic Unit
>
> | **Conditions:** Locate remote panel Remote panel power lamp illuminated Open customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the engine stop button input to customer interface box logic unit. Press the stop button. Verify the stop lamp illuminated on the customer interface box logic unit. | Stop lamp illuminated? **YESRepair:** Replace the customer interface box logic unit. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |
> | Stop lamp illuminated? **NO** | 2B |  |
>
> #### STEP 2B. Check Stop Button Operation
>
> | **Conditions:** Open remote panel Disconnect engine room panel cable connector from the control panel. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the stop button operation. Place one test lead on the remote panel stop supply terminal of the control panel connector. Place the other test lead on the remote panel power switch supply terminal of the control panel connector. Press the stop button. | Less than 10 ohms resistance? **YES** | 4B |
> | Less than 10 ohms resistance? **NORepair:** Replace the control panel. Refer to Procedure [[115-015-025 — Remote Panel\|015-025]]. | Repair complete. |  |
>
> ### STEP 3. Check Panel Wiring
>
> #### STEP 3A. Check Engine Room Panel Wiring
>
> | **Conditions:** Locate engine room panel Open engine room panel door. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check engine room panel wiring. Disconnect cable C14 from the engine room panel. Connect one test lead to the engine room power switch supply pin at the C14 connector. Place the other test lead on the engine room panel stop supply pin at the C14 connector. Press the stop button. | Less than 10 ohms resistance? **YES** | 4A |
> | Less than 10 ohms resistance? **NO** | 3A-1 |  |
>
> #### STEP 3A-1. Check Engine Room Power Switch Supply Wire
>
> | **Conditions:** Locate engine room panel Open engine room panel door. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check wires between harness connector and control panel connector. Disconnect cable C14 from the engine room panel. Place one test lead on the engine room power switch supply pin on connector C14. Place the other test lead on the engine room power switch supply pin on the control panel connector. | Less than 10 ohms resistance? **YES** | 3A-2 |
> | Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-024 — Engine Room Panel\|015-024]]. | Repair complete. |  |
>
> #### STEP 3A-2. Check Engine Room Panel Stop Supply Wire
>
> | **Conditions:** Locate engine room panel Open engine room panel door. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check wires between harness connector and control panel connector. Disconnect cable C14 from the engine room panel. Place one test lead on the engine room panel stop supply pin on the C14 connector. Place the other test lead on the engine room panel stop supply pin on the control panel connector. | Less than 10 ohms resistance? **YES** | 4A |
> | Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-024 — Engine Room Panel\|015-024]]. | Repair complete. |  |
>
> ### STEP 4. Check Panel System Cables
>
> #### STEP 4A. Check Engine Room Panel Cable
>
> | **Conditions:** Disconnect cable connector C14 from the engine room panel Disconnect cable connector C7 from the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check engine room panel cable. Install a jumper between engine room power switch supply pin and the engine room panel stop supply pin in connector C14. Place one test lead in the engine room power switch supply pin in connector C7. Place the other test lead in the engine room panel stop supply pin in connector C7. | Less than 10 ohms resistance? **YES** | 5A |
> | Less than 10 ohms resistance? **NORepair:** Replace the cable. | Repair complete. |  |
>
> #### STEP 4B. Check Remote Panel Cable
>
> | **Conditions:** Locate and open customer interface box Locate and open remote panel Disconnect remote panel cable from customer interface box X4 connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the remote panel cable. Install a jumper between remote panel power switch supply terminal and remote panel stop supply terminal on remote control panel X4 in the remote control panel. Place one test lead on the remote panel power switch supply wire. Place the other test lead on the remote panel stop supply wire. | Less than 10 ohms resistance? **YES** | 5B |
> | Less than 10 ohms resistance? **NORepair:** Replace the cable. | Repair complete. |  |
>
> ### STEP 5. Check Customer Interface Box Wiring
>
> #### STEP 5A. Check Engine Room Panel Stop Supply Wire
>
> | **Conditions:** Open the customer interface box Disconnect engine room cable at connector C7 from the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the engine room panel stop supply wire. Place one test lead on the engine room panel stop supply pin in connector C7. Place the other test lead on the engine room panel stop supply terminal on the customer interface box logic unit. | Less than 10 ohms resistance? **YES** | 2A |
> | Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |  |
>
> #### STEP 5B. Check the Remote Panel Stop Supply Wire
>
> | **Conditions:** Open the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the remote panel stop supply wire. Place one test lead on the remote panel stop supply wire terminal in the customer interface box X4 connector. Place the other test lead on the remote panel stop supply wire terminal on the customer interface box logic unit. | Less than 10 ohms resistance? **YESRepair:** Replace the customer interface box logic unit. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |
> | Less than 10 ohms resistance? **NORepair:** Replace the wire. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |  |
