---
aliases:
  - "Неисправности сигнала регулировки нагрузки"
type: "Процедура"
doc: "300-t02-1022"
title_en: "Load Adjust Signal Malfunctions"
title_ru: "Неисправности сигнала регулировки нагрузки"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/300/300-t02-1022.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/300-t02-1022.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/300"
  - "перевод/машинный"
---

# Load Adjust Signal Malfunctions
**Неисправности сигнала регулировки нагрузки**

> [!abstract] Процедура · `300-t02-1022`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[4332828 — Marine C Command HD Elite™ Panel System Master Repair Manual|4332828]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2019-05-22
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/300/300-t02-1022.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/300-t02-1022.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

- Двигатель **не** отвечает на запрос регулировки нагрузки.

### Как пользоваться этим деревом

Это дерево симптомов может быть использовано для устранения симптомов двигателя. Начните с шага 1 поиска неисправностей. На шаге 2 система задаст ряд вопросов и по симптому выдаст перечень действий по поиску неисправности.

### Практические замечания

Нет.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте клиентский интерфейс (C.I.B.) проводов. |  |
|  | **ШАГ 1А.** Проверьте проволоку с потенциометром с откидным регулированием. | Менее 10 Ом? |
|  | **ШАГ 1В.** Проверьте проволоку RETURN с потенциометром с откидным регулированием. | Менее 10 Ом? |
|  | **STEP 1C.** Проверьте частотный регулировочный провод SIGNAL. | Менее 10 Ом? |
| ШАГ 2. | Проверьте жгут электропроводки двигателя на C.I.B. |  |
|  | **ШАГ 2А.** Проверить частотную регулировку проводов SUPPLY и SIGNAL. | Менее 10 Ом? |
|  | **ШАГ 2В.** Проверить частотный регулировочный ВПЕРЕД и SIGNAL провода. | Менее 10 Ом? |

### ШАГ 1. Проверьте C.I.B. проводка.

#### ШАГ 1A. Проверьте проволоку с потенциометром регулировки слюны.

| **Условия: **Открыть ЦБ. Отключите компьютерную систему. к проводах двигателя упряжь кабельного разъёма С1 от C.I.B. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте проволоку с потенциометром регулировки слюны. Поместите один испытательный щуп на суп-регулировку потенциометра 5 вольт контакта питания в разъёме С1. Поместите другой испытательный щуп на потенциометр 5 вольт с отрегулировкой потемнения на разъем X1. | Менее 10 Ом? *Да | 1В |
| Менее 10 Ом? **NORepair:** Заменить провод.[[300-015-023 — Customer Interface Box\|См. процедуру 015-023 в разделе 15.]] | Ремонт завершён |  |

#### ШАГ 1B. Проверьте проволоку RETURN с потенциометром регулировки сбрасывания.

| **Условия: **Открыть ЦБ. Отключите компьютерную систему. к проводах двигателя упряжь кабельного разъёма С1 от C.I.B. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте проволоку RETURN с потенциометром регулировки сбрасывания. Поместите один испытательный щуп на обратный контакт потенциометра с откидным регулятором в разъёме C1. Поместите другой тест на обратный терминал потенциометра с откидным регулировкой на разъем X1. | Менее 10 Ом? *Да | 1С |
| Менее 10 Ом? **NORepair:** Заменить провод.[[300-015-023 — Customer Interface Box\|См. процедуру 015-023 в разделе 15.]] | Ремонт завершён |  |

#### ШАГ 1C. Проверьте частотный регулировочный провод SIGNAL.

| **Условия: **Открыть ЦБ. Отключите компьютерную систему. к проводах двигателя упряжь кабельного разъёма С1 от C.I.B. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте частотный регулировочный провод SIGNAL. Поместите один испытательный щуп на генератор выходной частоты регулировки потенциометра сигнала контакта в разъеме С1. Поместите другой испытательный щуп на выходную частоту генератора регулировки сигнального терминала потенциометра на разъем X1. | Менее 10 Ом? *Да | 2А |
| Менее 10 Ом? **NORepair:** Заменить провод.[[300-015-023 — Customer Interface Box\|См. процедуру 015-023 в разделе 15.]] | Ремонт завершён |  |

### ШАГ 2. Проверьте жгут электропроводки двигателя на C.I.B.

#### ШАГ 2A. Проверьте частотную регулировку проводов SUPPLY и SIGNAL.

| **Условия: **Отключить C.I.B. к проводах двигателя упряжь кабельного разъёма С1 от C.I.B. Отключите компьютерную систему. кабель для проводов двигателя от двигателя. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверяйте частоту регулировки проводов SUPPLY и SIGNAL. Поместите перемычку между контактом питания с потенциометром 5 вольт с регулировкой сбрасывания и контактом сигнала с выходной частотой генератора с регулировкой потенциометра в соединении на стороне двигателя. Поместите один испытательный щуп в потенциометр 5 вольт с подачей сбрасывания в контакт разъема C1. Поместите другой испытательный щуп в генератор выходной частоты регулировки потенциометра сигнала контакта разъема С1. | Менее 10 Ом? *Да | 2В |
| Менее 10 Ом? **Заменить кабель.** | Ремонт завершён |  |

#### ШАГ 2B. Проверьте частотную регулировку проводов RETURN и SIGNAL.

