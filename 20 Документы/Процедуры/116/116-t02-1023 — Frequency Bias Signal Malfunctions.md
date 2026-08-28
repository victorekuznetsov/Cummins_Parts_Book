---
aliases:
  - "Неисправности сигнала частотной коррекции"
type: "Процедура"
doc: "116-t02-1023"
title_en: "Frequency Bias Signal Malfunctions"
title_ru: "Неисправности сигнала частотной коррекции"
modified: "2007-03-02"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4021617"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1023.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1023.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/116"
  - "перевод/машинный"
---

# Frequency Bias Signal Malfunctions
**Неисправности сигнала частотной коррекции**

> [!abstract] Процедура · `116-t02-1023`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2007-03-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1023.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1023.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

- Двигатель **не** отвечает на запрос о смещении фрэкентности.

### Как пользоваться этим деревом

Это дерево симптомов может быть использовано для устранения симптомов двигателя. Начните с шага 1 поиска неисправностей. На шаге 2 система задаст ряд вопросов и по симптому выдаст перечень действий по поиску неисправности.

### Практические замечания

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверка проводки интерфейсной коробки заказчика |  |
|  | **STEP 1A.** Проверьте скорость генератора/нагрузку, управляющую проводом для нерегулярного снабжения | Менее 10 Ом? |
|  | **STEP 1B.** Проверьте скорость генератора/загрузку, управляющую предвзятостью возврата провода | Менее 10 Ом? |
|  | **STEP 1C.** Проверьте скорость генератора/загрузку, управляющую неровной сигнальной проводкой | Менее 10 Ом? |
| ШАГ 2. | Проверьте электропроводку двигателя на кабель клиентского интерфейса |  |
|  | **STEP 2A.** Проверьте скорость генератора/нагрузку управляющих каналов и каналов связи | Менее 10 Ом? |
|  | **STEP 2B.** Проверьте скорость генератора/нагрузку, управляющую возвратом и сигнальными проводами | Менее 10 Ом? |

### ШАГ 1. Проверка проводки интерфейсной коробки заказчика

#### ШАГ 1A. Проверьте скорость генератора / нагрузку, управляющую проводом для нерегулярного снабжения

| **Условия:** Откройте окно клиентского интерфейса Отключить окно клиентского интерфейса к проводах двигателя, разъёму кабеля C3 от окна клиентского интерфейса. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте скорость генератора / нагрузку, управляющую смещенным проводом питания. Поместите один испытательный щуп на генератор скорости/нагрузки, управляющий смещенным 5-вольтовым подачей (сенсорным подачей 4) штифта в разъем C3. Поместите другой испытательный щуп на терминал генератора скорости/нагрузки, управляющий напряжением 5 вольт (сенсорная подачей 4) на разъеме X4. | Менее 10 Ом? *Да | 1В |
| Менее 10 Ом? **NORepair:** Заменить провод. См. процедуру[[116-015-023 — Customer Interface Box\|015-023]]. | Ремонт завершён. |  |

#### ШАГ 1B. Проверьте скорость генератора / скорость нагрузки, управляющие предвзятостью возврата провода

| **Условия:** Откройте окно клиентского интерфейса Отключить окно клиентского интерфейса к проводах двигателя, разъёму кабеля C3 от окна клиентского интерфейса. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте скорость генератора / нагрузку, управляющую проводом возврата смещения. Поместите один испытательный щуп на штифт генератора скорости/нагрузки, регулирующий возврат смещения (отдача датчика 4) в разъем C3. Поместите другой испытательный щуп на терминал возврата смещения генератора скорости/нагрузки (датчик возврата 4) на разъеме X4. | Менее 10 Ом? *Да | 1С |
| Менее 10 Ом? **NORepair:** Заменить провод. См. процедуру[[116-015-023 — Customer Interface Box\|015-023]]. | Ремонт завершён. |  |

#### ШАГ 1C. Проверьте скорость генератора / загрузку, управляющую неровной сигнальной проводкой

