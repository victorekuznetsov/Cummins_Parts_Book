---
aliases:
  - "Не работает функция отключения звука на дистанционном пульте"
type: "Процедура"
doc: "116-t02-1038"
title_en: "Remote Panel Silence Function Not Working"
title_ru: "Не работает функция отключения звука на дистанционном пульте"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1038.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1038.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/116"
  - "перевод/машинный"
---

# Remote Panel Silence Function Not Working
**Не работает функция отключения звука на дистанционном пульте**

> [!abstract] Процедура · `116-t02-1038`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2008-05-22
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1038.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1038.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

- Сигнализация **не** заставит замолчать, когда кнопка тишины нажата на удаленную панель

- Сигнал тревоги замолчит, когда на блок DCU410 нажата кнопка тишины.

### Как пользоваться этим деревом

По этому дереву симптомов можно вести поиск неисправности. Начните с шага 1 поиска неисправностей. На шаге 2 система задаст ряд вопросов и по симптому выдаст перечень действий по поиску неисправности.

### Практические замечания

Установка DCU410 и удаленные панели имеют кнопку тишины. ECM доставляет информацию тревоги в логический блок клиентского интерфейса. Логический блок клиентского интерфейса доставляет информацию тревоги в блок DCU410 и удаленную панель. Блок DCU410 и удаленная панель передают оператору сигнализацию в визуальном и звуковом формате. Кнопка тишины позволяет заглушить звуковой сигнал тревоги.

Когда возникает состояние тревоги, звуковой сигнал тревоги может быть отключен на всех панелях, нажав кнопку тишины в любом удаленном месте панели.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте окно интерфейса клиента. |  |
|  | **STEP 1A.** Проверьте дисплей блока DCU410 на наличие неисправностей. |  |
|  | **STEP 1A-1.** Проверьте провод блока питания DCU410 на напряжение +24-VDC. |  |
| ШАГ 2. | Проверьте сигнализацию удаленной панели. |  |
|  | **STEP 2A.** Проверьте кнопку тишины на блоке DCU410 и удаленной панели. |  |
| ШАГ 3. | Проверьте проводку удаленной панели. |  |
|  | **STEP 3A.** Проверьте провод питания пульта дистанционного управления на наличие открытого. |  |

### ШАГ 1. Проверьте окно интерфейса клиента.

#### ШАГ 1A. Проверьте дисплей блока DCU410 на наличие неисправностей.

| **Условия: **Найдите дисплей блока DCU410. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте дисплей блока DCU410 для указания неисправностей. | DCU410 указывает на неисправность (неисправности)? *Да | 2А |
| DCU410 указывает на неисправность (неисправности)? **НЕТ** | 1А-1-1 |  |

#### ШАГ 1A-1. Проверьте провод блока питания DCU410 на напряжение +24-VDC.

| **Условия: **Откройте окно интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте напряжение на батарее 1 напряжения (переключенной мощности) в блоке DCU410. Поместите один тест на провод питания напряжения батареи 1 в блок DCU410. Поместите другой испытательный щуп на панельную площадку. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Меньше +24-VDC? **Ремонт:** Проверить аккумуляторы. См. руководство по обслуживанию OEM. | Ремонт завершён |
| Меньше +24-VDC? **НЕТ** | 2А |  |

### ШАГ 2. Проверьте сигнализацию удаленной панели.

#### ШАГ 2A. Проверьте, работает ли кнопка тишины.

| **Условия: **Откройте окно интерфейса клиента. Поверните DCU410 и переключитесь на удаленную панель в положение выключения. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте кнопку тишины на блоке DCU410 и удаленной панели. Поместите один испытательный щуп на провод питания выключателя удаленной панели в соединение X4. Поместите другой испытательный щуп на провод подачи сигнала тревоги на удаленной панели в соединение X4. Нажмите кнопку молчания. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да | 3А |
| Менее 10 Ом? **NORepair:** Заменить пульт дистанционного управления. Обратитесь в авторизованный сервисный центр Cummins®. | Ремонт завершён |  |

### ШАГ 3. Проверьте проводку удаленной панели.

#### ШАГ 3A. Проверьте провод питания пульта дистанционного питания для открытого.

| **Условия: **Откройте окно интерфейса клиента. Отключите провод питания сигнализации удаленной панели на блоке DCU410 и соединении X4. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте провод питания пульта дистанционного питания для открытого. Поместите один испытательный щуп на провод питания сигнализации тишины на удаленной панели в блоке DCU410. Поместите другой испытательный щуп на провод питания сигнализации тишины удаленной панели на соединение X4. См. соответствующую схему или схему проводов для идентификации штифта и провода. | Менее 10 Ом? *Да | Обратитесь в авторизованный сервисный центр Cummins®. |
| Менее 10 Ом? **NORepair:** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> - Alarm will **not** silence when silence button is pushed on remote panel
>
> - Alarm will silence when silence button is pushed on DCU410 unit.
>
> ### How To Use This Tree
>
> This symptom tree can be used to troubleshoot a malfunction. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.
>
> ### Shoptalk
>
> The DCU410 unit and remote panels each have a silence button. The ECM delivers alarm information to the customer interface box logic unit. The customer interface box logic unit delivers alarm information to the DCU410 unit and remote panel. The DCU410 unit and remote panel deliver alarm information to the operator in visual and audible format. A silence button allows the audible alarm to be silenced.
>
> When an alarm condition occurs the audible alarm can be shut off at all panels by pressing the silence button at any remote panel location.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the customer interface box. |  |
> |  | **STEP 1A.** Check the DCU410 unit display for faults. |  |
> |  | **STEP 1A-1.** Check the DCU410 unit power supply wire for voltage +24-VDC. |  |
> | STEP 2. | Check the remote panel alarm. |  |
> |  | **STEP 2A.** Check the silence button at the DCU410 unit and remote panel. |  |
> | STEP 3. | Check the remote panel wiring. |  |
> |  | **STEP 3A.** Check the remote panel power switch supply wire for an open. |  |
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
> ### STEP 2. Check the remote panel alarm.
>
> #### STEP 2A. Verify the silence button is functioning.
>
> | **Conditions:** Open the customer interface box. Turn the DCU410 and remote panel switch to the OFF position. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the silence button at the DCU410 unit and remote panel. Place one test lead on the remote panel power switch supply wire at the X4 connection. Place the other test lead on the remote panel alarm silence supply wire at the X4 connection. Press the silence button. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 3A |
> | Less than 10 ohms? **NORepair:** Replace the remote panel. Contact a Cummins® Authorized Repair Location. | Repair complete |  |
>
> ### STEP 3. Check the remote panel wiring.
>
> #### STEP 3A. Check the remote panel power switch supply wire for an open.
>
> | **Conditions:** Open the customer interface box. Disconnect the remote panel alarm supply wire at the DCU410 unit and X4 connection. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the remote panel power switch supply wire for an open. Place one test lead on the remote panel silence alarm supply wire at the DCU410 unit. Place the other test lead on the remote panel silence alarm supply wire at the X4 connection. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | Contact a Cummins® Authorized Repair Location. |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |
