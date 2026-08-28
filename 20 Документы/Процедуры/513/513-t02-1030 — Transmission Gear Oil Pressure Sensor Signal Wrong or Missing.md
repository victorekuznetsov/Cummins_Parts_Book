---
type: "Процедура"
doc: "513-t02-1030"
title_en: "Transmission Gear Oil Pressure Sensor Signal Wrong or Missing"
modified: "2019-10-18"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-t02-1030.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-t02-1030.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/513"
  - "перевод/машинный"
---

# Transmission Gear Oil Pressure Sensor Signal Wrong or Missing

> [!abstract] Процедура · `513-t02-1030`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[5411480 — C Command Connect and Connect Premier Marine Panel Systems PS102, PS103 and PS108 Mas|5411480]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2019-10-18
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-t02-1030.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-t02-1030.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

- Значение давления масла в передаточной передаче постоянно на дисплее ED-4.

### Как пользоваться этим деревом

Это дерево симптомов может быть использовано для устранения неисправности датчика давления масла передач. Начните с шага 1 поиска неисправностей. На шаге 2 система задаст ряд вопросов и по симптому выдаст перечень действий по поиску неисправности.

### Практические замечания

Возможные причины:

- Сигнал датчика давления масла в передаточном механизме открыт.

- Неисправность датчика давления масла в трансмиссии.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте код сигнализации. |  |
|  | **STEP 1A.** Проверить наличие активного кода неисправности. | Код 1199 или 1214 неисправности активен или неактивен, включив более одного номера за последние 25 часов работы двигателя. |
|  | **ШАГ 1В.** Проверьте активный код сигнализации. | Код тревоги 1214 или 1199 активен? |
| ШАГ 2. | Проверьте дисплей ED-4. |  |
|  | **STEP 2A.** Проверить данные датчика на дисплее ED-4. | Измеренная стоимость соответствует зарегистрированной стоимости? |
| ШАГ 3. | Проверьте датчик проводов жгута. |  |
|  | **ШАГ 3А.** Проверить электропроводку упряжки. | Грязные или поврежденные контакты? |
|  | **STEP 3B.** Проверьте реакцию цепи. | Код тревоги 1199 активен? |
|  | **STEP 3C** Проверить наличие открытой цепи в цепи передачи сигнала давления масла. | Менее 10 Ом? |

### ШАГ 1. Проверьте код сигнализации.

#### ШАГ 1A. Проверьте активный код ошибки.

| **Условия:** Включить переключатель зажигания. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте активный код ошибки. Используйте инструмент электронного сервиса INSITETM для считывания кодов неактивных ошибок. | Код 1199 или 1214 неисправности активен или неактивен, включив более одного номера за последние 25 часов работы двигателя. *Да | Перейдите к соответствующему дереву для устранения неполадок. |
| Код 1199 или 1214 неисправности активен или неактивен, включив более одного номера за последние 25 часов работы двигателя. **НЕТ** | Нет ремонта. |  |

#### ШАГ 1B. Проверьте активный код тревоги.

| **Условия:** Система включения включает включение. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Подождите 30 секунд, прочитайте ED-4 Display. | Код тревоги 1214 или 1199 активен? *Да | Перейдите к соответствующему дереву устранения неполадок кода сигнализации в разделе ТА. |
| Код тревоги 1214 или 1199 активен? **НЕТ** | 2А |  |

### ШАГ 2. Проверьте дисплей ED-4.

#### ШАГ 2A. Проверка данных датчика на дисплее ED-4.

| **Условия:** Система включения включает включение. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте давление масла в трансмиссии. Запись датчика давления масла передатчика в необработанном виде в I/O зрителе. Отсоедините дисплей ED-4 от окна интерфейса клиента (C.I.B.). См. процедуру 015-023 в разделе 15. Отсоедините первичный и вторичный разъемы от дисплея ED-4. Поместите один свинец на датчик давления масла трансмиссии SIGNAL контакт 2 на вторичный разъем ED-4. Поместите другой свинец на контакт 1 ВПЕРЕДЕНИЯ на первичный разъем ED-4. См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Измеренная стоимость соответствует зарегистрированной стоимости? *Да | 3А |
| Измеренная стоимость соответствует зарегистрированной стоимости? **NORepair:** Проверить каналы ввода аналогового дисплея ED-4 в журнале данных и в разделе просмотра ввода/вывода.[[513-015-035 — Display(s) and Instrumentation\|См. процедуру 015-035 в разделе 15.]]Замените ED-4, если аналоговый канал работает неправильно. См. процедуру 015-023 в разделе 15. | Ремонт завершён |  |

