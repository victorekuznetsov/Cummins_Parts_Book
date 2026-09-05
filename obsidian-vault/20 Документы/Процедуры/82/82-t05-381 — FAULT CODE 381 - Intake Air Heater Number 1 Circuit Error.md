---
aliases:
  - "Код 381 — ошибка цепи подогревателя впускного воздуха 1"
type: "Процедура"
doc: "82-t05-381"
title_en: "FAULT CODE 381 - Intake Air Heater Number 1 Circuit Error"
title_ru: "Код 381 — ошибка цепи подогревателя впускного воздуха 1"
modified: "2012-08-26"
engines:
  - "41343322"
  - "41370103"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-t05-381.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-t05-381.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
  - "перевод/машинный"
---

# FAULT CODE 381 - Intake Air Heater Number 1 Circuit Error
**Код 381 — ошибка цепи подогревателя впускного воздуха 1**

> [!abstract] Процедура · `82-t05-381`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-08-26
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-t05-381.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-t05-381.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

## Предупреждения и меры предосторожности

> [!warning] ОСТОРОЖНО
> Чтобы не повредить новый блок управления двигателем (ЭБУ), перед его заменой разберитесь со всеми остальными активными кодами неисправностей.

> [!warning] ОСТОРОЖНО
> Чтобы не повредить контакты и жгут, при измерениях пользуйтесь следующими измерительными проводами: Номер детали 3822758 - пробный щуп типа вилки DeutschTM/AMPTM/Metri-PackTM и номер детали 3822917 - пробный щуп типа розетки DeutschTM/AMPTM/Metri-PackTM.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте коды неисправностей. |  |
|  | **STEP 1A.** Проверить неактивный код ошибки. | Код 381 неактивен? |
| ШАГ 2. | Проверьте реле и схему впускного воздушного нагревателя. |  |
|  | **STEP 2A.** Проверить реле впускного воздушного нагревателя и электрические соединения. | Грязные или поврежденные контакты? |
|  | **STEP 2B.** Проверьте наличие открытой цепи в реле впускного воздушного нагревателя. | Менее 10 Ом? |
|  | **STEP 2C.** Проверьте диагностическое напряжение впускного воздушного нагревателя, провода SUPPLY и обратную цепь. | Больше, чем 3,75-VDC? |
|  | **STEP 2D.** Проверьте наличие открытой цепи в цепи возврата реле впускного воздушного нагревателя. | Менее 10 Ом? |
| ШАГ 3. | Проверьте электропроводку ECM и производителя оригинального оборудования (OEM). |  |
|  | **STEP 3A.** Проверить контакты разъёма электропроводки ECM и OEM. | Грязные или поврежденные контакты? |
|  | **STEP 3B.** Проверьте наличие открытой цепи в электропроводке OEM. | Менее 10 Ом? |
|  | **STEP 3C.** Проверьте короткое замыкание в проводной ремне OEM. | Больше 100 тысяч ом? |
|  | **STEP 3D.** Проверить неактивный код ошибки. | Код 381 неактивен? |
| ШАГ 4. | Очистите код ошибки. |  |
|  | **STEP 4A.** Отключить код ошибки. | Код 381 неактивен? |
|  | **STEP 4B.** Очистить коды неактивных ошибок. | Все коды неисправностей очищены? |

### ШАГ 1. Проверьте коды неисправностей.

#### ШАГ 1A. Проверьте неактивный код ошибки.

| **Условия:** Включить переключатель зажигания. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте неактивный код ошибки. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Код 381 неактивен? *Да | [[99-019-362 — Inactive or Intermittent Fault Code\|См. процедуру 019-362 в разделе 19.]] |
| Код 381 неактивен? **НЕТ** | 2А |  |

### ШАГ 2. Проверьте реле и схему впускного воздушного нагревателя.

#### ШАГ 2A. Осмотрите реле впускного воздушного нагревателя и электрические соединения.

