---
aliases:
  - "Индикация тревоги не поступает при её срабатывании"
type: "Процедура"
doc: "115-t02-1010"
title_en: "Alarm Indication Not Received When Alarm Activated"
title_ru: "Индикация тревоги не поступает при её срабатывании"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/115/115-t02-1010.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/115-t02-1010.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/115"
  - "перевод/машинный"
---

# Alarm Indication Not Received When Alarm Activated
**Индикация тревоги не поступает при её срабатывании**

> [!abstract] Процедура · `115-t02-1010`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021587 — C Command Panel System Marine Master Repair Manual|4021587]]
> **Секции:** Section TT — Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2007-01-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/115/115-t02-1010.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/115-t02-1010.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

- Панель машинного отделения или удаленная панель **не** указывают сигнал тревоги при активной работе.

### Как пользоваться этим деревом

Это дерево симптомов может быть использовано для устранения симптомов тревоги двигателя. Начните с шага 1 поиска неисправностей. На шаге 2 система задаст ряд вопросов и по симптому выдаст перечень действий по поиску неисправности.

### Практические замечания

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте клиентский интерфейс Box Logic |  |
|  | **STEP 1A.** Проверьте логику блока интерфейса пользователя Red Lamp | Подсвечивается ли красный индикатор лампы? |
| ШАГ 2. | Проверить Panel Wiring |  |
|  | **STEP 2A** Проверить проводку панели машинного отделения | Светильник подсвечивается? |
|  | **STEP 2A-1.** Проверьте сигнализацию панели двигателя (Красная лампа) | Сопротивление менее 10 Ом? |
|  | **STEP 2A-2.** Проверьте возвратную проводку панели машинного отделения | Сопротивление менее 10 Ом? |
| ШАГ 3. | Проверить панель кабеля машинного отделения |  |
|  | **STEP 3A.** Проверить панельный кабель машинного отделения на открытой схеме | Сопротивление менее 10 Ом? |
| ШАГ 4. | Проверьте интерфейс клиента проводка коробка связана с панелью машинного отделения |  |
|  | **STEP 4A.** Проверить сигнализацию панели двигателя (Красная лампа) | Сопротивление менее 10 Ом? |
|  | **STEP 4B.** Проверьте устройство возврата панели двигателя | Сопротивление менее 10 Ом? |
| ШАГ 5. | Проверьте удаленную панель |  |
|  | **STEP 5A.** Проверьте сигнализацию удаленной панели | Светильник подсвечивается? |
| ШАГ 6. | Проверьте удаленный панельный кабель |  |
|  | **STEP 6A.** Проверьте кабель удаленной панели для открытой схемы | Сопротивление менее 10 Ом? |
| ШАГ 7. | Проверьте интерфейс клиента Box Wiring, связанный с удаленной панелью |  |
|  | **STEP 7A.** Проверьте сигнализацию удаленной панели (Красная лампа) | Сопротивление менее 10 Ом? |
|  | **STEP 7B.** Проверьте удаленную панель | Сопротивление менее 10 Ом? |
| ШАГ 8. | Проверьте интерфейс клиента, связанный с драйвером красной лампы |  |
|  | **ШАГ 8А** Проверьте сигнал красной лампы | Сопротивление менее 10 Ом? |
| ШАГ 9. | Проверьте клиентский интерфейс Box на проводку двигателя с помощью кабеля |  |
|  | **STEP 9A** Проверить сигнал красной лампы | Сопротивление менее 10 Ом? |
| ШАГ 10. | Проверка неисправного компонента |  |
|  | **STEP 10A.** Проверьте блок логики интерфейса клиента и панель управления | Красная лампа подсвечивается? |

### ШАГ 1. Проверьте клиентский интерфейс Box Logic

#### ШАГ 1A. Проверьте индикатор Red Lamp Box Logic Unit

| **Условия:** Найти окно клиентского интерфейса Открытый ящик клиентского интерфейса. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверить, что индикатор красной лампы освещен. | Подсвечивается ли красный индикатор лампы? *Да | 2А |
| Подсвечивается ли красный индикатор лампы? **НЕТ** | 8а |  |

