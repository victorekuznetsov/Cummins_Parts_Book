---
aliases:
  - "Индикация неисправности ЭБУ не отображается"
type: "Процедура"
doc: "115-t02-1012"
title_en: "ECM Fault Indication Not Indicated"
title_ru: "Индикация неисправности ЭБУ не отображается"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/115/115-t02-1012.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/115-t02-1012.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/115"
  - "перевод/машинный"
---

# ECM Fault Indication Not Indicated
**Индикация неисправности ЭБУ не отображается**

> [!abstract] Процедура · `115-t02-1012`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021587 — C Command Panel System Marine Master Repair Manual|4021587]]
> **Секции:** Section TT — Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2007-01-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/115/115-t02-1012.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/115-t02-1012.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

- Панель машинного отделения ED3 или удаленная панель ED3 или датчики **не** указывают на неисправности, потому что она **не** имеет мощность.

- Подсвечивается панель машинного отделения и пультовые лампы питания.

- У ECM есть активные дефекты.

### Как пользоваться этим деревом

Это дерево симптомов может быть использовано для устранения симптомов, связанных с признаками неисправности. Начните с шага 1 поиска неисправностей. На шаге 2 система задаст ряд вопросов и по симптому выдаст перечень действий по поиску неисправности.

### Практические замечания

Шина данных SAE J1939 CAN передает сигнал тревоги, генерируемый ECM, в окно интерфейса клиента. Коробка интерфейса клиента передает информацию о тревоге на ED3 на панели машинного отделения и ED3 или датчиках в удаленной панели (панелях).

Это дерево обращается к ED3 или датчикам питания и возврата.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверить Panel Wiring |  |
|  | **STEP 1A** Проверить проводку панели машинного отделения | ED3 указывает на ошибку(ы)? |
|  | **STEP 1A-1.** Проверить питание коммутатора двигателя (C14 Connector to Control Panel Connector) | Сопротивление менее 10 Ом? |
|  | **STEP 1A-2.** Проверить щиток питания переключателя питания в машинном отделении (C14 Connector to Instrument Panel Connector) | Сопротивление менее 10 Ом? |
|  | **STEP 1A-3.** Проверьте возвратную проводку панели машинного отделения (подключатель C14 к разъему панели управления) | Сопротивление менее 10 Ом? |
|  | **STEP 1A-4.** Проверка возврата провода панели машинного отделения (C14 Connector to Instrument Panel Connector) | Сопротивление менее 10 Ом? |
|  | **STEP 1B.** Проверьте проводку удаленной панели | ED3 или датчики указывают на неисправность (неисправности)? |
|  | **STEP 1B-1.** Проверьте провода питания коммутатора удаленной панели | Сопротивление менее 10 Ом? |
|  | **STEP 1B-2.** Проверьте удаленную панель возврата провода | Сопротивление менее 10 Ом? |
| ШАГ 2. | Проверьте кабели Панельной системы |  |
|  | **STEP 2A.** Проверить кабель панели машинного отделения | Сопротивление менее 10 Ом? |
|  | **STEP 2B.** Проверьте кабель дистанционной панели | Сопротивление менее 10 Ом? |
| ШАГ 3. | Проверка проводки интерфейсной коробки заказчика |  |
|  | **STEP 3A.** Проверьте машинное отделение и провода для коммутатора дистанционного питания | Сопротивление менее 10 Ом? |
|  | **STEP 3B.** Проверьте возврат провода в панели машинного отделения | Сопротивление менее 10 Ом? |

### ШАГ 1. Проверить Panel Wiring

#### ШАГ 1A. Проверка проводов панели Engine Room

| **Условия:** Расположение панели машинного отделения |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте ED3 дисплей для выявления неисправностей. | ED3 указывает на ошибку(ы)? *Да | 1В |
| ED3 указывает на ошибку(ы)? **НЕТ** | 1А-1-1 |  |

#### ШАГ 1A-1. Проверка коммутатора питания в машинном отделении (C14 Connector to Control Panel Connector)

