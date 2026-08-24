---
aliases:
  - "Неисправность выходного сигнала указателя температуры ОЖ ЭБУ"
type: "Процедура"
doc: "116-t02-1067"
title_en: "ECM Coolant Temperature Gauge Output Signal Malfunction"
title_ru: "Неисправность выходного сигнала указателя температуры ОЖ ЭБУ"
modified: "2007-03-02"
engines:
  - "41349633"
families:
  - "QSK19"
manuals:
  - "4021617"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1067.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/116-t02-1067.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/116"
  - "перевод/машинный"
---

# ECM Coolant Temperature Gauge Output Signal Malfunction
**Неисправность выходного сигнала указателя температуры ОЖ ЭБУ**

> [!abstract] Процедура · `116-t02-1067`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2007-03-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1067.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/116-t02-1067.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

- Выходной сигнал измерения температуры охлаждающей жидкости ECM ** не доступен.

### Как пользоваться этим деревом

Это дерево симптомов может быть использовано для устранения неисправности выходного сигнала измерения температуры охлаждающей жидкости ECM. Начните с шага 1 поиска неисправностей. На шаге 2 система задаст ряд вопросов и по симптому выдаст перечень действий по поиску неисправности.

### Практические замечания

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверка проводки интерфейсной коробки заказчика |  |
|  | **STEP 1A.** Проверьте наличие провода для измерения температуры охлаждающей жидкости | Менее 10 Ом? |
|  | **ШАГ 1В.** Проверьте температурный индикатор охлаждающего устройства для провода с коротким проводом | Менее 10 Ом? |
|  | **STEP 1C.** Проверьте температурный индикатор охлаждающей жидкости на короткое время | Менее 10 Ом? |
| ШАГ 2. | Проверьте электропроводку двигателя на кабель клиентского интерфейса |  |
|  | **STEP 2A.** Проверьте наличие провода для измерения температуры охлаждающей жидкости | Менее 10 Ом? |
|  | **STEP 2B.** Проверьте температурный индикатор охлаждающей жидкости для короткой проводной проводов | Менее 10 Ом? |

### ШАГ 1. Проверка проводки интерфейсной коробки заказчика

#### ШАГ 1A. Проверьте сигнальный провод температуры охлаждающей жидкости для открытого

| **Условия: ** Откройте окно клиентского интерфейса Отключить окно клиентского интерфейса к проводах двигателя, разъёму кабеля C2 от окна клиентского интерфейса. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте сигнальный провод измерителя температуры охлаждающей жидкости на наличие открытого. Поместите один испытательный щуп на контакт сигнала измерителя температуры охлаждающей жидкости в разъём C2. Поместите другой испытательный щуп на сигнальный терминал измерителя температуры охлаждающей жидкости на разъем X4. | Менее 10 Ом? *Да** | 1В |
| Менее 10 Ом? **NORepair:** Заменить провод. См. процедуру[[116-015-023 — Customer Interface Box\|015-023]]. | Ремонт завершён |  |

#### ШАГ 1B. Проверьте сигнальный датчик температуры охлаждающей жидкости для провода для провода короткого

| **Условия: ** Откройте окно клиентского интерфейса Отключить окно клиентского интерфейса к проводах двигателя, разъёму кабеля C2 от окна клиентского интерфейса. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте сигнальный провод измерителя температуры охлаждающей жидкости для провода для короткого провода. Поместите один испытательный щуп на контакт сигнала измерителя температуры охлаждающей жидкости в разъём C2. Поместите другой испытательный щуп на каждый из оставшихся терминалов в разъем X4. | Менее 10 Ом? *** Заменить провод. См. процедуру[[116-015-023 — Customer Interface Box\|015-023]]. | Ремонт завершён |
| Менее 10 Ом? ** НЕТ** | 1С |  |

#### ШАГ 1C. Проверьте сигнальную проволоку с температурой охлаждающей жидкости для короткой посадки

| **Условия: ** Откройте окно клиентского интерфейса Отключить окно клиентского интерфейса к проводах двигателя, разъёму кабеля C2 от окна клиентского интерфейса. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте сигнальный провод измерителя температуры охлаждающей жидкости для короткого заземления. Поместите один испытательный щуп на контакт сигнала измерителя температуры охлаждающей жидкости в разъём C2. Поместите другой испытательный щуп на панельную площадку. | Менее 10 Ом? *** Заменить провод. См. процедуру[[116-015-023 — Customer Interface Box\|015-023]]. | Ремонт завершён |
| Менее 10 Ом? ** НЕТ** | 2А |  |

### ШАГ 2. Проверьте электропроводку двигателя на кабель клиентского интерфейса

#### ШАГ 2A. Проверьте сигнальный провод температуры охлаждающей жидкости для открытого

| **Условия:** Отсоединить окно интерфейса клиента к разъёму кабеля C2 с помощью проводов двигателя от окна интерфейса клиента Отключить окно интерфейса клиента к разъёму кабеля C9 с помощью проводов двигателя. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте сигнальный провод измерителя температуры охлаждающей жидкости на наличие открытого. Поместите перемычку между контактом сигнала измерителя температуры охлаждающей жидкости и контактом сигнала потенциометра с отсевом в разъеме C9. Поместите один испытательный щуп в контакт сигнала измерителя температуры охлаждающей жидкости разъёма C2. Поместите другой испытательный щуп в контакт сигнала потенциометра с подвеской от суп-регулировки разъема C2. | Менее 10 Ом? *Да** | 2В |
| Менее 10 Ом? **Заменить кабель.** | Ремонт завершён |  |

#### ШАГ 2B. Проверьте сигнальный датчик температуры охлаждающей жидкости для провода для провода короткого