### ШАГ 2. Проверить Panel Wiring

#### ШАГ 2A. Проверка проводов панели Engine Room

| **Условия:** Расположение панели машинного отделения |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверить, не подсвечивается ли сигнализация красной лампы. | Светильник подсвечивается? *Да | 5а |
| Светильник подсвечивается? **НЕТ** | 2А-1-1 |  |

#### ШАГ 2A-1. Проверка сигнализации панели двигателя (Красная лампа)

| **Условия:** Найдите панель машинного отделения Открытая дверь панели машинного отделения. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверяйте провода между разъёмом жгута проводов и разъёмом панели контоля. Отсоедините кабель C14 от панели машинного отделения. Поместите один испытательный щуп на панель сигнализации машинного отделения (красная лампа) на контакт питания на разъеме С14. Поместите другой испытательный щуп на панель сигнализации машинного отделения (красная лампа) на разъёме панели управления. | Сопротивление менее 10 Ом? *Да | 2А-2 |
| Сопротивление менее 10 Ом? **NORepair:** Заменить неисправный провод. См. процедуру[[115-015-024 — Engine Room Panel\|015-024]]. | Ремонт завершён. |  |

#### ШАГ 2A-2. Проверьте панель возврата двигателя

| **Условия:** Найдите панель машинного отделения Открытая дверь панели машинного отделения. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверяйте провода между разъёмом жгута проводов и разъёмом панели управления. Отсоедините кабель C14 от панели машинного отделения. Подключите один испытательный щуп на панели машинного отделения обратного контакта на разъеме С14. Поместите другой испытательный щуп на возвратный терминал панели машинного отделения на разъем панели управления. | Сопротивление менее 10 Ом? *Да | 3А |
| Сопротивление менее 10 Ом? **NORepair:** Заменить провод неисправности. См. процедуру[[115-015-024 — Engine Room Panel\|015-024]]. | Ремонт завершён. |  |

### ШАГ 3. Проверить панель кабеля машинного отделения

#### ШАГ 3A. Проверьте панельный кабель машинного отделения для открытой цепи

| **Условия:** Отсоединить кабельный разъём С14 от панели машинного отделения Отключить кабельный разъём С7 от окна интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте кабель панели машинного отделения. Установите перемычку между контактом питания панели машинного отделения (красная лампа) и контактом обратного питания панели машинного отделения в разъеме C14. Поместите один испытательный щуп в панельной сигнализации машинного отделения (красная лампа) контакта питания в разъем С7. Поместите другой испытательный щуп в панель машинного отделения обратного контакта в разъем С7. | Сопротивление менее 10 Ом? *Да | 4А |
| Сопротивление менее 10 Ом? **Заменить кабель.** | Ремонт завершён. |  |

### ШАГ 4. Проверьте интерфейс клиента проводка коробка связана с панелью машинного отделения

#### ШАГ 4A. Проверка сигнализации панели двигателя (Красная лампа)

| **Условия:** Откройте окно интерфейса клиента Отключите кабель машинного отделения на разъеме C7 от окна интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте панель сигнализации машинного отделения (красная лампа) провода питания. Поместите один испытательный щуп на панель сигнализации машинного отделения (красная лампа) в разъём С7. Поместите другой испытательный щуп на панель сигнализации машинного отделения (красная лампа) на логическом блоке клиентского интерфейса. | Сопротивление менее 10 Ом? *Да | 4B |
| Сопротивление менее 10 Ом? **NORepair:** Заменить неисправный провод. См. процедуру[[115-015-023 — Customer Interface Box\|015-023]]. | Ремонт завершён. |  |

#### ШАГ 4B. Проверьте панель возврата двигателя

