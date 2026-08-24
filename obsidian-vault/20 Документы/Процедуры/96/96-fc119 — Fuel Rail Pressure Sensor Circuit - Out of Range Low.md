---
aliases:
  - "Цепь датчика давления рампы — ниже диапазона"
type: "Процедура"
doc: "96-fc119"
title_en: "Fuel Rail Pressure Sensor Circuit - Out of Range Low"
title_ru: "Цепь датчика давления рампы — ниже диапазона"
modified: "2004-02-25"
engines:
  - "37292556"
  - "37295879"
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
  - "QST30"
manuals:
  - "3666231"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/96/96-fc119.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/96-fc119.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "двигатель/QST30"
  - "группа/96"
  - "перевод/машинный"
---

# Fuel Rail Pressure Sensor Circuit - Out of Range Low
**Цепь датчика давления рампы — ниже диапазона**

> [!abstract] Процедура · `96-fc119`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]], [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11, QST30
> **Входит в руководства:** [[3666231 — Centinel™ Master Repair Manual|3666231]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2004-02-25
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/96/96-fc119.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/96-fc119.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 119

### Цепь датчика давления рампы — ниже диапазона

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 119 P(P): СПН: ФМИ: Лампа: Красная СТО: | Цепь датчика давления рампы — ниже диапазона. Давление на топливных рельсах низкое. | Система CentinelTM будет работать **не**. |

![[05800059.png]]

### Описание цепи

Датчик давления топливной рельсы контролирует давление топливной рельсы. Когда датчик выходит из строя высоко или низко, возникает неисправность датчика давления топливной рельсы.

### Расположение компонента

Датчик давления топливной рельсы расположен на блоке соединения топлива на кронштейне установки клапана управления маслом CentinelTM.

## Предупреждения и меры предосторожности

> [!warning] ОСТОРОЖНО
>

** Чтобы избежать повреждения штифта и проводов, используйте следующий испытательный щуп при проведении измерений: Штыревая пушка, Metri-Pack, Deutsch измерительный щуп, Часть Номер 3822758 Гнездовой AMP, Metri-Pack, Deutsch измерительный щуп, Часть Номер 3822917 Штыревой Deutsch измерительный щуп, Часть Номер 3823993 Гнездовой Deutsch измерительный щуп, Часть Номер 3823994.

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Проверьте датчик давления топливной рельсы. |  |
|  | **STEP 1A.** Осмотрите датчик давления в топливной рельсе и разъёмы проводной ремни CentinelTM. | Никаких поврежденных контактов |
|  | **STEP 1B.** Проверьте напряжение питания датчика давления рельсовой магистрали модуля управления CentinelTM. | 4,75-5,25 VDC |
|  | **STEP 1C** Проверьте датчик давления в топливной рельсе на наличие открытого отверстия. | Менее 2 м ом |
| ШАГ 2. | Проверьте проводную упряжку CentinelTM. |  |
|  | **STEP 2A.** Осмотрите жгут проводов CentinelTM и разъемы модуля управления CentinelTM. | Никаких поврежденных контактов |
|  | **ШАГ 2В.** Проверить наличие открытой цепи. | Менее 10 Ом |
|  | **ШАГ 2С.** Проверить короткое замыкание на землю. | Более 1к Ом |
|  | **STEP 2D.** Проверьте короткое замыкание от пин-кодов до пин-кодов. | Более 1к Ом |
| ШАГ 3. | Сбросьте коды неисправностей. |  |
|  | **STEP 3A.** Отключить код ошибки. | Код ошибки 119 неактивен |

### ШАГ 1. Проверьте датчик давления топливной рельсы.

#### ШАГ 1A. Проверьте датчик давления топливной рельсы и разъём проводов CentinelTM.

| **Условия:** Выключите замок зажигания. Отсоедините проводную упряжку CentinelTM от датчика давления топливной рельсы. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разъема разъема разъема разъема разъема или разъема разъема разъема или разъема разъема разъема или на разъеме разъема повреждения изоляции Проволоки Разъемная оболочка разорвана Поврежденная блокировка вкладки разъема. Для общих методов проверки обратитесь к компонентному коннектору и Pin-инспекции, процедура[[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | Никаких поврежденных контактов | 1В |
| ** Поврежденные контакты** Починить или заменить проводную упряжку CentinelTM или датчик давления в топливной рельсе, в зависимости от того, какие контакты повреждены. Ремонт проводной упряжки CentinelTM. См. процедуру 019-202. Замените проводную упряжку CentinelTM. См. процедуру 019-131. Замените датчик давления в топливной рельсе. См. процедуру 019-115. Установите соответствующий уплотнитель разъема, если он поврежден или отсутствует. | 3А |  |

#### ШАГ 1B. Проверьте модуль управления CentinelTM датчик давления топлива на подаче напряжения.

| **Условия:** Включить переключатель зажигания. Отсоедините датчик давления топливной рельсы от проводной ремни CentinelTM. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Измерьте напряжение питания от контакта А до контакта В на стороне проводов ремня давления топливной рельсы. См. схему проводов для идентификации контакта с разъемом. | 4,75-5,25 VDC | 1С |
| **Заменить электропроводку ремня управления или модуля управления CentinelTM** См. процедуру[[96-019-130-tr — Centinel™ Control Module\|019-130]]. | 3А |  |

#### ШАГ 1C. Проверьте датчик давления топливной рельсы на наличие открытого.

| **Условия:** Выключите замок зажигания. Отсоедините датчик давления топливной рельсы от проводной ремни CentinelTM. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Измерить сопротивление от контакта В до контакта С датчика давления топливной рельсы. См. схему проводов для идентификации контакта с разъемом. Для общих методов измерения сопротивления, обратитесь к измерениям сопротивления с использованием мультиметра и схемы проводов, процедуры[[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Менее 2 м ом | 2А |
| ** Заменить датчик давления в топливной рельсе** См. процедуру[[96-019-115 — Rail Fuel Pressure Sensor\|019-115]]. | 3А |  |

### ШАГ 2. Проверьте проводную упряжку CentinelTM.

#### ШАГ 2A. Осмотрите проводную упряжку CentinelTM и разъёмы модуля управления CentinelTM.

| **Условия:** Выключите замок зажигания. Отсоедините проводную упряжку CentinelTM от модуля управления CentinelTM. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема Разъем разъема разъема или разъема разъема разъема разъема разъема или разъема разъема разъема или разъема разъема разъема или на разъеме разъема повреждения изоляции Проволоки Разъемная оболочка разорвана Поврежденная блокировка вкладки разъема. Для общих методов проверки обратитесь к компонентному коннектору и Pin-инспекции, процедура[[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | Никаких поврежденных контактов | 2В |
| ** Починить поврежденные контакты** Починить или заменить проводную упряжку CentinelTM или модуль управления CentinelTM, в зависимости от того, какие контакты повреждены. Ремонт проводной упряжки CentinelTM. См. процедуру 019-202. Замените проводную упряжку CentinelTM. См. процедуру 019-131. Заменить модуль управления CentinelTM. См. процедуру 019-130. | 3А |  |

#### ШАГ 2B. Проверьте цепь на обрыв.

| **Условия:** Выключите замок зажигания. Отсоедините датчик давления топливной рельсы от проводной ремни CentinelTM. Отсоедините проводную упряжку CentinelTM от модуля управления CentinelTM. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Измерьте сопротивление от контакта 11 разъёма проводной ремни CentinelTM, чтобы связаться с датчиком давления топливной рельсы, стороной проводной ремни. Измерить сопротивление от контакта 27 проводов разъема упряжки CentinelTM до контакта В датчика давления рельса топлива, проводов упряжки борта. Измерить сопротивление от контакта 14 проводов разъема упряжки CentinelTM до контакта C датчика давления топливной рельсы, проводов упряжки борта. См. схему проводов для идентификации контакта с разъемом. Для общих методов измерения сопротивления, обратитесь к измерениям сопротивления с использованием мультиметра и схемы проводов, процедуры[[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Менее 10 Ом | 2C |
| ** Починить или заменить проводную упряжку CentinelTM** Заменить проводную упряжку CentinelTM. См. процедуру[[96-019-131-tr — Centinel™ Wiring Harness\|019-131]]. | 3А |  |

#### ШАГ 2C. Проверьте короткое замыкание на землю.

| **Условия:** Выключите замок зажигания. Отсоедините датчик давления топливной рельсы от проводной ремни CentinelTM. Отсоедините проводную упряжку CentinelTM от модуля управления CentinelTM. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Измерьте сопротивление контактов 11 и 14 разъёма проводной ремни CentinelTM к заземлению блока двигателя. См. схему проводов для идентификации контакта с разъемом. Для общих методов измерения сопротивления, обратитесь к измерениям сопротивления с использованием мультиметра и схемы проводов, процедуры[[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Более 1к Ом | 2D |
| **Заменить проводную упряжку CentinelTM**См. процедуру[[96-019-131-tr — Centinel™ Wiring Harness\|019-131]]. | 3А |  |

#### ШАГ 2D. Проверьте короткое замыкание от пин-кодов до пин-кодов.

| **Условия:** Выключите замок зажигания. Отсоедините проводную упряжку CentinelTM от датчика давления топливной рельсы. Отсоедините проводную упряжку CentinelTM от модуля управления CentinelTM. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Измерьте сопротивление контактов 11, 14 и 27 разъёма проводов CentinelTM со всеми другими штифтами в разъеме. См. схему проводов для идентификации контакта с разъемом. Для общих методов измерения сопротивления, обратитесь к измерениям сопротивления с использованием мультиметра и схемы проводов, процедуры[[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Более 1к Ом | 3А |
| **Заменить проводную упряжку CentinelTM**См. процедуру[[96-019-131-tr — Centinel™ Wiring Harness\|019-131]]. | 3А |  |

### ШАГ 3. Сбросьте коды неисправностей.

#### ШАГ 3A. Отключите код неисправности.

| **Условия: ** Соедините все компоненты. Включите замок зажигания. |  |  |
|---|---|---|
| **Действие** | ** Спецификация/ремонт** | ** Следующий шаг** |
| Запустите двигатель и запускайте его на холостом ходу в течение 1 минуты. Убедитесь, что код 119 неактивен, проверив красный свет. | Код ошибки 119 неактивный/красный свет выключен | Полный комплект |
| Вернитесь к шагам устранения неполадок или свяжитесь с вашим местным авторизованным ремонтным центром Cummins, если все шаги были завершены и проверены снова. | 1А |  |


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 119
>
> ### Fuel Rail Pressure Sensor Circuit - Out of Range Low
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 119 PID(P): SPN: FMI: Lamp: Red SRT: | Fuel Rail Pressure Sensor Circuit - Out of Range Low. The fuel rail pressure is low. | The Centinel™ system will **not** function. |
>
> ### Circuit Description
>
> The fuel rail pressure sensor monitors the fuel rail pressure. When the sensor fails high or low, the fuel rail pressure sensor fault will occur.
>
> ### Component Location
>
> The fuel rail pressure sensor is located on the fuel connecting block on the Centinel™ oil control valve mounting bracket.
>
> ## Warnings and Cautions
>
> **CAUTION · Осторожно**
>
> **To avoid pin and harness damage, use the following test leads when taking measurements: Male Cannon, Metri-Pack, Deutsch test lead, Part Number 3822758 Female AMP, Metri-Pack, Deutsch test lead, Part Number 3822917 Male Deutsch test lead, Part Number 3823993 Female Deutsch test lead, Part Number 3823994.**
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Check the fuel rail pressure sensor. |  |
> |  | **STEP 1A.** Inspect the fuel rail pressure sensor and Centinel™ harness connectors. | No damaged pins |
> |  | **STEP 1B.** Check the Centinel™ control module fuel rail pressure sensor supply voltage. | 4.75 to 5.25 VDC |
> |  | **STEP 1C.** Check the fuel rail pressure sensor for an open. | Less than 2M ohms |
> | STEP 2. | Check the Centinel™ harness. |  |
> |  | **STEP 2A.** Inspect the Centinel™ harness and the Centinel™ control module connectors. | No damaged pins |
> |  | **STEP 2B.** Check for an open circuit. | Less than 10 ohms |
> |  | **STEP 2C.** Check for a short circuit to ground. | More than 1k ohms |
> |  | **STEP 2D.** Check for a short circuit from pin to pin. | More than 1k ohms |
> | STEP 3. | Clear the fault codes. |  |
> |  | **STEP 3A.** Disable the fault code. | Fault Code 119 inactive |
>
> ### STEP 1. Check the fuel rail pressure sensor.
>
> #### STEP 1A. Inspect the fuel rail pressure sensor and the Centinel™ harness connector.
>
> | **Conditions:** Turn the keyswitch OFF. Disconnect the Centinel™ harness from the fuel rail pressure sensor. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Wire insulation damage Connector shell broken Damaged locking tab connector. For general inspection techniques, refer to Component Connector and Pin Inspection, Procedure [[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | No damaged pins | 1B |
> | **Repair the damaged pins** Repair or replace the Centinel™ harness or the fuel rail pressure sensor, whichever has damaged pins. Repair the Centinel™ harness. Refer to Procedure 019-202. Replace the Centinel™ harness. Refer to Procedure 019-131. Replace the fuel rail pressure sensor. Refer to Procedure 019-115. Install the appropriate connector seal if damaged or missing. | 3A |  |
>
> #### STEP 1B. Check the Centinel™ control module fuel rail pressure sensor supply voltage.
>
> | **Conditions:** Turn the keyswitch ON. Disconnect the fuel rail pressure sensor from the Centinel™ harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the supply voltage from pin A to pin B on the harness side of the fuel rail pressure sensor. Refer to the wiring diagram for connector pin identification. | 4.75 to 5.25 VDC | 1C |
> | **Replace the harness or Centinel™ control module** Refer to Procedure [[96-019-130-tr — Centinel™ Control Module\|019-130]]. | 3A |  |
>
> #### STEP 1C. Check the fuel rail pressure sensor for an open.
>
> | **Conditions:** Turn the keyswitch OFF. Disconnect the fuel rail pressure sensor from the Centinel™ harness. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from pin B to pin C of the fuel rail pressure sensor connector. Refer to the wiring diagram for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Less than 2M ohms | 2A |
> | **Replace the fuel rail pressure sensor** Refer to Procedure [[96-019-115 — Rail Fuel Pressure Sensor\|019-115]]. | 3A |  |
>
> ### STEP 2. Check the Centinel™ harness.
>
> #### STEP 2A. Inspect the Centinel™ harness and Centinel™ control module connectors.
>
> | **Conditions:** Turn the keyswitch OFF. Disconnect the Centinel™ harness from the Centinel™ control module. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Wire insulation damage Connector shell broken Damaged locking tab connector. For general inspection techniques, refer to Component Connector and Pin Inspection, Procedure [[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | No damaged pins | 2B |
> | **Repair the damaged pins** Repair or replace the Centinel™ harness or the Centinel™ control module, whichever has the damaged pins. Repair the Centinel™ harness. Refer to Procedure 019-202. Replace the Centinel™ harness. Refer to Procedure 019-131. Replace the Centinel™ control module. Refer to Procedure 019-130. | 3A |  |
>
> #### STEP 2B. Check for an open circuit.
>
> | **Conditions:** Turn the keyswitch OFF. Disconnect the fuel rail pressure sensor from the Centinel™ harness. Disconnect the Centinel™ harness from the Centinel™ control module. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from pin 11 of the Centinel™ harness connector to pin A of the fuel rail pressure sensor, harness side. Measure the resistance from pin 27 of the Centinel™ harness connector to pin B of the fuel rail pressure sensor, harness side. Measure the resistance from pin 14 of the Centinel™ harness connector to pin C of the fuel rail pressure sensor, harness side. Refer to the wiring diagram for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Less than 10 ohms | 2C |
> | **Repair or replace the Centinel™ harness** Replace the Centinel™ harness. Refer to Procedure [[96-019-131-tr — Centinel™ Wiring Harness\|019-131]]. | 3A |  |
>
> #### STEP 2C. Check for a short circuit to ground.
>
> | **Conditions:** Turn the keyswitch OFF. Disconnect the fuel rail pressure sensor from the Centinel™ harness. Disconnect the Centinel™ harness from the Centinel™ control module. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from pins 11 and 14 of the Centinel™ harness connector to engine block ground. Refer to the wiring diagram for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | More than 1k ohms | 2D |
> | **Replace the Centinel™ wiring harness** Refer to Procedure [[96-019-131-tr — Centinel™ Wiring Harness\|019-131]]. | 3A |  |
>
> #### STEP 2D. Check for a short circuit from pin to pin.
>
> | **Conditions:** Turn the keyswitch OFF. Disconnect the Centinel™ harness from the fuel rail pressure sensor. Disconnect the Centinel™ harness from the Centinel™ control module. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from pins 11, 14, and 27 of the Centinel™ harness connector to all other pins in the connector. Refer to the wiring diagram for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | More than 1k ohms | 3A |
> | **Replace the Centinel™ wiring harness** Refer to Procedure [[96-019-131-tr — Centinel™ Wiring Harness\|019-131]]. | 3A |  |
>
> ### STEP 3. Clear the fault codes.
>
> #### STEP 3A. Disable the fault code.
>
> | **Conditions:** Connect all the components. Turn the keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Start the engine and let it idle for 1 minute. Verify that Fault Code 119 is inactive by checking the red light. | Fault Code 119 inactive/red light off | Complete |
> | Return to troubleshooting steps or contact your local Cummins Authorized Repair Location if all the steps have been completed and checked again. | 1A |  |