| **Условия:** Найдите панель машинного отделения Открытая дверь панели машинного отделения. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверяйте провода между разъёмом жгута проводов и разъёмом панели управления. Отсоедините кабель C14 от панели машинного отделения. Поместите один испытательный щуп на контакт питания переключателя двигателя в разъеме C14. Поместите другой испытательный щуп на контакт питания переключателя в машинном отделении на разъем панели управления. | Сопротивление менее 10 Ом? *Да | 1А-2 |
| Сопротивление менее 10 Ом? **NORepair:** Заменить неисправный провод. См. процедуру[[115-015-024 — Engine Room Panel\|015-024]]. | Ремонт завершён. |  |

#### ШАГ 1A-2. Проверить панель питания коммутатора двигателя (C14 Connector to Instrument Panel Connector)

| **Условия:** Найдите панель машинного отделения Открытая дверь панели машинного отделения. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте проводку панели машинного отделения. Отсоедините кабель C14 от панели машинного отделения. Поместите один испытательный щуп на контакт питания переключателя двигателя в разъеме C14. Поместите другой испытательный щуп на провод питания переключателя питания в машинном отделении на разъем панели приборов. | Сопротивление менее 10 Ом? *Да | 1А-3 |
| Сопротивление менее 10 Ом? **NORepair:** Заменить неисправный провод. См. процедуру[[115-015-024 — Engine Room Panel\|015-024]]. | Ремонт завершён. |  |

#### ШАГ 1A-3. Проверить возвратный провод панели машинного отделения (C14 Connector to Control Panel Connector)

| **Условия:** Найдите панель машинного отделения Открытая дверь панели машинного отделения. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверяйте провода между разъёмом жгута проводов и разъемом панели управления. Отсоедините кабель C14 от панели машинного отделения. Поместите один испытательный щуп на панель машинного отделения обратного контакта на разъем С14. Поместите другой испытательный щуп на панель машинного отделения обратного контакта на разъем панели управления. | Сопротивление менее 10 Ом? *Да | 1А-4 |
| Сопротивление менее 10 Ом? **NORepair:** Заменить неисправный провод. См. процедуру[[115-015-024 — Engine Room Panel\|015-024]]. | Ремонт завершён. |  |

#### ШАГ 1A-4. Проверка возврата провода панели машинного отделения (C14 Connector to Instrument Panel Connector)

| **Условия:** Найдите панель машинного отделения Открытая дверь панели машинного отделения. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте проводку панели машинного отделения. Отсоедините кабель C14 от панели машинного отделения. Поместите один испытательный щуп на панель машинного отделения обратного контакта на разъеме С14. Поместите другой испытательный щуп на разъём панели приборной панели возвратного проволоки машинного отделения. | Сопротивление менее 10 Ом? *Да | 2А |
| Сопротивление менее 10 Ом? **NORepair:** Заменить неисправный провод. См. процедуру[[115-015-024 — Engine Room Panel\|015-024]]. | Ремонт завершён. |  |

#### ШАГ 1B. Проверьте удаленную панель Wiring

| **Условия:** Расположение панели машинного отделения |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте дисплей для указания неисправностей. | ED3 или датчики указывают на неисправность (неисправности)? *Да | Ремонт завершён. |
| ED3 или датчики указывают на неисправность (неисправности)? **НЕТ** | 1В-1-1 |  |

#### ШАГ 1B-1. Проверьте удаленный коммутатор питания панели Wire

| **Условия:** Расположение пульта Удалённая панель Открытая пульт дистанционного управления. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте удаленную проводку панели. Поместите один испытательный щуп на терминал питания пульта дистанционного питания разъема X4. Поместите другой испытательный щуп на провод питания переключателя питания на дисплее. | Сопротивление менее 10 Ом? *Да | 1В-2-2 |
| Сопротивление менее 10 Ом? **NORepair:** Заменить неисправный провод. См. процедуру[[115-015-025 — Remote Panel\|015-025]]. | Ремонт завершён. |  |

#### ШАГ 1B-2. Проверить удаленную панель Return Wire