| **Условия: **Отключить C.I.B. к проводах двигателя упряжь кабельного разъёма С1 от C.I.B. Отсоедините C.I.B к проводах двигателя от кабеля жгута проводов. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверяйте частоту регулировки ВПЕРЕД и SIGNAL проводов. Поместите перемычку между контактом сигнала потенциометра с выходной частотой генератора и обратным контактом потенциометра с регулировкой понижания в соединении на стороне двигателя. Поместите один испытательный щуп в потенциометр обратного контакта разъема C1 с регулировкой сбрасывания. Поместите другой испытательный щуп в генератор выходной частоты регулировки потенциометра сигнала контакта разъема С1. | Менее 10 Ом? **Ремонт: **Используйте следующие инструкции по ремонту потенциометра. Ссылка на Руководство по устранению неполадок в коде CM850 морского вспомогательного QSB7-DM, Бюллетень 4325972, Раздел TF или Руководство по устранению и ремонту неполадок в электронной системе управления ISM и QSM 11, Бюллетень [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual\|3666266]], Раздел TF, Секция TF, Руководство по устранению неполадок в коде X15 CM2350 X125M, Бюллетень 5504346, Раздел TF или ссылка на информацию об услугах производителя оборудования. | Ремонт завершён |
| Менее 10 Ом? **Заменить кабель.** | Ремонт завершён |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> - Engine does **not** respond to load adjust request.
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
> |  | **STEP 1A.** Check the droop adjust potentiometer SUPPLY wire. | Less than 10 ohms? |
> |  | **STEP 1B.** Check the droop adjust potentiometer RETURN wire. | Less than 10 ohms? |
> |  | **STEP 1C.** Check the frequency adjust SIGNAL wire. | Less than 10 ohms? |
> | STEP 2. | Check the engine harness to the C.I.B. |  |
> |  | **STEP 2A.** Check the frequency adjust SUPPLY and SIGNAL wires. | Less than 10 ohms? |
> |  | **STEP 2B.** Check the frequency adjust RETURN and SIGNAL wires. | Less than 10 ohms? |
>
> ### STEP 1. Check the C.I.B. wiring.
>
> #### STEP 1A. Check the droop adjust potentiometer SUPPLY wire.
>
> | **Conditions:** Open the C.I.B. Disconnect the C.I.B. to the engine harness cable connector C1 from the C.I.B. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the droop adjust potentiometer SUPPLY wire. Place one test lead on the droop adjust potentiometer 5 volt SUPPLY pin in connector C1. Place the other test lead on the droop adjust potentiometer 5 volt supply terminal on the X1 connector. | Less than 10 ohms? **YES** | 1B |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[300-015-023 — Customer Interface Box\|Refer to Procedure 015-023 in Section 15.]] | Repair complete |  |
>
> #### STEP 1B. Check the droop adjust potentiometer RETURN wire.
>
> | **Conditions:** Open the C.I.B. Disconnect the C.I.B. to the engine harness cable connector C1 from the C.I.B. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the droop adjust potentiometer RETURN wire. Place one test lead on the droop adjust potentiometer RETURN pin in connector C1. Place the other test on droop adjust potentiometer return terminal on the X1 connector. | Less than 10 ohms? **YES** | 1C |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[300-015-023 — Customer Interface Box\|Refer to Procedure 015-023 in Section 15.]] | Repair complete |  |
>
> #### STEP 1C. Check the frequency adjust SIGNAL wire.
>
> | **Conditions:** Open the C.I.B. Disconnect the C.I.B. to the engine harness cable connector C1 from the C.I.B. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the frequency adjust SIGNAL wire. Place one test lead on the generator output frequency adjust potentiometer SIGNAL pin in connector C1. Place the other test lead on the generator output frequency adjust potentiometer signal terminal on the X1 connector. | Less than 10 ohms? **YES** | 2A |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[300-015-023 — Customer Interface Box\|Refer to Procedure 015-023 in Section 15.]] | Repair complete |  |
>
> ### STEP 2. Check the engine harness to the C.I.B.
>
> #### STEP 2A. Check the frequency adjust SUPPLY and SIGNAL wires.
>
> | **Conditions:** Disconnect the C.I.B. to the engine harness cable connector C1 from the C.I.B. Disconnect the C.I.B. to the engine harness cable from the engine. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check frequency adjust SUPPLY and SIGNAL wires. Place a jumper between the droop adjust potentiometer 5 volt SUPPLY pin and the generator output frequency adjust potentiometer SIGNAL pin in the engine-side connection. Place one test lead in the droop adjust potentiometer 5 volt SUPPLY pin of the C1 connector. Place the other test lead in the generator output frequency adjust potentiometer SIGNAL pin of the C1 connector. | Less than 10 ohms? **YES** | 2B |
> | Less than 10 ohms? **NORepair:** Replace the cable. | Repair complete |  |
>
> #### STEP 2B. Check the frequency adjust RETURN and SIGNAL wires.
>
> | **Conditions:** Disconnect the C.I.B. to the engine harness cable connector C1 from the C.I.B. Disconnect the C.I.B to engine harness cable from the engine. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check frequency adjust RETURN and SIGNAL wires. Place a jumper between the generator output frequency adjust potentiometer SIGNAL pin and the droop adjust potentiometer RETURN pin in the engine-side connection. Place one test lead in the droop adjust potentiometer RETURN pin of the C1 connector. Place the other test lead in the generator output frequency adjust potentiometer SIGNAL pin of the C1 connector. | Less than 10 ohms? **YESRepair:** Use the following for potentiometer repair instructions. Reference the Marine Auxiliary QSB7-DM CM850 Fault Code Troubleshooting Manual, Bulletin 4325972, Section TF, or the ISM and QSM 11 Electronic Control System Troubleshooting and Repair Manual, Bulletin [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual\|3666266]], Section TF, X15 CM2350 X125M Fault Code Troubleshooting Manual, Bulletin 5504346, Section TF or refer to the equipment manufacturer service information. | Repair complete |
> | Less than 10 ohms? **NORepair:** Replace the cable. | Repair complete |  |
