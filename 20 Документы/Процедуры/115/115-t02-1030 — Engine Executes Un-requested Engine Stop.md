---
aliases:
  - "Двигатель самопроизвольно останавливается"
type: "Процедура"
doc: "115-t02-1030"
title_en: "Engine Executes Un-requested Engine Stop"
title_ru: "Двигатель самопроизвольно останавливается"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/115/115-t02-1030.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/115-t02-1030.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/115"
  - "перевод/машинный"
---

# Engine Executes Un-requested Engine Stop
**Двигатель самопроизвольно останавливается**

> [!abstract] Процедура · `115-t02-1030`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021587 — C Command Panel System Marine Master Repair Manual|4021587]]
> **Секции:** Section TT — Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2007-01-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/115/115-t02-1030.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/115-t02-1030.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

- Двигатель выключен без запроса оператора.

### Как пользоваться этим деревом

Это дерево симптомов может быть использовано для устранения симптомов остановки двигателя. Начните с шага 1 поиска неисправностей. На шаге 2 система задаст ряд вопросов и по симптому выдаст перечень действий по поиску неисправности.

### Практические замечания

Перед началом этого дерева устранения неполадок убедитесь, что двигатель не выключен из-за проблем с двигателем, вызванных ECM или механическими проблемами двигателя. Эта процедура устранения неполадок **только **обращается к панели системы.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверить панель машинного отделения |  |
|  | **STEP 1A** Проверить проводку панели машинного отделения | Сопротивление менее 10 Ом? |
|  | **ШАГ 1А-1.** Проверить переключатель зажигания Провода питания | Сопротивление менее 10 Ом? |
|  | **ШАГ 1А-2.** Проверка зажигания (остановка двигателя) Провода питания | Сопротивление менее 10 Ом? |
| ШАГ 2. | Проверьте кабели Панельной системы |  |
|  | **STEP 2A.** Проверить кабель панели машинного отделения | Сопротивление менее 10 Ом? |
| ШАГ 3. | Проверьте интерфейс клиента |  |
|  | **STEP 3A.** Проверьте замок зажигания | Сопротивление менее 10 Ом? |
|  | **STEP 3B.** Проверьте зажигание (остановка двигателя) | Сопротивление менее 10 Ом? |
|  | **STEP 3C** Check Engine Stop Switch (переключатель остановки двигателя) | Сопротивление менее 10 Ом? |
|  | **STEP 3D.** Check Ignition (Engine Stop) - Проводка от переключателя остановки двигателя | Сопротивление менее 10 Ом? |
| ШАГ 4. | Проверьте клиентский интерфейс Box на проводку двигателя с помощью кабеля |  |
|  | **STEP 4A.** Check Ignition (Engine Stop) Проводка для подачи топлива | Сопротивление менее 10 Ом? |

### ШАГ 1. Проверить панель машинного отделения

#### ШАГ 1A. Проверка проводов панели Engine Room

| **Условия: **Найдите панель машинного отделения Открытая дверь панели машинного отделения. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте выключатель питания в машинном отделении. Отсоедините кабель C14 от панели машинного отделения. Отключите разъем панели управления. Поместите один испытательный щуп на выводной клеммой питания переключателя зажигания разъёма панели управления. Поместите другой испытательный щуп на терминал подачи зажигания (остановка двигателя) разъема панели управления. Включи выключатель питания. | Сопротивление менее 10 Ом? *Да | 1А-1-1 |
| Сопротивление менее 10 Ом? **NORepair:** Заменить панель управления. См. процедуру[[115-015-024 — Engine Room Panel\|015-024]]. | Ремонт завершён. |  |

#### ШАГ 1A-1. Проверить переключатель зажигания Провода снабжения

| **Условия: **Найдите панель машинного отделения Открытая дверь панели машинного отделения. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверяйте провода между разъёмом жгута проводов и разъёмом панели управления. Отсоедините кабель C14 от панели машинного отделения. Поместите один испытательный щуп на контакт питания переключателя зажигания на разъём С14. Поместите другой испытательный щуп на контакт питания переключателя зажигания на разъёме панели управления. | Сопротивление менее 10 Ом? *Да | 1А-2 |
| Сопротивление менее 10 Ом? **NORepair:** Заменить неисправный провод. См. процедуру[[115-015-024 — Engine Room Panel\|015-024]]. | Ремонт завершён. |  |

