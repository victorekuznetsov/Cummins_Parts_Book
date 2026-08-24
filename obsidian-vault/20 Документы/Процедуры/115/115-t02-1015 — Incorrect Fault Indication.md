---
aliases:
  - "Неверная индикация неисправности"
type: "Процедура"
doc: "115-t02-1015"
title_en: "Incorrect Fault Indication"
title_ru: "Неверная индикация неисправности"
modified: "2007-01-08"
engines:
  - "41349633"
families:
  - "QSK19"
manuals:
  - "4021587"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/115/115-t02-1015.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/115-t02-1015.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/115"
  - "перевод/машинный"
---

# Incorrect Fault Indication
**Неверная индикация неисправности**

> [!abstract] Процедура · `115-t02-1015`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021587 — C Command Panel System Marine Master Repair Manual|4021587]]
> **Секции:** Section TT — Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2007-01-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/115/115-t02-1015.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/115-t02-1015.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

- Сигнальная лампа ** не** освещается на панели машинного отделения или на удаленной панели при наличии сигнализации.

### Как пользоваться этим деревом

Это дерево симптомов может быть использовано для устранения симптомов неисправности панели. Начните с шага 1 поиска неисправностей. На шаге 2 система задаст ряд вопросов и по симптому выдаст перечень действий по поиску неисправности.

### Практические замечания

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверить индикатор сигнализации панели |  |
|  | **STEP 1A.** Проверить индикатор сигнализации лампы в машинном отделении | Сигнальная лампа подсвечивается? |
|  | **STEP 1B.** Проверить индикатор сигнализации дистанционного управления | Сигнальная лампа подсвечивается? |
| ШАГ 2. | Проверка проводов панели Engine Room |  |
|  | **STEP 2A.** Проверить сигнализацию панели двигателя (Красная лампа) | Сопротивление менее 10 Ом? |
|  | **STEP 2B** Проверить устройство возврата панели машинного отделения | Сопротивление менее 10 Ом? |
| ШАГ 3. | Проверьте кабели Панельной системы |  |
|  | **STEP 3A.** Проверить кабель панели машинного отделения | Сопротивление менее 10 Ом? |
|  | **STEP 3B.** Проверьте кабель дистанционной панели | Сопротивление менее 10 Ом? |
| ШАГ 4. | Проверьте интерфейс клиента |  |
|  | **STEP 4A.** Проверьте сигнализацию панели двигателя (Красная лампа) | Сопротивление менее 10 Ом? |
|  | **STEP 4B.** Проверить сигнализацию удаленной панели (Красная лампа) | Сопротивление менее 10 Ом? |
|  | **STEP 4C** Проверить сигнал красной лампы | Сопротивление менее 10 Ом? |
| ШАГ 5. | Проверьте клиентский интерфейс Box на проводку двигателя с помощью кабеля |  |
|  | **STEP 5A** Проверить сигнал красной лампы | Сопротивление менее 10 Ом? |
| ШАГ 6. | Проверьте клиентский интерфейс Box Logic |  |
|  | **STEP 6A.** Проверить сигнализацию панели двигателя (Красная лампа) | 24 VDC |

### ШАГ 1. Проверить индикатор сигнализации панели

#### ШАГ 1A. Проверьте индикатор сигнализации лампы будильника в машинном отделении

| ** Условия:** Расположение панели машинного отделения |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте, подсвечивается лампа аварийной сигнализации в машинном отделении. | Сигнальная лампа подсвечивается? *Да** | 1В |
| Сигнальная лампа подсвечивается? ** НЕТ** | 2А |  |

#### ШАГ 1B. Проверьте индикатор сигнализации дистанционной панели

| ** Условия:** Расположение удаленной панели |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте, что лампа тревоги удаленной панели освещена. | Сигнальная лампа подсвечивается? *Да** | Ремонт завершён. |
| Сигнальная лампа подсвечивается? ** НЕТ** | 3B |  |

### ШАГ 2. Проверка проводов панели Engine Room

#### ШАГ 2A. Проверка сигнализации панели двигателя (Красная лампа)

| ** Условия: ** Найдите панель машинного отделения Открытая дверь панели машинного отделения. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверяйте провода между разъёмом жгута проводов и разъёмом панели управления. Отсоедините кабель C14 от панели машинного отделения Поместите один испытательный щуп на панельной сигнализации машинного отделения (красная лампа) контакта питания на разъеме C14. Поместите другой испытательный щуп на панель сигнализации машинного отделения (красная лампа) на разъёме панели управления. | Сопротивление менее 10 Ом? *Да** | 2В |
| Сопротивление менее 10 Ом? **NORepair:** Заменить неисправный провод. См. процедуру[[115-015-024 — Engine Room Panel\|015-024]]. | Ремонт завершён. |  |

