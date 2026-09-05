---
type: "Процедура"
doc: "97-fc199int"
title_en: "ICON™ Lamp Circuit - Voltage Below Normal or Shorted to Low Source"
modified: "2004-10-04"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-fc199int.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-fc199int.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "двигатель/QSX15"
  - "группа/97"
  - "перевод/машинный"
---

# ICON™ Lamp Circuit - Voltage Below Normal or Shorted to Low Source

> [!abstract] Процедура · `97-fc199int`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSM11, QSX15
> **Входит в руководства:** [[3666415 — ICON Idle Control System Master Repair Manual|3666415]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2004-10-04
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-fc199int.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-fc199int.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


### Код неисправности: 199 (интегрированный)

### ICONTM Lamp Circuit - напряжение ниже нормального или короткое до низкого источника

Версия для печати

### Обзор

| Коды | Причина | Последствия |
|---|---|---|
| Код неисправности: 199 PID(P): S122, 4 SPN: 612 FMI: 4 лампы: Желтая СТО: | ICONTM Lamp Circuit - напряжение ниже нормального или короткое до низкого источника. Менее 6 VDC (низкое напряжение) обнаружено на ламповой цепи ICONTM, когда высокое напряжение ожидал электронный модуль управления двигателем (ECM). | не позволит активировать ICONTM, однако, если ICONTM активирован и код ошибки 199 активируется, ICONTM будет отключен. |

![[19803214.png]]

### Описание цепи

Схема лампы ICONTM освещает лампу ICONTM, чтобы указать, когда система ICONTM активна. Кроме того, на этой лампе будут высвечиваться активные коды неисправностей ICONTM. Схема лампы требует определенного времени вспышки (включения или выключения). Если напряжение включено или выключено неправильно, система ICONTM будет отключена. Схема лампы должна быть функциональной для включения системы ICONTM.

### Расположение компонента

Лампа ICONTM расположена в кабине автомобиля на приборной панели.

### Практические замечания

Этот дефект указывает на короткое замыкание на землю или открытую цепь.

## Предупреждения и меры предосторожности

> [!warning] ОСТОРОЖНО
>

**Для уменьшения возможности повреждения штифта и проводов жгута проводов используйте при проведении измерений следующий испытательный щуп: Номер детали 3822917 - пробный щуп типа гнезда Deutsch/AMP/Metri-Pack Номер детали 3822758 - пробный щуп типа пробки Deutsch/AMP/Metri-Pack.**

## Сводка по поиску неисправности

| Степс | Спецификации |  |
|---|---|---|
| ШАГ 1. | Прочитайте все коды ошибок. |  |
|  | **ШАГ 1А.** Прочитайте коды неисправностей с помощью инструментария электронного обслуживания INSITETM или выключите лампу двигателя для активного кода неисправности. | Код ошибки 199 неактивен |
| ШАГ 2. | Проверьте лампу ICONTM. |  |
|  | **ШАГ 2А.** Проверить лампочку на предмет непрерывности. | Менее 35 Ом |
|  | **ШАГ 2В.** Проверить на напряжение лампы ИКОНТМ. | Более 6 VDC |
| ШАГ 3. | Проверьте предохранитель. |  |
|  | **ШАГ 3А.** Проверьте 5-амперный предохранитель зажигания. | предохранитель установлен правильно |
|  | **ШАГ 3В.** Проверьте, не взорван ли 5-амперный предохранитель. | предохранитель не взорван |
| ШАГ 4. | Проверьте разъемы кабины OEM на брандмауэре и разъем ECM для OEM-модуля. |  |
|  | **STEP 4A.** Проверить электропроводку OEM-устройства на наличие поврежденных контактов. | Никаких поврежденных контактов |
| ШАГ 5. | Проверьте схему лампы ICONTM на открытое или короткое замыкание. |  |
|  | **STEP 5A.** Проверьте лампу ICONTM на наличие открытой цепи. | Менее 10 Ом |
|  | **СТЭП 5В.** Проверить короткое замыкание. | Более 100 тыс. ом |
|  | **STEP 5C.** Проверьте короткое замыкание от пин-кодов до пин-кодов. | Более 100 тыс. ом |
| ШАГ 6. | Очистите код ошибки. |  |
|  | **STEP 6A.** Отключить код ошибки. | Код ошибки 199 неактивен |

### ШАГ 1. Прочитайте все коды ошибок.

#### ШАГ 1A. Прочитайте коды неисправностей с помощью электронного инструментария обслуживания INSITETM или выключите лампу двигателя для активного кода неисправности.

| **Условия:** Включить переключатель зажигания. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Прочитайте коды неисправностей с помощью инструментария электронного обслуживания INSITETM или выключите лампу двигателя для активных кодов неисправностей. | Код ошибки 199 неактивен | 6А |
| Код ошибки 199 активный | 2А |  |

### ШАГ 2. Проверьте лампу ICONTM.

#### ШАГ 2A. Проверьте лампу на предмет непрерывности.

| **Условия:** Выключите замок зажигания. Удалите лампу из держателя. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Используйте мультиметр для проверки сопротивления лампы. Для общих методов измерения сопротивления, обратитесь к измерениям сопротивления с использованием мультиметра и схемы проводов, процедуры[[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Менее 35 Ом | 2В |
| Замените лампу на 12-VDC с лампой 1892 General Electric или эквивалентом. | 6А |  |

#### ШАГ 2B. Проверьте напряжение на лампе ICONTM.

| **Условия:** Удалить лампочку из держателя. Включите зажигание. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Используйте мультиметр для измерения напряжения на стороне переключателя зажигания держателя лампы (сторона питания) на землю шасси. Для методов использования мультиметра, обратитесь к использованию мультиметра, процедура[[99-019-359 — Multimeter Usage\|019-359]]. | Более 6 VDC | 4А |
| Менее 6 VDC | 3А |  |

### ШАГ 3. Проверьте предохранитель.

#### ШАГ 3A. Проверьте 5-амперный предохранитель зажигания.

| **Условия:** Выключите замок зажигания. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| См. процедуру[[99-019-198 — Fuse, Harness In-Line\|019-198]]. | предохранитель установлен правильно | 3B |
| Установите предохранитель правильно. См. процедуру[[99-019-198 — Fuse, Harness In-Line\|019-198]]. | 6А |  |

#### ШАГ 3B. Проверьте, не взорван ли 5-амперный предохранитель.

| **Условия:** Выключите замок зажигания. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| См. процедуру[[99-019-198 — Fuse, Harness In-Line\|019-198]]. | предохранитель не взорван | 4А |
| Замените выдувной предохранитель. См. процедуру[[99-019-198 — Fuse, Harness In-Line\|019-198]]. | 6А |  |

### ШАГ 4. Проверьте разъемы кабины OEM на противопожарной стене и разъем ECM для OEM-модуля.

#### ШАГ 4A. Проверьте электропроводку OEM для поврежденных контактов.

| **Условия:** Выключите замок зажигания. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Корродированные штифты Бент или сломанные штифты Отталкивание назад или расширенные штифты Проводная изоляция Повреждение Влажность в или на разъем Пропавшие или поврежденные соединительные штифты Коннекторная оболочка разбитая Грязь или мусор в или на разъемных контактах. Для общих методов проверки обратитесь к компонентному коннектору и Pin-инспекции, процедура[[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | Никаких поврежденных контактов | 5а |
| Ремонт или замена OEM проводов жгута. См. сервисное руководство изготовителя машины. | 6А |  |

### ШАГ 5. Проверьте схему лампы ICONTM на открытое или короткое замыкание.

#### ШАГ 5A. Проверьте лампу ICONTM на наличие открытой цепи.

| **Условия:** Выключите замок зажигания. Отсоедините разъем OEM-проводов от двигателя ECM. Удалите лампу ICONTM из держателя лампы. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерить сопротивление от контакта 4 разъёма проводов OEM на двигателе ECM к обратной стороне (сбоку двигателя ECM) держателя лампы ICONTM. См. схему проводов или описание схемы в начале этого кода неисправности для идентификации контакта с разъемом. Для общих методов измерения сопротивления, обратитесь к измерениям сопротивления с использованием мультиметра и схемы проводов, процедуры[[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Менее 10 Ом | 5В |
| Ремонт или замена OEM проводов жгута. См. сервисное руководство изготовителя машины. | 6А |  |

#### ШАГ 5B. Проверьте цепь на короткое замыкание.

| **Условия:** Выключите замок зажигания. Отсоедините разъем OEM-проводов от двигателя ECM. Удалите лампу ICONTM из держателя лампы. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерить сопротивление от контакта 4 проводов OEM-разъема упряжки при двигателе ECM к земле. См. схему проводов или описание схемы в начале этого кода неисправности для идентификации контакта с разъемом. Для общих методов измерения сопротивления, обратитесь к измерениям сопротивления с использованием мультиметра и схемы проводов, процедуры[[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Более 100 тыс. ом | 5С |
| Ремонт или замена OEM проводов жгута. См. сервисное руководство изготовителя машины. | 6А |  |

#### ШАГ 5C. Проверьте короткое замыкание от пин-кодов до пин-кодов.

| **Условия:** Выключите замок зажигания. Отсоедините разъем OEM-проводов от двигателя ECM. Удалите лампу ICONTM из держателя лампы. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Измерьте сопротивление от контакта 4 разъёма OEM-проводов на ЭКМ двигателя ко всем другим штифтам в разъеме. См. схему проводов или описание схемы в начале этого кода неисправности для идентификации контакта с разъемом. Для общих методов измерения сопротивления, обратитесь к измерениям сопротивления с использованием мультиметра и схемы проводов, процедуры[[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Более 100 тыс. ом | 6А |
| Ремонт или замена OEM проводов жгута. См. сервисное руководство изготовителя машины. | 6А |  |

### ШАГ 6. Очистите код ошибки.

#### ШАГ 6A. Отключите код неисправности.

| **Условия: **Соединить все компоненты. Включите зажигание. |  |  |
|---|---|---|
| **Действие** | **Спецификация/ремонт** | **Следующий шаг** |
| Убедитесь, что код 199 неактивен. Стирать неактивные коды неисправностей с помощью INSITETM. | Код ошибки 199 неактивен | Ремонт завершён |
| Вернитесь к шагам устранения неполадок или свяжитесь с ближайшим авторизованным ремонтным центром Cummins, если все шаги были завершены и перепроверены. Устранение неполадок с оставшимися активными кодами неисправностей. | Соответствующие диаграммы устранения неполадок |  |


> [!quote]- Original (English) · английский оригинал
> ### Fault Code: 199 (Integrated)
>
> ### ICON™ Lamp Circuit - Voltage Below Normal or Shorted to Low Source
>
> Printable Version
>
> ### Overview
>
> | Codes | Reason | Effect |
> |---|---|---|
> | Fault Code: 199 PID(P): S122, 4 SPN: 612 FMI: 4 Lamp: Yellow SRT: | ICON™ Lamp Circuit - Voltage Below Normal or Shorted to Low Source. Less than 6 VDC (low voltage) detected at the ICON™ lamp circuit when high voltage was expected by the engine electronic control module (ECM). | Will **not** allow ICON™ to activate, however if ICON™ is engaged and fault code 199 becomes active, ICON™ will **not** be disabled. |
>
> ### Circuit Description
>
> The ICON™ lamp circuit illuminates the ICON™ lamp to indicate when the ICON™ system is active. In addition, ICON™ active fault codes will be flashed out on this lamp. The lamp circuit requires a specific flash timing (on or off timing). If the on or off voltage is incorrect, the ICON™ system will be disabled. The lamp circuit **must** be functional to enable the ICON™ system.
>
> ### Component Location
>
> The ICON™ lamp is located in the vehicle cab on the dash panel.
>
> ### Shoptalk
>
> This fault indicates a short circuit to ground or an open circuit.
>
> ## Warnings and Cautions
>
> **CAUTION · Осторожно**
>
> **To reduce the possibility of pin and harness damage, use the following test leads when taking a measurement: Part Number 3822917 - female Deutsch/AMP/Metri-Pack test lead Part Number 3822758 - male Deutsch/AMP/Metri-Pack test lead.**
>
> ## Troubleshooting Summary
>
> | STEPS | SPECIFICATIONS |  |
> |---|---|---|
> | STEP 1. | Read all fault codes. |  |
> |  | **STEP 1A.** Read the fault codes with INSITE™ electronic service tool, or flash out engine lamp for active fault code. | Fault Code 199 inactive |
> | STEP 2. | Check the ICON™ lamp. |  |
> |  | **STEP 2A.** Check the bulb for continuity. | Less than 35 ohms |
> |  | **STEP 2B.** Check for voltage to the ICON™ lamp. | More than 6 VDC |
> | STEP 3. | Check the fuse. |  |
> |  | **STEP 3A.** Check the 5-amp ignition fuse. | Fuse installed correctly |
> |  | **STEP 3B.** Check if the 5-amp fuse is blown. | Fuse not blown |
> | STEP 4. | Check the OEM cab harness connectors at the firewall and the OEM harness engine ECM connector. |  |
> |  | **STEP 4A.** Inspect the OEM harness for damaged pins. | No damaged pins |
> | STEP 5. | Check the ICON™ lamp circuit for an open or short circuit. |  |
> |  | **STEP 5A.** Check the ICON™ lamp for an open circuit. | Less than 10 ohms |
> |  | **STEP 5B.** Check for a short circuit. | More than 100k ohms |
> |  | **STEP 5C.** Check for a short circuit from pin to pin. | More than 100k ohms |
> | STEP 6. | Clear the fault code. |  |
> |  | **STEP 6A.** Disable the fault code. | Fault Code 199 inactive |
>
> ### STEP 1. Read all fault codes.
>
> #### STEP 1A. Read the fault codes with INSITE™ electronic service tool, or flash out engine lamp for active fault code.
>
> | **Conditions:** Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Read the fault codes using INSITE™ electronic service tool, or flash out engine lamp for active fault codes. | Fault Code 199 inactive | 6A |
> | Fault Code 199 active | 2A |  |
>
> ### STEP 2. Check the ICON™ lamp.
>
> #### STEP 2A. Check the bulb for continuity.
>
> | **Conditions:** Turn keyswitch OFF. Remove the bulb from the holder. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Use a multimeter to check the resistance of the bulb. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Less than 35 ohms | 2B |
> | Replace the bulb for a 12-VDC system with a General Electric 1892 bulb or equivalent. | 6A |  |
>
> #### STEP 2B. Check for voltage to the ICON™ lamp.
>
> | **Conditions:** Remove the bulb from the holder. Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Use a multimeter to measure the voltage at the lamp bulb holder keyswitch side (power side) to chassis ground. For multimeter usage techniques, refer to Multimeter Usage, Procedure [[99-019-359 — Multimeter Usage\|019-359]]. | More than 6 VDC | 4A |
> | Less than 6 VDC | 3A |  |
>
> ### STEP 3. Check the fuse.
>
> #### STEP 3A. Check the 5-amp ignition fuse.
>
> | **Conditions:** Turn keyswitch OFF. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Refer to Procedure [[99-019-198 — Fuse, Harness In-Line\|019-198]]. | Fuse installed correctly | 3B |
> | Install fuse correctly. Refer to Procedure [[99-019-198 — Fuse, Harness In-Line\|019-198]]. | 6A |  |
>
> #### STEP 3B. Check if the 5-amp fuse is blown.
>
> | **Conditions:** Turn keyswitch OFF. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Refer to Procedure [[99-019-198 — Fuse, Harness In-Line\|019-198]]. | Fuse not blown | 4A |
> | Replace the blown fuse. Refer to Procedure [[99-019-198 — Fuse, Harness In-Line\|019-198]]. | 6A |  |
>
> ### STEP 4. Check the OEM cab harness connectors at the fire wall and the OEM harness engine ECM connector.
>
> #### STEP 4A. Inspect the OEM harness for damaged pins.
>
> | **Conditions:** Turn keyswitch OFF. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Corroded pins Bent or broken pins Pushed back or expanded pins Wire insulation damage Moisture in or on the connector Missing or damaged connector seals Connector shell broken Dirt or debris in or on the connector pins. For general inspection techniques, refer to Component Connector and Pin Inspection, Procedure [[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | No damaged pins | 5A |
> | Repair or replace the OEM harness. Refer to the OEM service manual. | 6A |  |
>
> ### STEP 5. Check the ICON™ lamp circuit for an open or short circuit.
>
> #### STEP 5A. Check the ICON™ lamp for an open circuit.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness connector from the engine ECM. Remove the ICON™ lamp bulb from the bulb holder. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from pin 4 of the OEM harness connector at the engine ECM to the return side (engine ECM side) of the ICON™ lamp bulb holder. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Less than 10 ohms | 5B |
> | Repair or replace the OEM harness. Refer to the OEM service manual. | 6A |  |
>
> #### STEP 5B. Check for a short circuit.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness connector from the engine ECM. Remove the ICON™ lamp bulb from the bulb holder. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from pin 4 of the OEM harness connector at the engine ECM to ground. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | More than 100k ohms | 5C |
> | Repair or replace the OEM harness. Refer to the OEM service manual. | 6A |  |
>
> #### STEP 5C. Check for a short circuit from pin to pin.
>
> | **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness connector from the engine ECM. Remove the ICON™ lamp bulb from the bulb holder. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Measure the resistance from pin 4 of the OEM harness connector at the engine ECM to all other pins in the connector. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | More than 100k ohms | 6A |
> | Repair or replace the OEM harness. Refer to the OEM service manual. | 6A |  |
>
> ### STEP 6. Clear the fault code.
>
> #### STEP 6A. Disable the fault code.
>
> | **Conditions:** Connect all components. Turn keyswitch ON. |  |  |
> |---|---|---|
> | **Action** | **Specification/Repair** | **Next Step** |
> | Verify that Fault Code 199 is inactive. Erase the inactive fault codes using INSITE™. | Fault Code 199 inactive | Repair complete |
> | Return to the troubleshooting steps, or contact the nearest Cummins Authorized Repair Location if all the steps have been completed and rechecked. Troubleshoot any remaining active fault codes. | Appropriate troubleshooting charts |  |