| **Условия:** Расположение пульта Удалённая панель Открытая пульт дистанционного управления. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте удаленную проводку панели. Поместите один испытательный щуп на удаленный панельный терминал возврата разъема X4. Поместите другой испытательный щуп на провод возврата удаленной панели на дисплее. | Сопротивление менее 10 Ом? *Да | 2В |
| Сопротивление менее 10 Ом? **NORepair:** Заменить неисправный провод. См. процедуру[[115-015-025 — Remote Panel\|015-025]]. | Ремонт завершён. |  |

### ШАГ 2. Проверьте кабели Панельной системы

#### ШАГ 2A. Проверить панель кабеля машинного отделения

| **Условия:** Отсоединить кабельный разъём С14 от панели машинного отделения Отключить кабельный разъём С7 от окна интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте кабель панели машинного отделения. Установите перемычку между контактом питания переключателя двигателя и обратным контактом машинного отделения в разъеме C14. Поместите один испытательный щуп в контакт питания переключателя в разъеме C7. Поместите другой испытательный щуп в машинное отделение обратного контакта в разъем С7. | Сопротивление менее 10 Ом? *Да | 3А |
| Сопротивление менее 10 Ом? **Заменить кабель.** | Ремонт завершён. |  |

#### ШАГ 2B. Проверьте удаленный панельный кабель

| **Условия:** Найти и открыть окно интерфейса клиента Найти и открыть удаленную панель Отключить кабель удаленной панели от разъема интерфейса клиента X4. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте кабель удаленной панели. Установите перемычку между терминалом питания переключателя удаленной панели и терминалом возврата удаленной панели на панели дистанционного управления X4 в панели дистанционного управления. Поместите один испытательный щуп на терминал питания пульта дистанционного питания кабеля дистанционного управления. Поместите другой испытательный щуп на терминал возврата удаленной панели кабеля удаленной панели. | Сопротивление менее 10 Ом? *Да | 3А |
| Сопротивление менее 10 Ом? **Заменить кабель.** | Ремонт завершён. |  |

### ШАГ 3. Проверка проводки интерфейсной коробки заказчика

#### ШАГ 3A. Проверьте машинное отделение и провода для дистанционного питания коммутатора

| **Условия:** Откройте окно интерфейса клиента Отключите кабель машинного отделения на разъеме C7 от окна интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте провод питания выключателя двигателя. Поместите один испытательный щуп на контакт питания переключателя в разъеме C7. Поместите другой измерительный щуп на удаленную панель обратного контакта на полосе терминала клиентского интерфейса X4. | Сопротивление менее 10 Ом? *Да | 3B |
| Сопротивление менее 10 Ом? **NORepair:** Заменить неисправный провод. См. процедуру[[115-015-023 — Customer Interface Box\|015-023]]. | Ремонт завершён. |  |

#### ШАГ 3B. Проверьте панель возврата двигателя

