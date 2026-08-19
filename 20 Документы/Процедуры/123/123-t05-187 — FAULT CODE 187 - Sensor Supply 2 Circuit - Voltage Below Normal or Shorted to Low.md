---
aliases:
  - "Код 187 — цепь питания датчиков 2 — напряжение ниже нормы"
type: "Процедура"
doc: "123-t05-187"
title_en: "FAULT CODE 187 - Sensor Supply 2 Circuit - Voltage Below Normal or Shorted to Low Source"
title_ru: "Код 187 — цепь питания датчиков 2 — напряжение ниже нормы"
modified: "2026-02-06"
engines:
  - "41349633"
families:
  - "QSK19"
manuals:
  - "4022094"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/123/123-t05-187.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/123-t05-187.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/123"
  - "перевод/машинный"
---

# FAULT CODE 187 - Sensor Supply 2 Circuit - Voltage Below Normal or Shorted to Low Source
**Код 187 — цепь питания датчиков 2 — напряжение ниже нормы**

> [!abstract] Процедура · `123-t05-187`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4022094 — QSK19 CM2150 and CM2670 Electronic Control System Troubleshooting and Repair Manual|4022094]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2026-02-06
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/123/123-t05-187.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/123-t05-187.pdf)

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
> Чтобы не повредить контакты и жгут, при измерениях пользуйтесь следующими измерительными проводами: Номер детали 3822758 — пробный щуп типа штепсельной заглушки DeutschTM/AMPTM/Metri-PackTM, номер детали 3822917 — пробный щуп типа розетки DeutschTM/AMPTM/Metri-PackTM, номер детали 3164596 — штыревой пробный щуп FramatomeTM, а номер детали 3164597 — гнездовой пробный щуп FramatomeTM.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте коды неисправностей. |  |
|  | **STEP 1A.** Проверить наличие активного кода неисправности. | Код ошибки 187 активен? |
| ШАГ 2. | Проверьте датчики и схемы, подключенные к датчику питания 2 и возвращайтесь. |  |
|  | **STEP 2A.** Проверить датчики и схемы, подключенные к датчику питания 2 и возврата. | Грязные или поврежденные контакты? |
|  | **STEP 2B.** Проверьте реакцию цепи. | Код ошибки 187 активен? |
| ШАГ 3. | Проверьте ECM. |  |
|  | **STEP 3A.** Проверить контакты разъема ECM и проводов двигателя. | Грязные или поврежденные контакты? |
|  | **STEP 3B.** Проверьте короткое замыкание. | Больше 100 тысяч ом? |
|  | **ШАГ 3В-1.** Проверьте короткое замыкание штифта на землю. | Больше 100 тысяч ом? |
| ШАГ 4. | Сбросьте коды неисправностей. |  |
|  | **STEP 4A.** Отключить код ошибки. | Код ошибки 187 неактивен? |
|  | **STEP 4B.** Очистить коды неактивных ошибок. | Все коды неисправностей очищены? |

### ШАГ 1. Проверьте коды неисправностей.

#### ШАГ 1A. Проверьте активный код ошибки.

| **Условия:** Включить переключатель зажигания. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте активный код ошибки. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Код ошибки 187 активен? *Да** | 2А |
| Код ошибки 187 активен? ** НЕТ** | Используйте следующую процедуру для неактивного или прерывистого кода неисправности.[[99-019-362 — Inactive or Intermittent Fault Code\|См. процедуру 019-362 в разделе 19.]] |  |

### ШАГ 2. Проверьте датчики и схемы, подключенные к датчику питания 2 и возвращайтесь.

#### ШАГ 2A. Осмотрите датчики и схемы, подключенные к датчику питания 2 и возвращайте.

| **Условия:** Выключите замок зажигания. Отсоедините педаль акселератора или разъем датчика положения рычага от разъема проводов OEM, если он оборудован. Отключите разъем с уклоном скорости от разъема OEM-проводов, если он оборудован. Отсоедините разъем потенциометра с разъемом OEM-проводов, если он оборудован. Отсоедините разъем жгута проводов двигателя от 31-контактного OEM-разъема. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Осмотрите разъёмы жгута проводов и контакты разъёма датчика для следующего: Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема разъема разъема или на разъеме контакты Разъема оболочки разбитого Провода изоляционного повреждения Поврежденный разъем блокировки вкладки. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Грязные или поврежденные контакты? **Ремонт: ** В датчике или разъёме жгута проводов было обнаружено поврежденное соединение. Очистите разъем и булавки. Замените поврежденный участок проводов ремня или поврежденный датчик. См. схему или схему проводов для всех соединений проводов. См. процедуру 019-043 в разделе 19. См. процедуру 019-085 в разделе 19. См. процедуру 019-071 в разделе 19. | 4А |
| Грязные или поврежденные контакты? ** НЕТ** | 2В |  |

