---
aliases:
  - "Останов двигателя без активного верхнего диапазона частот, когда он применим"
type: "Процедура"
doc: "116-t02-1096"
title_en: "Engine Shutdown With High Speed Range Not Active When Applicable"
title_ru: "Останов двигателя без активного верхнего диапазона частот, когда он применим"
modified: "2009-07-17"
engines:
  - "41349633"
families:
  - "QSK19"
manuals:
  - "4021617"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1096.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/116-t02-1096.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/116"
  - "перевод/машинный"
---

# Engine Shutdown With High Speed Range Not Active When Applicable
**Останов двигателя без активного верхнего диапазона частот, когда он применим**

> [!abstract] Процедура · `116-t02-1096`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2009-07-17
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1096.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/116-t02-1096.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

- Блок SDU410 не реагирует на датчик диапазона скоростей при активации и не выключает двигатель.

### Как пользоваться этим деревом

По этому дереву симптомов можно вести поиск неисправности. Начните с шага 1 поиска неисправностей. На шаге 2 система задаст ряд вопросов и по симптому выдаст перечень действий по поиску неисправности.

### Практические замечания

Входные сигналы SDU410 являются переключателями. Эти переключатели обычно открыты и закрыты для активации отключения.

Устройство SDU410 имеет два датчика давления моторного масла. Один для диапазона низких оборотов двигателя (LSR) и один для диапазона высоких оборотов двигателя (HSR). Датчик LSR всегда активен, но датчик HSR активен только тогда, когда скорость двигателя превышает 1400 оборотов в минуту.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте интерфейс клиента |  |
|  | **STEP 1A.** Проверьте логическую блокировку светодиодного освещения в интерфейсе клиента. | Активны ли какие-либо сигналы тревоги или светодиоды освещены? |
|  | **STEP 1B.** Проверьте провод электропитания SDU410 на +24-VDC. | Меньше +24-VDC? |
| ШАГ 2. | Проверьте скорость двигателя |  |
|  | **STEP 2A.** Проверьте скорость двигателя на дисплее SDU410. | Скорость двигателя выше 1400 об/мин. |
| ШАГ 3. | Проверьте OEM-проводку для кабеля интерфейса клиента |  |
|  | **STEP 3A.** Проверьте скорость двигателя 1 и скорость двигателя 2 сигнала и возвращайте провода для открытого. | Менее 10 Ом? |

### ШАГ 1. Проверьте интерфейс клиента

#### ШАГ 1A. Проверьте логическое устройство клиентского интерфейса LED подсветка.

| ** Условия:** Проверьте устройство DCU410 на наличие сигнализации и светодиодной подсветки. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте наличие сигнализации и светодиодной подсветки на устройстве DCU410. | Активны ли какие-либо сигналы тревоги или светодиоды освещены? *Да** | Свяжитесь с авторизованным местом ремонта Cummins® |
| Активны ли какие-либо сигналы тревоги или светодиоды освещены? ** НЕТ** | 1В |  |

#### ШАГ 1B. Проверьте провод питания DCU410 для +24-VDC.

| ** Условия: ** Откройте окно интерфейса клиента |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте напряжение на блоке отключения питания 24-VDC на блоке SDU410. Поместите один испытательный щуп на блок отключения питания 24-VDC на блоке питания SDU410. Поместите другой испытательный щуп на провод возврата блока отключения в блок SDU410. См. соответствующую схему или схему проводов для идентификации соединительного штифта. | Меньше +24-VDC? *** Ремонт:** Проверить аккумуляторы. См. руководство по обслуживанию OEM или свяжитесь с авторизованным местом ремонта Cummins®. | Ремонт завершён |
| Меньше +24-VDC? ** НЕТ** | 2А |  |

### ШАГ 2. Проверьте скорость двигателя

#### ШАГ 2A. Проверьте показания скорости двигателя на блоке SDU410.

| **Условия: ** Двигатель работает. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте скорость двигателя. Проверьте скорость двигателя на дисплее SDU410. | Скорость двигателя выше 1400 об/мин. **************************************************************************************************************************************************************************************************************************************************************** Обратитесь в авторизованный сервисный центр Cummins®. | Ремонт завершён |
| Скорость двигателя выше 1400 об/мин. **NORepair:** Заменить модуль SDU410. Обратитесь в авторизованный сервисный центр Cummins®. | 3А |  |

### ШАГ 3. Проверьте OEM-проводку для кабеля интерфейса клиента

#### ШАГ 3A. Проверьте скорость двигателя 1 и скорость двигателя 2 сигнал и возврат проводов для открытого.

