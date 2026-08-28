---
aliases:
  - "Переключатель блока управления дизелем не переходит в местный режим"
type: "Процедура"
doc: "116-t02-1050"
title_en: "Diesel Control Unit Local/Remote Switch Does Not Switch to Local"
title_ru: "Переключатель блока управления дизелем не переходит в местный режим"
modified: "2008-05-22"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4021617"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1050.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1050.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/116"
  - "перевод/машинный"
---

# Diesel Control Unit Local/Remote Switch Does Not Switch to Local
**Переключатель блока управления дизелем не переходит в местный режим**

> [!abstract] Процедура · `116-t02-1050`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2008-05-22
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1050.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1050.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

Двигатель **не** будет сворачиваться, когда кнопка запуска нажимается на удаленной панели.

- Дизельный блок управления локальным/удалённым переключателем делает **не** переключаться на удаленный

- Дизельный блок управления указывает на неправильное назначение

- Удаленный экран **не** переключается на локальный

- Дистанционная панель **не** переключается на удаленную

- Дистанционный пульт показывает неверное назначение.

### Как пользоваться этим деревом

По этому дереву симптомов можно вести поиск неисправности. Начните с шага 1 поиска неисправностей. На шаге 2 система задаст ряд вопросов и по симптому выдаст перечень действий по поиску неисправности.

### Практические замечания

Для запуска коленчатого механизма двигателя с удаленной панели должны быть соблюдены следующие параметры панели:

- Удаленный панельный силовой фонарь подсвечивается

- Локальная стартовая **только** лампа **не** освещена

- Двигатель должен быть остановлен.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте окно интерфейса клиента. |  |
|  | **STEP 1A.** Проверьте дисплей блока DCU410 на наличие неисправностей. |  |
|  | **STEP 1A-1.** Проверьте провод блока питания DCU410 на напряжение +24-VDC. |  |
|  | **STEP 1B.** Проверьте функцию кнопки запуска. |  |
|  | **STEP 1C** Проверить провод индикатора остановки двигателя на наличие открытого отверстия. |  |
|  | **STEP 1D.** Проверьте подачу сигнала стоп-сигнала двигателя зажигания и провода переключения остановки двигателя на предмет открытия. |  |
|  | **STEP 1E.** Проверьте провод сигнала Ethernet шины данных CAN на открытом месте. |  |
|  | **ШАГ 1F.** Проверьте указательный провод остановки двигателя на короткое расстояние от провода до провода. |  |
|  | **STEP 1G.** Проверьте подачу сигнала стоп-сигнала двигателя зажигания и провода переключения остановки двигателя для короткого провода к проводу. |  |
|  | **STEP 1H.** Проверьте провод передачи данных шины передачи данных CAN Ethernet на короткое расстояние от провода к проводу. |  |
|  | **ШАГ 1I.** Проверить проволоку с указанием остановки двигателя на короткое время до заземления. |  |
|  | **STEP 1J.** Проверьте подачу сигнала о зажигании двигателя и провода переключения остановки двигателя на короткое время до земли. |  |
|  | **STEP 1K.** Проверьте на короткое время наземный провод сигнала шины передачи данных CAN Ethernet. |  |

### ШАГ 1. Проверьте окно интерфейса клиента.

#### ШАГ 1A. Проверьте дисплей блока DCU410 на наличие неисправностей.

| **Условия:** Найдите дисплей блока DCU410. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте дисплей блока DCU410 для указания неисправностей. | DCU410 указывает на неисправность (неисправности)? *Да | 1В |
| DCU410 указывает на неисправность (неисправности)? **НЕТ** | 1А-1-1 |  |

#### ШАГ 1A-1. Проверьте провод блока питания DCU410 на напряжение +24-VDC.

