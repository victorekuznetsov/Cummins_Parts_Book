---
aliases:
  - "Неисправности сигнала регулировки нагрузки"
type: "Процедура"
doc: "115-t02-1022"
title_en: "Load Adjust Signal Malfunctions"
title_ru: "Неисправности сигнала регулировки нагрузки"
modified: "2006-08-09"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4021587"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/115/115-t02-1022.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/115-t02-1022.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/115"
  - "перевод/машинный"
---

# Load Adjust Signal Malfunctions
**Неисправности сигнала регулировки нагрузки**

> [!abstract] Процедура · `115-t02-1022`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021587 — C Command Panel System Marine Master Repair Manual|4021587]]
> **Секции:** Section TT — Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2006-08-09
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/115/115-t02-1022.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/115-t02-1022.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

- Сигнал регулировки нагрузки **не** доступен из окна интерфейса клиента.

### Как пользоваться этим деревом

Это дерево симптомов может быть использовано для устранения симптомов двигателя. Начните с шага 1 поиска неисправностей. На шаге 2 система задаст ряд вопросов и по симптому выдаст перечень действий по поиску неисправности.

### Практические замечания

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверка проводки интерфейсной коробки заказчика |  |
|  | **ШАГ 1А.** Проверьте, чтобы настроить потенциометр | Сопротивление менее 10 Ом? |
|  | **ШАГ 1В** Проверьте, чтобы настроить петлю обратной проводов потенциометра | Сопротивление менее 10 Ом? |
|  | **STEP 1C.** Проверить частоту настройки сигнала | Сопротивление менее 10 Ом? |
| ШАГ 2. | Проверьте электропроводку двигателя на кабель клиентского интерфейса |  |
|  | **STEP 2A.** Проверить частоту регулировки подачи и сигнала | Сопротивление менее 10 Ом? |
|  | **STEP 2B.** Проверить частоту возврата и сигнальные провода | Сопротивление менее 10 Ом? |

### ШАГ 1. Проверка проводки интерфейсной коробки заказчика

#### ШАГ 1A. Проверьте Droop Adjust Potentiometer

| **Условия: **Откройте окно клиентского интерфейса Отключить окно клиентского интерфейса к проводах двигателя, разъёму кабеля C3 от окна клиентского интерфейса. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте проволоку питания потенциометра с отвисанием. Поместите один испытательный щуп на штифт с потенциометром 5 вольт (сенсорный штифт 1) в разъем C3. Поместите другой испытательный щуп на потенциометр 5 вольт с отрегулировкой сбрасывания (сенсорный источник 1) на разъем X4. | Сопротивление менее 10 Ом? *Да | 1В |
| Сопротивление менее 10 Ом? **NORepair:** Заменить провод. См. процедуру[[115-015-023 — Customer Interface Box\|015-023]]. | Ремонт завершён. |  |

#### ШАГ 1B. Проверить регулировку петли Potentiometer Return Wire

| **Условия: **Откройте окно клиентского интерфейса Отключить окно клиентского интерфейса к проводах двигателя, разъёму кабеля C3 от окна клиентского интерфейса. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте провод возврата потенциометра с откидным регулировкой. Поместите один пробный щуп на штифт возврата потенциометра с откидным регулированием (отдача датчика 1) в разъём C3. Поместите другой тест на выводной потенциометр с отрегулировкой сбрасывания (отдача датчика 1) на разъем X4. | Сопротивление менее 10 Ом? *Да | 1С |
| Сопротивление менее 10 Ом? **NORepair:** Заменить провод. См. процедуру[[115-015-023 — Customer Interface Box\|015-023]]. | Ремонт завершён. |  |

#### ШАГ 1C. Проверьте частоту Adjust Signal Wire

| **Условия: **Откройте окно клиентского интерфейса Отключить окно клиентского интерфейса к проводах двигателя, разъёму кабеля C3 от окна клиентского интерфейса. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте частотный сигнальный провод. Поместите один испытательный щуп на генератор выходной частоты регулировки потенциометра сигнала контакта в разъеме С3. Поместите другой испытательный щуп на выходную частоту генератора регулировки сигнального терминала потенциометра на разъем X4. | Сопротивление менее 10 Ом? *Да | 2А |
| Сопротивление менее 10 Ом? **NORepair:** Заменить провод. См. процедуру[[115-015-023 — Customer Interface Box\|015-023]]. | Ремонт завершён. |  |

### ШАГ 2. Проверьте электропроводку двигателя на кабель клиентского интерфейса

#### ШАГ 2A. Проверьте частоту настройки подачи и сигнальных проводов

| **Условия:** Отсоединить окно интерфейса клиента к разъёму кабеля C3 с помощью проводов двигателя от окна интерфейса клиента Отключить окно интерфейса клиента к разъёму кабеля C9 с помощью проводов двигателя. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте частоту регулировки подачи и сигнала проводов. Поместите перемычку между штырем питания с потенциометром 5 вольт (сенсорный источник питания 1) и контактом сигнала с выходной частотой генератора с потенциометром в разъеме C9. Поместите один испытательный щуп в штепсель потенциометра 5 вольт (сенсорный штифт 1) разъема C3. Поместите другой испытательный щуп в генератор выходной частоты регулировки потенциометра сигнала контакта разъема С3. | Сопротивление менее 10 Ом? *Да | 2В |
| Сопротивление менее 10 Ом? **Заменить кабель.** | Ремонт завершён. |  |

#### ШАГ 2B. Проверьте частоту регулировки возврата и сигнальных проводов

