---
type: "Процедура"
doc: "513-t02-11543"
title_en: "OEM Installed Sensor – Shorted to Low"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-t02-11543.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-t02-11543.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/513"
  - "перевод/машинный"
---

# OEM Installed Sensor – Shorted to Low

> [!abstract] Процедура · `513-t02-11543`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[5411480 — C Command Connect and Connect Premier Marine Panel Systems PS102, PS103 and PS108 Mas|5411480]]
> **Секции:** Section TA - Troubleshooting Alarm Codes
> **Даты:** изменён 2020-06-22
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-t02-11543.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-t02-11543.pdf)

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

- OEM-установка датчика неисправности.

- OEM-установка датчика сигнала закорочена низко.

Дисплей ED-4 способен контролировать резистивные отправители с максимальным сопротивлением примерно 1100 Ом и отправители напряжения с максимальным напряжением 10 Вольт.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте коды сигнализации. |  |
|  | **STEP 1A.** Проверить коды сигнализации датчика питания. | OEM-установка датчика Alarm Active? |
| ШАГ 2. | Проверьте дисплей ED-4. |  |
|  | **STEP 2A.** Проверить данные датчика на дисплее ED-4. | Измеренная стоимость соответствует зарегистрированной стоимости? |
| Шаг. |  |  |
|  | **ШАГ 3.** Проверьте установленный датчик OEM и разъём жгута проводов. |  |
|  | **STEP 3A.** Проверить установленные датчик и соединительные контакты OEM. | Грязные или поврежденные контакты? |
|  | **STEP 3B.** Проверьте реакцию цепи. | Примерно 5 VDC. OEM-установленный датчик — закороченный до низкого кода сигнализации? |
|  | **STEP 3C** Проверить коды сигнализации и состояние датчика. | OEM-установленный датчик — закороченный до низкого кода сигнализации? |
| ШАГ 4. | Проверьте оригинальную проводку датчика производителя оборудования (OEM). |  |
|  | **STEP 4A.** Проверить установленные датчиком проводов датчика контакты разъема жгута. | Грязные или поврежденные контакты? |
|  | **STEP 4B.** Проверьте короткое замыкание в установленной OEM-датчиком проводах. | Менее 10 Ом? |
|  | **STEP 4C.** Проверьте короткое замыкание от пин-до земли. | Менее 10 Ом? |
|  | **ШАГ** |  |
|  | **STEP 4D.** Проверить неактивный код сигнализации. | OEM-установка датчика - от короткого до низкого сигнала тревоги больше не активна? |

### Шаг. Проверьте коды сигнализации.

#### ШАГ 1A. Проверьте коды сигнализации датчика питания.

| **Условия: **Включите включение. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте дисплей ED-4, чтобы прочитать коды сигнализации. | OEM-установка датчика - закороченная до низкой сигнализации активная? *Да | 2А |
| OEM-установка датчика - закороченная до низкой сигнализации активная? **НЕТ** | 2А |  |

### ШАГ 2. Проверьте дисплей ED-4.

#### ШАГ 2A. Проверка данных датчика на дисплее ED-4.

| **Условия:** Система включения включает включение. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Запись установленного OEM-датчика режима измерения в I/O-просмотрщике. Запись установленного OEM-датчика сопротивления или необработанного значения напряжения в I/O-просмотрщике. Отсоедините дисплей ED-4 от окна интерфейса клиента (C.I.B.). В разделе 15. Отсоедините первичный и вторичный разъемы от дисплея ED-4. Поместите один свинец на контакт сигнала датчика OEM на вторичный разъем ED-4. Поместите другой свинец на контакт 1 ВПЕРЕДЕНИЯ на первичный разъем ED-4. | Измеренная стоимость соответствует зарегистрированной стоимости? *Да | 3А |
| Измеренная стоимость соответствует зарегистрированной стоимости? **NORepair:** Проверить аналоговые каналы ввода ED-4 в журнале данных и в разделе просмотра ввода/вывода.[[513-015-035 — Display(s) and Instrumentation\|См. процедуру 015-035]]В разделе 15. Заменить ED-4, если аналоговый канал не работает. См. процедуру 015-023 в разделе 15. | Ремонт завершён |  |

### ШАГ 3. Проверьте установленный датчик OEM и разъём жгута проводов.

#### ШАГ 3A. Проверьте установленные датчики OEM и контакты разъема.