| **Условия:** Откройте окно интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте напряжение на батарее 1 напряжения (переключенной мощности) в блоке DCU410. Поместите один тест на провод питания напряжения батареи 1 в блок DCU410. Поместите другой испытательный щуп на панельную площадку. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Меньше +24-VDC? *** Ремонт:** Проверить аккумуляторы. См. руководство по обслуживанию OEM. | Ремонт завершён |
| Меньше +24-VDC? **НЕТ** | 1В |  |

#### ШАГ 1B. Проверьте функцию кнопки запуска.

| **Условия:** Откройте окно интерфейса клиента. Отключите провод питания локального режима в блоке DCU410, соединениях CLU и X4. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте функцию кнопки остановки. Поместите один испытательный щуп на провод питания локального режима в блок DCU410. Поместите другой испытательный щуп на провод питания локального режима в блоке CLU. Поместите один испытательный щуп на провод питания локального режима в блок DCU410. Поместите другой испытательный щуп на провод питания локального режима в соединение X4. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да | 1С |
| Менее 10 Ом? **NORepair:** Заменить блок DCU410. Обратитесь в авторизованный сервисный центр Cummins®. | Ремонт завершён |  |

#### ШАГ 1C. Проверьте провод индикатора остановки двигателя на наличие открытого.

| **Условия:** Откройте окно интерфейса клиента. Отключите индикатор остановки двигателя и подзарядите, чтобы остановить ретрансляционные провода от блока DCU410 и блока CLU. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте провод индикатора остановки двигателя на наличие открытого. Поместите один испытательный щуп на провод подачи сигнала остановки двигателя в блок DCU410. Поместите другой испытательный щуп на провод подачи сигнала остановки двигателя в блок CLU. Поместите один испытательный щуп на подачу энергии, чтобы остановить ретрансляционный провод в блоке DCU410. Поместите другой тест на под напряжением, чтобы остановить реле обратного провода в блоке CLU. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да | 1D |
| Менее 10 Ом? **NORepair:** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |  |

#### ШАГ 1D. Проверьте подачу стоп-сигнала двигателя зажигания и провода переключения остановки двигателя для открытого.

| **Условия:** Откройте окно интерфейса клиента. Отсоедините подачу стоп-сигнала двигателя зажигания и провода переключения остановки двигателя от разъема и переключателя C1. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте подачу стоп-сигнала двигателя зажигания и провода переключения остановки двигателя для открытого. Поместите один испытательный щуп на провод подачи зажигания на разъеме С1. Поместите другой испытательный щуп на провод подачи зажигания на выключателе остановки двигателя. Поместите один испытательный щуп на провод переключателя остановки двигателя в блок DCU410. Поместите другой испытательный щуп на провод остановки двигателя на выключателе остановки двигателя. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да | 1Е |
| Менее 10 Ом? **NORepair:** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]]Замените выключатель остановки двигателя.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |  |

#### ШАГ 1E. Проверьте удаленный провод передачи данных CAN Ethernet для открытого.

| **Условия:** Откройте окно интерфейса клиента. Отключите провод передачи данных шины передачи данных CAN Ethernet на блоке DCU410 и коммутаторе Ethernet. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте удаленный провод передачи данных CAN Ethernet для открытого. Поместите один измерительный щуп на удаленную шину данных CAN Ethernet сигнального провода в блок DCU410. Поместите другой измерительный щуп на удаленный провод передачи данных CAN Ethernet на коммутаторе Ethernet. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да | 1F |
| Менее 10 Ом? **NORepair:** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |  |

#### ШАГ 1F. Проверьте провод индикатора остановки двигателя на короткое расстояние от провода к проводу.

| **Условия:** Откройте окно интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте указательный провод остановки двигателя для провода, чтобы проволочь была короткой. Поместите один испытательный щуп на провод подачи сигнала остановки двигателя в блок DCU410. Поместите другой испытательный щуп на все провода в блок DCU410. Поместите один испытательный щуп на подачу энергии, чтобы остановить ретрансляционный провод в блоке DCU410. Поместите другой тест на все другие провода в блок DCU410. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да | 1G |
| Менее 10 Ом? **NORepair:** Заменить блок DCU410. Обратитесь в авторизованный сервисный центр Cummins®. | Ремонт завершён |  |

#### ШАГ 1G. Проверьте подачу стоп-сигнала двигателя зажигания и провода переключения остановки двигателя для короткого провода к проводу.

| **Условия:** Откройте окно интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте подачу стоп-сигнала двигателя зажигания и провода переключения остановки двигателя для короткого провода к проводу. Поместите один испытательный щуп на провод подачи зажигания на разъеме С1. Поместите другой испытательный щуп на все другие провода в разъем С1. Поместите один испытательный щуп на провод переключателя остановки двигателя в блок DCU410. Поместите другой испытательный щуп на все провода в блок DCU410. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да | 1 ч. |
| Менее 10 Ом? **NORepair:** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]]Заменить DCU410. Обратитесь в авторизованный сервисный центр Cummins®. | Ремонт завершён |  |

#### ШАГ 1H. Проверьте удаленный провод передачи данных CAN Ethernet для короткого провода к проводу.

| **Условия:** Откройте окно интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте удаленный провод передачи данных CAN Ethernet для короткого провода к проводу. Поместите один измерительный щуп на удаленную шину данных CAN Ethernet сигнального провода в блок DCU410. Поместите другой испытательный щуп на все другие провода в блок DCU410. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да | 1II |
| Менее 10 Ом? **NORepair:** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |  |

#### ШАГ 1I. Проверьте проволоку индикации остановки двигателя для короткого приземления.

| **Условия:** Откройте окно интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте проволоку индикации остановки двигателя для короткого приземления. Поместите один испытательный щуп на провод подачи сигнала остановки двигателя в блок DCU410. Поместите другой испытательный щуп на панельную площадку. Поместите один испытательный щуп на подачу энергии, чтобы остановить ретрансляционный провод в блоке DCU410. Поместите другой тест на панельную площадку. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да | 1J |
| Менее 10 Ом? **NORepair:** Заменить блок DCU410. Обратитесь в авторизованный сервисный центр Cummins®. | Ремонт завершён |  |

#### ШАГ 1J. Проверьте подачу стоп-сигнала двигателя зажигания и выключите провода остановки двигателя для короткого заземления.

| **Условия:** Откройте окно интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте подачу стоп-сигнала двигателя зажигания и выключите провода остановки двигателя для короткого заземления. Поместите один испытательный щуп на провод подачи зажигания на разъеме С1. Поместите другой испытательный щуп на панельную площадку. Поместите один испытательный щуп на провод переключателя остановки двигателя в блок DCU410. Поместите другой испытательный щуп на панельную площадку. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да | 1кг |
| Менее 10 Ом? **NORepair:** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]]Заменить DCU410. Обратитесь в авторизованный сервисный центр Cummins®. | Ремонт завершён |  |

#### ШАГ 1K. Проверьте удаленный провод передачи данных CAN Ethernet для короткого приземления.

