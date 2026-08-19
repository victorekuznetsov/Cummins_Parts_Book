---
aliases:
  - "Не работает функция отключения звука на дистанционном пульте"
type: "Процедура"
doc: "115-t02-1038"
title_en: "Remote Panel Silence Function Not Working"
title_ru: "Не работает функция отключения звука на дистанционном пульте"
modified: "2006-06-12"
engines:
  - "41349633"
families:
  - "QSK19"
manuals:
  - "4021587"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/115/115-t02-1038.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/115-t02-1038.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/115"
  - "перевод/машинный"
---

# Remote Panel Silence Function Not Working
**Не работает функция отключения звука на дистанционном пульте**

> [!abstract] Процедура · `115-t02-1038`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021587 — C Command Panel System Marine Master Repair Manual|4021587]]
> **Секции:** Section TT — Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2006-06-12
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/115/115-t02-1038.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/115-t02-1038.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

- Buzzer будет **не** молчать, когда кнопка тишины нажата на удаленную панель.

- Buzzer замолчит, когда кнопка тишины нажимается на панель машинного отделения.

### Как пользоваться этим деревом

Это дерево симптомов может быть использовано для устранения симптомов тревожного молчания. Начните с шага 1 поиска неисправностей. На шаге 2 система задаст ряд вопросов и по симптому выдаст перечень действий по поиску неисправности.

### Практические замечания

Панель машинного отделения и удаленная панель имеют кнопку тишины. ECM доставляет информацию тревоги в логический блок клиентского интерфейса. Логический блок клиентского интерфейса доставляет информацию о тревоге на панель машинного отделения и удаленную панель. Панель машинного отделения и пульт дистанционного управления доставляют оператору сигнализацию в визуальном и звуковом формате. Кнопка тишины позволяет заглушить звуковой сигнал тревоги.

Когда возникает состояние тревоги, звуковой сигнал тревоги может быть отключен на всех панелях, нажав кнопку тишины на любой панели.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте удаленную панель |  |
|  | **ШАГ 1А.** Проверьте кнопку тишины | Сопротивление менее 10 Ом? |
| ШАГ 2. | Проверьте панельную систему кабеля |  |
|  | **STEP 2A.** Проверить кабель дистанционной панели | Сопротивление менее 10 Ом? |
| ШАГ 3. | Проверка проводки интерфейсной коробки заказчика |  |
|  | **STEP 3A.** Проверьте беспроводную систему дистанционного оповещения о тревоге | Сопротивление менее 10 Ом? |

### ШАГ 1. Проверьте удаленную панель

#### ШАГ 1A. Проверить кнопку тишины

| **Условия:** Выключите питание панели машинного отделения Найти удаленную панель Отключить провода от панели управления разъемом Х4. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте функцию кнопки тишины: Поместите один испытательный щуп на терминал питания пульта дистанционного питания распределителя разъёма панели управления X4. Поместите другой испытательный щуп на удаленный панельный терминал подачи сигнала тревоги разъема панели управления X4. Нажмите кнопку молчания. | Сопротивление менее 10 Ом? *Да** | 2В |
| Сопротивление менее 10 Ом? **NORepair:** Заменить панель управления. См. процедуру[[115-015-024 — Engine Room Panel\|015-024]]. | Ремонт завершён. |  |

### ШАГ 2. Проверьте панельную систему кабеля

#### ШАГ 2A. Проверьте удаленный панельный кабель

| **Условия: ** Найти и открыть окно клиентского интерфейса Отключить кабель удаленной панели от окна клиентского интерфейса X4 Разъем Найти и открыть удаленную панель. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте кабель удаленной панели. Установите перемычку между терминалом питания переключателя удаленной панели и терминалом питания аварийной тишины удаленной панели на панели дистанционного управления X4 в панели дистанционного управления. Поместите один испытательный щуп на терминал питания переключателя удаленной панели в кабель удаленной панели. Поместите другой испытательный щуп на терминал подачи сигнала тревоги удаленной панели в кабель удаленной панели. | Сопротивление менее 10 Ом? *Да** | 3А |
| Сопротивление менее 10 Ом? **Заменить кабель.** | Ремонт завершён. |  |

