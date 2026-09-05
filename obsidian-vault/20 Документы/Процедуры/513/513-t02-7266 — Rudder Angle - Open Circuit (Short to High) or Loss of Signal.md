---
type: "Процедура"
doc: "513-t02-7266"
title_en: "Rudder Angle - Open Circuit (Short to High) or Loss of Signal"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-t02-7266.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-t02-7266.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/513"
  - "перевод/машинный"
---

# Rudder Angle - Open Circuit (Short to High) or Loss of Signal

> [!abstract] Процедура · `513-t02-7266`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[5411480 — C Command Connect and Connect Premier Marine Panel Systems PS102, PS103 and PS108 Mas|5411480]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2019-09-27
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-t02-7266.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-t02-7266.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

- Код тревоги 7266 или 7665, отображаемый на экране ED-4.

- Угол руля является постоянным значением.

### Как пользоваться этим деревом

Это дерево симптомов может быть использовано для устранения неполадок датчика угла поворота руля Alarm Code. Начните с шага 1 поиска неисправностей. На шаге 2 система задаст ряд вопросов и по симптому выдаст перечень действий по поиску неисправности.

### Практические замечания

Код сигнализации 7266 и 7265 поддерживается на ED-4, работающем с любым программным обеспечением версии 5 или ниже.

Код сигнализации 7665 и 7664 поддерживается на ED-4, работающем с любым программным обеспечением версии 6 или выше.

Возможные причины включают:

- Неисправность датчика угла поворота

- Сигнал угла поворота закоротился высоко.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте коды тревоги. |  |
|  | **STEP 1A.** Проверить наличие активного кода неисправности. | Код тревоги 7266 или 7665 активен? |
| ШАГ 2. | Проверьте дисплей ED-4. |  |
|  | **STEP 2A.** Проверить данные датчика на дисплее ED-4. | Измеренная стоимость соответствует зарегистрированной стоимости? |
| ШАГ 3. | Проверьте датчик и схему дисплея ED-4. |  |
|  | **STEP 3A.** Проверить датчик дисплея ED-4 и контакты разъема. | Грязные или поврежденные контакты? |
|  | **STEP 3B.** Проверьте реакцию цепи. | Код 7267 или 7664 активен, а код 7266 или 7665 неактивен? |
|  | **STEP 3C** Проверить коды сигнализации и состояние датчика. | Код тревоги 7266 или 7665 активен? |
| ШАГ 4. | Проверьте оригинальную проводку датчика производителя оборудования (OEM). |  |
|  | **STEP 4A.** Проверить контакты разъёма соединительного устройства с датчиком OEM. | Грязные или поврежденные контакты? |
|  | **STEP 4B.** Проверьте наличие открытой обратной цепи в электропроводке датчика OEM. | Менее 10 Ом? |
|  | **STEP 4C.** Проверьте наличие цепи открытого сигнала в электропроводке датчика OEM. | Менее 10 Ом? |
|  | **STEP 4D.** Проверить неактивный код ошибки. | Код тревоги 7266 или 7665 больше не активен? |

### ШАГ 1. Проверьте коды тревоги.

#### ШАГ 1A. Проверьте активный код ошибки.

| **Условия:** Система включения включает включение. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте дисплей ED-4, чтобы прочитать коды тревоги. | Код тревоги 7266 или 7665 активен? *Да | 2А |
| Код тревоги 7266 или 7665 активен? **НЕТ** | 2А |  |

### ШАГ 2. Проверьте дисплей ED-4.

#### ШАГ 2A. Проверка данных датчика на дисплее ED-4.

| **Условия:** Система включения включает включение. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Запись ED-4 датчика отображения необработанного значения в I/O зрителе. Отключите дисплей ED-4 от окна клиентского интерфейса (C.I.B.). См. процедуру 015-023 в разделе 15. Отсоедините первичный и вторичный разъемы от дисплея ED-4. Поместите один свинец на датчик дисплея ED-4 SIGNAL контакт 4 на вторичный разъем ED-4. Поместите другой свинец на контакт 1 ВПЕРЕДЕНИЯ на первичный разъем ED-4. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Измеренная стоимость соответствует зарегистрированной стоимости? *Да | 3А |
| Измеренная стоимость соответствует зарегистрированной стоимости? **NORepair:** Проверить аналоговые каналы ввода ED-4 в журнале данных и в разделе просмотра ввода/вывода.[[513-015-035 — Display(s) and Instrumentation\|См. процедуру 015-035 в разделе 15.]]Замените ED-4, если аналоговый канал работает неправильно. См. процедуру 015-023 в разделе 15. | Ремонт завершён. |  |

