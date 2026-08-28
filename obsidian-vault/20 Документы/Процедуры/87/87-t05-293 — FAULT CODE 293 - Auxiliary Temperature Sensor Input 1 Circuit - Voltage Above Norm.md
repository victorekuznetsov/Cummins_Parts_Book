---
aliases:
  - "Код 293 — цепь вспомогательного датчика температуры 1 — напряжение выше нормы"
type: "Процедура"
doc: "87-t05-293"
title_en: "FAULT CODE 293 - Auxiliary Temperature Sensor Input 1 Circuit - Voltage Above Normal or Shorted to High Source"
title_ru: "Код 293 — цепь вспомогательного датчика температуры 1 — напряжение выше нормы"
modified: "2020-01-28"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666214"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-t05-293.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-t05-293.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
  - "перевод/машинный"
---

# FAULT CODE 293 - Auxiliary Temperature Sensor Input 1 Circuit - Voltage Above Normal or Shorted to High Source
**Код 293 — цепь вспомогательного датчика температуры 1 — напряжение выше нормы**

> [!abstract] Процедура · `87-t05-293`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2020-01-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-t05-293.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-t05-293.pdf)

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

> [!warning] ОСТОРОЖНО
> Чтобы не повредить контакты и жгут, при измерениях пользуйтесь следующими измерительными проводами: Номер детали 3823993 - пробный щуп типа пробки DeutschTM, номер детали 3823994 - пробный щуп типа гнезда DeutschTM, номер детали 3822758 - пробный щуп типа пробки DeutschTM/AMPTM/Metri-PackTM, номер детали 3822917 - пробный щуп типа разъема DeutschTM/AMPTM/Metri-PackTM.

> [!warning] ОСТОРОЖНО
>

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте коды неисправностей. |  |
|  | **STEP 1A.** Проверить наличие активного кода неисправности. | Коды 133 неисправностей активны или неактивны, если количество не превышает одного за последние 25 часов работы двигателя? |
| ШАГ 2. | Проверьте оригинальную проводку производителя оборудования (OEM). |  |
|  | **STEP 2A.** Проверить OEM-проводку и OEM-интерфейс проводов жгута разъема и штифтов. | Грязные или поврежденные контакты? |
|  | **ШАГ 2В.** Проверить наличие открытой цепи. | Менее 10 Ом? |
|  | **STEP 2C.** Проверьте короткое замыкание от пин-кодов до пин-кодов. | Больше 100 тысяч ом? |
|  | **STEP 2D.** Проверьте короткое замыкание на блокировке двигателя. | Больше 100 тысяч ом? |
| ШАГ 3. | Проверьте напряжение модуля управления двигателем (ECM). |  |
|  | **ШАГ 3А.** Проверьте напряжение от ECM. | Напряжение между 4,75 и 5,25 вольт постоянного тока (VDC)? |
| ШАГ 4. | Вспомогательный датчик температуры OEM работает неправильно. |  |
|  | **STEP 4A.** Обнаружен неисправный вспомогательный датчик температуры OEM. | Все остальные процедуры устранения неполадок были завершены, а код неисправности по-прежнему активен или неактивен с более чем одним подсчетом в течение последних 25 часов работы двигателя? |
| ШАГ 5. | Проверьте калибровку ECM и четкие коды неисправностей. |  |
|  | **STEP 5A.** Проверьте наличие обновлений калибровки ECM. | Если доступно обновление калибровки для этого кода неисправности, содержит ли ECM эту правку или выше? |
|  | **STEP 5B.** Отключить код ошибки. | Код неактивен? |
|  | **ШАГ** |  |

### ШАГ 1. Проверьте коды неисправностей.

#### ШАГ 1A. Проверьте активный код ошибки.

| **Условия:** Включить переключатель зажигания. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте неактивный код ошибки. Запускай двигатель. Запускайте его на холостом ходу в течение 1 минуты. Используйте инструмент электронного сервиса INSITETM для считывания кода ошибки. | Коды 133 активных или неактивных с более чем 1 количеством в течение последних 25 часов работы двигателя. *Да | Аппродировать код неисправности, устраняя симптомы дерева |
| Коды 133 активных или неактивных с более чем 1 количеством в течение последних 25 часов работы двигателя. **НЕТ** | 2А |  |