### ШАГ 3. Проверка проводки интерфейсной коробки заказчика

#### ШАГ 3A. Проверить удаленную панель сигнализации Silence Wire

| ** Условия: ** Откройте окно интерфейса клиента |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте провод питания пульта дистанционного управления. Поместите один испытательный щуп на провод питания аварийной тишины удаленной панели на разъеме интерфейса клиента X4. Поместите другой испытательный щуп на удаленную панель терминала подачи сигнала тревоги на логический блок окна интерфейса клиента. | Сопротивление менее 10 Ом? **** Заменить логический блок клиентского интерфейса. См. процедуру[[115-015-023 — Customer Interface Box\|015-023]]. | Ремонт завершён. |
| Сопротивление менее 10 Ом? **NORepair:** Заменить провод. См. процедуру[[115-015-023 — Customer Interface Box\|015-023]]. | Ремонт завершён. |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> - Buzzer will **not** silence when silence button pushed at remote panel.
>
> - Buzzer will silence when silence button pushed at engine room panel.
>
> ### How To Use This Tree
>
> This symptom tree can be used to troubleshoot alarm silence symptoms. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.
>
> ### Shoptalk
>
> The engine room panel and remote panel each have a silence button. The ECM delivers alarm information to the customer interface box logic unit. The customer interface box logic unit delivers alarm information to the engine room panel and remote panel. The engine room panel and remote panel deliver alarm information to the operator in visual and audible format. A silence button allows the audible alarm to be silenced.
>
> When an alarm condition occurs the audible alarm can be shut off at all panels by pressing the silence button at any panel.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check Remote Panel |  |
> |  | **STEP 1A.** Check Silence Button | Less than 10 ohms resistance? |
> | STEP 2. | Check Panel System Cable |  |
> |  | **STEP 2A.** Check Remote Panel Cable | Less than 10 ohms resistance? |
> | STEP 3. | Check Customer Interface Box Wiring |  |
> |  | **STEP 3A.** Check Remote Panel Alarm Silence Supply Wire | Less than 10 ohms resistance? |
>
> ### STEP 1. Check Remote Panel
>
> #### STEP 1A. Check Silence Button
>
> | **Conditions:** Turn engine room panel power switch off Locate remote panel Disconnect wires from control panel X4 connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Verify silence button function: Place one test lead on the remote panel power switch supply terminal of the control panel X4 connector. Place the other test lead on the remote panel alarm silence supply terminal of the control panel X4 connector. Press the silence button. | Less than 10 ohms resistance? **YES** | 2B |
> | Less than 10 ohms resistance? **NORepair:** Replace the control panel. Refer to Procedure [[115-015-024 — Engine Room Panel\|015-024]]. | Repair complete. |  |
>
> ### STEP 2. Check Panel System Cable
>
> #### STEP 2A. Check Remote Panel Cable
>
> | **Conditions:** Locate and open customer interface box Disconnect remote panel cable from customer interface box X4 connector Locate and open remote panel. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the remote panel cable. Install a jumper between remote panel power switch supply terminal and the remote panel alarm silence supply terminal on remote control panel X4 in the remote control panel. Place one test lead on the remote panel power switch supply terminal in the remote panel cable. Place the other test lead on the remote panel alarm silence supply terminal in the remote panel cable. | Less than 10 ohms resistance? **YES** | 3A |
> | Less than 10 ohms resistance? **NORepair:** Replace the cable. | Repair complete. |  |
>
> ### STEP 3. Check Customer Interface Box Wiring
>
> #### STEP 3A. Check Remote Panel Alarm Silence Supply Wire
>
> | **Conditions:** Open the customer interface box |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the remote panel alarm silence supply wire. Place one test lead on the remote panel alarm silence supply wire on the customer interface box X4 connector. Place the other test lead on the remote panel alarm silence supply terminal on the customer interface box logic unit. | Less than 10 ohms resistance? **YESRepair:** Replace the customer interface box logic unit. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |
> | Less than 10 ohms resistance? **NORepair:** Replace the wire. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |  |
