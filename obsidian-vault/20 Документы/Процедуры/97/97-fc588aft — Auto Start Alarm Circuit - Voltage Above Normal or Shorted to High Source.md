---
type: "Процедура"
doc: "97-fc588aft"
title_en: "Auto Start Alarm Circuit - Voltage Above Normal or Shorted to High Source"
modified: "2004-10-07"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-fc588aft.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-fc588aft.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "двигатель/QSX15"
  - "группа/97"
  - "перевод/машинный"
---

# Auto Start Alarm Circuit - Voltage Above Normal or Shorted to High Source

> [!abstract] Процедура · `97-fc588aft`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSM11, QSX15
> **Входит в руководства:** [[3666415 — ICON Idle Control System Master Repair Manual|3666415]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2004-10-07
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-fc588aft.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-fc588aft.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 588 (Послепродажное и OEM)

### Автоматическая система сигнализации запуска - напряжение выше нормального или короткое до высокого источника

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 588 PID(P): СПН: ФМИ: Лампа: СТО: | Автоматическая система сигнализации запуска - напряжение выше нормального или короткое до высокого источника. Высокое напряжение, обнаруженное на цепи сигнализации, когда низкое напряжение ожидалось модулем управления ICONTM. | Система ICONTM будет отключена. Включено только обязательное отключение. Двигатель запускается нормально. |

![[19803013.png]]

### Описание цепи

Схема сигнализации включает звуковую сигнализацию, чтобы предупредить о предстоящем запуске двигателя. Вышеупомянутая схема может варьироваться, например, разъем или штифты, в зависимости от марки или модели транспортного средства. Установки OEM могут обеспечить взаимодействие между модулем управления холостым ходом и другими устройствами ICONTM.

### Расположение компонента

Сигнализация запуска двигателя обычно устанавливается на переборке транспортного средства на впускной стороне двигателя.

Модуль ICONTM может быть расположен в другом месте в зависимости от применения транспортного средства.

### Практические замечания

Эта неисправность обычно указывает на короткое замыкание к напряжению батареи на контакте А разъема сигнализации. Эта ошибка может привести к тому, что сигнал тревоги будет звучать **не**. Сигнал тревоги может звучать в течение 14 секунд до запуска двигателя. Сигнализация активируется путем нанесения заземления от контакта 3 неработающего модуля управления ICONTM B разъема на контакт А разъема тревоги.

Система ICONTM может отображать только текущий активный код неисправности. Если одновременно активируется более одного кода неисправности, система ICONTM выдает наиболее приоритетную ошибку. После того, как ошибка была исправлена, будет выброшена следующая активная ошибка.

**Примечание: **Электронная система ICONTM может отображать более одного активного и неактивного кода неисправности одновременно.

## Предупреждения и меры предосторожности

> [!warning] ОСТОРОЖНО
>

**Для уменьшения возможности повреждения штифта и проводов жгута проводов используйте при проведении измерений следующий испытательный щуп: Номер детали 3822758 - пробный щуп типа пробоотвода Deutsch/AMP/Metri-Pack Номер детали 3822917 - пробный щуп типа разъема Deutsch/AMP/Metri-Pack.**

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проведите тест на сигнализацию. |  |
|  | **ШАГ 1А.** Испытайте сигнализацию запуска ИКОНТМ. | Звуки тревоги |
|  | **STEP 1B.** Проверьте работу модуля управления холостым ходом ICONTM. | Звуки тревоги и код неисправности неактивны |
| ШАГ 2. | Проверьте сигнализацию запуска двигателя. |  |
|  | **STEP 2A.** Проверить контакты разъема аварийной сигнализации двигателя. | Никаких поврежденных контактов |
|  | **STEP 2A-1.** Проверить контактные устройства разъема аварийной сигнализации. | Никаких поврежденных контактов |
|  | **STEP 2B.** Проверьте сопротивление сигнализации двигателя. | 800-1200 Ом |
| ШАГ 3. | Проверьте двигатель ICONTM или OEM-проводку. |  |
|  | **STEP 3A.** Проверить коннекторы разъемов двигателя ICONTM и коннекторов модуля управления ICONTM. | Никаких поврежденных контактов |
|  | **ШАГ 3В.** Проверить короткое замыкание от пин-кодов до пин-кодов. | Более 100 тыс. ом |
|  | **STEP 3C** Проверьте короткое замыкание на аккумуляторе. | Менее 0,5 VDC |
| ШАГ 3. | Очистите код ошибки. |  |
|  | **STEP 3A.** Отключить код ошибки. | Код ошибки 588 очищен |

### ШАГ 1. Проведите тест на сигнализацию.

#### ШАГ 1A. Проверить сигнализацию ICONTM.

| **Условия:** Выключите замок зажигания. Подключите электронный сервис ICONTM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
|  | Звуки тревоги | 1В |
|  | 2А |  |

#### ШАГ 1B. Проверьте работу модуля управления ICONTM.

| **Условия:** Включить переключатель зажигания. Подключите электронный сервис ICONTM. Запускай двигатель. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
|  | Сигналы тревоги и код неактивности см. Неактивные или прерывистые коды ошибок, процедура[[99-019-362 — Inactive or Intermittent Fault Code\|019-362]]. | 4А |
| Заменить модуль управления ICONTM idle. См. процедуру[[97-019-358 — ICON™ Idle Control Module\|019-358]]. | Ремонт завершён |  |

### ШАГ 2. Проверьте сигнализацию запуска двигателя.

#### ШАГ 2A. Проверьте контакты разъема аварийной сигнализации двигателя.

| **Условия:** Выключите замок зажигания. Отключите разъем аварийной сигнализации двигателя от электропроводки ICONTM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Корродированные штифты Бент или сломанные штифты Отталкивание назад или расширенные штифты Проводная изоляция Повреждение Влажность в или на разъем Пропавшие или поврежденные соединительные штифты Коннекторная оболочка разбитая Грязь или мусор в или на разъемных контактах. Для общих методов проверки обратитесь к компонентному коннектору и Pin-инспекции, процедура[[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | Никаких поврежденных контактов | 2А-1-1 |
| Ремонт контактов разъема. Промывайте грязь, мусор или влагу от контактов разъема с помощью электрического контактного очистителя, Номер детали 3824510. Установите соответствующий уплотнитель разъема, если он поврежден или отсутствует. Ремонт контактов разъема. См. процедуру 019-202 или 019-206. | 4А |  |

#### ШАГ 2A-1. Проверьте контакты разъема аварийной сигнализации.

| **Условия:** Выключите замок зажигания. Отключите сигнализацию запуска ICONTM от электропроводки двигателя ICONTM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Корродированные штифты Бент или сломанные штифты Отталкивание назад или расширенные штифты Проводная изоляция Повреждение Влажность в или на разъем Пропавшие или поврежденные соединительные штифты Коннекторная оболочка разбитая Грязь или мусор в или на разъемных контактах. Для общих методов проверки обратитесь к компонентному коннектору и Pin-инспекции, процедура[[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | Никаких поврежденных контактов | 2В |
| Ремонт поврежденных контактов. Промывайте грязь, мусор или влагу от контактов разъема с помощью электрического контактного очистителя, Номер детали 3824510. Установите соответствующий уплотнитель разъема, если он поврежден или отсутствует. Ремонт ремня электропроводки двигателя ICONTM. См. процедуру 019-206 или 019-207. Заменить электропроводку двигателя ICONTM. См. процедуру 019-043. По мере необходимости ремонтировать или заменять электропроводку OEM. | 4А |  |

#### ШАГ 2B. Проверьте сопротивление сигнализации запуска двигателя.

| **Условия:** Выключите замок зажигания. Отключите разъем аварийной сигнализации двигателя от электропроводки ICONTM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте сопротивление от контакта А разъема аварийной сигнализации двигателя к контакту В разъема. См. схему проводов или описание схемы в начале этого кода неисправности для идентификации контакта с разъемом. Для общих методов измерения сопротивления, обратитесь к измерениям сопротивления с использованием мультиметра и схемы проводов, процедуры[[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | 800-1200 Ом | 3А |
| Замените сигнализацию запуска двигателя. См. процедуру[[97-019-293 — Engine Start Alarm\|019-293]]. | 4А |  |

### ШАГ 3. Проверьте двигатель ICONTM или OEM-проводку.

#### ШАГ 3A. Осмотрите контактные линзы разъема для проводов двигателя ICONTM и коннектора модуля управления ICONTM.

| **Условия:** Выключите замок зажигания. Отсоедините разъемы ICONTM Idle Control Module A и B от модуля ICONTM idle Control. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Корродированные штифты Бент или сломанные штифты Отталкивание назад или расширенные штифты Проводная изоляция Повреждение Влажность в или на разъем Пропавшие или поврежденные соединительные штифты Коннекторная оболочка разбитая Грязь или мусор в или на разъемных контактах. Для общих методов проверки обратитесь к компонентному коннектору и Pin-инспекции, процедура[[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | Никаких поврежденных контактов | 3B |
| Ремонт поврежденных контактов. Промывайте грязь, мусор или влагу от контактов разъема с помощью электрического контактного очистителя, Номер детали 3824510. Установите соответствующий уплотнитель разъема, если он поврежден или отсутствует. Ремонт ремня электропроводки двигателя ICONTM. См. процедуру 019-206. Заменить электропроводку двигателя ICONTM. См. процедуру 019-043. По мере необходимости ремонтировать или заменять электропроводку OEM. | 4А |  |

#### ШАГ 3B. Проверьте короткое замыкание от пин-кодов до пин-кодов.

| **Условия:** Выключите замок зажигания. Отсоедините модуль управления ICONTM A и B проводов ремня разъемов от модуля управления ICONTM. Отключите разъем аварийной сигнализации двигателя от электропроводки ICONTM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте сопротивление от контакта 3 модуля управления ICONTM холостого хода B проводов жгута разъёма ко всем штифтам в разъёмах A и B проводов жгута. См. схему проводов или описание схемы в начале этого кода неисправности для идентификации контакта с разъемом. Для общих методов измерения сопротивления, обратитесь к измерениям сопротивления с использованием мультиметра и схемы проводов, процедуры[[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Более 100 тыс. ом | 3C |
| Ремонт или замена ремня электропроводки двигателя ICONTM. Ремонт ремня электропроводки двигателя ICONTM. См. процедуру 019-202 или 019-206. Заменить электропроводку двигателя ICONTM. См. процедуру 019-043. По мере необходимости ремонтировать или заменять электропроводку OEM. | 4А |  |

#### ШАГ 3C. Проверьте короткое замыкание на аккумуляторе.

| **Условия:** Отсоедините разъем аварийной сигнализации двигателя от ремня электропроводки двигателя ICONTM. Отсоедините разъем B модуля управления ICONTM от модуля управления ICONTM. Включите зажигание. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте напряжение от контакта 3 модуля управления ICONTM холостого хода B проводов ремня разъема к заземлению блока двигателя. См. схему проводов или описание схемы в начале этого кода неисправности для идентификации контакта с разъемом. | Менее 0,5 VDC Заменить модуль управления ICONTM. См. процедуру[[97-019-358 — ICON™ Idle Control Module\|019-358]]. | Ремонт завершён |
| Ремонт или замена ремня электропроводки двигателя ICONTM. Ремонт ремня электропроводки двигателя ICONTM. См. процедуру 019-202 или 019-206. Заменить электропроводку двигателя ICONTM. См. процедуру 019-043. По мере необходимости ремонтировать или заменять электропроводку OEM. | 4А |  |

### ШАГ 4. Очистите код ошибки.

#### ШАГ 4A. Отключите код неисправности.

| **Условия: **Соединить все компоненты. Включите зажигание. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Цикл переключателя зажигания для проверки кода неисправности неактивен. | Код ошибки 588 очищен | Ремонт завершён |
| Устранение неполадок с оставшимися активными кодами неисправностей. | Соответствующие диаграммы устранения неполадок |  |


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 588 (Aftermarket and OEM)
>
> ### Auto Start Alarm Circuit - Voltage Above Normal or Shorted to High Source
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 588 PID(P): SPN: FMI: Lamp: SRT: | Auto Start Alarm Circuit - Voltage Above Normal or Shorted to High Source. High voltage detected at the alarm circuit when low voltage was expected by the ICON™ idle control module. | The ICON™ system will be disabled. **Only** mandatory shutdown will be enabled. Engine will start normally. |
>
> ### Circuit Description
>
> The alarm circuit turns on the audible alarm to warn of an impending engine start. The above circuit diagram can vary, such as connector or pins, depending on the vehicle make or model. OEM installations can possibly provide the harnessing between the idle control module and other ICON™ devices.
>
> ### Component Location
>
> The engine start alarm is typically mounted on the vehicle's bulkhead on the intake side of the engine.
>
> The ICON™ module can be located in a different location depending on the vehicle application.
>
> ### Shoptalk
>
> This fault typically indicates a short circuit to battery voltage on pin A of the alarm connector. This fault can cause the alarm to **not** sound. The alarm can sound for 14 seconds before an engine start. The alarm is activated by applying a ground from pin 3 of the ICON™ idle control module B connector to pin A of the alarm connector.
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
> | STEP 1. | Perform the alarm test. |  |
> |  | **STEP 1A.** Test the ICON™ start alarm. | Alarm sounds |
> |  | **STEP 1B.** Check the ICON™ idle control module operation. | Alarm sounds and fault code inactive |
> | STEP 2. | Check the engine start alarm. |  |
> |  | **STEP 2A.** Inspect the engine start alarm connector pins. | No damaged pins |
> |  | **STEP 2A-1.** Inspect the engine harness start alarm connector pins. | No damaged pins |
> |  | **STEP 2B.** Check the engine start alarm resistance. | 800 to 1200 ohms |
> | STEP 3. | Check the ICON™ engine or OEM harness. |  |
> |  | **STEP 3A.** Inspect the ICON™ engine harness and ICON™ idle control module connector pins. | No damaged pins |
> |  | **STEP 3B.** Check for a short circuit from pin to pin. | More than 100k ohms |
> |  | **STEP 3C.** Check for a short circuit to the battery. | Less than 0.5 VDC |
> | STEP 3. | Clear the fault code. |  |
> |  | **STEP 3A.** Disable the fault code. | Fault Code 588 cleared |
>
> ### STEP 1. Perform the alarm test.
>
> #### STEP 1A. Test the ICON™ start alarm.
>
> | **Conditions:** Turn keyswitch OFF. Connect the ICON™ electronic service tool. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> |  | Alarm sounds | 1B |
> |  | 2A |  |
>
> #### STEP 1B. Check the ICON™ idle control module operation.
>
> | **Conditions:** Turn keyswitch ON. Connect the ICON™ electronic service tool. Start the engine. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> |  | Alarm sounds and fault code inactive Refer to Inactive or Intermittent Fault Codes, Procedure [[99-019-362 — Inactive or Intermittent Fault Code\|019-362]]. | 4A |
> | Replace the ICON™ idle control module. Refer to Procedure [[97-019-358 — ICON™ Idle Control Module\|019-358]]. | Repair Complete |  |
>
> ### STEP 2. Check the engine start alarm.
>
> #### STEP 2A. Inspect the engine start alarm connector pins.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine start alarm connector from the ICON™ engine harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Corroded pins Bent or broken pins Pushed back or expanded pins Wire insulation damage Moisture in or on the connector Missing or damaged connector seals Connector shell broken Dirt or debris in or on the connector pins. For general inspection techniques, refer to Component Connector and Pin Inspection, Procedure [[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | No damaged pins | 2A-1 |
> | Repair the connector pins. Flush the dirt, debris, or moisture from the connector pins using electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair the connector pins. Refer to Procedure 019-202 or 019-206. | 4A |  |
>
> #### STEP 2A-1. Inspect the engine harness start alarm connector pins.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the ICON™ start alarm from the ICON™ engine harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Corroded pins Bent or broken pins Pushed back or expanded pins Wire insulation damage Moisture in or on the connector Missing or damaged connector seals Connector shell broken Dirt or debris in or on the connector pins. For general inspection techniques, refer to Component Connector and Pin Inspection, Procedure [[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | No damaged pins | 2B |
> | Repair the damaged pins. Flush the dirt, debris, or moisture from the connector pins using electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair the ICON™ engine harness. Refer to Procedure 019-206 or 019-207. Replace the ICON™ engine harness. Refer to Procedure 019-043. Repair or replace the OEM wiring harness as necessary. | 4A |  |
>
> #### STEP 2B. Check the engine start alarm resistance.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine start alarm connector from the ICON™ engine harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from pin A of the engine start alarm connector to pin B of the connector. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | 800 to 1200 ohms | 3A |
> | Replace the engine start alarm. Refer to Procedure [[97-019-293 — Engine Start Alarm\|019-293]]. | 4A |  |
>
> ### STEP 3. Check the ICON™ engine or OEM harness.
>
> #### STEP 3A. Inspect the ICON™ engine harness and ICON™ idle control module connector pins.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the ICON™ idle control module A and B connectors from the ICON™ idle control module. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Corroded pins Bent or broken pins Pushed back or expanded pins Wire insulation damage Moisture in or on the connector Missing or damaged connector seals Connector shell broken Dirt or debris in or on the connector pins. For general inspection techniques, refer to Component Connector and Pin Inspection, Procedure [[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | No damaged pins | 3B |
> | Repair the damaged pins. Flush the dirt, debris, or moisture from the connector pins using electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair the ICON™ engine harness. Refer to Procedure 019-206. Replace the ICON™ engine harness. Refer to Procedure 019-043. Repair or replace the OEM wiring harness as necessary. | 4A |  |
>
> #### STEP 3B. Check for a short circuit from pin to pin.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the ICON™ idle control module A and B harness connectors from the ICON™ idle control module. Disconnect the engine start alarm connector from the ICON™ engine harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from pin 3 of the ICON™ idle control module B harness connector to all pins in the A and B harness connectors. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | More than 100k ohms | 3C |
> | Repair or replace the ICON™ engine harness. Repair the ICON™ engine harness. Refer to Procedure 019-202 or 019-206. Replace the ICON™ engine harness. Refer to Procedure 019-043. Repair or replace the OEM wiring harness as necessary. | 4A |  |
>
> #### STEP 3C. Check for a short circuit to the battery.
>
> | **Conditions:** Disconnect the engine start alarm connector from the ICON™ engine harness. Disconnect the ICON™ idle control module B connector from the ICON™ idle control module. Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the voltage from pin 3 of the ICON™ idle control module B harness connector to engine block ground. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. | Less than 0.5 VDC Replace the ICON™ idle control module. Refer to Procedure [[97-019-358 — ICON™ Idle Control Module\|019-358]]. | Repair Complete |
> | Repair or replace the ICON™ engine harness. Repair the ICON™ engine harness. Refer to Procedure 019-202 or 019-206. Replace the ICON™ engine harness. Refer to Procedure 019-043. Repair or replace the OEM wiring harness as necessary. | 4A |  |
>
> ### STEP 4. Clear the fault code.
>
> #### STEP 4A. Disable the fault code.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Cycle the keyswitch to verify the fault code is inactive. | Fault Code 588 cleared | Repair complete |
> | Troubleshoot any remaining active fault codes. | Appropriate troubleshooting charts |  |