#### ШАГ 2B. Проверьте отклик цепи.

| **Условия:** Выключите замок зажигания. Отсоедините педаль акселератора или разъем датчика положения рычага от разъема проводов OEM, если он оборудован. Отключите разъем с уклоном скорости от разъема OEM-проводов, если он оборудован. Отсоедините разъем потенциометра с разъемом OEM-проводов, если он оборудован. Включите зажигание. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте соответствующий ответ на ECM через 30 секунд. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Код ошибки 187 активен? *Да** | 3А |
| Код ошибки 187 активен? **NORepair:** Заменить педаль акселератора или датчик положения рычага, если он оборудован. См. процедуру 019-085 в разделе 19. Замените переключатель смещения скорости, если он оборудован. См. сервисное руководство изготовителя машины. Заменить на коэффициент усиления регулировки потенциометром, если он оборудован. См. сервисное руководство изготовителя машины. | 4А |  |

### ШАГ 3. Проверьте ECM.

#### ШАГ 3A. Проверьте контакты разъема ECM и проводов двигателя.

| **Условия:** Выключите замок зажигания. Отсоедините разъем жгута проводов двигателя от разъема порта ECM 60-pin OEM. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Осмотрите контакты электропроводки двигателя и разъема ECM на предмет: Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема разъема разъема или на разъеме контакты Разъема оболочки разбитого Провода изоляционного повреждения Поврежденный разъем блокировки вкладки. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Грязные или поврежденные контакты? **Ремонт: ** В разъеме ECM или в ремне электропроводки двигателя обнаружено поврежденное соединение. Очистите разъем и булавки. Замените поврежденный участок проводов жгутом. См. схему или схему проводов для всех соединений жгутов проводов двигателя. См. процедуру 019-043 в разделе 19. См. процедуру 019-199 в разделе 19. Заменить ECM.[[123-019-031 — Engine Control Module\|См. процедуру 019-031 в разделе 19.]] | 4А |
| Грязные или поврежденные контакты? ** НЕТ** | 3B |  |

#### ШАГ 3B. Проверьте короткое замыкание контакт-контакт.

| **Условия:** Выключите замок зажигания. Отсоедините разъем жгута проводов двигателя от разъема порта ECM 60-pin OEM. Отсоедините педаль акселератора или разъем датчика положения рычага от разъема проводов OEM, если он оборудован. Отключите разъем с уклоном скорости от разъема OEM-проводов, если он оборудован. Отсоедините разъем потенциометра с разъемом OEM-проводов, если он оборудован. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте короткое контактное соединение. Измерьте сопротивление между 5-вольтным штифтом SUPPLY (сенсорная подачу 2) в разъеме электропроводки двигателя ECM и всеми другими штифтами в разъеме ECM. См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Больше 100 тысяч ом? *Да** | 3В-1-1 |
| Больше 100 тысяч ом? **NORepair: ** В проводе 5-вольтового питания (сенсорного питания 2) обнаружено короткое замыкание. Устранение неполадок проводов жгутов, соединенных последовательно, чтобы определить, который содержит контакт-контакт короткий. См. схему или схему проводов для всех соединений проводов. Заменить поврежденный участок проводов жгутом. См. процедуру 019-071 в разделе 19. См. процедуру 019-199 в разделе 19. См. процедуру 019-043 в разделе 19. | 4А |  |

#### ШАГ 3B-1. Проверьте короткое замыкание штифта на землю.

| **Условия:** Выключите замок зажигания. Отсоедините разъем жгута проводов двигателя от разъема порта ECM 60-pin OEM. Отсоедините педаль акселератора или разъем датчика положения рычага от разъема проводов OEM, если он оборудован. Отключите разъем с уклоном скорости от разъема OEM-проводов, если он оборудован. Отсоедините разъем потенциометра с разъемом OEM-проводов, если он оборудован. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Проверьте короткое замыкание на землю. Измерьте сопротивление между 5-вольтным штифтом SUPPLY (сенсорная подачей 2) в разъёме электропроводки двигателя ECM и земле. См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Больше 100 тысяч ом? *** Заменить ЭКМ.[[123-019-031 — Engine Control Module\|См. процедуру 019-031 в разделе 19.]] | 4А |
| Больше 100 тысяч ом? **NORepair: ** В проводе 5-вольтового питания (сенсорного питания 2) обнаружено короткое замыкание. Устранение неполадок проводов жгутов, соединенных последовательно, чтобы определить, который содержит короткое замыкание на землю. См. схему или схему проводов для всех соединений проводов. Замените поврежденный участок проводов жгутами. См. процедуру 019-071 в разделе 19. См. процедуру 019-199 в разделе 19. См. процедуру 019-043 в разделе 19. | 4А |  |

