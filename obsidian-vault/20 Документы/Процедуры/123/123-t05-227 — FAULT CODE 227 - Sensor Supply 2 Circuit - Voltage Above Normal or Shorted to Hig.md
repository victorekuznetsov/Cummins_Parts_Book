---
aliases:
  - "Код 227 — цепь питания датчиков 2 — напряжение выше нормы"
type: "Процедура"
doc: "123-t05-227"
title_en: "FAULT CODE 227 - Sensor Supply 2 Circuit - Voltage Above Normal or Shorted to High Source"
title_ru: "Код 227 — цепь питания датчиков 2 — напряжение выше нормы"
modified: "2026-02-06"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4022094"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/123/123-t05-227.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/123-t05-227.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/123"
  - "перевод/машинный"
---

# FAULT CODE 227 - Sensor Supply 2 Circuit - Voltage Above Normal or Shorted to High Source
**Код 227 — цепь питания датчиков 2 — напряжение выше нормы**

> [!abstract] Процедура · `123-t05-227`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4022094 — QSK19 CM2150 and CM2670 Electronic Control System Troubleshooting and Repair Manual|4022094]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2026-02-06
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/123/123-t05-227.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/123-t05-227.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


Версия для печати

## Предупреждения и меры предосторожности

> [!warning] ОСТОРОЖНО
> Чтобы уменьшить вероятность повреждения новой ECM, все другие активные коды неисправностей должны быть исследованы до замены ECM.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте коды неисправностей. |  |
|  | **STEP 1A.** Проверить наличие активного кода неисправности. | Код ошибки 227 активен? |
| ШАГ 2. | Проверьте ECM, OEM-проводку и электропроводку двигателя. |  |
|  | **STEP 2A.** Проверить контакты разъема ECM, OEM-проводов и проводов двигателя. | Грязные или поврежденные контакты? |
|  | **STEP 2B.** Проверьте короткое замыкание в электропроводке OEM или электропроводке двигателя. | Больше 100 тысяч ом? |
|  | **STEP 2C.** Проверьте короткое замыкание в непереключенной электропроводке питания батареи. | Больше 100 тысяч ом? |
| ШАГ 3. | Сбросьте коды неисправностей. |  |
|  | **STEP 3A.** Отключить код ошибки. | Код 227 неактивен? |
|  | **STEP 3B.** Очистить коды неактивных ошибок. | Все коды неисправностей очищены? |

### ШАГ 1. Проверьте коды неисправностей.

#### ШАГ 1A. Проверьте активный код ошибки.

| **Условия:** Включить переключатель зажигания. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте активный код ошибки. Используйте инструмент электронного сервиса INSITETM для считывания кодов неисправностей. | Код ошибки 227 активен? *Да | 2А |
| Код ошибки 227 активен? **НЕТ** | Используйте следующую процедуру для неактивного или прерывистого кода неисправности.[[99-019-362 — Inactive or Intermittent Fault Code\|См. процедуру 019-362 в разделе 19.]] |  |

### ШАГ 2. Проверьте ECM, OEM-проводку и электропроводку двигателя.

#### ШАГ 2A. Проверьте контакты разъема ECM, OEM-проводов и соединительного устройства.

| **Условия:** Выключите замок зажигания. Отсоедините педаль акселератора или разъем датчика положения рычага от разъема проводов OEM, если он оборудован. Отключите разъем с уклоном скорости от разъема OEM-проводов, если он оборудован. Отсоедините разъем потенциометра с разъемом OEM-проводов, если он оборудован. Отсоедините разъем жгута проводов двигателя от разъема порта ECM 60-pin OEM. Отсоедините разъем жгута проводов двигателя от 31-контактного OEM-разъема. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Осмотрите контактные линзы для проводов двигателя и разъёма датчика на предмет: Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема разъема разъема или на разъеме контакты Разъема оболочки разбитого Провода изоляционного повреждения Поврежденный разъем блокировки вкладки. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Грязные или поврежденные контакты? *** Ремонт:** Очистить разъем и штифты. По возможности отремонтируйте поврежденную проводку, разъем или штифты. См. схему или схему проводов для всех соединений жгутов проводов двигателя. См. процедуру 019-071 в разделе 19. См. процедуру 019-204 в разделе 19. См. процедуру 019-043 в разделе 19. См. руководство по обслуживанию OEM для инструкций по ремонту педали акселератора или датчика положения рычага. Заменить ECM.[[123-019-031 — Engine Control Module\|См. процедуру 019-031 в разделе 19.]] | 3А |
| Грязные или поврежденные контакты? **НЕТ** | 2В |  |

#### ШАГ 2B. Проверьте короткое замыкание контакта с контактом в OEM-проводнике или упряжке для проводов двигателя.