| **Условия:** Выключите замок зажигания. Отсоедините реле впускного воздушного нагревателя от проводной ремни OEM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Осмотрите проводные реле OEM-проводов и реле реле впускного воздушного нагревателя на предмет: Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема или разъема разъема разъема оболочки разбитого изоляционного повреждения Проволоки Поврежденный разъем блокировки вкладки. Выполните эти проверки на всех соединительных проводных разъёмах в цепи. Смотрите схему или схему проводов, чтобы идентифицировать разъемы и контакты. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Грязные или поврежденные контакты? **Ремонт: **В датчике или разъёме жгута проводов обнаружено поврежденное соединение. По возможности отремонтируйте поврежденную проводку, разъем или штифты. Смой грязь, мусор или влагу из контактов разъема. Используйте электрическую контактную очистку, номер детали 3824510. Установите соответствующий уплотнитель разъема, если он поврежден или отсутствует. См. процедуру 019-071 в разделе 19. | 4А |
| Грязные или поврежденные контакты? **НЕТ** | 2В |  |

#### ШАГ 2B. Проверьте наличие открытой цепи в реле впускного воздушного нагревателя.

| **Условия:** Выключите замок зажигания. Отсоедините реле впускного воздушного нагревателя от проводной упряжки OEM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте сопротивление реле впускного воздушного нагревателя. Измерить сопротивление между контактом сигнала впускного воздушного нагревателя и обратным контактом впускного воздушного нагревателя на реле впускного воздушного нагревателя. Примечание: Для 12-вольтных систем оба реле **должны проверяться индивидуально. См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Менее 10 Ом? *Да** | 2C |
| Менее 10 Ом? **NORepair:** В реле впускного воздушного нагревателя обнаружена открытая схема. Заменить реле впускного воздушного нагревателя. См. сервисное руководство изготовителя машины. | 4А |  |

#### ШАГ 2C. Проверьте диагностическое напряжение впускного воздушного нагревателя, провод SUPPLY и обратную цепь.

| **Условия:** Выключите замок зажигания. Отсоедините реле впускного воздушного нагревателя от проводной упряжки OEM. Включите зажигание. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте напряжение подачи впускного воздушного нагревателя и обратную цепь. Измерить напряжение между реле воздухонагревателя впускного воздуха SIGNAL провода и реле воздухонагревателя впускного воздуха RETURN провода на реле впускного нагревателя реле разъёма провода OEM. Примечание: Для 12-вольтных систем оба провода **должны быть протестированы. | Больше, чем 3,75-VDC? *Да** | 3C |
| Больше, чем 3,75-VDC? **НЕТ** | 2D |  |

#### ШАГ 2D. Проверьте наличие открытой цепи в цепи возврата реле впускного воздушного нагревателя.

| **Условия:** Выключите замок зажигания. Отсоедините реле впускного воздушного нагревателя от проводной упряжки OEM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте цепь на обрыв. Измерить сопротивление между реле реле впускного воздушного нагревателя обратного контакта на реле реле впускного воздушного нагревателя разъёма с землей. См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Менее 10 Ом? *Да | 3А |
| Менее 10 Ом? **NORepair: **Открытая цепь на проводе RETURN обнаружена. См. диаграмму проводов OEM для конфигурации провода RETURN. Если ВПВП подключен к ECM, отремонтируйте или замените проводку OEM. См. процедуру 019-071 в разделе 19. Если провод RETURN заземлен до заземления шасси или блока двигателя, отремонтируйте источник поврежденного соединения. Очистите, отремонтируйте или замените электропроводку OEM, если это возможно. См. процедуру 019-071 в разделе 19. | 4А |  |

### ШАГ 3. Проверьте электропроводку ECM и OEM.

#### ШАГ 3A. Проверьте контакты разъёма ECM и OEM-проводов.