#### ШАГ 1A-2. Проверка зажигания (остановка двигателя) провода питания

| **Условия: **Найдите панель машинного отделения Открытая дверь панели машинного отделения. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверяйте провода между разъёмом жгута проводов и разъёмом панели управления. Отсоедините кабель C14 от панели машинного отделения. Подключите один испытательный щуп на контакт подачи зажигания (остановка двигателя) на разъеме С14. Поместите другой испытательный щуп на контакт подачи зажигания (остановка двигателя) на разъёме панели управления. | Сопротивление менее 10 Ом? *Да | 2А |
| Сопротивление менее 10 Ом? **NORepair:** Заменить неисправный провод. См. процедуру[[115-015-024 — Engine Room Panel\|015-024]]. | Ремонт завершён. |  |

### ШАГ 2. Проверьте кабели Панельной системы

#### ШАГ 2A. Проверить панель кабеля машинного отделения

| **Условия:** Отсоединить кабельный разъём С14 от панели машинного отделения Отключить кабельный разъём С7 от окна интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте кабель панели машинного отделения. Установите перемычку между контактом подачи переключателя зажигания и контактом подачи зажигания (остановка двигателя) в разъёме C14. Поместите один испытательный щуп в контакт питания переключателя зажигания в разъём С7. Поместите другой испытательный щуп в контакт подачи зажигания (остановка двигателя) в разъём C7. | Сопротивление менее 10 Ом? *Да | 3А |
| Сопротивление менее 10 Ом? **Заменить кабель.** | Ремонт завершён. |  |

### ШАГ 3. Проверьте интерфейс клиента

#### ШАГ 3A. Проверьте замок зажигания Проводник питания

| **Условия: **Откройте окно интерфейса клиента Отключите кабель машинного отделения на разъеме C7 от окна интерфейса клиента Отключите окно интерфейса клиента к кабелю упряжки для проводов двигателя на разъеме C1 от окна интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте провод подачи зажигания. Поместите один испытательный щуп на контакт подачи переключателя зажигания в разъём С7. Поместите другой испытательный щуп на терминал подачи переключателя зажигания на логический блок окна интерфейса клиента. | Сопротивление менее 10 Ом? *Да | 3B |
| Сопротивление менее 10 Ом? **NORepair:** Заменить провод с фаутлиной. См. процедуру[[115-015-023 — Customer Interface Box\|015-023]]. | Ремонт завершён. |  |

#### ШАГ 3B. Проверьте подачу сигнала (Engine Stop)

| **Условия: **Откройте окно интерфейса клиента Отключите кабель машинного отделения на разъеме C7 от окна интерфейса клиента Отключите окно интерфейса клиента к кабелю упряжки для проводов двигателя на разъеме C1 от окна интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте подачу зажигания (остановка двигателя) проводом. Поместите один испытательный щуп на контакт подачи зажигания (остановка двигателя) в разъём С7. Поместите другой испытательный щуп на терминал подачи зажигания (остановка двигателя) на выключателе остановки двигателя. | Сопротивление менее 10 Ом? *Да | 3C |
| Сопротивление менее 10 Ом? **NORepair:** Заменить неисправный провод. См. процедуру[[115-015-023 — Customer Interface Box\|015-023]]. | Ремонт завершён. |  |

#### ШАГ 3C. Проверьте переключатель Engine Stop

| **Условия: **Откройте окно клиентского интерфейса Отключить зажигание (остановка двигателя) подводящие провода от переключателя остановки двигателя Отключить окно клиентского интерфейса к проводах двигателя кабель жгута проводов на разъеме С1 от окна клиентского интерфейса. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте выключатель остановки двигателя. Поместите один испытательный щуп на терминал подачи зажигания (остановка двигателя) выключателя остановки двигателя. Поместите другой испытательный щуп на другой стороне стоп-сигнала двигателя на терминал подачи зажигания (остановки двигателя). Убедитесь, что переключатель не задействован. | Сопротивление менее 10 Ом? *Да | 3D |
| Сопротивление менее 10 Ом? **NORepair:** Заменить выключатель остановки двигателя. См. процедуру[[115-015-023 — Customer Interface Box\|015-023]]. | Ремонт завершён. |  |

#### ШАГ 3D. Check Ignition (Engine Stop) - Проводная система от переключателя Engine Stop

