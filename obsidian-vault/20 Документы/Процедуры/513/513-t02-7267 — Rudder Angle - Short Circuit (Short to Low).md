---
type: "Процедура"
doc: "513-t02-7267"
title_en: "Rudder Angle - Short Circuit (Short to Low)"
modified: "2019-09-30"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-t02-7267.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-t02-7267.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/513"
  - "перевод/машинный"
---

# Rudder Angle - Short Circuit (Short to Low)

> [!abstract] Процедура · `513-t02-7267`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[5411480 — C Command Connect and Connect Premier Marine Panel Systems PS102, PS103 and PS108 Mas|5411480]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2019-09-30
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-t02-7267.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-t02-7267.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

### Симптомы

- Код тревоги 7267 или 7664, отображаемый на экране ED-4.

- Угол руля является постоянным значением.

### Как пользоваться этим деревом

Это дерево симптомов может быть использовано для устранения неполадок датчика угла поворота руля. Начните с шага 1 поиска неисправностей. На шаге 2 система задаст ряд вопросов и по симптому выдаст перечень действий по поиску неисправности.

### Практические замечания

Код сигнализации 7266 и 7265 поддерживается на ED-4, работающем с любым программным обеспечением версии 5 или ниже.

Код сигнализации 7665 и 7664 поддерживается на ED-4, работающем с любым программным обеспечением версии 6 или выше.

Возможные причины включают:

- Неисправность датчика угла поворота

- Сигнал угла поворота закоротил низко.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте коды сигнализации. |  |
|  | **STEP 1A.** Проверить коды сигнализации датчика питания. | Код тревоги 7267 или 7664 активен? |
| ШАГ 2. | Проверьте дисплей ED-4. |  |
|  | **STEP 2A.** Проверить данные датчика на дисплее ED-4. | Измеренная стоимость соответствует зарегистрированной стоимости? |
| ШАГ 3. | Проверьте датчик угла поворота руля и разъём жгута проводов. |  |
|  | **STEP 3A.** Осмотрите датчик угла поворота руля и контакты разъема. | Грязные или поврежденные контакты? |
|  | **STEP 3B.** Проверьте реакцию цепи. | Примерно 12 ВДЦ? |
|  | **STEP 3C.** Проверьте реакцию цепи. | Код 7267 или 7664 активен, а код 7267 или 7664 неактивен? |
|  | **STEP 3D.** Проверьте коды сигнализации и состояние датчика. | Код тревоги 7267 или 7664 активен? |
| ШАГ 4. | Проверьте оригинальную проводку датчика производителя оборудования (OEM). |  |
|  | **STEP 4A.** Проверить контакты разъёма соединительного устройства с датчиком OEM. | Грязные или поврежденные контакты? |
|  | **STEP 4B.** Проверьте короткое замыкание в проводах датчика OEM. | Больше 100 тысяч ом? |
|  | **STEP 4C.** Проверьте короткое замыкание от пин-до земли. | Больше 100 тысяч ом? |
|  | **STEP 4D.** Проверить неактивный код ошибки. | Код тревоги 7267 или 7664 больше не активен? |

### ШАГ 1. Проверьте коды сигнализации.

#### ШАГ 1A. Проверьте коды сигнализации датчика питания.

| **Условия:** Система включения включает включение. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Подожди 30 секунд. Проверьте дисплей ED-4, чтобы прочитать коды сигнализации. | Код тревоги 7267 или 7664 активен? *Да | 2А |
| Код тревоги 7267 или 7664 активен? **НЕТ** | 2А |  |

### ШАГ 2. Проверьте дисплей ED-4.

#### ШАГ 2A. Проверка данных датчика на дисплее ED-4.

| **Условия:** Система включения включает включение. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Запись угла поворота руля датчик необработанного значения в I/O зритель. Отключите дисплей ED-4 от окна клиентского интерфейса (C.I.B.). См. процедуру 015-023 в разделе 15. Отсоедините первичный и вторичный разъемы от дисплея ED-4. Поместите один свинец на датчик дисплея ED-4 SIGNAL контакт 4 на вторичный разъем ED-4. Поместите другой свинец на контакт 1 ВПЕРЕДЕНИЯ на первичный разъем ED-4. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Измеренная стоимость соответствует зарегистрированной стоимости? *Да | 3А |
| Измеренная стоимость соответствует зарегистрированной стоимости? **NORepair:** Проверить аналоговые каналы ввода ED-4 в журнале данных и в разделе просмотра ввода/вывода.[[513-015-035 — Display(s) and Instrumentation\|См. процедуру 015-035 в разделе 15.]]Замените ED-4, если аналоговый канал работает неправильно. См. процедуру 015-023 в разделе 15. | Ремонт завершён. |  |

