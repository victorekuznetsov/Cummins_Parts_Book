---
type: "Процедура"
doc: "97-fc588int"
title_en: "Autostart Alarm Circuit - Voltage Above Normal or Shorted to High Source"
modified: "2004-09-28"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-fc588int.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-fc588int.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "двигатель/QSX15"
  - "группа/97"
  - "перевод/машинный"
---

# Autostart Alarm Circuit - Voltage Above Normal or Shorted to High Source

> [!abstract] Процедура · `97-fc588int`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSM11, QSX15
> **Входит в руководства:** [[3666415 — ICON Idle Control System Master Repair Manual|3666415]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2004-09-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-fc588int.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-fc588int.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 588 (интегрированный)

### Автозапуск сигнализации - напряжение выше нормального или короткое до высокого источника

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 588 PID(P): S121 SPN: 611 FMI: 3/3 лампы: Желтая СТО: | Автозапуск сигнализации - напряжение выше нормального или короткое до высокого источника. Высокое напряжение, обнаруженное на цепи сигнализации, когда низкое напряжение ожидалось электронным модулем управления двигателем (ECM). | Система ICONTM будет отключена. Включено только обязательное отключение. Двигатель можно запускать нормально. |

![[19803489.png]]

### Описание цепи

Схема сигнализации включает звуковую сигнализацию, чтобы предупредить о предстоящем запуске двигателя.

### Расположение компонента

Сигнализация ICONTM установлена на огневой стенке автомобиля на стороне впуска двигателя.

### Практические замечания

Эта неисправность обычно указывает на короткое замыкание к батарее или открытому контуру. Функция сцепления вентилятора 2 **не используется на ISM. Для подключения к системе Signature/ISX требуется ремень тормозной проводов двигателя ICONTM. **Для Signature/ISX с установленной системой ICONTM доступен только 3-позиционный тормозной переключатель двигателя.

## Предупреждения и меры предосторожности

> [!warning] ОСТОРОЖНО
>

**Для уменьшения возможности повреждения штифта и проводов жгута проводов используйте при проведении измерений следующий испытательный щуп: Номер детали 3822758 - пробный щуп типа пробоотвода Deutsch/AMP/Metri-Pack Номер детали 3822917 - пробный щуп типа разъема Deutsch/AMP/Metri-Pack.**

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Прочитайте все коды ошибок. |  |
|  | **ШАГ 1А.** Прочитайте коды неисправностей с помощью инструментария электронного обслуживания INSITETM или выключите светильник ICONTM. | Код ошибки 588 неактивен |
|  | **STEP 1B.** Проведите тест на сигнализацию ICONTM. | Звуки тревоги |
| ШАГ 2. | Проверьте сигнализацию запуска двигателя. |  |
|  | **STEP 2A.** Проверить разъем аварийной сигнализации двигателя на наличие поврежденных контактов. | Никаких поврежденных контактов |
|  | **STEP 2B.** Проверьте сопротивление сигнализации запуска двигателя от пин-кодов до пин-кодов. | Более 800 и менее 1200 Ом |
| ШАГ 3. | Проверьте жгут электропроводки двигателя. |  |
|  | **STEP 3A.** Осмотрите жгут электропроводки двигателя и контакты разъема сигнализации двигателя. | Никаких поврежденных контактов |
|  | **STEP 3B.** Проверьте короткое замыкание на напряжение батареи. | Менее положительного (+) 1,5 VDC |
|  | **STEP 3B-1.** Проверьте короткое замыкание напряжения батареи в электропроводке OEM. | Менее положительного (+) 1,5 VDC |
| ШАГ 4. | Сбросьте коды неисправностей. |  |
|  | **STEP 4A.** Отключить код ошибки. | Код ошибки 588 неактивен |

### ШАГ 1. Прочитайте все коды ошибок.

#### ШАГ 1A. Прочитайте коды неисправностей с помощью инструментария электронного обслуживания INSITETM или выключите лампу ICONTM.

| **Условия:** Включить переключатель зажигания. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
|  | Код ошибки 588 неактивен | 1В |
| Код ошибки 588 Active | 1В |  |

#### ШАГ 1B. Проведите тест на сигнализацию ICONTM.

| **Условия:** Подключить электронный сервисный инструмент INSITETM к двигателю. Включите зажигание. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Используйте INSITETM для выполнения теста сигнализации ICONTM. | Звуки тревоги | 4А |
| Тревога **не** звучит | 2А |  |

### ШАГ 2. Проверьте сигнализацию запуска двигателя.

#### ШАГ 2A. Проверьте разъем аварийной сигнализации двигателя на наличие поврежденных контактов.

| **Условия:** Выключите замок зажигания. Отключите сигнализацию запуска двигателя от электропроводки двигателя. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Корродированные штифты Бент или сломанные штифты Отталкивание назад или расширенные штифты Проводная изоляция Повреждение Влажность в или на разъем Пропавшие или поврежденные соединительные штифты Коннекторная оболочка разбитая Грязь или мусор в или на разъемных контактах. Для общих методов проверки обратитесь к компонентному коннектору и Pin-инспекции, процедура[[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | Никаких поврежденных контактов | 2В |
| Ремонт или замена поврежденных контактов. Промывайте грязь, мусор и влагу от контактов разъема с помощью электрического контактного очистителя, Номер детали 3824510. Установите соответствующий уплотнитель разъема, если он поврежден или отсутствует. Ремонт разъема аварийной сигнализации двигателя. См. процедуру 019-202 или 019-206. Замените сигнализацию запуска двигателя. См. процедуру 019-293. | 4А |  |

#### ШАГ 2B. Проверьте сопротивление сигнализации запуска двигателя от пин-кодов до пин-кодов.

| **Условия:** Выключите замок зажигания. Отключите сигнализацию запуска двигателя от электропроводки двигателя. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте сопротивление от контакта А (или 1) до контакта В (или 2) разъема аварийной сигнализации двигателя. См. схему проводов или описание схемы в начале этого кода неисправности для идентификации контакта с разъемом. Для общих методов измерения сопротивления, обратитесь к измерениям сопротивления с использованием мультиметра и схемы проводов, процедуры[[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Более 800 и менее 1200 Ом | 3А |
| Замените сигнализацию запуска двигателя. См. процедуру 019-293. | 4А |  |

### ШАГ 3. Проверьте жгут электропроводки двигателя.

#### ШАГ 3A. Проверьте жгут проводов двигателя и контакты разъема сигнализации двигателя.

| **Условия:** Выключите замок зажигания. Отключите сигнализацию запуска двигателя от электропроводки двигателя. Отсоедините разъем электропроводки привода от двигателя ECM. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Корродированные штифты Бент или сломанные штифты Отталкивание назад или расширенные штифты Проводная изоляция Повреждение Влажность в или на разъем Пропавшие или поврежденные соединительные штифты Коннекторная оболочка разбитая Грязь или мусор в или на разъемных контактах. Для общих методов проверки обратитесь к компонентному коннектору и Pin-инспекции, процедура[[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | Никаких поврежденных контактов | 3B |
| Ремонт или замена ремня электропроводки двигателя. См. процедуру 019-043 в руководстве по устранению и устранению неполадок, CELECT Plus Engines, Bulletin 3666084 или процедуру 019-043 в руководстве по устранению и устранению неполадок, электронную систему управления, ISM, в руководстве по устранению и устранению неполадок, или процедуру 019-031 в руководстве по устранению и устранению неполадок, электронную систему управления, систему 3666259 или процедуру 019-043 в руководстве по устранению и устранению неполадок, электронную систему управления, CM870 ISM, в руководстве по устранению и устранению неполадок или процедуру 019-043 в руководстве по устранению и устранению неполадок, в руководстве по электронной системе управления, в руководстве по устранению и устранению неполадок, в руководстве по электронной системе управления, в руководстве по устранению и устранению неполадок, в руководстве по электронной системе управления, в руководстве по устранению и устран Ремонт или замена сигнализации запуска двигателя. См. процедуру 019-293. | 4А |  |

#### ШАГ 3B. Проверьте короткое замыкание на напряжение батареи.

| **Условия:** Отключите сигнализацию запуска двигателя от электропроводки двигателя. Отсоедините разъем электропроводки привода от двигателя ECM. Включите зажигание. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте напряжение от контакта 25 проводов привода разъема жгута с заземлением блока двигателя. Для методов использования мультиметра, обратитесь к использованию мультиметра, процедура[[99-019-359 — Multimeter Usage\|019-359]]. | Менее положительного (+) 1,5 VDC | 3В-1-1 |
| Ремонт или замена ремня электропроводки двигателя. См. процедуру 019-043 в руководстве по устранению и устранению неполадок, CELECT Plus Engines, Bulletin 3666084 или процедуру 019-043 в руководстве по устранению и устранению неполадок, электронную систему управления, ISM, в руководстве по устранению и устранению неполадок, или процедуру 019-031 в руководстве по устранению и устранению неполадок, электронную систему управления, систему 3666259 или процедуру 019-043 в руководстве по устранению и устранению неполадок, электронную систему управления, CM870 ISM, в руководстве по устранению и устранению неполадок или процедуру 019-043 в руководстве по устранению и устранению неполадок, в руководстве по электронной системе управления, в руководстве по устранению и устранению неполадок, в руководстве по электронной системе управления, в руководстве по устранению и устранению неполадок, в руководстве по электронной системе управления, в руководстве по устранению и устран | 4А |  |

#### ШАГ 3B-1. Проверьте короткое замыкание на напряжение батареи в OEM-проводах.

| **Условия: **Отключите 31-контактный OEM-разъем. Отключите сигнализацию запуска двигателя от электропроводки двигателя. Включите зажигание. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте напряжение от контакта 29 31-контактного OEM-разъема, OEM-проводов с ремнями безопасности, до заземления блока двигателя. Для методов использования мультиметра, обратитесь к использованию мультиметра, процедура[[99-019-359 — Multimeter Usage\|019-359]]. | Менее положительного (+) 1,5 VDC | 4А |
| не соответствует спецификациям. Ремонт или замена OEM проводов жгута. См. сервисное руководство изготовителя машины. | 4А |  |

### ШАГ 4. Сбросьте коды неисправностей.

#### ШАГ 4A. Отключите код неисправности.

| **Условия: **Соединить все компоненты. Включите зажигание. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Убедитесь, что код 588 неактивен с помощью инструментария электронного обслуживания INSITETM. Проведите тест сигнализации с помощью электронного инструментария INSITETM. Стирайте неактивные коды неисправностей с помощью инструментария электронного обслуживания INSITETM. | Код ошибки 588 неактивен | Ремонт завершён |
| Вернитесь к шагам устранения неполадок или свяжитесь с местным авторизованным ремонтным центром Cummins, если все шаги были завершены и перепроверены. Устранение неполадок с оставшимися активными кодами неисправностей. | Соответствующие диаграммы устранения неполадок |  |


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 588 (Integrated)
>
> ### Autostart Alarm Circuit - Voltage Above Normal or Shorted to High Source
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 588 PID(P): S121 SPN: 611 FMI: 3/3 Lamp: Yellow SRT: | Autostart Alarm Circuit - Voltage Above Normal or Shorted to High Source. High voltage detected at the alarm circuit when low voltage was expected by the engine electronic control module (ECM). | The ICON™ system will be disabled. **Only** mandatory shutdown will be enabled. Engine can be started normally. |
>
> ### Circuit Description
>
> The alarm circuit turns on the audible alarm to warn of an impending engine start.
>
> ### Component Location
>
> The ICON™ alarm is mounted on the vehicle's fire wall on the intake side of the engine.
>
> ### Shoptalk
>
> This fault typically indicates short circuit to battery or an open circuit. The fan 2 clutch feature is **not** used on ISM. ICON™ engine brake harness is required for Signature/ISX. **Only** 3-position engine brake switch is available for Signature/ISX with ICON™ installed.
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
> | STEP 1. | Read all fault codes. |  |
> |  | **STEP 1A.** Read the fault codes with INSITE™ electronic service tool or flash out with the ICON™ lamp. | Fault Code 588 inactive |
> |  | **STEP 1B.** Perform the ICON™ alarm test. | Alarm sounds |
> | STEP 2. | Check the engine start alarm. |  |
> |  | **STEP 2A.** Inspect the engine start alarm connector for damaged pins. | No damaged pins |
> |  | **STEP 2B.** Check the engine start alarm resistance from pin to pin. | More than 800 and less than 1200 ohms |
> | STEP 3. | Check the engine wiring harness. |  |
> |  | **STEP 3A.** Inspect the engine wiring harness and the engine start alarm connector pins. | No damaged pins |
> |  | **STEP 3B.** Check for a short circuit to battery voltage. | Less than positive (+) 1.5 VDC |
> |  | **STEP 3B-1.** Check for a short circuit to battery voltage in the OEM harness. | Less than positive (+) 1.5 VDC |
> | STEP 4. | Clear the fault codes. |  |
> |  | **STEP 4A.** Disable the fault code. | Fault Code 588 inactive |
>
> ### STEP 1. Read all fault codes.
>
> #### STEP 1A. Read the fault codes with INSITE™ electronic service tool or flash out with the ICON™ lamp.
>
> | **Conditions:** Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> |  | Fault Code 588 inactive | 1B |
> | Fault Code 588 active | 1B |  |
>
> #### STEP 1B. Perform the ICON™ alarm test.
>
> | **Conditions:** Connect the INSITE™ electronic service tool to the engine. Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Use INSITE™ to perform the ICON™ alarm test. | Alarm sounds | 4A |
> | Alarm does **not** sound | 2A |  |
>
> ### STEP 2. Check the engine start alarm.
>
> #### STEP 2A. Inspect the engine start alarm connector for damaged pins.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine start alarm from the engine harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Corroded pins Bent or broken pins Pushed back or expanded pins Wire insulation damage Moisture in or on the connector Missing or damaged connector seals Connector shell broken Dirt or debris in or on the connector pins. For general inspection techniques, refer to Component Connector and Pin Inspection, Procedure [[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | No damaged pins | 2B |
> | Repair or replace the damaged pins. Flush the dirt, debris, and moisture from the connector pins using electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair the engine start alarm connector. Refer to Procedure 019-202 or 019-206. Replace the engine start alarm. Refer to Procedure 019-293. | 4A |  |
>
> #### STEP 2B. Check the engine start alarm resistance from pin to pin.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine start alarm from the engine harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from pin A (or 1) to pin B (or 2) of the engine start alarm connector. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | More than 800 and less than 1200 ohms | 3A |
> | Replace the engine start alarm. Refer to Procedure 019-293. | 4A |  |
>
> ### STEP 3. Check the engine wiring harness.
>
> #### STEP 3A. Inspect the engine wiring harness and the engine start alarm connector pins.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the engine start alarm from the engine harness. Disconnect the actuator harness connector from the engine ECM. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Corroded pins Bent or broken pins Pushed back or expanded pins Wire insulation damage Moisture in or on the connector Missing or damaged connector seals Connector shell broken Dirt or debris in or on the connector pins. For general inspection techniques, refer to Component Connector and Pin Inspection, Procedure [[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | No damaged pins | 3B |
> | Repair or replace the engine harness. Refer to Procedure 019-043 in Troubleshooting and Repair Manual, CELECT Plus Engines, Bulletin 3666084, or Procedure 019-043 in Troubleshooting and Repair Manual, Electronic Control System, ISM, Bulletin [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual\|3666266]], or Procedure 019-031 in Troubleshooting and Repair Manual, Electronic Control System, Signature and ISX, Bulletin 3666259, or Procedure 019-043 in Troubleshooting and Repair Manual, Electronic Control System, CM870 ISM, Bulletin 4021381, or Procedure 019-043 in Troubleshooting and Repair Manual, Electronic Control System, CM870 Signature and ISX, Bulletin 4021334, or Procedure 019-043 in Troubleshooting and Repair Manual, Electronic Control System, CM875 ISM, Bulletin 4021477. Repair or replace the engine start alarm. Refer to Procedure 019-293. | 4A |  |
>
> #### STEP 3B. Check for a short circuit to battery voltage.
>
> | **Conditions:** Disconnect the engine start alarm from the engine harness. Disconnect the actuator harness connector from the engine ECM. Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the voltage from pin 25 of the actuator harness connector to engine block ground. For multimeter usage techniques, refer to Multimeter Usage, Procedure [[99-019-359 — Multimeter Usage\|019-359]]. | Less than positive (+) 1.5 VDC | 3B-1 |
> | Repair or replace the engine harness. Refer to Procedure 019-043 in Troubleshooting and Repair Manual, CELECT Plus Engines, Bulletin 3666084, or Procedure 019-043 in Troubleshooting and Repair Manual, Electronic Control System, ISM, Bulletin [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual\|3666266]], or Procedure 019-031 in Troubleshooting and Repair Manual, Electronic Control System, Signature and ISX, Bulletin 3666259, or Procedure 019-043 in Troubleshooting and Repair Manual, Electronic Control System, CM870 ISM, Bulletin 4021381, or Procedure 019-043 in Troubleshooting and Repair Manual, Electronic Control System, CM870 Signature and ISX, Bulletin 4021334, or Procedure 019-043 in Troubleshooting and Repair Manual, Electronic Control System, CM875 ISM, Bulletin 4021477. | 4A |  |
>
> #### STEP 3B-1. Check for a short circuit to battery voltage in the OEM harness.
>
> | **Conditions:** Disconnect the 31-pin OEM connector. Disconnect the engine start alarm from the engine harness. Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the voltage from pin 29 of the 31-pin OEM connector, OEM harness side, to engine block ground. For multimeter usage techniques, refer to Multimeter Usage, Procedure [[99-019-359 — Multimeter Usage\|019-359]]. | Less than positive (+) 1.5 VDC | 4A |
> | Does **not** meet specifications. Repair or replace the OEM harness. Refer to the OEM service manual. | 4A |  |
>
> ### STEP 4. Clear the fault codes.
>
> #### STEP 4A. Disable the fault code.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Verify that Fault Code 588 is inactive using INSITE™ electronic service tool. Perform alarm test with INSITE™ electronic service tool. Erase the inactive fault codes using INSITE™ electronic service tool. | Fault Code 588 inactive | Repair complete |
> | Return to the troubleshooting steps, or contact the local Cummins Authorized Repair Location if all the steps have been completed and rechecked. Troubleshoot any remaining active fault codes. | Appropriate troubleshooting charts |  |