| **Условия: ** Отключить окно интерфейса клиента к OEM-проводах кабельного разъема. Отключите OEM-разъем C11 на двигателе. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте скорость двигателя 1 и скорость двигателя 2 сигнал и возврат проводов для открытого. Поместите один испытательный щуп на сигнал скорости двигателя 1 на разъеме C4. Поместите другой испытательный щуп на провод сигнала 1 скорости двигателя на разъеме OEM C11. Поместите один испытательный щуп на возврат скорости двигателя 1 на разъеме C4. Поместите другой испытательный щуп на провод возврата скорости двигателя 1 на разъеме OEM C11. Поместите один испытательный щуп на сигнал 2 оборота двигателя на разъеме C4. Поместите другой испытательный щуп на провод сигнала 2 оборота двигателя на разъем OEM C11. Поместите один испытательный щуп на скорость 2 вращения двигателя на разъеме C4. Поместите другой испытательный щуп на обратный провод 2 оборота двигателя на разъем OEM C11. См. соответствующую схему или схему проводов для идентификации соединительного штифта. | Менее 10 Ом? *Да** | Ремонт завершён |
| Менее 10 Ом? **NORepair:** Заменить проводку OEM. См. инструкции по установке OEM. Заменить SDU410. Обратитесь в авторизованный сервисный центр Cummins®. | Свяжитесь с авторизованным местом ремонта Cummins® |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> - The SDU410 unit is **not** reacting to the high speed range sensor when activated and does **not** shut down the engine.
>
> ### How To Use This Tree
>
> This symptom tree can be used to troubleshoot a malfunction. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.
>
> ### Shoptalk
>
> The SDU410 input signals are switches. These switches are normally open and closed to activate a shutdown.
>
> The SDU410 unit has two lube oil pressure sensors. One for the low engine speed range (LSR) and one for the high engine speed range (HSR). The LSR sensor is **always** active, but the HSR sensor is **only** active when the engine speed is above 1400 rpm.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check customer interface box |  |
> |  | **STEP 1A.** Check the customer interface box logic unit LED illumination. | Are any alarms active or LEDs illuminated? |
> |  | **STEP 1B.** Check the SDU410 power supply wire for +24-VDC. | Less than +24-VDC? |
> | STEP 2. | Check engine speed |  |
> |  | **STEP 2A.** Check the engine speed on the SDU410 unit display. | Engine speed above 1400 rpm? |
> | STEP 3. | Check OEM harness to customer interface box cable |  |
> |  | **STEP 3A.** Check the engine speed 1 and engine speed 2 signal and return wires for an open. | Less than 10 ohms? |
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
> ### STEP 2. Check engine speed
>
> #### STEP 2A. Check the engine speed reading on the SDU410 unit.
>
> | **Conditions:** Engine running. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the engine speed. Verify the engine speed on the SDU410 unit display. | Engine speed above 1400 rpm? **YESRepair:** Check the SDU410 configuration. Contact a Cummins® Authorized Repair Location. | Repair complete |
> | Engine speed above 1400 rpm? **NORepair:** Replace the SDU410 unit. Contact a Cummins® Authorized Repair Location. | 3A |  |
>
> ### STEP 3. Check OEM Harness to customer interface box cable
>
> #### STEP 3A. Check the engine speed 1 and engine speed 2 signal and return wires for an open.
>
> | **Conditions:** Disconnect customer interface box to OEM harness cable connector. Disconnect the OEM disconnect C11 connector on engine. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the engine speed 1 and engine speed 2 signal and return wires for an open. Place one test lead on the engine speed 1 signal at the C4 connector. Place the other test lead on the engine speed 1 signal wire at the OEM C11 connector. Place one test lead on the engine speed 1 return at the C4 connector. Place the other test lead on the engine speed 1 return wire at the OEM C11 connector. Place one test lead on the engine speed 2 signal at the C4 connector. Place the other test lead on the engine speed 2 signal wire at the OEM C11 connector. Place one test lead on the engine speed 2 return at the C4 connector. Place the other test lead on the engine speed 2 return wire at the OEM C11 connector. Refer to the appropriate circuit diagram or wiring diagram for connection pin identification. | Less than 10 ohms? **YES** | Repair complete |
> | Less than 10 ohms? **NORepair:** Replace the OEM wiring harness. Refer to the OEM installation instructions. Replace the SDU410 unit. Contact a Cummins® Authorized Repair Location. | Contact a Cummins® Authorized Repair Location |  |
