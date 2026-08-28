---
aliases:
  - "Двигатель не останавливается ни от блока управления, ни с дистанционного пульта"
type: "Процедура"
doc: "116-t02-1048"
title_en: "Engine Will Not Stop from Diesel Control Unit or Remote Panel"
title_ru: "Двигатель не останавливается ни от блока управления, ни с дистанционного пульта"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1048.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1048.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/116"
  - "перевод/машинный"
---

# Engine Will Not Stop from Diesel Control Unit or Remote Panel
**Двигатель не останавливается ни от блока управления, ни с дистанционного пульта**

> [!abstract] Процедура · `116-t02-1048`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2008-05-22
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1048.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1048.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

- Двигатель не реагирует на остановку двигателя.

- Двигатель самопроизвольно останавливается.

### Как пользоваться этим деревом

По этому дереву симптомов можно вести поиск неисправности. Начните с шага 1 поиска неисправностей. На шаге 2 система задаст ряд вопросов и по симптому выдаст перечень действий по поиску неисправности.

### Практические замечания

Двигатель можно остановить, нажав кнопку остановки на блоке DCU410 или удаленной панели.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте окно интерфейса клиента. |  |
|  | **STEP 1A.** Проверьте дисплей блока DCU410 на наличие неисправностей. |  |
|  | **STEP 1A-1.** Проверьте провод блока питания DCU410 на напряжение +24-VDC. |  |
| ШАГ 2. | Проверьте клиентский интерфейс коробки проводов. |  |
|  | **STEP 2A.** Проверьте переключаемый входной источник питания 2 провода на наличие открытого. |  |
|  | **STEP 2B.** Проверьте провод дистанционного питания на наличие открытого. |  |
|  | **STEP 2C.** Проверьте проволоку подачи сигнала остановки двигателя на предмет наличия открытого отверстия. |  |
|  | **STEP 2D.** Проверьте заряд энергии, чтобы остановить ретрансляционный провод для открытия в блоке DCU410 и блоке CLU. |  |
| ШАГ 3. | Проверьте кнопку остановки двигателя. |  |
|  | **STEP 3A.** Проверить мощность сигнального провода на блоке SDU410 и выключателе остановки двигателя. |  |
|  | **STEP 3B.** Проверьте провод подачи зажигания (остановка двигателя) на разъеме С1 и выключателе остановки двигателя. |  |

### ШАГ 1. Проверьте окно интерфейса клиента.

#### ШАГ 1A. Проверьте дисплей блока DCU410 на наличие неисправностей.

| **Условия:** Найдите дисплей блока DCU410. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте дисплей блока DCU410 для указания неисправностей. | DCU410 указывает на неисправность (неисправности)? *Да | 2А |
| DCU410 указывает на неисправность (неисправности)? **НЕТ** | 1А-1-1 |  |

#### ШАГ 1A-1. Проверьте провод блока питания DCU410 на напряжение +24-VDC.

| **Условия:** Откройте окно интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте напряжение на батарее 1 напряжения (переключенной мощности) в блоке DCU410. Поместите один тест на провод питания напряжения батареи 1 в блок DCU410. Поместите другой испытательный щуп на панельную площадку. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Меньше +24-VDC? *** Ремонт:** Проверить аккумуляторы. См. руководство по обслуживанию OEM. | Ремонт завершён |
| Меньше +24-VDC? **НЕТ** | 2А |  |

### ШАГ 2. Проверьте клиентский интерфейс коробки проводов.

#### ШАГ 2A. Проверьте переключаемый входной источник питания 2 провода на наличие открытого.

| **Условия:** Откройте окно интерфейса клиента. Отключите переключаемый входной источник питания 2 провода от блока DCU410 и разъема X4. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте переключаемый входной источник питания 2 провода на наличие открытого. Поместите один испытательный щуп на переключенный входной провод 2 питания в блок DCU410. Поместите другой испытательный щуп на переключенный входной провод 2 питания в соединение X4. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да | 2В |
| Менее 10 Ом? **NORepair:** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |  |