#### ШАГ 2B. Проверить двигатель комнаты панель возврат провода

| ** Условия: ** Найдите панель машинного отделения Открытая дверь панели машинного отделения. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверяйте провода между разъёмом жгута проводов и разъёмом панели управления. Отсоедините кабель C14 от панели машинного отделения. Поместите один испытательный щуп на панель машинного отделения обратного контакта на разъеме С14. Поместите другой испытательный щуп на панель машинного отделения обратного контакта на разъем панели управления. | Сопротивление менее 10 Ом? *Да** | 3А |
| Сопротивление менее 10 Ом? **NORepair:** Заменить неисправный провод. См. процедуру[[115-015-024 — Engine Room Panel\|015-024]]. | Ремонт завершён. |  |

### ШАГ 3. Проверьте кабели Панельной системы

#### ШАГ 3A. Проверить панель кабеля машинного отделения

| **Условия:** Отсоединить кабельный разъём С14 от панели машинного отделения Отключить кабельный разъём С7 от окна интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте кабель панели машинного отделения. Установите перемычку между контактом питания панели машинного отделения (красная лампа) и обратным контактом панели машинного отделения в разъеме C14. Поместите другой испытательный щуп в панель сигнализации машинного отделения (красная лампа) в разъём C7. Поместите другой испытательный щуп в панель машинного отделения обратного контакта в разъем С7. | Сопротивление менее 10 Ом? *Да** | 4А |
| Сопротивление менее 10 Ом? **Заменить кабель.** | Ремонт завершён. |  |

#### ШАГ 3B. Проверьте удаленный панельный кабель

| **Условия: ** Найти и открыть окно клиентского интерфейса Найти и открыть пульт дистанционного подключения Отключить кабель удаленной панели от окна клиентского интерфейса X4 разъема. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте кабель удаленной панели. Установите перемычку между терминалом подачи сигнализации удаленной панели (красной лампой) и терминалом возврата удаленной панели на панели дистанционного управления X4 в панели дистанционного управления. Поместите один испытательный щуп на провод подачи сигнализации удаленной панели (красная лампа). Поместите другой испытательный щуп на провод возврата удаленной панели. | Сопротивление менее 10 Ом? *Да** | 4B |
| Сопротивление менее 10 Ом? **Заменить кабель.** | Ремонт завершён. |  |

### ШАГ 4. Проверьте интерфейс клиента

#### ШАГ 4A. Проверьте сигнализацию панели двигателя (Красная лампа)

| **Условия: ** Откройте окно интерфейса клиента Отключите кабель машинного отделения на разъеме C7 от окна интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте панель сигнализации машинного отделения (красная лампа) провода питания. Поместите один испытательный щуп на панель сигнализации машинного отделения (красная лампа) в разъём С7. Поместите другой испытательный щуп на панель сигнализации машинного отделения (красная лампа) на логическом блоке клиентского интерфейса. | Сопротивление менее 10 Ом? *Да** | 4C |
| Сопротивление менее 10 Ом? **NORepair:** Заменить неисправный провод. См. процедуру[[115-015-023 — Customer Interface Box\|015-023]]. | Ремонт завершён. |  |

#### ШАГ 4B. Проверить сигнализацию удаленной панели (Красная лампа)

| ** Условия: ** Откройте окно интерфейса клиента |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте провод подачи сигнализации удаленной панели (красная лампа). Поместите один испытательный щуп на терминал подачи проводов дистанционной панели (красная лампа) в разъеме клиентского интерфейса X4. Поместите другой испытательный щуп на терминал подачи сигнализации удаленной панели (красная лампа) блока логики окна интерфейса клиента. | Сопротивление менее 10 Ом? *Да** | 4C |
| Сопротивление менее 10 Ом? **NORepair:** Заменить неисправный провод. См. процедуру[[115-015-023 — Customer Interface Box\|015-023]]. | Ремонт завершён. |  |

#### ШАГ 4C. Проверить сигнал красной лампы

| **Условия: ** Откройте окно интерфейса клиента Отключите окно интерфейса клиента к кабелю ремня электропроводки двигателя на разъеме C3. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте сигнал красной лампы. Поместите один испытательный щуп на контакт сигнала красной лампы в разъём C3. Поместите другой испытательный щуп на сигнальный терминал красной лампы логического блока окна интерфейса клиента. | Сопротивление менее 10 Ом? *Да** | 5а |
| Сопротивление менее 10 Ом? **NORepair:** Заменить неисправный провод. См. процедуру[[115-015-023 — Customer Interface Box\|015-023]]. | Ремонт завершён. |  |