| **Условия: **Откройте окно интерфейса клиента Отключите кабель машинного отделения на разъеме C7 от окна интерфейса клиента Отключите окно интерфейса клиента к кабелю упряжки для проводов двигателя на разъеме C1 от окна интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте подачу зажигания (остановка двигателя) проводом. Поместите один испытательный щуп на провод подачи зажигания (остановка двигателя) на выключателе остановки двигателя. Поместите другой испытательный щуп на контакт подачи зажигания (остановка двигателя) в разъем C1 | Сопротивление менее 10 Ом? *Да | 4А |
| Сопротивление менее 10 Ом? **NORepair:** Заменить неисправный провод. См. процедуру[[115-015-023 — Customer Interface Box\|015-023]]. | Ремонт завершён. |  |

### ШАГ 4. Проверьте клиентский интерфейс Box на проводку двигателя с помощью кабеля

#### ШАГ 4A. Проверка зажигания (остановка двигателя) провода питания

| **Условия:** Отсоединить кабельный разъем С1 от окна интерфейса клиента Отключить кабельный разъем С8 от электропроводки двигателя ремня. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверка зажигания (остановка двигателя) провода питания. Поместите один испытательный щуп в контакт подачи зажигания (остановка двигателя) разъема С1. Поместите другой испытательный щуп в контакт подачи зажигания (остановка двигателя) разъема С8. | Сопротивление менее 10 Ом? **YESRepair:** Заменить логический блок клиентского интерфейса после проверки правильности работы электропроводки и модуля управления двигателем. См. процедуру[[115-015-023 — Customer Interface Box\|015-023]]. | Ремонт завершён. |
| Сопротивление менее 10 Ом? **Заменить кабель.** | Ремонт завершён. |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> - The engine shut down without operator request.
>
> ### How To Use This Tree
>
> This symptom tree can be used to troubleshoot engine stop symptoms. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.
>
> ### Shoptalk
>
> Prior to starting this troubleshooting tree, verify the engine did **not** shut down because of ECM generated or mechanical engine problems. This troubleshooting procedure **only** addresses the panel side of the system.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check Engine Room Panel |  |
> |  | **STEP 1A.** Check Engine Room Panel Wiring | Less than 10 ohms resistance? |
> |  | **STEP 1A-1.** Check Keyswitch Supply Wire | Less than 10 ohms resistance? |
> |  | **STEP 1A-2.** Check Ignition (Engine Stop) Supply Wire | Less than 10 ohms resistance? |
> | STEP 2. | Check Panel System Cables |  |
> |  | **STEP 2A.** Check Engine Room Panel Cable | Less than 10 ohms resistance? |
> | STEP 3. | Check Customer Interface Box |  |
> |  | **STEP 3A.** Check the Keyswitch Supply Wire | Less than 10 ohms resistance? |
> |  | **STEP 3B.** Check the Ignition (Engine Stop) Supply Wire | Less than 10 ohms resistance? |
> |  | **STEP 3C.** Check Engine Stop Switch | Less than 10 ohms resistance? |
> |  | **STEP 3D.** Check Ignition (Engine Stop) Supply Wire from Engine Stop Switch | Less than 10 ohms resistance? |
> | STEP 4. | Check Customer Interface Box to Engine Harness Cable |  |
> |  | **STEP 4A.** Check Ignition (Engine Stop) Supply Wire | Less than 10 ohms resistance? |
>
> ### STEP 1. Check Engine Room Panel
>
> #### STEP 1A. Check Engine Room Panel Wiring
>
> | **Conditions:** Locate engine room panel Open engine room panel door. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check engine room panel power switch. Disconnect cable C14 from the engine room panel. Disconnect the control panel connector. Place one test lead on the keyswitch supply terminal of the control panel connector. Place the other test lead on the ignition (engine stop) supply terminal of the control panel connector. Turn on the power switch. | Less than 10 ohms resistance? **YES** | 1A-1 |
> | Less than 10 ohms resistance? **NORepair:** Replace the control panel. Refer to Procedure [[115-015-024 — Engine Room Panel\|015-024]]. | Repair complete. |  |
>
> #### STEP 1A-1. Check Keyswitch Supply Wire
>
> | **Conditions:** Locate engine room panel Open engine room panel door. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check wires between harness connector and control panel connector. Disconnect cable C14 from the engine room panel. Place one test lead on the keyswitch supply pin on connector C14. Place the other test lead on the keyswitch supply pin on the control panel connector. | Less than 10 ohms resistance? **YES** | 1A-2 |
> | Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-024 — Engine Room Panel\|015-024]]. | Repair complete. |  |
>
> #### STEP 1A-2. Check Ignition (Engine Stop) Supply Wire
>
> | **Conditions:** Locate engine room panel Open engine room panel door. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check wires between harness connector and control panel connector. Disconnect cable C14 from the engine room panel. Connect one test lead on the ignition (engine stop) supply pin on the on connector C14. Place the other test lead on the ignition (engine stop) supply pin on the control panel connector. | Less than 10 ohms resistance? **YES** | 2A |
> | Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-024 — Engine Room Panel\|015-024]]. | Repair complete. |  |
>
> ### STEP 2. Check Panel System Cables
>
> #### STEP 2A. Check Engine Room Panel Cable
>
> | **Conditions:** Disconnect cable connector C14 from the engine room panel Disconnect cable connector C7 from the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the engine room panel cable. Install a jumper between keyswitch supply pin and the ignition (engine stop) supply pin in connector C14. Place one test lead in the keyswitch supply pin in connector C7. Place the other test lead in the ignition (engine stop) supply pin in connector C7. | Less than 10 ohms resistance? **YES** | 3A |
> | Less than 10 ohms resistance? **NORepair:** Replace the cable. | Repair complete. |  |
>
> ### STEP 3. Check Customer Interface Box
>
> #### STEP 3A. Check the Keyswitch Supply Wire
>
> | **Conditions:** Open the customer interface box Disconnect engine room cable at connector C7 from the customer interface box Disconnect customer interface box to engine harness cable at connector C1 from the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the keyswitch supply wire. Place one test lead on the keyswitch supply pin in connector C7. Place the other test lead on the keyswitch supply terminal on the customer interface box logic unit. | Less than 10 ohms resistance? **YES** | 3B |
> | Less than 10 ohms resistance? **NORepair:** Replace the fautly wire. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |  |
>
> #### STEP 3B. Check the Ignition (Engine Stop) Supply Wire
>
> | **Conditions:** Open the customer interface box Disconnect engine room cable at connector C7 from the customer interface box Disconnect customer interface box to engine harness cable at connector C1 from the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the ignition (engine stop) supply wire. Place one test lead on the ignition (engine stop) supply pin in connector C7. Place the other test lead on the ignition (engine stop) supply terminal on the engine stop switch. | Less than 10 ohms resistance? **YES** | 3C |
> | Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |  |
>
> #### STEP 3C. Check Engine Stop Switch
>
> | **Conditions:** Open the customer interface box Disconnect ignition (engine stop) supply wires from the engine stop switch Disconnect customer interface box to engine harness cable at connector C1 from the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the engine stop switch. Place one test lead on the ignition (engine stop) supply terminal of the engine stop switch. Place the other test lead on the other side of the engine stop switch at the ignition (engine stop) supply terminal. Make sure the switch is not engaged. | Less than 10 ohms resistance? **YES** | 3D |
> | Less than 10 ohms resistance? **NORepair:** Replace the engine stop switch. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |  |
>
> #### STEP 3D. Check Ignition (Engine Stop) Supply Wire from Engine Stop Switch
>
> | **Conditions:** Open the customer interface box Disconnect engine room cable at connector C7 from the customer interface box Disconnect customer interface box to engine harness cable at connector C1 from the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the ignition (engine stop) supply wire. Place one test lead on the ignition (engine stop) supply wire on the engine stop switch. Place the other test lead on the ignition (engine stop) supply pin in the C1 connector | Less than 10 ohms resistance? **YES** | 4A |
> | Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |  |
>
> ### STEP 4. Check Customer Interface Box to Engine Harness Cable
>
> #### STEP 4A. Check Ignition (Engine Stop) Supply Wire
>
> | **Conditions:** Disconnect cable connector C1 from the customer interface box Disconnect cable connector C8 from the engine harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check ignition (engine stop) supply wire. Place one test lead in the ignition (engine stop) supply pin of the C1 connector. Place the other test lead in the ignition (engine stop) supply pin of the C8 connector. | Less than 10 ohms resistance? **YESRepair:** Replace customer interface box logic unit after verifying on-engine harness and engine control module are operating properly. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |
> | Less than 10 ohms resistance? **NORepair:** Replace the cable. | Repair complete. |  |