#### ШАГ 2B. Проверьте провод дистанционного питания для открытия.

| **Условия:** Откройте окно интерфейса клиента. Отключите переключаемый входной источник питания 2 провода от блока DCU410 и соединения X4. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте провод дистанционного питания для открытия. Поместите один испытательный щуп на провод дистанционного остановочного питания в блок DCU410. Поместите другой испытательный щуп на провод дистанционного остановки питания в соединение X4. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да | 2C |
| Менее 10 Ом? **NORepair:** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |  |

#### ШАГ 2C. Проверьте проволоку подачи сигнала остановки двигателя на наличие открытого.

| **Условия:** Откройте окно интерфейса клиента. Отсоедините провод подачи сигнала остановки двигателя на блоке DCU410 и блоке CLU. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте проволоку подачи сигнала остановки двигателя на наличие открытого. Поместите один испытательный щуп на провод подачи сигнала остановки двигателя в блок DCU410. Поместите другой испытательный щуп на провод подачи сигнала остановки двигателя в блок CLU. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да | 2D |
| Менее 10 Ом? **NORepair:** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |  |

#### ШАГ 2D. Проверьте заряд энергии, чтобы остановить обратный провод реле для открытия в блоке DCU410 и блоке CLU.

| **Условия:** Откройте окно интерфейса клиента. Отключите под напряжением, чтобы остановить ретрансляционный провод реле на блоке DCU410 и блоке CLU. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте заряд энергии, чтобы остановить обратный провод реле для открытия в блоке DCU410 и блоке CLU. Поместите один испытательный щуп на подачу энергии, чтобы остановить ретрансляционный провод в блоке DCU410. Поместите другой испытательный щуп на под напряжением, чтобы остановить ретрансляционный провод в блоке CLU. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да | 3А |
| Менее 10 Ом? **NORepair:** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |  |

### ШАГ 3. Проверьте кнопку остановки двигателя.

#### ШАГ 3A. Проверьте мощность сигнального провода на блоке SDU410 и выключателе остановки двигателя.

| **Условия:** Откройте окно интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте мощность сигнального провода на блоке SDU410 и выключателе остановки двигателя. Поместите один испытательный щуп на мощность на сигнальном проводе в блоке SDU410. Поместите другой испытательный щуп на выключатель остановки двигателя. Управляйте выключателем остановки двигателя. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да | 3B |
| Менее 10 Ом? **NORepair:** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]]Замените выключатель остановки двигателя.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |  |

#### ШАГ 3B. Проверьте провод подачи зажигания (остановка двигателя) на разъеме C1 и выключателе остановки двигателя.