| **Условия:** Выключите замок зажигания. Отсоедините проводку OEM от разъема ECM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Осмотрите контакты разъема ECM с проводкой OEM для следующих целей: Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема или разъема разъема разъема оболочки разбитого изоляционного повреждения Проволоки Поврежденный разъем блокировки вкладки. Выполните эти проверки на всех соединительных проводных разъёмах в цепи. Используйте схему или схему проводов для идентификации разъемов и контактов. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Грязные или поврежденные контакты? **Ремонт: **В разъеме электропроводки ECM или OEM обнаружено поврежденное соединение. По возможности отремонтируйте поврежденную проводку, разъем или штифты. Смой грязь, мусор или влагу из контактов разъема. Используйте электрическую контактную очистку, номер детали 3824510. Установите соответствующий уплотнитель разъема, если он поврежден или отсутствует. См. процедуру 019-071 в разделе 19. | 4А |
| Грязные или поврежденные контакты? **НЕТ** | 3B |  |

#### ШАГ 3B. Проверьте наличие открытой цепи в OEM-проводах.

| **Условия:** Выключите замок зажигания. Отсоедините проводку OEM от разъема ECM. Отсоедините реле впускного воздушного нагревателя от проводной упряжки OEM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте цепь на обрыв. Измерить сопротивление между OEM проводкой реле реле впускного воздушного нагревателя ECM и реле OEM реле SIGNAL провода. Примечание: Для 12-вольтных систем оба провода **должны быть протестированы. См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Менее 10 Ом? *Да** | 3C |
| Менее 10 Ом? **NORepair:** В электропроводке OEM обнаружена схема ретрансляции реле впускного воздушного нагревателя. Ремонт или замена OEM проводов жгута. См. процедуру 019-071 в разделе 19. | 4А |  |

#### ШАГ 3C. Проверьте короткое замыкание контакт-контакт в электропроводке OEM.

| **Условия:** Выключите замок зажигания. Отсоедините проводку OEM от разъема ECM. Отсоедините впускной воздушный обогреватель от проводной упряжки OEM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте короткое контактное соединение. Измерьте сопротивление между контактом ретранслятора впускного воздушного нагревателя в разъёме ECM проводов OEM и всеми другими штифтами в разъеме ECM. См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Больше 100 тысяч ом? *Да | 3D |
| Больше 100 тысяч ом? **NORepair:** В электропроводке OEM обнаружено короткое замыкание на реле впускного воздушного нагревателя SIGNAL. Ремонт или замена OEM проводов жгута. См. процедуру 019-071 в разделе 19. | 4А |  |

#### ШАГ 3D. Проверьте неактивный код ошибки.

| **Условия: **Соединить все компоненты. Включите зажигание. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте соответствующую реакцию цепи через 30 секунд. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Код 381 неактивен? **Ремонт: **Нет. Удаление и установка разъема исправили неисправность. | 4А |
| Код 381 неактивен? Заменить ЭКМ.[[82-019-031 — Engine Control Module\|См. процедуру 019-031 в разделе 19.]] | 4А |  |

### ШАГ 4. Очистите код ошибки.

#### ШАГ 4A. Отключите код неисправности.

| **Условия: **Соединить все компоненты. Включите зажигание. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Отключите код неисправности. Запустите двигатель и запускайте его на холостом ходу в течение 1 минуты. Используйте инструмент электронного сервиса INSITETM для проверки неактивности кода ошибки. | Код 381 неактивен? *Да | 4B |
| Код 381 неактивен? **NORepair:** Возврат к шагам устранения неполадок или свяжитесь с авторизованным местом ремонта Cummins®, если все шаги были завершены и проверены снова. | 1А |  |

#### ШАГ 4B. Сбросьте неактивные коды неисправностей.

