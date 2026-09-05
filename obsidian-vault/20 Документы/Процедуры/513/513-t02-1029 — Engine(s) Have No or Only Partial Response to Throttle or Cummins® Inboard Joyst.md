---
type: "Процедура"
doc: "513-t02-1029"
title_en: "Engine(s) Have No or Only Partial Response to Throttle or Cummins® Inboard Joystick Operation"
modified: "2019-09-27"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "5411480"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-t02-1029.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-t02-1029.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/513"
  - "перевод/машинный"
---

# Engine(s) Have No or Only Partial Response to Throttle or Cummins® Inboard Joystick Operation

> [!abstract] Процедура · `513-t02-1029`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[5411480 — C Command Connect and Connect Premier Marine Panel Systems PS102, PS103 and PS108 Mas|5411480]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2019-09-27
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-t02-1029.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-t02-1029.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

- При использовании дроссель не активируется или частично функционирует.

### Как пользоваться этим деревом

По этому дереву симптомов можно вести поиск неисправности. Начните с шага 1 поиска неисправностей. На шаге 2 система задаст ряд вопросов и по симптому выдаст перечень действий по поиску неисправности.

### Практические замечания

Возможные причины включают:

- Схема открытого сигнала в дроссельной заслоне Сигнал

- Неисправный дроссел

- Неисправный резервный дроссел

- На борту джойстик неисправен.

Ссылка на соответствующую схему проводов производителя оригинального оборудования (OEM) при схемах устранения неполадок, которые используют проводку, поставляемую OEM.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте судно на наличие неисправности или кодов сигнализации. |  |
|  | **STEP 1A.** Проверить судно на наличие бортового джойстика Cummins® или дроссельной заслонки Cummins®. | Cummins® в бортовой джойстик или установлена электронная дроссельная заслонка и смещение? |
|  | **СТЭП 1В.** Прочитайте коды сигнализации. | Световой индикатор сигнализации освещен? |
|  | **STEP 1C** См. коды неисправностей модуля управления двигателем (ECM). | Активны перебои с подачей дроссельной заслонки или датчика? |
| ШАГ 2. | Проверьте цепь дроссельной заслонки. |  |
|  | **STEP 2A.** Проверьте напряжение дросселя в интерфейсе двигателя. | 4,75 VDC и 5,25 VDC? |
|  | **ШАГ 2В.** Проверьте интерфейс двигателя, проводя упряжку дроссельной заслонки SIGNAL. | Менее 10 Ом? |

### ШАГ 1. Проверьте судно на наличие неисправности или кодов сигнализации.

#### ШАГ 1A. Проверьте судно на наличие бортового джойстика Cummins® или дросселя Cummins®.

| **Условия: **Выключите выключатель системы. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверка судна на наличие джойстика Cummins® или дроссельной пересадки Cummins® | Cummins® в бортовой джойстик или установлена электронная дроссельная заслонка и смещение? *Да | 1В |
| Cummins® в бортовой джойстик или установлена электронная дроссельная заслонка и смещение? **НЕТ** | 1С |  |

#### ШАГ 1B. Прочитайте коды сигнализации.

| **Условия: **Включить включение системы. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Прочитайте коды сигнализации. Записывайте последовательность чередующихся медленных и быстрых мигающих индикаторных огней. | Световой индикатор сигнализации освещен? См. руководство по ремонту судов Cummins® Electronic Throttle and Shift and Cummins® Inboard Joystick Marine Controls MC101 Master Repair Manual. | Перейдите к соответствующему дереву для устранения неполадок кода сигнализации |
| Световой индикатор сигнализации освещен? **НЕТ** | 1С |  |

#### ШАГ 1C. Прочитайте коды ошибок ECM.

| **Условия: **Включить включение системы. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Прочитайте коды ошибок ECM. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Активны ли какие-либо сбои в дроссельной заслоне или датчике? См. руководство по коду неисправности Cummins® для двигателя. | Перейдите к соответствующему дереву устранения неисправностей кода ошибки. |
| Активны ли какие-либо сбои в дроссельной заслоне или датчике? **НЕТ** | 2А |  |

### ШАГ 2. Проверьте цепь дроссельной заслонки.

#### ШАГ 2A. Проверьте интерфейс двигателя проводов жгута напряжения дроссельной заслонки.

| **Условия: **Включить включение системы. Отсоедините дроссельную проводку от 3-контактного разъема на интерфейсе двигателя. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте интерфейс двигателя проводов жгута напряжения дроссельной заслонки. Поместите один испытательный щуп на Pin A интерфейса двигателя, проводя ремень 3-контактного дроссельного разъема. Поместите другой свинец на Pin C интерфейса двигателя, проводя ремень 3-контактного дроссельного разъема. | 4,75 VDC и 5,25 VDC? *Да | 2В |
| 4,75 VDC и 5,25 VDC? **NORepair: **Открытое Поставки или возврата обнаруживается в интерфейсе двигателя проводов жгута или проводов двигателя жгута. Устранение неполадок и ремонт проводной упряжки. Интерфейс двигателя проводка жгут: См. процедуру 015-093 в разделе 15. Жгут проводов двигателя: См. Процедуру 019-043 в руководстве по эксплуатации двигателя Cummins®. | Ремонт завершён. |  |

#### ШАГ 2B. Проверьте интерфейс двигателя, проводка ремня дроссельной заслонки SIGNAL.