| **Условия:** Откройте окно интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте провод подачи зажигания (остановка двигателя) на разъеме C1 и выключателе остановки двигателя. Поместите один испытательный щуп на провод подачи зажигания (остановка двигателя) на разъем С1. Поместите другой испытательный щуп на выключатель остановки двигателя. Управляйте выключателем остановки двигателя. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да | Обратитесь в авторизованный сервисный центр Cummins®. |
| Менее 10 Ом? **NORepair:** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]]Замените выключатель остановки двигателя.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> - Engine does **not** respond to engine stop.
>
> - Engine executes un-requested engine stop.
>
> ### How To Use This Tree
>
> This symptom tree can be used to troubleshoot a malfunction. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.
>
> ### Shoptalk
>
> The engine can be stopped by pushing the stop button on the DCU410 unit or remote panel.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the customer interface box. |  |
> |  | **STEP 1A.** Check the DCU410 unit display for faults. |  |
> |  | **STEP 1A-1.** Check the DCU410 unit power supply wire for voltage +24-VDC. |  |
> | STEP 2. | Check the customer interface box wiring. |  |
> |  | **STEP 2A.** Check the switched inputs power supply 2 wire for an open. |  |
> |  | **STEP 2B.** Check the remote stop supply wire for an open. |  |
> |  | **STEP 2C.** Check the engine stop indication supply wire for an open. |  |
> |  | **STEP 2D.** Check the energize to stop relay return wire for an open at the DCU410 unit and CLU unit. |  |
> | STEP 3. | Check the engine stop button. |  |
> |  | **STEP 3A.** Check the power on signal wire at the SDU410 unit and engine stop switch. |  |
> |  | **STEP 3B.** Check the ignition (engine stop) supply wire at the C1 connector and engine stop switch. |  |
>
> ### STEP 1. Check the customer interface box.
>
> #### STEP 1A. Check the DCU410 unit display for faults.
>
> | **Conditions:** Locate the DCU410 unit display. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the DCU410 unit display for indication of faults. | DCU410 unit indicates fault(s)? **YES** | 2A |
> | DCU410 unit indicates fault(s)? **NO** | 1A-1 |  |
>
> #### STEP 1A-1. Check the DCU410 unit power supply wire for voltage +24-VDC.
>
> | **Conditions:** Open the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the voltage at the battery 1 voltage (switched power) at the DCU410 unit. Place one test on the battery 1 voltage supply wire at the DCU410 unit. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than +24-VDC? **YESRepair:** Check the batteries. Refer to OEM service manual. | Repair complete |
> | Less than +24-VDC? **NO** | 2A |  |
>
> ### STEP 2. Check the customer interface box wiring.
>
> #### STEP 2A. Check the switched inputs power supply 2 wire for an open.
>
> | **Conditions:** Open the customer interface box. Disconnect the switched inputs power supply 2 wire from the DCU410 unit and the X4 connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the switched inputs power supply 2 wire for an open. Place one test lead on the switched inputs power supply 2 wire at the DCU410 unit. Place the other test lead on the switched inputs power supply 2 wire at the X4 connection. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 2B |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |
>
> #### STEP 2B. Check the remote stop supply wire for an open.
>
> | **Conditions:** Open the customer interface box. Disconnect the switched inputs power supply 2 wire from the DCU410 unit and the X4 connection. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the remote stop supply wire for an open. Place one test lead on the remote stop supply wire at the DCU410 unit. Place the other test lead on the remote stop supply wire at the X4 connection. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 2C |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |
>
> #### STEP 2C. Check the engine stop indication supply wire for an open.
>
> | **Conditions:** Open the customer interface box. Disconnect the engine stop indication supply wire at the DCU410 unit and the CLU unit. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the engine stop indication supply wire for an open. Place one test lead on the engine stop indication supply wire at the DCU410 unit. Place the other test lead on the engine stop indication supply wire at the CLU unit. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 2D |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |
>
> #### STEP 2D. Check the energize to stop relay return wire for an open at the DCU410 unit and CLU unit.
>
> | **Conditions:** Open the customer interface box. Disconnect the energize to stop relay return wire at the DCU410 unit and CLU unit. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the energize to stop relay return wire for an open at the DCU410 unit and CLU unit. Place one test lead on the energize to stop relay return wire at the DCU410 unit. Place the other test lead on the energize to stop relay return wire at the CLU unit. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 3A |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |
>
> ### STEP 3. Check the engine stop button.
>
> #### STEP 3A. Check the power on signal wire at the SDU410 unit and engine stop switch.
>
> | **Conditions:** Open the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the power on signal wire at the SDU410 unit and engine stop switch. Place one test lead on the power on signal wire at the SDU410 unit. Place the other test lead on the engine stop switch. Operate the engine stop switch. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 3B |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] Replace the engine stop switch. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |
>
> #### STEP 3B. Check the ignition (engine stop) supply wire at the C1 connector and engine stop switch.
>
> | **Conditions:** Open the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the ignition (engine stop) supply wire at the C1 connector and engine stop switch. Place one test lead on the ignition (engine stop) supply wire at the C1 connector. Place the other test lead on the engine stop switch. Operate the engine stop switch. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | Contact a Cummins® Authorized Repair Location. |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] Replace the engine stop switch. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |
