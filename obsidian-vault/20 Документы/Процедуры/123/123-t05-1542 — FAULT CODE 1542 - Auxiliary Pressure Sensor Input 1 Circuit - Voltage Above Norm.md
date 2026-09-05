---
aliases:
  - "Код 1542 — цепь вспомогательного датчика давления 1 — напряжение выше нормы"
type: "Процедура"
doc: "123-t05-1542"
title_en: "FAULT CODE 1542 - Auxiliary Pressure Sensor Input 1 Circuit - Voltage Above Normal or Shorted to High Source"
title_ru: "Код 1542 — цепь вспомогательного датчика давления 1 — напряжение выше нормы"
modified: "2013-11-05"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4022094"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/123/123-t05-1542.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/123-t05-1542.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/123"
  - "перевод/машинный"
---

# FAULT CODE 1542 - Auxiliary Pressure Sensor Input 1 Circuit - Voltage Above Normal or Shorted to High Source
**Код 1542 — цепь вспомогательного датчика давления 1 — напряжение выше нормы**

> [!abstract] Процедура · `123-t05-1542`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4022094 — QSK19 CM2150 and CM2670 Electronic Control System Troubleshooting and Repair Manual|4022094]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2013-11-05
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/123/123-t05-1542.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/123-t05-1542.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте коды неисправностей. |  |
|  | **STEP 1A.** Проверка наличия датчика или нескольких кодов неисправностей. | Код ошибки 386 активен? |
| ШАГ 2. | Проверьте датчик давления и схему оригинального производителя оборудования (OEM). |  |
|  | **STEP 2A.** Проверить датчик давления OEM и контакты разъема. | Грязные или поврежденные контакты? |
|  | **STEP 2B.** Проверьте реакцию цепи. | Код 1543 активен, а Код 1542 неактивен? |
|  | **STEP 2C** Проверьте напряжение питания датчика и схему возврата. | Напряжение между 4,75-VDC и 5,25-VDC? |
|  | **STEP 2D.** Проверьте коды неисправностей и состояние датчика. | Код 1542 активен? |
| ШАГ 3. | Проверьте модуль управления двигателем (ECM) и OEM-проводку. |  |
|  | **STEP 3A.** Проверить контакты разъёма электропроводки ECM и OEM. | Грязные или поврежденные контакты? |
|  | **STEP 3B.** Проверьте наличие открытой цепи в электропроводке OEM. | Менее 10 Ом? |
|  | **STEP 3C.** Проверьте короткое замыкание в проводной ремне OEM. | Больше 100 Км? |
|  | **STEP 3D.** Проверьте короткое замыкание в проводной ремне OEM. | Больше 100 Км? |
|  | **STEP 3E.** Проверить неактивный код ошибки. | Код 1542 неактивен? |
| ШАГ 4. | Сбросьте коды неисправностей. |  |
|  | **STEP 4A.** Отключить код ошибки. | Код 1542 неактивен? |
|  | **STEP 4B.** Очистить коды неактивных ошибок. | Все коды неисправностей очищены? |

### ШАГ 1. Проверьте коды неисправностей.

#### ШАГ 1A. Проверьте наличие датчика или нескольких кодов неисправностей.

| **Условия:** Включить переключатель зажигания. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте коды неисправностей датчика. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Код ошибки 386 активен? *Да | Посмотреть дерево устранения неполадок для кода 386. |
| Код ошибки 386 активен? **НЕТ** | 2А |  |

### ШАГ 2. Проверьте датчик давления OEM и схему.

#### ШАГ 2A. Проверьте датчик давления OEM и контакты разъема.

| **Условия:** Включить переключатель зажигания. Отсоедините датчик давления OEM от электропроводки OEM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Осмотрите контактные линзы разъёма OEM-проводов и датчика давления OEM для следующих целей: Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема или разъема разъема разъема оболочки разбитого изоляционного повреждения Проволоки Поврежденный разъем блокировки вкладки. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Грязные или поврежденные контакты? **Ремонт: **В датчике или разъёме жгута проводов обнаружено поврежденное соединение. Очистите разъем и булавки. По возможности отремонтируйте поврежденную проводку, разъем или штифты. Ремонт проводной упряжки OEM. См. процедуру 019-071 в разделе 19. | 4А |
| Грязные или поврежденные контакты? **НЕТ** | 2В |  |

#### ШАГ 2B. Проверьте отклик цепи.

| **Условия:** Выключите замок зажигания. Отсоедините датчик давления OEM от электропроводки OEM. Включите зажигание. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте соответствующую реакцию цепи через 30 секунд. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Код 1543 активен, а Код 1542 неактивен? *Да | 2C |
| Код 1543 активен, а Код 1542 неактивен? **НЕТ** | 3А |  |