| **Условия: **Выключите выключатель системы. Отсоедините дроссельную проводку от 3-контактного разъема на интерфейсе двигателя. Отсоедините проводную упряжку от модуля процессора управления дроссельной заслонки или дроссельной заслонки |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте интерфейс двигателя, проводка ремня дроссельной заслонки SIGNAL. Измерить сопротивление контакта сигнала дроссельной заслонки на интерфейсе двигателя, проводя ремень к контакту сигнала дроссельной заслонки на дроссельной заслоне или модуль процессора управления дроссельной заслонки. | Менее 10 Ом? **Ремонт: **См. соответствующий Симптом в руководстве по ремонту судовых джойстиков MC101 «Электронная дроссельная заслонка и смещение» Cummins® и «Cummins® Inboard Joystick Marine Controls». Для Non Cummins® дроссель относится к дроссельной OEM-службе | Перейдите к соответствующему дереву для устранения неполадок кода сигнализации. |
| Менее 10 Ом? **NORepair: **Обнаружен сигнал открытого дросселя. Ремонт или замена проводов ремня или межсоединений. | Ремонт завершён. |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> - Throttle will **not** activate or partially function when used.
>
> ### How To Use This Tree
>
> This symptom tree can be used to troubleshoot a malfunction. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.
>
> ### Shoptalk
>
> Possible causes include:
>
> - Open signal circuit in throttle Signal
>
> - Malfunctioning throttle
>
> - Malfunctioning backup throttle
>
> - Inboard joystick is malfunctioning.
>
> Reference the appropriate original equipment manufacturer (OEM) wiring diagram when troubleshooting circuits that utilize wiring supplied by the OEM.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check vessel for fault or alarm codes. |  |
> |  | **STEP 1A.** Check vessel for Cummins® inboard joystick or Cummins® Throttle Shift. | Cummins® inboard joystick or Electronic Throttle and Shift installed? |
> |  | **STEP 1B.** Read the alarm codes. | Alarm code indicator light illuminated? |
> |  | **STEP 1C.** Read the engine control module (ECM) fault codes. | Throttle or sensor supply faults active? |
> | STEP 2. | Check the throttle circuit. |  |
> |  | **STEP 2A.** Check the engine interface wiring harness throttle voltage. | Between 4.75 VDC and 5.25 VDC? |
> |  | **STEP 2B.** Check the engine interface wiring harness throttle SIGNAL. | Less than 10 ohms? |
>
> ### STEP 1. Check vessel for fault or alarm codes.
>
> #### STEP 1A. Check vessel for Cummins® inboard joystick or Cummins® Throttle Shift.
>
> | **Conditions:** Turn System Enable switch OFF. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check vessel for Cummins® inboard joystick or Cummins® Throttle Shift | Cummins® inboard joystick or Electronic Throttle and Shift installed? **YES** | 1B |
> | Cummins® inboard joystick or Electronic Throttle and Shift installed? **NO** | 1C |  |
>
> #### STEP 1B. Read the alarm codes.
>
> | **Conditions:** Turn System Enable switch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Read the alarm codes. Record the sequence of alternating slow and fast blinking indicator lights. | Alarm code indicator light illuminated? **YESRepair:** See the Cummins® Electronic Throttle and Shift and Cummins® Inboard Joystick Marine Controls MC101 Master Repair Manual. | Go to the appropriate alarm code troubleshooting tree |
> | Alarm code indicator light illuminated? **NO** | 1C |  |
>
> #### STEP 1C. Read the ECM fault codes.
>
> | **Conditions:** Turn System Enable switch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Read the ECM fault codes. Use INSITE™ electronic service tool to read the fault codes. | Any throttle or sensor supply faults active? **YESRepair:** See the Cummins® fault code manual for the engine. | Go to the appropriate fault code troubleshooting tree. |
> | Any throttle or sensor supply faults active? **NO** | 2A |  |
>
> ### STEP 2. Check the throttle circuit.
>
> #### STEP 2A. Check the engine interface wiring harness throttle voltage.
>
> | **Conditions:** Turn System Enable switch ON. Disconnect the throttle harness from the 3 pin connector on the engine interface wiring harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the engine interface wiring harness throttle voltage. Place one test lead on Pin A of the engine interface wiring harness 3 pin throttle connector. Place the other lead on Pin C of the engine interface wiring harness 3 pin throttle connector. | Between 4.75 VDC and 5.25 VDC? **YES** | 2B |
> | Between 4.75 VDC and 5.25 VDC? **NORepair:** An open Supply or Return is detected in the engine interface harness or engine wiring harness. Troubleshoot and repair the harness. Engine interface harness: Refer to Procedure 015-093 in Section 15. Engine wiring harness: See Procedure 019-043 in the Cummins® service manual for the engine. | Repair complete. |  |
>
> #### STEP 2B. Check the engine interface wiring harness throttle SIGNAL.
>
> | **Conditions:** Turn System Enable switch OFF. Disconnect the throttle harness from the 3 pin connector on the engine interface wiring harness. Disconnect the harness from the throttle or throttle control processor module |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the engine interface wiring harness throttle SIGNAL. Measure the resistance of the throttle SIGNAL pin at the engine interface harness to the throttle SIGNAL pin at the throttle or the throttle control processor module. | Less than 10 ohms? **YESRepair:** Refer to the appropriate Symptom in the Cummins® Electronic Throttle and Shift and Cummins® Inboard Joystick Marine Controls MC101 Master Repair Manual. For Non Cummins® throttle refer to throttle OEM service manual | Go to the appropriate alarm code troubleshooting tree. |
> | Less than 10 ohms? **NORepair:** An open throttle signal has been detected. Repair or replace the harness or interconnects. | Repair complete. |  |