| **Условия: **Соединить все компоненты. Включите зажигание. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Сбросьте неактивные коды неисправностей. Используйте инструмент электронного сервиса INSITETM для очистки кодов неактивных ошибок. | Все коды неисправностей очищены? *Да | Ремонт завершён |
| Все коды неисправностей очищены? **NORepair: **Устранение неполадок с оставшимися активными кодами неисправностей. | Соответствующие шаги по устранению неполадок |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ## Warnings and Cautions
>
> **CAUTION · Осторожно**
> To reduce the possibility of damaging a new engine control module (ECM), all other active fault codes must be investigated prior to replacing the ECM.
>
> **CAUTION · Осторожно**
> To reduce the possibility of pin and harness damage, use the following test leads when taking a measurement: Part Number 3822758 - male Deutsch™/AMP™/Metri-Pack™ test lead and Part Number 3822917 - female Deutsch™/AMP™/Metri-Pack™ test lead.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the fault codes. |  |
> |  | **STEP 1A.** Check for an inactive fault code. | Fault Code 381 inactive? |
> | STEP 2. | Check the intake air heater relay and circuit. |  |
> |  | **STEP 2A.** Inspect the intake air heater relay and electrical connections. | Dirty or damaged pins? |
> |  | **STEP 2B.** Check for an open circuit in the intake air heater relay. | Less than 10 ohms? |
> |  | **STEP 2C.** Check the intake air heater diagnostic voltage, SUPPLY wire, and return circuit. | Greater than 3.75-VDC? |
> |  | **STEP 2D.** Check for an open circuit in the intake air heater relay return circuit. | Less than 10 ohms? |
> | STEP 3. | Check the ECM and original equipment manufacturer (OEM) harness. |  |
> |  | **STEP 3A.** Inspect the ECM and OEM harness connector pins. | Dirty or damaged pins? |
> |  | **STEP 3B.** Check for an open circuit in the OEM harness. | Less than 10 ohms? |
> |  | **STEP 3C.** Check for a pin-to-pin short circuit in the OEM harness. | Greater than 100k ohms? |
> |  | **STEP 3D.** Check for an inactive fault code. | Fault Code 381 inactive? |
> | STEP 4. | Clear the fault code. |  |
> |  | **STEP 4A.** Disable the fault code. | Fault Code 381 inactive? |
> |  | **STEP 4B.** Clear the inactive fault codes. | All fault codes cleared? |
>
> ### STEP 1. Check the fault codes.
>
> #### STEP 1A. Check for an inactive fault code.
>
> | **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for an inactive fault code. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 381 inactive? **YES** | [[99-019-362 — Inactive or Intermittent Fault Code\|Refer to Procedure 019-362 in Section 19.]] |
> | Fault Code 381 inactive? **NO** | 2A |  |
>
> ### STEP 2. Check the intake air heater relay and circuit.
>
> #### STEP 2A. Inspect the intake air heater relay and electrical connections.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the intake air heater relays from the OEM harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the OEM harness and intake air heater relay connections for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Perform these checks on all interconnecting harness connectors in the circuit. Refer to the circuit art or wiring diagram to identify the connectors and pins. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the sensor or harness connector. Repair the damaged harness, connector, or pins, if possible. Flush the dirt, debris, or moisture from the connector pins. Use electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Refer to Procedure 019-071 in Section 19. | 4A |
> | Dirty or damaged pins? **NO** | 2B |  |
>
> #### STEP 2B. Check for an open circuit in the intake air heater relay.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the intake air heater relay from the OEM harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the intake air heater relay resistance. Measure the resistance between the intake air heater SIGNAL pin and the intake air heater RETURN pin at the intake air heater relay. Note: For 12 volt systems, both relays **must** be checked individually. Refer to the circuit diagram or the wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Less than 10 ohms? **YES** | 2C |
> | Less than 10 ohms? **NORepair:** An open circuit has been detected in the intake air heater relay. Replace the intake air heater relay. Refer to the OEM service manual. | 4A |  |
>
> #### STEP 2C. Check the intake air heater diagnostic voltage, SUPPLY wire, and return circuit.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the intake air heater relay from the OEM harness. Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the intake air heater supply voltage and return circuit. Measure the voltage between the intake air heater relay SIGNAL wire and the intake air heater relay RETURN wire at the intake air heater relay connector of the OEM harness. Note: For 12 volt systems, both leads **must** be tested. | Greater than 3.75-VDC? **YES** | 3C |
> | Greater than 3.75-VDC? **NO** | 2D |  |
>
> #### STEP 2D. Check for an open circuit in the intake air heater relay return circuit.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the intake air heater relay from the OEM harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for an open circuit. Measure the resistance between the intake air heater relay RETURN pin at the intake air heater relay connector to ground. Refer to the circuit diagram or the wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Less than 10 ohms? **YES** | 3A |
> | Less than 10 ohms? **NORepair:** An open circuit on the RETURN wire has been detected. Refer to the OEM wiring diagram for RETURN wire configuration. If the RETURN is wired to the ECM, repair or replace the OEM harness. Refer to Procedure 019-071 in Section 19. If the RETURN wire is grounded to chassis or engine block ground, repair the source of the damaged connection. Clean, repair, or replace the OEM harness, if possible. Refer to Procedure 019-071 in Section 19. | 4A |  |
>
> ### STEP 3. Check the ECM and OEM harness.
>
> #### STEP 3A. Inspect the ECM and OEM harness connector pins.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness from the ECM connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the OEM harness ECM connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Perform these checks on all interconnecting harness connectors in the circuit. Use the circuit art or wiring diagram to identify the connectors and pins. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the ECM or OEM harness connector. Repair the damaged harness, connector, or pins, if possible. Flush the dirt, debris, or moisture from the connector pins. Use electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Refer to Procedure 019-071 in Section 19. | 4A |
> | Dirty or damaged pins? **NO** | 3B |  |
>
> #### STEP 3B. Check for an open circuit in the OEM harness.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness from the ECM connector. Disconnect the intake air heater relay from the OEM harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for an open circuit. Measure the resistance between the OEM harness ECM connector intake air heater relay SIGNAL pin and the OEM harness intake air heater relay connector SIGNAL wire. Note: For 12 volt systems, both leads **must** be tested. Refer to the circuit diagram or the wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Less than 10 ohms? **YES** | 3C |
> | Less than 10 ohms? **NORepair:** An open intake air heater relay signal circuit has been detected in the OEM harness. Repair or replace the OEM harness. Refer to Procedure 019-071 in Section 19. | 4A |  |
>
> #### STEP 3C. Check for a pin-to-pin short circuit in the OEM harness.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness from the ECM connector. Disconnect the intake air heater from the OEM harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for a pin-to-pin short. Measure the resistance between the intake air heater relay SIGNAL pin in the OEM harness ECM connector and all other pins in the ECM connector. Refer to the circuit diagram or the wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Greater than 100k ohms? **YES** | 3D |
> | Greater than 100k ohms? **NORepair:** A pin-to-pin short circuit on the intake air heater relay SIGNAL wire has been detected in the OEM harness. Repair or replace the OEM harness. Refer to Procedure 019-071 in Section 19. | 4A |  |
>
> #### STEP 3D. Check for an inactive fault code.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for the appropriate circuit response after 30 seconds. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 381 inactive? **YESRepair:** None. The removal and installation of the connector corrected the fault. | 4A |
> | Fault Code 381 inactive? **NORepair:** Replace the ECM. [[82-019-031 — Engine Control Module\|Refer to Procedure 019-031 in Section 19.]] | 4A |  |
>
> ### STEP 4. Clear the fault code.
>
> #### STEP 4A. Disable the fault code.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Disable the fault code. Start the engine and let it idle for 1 minute. Use INSITE™ electronic service tool to verify that the fault code is inactive. | Fault Code 381 inactive? **YES** | 4B |
> | Fault Code 381 inactive? **NORepair:** Return to the troubleshooting steps or contact a Cummins® Authorized Repair Location if all steps have been completed and checked again. | 1A |  |
>
> #### STEP 4B. Clear the inactive fault codes.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Clear the inactive fault codes. Use INSITE™ electronic service tool to clear the inactive fault codes. | All fault codes cleared? **YES** | Repair complete |
> | All fault codes cleared? **NORepair:** Troubleshoot any remaining active fault codes. | Appropriate troubleshooting steps |  |