### ШАГ 2. Проверьте оригинальную проводку производителя оборудования (OEM).

#### ШАГ 2A. Осмотрите OEM-проводку и контакты разъема OEM-интерфейса с левым берегом.

| **Условия:** Выключите замок зажигания. Отсоедините разъём OEM-проводов от вспомогательного датчика температуры OEM. Отключите разъем OEM-интерфейса с левым берегом от ECM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Осмотрите контактные линзы разъёма OEM-проводов и датчика температуры OEM для следующих целей: Разъем разъема разъединенный Корродированные штифты Сгибаемые или сломанные штифты Отталкивающиеся назад или расширенные штифты. Влага в или на разъеме Пропавшие или поврежденные разъёмы Уплотняет Грязь или мусор в или на разъеме Контакты Скорлупа разорванной Проволоки Повреждение изоляции Разъем блокирует вкладку. Используйте следующую процедуру для общих методов проверки.[[99-019-361 — Component Connector and Pin Inspection\|См. процедуру 019-361 в разделе 19.]] | Грязные или поврежденные контакты? **Ремонт:** В датчике или разъёме жгута проводов обнаружено поврежденное соединение. Очистите разъем и булавки. По возможности отремонтируйте поврежденную проводку, разъём или штифты.[[99-019-071 — OEM Wiring Harness\|См. процедуру 019-071 в разделе 19.]] | 5а |
| Грязные или поврежденные контакты? **НЕТ** | 2В |  |

#### ШАГ 2B. Проверьте цепь на обрыв.

| **Условия:** Выключите замок зажигания. Отсоедините разъём OEM-проводов от вспомогательного датчика температуры OEM. Отключите разъем OEM-интерфейса с левым берегом от ECM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерить сопротивление от контакта питания вспомогательного датчика температуры OEM вспомогательного датчика температуры OEM разъёма проводов OEM к контакту питания вспомогательного датчика температуры OEM разъёма проводов ECM интерфейса OEM левого берега. Измерить сопротивление от OEM вспомогательного датчика температуры обратного контакта OEM вспомогательного датчика температуры OEM проводов разъёма жгута проводов к OEM вспомогательного датчика температуры обратного контакта левобережного интерфейса проводов ремня ECM разъема. | Менее 10 Ом? *Да | 2C |
| Менее 10 Ом? **NORepair:** Открытая схема в электропроводке OEM была обнаружена. Устранение неполадок в электропроводке OEM и всех межсоединений. | 5а |  |

#### ШАГ 2C. Проверьте короткое замыкание от пин-кодов до пин-кодов.

| **Условия:** Выключите замок зажигания. Отсоедините разъём OEM-проводов от вспомогательного датчика температуры OEM. Отключите разъем OEM-интерфейса с левым берегом от ECM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерить сопротивление от контакта питания вспомогательного датчика температуры OEM в разъеме вспомогательного датчика температуры OEM ко всем другим штифтам в разъеме ECM с левым берегом OEM интерфейса проводов. Измерить сопротивление от OEM вспомогательного датчика температуры обратного контакта в OEM вспомогательного датчика температуры разъёма со всеми другими штифтами в левобережном OEM интерфейса проводов жгута ECM разъема. | Более 100 тысяч ом? *Да | 2D |
| Более 100 тысяч ом? **NORepair:** В электропроводке OEM обнаружено короткое замыкание. Устранение неполадок в электропроводке OEM и всех межсоединений. | 5а |  |

#### ШАГ 2D. Проверьте короткое замыкание на блокировку двигателя.