| **Условия:** Откройте окно клиентского интерфейса Отключить окно клиентского интерфейса к проводах двигателя, разъёму кабеля C3 от окна клиентского интерфейса. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте скорость генератора / нагрузку, управляющую сигнальным проводом смещения. Поместите один испытательный щуп на генератор скорости/нагрузки, управляющий контактом сигнала смещения в разъеме C3. Поместите другой испытательный щуп на терминал сигнала смещения генератора скорости/нагрузки на разъеме X4. | Менее 10 Ом? *Да | 2А |
| Менее 10 Ом? **NORepair:** Заменить провод. См. процедуру[[116-015-023 — Customer Interface Box\|015-023]]. | Ремонт завершён. |  |

### ШАГ 2. Проверьте электропроводку двигателя на кабель клиентского интерфейса

#### ШАГ 2A. Проверьте скорость генератора / управление нагрузкой и провода сигналов

| **Условия:** Отсоедините окно интерфейса клиента к проводах двигателя, ремня кабельного разъема C3 от окна интерфейса клиента. Отсоедините окно интерфейса клиента к проводах двигателя кабельного разъема C10 от проводов двигателя. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте скорость генератора / нагрузку, управляющую смещенностью подачи и сигнальных проводов. Поместите перемычку между пинком генератора скорости/нагрузки, управляющим смещением 5 вольт (сенсорная подачей 4), и контактным сигналом с перегрузкой генератора, управляющим смещением в разъеме C10. Поместите один испытательный щуп в штырь генератора скорости/нагрузки, управляющий смещением 5 вольт подачи (сенсорная подачей 4) разъема C3. Поместите другой испытательный щуп в генератор скорости/нагрузки, управляющий сигналом смещения контакта разъема C3. | Менее 10 Ом? *Да | 2В |
| Менее 10 Ом? **Заменить кабель.** | Ремонт завершён. |  |

#### ШАГ 2B. Проверьте скорость генератора / скорость нагрузки, управляющие предвзятостью возврата и сигнальные провода