### ШАГ 3. Проверьте датчик угла поворота руля и разъём жгута проводов.

#### ШАГ 3A. Проверьте датчик угла поворота руля и контакты разъема.

| **Условия:** Система поворота позволяет выключать выключатель. Отсоедините датчик угла поворота руля от электропроводки датчика OEM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема или разъема разъема разъема оболочки разбитого изоляционного повреждения Проволоки Поврежденный разъем блокировки вкладки. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Грязные или поврежденные контакты? **Ремонт: **В датчике или разъёме жгута проводов обнаружено поврежденное соединение. Очистите разъем и булавки. Ремонт поврежденной проводов жгута, разъема или булавок. Замените проводку упряжкой. См. процедуру 015-103 в разделе 15. | Ремонт завершён. |
| Грязные или поврежденные контакты? **НЕТ** | 3B |  |

#### ШАГ 3B. Проверьте отклик цепи.

| **Условия:** Система поворота позволяет выключать выключатель. Отсоедините разъем датчика угла руля от проводов датчика OEM. Система включения включает переключатель. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерить напряжение между контактом питания уровня угла руля и обратным контактом уровня угла руля на разъеме датчика уровня угла руля проводов OEM-датчика. См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов использования мультиметра.[[99-019-359 — Multimeter Usage\|См. процедуру 019-359 в разделе 19.]] | Примерно 12 ВДЦ? *Да | 3C |
| Примерно 12 ВДЦ? **НЕТ** | 4А |  |

#### ШАГ 3C. Проверьте отклик цепи.

| **Условия:** Система поворота позволяет выключать выключатель. Отсоедините датчик угла поворота руля от электропроводки датчика OEM. Система включения включает переключатель. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Подожди 30 секунд. Проверьте дисплей ED-4, чтобы прочитать коды сигнализации. | Код 7266 или 7665 активен, а код 7267 или 7664 неактивен? *Да | 3D |
| Код 7266 или 7665 активен, а код 7267 или 7664 неактивен? **НЕТ** | 4А |  |

#### ШАГ 3D. Проверьте коды сигнализации и состояние датчика.

| **Условия:** Система поворота позволяет выключать выключатель. Отсоедините датчик угла поворота руля от электропроводки датчика OEM. Система включения включает переключатель. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Подожди 30 секунд. Проверьте дисплей ED-4, чтобы прочитать коды сигнализации. | Код тревоги 7267 или 7664 активен? Поврежденный датчик был обнаружен. См. сервисную документацию изготовителя оборудования. | Ремонт завершён. |
| Код тревоги 7267 или 7664 активен? **Норвегия: **Нет. Удаление и установка разъема исправили неисправность. | Ремонт завершён. |  |

### ШАГ 4. Проверьте оригинальную проводку датчика производителя оборудования (OEM).

#### ШАГ 4A. Проверьте контакты разъёма OEM-датчика.

| **Условия:** Система поворота позволяет выключать выключатель. Отсоедините проводку датчика OEM от C.I.B. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема или разъема разъема разъема оболочки разбитого изоляционного повреждения Проволоки Поврежденный разъем блокировки вкладки. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Грязные или поврежденные контакты? **YESRepair:** В разъеме электропроводки датчика OEM обнаружено поврежденное соединение. Очистите разъем и булавки. По возможности отремонтируйте поврежденную проводку, разъем или штифты. См. процедуру 015-103 в разделе 15. | Ремонт завершён. |
| Грязные или поврежденные контакты? **НЕТ** | 4B |  |

#### ШАГ 4B. Проверьте короткое замыкание контакт-контакт в электропроводке датчика OEM.

| **Условия:** Система поворота позволяет выключать выключатель. Отсоедините разъем OEM-датчика от C.I.B. Отсоедините датчик угла поворота руля от электропроводки датчика OEM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерить сопротивление между контактом сигнала датчика угла поворота руля в проводах датчика OEM C.I.B. разъем и все другие штифты в проводах датчика OEM C.I.B. разъём. Ссылка на схему схемы или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Больше 100 тысяч ом? *Да | 4C |
| Больше 100 тысяч ом? **NORepair: **В электропроводке датчика OEM обнаружено короткое замыкание на проводе SIGNAL. Замените при необходимости проводку датчика OEM. См. процедуру 015-103 в разделе 15. | Ремонт завершён. |  |

#### ШАГ 4C. Проверьте короткое замыкание от булавки до земли.

