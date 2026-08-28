---
aliases:
  - "Блок останова самопроизвольно останавливает двигатель"
type: "Процедура"
doc: "116-t02-1080"
title_en: "Shutdown Unit Shuts Engine Down Un-Requested"
title_ru: "Блок останова самопроизвольно останавливает двигатель"
modified: "2009-07-15"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4021617"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1080.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1080.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/116"
  - "перевод/машинный"
---

# Shutdown Unit Shuts Engine Down Un-Requested
**Блок останова самопроизвольно останавливает двигатель**

> [!abstract] Процедура · `116-t02-1080`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2009-07-15
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1080.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1080.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

- SDU410 отключит двигатель с переключателем зажигания в положении ON. Открытое существует в мощности на цепи питания и сигнала.

### Как пользоваться этим деревом

По этому дереву симптомов можно вести поиск неисправности. Начните с шага 1 поиска неисправностей. На шаге 2 система задаст ряд вопросов и по симптому выдаст перечень действий по поиску неисправности.

### Практические замечания

Входные сигналы SDU410 являются переключателями. Эти переключатели обычно открыты и закрыты для активации отключения.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте интерфейс клиента |  |
|  | **STEP 1A.** Проверьте логическую блокировку светодиодного освещения в интерфейсе клиента. | Активны ли какие-либо сигналы тревоги или светодиоды освещены? |
|  | **STEP 1B.** Проверьте провод электропитания SDU410 на +24-VDC. | Меньше +24-VDC? |
| ШАГ 2. | Проверка проводки интерфейсной коробки заказчика |  |
|  | **ШАГ 2А.** Проверить мощность на питающих и сигнальных проводах на наличие открытого. | Менее 10 Ом? |
|  | **STEP 2B.** Проверьте мощность на питающих и сигнальных проводах на напряжение. | Меньше +24-VDC? |
| ШАГ 3. | Проверьте OEM-проводку для кабеля интерфейса клиента |  |
|  | **STEP 3A.** Проверьте проволоку подачи зажигания (остановка двигателя) на предмет наличия открытого зажигания. | Менее 10 Ом? |

### ШАГ 1. Проверьте интерфейс клиента

#### ШАГ 1A. Проверьте логическое устройство клиентского интерфейса LED подсветка.

| **Условия:** Проверьте устройство DCU410 на наличие сигнализации и светодиодной подсветки. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте наличие сигнализации и светодиодной подсветки на устройстве DCU410. | Активны ли какие-либо сигналы тревоги или светодиоды освещены? *Да | Свяжитесь с авторизованным местом ремонта Cummins® |
| Активны ли какие-либо сигналы тревоги или светодиоды освещены? **НЕТ** | 1В |  |

#### ШАГ 1B. Проверьте провод питания DCU410 для +24-VDC.

| **Условия: **Откройте окно интерфейса клиента |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте напряжение на блоке отключения питания 24-VDC на блоке SDU410. Поместите один испытательный щуп на блок отключения питания 24-VDC на блоке питания SDU410. Поместите другой испытательный щуп на провод возврата блока отключения в блок SDU410. См. соответствующую схему или схему проводов для идентификации соединительного штифта. | Меньше +24-VDC? **Ремонт:** Проверить аккумуляторы. См. руководство по обслуживанию OEM или свяжитесь с авторизованным местом ремонта Cummins®. | Ремонт завершён |
| Меньше +24-VDC? **НЕТ** | 2А |  |

### ШАГ 2. Проверка проводки интерфейсной коробки заказчика

#### ШАГ 2A. Проверьте мощность на подаче и сигнальных проводах на наличие открытого.

| **Условия: **Откройте окно интерфейса клиента Отключите провод на питании на питании и питание на сигнальных проводах на блоке SDU410 и питание на питающих и сигнальных проводах на логическом блоке клиента. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте мощность на подаче и сигнальных проводах на наличие открытого. Поместите один испытательный щуп на питание на проводе питания в блоке SDU410. Поместите другой измерительный щуп на питание на проводе питания в логический блок клиентского интерфейса. Поместите один испытательный щуп на мощность на сигнальном проводе в блоке SDU410. Поместите другой измерительный щуп на мощность на сигнальном проводе в логический блок окна интерфейса клиента. См. соответствующую схему или схему проводов для идентификации соединительного штифта. | Менее 10 Ом? *Да | 2В |
| Менее 10 Ом? **NORepair:** Заменить провод.[[116-015-023 — Customer Interface Box\|См. процедуру 015-023 (Customer Interface Box) в разделе 15.]] | Ремонт завершён |  |

#### ШАГ 2B. Проверьте мощность на питающих и сигнальных проводах на напряжение.

| **Условия: **Откройте окно интерфейса клиента. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте мощность на питающих и сигнальных проводах на напряжение. Поместите один испытательный щуп на питание на проводе питания в блоке SDU410. Поместите другой испытательный щуп на землю панели. Поместите один измерительный щуп на мощность на сигнальном проводе в блок логики интерфейса клиента. Поместите другой испытательный щуп на землю панели. См. соответствующую схему или схему проводов для идентификации соединительного штифта. | Меньше +24-VDC? Заменить модуль SDU410. Обратитесь в авторизованный сервисный центр Cummins®. | 3А |
| Меньше +24-VDC? **НЕТ** | Ремонт завершён |  |

### ШАГ 3. Проверьте OEM-проводку для кабеля интерфейса клиента