### ШАГ 3. Проверьте датчик проводов жгута.

#### ШАГ 3A. Проверьте проводку.

| **Условия:** Система поворота позволяет выключать выключатель. Отсоедините датчик давления масла передаточной передачи от проводной ремни. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте проводку. Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема или разъема разъема разъема оболочки разбитого изоляционного повреждения Проволоки Поврежденный разъем блокировки вкладки. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Грязные или поврежденные контакты? **Ремонт: **В разъёме жгута проводов обнаружено поврежденное соединение. Очистите разъем и булавки. По возможности отремонтируйте поврежденную проводку, разъем или штифты. | Ремонт завершён |
| Грязные или поврежденные контакты? **НЕТ** | 3B |  |

#### ШАГ 3B. Проверьте отклик цепи.

| **Условия:** Система поворота позволяет выключать выключатель. Отсоедините датчик давления масла передаточной передачи от проводной ремни. Система включения включает переключатель. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте проводку. Поместите провод перемычки между передающим масляным давлением +5 вольт обратным контактом и передающим передаточным масляным сигналом контакта на передаточном передаточном масляном разъеме проводной ремни. См. схему или схему проводов для идентификации контакта с разъемом. Проверьте соответствующую реакцию цепи через 30 секунд. Подождите 30 секунд, прочитайте дисплей ED-4. | Код тревоги 1199 активен? **Ремонт:** Заменить датчик давления масла в передаточной коробке.[[513-019-641 — Transmission Gear Oil Pressure Sensor\|См. процедуру 019-641 в разделе 19.]] | Ремонт завершён |
| Код тревоги 1199 активен? **НЕТ** | 3C |  |

#### ШАГ 3C. Проверьте наличие открытой цепи в цепи сигнала давления масла передатчика.