### ШАГ 3. Проверьте датчик и схему дисплея ED-4.

#### ШАГ 3A. Проверьте датчик дисплея ED-4 и контакты разъема.

| **Условия:** Система поворота позволяет выключать выключатель. Отсоедините датчик дисплея ED-4 от проводов датчика OEM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема или разъема разъема разъема оболочки разбитого изоляционного повреждения Проволоки Поврежденный разъем блокировки вкладки. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Грязные или поврежденные контакты? **Ремонт: **В разъеме датчика или разъеме жгута проводов обнаружено поврежденное соединение. Очистите разъем и булавки. Почините поврежденный жгут проводов, разъем или штифты или замените датчик дисплея ED-4. Замените проводку датчика OEM. См. процедуру 015-103 в разделе 15. | Ремонт завершён. |
| Грязные или поврежденные контакты? **НЕТ** | 3B |  |

#### ШАГ 3B. Проверьте отклик цепи.

| **Условия:** Система поворота позволяет выключать выключатель. Отсоедините датчик дисплея ED-4 от проводов датчика OEM. Система включения включает переключатель. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Поместите провод перемычки между контактом сигнала датчика ED-4 и обратным контактом датчика ED-4 на разъеме проводов датчика OEM. Подожди 30 секунд. Проверьте дисплей ED-4, чтобы прочитать коды тревоги. Ссылка на соответствующую схему или схему проводов для идентификации контакта с разъемом. | Код 7267 или 7264 активен, а код 7266 или 7665 неактивен? *Да | 3C |
| Код 7267 или 7264 активен, а код 7266 или 7665 неактивен? **НЕТ** | 4А |  |

#### ШАГ 3C. Проверьте коды сигнализации и состояние датчика.

| **Условия:** Система поворота позволяет выключать выключатель. Подключите датчик дисплея ED-4 от OEM-датчика проводов. Система включения включает переключатель. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Подожди 30 секунд. Проверьте дисплей ED-4, чтобы прочитать коды тревоги. | Код тревоги 7266 или 7665 активен? Поврежденный датчик был обнаружен. См. сервисную документацию изготовителя оборудования. | Ремонт завершён. |
| Код тревоги 7266 или 7665 активен? **Норвегия: **Нет. Удаление и установка разъема исправили неисправность. | Ремонт завершён. |  |

### ШАГ 4. Проверьте оригинальную проводку датчика производителя оборудования (OEM).

#### ШАГ 4A. Проверьте контакты разъёма OEM-датчика.

| **Условия:** Система поворота позволяет выключать выключатель. Отсоедините проводку датчика OEM от C.I.B. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема или разъема разъема разъема оболочки разбитого изоляционного повреждения Проволоки Поврежденный разъем блокировки вкладки. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Грязные или поврежденные контакты? **YESRepair:** В разъеме электропроводки датчика OEM обнаружено поврежденное соединение. Очистите разъем и булавки. Замените поврежденный участок проводов датчика OEM или C.I.B. По возможности отремонтируйте поврежденную проводку, разъем или штифты. См. процедуру 015-103 в разделе 15. | Ремонт завершён. |
| Грязные или поврежденные контакты? **НЕТ** | 4B |  |

#### ШАГ 4B. Проверьте наличие открытой обратной цепи в проводах датчика OEM.

| **Условия:** Система поворота позволяет выключать выключатель. Отсоедините разъем OEM-датчика от C.I.B. Отсоедините датчик дисплея ED-4 от проводов датчика OEM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Поместите один испытательный щуп на датчик возврата дисплея ED-4 в проводку датчика OEM C.I.B. разъём. Поместите другой испытательный щуп на датчик возврата дисплея ED-4 в разъем датчика проводов OEM-датчика. Ссылка на схему схемы или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Менее 10 Ом? *Да | 4C |
| Менее 10 Ом? **NORepair:** В электропроводке датчика OEM обнаружена схема с открытым возвратом. Устранение неполадок в каждой части проводов и блока терминала. Замените при необходимости проводку датчика OEM. См. процедуру 015-103 в разделе 15. | Ремонт завершён. |  |

#### ШАГ 4C. Проверьте наличие схемы открытого сигнала в проводах датчика OEM.

| **Условия:** Система поворота позволяет выключать выключатель. Отсоедините разъем OEM-датчика от C.I.B. Отсоедините датчик дисплея ED-4 от проводов датчика OEM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Поместите один испытательный щуп на контакт сигнала датчика ED-4 на проводах датчика OEM C.I.B. разъём. Поместите другой испытательный щуп на контакт сигнала датчика ED-4 на разъем датчика проводов OEM-датчика. Ссылка на схему схемы или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Менее 10 Ом? *Да | 4D |
| Менее 10 Ом? **NORepair:** В электропроводке датчика OEM обнаружена схема открытого сигнала. Устранение неполадок в каждой части проводов и блока терминала. Замените при необходимости проводку датчика OEM. См. процедуру 015-103 в разделе 15. | Ремонт завершён |  |

#### ШАГ 4D. Проверьте неактивный код ошибки.

| **Условия: **Соединить все компоненты. Система включения включает переключатель. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте дисплей ED-4, чтобы прочитать коды тревоги. | Код ошибки AC 7266 или 7665 больше не активен? **Ремонт: **Нет. Удаление и установка разъема исправили неисправность. | Ремонт завершён. |
| Код ошибки AC 7266 или 7665 больше не активен? **Норэпар: **Поврежденный датчик обнаружен. См. информацию об услугах производителя оборудования для замены датчиков. | Ремонт завершён. |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> - Alarm Code 7266 or 7665 displayed on ED-4 screen.
>
> - Rudder angle is a constant value.
>
> ### How To Use This Tree
>
> This symptom tree can be used to troubleshoot rudder angle sensor Alarm Code. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.
>
> ### Shoptalk
>
> Alarm code 7266 and 7265 are supported on ED-4 operating with any Software Version 5 or lower
>
> Alarm code 7665 and 7664 are supported on ED-4 operating with any Software Version 6 or greater
>
> Possible causes include:
>
> - Rudder angle sensor malfunction
>
> - Rudder angle signal shorted high.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the Alarm Codes. |  |
> |  | **STEP 1A.** Check for an active fault code. | Alarm Code 7266 or 7665 active? |
> | STEP 2. | Check the ED-4 display. |  |
> |  | **STEP 2A.** Verify sensor data in the ED-4 display. | Measured value matches the recorded value? |
> | STEP 3. | Check the ED-4 display sensor and circuit. |  |
> |  | **STEP 3A.** Inspect the ED-4 display sensor and connector pins. | Dirty or damaged pins? |
> |  | **STEP 3B.** Check the circuit response. | Alarm Code 7267 or 7664 active and Alarm Code 7266 or 7665 inactive? |
> |  | **STEP 3C.** Check the Alarm Codes and verify sensor condition. | Alarm Code 7266 or 7665 active? |
> | STEP 4. | Check the original equipment manufacturer (OEM) sensor wiring harness. |  |
> |  | **STEP 4A.** Inspect the OEM sensor wiring harness connector pins. | Dirty or damaged pins? |
> |  | **STEP 4B.** Check for an open return circuit in the OEM sensor wiring harness. | Less than 10 ohms? |
> |  | **STEP 4C.** Check for an open signal circuit in the OEM sensor wiring harness. | Less than 10 ohms? |
> |  | **STEP 4D.** Check for an inactive fault code. | Alarm Code 7266 or 7665 no longer active? |
>
> ### STEP 1. Check the Alarm Codes.
>
> #### STEP 1A. Check for an active fault code.
>
> | **Conditions:** Turn system enable switch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the ED-4 display to read the Alarm Codes. | Alarm Code 7266 or 7665 active? **YES** | 2A |
> | Alarm Code 7266 or 7665 active? **NO** | 2A |  |
>
> ### STEP 2. Check the ED-4 display.
>
> #### STEP 2A. Verify sensor data in the ED-4 display.
>
> | **Conditions:** Turn system enable switch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Record the ED-4 display sensor raw value in the I/O viewer. Disconnect the ED-4 display from the Customer Interface Box (C.I.B.). Refer to Procedure 015-023 in section 15. Disconnect the primary and secondary connectors from the ED-4 display. Place one lead on ED-4 display sensor SIGNAL pin 4 on the ED-4 secondary connector. Place the other lead on the RETURN pin 1 on the ED-4 primary connector. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Measured value matches the recorded value? **YES** | 3A |
> | Measured value matches the recorded value? **NORepair:** Check ED-4 display analog Input channels in the data log and view - I/O viewer section. [[513-015-035 — Display(s) and Instrumentation\|Refer to Procedure 015-035 in section 15.]] Replace ED-4 if analog channel is **not** working properly. Refer to Procedure 015-023 in section 15. | Repair complete. |  |
>
> ### STEP 3. Check the ED-4 display sensor and circuit.
>
> #### STEP 3A. Inspect the ED-4 display sensor and connector pins.
>
> | **Conditions:** Turn system enable switch OFF. Disconnect the ED-4 display sensor from the OEM sensor wiring harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the sensor connector or harness connector. Clean the connector and pins. Repair the damaged harness, connector, or pins, or replace the ED-4 display sensor. Replace the OEM sensor wiring harness. Refer to Procedure 015-103 in Section 15. | Repair complete. |
> | Dirty or damaged pins? **NO** | 3B |  |
>
> #### STEP 3B. Check the circuit response.
>
> | **Conditions:** Turn system enable switch OFF. Disconnect the ED-4 display sensor from the OEM sensor wiring harness. Turn system enable switch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Place a jumper wire between the ED-4 display sensor SIGNAL pin and ED-4 display sensor RETURN pin at the OEM sensor wiring harness connector. Wait 30 seconds. Check the ED-4 display to read the Alarm Codes. Reference the appropriate circuit or wiring diagram for connector pin identification. | Alarm Code 7267 or 7264 active and Alarm Code 7266 or 7665 inactive? **YES** | 3C |
> | Alarm Code 7267 or 7264 active and Alarm Code 7266 or 7665 inactive? **NO** | 4A |  |
>
> #### STEP 3C. Check the Alarm Codes and verify sensor condition.
>
> | **Conditions:** Turn system enable switch OFF. Connect the ED-4 display sensor from the OEM sensor wiring harness. Turn system enable switch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Wait 30 seconds. Check the ED-4 display to read the Alarm Codes. | Alarm Code 7266 or 7665 active? **YESRepair:** A damaged sensor has been detected. See equipment manufacturer service information. | Repair complete. |
> | Alarm Code 7266 or 7665 active? **NORepair:** None. The removal and installation of the connector corrected the fault. | Repair complete. |  |
>
> ### STEP 4. Check the original equipment manufacturer (OEM) sensor wiring harness.
>
> #### STEP 4A. Inspect the OEM sensor wiring harness connector pins.
>
> | **Conditions:** Turn system enable switch OFF. Disconnect the OEM sensor wiring harness from the C.I.B. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the OEM sensor wiring harness connector. Clean the connector and pins. Replace the damaged section of the OEM sensor wiring harness or the C.I.B. Repair the damaged harness, connector, or pins, if possible. Refer to Procedure 015-103 in Section 15. | Repair complete. |
> | Dirty or damaged pins? **NO** | 4B |  |
>
> #### STEP 4B. Check for an open return circuit in the OEM sensor wiring harness.
>
> | **Conditions:** Turn system enable switch OFF. Disconnect the OEM sensor wiring harness connector from the C.I.B. Disconnect the ED-4 display sensor from the OEM sensor wiring harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Place one test lead on the ED-4 display sensor RETURN pin at the OEM sensor wiring harness C.I.B. connector. Place the other test lead on the ED-4 display sensor RETURN pin at the OEM sensor wiring harness sensor connector. Reference the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Less than 10 ohms? **YES** | 4C |
> | Less than 10 ohms? **NORepair:** An open return circuit has been detected in the OEM sensor wiring harness. Troubleshoot each section of the harness and terminal block. Replace the OEM sensor wiring harness, if necessary. Refer to Procedure 015-103 in Section 15. | Repair complete. |  |
>
> #### STEP 4C. Check for an open signal circuit in the OEM sensor wiring harness.
>
> | **Conditions:** Turn system enable switch OFF. Disconnect the OEM sensor wiring harness connector from the C.I.B. Disconnect the ED-4 display sensor from the OEM sensor wiring harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Place one test lead on the ED-4 display sensor SIGNAL pin at the OEM sensor wiring harness C.I.B. connector. Place the other test lead on the ED-4 display sensor SIGNAL pin at the OEM sensor wiring harness sensor connector. Reference the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Less than 10 ohms? **YES** | 4D |
> | Less than 10 ohms? **NORepair:** An open signal circuit has been detected in the OEM sensor wiring harness. Troubleshoot each section of the harness and terminal block. Replace the OEM sensor wiring harness, if necessary. Refer to Procedure 015-103 in Section 15. | Repair complete |  |
>
> #### STEP 4D. Check for an inactive fault code.
>
> | **Conditions:** Connect all components. Turn system enable switch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the ED-4 display to read the Alarm Codes. | Fault Code AC 7266 or 7665 no longer active? **YESRepair:** None. The removal and installation of the connector corrected the fault. | Repair complete. |
> | Fault Code AC 7266 or 7665 no longer active? **NORepair:** A damaged sensor has been detected. See equipment manufacturer service information for sensor replacement. | Repair complete. |  |