| **Условия:** Система поворота позволяет выключать выключатель. Отсоедините разъем OEM-датчика от C.I.B. Отсоедините датчик угла поворота руля от электропроводки датчика OEM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерить сопротивление между контактом сигнала датчика угла поворота руля в проводах датчика OEM C.I.B. Разъем и земля. Ссылка на схему схемы или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Больше 100 тысяч ом? *Да | 4D |
| Больше 100 тысяч ом? **NORepair:** В электропроводке датчика OEM обнаружено короткое замыкание от пин-до земли на проводе SIGNAL. Устранение неполадок в каждой части проводов и блока терминала. Замените при необходимости проводку датчика OEM. См. процедуру 015-103 в разделе 15. | Ремонт завершён. |  |

#### ШАГ 4D. Проверьте неактивный код ошибки.

| **Условия: **Соединить все компоненты. Система включения включает переключатель. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Подожди 30 секунд. Проверьте дисплей ED-4, чтобы прочитать коды сигнализации. | Код тревоги 7267 или 7664 больше не активен? **Ремонт: **Нет. Удаление и установка разъема исправили неисправность. | Ремонт завершён. |
| Код тревоги 7267 или 7664 больше не активен? **Норэпар: **Поврежденный датчик обнаружен. Заменить датчик угла поворота руля. См. сервисную документацию изготовителя оборудования. | Ремонт завершён. |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ### Symptoms
>
> - Alarm Code 7267 or 7664 displayed on ED-4 screen.
>
> - Rudder angle is a constant value.
>
> ### How To Use This Tree
>
> This symptom tree can be used to troubleshoot rudder angle sensor alarm code. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.
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
> - Rudder angle signal shorted low.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the alarm codes. |  |
> |  | **STEP 1A.** Check for sensor supply alarm codes. | Alarm Code 7267 or 7664 active? |
> | STEP 2. | Check the ED-4 display. |  |
> |  | **STEP 2A.** Verify sensor data in the ED-4 display. | Measured value matches the recorded value? |
> | STEP 3. | Check the rudder angle level sensor and harness connector. |  |
> |  | **STEP 3A.** Inspect the rudder angle level sensor and connector pins. | Dirty or damaged pins? |
> |  | **STEP 3B.** Check the circuit response. | Approximately 12 VDC? |
> |  | **STEP 3C.** Check the circuit response. | Alarm Code 7267 or 7664 active and Alarm Code 7267 or 7664 inactive? |
> |  | **STEP 3D.** Check the alarm codes and verify sensor condition. | Alarm Code 7267 or 7664 active? |
> | STEP 4. | Check the original equipment manufacturer (OEM) sensor wiring harness. |  |
> |  | **STEP 4A.** Inspect the OEM sensor wiring harness connector pins. | Dirty or damaged pins? |
> |  | **STEP 4B.** Check for a pin-to-pin short circuit in the OEM sensor wiring harness. | Greater than 100k ohms? |
> |  | **STEP 4C.** Check for a pin-to-ground short circuit. | Greater than 100k ohms? |
> |  | **STEP 4D.** Check for an inactive fault code. | Alarm Code 7267 or 7664 no longer active? |
>
> ### STEP 1. Check the alarm codes.
>
> #### STEP 1A. Check for sensor supply alarm codes.
>
> | **Conditions:** Turn system enable switch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Wait 30 seconds. Check the ED-4 display to read the alarm codes. | Alarm Code 7267 or 7664 active? **YES** | 2A |
> | Alarm Code 7267 or 7664 active? **NO** | 2A |  |
>
> ### STEP 2. Check the ED-4 display.
>
> #### STEP 2A. Verify sensor data in the ED-4 display.
>
> | **Conditions:** Turn system enable switch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Record the rudder angle sensor raw value in the I/O viewer. Disconnect the ED-4 display from the Customer Interface Box (C.I.B.). Refer to Procedure 015-023 in section 15. Disconnect the primary and secondary connectors from the ED-4 display. Place one lead on ED-4 display sensor SIGNAL pin 4 on the ED-4 secondary connector. Place the other lead on the RETURN pin 1 on the ED-4 primary connector. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Measured value matches the recorded value? **YES** | 3A |
> | Measured value matches the recorded value? **NORepair:** Check ED-4 display analog input channels in the data log and view - I/O viewer section. [[513-015-035 — Display(s) and Instrumentation\|Refer to Procedure 015-035 in section 15.]] Replace ED-4 if analog channel is **not** working properly. Refer to Procedure 015-023 in section 15. | Repair complete. |  |
>
> ### STEP 3. Check the rudder angle level sensor and harness connector.
>
> #### STEP 3A. Inspect the rudder angle level sensor and connector pins.
>
> | **Conditions:** Turn system enable switch OFF. Disconnect the rudder angle level sensor from the OEM sensor wiring harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the sensor or harness connector. Clean the connector and pins. Repair the damaged harness, connector, or pins. Replace the harness. Refer to Procedure 015-103 in Section 15. | Repair complete. |
> | Dirty or damaged pins? **NO** | 3B |  |
>
> #### STEP 3B. Check the circuit response.
>
> | **Conditions:** Turn system enable switch OFF. Disconnect the rudder angle sensor connector from the OEM sensor wiring harness. Turn system enable switch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the voltage between the rudder angle level SUPPLY pin and the rudder angle level RETURN pin at the rudder angle level sensor connector of the OEM sensor wiring harness. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general multimeter usage techniques. [[99-019-359 — Multimeter Usage\|Refer to Procedure 019-359 in Section 19.]] | Approximately 12 VDC? **YES** | 3C |
> | Approximately 12 VDC? **NO** | 4A |  |
>
> #### STEP 3C. Check the circuit response.
>
> | **Conditions:** Turn system enable switch OFF. Disconnect the rudder angle level sensor from the OEM sensor wiring harness. Turn system enable switch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Wait 30 seconds. Check the ED-4 display to read the alarm codes. | Alarm Code 7266 or 7665 active and Alarm Code 7267 or 7664 inactive? **YES** | 3D |
> | Alarm Code 7266 or 7665 active and Alarm Code 7267 or 7664 inactive? **NO** | 4A |  |
>
> #### STEP 3D. Check the alarm codes and verify sensor condition.
>
> | **Conditions:** Turn system enable switch OFF. Disconnect the rudder angle level sensor from the OEM sensor wiring harness. Turn system enable switch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Wait 30 seconds. Check the ED-4 display to read the alarm codes. | Alarm Code 7267 or 7664 active? **YESRepair:** A damaged sensor has been detected. See equipment manufacturer service information. | Repair complete. |
> | Alarm Code 7267 or 7664 active? **NORepair:** None. The removal and installation of the connector corrected the fault. | Repair complete. |  |
>
> ### STEP 4. Check the original equipment manufacturer (OEM) sensor wiring harness.
>
> #### STEP 4A. Inspect the OEM sensor wiring harness connector pins.
>
> | **Conditions:** Turn system enable switch OFF. Disconnect the OEM sensor wiring harness from the C.I.B. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the OEM sensor wiring harness connector. Clean the connector and pins. Repair the damaged harness, connector, or pins, if possible. Refer to Procedure 015-103 in Section 15. | Repair complete. |
> | Dirty or damaged pins? **NO** | 4B |  |
>
> #### STEP 4B. Check for a pin-to-pin short circuit in the OEM sensor wiring harness.
>
> | **Conditions:** Turn system enable switch OFF. Disconnect the OEM sensor wiring harness connector from the C.I.B. Disconnect the rudder angle level sensor from the OEM sensor wiring harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance between the rudder angle level sensor SIGNAL pin in the OEM sensor wiring harness C.I.B. connector and all other pins in the OEM sensor wiring harness C.I.B. connector. Reference the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Greater than 100k ohms? **YES** | 4C |
> | Greater than 100k ohms? **NORepair:** A pin-to-pin short circuit on the SIGNAL wire has been detected in the OEM sensor wiring harness. Replace the OEM sensor wiring harness, if necessary. Refer to Procedure 015-103 in Section 15. | Repair complete. |  |
>
> #### STEP 4C. Check for a pin-to-ground short circuit.
>
> | **Conditions:** Turn system enable switch OFF. Disconnect the OEM sensor wiring harness connector from the C.I.B. Disconnect the rudder angle level sensor from the OEM sensor wiring harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance between the rudder angle level sensor SIGNAL pin in the OEM sensor wiring harness C.I.B. connector and ground. Reference the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Greater than 100k ohms? **YES** | 4D |
> | Greater than 100k ohms? **NORepair:** A pin-to-ground short circuit on the SIGNAL wire has been detected in the OEM sensor wiring harness. Troubleshoot each section of the harness and terminal block. Replace the OEM sensor wiring harness, if necessary. Refer to Procedure 015-103 in Section 15. | Repair complete. |  |
>
> #### STEP 4D. Check for an inactive fault code.
>
> | **Conditions:** Connect all components. Turn system enable switch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Wait 30 seconds. Check the ED-4 display to read the alarm codes. | Alarm Code 7267 or 7664 no longer active? **YESRepair:** None. The removal and installation of the connector corrected the fault. | Repair complete. |
> | Alarm Code 7267 or 7664 no longer active? **NORepair:** A damaged sensor has been detected. Replace the rudder angle level sensor. See equipment manufacturer service information. | Repair complete. |  |