#### ШАГ 3A. Проверьте провод подачи зажигания (остановка двигателя) на наличие открытого.

| **Условия: **Отсоедините окно интерфейса клиента к OEM-проводах, подключите кабельный разъем C1 от окна интерфейса клиента. Отсоедините проводку OEM от разъема C1 на двигателе. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте провод подачи зажигания (остановка двигателя) на наличие открытого. Поместите перемычку между зажиганием (остановкой двигателя) в разъем С1. Поместите один испытательный щуп на штифт зажигания (остановка двигателя) в разъем OEM на двигателе. Поместите другой испытательный щуп на штифт зажигания (остановка двигателя) на разъем С8. См. соответствующую схему или схему проводов для идентификации соединительного штифта. | Менее 10 Ом? *Да | Ремонт завершён |
| Менее 10 Ом? **NORepair:** Заменить проводку OEM. См. инструкции по установке OEM. | Свяжитесь с авторизованным местом ремонта Cummins® |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> - The SDU410 will shut down the engine with ignition keyswitch in the ON position. An open exists in the power on supply and signal circuit.
>
> ### How To Use This Tree
>
> This symptom tree can be used to troubleshoot a malfunction. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.
>
> ### Shoptalk
>
> The SDU410 input signals are switches. These switches are normally open and closed to activate a shutdown.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check customer interface box |  |
> |  | **STEP 1A.** Check the customer interface box logic unit LED illumination. | Are any alarms active or LEDs illuminated? |
> |  | **STEP 1B.** Check the SDU410 power supply wire for +24-VDC. | Less than +24-VDC? |
> | STEP 2. | Check customer interface box wiring |  |
> |  | **STEP 2A.** Check the power on supply and signal wires for an open. | Less than 10 ohms? |
> |  | **STEP 2B.** Check the power on supply and signal wires for voltage. | Less than +24-VDC? |
> | STEP 3. | Check the OEM harness to customer interface box cable |  |
> |  | **STEP 3A.** Check the ignition (engine stop) supply wire for an open. | Less than 10 ohms? |
>
> ### STEP 1. Check customer interface box
>
> #### STEP 1A. Check the customer interface box logic unit LED illumination.
>
> | **Conditions:** Check the DCU410 unit for alarms and LED illumination. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for alarms and LED illumination on the DCU410 unit. | Are any alarms active or LEDs illuminated? **YES** | Contact a Cummins® Authorized Repair Location |
> | Are any alarms active or LEDs illuminated? **NO** | 1B |  |
>
> #### STEP 1B. Check the DCU410 power supply wire for +24-VDC.
>
> | **Conditions:** Open the customer interface box |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the voltage at the shutdown unit supply 24-VDC at the SDU410 unit. Place one test lead on the shutdown unit supply 24-VDC supply wire at the SDU410 unit. Place the other test lead on the shutdown unit return wire at the SDU410 unit. Refer to the appropriate circuit diagram or wiring diagram for connection pin identification. | Less than +24-VDC? **YESRepair:** Check the batteries. Refer to the OEM service manual or contact a Cummins® Authorized Repair Location. | Repair complete |
> | Less than +24-VDC? **NO** | 2A |  |
>
> ### STEP 2. Check customer interface box wiring
>
> #### STEP 2A. Check the power on supply and signal wires for an open.
>
> | **Conditions:** Open the customer interface box Disconnect the wire at the power on supply and power on signal wires at the SDU410 unit and the power on supply and signal wires at the customer logic unit. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the power on supply and signal wires for an open. Place one test lead on the power on supply wire at the SDU410 unit. Place the other test lead on the power on supply wire at the customer interface box logic unit. Place one test lead on the power on signal wire at the SDU410 unit. Place the other test lead on the power on signal wire at the customer interface box logic unit. Refer to the appropriate circuit diagram or wiring diagram for connection pin identification. | Less than 10 ohms? **YES** | 2B |
> | Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |
>
> #### STEP 2B. Check the power on supply and signal wires for voltage.
>
> | **Conditions:** Open the customer interface box. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the power on supply and signal wires for voltage. Place one test lead on the power on supply wire at the SDU410 unit. Place the other test lead on the panel ground. Place one test lead on the power on signal wire at the customer interface box logic unit. Place the other test lead on the panel ground. Refer to the appropriate circuit diagram or wiring diagram for connection pin identification. | Less than +24-VDC? **YESRepair:** Replace the SDU410 unit. Contact a Cummins® Authorized Repair Location. | 3A |
> | Less than +24-VDC? **NO** | Repair complete |  |
>
> ### STEP 3. Check OEM harness to customer interface box cable
>
> #### STEP 3A. Check the ignition (engine stop) supply wire for an open.
>
> | **Conditions:** Disconnect customer interface box to OEM harness cable connector C1 from the customer interface box. Disconnect the OEM harness from the C1 connector on the engine. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the ignition (engine stop) supply wire for an open. Place a jumper between the ignition (engine stop) pin in the C1 connector. Place one test lead on the ignition (engine stop) pin in the OEM connector on the engine. Place the other test lead on the ignition (engine stop) pin at the C8 connector. Refer to the appropriate circuit diagram or wiring diagram for connection pin identification. | Less than 10 ohms? **YES** | Repair complete |
> | Less than 10 ohms? **NORepair:** Replace the OEM wiring harness. Refer to the OEM installation instructions. | Contact a Cummins® Authorized Repair Location |  |