| **Условия:** Откройте окно интерфейса клиента Отключите кабель машинного отделения на разъеме C7 от окна интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте провод возврата панели машинного отделения. Поместите один испытательный щуп на панель машинного отделения обратного контакта в разъеме С7. Поместите другой измерительный щуп на удаленную панель обратного контакта на полосе терминала клиентского интерфейса X4. | Сопротивление менее 10 Ом? *** Ремонт:** Заменить неисправный дисплей. См. процедуру[[115-015-024 — Engine Room Panel\|015-024]]или[[115-015-025 — Remote Panel\|015-025]]. | Ремонт завершён. |
| Сопротивление менее 10 Ом? **NORepair:** Заменить неисправный провод. См. процедуру[[115-015-023 — Customer Interface Box\|015-023]]. | Ремонт завершён. |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> - The engine room panel ED3 or remote panel ED3 or gauges does **not** indicate faults because it does **not** have power.
>
> - The engine room panel and remote panel power lamps are illuminated.
>
> - The ECM has active faults.
>
> ### How To Use This Tree
>
> This symptom tree can be used to troubleshoot fault indication related symptoms. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.
>
> ### Shoptalk
>
> The SAE J1939 datalink delivers alarm information, generated by the ECM, to the customer interface box. The customer interface box transfers alarm information to the ED3 on the engine room panel and ED3 or gauges in the remote panel(s).
>
> This tree addresses the ED3 or gauges power supply and return.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check Panel Wiring |  |
> |  | **STEP 1A.** Check Engine Room Panel Wiring | ED3 indicate fault(s)? |
> |  | **STEP 1A-1.** Check Engine Room Power Switch Supply Wire (C14 Connector to Control Panel Connector) | Less than 10 ohms resistance? |
> |  | **STEP 1A-2.** Check Engine Room Panel Power Switch Supply Wire (C14 Connector to Instrument Panel Connector) | Less than 10 ohms resistance? |
> |  | **STEP 1A-3.** Check the Engine Room Panel Return Wire (C14 Connector to Control Panel Connector) | Less than 10 ohms resistance? |
> |  | **STEP 1A-4.** Check Engine Room Panel Return Wire (C14 Connector to Instrument Panel Connector) | Less than 10 ohms resistance? |
> |  | **STEP 1B.** Check Remote Panel Wiring | ED3 or gauges indicate fault(s)? |
> |  | **STEP 1B-1.** Check Remote Panel Power Switch Supply Wire | Less than 10 ohms resistance? |
> |  | **STEP 1B-2.** Check Remote Panel Return Wire | Less than 10 ohms resistance? |
> | STEP 2. | Check Panel System Cables |  |
> |  | **STEP 2A.** Check Engine Room Panel Cable | Less than 10 ohms resistance? |
> |  | **STEP 2B.** Check Remote Panel Cable | Less than 10 ohms resistance? |
> | STEP 3. | Check Customer Interface Box Wiring |  |
> |  | **STEP 3A.** Check the Engine Room and Remote Power Switch Supply Wire | Less than 10 ohms resistance? |
> |  | **STEP 3B.** Check the Engine Room Panel Return Wire | Less than 10 ohms resistance? |
>
> ### STEP 1. Check Panel Wiring
>
> #### STEP 1A. Check Engine Room Panel Wiring
>
> | **Conditions:** Locate engine room panel |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check ED3 display for indication of faults. | ED3 indicate fault(s)? **YES** | 1B |
> | ED3 indicate fault(s)? **NO** | 1A-1 |  |
>
> #### STEP 1A-1. Check Engine Room Power Switch Supply Wire (C14 Connector to Control Panel Connector)
>
> | **Conditions:** Locate engine room panel Open engine room panel door. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check wires between harness connector and control panel connector. Disconnect cable C14 from the engine room panel. Place one test lead on the engine room power switch supply pin on connector C14. Place the other test lead on the engine room power switch supply pin on the control panel connector. | Less than 10 ohms resistance? **YES** | 1A-2 |
> | Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-024 — Engine Room Panel\|015-024]]. | Repair complete. |  |
>
> #### STEP 1A-2. Check Engine Room Panel Power Switch Supply Wire (C14 Connector to Instrument Panel Connector)
>
> | **Conditions:** Locate engine room panel Open engine room panel door. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check engine room panel wiring. Disconnect cable C14 from the engine room panel. Place one test lead on the engine room power switch supply pin on the C14 connector. Place the other test lead on the engine room power switch supply wire at the instrument panel connector. | Less than 10 ohms resistance? **YES** | 1A-3 |
> | Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-024 — Engine Room Panel\|015-024]]. | Repair complete. |  |
>
> #### STEP 1A-3. Check the Engine Room Panel Return Wire (C14 Connector to Control Panel Connector)
>
> | **Conditions:** Locate engine room panel Open engine room panel door. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check wires between harness connector and econtrol panel connector. Disconnect cable C14 from the engine room panel. Place one test lead on the engine room panel return pin on the on connector C14. Place the other test lead on the engine room panel return pin on the control panel connector. | Less than 10 ohms resistance? **YES** | 1A-4 |
> | Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-024 — Engine Room Panel\|015-024]]. | Repair complete. |  |
>
> #### STEP 1A-4. Check Engine Room Panel Return Wire (C14 Connector to Instrument Panel Connector)
>
> | **Conditions:** Locate engine room panel Open engine room panel door. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check engine room panel wiring. Disconnect cable C14 from the engine room panel. Place one test lead on the engine room panel return pin on the C14 connector. Place the other test lead on the engine room panel return wire instrument panel connector. | Less than 10 ohms resistance? **YES** | 2A |
> | Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-024 — Engine Room Panel\|015-024]]. | Repair complete. |  |
>
> #### STEP 1B. Check Remote Panel Wiring
>
> | **Conditions:** Locate engine room panel |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check display for indication of faults. | ED3 or gauges indicate fault(s)? **YES** | Repair complete. |
> | ED3 or gauges indicate fault(s)? **NO** | 1B-1 |  |
>
> #### STEP 1B-1. Check Remote Panel Power Switch Supply Wire
>
> | **Conditions:** Locate remote panel Open remote panel. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check remote panel wiring. Place one test lead on the remote panel power switch supply terminal of the X4 connector. Place the other test lead on the power switch supply wire at the display. | Less than 10 ohms resistance? **YES** | 1B-2 |
> | Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-025 — Remote Panel\|015-025]]. | Repair complete. |  |
>
> #### STEP 1B-2. Check Remote Panel Return Wire
>
> | **Conditions:** Locate remote panel Open remote panel. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check remote panel wiring. Place one test lead on the remote panel return terminal of the X4 connector. Place the other test lead on the remote panel return wire at the display. | Less than 10 ohms resistance? **YES** | 2B |
> | Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-025 — Remote Panel\|015-025]]. | Repair complete. |  |
>
> ### STEP 2. Check Panel System Cables
>
> #### STEP 2A. Check Engine Room Panel Cable
>
> | **Conditions:** Disconnect cable connector C14 from the engine room panel Disconnect cable connector C7 from the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the engine room panel cable. Install a jumper between engine room power switch supply pin and the engine room return pin in connector C14. Place one test lead in the engine room power switch supply pin in connector C7. Place the other test lead in the engine room return pin in connector C7. | Less than 10 ohms resistance? **YES** | 3A |
> | Less than 10 ohms resistance? **NORepair:** Replace the cable. | Repair complete. |  |
>
> #### STEP 2B. Check Remote Panel Cable
>
> | **Conditions:** Locate and open customer interface box Locate and open remote panel Disconnect the remote panel cable from the customer interface box X4 connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the remote panel cable. Install a jumper between remote panel power switch supply terminal and remote panel return terminal on remote control panel X4 in the remote control panel. Place one test lead on the remote panel power switch supply terminal of the remote panel cable. Place the other test lead on the remote panel return terminal of the remote panel cable. | Less than 10 ohms resistance? **YES** | 3A |
> | Less than 10 ohms resistance? **NORepair:** Replace the cable. | Repair complete. |  |
>
> ### STEP 3. Check Customer Interface Box Wiring
>
> #### STEP 3A. Check the Engine Room and Remote Power Switch Supply Wire
>
> | **Conditions:** Open the customer interface box Disconnect engine room cable at connector C7 from the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the engine room power switch supply wire. Place one test lead on the engine room power switch supply pin in connector C7. Place the other test lead on the remote panel return pin on the customer interface box terminal strip X4. | Less than 10 ohms resistance? **YES** | 3B |
> | Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |  |
>
> #### STEP 3B. Check the Engine Room Panel Return Wire
>
> | **Conditions:** Open the customer interface box Disconnect engine room cable at connector C7 from the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the engine room panel return wire. Place one test lead on the engine room panel return pin in connector C7. Place the other test lead on the remote panel return pin on the customer interface box terminal strip X4. | Less than 10 ohms resistance? **YESRepair:** Replace the faulty display. Refer to Procedure [[115-015-024 — Engine Room Panel\|015-024]] or [[115-015-025 — Remote Panel\|015-025]]. | Repair complete. |
> | Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |  |