| **Условия:** Выключите замок зажигания. Отсоедините разъём OEM-проводов от вспомогательного датчика температуры OEM. Отключите разъем OEM-интерфейса с левым берегом от ECM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерить сопротивление от контакта питания вспомогательного датчика OEM в разъёме вспомогательного датчика температуры OEM к заземлению блока двигателя. | Более 100 тысяч ом? *Да | 3А |
| Более 100 тысяч ом? **NORepair:** В электропроводке OEM обнаружено короткое замыкание. Устранение неполадок в электропроводке OEM и всех межсоединений. | 5а |  |

### ШАГ 3. Проверьте напряжение ECM.

#### ШАГ 3A. Проверьте напряжение от ECM.

| **Условия:** Выключите замок зажигания. Отключите разъем OEM-интерфейса с левым берегом от ECM. Включите замок зажигания. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерить напряжение между вспомогательным датчиком температуры OEM ECM, контактирующим с подачей питания на разъеме ECM, и обратным контактом вспомогательного датчика температуры OEM на разъеме ECM. | Напряжение между 4,75 и 5,25 ВДК? *Да | 4А |
| Напряжение между 4,75 и 5,25 ВДК? **NORepair:** Выявлена неисправная ЭКМ. См. процедуру 019-031 в разделе 19. | Ремонт завершён |  |

### ШАГ 4. Вспомогательный датчик температуры OEM работает неправильно.

#### ШАГ 4A. Был обнаружен неисправный вспомогательный датчик температуры OEM.

| **Условия:** Выключите замок зажигания. Отсоедините разъём OEM-проводов от вспомогательного датчика температуры OEM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Убедитесь, что все предыдущие проверки решения для этого кода неисправности были выполнены. | Все остальные процедуры устранения неполадок были завершены, а код неисправности по-прежнему активен или неактивен с более чем одним подсчетом в течение последних 25 часов работы двигателя? *** Ремонт:** Обнаружен неисправный вспомогательный датчик температуры OEM. Заменить вспомогательный датчик температуры OEM. См. сервисную документацию изготовителя оборудования. | 5а |
| Все остальные процедуры устранения неполадок были завершены, а код неисправности по-прежнему активен или неактивен с более чем одним подсчетом в течение последних 25 часов работы двигателя? **НЕТ** | 5а |  |

### ШАГ 5. Проверьте калибровку ECM и четкие коды неисправностей.

#### ШАГ 5A. Проверьте, доступно ли обновление калибровки ECM.

| **Условия:** Соединить все компоненты. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Сравните код ECM и номер пересмотра в ECM с калибровочными изменениями, перечисленными в истории калибровочных ревизий ECM, для применимых изменений, связанных с этим кодом неисправности. Используйте инструмент электронного сервиса INSITETM, чтобы найти в ECM код и номер версии. Код и номер исправления ECM находятся в разделе «Информация о калибровке» идентификатора системы и таблички данных в функциях и параметрах. | Если доступно обновление калибровки для этого кода неисправности, содержит ли ECM эту правку или выше? *Да | 5В |
| Если доступно обновление калибровки для этого кода неисправности, содержит ли ECM эту правку или выше? **NORepair:** При необходимости откалибровать ECM.[[87-019-032 — ECM Calibration Code\|См. процедуру 019-032]]В разделе 19. | 5В |  |

#### ШАГ 5B. Отключите код неисправности.

| **Условия:** Соединить все компоненты. Подключите инструмент электронного сервиса INSITETM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Отключите и очистите код ошибки. Управляйте двигателем в рамках «Условий для устранения кода неисправности», найденных в разделе Обзор этой процедуры устранения неполадок. | Код неактивен? *Да | Ремонт завершён |
| Код неактивен? **НЕТ** | Эскалация или призыв к помощи |  |