| **Условия:** Отсоединить окно интерфейса клиента к разъёму кабеля C2 с помощью проводов двигателя от окна интерфейса клиента Отключить окно интерфейса клиента к разъёму кабеля C9 с помощью проводов двигателя. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте сигнальный провод измерителя температуры охлаждающей жидкости для провода для короткого провода. Поместите один испытательный щуп в контакт выходного сигнала датчика температуры охлаждающей жидкости в разъёме C2. Поместите другой испытательный щуп на каждый из оставшихся штифтов в разъеме C2. | Менее 10 Ом? *Да** | Ремонт завершён |
| Менее 10 Ом? **NORepair: ** См. раздел TF в руководстве по устранению неполадок и ремонту, электронной системе управления, двигателях серий модульных систем общего пользования QSK19 CM850, в бюллетене 4021493 или руководстве по устранению неполадок и ремонту, электронной системе управления, QSK38, QSK50 и QSK60, двигателях серий модульных систем общего пользования CM850, в бюллетене 4021533 или обратитесь к руководству по обслуживанию OEM. | Ремонт завершён |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> - ECM coolant temperature gauge output signal is **not** available.
>
> ### How To Use This Tree
>
> This symptom tree can be used to troubleshoot an ECM coolant temperature gauge output signal malfunction. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.
>
> ### Shoptalk
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check Customer Interface Box Wiring |  |
> |  | **STEP 1A.** Check Coolant Temperature Meter Signal Wire for Open | Less than 10 ohms? |
> |  | **STEP 1B.** Check Coolant Temperature Meter Signal Wire for Wire to Wire Short | Less than 10 ohms? |
> |  | **STEP 1C.** Check Coolant Temperature Meter Signal Wire for Short to Ground | Less than 10 ohms? |
> | STEP 2. | Check Engine Harness to Customer Interface Box Cable |  |
> |  | **STEP 2A.** Check Coolant Temperature Meter Signal Wire for Open | Less than 10 ohms? |
> |  | **STEP 2B.** Check Coolant Temperature Meter Signal Wire for Wire to Wire Short | Less than 10 ohms? |
>
> ### STEP 1. Check Customer Interface Box Wiring
>
> #### STEP 1A. Check Coolant Temperature Meter Signal Wire for Open
>
> | **Conditions:** Open the customer interface box Disconnect customer interface box to engine harness cable connector C2 from the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the coolant temperature meter signal wire for an open. Place one test lead on the coolant temperature meter signal pin in connector C2. Place the other test lead on coolant temperature meter signal terminal on the X4 connector. | Less than 10 ohms? **YES** | 1B |
> | Less than 10 ohms? **NORepair:** Replace the wire. Refer to Procedure [[116-015-023 — Customer Interface Box\|015-023]]. | Repair complete |  |
>
> #### STEP 1B. Check Coolant Temperature Meter Signal Wire for Wire to Wire Short
>
> | **Conditions:** Open the customer interface box Disconnect customer interface box to engine harness cable connector C2 from the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the coolant temperature meter signal wire for wire to wire short. Place one test lead on the coolant temperature meter signal pin in connector C2. Place the other test lead on each of the remaining terminals in X4 connector. | Less than 10 ohms? **YESRepair:** Replace the wire. Refer to Procedure [[116-015-023 — Customer Interface Box\|015-023]]. | Repair complete |
> | Less than 10 ohms? **NO** | 1C |  |
>
> #### STEP 1C. Check Coolant Temperature Meter Signal Wire for Short to Ground
>
> | **Conditions:** Open the customer interface box Disconnect customer interface box to engine harness cable connector C2 from the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the coolant temperature meter signal wire for short to ground. Place one test lead on the coolant temperature meter signal pin in connector C2. Place the other test lead on panel ground. | Less than 10 ohms? **YESRepair:** Replace the wire. Refer to Procedure [[116-015-023 — Customer Interface Box\|015-023]]. | Repair complete |
> | Less than 10 ohms? **NO** | 2A |  |
>
> ### STEP 2. Check Engine Harness to Customer Interface Box Cable
>
> #### STEP 2A. Check Coolant Temperature Meter Signal Wire for Open
>
> | **Conditions:** Disconnect customer interface box to engine harness cable connector C2 from the customer interface box Disconnect customer interface box to engine harness cable connector C9 from the engine harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check coolant temperature meter signal wire for an open. Place a jumper between the coolant temperature meter signal pin and the droop adjust potentiometer signal pin in the C9 connector. Place one test lead in the coolant temperature meter signal pin of the C2 connector. Place the other test lead in the droop adjust potentiometer signal pin of the C2 connector. | Less than 10 ohms? **YES** | 2B |
> | Less than 10 ohms? **NORepair:** Replace the cable. | Repair complete |  |
>
> #### STEP 2B. Check Coolant Temperature Meter Signal Wire for Wire to Wire Short
>
> | **Conditions:** Disconnect customer interface box to engine harness cable connector C2 from the customer interface box Disconnect customer interface box to engine harness cable connector C9 from the engine harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check coolant temperature meter signal wire for a wire to wire short. Place one test lead in the coolant temperature gauge output signal pin in connector C2. Place the other test lead on each of the remaining pins in the C2 connector. | Less than 10 ohms? **YES** | Repair complete |
> | Less than 10 ohms? **NORepair:** Refer to Section TF in the Troubleshooting and Repair Manual, Electronic Control System, QSK19 CM850 Modular Common Rail System Series Engines, Bulletin 4021493, or the Troubleshooting and Repair Manual, Electronic Control System, QSK38, QSK50, and QSK60, CM850 Modular Common Rail System Series Engines, Bulletin 4021533, or refer to the OEM service manual. | Repair complete |  |