| **Условия:** Отсоедините окно интерфейса клиента к проводах двигателя, ремня кабельного разъема C3 от окна интерфейса клиента. Отсоедините окно интерфейса клиента к проводах двигателя кабельного разъема C9 от проводов двигателя. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте частоту регулировки возврата и сигнальных проводов. Поместите перемычку между контактом сигнала потенциометра с регулировкой выходной частоты генератора и штифтом возврата потенциометра с регулировкой понижания (отдача датчика 1) в разъеме C9. Поместите один пробный щуп в штырь с откидным регулятором возврата потенциометра (датчик возврата 1) разъема C3. Поместите другой испытательный щуп в генератор выходной частоты регулировки потенциометра сигнала контакта разъема С3. | Сопротивление менее 10 Ом? **Ремонт: **См. раздел TF в Руководстве по устранению неполадок и ремонту, Электронная система управления, QSK19 CM850, Модульная общая железнодорожная система, Серийные двигатели, Вестник 4021493 или обратитесь к Руководству по обслуживанию OEM для инструкций по ремонту потенциометра. | Ремонт завершён. |
| Сопротивление менее 10 Ом? **Заменить кабель.** | Ремонт завершён. |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> - Load adjust signal **not** available from customer interface box.
>
> ### How To Use This Tree
>
> This symptom tree can be used to troubleshoot engine symptoms. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.
>
> ### Shoptalk
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check Customer Interface Box Wiring |  |
> |  | **STEP 1A.** Check Droop Adjust Potentiometer Supply Wire | Less than 10 ohms resistance? |
> |  | **STEP 1B.** Check Droop Adjust Potentiometer Return Wire | Less than 10 ohms resistance? |
> |  | **STEP 1C.** Check Frequency Adjust Signal Wire | Less than 10 ohms resistance? |
> | STEP 2. | Check Engine Harness to Customer Interface Box Cable |  |
> |  | **STEP 2A.** Check Frequency Adjust Supply and Signal Wires | Less than 10 ohms resistance? |
> |  | **STEP 2B.** Check Frequency Adjust Return and Signal Wires | Less than 10 ohms resistance? |
>
> ### STEP 1. Check Customer Interface Box Wiring
>
> #### STEP 1A. Check Droop Adjust Potentiometer Supply Wire
>
> | **Conditions:** Open the customer interface box Disconnect customer interface box to engine harness cable connector C3 from the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the droop adjust potentiometer supply wire. Place one test lead on the droop adjust potentiometer 5 volt supply (sensor supply 1) pin in connector C3. Place the other test lead on the droop adjust potentiometer 5 volt supply (sensor supply 1) terminal on the X4 connector. | Less than 10 ohms resistance? **YES** | 1B |
> | Less than 10 ohms resistance? **NORepair:** Replace the wire. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |  |
>
> #### STEP 1B. Check Droop Adjust Potentiometer Return Wire
>
> | **Conditions:** Open the customer interface box Disconnect customer interface box to engine harness cable connector C3 from the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the droop adjust potentiometer return wire. Place one test lead on the droop adjust potentiometer return (sensor return 1) pin in connector C3. Place the other test on droop adjust potentiometer return (sensor return 1) terminal on the X4 connector. | Less than 10 ohms resistance? **YES** | 1C |
> | Less than 10 ohms resistance? **NORepair:** Replace the wire. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |  |
>
> #### STEP 1C. Check Frequency Adjust Signal Wire
>
> | **Conditions:** Open the customer interface box Disconnect customer interface box to engine harness cable connector C3 from the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the frequency adjust signal wire. Place one test lead on the generator output frequency adjust potentiometer signal pin in connector C3. Place the other test lead on the generator output frequency adjust potentiometer signal terminal on the X4 connector. | Less than 10 ohms resistance? **YES** | 2A |
> | Less than 10 ohms resistance? **NORepair:** Replace the wire. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |  |
>
> ### STEP 2. Check Engine Harness to Customer Interface Box Cable
>
> #### STEP 2A. Check Frequency Adjust Supply and Signal Wires
>
> | **Conditions:** Disconnect customer interface box to engine harness cable connector C3 from the customer interface box Disconnect customer interface box to engine harness cable connector C9 from the engine harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check frequency adjust supply and signal wires. Place a jumper between the droop adjust potentiometer 5 volt supply (sensor supply 1) pin and the generator output frequency adjust potentiometer signal pin in the C9 connector. Place one test lead in the droop adjust potentiometer 5 volt supply (sensor supply 1) pin of the C3 connector. Place the other test lead in the generator output frequency adjust potentiometer signal pin of the C3 connector. | Less than 10 ohms resistance? **YES** | 2B |
> | Less than 10 ohms resistance? **NORepair:** Replace the cable. | Repair complete. |  |
>
> #### STEP 2B. Check Frequency Adjust Return and Signal Wires
>
> | **Conditions:** Disconnect customer interface box to engine harness cable connector C3 from the customer interface box. Disconnect customer interface box to engine harness cable connector C9 from the engine harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check frequency adjust return and signal wires. Place a jumper between the generator output frequency adjust potentiometer signal pin and the droop adjust potentiometer return (sensor return 1) pin in the C9 connector. Place one test lead in the droop adjust potentiometer return (sensor return 1) pin of the C3 connector. Place the other test lead in the generator output frequency adjust potentiometer signal pin of the C3 connector. | Less than 10 ohms resistance? **YESRepair:** Refer to Section TF in the Troubleshooting and Repair Manual, Electronic Control System, QSK19 CM850, Modular Common Rail System, Series Engines, Bulletin 4021493 or refer to the OEM Service Manual for potentiometer repair instructions. | Repair complete. |
> | Less than 10 ohms resistance? **NORepair:** Replace the cable. | Repair complete. |  |
