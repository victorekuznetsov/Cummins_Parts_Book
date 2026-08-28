---
type: "Процедура"
doc: "513-t02-11542"
title_en: "OEM Installed Sensor – Shorted to High"
modified: "2020-06-25"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-t02-11542.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-t02-11542.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/513"
  - "перевод/машинный"
---

# OEM Installed Sensor – Shorted to High

> [!abstract] Процедура · `513-t02-11542`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[5411480 — C Command Connect and Connect Premier Marine Panel Systems PS102, PS103 and PS108 Mas|5411480]]
> **Секции:** Section TA - Troubleshooting Alarm Codes
> **Даты:** изменён 2020-06-25
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-t02-11542.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-t02-11542.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

- OEM-установка датчика Alarm, отображаемого на экране ED-4.

- Установленный OEM-датчик представляет собой постоянное значение.

### Как пользоваться этим деревом

Это дерево симптомов может быть использовано для устранения неполадок установленного датчика сигнализации OEM. Начните с шага 1 поиска неисправностей. На шаге 2 система задаст ряд вопросов и по симптому выдаст перечень действий по поиску неисправности.

### Практические замечания

Возможные причины:

- OEM-установка датчика сигнализации неисправности.

- OEM-установка датчика Alarm закорочена высоко.

Дисплей ED-4 способен контролировать резистивные отправители с максимальным сопротивлением примерно 1100 Ом и отправители напряжения с максимальным напряжением 10 Вольт.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте установленный датчик сигнализации OEM. |  |
|  | **STEP 1A.** Проверьте наличие активной сигнализации датчика, установленной OEM-производителем. | OEM-установленный датчик — закороченный до высокой сигнализации? |
| ШАГ 2. | Проверьте дисплей ED-4. |  |
|  | **STEP 2A.** Проверить данные датчика на дисплее ED-4. | Измеренная стоимость соответствует зарегистрированной стоимости? |
| ШАГ 3. | Проверьте установленный OEM-датчик и схему. |  |
|  | **STEP 3A.** Проверить установленные датчик и контакты разъема OEM. | Грязные или поврежденные контакты? |
|  | **STEP 3B.** Проверьте реакцию цепи. | OEM-установленный датчик - сокращенный до высокоактивного сигнала тревоги и OEM-установленный датчик - сокращенный до низкого неактивного сигнала тревоги? |
|  | **STEP 3C** Проверьте установленный датчик сигнализации OEM и проверьте состояние датчика. | OEM-установленный датчик — закороченный до высокой сигнализации? |
| ШАГ 4. | Проверьте оригинальную проводку датчика производителя оборудования (OEM). |  |
|  | **STEP 4A.** Проверить установленные датчиком проводов датчика контакты разъема жгута. | Грязные или поврежденные контакты? |
|  | **STEP 4B.** Проверьте наличие открытой обратной цепи в установленной OEM-производителем проводах датчика. | Менее 10 Ом? |
|  | **STEP 4C.** Проверьте наличие открытой цепи в установленной OEM-производителем проводах датчика. | Больше 100 тысяч ом? |
|  | **STEP 4D.** Проверить неактивный код ошибки. | Установленный датчик OEM - с высокой сигнализацией больше не активен? |

### ШАГ 1. Проверьте коды сигнализации.

#### ШАГ 1A. Проверьте активный код ошибки.

| **Условия:** Система включения включает включение. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте дисплей ED-4, чтобы прочитать коды сигнализации. | OEM-установленный датчик — закороченный до высокой сигнализации? *Да | 2А |
| OEM-установленный датчик — закороченный до высокой сигнализации? **НЕТ** | Используйте следующую процедуру для неактивных и периодических кодов сигнализации. |  |

### ШАГ 2. Проверьте дисплей ED-4.

#### ШАГ 2A. Проверка данных датчика на дисплее ED-4.

| **Условия:** Система включения включает включение. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Запись установленного OEM-датчика режима измерения в I/O-просмотрщике. Запись установленного OEM-датчика сопротивления или необработанного значения напряжения в I/O-просмотрщике. Отсоедините дисплей ED-4 от окна интерфейса клиента (C.I.B.). См. процедуру 015-023. Отсоедините первичный и вторичный разъемы от дисплея ED-4. Поместите один свинец на установленный датчиком контакт сигнала на вторичный разъем ED-4. Поместите другой свинец на контакт 1 ВПЕРЕДЕНИЯ на первичный разъем ED-4. | Измеренная стоимость соответствует зарегистрированной стоимости? *Да | 3А |
| Измеренная стоимость соответствует зарегистрированной стоимости? **NORepair: **Заменить ED-4, если аналоговый канал не работает должным образом. См. процедуру 015-023 в разделе 15. | Ремонт завершён. |  |