### ШАГ 5. Проверьте клиентский интерфейс Box на проводку двигателя с помощью кабеля

#### ШАГ 5A. Проверить сигнал красной лампы

| **Условия:** Отсоединить кабельный разъём C10 от проводов двигателя упряжкой Отключить кабельный разъём C3 от окна интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте окно интерфейса клиента на проводку двигателя кабеля. Поместите один испытательный щуп в контакт сигнала красной лампы в разъём C10. Поместите другой испытательный щуп в контакт сигнала красной лампы в разъём C3. | Сопротивление менее 10 Ом? *Да** | 6А |
| Сопротивление менее 10 Ом? **Заменить кабель.** | Ремонт завершён. |  |

### ШАГ 6. Проверьте клиентский интерфейс Box Logic

#### ШАГ 6A. Проверка сигнализации панели машинного отделения (Красная лампа)

| **Условия: ** Найти окно клиентского интерфейса Откройте окно клиентского интерфейса. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверить панель сигнализации машинного отделения (красная лампа) на входе в логическую часть клиентского интерфейса составляет 24 VDC. | 24 VDC **YESRepair:** Заменить неисправную панель управления. См. процедуру[[115-015-024 — Engine Room Panel\|015-024]]или[[115-015-025 — Remote Panel\|015-025]]. | Ремонт завершён. |
| 24 VDC **NORepair: ** Заменить логический блок клиентского интерфейса после проверки свойств работы электропроводки и модуля управления двигателем. См. процедуру[[115-015-023 — Customer Interface Box\|015-023]]. | Ремонт завершён. |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> - Alarm lamp is **not** illuminated at the engine room panel or the remote panel when alarm condition is present.
>
> ### How To Use This Tree
>
> This symptom tree can be used to troubleshoot panel fault symptoms. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.
>
> ### Shoptalk
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check Panel Alarm Lamp Indication |  |
> |  | **STEP 1A.** Check Engine Room Panel Alarm Lamp Indication | Alarm lamp illuminated? |
> |  | **STEP 1B.** Check Remote Panel Alarm Lamp Indication | Alarm lamp illuminated? |
> | STEP 2. | Check Engine Room Panel Wiring |  |
> |  | **STEP 2A.** Check Engine Room Panel Alarm (Red Lamp) Supply Wire | Less than 10 ohms resistance? |
> |  | **STEP 2B.** Check Engine Room Panel Return Wire | Less than 10 ohms resistance? |
> | STEP 3. | Check Panel System Cables |  |
> |  | **STEP 3A.** Check Engine Room Panel Cable | Less than 10 ohms resistance? |
> |  | **STEP 3B.** Check Remote Panel Cable | Less than 10 ohms resistance? |
> | STEP 4. | Check Customer Interface Box |  |
> |  | **STEP 4A.** Check the Engine Room Panel Alarm (Red Lamp) Supply Wire | Less than 10 ohms resistance? |
> |  | **STEP 4B.** Check Remote Panel Alarm (Red Lamp) Supply Wire | Less than 10 ohms resistance? |
> |  | **STEP 4C.** Check Red Lamp Signal Wire | Less than 10 ohms resistance? |
> | STEP 5. | Check Customer Interface Box to Engine Harness Cable |  |
> |  | **STEP 5A.** Check Red Lamp Signal Wire | Less than 10 ohms resistance? |
> | STEP 6. | Check Customer Interface Box Logic Unit |  |
> |  | **STEP 6A.** Check Engine Room Panel Alarm (Red Lamp) Supply Terminal | 24 VDC |
>
> ### STEP 1. Check Panel Alarm Lamp Indication
>
> #### STEP 1A. Check Engine Room Panel Alarm Lamp Indication
>
> | **Conditions:** Locate engine room panel |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Verify engine room panel alarm lamp is illuminated. | Alarm lamp illuminated? **YES** | 1B |
> | Alarm lamp illuminated? **NO** | 2A |  |
>
> #### STEP 1B. Check Remote Panel Alarm Lamp Indication
>
> | **Conditions:** Locate remote panel |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Verify remote panel alarm lamp is illuminated. | Alarm lamp illuminated? **YES** | Repair complete. |
> | Alarm lamp illuminated? **NO** | 3B |  |
>
> ### STEP 2. Check Engine Room Panel Wiring
>
> #### STEP 2A. Check Engine Room Panel Alarm (Red Lamp) Supply Wire
>
> | **Conditions:** Locate engine room panel Open engine room panel door. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check wires between harness connector and control panel connector. Disconnect cable C14 from the engine room panel Place one test lead on the engine room panel alarm (red lamp) supply pin on connector C14. Place the other test lead on the engine room panel alarm (red lamp) supply pin on the control panel connector. | Less than 10 ohms resistance? **YES** | 2B |
> | Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-024 — Engine Room Panel\|015-024]]. | Repair complete. |  |
>
> #### STEP 2B. Check Engine Room Panel Return Wire
>
> | **Conditions:** Locate engine room panel Open engine room panel door. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check wires between harness connector and control panel connector. Disconnect cable C14 from the engine room panel. Place one test lead on the engine room panel return pin on connector C14. Place the other test lead on the engine room panel return pin on the control panel connector. | Less than 10 ohms resistance? **YES** | 3A |
> | Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-024 — Engine Room Panel\|015-024]]. | Repair complete. |  |
>
> ### STEP 3. Check Panel System Cables
>
> #### STEP 3A. Check Engine Room Panel Cable
>
> | **Conditions:** Disconnect cable connector C14 from the engine room panel Disconnect cable connector C7 from the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the engine room panel cable. Install a jumper between engine room panel alarm (red lamp) supply pin and the engine room panel return pin in connector C14. Place the other test lead in the engine room panel alarm (red lamp) supply pin in connector C7. Place the other test lead in the engine room panel return pin in connector C7. | Less than 10 ohms resistance? **YES** | 4A |
> | Less than 10 ohms resistance? **NORepair:** Replace the cable. | Repair complete. |  |
>
> #### STEP 3B. Check Remote Panel Cable
>
> | **Conditions:** Locate and open customer interface box Locate and open remote panel Disconnect remote panel cable from customer interface box X4 connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the remote panel cable. Install a jumper between remote panel alarm (red lamp) supply terminal and the remote panel return terminal on the remote control panel X4 in the remote control panel. Place one test lead on the remote panel alarm (red lamp) supply wire. Place the other test lead on the remote panel return wire. | Less than 10 ohms resistance? **YES** | 4B |
> | Less than 10 ohms resistance? **NORepair:** Replace the cable. | Repair complete. |  |
>
> ### STEP 4. Check Customer Interface Box
>
> #### STEP 4A. Check the Engine Room Panel Alarm (Red Lamp) Supply Wire
>
> | **Conditions:** Open the customer interface box Disconnect engine room cable at connector C7 from the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the engine room panel alarm (red lamp) supply wire. Place one test lead on the engine room panel alarm (red lamp) supply pin in connector C7. Place the other test lead on the engine room panel alarm (red lamp) supply terminal on the customer interface box logic unit. | Less than 10 ohms resistance? **YES** | 4C |
> | Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |  |
>
> #### STEP 4B. Check Remote Panel Alarm (Red Lamp) Supply Wire
>
> | **Conditions:** Open the customer interface box |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the remote panel alarm (red lamp) supply wire. Place one test lead on the remote panel alarm (red lamp) supply wire terminal in customer interface box X4 connector. Place the other test lead on the remote panel alarm (red lamp) supply terminal of the customer interface box logic unit. | Less than 10 ohms resistance? **YES** | 4C |
> | Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |  |
>
> #### STEP 4C. Check Red Lamp Signal Wire
>
> | **Conditions:** Open the customer interface box Disconnect the customer interface box to engine harness cable at the C3 connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the red lamp signal wire. Place one test lead on the red lamp signal pin in connector C3. Place the other test lead on the red lamp signal terminal of the customer interface box logic unit. | Less than 10 ohms resistance? **YES** | 5A |
> | Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |  |
>
> ### STEP 5. Check Customer Interface Box to Engine Harness Cable
>
> #### STEP 5A. Check Red Lamp Signal Wire
>
> | **Conditions:** Disconnect cable connector C10 from the engine harness Disconnect cable connector C3 from the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the customer interface box to engine harness cable. Place one test lead in the red lamp signal pin in connector C10. Place the other test lead in the red lamp signal pin in connector C3. | Less than 10 ohms resistance? **YES** | 6A |
> | Less than 10 ohms resistance? **NORepair:** Replace the cable. | Repair complete. |  |
>
> ### STEP 6. Check Customer Interface Box Logic Unit
>
> #### STEP 6A. Check Engine Room Panel Alarm (Red Lamp) Supply Terminal
>
> | **Conditions:** Locate customer interface box Open the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Verify the engine room panel alarm (red lamp) supply terminal of the customer interface box logic unit is 24 VDC. | 24 VDC **YESRepair:** Replace the faulty control panel. Refer to Procedure [[115-015-024 — Engine Room Panel\|015-024]] or [[115-015-025 — Remote Panel\|015-025]]. | Repair complete. |
> | 24 VDC **NORepair:** Replace customer interface box logic unit after verifying on-engine harness and engine control module are operating property. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |  |
