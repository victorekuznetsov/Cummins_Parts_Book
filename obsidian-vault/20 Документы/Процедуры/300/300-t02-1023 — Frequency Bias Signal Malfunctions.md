---
aliases:
  - "Неисправности сигнала частотной коррекции"
type: "Процедура"
doc: "300-t02-1023"
title_en: "Frequency Bias Signal Malfunctions"
title_ru: "Неисправности сигнала частотной коррекции"
modified: "2019-05-22"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "4332828"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/300/300-t02-1023.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/300-t02-1023.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/300"
  - "перевод/машинный"
---

# Frequency Bias Signal Malfunctions
**Неисправности сигнала частотной коррекции**

> [!abstract] Процедура · `300-t02-1023`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[4332828 — Marine C Command HD Elite™ Panel System Master Repair Manual|4332828]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2019-05-22
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/300/300-t02-1023.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/300-t02-1023.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

- Двигатель не реагирует на запрос частоты смещения.

### Как пользоваться этим деревом

Это дерево симптомов может быть использовано для устранения симптомов двигателя. Начните с шага 1 поиска неисправностей. На шаге 2 система задаст ряд вопросов и по симптому выдаст перечень действий по поиску неисправности.

### Практические замечания

Нет.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте клиентский интерфейс (C.I.B.) проводов. |  |
|  | **ШАГ 1А.** Проверьте скорость/нагрузку генератора, управляющего смещенным проводом SUPPLY. | Менее 10 Ом? |
|  | **ШАГ 1В.** Проверьте скорость/нагрузку генератора, управляющего смещенным проводом ВПЕРЕД. | Менее 10 Ом? |
|  | **STEP 1C.** Проверьте скорость/нагрузку генератора, управляющего смещенным проводом SIGNAL. | Менее 10 Ом? |
| ШАГ 2. | Проверьте жгут электропроводки двигателя на C.I.B. |  |
|  | **ШАГ 2А.** Проверьте скорость/нагрузку генератора, управляющего смещениями SUPPLY и SIGNAL проводов. | Менее 10 Ом? |
|  | **ШАГ 2В.** Проверьте скорость/нагрузку генератора, управляющего смещениями ВПЕРЕД и SIGNAL проводов. | Менее 10 Ом? |

### ШАГ 1. Проверьте клиентский интерфейс (C.I.B.) проводов.

#### ШАГ 1A. Проверьте скорость генератора / нагрузку, управляющую смещенностью провода SUPPLY.

| **Условия: **Открыть ЦБ. Отключите компьютерную систему. к проводах двигателя упряжь кабельного разъёма С1 от C.I.B. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте скорость генератора / нагрузку, управляющую смещенностью провода SUPPLY. Поместите один испытательный щуп на генератор скорости/нагрузки, управляющий смещенным 5-вольтным контактом питания в разъеме С1. Поместите другой испытательный щуп на генератор скорости/нагрузки, управляющий смещенным 5-вольтным терминалом SUPPLY на разъеме X1. | Менее 10 Ом? *Да | 1В |
| Менее 10 Ом? **NORepair:** Заменить провод.[[300-015-023 — Customer Interface Box\|См. процедуру 015-023 в разделе 15.]] | Ремонт завершён |  |

#### ШАГ 1B. Проверьте скорость генератора / нагрузку, управляющую смещенностью провода RETURN.

| **Условия: **Открыть ЦБ. Отключите компьютерную систему. к проводах двигателя упряжь кабельного разъёма С1 от C.I.B. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте скорость генератора / нагрузку, управляющую смещенностью провода RETURN. Поместите один испытательный щуп на генератор скорости/нагрузки, управляющий смещенным обратным контактом в разъеме С1. Поместите другой испытательный щуп на терминал возврата частоты/нагрузки генератора, регулирующий возврат смещения, на разъем X1. | Менее 10 Ом? *Да | 2А |
| Менее 10 Ом? **NORepair:** Заменить провод.[[300-015-023 — Customer Interface Box\|См. процедуру 015-023 в разделе 15.]] | Ремонт завершён |  |

#### ШАГ 1C. Проверьте скорость генератора / нагрузку, управляющую смещенностью провода SIGNAL.

| **Условия: **Открыть ЦБ. Отключите компьютерную систему. к проводах двигателя упряжь кабельного разъёма С1 от C.I.B. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте скорость генератора / нагрузку, управляющую смещенностью провода SIGNAL. Поместите один испытательный щуп на генератор скорости/нагрузки, управляющий контактом сигнала смещения в разъеме С1. Поместите другой испытательный щуп на терминал сигнала смещения генератора скорости/нагрузки на разъеме X1. | Менее 10 Ом? *Да | 2А |
| Менее 10 Ом? **NORepair:** Заменить провод.[[300-015-023 — Customer Interface Box\|См. процедуру 015-023 в разделе 15.]] | Ремонт завершён |  |

### ШАГ 2. Проверьте жгут электропроводки двигателя на C.I.B.

#### ШАГ 2A. Проверьте скорость генератора / нагрузку, управляющую смещениями SUPPLY и SIGNAL проводов.

| **Условия: **Отключить C.I.B. к проводах двигателя упряжь кабельного разъёма С1 от C.I.B. Отключите компьютерную систему. кабель для проводов двигателя от двигателя. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте скорость генератора / нагрузку, управляющую смещениями SUPPLY и SIGNAL проводов. Поместите перемычку между генератором скорости/нагрузки, управляющим смещением 5 вольт контакта питания и частотного смещением сигнала контакта в соединении стороны двигателя. Поместите один испытательный щуп в генератор скорости/нагрузки, управляющий смещенным 5-вольтным контактом подачи разъема C1. Поместите другой испытательный щуп в генератор скорости/нагрузки, управляющий сигналом смещения контакта разъема C1. | Менее 10 Ом? *Да | 2В |
| Менее 10 Ом? **Заменить кабель.** | Ремонт завершён |  |

#### ШАГ 2B. Проверьте скорость генератора / нагрузку, управляющую смещениями ВПЕРЕД и SIGNAL проводов.