### ШАГ 3. Проверьте установленный OEM-датчик и схему.

#### ШАГ 3A. Осмотрите установленные OEM-датчик и контакты разъема.

| **Условия:** Система поворота позволяет выключать выключатель. Отсоедините установленный OEM-датчик от проводной ремни. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема или разъема разъема разъема оболочки разбитого изоляционного повреждения Проволоки Поврежденный разъем блокировки вкладки. | Грязные или поврежденные контакты? **Ремонт: **В разъеме датчика или разъеме жгута проводов обнаружено поврежденное соединение. Очистите разъем и булавки. Почините поврежденный жгут проводов, разъем или штифты или замените установленный датчик OEM. Замените установленную OEM-датчиком проводку жгутом. См. процедуру 015-103 в разделе 15. | Ремонт завершён. |
| Грязные или поврежденные контакты? **НЕТ** | 3B |  |

#### ШАГ 3B. Проверьте установленное OEM-датчиком напряжение.

| **Условия:** Система включения включает включение. Отсоедините установленный OEM-датчик от проводной ремни. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте напряжение. Поместите один свинец на установленный OEM датчик контакта питания в проводной ремне. Поместите другой свинец на установленный OEM датчик обратного контакта в проводной ремне. Повреждение изоляции провода. Поврежденная блокировка разъема. | Между 4,75 и 5,25 вольт? *Да | 3C |
| Между 4,75 и 5,25 вольт? **НЕТ** | 4А |  |

#### ШАГ 3C. Проверьте установленную OEM-сенсорную сигнализацию и проверьте состояние датчика.

| **Условия:** Система поворота позволяет выключать выключатель. Подключите установленный OEM-датчик от установленного OEM-датчика проводов ремня. Система включения включает переключатель. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Подожди 30 секунд. Проверьте дисплей ED-4, чтобы прочитать коды сигнализации. | OEM-установка датчика — закороченная до высокой сигнализации активная? Поврежденный датчик был обнаружен. Ссылка на OEM для замены датчика. | Ремонт завершён. |
| OEM-установка датчика - закороченная до высокой сигнализации активная? **Норвегия: **Нет. Удаление и установка разъема исправили неисправность. | Ремонт завершён. |  |

### ШАГ 4. Проверьте оригинальную проводку датчика производителя оборудования (OEM).

#### ШАГ 4A. Проверьте установленный OEM-датчик проводов жгута от C.I.B.

| **Условия:** Система поворота позволяет выключать выключатель. Отсоедините установленный OEM-датчик от сети C.I.B. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема или разъема разъема разъема оболочки разбитого изоляционного повреждения Проволоки Поврежденный разъем блокировки вкладки. | Грязные или поврежденные контакты? **YESRepair:** В установленном OEM-производителем разъеме датчика проводов обнаружено поврежденное соединение. Очистите разъем и булавки. Замените поврежденный участок установленной OEM-датчиком проводов ремня или C.I.B. По возможности отремонтируйте поврежденную проводку, разъем или штифты. См. процедуру 015-103. | Ремонт завершён. |
| Грязные или поврежденные контакты? **НЕТ** | 4B |  |

#### ШАГ 4B. Проверьте наличие открытой обратной цепи в установленной OEM-датчиком проводах.

| **Условия:** Система поворота позволяет выключать выключатель. Отсоедините установленный OEM-датчик от разъема жгутов проводов C.I.B. Отключите установленный OEM-датчик от установленной OEM-датчиком проводов вредит. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте сопротивление. Поместите один испытательный щуп на установленный OEM датчик обратного контакта на установленный OEM датчик проводов ремня C.I.B разъема. Поместите другой испытательный щуп на установленный OEM датчик обратного контакта на установленный OEM датчик проводов разъёма датчика. Ссылка на схему схемы или схему проводов для идентификации контакта с разъемом. | Менее 10 Ом? *Да | 4C |
| Менее 10 Ом? **NORepair:** В установленной OEM-производителем электропроводке датчика обнаружена схема открытого возврата. Устранение неполадок в каждой части проводов и блока терминала. Замените установленный OEM-датчик проводкой ремня, если это необходимо. См. процедуру 015-103. | Ремонт завершён. |  |

#### ШАГ 4C. Проверьте наличие открытой цепи в установленной OEM-датчиком проводах.