#### ШАГ 2C. Проверьте напряжение питания датчика и обратную цепь.

| **Условия:** Выключите замок зажигания. Отсоедините датчик давления OEM от электропроводки OEM. Включите зажигание. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте напряжение питания и обратную цепь. Измерьте напряжение между контактом питания OEM + 5 вольт и обратным контактом давления OEM на разъеме датчика проводов OEM. См. схему или схему проводов для идентификации контакта с разъемом. | Напряжение между 4,75-VDC и 5,25-VDC? *Да | 2D |
| Напряжение между 4,75-VDC и 5,25-VDC? **НЕТ** | 3А |  |

#### ШАГ 2D. Проверьте коды неисправностей и состояние датчика.

| **Условия:** Выключите замок зажигания. Подключите датчик давления OEM к электропроводке OEM. Включите зажигание. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте соответствующую реакцию цепи через 30 секунд. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Код ошибки 1542 активен? Поврежденный датчик был обнаружен. Замените датчик давления OEM. См. руководство по обслуживанию OEM. | 4А |
| Код ошибки 1542 активен? **Норвегия: **Нет. Удаление и установка разъема исправили неисправность. | 4А |  |

### ШАГ 3. Проверьте электропроводку ECM и OEM.

#### ШАГ 3A. Проверить контакты разъёма ECM и OEM-проводов.

| **Условия:** Выключите замок зажигания. Отсоедините проводку OEM от разъема ECM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Осмотрите контакты проводов OEM и разъема ECM на предмет: Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема или разъема разъема разъема оболочки разбитого изоляционного повреждения Проволоки Поврежденный разъем блокировки вкладки. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Грязные или поврежденные контакты? **Ремонт: **В разъеме ECM или разъеме OEM-проводов обнаружено поврежденное соединение. Очистите разъем и булавки. По возможности отремонтируйте поврежденную проводку, разъем или штифты. Ремонт проводной упряжки OEM. См. процедуру 019-071 в разделе 19. | 4А |
| Грязные или поврежденные контакты? **НЕТ** | 3B |  |

#### ШАГ 3B. Проверьте наличие открытой цепи в OEM-проводах.

| **Условия:** Выключите замок зажигания. Отсоедините проводку OEM от разъема ECM. Отсоедините датчик давления OEM от электропроводки OEM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте цепь на обрыв. Измерить сопротивление между OEM проводкой ремня разъема ECM OEM давления возвратного контакта и OEM проводов ремня OEM датчика давления разъёма обратного контакта. См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Менее 10 Ом? *Да | 3C |
| Менее 10 Ом? **NORepair: **В электропроводке OEM обнаружена открытая схема RETURN. Устранение неполадок в каждой проводах, соединенной последовательно, чтобы определить, которая содержит открытую обратную цепь. Ремонт проводной упряжки OEM. См. процедуру 019-071 в разделе 19. | 4А |  |

#### ШАГ 3C. Проверьте короткое замыкание контакт-контакт в электропроводке OEM.

| **Условия:** Выключите замок зажигания. Отсоедините проводку OEM от разъема ECM. Отсоедините датчик давления OEM от электропроводки OEM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте короткое контактное соединение. Измерьте сопротивление между контактом подачи давления OEM в разъеме ECM проводов OEM и всеми другими штифтами в разъеме ECM OEM. См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Больше 100 Км? *Да | 3E |
| Больше 100 Км? **NORepair: **В электропроводке OEM обнаружено короткое замыкание контакта с контактом на проводе SUPPLY. Устранение неполадок в каждой проводах, соединенной последовательно, чтобы определить, которая содержит контактную короткое цепь питания. Ремонт проводной упряжки OEM. См. процедуру 019-071 в разделе 19. | 4А |  |

#### ШАГ 3D. Проверьте короткое замыкание контакт-контакт в электропроводке OEM.

| **Условия:** Выключите замок зажигания. Отсоедините проводку OEM от разъема ECM. Отсоедините датчик давления OEM от электропроводки OEM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте короткое контактное соединение. Измерьте сопротивление между контактом подачи давления OEM в разъеме ECM проводов OEM и всеми другими штифтами в разъеме ECM OEM. См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Больше 100 Км? *Да | 3E |
| Больше 100 Км? **NORepair: **В электропроводке OEM обнаружено короткое замыкание контакта с контактом на проводе SUPPLY. Устранение неполадок в каждой проводах, соединенной последовательно, чтобы определить, которая содержит короткое цепь сигнала на землю. Ремонт проводной упряжки OEM. См. процедуру 019-071 в разделе 19. | 4А |  |