| **Условия:** Откройте окно интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте удаленный провод передачи данных CAN Ethernet для короткого приземления. Поместите один измерительный щуп на удаленную шину данных CAN Ethernet сигнального провода в блок DCU410. Поместите другой испытательный щуп на панельную площадку. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да | Обратитесь в авторизованный сервисный центр Cummins®. |
| Менее 10 Ом? **NORepair:** Заменить блок DCU410. Обратитесь в авторизованный сервисный центр Cummins®. | Ремонт завершён |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> Engine will **not** crank when the start button is pressed at the remote panel.
>
> - Diesel control unit local/remote switch does **not** to switch to remote
>
> - Diesel control unit indicates incorrect assignment
>
> - Remote panel does **not** switch to local
>
> - Remote panel does **not** switch to remote
>
> - Remote panel indicates incorrect assignment.
>
> ### How To Use This Tree
>
> This symptom tree can be used to troubleshoot a malfunction. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.
>
> ### Shoptalk
>
> To initiate engine crank from the remote panel, the following panel parameters **must** be met:
>
> - The remote panel power lamp illuminated
>
> - The local start **only** lamp is **not** illuminated
>
> - The engine **must** be stopped.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the customer interface box. |  |
> |  | **STEP 1A.** Check the DCU410 unit display for faults. |  |
> |  | **STEP 1A-1.** Check the DCU410 unit power supply wire for voltage +24-VDC. |  |
> |  | **STEP 1B.** Check the function of the start button. |  |
> |  | **STEP 1C.** Check the engine stop indication wire for an open. |  |
> |  | **STEP 1D.** Check the ignition engine stop supply and engine stop switch wires for an open. |  |
> |  | **STEP 1E.** Check the vessel remote data link Ethernet signal wire for an open. |  |
> |  | **STEP 1F.** Check the engine stop indication wire for a wire-to-wire short. |  |
> |  | **STEP 1G.** Check the ignition engine stop supply and engine stop switch wires for a wire-to-wire short. |  |
> |  | **STEP 1H.** Check the vessel remote data link Ethernet signal wire for a wire-to-wire short. |  |
> |  | **STEP 1I.** Check the engine stop indication wire for a short to ground. |  |
> |  | **STEP 1J.** Check the ignition engine stop supply and engine stop switch wires for a short to ground. |  |
> |  | **STEP 1K.** Check the vessel remote data link Ethernet signal wire for a short to ground. |  |
>
> ### STEP 1. Check the customer interface box.
>
> #### STEP 1A. Check the DCU410 unit display for faults.
>
> | **Conditions:** Locate the DCU410 unit display. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the DCU410 unit display for indication of faults. | DCU410 unit indicates fault(s)? **YES** | 1B |
> | DCU410 unit indicates fault(s)? **NO** | 1A-1 |  |
>
> #### STEP 1A-1. Check the DCU410 unit power supply wire for voltage +24-VDC.
>
> | **Conditions:** Open the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the voltage at the battery 1 voltage (switched power) at the DCU410 unit. Place one test on the battery 1 voltage supply wire at the DCU410 unit. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than +24-VDC? **YESRepair:** Check the batteries. Refer to OEM service manual. | Repair complete |
> | Less than +24-VDC? **NO** | 1B |  |
>
> #### STEP 1B. Check the function of the start button.
>
> | **Conditions:** Open the customer interface box. Disconnect the local mode supply wire at the DCU410 unit, CLU, and X4 connections. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the function of the stop button. Place one test lead on the local mode supply wire at the DCU410 unit. Place the other test lead on the local mode supply wire at the CLU unit. Place one test lead on the local mode supply wire at the DCU410 unit. Place the other test lead on the local mode supply wire at the X4 connection. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1C |
> | Less than 10 ohms? **NORepair:** Replace the DCU410 unit. Contact a Cummins® Authorized Repair Location. | Repair complete |  |
>
> #### STEP 1C. Check the engine stop indication wire for an open.
>
> | **Conditions:** Open the customer interface box. Disconnect the engine stop indication and energize to stop relay wires from the DCU410 unit and CLU unit. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the engine stop indication wire for an open. Place one test lead on the engine stop indication supply wire at the DCU410 unit. Place the other test lead on the engine stop indication supply wire at the CLU unit. Place one test lead on the energize to stop relay return wire at the DCU410 unit. Place the other test on the energize to stop relay return wire at the CLU unit. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1D |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |
>
> #### STEP 1D. Check the ignition engine stop supply and engine stop switch wires for an open.
>
> | **Conditions:** Open the customer interface box. Disconnect the ignition engine stop supply and engine stop switch wires from the C1 connector and switch. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the ignition engine stop supply and engine stop switch wires for an open. Place one test lead on the ignition stop supply wire at the C1 connector. Place the other test lead on the ignition stop supply wire at the engine stop switch. Place one test lead on the engine stop switch wire at the DCU410 unit. Place the other test lead on the engine stop switch wire at the engine stop switch. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1E |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] Replace the engine stop switch. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |
>
> #### STEP 1E. Check the vessel remote data link Ethernet signal wire for an open.
>
> | **Conditions:** Open the customer interface box. Disconnect the vessel remote data link Ethernet signal wire at the DCU410 unit and Ethernet switch. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the vessel remote data link Ethernet signal wire for an open. Place one test lead on the vessel remote data link Ethernet signal wire at the DCU410 unit. Place the other test lead on the vessel remote data link Ethernet signal wire at the Ethernet switch. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1F |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |
>
> #### STEP 1F. Check the engine stop indication wire for a wire-to-wire short.
>
> | **Conditions:** Open the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the engine stop indication wire for a wire to wire short. Place one test lead on the engine stop indication supply wire at the DCU410 unit. Place the other test lead on all wires at the DCU410 unit. Place one test lead on the energize to stop relay return wire at the DCU410 unit. Place the other test on all other wires at the DCU410 unit. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1G |
> | Less than 10 ohms? **NORepair:** Replace the DCU410 unit. Contact a Cummins® Authorized Repair Location. | Repair complete |  |
>
> #### STEP 1G. Check the ignition engine stop supply and engine stop switch wires for a wire-to-wire short.
>
> | **Conditions:** Open the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the ignition engine stop supply and engine stop switch wires for a wire-to-wire short. Place one test lead on the ignition stop supply wire at the C1 connector. Place the other test lead on all other wires at the C1 connector. Place one test lead on the engine stop switch wire at the DCU410 unit. Place the other test lead on all wires at the DCU410 unit. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1H |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] Replace the DCU410 unit. Contact a Cummins® Authorized Repair Location. | Repair complete |  |
>
> #### STEP 1H. Check the vessel remote data link Ethernet signal wire for a wire-to-wire short.
>
> | **Conditions:** Open the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the vessel remote data link Ethernet signal wire for a wire-to-wire short. Place one test lead on the vessel remote data link Ethernet signal wire at the DCU410 unit. Place the other test lead on all other wires at the DCU410 unit. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1I |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |
>
> #### STEP 1I. Check the engine stop indication wire for a short to ground.
>
> | **Conditions:** Open the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the engine stop indication wire for a short to ground. Place one test lead on the engine stop indication supply wire at the DCU410 unit. Place the other test lead on panel ground. Place one test lead on the energize to stop relay return wire at the DCU410 unit. Place the other test on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1J |
> | Less than 10 ohms? **NORepair:** Replace the DCU410 unit. Contact a Cummins® Authorized Repair Location. | Repair complete |  |
>
> #### STEP 1J. Check the ignition engine stop supply and engine stop switch wires for a short to ground.
>
> | **Conditions:** Open the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the ignition engine stop supply and engine stop switch wires for a short to ground. Place one test lead on the ignition stop supply wire at the C1 connector. Place the other test lead on panel ground. Place one test lead on the engine stop switch wire at the DCU410 unit. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1K |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] Replace the DCU410 unit. Contact a Cummins® Authorized Repair Location. | Repair complete |  |
>
> #### STEP 1K. Check the vessel remote data link Ethernet signal wire for a short to ground.
>
> | **Conditions:** Open the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the vessel remote data link Ethernet signal wire for a short to ground. Place one test lead on the vessel remote data link Ethernet signal wire at the DCU410 unit. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | Contact a Cummins® Authorized Repair Location. |
> | Less than 10 ohms? **NORepair:** Replace the DCU410 unit. Contact a Cummins® Authorized Repair Location. | Repair complete |  |