| **Условия:** Выключите замок зажигания. Отсоедините разъем жгута проводов двигателя от разъема порта ECM 60-pin OEM. Отсоедините педаль акселератора или разъем датчика положения рычага от разъема проводов OEM, если он оборудован. Отключите разъем с уклоном скорости от разъема OEM-проводов, если он оборудован. Отсоедините разъем потенциометра с разъемом OEM-проводов, если он оборудован. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте короткое контактное соединение. Измерьте сопротивление между 5-вольтным штифтом SUPPLY (сенсорная подачей 2) в разъеме электропроводки двигателя ECM и всеми другими штифтами в разъеме. См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Больше 100 тысяч ом? *Да | 2C |
| Больше 100 тысяч ом? **NORepair:** В проводе 5-вольтового питания (сенсорного питания 2) обнаружено короткое замыкание. Устранение неполадок все проводов, соединенные последовательно, чтобы определить, который содержит контакт-контакт коротко. См. схему или схему проводов для всех соединений проводов. Замените поврежденный участок проводов жгутом. См. процедуру 019-071 в разделе 19. См. процедуру 019-199 в разделе 19. См. процедуру 019-043 в разделе 19. | 3А |  |

#### ШАГ 2C. Проверьте короткое замыкание в непереключенной электропроводке питания батареи.

| **Условия:** Выключите замок зажигания. Отсоедините разъем жгута проводов двигателя от разъема порта ECM 60-pin OEM. Отсоедините педаль акселератора или разъем датчика положения рычага от разъема проводов OEM, если он оборудован. Отключите разъем с уклоном скорости от разъема OEM-проводов, если он оборудован. Отсоедините разъем потенциометра с разъемом OEM-проводов, если он оборудован. Отсоедините разъем силовой проводов двигателя от разъема ECM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте короткое замыкание на аккумулятор. Измерьте сопротивление между 5-вольтным штифтом SUPPLY (сенсорная подачей 2) в разъеме ECM электропроводки двигателя и штифтом SUPPLY (+) батареи ECM или разъемом ECM электропроводки электропроводки. См. схему или схему проводов для идентификации контакта с разъемом. Используйте следующую процедуру для общих методов измерения сопротивления.[[99-019-360 — Resistance Measurement Using a Multimeter\|См. процедуру 019-360 в разделе 19.]] | Больше 100 тысяч ом? * Заменить ЭКМ.[[123-019-031 — Engine Control Module\|См. процедуру 019-031 в разделе 19.]] | 3А |
| Больше 100 тысяч ом? **NORepair:** В электропроводке OEM или электропроводке двигателя обнаружено короткое замыкание на аккумуляторе. Ремонт проводной упряжки OEM. См. процедуру 019-071 в разделе 19. Ремонт ремня электропроводки двигателя. См. процедуру 019-043 в разделе 19. | 3А |  |

### ШАГ 3. Сбросьте коды неисправностей.

#### ШАГ 3A. Отключите код неисправности.

| **Условия:** Соединить все компоненты. Включите зажигание. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Отключите код неисправности. Используйте инструмент электронного сервиса INSITETM для проверки неактивности кода ошибки. | Код 227 неактивен? *Да | 3B |
| Код 227 неактивен? **NORepair:** Возврат к шагам устранения неполадок или свяжитесь с авторизованным местом ремонта Cummins®, если все шаги были завершены и проверены снова. | 1А |  |

#### ШАГ 3B. Сбросьте неактивные коды неисправностей.

| **Условия:** Соединить все компоненты. Включите зажигание. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Сбросьте неактивные коды неисправностей. Используйте инструмент электронного сервиса INSITETM для очистки кодов неактивных ошибок. | Все коды неисправностей очищены? *Да | Ремонт завершён. |
| Все коды неисправностей очищены? **NORepair:** Устранение неполадок с оставшимися активными кодами неисправностей. | Перейдите к соответствующим шагам устранения неполадок. |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ## Warnings and Cautions
>
> **CAUTION · Осторожно**
> To reduce the possibility of damaging a new ECM, all other active fault codes must be investigated prior to replacing the ECM.
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the fault codes. |  |
> |  | **STEP 1A.** Check for an active fault code. | Fault Code 227 active? |
> | STEP 2. | Check the ECM, OEM harness, and engine harness. |  |
> |  | **STEP 2A..** Inspect the ECM, OEM harness, and engine harness connector pins. | Dirty or damaged pins? |
> |  | **STEP 2B.** Check for a pin-to-pin short circuit in the OEM harness or engine harness. | Greater than 100k ohms? |
> |  | **STEP 2C.** Check for a short circuit in the unswitched battery supply power harness. | Greater than 100k ohms? |
> | STEP 3. | Clear the fault codes. |  |
> |  | **STEP 3A.** Disable the fault code. | Fault Code 227 inactive? |
> |  | **STEP 3B.** Clear the inactive fault codes. | All fault codes cleared? |
>
> ### STEP 1. Check the fault codes.
>
> #### STEP 1A. Check for an active fault code.
>
> | **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for an active fault code. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 227 active? **YES** | 2A |
> | Fault Code 227 active? **NO** | Use the following procedure for an inactive or intermittent fault code. [[99-019-362 — Inactive or Intermittent Fault Code\|Refer to Procedure 019-362 in Section 19.]] |  |
>
> ### STEP 2. Check the ECM, OEM harness, and engine harness.
>
> #### STEP 2A. Inspect the ECM, OEM harness, and engine harness connector pins.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the accelerator pedal or lever position sensor connector from the OEM harness connector, if equipped. Disconnect the speed bias connector from the OEM harness connector, if equipped. Disconnect the gain adjust potentiometer connector from the OEM harness connector, if equipped. Disconnect the engine harness connector from the ECM 60-pin OEM port connector. Disconnect the engine harness connector from the 31-pin OEM connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the engine harness and sensor connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** Clean the connector and pins. Repair the damaged harness, connector, or pins if possible. Refer to the circuit diagram or wiring diagram for all engine harness interconnections. Refer to Procedure 019-071 in Section 19. Refer to Procedure 019-204 in Section 19. Refer to Procedure 019-043 in Section 19. Refer to the OEM service manual for accelerator pedal or lever position sensor repair instructions. Replace the ECM. [[123-019-031 — Engine Control Module\|Refer to Procedure 019-031 in Section 19.]] | 3A |
> | Dirty or damaged pins? **NO** | 2B |  |
>
> #### STEP 2B. Check for a pin-to-pin short circuit in the OEM harness or engine harness.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine harness connector from the ECM 60-pin OEM port connector. Disconnect the accelerator pedal or lever position sensor connector from the OEM harness connector, if equipped. Disconnect the speed bias connector from the OEM harness connector, if equipped. Disconnect the gain adjust potentiometer connector from the OEM harness connector, if equipped. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for a pin-to-pin short. Measure the resistance between the 5 volt SUPPLY (sensor supply 2) pin in the engine harness ECM connector and all other pins in the connector. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Greater than 100k ohms? **YES** | 2C |
> | Greater than 100k ohms? **NORepair:** A short circuit has been detected in the 5 volt SUPPLY (sensor supply 2) wire. Troubleshoot all harnesses connected in series to determine which contains the pin-to-pin short. Refer to the circuit diagram or wiring diagram for all harness interconnections. Replace the damaged section of harness. Refer to Procedure 019-071 in Section 19. Refer to Procedure 019-199 in Section 19. Refer to Procedure 019-043 in Section 19. | 3A |  |
>
> #### STEP 2C. Check for a short circuit in the unswitched battery supply power harness.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine harness connector from the ECM 60-pin OEM port connector. Disconnect the accelerator pedal or lever position sensor connector from the OEM harness connector, if equipped. Disconnect the speed bias connector from the OEM harness connector, if equipped. Disconnect the gain adjust potentiometer connector from the OEM harness connector, if equipped. Disconnect the engine power harness connector from the ECM connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for a short circuit to battery. Measure the resistance between the 5 volt SUPPLY (sensor supply 2) pin in the engine harness ECM connector and the ECM battery SUPPLY (+) pin or the power harness ECM connector. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Greater than 100k ohms? **YESRepair:** Replace the ECM. [[123-019-031 — Engine Control Module\|Refer to Procedure 019-031 in Section 19.]] | 3A |
> | Greater than 100k ohms? **NORepair:** A short circuit to the battery has been detected in the OEM harness or engine harness. Repair the OEM harness. Refer to Procedure 019-071 in Section 19. Repair the engine harness. Refer to Procedure 019-043 in Section 19. | 3A |  |
>
> ### STEP 3. Clear the fault codes.
>
> #### STEP 3A. Disable the fault code.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Disable the fault code. Use INSITE™ electronic service tool to verify the fault code is inactive. | Fault Code 227 inactive? **YES** | 3B |
> | Fault Code 227 inactive? **NORepair:** Return to the troubleshooting steps or contact a Cummins® Authorized Repair Location if all steps have been completed and checked again. | 1A |  |
>
> #### STEP 3B. Clear the inactive fault codes.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Clear the inactive fault codes. Use INSITE™ electronic service tool to clear the inactive fault codes. | All fault codes cleared? **YES** | Repair complete. |
> | All fault codes cleared? **NORepair:** Troubleshoot any remaining active fault codes. | Go to the appropriate troubleshooting steps. |  |