| **Условия:** Система поворота позволяет выключать выключатель. Отсоедините установленный OEM-датчик от установленного OEM-датчика проводов. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема изоляции Поврежденный разъем блокировки вкладки. | Грязные или поврежденные контакты? **Ремонт: **В датчике или разъёме жгута проводов обнаружено поврежденное соединение. Очистите контакты разъема. По возможности отремонтируйте поврежденную проводку, разъёмы или штифты. См. процедуру 015-103 в разделе 15. | Ремонт завершён. |
| Грязные или поврежденные контакты? **НЕТ** | 3B |  |

#### ШАГ 3B. Проверьте установленное OEM-датчиком напряжение.

| **Условия:** Система поворота позволяет выключать выключатель. Отсоедините установленный OEM-разъем датчика от установленной OEM-подключателя датчика. Включите систему, включите переключатель. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте напряжение между установленным датчиком питания OEM и установленным датчиком обратного контакта OEM на установленном датчике OEM разъеме установленной датчиком OEM проводов. Ссылка на схему схемы или схему проводов для идентификации контакта с разъемом. | Между 4,75 и 5,25 вольт? *Да | 3C |
| Между 4,75 и 5,25 вольт? **НЕТ** | 4А |  |

#### ШАГ 3C. Проверьте коды сигнализации и состояние датчика.

| **Условия:** Система поворота позволяет выключать выключатель. Отсоедините установленный датчик уровня OEM от установленной OEM проводов датчика. Система включения включает переключатель. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Подожди 30 секунд. Проверьте дисплей ED-4, чтобы прочитать коды сигнализации. | OEM-установка датчика - короткая или низкая активная сигнализация? Поврежденный датчик был обнаружен. Замените установленный датчик OEM. См. сервисную документацию изготовителя оборудования. | Ремонт завершён. |
| OEM-сенсор — короткое или низкое сигнал тревоги? **Норвегия: **Нет. Удаление и установка разъема исправили неисправность. | Ремонт завершён. |  |

### ШАГ 4. Проверьте оригинальную проводку датчика производителя оборудования (OEM).

#### ШАГ 4A. Осмотрите установленные OEM датчиком проводов контактных соединений ремня.

| **Условия:** Система поворота позволяет выключать выключатель. Отсоедините установленный OEM-датчик от сети C.I.B. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Разъем разъема Разъем разъема Разъем разъема Разъем или разбитые штифты Отодвинутые назад или расширенные штифты Влажность в разъеме или на разъеме. Пропавшие или поврежденные соединительные уплотнения. Грязь или мусор в контактах или разъёме. Оболочка разбитого коннектора повреждена изоляцией провода Повреждена блокировка разъёма вкладкой. | Грязные или поврежденные контакты? **YESRepair:** В установленном OEM-производителем разъеме датчика проводов обнаружено поврежденное соединение. Очистите разъем и булавки. По возможности отремонтируйте поврежденную проводку, разъем или штифты. См. процедуру 015-103 в разделе 15. | Ремонт завершён. |
| Грязные или поврежденные контакты? **НЕТ** | 4B |  |

#### ШАГ 4B. Проверьте короткое замыкание контакт-контакт в установленной OEM-датчиком проводах.

| **Условия:** Система поворота позволяет выключать выключатель. Отсоедините установленный OEM-датчик от сети C.I.B. Отсоедините установленный OEM-датчик от установленного OEM-датчика проводов. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерить сопротивление между OEM-установленным датчиком сигнала контакта в OEM-установленном датчике проводов ремня C.I.B. разъем и все остальные штифты в OEM-установке датчика проводов упряжки C.I.B. разъём. Ссылка на соответствующую схему или схему проводов для идентификации контакта с разъемом. | Больше 100 тысяч ом? *Да | 4C |
| Больше 100 тысяч ом? **NORepair:** При необходимости заменить установленную OEM-датчиком проводку. См. процедуру 015-103 в разделе 15. | Ремонт завершён. |  |

#### ШАГ 4C. Проверьте короткое замыкание от булавки до земли.

| **Условия:** Система поворота позволяет выключать выключатель. Отсоедините установленный OEM-датчик от сети C.I.B. Отсоедините установленный OEM-датчик от установленного OEM-датчика проводов. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерить сопротивление между OEM-установленным датчиком сигнала контакта в OEM-установленном датчике проводов ремня C.I.B. Разъем и земля. Ссылка на соответствующую схему или схему проводов для идентификации контакта с разъемом. | Менее 10 тысяч ом? *Да | 4D |
| Менее 10 тысяч ом? **NORepair:** В установленной OEM-производителем проводах датчика обнаружено короткое замыкание на проводе SIGNAL. Устранение неполадок в каждом из проводных упряжек/терминального блока. Замените установленный OEM-датчик проводкой ремня, если это необходимо. См. процедуру 015-103 в разделе 15. | Ремонт завершён. |  |