#### ШАГ 3E. Проверьте неактивный код ошибки.

| **Условия: **Соединить все компоненты. Включите зажигание. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте соответствующую реакцию цепи через 30 секунд. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Код 1542 неактивен? **Ремонт: **Нет. Удаление и установка разъема исправили неисправность. | 4А |
| Код 1542 неактивен? Заменить ЭКМ. См. процедуру 019-031 в разделе 19. | 4А |  |

### ШАГ 4. Сбросьте коды неисправностей.

#### ШАГ 4A. Отключить код неисправности

| **Условия: **Соединить все компоненты. Включите зажигание. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Отключите код неисправности. Используйте инструмент электронного сервиса INSITETM для проверки неактивности кода ошибки. | Код 1542 неактивен? *Да | 4B |
| Код 1542 неактивен? **NORepair:** Возврат к шагам устранения неполадок или свяжитесь с авторизованным местом ремонта Cummins®, если все шаги были завершены и проверены снова. | 1А |  |

#### ШАГ 4B. Сбросьте неактивные коды неисправностей.

| **Условия: **Соединить все компоненты. Включите зажигание. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Сбросьте неактивные коды неисправностей. Используйте инструмент электронного сервиса INSITETM для очистки кодов неактивных ошибок. | Все коды неисправностей очищены? *Да | Ремонт завершён. |
| Все коды неисправностей очищены? **NORepair:** Перейдите к соответствующим шагам по устранению неполадок. | 1А |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the fault codes. |  |
> |  | **STEP 1A.** Check for sensor supply or multiple fault codes. | Fault Code 386 active? |
> | STEP 2. | Check the original equipment manufacturer (OEM) pressure sensor and circuit. |  |
> |  | **STEP 2A.** Inspect the OEM pressure sensor and connector pins. | Dirty or damaged pins? |
> |  | **STEP 2B.** Check the circuit response. | Fault Code 1543 active and Fault Code 1542 inactive? |
> |  | **STEP 2C.** Check the sensor supply voltage and return circuit. | Voltage between 4.75-VDC and 5.25-VDC? |
> |  | **STEP 2D.** Check the fault codes and verify sensor condition. | Fault Code 1542 is active? |
> | STEP 3. | Check the engine control module (ECM) and OEM harness. |  |
> |  | **STEP 3A.** Inspect the ECM and OEM harness connector pins. | Dirty or damaged pins? |
> |  | **STEP 3B.** Check for an open circuit in the OEM harness. | Less than 10 ohms? |
> |  | **STEP 3C.** Check for a pin-to-pin short circuit in the OEM harness. | Greater than 100K ohms? |
> |  | **STEP 3D.** Check for a pin-to-pin short circuit in the OEM harness. | Greater than 100K ohms? |
> |  | **STEP 3E.** Check for an inactive fault code. | Fault Code 1542 inactive? |
> | STEP 4. | Clear the fault codes. |  |
> |  | **STEP 4A.** Disable the fault code. | Fault Code 1542 inactive? |
> |  | **STEP 4B.** Clear the inactive fault codes. | All fault codes cleared? |
>
> ### STEP 1. Check the fault codes.
>
> #### STEP 1A. Check for sensor supply or multiple fault codes.
>
> | **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for sensor supply fault codes. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 386 active? **YES** | See the troubleshooting tree for Fault Code 386. |
> | Fault Code 386 active? **NO** | 2A |  |
>
> ### STEP 2. Check the OEM pressure sensor and circuit.
>
> #### STEP 2A. Inspect the OEM pressure sensor and connector pins.
>
> | **Conditions:** Turn keyswitch ON. Disconnect the OEM pressure sensor from the OEM harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the OEM harness and OEM pressure sensor connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the sensor or harness connector. Clean the connector and pins. Repair the damaged harness, connector, or pins, if possible. Repair the OEM harness. Refer to Procedure 019-071 in Section 19. | 4A |
> | Dirty or damaged pins? **NO** | 2B |  |
>
> #### STEP 2B. Check the circuit response.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the OEM pressure sensor from the OEM harness. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for the appropriate circuit response after 30 seconds. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 1543 active and Fault Code 1542 inactive? **YES** | 2C |
> | Fault Code 1543 active and Fault Code 1542 inactive? **NO** | 3A |  |
>
> #### STEP 2C. Check the sensor supply voltage and return circuit.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the OEM pressure sensor from the OEM harness. Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the supply voltage and return circuit. Measure the voltage between the OEM pressure +5 volt SUPPLY pin and the OEM pressure RETURN pin at the sensor connector of the OEM harness. Refer to the circuit diagram or the wiring diagram for connector pin identification. | Voltage between 4.75-VDC and 5.25-VDC? **YES** | 2D |
> | Voltage between 4.75-VDC and 5.25-VDC? **NO** | 3A |  |
>
> #### STEP 2D. Check the fault codes and verify sensor condition.
>
> | **Conditions:** Turn keyswitch OFF. Connect the OEM pressure sensor to the OEM harness. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for the appropriate circuit response after 30 seconds. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 1542 active? **YESRepair:** A damaged sensor has been detected. Replace the OEM pressure sensor. Refer to OEM service manual. | 4A |
> | Fault Code 1542 active? **NORepair:** None. The removal and installation of the connector corrected the fault. | 4A |  |
>
> ### STEP 3. Check the ECM and OEM harness.
>
> #### STEP 3A. Inspect ECM and OEM harness connector pins.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness from the ECM connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the OEM harness and ECM connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the ECM connector or OEM harness connector. Clean the connector and pins. Repair the damaged harness, connector, or pins, if possible. Repair the OEM harness. Refer to Procedure 019-071 in Section 19. | 4A |
> | Dirty or damaged pins? **NO** | 3B |  |
>
> #### STEP 3B. Check for an open circuit in the OEM harness.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness from the ECM connector. Disconnect the OEM pressure sensor from the OEM harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for an open circuit. Measure the resistance between the OEM harness ECM connector OEM pressure RETURN pin and the OEM harness OEM pressure sensor connector RETURN pin. Refer to the circuit diagram or the wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Less than 10 ohms? **YES** | 3C |
> | Less than 10 ohms? **NORepair:** An open RETURN circuit has been detected in the OEM harness. Troubleshoot each harness connected in series to determine which contains the open return circuit. Repair the OEM harness. Refer to Procedure 019-071 in Section 19. | 4A |  |
>
> #### STEP 3C. Check for a pin-to-pin short circuit in the OEM harness.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness from the ECM connector. Disconnect the OEM pressure sensor from the OEM harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for a pin-to-pin short. Measure the resistance between the OEM pressure SUPPLY pin in the OEM harness ECM connector and all other pins in the ECM OEM connector. Refer to the circuit diagram or the wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Greater than 100K ohms? **YES** | 3E |
> | Greater than 100K ohms? **NORepair:** A pin-to-pin short circuit on the SUPPLY wire has been detected in the OEM harness. Troubleshoot each harness connected in series to determine which contains the pin-to-pin shorted supply circuit. Repair the OEM harness. Refer to Procedure 019-071 in Section 19. | 4A |  |
>
> #### STEP 3D. Check for a pin-to-pin short circuit in the OEM harness.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness from the ECM connector. Disconnect the OEM pressure sensor from the OEM harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for a pin-to-pin short. Measure the resistance between the OEM pressure SUPPLY pin in the OEM harness ECM connector and all other pins in the ECM OEM connector. Refer to the circuit diagram or the wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Greater than 100K ohms? **YES** | 3E |
> | Greater than 100K ohms? **NORepair:** A pin-to-pin short circuit on the SUPPLY wire has been detected in the OEM harness. Troubleshoot each harness connected in series to determine which contains the shorted signal circuit to ground. Repair the OEM harness. Refer to Procedure 019-071 in Section 19. | 4A |  |
>
> #### STEP 3E. Check for an inactive fault code.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for the appropriate circuit response after 30 seconds. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 1542 inactive? **YESRepair:** None. The removal and installation of the connector corrected the fault. | 4A |
> | Fault Code 1542 inactive? **NORepair:** Replace the ECM. Refer to Procedure 019-031 in Section 19. | 4A |  |
>
> ### STEP 4. Clear the fault codes.
>
> #### STEP 4A. Disable the fault code
>
> | **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Disable the fault code. Use INSITE™ electronic service tool to verify that the fault code is inactive. | Fault Code 1542 inactive? **YES** | 4B |
> | Fault Code 1542 inactive? **NORepair:** Return to the troubleshooting steps or contact a Cummins® Authorized Repair Location if all steps have been completed and checked again. | 1A |  |
>
> #### STEP 4B. Clear the inactive fault codes.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Clear the inactive fault codes. Use INSITE™ electronic service tool to clear the inactive fault codes. | All fault codes cleared? **YES** | Repair complete. |
> | All fault codes cleared? **NORepair:** Go to the appropriate troubleshooting steps. | 1A |  |