| **Условия: **Отключить C.I.B. к проводах двигателя упряжь кабельного разъёма С1 от C.I.B. Отключите компьютерную систему. кабель для проводов двигателя от двигателя. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте скорость генератора / нагрузку, управляющую смещениями SUPPLY и SIGNAL проводов. Поместите перемычку между обратным контактом с частотным уклоном и контактом с сигналом смещения генератора / нагрузки, регулирующим контакт с уклоном в соединении на стороне двигателя. Поместите один испытательный щуп в генератор скорости/нагрузки, регулирующий обратный контакт смещения разъема C1. Поместите другой испытательный щуп в частотный сигнал смещения контакта разъема C1. | Менее 10 Ом? **Ремонт: **Используйте следующие инструкции по ремонту потенциометра. См. Руководство по устранению неполадок в коде CM850 морского вспомогательного QSB7-DM, Бюллетень 4325972, Раздел TF; Руководство по устранению и ремонту неполадок в электронной системе управления ISM и QSM11, Бюллетень [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual\|3666266]], Раздел TF; Руководство по устранению неполадок в коде X15 CM2350 X125M, Бюллетень 5504346, Раздел TF; или информация об услугах производителя оборудования. | Ремонт завершён |
| Менее 10 Ом? **Заменить кабель.** | Ремонт завершён |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> - Engine does **not** respond to frequency bias request.
>
> ### How To Use This Tree
>
> This symptom tree can be used to troubleshoot engine symptoms. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.
>
> ### Shoptalk
>
> None.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the customer interface box (C.I.B.) wiring. |  |
> |  | **STEP 1A.** Check the generator speed/load governing bias SUPPLY wire. | Less than 10 ohms? |
> |  | **STEP 1B.** Check the generator speed/load governing bias RETURN wire. | Less than 10 ohms? |
> |  | **STEP 1C.** Check the generator speed/load governing bias SIGNAL wire. | Less than 10 ohms? |
> | STEP 2. | Check the engine harness to the C.I.B. |  |
> |  | **STEP 2A.** Check the generator speed/load governing bias SUPPLY and SIGNAL wires. | Less than 10 ohms? |
> |  | **STEP 2B.** Check the generator speed/load governing bias RETURN and SIGNAL wires. | Less than 10 ohms? |
>
> ### STEP 1. Check the customer interface box (C.I.B.) wiring.
>
> #### STEP 1A. Check the generator speed/load governing bias SUPPLY wire.
>
> | **Conditions:** Open the C.I.B. Disconnect the C.I.B. to the engine harness cable connector C1 from the C.I.B. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the generator speed/load governing bias SUPPLY wire. Place one test lead on the generator speed/load governing bias 5 volt SUPPLY pin in connector C1. Place the other test lead on the generator speed/load governing bias 5 volt SUPPLY terminal on the X1 connector. | Less than 10 ohms? **YES** | 1B |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[300-015-023 — Customer Interface Box\|Refer to Procedure 015-023 in Section 15.]] | Repair complete |  |
>
> #### STEP 1B. Check the generator speed/load governing bias RETURN wire.
>
> | **Conditions:** Open the C.I.B. Disconnect the C.I.B. to the engine harness cable connector C1 from the C.I.B. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the generator speed/load governing bias RETURN wire. Place one test lead on the generator speed/load governing bias RETURN pin in connector C1. Place the other test lead on the generator speed/load governing bias return terminal on the X1 connector. | Less than 10 ohms? **YES** | 2A |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[300-015-023 — Customer Interface Box\|Refer to Procedure 015-023 in Section 15.]] | Repair complete |  |
>
> #### STEP 1C. Check the generator speed/load governing bias SIGNAL wire.
>
> | **Conditions:** Open the C.I.B. Disconnect the C.I.B. to the engine harness cable connector C1 from the C.I.B. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the generator speed/load governing bias SIGNAL wire. Place one test lead on the generator speed/load governing bias SIGNAL pin in connector C1. Place the other test lead on the generator speed/load governing bias signal terminal on the X1 connector. | Less than 10 ohms? **YES** | 2A |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[300-015-023 — Customer Interface Box\|Refer to Procedure 015-023 in Section 15.]] | Repair complete |  |
>
> ### STEP 2. Check the engine harness to the C.I.B.
>
> #### STEP 2A. Check the generator speed/load governing bias SUPPLY and SIGNAL wires.
>
> | **Conditions:** Disconnect the C.I.B. to the engine harness cable connector C1 from the C.I.B. Disconnect the C.I.B. to the engine harness cable from the engine. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the generator speed/load governing bias SUPPLY and SIGNAL wires. Place a jumper between the generator speed/load governing bias 5 volt SUPPLY pin and the frequency bias SIGNAL pin in the engine-side connection. Place one test lead in the generator speed/load governing bias 5 volt SUPPLY pin of the C1 connector. Place the other test lead in the generator speed/load governing bias SIGNAL pin of the C1 connector. | Less than 10 ohms? **YES** | 2B |
> | Less than 10 ohms? **NORepair:** Replace the cable. | Repair complete |  |
>
> #### STEP 2B. Check the generator speed/load governing bias RETURN and SIGNAL wires.
>
> | **Conditions:** Disconnect the C.I.B. to the engine harness cable connector C1 from the C.I.B. Disconnect the C.I.B. to the engine harness cable from the engine. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the generator speed/load governing bias SUPPLY and SIGNAL wires. Place a jumper between the frequency bias RETURN pin and the generator speed/load governing bias SIGNAL pin in the engine-side connection. Place one test lead in the generator speed/load governing bias RETURN pin of the C1 connector. Place the other test lead in the frequency bias SIGNAL pin of the C1 connector. | Less than 10 ohms? **YESRepair:** Use the following for potentiometer repair instructions. Reference the Marine Auxiliary QSB7-DM CM850 Fault Code Troubleshooting Manual, Bulletin 4325972, Section TF; the ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual, Bulletin [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual\|3666266]], Section TF; X15 CM2350 X125M Fault Code Troubleshooting Manual, Bulletin 5504346, Section TF; or the equipment manufacturer service information. | Repair complete |
> | Less than 10 ohms? **NORepair:** Replace the cable. | Repair complete |  |