| **Условия:** Система поворота позволяет выключать выключатель. Отсоедините установленный OEM-датчик от сети C.I.B. Отсоедините установленный OEM-датчик от установленного OEM-датчика проводов. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте сопротивление. Поместите один испытательный щуп на установленный OEM датчик сигнала контакта в установленный OEM датчик проводов ремня C.I.B разъема. Поместите другой испытательный щуп на установленный датчиком контакт сигнала OEM в установленный датчиком OEM разъем датчика жгута. Ссылка на схему схемы или схему проводов для идентификации контакта с разъемом. | Менее 10 Ом? **Ремонт:** | 4D |
| Менее 10 Ом? **NORepair: **Открытая цепь на сигнальной линии была обнаружена в установленной OEM-производителем проводах датчика. Устранение неполадок в каждой части проводов и блока терминала. Замените установленный OEM-датчик проводкой ремня, если это необходимо. См. процедуру 015-103. | Ремонт завершён. |  |

#### ШАГ 4D. Проверьте наличие неактивной сигнализации датчика, установленной OEM.

| **Условия: **Соединить все компоненты. Система включения включает переключатель. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Подожди 30 секунд. Проверьте дисплей ED-4, чтобы прочитать коды сигнализации. | OEM-сенсор - от короткой до высокой сигнализации больше не активен? **Ремонт: **Нет. Удаление и установка разъема исправили неисправность. | Ремонт завершён. |
| OEM-сенсор - от короткой до высокой сигнализации больше не активен? **Норэпар: **Поврежденный датчик обнаружен. Ссылка на OEM для замены датчика. | Ремонт завершён. |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> - OEM installed sensor Alarm displayed on ED-4 screen.
>
> - OEM installed sensor is a constant value.
>
> ### How To Use This Tree
>
> This symptom tree can be used to troubleshoot OEM installed sensor Alarm. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.
>
> ### Shoptalk
>
> Possible causes are:
>
> - OEM installed sensor Alarm malfunction.
>
> - OEM installed sensor Alarm shorted high.
>
> ED-4 display is capable of monitoring resistive senders with maximum resistance of approximately 1100 ohms and voltage senders with maximum voltage of 10 Volts.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the OEM installed sensor alarm. |  |
> |  | **STEP 1A.** Check for an active OEM installed sensor alarm. | OEM installed sensor – shorted to high Alarm active? |
> | STEP 2. | Check the ED-4 display. |  |
> |  | **STEP 2A.** Verify sensor data in the ED-4 display. | Measured value match the recorded value? |
> | STEP 3. | Check the OEM installed sensor and circuit. |  |
> |  | **STEP 3A.** Inspect the OEM Installed sensor and connector pins. | Dirty or damaged pins? |
> |  | **STEP 3B.** Check the circuit response. | OEM installed sensor – shorted to high Alarm active and OEM installed sensor - shorted to low Alarm inactive? |
> |  | **STEP 3C.** Check the OEM installed sensor Alarm and verify sensor condition. | OEM installed sensor – shorted to high Alarm active? |
> | STEP 4. | Check the original equipment manufacturer (OEM) sensor wiring harness. |  |
> |  | **STEP 4A.** Inspect the OEM installed sensor wiring harness connector pins. | Dirty or damaged pins? |
> |  | **STEP 4B.** Check for an open return circuit in the OEM installed sensor wiring harness. | Less than 10 ohms? |
> |  | **STEP 4C.** Check for an open circuit in the OEM installed sensor wiring harness. | Greater than 100k ohms? |
> |  | **STEP 4D.** Check for an inactive fault code. | OEM installed sensor – Shorted to High Alarm no longer active? |
>
> ### STEP 1. Check the alarm codes.
>
> #### STEP 1A. Check for an active fault code.
>
> | **Conditions:** Turn system enable switch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the ED-4 display to read the alarm codes. | OEM installed sensor – shorted to high Alarm active? **YES** | 2A |
> | OEM installed sensor – shorted to high Alarm active? **NO** | Use the following procedure for inactive and intermittent alarm codes. |  |
>
> ### STEP 2. Check the ED-4 display.
>
> #### STEP 2A. Verify sensor data in the ED-4 display.
>
> | **Conditions:** Turn system enable switch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Record the OEM installed sensor Measurement Mode in the I/O viewer. Record the OEM installed sensor resistance or voltage raw value in the I/O viewer. Disconnect the ED-4 display from the customer interface box (C.I.B.). Refer to Procedure 015-023. Disconnect the primary and secondary connectors from the ED-4 display. Place one lead on OEM installed sensor SIGNAL pin on the ED-4 secondary connector. Place the other lead on the RETURN pin 1 on the ED-4 primary connector. | Measured value match the recorded value? **YES** | 3A |
> | Measured value match the recorded value? **NORepair:** Replace ED-4 if analog channel is **not** working properly. Refer to Procedure 015-023 in Section 15. | Repair complete. |  |
>
> ### STEP 3. Check the OEM installed sensor and circuit.
>
> #### STEP 3A. Inspect the OEM installed sensor and connector pins.
>
> | **Conditions:** Turn system enable switch OFF. Disconnect the OEM installed sensor from the wiring harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the sensor connector or harness connector. Clean the connector and pins. Repair the damaged harness, connector, or pins, or replace the OEM installed sensor. Replace the OEM installed sensor wiring harness. Refer to Procedure 015-103 in Section 15. | Repair complete. |
> | Dirty or damaged pins? **NO** | 3B |  |
>
> #### STEP 3B. Check the OEM installed sensor voltage.
>
> | **Conditions:** Turn system enable switch ON. Disconnect the OEM installed sensor from the wiring harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the voltage. Place one lead on the OEM installed sensor SUPPLY pin at the wiring harness. Place the other lead on the OEM installed sensor RETURN pin at the wiring harness. Wire insulation damage. Damaged connector locking tab. | Between 4.75 and 5.25 volts? **YES** | 3C |
> | Between 4.75 and 5.25 volts? **NO** | 4A |  |
>
> #### STEP 3C. Check the OEM installed sensor alarm and verify sensor condition.
>
> | **Conditions:** Turn system enable switch OFF. Connect the OEM installed sensor from the OEM installed sensor wiring harness. Turn system enable switch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Wait 30 seconds. Check the ED-4 display to read the alarm codes. | OEM installed sensor – shorted to high alarm active? **YESRepair:** A damaged sensor has been detected. Reference the OEM for sensor replacement. | Repair complete. |
> | OEM installed sensor - shorted to high alarm active? **NORepair:** None. The removal and installation of the connector corrected the fault. | Repair complete. |  |
>
> ### STEP 4. Check the original equipment manfacturer (OEM) sensor wiring harness.
>
> #### STEP 4A. Inspect the OEM installed sensor wiring harness from the C.I.B.
>
> | **Conditions:** Turn system enable switch OFF. Disconnect the OEM installed sensor wiring harness from the C.I.B. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the OEM installed sensor wiring harness connector. Clean the connector and pins. Replace the damaged section of the OEM installed sensor wiring harness or the C.I.B. Repair the damaged harness, connector, or pins, if possible. Refer to Procedure 015-103. | Repair complete. |
> | Dirty or damaged pins? **NO** | 4B |  |
>
> #### STEP 4B. Check for an open return circuit in the OEM installed sensor wiring harness.
>
> | **Conditions:** Turn system enable switch OFF. Disconnect the OEM installed sensor wiring harness connector from the C.I.B. Disconnect the OEM installed sensor from the OEM installed sensor wiring harmess. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance. Place one test lead on the OEM installed sensor RETURN pin at the OEM installed sensor wiring harness C.I.B connector. Place the other test lead on the OEM installed sensor RETURN pin at the OEM installed sensor wiring harness sensor connector. Reference the circuit diagram or wiring diagram for connector pin identification. | Less than 10 ohms? **YES** | 4C |
> | Less than 10 ohms? **NORepair:** An open return circuit has been detected in the OEM installed sensor wiring harness. Troubleshoot each section of the harness and terminal block. Replace the OEM installed sensor wiring harness, if necessary. Refer to Procedure 015-103. | Repair complete. |  |
>
> #### STEP 4C. Check for an open circuit in the OEM installed sensor wiring harness.
>
> | **Conditions:** Turn system enable switch OFF. Disconnect the OEM installed sensor wiring harness from the C.I.B. Disconnect the OEM installed sensor from the OEM installed sensor wiring harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance. Place one test lead on the OEM installed sensor SIGNAL pin at the OEM installed sensor wiring harness C.I.B connector. Place the other test lead on the OEM installed sensor SIGNAL pin at the OEM installed sensor wiring harness sensor connector. Reference the circuit diagram or wiring diagram for connector pin identification. | Less than 10 ohms? **YESRepair:** | 4D |
> | Less than 10 ohms? **NORepair:** An open circuit on the signal line has been detected in the OEM installed sensor wiring harness. Troubleshoot each section of the harness and terminal block. Replace the OEM installed sensor wiring harness, if necessary. Refer to Procedure 015-103. | Repair complete. |  |
>
> #### STEP 4D. Check for an inactive OEM installed sensor alarm.
>
> | **Conditions:** Connect all components. Turn system enable switch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Wait 30 seconds. Check the ED-4 display to read the alarm codes. | OEM installed sensor - short to high alarm no longer active? **YESRepair:** None. The removal and installation of the connector corrected the fault. | Repair complete. |
> | OEM installed sensor - short to high alarm no longer active? **NORepair:** A damaged sensor has been detected. Reference the OEM for sensor replacement. | Repair complete. |  |