| **Условия:** Отсоедините окно интерфейса клиента к проводах двигателя, ремня кабельного разъема C3 от окна интерфейса клиента. Отсоедините окно интерфейса клиента к проводах двигателя кабельного разъема C10 от проводов двигателя. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте скорость генератора / нагрузку, управляющую смещенностью подачи и сигнальных проводов. Поместите перемычку между штифтом генератора скорости/нагрузки, управляющим возвратом смещения (датчик возврата 4), и контактом сигнала смещения генератора/нагрузки, управляющего контактом смещения в разъеме C10. Поместите один испытательный щуп в штырь генератора скорости/нагрузки, регулирующий возврат смещения (отдача датчика 4) разъема C3. Поместите другой испытательный щуп в генератор скорости/нагрузки, управляющий сигналом смещения контакта разъема C3. | Менее 10 Ом? **Ремонт:** См. раздел TF в руководстве по устранению неполадок и ремонту, QSK19 CM850 Модульные двигатели общей системы железной дороги, Вестник 4021493 или Руководство по устранению неполадок и ремонту, Электронная система управления, Двигатели серии модульной общей системы железной дороги CM850, Вестник 4021533 или обратитесь к руководству по обслуживанию OEM для инструкций по ремонту потенциометра. | Ремонт завершён. |
| Менее 10 Ом? **Заменить кабель.** | Ремонт завершён. |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> - Engine does **not** respond to freqency bias request.
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
> |  | **STEP 1A.** Check Generator Speed/Load Governing Bias Supply Wire | Less than 10 ohms? |
> |  | **STEP 1B.** Check Generator Speed/Load Governing Bias Return Wire | Less than 10 ohms? |
> |  | **STEP 1C.** Check Generator Speed/Load Governing Bias Signal Wire | Less than 10 ohms? |
> | STEP 2. | Check Engine Harness to Customer Interface Box Cable |  |
> |  | **STEP 2A.** Check Generator Speed/Load Governing Supply and Signal Wires | Less than 10 ohms? |
> |  | **STEP 2B.** Check Generator Speed/Load Governing Return and Signal Wires | Less than 10 ohms? |
>
> ### STEP 1. Check Customer Interface Box Wiring
>
> #### STEP 1A. Check Generator Speed/Load Governing Bias Supply Wire
>
> | **Conditions:** Open the customer interface box Disconnect customer interface box to engine harness cable connector C3 from the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the generator speed/load governing bias supply wire. Place one test lead on the generator speed/load governing bias 5 volt supply (sensor supply 4) pin in connector C3. Place the other test lead on the generator speed/load governing bias 5 volt supply (sensor supply 4) terminal on the X4 connector. | Less than 10 ohms? **YES** | 1B |
> | Less than 10 ohms? **NORepair:** Replace the wire. Refer to Procedure [[116-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |  |
>
> #### STEP 1B. Check Generator Speed/Load Governing Bias Return Wire
>
> | **Conditions:** Open the customer interface box Disconnect customer interface box to engine harness cable connector C3 from the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the generator speed/load governing bias return wire. Place one test lead on the generator speed/load governing bias return (sensor return 4) pin in connector C3. Place the other test lead on the generator speed/load governing bias return (sensor return 4) terminal on the X4 connector. | Less than 10 ohms? **YES** | 1C |
> | Less than 10 ohms? **NORepair:** Replace the wire. Refer to Procedure [[116-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |  |
>
> #### STEP 1C. Check Generator Speed/Load Governing Bias Signal Wire
>
> | **Conditions:** Open the customer interface box Disconnect customer interface box to engine harness cable connector C3 from the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the generator speed/load governing bias signal wire. Place one test lead on the generator speed/load governing bias signal pin in connector C3. Place the other test lead on the generator speed/load governing bias signal terminal on the X4 connector. | Less than 10 ohms? **YES** | 2A |
> | Less than 10 ohms? **NORepair:** Replace the wire. Refer to Procedure [[116-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |  |
>
> ### STEP 2. Check Engine Harness to Customer Interface Box Cable
>
> #### STEP 2A. Check Generator Speed/Load Governing Supply and Signal Wires
>
> | **Conditions:** Disconnect customer interface box to engine harness cable connector C3 from the customer interface box. Disconnect customer interface box to engine harness cable connector C10 from the engine harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check generator speed/load governing bias supply and signal wires. Place a jumper between the generator speed/load governing bias 5 volt supply (sensor supply 4) pin and the generator speed/load governing bias signal pin in the C10 connector. Place one test lead in the generator speed/load governing bias 5 volt supply (sensor supply 4) pin of the C3 connector. Place the other test lead in the generator speed/load governing bias signal pin of the C3 connector. | Less than 10 ohms? **YES** | 2B |
> | Less than 10 ohms? **NORepair:** Replace the cable. | Repair complete. |  |
>
> #### STEP 2B. Check Generator Speed/Load Governing Bias Return and Signal Wires
>
> | **Conditions:** Disconnect customer interface box to engine harness cable connector C3 from the customer interface box. Disconnect customer interface box to engine harness cable connector C10 from the engine harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check generator speed/load governing bias supply and signal wires. Place a jumper between the generator speed/load governing bias return (sensor return 4) pin and the generator speed/load governing bias signal pin in the C10 connector. Place one test lead in the generator speed/load governing bias return (sensor return 4) pin of the C3 connector. Place the other test lead in the generator speed/load governing bias signal pin of the C3 connector. | Less than 10 ohms? **YESRepair:** Refer to Section TF in the Troubleshooting and Repair Manual, QSK19 CM850 Modular Common Rail System Series Engines, Bulletin 4021493, or the Troubleshooting and Repair Manual, Electronic Control System, CM850 Modular Common Rail System Series Engines, Bulletin 4021533, or refer to the OEM service manual for potentiometer repair instructions. | Repair complete. |
> | Less than 10 ohms? **NORepair:** Replace the cable. | Repair complete. |  |