> [!quote]- Original (English) · английский оригинал
> Printable Version
>
> ## Warnings and Cautions
>
> **CAUTION · Осторожно**
> To reduce the possibility of damaging a new ECM, all other active fault codes must be investigated prior to replacing the ECM.
>
> **CAUTION · Осторожно**
> To reduce the possibility of pin and harness damage, use the following test leads when taking a measurement: Part Number 3823993 - male Deutsch™ test lead, Part Number 3823994 - female Deutsch™ test lead, Part Number 3822758 - male Deutsch™/AMP™/Metri-Pack™ test lead, Part Number 3822917 - female Deutsch™/AMP™/Metri-Pack™ test lead.
>
> **CAUTION · Осторожно**
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the fault codes. |  |
> |  | **STEP 1A.** Check for an active fault code. | Fault Codes 133 active or inactive with more than one count in the last 25 engine hours? |
> | STEP 2. | Check the original equipment manufacturer (OEM) wiring harness. |  |
> |  | **STEP 2A.** Inspect the OEM wiring harness and OEM interface wiring harness connector and pins. | Dirty or damaged pins? |
> |  | **STEP 2B.** Check for an open circuit. | Less than 10 ohms? |
> |  | **STEP 2C.** Check for a short circuit from pin to pin. | Greater than 100k ohms? |
> |  | **STEP 2D.** Check for a short circuit to engine block ground. | Greater than 100k ohms? |
> | STEP 3. | Check the engine control module (ECM) voltage. |  |
> |  | **STEP 3A.** Check the voltage from the ECM. | Voltage between 4.75 and 5.25 volts direct current (VDC)? |
> | STEP 4. | OEM auxiliary temperature sensor is malfunctioning. |  |
> |  | **STEP 4A.** A malfunctioning OEM auxiliary temperature sensor has been detected. | All other troubleshooting procedures have been completed, and the fault code is still active or inactive with more than one count within the last 25 engine hours? |
> | STEP 5. | Check the ECM calibration and clear fault codes. |  |
> |  | **STEP 5A.** Check if an ECM calibration update is available. | If a calibration update for this fault code is available, does the ECM contain that revision or higher? |
> |  | **STEP 5B.** Disable the fault code. | Fault code inactive? |
> |  | **STEP.** |  |
>
> ### STEP 1. Check the fault codes.
>
> #### STEP 1A. Check for an active fault code.
>
> | **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for an inactive fault code. Start the engine. Let it idle for 1 minute. Use INSITE™ electronic service tool to read the fault code. | Fault Codes 133 active or inactive with more than 1 count in the last 25 engine hours? **YES** | Appropiate fault code troubleshooting symptom tree |
> | Fault Codes 133 active or inactive with more than 1 count in the last 25 engine hours? **NO** | 2A |  |
>
> ### STEP 2. Check the original equipment manufacturer (OEM) wiring harness.
>
> #### STEP 2A. Inspect the OEM wiring harness and the left bank OEM interface wiring harness connector pins.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the OEM wiring harness connector from the OEM auxiliary temperature sensor. Disconnect the left bank OEM interface wiring harness connector from the ECM. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the OEM harness and OEM temperature sensor connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins. Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the sensor or harness connector. Clean the connector and pins. Repair the damaged harness, connector or pins, if possible. [[99-019-071 — OEM Wiring Harness\|Refer to Procedure 019-071 in Section 19.]] | 5A |
> | Dirty or damaged pins? **NO** | 2B |  |
>
> #### STEP 2B. Check for an open circuit.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the OEM wiring harness connector from the OEM auxiliary temperature sensor. Disconnect the left bank OEM interface wiring harness connector from the ECM. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from the OEM auxiliary temperature sensor SUPPLY pin of the OEM auxiliary temperature sensor OEM wiring harness connector to the OEM auxiliary temperature sensor SUPPLY pin of the left bank OEM interface wiring harness ECM connector. Measure the resistance from the OEM auxiliary temperature sensor RETURN pin of the OEM auxiliary temperature sensor OEM wiring harness connector to the OEM auxiliary temperature sensor RETURN pin of the left bank OEM interface wiring harness ECM connector. | Less than 10 ohms? **YES** | 2C |
> | Less than 10 ohms? **NORepair:** An open circuit in the OEM wiring harness has been detected. Troubleshoot the OEM wiring harness and all interconnects. | 5A |  |
>
> #### STEP 2C. Check for a short circuit from pin to pin.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the OEM wiring harness connector from the OEM auxiliary temperature sensor. Disconnect the left bank OEM interface wiring harness connector from the ECM. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from the OEM auxiliary temperature sensor SUPPLY pin in the OEM auxiliary temperature sensor connector to all other pins in the left bank OEM interface wiring harness ECM connector. Measure the resistance from the OEM auxiliary temperature sensor RETURN pin in the OEM auxiliary temperature sensor connector to all other pins in the left bank OEM interface wiring harness ECM connector. | More than 100k ohms? **YES** | 2D |
> | More than 100k ohms? **NORepair:** A short circuit in the OEM wiring harness has been detected. Troubleshoot the OEM wiring harness and all interconnects. | 5A |  |
>
> #### STEP 2D. Check for a short circuit to engine block ground.
>
> | **Conditions:** Turn the keyswitch OFF. Disconnect the OEM wiring harness connector from the OEM auxiliary temperature sensor. Disconnect the left bank OEM interface wiring harness connector from the ECM. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from the OEM auxiliary sensor SUPPLY pin in the OEM auxiliary temperature sensor connector to engine block ground. | More than 100k ohms? **YES** | 3A |
> | More than 100k ohms? **NORepair:** A short circuit in the OEM wiring harness has been detected. Troubleshoot the OEM wiring harness and all interconnects. | 5A |  |
>
> ### STEP 3. Check the ECM voltage.
>
> #### STEP 3A. Check the voltage from the ECM.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the left bank OEM interface wiring harness connector from the ECM. Turn the keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the Voltage between the OEM auxiliary temperature sensor ECM SUPPLY pin at the ECM connector and the OEM auxiliary temperature sensor ECM RETURN pin at the ECM connector. | Voltage between 4.75 and 5.25 VDC? **YES** | 4A |
> | Voltage between 4.75 and 5.25 VDC? **NORepair:** A malfunctioning ECM has been detected. Refer to Procedure 019-031 in Section 19. | Repair complete |  |
>
> ### STEP 4. OEM auxiliary temperature sensor is malfunctioning.
>
> #### STEP 4A. A malfunctioning OEM auxiliary temperature sensor has been detected.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the OEM wiring harness connector from the OEM auxiliary temperature sensor. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Verify that all preceding solution verifications, for this fault code, have been performed. | All other troubleshooting procedures have been completed, and the fault code is still active or inactive with more than one count within the last 25 engine hours? **YESRepair:** A malfunctioning OEM auxiliary temperature sensor has been detected. Replace the OEM auxiliary temperature sensor. See equipment manufacturer service information. | 5A |
> | All other troubleshooting procedures have been completed, and the fault code is still active or inactive with more than one count within the last 25 engine hours? **NO** | 5A |  |
>
> ### STEP 5. Check ECM calibration and clear fault codes.
>
> #### STEP 5A. Check if an ECM calibration update is available.
>
> | **Conditions:** Connect all components. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Compare the ECM code and revision number in the ECM to the calibration revisions listed in the ECM Calibration Revision History for applicable changes related to this fault code. Use INSITE™ electronic service tool to find the present ECM code and revision number in the ECM. The ECM code and revision number are found in the Calibration Information section of System ID and Dataplate in Features and Parameters. | If a calibration update for this fault code is available, does the ECM contain that revision or higher? **YES** | 5B |
> | If a calibration update for this fault code is available, does the ECM contain that revision or higher? **NORepair:** If necessary, calibrate the ECM. [[87-019-032 — ECM Calibration Code\|Refer to Procedure 019-032]] in Section 19. | 5B |  |
>
> #### STEP 5B. Disable the fault code.
>
> | **Conditions:** Connect all components. Connect INSITE™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Disable and clear the fault code. Operate the engine within the "Conditions for Clearing the Fault Code" found in the Overview section of this troubleshooting procedure. | Fault code inactive? **YES** | Repair complete |
> | Fault code inactive? **NO** | Escalate or call for assistance |  |