| **Условия:** Откройте окно интерфейса клиента Отключите кабель машинного отделения на разъеме C7 от окна интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте провод возврата панели машинного отделения. Поместите один испытательный щуп на панель машинного отделения обратного контакта в разъеме С7. Поместите другой измерительный щуп на обратный контакт напряжения батареи на логическом блоке окна интерфейса клиента. | Сопротивление менее 10 Ом? *Да | 5а |
| Сопротивление менее 10 Ом? **NORepair:** Заменить неисправный провод. См. процедуру[[115-015-023 — Customer Interface Box\|015-023]]. | Ремонт завершён. |  |

### ШАГ 5. Проверьте удаленную панель

#### ШАГ 5A. Проверить лампу дистанционного сигнализации панели

| **Условия:** Расположение удаленной панели. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверить, что красный сигнальный фонарь подсвечивается. | Светильник подсвечивается? *Да | 10А |
| Светильник подсвечивается? **НЕТ** | 6А |  |

### ШАГ 6. Проверьте удаленный панельный кабель

#### ШАГ 6A. Проверить удаленный панельный кабель для открытой схемы

| **Условия:** Найти и открыть окно клиентского интерфейса Отключить кабель удаленной панели от окна клиентского интерфейса X4 Разъем Найти и открыть удаленную панель. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте кабель удаленной панели. Установите перемычку между терминалом подачи сигнализации удаленной панели (красной лампой) и терминалом возврата удаленной панели на панели дистанционного управления X4 в панели дистанционного управления. Поместите один испытательный щуп на терминал подачи сигнализации удаленной панели (красная лампа) в кабель удаленной панели. Поместите другой испытательный щуп на терминал возврата удаленной панели в кабель удаленной панели. | Сопротивление менее 10 Ом? *Да | 7А |
| Сопротивление менее 10 Ом? **Заменить кабель.** | Ремонт завершён. |  |

### ШАГ 7. Проверьте интерфейс клиента Box Wiring, связанный с удаленной панелью

#### ШАГ 7A. Проверьте сигнализацию удаленной панели (Красная лампа)

| **Условия:** Откройте окно интерфейса клиента Отключите кабель машинного отделения на разъеме C7 от окна интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте провод подачи сигнализации удаленной панели (красная лампа). Поместите один испытательный щуп на пульт дистанционного управления сигнализацией (красная лампа) на выходе из терминала полосы X4. Поместите другой испытательный щуп на терминал подачи сигнализации удаленной панели (красная лампа) в логический блок окна интерфейса клиента. | Сопротивление менее 10 Ом? *Да | 7B |
| Сопротивление менее 10 Ом? **NORepair:** Заменить неисправный провод. См. процедуру[[115-015-023 — Customer Interface Box\|015-023]]. | Ремонт завершён. |  |

#### ШАГ 7B. Проверить Remote Panel Return Wire

| **Условия:** Откройте окно интерфейса клиента Отключите кабель машинного отделения на разъеме C7 от окна интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте провод возврата удаленной панели. Поместите один испытательный щуп на удаленный панель возвратного терминала терминальной полосы X4. Поместите другой измерительный щуп на терминал возврата удаленной панели на логический блок окна интерфейса клиента. | Сопротивление менее 10 Ом? *Да | 10А |
| Сопротивление менее 10 Ом? **NORepair:** Заменить неисправный провод. См. процедуру[[115-015-023 — Customer Interface Box\|015-023]]. | Ремонт завершён. |  |

### ШАГ 8. Проверьте интерфейс клиента, связанный с драйвером красной лампы

#### ШАГ 8A. Проверить сигнал красной лампы

| **Условия:** Отключить кабельный разъем C3 от окна интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте сигнал красной лампы. Поместите один испытательный щуп на контакт сигнала красной лампы на разъеме C3. Поместите другой испытательный щуп в сигнальный терминал красной лампы логического блока окна интерфейса клиента. | Сопротивление менее 10 Ом? *Да | 9а |
| Сопротивление менее 10 Ом? **NORepair:** Заменить неисправный провод. См. процедуру[[115-015-023 — Customer Interface Box\|015-023]]. | Ремонт завершён. |  |

### ШАГ 9. Проверьте клиентский интерфейс Box на проводку двигателя с помощью кабеля

