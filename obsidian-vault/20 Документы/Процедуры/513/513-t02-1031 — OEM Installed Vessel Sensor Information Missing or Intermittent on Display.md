---
type: "Процедура"
doc: "513-t02-1031"
title_en: "OEM Installed Vessel Sensor Information Missing or Intermittent on Display"
modified: "2020-06-22"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-t02-1031.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-t02-1031.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/513"
  - "перевод/машинный"
---

# OEM Installed Vessel Sensor Information Missing or Intermittent on Display

> [!abstract] Процедура · `513-t02-1031`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[5411480 — C Command Connect and Connect Premier Marine Panel Systems PS102, PS103 and PS108 Mas|5411480]]
> **Секции:** Section TA - Troubleshooting Alarm Codes · Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2020-06-22
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-t02-1031.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-t02-1031.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

- Параметры датчика или данные не отображаются правильно или неверны.

### Как пользоваться этим деревом

Это дерево симптомов может быть использовано для устранения проблем с отображением данных. Начните с шага 1 поиска неисправностей. На шаге 2 система задаст ряд вопросов и по симптому выдаст перечень действий по поиску неисправности.

### Практические замечания

Возможные причины:

- Неправильный файл личности судна

- Коробка интерфейса клиента (C.I.B.)

- Оригинальные датчики оборудования Manufacutrer (OEM).

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте дисплей ED-4. |  |
|  | **STEP 1A.** Проверить наличие кода активной ошибки. | Неисправность или активная сигнализация? |
|  | **STEP 1B.** Проверить файл личности судна. | Файл личности судна правильный для этого судна? |
|  | **STEP 1C** Проверить соединения датчиков. | Все датчики и соединения установлены правильно? |
| ШАГ 2. | Проверьте C.I.B. |  |
|  | **STEP 2A.** Проверьте настройку датчика на дисплее ED-4. | Примерно 5 вольт? |

### ШАГ 1. Проверьте дисплей ED-4.

#### ШАГ 1A. Проверьте активный код ошибки.

| **Условия: **Включите включение. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте код ошибки. Проверьте, активен ли сбой в расширенном экране сбоев. | Неисправность или активная сигнализация? *Да | Перейдите к соответствующему дереву устранения неполадок или обратитесь к процедуре, упомянутой в описании кода неисправности на экране Advanced Fault. |
| Неисправность или активная сигнализация? **НЕТ** | 1В |  |

#### ШАГ 1B. Проверьте личные данные судна.

| **Условия: **Включите включение. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте личные данные судна. Проверьте, правильно ли файл личности судна загружается на дисплее. См. процедуру 015-044 в разделе 15. | Файл личности судна правильный для этого судна? *Да | 1С |
| Файл личности судна правильный для этого судна? **NORepair:** Скачать правильный файл личности судна на дисплей от Cummins QuickServe® Online.[[513-015-044 — Managing Vessel Personalities\|См. процедуру 015-044 в разделе 15.]] | Ремонт завершён |  |

#### ШАГ 1C. Проверьте сенсорные соединения.

| **Условия: **Выключите выключатель. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте связи. Проверяйте датчик, проводку и соединения терминальных блоков на OEM-датчике. | Все датчики и соединения установлены правильно? *Да | 2А |
| Все датчики и соединения установлены правильно? **NORepair:** Ремонт или ремонт соединений или установки. | Ремонт завершён |  |

### ШАГ 2. Проверьте C.I.B.

#### ШАГ 2A. Проверьте настройку датчика на дисплее ED-4.

| **Условия: **Выключите выключатель. Отсоедините проводку датчика OEM от C.I.B. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте напряжение. Поместите один свинец на датчик SUPPLY контакта 1 на C.I.B. разъем (присоединение к OEM-датчику проводов). Поместите другой свинец на датчик RETURN 2 на C.I.B. разъем (присоединение к OEM-датчику проводов). См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов использования мультиметра.[[99-019-359 — Multimeter Usage\|См. процедуру 019-359 в разделе 19.]] | Примерно 5 вольт? **YESRepair:** Ремонт или замена электропроводки датчика OEM. См. процедуру 015-103 в разделе 15. | Ремонт завершён |
| Примерно 5 вольт? **NORepair:** Заменить C.I.B. См. процедуру 015-023 в разделе 15. | Ремонт завершён |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> - Sensor parameters or data does **not** display correctly or is incorrect.
>
> ### How To Use This Tree
>
> This symptom tree can be used to troubleshoot display data issues. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.
>
> ### Shoptalk
>
> Possible causes are:
>
> - Incorrect vessel personality file
>
> - Customer interface box (C.I.B.)
>
> - Original equipment manufacutrer (OEM) sensors.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the ED-4 display. |  |
> |  | **STEP 1A.** Check for active fault code. | Fault or alarm code active? |
> |  | **STEP 1B.** Check vessel personality file. | Vessel personality file correct for this vessel? |
> |  | **STEP 1C.** Check the sensor connections. | All sensors and connections installed properly? |
> | STEP 2. | Check the C.I.B. |  |
> |  | **STEP 2A.** Check the sensor setup in the ED-4 display. | Approximately 5 volts? |
>
> ### STEP 1. Check the ED-4 display.
>
> #### STEP 1A. Check for active fault code.
>
> | **Conditions:** Turn enable switch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for fault code. Check if fault is active in Advanced fault screen. | Fault or alarm code active? **YES** | Go to appropriate troubleshooting tree or refer to procedure mentioned in fault code description on the Advanced Fault screen. |
> | Fault or alarm code active? **NO** | 1B |  |
>
> #### STEP 1B. Check vessel personality file.
>
> | **Conditions:** Turn enable switch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check vessel personality file. Verify correct vessel personality file is downloaded in the display. Refer to Procedure 015-044 in Section 15. | Vessel personality file correct for this vessel? **YES** | 1C |
> | Vessel personality file correct for this vessel? **NORepair:** Download correct vessel personality file to the display from Cummins QuickServe® Online. [[513-015-044 — Managing Vessel Personalities\|Refer to Procedure 015-044 in Section 15.]] | Repair complete |  |
>
> #### STEP 1C. Check the sensor connections.
>
> | **Conditions:** Turn enable switch OFF. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check connections. Inspect sensor, harness, and terminal block connections on OEM sensor wiring harness. | All sensor and connections installed properly? **YES** | 2A |
> | All sensor and connections installed properly? **NORepair:** Repair or fix connections or installation. | Repair complete |  |
>
> ### STEP 2. Check the C.I.B.
>
> #### STEP 2A. Check the sensor setup in the ED-4 display.
>
> | **Conditions:** Turn enable switch OFF. Disconnect the OEM sensor wiring harness from the C.I.B. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check voltage. Place one lead on sensor SUPPLY pin 1 on the C.I.B. connector (mating to the OEM sensor harness). Place the other lead on sensor RETURN pin 2 on the C.I.B. connector (mating to the OEM sensor harness). Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general multimeter usage techniques. [[99-019-359 — Multimeter Usage\|Refer to Procedure 019-359 in Section 19.]] | Approximately 5 volts? **YESRepair:** Repair or replace the OEM sensor wiring harness. Refer to Procedure 015-103 in Section 15. | Repair complete |
> | Approximately 5 volts? **NORepair:** Replace the C.I.B. Refer to Procedure 015-023 in Section 15. | Repair complete |  |