#### ШАГ 4D. Проверьте неактивный код тревоги.

| **Условия: **Соединить все компоненты. Система включения включает переключатель. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте дисплей ED-4, чтобы прочитать коды сигнализации. | OEM-сенсор - сигнализация от короткой до низкой больше не активна? **Ремонт: **Нет. Удаление и установка разъема исправили неисправность. | Ремонт завершён. |
| OEM-сенсор — от короткой до низкой тревоги больше не активен? **Норэпар: **Поврежденный датчик обнаружен. Замените установленный датчик OEM. См. сервисную документацию изготовителя оборудования. | Ремонт завершён. |  |


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
> This symptom tree can be used to troubleshoot OEM installed sensor alarm code. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.
>
> ### Shoptalk
>
> Possible causes are:
>
> - OEM installed sensor malfunction.
>
> - OEM installed sensor signal shorted low.
>
> ED-4 display is capable of monitoring resistive senders with maximum resistance of approximately 1100 ohms and voltage senders with maximum voltage of 10 Volts.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the alarm codes. |  |
> |  | **STEP 1A.** Check for sensor supply alarm codes. | OEM installed sensor Alarm active? |
> | STEP 2. | Check the ED-4 display. |  |
> |  | **STEP 2A.** Verify sensor data in the ED-4 display. | Measured value match the recorded value? |
> | STEP. |  |  |
> |  | **STEP 3.** Check the OEM installed sensor and harness connector. |  |
> |  | **STEP 3A.** Inspect the OEM installed sensor and connector pins. | Dirty or damaged pins? |
> |  | **STEP 3B.** Check the circuit response. | Approximately 5 VDC. OEM installed sensor – shorted to low Alarm Code active? |
> |  | **STEP 3C.** Check the alarm codes and verify sensor condition. | OEM installed sensor – shorted to low Alarm Code active? |
> | STEP 4. | Check the original equipment manufacturer (OEM) sensor wiring harness. |  |
> |  | **STEP 4A.** Inspect the OEM installed sensor wiring harness connector pins. | Dirty or damaged pins? |
> |  | **STEP 4B.** Check for a pin-to-pin short circuit in the OEM installed sensor wiring harness. | Less than 10 ohms? |
> |  | **STEP 4C.** Check for a pin-to-ground short circuit. | Less than 10 ohms? |
> |  | **STEP.** |  |
> |  | **STEP 4D.** Check for an inactive alarm code. | OEM installed sensor - shorted to low alarm no longer active? |
>
> ### STEP. Check the alarm codes.
>
> #### STEP 1A. Check for sensor supply alarm codes.
>
> | **Conditions:** Turn enable switch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the ED-4 display to read the alarm codes. | OEM installed sensor - shorted to low alarm active? **YES** | 2A |
> | OEM installed sensor - shorted to low alarm active? **NO** | 2A |  |
>
> ### STEP 2. Check the ED-4 display.
>
> #### STEP 2A. Verify sensor data in the ED-4 display.
>
> | **Conditions:** Turn system enable switch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Record the OEM installed sensor Measurement Mode in the I/O viewer. Record the OEM installed sensor resistance or voltage raw value in the I/O viewer. Disconnect the ED-4 display from the customer interface box (C.I.B.). in Section 15. Disconnect the primary and secondary connectors from the ED-4 display. Place one lead on OEM sensor SIGNAL pin on the ED-4 secondary connector. Place the other lead on the RETURN pin 1 on the ED-4 primary connector. | Measured value match the recorded value? **YES** | 3A |
> | Measured value match the recorded value? **NORepair:** Check ED-4 display analog input channels in the data log and view - I/O viewer section. [[513-015-035 — Display(s) and Instrumentation\|Refer to Procedure 015-035]] in Section 15. Replace ED-4 if analog channel is **not** working. Refer to Procedure 015-023 in Section 15. | Repair complete |  |
>
> ### STEP 3. Check the OEM Installed Sensor and harness connector.
>
> #### STEP 3A. Inspect the OEM Installed Sensor and connector pins.
>
> | **Conditions:** Turn system enable switch OFF. Disconnect the OEM installed sensor from the OEM installed sensor wiring harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the sensor or harness connector. Clean the connector pins. Repair the damaged harness, connectors, or pins, if possible. Refer to Procedure 015-103 in Section 15. | Repair complete. |
> | Dirty or damaged pins? **NO** | 3B |  |
>
> #### STEP 3B. Check the OEM installed sensor voltage.
>
> | **Conditions:** Turn system enable switch OFF. Disconnect the OEM installed sensor connector from the OEM installed sensor wiring harness. Turn the system enable switch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the voltage between the OEM installed sensor SUPPLY pin and the OEM installed sensor RETURN pin at the OEM installed sensor connector of the OEM installed sensor wiring harness. Reference the circuit diagram or wiring diagram for connector pin identification. | Between 4.75 and 5.25 volts? **YES** | 3C |
> | Between 4.75 and 5.25 volts? **NO** | 4A |  |
>
> #### STEP 3C. Check the alarm codes and verify sensor condition.
>
> | **Conditions:** Turn system enable switch OFF. Disconnect the OEM installed level sensor from the OEM installed sensor wiring harness. Turn system enable switch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Wait 30 seconds. Check the ED-4 display to read the alarm codes. | OEM installed sensor - short to low alarm active? **YESRepair:** A damaged sensor has been detected. Replace the OEM installed sensor. See equipment manufacturer service information. | Repair complete. |
> | OEM installed sensor – short to low Alarm active? **NORepair:** None. The removal and installation of the connector corrected the fault. | Repair complete. |  |
>
> ### STEP 4. Check the original equipment manufacturer (OEM) sensor wiring harness.
>
> #### STEP 4A. Inspect the OEM installed sensor wiring harness connector pins.
>
> | **Conditions:** Turn system enable switch OFF. Disconnect the OEM installed sensor wiring harness from the C.I.B. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector. Missing or damaged connector seals. Dirt or debris in or the connector pins. Connector shell broken Wire insulation damage Damaged connector locking tab. | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the OEM installed sensor wiring harness connector. Clean the connector and pins. Repair the damaged harness, connector, or pins, if possible. Refer to Procedure 015-103 in Section 15. | Repair complete. |
> | Dirty or damaged pins? **NO** | 4B |  |
>
> #### STEP 4B. Check for a pin-to-pin short circuit in the OEM installed sensor wiring harness.
>
> | **Conditions:** Turn system enable switch OFF. Disconnect the OEM installed sensor wiring harness from the C.I.B. Disconnect the OEM installed sensor from the OEM installed sensor wiring harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance between the OEM installed sensor SIGNAL pin in the OEM installed sensor wiring harness C.I.B. connector and all other pins in the OEM installed sensor wiring harness C.I.B. connector. Reference the appropriate circuit or wiring diagram for connector pin identification. | Greater than 100k ohms? **YES** | 4C |
> | Greater than 100k ohms? **NORepair:** Replace the OEM installed sensor wiring harness, if necessary. Refer to Procedure 015-103 in Section 15. | Repair complete. |  |
>
> #### STEP 4C. Check for a pin-to-ground short circuit.
>
> | **Conditions:** Turn system enable switch OFF. Disconnect the OEM installed sensor wiring harness from the C.I.B. Disconnect the OEM installed sensor from the OEM installed sensor wiring harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance between the OEM installed sensor SIGNAL pin in the OEM installed sensor wiring harness C.I.B. connector and ground. Reference the appropriate circuit or wiring diagram for connector pin identification. | Less than 10k ohms? **YES** | 4D |
> | Less than 10k ohms? **NORepair:** A pin-to-ground short circuit on the SIGNAL wire has been detected in the OEM installed sensor wiring harness. Troubleshoot each of the harness/terminal block. Replace the OEM installed sensor wiring harness, if necessary. Refer to Procedure 015-103 in Section 15. | Repair complete. |  |
>
> #### STEP 4D. Check for an inactive alarm code.
>
> | **Conditions:** Connect all components. Turn system enable switch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the ED-4 display to read the alarm codes. | OEM installed sensor - short to low alarm no longer active? **YESRepair:** None. The removal and installation of the connector corrected the fault. | Repair complete. |
> | OEM installed sensor – short to low Alarm no longer active? **NORepair:** A damaged sensor has been detected. Replace the OEM installed sensor. See equipment manufacturer service information. | Repair complete. |  |