#### ШАГ 9A. Проверить сигнал красной лампы

| **Условия:** Отсоединить кабельный разъем С1 от окна интерфейса клиента Отключить кабельный разъем С8 от электропроводки двигателя ремня. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте сигнал красной лампы. Установите перемычку между контактом сигнала красной лампы и возвратным штифтом уровня 1 охлаждающей жидкости (охлажденный киль) (датчик возврата 1) в разъеме C8. Поместите один испытательный щуп в контакт красной лампы с разъемом C1. Поместите другой испытательный щуп в штырь разъема С1 охлаждающей жидкости 1 (охлажденный килем) возврата (датчик возврата 1). | Сопротивление менее 10 Ом? *Да | 10А |
| Сопротивление менее 10 Ом? **Заменить кабель.** | Ремонт завершён. |  |

### ШАГ 10. Проверка неисправного компонента

#### ШАГ 10A. Проверьте клиентский интерфейс Box Logic Unit и панель управления

| **Условия:** Открытый интерфейс клиента Убедитесь, что все кабели системы панели подключены. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте индикатор красной лампы на логическом блоке клиентского интерфейса. | Красная лампа подсвечивается? * Заменить панель управления. См. процедуру[[115-015-024 — Engine Room Panel\|015-024]]или[[115-015-025 — Remote Panel\|015-025]]. | Ремонт завершён. |
| Красная лампа подсвечивается? **NORepair:** Заменить логический блок коробки интерфейса клиента после проверки правильности работы электропроводки и модуля управления двигателем. См. процедуру[[115-015-024 — Engine Room Panel\|015-024]]. | Ремонт завершён. |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> - The engine room panel or remote panel does **not** indicate an alarm when active.
>
> ### How To Use This Tree
>
> This symptom tree can be used to troubleshoot engine alarm symptoms. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.
>
> ### Shoptalk
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check Customer Interface Box Logic Unit |  |
> |  | **STEP 1A.** Check Customer Interface Box Logic Unit Red Lamp Indicator | Is red lamp indicator illuminated? |
> | STEP 2. | Check Panel Wiring |  |
> |  | **STEP 2A.** Check Engine Room Panel Wiring | Is alarm lamp illuminated? |
> |  | **STEP 2A-1.** Check Engine Room Panel Alarm (Red Lamp) Supply Wire | Less than 10 ohms resistance? |
> |  | **STEP 2A-2.** Check the Engine Room Panel Return Wire | Less than 10 ohms resistance? |
> | STEP 3. | Check Engine Room Panel Cable |  |
> |  | **STEP 3A.** Check Engine Room Panel Cable for Open Circuit | Less than 10 ohms resistance? |
> | STEP 4. | Check Customer Interface Box Wiring Associated with Engine Room Panel |  |
> |  | **STEP 4A.** Check Engine Room Panel Alarm (Red Lamp) Supply Wire | Less than 10 ohms resistance? |
> |  | **STEP 4B.** Check the Engine Room Panel Return Wire | Less than 10 ohms resistance? |
> | STEP 5. | Check Remote Panel |  |
> |  | **STEP 5A.** Check Remote Panel Alarm Lamp | Is alarm lamp illuminated? |
> | STEP 6. | Check Remote Panel Cable |  |
> |  | **STEP 6A.** Check Remote Panel Cable for Open Circuit | Less than 10 ohms resistance? |
> | STEP 7. | Check Customer Interface Box Wiring Associated with Remote Panel |  |
> |  | **STEP 7A.** Check the Remote Panel Alarm (Red Lamp) Supply Wire | Less than 10 ohms resistance? |
> |  | **STEP 7B.** Check the Remote Panel Return Wire | Less than 10 ohms resistance? |
> | STEP 8. | Check Customer Interface Box Wiring Associated with Red Lamp Driver |  |
> |  | **STEP 8A.** Check Red Lamp Signal Wire | Less than 10 ohms resistance? |
> | STEP 9. | Check Customer Interface Box to Engine Harness Cable |  |
> |  | **STEP 9A.** Check Red Lamp Signal Wire | Less than 10 ohms resistance? |
> | STEP 10. | Check For Failed Component |  |
> |  | **STEP 10A.** Check Customer Interface Box Logic Unit and Control Panel | Red lamp illuminated? |
>
> ### STEP 1. Check Customer Interface Box Logic Unit
>
> #### STEP 1A. Check Customer Interface Box Logic Unit Red Lamp Indicator
>
> | **Conditions:** Locate customer interface box Open customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Verify red lamp indicator is illuminated. | Is red lamp indicator illuminated? **YES** | 2A |
> | Is red lamp indicator illuminated? **NO** | 8A |  |
>
> ### STEP 2. Check Panel Wiring
>
> #### STEP 2A. Check Engine Room Panel Wiring
>
> | **Conditions:** Locate engine room panel |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Verify alarm red lamp is illumintated. | Is alarm lamp illuminated? **YES** | 5A |
> | Is alarm lamp illuminated? **NO** | 2A-1 |  |
>
> #### STEP 2A-1. Check Engine Room Panel Alarm (Red Lamp) Supply Wire
>
> | **Conditions:** Locate engine room panel Open engine room panel door. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check wires between harness connector and contol panel connector. Disconnect cable C14 from the engine room panel. Place one test lead on the engine room panel alarm (red lamp) supply pin on connector C14. Place the other test lead on the engine room panel alarm (red lamp) supply pin on the control panel connector. | Less than 10 ohms resistance? **YES** | 2A-2 |
> | Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-024 — Engine Room Panel\|015-024]]. | Repair complete. |  |
>
> #### STEP 2A-2. Check the Engine Room Panel Return Wire
>
> | **Conditions:** Locate engine room panel Open engine room panel door. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check wires between harness connector and control panel connector. Disconnect cable C14 from the engine room panel. Connect one test lead on the engine room panel return pin on the on connector C14. Place the other test lead on the engine room panel return terminal on the control panel connector. | Less than 10 ohms resistance? **YES** | 3A |
> | Less than 10 ohms resistance? **NORepair:** Replace the fault wire. Refer to Procedure [[115-015-024 — Engine Room Panel\|015-024]]. | Repair complete. |  |
>
> ### STEP 3. Check Engine Room Panel Cable
>
> #### STEP 3A. Check Engine Room Panel Cable for Open Circuit
>
> | **Conditions:** Disconnect cable connector C14 from the engine room panel Disconnect cable connector C7 from the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the engine room panel cable. Install a jumper between engine room panel alarm (red lamp) supply pin and the engine room panel return supply pin in connector C14. Place one test lead in the engine room panel alarm (red lamp) supply pin in connector C7. Place the other test lead in the engine room panel return pin in connector C7. | Less than 10 ohms resistance? **YES** | 4A |
> | Less than 10 ohms resistance? **NORepair:** Replace the cable. | Repair complete. |  |
>
> ### STEP 4. Check Customer Interface Box Wiring Associated with Engine Room Panel
>
> #### STEP 4A. Check Engine Room Panel Alarm (Red Lamp) Supply Wire
>
> | **Conditions:** Open the customer interface box Disconnect engine room cable at connector C7 from the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the engine room panel alarm (red lamp) supply wire. Place one test lead on the engine room panel alarm (red lamp) supply pin in connector C7. Place the other test lead on the engine room panel alarm (red lamp) supply terminal on the customer interface box logic unit. | Less than 10 ohms resistance? **YES** | 4B |
> | Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |  |
>
> #### STEP 4B. Check the Engine Room Panel Return Wire
>
> | **Conditions:** Open the customer interface box Disconnect engine room cable at connector C7 from the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the engine room panel return wire. Place one test lead on the engine room panel return pin in connector C7. Place the other test lead on the battery voltage return pin on the customer interface box logic unit. | Less than 10 ohms resistance? **YES** | 5A |
> | Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |  |
>
> ### STEP 5. Check Remote Panel
>
> #### STEP 5A. Check Remote Panel Alarm Lamp
>
> | **Conditions:** Locate remote panel. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Verify red alarm lamp is illuminated. | Is alarm lamp illuminated? **YES** | 10A |
> | Is alarm lamp illuminated? **NO** | 6A |  |
>
> ### STEP 6. Check Remote Panel Cable
>
> #### STEP 6A. Check Remote Panel Cable for Open Circuit
>
> | **Conditions:** Locate and open customer interface box Disconnect remote panel cable from customer interface box X4 connector Locate and open remote panel. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the remote panel cable. Install a jumper between remote panel alarm (red lamp) supply terminal and the remote panel return terminal on remote control panel X4 in the remote control panel. Place one test lead on the remote panel alarm (red lamp) supply terminal in the remote panel cable. Place the other test lead on the remote panel return terminal in the remote panel cable. | Less than 10 ohms resistance? **YES** | 7A |
> | Less than 10 ohms resistance? **NORepair:** Replace the cable. | Repair complete. |  |
>
> ### STEP 7. Check Customer Interface Box Wiring Associated with Remote Panel
>
> #### STEP 7A. Check the Remote Panel Alarm (Red Lamp) Supply Wire
>
> | **Conditions:** Open the customer interface box Disconnect engine room cable at connector C7 from the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the remote panel alarm (red lamp) supply wire. Place one test lead on the remote panel alarm (red lamp) supply terminal of terminal strip X4. Place the other test lead on the remote panel alarm (red lamp) supply terminal in the customer interface box logic unit. | Less than 10 ohms resistance? **YES** | 7B |
> | Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |  |
>
> #### STEP 7B. Check the Remote Panel Return Wire
>
> | **Conditions:** Open the customer interface box Disconnect engine room cable at connector C7 from the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the remote panel return wire. Place one test lead on the remote panel return terminal of terminal strip X4. Place the other test lead on the remote panel return terminal on the customer interface box logic unit. | Less than 10 ohms resistance? **YES** | 10A |
> | Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |  |
>
> ### STEP 8. Check Customer Interface Box Wiring Associated with Red Lamp Driver
>
> #### STEP 8A. Check Red Lamp Signal Wire
>
> | **Conditions:** Disconnect cable connector C3 from the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check red lamp signal wire. Place one test lead on the red lamp signal pin at the C3 connector. Place the other test lead in the red lamp signal terminal of the customer interface box logic unit. | Less than 10 ohms resistance? **YES** | 9A |
> | Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |  |
>
> ### STEP 9. Check Customer Interface Box to Engine Harness Cable
>
> #### STEP 9A. Check Red Lamp Signal Wire
>
> | **Conditions:** Disconnect cable connector C1 from the customer interface box Disconnect cable connector C8 from the engine harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check red lamp signal wire. Install a jumper between red lamp signal pin and coolant level 1 (keel cooled) return (sensor return 1) pin in the C8 connector. Place one test lead in the red lamp signal pin of the C1 connector. Place the other test lead in the coolant level 1 (keel cooled) return (sensor return 1) pin of the C1 connector. | Less than 10 ohms resistance? **YES** | 10A |
> | Less than 10 ohms resistance? **NORepair:** Replace the cable. | Repair complete. |  |
>
> ### STEP 10. Check For Failed Component
>
> #### STEP 10A. Check Customer Interface Box Logic Unit and Control Panel
>
> | **Conditions:** Open customer interface box Make sure all panel system cables are connected. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check red lamp indicator on customer interface box logic unit. | Red lamp illuminated? **YESRepair:** Replace control panel. Refer to Procedure [[115-015-024 — Engine Room Panel\|015-024]] or [[115-015-025 — Remote Panel\|015-025]]. | Repair complete. |
> | Red lamp illuminated? **NORepair:** Replace the customer interface box logic unit after verifying on-engine harness and engine control module are operating properly. Refer to Procedure [[115-015-024 — Engine Room Panel\|015-024]]. | Repair complete. |  |