| **Условия:** Система поворота позволяет выключать выключатель. Отсоедините датчик давления масла передаточной передачи от проводной ремни. Отключите всю проводку ремня последовательно от датчика давления масла передатчика передачи к C.I.B. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте сопротивление. Поместите один свинец на передаточный механизм масляного давления датчика сигнала контакта на разъёме проводов ремня. Поместите другой свинец на передаточный датчик давления масла контактного сигнала в проводах жгута проводов альтернативного разъёма. См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов использования мультиметра.[[99-019-359 — Multimeter Usage\|См. процедуру 019-359 в разделе 19.]] | Менее 10 Ом? Заменить датчик давления масла в трансмиссии.[[513-019-641 — Transmission Gear Oil Pressure Sensor\|См. процедуру 019-641 в разделе 19.]]. | Ремонт завершён |
| Менее 10 Ом? **NORepair:** В цепи сигнала датчика давления масла в передающей передаче обнаружена открытая цепь. Устранение неполадок в каждой проводах ремня последовательно, чтобы определить, какая проводка ремня или разъем содержит открытую цепь. Ремонт или замена соответствующей проводов жгута. | Ремонт завершён. |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> - Transmission gear oil pressure value is constant on ED-4 display.
>
> ### How To Use This Tree
>
> This symptom tree can be used to troubleshoot a transmission gear oil pressure sensor fault. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.
>
> ### Shoptalk
>
> Possible causes are:
>
> - Transmission gear oil pressure sensor signal is open.
>
> - Transmission gear oil pressure sensor malfunction.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the alarm code. |  |
> |  | **STEP 1A.** Check for an active fault code. | Fault Code 1199 or 1214 active or inactive with more than one count logged in the last 25 engine hours? |
> |  | **STEP 1B.** Check for an active alarm code. | Alarm Code 1214 or 1199 active? |
> | STEP 2. | Check the ED-4 display. |  |
> |  | **STEP 2A.** Verify sensor data in the ED-4 display. | Measured value match the recorded value? |
> | STEP 3. | Check the sensor wiring harness. |  |
> |  | **STEP 3A.** Inspect the wiring harness. | Dirty or damaged pins? |
> |  | **STEP 3B.** Check the circuit response. | Alarm Code 1199 active? |
> |  | **STEP 3C.** Check for an open circuit in the transmission gear oil pressure signal circuit. | Less than 10 ohms? |
>
> ### STEP 1. Check the alarm code.
>
> #### STEP 1A. Check for an active fault code.
>
> | **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for active fault code. Use INSITE™ electronic service tool to read the inactive fault codes. | Fault Code 1199 or 1214 active or inactive with more than one count logged in the last 25 engine hours? **YES** | Go to the appropriate troubleshooting tree. |
> | Fault Code 1199 or 1214 active or inactive with more than one count logged in the last 25 engine hours? **NO** | No repair. |  |
>
> #### STEP 1B. Check for an active alarm code.
>
> | **Conditions:** Turn system enable switch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Wait 30 seconds, read the ED-4 Display. | Alarm Code 1214 or 1199 active? **YES** | Go to appropriate alarm code troubleshooting tree in Section TA. |
> | Alarm Code 1214 or 1199 active? **NO** | 2A |  |
>
> ### STEP 2. Check the ED-4 display.
>
> #### STEP 2A. Verify sensor data in the ED-4 display.
>
> | **Conditions:** Turn system enable switch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check transmission gear oil pressure. Record the transmission gear oil pressure sensor raw value in the I/O viewer. Disconnect the ED-4 display from the customer interface box (C.I.B.). Refer to Procedure 015-023 in Section 15. Disconnect the primary and secondary connectors from the ED-4 display. Place one lead on transmission gear oil pressure sensor SIGNAL pin 2 on the ED-4 secondary connector. Place the other lead on the RETURN pin 1 on the ED-4 primary connector. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Measured value match the recorded value? **YES** | 3A |
> | Measured value match the recorded value? **NORepair:** Check ED-4 Display Analog Input channels in the data log and view - I/O viewer section. [[513-015-035 — Display(s) and Instrumentation\|Refer to Procedure 015-035 in Section 15.]] Replace ED-4 if analog channel is **not** working properly. Refer to Procedure 015-023 in Section 15. | Repair complete |  |
>
> ### STEP 3. Check the sensor wiring harness.
>
> #### STEP 3A. Inspect the wiring harness.
>
> | **Conditions:** Turn system enable switch OFF. Disconnect the transmission gear oil pressure sensor from the wiring harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the wiring harness. Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the harness connector. Clean the connector and pins. Repair the damaged harness, connector, or pins, if possible. | Repair complete |
> | Dirty or damaged pins? **NO** | 3B |  |
>
> #### STEP 3B. Check the circuit response.
>
> | **Conditions:** Turn system enable switch OFF. Disconnect the transmission gear oil pressure sensor from the wiring harness. Turn system enable switch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the wiring harness. Place a jumper wire between the transmission Gear oil pressure +5 volt RETURN pin and the transmission gear oil pressure SIGNAL pin at transmission gear oil pressure sensor connector of the harness. Refer to the circuit diagram or wiring diagram for connector pin identification. Check for the appropriate circuit response after 30 seconds. Wait 30 seconds, read the ED-4 display. | Alarm Code 1199 active? **YESRepair:** Replace the transmission gear oil pressure sensor. [[513-019-641 — Transmission Gear Oil Pressure Sensor\|Refer to Procedure 019-641 in Section 19.]] | Repair complete |
> | Alarm Code 1199 active? **NO** | 3C |  |
>
> #### STEP 3C. Check for an open circuit in the transmission gear oil pressure signal circuit.
>
> | **Conditions:** Turn system enable switch OFF. Disconnect the transmission gear oil pressure sensor from the wiring harness. Disconnect all wiring harness in series from the transmission gear oil pressure sensor to the C.I.B. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance. Place one lead on the transmission gear oil pressure sensor SIGNAL pin on the wiring harness connector. Place the other lead on the transmission gear oil pressure sensor SIGNAL pin in the wiring harness alternate connector. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general multimeter usage techniques. [[99-019-359 — Multimeter Usage\|Refer to Procedure 019-359 in Section 19.]] | Less than 10 ohms? **YESRepair:** Replace transmission oil pressure sensor. [[513-019-641 — Transmission Gear Oil Pressure Sensor\|Refer to Procedure 019-641 in Section 19]]. | Repair complete |
> | Less than 10 ohms? **NORepair:** An open in the transmission gear oil pressure sensor signal circuit has been detected. Troubleshoot each harness in series to determine which harness or connector contains the open circuit. Repair or replace the appropriate harness. | Repair complete. |  |
