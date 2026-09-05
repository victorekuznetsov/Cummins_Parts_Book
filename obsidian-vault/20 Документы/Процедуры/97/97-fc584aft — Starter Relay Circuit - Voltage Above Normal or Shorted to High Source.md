---
type: "Процедура"
doc: "97-fc584aft"
title_en: "Starter Relay Circuit - Voltage Above Normal or Shorted to High Source"
modified: "2007-01-26"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
  - "80141463"
  - "80248213"
families:
  - "QSM11"
  - "QSX15"
manuals:
  - "3666415"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-fc584aft.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-fc584aft.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "двигатель/QSX15"
  - "группа/97"
  - "перевод/машинный"
---

# Starter Relay Circuit - Voltage Above Normal or Shorted to High Source

> [!abstract] Процедура · `97-fc584aft`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSM11, QSX15
> **Входит в руководства:** [[3666415 — ICON Idle Control System Master Repair Manual|3666415]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2007-01-26
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-fc584aft.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-fc584aft.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 584 (Послепродажное и OEM)

### Стартовая релейная схема - напряжение выше нормального или короткое до высокого источника

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 584 PID(P): СПН: ФМИ: Лампа: СТО: | Стартовая релейная схема - напряжение выше нормального или короткое до высокого источника. Высокое напряжение, обнаруженное в цепи стартового реле, когда низкое напряжение ожидалось модулем управления ICONTM. | Система ICONTM будет отключена. **Включено только обязательное отключение. Двигатель может быть запущен **не в обычном режиме. |

![[19c01537.png]]

### Описание цепи

Стартерная реле соединяет мощность с стартовым магнитным переключателем для запуска двигателя. Вышеупомянутая схема может варьироваться, например, разъем или штифты, в зависимости от марки или модели транспортного средства. Установки OEM могут обеспечить взаимодействие между модулем управления холостым ходом и другими устройствами ICONTM.

### Расположение компонента

Стартовое реле обычно устанавливается на переборке транспортного средства на впускной стороне двигателя.

Модуль ICONTM может быть расположен в другом месте в зависимости от применения транспортного средства.

### Практические замечания

Эта неисправность обычно указывает на короткое замыкание к напряжению батареи. Если есть короткое замыкание на аккумуляторе, двигатель может **не **быть запущен.

Система ICONTM может отображать только текущий активный код неисправности. Если одновременно активируется более одного кода неисправности, система ICONTM выдает наиболее приоритетную ошибку. После того, как ошибка была исправлена, будет выброшена следующая активная ошибка.

**Примечание: **Электронная система ICONTM может отображать более одного активного и неактивного кода неисправности одновременно.

## Предупреждения и меры предосторожности

> [!warning] ОСТОРОЖНО
>

**Для уменьшения возможности повреждения штифта и проводов жгута проводов используйте при проведении измерений следующий испытательный щуп: Номер детали 3822758 - пробный щуп типа пробоотвода Deutsch/AMP/Metri-Pack Номер детали 3822917 - пробный щуп типа разъема Deutsch/AMP/Metri-Pack.**

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Считайте коды неисправностей. |  |
|  | **STEP 1A.** Используйте функцию вспышки неисправности или инструмент электронного сервиса ICONTM для считывания кодов неисправностей. | Код ошибки 584 неактивен |
| ШАГ 2. | Стартовый тест |  |
|  | **ШАГ 2А.** Пройдите тест на старт. | Стартап работает правильно |
| ШАГ 3. | Проверьте стартовую эстафету. |  |
|  | **STEP 3A.** Проверить контакты ретранслятора стартера. | Никаких поврежденных контактов |
|  | **STEP 3B.** Проверьте сопротивление катушки реле стартера. | От 30 до 99 Ом |
|  | **ШАГ 3С.** Проверить на короткое замыкание. | Более 100 тыс. ом |
| ШАГ 4. | Проверьте проводные ремни ICONTM. |  |
|  | **STEP 4A.** Проверить контакты разъема модуля управления ICONTM с проводкой двигателя, кабины и проводов ICONTM. | Никаких поврежденных контактов |
|  | **STEP 4B.** Проверьте короткое замыкание от пин-кодов до пин-кодов. | Более 100 тыс. ом |
|  | **STEP 4C.** Проверьте короткое замыкание на аккумуляторе. | Менее 0,5 VDC |
| ШАГ 5. | Очистите код ошибки. |  |
|  | **STEP 5A.** Отключить код ошибки. | Код ошибки 584 обезврежен |

### ШАГ 1. Считайте коды неисправностей.

#### ШАГ 1A. Используйте функцию вспышки неисправности или инструмент электронного сервиса ICONTM для считывания кодов неисправностей.

| **Условия: **Соединить все компоненты. Включите зажигание. Подключите электронный сервис ICONTM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Используйте функцию вспышки неисправности или инструмент электронного сервиса ICONTM для считывания кодов неисправностей. | Код ошибки 584 неактивен. | 2А |
|  | 3А |  |

### ШАГ 2. Стартовый тест

#### ШАГ 2A. Проведите тест на старт.

| **Условия:** Включить переключатель зажигания. Подключите электронный сервис ICONTM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проведите тест на старт. | Стартер работает должным образом см. Неактивные или периодические коды ошибок, процедура[[99-019-362 — Inactive or Intermittent Fault Code\|019-362]]. | 5а |
|  | 3А |  |

### ШАГ 3. Проверьте стартовую эстафету.

#### ШАГ 3A. Проверьте контакты стартера реле.

| **Условия:** Выключите замок зажигания. Отсоедините стартовую реле от ремня электропроводки двигателя ICONTM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Осмотрите стартовое реле на предмет: Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема разъема разъема или разъема изоляции Поврежденный разъем блокировки вкладки. Для общих методов проверки обратитесь к компонентному коннектору и Pin-инспекции, процедура[[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | Никаких поврежденных контактов | 3B |
| Замените реле Смой грязь, мусор или влагу из контактов реле-коннектора с помощью электрического контактного очистителя, Номер детали 3824510. Установите соответствующий уплотнитель разъема, если он поврежден или отсутствует. Замените стартер реле. См. процедуру 019-302. | 5а |  |

#### ШАГ 3B. Проверьте сопротивление катушки реле стартера.

| **Условия:** Выключите замок зажигания. Отсоедините стартовую реле от ремня электропроводки двигателя ICONTM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте сопротивление катушки реле стартера. Измерить сопротивление от контакта 85 стартового реле до контакта 86 реле. См. схему проводов или схему схемы для идентификации контакта с разъемом. Для общих методов измерения сопротивления, обратитесь к измерениям сопротивления с использованием мультиметра и схемы проводов, процедуры[[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | От 30 до 99 Ом | 3C |
| Замените реле. См. процедуру[[97-019-302 — Starter Relay\|019-302]]. | 5а |  |

#### ШАГ 3C. Проверьте цепь на короткое замыкание.

| **Условия:** Выключите замок зажигания. Отсоедините стартовую реле от ремня электропроводки двигателя ICONTM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте короткий контакт. Измерить сопротивление от контакта 87 реле стартера ко всем другим штифтам, кроме контакта 87А. **Примечание: **Это обычно открытый реле. См. схему проводов или схему схемы для идентификации контакта с разъемом. Для общих методов измерения сопротивления, обратитесь к измерениям сопротивления с использованием мультиметра и схемы проводов, процедуры[[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Более 100 тыс. ом | 4А |
| Замените реле. См. процедуру[[97-019-302 — Starter Relay\|019-302]]. | 5а |  |

### ШАГ 4. Проверьте проводные ремни ICONTM.

#### ШАГ 4A. Осмотрите контактные линзы разъема для проводов двигателя ICONTM и коннектора модуля управления ICONTM.

| **Условия:** Выключите замок зажигания. Отсоедините разъем B модуля управления ICONTM от модуля управления ICONTM. Отключите стартовую реле. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Осмотрите контакты разъема модуля управления ICONTM для проводов двигателя, кабины и коннектора модуля управления ICONTM для следующего: Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разбитые штифты Разъем разъема разъема или разъема разъема разъема или разъема изоляции Поврежденный разъем блокировки вкладки. Для общих методов проверки обратитесь к компонентному коннектору и Pin-инспекции, процедура[[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | Никаких поврежденных контактов | 4B |
| Ремонт поврежденных контактов. Промывайте грязь, мусор или влагу от контактов разъема с помощью электрического контактного очистителя, Номер детали 3824510. Установите соответствующий уплотнитель разъема, если он поврежден или отсутствует. Ремонт ремня электропроводки двигателя ICONTM. См. процедуру 019-206 или 019-207. Заменить электропроводку двигателя ICONTM. См. процедуру 019-043. | 5а |  |

#### ШАГ 4B. Проверьте короткое замыкание от пин-кодов до пин-кодов.

| **Условия:** Выключите замок зажигания. Отсоедините разъемы ICONTM Idle Control Module A и B от модуля ICONTM idle Control. Отключите разъем OEM ECM двигателя. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте короткое замыкание от пин-кодов до пин-кодов. Измерьте сопротивление контакта 6 в разъеме для проводов Aftermarket или OEM ICONTM B со всеми другими штифтами в разъемах для проводов ICONTM A и B, за исключением контакта 5 в разъеме для проводов ICONTM B. См. схему проводов или схему схемы для идентификации контакта с разъемом. Для общих методов измерения сопротивления, обратитесь к измерениям сопротивления с использованием мультиметра и схемы проводов, процедуры[[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Более 100 тыс. ом | 4C |
| Ремонт ремня электропроводки двигателя ICONTM. См. процедуру 019-206 или 019-207. Заменить электропроводку двигателя ICONTM. См. процедуру 019-043. Ремонт проводов такси. См. 019-206 или 019-207. Замените проводку кабины. См. процедуру 019-305. По мере необходимости ремонтировать или заменять электропроводку OEM. | 5а |  |

#### ШАГ 4C. Проверьте короткое замыкание на аккумуляторе.

| **Условия:** Отсоединить разъем B модуля управления ICONTM от модуля управления ICONTM. Включите зажигание. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Проверьте короткое замыкание на аккумуляторе. Измерьте напряжение от контакта 6 разъема проводов Aftermarket или OEM ICONTM B с заземлением блока двигателя. | Менее 0,5 VDC Заменить модуль управления ICONTM. См. процедуру[[97-019-358 — ICON™ Idle Control Module\|019-358]]. | Ремонт завершён |
| Ремонт ремня электропроводки двигателя ICONTM. См. процедуру 019-206 или 019-207. Заменить электропроводку двигателя ICONTM. См. процедуру 019-043. По мере необходимости ремонтировать или заменять электропроводку OEM. | 5а |  |

### ШАГ 5. Очистите код ошибки.

#### ШАГ 5A. Отключите код неисправности.

| **Условия: **Соединить все компоненты. Включите зажигание. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Очистите код неактивной ошибки. Цикл переключателя зажигания для проверки кода неисправности неактивен. | Код ошибки 584 обезврежен | Ремонт завершён |
| Устранение неполадок с оставшимися активными кодами неисправностей. | Соответствующие диаграммы устранения неполадок |  |


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 584 (Aftermarket and OEM)
>
> ### Starter Relay Circuit - Voltage Above Normal or Shorted to High Source
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 584 PID(P): SPN: FMI: Lamp: SRT: | Starter Relay Circuit - Voltage Above Normal or Shorted to High Source. High voltage detected at the starter relay circuit when low voltage was expected by the ICON™ idle control module. | The ICON™ system will be disabled. **Only** mandatory shutdown will be enabled. Engine can possibly **not** be started normally. |
>
> ### Circuit Description
>
> The starter relay connects power to the starter magnetic switch for starting the engine. The above circuit diagram can vary, such as connector or pins, depending on the vehicle make or model. OEM installations can possibly provide the harnessing between the idle control module and other ICON™ devices.
>
> ### Component Location
>
> The starter relay is typically mounted on the vehicle's bulkhead on the intake side of the engine.
>
> The ICON™ module can be located in a different location depending on the vehicle application.
>
> ### Shoptalk
>
> This fault typically indicates a short circuit to battery voltage. If there is a short circuit to battery, the engine can **not** be started.
>
> The ICON™ system can display **only** the present active fault code. If more than one fault code is active at the same time, the ICON™ system flashes out the highest priority fault. After the fault has been corrected then the next active fault will be flashed out.
>
> **Note:** The ICON™ electronic service tool can display more than one active and or inactive fault codes at the same time.
>
> ## Warnings and Cautions
>
> **CAUTION · Осторожно**
>
> **To reduce the possibility of pin and harness damage, use the following test leads when taking a measurement: Part Number 3822758 - male Deutsch/AMP/Metri-Pack test lead Part Number 3822917 - female Deutsch/AMP/Metri-Pack test lead.**
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Read the fault codes. |  |
> |  | **STEP 1A.** Use the fault flashout feature or the ICON™ electronic service tool to read the fault codes. | Fault Code 584 inactive |
> | STEP 2. | Starter Test |  |
> |  | **STEP 2A.** Run starter test. | Starter operates properly |
> | STEP 3. | Check the starter relay. |  |
> |  | **STEP 3A.** Inspect the starter relay connector pins. | No damaged pins |
> |  | **STEP 3B.** Check the starter relay coil resistance. | 30 to 99 ohms |
> |  | **STEP 3C.** Check for a short circuit. | More than 100k ohms |
> | STEP 4. | Check the ICON™ harnesses. |  |
> |  | **STEP 4A.** Inspect the ICON™ engine harness, cab harness, and ICON™ idle control module connector pins. | No damaged pins |
> |  | **STEP 4B.** Check for a short circuit from pin to pin. | More than 100k ohms |
> |  | **STEP 4C.** Check for a short circuit to the battery. | Less than 0.5 VDC |
> | STEP 5. | Clear the fault code. |  |
> |  | **STEP 5A.** Disable the fault code. | Fault Code 584 cleared |
>
> ### STEP 1. Read the fault codes.
>
> #### STEP 1A. Use the fault flashout feature or the ICON™ electronic service tool read the fault codes.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. Connect the ICON™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Use the fault flashout feature or the ICON™ electronic service tool read the fault codes. | Fault Code 584 inactive. | 2A |
> |  | 3A |  |
>
> ### STEP 2. Starter Test
>
> #### STEP 2A. Run starter test.
>
> | **Conditions:** Turn keyswitch ON. Connect the ICON™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Run the starter test. | Starter operates properly Refer to Inactive or Intermittent Fault Codes, Procedure [[99-019-362 — Inactive or Intermittent Fault Code\|019-362]]. | 5A |
> |  | 3A |  |
>
> ### STEP 3. Check the starter relay.
>
> #### STEP 3A. Inspect the starter relay connector pins.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the starter relay from the ICON™ engine harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the starter relay for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris on or in the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. For general inspection techniques, refer to Component Connector and Pin Inspection, Procedure [[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | No damaged pins | 3B |
> | Replace the relay Flush the dirt, debris, or moisture from the relay connector pins using electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Replace the starter relay. Refer to Procedure 019-302. | 5A |  |
>
> #### STEP 3B. Check the starter relay coil resistance.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the starter relay from the ICON™ engine harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check the starter relay coil resistance. Measure the resistance from pin 85 of the starter relay to pin 86 of the relay. Refer to the wiring diagram or the circuit diagram for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | 30 to 99 ohms | 3C |
> | Replace the relay. Refer to Procedure [[97-019-302 — Starter Relay\|019-302]]. | 5A |  |
>
> #### STEP 3C. Check for a short circuit.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the starter relay from the ICON™ engine harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for a shorted contact. Measure the resistance from pin 87 of the starter relay to all other pins except pin 87A. **NOTE:** This is a normally open relay. Refer to the wiring diagram or the circuit diagram for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | More than 100k ohms | 4A |
> | Replace the relay. Refer to Procedure [[97-019-302 — Starter Relay\|019-302]]. | 5A |  |
>
> ### STEP 4. Check the ICON™ harnesses.
>
> #### STEP 4A. Inspect the ICON™ engine harness and ICON™ idle control module connector pins.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the ICON™ idle control module B connector from the ICON™ idle control module. Disconnect the starter relay. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Inspect the ICON™ engine harness, cab harness, and ICON™ idle control module connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris on or in the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. For general inspection techniques, refer to Component Connector and Pin Inspection, Procedure [[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | No damaged pins | 4B |
> | Repair the damaged pins. Flush the dirt, debris, or moisture from the connector pins using electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair the ICON™ engine harness. Refer to Procedure 019-206 or 019-207. Replace the ICON™ engine harness. Refer to Procedure 019-043. | 5A |  |
>
> #### STEP 4B. Check for a short circuit from pin to pin.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the ICON™ idle control module A and B connectors from the ICON™ idle control module. Disconnect the engine OEM ECM connector. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for a short circuit from pin to pin. Measure the resistance from pin 6 in the Aftermarket or OEM ICON™ B harness connector to all other pins in the ICON™ A and B harness connectors, except pin 5 in ICON™ B harness connector. Refer to the wiring diagram or the circuit diagram for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | More than 100k ohms | 4C |
> | Repair the ICON™ engine harness. Refer to Procedure 019-206 or 019-207. Replace the ICON™ engine harness. Refer to Procedure 019-043. Repair the cab harness. Refer to 019-206 or 019-207. Replace the cab harness. Refer to Procedure 019-305. Repair or replace the OEM wiring harness as necessary. | 5A |  |
>
> #### STEP 4C. Check for a short circuit to the battery.
>
> | **Conditions:** Disconnect the ICON™ idle control module B connector from the ICON™ idle control module. Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Check for a short circuit to the battery. Measure the voltage from pin 6 of the Aftermarket or OEM ICON™ B harness connector to engine block ground. | Less than 0.5 VDC Replace the ICON™ idle control module. Refer to Procedure [[97-019-358 — ICON™ Idle Control Module\|019-358]]. | Repair complete |
> | Repair the ICON™ engine harness. Refer to Procedure 019-206 or 019-207. Replace the ICON™ engine harness. Refer to Procedure 019-043. Repair or replace the OEM wiring harness as necessary. | 5A |  |
>
> ### STEP 5. Clear the fault code.
>
> #### STEP 5A. Disable the fault code.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Clear the inactive fault code. Cycle the keyswitch to verify the fault code is inactive. | Fault Code 584 cleared | Repair complete |
> | Troubleshoot any remaining active fault codes. | Appropriate troubleshooting charts |  |