### ШАГ 4. Сбросьте коды неисправностей.

#### ШАГ 4A. Отключите код неисправности.

| **Условия: ** Соединить все компоненты. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Отключите код неисправности. Используйте инструмент электронного сервиса INSITETM для проверки неактивности кода ошибки. | Код ошибки 187 неактивен? *Да** | 4B |
| Код ошибки 187 неактивен? **NORepair:** Возврат к шагам устранения неполадок или свяжитесь с авторизованным местом ремонта Cummins®, если все шаги были завершены и проверены снова. | 1А |  |

#### ШАГ 4B. Сбросьте неактивные коды неисправностей.

| **Условия: ** Соединить все компоненты. Включите зажигание. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Сбросьте неактивные коды неисправностей. Используйте инструмент электронного сервиса INSITETM для очистки кодов неактивных ошибок. | Все коды неисправностей очищены? *Да** | Ремонт завершён |
| Все коды неисправностей очищены? ** НЕТ** | Соответствующие шаги по устранению неполадок |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ## Warnings and Cautions
>
> **CAUTION · Осторожно**
> To reduce the possibility of damaging a new engine control module (ECM), all other active fault codes must be investigated prior to replacing the ECM.
>
> **CAUTION · Осторожно**
> To reduce the possibility of pin and harness damage, use the following test leads when taking a measurement: Part Number 3822758 - male Deutsch™/AMP™/Metri-Pack™ test lead, Part Number 3822917 - female Deutsch™/AMP™/Metri-Pack™ test lead, Part Number 3164596 - male Framatome™ test lead, and Part Number 3164597 - female Framatome™ test lead.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the fault codes. |  |
> |  | **STEP 1A.** Check for an active fault code. | Fault Code 187 active? |
> | STEP 2. | Check the sensors and circuits connected to the sensor supply 2 and return. |  |
> |  | **STEP 2A.** Inspect the sensors and circuits connected to the sensor supply 2 and return. | Dirty or damaged pins? |
> |  | **STEP 2B.** Check the circuit response. | Fault Code 187 active? |
> | STEP 3. | Check the ECM. |  |
> |  | **STEP 3A.** Inspect the ECM and engine harness connector pins. | Dirty or damaged pins? |
> |  | **STEP 3B.** Check for a pin-to-pin short circuit. | Greater than 100k ohms? |
> |  | **STEP 3B-1.** Check for a pin short circuit to ground. | Greater than 100k ohms? |
> | STEP 4. | Clear the fault codes. |  |
> |  | **STEP 4A.** Disable the fault code. | Fault Code 187 inactive? |
> |  | **STEP 4B.** Clear the inactive fault codes. | All fault codes cleared? |
>
> ### STEP 1. Check the fault codes.
>
> #### STEP 1A. Check for an active fault code.
>
> | **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for an active fault code. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 187 active? **YES** | 2A |
> | Fault Code 187 active? **NO** | Use the following procedure for an inactive or intermittent fault code. [[99-019-362 — Inactive or Intermittent Fault Code\|Refer to Procedure 019-362 in Section 19.]] |  |
>
> ### STEP 2. Check the sensors and circuits connected to the sensor supply 2 and return.
>
> #### STEP 2A. Inspect the sensors and circuits connected to the sensor supply 2 and return.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the accelerator pedal or lever position sensor connector from the OEM harness connector, if equipped. Disconnect the speed bias connector from the OEM harness connector, if equipped. Disconnect the gain adjust potentiometer connector from the OEM harness connector, if equipped. Disconnect the engine harness connector from the 31-pin OEM connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the harness connectors and sensor connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection had been detected in the sensor or harness connector. Clean the connector and pins. Replace the damaged section of the harness or damaged sensor. Refer to circuit diagram or wiring diagram for all harness interconnections. Refer to Procedure 019-043 in Section 19. Refer to Procedure 019-085 in Section 19. Refer to Procedure 019-071 in Section 19. | 4A |
> | Dirty or damaged pins? **NO** | 2B |  |
>
> #### STEP 2B. Check the circuit response.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the accelerator pedal or lever position sensor connector from the OEM harness connector, if equipped. Disconnect the speed bias connector from the OEM harness connector, if equipped. Disconnect the gain adjust potentiometer connector from the OEM harness connector, if equipped. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for the appropriate ECM response after 30 seconds. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 187 active? **YES** | 3A |
> | Fault Code 187 active? **NORepair:** Replace the accelerator pedal or lever position sensor, if equipped. Refer to Procedure 019-085 in Section 19. Replace the speed bias switch, if equipped. Refer to the OEM Service Manual. Replace the gain adjust potentiometer, if equipped. Refer to the OEM Service Manual. | 4A |  |
>
> ### STEP 3. Check the ECM.
>
> #### STEP 3A. Inspect the ECM and engine harness connector pins.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine harness connector from the ECM 60-pin OEM port connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the engine harness and ECM connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the ECM connector or the engine harness. Clean the connector and pins. Replace the damaged section of harness. Refer to the circuit diagram or wiring diagram for all engine harness interconnections. Refer to Procedure 019-043 in Section 19. Refer to Procedure 019-199 in Section 19. Replace the ECM. [[123-019-031 — Engine Control Module\|Refer to Procedure 019-031 in Section 19.]] | 4A |
> | Dirty or damaged pins? **NO** | 3B |  |
>
> #### STEP 3B. Check for a pin-to-pin short circuit.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine harness connector from the ECM 60-pin OEM port connector. Disconnect the accelerator pedal or lever position sensor connector from the OEM harness connector, if equipped. Disconnect the speed bias connector from the OEM harness connector, if equipped. Disconnect the gain adjust potentiometer connector from the OEM harness connector, if equipped. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for a pin-to-pin short. Measure the resistance between the 5 volt SUPPLY (sensor supply 2) pin in the engine harness ECM connector and all other pins in the ECM connector. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Greater than 100k ohms? **YES** | 3B-1 |
> | Greater than 100k ohms? **NORepair:** A short circuit has been detected in the 5 volt SUPPLY (sensor supply 2) wire. Troubleshoot harnesses connected in series to determine which contains the pin-to-pin short. Refer to the circuit diagram or wiring diagram for all harness interconnections. Replace the damaged section of the harness. Refer to Procedure 019-071 in Section 19. Refer to Procedure 019-199 in Section 19. Refer to Procedure 019-043 in Section 19. | 4A |  |
>
> #### STEP 3B-1. Check for a pin short circuit to ground.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine harness connector from the ECM 60-pin OEM port connector. Disconnect the accelerator pedal or lever position sensor connector from the OEM harness connector, if equipped. Disconnect the speed bias connector from the OEM harness connector, if equipped. Disconnect the gain adjust potentiometer connector from the OEM harness connector, if equipped. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for a short circuit to ground. Measure the resistance between the 5 volt SUPPLY (sensor supply 2) pin in the engine harness ECM connector and ground. Refer to the circuit diagram or the wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Greater than 100k ohms? **YESRepair:** Replace the ECM. [[123-019-031 — Engine Control Module\|Refer to Procedure 019-031 in Section 19.]] | 4A |
> | Greater than 100k ohms? **NORepair:** A short circuit has been detected in the 5 volt SUPPLY (sensor supply 2) wire. Troubleshoot harnesses connected in series to determine which contains the short circuit to ground. Refer to the circuit diagram or wiring diagram for all harness interconnections. Replace the damaged section of harnesses. Refer to Procedure 019-071 in Section 19. Refer to Procedure 019-199 in Section 19. Refer to Procedure 019-043 in Section 19. | 4A |  |
>
> ### STEP 4. Clear the fault codes.
>
> #### STEP 4A. Disable the fault code.
>
> | **Conditions:** Connect all components. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Disable the fault code. Use INSITE™ electronic service tool to verify the fault code is inactive. | Fault Code 187 inactive? **YES** | 4B |
> | Fault Code 187 inactive? **NORepair:** Return to the troubleshooting steps or contact a Cummins® Authorized Repair Location if all steps have been completed and checked again. | 1A |  |
>
> #### STEP 4B. Clear the inactive fault codes.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Clear the inactive fault codes. Use INSITE™ electronic service tool to clear the inactive fault codes. | All fault codes cleared? **YES** | Repair complete |
> | All fault codes cleared? **NO** | Appropriate troubleshooting steps |  |
